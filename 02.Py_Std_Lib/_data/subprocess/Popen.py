import os
from subprocess import Popen, PIPE
from warnings import warn


def which(program):
    # Add .exe program extension for windows support
    if os.name == "nt" and not program.endswith(".exe"):
        program += ".exe"

    envdir_list = [os.curdir] + os.environ["PATH"].split(os.pathsep)

    for envdir in envdir_list:
        program_path = os.path.join(envdir, program)
        if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
            return program_path


def cmd():
    if which("cmd"):
        return "cmd"
    else:
        warn("cmd", RuntimeWarning)
        exit ()

def batch(filepath):

    prober = cmd()
    command_args = [
        "-v", "info",
        "-show_format",
        "-show_streams",
    ]
    try:
        command_args += [fsdecode(filepath)]
        stdin_parameter = None
        stdin_data = None
    except TypeError:
        command_args += ["-"]
        stdin_parameter = PIPE
        file = _fd_or_path_or_tempfile(filepath, 'rb', tempfile=False)
        file.seek(0)
        stdin_data = file.read()

    command = [prober, '-of', 'json'] + command_args
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
    output, stderr = res.communicate(input=stdin_data)
    output = output.decode("utf-8", 'ignore')
    stderr = stderr.decode("utf-8", 'ignore')

    info = json.loads(output)

    if not info:
        # If ffprobe didn't give any information, just return it
        # (for example, because the file doesn't exist)
        return info

    extra_info = get_extra_info(stderr)

    audio_streams = [x for x in info['streams'] if x['codec_type'] == 'audio']
    if len(audio_streams) == 0:
        return info

    # We just operate on the first audio stream in case there are more
    stream = audio_streams[0]

    def set_property(stream, prop, value):
        if prop not in stream or stream[prop] == 0:
            stream[prop] = value

    for token in extra_info[stream['index']]:
        m = re.match('([su]([0-9]{1,2})p?) \(([0-9]{1,2}) bit\)$', token)
        m2 = re.match('([su]([0-9]{1,2})p?)( \(default\))?$', token)
        if m:
            set_property(stream, 'sample_fmt', m.group(1))
            set_property(stream, 'bits_per_sample', int(m.group(2)))
            set_property(stream, 'bits_per_raw_sample', int(m.group(3)))
        elif m2:
            set_property(stream, 'sample_fmt', m2.group(1))
            set_property(stream, 'bits_per_sample', int(m2.group(2)))
            set_property(stream, 'bits_per_raw_sample', int(m2.group(2)))
        elif re.match('(flt)p?( \(default\))?$', token):
            set_property(stream, 'sample_fmt', token)
            set_property(stream, 'bits_per_sample', 32)
            set_property(stream, 'bits_per_raw_sample', 32)
        elif re.match('(dbl)p?( \(default\))?$', token):
            set_property(stream, 'sample_fmt', token)
            set_property(stream, 'bits_per_sample', 64)
            set_property(stream, 'bits_per_raw_sample', 64)
    return info

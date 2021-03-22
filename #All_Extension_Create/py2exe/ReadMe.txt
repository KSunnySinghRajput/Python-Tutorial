1.python -m venv py2exe
2.py2exe\Scripts\activate
3.python -m pip install --upgrade pip
4.pip install pyinstaller
	(py2exe) E:\#Programming\#Python\#Project\py2exe>pyinstaller
	usage: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--add-data <SRC;DEST or SRC:DEST>]
                   [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                   [--hidden-import MODULENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--key KEY] [-d {all,imports,bootloader,noarchive}] [-s]
                   [--noupx] [--upx-exclude FILE] [-c] [-w]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns>]
                   [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                   [--win-no-prefer-redirects]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--runtime-tmpdir PATH] [--bootloader-ignore-signals]
                   [--distpath DIR] [--workpath WORKPATH] [-y]
                   [--upx-dir UPX_DIR] [-a] [--clean] [--log-level LEVEL]
                   scriptname [scriptname ...]

5.pyinstaller file.py
6.pyinstaller -F file.py -i <FILE.ico>
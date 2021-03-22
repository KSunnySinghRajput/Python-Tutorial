#pip install configparser
import configparser
config = configparser.ConfigParser()
config.read("was-config.ini")
api = config.get("VIRUS-TOTAL", "api-key")
lang = config.get("NOTIFICATIONS", "lang")
audio = config.get("NOTIFICATIONS", "audio")
lock = config.get("FILE-LOCKING", "lock")
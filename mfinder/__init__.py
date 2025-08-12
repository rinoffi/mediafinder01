import os
import re
import logging
import logging.config
from dotenv import load_dotenv


load_dotenv()


id_pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "24160099")
API_HASH = os.environ.get("API_HASH", "381515f2540b0bf817a68af8b352f5b7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8012478742:AAEBtfyswWjw9onIUYGgmZGmWnAR7zIoBYQ")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://haribotx:haribotx@cluster0.i3skil4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(os.environ.get("OWNER_ID", "6248675084"))
ADMINS = [
    int(user) if id_pattern.search(user) else user
    for user in os.environ.get("ADMINS", "7189632039").split()
] + [OWNER_ID]
DB_CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in os.environ.get("DB_CHANNELS", "-1002730747385").split()
]

try:
    import const
except Exception:
    import sample_const as const

START_MSG = const.START_MSG
START_KB = const.START_KB
HELP_MSG = const.HELP_MSG
HELP_KB = const.HELP_KB


# logging Conf
logging.config.fileConfig(fname="config.ini", disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



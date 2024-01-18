from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20631366"))
API_HASH = getenv("API_HASH", "0542fb72defcdfcab59599238f13ba1c")

BOT_TOKEN = getenv("BOT_TOKEN", "5992301514:AAHck8oGq4i0uwuxxebZzy6fK5Gz_rN0euM")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ok:ok@cluster0.uooya.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))

OWNER_ID = int(getenv("OWNER_ID", "5021621064"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BABkb62UqrDuo4zTvpmOd_lSPevEoIqnn3nAT2UdrBMdtfH4jDjpyuWAFGPIyrKpbf2C4Goh72FEsauJ13e_iw1eLPk2gELoR13ERo-H5tCnq9RdkvNW7IxTAfkseF2p8IIRY2AKnPgVbz82CrplszTogghd8OuleOn7mYzh35MtBgBPbcOTz6ZIYeOv6HvgQlOnPgNjky2xzvO38b6T197cJVL4jLBI9UAwrHFRmZOKUaMHRCm-97FJDtnpfW7ogEdrhxqnbhoSjA1bo3JAs0sXnvtWsG8salW-HxQPTi-N0Zv42XDJx87Hh9Q64D5BaLjQKX2WVy_PwMmD3VTakeYYAAAAAWBpS6sA" None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/melodisupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botDestekKanali")
PLAYLIST = getenv("PLAYLIST", "https://t.me/melodiplaylist")

PLAYLIST_ID = int(getenv("PLAYLIST_ID", "-1002012164341"))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "6678456418"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://udoh:udoh@cluster0.sdmodpx.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6436282424:AAEdIBeCJnzvbVLIS0PDAHkFcB-R56y2OqE")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/setres")
CMD_HNDLR = getenv("CMD_HNDLR", ",")
SESSION1 = getenv("SESSION1", "BQADMVMAVFXcO6ZeD9cJ0h-4HikszZwgJ6p6COYECFxcCNws8FmFTP97iIHCyK3uveqcCjNKGUBi22fu1-5GFxizF7fvYhBkHbVbtV1y9xrxUQOM5e1C0aXI762n-T8_pWraJLoaabZ4dIAv9kd88fNWNYnqv6bdk7glUnx3quJEbS0_GNoegUYcuRWbnXeV6yMJKzP7T0pHAekXxnYz28z9KLeJynaptiYl8d4XFLV4j_NFkDu2h9el_g4pjNgDFwVxOMjUfIIJkVr1_eGRdzYZ1z3qN40_g_ea6fZd-RxkJHQPM9QL-wuxQo8Hr8-Kyd-MHHjkctYB4odVncNEDMMwYgKn2wAAAAGOEShiAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")

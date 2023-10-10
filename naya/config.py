from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "1948147616"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://udoh:udoh@cluster0.sdmodpx.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6484534684:AAFhc381-zhXgXLXG9eNf37ED4DDafZc1yc")
OPENAI_API = getenv("OPENAI_API", "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")
GIT_TOKEN = getenv("GIT_TOKEN", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "none")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "none")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/setres")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "BQCc5pIASNJpvUaqHY9vDXrBYYh2hk5KmauF9RF43jxFfEXu3O22P-MZG89Ui1bZBdOh_CekX1XUbisW1Jy4uB2iYeKg5603u9ZYIbUicswZauHqUoK7m4k5u7lpRGMMqfw3IsRi1gPgaRlbCiW7feojl_fOx7rTVNHuQ3oFZwSQrUaTK2KLa9_UEEJEFvvRaDfNcy7EmhxD47fE4H3qSCvS9WVAiYwUdNGEGun3aXn8iPjNCbiNQBUlQ-EKzr79jjw7bGStJ-EP4eP1Cdp0fFYgm7DzQL5TQ0gamBoO5S_a9-UAi0234wh4533_BedGNFEbNhS4naAMbhBVa3M6Mr3WACND9QAAAAB10wXTAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")

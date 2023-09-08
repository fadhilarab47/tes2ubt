from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "22986689"))
OWNER = int(getenv("OWNER", "6594709698"))
API_HASH = getenv("API_HASH", "693ac2caf9d8941af4cdd2c1f4fd7269")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fakih:fakih@cluster0.k1pn6s6.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6436282424:AAEdIBeCJnzvbVLIS0PDAHkFcB-R56y2OqE")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/setres")
CMD_HNDLR = getenv("CMD_HNDLR", ",")
SESSION1 = getenv("SESSION1", "BQFev8EAlRn_QQ6rVo7hI9Xud_9Zhf0lVk6_BiQ519v_n_QAheIyiXx9mVbpuzV5pmmB1KNLITWlvfMTdPz0GtFgQ-3mYOyQmRrLSDw7a4X0qR7D8q7mFM-Y1DXePxirwVAvT7_RPq8VE0dVfiwesdJqIyFSC2zTbUNNfc2iMSS5ZPzvTvN-f2GSX2vgfsAoIaSosqk9Z6Ft1LRSyLBn_UeZUHDXBRXBNknEIQOHW2fuZJaepQvpTFO_ze_0RZ2W4lXxIU-Ny1GST7dEmKvpWCnJKJvTJLwK-ooG4Pb-LsTIQL-5Xy6MiYeo3ddHDSuJSNbo6x9H3Ts5asR870PpSZ24-CLQAAAAGJE0jCAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")

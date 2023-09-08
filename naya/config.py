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
SESSION1 = getenv("SESSION1", "BQFev8EAHJYHkOnMJFCsPtSAoObZ_T-bUVlVSKUafBGa0olBOVzFuAStXSjKXIRvxFAt3M8NsUIbv2Sylvmld-UqJsEk78m_hSsDvCNTXS1xvGEVcvsIsJ7ZcTGBmtMcfwEP8MxcZQq959Q209uIwAP-YEiydxe4HwRmVsJMQtQdN3vNmPadYnlR68q25d4clqkMfGBATctuHNGyTM4xVOAjsQFIEz29XSZS7IukmlJ5KTBvSn6Gj4iuq8I-aAXzVnaqwS5K1qoOPrxwrKJqbgR6S0HAJvjrKJ2uj0wzYfqXMknAYyWRaZZgVi47NXgtbMBzOCUrpxQhJz3oBflLkrWp0PKx5QAAAAGJE0jCAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")

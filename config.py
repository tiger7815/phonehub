import os

API_ID = API_ID = 22609670

API_HASH = os.environ.get("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6818941008:AAHaOnSmbog-UxpNZWZnMCDtypKgtTyrbGI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6890272504))

LOG = -1002021098463

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6693536228 6693536228 1511103739 5684410709 6034357260 585731991 6488555238 1406300051").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



import os

API_ID = API_ID = 21408627

API_HASH = os.environ.get("API_HASH", "465cca6fa782695983d49db306e0f8be")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6446968748:AAFjKdU2XrFSfEsFrNQ-R8iyTja9Q2ZR97g")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6890272504))

LOG = -1972560469

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6693536228 6693536228 1511103739 5684410709 6034357260 585731991 6488555238 1406300051").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



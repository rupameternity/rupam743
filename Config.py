import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5793203213:AAH4p1gXddFRS3S4hY4ImI2tTn6tiIJARuc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOK4Buxhige-RtUMb7bDkgxy6JWBFmtgjXCP8sWy9Bt1-e5mr-4xzIOumLm12s5KGJYCTO_jVYitvztUdlBh6f-JxRV9Ou-134HFDfKTDJD6yhfKt3vOeZNDi-9sNcbZVKIAtji5gqH_wyhtRLuZBVcTqc9H5M3B_N_MmQ25Iw0sc93Ps0kcUVcDELRCPQhogIFQfRKBeNdwuTO6nI2sRl9LE8RbFB9G6xuBmm9PDXk4fVemNBkJsWovJjRIDvNX0JBuwuX-s94DP0G1jwhZWnyA9c-p7TuA0CJb41HXyQX2EAvb7wKhl4b_Qps6JghuxoXQOtUrtbh6zUveRAlMcae-v4QE=") #pastw string sess
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "rupam_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5601996259")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional

import os

class Config:
    # Telegram API credentials
    API_ID = int(os.getenv("API_ID", 29158577))  # Your API ID
    API_HASH = os.getenv("API_HASH", "5a31bb001fafce5f0c8669b0a8138280")  # Your API Hash
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8445776517:AAFACN-ITibKhAKgrxD3IgSXlvA3RZKq5c4")  # Your Bot Token
    
    # MongoDB configuration
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://imaxprime:imaxprime@entiredatabase.pgyu5ay.mongodb.net/?appName=EntireDatabase")  # MongoDB URI
    DB_NAME = os.getenv("DB_NAME", "premium_group_bot")  # Database name
    
    # PayTM Merchant configuration
    PAYTM_MERCHANT_ID = os.getenv("PAYTM_MERCHANT_ID", "IKFMfs86057296096803")
    PAYTM_MERCHANT_KEY = os.getenv("PAYTM_MERCHANT_KEY", "Yrq0NIq2hqVS3V@a")
    PAYTM_WEBSITE = os.getenv("PAYTM_WEBSITE", "WEBSTAGING")
    PAYTM_CALLBACK_URL = os.getenv("PAYTM_CALLBACK_URL", "https://yourdomain.com/callback")
    
    # Payment plans
    PAYMENT_PLANS = {
        "weekly": 3,
        "monthly": 10,
        "yearly": 99
    }
    
    # Admin user IDs
    ADMINS = [5442514242]  # Add your admin user IDs here
    
    # Group configuration
    MAIN_GROUP_ID = -1003350550618 # Your main group ID
    LOG_CHANNEL_ID = -1003386923017  # Channel for logging

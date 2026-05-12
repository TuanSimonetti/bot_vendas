from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
try:
    load_dotenv()
except:
    pass

# INSTAGRAM
instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
instagram_user_id = os.getenv('INSTAGRAM_USER_ID')
# TIKTOK
tiktok_url_base = os.getenv('TIKTOK_URL_BASE')
tiktok_client_key = os.getenv('TIKTOK_CLIENT_KEY')
tiktok_client_secret = os.getenv('TIKTOK_CLIENT_SECRET')
tiktok_code = os.getenv('TIKTOK_CODE')
toktok_authorization_code = os.getenv('TIKTOK_AUTHORIZATION_CODE')
tiktok_url_redirect = os.getenv('TIKTOK_URL_REDIRECT')

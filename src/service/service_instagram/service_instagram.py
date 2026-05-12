from src.client.client_instagram.client_instagram import client_instagram_check
from src.config_env.env_config import instagram_user_id, instagram_access_token


def service_instagram_check():
    return client_instagram_check(user_id=instagram_user_id, access_token=instagram_access_token)
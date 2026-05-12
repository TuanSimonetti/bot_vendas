from src.client.client_tiktok.client_tiktok import client_tiktok_check
from src.config_env.env_config import tiktok_client_key, tiktok_client_secret, tiktok_code, tiktok_url_redirect, tiktok_url_base


def service_tiktok_check():
    return client_tiktok_check(tiktok_client_key=tiktok_client_key,
                               tiktok_client_secret=tiktok_client_secret,
                               tiktok_code=tiktok_code,
                               tiktok_url_redirect=tiktok_url_redirect,
                               tiktok_url_base=tiktok_url_base)
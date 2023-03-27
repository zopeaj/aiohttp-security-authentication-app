from pydantic import BaseSettings

class Settings(BaseSettings):
    EMAILS_TEMPLATE_DIR = '/app/core/business/shared/emails-templates/src'


settings = Settings()

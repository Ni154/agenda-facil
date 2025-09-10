from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"  # fallback for local
    JWT_SECRET: str = "dev-secret"
    JWT_EXPIRES_MIN: int = 60 * 24
    CORS_ORIGINS: str = "*"
    ENCRYPTION_SECRET: str = "YmFzZTY0LXNpbXBsZS1rZXktMzJieXRlLXNob3VsZC1iZS1oZXJl"  # base64 32 bytes (placeholder)
    ADMIN_EMAIL: str = "admin@erp.local"
    ADMIN_PASSWORD: str = "admin123"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

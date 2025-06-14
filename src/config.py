from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PATH_TO_SRC = Path(__file__).parent.parent


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=f"{PATH_TO_SRC}/.env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    DB_HOST: str
    DB_USER: str
    DB_PORT: int
    DB_PASS: str
    DB_NAME: str
    DB_URL: str

    @property
    def db_url(self) -> str:
        return self.DB_URL.format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME,
        )


class AuthJWT(BaseSettings):
    private_key_path: Path = PATH_TO_SRC / "certs" / "jwt-private.pem"
    public_key_path: Path = PATH_TO_SRC / "certs" / "jwt-public.pem"
    ALGORITHM: str = "RS256"


def load_settings() -> Settings:
    return Settings()


def load_auth_jwt() -> AuthJWT:
    return AuthJWT()

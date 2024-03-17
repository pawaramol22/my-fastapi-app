from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool =True
    DB_URL: str = "mongodb+srv://<username>:<password>@cluster0.fiwhsqt.mongodb.net/?retryWrites=true&w=majority" 
    DB_NAME: str = "myproducts"

    class Config:
        env_file = ".env"  # Load from a .env file 

settings = Settings()

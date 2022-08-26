import os
import pathlib
from dotenv import load_dotenv


class Config:
    dotenvPath = pathlib.Path(__file__).parent.joinpath('.env')
    load_dotenv(dotenvPath)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    print(SECRET_KEY)
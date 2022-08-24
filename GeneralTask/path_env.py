import os
import pathlib

from dotenv import load_dotenv

# get the full directory of this python script parent directory
path_base = pathlib.Path(__file__).parent


#[0] get the parent directory, [1] get grandparent direcotry as so on
path_base = pathlib.Path(__file__).parents[1]

#get the file extension of the last component of your path
path_base = pathlib.Path(__file__).suffix

#get file name
path_base = pathlib.Path(__file__).name

#get file name without extension
path_base = pathlib.Path(__file__).stem

#concatenate the path with given arguments
path_base = pathlib.Path(__file__).parent.joinpath('script', 'abc.txt')

dotenvPath = pathlib.Path(__file__).parent.joinpath('.env')
load_dotenv(dotenvPath)
sKey = os.getenv('SECRET_KEY')
pw = os.getenv("DB_PW")

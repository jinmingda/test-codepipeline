"""The common settings, some expected to be overwritten by later settings."""
from environs import Env

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY", None)

DATABASE_URL = env.str("DATABASE_URL")

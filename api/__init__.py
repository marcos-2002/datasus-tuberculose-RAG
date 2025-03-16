from quart import Quart
import database
from tortoise import run_async

app = Quart(__name__)
app.config.from_object("config.Config")
run_async(database.init())
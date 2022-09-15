
from squarecloud_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app= id_app, key_api= key_api)

bot.start() #ele ira iniciar seu bot
bot.stop() #ele ira parar seu bot
bot.restart() #ele ira reiniciar seu bot
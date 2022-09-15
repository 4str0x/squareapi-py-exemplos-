from squarecloud_py import app

id_app = '994389270607441970'
key_api = '927018673338728488-c1a3b3aff86a4b859e43c5835b36eeaaec588bfc48f6093b7589a9c47d51098d'

bot = app.Client(id_app= id_app, key_api= key_api)

print(bot.backup())
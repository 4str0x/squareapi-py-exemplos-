from squarecloud_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app= id_app, key_api= key_api)

print(bot.status_format()) #todos os status ja formatado

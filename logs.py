from squareapi_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app= id_app, key_api= key_api)

print(bot.logs()) # as ultimas 5 logs
print(bot.log_complete()) # link para as logs completas
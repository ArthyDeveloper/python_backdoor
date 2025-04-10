from pymongo import MongoClient;
import time, sys, os;

user = str(input("Digite seu nome: "))

uri = "MONGODB_URI"
client = MongoClient(uri)

while True:
  try:
    client.server_info()
    print("Conexão Feita!")
    break
  except Exception as erro:
    print(f"Erro: {erro} | Tentando novamente.")

col = client["Database"]["Comunicação"]
result = col.find_one({"type": "usersDoc"})
usersList = result.get("users")
lastMsg = result.get("lastMessages", {})

if user not in usersList:
  print("Usuário não encontrado, criando um novo...")
  col.update_one(
    {"type": "usersDoc"},
    {"$set": {f"lastMessages.{user}": [False, ""]}}
  )

  col.update_one(
    {"type": "usersDoc"},
    {"$push": {"users": user}}
  )

comandos = ["/clear", "/off", "/on", "/removeUser"]

def enviarMensagem(user, message):
  col.update_one(
    {"type": "usersDoc"},
    {"$set": {f"lastMessages.{user}.1": message}}
  )
  time.sleep(1)
  os.system("cls")

def on(user):
  print("Sua status agora é Online!")
  col.update_one(
    {"type": "usersDoc"},
    {"$set": {f"lastMessages.{user}.0": True}}
  )

def off(user):
  print("Sua status agora é Offline!")
  col.update_one(
    {"type": "usersDoc"},
    {"$set": {f"lastMessages.{user}.0": False}}
  )

def clear(user):
  print("Sua última mensagem foi limpa!")
  col.update_one(
    {"type": "usersDoc"},
    {"$set": {f"lastMessages.{user}.1": ""}}
  )

def removeUser(user):
  print("Usuário removido!")
  print("Saindo do mensageiro...")
  col.update_one(
    {"type": "usersDoc"},
    {"$unset": {f"lastMessages.{user}": ""}}
  )
  
  col.update_one(
    {"type": "usersDoc"},
    {"$pull": {"users": user}}
  )

  time.sleep(3)
  sys.exit()

while True:
  msg = str(input("Msg: "))
  if msg == "":
    print("Digite algo!")
    time.sleep(1)
    os.system("cls")
  elif msg == "/on":
    on(user)
  elif msg == "/off":
    off(user)
  elif msg == "/clear":
    clear(user)
  elif msg == "/removeUser":
    removeUser(user)
  else:
    enviarMensagem(user, msg)

  time.sleep(1)
  os.system("cls")
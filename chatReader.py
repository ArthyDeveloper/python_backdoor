from pymongo import MongoClient;
import time, os;

uri = "mongodb+srv://admin:sKIFp5wbtLKM3kNm@cluster0.u8bat.mongodb.net/"
client = MongoClient(uri)

while True:
  try:
    client.server_info()
    print("Conexão Feita!")
    break
  except Exception as erro:
    print(f"Erro: {erro} | Tentando novamente.")


while True:
  col = client["Database"]["Comunicação"]
  result = col.find_one({"type": "usersDoc"})
  lastMsg = result.get("lastMessages", {})
  for u, msg in lastMsg.items():
    if msg[0] != False:
      print(f"{u}: {msg[1]}")
    else: continue
  time.sleep(1)
  os.system("cls")
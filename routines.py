import aiohttp, asyncio
from aiohttp import ContentTypeError

async def api_request(type, data={}):
  route = f"http://localhost:3000/api" # TODO: Trocar para link normal depois.
  async with aiohttp.ClientSession() as session:
    if type == "GET":
      async with session.get(url=route) as response:
        return await response.json()
    elif type == "POST":
      async with session.post(url=route, json=data) as response:
        return await response.json()

async def request(link, type, data={}):
  async with aiohttp.ClientSession() as session:
    if type == "GET":
      async with session.get(url=link) as response:
        return await response.json()
    elif type == "POST":
      async with session.post(url=link, json=data) as response:
        if response.status == 204:
          return "Requisição feita com sucesso."
        try:
          print("Tentando JSON")
          return await response.json()
        except ContentTypeError:
          print("Tentando TEXT")
          return await response.text()

async def main():
  result = await api_request("POST", {"route":"register", "data":{"mac_address":"18:03:73:EB:0A:54"}})
  print(result["result"]["status"])

if __name__ == "__main__":
  asyncio.run(main())
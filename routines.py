import aiohttp, asyncio

async def request(route, type, data={}):
  async with aiohttp.ClientSession() as session:
    if type == "GET":
      async with session.get(url=route) as response:
        return response
    elif type == "POST":
      async with session.post(url=route, json=data) as response:
        return response

configs = {
  "API": "http://localhost:3000/api"
}

api = configs["API"]
async def main():
  result = await request(f"{api}/database/register", "POST", {"mac_address":"18:03:73:EB:0A:54"})
  print(result)

if __name__ == "__main__":
  asyncio.run(main())
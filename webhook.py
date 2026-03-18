import requests, time, mss, io, os
from PIL import Image
from dotenv import load_dotenv
import asyncio
from basicFunctions import *

async def main():
  load_dotenv()
  webhook = os.getenv('TEST_WEBHOOK')
  #send(webhook)
  #resultado = await request(webhook, "POST", {"username":"Anunciador", "content": "Só um teste\nOk"})
  image = screenshot()["file"]
  #resultado = await api_request("POST", {"route":"webhook", "data":{"mac_address":"18:03:73:EB:0A:54", "nickname":"Test", "webhook_message":"teste", "webhook_file":image}})
  resultado = requests.post(webhook, files={"file":image})
  print(resultado)

def send(WEBHOOK_URL):
  file = screenshot()
  response = requests.post(WEBHOOK_URL, files=file)
  print(f"Uploaded screenshot: {response.status_code}")

def screenshot(monitor = 1):
  sct = mss.mss()
  monitor = sct.monitors[monitor]
  img = sct.grab(monitor)
  image = Image.frombytes('RGB', img.size, img.rgb)

  buf = io.BytesIO()
  image.save(buf, format='JPEG', quality=70)
  buf.seek(0)

  files = {
    'file': ('screenshot.jpg', buf, 'image/jpeg')
  }

  return files

if __name__ == '__main__':
  asyncio.run(main())
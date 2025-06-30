import requests, time, mss, io, os
from PIL import Image
from dotenv import dotenv_values, load_dotenv


def main():
  load_dotenv()
  webhook = os.getenv('TEST_WEBHOOK')
  send(webhook)

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

def send(WEBHOOK_URL):
  file = screenshot()
  response = requests.post(WEBHOOK_URL, files=file)
  print(f"Uploaded screenshot: {response.status_code}")


if __name__ == '__main__':
  main()
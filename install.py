from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import requests, uuid, os

def main():
  client = connect_db()
  db_master = client['Ouroboros']
  col_configs = db_master['Configs']

  db_machines = client['Machines']

  wh_alerts = col_configs.distinct('webhooks.wh_alerts')[0]
  #wh_alerts = client['Ouroboros']['Ouroboros'].find_one({"webhook.wh_alerts": {"$exists": True}})

  add_machine(db_machines)

  #message(wh_alerts, f'Install: {mac}')

def connect_db():
  #TODO: Colocar URI fixa.
  load_dotenv()
  connection = os.getenv('MONGODB_URI')
  return MongoClient(connection)

def message(webhook, message):
  headers = {'Content-Type': 'application/json'}
  requests.post(webhook, json={'content': message}, headers=headers)

def add_machine(db_machines):
  mac = get_mac_address()
  if mac not in db_machines.list_collection_names():
    db_machines[mac].insert_one(
      {
        'infos': {
          'name': '',
          'date_implanted': datetime.now(),
          'machine_mac': mac
        },

        'configs': {
          'prints': {
            'webhook': '',
            'auto_send' : False,
            'delay': 5000
          }
        }
      }
    )
    print('Machine Added Sucessfully!')
  else:
    print('Machine exists!')

def get_mac_address():
  try:
    mac = uuid.getnode()
    if (mac >> 40) % 2:
      return "unknown_mac"  # Random MAC
    return str(mac)
  except:
    return "unknown_mac"

if __name__ == '__main__':
  main()
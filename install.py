from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import requests, warnings, uuid, sys, os
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)

def main():
  client = connect_db()
  mac = get_mac_address()
  db_master = client['Ouroboros']
  db_machines = client['Machines']

  col_configs = db_master['Configs']
  wh_alerts = col_configs.distinct('webhooks.wh_alerts')[0]

  install = add_machine(db_machines, mac)
  if install[0] == True:
    print(install[-1])
    #message(wh_alerts, f'New machine: {mac}')
  else:    
    print(install[-1])

def connect_db():
  #TODO: Colocar URI fixa.
  load_dotenv()
  connection = os.getenv('MONGODB_URI')
  return MongoClient(connection)

def message(webhook, message):
  headers = {'Content-Type': 'application/json'}
  requests.post(webhook, json={'content': message}, headers=headers)

def add_machine(db_machines, mac):
  try:
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
      return [True, 'Machine Added!']
    else:
      return [True, 'Machine Already Exists!']
  except Exception as e:
    return [False, e]

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
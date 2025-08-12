from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import requests, uuid, os

def main():
  client = connect_db()
  machines_db = client['Machines']

  mac = get_mac_address()
  add_machine(mac, machines_db)

def connect_db():
  load_dotenv()
  connection = os.getenv('MONGODB_URI')
  return MongoClient(connection)

def add_machine(mac, machines_db):
  if mac not in machines_db.list_collection_names():
    print('Machine does not exist')
    print('Adding Machine...')
    machines_db[mac].insert_one(
      {
        'date_implanted': datetime.now(),
        'machine_mac': mac
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
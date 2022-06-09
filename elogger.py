import json
import logging
import ecs_logging
import requests
import uuid
import os

def write(event_string):
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('/home/tzur/elvis.json')
    handler.setFormatter(ecs_logging.StdlibFormatter())
    logger.addHandler(handler)
    json_UUID = uuid.uuid4()
    keywords_arr = ["arrivedtoserver", "sent", "didntsent", "wrote"]
    
    # TODO: add value check

    logger.info(event_string, extra={"http.request.method": "get", "UUID": json_UUID})
    a_file = open("/home/tzur/elvis.json", "r")
    a_json = json.load(a_file)
    a_file.close()

    os.remove("/home/tzur/elvis.json")

    doc_UUID = uuid.uuid4()
    resp = requests.put(url=f"http://13.81.211.207:9200/{event_string}/_doc/{doc_UUID}", json=a_json,
                        headers={'Content-Type': 'application/json'})
    #print(resp.json())


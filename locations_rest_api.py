import requests
import uuid

def delete_all_locations():
    requests.delete("http://127.0.0.1:8080/api/locations")


def create_location(name_prefix, coords):
    name = name_prefix + "" + str(uuid.uuid4())
    data = {"name": name, "coords": "5,5"}
    requests.post("http://127.0.0.1:8080/api/locations", json=data)

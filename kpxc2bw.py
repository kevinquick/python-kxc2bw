import sys
import json
import uuid
from pykeepass import PyKeePass

def load_keepassdb(database, password, bitwarden_json):
    kp = PyKeePass(filename=database, password=password)
    # Prepare data for Bitwarden format
    items = []
    for entry in kp.entries:
        # Directly use TOTP URI from KeePass if available
        totp_uri = entry.otp if entry.otp else None

        item = {
            "passwordHistory": [
                {"lastUsedDate": entry.mtime.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                 "password": entry.password}
            ],
            "revisionDate": entry.mtime.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "creationDate": entry.ctime.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "deletedDate": None,
            "id": str(uuid.uuid4()),
            "organizationId": None,
            "folderId": None,
            "type": 1,
            "reprompt": 0,
            "name": entry.title or "No Title",
            "notes": entry.notes or "",
            "favorite": False,
            "fields": [
                {"name": key, "value": value, "type": 0}
                for key, value in entry.custom_properties.items()
            ],
            "login": {
                "uris": [
                    {"match": None, "uri": entry.url or "No URL"}
                ],
                "username": entry.username or "No Username",
                "password": entry.password,
                "totp": totp_uri
            },
            "collectionIds": None
        }
        items.append(item)

    bitwarden_data = {
        "folders": [],
        "items": items
    }

    # Write JSON data to file
    with open(bitwarden_json, 'w') as f:
        json.dump(bitwarden_data, f, indent=4)

    print(f"Data written to {bitwarden_json}")

if __name__ == '__main__':
    keepass_database = sys.argv[1]
    keepass_password = sys.argv[2]
    bitwarden_json = sys.argv[3]
    load_keepassdb(keepass_database, keepass_password, bitwarden_json)
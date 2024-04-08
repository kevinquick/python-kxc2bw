# KeePassXC to Bitwarden/Vaultwarden converter
This Python script has been developed since there was no good alternative for importing KeePassXC (.kdbx) entries in Bitwarden/Vaultwarden

It supports all field types in KeePassXC, including TOTP and custom fields

There is no support for conversion to different entry types in Bitwarden, conversion is done for the "Login" entry type only

## Requirements
pykeepass
```
pip install pykeepass
```

## Usage
Usage is very simple, the script should be able to find the KeePassXC database, and the database should be opened with a master password which you need to provide.

This results in a JSON formatted file which can be directly import in Bitwarden/Vaultwarden as a `Bitwarden (json)*` file format, in the `Import data` in Bitwarden/Vaultwarden.

It expects the following arguments:
```
python kpxc2bw.py <vault.kdbx> <vault password> <output json>
```
Example:
```
python kpxc2bw.py keepass.kdbx P4ssw0rd bitwarden.json
```

## Notes
JSON file has been formatted according to the official Bitwarden documentation:
[Condition a Bitwarden .csv or .json](https://bitwarden.com/help/condition-bitwarden-import/)
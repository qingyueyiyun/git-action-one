import os
import sys
import hashlib

file_name = sys.argv[1]

if not os.path.exists(file_name):
    raise ValueError(f"{file_name} is not exist")

if not os.path.isfile(file_name):
    raise ValueError(f"{file_name} is not a file")

with open(file_name, "rb") as f:
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest().upper()
    print(f"sha256: {readable_hash}")
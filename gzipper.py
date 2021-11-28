from pathlib import Path
import os

for path in Path("./").rglob("*.json"):
    print(path)
    os.system("gzip -k -f " + str(path))

import os
import re

VAULT_FOLDER = "reels"
INDEX_FILE = "reels.md"

os.makedirs(VAULT_FOLDER, exist_ok=True)

existing = set()
urls = []

# scan existing nodes
for file in os.listdir(VAULT_FOLDER):
    if file.endswith(".md"):
        path = os.path.join(VAULT_FOLDER, file)

        with open(path, encoding="utf-8") as f:
            content = f.read()

        match = re.search(r"id:\s*reel_([A-Za-z0-9_-]+)", content)
        if match:
            existing.add(match.group(1))

# read reel index
with open(INDEX_FILE, encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith("- "):
            urls.append(line[2:])

# create missing nodes
for url in urls:

    shortcode = url.split("/")[-2]

    if shortcode in existing:
        continue

    filename = f"reel_{shortcode}.md"
    path = os.path.join(VAULT_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as note:
        note.write(f"""---
id: reel_{shortcode}
source: {url}
type: reel
---

# Reel {shortcode}

Source: {url}

Notes:
-
""")

    print(f"Created node for {shortcode}")
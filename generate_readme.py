from datetime import datetime
import re

today = datetime.utcnow().strftime("%Y-%m-%d")
date_line = f"_Last updated: {today} UTC_"

with open("README.md", "r") as f:
    content = f.read()

# Replace or append the last updated line
if re.search(r"_Last updated: .+ UTC_", content):
    content = re.sub(r"_Last updated: .+ UTC_", date_line, content)
else:
    if not content.endswith("\n"):
        content += "\n"
    content += f"\n{date_line}\n"

with open("README.md", "w") as f:
    f.write(content)

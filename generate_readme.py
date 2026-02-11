import random
from datetime import datetime

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency."
]

quote = random.choice(quotes)
today = datetime.utcnow().strftime("%Y-%m-%d")

content = f"""
# Kamran Khalid

Backend Architect | Fintech | PHP | Node.js | Microservices

## Daily Developer Thought
> {quote}

_Last updated: {today} UTC_
"""

with open("README.md", "w") as f:
    f.write(content)

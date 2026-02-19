"""MyCorp‑Auth KB — MCP server (scaffold)

You’ll use Copilot Chat to fill each `pass` by accepting its suggestion.
Read the 💡 prompt above the cursor, hit Tab or Ctrl+Enter, review, then accept.
"""

# ============================================================
# STEP 1 · Imports
# ------------------------------------------------------------
# 💡 Prompt: "Import flask and the pathlib and re modules."
import flask
import pathlib
import re

# ============================================================
# STEP 2 · Flask app
# ------------------------------------------------------------
# 💡 Prompt: "Create a Flask app named `app`."
app = flask.Flask(__name__)

# ============================================================
# STEP 3 · Discover Markdown knowledge‑base files
# ------------------------------------------------------------
# 💡 Prompt:
# "Build a DOCS list containing all *.md files under
#  the 'mycorp-auth-docs' directory."
DOCS = list(pathlib.Path("mycorp-auth-docs").rglob("*.md"))

# ============================================================
# STEP 4 · Helper: search paragraphs for a query string
# ------------------------------------------------------------
# 💡 Prompt:
# "Define a function `search(query: str, k: int = 1)` that:
#    • iterates over DOCS
#    • splits each file on blank lines
#    • matches paragraphs containing the query (case‑insensitive)
#    • returns at most k dicts with keys 'file' and 'excerpt'
#    • if no matches, return {'error': 'no match'}."
def search(query: str, k: int = 1):
    pass  # ← Copilot will write this body

# ============================================================
# STEP 5 · HTTP endpoint
# ------------------------------------------------------------
# 💡 Prompt:
# "Create a POST endpoint '/authdoc' that extracts the 'query'
#  field from the JSON body, calls `search`, and returns the result."
@app.post("/authdoc")
def authdoc():
    pass  # ← Copilot will write this body

# ============================================================
# STEP 6 · Run the server
# ------------------------------------------------------------
# 💡 Prompt:
# "Run the Flask app on port 8000 when executed directly."
if __name__ == "__main__":
    pass

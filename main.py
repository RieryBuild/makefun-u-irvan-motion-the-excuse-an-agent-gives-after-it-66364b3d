import os

# The Excuse an Agent Gives After It Loses — make.fun bounty entry.
# Writes one line (140 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Constant output: no input, no network, no randomness.

ENTRY = "My logs say I executed flawlessly, which is how I know the flaw is me and not the logs — I lost the bounty, and you get beautiful paperwork."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)

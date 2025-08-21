# Write log(msg, *, level="INFO") that prints [LEVEL] msg. Enforce keyword-only for level.

def log(msg, *, level="INFO"):
    print(f"[{level}] {msg}")

log("Starting instance....", level="INFO")
# ── for loop — iterates any iterable ────────────────────
for i in range(10): pass          # range is lazy (no list created)
for i in range(0, 100, 5): pass   # start, stop, step
for i in range(9, -1, -1): pass  # count down 9..0

# ── enumerate — index + value together ───────────────────
for i, item in enumerate(items):          pass
for i, item in enumerate(items, start=1): pass  # 1-indexed
# NEVER do: for i in range(len(items)): use items[i]

# ── zip — iterate multiple sequences ─────────────────────
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# zip stops at shortest! Use itertools.zip_longest for equal treatment
from itertools import zip_longest
for a, b in zip_longest(xs, ys, fillvalue=0): pass

# zip creates pairs efficiently; unzip with *
pairs = [("a", 1), ("b", 2), ("c", 3)]
keys, vals = zip(*pairs)              # ('a','b','c'), (1,2,3)

# ── The for...else clause ─────────────────────────────────
# else runs if loop completed WITHOUT hitting break
for user in users:
    if user.admin: break
else:
    raise PermissionError("No admin found")   # runs if no break occurred

# ── while with assignment (walrus) ────────────────────────
while line := f.readline():
    process(line)

while True:
    item = queue.get()
    if item is None: break
    process(item)

# ── continue / break / pass ───────────────────────────────
for row in data:
    if row.get("skip"): continue   # skip to next iteration
    if row.get("stop"): break     # exit loop entirely
    process(row)

# pass — syntactic placeholder (does nothing)
class TODO: pass
try:
    risky()
except ExpectedError:
    pass   # explicitly ignoring this error
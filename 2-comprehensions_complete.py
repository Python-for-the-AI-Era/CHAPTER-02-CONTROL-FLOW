# ── List comprehension ────────────────────────────────────
squares  = [x**2 for x in range(10)]
evens    = [x for x in range(20) if x % 2 == 0]
cleaned  = [s.strip().lower() for s in raw if s.strip()]
flat     = [x for row in matrix for x in row]  # nested: outer first
pairs    = [(x, y) for x in [1,2] for y in [3,4]]  # [(1,3),(1,4),(2,3),(2,4)]

# ── Dict comprehension ────────────────────────────────────
word_len = {w: len(w) for w in words}
inverted = {v: k for k, v in mapping.items()}
filtered = {k: v for k, v in data.items() if v is not None}
squares  = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# ── Set comprehension ─────────────────────────────────────
unique_domains = {email.split("@")[1] for email in emails}
common = {x for x in a} & {x for x in b}  # intersection

# ── Generator expression ─────────────────────────────────
# Uses () instead of [] — lazy, doesn't build list in memory
total = sum(x**2 for x in range(1_000_000))  # no million-element list
first = next(x for x in items if x.valid)      # stops at first match
any(x > 100 for x in nums)                     # short-circuits on first True
all(x > 0 for x in nums)                       # short-circuits on first False
max(user.score for user in users)
sorted(user.name for user in users if user.active)

# ── When to use which ─────────────────────────────────────
# list comprehension: when you need the full list (index, len, multiple passes)
# generator: when consuming once in a pipeline (sum, max, any, next, for-loop)
# dict comp: build a dict from an iterable
# set comp: unique values
# AVOID: deeply nested comprehensions (>2 levels) — use explicit loops

# ── Performance ───────────────────────────────────────────
# List comp is ~1.5x faster than equivalent for-loop
# Generator uses O(1) memory vs O(n) for list comp
# For large data: always prefer generator expressions
# ── Falsy values — ALL other objects are truthy ───────────
# False, None, 0, 0.0, 0j, "", b"", [], {}, set(), ()
# Any object with __bool__ returning False or __len__ returning 0

if not items:           # idiomatic: check for empty list
    print("nothing")
if user and user.active:  # short-circuit: user.active only evaluated if user is truthy
    allow_access(user)
if data or []:           # 'or' returns first truthy operand or last operand
    pass

# Short-circuit rules:
# and: returns first FALSY value, or LAST value if all truthy
# or:  returns first TRUTHY value, or LAST value if all falsy
name = user.name or "Anonymous"    # common default pattern
value = d.get("key") or default    # caution: 0/""/[] all fall through to default!
value = d.get("key", default)      # better when 0 or "" are valid values

# ── Ternary (conditional expression) ─────────────────────
label = "active" if user.active else "inactive"
x = a if a > 0 else -a              # abs(a)

# Nested ternary — readable limit: max 1 level
grade = "A" if score >= 90 else "B" if score >= 80 else "C"  # ok

# ── Walrus operator := (3.8+) ─────────────────────────────
# Assigns AND returns value in one expression
if n := len(data):
    print(f"Processing {n} items")  # n already computed and bound

while chunk := f.read(8192):        # read until empty bytes
    process(chunk)

# Very useful with regex
import re
if m := re.match(r"\d+", line):
    print(m.group())                 # m is available inside block

# ── is vs == ─────────────────────────────────────────────
x = [1, 2, 3]
y = [1, 2, 3]
x == y     # True  — same value
x is y     # False — different objects
x is None  # CORRECT way to check for None
x == None  # WRONG — calls __eq__, can be overridden

# Small integer caching: CPython caches -5 to 256
a = b = 256; a is b  # True (same object)
a = b = 257; a is b  # False (new objects) — never rely on this
from itertools import (
    chain, chain.from_iterable, islice, count, cycle, repeat,
    product, combinations, combinations_with_replacement, permutations,
    groupby, filterfalse, takewhile, dropwhile, compress,
    accumulate, pairwise, starmap, tee, zip_longest, batched
)

# ── Infinite iterators ────────────────────────────────────
count(10, 2)          # 10, 12, 14, 16, ...  (step=2)
cycle(["A","B","C"])  # A, B, C, A, B, C, ...  (infinite)
repeat(42, 5)         # 42, 42, 42, 42, 42  (n times)

# ── Chaining / combining ──────────────────────────────────
chain([1,2], [3,4], [5])     # 1,2,3,4,5 — flatten multiple iterables
chain.from_iterable([[1],[2],[3]])  # same but from single iterable of iterables
# Alternative: [x for xs in nested for x in xs]

# ── Slicing / filtering lazy iterables ────────────────────
islice(it, 5)          # first 5 elements (like it[:5] for generators)
islice(it, 2, 8, 2)   # start, stop, step
takewhile(lambda x: x < 10, nums)  # yield while condition True
dropwhile(lambda x: x < 10, nums)  # skip while True, then yield rest
filterfalse(lambda x: x % 2, nums) # opposite of filter()
compress(data, selectors)           # compress("ABCD",[1,0,1,1]) → A,C,D

# ── Combinatoric generators ───────────────────────────────
product("AB", repeat=2)    # AA,AB,BA,BB (cartesian product)
permutations("ABC", 2)      # AB,AC,BA,BC,CA,CB (ordered)
combinations("ABC", 2)       # AB,AC,BC (unordered, no repeats)
combinations_with_replacement("ABC", 2)  # AA,AB,AC,BB,BC,CC

# ── groupby — group consecutive same-key items ────────────
# IMPORTANT: data must be sorted by key first!
data = sorted(users, key=lambda u: u.city)
for city, group in groupby(data, key=lambda u: u.city):
    users_in_city = list(group)   # group is a lazy iterator — consume before next iter!

# ── Batching ─────────────────────────────────────────────
for batch in batched(items, n=100):   # Python 3.12+ — chunks of 100
    db.bulk_insert(batch)

# ── pairwise — sliding window of 2 ────────────────────────
pairwise([1,2,3,4])   # (1,2),(2,3),(3,4) — Python 3.10+

# ── accumulate — running aggregate ───────────────────────
accumulate([1,2,3,4])            # 1,3,6,10  (running sum)
accumulate([1,2,3], max)         # 1,2,3     (running max)
accumulate([1,2,3], initial=0)  # 0,1,3,6  (starts from initial)

# ── tee — split one iterator into n ──────────────────────
iter1, iter2 = tee(some_generator, 2)  # safe to iterate both independently
# WARNING: advancing one tee iterator buffers consumed items — memory grows

# ── starmap ───────────────────────────────────────────────
starmap(pow, [(2,3), (3,2), (4,2)])  # 8, 9, 16  (unpacks tuples as args)
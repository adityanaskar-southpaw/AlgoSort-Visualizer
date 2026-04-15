import random

# -----------------------------
# RANDOM DATA
# -----------------------------
def generate_random(n):
    return [random.randint(1, 1000) for _ in range(n)]

# -----------------------------
# SORTED DATA (BEST CASE)
# -----------------------------
def generate_sorted(n):
    return list(range(n))

# -----------------------------
# REVERSED DATA (WORST CASE)
# -----------------------------
def generate_reversed(n):
    return list(range(n, 0, -1))

# -----------------------------
# DUPLICATE HEAVY DATA (OPTIONAL)
# -----------------------------
def generate_duplicates(n):
    return [random.choice([10, 20, 30, 40, 50]) for _ in range(n)]
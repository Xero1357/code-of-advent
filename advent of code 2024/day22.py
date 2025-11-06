from collections import defaultdict

# --- Load input file ---
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day22.txt") as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

MOD = 16777216  # 2^24

# --- Function to evolve one secret number ---
def next_secret(secret):
    secret = (secret ^ (secret * 64)) % MOD
    secret = (secret ^ (secret // 32)) % MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret

# --- Part 1 ---
total_part1 = 0
for initial in numbers:
    s = initial
    for _ in range(2000):
        s = next_secret(s)
    total_part1 += s
print(total_part1)  # Only the answer, no extra text

# --- Part 2 ---
sequence_to_price = defaultdict(int)  # sum of best prices for each sequence

for initial in numbers:
    secret = initial
    prices = []
    for _ in range(2000):
        secret = next_secret(secret)
        prices.append(secret % 10)
    
    # compute changes
    changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    
    seen = set()  # ensure we only take the first occurrence per sequence per buyer
    for i in range(len(changes) - 3):
        seq = tuple(changes[i:i+4])
        if seq not in seen:
            seen.add(seq)
            price_after_seq = prices[i+4]  # price after this 4-change sequence
            sequence_to_price[seq] += price_after_seq

# find the sequence giving maximum bananas total
best_total = max(sequence_to_price.values())
print(best_total)

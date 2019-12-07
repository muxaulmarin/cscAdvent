print(
sum(
set(
[gcd(2**i + 1, 2**j + 1) for i in range(1, 2020) for j in range(1, 2020) if i != j or i < j]
)
)
)

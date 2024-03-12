import math

n = 6

m = 4

k = 0

l = 3

nu = 4

fk = [0] * 500

pk = [0] * 500

alfa = l / nu

sumfk = 1

p0 = 1

toc = 0

fk[k] = 1.0

while fk[k] >= 0.01:

    k += 1

    if k < m:
        fk[k] = ((l + (k - 1) * nu) * fk[k - 1]) / (k * nu)

    if k >= m and k <= n:
        fk[k] = ((l + (k - 1) * nu) * fk[k - 1]) / (k * nu) - (l * fk[k - m]) / (k * nu)

    if k > n:
        fk[k] = ((l + n * nu) * fk[k - 1]) / (n * nu) - (l * fk[k - m]) / (n * nu)

    sumfk += fk[k]

p0 = 1 / sumfk

Mc = 0

Moc = 0

No = 0

for i in range(k):

    pk[i] = fk[i] * p0

    Mc += i * pk[i]

    if i > n:
        Moc += (i - n) * pk[i]

    if i < n:
        No += (n - i) * pk[i]

print(f"Moc: {Moc:.3f}")

print(f"Mc: {Mc:.3f}")

print(f"No: {No:.3f}")

toc = (Moc / l) * 24

print(f"Toc: {toc:.3f} hours")
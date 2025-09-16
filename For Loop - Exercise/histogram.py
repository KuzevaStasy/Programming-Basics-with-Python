n = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    else:
        p5 += 1

p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

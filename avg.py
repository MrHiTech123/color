from sys import argv

def avg_two(a, b):
    return (a + b) // 2

if len(argv) < 2:
    print('Usage: main.py num1 num2')
    raise SystemExit(0)


color1 = argv[1]
color2 = argv[2]

while len(color1) < 6:
    color1 = '0' + color1

while len(color2) < 6:
    color2 = '0' + color2


color1 = [(color1[i:i + 2]) for i in range(0, 6, 2)]
color2 = [(color2[i:i + 2]) for i in range(0, 6, 2)]

print(len(color1), len(color2))
for c1, c2 in zip(color1, color2):
    avg = ((int(c1, 16) + int(c2, 16)) // 2)
    # print(c1, c2, avg)
    if avg > 16:
        print(hex(avg)[2:], end='')
    else:
        print('0' + hex(avg)[2:], end='')
print()

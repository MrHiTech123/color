from sys import argv

if len(argv) < 2:
    print('Usage: neg hexcolor')
    raise SystemExit(0)


print((int(argv[1], 16) - int('FFFFFF', 16)))






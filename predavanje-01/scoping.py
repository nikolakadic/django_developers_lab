# NAMESPACES
# 1 - local
# 2 - global
# 3 - built - in 


def ime_funkcije():
    global ime_globalne
    print(ime_globalne)
    ime_globalne = 52
    print(ime_globalne)

ime_globalne = 12


ime_funkcije()

print(ime_globalne)
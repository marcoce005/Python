from math import pi


def sphere_volume(r):
    return (4 / 3) * pi * (r**3)


def sphere_surface(r):
    return 4 * pi * (r**2)


def cylinder_volume(r, h):
    return (r**2) * pi * h


def cylinder_surface(r, h):
    return 2 * r * pi * h + (2 * (r**2) * pi)


def cone_volume(r, h):
    return (pi * (r**2) * h) / 3


def cone_surface(r, h):
    return (((r**2) + (h**2)) ** 0.5) * pi * r


r = 5  # raggio in unità
h = 10  # altezza in unità

# Chiamate delle funzioni
volume_sfera = sphere_volume(r)
superficie_sfera = sphere_surface(r)
volume_cilindro = cylinder_volume(r, h)
superficie_cilindro = cylinder_surface(r, h)
volume_cono = cone_volume(r, h)
superficie_cono = cone_surface(r, h)

print("Volume della sfera:", volume_sfera)
print("Superficie della sfera:", superficie_sfera)
print("Volume del cilindro:", volume_cilindro)
print("Superficie del cilindro:", superficie_cilindro)
print("Volume del cono:", volume_cono)
print("Superficie del cono:", superficie_cono)
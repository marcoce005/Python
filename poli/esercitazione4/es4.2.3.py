from math import cos, sin, pi

def degree_to_rad(a):
    return (pi / 180) * a

DELTA_T = 0.01
G = 9.81

v = float(input("Inserire la velocità iniziale [m / s]:\t"))
alpha = degree_to_rad(float(input("Inserire l'angolo di incidenza della palla di cannone [in gradi]:\t")))
s = 0
v_y = v * sin(alpha)
v_x = v * cos(alpha)

while v_y > 0:
    s += v_x * DELTA_T
    v_y -= G * DELTA_T

s *= 2  # facendo una parabola la distanza è doppia

print(f"Partendo con una velocità iniziale di {v} m / s la palla di cannone ha percorso:\n{s:.5f} m")

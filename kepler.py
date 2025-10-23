import math
import datetime

Initial_value = 0
E_before = Initial_value

First_date = datetime.datetime(2024, 10 , 28, 16, 1, 5)
Second_date = datetime.datetime(2025, 10 , 29, 2, 15, 0)
a = 9570*1000
e = 0.1
Ue = 3.986*(10**14)

def delta_time(x, y):
    delta_time = y - x
    return delta_time.total_seconds()

def kepler(a, e, t, U, E):
    f = E - (e * math.sin(E)) - ((math.sqrt(U/(a**3)) * t)%(2*math.pi))
    f_prime = 1 - e * math.cos(E)
    E_next = E - (f / f_prime)
    return E_next

def cal_para(E, a, e):
    r = a * (1 - e*math.cos(E))
    x_w = a*(math.cos(E) -e)
    y_w = a*math.sqrt(1 - e**2)*math.sin(E)
    return r, x_w, y_w

if __name__ == "__main__":
    t = delta_time(First_date, Second_date)
    while True:
        E = kepler(a, e, t, Ue, E_before)
        if abs(E - E_before) < 1e-6:
            break
        E_before = E
    r, x_w, y_w = cal_para(E, a, e)
    print(f"Distance (r): {r} meters")
    print(f"Position in orbital plane (x_w, y_w): ({x_w}, {y_w}) meters")
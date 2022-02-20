import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1  # kg
k_air = 0.00324844  # kg/m
F_M = 12.2  # N/kg
g = 9.8  # m/s^2
miu = 0.6
r_wheel = 0.75  # m

INF = 999999

theta1 = 2
A1 = F_M - (m * g * miu) / (r_wheel) - m * g * (math.sin(math.pi * theta1 / 180.00))
# initial condition
v0 = 0
# time points
t = np.linspace(0, 50)
analytical1 = [0 for i in range(len(t))]
for i in range(len(t)):
    analytical1[i] = (math.sqrt(A1) * np.tanh((t[i] * math.sqrt(A1 * k_air)) / m)) / (math.sqrt(k_air))
upper = (math.sqrt(A1) * np.tanh((INF * math.sqrt(A1 * k_air)) / m)) / (math.sqrt(k_air))
l = [upper for i in range(len(t))]
fig = plt.figure(figsize=(figsizex, figsizey), dpi=80)
# plot results
plt.plot(t, l, ':')
plt.plot(t, analytical1)
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend(['maximum possible velocity with human force\n=' + str(round(upper, 2)) + 'm/s', 'analytical1 solution'])
plt.show()


get_velocity_graph(5, 5, 5)
get_velocity_graph(8, 5, 5)
get_velocity_graph(10, 5, 5)

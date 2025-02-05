import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore

# Definimos la función vectorial r(t) = (x(t), y(t), z(t))
def r(t):
    x = np.cos(t)  # Movimiento circular en X
    y = np.sin(t)  # Movimiento circular en Y
    z = t / 5      # Movimiento lineal en Z
    return np.array([x, y, z])

# Definimos la derivada de r(t) para la velocidad
def v(t):
    dx = -np.sin(t)  # Derivada de cos(t)
    dy = np.cos(t)   # Derivada de sin(t)
    dz = 1/5         # Derivada de t/5
    return np.array([dx, dy, dz])

# Definimos la derivada de v(t) para la aceleración
def a(t):
    ddx = -np.cos(t)  # Segunda derivada de cos(t)
    ddy = -np.sin(t)  # Segunda derivada de sin(t)
    ddz = 0           # Segunda derivada de t/5
    return np.array([ddx, ddy, ddz])

# Generamos valores de t
t_values = np.linspace(0, 10, 100)
trajectory = np.array([r(t) for t in t_values])
velocity = np.array([v(t) for t in t_values])
acceleration = np.array([a(t) for t in t_values])

# Graficamos la trayectoria, velocidad y aceleración
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], label='Trayectoria', color='b')
ax.quiver(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 
          velocity[:, 0], velocity[:, 1], velocity[:, 2],
          color='r', length=0.2, normalize=True, label='Velocidad')
ax.quiver(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 
          acceleration[:, 0], acceleration[:, 1], acceleration[:, 2],
          color='g', length=0.2, normalize=True, label='Aceleración')

# Etiquetas y leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Simulación del Movimiento de una Partícula en el Espacio')
ax.legend()

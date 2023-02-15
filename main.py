import psycopg2
import db_info
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

table = psycopg2.connect(
    host=db_info.host,
    user=db_info.user,
    password=db_info.password,
    database='foucault'
)
select = f'SELECT * FROM foucault_consts'
with table.cursor() as cursor:
    cursor.execute(select)
    result = cursor.fetchall()

g, L, init_x, init_y, init_xdot, init_ydot, omega, lamb = [float(result[0][i]) for i in range(8)]

fig = plt.figure()
lines = plt.plot([], '.', lw=0.1)
line = lines[0]
plt.axis('scaled')
plt.xlim(-0.7, 0.7)
plt.ylim(-0.7, 0.7)
plt.title('Маятник Фуко')
plt.xlabel('x')
plt.ylabel('y')

x = list()
y = list()


def animate(frame):
    t = frame*10
    x0 = init_x * np.cos(g/L * t) * np.cos(omega * np.sin(lamb) * t)
    y0 = -init_x * np.cos(g/L * t) * np.sin(omega * np.sin(lamb) * t)
    x.append(x0)
    y.append(y0)
    line.set_data((x, y))


anim = FuncAnimation(fig, animate, frames=8640, interval=1)
# anim.save('video.mp4')
plt.show()

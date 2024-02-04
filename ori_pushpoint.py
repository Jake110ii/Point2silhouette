import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ln, = ax.plot([],[],'bo')
cur, = ax.plot([],[],'ro')

def motion(event):
    x = event.xdata
    y = event.ydata

    cur.set_data(x,y)
    plt.draw()

def onclick(event):
    x = event.xdata
    y = event.ydata

    ln.set_data(x,y)
    ax.set_title('x = {}, y = {}'.format(event.xdata, event.ydata))
    plt.draw()

fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('motion_notify_event', motion)
plt.show()

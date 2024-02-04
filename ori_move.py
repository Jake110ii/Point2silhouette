import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

def motion(event):
    global gco, xdata, ydata, ind
    if gco is None:
        return
    x = event.xdata
    y = event.ydata
    if x == None or y == None:
        return
    xdata[ind] = x
    ydata[ind] = y
    gco.set_data(xdata,ydata)
    plt.draw()

def onpick(event):
    global gco, xdata, ydata, ind
    gco = event.artist
    xdata = gco.get_xdata()
    ydata = gco.get_ydata()
    ind = event.ind[0]

def release(event):
    global gco
    gco = None

gco = None     # ピックした要素が含まれる直線(Line2Dクラス)
ind = None     # ピックした直線のインデックス
xdata = None     # ドラッグするまえの直線のxデータを入れておく
ydata = None     # ドラッグするまえの直線のyデータを入れておく
fig, ax = plt.subplots()
ax.plot(np.random.rand(10),"o-",picker=15)

fig.canvas.mpl_connect('pick_event', onpick)
fig.canvas.mpl_connect('motion_notify_event', motion)
fig.canvas.mpl_connect('button_release_event', release)
plt.show()

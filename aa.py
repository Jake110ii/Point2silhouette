import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as wg
from utils.NearestNeighbor import nearest_sort

class Img2silhouette:
    def __init__(self, ax):
        self.ax = ax
        self.ln, = ax[0].plot([], [], 'bo')
        self.cur, = ax[0].plot([], [], 'ro')
        self.x = []
        self.y = []
        self.ax[0].set_xlim(-500, 4000)
        self.ax[0].set_ylim(-400, 2000)
        self.line_pre = None
        self.gco = None
        self.xdata = None
        self.ydata = None
        self.ind = None
        self.btn2mode = Btn2mode(self)

    def on_pick(self, event):
        self.gco = event.artist
        self.xdata = self.gco.get_xdata()
        self.ydata = self.gco.get_ydata()
        self.ind = event.ind[0]

    def motion_drag(self, event):
        if self.gco is None:
            return
        x = event.xdata
        y = event.ydata
        if x is None or y is None:
            return
        self.xdata[self.ind] = x
        self.ydata[self.ind] = y
        self.gco.set_data(self.xdata, self.ydata)
        plt.draw()

    def release(self, event):
        self.gco = None

    def onclick(self, event):
        x = event.xdata
        y = event.ydata
        self.x.append(x)
        self.y.append(y)
        self.cur.set_data(x, y)
        self.ln.set_data(self.x, self.y)
        self.ax[0].set_title('x = {}, y = {}'.format(event.xdata, event.ydata))
        plt.draw()

    def btn_click(self, event):
        if self.line_pre is not None:
            self.line_pre.remove()
        self.x.pop()
        self.y.pop()
        self.x, self.y = nearest_sort(self.x, self.y)
        self.line_pre, = self.ax[0].plot(self.x + [self.x[0]], self.y + [self.y[0]])
        self.cur.set_data(self.x[0], self.y[0])
        self.ln.set_data(self.x, self.y)
        plt.draw()

    def setup_callbacks(self):
        fig.canvas.mpl_connect('button_press_event', self.onclick)
        fig.canvas.mpl_connect('motion_notify_event', self.motion_drag)
        fig.canvas.mpl_connect('pick_event', self.on_pick)
        fig.canvas.mpl_connect('button_release_event', self.release)
        self.btn2mode.setup_callbacks()

class Btn2mode:
    def __init__(self, img2silhouette):
        self.img2silhouette = img2silhouette
        self.btn = wg.Button(ax[1], 'Random', color='#f8e58c', hovercolor='#38b48b')

    def btn_click(self, event):
        self.img2silhouette.btn_click(event)

    def setup_callbacks(self):
        self.btn.on_clicked(self.btn_click)

fig, ax = plt.subplots(2, 1, gridspec_kw=dict(width_ratios=[1], height_ratios=[8, 1]))
img2silhouette = Img2silhouette(ax)
img2silhouette.setup_callbacks()

plt.show()


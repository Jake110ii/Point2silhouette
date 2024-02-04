import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as wg
from matplotlib.patches import Rectangle
import utils.NearestNeighbor as near

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
        self.mode_switch = "onclick"  # 初期モードは onclick

    def motion(self, event):
        if self.mode_switch == "motion":
            x = event.xdata
            y = event.ydata
            plt.draw()

    def onclick(self, event):
        if self.mode_switch == "onclick":
            print('onclick')
            x = event.xdata
            y = event.ydata
            self.x.append(x)
            self.y.append(y)
            self.cur.set_data(x, y)
            self.ln.set_data(self.x, self.y)
            self.ax[0].set_title('x = {}, y = {}'.format(x, y))
            plt.draw()

    def btn_click(self, event):
        if self.line_pre is not None:
            self.line_pre.remove()
        print('btn')
        self.x.pop()
        self.y.pop()

        # nearest sort
        self.x, self.y = near.nearest_sort(self.x, self.y)

        self.line_pre, = self.ax[0].plot(self.x + [self.x[0]], self.y + [self.y[0]])
        self.cur.set_data(self.x[0], self.y[0])
        self.ln.set_data(self.x, self.y)
        plt.draw()

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

    def onpick(self, event):
        self.gco = event.artist
        self.xdata = self.gco.get_xdata()
        self.ydata = self.gco.get_ydata()
        self.ind = event.ind[0]

    def release(self, event):
        self.gco = None

    def switch_mode(self, event):
        if self.mode_switch == "onclick":
            self.mode_switch = "motion"
            print("Switched to motion mode")
        elif self.mode_switch == "motion":
            self.mode_switch = "onclick"
            print("Switched to onclick mode")

    def setup_callbacks(self):
        fig.canvas.mpl_connect('button_press_event', self.onclick)
        fig.canvas.mpl_connect('motion_notify_event', self.motion)
        fig.canvas.mpl_connect('pick_event', self.onpick)
        fig.canvas.mpl_connect('button_release_event', self.release)

        btn = wg.Button(ax[1], 'Random', color='#f8e58c', hovercolor='#38b48b')
        btn.on_clicked(self.btn_click)

        switch_btn = wg.Button(ax[1], 'Switch Mode', color='#f8e58c', hovercolor='#38b48b')
        switch_btn.on_clicked(self.switch_mode)

        fig.canvas.mpl_connect('motion_notify_event', self.motion_drag)

fig, ax = plt.subplots(2, 1, gridspec_kw=dict(width_ratios=[1], height_ratios=[8, 1]))
img2silhouette = Img2silhouette(ax)
img2silhouette.setup_callbacks()

plt.show()


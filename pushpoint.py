import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as wg
import matplotlib.gridspec as gridspec

#from utils. import nearest_sorti
import utils.NearestNeighbor as near

#nearest_sort(x_list, y_list)

class Img2silhouette():
    def __init__(self, gs):
        self.ax0 = plt.subplot(gs[0, :])
        self.ax1 = plt.subplot(gs[1, 0])
        self.ax2 = plt.subplot(gs[1, 1])
        self.ax3 = plt.subplot(gs[1, 2])
        self.ln, = self.ax0.plot([],[],'bo')
        self.cur, = self.ax0.plot([],[],'ro')
        self.x = []
        self.y = []
        self.ax0.set_xlim(-500, 4000)
        self.ax0.set_ylim(-400, 2000)
        self.line_pre = None
        self.btn2mode = Btn2mode(self)
    
    @staticmethod
    def motion(event):
        x = event.xdata
        y = event.ydata
        plt.draw()
    
    def onclick(self, event):
        print('onclick')
        x = event.xdata
        y = event.ydata
        self.x.append(x)
        self.y.append(y)

        self.cur.set_data(x, y)
        self.ln.set_data(self.x, self.y)
        self.ax0.set_title('x = {}, y = {}'.format(event.xdata, event.ydata))
        plt.draw()
    
    def btn_click(self, event):
        if self.line_pre is not None:
            self.line_pre.remove()
        print('btn')
        self.x.pop()
        self.y.pop()

        # nearest sort
        self.x, self.y = near.nearest_sort(self.x, self.y)
        self.line_pre, = self.ax0.plot(self.x + [self.x[0]], self.y + [self.y[0]])
        self.cur.set_data(self.x[0], self.y[0])
        self.ln.set_data(self.x, self.y)
        plt.draw()

    def setup_callbacks(self):
        fig.canvas.mpl_connect('button_press_event', self.onclick)
        fig.canvas.mpl_connect('motion_notify_event', self.motion)

        self.btn2mode.setup_callbacks()


class Btn2mode:
    def __init__(self, img2silhouette):
        self.img2silhouette = img2silhouette
        self.btn = wg.Button(img2silhouette.ax1, 'silhouette', color='#ffffff', hovercolor='#38b48b')
        self.btn_clear = wg.Button(img2silhouette.ax2, 'clear', color='#ffffff', hovercolor='#38b48b')

    def btn_click(self, event):
        self.img2silhouette.btn_click(event)

    def btn_clear_click(self, event):
        # Clear all points
        self.img2silhouette.x.clear()
        self.img2silhouette.y.clear()
        self.img2silhouette.ln.set_data([], [])
        self.img2silhouette.cur.set_data([], [])
        if self.img2silhouette.line_pre is not None:
            self.img2silhouette.line_pre.remove()
            self.img2silhouette.line_pre = None
        plt.draw()

    def setup_callbacks(self):
        self.btn.on_clicked(self.btn_click)
        self.btn_clear.on_clicked(self.btn_clear_click)




# FigureとGridSpecの作成
fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 3, height_ratios=(8, 1))

#ax0 = plt.subplot(gs[0, :])
img2silhouette = Img2silhouette(gs)
img2silhouette.setup_callbacks()

#ax1 = plt.subplot(gs[1, 0])
#btn = wg.Button(ax1, 'Silhouette', color='#ffffff', hovercolor='#38b48b')
#btn.on_clicked(img2silhouette.btn_click)

ax2 = plt.subplot(gs[1, 1])
#btn = wg.Button(ax2, 'Switch', color='#ffffff', hovercolor='#38b48b')
#btn.on_clicked(img2silhouette.btn_click)

ax3 = plt.subplot(gs[1, 2])
#btn = wg.Button(ax3, 'Switch', color='#ffffff', hovercolor='#38b48b')
#btn.on_clicked(img2silhouette.btn_click)


plt.show()

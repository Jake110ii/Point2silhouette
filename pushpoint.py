import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as wg

#from utils. import nearest_sorti
import utils.NearestNeighbor as near

#nearest_sort(x_list, y_list)

class Img2silhouette():
    def __init__(self, ax):
        self.ax = ax
        self.ln, = ax[0].plot([],[],'bo')
        self.cur, = ax[0].plot([],[],'ro')
        self.x = []
        self.y = []
        self.ax[0].set_xlim(-500, 4000)
        self.ax[0].set_ylim(-400, 2000)
        self.line_pre = None
    
    @staticmethod
    def motion(event):
        x = event.xdata
        y = event.ydata
        plt.draw()
    
    def onclick(self, event):
        print('click')
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
        print('btn')
        self.x.pop()
        self.y.pop()
        print(self.x)
        print(self.x + [self.x[0]])

        # nearest sort
        self.x, self.y = near.nearest_sort(self.x, self.y)
        print('after:', self.x)

        self.line_pre, = self.ax[0].plot(self.x + [self.x[0]], self.y + [self.y[0]])
        self.cur.set_data(self.x[0], self.y[0])
        self.ln.set_data(self.x, self.y)
        plt.draw()

      
        
fig, ax = plt.subplots(2, 1, gridspec_kw=dict(width_ratios=[1], height_ratios=[8, 1]))
img2silhouette = Img2silhouette(ax)
fig.canvas.mpl_connect('button_press_event', img2silhouette.onclick)
fig.canvas.mpl_connect('motion_notify_event', img2silhouette.motion)
btn = wg.Button(ax[1], 'Random', color='#f8e58c', hovercolor='#38b48b')
btn.on_clicked(img2silhouette.btn_click)
plt.show()

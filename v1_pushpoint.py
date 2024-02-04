import matplotlib.pyplot as plt
import numpy as np

class Img2silhouette():
    def __init__(self, ax):
        self.ax = ax
        self.ln, = ax.plot([],[],'bo')
        self.cur, = ax.plot([],[],'ro')
        self.x = []
        self.y = []
    
    @staticmethod
    def motion(event):
        x = event.xdata
        y = event.ydata
        plt.draw()
    
    def onclick(self, event):
        x = event.xdata
        y = event.ydata
        self.x.append(x)
        self.y.append(y)

        self.cur.set_data(x, y)
        self.ln.set_data(self.x,self.y)
        self.ax.set_title('x = {}, y = {}'.format(event.xdata, event.ydata))
        plt.draw()
    
       
fig, ax = plt.subplots()
img2silhouette = Img2silhouette(ax)
fig.canvas.mpl_connect('button_press_event', img2silhouette.onclick)
fig.canvas.mpl_connect('motion_notify_event', img2silhouette.motion)
plt.show()

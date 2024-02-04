import matplotlib.pyplot as plt
from matplotlib.widgets import Button, SpanSelector
import numpy as np

class ModeSwitcher:
    def __init__(self, ax, switch_callback):
        self.ax = ax
        self.switch_callback = switch_callback
        self.mode = 'select'

        self.button_ax = plt.axes([0.81, 0.01, 0.1, 0.05])
        self.button = Button(self.button_ax, 'Switch Mode')
        self.button.on_clicked(self.switch_mode)

        self.span_selector = SpanSelector(ax, self.onselect, 'horizontal', useblit=True)  # 透明度はここで指定
        self.span_selector.set_active(True)

    def onselect(self, xmin, xmax):
        if self.mode == 'select':
            print(f'Selected range: {xmin} to {xmax}')
        elif self.mode == 'delete':
            print(f'Delete points in range: {xmin} to {xmax}')

    def switch_mode(self, event):
        if self.mode == 'select':
            self.mode = 'delete'
            self.span_selector.set_active(False)
            self.span_selector.facecolor = 'blue'
            print('Switched to Delete Mode')
        elif self.mode == 'delete':
            self.mode = 'select'
            self.span_selector.set_active(True)
            self.span_selector.facecolor = 'red'
            print('Switched to Select Mode')

def main():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)

    mode_switcher = ModeSwitcher(ax, switch_callback=None)

    plt.show()

if __name__ == "__main__":
    main()


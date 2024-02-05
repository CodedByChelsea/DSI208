from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def get_color(index):
    colors = [(13, 71, 161),   # Red
              (100, 180, 246),  # Blue
              (30, 136, 229),   # Yellow
              (187, 222, 251),  # Indigo
              (21, 121, 192),   # Orange
              (227, 242, 253),  # Violet
              (33, 150, 241)]   # Green
    return colors[index % len(colors)]

class Renderer(Window):
    def __init__(self):
        super().__init__(950, 850, "Rainbow")
        self.batch = Batch()
        self.x = [7, 3, 5, 2, 6, 1, 4]
        self.colors = [get_color(i) for i in range(len(self.x))]
        self.circles = [Circle(100 + e*50, 200 + i*50, 30, color=color, batch=self.batch) for e, (i, color) in enumerate(zip(self.x, self.colors))]

    def on_update(self, deltatime):
        n = len(self.x)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.x[j] > self.x[j+1]:
                    self.x[j], self.x[j+1] = self.x[j+1], self.x[j]
                    self.colors[j], self.colors[j+1] = self.colors[j+1], self.colors[j]
                    self.circles = [Circle(100 + e*50, 200 + i*50, 30, color=color, batch=self.batch) for e, (i, color) in enumerate(zip(self.x, self.colors))]
                    return

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()







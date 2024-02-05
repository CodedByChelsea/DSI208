from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Line
from pyglet.graphics import Batch
from pyglet import clock

def merge_sort(arr, colors):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_colors = colors[:mid]
        right_colors = colors[mid:]

        merge_sort(left_half, left_colors)
        merge_sort(right_half, right_colors)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                colors[k] = left_colors[i]
                i += 1
            else:
                arr[k] = right_half[j]
                colors[k] = right_colors[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            colors[k] = left_colors[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            colors[k] = right_colors[j]
            j += 1
            k += 1

def get_color(index, colors):
    return colors[index]

class Renderer(Window):
    def __init__(self):
        super().__init__(950, 850, "Rainbow")
        self.batch = Batch()
        self.x = [7, 3, 5, 2, 6, 1, 4]
        self.colors = [(189, 178, 255), (253, 255, 182), (160, 196, 255), (255, 214, 165), (155, 246, 255), (255, 173, 173), (202, 255, 191)]
        self.lines = [Line(100 + e * 50, 200 + i * 50, 100 + (e + 1) * 100, 200 + i * 50, color=color, batch=self.batch, width=10) for e, (i, color) in enumerate(zip(self.x, self.colors))]
        self.sorting_complete = False

    def merge_sort_step(self):
        if len(self.x) > 1:
            merge_sort(self.x, self.colors)
            self.lines = [Line(100 + e * 50, 200 + i * 50, 100 + (e + 1) * 100, 200 + i * 50, color=get_color(e, self.colors), batch=self.batch, width=10) for e, i in enumerate(self.x)]

    def on_update(self, deltatime):
        if not self.sorting_complete:
            self.merge_sort_step()
            if len(set(self.x)) == len(self.x):
                self.sorting_complete = True
                clock.unschedule(self.on_update)

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()


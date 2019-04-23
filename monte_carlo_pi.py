from tkinter import Tk, Canvas, Label, IntVar, Entry, Button
from math import pi, sqrt
from random import randint


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        self.title('Monte Carlo Algorithm: Pi')

        self.width = 600
        self.height = 700

        self.x_center = self.winfo_screenwidth() / 2 - self.width / 2
        self.y_center = self.winfo_screenheight() / 2 - self.height / 2
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x_center, self.y_center))

        # Create canvas
        self.canvas_side = 500
        self.canvas = Canvas(self, width=self.canvas_side, height=self.canvas_side)
        self.canvas.configure(highlightthickness=0, borderwidth=0)

        # Set number of iterations
        self.number_of_iterations_box = Entry(self)
        self.number_of_iterations_box.insert(0, '1000')

        # Init points inside circle
        self.number_inside_circle = 0

        # Start button
        self.start_button = Button(self, text='Start', command=self.start)

        # Label for pi value
        # self.calculated_pi_value = IntVar()
        # self.calculated_pi_value.set(0)
        self.pi_label = Label(self, text='N/A')

        # Label for number of points
        # self.points_value = IntVar()
        # self.points_value.set(0)
        self.points_label = Label(self, text='N/A')

        # Label for accuracy of calculation
        self.accuracy_label = Label(self, text='N/A')

        # Pack UI
        self.init_ui()

    def init_ui(self):
        self.number_of_iterations_box.pack()
        self.start_button.pack()
        self.canvas.pack()
        self.pi_label.pack()
        self.points_label.pack()
        self.accuracy_label.pack()

        self.reset_canvas()

    def reset_canvas(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, 500, 500, fill='light gray', outline='')
        self.canvas.create_oval(0, 0, 500, 500, fill='hot pink', outline='')

    def start(self):
        for _ in range(int(self.number_of_iterations_box.get())):
            self.draw_point()

    def draw_point(self):
        x = randint(1, 499)
        y = randint(1, 499)
        self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='blue', outline='blue')
        self.in_circle(x, y)

    def in_circle(self, x, y):
        distance = sqrt((self.canvas_side / 2 - x) ** 2 + (self.canvas_side / 2 - y) ** 2)
        if distance <= self.canvas_side / 2:
            pass



if __name__ == '__main__':
    window = Main()
    window.mainloop()

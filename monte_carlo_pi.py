from math import pi, sqrt
from random import uniform
from tkinter import Tk, Canvas, Label, Entry, Button, Checkbutton, IntVar


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

        # Start button
        self.start_button = Button(self, text='Start', command=self.start)

        # Animate
        self.animate_var = IntVar()
        self.animate = Checkbutton(self, text='Animate', var=self.animate_var)
        
        self.animation_step = 3  # updates every x circles drawn

        # Init points inside circle
        self.number_inside_circle = 0

        # Init total points
        self.total_points = 0

        # Label for pi value
        self.pi_label = Label(self)

        # Label for number of points
        self.points_label = Label(self)

        # Label for accuracy of calculation
        self.error = '0%'
        self.error_label = Label(self)

        # Pack UI
        self.init_ui()

    def init_ui(self):
        self.number_of_iterations_box.pack()
        self.start_button.pack()
        self.animate.pack()
        self.canvas.pack()
        self.pi_label.pack()
        self.points_label.pack()
        self.error_label.pack()

        self.reset()

    def reset(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, 500, 500, fill='gray90', outline='')
        self.canvas.create_oval(0, 0, 500, 500, fill='orchid1', outline='')

        self.pi_label.configure(text='Approximate Pi:\n0')
        self.number_inside_circle = 0
        self.total_points = 0
        self.points_label.configure(text='Points:\n0/0')
        self.error_label.configure(text='Error:\n0%')

    def start(self):
        self.start_button.configure(state='disable')
        self.reset()
        for i in range(int(self.number_of_iterations_box.get())):
            self.draw_point(i)
        self.start_button.configure(state='normal')
        self.update_ui()

    def draw_point(self, i):
        x = uniform(.5, 499.5)
        y = uniform(.5, 499.5)
        self.canvas.create_oval(x - .5, y - .5, x + .5, y + .5, fill='blue', outline='')
        self.in_circle(x, y)
        if i % self.animation_step == 0 and self.animate_var.get():
            self.update_ui()

    def in_circle(self, x, y):
        distance = sqrt((self.canvas_side / 2 - x) ** 2 + (self.canvas_side / 2 - y) ** 2)
        if distance <= self.canvas_side / 2:
            self.number_inside_circle += 1
        self.total_points += 1

    def update_ui(self):
        calculated_pi = self.number_inside_circle / self.total_points * 4
        self.pi_label.configure(text=f'Approximate Pi:\n{calculated_pi:.4f}')
        self.points_label.configure(text=f'Points:\n{self.number_inside_circle}/{self.total_points}')
        self.error_label.configure(text=f'Error:\n{(abs(calculated_pi - pi) / pi * 100):.3f}%')
        self.canvas.update()


if __name__ == '__main__':
    window = Main()
    window.mainloop()

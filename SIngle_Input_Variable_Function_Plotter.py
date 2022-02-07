from tkinter import *
from ast import literal_eval
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class LeftFrame00(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="orange")
        self.master = master
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=S + N + E + W)
        self.label1 = Label(self, text="EXPRESSION", bg="yellow", relief="raised", padx=10, pady=10,
                            font=('Helvetica', 10, 'bold'))
        self.label1.grid(row=0, column=0, sticky=S+N+E+W)
        self.label2 = Label(self, text="Enter your expression in one variable(x) below:", bg="salmon", relief="raised",
                            padx=5, pady=5, font=('Helvetica', 10, 'bold'))
        self.label2.grid(row=1, column=0, sticky=S+N+E+W)
        self.textbox1 = Text(self, width=60, height=5, padx=10, pady=10, bd=8, relief="sunken",
                             font=('Helvetica', 10, 'bold'))
        self.textbox1.grid(row=2, column=0, sticky=S + N + E + W)
        self.grid_columnconfigure(0, weight=1)


class LeftFrame10(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="Navy")
        self.master = master
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=0, sticky=S + N + E + W)
        self.label1 = Label(self, text="VARIABLE RANGE", bg="LightBlue", relief="raised", padx=10, pady=10,
                            font=('Helvetica', 10, 'bold'))
        self.label1.grid(row=0, column=0, sticky=S+N+E+W)
        self.label2 = Label(self, text="Enter your variable's range in the form of (a,b) below:", bg="LightSteelBlue1",
                            relief="raised", padx=5, pady=5, font=('Helvetica', 10, 'bold'))
        self.label2.grid(row=1, column=0, sticky=S+N+E+W)
        self.textbox1 = Text(self, width=60, height=5, padx=10, pady=10, bd=8, relief="sunken",
                             font=('Helvetica', 10, 'bold'))
        self.textbox1.grid(row=2, column=0, sticky=S+N+E+W)
        self.grid_columnconfigure(0, weight=1)


class LeftFrame20(Frame):
    def __init__(self, master=None, right_frame=None):
        super().__init__(master, bg="Cyan")
        self.master = master
        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.grid(row=2, column=0, sticky=S + N + E + W)
        for j in range(5):
            self.grid_columnconfigure(j, weight=1)
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        self.evaluate_button = Button(self, text="Evaluate", command=right_frame.evaluate_expr, width=10, height=1,
                                      bd=4, padx=2, pady=2, relief="raised", font=('Helvetica', 11, 'bold'),
                                      bg="#00a108", fg="yellow")
        self.evaluate_button.grid(row=1, column=1, sticky="ew")
        self.exit_button = Button(self, text="Exit", command=exit, width=5, height=1, bd=4, padx=2, pady=2,
                                  relief="raised", font=('Helvetica', 11, 'bold'), bg="#ff0000", fg="black")
        self.exit_button.grid(row=1, column=3, sticky="ew")


class RightFrame(Frame):
    def __init__(self, master, left_frame1, left_frame2):
        super().__init__(master, bg="Black")
        self.master = master
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=5)
        self.left_frame1 = left_frame1
        self.left_frame2 = left_frame2
        self.grid(row=0, column=1, rowspan=3, sticky=S + N + E + W)
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(7):
            self.grid_columnconfigure(j, weight=1)
        self.label1 = Label(self, text="GRAPH", bg="white", relief="raised", padx=10, pady=10)
        self.label1.grid(row=0, column=0, columnspan=7, sticky=N+E+W)

    def evaluate_expr(self):
        expr = self.left_frame1.textbox1.get(1.0, END)
        expr = expr.strip('\n')
        variable_range = self.left_frame2.textbox1.get(1.0, END)
        v = literal_eval(variable_range)
        X = np.linspace(v[0], v[1], 1024)
        Y = [eval(expr) for x in X]
        fig = Figure(figsize=(5, 5))
        canvas = FigureCanvasTkAgg(fig, master=self)
        subplot = fig.add_subplot()
        subplot.plot(X, Y)
        subplot.set_xlabel("x values --->")
        subplot.set_ylabel("y = "+expr+" --->")
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=3, sticky=E + W + N + S)
        toolbar_frame = Frame(master=self)
        toolbar_frame.grid(row=7, column=3)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()


class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.geometry("1000x600")
        master.wm_title("Expression Graphing Calculator")
        self.left_frame1 = LeftFrame00(master)
        self.left_frame2 = LeftFrame10(master)
        self.right_frame = RightFrame(master, self.left_frame1, self.left_frame2)
        self.left_frame3 = LeftFrame20(master, self.right_frame)
        self.grid(row=0, column=0, sticky="nsew")


root = Tk()

app = Window(root)

root.mainloop()

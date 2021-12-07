from tkinter import *
from math import *
import math

is_pressed = True
pressed = True
pressed1 = True

def switch():
    global is_pressed

    if is_pressed:
        Scientific(root)
        is_pressed = False
    else:
        Standard(root)
        is_pressed = True

def color():
    global pressed
    global pressed1

    if pressed:
        pressed = False
        pressed1 = False
        Standard(root)
    else:
        pressed = True
        pressed1 = True
        Standard(root)

def color1():
    global pressed
    global pressed1

    if pressed1:
        pressed1 = False
        pressed = False
        Scientific(root)
    else:
        pressed1 = True
        pressed = True
        Scientific(root)

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

convert_constant = 1
inverse_convert_constant = 1

def SIN(arg):
    return sin(arg * convert_constant)


def COS(arg):
    return cos(arg * convert_constant)


def TAN(arg):
    return tan(arg * convert_constant)


def arcsin(arg):
    return inverse_convert_constant * (asin(arg))


def arccos(arg):
    return inverse_convert_constant * (acos(arg))


def arctan(arg):
    return inverse_convert_constant * (atan(arg))

root = Tk()

class Scientific:
    def __init__(self, master):
        clear_frame()
        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = StringVar()
        self.master = master
        self.color_change()

        root.title("Scientific Calculator")
        root.configure(bg=self.button_color, bd=10)
        button_params = {'bd':5, 'fg':self.text_color, 'bg':self.button_color, 'font':('sans-serif', 20, 'bold')}

        # row 0
        self.quit_btn = Button(root, button_params, text='X', command=lambda: root.destroy()).grid(row=0, column= 0, sticky="nsew")
        self.dark_mode = Button(root, button_params, text=self.mode, command = color1).grid(row=0, column= 2, sticky="nsew")
        self.standard = Button(root, button_params, text='Standard', command = switch).grid(row=0, column= 1, sticky="nsew")

        # row 1
        self.text_display = Entry(root, font=('sans-serif', 20, 'bold'), textvariable=self.text_input, width=70, bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(row=1, column= 0, columnspan=6, padx = 10, pady = 15)
        self.delete_one = Button(root, button_params, text='⌫', command=self.btn_clear1).grid(row=1, column=6, sticky="nsew")

        # row 2
        self.btn_Deg = Button(root, command=self.convert_deg)
        self.btn_Deg.grid(row=2, column=0, sticky="nsew")
        self.btn_Deg.configure(button_params, activeforeground='orange', text="Deg")
        self.btn_Rad = Button(root, command=self.convert_rad)
        self.btn_Rad.grid(row=2, column=1, sticky="nsew")
        self.btn_Rad.configure(button_params, foreground='orange', activeforeground='orange', text="Rad")
        self.btn_fact = Button(root, button_params, text="x!", command=lambda: self.btn_click('factorial(')).grid(row=2, column=2, sticky="nsew")
        self.btn_left_brack = Button(root, button_params, text="(", command=lambda: self.btn_click('(')).grid(row=2, column=3, sticky="nsew")
        self.btn_right_brack = Button(root, button_params, text=")", command=lambda: self.btn_click(')')).grid(row=2, column=4, sticky="nsew")
        self.btn_percent = Button(root, button_params, text="%", command=self.percent).grid(row=2, column=5, sticky="nsew")
        self.btn_clear = Button(root, button_params, text="C", command=self.btn_clear_all).grid(row=2, column=6, sticky="nsew")

        # row 3
        self.btn_sin = Button(root, button_params, text="sin", command=lambda: self.btn_click('SIN(')).grid(row=3, column=0, sticky="nsew")
        self.btn_cos = Button(root, button_params, text="cos", command=lambda: self.btn_click('COS(')).grid(row=3, column=1, sticky="nsew")
        self.btn_tan = Button(root, button_params, text="tan", command=lambda: self.btn_click('TAN(')).grid(row=3, column=2, sticky="nsew")
        self.btn_7 = Button(root, button_params, text="7", command=lambda: self.btn_click(7)).grid(row=3, column=3, sticky="nsew")
        self.btn_8 = Button(root, button_params, text="8", command=lambda: self.btn_click(8)).grid(row=3, column=4, sticky="nsew")
        self.btn_9 = Button(root, button_params, text="9", command=lambda: self.btn_click(9)).grid(row=3, column=5, sticky="nsew")
        self.btn_mult = Button(root, button_params, text="x", command=lambda: self.btn_click('*')).grid(row=3, column=6, sticky="nsew")

        # row 4
        self.btn_sqrt = Button(root, button_params, text="sqrt", command=lambda: self.btn_click('sqrt(')).grid(row=4, column=0, sticky="nsew")
        self.btn_log = Button(root, button_params, text="log", command=lambda: self.btn_click('log10(')).grid(row=4, column=1, sticky="nsew")
        self.btn_ln = Button(root, button_params, text="ln", command=lambda: self.btn_click('log(')).grid(row=4, column=2, sticky="nsew")
        self.btn_4 = Button(root, button_params, text="4", command=lambda: self.btn_click(4)).grid(row=4, column=3, sticky="nsew")
        self.btn_5 = Button(root, button_params, text="5", command=lambda: self.btn_click(5)).grid(row=4, column=4, sticky="nsew")
        self.btn_6 = Button(root, button_params, text="6", command=lambda: self.btn_click(6)).grid(row=4, column=5, sticky="nsew")
        self.btn_div = Button(root, button_params, text="÷", command=lambda: self.btn_click('/')).grid(row=4, column=6, sticky="nsew")

        # row 5
        # self.btn_sin_inverse = Button(root, button_params, text=u"sin-\u00B9", command=lambda: self.btn_click('arcsin(')).grid(row=5, column=0, sticky="nsew")
        # self.btn_cos_inverse = Button(root, button_params, text=u"cos-\u00B9", command=lambda: self.btn_click('arccos(')).grid(row=5, column=1, sticky="nsew")
        # self.btn_tan_inverse = Button(root, button_params, text=u"tan-\u00B9", command=lambda: self.btn_click('arctan(')).grid(row=5, column=2, sticky="nsew")
        self.eulers_num = Button(root, button_params, text='e', command=lambda: self.btn_click('e')).grid(row=5, column=0, sticky="nsew")
        self.btn_pi = Button(root, button_params, text="π", command=lambda: self.btn_click('pi')).grid(row=5, column=1, sticky="nsew")
        self.btn_power = Button(root, button_params, text="x\u207f", command=lambda: self.btn_click('**')).grid(row=5, column=2, sticky="nsew")
        self.btn_1 = Button(root, button_params, text="1", command=lambda: self.btn_click(1)).grid(row=5, column=3, sticky="nsew")
        self.btn_2 = Button(root, button_params, text="2", command=lambda: self.btn_click(2)).grid(row=5, column=4, sticky="nsew")
        self.btn_3 = Button(root, button_params, text="3", command=lambda: self.btn_click(3)).grid(row=5, column=5, sticky="nsew")
        self.btn_add = Button(root, button_params, text="+", command=lambda: self.btn_click('+')).grid(row=5, column=6, sticky="nsew")

        # row 6
        # self.btn_sqr = Button(root, button_params, text=u"x\u00B2", command=lambda: self.btn_click('**2')).grid(row=6, column=1, sticky="nsew")
        self.btn_ans = Button(root, button_params, text="Ans", command=self.answer).grid(row=6, column=0, sticky="nsew")
        self.btn_exp = Button(root, button_params, text="EXP", command=lambda: self.btn_click('*10**')).grid(row=6, column=1, sticky="nsew")
        self.btn_signs = Button(root, button_params, text='\u00B1', command=self.change_signs).grid(row=6, column=2, sticky="nsew")
        self.btn_0 = Button(root, button_params, text="0", command=lambda: self.btn_click(0)).grid(row=6, column=3, sticky="nsew")
        self.btn_dec = Button(root, button_params, text=".", command=lambda: self.btn_click('.')).grid(row=6, column=4, sticky="nsew")
        self.btn_eq = Button(root, button_params, text="=", command=self.btn_equal).grid(row=6, column=5, sticky="nsew")
        self.btnSub = Button(root, button_params, text="-", command=lambda: self.btn_click('-')).grid(row=6, column=6, sticky="nsew")


    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        if self.expression[0]=='-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        self.text_input.set(self.expression)

    def percent(self):
        self.expression = str(eval(self.expression+'/100'))
        self.text_input.set(self.expression)

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    def color_change(self):
        if pressed1 == True:
            self.button_color='White'
            self.text_color='Black'
            self.mode='Dark Mode'
        elif pressed1 == False:
            self.button_color='Black'
            self.text_color='White'
            self.mode='Light Mode'

    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        button_params = {'bd':5, 'fg':self.text_color, 'bg':self.button_color, 'font':('sans-serif', 20, 'bold')}
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = self.text_color
        self.btn_Deg["foreground"] = 'orange'

    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'orange'
        self.btn_Deg["foreground"] = self.text_color

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


class Standard:
    def __init__(self, master):
        clear_frame()
        self.expression = ""
        self.sum_up = ""
        self.text_input = StringVar()
        self.master = master

        if pressed == True:
            button_color='White'
            text_color='Black'
            mode='Dark Mode'
        elif pressed == False:
            button_color='Black'
            text_color='White'
            mode='Light Mode'

        root.title("Standard Calculator")
        root.configure(bg=button_color, bd=10)
        button_params = {'bd':5, 'fg':text_color, 'bg':button_color, 'font':('sans-serif', 20, 'bold')}

        # row 0
        self.quit_btn = Button(root, button_params, text='X', command=lambda: root.destroy()).grid(row=0, column= 0, sticky="nsew")
        self.dark_mode = Button(root, button_params, text=mode, command = color).grid(row=0, column= 2, sticky="nsew")
        self.scientific = Button(root, button_params, text='Scientific', command = switch).grid(row=0, column= 1, sticky="nsew")

        # row 1
        self.text_display = Entry(root, font=('sans-serif', 20, 'bold'), textvariable=self.text_input, width=40, bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(row=1, column= 0, columnspan=5, padx = 10, pady = 15)

        # row 2
        self.btn_7 = Button(root, button_params, text="7", command=lambda: self.btn_click(7)).grid(row=2, column=0, sticky="nsew")
        self.btn_8 = Button(root, button_params, text="8", command=lambda: self.btn_click(8)).grid(row=2, column=1, sticky="nsew")
        self.btn_9 = Button(root, button_params, text="9", command=lambda: self.btn_click(9)).grid(row=2, column=2, sticky="nsew")
        self.btn_clear = Button(root, button_params, text="C", command=self.btn_clear_all).grid(row=2, column=3, sticky="nsew")
        self.delete_one = Button(root, button_params, text='⌫', command=self.btn_clear1).grid(row=2, column=4, sticky="nsew")

        # row 3
        self.btn_4 = Button(root, button_params, text="4", command=lambda: self.btn_click(4)).grid(row=3, column=0, sticky="nsew")
        self.btn_5 = Button(root, button_params, text="5", command=lambda: self.btn_click(5)).grid(row=3, column=1, sticky="nsew")
        self.btn_6 = Button(root, button_params, text="6", command=lambda: self.btn_click(6)).grid(row=3, column=2, sticky="nsew")
        self.btn_mult = Button(root, button_params, text="x", command=lambda: self.btn_click('*')).grid(row=3, column=3, sticky="nsew")
        self.btn_div = Button(root, button_params, text="÷", command=lambda: self.btn_click('/')).grid(row=3, column=4, sticky="nsew")

        # row 4
        self.btn_1 = Button(root, button_params, text="1", command=lambda: self.btn_click(1)).grid(row=4, column=0, sticky="nsew")
        self.btn_2 = Button(root, button_params, text="2", command=lambda: self.btn_click(2)).grid(row=4, column=1, sticky="nsew")
        self.btn_3 = Button(root, button_params, text="3", command=lambda: self.btn_click(3)).grid(row=4, column=2, sticky="nsew")
        self.btn_add = Button(root, button_params, text="+", command=lambda: self.btn_click('+')).grid(row=4, column=3, sticky="nsew")
        self.btnSub = Button(root, button_params, text="-", command=lambda: self.btn_click('-')).grid(row=4, column=4, sticky="nsew")

        # row 5
        self.btn_0 = Button(root, button_params, text="0", command=lambda: self.btn_click(0)).grid(row=5, column=0, sticky="nsew")
        self.btn_dec = Button(root, button_params, text=".", command=lambda: self.btn_click('.')).grid(row=5, column=1, sticky="nsew")
        self.btn_signs = Button(root, button_params, text='\u00B1', command=self.change_signs).grid(row=5, column=2, sticky="nsew")
        self.btn_eq = Button(root, button_params, text="=", command=self.btn_equal).grid(row=5, column=3, columnspan=2, sticky="nsew")


    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        if self.expression[0]=='-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        self.text_input.set(self.expression)

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


Standard(root)
root.mainloop()

from tkinter import *
import ast

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.display = Entry(root)
        self.display.grid(row=1, columnspan=6)
        self.root.geometry('142x180')
        self.i = 0
        self.create_buttons()

    def get_num(self, num):
        self.display.insert(self.i, num)
        self.i += 1

    def get_op(self, opp):
        if opp == '<-':
            self.undo()
            self.i -= 1
            return
        length_opp = len(opp)
        self.display.insert(self.i, opp)
        self.i += length_opp

    def clear(self):
        self.display.delete(0, END)

    def undo(self):
        current_text = self.display.get()
        if len(current_text):
            self.display.delete(len(current_text) - 1, END)

    def calculate(self):
        cal_string = self.display.get()
        try:
            node = ast.parse(cal_string, mode='eval')
            result = eval(compile(node, '<string>', 'eval'))
            self.clear()
            self.display.insert(0, result)
        except Exception as error:
            self.clear()
            print(error)
            self.display.insert(0, 'Error')

    def create_buttons(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter = 0
        for x in range(3):
            for y in range(3):
                button_text = numbers[counter]
                Button(self.root, text=button_text, width=2, height=2, 
                       command=lambda text=button_text: self.get_num(text)).grid(row=x + 2, column=y)
                counter += 1
        Button(self.root, text="0", width=2, height=2, 
               command=lambda: self.get_num('0')).grid(row=5, column=1)

        operations = ['<-', '(', ')', '+', '-', '*', '/', '%', '**2']
        count = 0
        for x in range(4):
            for y in range(3):
                if count < len(operations):
                    button_text = operations[count]
                    Button(self.root, text=button_text, width=2, height=2, 
                           command=lambda text=button_text: self.get_op(text)).grid(row=x + 2, column=y + 3)
                    count += 1

        Button(self.root, text="=", width=2, height=2, 
               command=self.calculate).grid(row=5, column=2)
        Button(self.root, text="AC", width=2, height=2, 
               command=self.clear).grid(row=5, column=0)


if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello,World')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


if __name__ == '__main__':
    app = Application()
    app.master.title('Hello, world')
    app.mainloop()
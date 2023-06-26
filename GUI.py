import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Loft Readout")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
		root.attributes('-fullscreen', True)
        root.resizable(width=False, height=False)

        GMessage_287=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_287["font"] = ft
        GMessage_287["fg"] = "#333333"
        GMessage_287["justify"] = "center"
        GMessage_287["text"] = "Info"
        GMessage_287.place(x=170,y=310,width=232,height=112)

        GLabel_362=tk.Label(root)
        ft = tkFont.Font(family='Times',size=40)
        GLabel_362["font"] = ft
        GLabel_362["fg"] = "#333333"
        GLabel_362["justify"] = "center"
        GLabel_362["text"] = "VRS:"
        GLabel_362.place(x=90,y=180,width=70,height=25)

        GLabel_924=tk.Label(root)
        ft = tkFont.Font(family='Times',size=40)
        GLabel_924["font"] = ft
        GLabel_924["fg"] = "#333333"
        GLabel_924["justify"] = "center"
        GLabel_924["text"] = "False"
        GLabel_924.place(x=370,y=180,width=70,height=25)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

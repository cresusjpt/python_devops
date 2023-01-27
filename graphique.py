from tkinter import Tk, Scrollbar, Canvas
root = Tk()
canvas = Canvas(root, background="white",
                             scrollregion=(0, 0, 1070, 400),
                             width=400, height=400)
scroll = Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.config(xscrollcommand=scroll.set)
canvas.create_rectangle((10,10),(60,60), fill="blue")
canvas.create_rectangle((1010,10),(1060,60), fill="blue")
root.columnconfigure(1, weight=1)
canvas.grid(sticky="ew", column=1)
scroll.grid(sticky="ew", column=1)
root.mainloop()
from tkinter import Tk, Label, Entry, Button


class MyWindow(Tk):
	def __init__(self, title, size):
		super().__init__()
		self.title(title)
		self.geometry(size)
		self.config(bg='#A1B9CF')


class MyLabel(Label):
	def __init__(self, master, text, width=20, padx=30):
		super().__init__(
			master, text=text, bg='#A1B9CF', fg='#005485',
			padx=padx, pady=20, width=width, anchor='w',
			font='roboto'
		)


class MyEntry(Entry):
	def __init__(self, master):
		super().__init__(
			master,
			width=20, bg='#A1B9CF', fg='#005485', bd=1, border=0,
			highlightcolor='#005485', selectbackground='#005485',
			font='roboto'
		)


class MyButton(Button):
	def __init__(self, master, label, on_click):
		super().__init__(
			master, text=label, width=20,
			bg='#A1B9CF', bd=0, border=0, fg='#005485', highlightcolor='#005485',
			font='roboto', command=on_click
		)


class MyDialog:
	def __init__(self, title, message, size='300x300'):
		self.master = MyWindow(title, size)

		MyLabel(self.master, message, 120, 10).pack(side='top', pady=30)
		MyButton(self.master, 'OK', lambda: self.master.destroy()).pack(side='bottom', pady=10)

	def show(self):
		self.master.mainloop()

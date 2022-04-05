from tkinter import StringVar, OptionMenu

from src.repository import Repository
from src.faculty import Employee, Teacher, Student
from src.search_page import SearchPage
from src.widgets import MyDialog, MyLabel, MyWindow, MyButton, MyEntry


class EntryPage:

	def __init__(self):
		master = MyWindow('Faculty', '800x400')

		label_text = ['NID', 'Name', 'Birth Date', 'Employee Degree', 'Employee Department']
		menu_options = ['Employee', 'Teacher', 'Student']
		labels = []

		menu_variable = StringVar(master)
		menu_variable.set(menu_options[0])

		def dropdown_menu_command(value):
			if value == menu_options[0]:
				labels[3].config(text='Employee Degree')
				labels[4].config(text='Employee Department')
			elif value == menu_options[1]:
				labels[3].config(text='Teacher Degree')
				labels[4].config(text='Teacher Department')
			elif value == menu_options[2]:
				labels[3].config(text='Student Number')
				labels[4].config(text='Student Department')

		entries = []
		for i in range(5):
			labels.append(MyLabel(master, label_text[i]))
			labels[i].grid(row=i, column=0)

			entries.append(MyEntry(master))
			entries[i].grid(row=i, column=1)
			master.update_idletasks()

		dropdown_menu = OptionMenu(
			master, menu_variable, menu_options[0], menu_options[1], menu_options[2], command=dropdown_menu_command
		)
		dropdown_menu.grid(row=2, column=2, padx=70, pady=30)
		dropdown_menu.config(
			width=20,
			bg='#A1B9CF', bd=0, border=0, fg='#005485', highlightcolor='#005485',
			font='roboto'
		)

		def btn_click():
			repo = Repository()
			try:
				if menu_variable.get() == menu_options[0]:
					repo.add_employee(
						Employee(
							entries[0].get(), entries[1].get(), entries[2].get(),
							entries[3].get(), entries[4].get()
						)
					)
				elif menu_variable.get() == menu_options[1]:
					repo.add_teacher(
						Teacher(
							entries[0].get(), entries[1].get(), entries[2].get(),
							entries[3].get(), entries[4].get()
						)
					)
				elif menu_variable.get() == menu_options[2]:
					repo.add_student(
						Student(
							entries[0].get(), entries[1].get(), entries[2].get(),
							entries[3].get(), entries[4].get()
						)
					)
			except Exception as e:
				MyDialog(title='Error', message=e).show()
			else:
				MyDialog(title='Success', message='Operation success').show()

		add_button = MyButton(master, 'Add New', btn_click)
		add_button.grid(row=3, column=2, padx=70, pady=30)

		go_to_search_page_button = MyButton(master, 'Go to search page', lambda: SearchPage())
		go_to_search_page_button.grid(row=4, column=2, padx=70, pady=30)

		master.mainloop()

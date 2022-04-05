from src.repository import Repository
from src.widgets import MyLabel, MyButton, MyEntry, MyWindow, MyDialog


class SearchPage:

	def __init__(self):
		self.master = MyWindow('Search Page', '500x200')

		MyLabel(self.master, 'Enter NID').grid(row=0, column=0, pady=10)
		self.search_box = MyEntry(self.master)
		self.search_box.grid(row=0, column=1, pady=10)
		MyButton(self.master, 'Search', self.on_search_click).grid(row=1, columnspan=2, pady=10)

		back_button = MyButton(self.master, 'Go Back', lambda: self.master.withdraw())
		back_button.grid(row=2, columnspan=2)

		self.master.mainloop()

	def on_search_click(self):
		repo = Repository()
		try:
			row = tuple(repo.get_object(int(self.search_box.get())).fetchone())
			t = row[5]
			attrib1 = 'attrib1'
			attrib2 = 'attrib2'
			if t == 'Employee':
				attrib1 = 'Employee Degree'
				attrib2 = 'Employee Department'
			elif t == 'Teacher':
				attrib1 = 'Teacher Degree'
				attrib2 = 'Teacher Department'
			elif t == 'Student':
				attrib1 = 'Student Number'
				attrib2 = 'Student Department'

			res = f'NID: {row[0]}\nName: {row[1]}\nBirth Date: {row[2]}\n{attrib1}: {row[3]}\n{attrib2}: {row[4]}\nType: {row[5]}'
			master = MyWindow('Search Result', '500x300')

			label = MyLabel(master, res)
			label.config(anchor='w', width=200, justify='left')
			label.pack(side='top', pady=10)
			MyButton(master, 'OK', lambda: master.destroy()).pack(side='bottom', pady=30)

		except Exception as e:
			print(e)
			MyDialog('No Result', 'No Results Found!', '300x200').show()

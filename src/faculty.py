class Person:
	def __init__(self, nid, name, birth_date):
		self._name = name
		self._birth_date = birth_date
		self._nid = nid

	def get_name(self):
		return self._name

	def get_birth_date(self):
		return self._birth_date

	def get_nid(self):
		return self._nid


class Employee(Person):
	def __init__(self, nid, name, birth_date, emp_degree, emp_department):
		super().__init__(nid, name, birth_date)
		self._emp_degree = emp_degree
		self._emp_department = emp_department

	def get_degree(self):
		return self._emp_degree

	def get_department(self):
		return self._emp_department


class Teacher(Person):
	def __init__(self, nid, name, birth_date, tet_degree, tet_department):
		super().__init__(nid, name, birth_date)
		self._tet_degree = tet_degree
		self._tet_department = tet_department

	def get_degree(self):
		return self._tet_degree

	def get_department(self):
		return self._tet_department


class Student(Person):
	def __init__(self, nid, name, birth_date, std_number, std_department):
		super().__init__(nid, name, birth_date)
		self._std_number = std_number
		self._std_department = std_department

	def get_number(self):
		return self._std_number

	def get_department(self):
		return self._std_department

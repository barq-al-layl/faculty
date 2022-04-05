import sqlite3
from sqlite3 import Cursor

from src.faculty import Employee, Teacher, Student


class Repository:

	def __init__(self):
		self.__connection = sqlite3.connect('../data/faculty.sqlite')

	def __del__(self):
		self.__connection.close()

	def add_employee(self, e: Employee):
		sql = f"INSERT INTO people VALUES ({e.get_nid()}, '{e.get_name()}', '{e.get_birth_date()}', '{e.get_degree()}', '{e.get_department()}', 'Employee')"
		self.__connection.execute(sql)
		self.__connection.commit()

	def add_teacher(self, t: Teacher):
		sql = f"INSERT INTO people VALUES ({t.get_nid()}, '{t.get_name()}', '{t.get_birth_date()}', '{t.get_degree()}', '{t.get_department()}', 'Teacher')"
		self.__connection.execute(sql)
		self.__connection.commit()

	def add_student(self, s: Student):
		sql = f"INSERT INTO people VALUES ({s.get_nid()}, '{s.get_name()}', '{s.get_birth_date()}', '{s.get_number()}', '{s.get_department()}', 'Student')"
		self.__connection.execute(sql)
		self.__connection.commit()

	def get_object(self, nid: int) -> Cursor:
		sql = f"SELECT * FROM people WHERE nid = {nid}"
		cur = self.__connection.cursor()
		cur.execute(sql)
		return cur

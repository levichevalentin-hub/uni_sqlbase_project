from datetime import datetime
import json
from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, Date, select
from sqlalchemy.orm import sessionmaker

from sql_engine import display_table, load_table

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "..")
sys.path.append(project_root)

from database.tables.student import Student
from database.tables.base import Base

class Student_in_class(Base):
    __tablename__ = "Student_in_class"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Student_in_class (id = {self.id}, class_id = {self.class_id}, student_id = {self.student_id}, teacher_idteacher_id = {self.teacher_id})"

# class Class(Base):
#     __tablename__ = "Class"

#     id = Column(Integer, primary_key=True)
#     class_name = Column(String, nullabe=False)
#     teacher_id = Column(Integer, nullable=False)
#     student_id = Column(Integer, nullable=False)
    

#     def __repr__(self):
#         return f"Class (id = {self.id},class_name = {self.class_name}, teacher_id = {self.teacher_id}, student_id = {self.student_id})"
    
class Grade_in_class(Base):
    __tablename__ = "Grade_in_class"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)
    grade_value = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)

    def __repr__(self):
        return f"Grade_in_class (id = {self.id}, class_id = {self.class_id}, student_id = {self.student_id}, teacher_id = {self.teacher_id}, grade = {self.grade}, created_at = {self.created_at})"
    
class Subject(Base):

    __tablename__ = "Subject"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, nullable=False)
    subject_name = Column(String, nullable=False)
    

    def __repr__(self):
        return f"Subject (id = {self.id}, teacher_id = {self.teacher_id}, subject_name = {self.subject_name})"

# TODO: Properly connect database
engine = create_engine("sqlite:///Project11.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

load_table(session, "data/students.json", Student, datetime_fields=['birthday'])
display_table(session, Student)

#teacherBen = session.query(Teacher).filter(Teacher.first_name.ilike("Ben")).all()
#print(teacherBen)

# NOTE: So far we have enough tables for initial setup. Let's proceed with business logic, afterwards we will add corresponding tables by necessity.

# TODO: The main idea is to create a basic foundation for our next features. Therefore we need to know how to connect with database, load data, display data.
# We will have linked models:
# 1. Database model: class Teacher(Base) as real database value.
# 2. JSON Model (teachers.json) as intial data for first setup.
# So we need to load JSON into SQL database, that is the first step!

# TODO: Create an initial program in this file with following functionality:
#  1. Init database connection,
#  2. Load all tables (one-by-one) into session via load_table, e.g. load_table("../data/teachers.json", Teaacher), load_table("../data/students.json", Student),
#  3. Display data from the tables.
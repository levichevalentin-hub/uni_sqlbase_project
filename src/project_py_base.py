import json
from pathlib import Path

from sqlalchemy import func, create_engine, Column, Integer, String, Date, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass

class Teacher(Base):
    __tablename__ = "Teacher"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    jmbg = Column(Integer, nullable=False)
    adress = Column(String, nullable=False)
    subject = Column(String, nullable = False)

    def __repr__(self):
        return f"Teacher (id = {self.id}, first_name = {self.first_name}, second_name = {self.second_name}, birthday = {self.birthday},  jmbg = {self.jmbg}, adress = {self.adress}, subject = {self.subject})"

class Student(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    jmbg = Column(Integer, nullable=False)
    adress = Column(String, nullable=False)
    index_number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Student (id = {self.id}, first_name = {self.first_name}, second_name = {self.second_name}, birthday = {self.birthday},  jmbg = {self.jmbg}, adress = {self.adress}, index_number = {self.index_number})"
    
class Student_in_class(Base):
    __tablename__ = "Student_in_class"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Student_in_class (id = {self.id}, class_id = {self.class_id}, student_id = {self.student_id}, teacher_idteacher_id = {self.teacher_id})"

class Class(Base):
    __tablename__ = "Class"

    id = Column(Integer, primary_key=True)
    class_name = Column(String, nullabe=False)
    teacher_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    

    def __repr__(self):
        return f"Class (id = {self.id},class_name = {self.class_name}, teacher_id = {self.teacher_id}, student_id = {self.student_id})"
    
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
engine = create_engine("sqlite:///Project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def load_table(file_path, model_class):
    try:
        # TODO: Write code for loaing 1 table, use session. Be careful with Date, issues may happen
        print(f"Data for {model_class.__tablename__} has been successfully loaded.")
    except Exception as ex:
        print(f"Error encountered during loading {model_class.__tablename__} data!")

def display_table(model_class):
    # TODO: display data from a specific table, model_class = table, e.g. Teacher

#adding like smth

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

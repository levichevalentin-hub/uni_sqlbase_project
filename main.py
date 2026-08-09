from datetime import datetime
import json
from pathlib import Path


from sqlalchemy import create_engine, Column, Integer, String, Date, select
from sqlalchemy.orm import sessionmaker


from database.sql_engine import display_table, load_table

from database.tables.school_class import SchoolClass

from database.tables.student import Student
from database.tables.teacher import Teacher

from database.tables.subject import Subject
from database.tables.grade_in_class import GradeInClass
from database.tables.student_in_class import StudInClass


# TODO: Properly connect database
engine = create_engine("sqlite:///UNI_SQL3.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


#region

load_table(session, "data/students.json", Student, datetime_fields=['birthday'])
display_table(session, Student)

load_table(session, "data/school_classes.json", SchoolClass)
display_table(session, SchoolClass)

load_table(session, "data/subjects.json", Subject)
display_table(session, Subject)

load_table(session, "data/students_in_classes.json", StudInClass)
display_table(session, StudInClass)

load_table(session, "data/teachers.json", Teacher, datetime_fields=['birthday'])
display_table(session, Teacher)

load_table(session, "data/grades_in_classes.json", GradeInClass, datetime_fields=['created_at'])
display_table(session, GradeInClass)

#endregion





#teacherBen = session.query(Teacher).filter(Teacher.first_name.ilike("Ben")).all()
#print(teacherBen)
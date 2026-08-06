from datetime import datetime
import json
from pathlib import Path


from sqlalchemy import create_engine, Column, Integer, String, Date, select
from sqlalchemy.orm import sessionmaker


from src.sql_engine import display_table, load_table

from database.tables.school_class import SchoolClass

from database.tables.student import Student
from database.tables.teacher import Teacher

from database.tables.subject import Subject
from database.tables.grade_in_class import GradeInClass
from database.tables.student_in_class import StudInClass


# TODO: Properly connect database
engine = create_engine("sqlite:///UNI_SQL1.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


#region

load_table(session, "data/school_classes.json", SchoolClass)
display_table(session, SchoolClass)

# load_table(session, "data/subject.json", Subject, datetime_fields=['birthday'])
# display_table(session, Subject)

# load_table(session, "data/class.json", Class, datetime_fields=['birthday'])
# display_table(session, Class)

# load_table(session, "data/student_in_class.json", StudInClass, datetime_fields=['birthday'])
# display_table(session, StudInClass)

# load_table(session, "data/teachers.json", Teacher, datetime_fields=['birthday'])
# display_table(session, Teacher)

#endregion





#teacherBen = session.query(Teacher).filter(Teacher.first_name.ilike("Ben")).all()
#print(teacherBen)
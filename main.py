from database.sql_engine import create_session, creeate_tables, display_table, load_table

from database.tables.school_class import SchoolClass
from database.tables.student import Student
from database.tables.teacher import Teacher
from database.tables.subject import Subject
from database.tables.grade_in_class import GradeInClass
from database.tables.student_in_class import StudInClass

session = create_session("sqlite:///UNI_SQL5.db")
creeate_tables(session)




#teacherBen = session.query(Teacher).filter(Teacher.first_name.ilike("Ben")).all()
#print(teacherBen)
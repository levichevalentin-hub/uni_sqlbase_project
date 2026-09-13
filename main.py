from database.sql_engine import create_session, creeate_tables, display_table, insert_into_table, load_table

from database.tables.school_class import SchoolClass
from database.tables.student import Student
from database.tables.teacher import Teacher
from database.tables.subject import Subject
from database.tables.grade_in_class import GradeInClass
from database.tables.student_in_class import StudInClass
from database.tables.auth import Auth

print("--------------------------------------------------------------")

session = create_session("sqlite:///UNI_SQL6.db", drop_previous_db=True)
creeate_tables(session)

print("--------------------------------------------------------------")

# Раскомметируй если хочешь посмотреть тестовые данные по учителю Бену
# В том числе можно использовать фильтры, например ilike для поиска по имени без учета регистра
# И можно использовать другие данные, например студентов, классов, предметов и т.д. в зависимости от того, что тебе нужно проверить
# teacherBen = session.query(Teacher).filter(Teacher.first_name.ilike("Ben")).all()
# print(teacherBen)

print("--------------------------------------------------------------")

# 1
insert_into_table(session, Auth, {
    "external_id": 1,
    "entity_type": "student",
    "username": "vasilii",
    "password": "1",
    "role": "user"
})

# 2
insert_into_table(session, Auth, {
    "external_id": 3,
    "entity_type": "student",
    "username": "alex",
    "password": "pass#123!",
    "role": "user"
})

# 3
insert_into_table(session, Auth, {
    "external_id": 1,
    "entity_type": "teacher",
    "username": "admin",
    "password": "admin123",
    "role": "admin"
})

# 4
insert_into_table(session, Auth, {
    "external_id": 2,
    "entity_type": "teacher",
    "username": "admin2",
    "password": "2",
    "role": "admin"
})

# Нужно создать три функции:

# 1. Фукнкция add_default_auth_student которая будет добавлять в таблицу auth запись с ролью user и entity_type student.
# Эта функция будет внутри себя вызывать insert_into_table, но при этом не нужно будет передавать role и entity_type, так как они будут по умолчанию user и student.
# Пример вызова функции: add_default_auth_student(session, external_id=1, username="new_user", password="new_pass").
# insert_into_table #1, #2 нужно переделать в add_default_auth_student.

# 2. Функция add_default_auth_teacher которая будет добавлять в таблицу auth запись с ролью admin и entity_type teacher.
# Эта функция будет внутри себя вызывать insert_into_table, но при этом не нужно будет передавать role и entity_type, так как они будут по умолчанию admin и teacher.
# Пример вызова функции: add_default_auth_teacher(session, external_id=2, username="new_teacher", password="new_pass").
# insert_into_table #3, #4 нужно переделать в add_default_auth_teacher.

# 3 Функция get_auth_by_username_and_password которая будет возвращать запись из таблицы auth по username и password.
# Пример вызова функции: get_auth_by_username_and_password(session, username="new_user", password="new_pass").

# Нужно покаать, что функции работают, для этого нужно вызвать их и вывести результат в консоль.

print("--------------------------------------------------------------")
from datetime import datetime
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.tables.school_class import SchoolClass
from database.tables.student import Student
from database.tables.teacher import Teacher
from database.tables.subject import Subject
from database.tables.grade_in_class import GradeInClass
from database.tables.student_in_class import StudInClass

from database.tables.base import Base

def create_session(name="UNI_SQL.db", drop_previous_db=False):
    engine = create_engine(name)
    if drop_previous_db:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()

def creeate_tables(session):
    # Load data from JSON files into the database
    load_table(session, "data/students.json", Student, datetime_fields=['birthday'])
    load_table(session, "data/school_classes.json", SchoolClass)
    load_table(session, "data/subjects.json", Subject)
    load_table(session, "data/students_in_classes.json", StudInClass)
    load_table(session, "data/teachers.json", Teacher, datetime_fields=['birthday'])
    load_table(session, "data/grades_in_classes.json", GradeInClass, datetime_fields=['created_at'])

def load_table(session, file_path, model_class, datetime_fields=[]):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            
            if isinstance(data, list):
                for item in data:
                    for field in datetime_fields:
                        if field in item and isinstance(item[field], str):
                            item[field] = datetime.strptime(item[field], "%Y-%m-%d").date()
                            
                    record = model_class(**item)
                    session.add(record)
                
                session.commit()
                print(f"Data for {model_class.__tablename__} has been successfully loaded.")
            else:
                print(f"Error: JSON file format is incorrect. Expected a list of objects.")
    except Exception as ex:
        print(f"Error encountered during loading {model_class.__tablename__} data: {ex}")

def display_table(session, model_class):
    try:
        records = session.query(model_class).all()
        
        print(f"\n--- Table: {model_class.__tablename__} ({len(records)} records) ---")
        
        if not records:
            print("Table is empty.")
            return

        for record in records:
            print(record)
            
    except Exception as ex:
        print(f"Error displaying {model_class.__tablename__} data! Details: {ex}")

def insert_into_table(session, model_class, data):
    try:
        record = model_class(**data) # Вот здесь конвертируем data в объект модели для базы данных
        session.add(record)  # Вставка сконвертированной записи в сессию, т.е. в базу данных

        session.commit() # подтверждение изменений в базе данных
        print(f"Data successfully inserted into {model_class.__tablename__}.")
    except Exception as ex:
        session.rollback() # откат изменений в случае ошибки
        print(f"Error inserting data into {model_class.__tablename__}! Details: {ex}")


# Создай функцию для поиска в SQL базе данных человека по
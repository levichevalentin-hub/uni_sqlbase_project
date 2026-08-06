from datetime import datetime
import json
from pathlib import Path

from sqlalchemy import UniqueConstraint, func, create_engine, Column, Integer, String, Date, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker

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
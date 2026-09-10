from sqlalchemy import UniqueConstraint, Column, Integer, String, Date

from database.tables.base import Base

class Teacher(Base):
    __tablename__ = "Teacher"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    jmbg = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    subject = Column(String, nullable = False)

    __table_args__ = (
        UniqueConstraint(
            'first_name', 
            'second_name', 
            'birthday', 
            name='uq_teacher_full_name_birthday'  # Имя индекса в базе данных
        ),
    )

    def __repr__(self):
        return f"Teacher (id = {self.id}, first_name = {self.first_name}, second_name = {self.second_name}, birthday = {self.birthday},  jmbg = {self.jmbg}, address = {self.address}, subject = {self.subject})"

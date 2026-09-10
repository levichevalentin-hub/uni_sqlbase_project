from sqlalchemy import UniqueConstraint, Column, Integer, String

from database.tables.base import Base

class SchoolClass(Base):
    __tablename__ = "SchoolClass"

    id = Column(Integer, primary_key=True)
    class_name = Column(String, nullable=False)
    teacher_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'teacher_id', 
            'student_id', 
            'class_name', 
            name='uq_class_teach_stud_id'
        ),
    )   

    def __repr__(self):
        return f"Class (id = {self.id},class_name = {self.class_name}, teacher_id = {self.teacher_id}, student_id = {self.student_id})"
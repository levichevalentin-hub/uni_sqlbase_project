from sqlalchemy import UniqueConstraint, Column, Integer, Date, DeclarativeBase

class GradeInClass(Base):
    __tablename__ = "GradeInClass"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    teacher_id = Column(Integer, nullable=False)
    grade_value = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'student_id', 
            'teacher_id',
            'grade_value',
            'created_at',
            name='uq_grade_id_value_date'
        ),
    )

    def __repr__(self):
        return f"GradeInClass(id={self.id}, class_id={self.class_id}, student_id={self.student_id}, teacher_id={self.teacher_id},grade_value={self.grade_value}, created_at={self.created_at})"
    
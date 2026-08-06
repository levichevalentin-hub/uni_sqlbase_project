from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, DeclarativeBase

class StudInClass(DeclarativeBase):
    __tablename__ = "StudentInClass"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("Class.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("Student.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("Teacher.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'class_id',
            'student_id',
            'teacher_id',
            name='uq_student_in_class'
        ),
    )

    def __repr__(self):
        return f"StudentInClass(id={self.id}, class_id={self.class_id}, student_id={self.student_id}, teacher_id={self.teacher_id})"
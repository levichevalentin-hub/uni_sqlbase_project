from sqlalchemy import UniqueConstraint, Column, Integer, String, Date, DeclarativeBase

class Subject(DeclarativeBase):
    __tablename__ = "Subject"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, nullable=False)
    subject_name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'teacher_id', 
            'subject_name',
            name='uq_subj_name_teach'
        ),
    )

    def __repr__(self):
        return f"Subject (id = {self.id}, teacher_id = {self.teacher_id}, subject_name = {self.subject_name})"
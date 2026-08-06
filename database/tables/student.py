from sqlalchemy import UniqueConstraint, Column, Integer, String, Date

class Student(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    jmbg = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    index_number = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'first_name', 
            'second_name', 
            'birthday', 
            name='uq_stud_full_name_birthday'
        ),
    )

    def __repr__(self):
        return f"Student (id = {self.id}, first_name = {self.first_name}, second_name = {self.second_name}, birthday = {self.birthday},  jmbg = {self.jmbg}, address = {self.address}, index_number = {self.index_number})"
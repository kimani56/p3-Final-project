from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from connect import engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', student_id={self.student_id})>"

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Grade(id={self.id}, value={self.value})>"

course_grade = Table('course_grade', Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id'), nullable=False),
    Column('grade_id', Integer, ForeignKey('grades.id'), nullable=False)
)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

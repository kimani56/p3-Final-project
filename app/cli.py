# student_management/cli.py

import click
from models import Session, Student, Course, Grade  
from faker import Faker

fake = Faker()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Student name', help='Name of the student')
def add_student(name):
    session = Session()  

    student = Student(name=name)
    session.add(student)
    session.commit()

    session.close()
    click.echo(f'Student "{name}" added successfully.')

@cli.command()
@click.option('--student-id', type=int, prompt='Student ID', help='ID of the student to update')
@click.option('--new-name', prompt='New name', help='New name for the student')
def update_student(student_id, new_name):
    session = Session()  
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        student.name = new_name
        session.commit()
        session.close()
        click.echo(f'Student ID {student_id} updated successfully.')
    else:
        session.close()
        click.echo(f"Student with ID {student_id} not found.")

@cli.command()
@click.option('--student-id', type=int, prompt='Student ID', help='ID of the student to delete')
def delete_student(student_id):
    session = Session()  
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        session.delete(student)
        session.commit()
        session.close()
        click.echo(f'Student ID {student_id} deleted successfully.')
    else:
        session.close()
        click.echo(f"Student with ID {student_id} not found.")

@cli.command()
@click.option('--student-id', type=int, prompt='Student ID', help='ID of the student to retrieve records for')
def retrieve_student_records(student_id):
    session = Session()  
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        click.echo(f'Student ID: {student.id}')
        click.echo(f'Student Name: {student.name}')
        click.echo('Courses:')
        for course in student.courses:
            click.echo(f'- Course ID: {course.id}, Name: {course.name}')
            click.echo('  Grades:')
            for grade in course.grades:
                click.echo(f'  - Grade ID: {grade.id}, Value: {grade.value}')
    else:
        click.echo(f"Student with ID {student_id} not found.")

@cli.command()
@click.option('--student-id', type=int, prompt='Student ID', help='ID of the student to add a course and grade')
@click.option('--course-name', prompt='Course name', help='Name of the course')
@click.option('--grade-value', type=float, prompt='Grade value', help='Grade value')
def add_course_and_grade(student_id, course_name, grade_value):
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        course = Course(name=course_name, student=student)
        grade = Grade(value=grade_value, course=course)
        session.add(course)
        session.add(grade)
        session.commit()
        session.close()
        click.echo(f'Course "{course_name}" and grade "{grade_value}" added to Student ID {student_id} successfully.')
    else:
        session.close()
        click.echo(f"Student with ID {student_id} not found.")

if __name__ == '__main__':
    cli()

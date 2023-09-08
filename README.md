# Student Management System

The Student Management System is a command-line application designed to help you manage student records, courses, and grades. It allows you to perform various actions such as adding, updating, and deleting student records, as well as adding courses and grades to students.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Available Commands](#available-commands)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- SQLite database engine.

### Installation

1. Clone this repository to your local machine:
git clone<repo link>

2. Navigate to the project directory:
use the cd command

3. install depandancies
use pipenv install

4. activate virtual env
use pipenv shell


## Usage

### Command-Line-Interface
- TO run the CLI, use the following command 
python cli.py

### Available Commands
- ADDING A STUDENT
 To add a student use the following command
 . python cli.py add_student --name "the _name"

- Updating a Student
 to update a students name, use the following command
 . python cli.py update_student --student-id 1 --new-name "Jane Smith"

- Deleting a Student
 To delete a student, use the following command:
 . python cli.py delete_student --student-id 1

- Retrieving Student Records
 To retrieve a student's records, including their courses and grades,use the following command:
  . python cli.py retrieve_student_records --student-id 1

- Adding a Course and Grade
 To add a course and grade to a student, use the following command:
 . python cli.py add_course_and_grade --student-id 1 --course-name "Math" --grade-value 85.5

### Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your fork.
Submit a pull request to the main branch of the original repository.

### License
This project is licensed under the MIT License. See the LICENSE file for details.




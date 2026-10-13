# Digital Exam & Results Management System

PROG211 Object-Oriented Programming 1 - Individual Assignment (Education domain)
Limkokwing University of Creative Technology, Sierra Leone

A simple console program that lets a lecturer register students and record exam results, then view grades and averages.

## How to run

python exam_results_system.py

Requires Python 3.8 or newer. No extra packages needed.

## OOP concepts used

- Classes, attributes, objects: Student, ExamResult, ResultsPortal
- Object interaction: a Student creates and holds ExamResult objects; ResultsPortal holds Student objects
- Data structure: one dictionary, ResultsPortal.students (student ID is the key)
- Add / display functions: add_student(), display_all()
- Instance methods: add_result(), update_record(), display_info(), average_score()
- Class method: Student.get_total_students() (@classmethod)
- Static method: Student.grade_from_score() (@staticmethod)
- Tuples (bonus): GRADE_BANDS constant stores fixed grade rules

## Digital Public Goods (DPG) alignment

- Open-source: the full source code is published on GitHub for anyone to use and improve.
- Inclusive and accessible: plain text menu, simple numbered options, clear error messages, runs on any basic computer.
- Privacy-respecting: only an anonymous student ID, a display name and a programme are stored. No phone numbers, addresses or national IDs.
- Modular and reusable: each class has one job, so Student and ExamResult can be reused in other school systems.

## Example usage

Choose an option: 2
Student ID: S001
Course code: prog300
Score (0-100): 91
Result saved.

Choose an option: 3
Student ID: S001

Student ID : S001
Name : Student A
Programme : BSc Information Technology
Results:
PROG211 Score: 78.0 Grade: B (Very Good)
PROG202 Score: 85.0 Grade: A (Excellent)
PROG300 Score: 91.0 Grade: A (Excellent)
Average : 84.7 Overall grade: A

## Files

- exam_results_system.py - source code
- README.md - this file


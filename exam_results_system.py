
# Tuples (optional bonus): fixed grade bands as (minimum score, grade, remark)
GRADE_BANDS = (
    (80, "A", "Excellent"),
    (70, "B", "Very Good"),
    (60, "C", "Good"),
    (50, "D", "Pass"),
    (0, "F", "Fail"),
)


class ExamResult:
    """Represents one exam result for one course."""

    def __init__(self, course_code, score):
        self.course_code = course_code.upper()
        self.score = score
        # Static method used here to convert score to grade
        self.grade, self.remark = Student.grade_from_score(score)

    def display_info(self):
        print(f"  {self.course_code:<10} Score: {self.score:>5.1f}  "
              f"Grade: {self.grade}  ({self.remark})")


class Student:
    """Represents a student using an anonymous ID (no sensitive data)."""

    total_students = 0  # class attribute shared by all objects

    def __init__(self, student_id, display_name, programme):
        self.student_id = student_id
        self.display_name = display_name
        self.programme = programme
        self.results = {}  # course_code -> ExamResult
        Student.total_students += 1

    # ---------- instance methods ----------
    def add_result(self, course_code, score):
        """Create an ExamResult object and attach it to this student."""
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        result = ExamResult(course_code, score)
        self.results[result.course_code] = result  # same course = update
        return result

    def update_record(self, display_name=None, programme=None):
        """Update the student's basic details."""
        if display_name:
            self.display_name = display_name
        if programme:
            self.programme = programme

    def average_score(self):
        if not self.results:
            return 0.0
        total = sum(r.score for r in self.results.values())
        return total / len(self.results)

    def display_info(self):
        print(f"\nStudent ID : {self.student_id}")
        print(f"Name       : {self.display_name}")
        print(f"Programme  : {self.programme}")
        if not self.results:
            print("  No results recorded yet.")
            return
        print("Results:")
        for result in self.results.values():
            result.display_info()
        avg = self.average_score()
        print(f"  Average    : {avg:.1f}  Overall grade: "
              f"{Student.grade_from_score(avg)[0]}")

    # ---------- class method ----------
    @classmethod
    def get_total_students(cls):
        """Return how many Student objects have been created."""
        return cls.total_students

    # ---------- static method ----------
    @staticmethod
    def grade_from_score(score):
        """Return (grade, remark) for a score using the GRADE_BANDS tuple."""
        for minimum, grade, remark in GRADE_BANDS:
            if score >= minimum:
                return grade, remark
        return "F", "Fail"


class ResultsPortal:
    """Stores many Student objects in ONE dictionary (ID is the key)."""

    def __init__(self):
        self.students = {}  # student_id -> Student

    def add_student(self, student_id, display_name, programme):
        if student_id in self.students:
            print("A student with that ID already exists.")
            return None
        student = Student(student_id, display_name, programme)
        self.students[student_id] = student
        print(f"Student {student_id} added.")
        return student

    def find_student(self, student_id):
        return self.students.get(student_id)

    def record_result(self, student_id, course_code, score):
        student = self.find_student(student_id)
        if student is None:
            print("Student not found.")
            return
        try:
            student.add_result(course_code, score)
            print("Result saved.")
        except ValueError as error:
            print(f"Error: {error}")

    def display_all(self):
        if not self.students:
            print("No student records yet.")
            return
        for student in self.students.values():
            student.display_info()
        print(f"\nTotal students: {Student.get_total_students()}")


def load_sample_data(portal):
    """Anonymous sample data for demonstration."""
    portal.add_student("S001", "Student A", "BSc Information Technology")
    portal.add_student("S002", "Student B", "BSc Software Engineering")
    portal.record_result("S001", "PROG211", 78)
    portal.record_result("S001", "PROG202", 85)
    portal.record_result("S002", "PROG211", 55)
    portal.record_result("S002", "BSEM1101", 62)


def read_score(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return -1  # will be rejected by add_result


def main():
    portal = ResultsPortal()
    load_sample_data(portal)

    menu = (
        "\n=== Digital Exam & Results Management System ===\n"
        "1. Add student\n"
        "2. Record exam result\n"
        "3. View one student\n"
        "4. View all students\n"
        "5. Update student details\n"
        "0. Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            portal.add_student(input("Student ID: ").strip(),
                               input("Display name (no full personal data): ").strip(),
                               input("Programme: ").strip())
        elif choice == "2":
            portal.record_result(input("Student ID: ").strip(),
                                 input("Course code: ").strip(),
                                 read_score("Score (0-100): "))
        elif choice == "3":
            student = portal.find_student(input("Student ID: ").strip())
            student.display_info() if student else print("Student not found.")
        elif choice == "4":
            portal.display_all()
        elif choice == "5":
            student = portal.find_student(input("Student ID: ").strip())
            if student:
                student.update_record(input("New name (blank to skip): ").strip(),
                                      input("New programme (blank to skip): ").strip())
                print("Record updated.")
            else:
                print("Student not found.")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

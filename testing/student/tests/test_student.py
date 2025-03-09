from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho", {"Math": ["Pitagor", "x + y = z",], "History": ["WWI", "Cold war"]})

    def test_init_courses_none(self):
        self.test_student = Student("Tosho")
        self.assertEqual({}, self.test_student.courses)
        self.assertEqual("Tosho", self.student.name)

    def test_init_with_courses(self):
        result = {"Math": ["Pitagor", "x + y = z",], "History": ["WWI", "Cold war"]}
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual(result, self.student.courses)

    def test_enroll_with_course_already_in(self):
        result = self.student.enroll("Math", ["2 * r * Pi", "r ** 2 * Pi"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["Pitagor", "x + y = z", "2 * r * Pi", "r ** 2 * Pi"], self.student.courses["Math"])

    def test_enroll_with_new_course_and_add_notes(self):
        result = self.student.enroll("Bulgarian", ["Ivan Vazov", "Hristo Botev"], "Y")
        all_courses = {"Math": ["Pitagor", "x + y = z"], "History": ["WWI", "Cold war"], "Bulgarian": ['Ivan Vazov', 'Hristo Botev']}
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(all_courses, self.student.courses)

    def test_enroll_with_new_course_and_add_notes_with_empty_string(self):
        result = self.student.enroll("Bulgarian", ["Ivan Vazov", "Hristo Botev"], "")
        all_courses = {"Math": ["Pitagor", "x + y = z"], "History": ["WWI", "Cold war"], "Bulgarian": ['Ivan Vazov', 'Hristo Botev']}
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(all_courses, self.student.courses)

    def test_enroll_with_new_course_and_no_notes(self):
        result = self.student.enroll("Geography", ["Africa", "Europe"], "Blu")
        all_courses = {"Math": ["Pitagor", "x + y = z"], "History": ["WWI", "Cold war"], "Geography": []}
        self.assertEqual("Course has been added.", result)
        self.assertEqual(all_courses, self.student.courses)

    def test_add_notes_if_course_in_dictionary(self):
        result = self.student.add_notes("History", ["French revolution", "American civil war"])
        new_notes = ["WWI", "Cold war", "French revolution", "American civil war"]
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(new_notes, self.student.courses["History"])

    def test_add_notes_for_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Music", ["Piano", "Bass"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_right_course(self):
        result = self.student.leave_course("Math")
        all_courses = {"History": ["WWI", "Cold war"]}
        self.assertEqual("Course has been removed", result)
        self.assertEqual(all_courses, self.student.courses)

    def test_leave_course_wrong_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Art")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



if __name__ == "__main__":
    main()
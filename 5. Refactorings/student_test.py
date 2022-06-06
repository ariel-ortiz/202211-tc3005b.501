# File: student_test.py
import sys
from io import StringIO
from unittest import TestCase, main
from student import Student

class StudentTest(TestCase):

  def setUp(self):
    self._out = StringIO()
    self._old_stdout = sys.stdout
    sys.stdout = self._out
    self._student1 = Student('John', 123, 10_000)
    self._student2 = Student('Mary', 222, 25_000)
    self._student1.add_grade(90).add_grade(84).add_grade(93)

  def tearDown(self):
    sys.stdout = self._old_stdout

  def test_meh(self):
    self.maxDiff = None
    self._student1.meh()
    self._student2.meh()
    self.assertEqual(
      'Name: John ID: 123\n'                                            \
      'Anual income: 10000\n'                                           \
      'Grade average: 89.0\n'                                           \
      'The contents of this class must not be considered an offer,\n'   \
      'proposal, understanding or agreement unless it is confirmed\n'   \
      'in a document signed by at least five blood-sucking lawyers.\n'  \
      'Name: Mary ID: 222\n'                                            \
      'Anual income: 25000\n'                                           \
      'Grade average: nan\n'                                            \
      'The contents of this class must not be considered an offer,\n'   \
      'proposal, understanding or agreement unless it is confirmed\n'   \
      'in a document signed by at least five blood-sucking lawyers.\n', \
      self._out.getvalue())

  def test_is_scholarship_worthy(self):
    self.assertTrue(self._student1.is_scholarship_worthy())
    self.assertTrue(-1, self._student2.is_scholarship_worthy())
    self._student2.add_grade(90)
    self.assertFalse(self._student2.is_scholarship_worthy())

if __name__ == '__main__':
    main()

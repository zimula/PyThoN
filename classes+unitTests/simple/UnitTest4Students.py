'library for printing to html'
from HtmlTestRunner import HTMLTestRunner

'code to be tested'
import StudentClass
'test library'
import unittest

'setting up the test'
class testStudent(unittest.TestCase):
    'check if gpa is calculated correclty'
    def test_gpa(self):
        'create student'
        student = StudentClass.Student("Jack", 100.0, 400.0)
        'run test'
        self.assertEqual(student.gpa(),4.0)
    'check if points are returned'

    def test_getQpoint(self):
        student = StudentClass.Student("Tom", 100.0, 500.0)
        self.assertEqual(student.getQpoint(),500.0)
    'test name string'
    def test_getName(sefl):
        student = StudentClass.Student("Zack", 100.0, 300.0)
        sefl.assertEqual(student.getName(),'Zack')
    'test hours'
    def test_getHours(self):
        student = StudentClass.Student("Roger", 100.0, 500.0)
        self.assertEqual(student.getHours(),100.0)



'make sure module is run as the main module'
'''if __name__ =='__main__':
    unittest.main(testRunner=HTMLTestRunner(output='tests'))
    - creates or locates a folder name tests and inserts the report.

    - the one below, adds name to report and choose a folder. 
'''
if __name__=='__main__':
    custom_report_file_name = "student_Test.html"
    runner = HTMLTestRunner(output="tests")
    unittest.main(testRunner=runner)


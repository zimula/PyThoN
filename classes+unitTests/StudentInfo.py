'''
KEY POINT IN THIS PROGRAM: 
- importing existing classes (open class to see how it's made)
- instantiation via stored data. 
- calling instance methods

'''






'importing student class from a different folder'
from simple import StudentClass

'function make students: takes data and feeds it to class constructor'
def makeStudent(infoStr):
    'infoStr = tab-separated line'
    name, hours, qpoints = infoStr.split("\t")
    'return student using data from infoStr'
    return StudentClass.Student(name, hours, qpoints)

'function to open file and check for best student'
def main():
    "open file"
    filename = input('Enter the name of the grade file: ')
    infile = open(filename, 'r')

    'find the first record'
    best = makeStudent(infile.readline())

    'loop through the lines and replace best with highest gpa'
    for line in infile:
        'turn line into student record'
        s = makeStudent(line)
        'remember if gpa is greater'
        if s.gpa() > best.gpa():
            best = s

    infile.close()
    'print results'
    print()
    print('The best student is: ', best.getName())
    print('hours: ', best.getHours())
    print('GPA: ', best.gpa())

'check whether current module is running as main'
if __name__ == "__main__":
    main()


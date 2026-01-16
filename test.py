import Globals
import FileHandler


def populateStudentlist(filename):
    tempstudentlist = FileHandler.ReadFile(filename)
    print(tempstudentlist)

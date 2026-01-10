import sys
import FileHandler

def ExitProgram():
        print("Saving data into Student Record")
        FileHandler.WriteFile()
        print("Saving done")
        print("Exiting now")
        sys.exit(0)
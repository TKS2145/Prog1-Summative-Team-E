import json
from Globals import Studentlist
from Globals import PaymentList

def ReadFile():
    pass

def WriteFile():
    '''
    example writing in file

    json_str = json.dumps(data, indent=4)
    with open("sample.json", "w") as f:
        f.write(json_str)

    '''
    #Over-write StudentRecords as it is not possible to modify a single entry of data

    with open("StudentRecords.json", "w") as fileWriter:
        for x in Studentlist:
            data = dict(x.to_dict())
            json_str = json.dumps(data, indent= 4)
            fileWriter.write(json_str)



def AppendFile():
    pass


import json
from Globals import Studentlist
from Globals import PaymentList

def ReadFile():
    pass

def WriteFile(filename ="StudentRecords.json"):
    #Over-write StudentRecords as it is not possible to modify a single entry of data

    with open(filename, "w") as fileWriter:
        data = dict(Studentlist[0].to_dict)
        json_str = json.dumps(data, indent= 4)
        fileWriter.write(json_str)

    AppendFile(filename, Studentlist)



def AppendFile(filename, appendinglist = PaymentList):
        
    with open("filename", "a") as fileWriter:
        for x in appendinglist:
            data = dict(x.to_dict)
            json_str = json.dumps(data, indent= 4)
            fileWriter.write(json_str)


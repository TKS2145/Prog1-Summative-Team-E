import json
from Globals import Studentlist
from Globals import PaymentList

def ReadFile():
    pass

def WriteFile(filename ="StudentRecords.json", list_to_write =[] ): #Writing to StudentRecord as it is only file which needs to be overwritten
    #Over-write StudentRecords as it is not possible to modify a single entry of data
    '''
        with open(filename, "w") as fileWriter:
            try:
                data = dict(Studentlist[0].to_dict())
                json_str = json.dumps(data, indent= 4)
                fileWriter.write(json_str)
            except:
                print("json formating error")

        if len(Studentlist) > 1:
            AppendFile(filename, Studentlist) #Sending StudentList
        else:
            return
        
    '''
    data = []
    for x in list_to_write:
        data.append(x.to_dict())

    with open(filename, "w") as fileWriter:
        try:
            json_str = json.dumps(data, indent= 4)
            fileWriter.write(json_str)
        except:
            print("json formating error")

'''
def AppendFile(filename, appendinglist = PaymentList): #Appending PaymentList as default
    
    with open(filename, "a") as fileWriter:
        
        for x in appendinglist:
            if x == appendinglist[0]:
                continue
            data = dict(x.to_dict())
            json_str = json.dumps(data, indent= 4)
            fileWriter.write(json_str)
'''
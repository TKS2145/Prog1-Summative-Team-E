import json

def ReadFile(filename):
    try:
        with open(filename, "r") as filereader:
            str_data = json.load(filereader)
            #print(str_data) #Just for testing
            return str_data
    except:
        print("File reading error. Check if file is empty.")
        return 

def WriteFile(filename, list_to_write =[] ): #Forcing lsit_to_write to be a list

    #Over-write StudentRecords as it is not possible to modify a single entry of data
    data = []
    for x in list_to_write:
        data.append(x.to_dict())

    with open(filename, "w") as fileWriter:
        try:
            json_str = json.dumps(data, indent= 4)
            fileWriter.write(json_str)
        except:
            print("json formating error")
import os.path
from os import path

def data_exists( names ):
    if type(names) == list:
        if len(names) == 1:
            return data_exists(names[0])
        else:
            names_exists = []
            for n in names:
                names_exists.append( data_exists(n) )
            return names_exists
    elif type(names) == str:
        return path.exists("/home/public/data/"+names+".csv")

def data_delete( names ):
    if type(names) == list:
        if len(names) == 1:
            delete_data(names[0])
        else:
            for n in names:
                delete_data(n)
    elif type(names) == str:
         os.remove("/home/public/data/"+names+".csv")

def data_move( names ):
    if type(names) == list:
        if len(names) == 1:
            delete_data(names[0])
        else:
            for n in names:
                delete_data(n)
    elif type(names) == str:
        shutil.move("./" + names + ".csv", "/home/public/data/" + names + ".csv")


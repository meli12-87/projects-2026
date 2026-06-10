from fastapi import FastAPI
import sqlite3

#DB_NAME = 'Library.db'
app = FastAPI()
mylist = []

@app.get('/')
def home():
    return{'HELLO': 'PYTHON'}

@app.post('/items/{newitem}')
def add_item(newitem):
    mylist.append(newitem)
    return {'Result': mylist}

@app.get("/getAll/")
def select_all_items():
    return {'Items': mylist}

@app.get("/getItem/{index}")
def get_item_by_index(index : int):
    if index < 0 or index >= len(mylist):
        return 'Index is wrong'
    else:
        return {'Result': mylist[index]}
    
@app.get("/getlastitem/")
def get_last_item():
    if len(mylist) == 0:
        return 'list is empty'
    else:
        return {'Result': mylist[-1]}
    
@app.delete("/deleteitembyindex/{index}")
def delete_item_by_index(index:int):
    if index > 0 and index >= len(mylist):
        return 'Index is wrong'
    else:
        result = mylist.pop(index)
        return f'{result} deleted from list'
    
@app.delete("/deleteitembyitem/{item}")
def delete_item(item):
    if item not in mylist:
        return 'item is not in mylist'
    else:
        result = mylist.remove(item)
        return {'mylist_after_remove': mylist}
    
@app.put('/updatebyindex/{index}')
def update_item(index:int, newitem):
    if index < 0 or index >= len(mylist) or len(mylist) == 0:
        return 'Index is wrong'
    else:
        mylist[index]=newitem
        return{'updated_list': mylist}
    
@app.put("/updatebyitem/{item}")
def item_update(item,newitem):
    if item not in mylist and len(mylist) == 0:
        return f'item either not in list or wrong'
    else:
        result = mylist.index
        mylist[result]=newitem
        return{'updated_list': mylist}

    



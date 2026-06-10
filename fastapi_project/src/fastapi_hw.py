from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

tasks = []

class task:
    def __init__(self, id, title, description, is_completed, createdat):
        self.id = id
        self.title = title
        self.description = description 
        self.is_completed = is_completed
        self.createdat = createdat

@app.get('/')
def home():
    return {'Output': "سلام خوش آمدید"}

@app.post('/add/{title}/{description}')
def add_task(title: str, description: str):
    new_id = len(tasks) + 1
    new_task = task(
        id=new_id,
        title=title,
        description=description,
        is_completed=False,
        createdat=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    tasks.append(new_task)
    return {'Output': 'کار اضافه شد', 'id': new_id}

@app.get('/alltasks/')
def get_all_tasks():
    if len(tasks) == 0:
        return {'Output': 'لیست خالی است'}
    
    result = []
    for t in tasks:
        result.append({
            'id': t.id,
            'title': t.title,
            'description': t.description,
            'is_completed': t.is_completed,
            'createdat': t.createdat
        })
    return {'All Tasks': result}

@app.get('/task/{task_id}')
def get_one_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return {
                'id': t.id,
                'title': t.title,
                'description': t.description,
                'is_completed': t.is_completed,
                'createdat': t.createdat
            }
    return {'error': 'کار پیدا نشد'}

@app.put('/complete/{task_id}')
def change_status(task_id: int):
    for t in tasks:
        if t.id == task_id:
            t.is_completed = not t.is_completed
            return {'message': 'وضعیت تغییر کرد', 'is_completed': t.is_completed}
    return {'error': 'کار پیدا نشد'}

@app.delete('/delete/{task_id}')
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            deleted = tasks.pop(i)
            return {'message': f'کار {deleted.title} حذف شد'}
    return {'error': 'کار پیدا نشد'}
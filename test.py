from fastapi import FastAPI

app = FastAPI()

df = {
    1 : {'nama':'budi','age':'19'},
    2 : {'nama':'budie','age':'15'},
    3 : {'nama':'budin','age':'12'}
}

@app.get('/')
def home_endpoint():
    return "halo ini main page"

@app.get('/get_data')
def get_data():
    return df

@app.post('/add_data')
def add_item(item:dict):
    new_key = max(df.keys()) + 1
    df[new_key] = item

    return {'message':f'item with id {new_key} has been added'}

@app.put('/update_data/{item_id}')
def update_item(item_id: int,item: dict):
    df[item_id].update(item)

    return {'message':f'item with id {item_id} has been updated'}
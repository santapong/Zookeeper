import uvicorn
from fastapi import FastAPI
 
app = FastAPI()

@app.get('/datas')
def fecth_data():
    return None

if __name__ == '__main__':
    uvicorn()
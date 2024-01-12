from fastapi import FastAPI
#Python의 type hint를 기반으로 fastapi
# POST다운(즉 query string을 노출시키지 않고 response body에 넣은) 통신을 위해 
from pydantic import BaseModel
from pydantic import Field

# fastapi의 GET, link에 query string이 생김
app = FastAPI()

# POST처럼 query string이 생기지 않게 하려면!
class DataInput(BaseModel):
  name: str

@app.get("/") # /는 현재경로
async def root():
  return {"message": "Hello World"}

#post는 http body에 들어가기 때문에 url에 노출되지 않음. Response body에 업데이트
@app.post("/")
def home_post(data_request : DataInput):
  return {"message": data_request.name, "POST" : "Hello"}

@app.get("/home")
def home():
  return {"message": "home"}


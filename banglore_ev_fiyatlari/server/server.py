from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import util
from schema import Input, Output

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get('/get_location_names',status_code=status.HTTP_200_OK)
def get_location_names():
    response ={
        'locations': util.get_location_names()
    }
    return response

@app.get('/predict_home_price',  response_model=Output)
def predict_home_price(location,sqft,bhk,bath):
    estimated_price =  util.get_estimated_price(
        location=str(location),
        sqft=float(sqft),
        bhk=int(bhk), 
        bath=int(bath)
        )
    result = Output(estimated_price=estimated_price)

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8899 )
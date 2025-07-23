from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")



class ConvertRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float


# Currency conversion code
@app.post("/convert")
async def convert_currency(req: ConvertRequest):
    print("Received request:", req)

    url = f"https://api.frankfurter.app/latest?amount={req.amount}&from={req.from_currency.upper()}&to={req.to_currency.upper()}"
    print("Requesting:", url)
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print("Response status:", response.status_code)
        print("Response content:", response.text)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch exchange rates")

        data = response.json()
        
      
        if req.to_currency.upper() not in data.get("rates", {}):
            raise HTTPException(status_code=400, detail="Invalid currency code")

        rate = data["rates"][req.to_currency.upper()]
        converted_amount = round(float(data["amount"]) * rate, 2)

        return {
            "from": req.from_currency.upper(),
            "to": req.to_currency.upper(),
            "original_amount": req.amount,
            "converted_amount": converted_amount,
            "rate": rate  
        }
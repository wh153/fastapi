from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/exponent/{num1}/{num2}")
async def exponent (num1: int, num2: int):
    """Get the power num2 of num1"""
    
        
    result = num1 ** num2
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
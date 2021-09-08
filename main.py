from fact import actual_recursive

import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to this simple calculator, please choose the calculation you want with the input"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}
    #return {"total": total}

@app.get("/exponent/{num1}/{num2}")
def exponent(num1: int, num2: int):
    """Get the power num2 of num1"""
    
        
    result = num1 ** num2
    return {"result": result}
    
@app.get("/factorial/{num1}")
def factorial(num1: int):
    """Get the factorial of num1"""
    
    result = actual_recursive(num1)
    return {"result": result}
    
@app.get("/fib/{n}")
def fib(n: int):
    """Get the nth element of Fibonacci sequence"""
    if n<= 0:
        return {"result": "Incorrect output"}
    data = [0, 1]
    if n > 2:
        for i in range (2, n+1):
            data.append(data[i-1] + data[i-2])
        result = data[n]
    else:
        result = 1
    return {"result": result}
    
    

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

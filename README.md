# FastAPI Project 1
This is a repository for project1 of IDS 706 Clouding computing. 


# Project1 - FastAPI Microservice build on AWS EC2 instance and hosted on AWS App Runner
using AWS cloud9 as development environment and github as source control, we create a microservice for two simple calculations utilizing recursion and dynamic programming.
Here are the two types of functions you can find:
 
 1. Simple addition and exponent calculation (usually for some testing):
   /add/{num1}/{num2} which returns the sum of num1 and num2 in the form of a json payload
   /exponent/{num1}/{num2} which returns the num2 th power of num1 in the form of a json payload

 2. Factorial calculation and the Nth item in a Fibonacci sequence:
   /factorial/{num1} which returns the result of num1! in the form of a json payload
   /fib/{n} which returns the nth element in the Fibonacci sequence

from fastapi import FastAPI
#Difference between fastapi and FastAPI:
#fastapi is a module/package
#FastAPI is a class

app = FastAPI()
#The FastAPI() in the line of code above is called a constructor function
#The app in the line above is called application object

@app.get("/welcomemessage")#Tells FastAPI that the function right below is in charge of handling requests that go to: the path/ using a get operation
#The @ at the start of the line of code is called a decorator, purpose is to link a url to the function
def read_root():
    return {"Hello": "World"}
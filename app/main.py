# import FastAPI class from fastapi module
from fastapi import FastAPI, status

# create instance of FastAPI class
# instance will an object containing two things
# attribute/properties + methods
# you need to store your instance in an app / server variable
# it is standard in API development - to use the app or server object name for your 
# api instance
app = FastAPI(
  title="Fastapi App 2025",
  description="Fastapi App to learn the fastapi 2025."
)

# creating end points for our api
'''
Here comes a concept of services
1. User Service ( User Authentication & User Authorization)
2. Task Service ( Create task and asign to the user to complete it)
'''

# How to create apis for above mention services
'''
Here comes the concept of operations
first we create path operation decorator
how many types of path operation decorator are
@app.get("/")
@app.post("/")
@app.delete("/")
@app.put("/")
@app.patch("/")
what includes in path operation decorator
@app - core decorator
.get, .post, .delete, .put, .patch - http methods / operations
("/") - endpoint / path / route 

when user send request on server, user must have two things
1- api endpoint
2- http method
to send the request my api app/server


action of endpoint
the action will be the function of python
- function can be simple python function
- function can be the async python function

we know that, fastapi is the asynchorous python web framework
to create the high performance, fast, relaible, light weight
backends for any type of website, web app, AI service, Data Science
Projects, IoT Products, or any automation tool.
'''


# we always create first endpoint to check the health of server / api
@app.get("/", status_code = status.HTTP_200_OK, summary="health check get endpoint", description="check the health check of api", tags=["Health Check"] )
async def health_check():

  # response
  return {"status":True, "message":"API is running Successfully"}

'''
as we are using python to create our apis, our action health_check
will return the python dictionary. and we use T capital in True
as it's convention in python

but when our fastapi process the returning python dictionary, then, fastapi
behined the scene use pydantic to serialize the python dictionary into json
(javascript object notation)

JSON is the standard format to send / receive data on network through apis.
JSON is language independant data format
'''
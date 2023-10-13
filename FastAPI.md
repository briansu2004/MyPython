# FastAPI

## FASTAPI keywords

- fastapi
- venv
- uvicorn
- ASGI
- Pydantic 
- Gunicorn
- SQLAlchemy (and Tortoise-ORM, pymongo, MongoClient etc.)

## FastAPI kickstart

FastAPI is a modern, fast, web framework for building RESTful APIs with Python. It's known for its simplicity, automatic documentation generation, and performance. Here are the steps to use FastAPI to build REST APIs:

1. **Setup Your Development Environment**:

   Before you start using FastAPI, make sure you have Python installed on your system. You can create a virtual environment and install FastAPI in it:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   pip install fastapi
   ```

2. **Create a FastAPI App**:

   FastAPI is designed to be simple and easy to use. Here's a minimal FastAPI application (name is `main.app`):

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   ```

3. **Run the FastAPI App**:

   You can run the app using the `uvicorn` ASGI server. Install it if you haven't already:

   ```bash
   pip install uvicorn
   ```

   Then, run your FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

   Here, `main` is the name of your Python file, and `app` is the name of the FastAPI instance you created. The `--reload` option enables auto-reloading during development.

4. **Define Endpoints**:

   FastAPI makes it easy to define API endpoints. You can use decorators like `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()` to define routes and HTTP methods. For example:

   ```python
   @app.get("/items/{item_id}")
   def read_item(item_id: int, query_param: str = None):
       return {"item_id": item_id, "query_param": query_param}
   ```

5. **Request and Response Models**:

   You can use Pydantic models for request and response validation. These models automatically parse request data and serialize response data.

   ```python
   from pydantic import BaseModel

   class Item(BaseModel):
       name: str
       description: str

   @app.post("/items/")
   def create_item(item: Item):
       return item
   ```

6. **Automatic Documentation**:

   FastAPI automatically generates documentation for your API. You can access the documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc` when the app is running.

7. **Query Parameters and Path Parameters**:

   FastAPI allows you to define query parameters and path parameters easily using the function arguments. You can also specify types and default values for these parameters.

8. **Authentication**:

   You can implement authentication mechanisms such as OAuth, API tokens, or basic authentication with FastAPI using third-party libraries.

9. **Testing**:

   FastAPI has built-in support for testing using tools like `pytest`. You can write tests for your API endpoints to ensure they work as expected.

10. **Deployment**:

    Deploy your FastAPI application on your choice of web servers, such as Gunicorn, or use platforms like Docker and AWS Lambda.

11. **Middleware**:

    You can use middleware to perform actions before and after handling requests, like authentication, logging, and error handling.

12. **Dependencies**:

    FastAPI allows you to define dependencies that can be used by multiple endpoints, helping to keep your code DRY (Don't Repeat Yourself).

13. **Security**:

    FastAPI has built-in features to handle security and prevent common vulnerabilities like SQL injection, XSS, and CSRF.

14. **Background Tasks**:

    You can run background tasks and schedule periodic tasks using FastAPI's `BackgroundTasks` and `FastAPI.tasks` module.

15. **Database Integration**:

    To work with databases, you can integrate FastAPI with various database libraries, such as SQLAlchemy, Tortoise-ORM, or use NoSQL databases like MongoDB.

FastAPI is a powerful framework that simplifies the process of building RESTful APIs in Python. It's well-documented, so you can refer to the official documentation (https://fastapi.tiangolo.com/) for more advanced features and in-depth usage details.

## Connect MongoDB with FastAPI

To connect MongoDB with FastAPI, you'll need to use a MongoDB driver for Python, such as PyMongo. Here are the steps to connect and work with MongoDB in a FastAPI application:

1. **Install Required Libraries**:

   Make sure you have FastAPI and PyMongo installed in your Python virtual environment:

   ```bash
   pip install fastapi
   pip install pymongo
   ```

2. **Import Required Modules**:

   In your FastAPI application, import the necessary modules:

   ```python
   from fastapi import FastAPI
   from pymongo import MongoClient
   ```

3. **Create a MongoDB Client**:

   You need to create a MongoClient to connect to your MongoDB server. You can specify the MongoDB connection URI as the argument to the MongoClient constructor:

   ```python
   client = MongoClient("mongodb://localhost:27017/")
   ```

   Replace `"mongodb://localhost:27017/"` with the connection URI for your MongoDB server.

4. **Access a Database**:

   Once you have a MongoClient, you can access a specific database by name. If the database doesn't exist, MongoDB will create it when you first write data to it:

   ```python
   db = client["mydatabase"]
   ```

   Replace `"mydatabase"` with the name of your MongoDB database.

5. **Define FastAPI Routes**:

   You can now define FastAPI routes that interact with MongoDB. For example, to create an item in your database:

   ```python
   @app.post("/items/")
   def create_item(item: dict):
       collection = db["items"]
       item_id = collection.insert_one(item).inserted_id
       return {"item_id": str(item_id), **item}
   ```

   In this example, we insert an item into a collection named "items" within the MongoDB database.

6. **Query MongoDB**:

   You can use PyMongo to query the MongoDB database. For example, to retrieve an item by its ID:

   ```python
   @app.get("/items/{item_id}")
   def read_item(item_id: str):
       collection = db["items"]
       item = collection.find_one({"_id": item_id})
       if item:
           item["_id"] = str(item["_id"])
           return item
       return {"error": "Item not found"}
   ```

   This route retrieves an item from the "items" collection based on the provided `item_id`.

7. **Close MongoDB Connection**:

   It's essential to close the MongoDB connection when your FastAPI application shuts down. You can use FastAPI's `@app.on_event("shutdown")` to handle this:

   ```python
   @app.on_event("shutdown")
   def shutdown_mongo_client():
       client.close()
   ```

8. **Run the FastAPI Application**:

   You can run your FastAPI application as described in the previous answer using `uvicorn`.

Make sure you handle error checking, authentication, and data validation appropriately in your FastAPI routes, as shown in the previous response. Additionally, you can consider using asynchronous features with FastAPI and PyMongo to make your application more efficient, especially if you expect a high number of concurrent users.

This example provides a basic connection to MongoDB in a FastAPI application. Depending on your application's requirements, you may need to implement more advanced features like authentication, validation, and complex queries against your MongoDB database.

## ASGI

ASGI stands for "Asynchronous Server Gateway Interface." It's a specification for building asynchronous web applications and frameworks in Python. ASGI is designed to handle HTTP and WebSocket protocols using asynchronous programming techniques. It provides a way to handle long-lived connections, multiple simultaneous connections, and real-time interactions efficiently.

ASGI is an evolution of the WSGI (Web Server Gateway Interface) standard, which is the traditional way to build web applications in Python. The key difference is that ASGI allows for asynchronous code execution, making it well-suited for handling asynchronous tasks, such as real-time chat applications, streaming, and other web services that require non-blocking operations.

ASGI-compatible web frameworks and servers allow developers to build high-performance, asynchronous web applications in Python. Some popular ASGI frameworks and servers include FastAPI, Django Channels, and Uvicorn. ASGI has become increasingly important in the Python web development ecosystem as it enables efficient handling of modern web application requirements.

from fastapi import FastAPI,Form
from pydantic import BaseModel,constr,conint,Field
from enum import Enum

userList = [{"name":"ali","age":25,"gender":"male"}]

baseApp = FastAPI(
    title="SSKM API",
    description="API for SSKM project",
    version="0.1.0"
)

class GenderModel(str,Enum):
    male = "male"
    female = "female"
    other = "other"

class UserValidator(BaseModel):
    name: constr(min_length=3,max_length=50) # type: ignore
    age: conint(ge=18,le=100) # type: ignore
    gender:GenderModel

@baseApp.post("/user")
def add_user(name:str=Form(...),age:int=Form(...),gender:GenderModel=Form(...)):
    try: 
        userData = UserValidator(name=name,age=age,gender=gender)
    except Exception as e:
        return {"job":"error","message":str(e)}
    
    
    
    # userObject = {"name":name,"age":age,"gender":gender}
    # userList.append(userObject)
    # return {"job":"ok","user":userObject}


# product => post get => model => {name,description,price,quantity,category}

class productModel(BaseModel):
    name: constr(min_length=3,max_length=50) # type: ignore
    description: constr(min_length=3,max_length=200) # type: ignore
    price: Field(...,ge=1,description="price should be greater than or equal to 1") # type: ignore
    quantity: conint(ge=1) # type: ignore
    category: constr(min_length=3,max_length=50) # type: ignore

@baseApp.post("/product")
def add_product(
    name:str=Form(...),
    description:str=Form(...),
    price:int=Form(...),
    quantity:int=Form(...),
    category:str=Form(...)
    ):
    try: 
        productData = productModel(name=name,
                                   description=description,
                                   price=price,
                                   quantity=quantity,
                                   category=category)
    except Exception as e:
        return {"job":"error","message":str(e)}
    
    # productObject = {"name":name,"description":description,"price":price,"quantity":quantity,"category":category}
    # productList.append(productObject)



# @baseApp.get("/users")
# def get_users():
#     return {"job":"ok", "users":userList}

# # form parameter
# @baseApp.post("/users")
# def add_user(userName:str=Form(...)):
#     return {"job":"ok","userName":userName}

# # dynamic path parameter
# @baseApp.delete("/users/{userId}")
# def delete_user(userId:int):
#     return {"job":"ok","id":userId}

# # query parameter 
# @baseApp.delete("/users2")
# def delete_user2(userId:int):
#     return {"job":"ok","id":userId}

# # combination of form and dynamic path parameter
# @baseApp.put("/users/{userId}")
# def update_user(userId:int,userName:str=Form(...)):
#     return {"job":"ok","id":userId,"userName":userName}
    




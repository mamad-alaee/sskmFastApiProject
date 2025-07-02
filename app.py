from fastapi import FastAPI,Form

userList = ["ali",
            "veli",
            "ayse",
            "hasan"]

baseApp = FastAPI(
    title="SSKM API",
    description="API for SSKM project",
    version="0.1.0"
)













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
    




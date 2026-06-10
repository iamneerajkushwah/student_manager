from fastapi import APIRouter, HTTPException

from database import users_collection
from models.user import User, UserLogin
from utils.security import hash_password, verify_password
from utils.token import create_acess_token

router = APIRouter(
    tags=["Athuentication"]
)

@router.post("/register")
def register(user: User):

    existing_user = users_collection.find_one(
        {"username": user.username}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    
    hashed_password = hash_password(
        user.password
    )

    users_collection.insert_one(
        {
            "username": user.username,
            "password": hashed_password
        }
    )

    return {
        "message": "User regitered successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    db_user = users_collection.find_one(
        {"username":user.username}
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    if not verify_password(
        user.password,
        db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    access_token = create_acess_token(
        {"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



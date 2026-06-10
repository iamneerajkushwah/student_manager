from fastapi import Header, HTTPException

from utils.token import verify_access_token

def get_current_user(
        authorization: str | None = Header(default=None)
):
    
    if not authorization: 
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
    
    if not authorization.startswith(
        "Bearer"
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    token = authorization.split(" ")[1]

    username = verify_access_token(
        token
    )

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    return username
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from controllers.auth.auth import auth_backend
from controllers.auth.database import User
from controllers.auth.manager import get_user_manager
from controllers.auth.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title="KinoHub")
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get('/protected-route')
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"

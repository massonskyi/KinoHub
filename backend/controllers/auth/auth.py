from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from config import SECRET_COOKIE

cookie_transport = CookieTransport(
    cookie_name="UNC",
    cookie_max_age=3600
)

SECRET = SECRET_COOKIE


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)

from fastapi import FastAPI

from auth import auth_router
from product import product_router
from schemas import JwtModel
from fastapi_jwt_auth import AuthJWT

app = FastAPI()

@AuthJWT.load_config
def config():
    return JwtModel()

app.include_router(auth_router)
# app.include_router(category_router)
# app.include_router(order_router)
app.include_router(product_router)


@app.get("/")
async def landing():
    return {"message": "This is landing page"}
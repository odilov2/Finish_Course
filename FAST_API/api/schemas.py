from datetime import date

from pydantic import BaseModel
from typing import Optional


class RegisterModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class LoginModel(BaseModel):
    username: str
    password: str


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    description: str
    count: int
    price: float
    image: str


class RecentProductModel(BaseModel):
    id: Optional[int]
    description: str
    count: int
    price: float
    image: str
    create_date: date


class OrderModel(BaseModel):
        id: Optional[int]
        users_id: int
        product_id: int


class UsersModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    image: str
    first_name: str
    last_name: str
    description: str


class UsersProductModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str


class TeamsModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    image: str
    first_name: str
    last_name: str
    position: str


class CategoryModel(BaseModel):
    id: Optional[int]
    name: str

class JwtModel(BaseModel):
    authjwt_secret_key: str = 'd23adc351e934a4badbd93fe268f9ac26b86db1a347488d8864d72652af65d53'


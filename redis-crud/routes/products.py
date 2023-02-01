from fastapi import APIRouter

from schemas import products
from db import crud

# from data.products import data # only for test

router = APIRouter()


@router.get("/")
def root():
    return "Example"


@router.get("/all", response_model=list[products.Product])
def get_all():
    products = crud.get_all_hash()
    return products


# @router.post("/create", response_model=products.Product)
@router.post("/create")
def create_product(product: products.Product):
    try:
        # data.append(product.dict())

        crud.save_hash(key=product.id, data=product.dict())

        return product
    except Exception as e:
        return e


@router.get("/product/{id}")
def get_product(id: str):
    try:
        # products = list(filter(lambda product: product["id"] == id, data))
        # product = products[0]

        product = crud.get_hash(key=id)

        return product
    except Exception as e:
        return e


@router.delete("/product/{id}")
def delete_product(id: str):
    try:
        # products = list(filter(lambda product: product["id"] == id, data))
        # product = products[0]
        # data.remove(product)
        keys = products.Product.__fields__.keys()

        product = crud.get_hash(key=id)

        if product:
            crud.delete_hash(key=id, keys=keys)

        return product
    except Exception as e:
        return e

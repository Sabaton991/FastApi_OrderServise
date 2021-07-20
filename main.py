from fastapi import FastAPI
from routers import user, orders, items
app = FastAPI()


app.include_router(user.router)
app.include_router(orders.router)
app.include_router(items.router)


@app.get('/')
def base_route():
    return {'data': 'Hello'}





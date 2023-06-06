from fastapi import Body, FastAPI, Path, Query

from constants import ModelName
from models import Item, User


app = FastAPI()


@app.get("/")
async def root():
    """First steps"""
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item, extra_param: str | None = None):
    """
    Request body
     * FastAPI recognises function parameters that match path parameters should be taken from the
       path, and that function parameters that are Pydantic models should be taken from the
       request body
    """
    payload = {**item.dict()}

    if extra_param:
        payload.update({"extra_param": extra_param})
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Path parameters - Predefined values
     * Path parameter with type annotation using `ModelName` will make the enum values of
       `ModelName` available as options in the interactive docs. I wonder how the docs does this
       and this functionality be used in e.g. form drop down options? Perhaps using OPTIONS?
    """
    payload = {"model_name": model_name, "message": ""}

    if model_name is ModelName.alexnet:
        payload["message"] = "Deep learning FTW!"
    elif model_name is ModelName.lenet:
        payload["message"] = "LeCNN all the images"

    return payload


@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(title="The ID of the item to get"),
    skip: int = 0,
    limit: int = 10,
    extra_param: str | None = Query(default=None, max_length=50),
    my_bool: bool = False,
):
    """
    Path parameters - Pydantic
     * `item_id` input type declaration is used by `FastAPI` to validate input data using
       `Pydantic`, but I don't think is standard within Python we have to use it explicitly
     * Type declaration is also used to set the `item_id` return value type
       Query parameters
     * Other function parameters are interpreted as querystring parameters if they don't have path
       parameters
     * Giving default values to these function parameters will set the values to defaults if the
       request querystring doesn't provide them
     * We can also have purely optional functional parameters
     * FastAPI can deal with lots of `boolean` type strings as query parameters (like 'yes',
       'true', 'on' etc) and if the query param type is `bool` will cast to a valid boolean
    Query parameters and string validation
     * Use the `Query` class to add validation to query parameters. Not sure I like this
       implementation, a lot of this will end up making the function def look a complete mess.
    Path parameters and numeric validations
     * Use the `Path` class to add validation to path parameters.
    """
    payload = {"item_id": item_id, "skip": skip, "limit": limit, "my_bool": my_bool}

    if extra_param:
        payload.update({"extra_param": extra_param})

    return payload


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(),
    extra_param: str | None = None,
):
    """
    Body - Multiple Parameters
     * If you declare multiple body parameters as Pydantic models, FastAPI will expect them to be
       posted as nested json
     * You can add a singular item as part of the request body using `Body`
    """
    payload = {
        "importance": importance,
        "item": item.dict(),
        "item_id": item_id,
        "user": user.dict(),
    }

    if extra_param:
        payload.update({"extra_param": extra_param})
    return payload

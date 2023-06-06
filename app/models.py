from pydantic import BaseModel, HttpUrl, Field


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    """
    Body - Fields
     * You can declare validation and metadata inside of Pydantic models using `Field`
    Body - nested models
     * Use can define a model attribute to be a subtype like `list`. Using `set` will also strip
       out any duplicates
    """

    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="Price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class User(BaseModel):
    usename: str
    full_name: str | None = None

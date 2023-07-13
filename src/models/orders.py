from pydantic import BaseModel


class Orders(BaseModel):
    id : int
    id_client : int
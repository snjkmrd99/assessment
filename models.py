from fastapi import Query
from pydantic import BaseModel, validator

class CalcGetRequest(BaseModel):
    expression: str = Query(None, max_length=50)


class CalcPostRequest(BaseModel):
    first: int
    last: int
    operator: str
    @validator('operator')
    def onlySimpleMath(cls, v):
        if v == '*' or v == '/' or v == '-' or v == '+':
            return v
        raise ValueError('only a simple mathematical query is possible')


class CalcResponce(BaseModel):
    result: str = None
    operation: str = None
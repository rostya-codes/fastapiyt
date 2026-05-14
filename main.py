from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI


app = FastAPI()

data = {
    'email': 'abc@mail.com',
    'bio': 'desc',
    'age': 12,
}

data_wo_age = {
    'email': 'abc@mail.com',
    'bio': 'desc',
    # 'gender': 'male',
    # 'born': '2022'
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)

    model_config = ConfigDict(extra='forbid')


users = []


@app.post('/users')
def add_user(user: UserSchema):
    users.append(user)
    return {'ok': True, 'msg': 'user added'}


@app.get('/users')
def get_users() -> list[UserSchema]:
    return users


# class UserAgeSchema(UserSchema):
#     age: int = Field(ge=0, le=130)


# user = (UserSchema(**data))
# print(user)
#

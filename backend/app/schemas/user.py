from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.models.user import UserRole


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    role: UserRole = UserRole.USER
    is_active: bool = True


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = Field(default=None, min_length=8)
    is_active: bool | None = None


class UserRead(UserBase):
    id: int
    is_verified: bool
    telegram_id: int | None = None
    telegram_username: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

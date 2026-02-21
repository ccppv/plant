from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.core.dependencies import CurrentUser, CurrentAdmin, DBSession
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_my_profile(current_user: CurrentUser) -> User:
    return current_user


@router.patch("/me", response_model=UserRead)
async def update_my_profile(
    user_in: UserUpdate, current_user: CurrentUser, db: DBSession
) -> User:
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    if user_in.password is not None:
        current_user.hashed_password = get_password_hash(user_in.password)
    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    return current_user


# Admin-only endpoints
@router.get("", response_model=list[UserRead], dependencies=[])
async def list_users(current_admin: CurrentAdmin, db: DBSession) -> list[User]:
    result = await db.execute(select(User).order_by(User.id))
    return list(result.scalars().all())


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, current_admin: CurrentAdmin, db: DBSession) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

from fastapi import HTTPException, status
from uuid import UUID

from src.Job.models import Job
from src.Transaction.schemas import TransactionType
from src.User.schemas import UserSchema, UserInfo
from src.UserAttribute.models import UserAttribute
from src.auth.UserManager import UserManager
from src.utils.UnitOfWork import InterfaceUnitOfWork


class UserService:

    async def get_all_users(self, uow: InterfaceUnitOfWork):
        """delete after testing"""
        async with uow:
            place_title = await uow.user.get_all()
            return place_title

    async def check_user_exist(self, uow: InterfaceUnitOfWork, **filter_by):
        """Проверяет существование пользователя по соответсвию полей"""
        async with uow:
            result = await uow.user.find_by_filter(**filter_by)
        return len(result) > 0

    async def register_user(
        self, uow: InterfaceUnitOfWork, user: UserSchema
    ) -> UserSchema:
        """Регистрация нового пользователя"""
        user_data = user.model_dump()
        async with uow:
            if await self.check_user_exist(uow=uow, email=user_data["email"]):
                raise HTTPException(
                    status_code=401,
                    detail={"warning": "email address is already taken"},
                )
            if await self.check_user_exist(uow=uow, login=user_data["login"]):
                raise HTTPException(
                    status_code=401, detail={"warning": "username is already taken"}
                )
            user_data["hashed_password"] = UserManager().hash_password(
                user_data["hashed_password"]
            )
            await uow.user.add_one(user_data)
        return user

    async def append_user_attribute(
        self, uow: InterfaceUnitOfWork, user_id: UUID, attr_id: UUID
    ) -> dict:
        """Добавление аттрибута пользователя"""
        async with uow:
            result = await uow.user.append_many_to_many_elem(
                user_id=user_id,
                elem_model=UserAttribute,
                elem_id=attr_id,
                row_name="attributes",
            )
        return result

    async def unassign_with_job(
        self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID
    ) -> dict:
        """Удаление связи с таблицей Job"""
        async with uow:
            result = await uow.user.remove_many_to_many_elem(
                user_id=user_id,
                elem_model=Job,
                elem_id=job_id,
                row_name="assigned_jobs",
            )
        return result

    async def unassign_with_attribute(
        self, uow: InterfaceUnitOfWork, user_id: UUID, attr_id: UUID
    ) -> dict:
        """Удаление аттрибута пользователя"""
        async with uow:
            result = await uow.user.remove_many_to_many_elem(
                user_id=user_id,
                elem_model=UserAttribute,
                elem_id=attr_id,
                row_name="attributes",
            )
        return result

    async def remove_user(self, uow: InterfaceUnitOfWork, user_id: UUID):
        """Удаление пользователя"""
        async with uow:
            result = await uow.user.delete_one(id=user_id)
        return result

    async def get_user_by_id(self, uow: InterfaceUnitOfWork, user_id: UUID):
        """Получение пользователя по id"""
        async with uow:
            result = await uow.user.find_by_filter(id=user_id)
        return UserInfo(
            id=result[0].id,
            full_name=result[0].full_name,
            login=result[0].login,
            email=result[0].email,
            is_active=result[0].is_active,
        )

    async def update_user_data(
        self, uow: InterfaceUnitOfWork, user_id: UUID, **update_data
    ):
        """Обновление данных пользователя"""
        async with uow:
            elem = await uow.user.find_by_filter(id=user_id)
            result = await uow.user.update_value(elem=elem[0], **update_data)
        return result

    async def response_for_job(
        self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID
    ):
        """Откликнуться от имени пользователя на вакансию"""
        async with uow:
            elem = await uow.user.append_many_to_many_elem(
                user_id=user_id,
                elem_model=Job,
                elem_id=job_id,
                row_name="assigned_jobs",
            )
        return elem

    async def get_user_balance(self, uow: InterfaceUnitOfWork, user) -> int:
        """Получение баланса пользователя"""
        async with uow:
            transaction_list = await uow.user.get_all_relationship_elements(
                user_id=user["id"], row_name="transactions_list"
            )
            balance = 0
            for elem in transaction_list:
                if elem.type == TransactionType.DEPOSIT:
                    balance += int(elem.amount)
                elif elem.type == TransactionType.WITHDRAWAL:
                    balance -= int(elem.amount)
                else:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"unexpected transaction type - {elem.type}",
                    )
            return balance

    async def get_user_assigned_jobs(self, uow: InterfaceUnitOfWork, user):
        result = await uow.user.get_user_assigned_jobs_with_status(
            user_id=user["id"])
        return result

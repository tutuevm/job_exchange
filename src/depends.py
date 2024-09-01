from typing import Annotated, Dict

from fastapi import Depends

from src.auth.UserManager import IUserManager, UserManager
from src.utils.UnitOfWork import InterfaceUnitOfWork, UnitOfWork

UOWDependence = Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)]

UserManagerDependence = Annotated[IUserManager, Depends(UserManager)]

UserPayloadDependence = Annotated[
    Dict, Depends(UserManager().get_current_auth_user_payload)
]

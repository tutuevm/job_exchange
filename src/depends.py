from typing import Annotated

from fastapi import Depends

from src.utils.UnitOfWork import InterfaceUnitOfWork, UnitOfWork

UOWDependence = Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)]
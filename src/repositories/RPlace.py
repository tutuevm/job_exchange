from src.utils.repository import SQLAlchemyRepository
from src.models.Place import Place


class PlaceRepository(SQLAlchemyRepository):
    model = Place

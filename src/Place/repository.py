from src.Place.models import Place
from src.utils.repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    model = Place

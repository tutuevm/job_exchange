from src.database import async_session_maker


class UnitOfWork:

    def __init__(self):
        self.session_maker = async_session_maker

    async def __aenter__(self):
        self.session = self.session_maker()

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        self.session.rollback()

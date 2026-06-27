from typing import Generic, Protocol, TypeVar
from uuid import UUID
from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.specifications.base import Specification

ModelT = TypeVar("ModelT")

class Repository(Protocol[ModelT]):
    async def get(self, id: UUID) -> ModelT | None: ...
    async def add(self, entity: ModelT) -> ModelT: ...
    async def list(self, specification: Specification | None = None) -> list[ModelT]: ...
    async def delete(self, entity: ModelT) -> None: ...

class SqlAlchemyRepository(Generic[ModelT]):
    def __init__(self, session: AsyncSession, model: type[ModelT]):
        self.session = session
        self.model = model

    async def get(self, id: UUID) -> ModelT | None:
        return await self.session.get(self.model, id)

    async def add(self, entity: ModelT) -> ModelT:
        self.session.add(entity)
        return entity

    async def list(self, specification: Specification | None = None) -> list[ModelT]:
        statement: Select = select(self.model)
        if specification:
            statement = statement.offset((specification.page - 1) * specification.per_page).limit(specification.per_page)
            for sort in specification.sorts:
                column = getattr(self.model, sort.field)
                statement = statement.order_by(column.desc() if sort.descending else column.asc())
        result = await self.session.scalars(statement)
        return list(result.all())

    async def delete(self, entity: ModelT) -> None:
        if hasattr(entity, "deleted_at"):
            from datetime import UTC, datetime
            entity.deleted_at = datetime.now(UTC)
        else:
            await self.session.delete(entity)

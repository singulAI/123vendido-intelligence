from collections.abc import Awaitable, Callable
from pydantic import BaseModel

class DomainEvent(BaseModel):
    name: str
    payload: dict = {}

EventHandler = Callable[[DomainEvent], Awaitable[None]]

class InMemoryEventBus:
    def __init__(self):
        self._handlers: dict[str, list[EventHandler]] = {}
    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        self._handlers.setdefault(event_name, []).append(handler)
    async def publish(self, event: DomainEvent) -> None:
        for handler in self._handlers.get(event.name, []):
            await handler(event)

EVENTS = ["EditalPublicado", "UploadFinalizado", "LotesImportados", "VeiculoAtualizado", "AnaliseGerada", "ScoreAtualizado", "UsuarioNotificado"]

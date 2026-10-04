from datetime import datetime, timezone
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

# --- Имена топиков ---
TOPIC_CREATED = "crm.customer.created"
TOPIC_REGISTERED = "crm.customer.registered"
TOPIC_FAILED = "crm.customer.failed"
TOPIC_DLQ = "crm.customer.dlq"


def _now() -> datetime:
    return datetime.now(timezone.utc)


# --- Данные клиента ---
class CustomerBase(BaseModel):
    name: str
    name_alias: str | None = None
    prospect: bool | None = None
    customer: bool | None = None
    customer_code:str | None = None
    address: str | None = None
    zipcode: str | None = None # почтовый индекс
    town: str | None = None
    country: str | None = None
    # Штат/Провинция (после утсановки страны) не получается выбрать из списка (пусто)
    phone: str | None = None
    fax: str | None = None
    url: str | None = None # сайт
    email: str | None = None
    idprof1: str | None = None
    idprof2: str | None = None
    idprof3: str | None = None
    idprof4: str | None = None
    idprof5: str | None = None
    idprof6: str | None = None
    assujtva_value: bool | None = None # Используется налог с продаж checkbox
    tva_intra: str | None = None # Код плательщика НДС
    euid: str | None = None # EUID


class CustomerMore(CustomerBase):
    pass

class Customer(CustomerMore):
    pass


# --- События (то, что лежит в Kafka) ---
class CustomerCreated(BaseModel):
    """Заявка создана. Робот читает это из топика crm.customer.created."""
    schema_version: int = 1
    event_id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    attempt: int = 0
    occurred_at: datetime = Field(default_factory=_now)
    customer: Customer


class RegisterResult(BaseModel):
    """Итог работы робота. Уходит в registered / failed / dlq."""
    schema_version: int = 1
    event_id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    status: Literal["registered", "failed", "error"]
    attempt: int = 0
    occurred_at: datetime = Field(default_factory=_now)
    customer_id: int | None = None   # socid из Dolibarr
    error: str | None = None

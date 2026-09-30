from uuid import UUID

from pydantic import BaseModel

from shared.customer import Customer


class CustomerCreated(BaseModel):
    event_id: UUID
    task_id: UUID
    customer: Customer

from pydantic import BaseModel


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

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    name_alias: str
    # лид, клиент, никто?
    customer_code:str | None = None
    address: str
    zipcode: str # почтовый индекс
    town: str
    # страна
    # Штат/Провинция (после утсановки страны)
    phone: str
    fax: str
    url: str # сайт
    email: str
    idprof1: str
    idprof2: str
    assujtva_value: bool # Используется налог с продаж checkbox
    tva_intra: str # Код плательщика НДС
    euid: str # EUID


class CustomerMore(CustomerBase):
    pass

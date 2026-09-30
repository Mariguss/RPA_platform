class BusinessException(Exception):
    ...   # данные плохие, повтор бессмысленен

class SystemException(Exception):
    ...     # сбой среды, можно повторить

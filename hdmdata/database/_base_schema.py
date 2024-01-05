from datetime import datetime
from pydantic import BaseModel, ConfigDict
from ._methods import save_model_to_db


TYPES_TO_IGNORE = (str, int, float, bool, datetime, list, None)


class BaseSchema(BaseModel):
    
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        arbitrary_types_allowed=True
        # revalidate_instances='always'
    )
    
    @staticmethod
    def _build_orm_objects(data):
        if not data:
            return
        for key, value in data:
            if type(value) not in TYPES_TO_IGNORE:
                orm_model = BaseSchema._build_orm_objects(getattr(data, key))
                setattr(data, key, orm_model)
            if isinstance(value, list):
                orm_model = []
                for item in value:
                    orm_model.append(BaseSchema._build_orm_objects(item))
                setattr(data, key, orm_model)
        return data.__orm_model__(**vars(data))

    @save_model_to_db
    def save(self):
        return BaseSchema._build_orm_objects(self)      

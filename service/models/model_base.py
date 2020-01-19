from enum import Enum


class ModelBase(object):
    def to_json(self):
        props = self.__dict__

        for key, value in props.items():
            if isinstance(value, ModelBase):
                props[key] = value.to_json()

            if isinstance(value, Enum):
                props[key] = value.value

        return props

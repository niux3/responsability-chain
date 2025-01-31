from sqlalchemy import or_
from .abstract_handler import AbstractHandler


class EqualsInsensitiveCaseHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 3:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(or_(column == value.lower(), column == value.upper()))
        return super().handle(query, filter_data)

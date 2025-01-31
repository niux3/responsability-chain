from .abstract_handler import AbstractHandler
from sqlalchemy import or_


class NotEqualsInsensitiveCaseHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 4:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(or_(column != value.lower(), column != value.upper()))
        return super().handle(query, filter_data)

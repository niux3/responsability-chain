from sqlalchemy import not_
from .abstract_handler import AbstractHandler


class NotEndHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 14:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(not_(column.endswith(value)))
        return super().handle(query, filter_data)

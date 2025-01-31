from sqlalchemy import not_
from .abstract_handler import AbstractHandler


class NotBeginHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 10:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(not_(column.startswith(value)))
        return super().handle(query, filter_data)

from .abstract_handler import AbstractHandler
from sqlalchemy import not_


class NotContainsHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 6:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(not_(column.like(f"%{value}%")))
        return super().handle(query, filter_data)

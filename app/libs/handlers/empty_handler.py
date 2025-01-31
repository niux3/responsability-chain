from sqlalchemy import or_
from .abstract_handler import AbstractHandler


class EmptyHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 17:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(or_(column == '', column == None))
        return super().handle(query, filter_data)

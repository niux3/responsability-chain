from .abstract_handler import AbstractHandler


class ContainsHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 5:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(column.like(f"%{value}%"))
        return super().handle(query, filter_data)

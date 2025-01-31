from .abstract_handler import AbstractHandler


class EqualsHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 1:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(column == value)
        return super().handle(query, filter_data)

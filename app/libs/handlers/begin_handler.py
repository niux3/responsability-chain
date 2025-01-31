from .abstract_handler import AbstractHandler


class BeginHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 9:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(column.startswith(value))
        return super().handle(query, filter_data)

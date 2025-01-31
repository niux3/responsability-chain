from .abstract_handler import AbstractHandler


class EndHandler(AbstractHandler):
    def handle(self, query, filter_data):
        if filter_data.get("comparator") == 13:
            column = filter_data["column"]
            value = filter_data["value"]
            query = query.filter(column.endswith(value))
        return super().handle(query, filter_data)

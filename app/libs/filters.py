from app.models import User, Company
from app.forms import data_field_0, filters, fields_company, fields_users
import app.libs.handlers as handlers_module


class Filters:
    @staticmethod
    def build_conditions(data):
        filter_conditions = []
        i = 0
        translate = {
            'company': {
                'model': Company,
                'fields': list(fields_company.values())
            }, 
            'user': {
                'model': User,
                'fields': list(fields_users.values())
            }
        }
        while True:
            fields_form = [
                f'field_{i}',
                f'field_filter_{i}',
                f'field_value_{i}',
            ]
            if any([f not in data.keys() for f in fields_form]):
                break
            # TODO : récupérer diretement le nom du champs comme ça, ça me parait risquer
            key_model, key_column_name = data[fields_form[0]].split('_')
            column_name = translate[key_model]['fields'][int(key_column_name)]

            # key_comparator = int(data[fields_form[1]])
            # comparator = filters[key_comparator]
            comparator = int(data[fields_form[1]])
            value = data[fields_form[2]]

            column = getattr(translate[key_model]['model'], column_name)
            filter_conditions.append({
                "column": column,
                "comparator": comparator,
                "value": value
            })
            i += 1
        return filter_conditions

    @staticmethod
    def execute(query, filter_conditions):
        handlers = {name: cls() for name, cls in vars(handlers_module).items() if isinstance(cls, type) and name != 'AbstractHandler'}
        handler_instances = list(handlers.values())
        for i in range(len(handler_instances) - 1):
            handler_instances[i].set_next(handler_instances[i + 1])
        first_handler = handler_instances[0]
        for condition in filter_conditions:
            query = first_handler.handle(query, condition)
        return query

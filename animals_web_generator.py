from data.data_service import load_data
from animals_file_management import read_html_template, write_html_content



animals_data = load_data()

fields_to_print = {
    "name": lambda x: x,
    "characteristics_diet": lambda x: x['diet']  if isinstance(x, dict) and x.get('diet') else None,
    "locations": lambda x: x[0] if isinstance(x, list) and x else None,
    "characteristics_type": lambda x: x['type'] if isinstance(x, dict) and x.get('type') else None,

}

output = ''

for animal in animals_data:
    for field, handler in fields_to_print.items():

        if '_' in field:
            field = field.split('_')
            base_key = field[0]
            actual_key =  field[1]
        else:
            base_key = field
            actual_key = field

        value = animal.get(base_key)
        if value is not None:
            processed = handler(value)
            if processed:
                output += f"{actual_key.title()}: {processed.title()} \n"


html_template = read_html_template()
html_template = html_template.replace('__REPLACE_ANIMALS_INFO__', output)
write_html_content(html_template)


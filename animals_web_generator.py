from data.data_service import load_data

animals_data = load_data()

fields_to_print = {
    "name": lambda x: x,
    "characteristics_diet": lambda x: x['diet']  if isinstance(x, dict) and x.get('diet') else None,
    "locations": lambda x: x[0] if isinstance(x, list) and x else None,
    "characteristics_type": lambda x: x['type'] if isinstance(x, dict) and x.get('type') else None,

}

for animal in animals_data:
    print()
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
                print(f"{actual_key}: {processed}")

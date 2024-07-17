def transform_data(data: dict) -> dict:
    """
    Apply a simple transformation to the input data.
    
    For this example, we will:
    - Convert the name to uppercase.
    - Add a new field 'is_adult' which is True if age >= 18.
    
    :param data: The original data dictionary.
    :return: The transformed data dictionary.
    """
    transformed_data = data.copy()
    transformed_data['name'] = transformed_data['name'].upper()
    transformed_data['is_adult'] = transformed_data['age'] >= 18
    return transformed_data

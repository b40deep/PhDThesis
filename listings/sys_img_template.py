image_prompt = f'''
    {"cartoon illustration of " if toon else ""}
    {selected_patient_name} is a {financial_status} {selected_patient_attr} patient from {patient_location}, 
    {prompt},
    {"cartoon illustration, comic book style, digital" if toon else ""}
    '''
def create_person(first_name: str, 
                  last_name: str, 
                  /, 
                  age: int, 
                  gender: int, 
                  *, 
                  size: int = 1.83, 
                  job: str = 'taxidermist') -> dict:
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender,
        'size': size,
        'job': job,
    }

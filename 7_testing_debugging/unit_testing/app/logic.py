def is_available_for_loan(income:float, age: int, employeement_status: str) -> bool:
    return (income >= 50000) and (age >= 21) and (employeement_status == "employed" )



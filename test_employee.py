#$test_employee.py
import pytest
from employeedetails import get_employee_info
def test_get_employee_info():
    #sample data
    name="Alice Smith"
    id="E202"
    department="HR"
    salary=60000
    #expected output
    expected_output=(
        "employee Name:Alice Smith,\n"
        "employee_id:E202,\n"
        "employee_id:HR,\n"
      "salary:60000.00"
    )
    #Assertion
    assert get_employee_info(name, id, department, salary) == expected_output

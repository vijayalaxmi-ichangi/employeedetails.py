def get_employee_info(name, id, department, salary):
    """
    Returns a formatted string containing employee details.
    """
    return (
        f"employee Name:{name},\n"
        f"employee_id:{id},\n"
        f"employee_id:{department},\n"
        f"salary:{salary:.2f}"
    )
    
if __name__ == "__main__":
    print(get_employee_info("john doe", "E101", "IT", 55000))
from server import mcp
from utils.file_reader import read_csv

@mcp.tool()
def get_leave_balance(employee_id: int) -> str:
    """
    Given an employee ID, return the leave balance for that employee from attendance.csv.

    Args:
        employee_id: The ID of the employee.

    Returns:
        A string describing the employee's leave balance.
    """
    df = read_csv('attendance.csv')
    row = df[df['id'] == employee_id]
    if row.empty:
        return f"Employee with ID {employee_id} not found."
    name = row.iloc[0]['name']
    leave_balance = row.iloc[0]['leave_balance']
    return f"Employee: {name} (ID: {employee_id}) has a leave balance of {leave_balance}."

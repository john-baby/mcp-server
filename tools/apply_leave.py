from server import mcp
from utils.file_reader import read_csv
import pandas as pd

@mcp.tool()
def apply_leave(employee_id: int) -> str:
    """
    Decrement the leave balance by 1 for the given employee in attendance.csv and return the updated balance.

    Args:
        employee_id: The ID of the employee.

    Returns:
        A string describing the updated leave balance along with their name.
    """
    df = read_csv('attendance.csv')
    row = df[df['id'] == employee_id]
    if row.empty:
        return f"Employee with ID {employee_id} not found."
    
    idx = row.index[0]
    if df.at[idx, 'leave_balance'] <= 0:
        return f"Employee {df.at[idx, 'name']} (ID: {employee_id}) has no remaining leave balance."
    df.at[idx, 'leave_balance'] -= 1

    from utils.file_writer import save_csv
    save_csv(df,'attendance.csv')

    return f"Employee: {df.at[idx, 'name']} (ID: {employee_id}) now has a leave balance of {df.at[idx, 'leave_balance']}."

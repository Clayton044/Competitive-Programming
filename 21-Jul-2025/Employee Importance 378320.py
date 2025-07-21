# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}

        def dfs(eid):
            employee = emp_map[eid]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)
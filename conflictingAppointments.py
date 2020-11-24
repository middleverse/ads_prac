# ========================
# Conflicting Appointments
# ========================

# Given an array of intervals representing ‘N’ appointments, 
# find out if a person can attend all the appointments.
# EXAMPLES
# 1. Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
# 2. Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

def can_attend_all_appointments(intervals):
    start, end = 0, 1
    i = 0
    intervals.sort(key = lambda x: x[0])
    while (i < len(intervals) - 1):
        if (intervals[i][end] >= intervals[i+1][start]):
            return False
        i += 1
    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()

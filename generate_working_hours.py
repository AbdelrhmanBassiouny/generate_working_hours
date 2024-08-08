import numpy as np
from typing import List

low = 6  # min hours per day
high = 10  # max hours per day
divisions_per_hour = 5
possible_values: List = np.arange(low, high, 0.25).tolist()
n_months = 7
vacation_days = [10, 0, 1, 13, 3, 4, 0]
days_per_month = [23, 21, 21, 22, 23, 20, 23]
tolerance_for_total_hours_of_whole_period = 8

while True:
    all_daily_working_hours = []
    all_monthly_working_hours = []
    total_hours_per_month = 0
    for m in range(n_months):
        per_month_daily_working_hours = []
        for i in range(days_per_month[m] - vacation_days[m]):
            hours_per_day_idx = np.random.randint(len(possible_values))
            hours_per_day = possible_values[hours_per_day_idx]
            per_month_daily_working_hours.append(hours_per_day)
            all_daily_working_hours.append(hours_per_day)
        all_monthly_working_hours.append(per_month_daily_working_hours)
    print(sum(all_daily_working_hours), "should be close to", 143*n_months,
          "error:", sum(all_daily_working_hours) - 143*n_months)
    if np.isclose(sum(all_daily_working_hours), 143*n_months, atol=tolerance_for_total_hours_of_whole_period):
        break

# print(all_daily_working_hours)
print(sum(all_daily_working_hours))
arr = np.array(all_monthly_working_hours)
print(arr)

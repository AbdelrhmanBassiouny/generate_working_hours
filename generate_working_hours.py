import numpy as np

low = 6  # min hours per day
high = 10  # max hours per day
step = 0.25
possible_values = np.arange(low, high + step, step)

n_months = 7
vacation_days = [10, 0, 1, 13, 3, 4, 0]
days_per_month = [23, 21, 21, 22, 23, 20, 23]
required_total_hours = 143 * n_months

tolerance_for_total_hours_of_whole_period = 0
debug = False  # to see if the total hours are close to 143*n_months and adjust the tolerance or low/high values.

while True:

    all_daily_working_hours = []
    all_monthly_working_hours = []

    for m in range(n_months):

        per_month_daily_working_hours = []

        for i in range(days_per_month[m] - vacation_days[m]):
            hours_per_day_idx = np.random.randint(len(possible_values))
            hours_per_day = possible_values[hours_per_day_idx]
            per_month_daily_working_hours.append(hours_per_day)
            all_daily_working_hours.append(hours_per_day)

        all_monthly_working_hours.append(per_month_daily_working_hours)

    if debug:
        print(sum(all_daily_working_hours), "should be close to", required_total_hours,
              "error:", sum(all_daily_working_hours) - required_total_hours)

    if np.isclose(sum(all_daily_working_hours), required_total_hours, atol=tolerance_for_total_hours_of_whole_period):
        break

print(f"Total working hours = {sum(all_daily_working_hours)}")
for i, row in enumerate(all_monthly_working_hours):
    print(f"Month {i}: {row}, total: {sum(row)}")

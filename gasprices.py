from collections import defaultdict #for storing data in defaultdict
from datetime import datetime #for handling the dates
def main():
    #Read the gas prices from the 'gas_prices.txt file:
    with open('gas_prices.txt', 'r') as file:
        gas_data = file.readlines()

    yearly_data = defaultdict(list)
    monthly_data = defaultdict(lambda: defaultdict(list))

    #Store each line in the file
    for entry in gas_data:
        date_str, price_str = entry.strip().split(':')
        date = datetime.strptime(date_str, '%m-%d-%Y')
        year = date.year
        month = date.strftime('%B')

        # Store data for yearly report
        yearly_data[year].append(float(price_str))

        # Store data for monthly report
        monthly_data[year][month].append(float(price_str))

    # Write the report to gas_report.txt
    with open('gas_report.txt', 'w') as report_file:
        for year, prices in sorted(yearly_data.items()):
            low_price = min(prices)
            avg_price = sum(prices) / len(prices)
            high_price = max(prices)

            # Write yearly report
            report_file.write(f"{year}:\n")
            report_file.write(f"  Low: ${low_price:.2f}, Avg: ${avg_price:.2f}, High: ${high_price:.2f}\n")

            # Write monthly report in  order
            for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                          'October', 'November', 'December']:
                if month in monthly_data[year]:
                    monthly_avg = sum(monthly_data[year][month]) / len(monthly_data[year][month])
                    report_file.write(f"  {month:<9} ${monthly_avg:.2f}\n")

            report_file.write("\n")


if __name__ == "__main__":
    main()

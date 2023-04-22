from datetime import datetime

std_date = "2023-04-08"
ddmm = datetime.strptime(std_date, "%Y-%m-%d").strftime("%d-%b")


print(ddmm)


def date_reformat(std_date):
    ddmm = datetime.strptime(std_date, "%Y-%m-%d").strftime("%d-%b")
    return ddmm


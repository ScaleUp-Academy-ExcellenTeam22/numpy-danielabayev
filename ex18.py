import numpy


def days_in_month(month: int, year: int) -> numpy.timedelta64:
    """
    A NumPy program to count the number of days of specific month.
    :param month:
    :param year:
    :return: number of days in this month.
    """
    date = 0

    # December case
    if month == 12:
        end = str(year) + '-' + str(month) + '-31'
        begin = str(year) + '-' + str(month) + '-01'
        date = 1

    else:
        # single digit months
        if month < 10:
            end_month = '-0' + str(month + 1)
            begin_month = '-0' + str(month)

        # double digit months
        else:
            end_month = '-' + str(month + 1)
            begin_month = '-' + str(month)

        end = str(year) + end_month + '-01'
        begin = str(year) + begin_month + '-01'

    # return number of days
    return numpy.datetime64(end) - numpy.datetime64(begin) + date


if __name__ == '__main__':
    print(days_in_month(12, 2022))

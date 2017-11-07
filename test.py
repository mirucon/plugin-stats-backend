import re
import datetime
wp_current = '4.9'


def validation(val):
    if re.search(r"\d", val):
        o = re.search(r"\d(.\d)?(.\d)?", val)
        o = o.group()

        if re.search(r"\d\d", o):
            return False

        if re.search(r"/", o):
            o = o.replace("/", ".")

        if re.search(r",", o):
            o = o.replace(",", ".")

        if re.fullmatch(r"\d", o):
            o = o + '.0'

        if re.fullmatch(r"\d.\d.\d", o):
            o = re.search(r"\d.\d", o)
            o = o.group()

        if o < wp_current:
            return False

        return (o)

    else:
        return False

# print(validation('4/9'))


def rel_time(val):
    cur_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    cur_time = datetime.datetime.strptime(cur_time, '%Y-%m-%d %H:%M:%S')
    print(cur_time)
    try:
        val = datetime.datetime.strptime(val, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return False

    val = cur_time - val
    val = val.days

    if 0 <= val < 30:
        o = 'Within a month ago'

    elif 30 < val < 90:
        o = '1 month ago'

    elif 90 < val < 180:
        o = '3 months ago'

    elif 180 < val < 365:
        o = '6 months ago'

    elif 365 < val < 730:
        o = 'a year ago'

    elif 730 < val < 1460:
        o = '2 years ago'

    elif 1460 < val:
        o = 'More than 4 years ago'

    else:
        return False

    return o

print(rel_time('-001-11-30T00:00:00'))

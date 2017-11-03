import re
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

        if o > wp_current:
            return False

        return (o)

    else:
        return False

print(validation('9.9'))
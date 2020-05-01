# key value pair of format: formatter class
formatters = {}


def register(format_, formatterClass):
    formatters[format_] = formatterClass

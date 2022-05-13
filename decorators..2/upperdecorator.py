def to_upper(func):
    def inner():
        return func().upper()
    return inner


def get_name():
    return "hello,world"
print(get_name())
import time


class DateTimeConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        time_array = time.strptime(value, "%Y-%m-%d-%H-%M-%S")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def to_url(self, value):
        time_array = time.localtime(value)
        time_string = time.strftime("%Y-%m-%d-%H-%M-%S", time_array)
        return time_string


class NumberListConverter:
    regex = r'[0-9]+(,[0-9]+)*'

    def to_python(self, value):
        item_list = [int(i) for i in value.split(",")]
        return item_list

    def to_url(self, value):
        item_string = ','.join([str(int(i)) for i in value])
        return item_string


class FloatConverter:
    regex = r'[0-9]+\.[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

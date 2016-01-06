# -*- coding: utf-8 -*-


class Condition(object):
    operator = ''

    def __init__(self, operator):
        super(Condition, self).__init__()
        self.operator = operator

    def equal(self, value1, value2):
        return (str(value1) == str(value2))

    def nequal(self, value1, value2):
        return (str(value1) != str(value2))

    def gthan(self, value1, value2):
        return (float(value1) > float(value2))

    def lthan(self, value1, value2):
        return (float(value1) < float(value2))

    def test(self, value1, value2):
        if (self.operator == 'equal'):
            return self.equal(value1, value2)
        elif(self.operator == 'nequal'):
            return self.nequal(value1, value2)
        elif(self.operator == 'gthan'):
            return self.gthan(value1, value2)
        elif(self.operator == 'lthan'):
            return self.lthan(value1, value2)

        return False
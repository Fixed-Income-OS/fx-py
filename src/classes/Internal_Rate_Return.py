import numpy_financial as npf


class InternalRateReturn:
    def __init__(self, price, cash_flow):
        self.price = price
        self.cash_flow = cash_flow

    def calculate(self):
        self.cash_flow.insert(0, self.price)
        return round(npf.irr(self.cash_flow) * 100)

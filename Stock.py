class Stock:
    def __init__(self, lot, avg_price):
        self.lot = lot
        self.avg_price = avg_price

    def __repr__(self):
        return f"Stock(lot={self.lot}, avg_price={self.avg_price})"
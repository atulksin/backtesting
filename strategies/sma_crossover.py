from backtesting impoart Strategy
from backtesting.lib import crossover

clas SMACrossover(Strategy):
    n1 = 10 # Short-term SMA period
    n2 = 30 # Long-term SMA period

    def init(self):
        # Compute moving averages
        self.sma1 = self.I(SMA, self.data.Close.rolling, self.n1)
        self.sma2 = self.I(SMA, self.data.Close.rolling, self.n2)

    def next(self):
        # If short-term SMA crosses above long-term SMA, buy
        if crossover(self.sma1, self.sma2):
            self.buy()
        # If short-term SMA crosses below long-term SMA, sell
        elif crossover(self.sma2, self.sma1):
            self.sell() 


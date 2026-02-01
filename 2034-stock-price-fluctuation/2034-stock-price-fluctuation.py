class StockPrice:

    def __init__(self):
        self.priceTracker = {}
        self.max_heap = []
        self.min_price = []
        self.max_price = []
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:

        heapq.heappush(self.max_heap,(-timestamp,price))
        self.priceTracker[timestamp] = price
        self.latest = max(self.latest,timestamp)
        heapq.heappush(self.min_price,(price,timestamp))
        heapq.heappush(self.max_price,(-price,timestamp)) 




    def current(self) -> int:
        # print(self.max_heap)
        return self.priceTracker[self.latest]

    def maximum(self) -> int:
        while -self.max_price[0][0] != self.priceTracker[self.max_price[0][1]]:
            p,t = heapq.heappop(self.max_price)
            heapq.heappush(self.max_price,(-self.priceTracker[t],t))

        return -self.max_price[0][0]

    def minimum(self) -> int:
        while self.min_price[0][0] != self.priceTracker[self.min_price[0][1]]:
            p,t = heapq.heappop(self.min_price)
            heapq.heappush(self.min_price,(self.priceTracker[t],t))

        return self.min_price[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
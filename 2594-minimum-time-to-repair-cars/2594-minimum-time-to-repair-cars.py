class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        return bisect_left(range(max(ranks) * cars * cars), cars, key=lambda x: sum(floor(math.sqrt(x // r)) for r in ranks))
        
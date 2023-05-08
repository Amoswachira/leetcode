class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        daysInWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #1
        DaysByMonthMod7 = [0,3,2,5,0,3,5,1,4,6,2,4]; # 2
        if(month < 3) : year = year - 1 # 3
        return daysInWeek[(year + (year//4 - year//100 + year//400) + DaysByMonthMod7[month-1] + day) % 7]; # 4
        
class sing:
    def __init__(self,person_count):
        self.person_count = person_count
    def total_by_person(self):#人頭計算函式
        total = ((350 + 138) * self.person_count) * 1.1
        return round(total,2)
    def total_by_box(self):#包廂計算函式
        if(self.person_count <= 3):
            total = (350 * 3 + 138 * self.person_count) * 1.1
        elif(self.person_count <= 6):
            total = (490 * 3 + 138 * self.person_count) * 1.1
        elif(self.person_count <= 9):
            total = (630 * 3 + 138 * self.person_count) * 1.1
        elif(self.person_count <= 12):
            total = (770 * 3 + 138 * self.person_count) * 1.1
        elif(self.person_count <= 15):
            total = (910 * 3 + 138 * self.person_count) * 1.1
        elif(self.person_count > 15):
            total = (1260 * 3 + 138 * self.person_count) * 1.1
        return round(total,2)
    def compare(self):#比較函式
        if self.total_by_person() < self.total_by_box():
            return "以人數計算較便宜"
        else:
            return "開包廂計算較便宜"
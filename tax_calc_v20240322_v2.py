class calc_tax: #2024年所得稅計算
    def __init__(self):#輸入年資、配偶狀態、年齡
        self.Total_revenue = int(input("輸入你的年薪："))
        self.Is_Single = input("輸入配偶狀態(單身/已婚)： ")
        self.Age = int(input("輸入年齡："))
        
        self.Payroll_deductions= 207000 #薪資扣除額
        self.tax_exemption = 92000 #免稅額
        self.standard_deduction = 124000 #標準扣除額
        
    def calc_person(self):#計算人數
        person_count = 0
        if(self.Is_Single == '單身'):#是否有伴侶
            person_count += 1
            return person_count
        elif(self.Is_Single == '已婚'):
            person_count += 2
            return person_count
            
    def calc_tax_exemption(self):
        total = 0
        if self.Age < 70:#免稅額判定 小於70歲
            self.tax_exemption
        else:
            self.tax_exemption = 138000
            
        if(self.Is_Single == '已婚'):#判定伴侶免稅額
            spouse_age = int(input("請輸入伴侶年齡："))#看是否能解決呼叫該函式時有伴侶都要重複輸出年齡的問題
            if spouse_age < 70:
                spouse_tax_exemption = 92000
            else:
                spouse_tax_exemption = 138000
        else:
            spouse_age = 0
            spouse_tax_exemption = 0
            
        total = spouse_tax_exemption + self.tax_exemption
        return total
            
    def basic_living_expeses(self):#基本生活費差額公式
        total = 202000 * self.calc_person() #基本生活費總額計算
        expense = total - self.calc_tax_exemption() - self.standard_deduction * self.calc_person() #基本生活費差額計算
        if expense > 0 :
            return expense
        else:
            return 0
   
    def Amount_of_tax(self): #納稅額公式
        Net_Amounts = self.Total_revenue - self.calc_tax_exemption() - self.standard_deduction * self.calc_person() - self.basic_living_expeses() #綜合所得稅計算 年收入 - 免稅額 - 標準扣除額 - 基本生活費差額
        tax = 0
        if(Net_Amounts < 0):#納稅額計算 = 所得淨額 * 稅率 - 累進差額
            print("納稅額為0,不用報稅！")
        elif(Net_Amounts > 0 and Net_Amounts < 560000): 
            tax = Net_Amounts * 0.05
        elif(Net_Amounts > 560001 and Net_Amounts < 1260000):
            tax = Net_Amounts * 0.12 - 39200
        elif(Net_Amounts > 1260001 and Net_Amounts < 2520000):
            tax = Net_Amounts * 0.2 - 140000
        elif(Net_Amounts > 2520001 and Net_Amounts < 4720000):
            tax = Net_Amounts * 0.3 - 392000
        elif(Net_Amounts > 4720000):
            tax = Net_Amounts * 0.4 - 864000
        print(f"納稅淨額為{Net_Amounts:,}元,應繳納稅額為{tax:,}元")
        
    def Is_No_Tax(self):#判斷是否不用繳稅   
        income_tax = self.calc_tax_exemption() + ((self.standard_deduction + self.Payroll_deductions) * self.calc_person()) #免課稅標準計算
        
        if self.Total_revenue < income_tax:#是否免繳稅判定 年收入小於免課稅標準即可不用繳稅
            print(f'您年薪為：{self.Total_revenue:,}元,免繳稅標準為：{income_tax:,}元，已達到免繳稅標準！')
        else:
            print(f'您年薪為{self.Total_revenue:,}元,免繳稅標準為{income_tax:,}元，未達到免額稅標準！')
def main():
    a = calc_tax()
    a.Amount_of_tax()
    a.Is_No_Tax()
if __name__ == '__main__':
    main()
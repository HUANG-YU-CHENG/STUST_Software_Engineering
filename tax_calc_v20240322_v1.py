class calc_tax: #2024年所得稅計算
    def __init__(self):#輸入年資、配偶狀態、年齡
        self.Total_revenue = int(input("輸入你的年薪："))
        self.Is_Single = input("輸入配偶狀態：")
        self.Age = int(input("輸入年齡："))
        
        self.Payroll_deductions= 207000 #薪資扣除額
        self.tax_exemption = 92000 #免稅額
        self.standard_deduction = 124000 #標準扣除額
        self.person_count = 0
        
    def calc_person(self):#計算人數 #判斷有誤 需要修改
        if(self.Is_Single == 'single'):#是否有伴侶 
            self.person_count += 1
            return self.person_count
        elif(self.Is_Single == 'couple'):
            self.person_count += 2
            return self.person_count
            
    def basic_living_expeses(self):#基本生活費差額公式
        total = 202000 * self.calc_person() #基本生活費總額計算
        expense = total - self.tax_exemption - self.standard_deduction * self.calc_person() #基本生活費差額計算
        if expense > 0 :
            return expense
        else:
            return 0
        
    def Net_Amounts(self): #綜合所得稅淨額計算
        Amounts = self.Total_revenue - self.tax_exemption - self.standard_deduction - self.basic_living_expeses() #年收入 - 免稅額 - 標準扣除額 - 基本生活費差額
        print(f'綜合所得稅淨額為{Amounts:,}元')
        
    def Amount_of_tax(self): #納稅額計算
        print()
        
    def Is_No_Tax(self):#判斷是否不用繳稅
        if self.Age < 70:#免稅額判定 小於70歲
            self.tax_exemption
        else:
            self.tax_exemption = 138000
            
        income_tax = (self.tax_exemption * self.calc_person()) + self.standard_deduction + (self.Payroll_deductions * self.calc_person()) #免課稅標準計算
        
        if self.Total_revenue < income_tax:#是否免繳稅判定 年收入小於免課稅標準即可不用繳稅
            print(f'您年薪為：{self.Total_revenue:,}元,免繳稅標準為：{income_tax:,}元，已達到免繳稅標準！')
        else:
            print(f'您年薪為{self.Total_revenue:,}元,免繳稅標準為{income_tax:,}元，未達到免額稅標準！')
def main():
    a = calc_tax()
    
    a.Is_No_Tax()
if __name__ == '__main__':
    main()
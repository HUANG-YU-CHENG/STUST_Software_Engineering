import pytest
from tax_calc import calc_tax

@pytest.mark.parametrize("Total_revenue, Is_Single , Age ,spouse_Age,expected_tax,expected_income_tax",[ #定義多組參數測試資料
    (500000,"單身",30,0,3850.0,423000),
    (500000,"單身",75,0,3850.0,423000),
    (1000000,"已婚",50,55,5400.0,892000),
    (1000000,"已婚",50,75,5400.0,892000),
    (52353000,"已婚",50,75,16543.0,892000)
])
def test_calc_tax(Total_revenue,Is_Single, Age,spouse_Age,expected_tax,expected_income_tax):
    #建立calc_tax的實例，並提供輸入資料
    test_data= calc_tax(Total_revenue,Is_Single,Age)
    test_data.spouse_age = spouse_Age
    
    #測試納稅額公式
    actual_tax = test_data.Amount_of_tax()
    
    #測試是否不用繳稅公式
    actual_income_tax = test_data.Is_No_Tax()
    
    #驗證結果是否符合預期 左邊為正確答案 右邊為猜測答案
    assert actual_tax == expected_tax
    assert actual_income_tax == expected_income_tax
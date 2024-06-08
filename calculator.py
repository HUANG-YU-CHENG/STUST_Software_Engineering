class Calculator:
    def evalString(self, expr):
        try:
            result = eval(expr)
            return str(result)#將結果轉換成字串型態
        except Exception as e:#結果輸出錯誤時回傳
            return "Invalid Input"






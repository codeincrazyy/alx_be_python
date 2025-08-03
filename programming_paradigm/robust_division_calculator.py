def safe_divide(numerator, denominator):
    try:
         num = float(numerator)
         denom = float(denominator)
         try:
            result = num / denom
            return f"reslut: {result}"
         except ZeroDivisionError:
            return "can not divied by zero"
    except ValueError:
            return "Error: Please enter numeric values only."
        
        
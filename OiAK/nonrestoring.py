def division(dividend, divisor):
    quotient = 0                        # iloraz to 0
    remainder = 0                       # reszta to 0
    bits = dividend.bit_length()
    for i in range(bits - 1, -1, -1):
        remainder = (remainder << 1) | ((dividend >> i) & 1)
        if remainder >= 0:
            remainder -= divisor
            quotient = (quotient << 1) | 1
        else:
            remainder += divisor
            quotient <<= 1
    if remainder < 0:
        remainder += divisor
    print(f"Non-restoring: Quotient = {quotient}, Remainder = {remainder}")
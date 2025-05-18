import time

def division(dividend, divisor):
    start = time.perf_counter()
    quotient = 0
    remainder = 0
    bits = dividend.bit_length()

    for i in range(bits - 1, -1, -1):
        # 1. Shift left remainder i dołącz kolejny bit z dividend
        remainder = (remainder << 1) | ((dividend >> i) & 1)

        # 2. Decyzja: jeśli poprzednia reszta ≥ 0, to odejmujemy; inaczej dodajemy
        if remainder >= 0:
            remainder -= divisor
        else:
            remainder += divisor

        # 3. Ustawienie bitu ilorazu: po odejmowaniu/dodawaniu patrzymy na nowy znak reszty
        if remainder >= 0:
            quotient = (quotient << 1) | 1
        else:
            quotient <<= 1

    # 4. Korekta końcowej reszty jeśli jest ujemna
    if remainder < 0:
        remainder += divisor

    end = time.perf_counter()

    time_performed = end - start

    print(f"Non-restoring: Quotient = {quotient}, Remainder = {remainder}")
    
    return time_performed

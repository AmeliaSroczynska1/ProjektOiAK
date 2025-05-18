import time

def division(dividend, divisor):
    start = time.perf_counter()

    quotient = 0                         # iloraz to 0
    remainder = 0                        # reszta to 0
    bits = dividend.bit_length()         # Liczba bitów potrzebna do reprezentacji dzielnej (bez wiodących zer)
    for i in range(bits - 1, -1, -1):
        remainder = (remainder << 1) | ((dividend >> i) & 1)
        quotient <<= 1
        old_remainder = remainder
        remainder -= divisor
        if remainder >= 0:
            quotient |= 1
        else:
            remainder = old_remainder  # Przywracamy wartość

    end = time.perf_counter()
    time_performed = end - start


    print(f"Restoring: Quotient = {quotient}, Remainder = {remainder}")

    return time_performed
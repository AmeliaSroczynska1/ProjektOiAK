import SRT
import restoring
import nonrestoring
import random


def main():
    for i in range(10):
        avg_time_rest = 0
        avg_time_non_rest = 0

        for j in range(100):
            dividend = random.randint(10 ** (1-1), 10 ** i)
            divisor = random.randint(1, dividend)
            restoring.division(dividend, divisor)
            time_performed = restoring.division(dividend, divisor)
            print(f"Time spend = {time_performed*1000: .4f} ms")
            time_performedNon = nonrestoring.division(dividend, divisor)
            print(f"Time spend = {time_performedNon*1000: .4f} ms")
            avg_time_rest += (time_performed * 1000)
            avg_time_non_rest += (time_performedNon * 1000)

        avg_time_rest = avg_time_rest/100
        avg_time_non_rest = avg_time_non_rest/100

        print(f"AVG Time spend = {avg_time_rest: .4f} ms")
        print(f"AVG Time spend = {avg_time_non_rest: .4f} ms")



if __name__ == '__main__':
    main()




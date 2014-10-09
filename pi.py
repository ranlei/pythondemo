#/usr/bin/env/ python
import math
def sqrt(n, one):
    floating_point_precision = 10 ** 16
    n_float = float((n * floating_point_precision) // one) / \
            floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // \
            floating_point_precision
    n_one = n * one
    while True:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x


def pi_chudnovksy(one):
    k = 1
    a_k = one
    a_tot = one 
    b_tot = 0
    C = 640320
    C3_OVER_24 = C**3 // 24
    while True:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k**3 * C3_OVER_24
        a_tot += a_k
        b_tot += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409 * a_tot + 545140134 * b_tot
    pi = (426880 * sqrt(10005 * one, one) * one) // total
    return pi


def validate_nonnegative_integer():
    while True:
        s = raw_input("How many digits of pi do you want to see? ")
        try:
            digits = int(s)
            if digits >= 10000:
                print "Enter a number smaller than 10000."
            elif digits > 0:
                return digits 
            else:
                print "Enter a nonnegative integer."
        except ValueError:
            print "Enter a nonnegative integer."


def main():
    digits = validate_nonnegative_integer()
    pi = str(pi_chudnovksy(10**(digits * 10)))[:digits]
    print pi[0] + "." + pi[1:]

    
if __name__ == "__main__":
    main()
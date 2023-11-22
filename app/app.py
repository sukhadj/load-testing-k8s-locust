from flask import Flask
import math
import random

app = Flask(__name__)

def calculate_pi(digits):
    """
    Calculate Pi to the specified number of digits using the Chudnovsky algorithm.
    This is a CPU-intensive task.
    """
    decimal_places = digits + 2
    k = 6 * decimal_places // 5 + 1
    result = 0
    for k in range(k):
        result += (-1) ** k * math.factorial(6 * k) * (545140134 * k + 13591409)
    return 1 / (12 ** 2 * math.factorial(decimal_places)) * result

@app.route("/")
def index():
    # calculate the pi
    rand_digits = random.randrange(1, 20)
    result = calculate_pi(rand_digits)

    # calculate sum of squares
    rand_number = random.randrange(1000, 10000)
    sum = 0
    for i in range(rand_number):
        sum = sum + i*i

    return "Task1: Calculated Pi with {0} digits: {1}\n Task2: Sum of squares till {2}: {3}".format(rand_digits, result, rand_number, sum)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
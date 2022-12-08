"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError()

    else:
        counter = 0
        num = 1

        while(counter != number_of_primes):
            num += 1
            holder = num - 1
            found = False

            while (holder > 1):
                if (num % holder == 0):
                    found = True
                    break
                else:
                    holder -= 1

            if found == False:
                list.append(num)
                counter += 1

    return list

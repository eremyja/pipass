# list prime numbers
def total_prime_numbers(max_number) :
    all_prime = [2]
    for i in range(3,max_number, 2) :
        is_prime = True
        for k in all_prime :
            if (i%k) == 0 :
                is_prime = False
                break

        if is_prime :
            all_prime.append(i)

    total_prime = len(all_prime) + 1
    return total_prime

#print(total_prime_numbers(30000))

#####

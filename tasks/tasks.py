def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def custom_range_generator(n):
    for i in range(1, n + 1):
        yield i


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_number_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def char_counter(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        yield char, count

if __name__ == "__main__":
    fibonacci_numbers = fibonacci_generator()
    for _ in range(10):
        print(next(fibonacci_numbers), end=" ")
    print()

    custom_numbers = custom_range_generator(5)
    for num in custom_numbers:
        print(num, end=" ")
    print()

    prime_numbers = prime_number_generator()
    for _ in range(10):
        print(next(prime_numbers), end=" ")
    print()

    text = "hello world"
    characters = char_counter(text)
    for char, count in characters:
        print(f"{char}: {count}")

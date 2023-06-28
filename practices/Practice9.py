def product_of_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a * b * c

product = product_of_pythagorean_triplet()
print("The product of pythagorean triplet for which a+b+c=1000 is ",product)
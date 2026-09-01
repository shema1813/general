input("Bit difference - XOR shows which bits differ. Press Enter ")
print(" 5 ^ 3 =", 5 ^ 3, " binary", bin(5 ^ 3)[2:], " bits difference:", bin(5 ^ 3).count('1'))
print(" 9 ^ 5 =", 9 ^ 5, " binary", bin(9 ^ 5)[2:], " bits difference:", bin(9 ^ 5).count('1'))

n = int(input("Enter number of elements (try 4 or 6): " ))
guess = input("How may bits differ between " + str(n) + " and 7? ")
input("XOR marks the differing bits - count the 1s. Press Enter")
diff = bin(n ^ 7).count('1')
print( " ", n, "^ 7 = binary", bin( n ^ 7)[2:], "different bits:", diff, " your guess:", guess)
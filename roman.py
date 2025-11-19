userinput = input("Enter an integer to convert to Roman num: ")

# Initialize the function that convert roman num to integer
def int_to_roman(num):
    final_ans = 0
    for i in num:
        if i == 'I':
            final_ans += 1
        elif i == 'V':
            final_ans += 5
        elif i == 'X':
            final_ans += 10
        elif i == 'L':
            final_ans += 50
        elif i == 'C':
            final_ans += 100
        elif i == 'D':
            final_ans += 500
        elif i == 'M':
            final_ans += 1000
        # Edge Cases
        if "CM" in num:
            final_answer += 900
            num = num.replace("CM", "")
        if "CD" in num:
            final_answer += 400
            num = num.replace("CD", "")
        if "XC" in num:
            final_answer += 90
            num = num.replace("XC", "")
        if "XL" in num:
            final_answer += 40
            num = num.replace("XL", "")
        if "IX" in num:
            final_answer += 9
            num = num.replace("IX", "")
        if "IV" in num:
            final_answer += 4
            num = num.replace("IV", "")
    print("The roman numerals you entered translates to: " + str(final_ans) + "!")


int_to_roman(userinput)


    
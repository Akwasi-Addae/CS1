import hw4_util

def rule_output(rule, num):
    '''Print the contribution of the rules'''
    if(num < 0):
        print(rule + ': ' + str(num))
    elif num > 0:
        print(rule + ': +' + str(num))

def length(password):
    ''' Calculate additional points based on length'''
    score = 0
    if 5 < len(password) < 8 :
        score += 1
    elif 7 < len(password) < 11:
        score += 2
    elif len(password) > 10:
        score += 3

    return score

def case(password):
    ''' Calculate score based on # of upper and lower cases'''
    upper = lower = score = 0
    for i in password:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1

    if upper >= 1 and lower >= 1:
        score += 1
    if upper >= 2 and lower >= 2:
        score += 1
    
    return score

def digits(password):
    ''' Calculate score based on # of digits'''
    score = digs = 0
    for i in password:
        if i.isnumeric():
            digs += 1
    
    if digs == 1:
        score += 1
    elif digs >= 2:
        score += 2
    
    return score

def punctuation(password):
    ''' Calculate score based on # of punctuations'''
    first_type = second_type = 0
    if password.count('!') or password.count('@') or password.count('#') or password.count('$') >= 1:
        first_type += 1

    if password.count('%') or password.count('^') or password.count('&') or password.count('*') >= 1:
        second_type += 1
        
    return (first_type, second_type)

def license(password):
    ''' Calculate score based on # of punctuations'''
    score = alpha_count = digit_count = 0
    password = password.lower()

    for i in password:
        if i.isalpha():                  # Condition for incrementing 
            alpha_count += 1

        if i.isnumeric() and alpha_count == 3:
            digit_count += 1
        elif not (i.isalpha()) and not i.isnumeric():
            digit_count = alpha_count = 0

    if alpha_count == 3 and digit_count >= 4:
        score -= 2

    return score

def common_passwords(passwords, password):
    score = 0
    if password.lower() in passwords:
        score = -3

    return score
    

if __name__ == "__main__":
    passwords = hw4_util.part1_get_top()
    password = input("Enter a password => ")
    print(password)
    
    length_score = length(password)
    rule_output("Length", length_score)

    case_score = case(password)
    rule_output("Cases", case_score)

    digits_score = digits(password)
    rule_output("Digits", digits_score)

    punctuation_score = punctuation(password)
    rule_output("!@#$", punctuation_score[0])
    rule_output("%^&*", punctuation_score[1])

    license_score = license(password)
    rule_output("License", license_score)

    common_password_score = common_passwords(passwords, password)
    rule_output("Common", common_password_score)

    score = length_score + case_score + digits_score + punctuation_score[0] + punctuation_score[1] + license_score + common_password_score

    print("Combined score:", score)
    if(score <= 0):
        print("Password is rejected")
    elif score <= 2:
        print("Password is poor")
    elif score <= 4:
        print("Password is fair")
    elif score <= 6:
        print("Password is good")
    else:
        print("Password is excellent")


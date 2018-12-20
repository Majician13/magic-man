# Ask for total of order and country.  

orderTotal = float(input("What is your total?  "))
country = input("What country are you from?  ").lower()

# If country is canada, ask for province

if country == "canada" :
    province = input("What province are you from?  ").lower()
    
    # if province is alberta, charge .05% tax
    
    if province == "alberta" :
        total = ((orderTotal * .0005) + orderTotal)
        print(total)
    
    # if province is ontario, new brunswick, or nova scotia, charge .13% tax
    
    elif province == "ontario" or province == "new brunswick" or province == "nova scotia" :
        total = ((orderTotal * .0013) + orderTotal)
        print(total)
    
    # for all other provinces, charge .06% tax
    
    else :
        total = ((orderTotal * .0006) + orderTotal)
        print(total)

# if outside of canada, don't charge tax

if country != "canada" :
    total = orderTotal
    print(total)


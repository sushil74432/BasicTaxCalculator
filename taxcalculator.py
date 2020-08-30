def getAnnualSalary(income):
    bonus = input("Do you get Festival Bonus(Y/N): ");
    if (bonus.lower() == "y"):
        income = income * 13;
    if (bonus.lower() == "n"):
        income = income * 12;
    return income

def tax(income, slab):
    tax_amount = 0;
    if income <= slab[0]:
        print("Falls in slab 1");
        tax_amount = (0.01 * income);
    elif income <= slab[1]:
        print("Falls in slab 2");
        tax_amount = (0.01 * slab[0]) + (0.1*(income - slab[0]));
    elif income <= slab[2]:
        print("Falls in slab 3");
        tax_amount = (0.01 * slab[0]) + (0.1*(slab[1]-slab[0])) + (0.2*(income-slab[1]));
    elif income <= slab[3]:
        print("Falls in slab 4");
        tax_amount = (0.01 * slab[0]) + (0.1*(slab[1]-slab[0])) + (0.2*(slab[2]-slab[1])) + (0.3*(income-slab[2]));
    elif income > slab[4]:
        print("Falls in slab 5");
        tax_amount = (0.01 * slab[0]) + (0.1*(slab[1]-slab[0])) + (0.2*(slab[2]-slab[1])) + (0.3*(slab[3]-slab[2])) + (0.36*(income-slab[3]));

    cash_in_hand = income - tax_amount;
    print("Your Tax Amount Is : " + str(tax_amount));
    print("Your Remaining Salary Is: " + str(cash_in_hand));


is_married = False
married_slabs = [450000, 550000, 750000, 1250000, 200000];
unmarried_slabs = [400000, 500000, 700000, 1300000, 2000000];

income = int(input("What is your gross monthly salary : "));
income = getAnnualSalary(income);
married = input("Are you married(Y/N) : ");
print("Your yearly income is : "+str(income));


if married.lower() == "y":
    is_married = True;
    # tax(income, married_slab1, married_slab2, married_slab3, married_slab4, married_slab5);
    tax(income, married_slabs);
elif married.lower() == "n":
    is_married = False
    # tax(income, unmarried_slab1, unmarried_slab2, unmarried_slab3, unmarried_slab4, unmarried_slab5);
    tax(income, unmarried_slabs);

# ---------------------------------------
# DSA 230/ CIS 492/ CIS 593, Intro to DS |
# Lab 3: Tax Calculator                 |
# Your Name                             |
# Date:                                 |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2024.  |
# ---------------------------------------

# The missing Python function goes here.
def unmarried_individual_tax(income):
    income=int(income)
    if (income-11600) > 0:
        tax_owed=11600*.1
    else:
        tax_owed=income*.1
        return(tax_owed)
    if (income-47150) > 0:
        tax_owed=tax_owed+((47150-11600)*.12)
    else:
        tax_owed=tax_owed+((income-11600)*.12)
        return(tax_owed)
    if (income-100525) > 0:
        tax_owed=tax_owed+((100525-47150)*.22)
    else:
        tax_owed=tax_owed+((income-47150)*.22)
        return(tax_owed)
    if (income-191950) > 0:
        tax_owed=tax_owed+((191950-100525)*.24)
    else:
        tax_owed=tax_owed+((income-100525)*.24)
        return(tax_owed)
    if (income-243725) > 0:
        tax_owed=tax_owed+((243725-191950)*.32)
    else:
        tax_owed=tax_owed+((income-191950)*.32)
        return(tax_owed)
    if (income-609350) > 0:
        tax_owed=tax_owed+((609350-243725)*.35)
    else:
        tax_owed=tax_owed+((income-243725)*.35)
        return(tax_owed)
    if income > 609351:
        tax_owed=tax_owed+((income-609351)*.37)
        return(tax_owed)
# ---------------------------------------


def process(income):
    print("The 2024 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()

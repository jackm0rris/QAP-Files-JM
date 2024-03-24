# Description: One Stop Insurance Company
# Author: Jack Morris
# Date(s) March 22nd, 2024

# Define required libraries
import FormatValues as FV
import datetime
import re
import time
import sys

# Define program constants
f = open('def.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_DISCOUNT = float(f.readline())
EXTRA_LIAB_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())
f.close()

CURR_DATE = datetime.datetime.now()


# Define program functions


# Main program starts here
while True:

    # Display inputs
    while True:
        FirstName = input("Enter the customers first name: ").title()
        if FV.ValidName(FirstName):
            break
        else:
            print("Error - Invalid characters.")
            
        

    while True:
        LastName = input("Enter the customers last name: ").title()
        if FV.ValidName(LastName):
            break
        else:
            print("Error - Invalid characters.")
        
        

    StAddress = input("Enter the customers street address: ").title()
    City = input("Enter the customers city: ").title()
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    while True:
        Prov = input("Enter the customer province (LL): ").upper()
        if Prov == "":
            print("Error - cannot be blank.")
        elif len(Prov) != 2:
            print("Error - must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Error - invalid province.")
        else:
            break
    PostalCode = input("Enter the postal code: (L9L 9L9): ").upper()

    while True:
        PhoneNum = input("Enter the customers phone number (999-999-9999): ")
        if FV.ValidNum(PhoneNum):
            break
        else:
            print("Error - Invalid characters.")
            


    NumCarInsured = input("Enter the number of cars insured: ")
    NumCarInsured = int(NumCarInsured)

    while True:
        ExtraLiability = input("Enter if you want extra liability or not. (Y/N): ").upper()
        if ExtraLiability == "":
            print("Error - cannot be blank")
        elif len(ExtraLiability) != 1:
            print("Error - must be 1 characters only.")
        else:
            break

    while True:
        GlassCoverage = input("Enter if you want glass coverage or not. (Y/N): ").upper()
        if GlassCoverage == "":
            print("Error - cannot be blank")
        elif len(GlassCoverage) != 1:
            print("Error - must be 1 characters only.")
        else:
            break

    while True:
        OptionalLoaner = input("Enter if you want an optional loaner or not. (Y/N): ").upper()
        if OptionalLoaner == "":
            print("Error - cannot be blank")
        elif len(OptionalLoaner) != 1:
            print("Error - must be 1 characters only.")
        else:
            break

    PaymentLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PaymentMethod = input("Enter the method of payment: ").title()
        if PaymentMethod == "":
            print("Error - cannot be blank.")
        elif PaymentMethod not in PaymentLst:
            print("Error - invalid method.")
        elif PaymentMethod == "Down Pay":
            try:
                DownPay = input("How much do you want to pay for down payment?: ")
                DownPay = float(DownPay)
                break
            except ValueError:
                print("Error - Enter a valid value")
        else:
            break

    Claims = []

    def GetClaims(Claims):
        print()
        print("Enter previous claim data. Type '999' in the claim number input to end.")
        print()
        while True:
            ClaimNumber = input("Enter claim number: ")
            if ClaimNumber == "999":
                break
            elif not ClaimNumber.isdigit():
                print("Error - enter a valid claim number.")
                continue

            while True:
                ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
                if ClaimDate == "000":
                    break
                try:
                    datetime.datetime.strptime(ClaimDate, '%Y-%m-%d')
                except ValueError:
                    print("Error - enter valid format.")
                    continue
                else:
                    break

            if ClaimDate == "000":
                break

            while True:
                try:
                    ClaimAmount = float(input("Enter claim amount: "))
                    ClaimAmount = FV.FDollar2(ClaimAmount)
                    break
                except ValueError:
                    print("Error -  enter valid number for claim amount.")
                    continue
                            # Check for duplicate claim number
            for claim in Claims:
                if claim['Claim Number'] == ClaimNumber:
                    print("Duplicate claim number. Please enter a different claim number.")
                    break
            else:
                Claims.append({'Claim Number': ClaimNumber, 'Claim Date': ClaimDate, 'Claim Amount': ClaimAmount})
                print("Claim added successfully.")
                return Claims


    # Calculations
    if NumCarInsured == 1:
        InsurancePrem = BASIC_PREM
    elif NumCarInsured > 1:
        InsurancePrem = BASIC_PREM * NumCarInsured * ADD_DISCOUNT

    if ExtraLiability == "Y":
        LiabilityCost = EXTRA_LIAB_COV * NumCarInsured
    else:
        LiabilityCost = 0

    if GlassCoverage == "Y":
        GlassCoverageCost = GLASS_COV * NumCarInsured
    else:
        GlassCoverageCost = 0

    if OptionalLoaner == "Y":
        LoanerInfoCost = LOANER_CAR * NumCarInsured
    else:
        LoanerInfoCost = 0

    TotExtraCost = LiabilityCost + GlassCoverageCost + LoanerInfoCost

    TotInsurPrem = InsurancePrem + TotExtraCost

    HST = TotInsurPrem * HST_RATE

    TotCost = HST + TotInsurPrem

    MonthlyPayment = (TotCost + PROC_FEE) / 8

    if PaymentMethod != "Down Pay":
        MonthlyPayment = (TotCost + PROC_FEE) / 8
    else:
        MonthlyPayment = TotCost - DownPay

    InvDate = CURR_DATE

    GetClaims(Claims)



    # Display results
    print()
    print(f"ONE STOP INSURANCE COMPANY")
    print(f"INSURANCE POLICY RECEIPT        {POLICY_NUM:<5}")
    print("--------------------------------------------------")
    print(f" Customer first name:        {FirstName:<10s}")
    print(f" Customer last name:         {LastName:<10s}")
    print(f" Street adress:              {StAddress:<25s}")
    print(f" City:                       {City:<15s}")
    print(f" Province:                   {Prov:<2s}")
    print(f" Postal code:                {PostalCode:<7s}")
    print(f" Phone number:               {PhoneNum:>12s}")
    print("--------------------------------------------------")
    print(f" Number of cars insured:    {NumCarInsured:>2d}")
    print(f" Extra liability:            {ExtraLiability:<1s}")
    print(f" Glass coverage:             {GlassCoverage:<1s}")
    print(f" Loaner car:                 {OptionalLoaner:<1s}")
    print("--------------------------------------------------")
    print(f" Payment method:             {PaymentMethod:<12s}")
    
    if PaymentMethod == "Down Payment":
        print(f" Down payment amount:    {FV.FDollar2(DownPay):>9s}")
    
    print(f" Total insurance premium:    {FV.FDollar2(TotInsurPrem):>9s}")
    print(f" Extra liability cost:     {FV.FDollar2(LiabilityCost):>9s}")
    print(f" Glass coverage cost:     {FV.FDollar2(GlassCoverageCost):>9s}")
    print(f" Loaner car cost:         {FV.FDollar2(LoanerInfoCost):>9s}")
    print("--------------------------------------------------")
    print(f" Total extra cost:         {FV.FDollar2(TotExtraCost):>9s}")
    print(f" HST:                      {FV.FDollar2(HST):>9s}")
    print(f" Total cost:                 {FV.FDollar2(TotCost):>9s}")
    print("--------------------------------------------------")
    print(f" Monthly payment           {FV.FDollar2(MonthlyPayment):>9s}")
    print()
    print(f" Invoice date:               {FV.FDateS(CURR_DATE):<10s}")

    while True:
        if PaymentMethod == "Down Payment"  or PaymentMethod == "Monthly":
            FirstPayDate = CURR_DATE + datetime.timedelta(days = 30)
            FirstPayDateDsp = datetime.datetime.strftime(FirstPayDate, "%Y-%m-%d")
            print(f" First payment date:     {FirstPayDateDsp}")
        print()
        break
    print("--------------------------------------------------")
    print(f"Claim Number:        Claim Date:          Amount:           ")
    print("--------------------------------------------------")
    for claim in Claims:
        print(f"{claim['Claim Number']:>5}                {claim['Claim Date']:<10}          {claim['Claim Amount']:<10}        ")
        print("--------------------------------------------------") 
        print()

            
        for _ in range(4): 
            print('Saving claim data ...', end='\r')
            time.sleep(.3)  
            sys.stdout.write('\033[2K\r')  
            time.sleep(.3)
        print()
        print("Claim data successfully saved ...", end='\r')
        time.sleep(1.5)  
        sys.stdout.write('\033[2K\r')  
        POLICY_NUM += 1
        print()


        if input("Do you want to start another program? (Y/N): ").upper() != "Y":
            print("Thank you for using One Stop Insurance!")
            break

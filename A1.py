class MortgagePayment:
    def __init__(self, interest_rate, amortization_period):
        self.interest_rate = interest_rate
        self.amortization_period = amortization_period

    def payments(self, principal_amount):
        rate = self.interest_rate/100

        # Monthly
        r_monthly = (1 + rate/2) ** (2/12) - 1
        monthly_period = self.amortization_period * 12
        monthly_payment = principal_amount/((1-(1+r_monthly)**-monthly_period)/r_monthly)
        print(f"Monthly Payment: ${monthly_payment:.2f}")

        # Semi-monthly
        r_semi_monthly = (1 + rate/2) ** (2/24) - 1
        semi_monthly_period = self.amortization_period * 24
        semi_monthly_payment = principal_amount/((1-(1+r_semi_monthly)**-semi_monthly_period)/r_semi_monthly)
        print(f"Semi-monthly Payment: ${semi_monthly_payment:.2f}")

        # Bi-weekly
        r_biweekly = (1 + rate/2) ** (2/26) - 1
        bi_weekly_period = self.amortization_period * 26
        bi_weekly_payment = principal_amount/((1-(1+r_biweekly)**-bi_weekly_period)/r_biweekly)
        print(f"Bi-weekly Payment: ${bi_weekly_payment:.2f}")

        # Weekly
        r_weekly = (1 + rate/2) ** (2/52) - 1
        weekly_period = self.amortization_period * 52
        weekly_payment = principal_amount/((1-(1+r_weekly)**-weekly_period)/r_weekly)
        print(f"Weekly Payment: ${weekly_payment:.2f}")

        # Rapid Bi-weekly
        rapid_biweekly_payment = monthly_payment / 2
        print(f"Rapid Bi-weekly Payment: ${rapid_biweekly_payment:.2f}")

        # Rapid Weekly 
        rapid_weekly_payment = monthly_payment / 4
        print(f"Rapid Weekly Payment: ${rapid_weekly_payment:.2f}")

def main():
    print("### PART 1 ###")
    principal_amount = float(input("What is the Principal Amount: "))
    quoted_interest_rate = float(input("What is the Quoted Interest Rate: "))
    amortization_period = int(input('What is the Amortization Period: '))

    mp = MortgagePayment(quoted_interest_rate, amortization_period)
    mp.payments(principal_amount)

    print("### PART 2 ###")


if __name__ == "__main__":
    main()

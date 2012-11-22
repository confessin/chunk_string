import chunk_string


#TODO (confessin): Write proper unit test cases for this.

RAW_TEXT = """
Debt consolidation entails taking out one loan to pay off many others. This is often done to secure a lower interest rate, secure a fixed interest rate or for the convenience of servicing only one loan.
Debt consolidation can simply be from a number of unsecured loans into another unsecured loan, but more often it involves a secured loan against an asset that serves as collateral, most commonly a house. In this case, a mortgage is secured against the house. The collateralization of the loan allows a lower interest rate than without it, because by collateralizing, the asset owner agrees to allow the forced sale (foreclosure) of the asset to pay back the loan. The risk to the lender is reduced so the interest rate offered is lower.
Sometimes, debt consolidation companies can discount the amount of the loan. When the debtor is in danger of bankruptcy, the debt consolidator will buy the loan at a discount. A prudent debtor can shop around for consolidators who will pass along some of the savings. Consolidation can affect the ability of the debtor to discharge debts in bankruptcy, so the decision to consolidate must be weighed carefully.
Debt consolidation is often advisable in theory when someone is paying credit card debt. Credit cards can carry a much larger interest rate than even an unsecured loan from a bank. Debtors with property such as a home or car may get a lower rate through a secured loan using their property as collateral. Then the total interest and the total cash flow paid towards the debt is lower allowing the debt to be paid off sooner, incurring less interest.
In a federal student loan consolidation, existing loans are purchased and closed by a loan consolidation company or by the Department of Education (depending on what type of federal student loan the borrower holds). Interest rates for the consolidation are based on that year's student loan rate, which is in turn based on the 91-day Treasury bill rate at the last auction in May of each calendar year.[citation needed]
Student loan rates can fluctuate from the current low of 4.70% to a maximum of 8.25% for federal Stafford loans, 9% for PLUS loans.[citation needed] The current consolidation program allows students to consolidate once with a private lender, and reconsolidate again only with the Department of Education.[citation needed] Upon consolidation, a fixed interest rate is set based on the then-current interest rate. Reconsolidating does not change that rate. If the student combines loans of different types and rates into one new consolidation loan, a weighted average calculation will establish the appropriate rate based on the then-current interest rates of the different loans being consolidated together.
Federal student loan consolidation is often referred to as refinancing, which is incorrect because the loan rates are not changed, merely locked in. Unlike private sector debt consolidation, student loan consolidation does not incur any fees for the borrower; private companies make money on student loan consolidation by reaping subsidies from the federal government.
Student loan consolidation can be beneficial to students' credit rating, but it's important to note that not all federal student loan consolidation companies report their loans to all credit bureaus.[citation needed].
"""

barx = "http://en.wikipedia.org/wiki/alexander%20the%20great"

if __name__ == '__main__':
  ins = chunk_string.CreateChunks()
  xxx = ins.start_chunks(RAW_TEXT,
                         keyword='debt consolidation loan credit')[0]
  print "number of keywords::%s" % len(xxx)
  print xxx

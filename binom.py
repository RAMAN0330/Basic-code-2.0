"""Write  a  function binc(n,r) that will compute the binomial coefficient : 
                        (n!/(r!(n-r)!))  
You can assume n<20, if it helps 
Using this for given input n, p, m find the probability that a binomial random variable with parameters n, p   
takes value less than or equal to m."""

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

def bin(n,r):
    binom = fact(n)/(fact(r)*fact(n-r))
    return binom

def main():
    no_of_trials = int(input("Enter number of trials : "))
    no_of_success = int(input("Enter number of success upto which you want to calculate probability : "))
    probability_success = float(input("Enter Probability of success : "))
    
    prob = 0
    
    for i in range(no_of_success+1):
        prob += bin(no_of_trials,i)*((probability_success**i)*((1-probability_success)**(no_of_trials-i)))
        
    print("<-------------------------------->")
    print(f"Probability of success after {no_of_success} of trials having {probability_success} chance of success is : {prob}")
    print("<-------------------------------->")
    
if __name__ == main():
    main()
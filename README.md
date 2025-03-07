# montyhall
This repository explains Monty Hall's paradox is correct.

# What is Monty Hall's Paradox?
Monty Hall's paradox is a famous probabilistic problem.   

To briefly explain the rules,   

Behind each of the three doors are two goats and a car.   

If you pick a car, you can get a car as a gift.   

The host knows the location of the goat, so after my choice, I open the door containing the goat among the other two options.   

And it gives you a chance to change.   

Let's say you picked A out of 3 doors [A B C].   

The host opened a C containing goat.   

In this case, the batch is [A(you) B C(goat)].   

Then would it be beneficial for me to switch to B,   

Or would it be beneficial to stay still with A?   

# Answer
Let's count the number of cases in which you randomly choose A from A, B, and C.   
1. If A is car    
A(car) B(goat) C(goat)   
-> The host will open either B or C.   
-> Therefore, if you change your choice, you will definitely get goat.   

2. If A is goat   
(1) A(goat) B(car) C(goat)
-> The host will open C.   
(2) A(goat) B(goat) C(car)   
-> The host will open B.   
-> It means if you change your choice, then you will definitely get a car.   

Thus, when you choose A, the probability of a car coming out is 2/3 and the probability of goat coming out is 1/3.   
After a total of 1 million trials,   
When you change your choice, the probability of a car coming out is about 0.666159, so we can see it very close to 2/3.   
Monty Hall is correct!   

# How to run?
1. Type your total number of runs.
2. Check if your result is over 0.666.

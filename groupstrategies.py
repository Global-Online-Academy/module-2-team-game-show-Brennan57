# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING
import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# If only 1 round has been played, if the opponent choose steal, choose steal; otherwise, choose split.
# If 2 or more have been played, look at the first 2 rounds, and choose steal if both of them are steal; otherwise choose split
# First round splits.
def cyan34Strategy1(history):
    steal = 0
    if len(history)==1:
        for i in history:
            (me,them) = i
            if them== "steal":
                steal+=1
        if steal==1:
            return random.choice(["split","steal"])
        else:
            return "split"
    elif len(history)>=2:
        for i in history:
            (me1,them1) = history[0]
            (me2,them2)= history[1]
            if them1=="steal" and them2 =="steal":
                return "steal"
            else:
                return "split"
    else:
        return "split"
print(cyan34Strategy1(hist4))


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 

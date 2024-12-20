score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Version 1 check lecture video for diff versions. he is changing '>=' to '<=' and rewriting the code.
    
#Version 2 is the Code Academy version if score >= 90: print("Grade A")  
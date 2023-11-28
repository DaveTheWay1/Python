# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
print("--users--")
print(users)

print(" ")
print("--resume data--")
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}
print(resume_data)


print(" ")
print("--accesing first users last name--")
# accesing first users last  name
print(users[0]["last"]) # prints Lovelace


# Ninja Challenge: On your own, predict what values 
# would print for the following lines of code without running it. 
# Feel free to make a diagram on paper or a white board the way 
# we did above. Want to check your answer? Run the code in your 
# terminal. Don't forget to copy the dictionaries too! :D

print(" ")
print(resume_data["skills"][1])
# predicted output: back-end
# correct
print(" ")
print(users[2]["first"])
# predicted out: Eric
# correct

print(" ")
resumes = [
        {
        #        	     0           1           2
        "skills": ["front-end", "back-end", "database"],
        #                0           1
        "languages": ["Python", "JavaScript"],
        #                0              1
        "hobbies":["rock climbing", "knitting"]
    },
        {
        #        	     0           1           2
        "skills": ["front-end", "back-end", "database"],
        #                0           1
        "languages": ["Python", "JavaScript"],
        #                0              1
        "hobbies":["rock climbing", "knitting"]
    },
        {
        #        	     0           1           2
        "skills": ["front-end", "back-end", "database"],
        #                0           1
        "languages": ["Python", "JavaScript"],
        #                0              1
        "hobbies":["rock climbing", "knitting"]
    }
]
print("--resumes--")
print(resumes)

print(" ")
print("--print what is in the first list for skills 3rd value--")
print(resumes[0]["skills"][2])
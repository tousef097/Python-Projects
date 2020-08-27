from PyDictionary import PyDictionary as pd

# User Input Section
print("Enter The Word To Get Its Meaning")
usr_inpt = input(":-")

# Fetching Section
core = pd.meaning(usr_inpt)

# For Getting The Type
keys = str(core.keys())
key_strt_cut = keys[12::1]
key_end_cut = key_strt_cut.replace("\'])", "")
print("Type Of The Word Is = ", key_end_cut)

# For Getting The Meaning
meanings = str(core.values())
means = str(meanings[14:200:1])
print("This are the meaning of the word you entered==")
print(means)

# Ending Code
print("\n Enter Any Character And Press Enter To Exit")
input(":-")
exit()
# UPPERCASE
word = 'particle'
wordd = word.upper()
print(f"The uppercase version of '{word}' is {wordd}")

# LOWERCASE
worda = 'PARTICLE'
worddd = worda.lower()
print(f"The lowercase version of '{worda}' is {worddd}")

# RSTRIP
# delete whitespace to the right or end of a string
print("particle       ".rstrip())

# LSTRIP
# inverse of rstrip
print("       particle".lstrip())

# STRIP
# delete whitespace  from both ends of a string
print("       particle       ".strip())

# in addition to delete the whitespace, strip can delete the desired word
print("gogogogoparticleCodegogogogo".strip('go'))

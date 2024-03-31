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

# START/END WITH
print("Particle Code".startswith("Particle"))
print("Particle Code".endswith("Code"))

# SPLIT and JOIN STRING
print(' '.join(['Particle', 'Code', "!"]))

print("Particle Code !".split())

# REPLACE STRING
string = "Let's be a Front End Developer with Particle Code! I know u can dude!"
print(string.replace("Code", "Coder"))

# STRING LITERALS
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# RAW STRING
print(r'Dicoding\nIndonesia')
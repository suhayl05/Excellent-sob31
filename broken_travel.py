# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?")) # (Mohammed suhayl, m01033117) year == int.input should be year = int(input and fixed mismatch quote

if year <= 1900: #(Mohammed suhayl,M01033117) fixed missing semicolon
    print ("Woah, that's the past!")#(Mohammed suhayl,M01033117) fixed incoorect quote
elif 1900 <= year < 2020: # (Mohammed suhayl,M01033117) incorrect and operator and fixed logic error
    print ("That's totally the present!")
else: # (Mohammed suhayl, M01033117) instead of elif it should be else
    print ("Far out, that's the future!!")
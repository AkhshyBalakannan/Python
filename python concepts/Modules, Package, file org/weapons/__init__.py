# THIS BLOCK OF CODE WILL RUN WHEN EVER WEAPON IS IMPORTED

print("YOUR WEAPONS MODULE IS INITIALIZED")

# The all name can also be omitted if not need
# its best to have that if user tries to import
# all he will have much faster import

# the below all line of code is to tell python when this
# package is imported from other module as from weaponsimport *
# We need to initialise and import the two modules
__all__ = ["weapon1", "weapon2"]

#Author Lauri Putkonen
#7. Create a short dictionary: e.g Finnish to English.
#Add some wordpairs to a list.
#Or as example, here are some English – Italian words:

dictionary = {
    "esimerkki" : "example",
    "ananas" : "pineapple",
    "sana" : "word",
    "lista" : "list",
    "ääni" : ["sound", "voice", "vote"]
    }

print(dictionary) # Print keys and values
print(dictionary.keys()) # Print all keys
print(dictionary["ananas"]) # Print "pineapple"
print(dictionary.get("ananas")) #print "pineapple"
print(dictionary.get("ääni")) # print ['sound', 'voice', 'vote']

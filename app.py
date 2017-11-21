from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country in country_counts:
        country_counts[country]+=1
    else:#defaultdict automatically does this, collections package
        country_counts[country]=1
        
print(country_counts)
        

# How to check Country with most users then find out which country that is
maxcount = [k for k, v in country_counts.items() if v == max(country_counts.values())]
print(maxcount)
v = max(country_counts.values())
print(v)

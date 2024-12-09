dict={"apple":80,"mango":50,"papaya":60,"orange":40}
print(dict)


# add element
dict["gulab jamun"]=30
print(dict)

# remove element
del dict["orange"]
print(dict)

# access value
price=dict["gulab jamun"]
print(price)

# update the value
dict["gulab jamun"]=400
print(dict)

# clear dict
# dict.clear()
# print(dict)

# lenght of a dictionary
print(len(dict))
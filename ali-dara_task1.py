# # ---------- 1 ----------
# text = input("Text: ")
# words = text.split()
# print("Original:", text)
# print("Characters:", len(text))
# print("Words:", len(words))
# print("First word:", words[0])
# print("Last word:", words[-1])
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())

# # ---------- 2 ----------
# name = input("Full name: ")
# clean_name = " ".join(name.split())
# print("Original:", name)
# print("Cleaned:", clean_name)
# print("Length:", len(clean_name))

# # ---------- 3 ----------
# name = input("Full name: ")
# username = name.strip().lower().replace(" ", "_")
# print(username)

# # ---------- 4 ----------
# username = input("Username: ")
# print("Original:", username)
# print("Length:", len(username))
# print("Uppercase:", username.upper())
# print("Lowercase:", username.lower())
# print("Underscores:", username.count("_"))
# print("Contains space:", " " in username)

# # ---------- 5 ----------
# phone = input("Phone: ")
# clean_phone = phone.replace("-", "").replace(" ", "")
# print("Phone:", clean_phone)
# print("Length:", len(clean_phone))

# # ---------- 6 ----------
# email = input("Email: ")
# username, domain = email.split("@")
# parts = domain.split(".")
# print("Username:", username)
# print("Domain:", domain)
# print("Service:", parts[0])
# print("Extension:", parts[-1])

# # ---------- 7 ----------
# name = input("Name: ")
# age = int(input("Age: "))
# city = input("City: ")
# email = input("Email: ")
# profile = {"name": name, "age": age, "city": city, "email": email}
# print(profile)
# print("Number of items:", len(profile))

# # ---------- 8 ----------
# products = []
# products.append(input("Product 1: "))
# products.append(input("Product 2: "))
# products.append(input("Product 3: "))
# products.append(input("Product 4: "))
# products.append(input("Product 5: "))
# print(products)
# print("Count:", len(products))
# print("First:", products[0])
# print("Last:", products[-1])
# products.append(input("New product: "))
# products.remove(input("Product to remove: "))
# print("Final list:", products)

# # ---------- 9 ----------
# guests = [input("Guest 1: "), input("Guest 2: "), input("Guest 3: "),input("Guest 4: "), input("Guest 5: ")]
# print("Count:", len(guests))
# print("First guest:", guests[0])
# print("Last guest:", guests[-1])
# guests[1] = input("New name for guest 2: ")
# guests.append(input("New guest: "))
# guests.pop()
# print("Final guests:", guests)

# # ---------- 10 ----------
# text = input("Products (comma separated): ")
# items = text.split(",")
# print("List count:", len(items))
# unique_items = set(items)
# print("Set count:", len(unique_items))
# print("Set:", unique_items)

# # ---------- 11 ----------
# sentence = input("Sentence: ")
# words = sentence.split()
# unique_words = set(words)
# print("Original list:", words)
# print("Original count:", len(words))
# print("Unique words:", unique_words)
# print("Unique count:", len(unique_words))

# # ---------- 12 ----------
# text = input("Text: ")
# search = input("Search: ")
# print(search, "appears", text.count(search), "times.")

# # ---------- 13 ----------
# text = input("Text: ")
# old_word = input("Old word: ")
# new_word = input("New word: ")
# print(text.replace(old_word, new_word))

# # ---------- 14 ----------
# name = input("Name: ")
# company = input("Company: ")
# print("Hello " + name + "!\nWelcome to " + company + ".\nWe are happy to have you.")

# # ---------- 15 ----------
# comment = input("Comment: ")
# words = comment.split()
# print("Characters:", len(comment))
# print("Words:", len(words))
# print("First word:", words[0])
# print("Last word:", words[-1])
# print("'product' count:", comment.lower().count("product"))
# print("Uppercase:", comment.upper())
# print("Lowercase:", comment.lower())

# # ---------- 16 ----------
# name = input("Product name: ")
# price = float(input("Price: "))
# stock = int(input("Stock: "))
# category = input("Category: ")
# product = {"name": name, "price": price, "stock": stock, "category": category}
# print(product)

# # ---------- 17 ----------
# name = input("Product name: ")
# price = float(input("Price: "))
# quantity = int(input("Quantity: "))
# print("Product:", name)
# print("Price:", price)
# print("Quantity:", quantity)
# print("Total:", price * quantity)

# # ---------- 18 ----------
# customer = input("Customer name: ")
# order_id = int(input("Order ID: "))
# product = input("Product: ")
# price = float(input("Price: "))
# quantity = int(input("Quantity: "))
# address = input("Address: ")
# order = {"customer": customer, "order_id": order_id, "product": product,
# "price": price, "quantity": quantity, "address": address}
# print("----- Order Report -----")
# print("Customer:", order["customer"])
# print("Order ID:", order["order_id"])
# print("Product:", order["product"])
# print("Price:", order["price"])
# print("Quantity:", order["quantity"])
# print("Total:", order["price"] * order["quantity"])
# print("Address:", order["address"])

# # ---------- 19 ----------
# address = input("Address: ")
# clean_address = address.strip()
# parts = clean_address.split(",")
# print("Original:", address)
# print("Cleaned:", clean_address)
# print("Parts count:", len(parts))
# print("First part:", parts[0].strip())
# print("Last part:", parts[-1].strip())

# # ---------- 21 ----------
# person1 = set(input("Person 1: ").split(","))
# person2 = set(input("Person 2: ").split(","))
# print("Common:", person1 & person2)
# print("Only person 1:", person1 - person2)
# print("Only person 2:", person2 - person1)
# print("All:", person1 | person2)

# # ---------- 22 ----------
# card = input("Card number: ")
# card = card.replace("-", "")
# print("Card:", card)
# print("Digits:", len(card))
# print("First 4:", card[:4])
# print("Last 4:", card[-4:])
# print("Masked:", card[:4] + "****" + card[-4:])

# # ---------- 23 ----------
# name = input("Name: ")
# order_id = int(input("Order ID: "))
# product = input("Product: ")
# code = name.strip().upper().replace(" ", "-") + "-" + str(order_id) + "-" + product.strip().upper()
# print(code)

# ---------- 24 ----------
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
skills = input("Skills: ").split(",")
hobbies = input("Hobbies: ").split(",")
profile = {"name": name, "age": age, "city": city, "skills": skills, "hobbies": hobbies}
print("----- Profile -----")
print("Name:", profile["name"])
print("Age:", profile["age"])
print("City:", profile["city"])
print("Skills:", profile["skills"])
print("Hobbies:", profile["hobbies"])

# ---------- 25 ----------
review = input("Review: ")
search = input("Search word: ")
words = review.split()
print("Review:", review)
print("Characters:", len(review))
print("Words:", len(words))
print("Unique words:", len(set(words)))
print("Search word count:", review.count(search))

# ---------- 26 ----------
name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")
city = input("City: ")
raw = {"name": name, "email": email, "phone": phone, "city": city}
final = {
    "name": " ".join(name.split()).title(),
    "email": email.strip().lower(),
    "phone": phone.replace("-", "").replace(" ", ""),
    "city": city.strip().title(),
}
print("Raw:", raw)
print("Final:", final)

# ---------- 27 ----------
text = input("Text: ")
start = input("Start: ")
end = input("End: ")
print("Starts with first word:", text.startswith(start))
print("Ends with second word:", text.endswith(end))

# ---------- 28 ----------
names = [input("Name 1: "), input("Name 2: "), input("Name 3: "),
         input("Name 4: "), input("Name 5: ")]
print("Original:", names)
names.sort()
print("Sorted:", names)
names.reverse()
print("Reversed:", names)

# ---------- 29 ----------
word = "Yellow"
low = word.lower()
guessed = ""

print("*" * len(word))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))

guessed = guessed + input("Letter: ").lower()
print("\n" * 30)   # push the old output away
print(word[0] * (low[0] in guessed) + "*" * (low[0] not in guessed)
      + word[1] * (low[1] in guessed) + "*" * (low[1] not in guessed)
      + word[2] * (low[2] in guessed) + "*" * (low[2] not in guessed)
      + word[3] * (low[3] in guessed) + "*" * (low[3] not in guessed)
      + word[4] * (low[4] in guessed) + "*" * (low[4] not in guessed)
      + word[5] * (low[5] in guessed) + "*" * (low[5] not in guessed))


# or this one 
print("*****",end="\r")
word = input()
print(word)

# ---------- 30 ----------
a = int(input("input1: "))
b = int(input("input2: "))
c = int(input("input3: "))
print(max(a, b, c))

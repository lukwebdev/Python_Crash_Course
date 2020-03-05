gueast = ["Ewa", "Mark", "John"]

invite = f"Hi {gueast[0]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[1]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[2]}, I woudlike invite you for diner!"
print(invite)

print(f"{gueast[0]} isn't comming!")

# gueast[0] = "Ola"
del(gueast[0])
gueast.insert(0, "Ola")

invite = f"Hi {gueast[0]}, I woudlike invite you for diner!"
print(invite)

print("We found a bigger dinner table")

gueast.insert(0, "Ala")
gueast.insert(2, "Ciara")
gueast.append("Zenek")

invite = f"Hi {gueast[0]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[1]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[2]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[3]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[4]}, I woudlike invite you for diner!"
print(invite)
invite = f"Hi {gueast[5]}, I woudlike invite you for diner!"
print(invite)

print("I can invite only two people for dinner")

invite = gueast.pop()
print(f"Sorry {invite}, party is cancel")
invite = gueast.pop()
print(f"Sorry {invite}, party is cancel")
invite = gueast.pop()
print(f"Sorry {invite}, party is cancel")
invite = gueast.pop()
print(f"Sorry {invite}, party is cancel")

del(gueast[1])
del(gueast[0])

print(gueast)
"""
If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

guest = ['arvind', 'bary', 'charlie']
print("Initial List of guest")
for g in guest:
    print(f"\nDear {g.title()},")
    print("You are cordially invited to a special dinner gathering.")

"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
"""
guest_unavailable = 'bary'
print(f"\nUnfortunately, {guest_unavailable.title()} can't make it to the dinner.")
guest.remove(guest_unavailable)

new_guest = 'bharath'
guest.insert(1, new_guest)
print(f"\nSecond list of guest {guest}")
for g in guest:
    print(f"\nDear {g.title()}")
    print("You are cordially invited to a special dinner gathering.")

"""
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

print(f"\n Second list guest {guest}")

new_guest_1 = 'anand'
guest.insert(0, new_guest_1)

new_guest_2 = 'bhubaneswar'
guest.insert(2, new_guest_2)

new_guest_3 = 'dany'
guest.append(new_guest_3)

print(f"\nFinal Guest List for the dinner {guest}")
for g in guest:
    print(f"\nDear {g.title()}")
    print("You are cordially invited to a special dinner gathering.")
    print("We look forward to an evening of stimulating conversation and delightful food.")

"""
You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of
your program.
"""

print("\nUnfortunately, the new dinner table won’t arrive in time.")
print("I can invite only two people for dinner.\n")

remove_guest_1 = guest.pop()
remove_guest_2 = guest.pop()

print(f"Sorry {remove_guest_1}, I can’t invite you to dinner.\n")
print(f"Sorry {remove_guest_2}, I can’t invite you to dinner.\n")

for g in guest:
    print(f"{g}, you're still invited to dinner!\n")

while len(guest) > 0:
    del guest[0]

print(f"Final guest list: {guest}")
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
•
Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
•
Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
•
Print a second set of invitation messages, one for each person who is still in
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
•
Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
•
Use insert() to add one new guest to the beginning of your list.
•
Use insert() to add one new guest to the middle of your list.
•
Use append() to add one new guest to the end of your list.
•
Print a new set of invitation messages, one for each person in your list.
"""

print(f"\n Second list guest {guest}")

new_guest_1 = 'Anand'
guest.insert(0, new_guest_1)

new_guest_2 = 'Bhubaneswar'
guest.insert(2, new_guest_2)

new_guest_3 = 'Dany'
guest.append(new_guest_3)

print(f"\nFinal Guest List for the dinner {guest}")
for g in guest:
    print(f"\nDear {g.title()}")
    print("You are cordially invited to a special dinner gathering.")
    print("We look forward to an evening of stimulating conversation and delightful food.")
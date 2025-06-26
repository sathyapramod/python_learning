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
print(f"\nFinal list of guest {guest}")
for g in guest:
    print(f"\nDear {g.title()}")
    print("You are cordially invited to a special dinner gathering.")

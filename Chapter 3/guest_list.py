# 3.4: My inital guest list of people invited to dinner

guest_list = ['spencer', 'mona', 'cece']

spencer_invite = "\nHello " + (guest_list[0]).title() + ", you're cordially invited to dinner."
print(spencer_invite)

mona_invite = "\nHello " + (guest_list[1]).title() + ", you're cordially invited to dinner."
print(mona_invite)

cece_invite = "\nHello " + (guest_list[-1]).title() + ", you're cordially invited to dinner."
print(cece_invite)

# 3.5: Changing the guest list
# Cece Drake could not make it to dinner, so I use the .pop() function to remove her name from the guest list.
popped_cece = guest_list.pop(-1)
print("\n\tUnfortunately, " + popped_cece.title() + " could not make it to dinner.")

# Since Cece is gone, I add Hanna to replace her at the end of the guest list.
guest_list.append('hanna')

# The guest list should be Spencer, Mona, Hanna
# Remaking the invitations

spencer_invite = "\n" + (guest_list[0]).title() + ", you're still invited."
print(spencer_invite)

mona_invite = "\n" + (guest_list[1]).title() + ", you're still invited."
print(mona_invite)

hanna_invite = "\nHello " + (guest_list[-1]).title() + ", you're cordinally invited to dinner."
print(hanna_invite)

# 3.6: A bigger table
print("\n\tWhy, I have found a bigger dinner table. Now more people will be able to attend !")

# Using insert() to add Emily to the beginning of the list
guest_list.insert(0, 'emily')
#The list should look like Emily, Spencer, Mona, Hanna

# Using insert() to add Aria to the middle of the list
guest_list.insert(2, 'aria')
#The list should go: Emily, Spencer, Aria, Mona, Hanna

# Using append() to add Ali to the end of the list.
guest_list.append('ali')
# The list should now look like: Emily, Spencer, Aria, Mona, Hanna, Ali

# A new set of invitations
emily_invite = "\nHello " + (guest_list[0]).title() + ", you're cordinally invited for dinner."
print(emily_invite)

spencer_invite = "\nYou're still invited, " + (guest_list[1]).title() + "."
print(spencer_invite)

aria_invite = "\nHello " + (guest_list[2]).title() + ", you're cordinally invited for dinner."
print(aria_invite)

mona_invite = "\nYouu're still invited, " + (guest_list[3]).title() + "."
print(mona_invite)

hanna_invite = "\nStill do come, " + (guest_list[-2]).title() + "."
print(hanna_invite)

ali_invite = "\nHello " + (guest_list[-1]).title() + ", you're cordinally invited for dinner."
print(ali_invite)

#Using the len() function to get number of people attending from the new list.
guests_attending = len(guest_list)
print("\n\tNumber of guests attending: " + str(guests_attending) )

# 3.7 Shrinking guest list
print("\n\tUnfortunately, it seems that the staff can't do their jobs. I could now only invite 2 people.")

# I will use the .pop() function to remove the following people from the list.
popped_emily = guest_list.pop(0)
print("\nApologies, " + popped_emily.title() + ", there's always another dinner I could host.")

popped_aria = guest_list.pop(1)
print("\nApologies, " + popped_aria.title() + ", there's always another dinner I could host.")

popped_mona = guest_list.pop(1)
print("\nApologies, " + popped_mona.title() + ", there's always another dinner I could host.")

popped_hanna = guest_list.pop(1)
print("\nApologies, " + popped_hanna.title() + ", there's always another dinner I could host.")

# The last two people who are still invited are Spencer and Ali.
spencer_invite = "\nHi " + (guest_list[0]).title() + ", you're still invited. Do come."
print(spencer_invite)

ali_invite = "\nHi " + (guest_list[-1]).title() + ", you're still invited. Do come."
print(ali_invite)

# Removing Spencer and Ali from the list
del guest_list[0]
del guest_list[-1]

# Making sure the guest list is empty
print(guest_list)

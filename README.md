# Deactivate-from-last-login
 Script to deactivate a user based on their last login parameter for Rocket.Chat

The script can be used up to 5,000 users.

The way it works is:

-> Get the list of users in the Workspace.
-> Verifies each user's info and get the params: `username` & `userId`.
-> Using the `userId` param, it gets the `last_login` info from each user
-> If the info is less than certain amount of days, it can deactivate the user. It always ask before to proceed if you would like to deactivate this user.
-> It can also be used to Activate some users, changing some params for it.

Hope it helps :rocket:
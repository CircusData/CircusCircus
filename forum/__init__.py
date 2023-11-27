""" __init__.py is not used, only included to make forum a package, for whatever reason"""

"""
Static file comparison to Dev on 11/27.
The file in here is more updated than Dev now.  Changes noted from Dev

Merge of .profileposts overwrote and removed styling, see from original:
.profileposts{
	overflow: hidden;
	vertical-align: middle;
	padding: 0.5%;
	margin-bottom: none;
	border-bottom: dashed;
}

From merged Dev:
.profileposts{
border-bottom: dashed;
}
FIXED


Add entire footer from Dev branch to this style.css file - FIXED

Count title in Dev is spaced wrong, if spacing matters:
.counttitle{
    float: right;
	    margin-left: auto;
	    margin-right: 0;
	    text-align: right;
}

.counttitle{
    float: right;
    margin-left: auto;
    margin-right: 0;
    text-align: right;
}
FIXED

"""



"""
Template Comparison to Dev on 11/27

createpost.html - matches
footer.html - matches
header.html - updated to match
    PI1 - header opening is using a flask route command to try and call the static folder url without a static view existing
layout.html - updated to mostly match (kept better spacing)
    PI1 - double indent of all divs and most calls within page div, FIXED in my version
    PI2 - added a javascript call in the head, no idea if its working or what it produces. 
login.html - matches
profile.html - matches
send_message.html - matches
subforum.html - matches
subforums.html - matches
user_settings.html - matches
viewmessage.html - matches
viewpost.html - Leaving likes out of comments since not associated in Model. 
    PI1 - Like buttons all crammed into posttime class, may be fine, but links aren't working
    PI2 - Does same with comment except missing <br> formatting tag at end and no links to anything.
viewprofile.html - matches

"""
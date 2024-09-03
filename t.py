msg = "How to split the msg in Python?"

if "&" in msg:
    words = msg.split("&")

    if len(words) > 1:
        words2 = words[1].split(",")
        if len(words2) == 2:
            latitude = float(words2[0])
            longitude = float(words2[1])
        else:
            print("Invalid format for latitude and longitude.")
    else:
        print("No latitude and longitude found after splitting.")
else:
    print("No '&' found in the msg.")

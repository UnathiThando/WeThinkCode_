def filename():
    filename = input("Enter a file name: ").lower()
    
    if filename.endswith((".png", ".jpg", ".gif", ".jpeg")):
        print("image/" + filename.split('.')[-1])
    elif filename.endswith((".pdf", ".txt", ".zip")):
        print("application/" + filename.split('.')[-1])
    else:
        print("Filename unavailable")

filename()

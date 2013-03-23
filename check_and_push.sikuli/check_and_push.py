num_of_records = 50308
scroll_times = 16

def test():
    hover("iWJ.png")
    doubleClick("iWJ.png")
    click("1364018307252.png")
    click("1364017967246.png")
    click("1364018307252.png")

def push_record_to_github():
    click("1364022281123.png")
    type("c", KEY_CMD) # copy url

    switchApp("Terminal")
    type("pbpaste >> record.txt")
    type(Key.ENTER)
    type("echo '' >> record.txt")
    type(Key.ENTER)    
    type("git add record.txt")
    type(Key.ENTER)
    type("git commit -m 'add new record by sikuli script'")
    type(Key.ENTER)
    type("git push -u origin master")
    type(Key.ENTER)
    switchApp("Safari")

def check():
    if exists("iWJ.png"):
        hover("iWJ.png")        # for human beings to see
        sleep(1)
        push_record_to_github()
        return True
    return False

    

# main program
for n in range(num_of_records):
    sleep(4)    # waiting for page loading 
    while(not exists("Ji.png")):
        if check() is True:
            type(Key.END)       # scroll to end
            break               # and leave loop
        else: # not found, continue...
            type(Key.PAGE_DOWN) # scroll down
    click("Ji.png")
    
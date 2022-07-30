#script variables

blacklist = []
whitelist = []

#starts the script and get user input
def start_script():     
    print("type your comand or 'help' to  view a list of all comands")
    get_command(blacklist, whitelist)

#Finds and reads and splits the arquive in lines
def get_arq(inpt, blacklist, whitelist):
    x = inpt.split()
    elem = len(x)
    if elem == 3:        
        with open(x[2], "rb") as file:
            text = file.read()
        text_lines = text.splitlines()
        pop_char_list(inpt, text, text_lines)
    else:
        get_command(blacklist, whitelist)


#reads the entire text and populates char_list with all the possible individual characters in the text
def pop_char_list(inpt, text, text_lines):
    txt = (str(text))
    charlist = []
    lenght = len(txt)
    i = 0
    while i < lenght:
        if txt[i] in charlist:
            i = i + 1
        else:
            charlist.append(txt[i])
            i = i + 1
    x = inpt[1]
    print(x)
    #if x == "-nl" or x == "-wl" or x == "-bl":
    plot_nl(inpt, charlist, text_lines)
    #else:
    #    print("invalid comand")


#plots graph with using the chosen command
def plot_nl(inpt, charlist, text_lines):
    letter_dict = {}
    letter_count = []
    list_line = []   
    #gets whitelist,blacklist or all the chars
    x= inpt.split()
    if x[1] == "-wl":
        charlist = []
        charlist = whitelist
    if x[1] == "-bl":
        k = 0
        l = 0
        while k < len(charlist):
            while l < len(blacklist):
                if charlist[k] == blacklist[l]:
                    charlist.remove(blacklist[l])
                l = l + 1
            l = 0
            k = k + 1
    i = len(charlist) - 1
    while i > 0:
        letter = charlist[i]
        e = 0
        while e < len(text_lines):
            line = str(text_lines[e])
            a = 0
            while a < len(line):
                list_line.append(line[a])
                a = a + 1
            letter_count.append(list_line.count(letter)) 
            list_line = []
            e = e + 1
        print(letter)
        print(letter_count)
        letter_dict[letter] = letter_count
        letter_count = []
        i = i - 1
    
    
def plot_wl(charlist, text_lines):
    letter_dict = {}
    letter_count = []
    list_line = []
    i = len(charlist) - 1
    print(charlist)
    while i > 0:
        letter = charlist[i]
        e = 0
        while e < len(text_lines):
            line = str(text_lines[e])
            a = 0
            while a < len(line):
                list_line.append(line[a])
                a = a + 1
            letter_count.append(list_line.count(letter))
            e = e + 1
        print(letter)
        print(letter_count)
        letter_dict[letter] = letter_count
        letter_count = []
        i = i - 1
    
#adds element to the white list
def add_wl(inpt, blacklist, whitelist):
    x = inpt.split('+')     
    #reads if list already has the element
    if x[1] in whitelist:
        print("Whitelist already has this element")
        get_command(blacklist, whitelist)
    else:
        whitelist.append(x[1])
        get_command(blacklist, whitelist)


#prints whitelist elements
def show_wl(blacklist, whitelist):
    if len(whitelist) == 0:
        print("White list is empty")
    else:
        print(whitelist)
    get_command(blacklist, whitelist)
    
    
#adds element to the black list
def add_bl(inpt, blacklist, whitelist):
    y = inpt.split('+')     
    #reads if list already has the element
    if y[1] in blacklist:
        print("Blacklist already has this element")
    else:
        blacklist.append(y[1])
    get_command(blacklist, whitelist)


#prints whitelist elements
def show_bl(blacklist, whitelist):
    if len(blacklist) == 0:
        print("White list is empty")
    else:
        print(blacklist)
    get_command(blacklist, whitelist)

   
#clear whitelist    
def clear_wl(blacklist, whitelist):
    whitelist.clear()
    print("whitelist is now empty")
    get_command(blacklist, whitelist)
 
 
#clear blacklist    
def clear_bl(blacklist, whitelist):
    blacklist.clear()
    print("blacklist is now empty")
    get_command(blacklist, whitelist)
  
  
#Shows the help screen
def show_help(blacklist, whitelist):
    print("Help ->\n" +
              "plot -nl 'arquive path'  -> plots a graph for the arquive in the path input with all the possible elements\n" +
              "plot -wl 'arquive path'  -> plots a graph for the arquive in the path input only with the elements in the white list\n" +
              "plot -bl 'arquive path'  -> plots a graph for the arquive in the path input with all the elements except the ones in the black list\n" +
              "wl +'element'            -> adds the input element to the white list\n" +
              "bl +'element'            -> adds the input element to the black list\n" +
              "show wl                  -> shows the elements in the white list\n" + 
              "show bl                  -> shows the elements in the black list\n" +
              "clear wl                 -> clears the white list\n" +
              "clear bl                 -> clears the black list\n" +
              "help                     -> show all the available comands\n" + 
              "exit                     -> stops the script")
    get_command(blacklist, whitelist)


#get user input
def get_command(blacklist, whitelist):
    inpt = input()
    if inpt == 'help':
        show_help(blacklist, whitelist)
        inpt = ""
    if inpt.startswith('plot ') and inpt.endswith('.txt'):
        get_arq(inpt, blacklist, whitelist)
        inpt = ""
    if inpt.startswith('wl +'):
        add_wl(inpt, blacklist, whitelist)
        inpt = ""
    if inpt.startswith('bl +'):
        add_bl(inpt, blacklist, whitelist)
        inpt = ""
    if inpt == "show wl":
        show_wl(blacklist, whitelist)
        inpt = ""
    if inpt == "show bl":
        show_bl(blacklist, whitelist)
        inpt = ""
    if inpt == "clear wl":
        clear_wl(blacklist, whitelist)
        inpt = ""
    if inpt == "clear bl":
        clear_bl(blacklist, whitelist)
        inpt = ""
    if inpt == "exit":
        exit()
    if inpt == "":
        get_command(blacklist, whitelist)
    else:
        print("invalid comand")
        get_command(blacklist, whitelist)

start_script()

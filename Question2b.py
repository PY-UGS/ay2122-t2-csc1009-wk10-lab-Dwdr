def switchcase(modules):        #function for switchcase
    switches = {
        "CSC1001": "Introduction to Computing",
        "CSC1002": "Mathematics 1",
        "CSC1003": "Programming Methodology",
        "CSC1004": "Computer Organisation and Architecture",
        "CSC1005": "Business Information Technology",
        "CSC1006": "Mathematics 2",
        "CSC1007":"Operating Systems",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object Oriented Programming",
        "CSC1010": "Computer Networks"
    }
    return switches.get(modules, "Invalid Module Code")     #if not in module, return invalid module code
modulecode = input("Enter Module Code (e.g. CSC1001): ")    #get input from user
print("The Module for code " + modulecode + " is " + switchcase(modulecode.upper()))    #change input to uppercase in case user inputs csc instead of CSC
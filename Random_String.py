from random import choice

#difine allowed characters by ASCII codes:
char_list = [chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]

#or could be:
another_list = ["a", "g", "3", "&"]


#most simple function:
def rand_string(n): #n -> length of generated string
    result = ''
    for i in range(n):
        result += choice(char_list)
    return result
        

#create non-duplicated strings:
def rand_string(inp_list, n):
    result = ''
    for i in range(n):
        result += choice(char_list)
    
    #if generated string is duplicated:
    if(result in inp_list):
        #generate another string:
        return rand_string(inp_list, n)
    else:
        return result

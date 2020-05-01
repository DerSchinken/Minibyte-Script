import sys
from itertools import islice

try:

    argv1 = sys.argv[1]

    variables = {}

    script = open(""+argv1+"", "r").read().replace("\n", "").split(";")

    def commands(script_tmp, i):
        global variables
        global s

        break_while = False

        #print
        if script_tmp[i].replace(" ", "").startswith('print:"'):
            print(script_tmp[i][8:].replace('"', ""))
        elif script_tmp[i].startswith('print:'):
            try:
                print(variables[script_tmp[i].replace(" ", "").replace('"', "")[6:]])
            except KeyError:
                print("NameError at line " + str(i) + " '" + script_tmp[i] + ";'")
        elif script_tmp[i].startswith('  print:'):
            try:
                print(variables[script_tmp[i].replace(" ", "").replace('"', "")[8:]])
            except KeyError:
                print("NameError at line " + str(i) + " '" + script_tmp[i] + ";'")
            

        #define
        elif script_tmp[i].replace("  ", "").startswith("define:"):
            variables[script_tmp[i][8:].replace(" ", "").split("=")[0]] = script_tmp[i][8:].replace(" ", "", 2).replace('"', "").split("=")[1]

        #add
        elif script_tmp[i].replace("  ", "").startswith("add:"):
            try:
                variables[script_tmp[i][5:].replace(" ", "").split("=")[0]] = int(variables[script_tmp[i][5:].replace(" ", "").split("=")[1].split("+")[0]]) + int(variables[script_tmp[i][5:].replace(" ", "").split("=")[1].split("+")[1]])
            except ValueError:
                variables[script_tmp[i][5:].replace(" ", "").replace('"', "").split("=")[0]] = str(variables[script_tmp[i][5:].replace(" ", "").replace('"', "").split("=")[1].split("+")[0]]) + str(variables[script_tmp[i][5:].replace(" ", "").split("=")[1].split("+")[1]])

        #dec
        elif script_tmp[i].replace("  ", "").startswith("dec:"):
            try:
                variables[script_tmp[i][5:].replace(" ", "").split("=")[0]] = int(variables[script_tmp[i][5:].replace(" ", "").split("=")[1].split("-")[0]]) - int(variables[script_tmp[i][5:].replace(" ", "").split("=")[1].split("-")[1]])        
            except ValueError:
                print("ValueError at lin: " + str(i) + " '" + script_tmp[i] + ";'")
                exit()

        #input
        elif script[i].replace("  ", "").startswith("inp:"):
            variables[script_tmp[i][5:]] = input()

        #for: 50 iterations , 2 commands to execute
        #for loop
        elif script[i].replace("  ", "").startswith("for:"):
            try:
                for o in range(int(script[i].split(",")[0][5:])-1):
                    for p in range(int(script[i].split(",")[1])):
                        commands(script_tmp, p+i+1)
                        if break_while:
                            #break_while = False
                            break
                    if break_while:
                        break_while = False
                        break
                for o in range(int(script[i].split(",")[1])-1):
                    next(s)
                    #pass
            except SyntaxError:
                print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")

        # This doesnt work
        #while: commands to execute
        #while loop
#        elif script[i].replace("  ", "").startswith("while:"):
#            try:
#                old_i = i
#                while True:
#                    i = old_i
#                    for l in range(int(script[i][6:])):
#                        commands(script_tmp, i+l+1)
#                        if break_while:
#                            #break_while = False
#                            break
#                    if break_while:
#                        break_while = False
#                        break
#                for k in range(int(script[i][6:])):
#                    next(s)
#            except SyntaxError:
#                print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")

        #this should work but if it does idk i will try that later
        #break
        elif script[i].replace("  ", "").startswith("break"):
            try:
                break_while = True
            except SyntaxError:
                print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")

        #comments
        elif script_tmp[i].replace("  ", "").startswith("#"):
            pass

        #free lines
        elif script_tmp[i].replace("  ", "").replace("\n", "").replace(" ", "") == "":
            pass

        #syntax error
        else:
            print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")
            exit()

    s = iter(range(len(script)))

    for i in s:
        script_tmp = script
        commands(script_tmp, i)

except KeyboardInterrupt:
    print("KeyboardInterrupt at line: " + str(i) + " '" + script[i] + ";'")
except IndexError:
    print("")



import sys
from itertools import islice

def prog_lang():
    global variables
    global s
    
    try:

        argv1 = sys.argv[1]

        variables = {}

        script = open(""+argv1+"", "r").read().replace("\n", "").split(";")

        def commands(script_tmp, i):
            global variables
            global s

            ##########
            # Basics #
            ##########

            #print
            if script_tmp[i].replace(" ", "").startswith('print:"'):
                print(script_tmp[i][8:].replace('"', ""))
            elif script_tmp[i].startswith('print:'):
                try:
                    print(variables[script_tmp[i].replace(" ", "").replace('"', "")[6:]])
                except KeyError:
                    print("NameError at line " + str(i) + " '" + script_tmp[i] + ";'")
                    exit()
            elif script_tmp[i].startswith('  print:'):
                try:
                    print(variables[script_tmp[i].replace(" ", "").replace('"', "")[8:]])
                except KeyError:
                    print("NameError at line " + str(i) + " '" + script_tmp[i] + ";'")
                    exit()

           #input
            elif script[i].replace("  ", "").startswith("inp:"):
                variables[script_tmp[i][5:]] = input()

            #for: iterations , commands to execute
            #for loop
            elif script[i].replace("  ", "").startswith("for:"):
                try:
                    for o in range(int(script[i].split(",")[0][5:])-1):
                        for p in range(int(script[i].split(",")[1])):
                            ret = commands(script_tmp, p+i+1)
                            if ret == "EXIT LOOP":
                                break
                        if ret == "EXIT LOOP":
                            break
                    for o in range(int(script[i].split(",")[1])-1):
                        next(s)
                except SyntaxError:
                    print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")
                    exit()

            #while: amount of commands to execute
            #while loop
            elif script[i].replace("  ", "").startswith("while:"):
                try:
                    while True:
                        for l in range(int(script[i][6:])):
                            ret = commands(script_tmp, i+l+1)
                            if ret == "EXIT LOOP":
                                break
                        if ret == "EXIT LOOP":
                            break
                            
                    for k in range(int(script[i][6:])):
                        next(s)
                except SyntaxError:
                    print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")
                    exit()

            #this works in while but not in for
            #break
            elif script[i].startswith("break"):
                try:
                    return "EXIT LOOP"
                except SyntaxError:
                    print("SyntaxError at line: " + str(i) + " '" + script_tmp[i] + ";'")
                    exit()

            # Commes soon
            # IF
#            elif "==" in script[i]:
#                if int():
#                    pass

            #comments
            elif script_tmp[i].replace("  ", "").startswith("#"):
                pass
             
            ########################
            # Calculation commands #
            ########################
            # NEEDS A REWORK!
            # Now it can only handle variables not plain values so
            # add, dec, mult: 10 +, -, * 10 wont work

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

            #multiply
            elif script_tmp[i].replace("  ", "").startswith("mult:"):
                try:
                    variables[script_tmp[i][6:].replace(" ", "").split("=")[0]] = int(variables[script_tmp[i][6:].replace(" ", "").split("=")[1].split("*")[0]]) * int(variables[script_tmp[i][6:].replace(" ", "").split("=")[1].split("*")[1]])
                except ValueError:
                    variables[script_tmp[i][6:].replace(" ", "").replace('"', "").split("=")[0]] = str(variables[script_tmp[i][6:].replace(" ", "").replace('"', "").split("=")[1].split("*")[0]]) * int(variables[script_tmp[i][6:].replace(" ", "").split("=")[1].split("*")[1]])

            ########
            # Misc #
            ########

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
        exit()
#    except IndexError:
#        print("MEScript Command usage:     MEScript [file path]")
#        exit()

if __name__ == "__main__":
    prog_lang()

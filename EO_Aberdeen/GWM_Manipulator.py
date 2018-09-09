
start_string1 = "OPTIMAL RATES FOR EACH FLOW VARIABLE"
start_string2 = "Q1"
end_string = "------------        ------------        ------------"
# starter_string = "Q1    "
line_cnt = 0
start_string1_flag = False
print_flag = False

with open("supply2.gwmout.parallel", 'r') as f:

    for line in f:
        line_cnt = line_cnt + 1

        if start_string1 in line:
            start_string1_flag = True
        if start_string1_flag and start_string2 in line:
            print_flag = True
        elif end_string in line:
            print_flag = False
            start_string1_flag = False

        if print_flag:
            print(line)

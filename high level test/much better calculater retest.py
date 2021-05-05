#options provider
enough_value_checker_1 = 2
enough_value_checker_2 = 2
value_storage_helper = 1
value_storage = dict()
value1 = 0
opr = ""
value2 = 0
result = 0
ending_var = 1
option_helper_1 = 2
option_helper_2 = 1
var_creator = dict()
var_name = ""
var_value = 0
operator_value_handler = 0
enough_operations_checker_1 = 1
enough_operations_checker_2 = 2
looping_one_step_1 = 1
looping_one_step_2 = 2


option_helper_2 = int(input("do you want to run calculater or declare your own variable(1 = declare variable 2 = calculater)----->"))


if option_helper_1 == option_helper_2:
    opr = input("enter in your operator:")
    while enough_value_checker_1 == enough_value_checker_2:
        try:
            value_storage["Value" + str(value_storage_helper)] = int(input("enter in your value"))
        except ValueError:
            value_storage["Value" + str(value_storage_helper)] = 0
        if value_storage["Value" + str(value_storage_helper)] == 0:
            enough_value_checker_2 = 1
        value_storage_helper += 1
        operator_value_handler += 2
else:
    var_num = int(input("How many variables would you please to create:"))
    for x in range(var_num):
        var_name = input("enter in your variable name:")
        var_value = input("enter in your variable value:")
        var_creator[var_name] = var_value
        var_name = ""
        var_value = 0

operator_value_handler += 2
print(str(1) + "   " +str(operator_value_handler))
print(str(2) + "   " + str(value_storage_helper))

for x in range(operator_value_handler):
    # if opr == "+":
        # result += value_storage["Value" + str(looping_one_step_1)] + value_storage["Value" + str(looping_one_step_2)]
    looping_one_step_1 += 2
    looping_one_step_2 += 2
print(str(3) + "    " + str(looping_one_step_1))
print(str(4) + "    " + str(looping_one_step_2))
print(result)
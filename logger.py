def logger(a):
    with open('logs.txt' , 'a') as file:
        file.write(a);

logger("first action1\n")
logger("second action2")
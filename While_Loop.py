#Activity 1: Chores Checklist
Chores = ["Make your bed", "Feed the pet", "Take out the trash", "Wash the dishes"]

Orig_Count = len(Chores)

print("You have {} chores to finish today".format(Orig_Count))

Completed_Count = 0

while len(Chores) > 0:

    next_chore = Chores[0]
    ans = input("\nHave you finished: {}? (Y/N): ".format(next_chore))
    if ans.lower() == "y":
        Chores.pop(0)
        Completed_Count = Completed_Count + 1
        print("Great job! Chore completed")
    else:
        print("Okay, finish it and come back!")
    
print("You have completed {} chores and have {} left to do".format(Completed_Count, len(Chores)))
print("\n=========== ALL CHORES COMPLETED! ===========")
print("\nGreat work finishing your entire checklist today!\nYou have completed {} chores and have {} left to do".format(Completed_Count, len(Chores)))

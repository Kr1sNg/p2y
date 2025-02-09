
<<<<<<< HEAD
# def balanced_brackets(my_string: str):
#     if len(my_string) == 0:
#         return True
#     if my_string[0] in "])":
#         return False
#     if my_string[0] == '(':
#         if len(my_string) == 1:
#             return False
#         if my_string[-1] == ')':
#             return balanced_brackets(my_string[1:-1])
#         elif my_string[-1] in "](":
#             return False
#         else:
#             return balanced_brackets(my_string[:-1])
#     elif my_string[0] == '[':
#         if len(my_string) == 1:
#             return False
#         if my_string[-1] == ']':
#             return balanced_brackets(my_string[1:-1])
#         elif my_string[-1] == ")[":
#             return False
#         else:
#             return balanced_brackets(my_string[:-1])
#     else:
#         return balanced_brackets(my_string[1:])

def balanced_brackets(mj: str):
    if len(mj) == 0:
        return True
    if not mj[0] in "()[]":
        return balanced_brackets(mj[1:])
    if not mj[-1] in "()[]":
        return balanced_brackets(mj[:-1])
    if mj[0] == '(' and mj[-1] == ')':
        return balanced_brackets(mj[1:-1])
    if mj[0] == '[' and mj[-1] == ']':
        return balanced_brackets(mj[1:-1])
    else:
        return False
    
    


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    print(balanced_brackets("((x)"))
    print(balanced_brackets("x[[]"))
=======
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])
>>>>>>> 3e7d1c54b079a3a498cf03351408be9bb4035f1c

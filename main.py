# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
  # Use a breakpoint in the code line below to debug your script.
  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# It takes useCase such as "sme-lending", "bnpl" and returns a score.
def scoring(useCase):
  # Use a breakpoint in the code line below to debug your script.
  print(f'Hi, {useCase}')  # Press ⌘F8 to toggle the breakpoint.
  if useCase == "sme-lending":
    # Use a corresponding model to score
    return 0.8
  elif useCase == "bnpl":
    return 0.9


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

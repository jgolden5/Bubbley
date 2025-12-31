import readchar

def first_is_higher_priority(a, b):
  print(f"\nWhich is higher priority?")
  print(f"1) {a}")
  print(f"2) {b}")
  print("Choose 1 or 2: ", end="", flush=True)
  choice = readchar.readkey()
  print(choice)
  if choice == "1" or choice == "2":
    return choice == "1"
  else:
    print("Input invalid, try again")
    first_is_higher_priority(a, b)

def user_compare_items(items):
  n = len(items)
  for i in range(n):
    swapped = False
    for j in range(n - i - 1):
      if not first_is_higher_priority(items[j], items[j+1]):
        items[j], items[j+1] = items[j+1], items[j]
        swapped = True
    if not swapped:
      break
  return items

def provide_items():
  raw = input('Enter items to be categorized, separated by commas:\n> ')
  items = []
  for item in raw.split(","):
    cleaned_item = item.strip()
    if cleaned_item:
      items.append(cleaned_item)
  return items

def display_sorted_items(sorted_items):
  print("Here are your items, sorted from highest to lowest priority:")
  n = 1
  for item in sorted_items:
    print(f"#{n}: {item}")
    n += 1

def main():
  print("Welcome to Bubbley -- a manual prioritization tool!\n")
  print("Enter items one per line. Leave blank to finish.\n")
  items = provide_items()
  if items:
    sorted_items = user_compare_items(items);
    display_sorted_items(sorted_items)
  else:
    print("Sorry, no valid items were found")

main()

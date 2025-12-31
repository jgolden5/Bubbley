#Original AI-generated template as a starter

def ask_user(a, b):
  print(f"\nWhich is higher priority?")
  print(f"1) {a}")
  print(f"2) {b}")
  choice = input("Choose 1 or 2: ").strip()
  return choice == "1"

def bubbley(items):
  n = len(items)
  for i in range(n):
    swapped = False
    for j in range(n - i - 1):
      if not ask_user(items[j], items[j+1]):
        items[j], items[j+1] = items[j+1], items[j]
        swapped = True
    if not swapped:
      break
  return items

def provide_inputs():
  raw = input('Enter items to be categorized, separated by commas:\n> ')
  items = []
  for item in raw.split(","):
    cleaned_item = item.strip()
    if cleaned_item:
      items.append(cleaned_item)
      print("Appeneded element", cleaned_item)

def main():
  print("Welcome to Bubbley — a manual prioritization tool!\n")
  print("Enter items one per line. Leave blank to finish.\n")
  inputs = provide_inputs()
  #bubbley();

main()

def reverse_text(text):
  """Reverses a given string of text."""
  return text[::-1]

def greet(name):
  """Greets the given name."""
  return f"Hello, {name}!"

if __name__ == "__main__":
  input_string = "Hello World!"
  reversed_string = reverse_text(input_string)
  print(f"Original: {input_string}")
  print(f"Reversed: {reversed_string}")

  person_name = "Alice"
  greeting = greet(person_name)
  print(greeting)
def get_term(n):
  """Calculates the nth term of the series."""
  return 3*n**2 - 7*n + 5

num_terms = 20
total_sum = 0

for n in range(1, num_terms + 1):
  term_value = get_term(n)
  total_sum += term_value

print(f"The sum of the series up to {num_terms} terms is: {total_sum}")
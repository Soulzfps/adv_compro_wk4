children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}
]

# Define the eligibility criteria using a lambda function
criteria = lambda child: child["age"] > 3 and child["height"] > 100

# Use filter() with the lambda function to get eligible children
eligible_children = list(filter(criteria, children))

print(eligible_children)
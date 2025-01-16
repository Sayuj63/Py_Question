# List comprehension
list_comp = [x ** 2 for x in range(10_000)]
print("List Comprehension - Memory Size:", list_comp.__sizeof__())

# Generator expression
gen_expr = (x ** 2 for x in range(10_000))
print("Generator Expression - Memory Size:", gen_expr.__sizeof__())

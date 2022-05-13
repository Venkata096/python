def gen_months():
    print("generating months")
    yield "jan"
    yield "feb"
    yield "mar"
    yield "apr"
    yield "may"
    
g = gen_months()
print(type(g))
for x in g:
    print(x)
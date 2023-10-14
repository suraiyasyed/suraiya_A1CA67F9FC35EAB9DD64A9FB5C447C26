# Program to perform linear search and display the index of target in a list if found
def linear_search_product(productList, target_product):
	indices=[]
	for i,p in enumerate(productList):
		if p == target_product:
			indices.append(i)
	return indices

products = ["leather", "jacket", "overcoat", "jean","jacket", "rain coat", "trench coat", "fleece","jacket"]
target1 = "Coat"
target = "jacket"
result= linear_search_product(products,target)

print("When Target is found: ")
print(result)


print("\nWhen Target is not found: ")

result1= linear_search_product(products,target1)
print(result1)
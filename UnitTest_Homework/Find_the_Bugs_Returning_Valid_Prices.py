def has_valid_price(product):
	if product == None:
		return False
	if ("product" not in product) or ("price" not in product):
		return False
	if type(product["price"]) == str or product["price"] == None:
		return False
	return product["price"] >= 0
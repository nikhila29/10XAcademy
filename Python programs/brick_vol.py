def calculate_total_price_of_bricks(dimensions, brick_count):
	w=60
	h=40
	if dimensions[0]!=-1:
		w=dimensions[0]
	if dimensions[1]!=-1:
		h=dimensions[1]
	vol=volume(length=100,width=w,height=h)
	total_price=calculate_price(vol*brick_count)
	return total_price
         


def volume(length=100,width=60,height=40):
    return length*width*height

def calculate_price(volume, price=0.00005):
    return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)
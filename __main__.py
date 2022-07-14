import requests
import color_print
from color_print import crint

def try_parse_int(string: str, err: str):
	if string.isdigit():
		return int(string)
	print(err)


def main():
	print("")
	keep_price = False
	while True:
		while True and not keep_price:
			min = try_parse_int(input(" Minimum activity cost? "), "Please input a number!")
			if min == None: continue
			break
		while True and not keep_price:
			max = try_parse_int(input(" Maximum activity cost? "), "Please input a number!")
			if max == None: continue
			break
		print(f" Min: ${min}, Max: ${max}")
		
		activity = requests.get(f"http://www.boredapi.com/api/activity?minprice={min}&maxprice={max}").json()
		if "error" in activity:
			crint["red"]("", activity["error"])
			crint.reset()
			continue
		crint["lightblue_ex"](f" Activity: {activity['activity']}")
		crint["lightred_ex"](f" Type: {activity['type']}")
		crint["yellow"](f" Participants: {activity['participants']}")
		crint["lightgreen_ex"](f" Price: {activity['price']}")
		crint.reset()

		cmd = input(" Keep price range: Yes / No / Quit ? ")[0].lower()

		if cmd == "y":
			keep_price = True
		elif cmd == "n":
			keep_price = False
		elif cmd == "q":
			print(" Thanks for coming!\n")
			return

if __name__ == "__main__":
	main()
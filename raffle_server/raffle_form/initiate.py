from . import tresbien


def raffle(**data):
	
#	print("\nData type of argument:",type(data))

	for key, value in data.items():
		if key == "raffle" and value == "tresbien":
			print("Initiate tresbien.py")
			tresbien.main(tresbien=data)



"""

Test & Build:

neo > build path test 07 05 True False

"""

from boa.interop.Neo.Runtime import Log, Notify

def Main():
	
	# Print translates to a `log` call
	print("log via print (1)")
	
	# Dev Info: To print variables such as lists, objects. Use `Notify`
	Log("normal log (2)")
	Notify("notify (3)")

	# Sending multiple args as notify payload
	msg = ["a", 1, 2 ,b"3"]
	Notify(msg)


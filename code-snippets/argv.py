# argv.py
import sys

print(f"Name of the script      : {sys.argv[0]=}")

args = sys.argv[1:]
print(args) 

# all(True, True, True) -> True 
# all(False, True, True) -> False
if all(arg.isdigit() for arg in args):
	print(f"input was all digits, sum:{sum(int(arg) for arg in args)}")

if all(arg.isascii() for arg in args):
	print(f"input was all characters: { ','.join(args) }")
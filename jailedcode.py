import sys
from io import StringIO

n=int(sys.stdin.read().strip())
std_stdout = sys.stdout
sys.stdout = StringIO()

__import__('sys').exit(open('jailed_code').read())
result =sys.stdout.getvalue().strip()
sys.stdout = std_stdout
if not result:
    sys.exit(f'Кажется вы ничего не вывели')
print((n-1)*' '+result)

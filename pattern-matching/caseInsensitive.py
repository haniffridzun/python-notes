import re

# ignore uppercase or lowercase
# pass re.IGNORECASE or re.I as 2nd argument to re.compile()
robocop = re.compile(r'robocop', re.I)
robo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(robo)     # output: 'RoboCop'

#Positional formating
print('to {}. Lorem ipsum dolor sit amet, {} consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore {} magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea {} commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla {} pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim {} id est laborum.'.format('nurung', 12, 'nurung', 'nurung', 'nurung', 'hi'))

#Named placeholder
print('to {name}. Lorem ipsum dolor sit amet, {name} consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore {age:d} magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea {name} commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla {name} pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim {name} id est laborum.'.format(name='nurung', age=12))
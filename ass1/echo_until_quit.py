"""
Define a function that asks for a string and echoes it back
until the input 'quit' is provided.
Example:
    echo()
    > Insert a string: hello
    > hello
    > Insert a string: world
    > world
    > Insert a string: quit
    > bye!
"""

def echo():
    s = str(raw_input('Insert a string: '))
    while s != 'quit':
        print s
        s = str(raw_input('Insert a string: '))
    else:
        print 'bye!'

echo()

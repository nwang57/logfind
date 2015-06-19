# logfind
First project from http://projectsthehardway.com/

## Instruction
    1. I specify what files are important in a ~/.logfind file, using regular expressions.
    2. Logfind takes any number of arguments as strings to find in those files, and assumes I mean and. So looking for “zed has blue eyes” means files that have “zed AND has AND blue AND eyes” in it.
    3. I can pass in one argument, -o (dash oh) and the default is then or logic instead. In the example above -o would change it to mean “zed OR has OR blue OR eyes”.
    4. I want to be able to install logfind on my computer and run it like other projects. However, don’t push this to PyPI as that’ll really annoy people.
    5. Extra bonus points if you can let me specify regular expressions as things to find in files.
    6. Finally, speed counts, so whoever can make the fastest logfind will win the prize. The prize is nothing, but you know you want it.

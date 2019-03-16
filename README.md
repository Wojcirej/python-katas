# Python katas
My solutions of katas available on codewars.com gathered in one place - Python Edition.
[![CodeWars](https://www.codewars.com/users/Wojcirej/badges/large)](https://www.codewars.com/users/Wojcirej/badges/large "My Honor Badge")
# Set up (virtual) environment
1. Install `virtualenv`:
```bash
sudo pip3 install virtualenv
```
2. Create directory for you local, virtual python environments:
```bash
mkdir ~/.python-virtual-environments
```
3. Create new python virtual environment named `python-katas` with packages currently available in the system:
```bash
virtualenv --system-site-packages ~/.python-virtual-environments/python-katas
```
4. Activate your virtual environment
```bash
. ~/.python-virtual-environments/python-katas/bin/activate
```

# Launch tests
`behave`
# Solution generator
`python3 generator.py <kata_name> [argument names]`
### Example of solution generator usage
`python3 generator.py test_kata arg1 arg2`
will generate template for kata with `test_kata` name in `/katas/` directory.

In this case, file within `katas/test_kata/` directory named `test_kata.py` will contain template for function named `test_kata` taking two arguments: `arg1` and `arg2`.

There will be also file template for tests in `/features/` directory, named `test_kata.feature`, containing steps for testing. The implementation of said steps is going to be placed in `/featutes/steps/` directory in file `test_kata.py`.
#### Test examples
Place test examples in `/test_examples/<kata_name>.txt` in following format:
```
what, how, who
lorem, that is a long value, 3.1415
ipsum, 89798, 0.2
```
And they will be included as examples for testing purposes. The first line always contains names of params.

#### Updating test examples only
Updating this Gherkin table is boring and time consuming. So I have script for this too. I'm lazy. :) But also I have nice, reusable pieces of code - or at least I think so.
1. Update source file in `test_examples` catalog, i.e. `test_examples/test_kata.txt`
2. Run `python3 update_tests.py test_kata [argument names]`
3. Enjoy your effects!

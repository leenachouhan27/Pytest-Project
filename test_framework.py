import pytest
#fixtures: fictures are decorators which will called before actual test case execution. Generally in fixtures we put the data related to setup, so that before test case execution this fixture will call and setup will be ready to test.

@pytest.fixture() #mentioning that below func is fixture
def setup_list(): #fixture method name can be start with anything.
    city = ['indore', 'delhi', 'pune']
    return city  #fixture returning list of city


@pytest.mark.string
def test_string_pallindrom():
    name = "leela"
    assert name == name[::-1]

@pytest.mark.string
@pytest.mark.skipif(test_string_pallindrom(),reason="dependent on above")
def test_reverse():
    name = "my name is leena and i am very good girl"
    assert name[-1] == "l"

@pytest.mark.pattern
def test_start_pattern():
    for i in range(1, 4):
    #print("*", end="")
        for j in range(1,4):
            print("*", end="")
        print()

@pytest.mark.list
def test_reverse_list_value(setup_list):  #calling fixture
    #a = ['abc', 'def', 'ghi']
    b = []
    for i in range(len(setup_list)):
        b.append(setup_list[i][::-1])
    print(b)
#
#

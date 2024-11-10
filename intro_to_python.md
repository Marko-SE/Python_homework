# Homework Python for 2024_11_11
## Exercise 1 
~~~ Python 3.12.7
    # print "Hello World!" by typing it inside print() function
    print("Hello World")
~~~
~~~ Python 3.12.7
    # assign "Hello World!" to the variable my_text
    my_text="Hello World"
    print(my_text)
~~~
## Exercise 2 - Python Variable
~~~ Python 3.12.7
    #Type here. Assign a number to the variable: glass_of_water
    glass_of_water=3
    print("I drank", glass_of_water, "glasses of water today.")
~~~
~~~ Python 3.12.7
    #Fill the print function so it prints glass_of_water
    glass_of_water=3
    glass_of_water=glass_of_water + 1
    print(glass_of_water)
~~~ 
~~~ Python 3.12.7
    #Assign an integer to the variable, then print it.
    men_stepped_on_the_moon=4
    print(men_stepped_on_the_moon)
~~~
~~~ Python 3.12.7
    #Type a couple of words or a short sentence for your variable, then print it.
    my_reason_for_coding="learn a new skill"
    print(my_reason_for_coding)
~~~
~~~ Python 3.12.7
    #Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.
    global_mean_sea_level_2018=21
    global_mean_sea_level_2018=21.36
    print(global_mean_sea_level_2018)
~~~
## Exercise 9 - String
~~~ Python 3.12.7
    # Assign the string below to the variable in the exercise.
    str="It's always darkest before dawn."
    print(str)
~~~
~~~ Python 3.12.7
    # By using first, second and last characters of the string, create a new string.
    str="It's always darkest before dawn."
    ans_1="It."
    print(ans_1)
~~~
~~~ Python 3.12.7
    # Replace the (.) with (!)
    str="It's always darkest before dawn!"
    print(str)
~~~
## Exercise 10 - .len()
~~~ Python 3.12.7
    # Using len() function find out how many items are in the list.
    lst=[11, 10, 12, 101, 99, 1000, 999]
    answer_1=len(lst)
    print(answer_1)
~~~
~~~ Python 3.12.7
    #Find out the length of the string given below.
    msg="Be yourself, everyone else is taken."
    msg_length=len(msg)
    print(msg_length)
~~~
~~~ Python 3.12.7
    # How many keys are there in the dictionary?
    dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
    ans_1=len(dict)
    print(ans_1)
~~~
## Exercise 11 - .sort()
~~~ Python 3.12.7
    # Sort the list in ascending order with .sort() method.
    lst=[11, 100, 99, 1000, 999]
    lst.sort()
    print(lst)
~~~
~~~ Python 3.12.7
    # This time sort the countries in alphabetic order.
    lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
    lst.sort()
    print(lst)
~~~
~~~ Python 3.12.7
    # Now sort the list in descending order with .sort() method.
    lst=[11, 100, 101, 999, 1001]
    lst.sort(reverse = True)
    print(lst)
    # .sort() method can be used with “reverse =” parameter.
~~~
## Exercise 12 - .pop()
~~~ Python 3.12.7
    # Pop the last item of the list below.
    lst=[11, 100, 99, 1000, 999]
    popped_item=lst.pop() 
    print(popped_item)
    print(lst)
~~~
~~~ Python 3.12.7
    # Remove "broccoli" from the list using .pop and .index methods.
    lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
    a=lst.index("broccoli")
    item=lst.index(a)
    print(lst, item)
~~~
~~~ Python 3.12.7
    # Save Italy's GDP in a separate variable and remove it from the dictionary.
    GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
    italy_gdp=GDP_2018.pop("Italy")
    print(GDP_2018)
    print(italy_gdp, "trillion USD")
~~~

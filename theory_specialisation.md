# Theory: Software Specialisation 
### Q1. How does Object-Oriented Programming differ from Process Oriented Programming?
#### What is POP?
Process Oriented Programming (POP) is a programming model based on a paper called 'Communicating Sequential Processes',
written by Tony Hoare in 1977. This was also commonly called the 'actor model of concurrency'.
POP is "a programming paradigm that separates the concerns of data structures and the concurrent process that act upon them"
(DBpedia, accessed 4th August 2022: https://dbpedia.org/page/Process-oriented_programming).
These data structures are often persistent, complex, and large scale, and the subject of general purpose applications. POP
allows for the creation of large scale applications that partially share common data sets.
The programs are functionally decomposed into parallel processes that create and act upon logically shared data.
POP was originally invented in the 1980s for parallel computers. 

#### What is OOP?
Meanwhile, Object-Oriented Programming (OOP) primarily deals with the static structure of data and function.
OOP is a computer programming model that organises software design around data, or 'objects', rather 
than functions and logic 
(Tech Target, accessed 4th August 2022: https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP).
An 'object' is defined as a data field that has unique attributes and behaviour. 
Developers focus on these objects rather than the logic required to manipulate them.
Objects may be small computer programs such as widgets,
or they may represent a physical entity, such as a person or an animal. 
This approach is well-suited for programs that are large, complex and actively maintained, 
including programs for manufacturing and design. 


#### Main differences (why is OOP better than POP?)

- POP is a top-down programming paradigm, whereas OOP uses a bottom-up approach. 

- Inheritance is used in OOP, whereas it is not used in POP. This means code is reusable in OOP,
so teams don't have to write code more than once. This helps developers keep the code 'DRY'
(Don't Repeat Yourself).

- OOP uses encapsulation (modularity), whereas POP doesn't. 
This means data can be hidden in OOP, and not POP; so OOP is considered to be more secure. 

- OOP aids collaborative development; projects can be divided into smaller parts, which can
be worked on by different members of the team.

- Another benefit of using classes/objects is that adding new data and functions is easy in OOP. 
Code is easily upgradable and scalable. Developers can implement independent system functionalities.
Expanding data/functions is not as easy in POP - modifications can affect the entire program.

- OOP is also flexible - polymorphism enables a single function to adapt to the class it is in. 
The same interface can have different objects passed through it. 


### Q2. What is polymorphism in OOP?

As mentioned above, polymorphism allows OOP to be very flexible. How does it do this?

Polymorphism is one of the core concepts of OOP. 'Polymorphism' in general describes 
something that exists in several forms. It derives from Greek, where 'poly' means 'many'
and 'morphism' means 'forms'. In this context, it refers to the fact that objects 
of different types can be accessed through the same interface. Each object can do something
different with the same interface. 

##### Static polymorphism 
OOP languages like Java allow developers to implement more than one method within the same class
that uses the same name. Java uses a set of parameters called 'method overloading', which is
a form of static polymorphism. These parameters must either: have a different number of parameters,
have a different type (e.g. one accepting a <i>string</i>, and one accepting a <i>long</i>), or the parameters
must be expected in a different order. As such, overloaded methods usually
provide different, but similar, functionalities. Each method will have a different signature, which
means the compiler can identify which method it needs to call and to bind it to the method call (static binding/static polymorphism).

##### Dynamic polymorphism

Dynamic polymorphism describes a situation in which a subclass can override a method of its
superclass, enabling the developer of the subclass to customise or completely replace the behaviour
of that method - and while both methods implemented by the super- (parent) and sub- (child) classes share the same name
and parameters, they provide a different functionality
(Janssen, 2021, accesses 7th August 2022: https://stackify.com/oop-concept-polymorphism/).

##### Polymorphism in Python 
- <u>With functions and objects</u>: you can create a function that can take any object, which allows for polymorphism.
- <u>With classes</u>: Python can use two different class types in the same way. In this case, developers can use a
<i>for</i> loop that iterates through a tuple of objects. Then, methods can be called without being
concerned about which class type each object is (Edureka, accessed 7th August 2022: https://www.edureka.co/blog/polymorphism-in-python/).
- <u>With inheritance</u>: python defines methods in the child class that have the same name as the methods
in the parent class. The child class inherits methods from the parent. Developers can also modify 
a method in a child class that it has inherited from the parent class. In this context, method
overriding is the process of re-implementing a method in the child class, and is used when
the method inherited from the parent class doesn't fit the child class.

##### Example of polymorphism in Python 
An example of polymorphism in Python is the '+' operator. It can perform different operations 
based on the context - in other words, depending on how it is used. 

For instance, you can use '+' to perform sums: 

    num_x = 1
    num_y = 2
    num_z = 1 + 2
    
    print(num_z)
    
    3

You can also add text together, using strings: 

    str_x = "My name is"
    str_y = "Olivia"
    str_z = str_x + str_y

    print(str_z)
    
    My name is Olivia

If used in conjunction with the operator '=' ('+='; the 'addition assignment' operator), adds two values together and assigns the final value
to a variable:  

    a = 10
    a += 7.5
    print(a)
    
    17.5

They can be used in simple operations (like above) or in more complex functions using <i>for </i>loops.

### Q3. What is inheritance in OOP?

As described above, in OOP language such as Python, there are 'parent' classes and 'child' classes. Child classes
are made from the parent class. This concept is called 'inheritance'. 
Inheritance allows developers to define a class (child class) that inherits the properties from
another class (parent class). 

##### What is a class? 
- A class can be considered to be like a 'blueprint' for creating objects in an OOP language, such as Python.
- Classes use build-in functions. All classes use a built-in function called __init__(), which initialises
the class. This function assigns values to object properties, or other initialising operations. __init__ is called
automatically every time the class is being used to create a new object. 
- Objects also contain methods - functions which belong to that object. 
- Classes also use the 'self' parameter - a reference to the current instance, used to access variables
belonging to the class. 

##### Creating a parent class
Parent classes are not special or specific - any class can become a parent class. For example,
you could make a class to describe 'Pet'. You may describe various elements, including 'name' and 'age'.
E.g. class Pet:


    class Pet:
        def __init__(self, name, age):
                self.name = name
                self.age = age

##### Creating a child class
In this example, a child class may describe a specific type of pet, e.g. 'Dog'. You can reference
the parent class in the brackets:   

    class Dog(Pet):
        def __init__(self, name, age)
            super().__init__(name, age)

Using the 'pass' keyword, the child class will inherit all the properties and methods of the parent. 
You can also use the super function (as above). 
In both scenarios, the dog class will inherit from the pet class, and will be able to have a name and an age. 
Developers can adapt the child class - methods and properties can be added, changed or removed.

##### Advantages of Inheritance
- Inheritance aids code usability. Codes are defined only once,
and can be used multiple times. This saves developers space, time, and effort. 
- Inheritance also improves the readability of code. Code will be shorter and more concise. 
- Codes using inheritance are easier to debug - problems can be identified more easily. 
- The code will be more flexible to change. 
- Code will be better organised - it will be written into smaller, simpler compilation units. 

##### Disadvantages of Inheritance
- 'Base' and 'super' classes can be highly dependent on each other.
- If functionality of the bass class changes, then these changes must be done on the child classes as well.
- If methods in the super class are deleted, it is very difficult to maintain the functionality
of the child class which uses the super class' method.

### Q4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
Imagine there are 5 contenders to be the funniest person in the office. Each person has a number:
    James = 1
    Hannah = 2
    Sophie = 3
    Gerard = 4
    Luke = 5
Now imagine 10 people work in this office, and each of them get to vote for the person they think is the funniest. 
The program would run the following function first, to get 10 user inputs: 

    def votes():
        vote_list = []
        for funny_person in range(1, 10):
            names = input("Who do you want to vote for? Enter number 1-5: ")
            vote_list.append(names)
        print(vote_list)

Now imagine that function has returned the following:
    ['2', '2', '2', '2', '3', '3', '3', '1', '5']

Now have a vote list, we can enter this list into the following function: 
    
    def three_funniest_people(vote_list):
        c = Counter(vote_list)
        most_common = c.most_common(3)
        for a, b in most_common:
            print(a)
    
    
    vote_list = (1, 2, 5, 4, 3, 2, 1, 5, 1, 2)

That function produces the following output:
1
2
5

Which means that persons 1 (James), 2 (Hannah), and 5 (Luke) are the funniest people in the office! 



### Q5. What is the software development cycle? 

The Software Development Life Cycle (SDLC) is a widely-used process that guides developing teams so that
they can produce software with high quality and low cost, in a short timeframe. There are different
SDLC models, including 'waterfall' and 'agile' (see answer below). 

There are six phases to the SDLC: 

##### Requirement Analysis
This stage identifies current problems. This may be the very first task on a new project, but can be done throughout
the project (i.e. this process is a cycle, and is not linear). This stage may require input from
stakeholders, customers, salespeople, experts, and programmers/developers. 
##### Planning
This stage plans how the requirements, identified in the last stage, will be met. This includes what
the necessary cost and the resources are likely to be, as well as identifying any potential risks 
and ways of softening those risks. This is where the feasibility of the project will be assessed,
and the best way of implementing the project. 
##### Architectural Design
This stage will turn the requirements/specifications of the project into a design plan. This is called
the Design Specification. This plan will be reviewed by relevant people (e.g. stakeholders) and they can
offer any feedback and suggestions they have. If there are failures at this stage, it will likely
result in cost overruns or even the collapse of the project. 
##### Software Development
This is the 'build' stage, where the actual development starts. At this time, the planning has been done,
so every developer must stick to the agreed blueprint. There should be practical guidelines in place,
e.g. for code styling (such as snake_case or CamelCase).
##### Testing
This stage will see whether the code works, i.e. was the required result achieved? Are there any
defects or deficiencies? If not, the product must be fixed. 
##### Software Development
At this stage, the software is deployed into the production environment. Users will start to use
the product. Before being released to the public, products are often put through more testing 
environments, which allows stakeholders to play with the product before its general release.
Any final mistakes can be caught before general release. 

In addition, as the product continues to develop and grow, some or all of these stages will be repeated - 
hence, the software <i> cycle </i>. 

### Q6. What is the difference between agile and waterfall?

#### What is the waterfall approach? 

The waterfall approach to project management is a sequential approach that divides the SDLC to distinct phases such as requirements
gathering, analysis and design, coding and unit testing, system and user acceptance testing, and
deployment (Morris, 2022, accessed 7th August 2022: https://project-management.com/agile-vs-waterfall/).
Once one phase is completed, the next phase can begin, and so on. Inbetween, a deliverable is expected
or perhaps a document will need to be signed off. 

##### Advantages of waterfall approach
- Can track detailed schedules and track costs.
- Enables full discovery across teams, and arguably leads to better design.
- There is clear agreement from all sides on project scopes and deliverables. 
- There is less ambiguity in terms of managing effort.

#### Disadvantages of waterfall approach
- This approach has a very rigid, formal style.
- Waterfall requires extended project planning phases. Getting the 'sign off' on various aspects of the project takes time.  
- There is a large focus on perfectly formatted, often lengthy deliverables such as reports and documentation, 
and requires even more time spent (or, some might say, wasted). 
- In waterfall design, testing only occurs at the end of the project; this means less opportunity for changes to be made, 
or to gain input from stakeholders for improvements. What is thought of on paper can differ from what
people want in reality. Making changes at this stage will be costly, both for time and financially. 
lengthy and excessive timelines for implementation can hurt the orgnaisation's return on investment.

#### What is the agile approach?

In contrast, the agile approach is a team-based approach that emphasises rapid deployment of a
functional application with a focus on customer satisfaction (Morris, 2022, accessed 7th August 2022: https://project-management.com/agile-vs-waterfall/).
All teams can be developed to be agile. There is a guiding framework: 

##### Sprints 
In Agile teams, there are time-boxed phases called 'sprints' with a defined duration, usually two weeks long. 
There will be allocated tasks which need to completed in the sprint. 

##### Daily Standups
There are likely to be daily 'standup' meetings to assess progress over a 24-hour period. This
doesn't have to be daily; some teams might decide to meet less often, e.g. two or three times a week.

##### Retrospectives 
At the end of each month (or sprint, or quarter), the team can meet up for a review of the work 
that has just been completed. The team can reflect on what went well, what didn't go well, 
and how to improve. 

##### Planning sessions
These sessions can be used to map out the next phase of work. They may contain risk planning, as well
as collaborative team planning. This is in comparison to a style of project management, where team
members are simply told what to do. 

##### Embed the customer throughout 
Teams can think about the customer in every stage. Like co-design in other fields, what the intended
users think and feel is very important. Potential customers can be included in multiple stages, 
e.g. planning and retrospective sessions. 

##### Iterative reviews 
Iterative reviews keep the customer and stakeholders engaged in the development process. This helps
ensure the team knows exactly what is required and can adapt and change based on feedback.

##### Main difference between Agile and Waterfall
The main difference between agile and waterfall is in their structure. Agile is an iterative methodology 
that incorporates a cyclic and collaborative process, whereas waterfall is a sequential methodology
that can be collaborative, but generally, tasks are handled in a more linear process (Towner, 2022:
accessed 7th August 2022: https://www.forecast.app/blog/difference-between-agile-waterfall)


### Q7. What is a reduced function used for? 

Reduce() is a function used in Python. it implements a mathematical technique: 'folding', or as it is 
otherwise known, 'reduction'. Reduce is used when you need to apply a pre-defined function to an iterable, 
and reduce it to a single cumulative value (Ramos, 2020, accessed 7th August 2022: https://realpython.com/python-reduce-function/). 
Reduce() works on any iterable, not just lists - so tuples and sets, etc. Reduce uses the following steps: 
- Apply a function, or another callable, to the first two items in an iterable, and generate a partial result.
- This result, with the third item of the iterable, will generate another partial result. 
- This process gets repeated until there is no items left in the itable, and then a single cumulative 
value is returned. 

The idea is to take an existing function, apply it cumulatively to items in an iterable, and return a final value.
In Python 2.x, reduce() was an in-built function, but was moved to functools.reduce() in Python 3. 

For example: 

    from functools import reduce
    
    def product (x,y):
        return x*y
    
    ans = reduce(product, [2, 5, 3, 7])
    print(ans)
    
    24

In this instance, reduce() calculates the result of the following - (((2x5)x3)x7). It multiplies
2 and 5 (first two items in iterable) and goes through the rest of items, multiplying them (3, then 7).

### Q8. How does merge sort work? 

Merge Sort is a common sorting algorithm. It can be used to sort the values in an iterable,
such as a list. It is described as a 'divide-and-conquer' strategy. It divides the unsorted list in halves into sublists,
and combines them in a sorted manner. It can be thought of as a recursive algorithm that continuously
splits the array in half until it cannot be further divided; this means that the dividing stops when the array becomes empty
or has only one element left (GeeksforGeeks, accessed 7th August 2022: https://www.geeksforgeeks.org/merge-sort/).
If the array has multiple elements, the array gets split into halves and then the merge sort is
carried out on both halves. When both halves are sorted, the merge operation is applied - the process
of taking two smaller sorted arrays and combining them to make a larger one. 

Below is an example of a merge sort in Python: 

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

### Q9. Generators - generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?

##### What is a generator? 
There are two main ways to iterate in Python. One is to build an iterator, a process which is lengthy
and potentially counterintuitive. To do this, you implement a class with __iter__() and __next__() methods,
and raise StopIteration when you want the iterating to stop. 

Meanwhile, Python generators are more simple and arguably straight-forward. Generators are functions
that return an object (iterator) which we can iterate over, one value at a time (Programiz, accessed
7th August 2022: https://www.programiz.com/python-programming/generator). Generators differ from
normal functions, in that they use the 'yield' statement instead of the 'return' statement. 
If a function contains at least one 'yield' statement, it becomes a generator function,
regardless of whether it also has a 'return' statement.
When it is called, the generator will return an object (iterator) but won't begin immediately - 
you iterate through the object using next(). Local variables will be remembered between calls of the generator
function. When the function ends, StopIteration is raised automatically. 

##### When and why should you use generators, (i.e. what is the use case)?

- <u>To achieve lazy evaluation</u>: generators are referred to as giving 'lazy evaluation', because they don't
compute the value of each item when being instantiated - instead, they compute only when asked. Thus, 
generators allow us to process and deal with one value at a time without having to load everything
in memory first. 
- <u>When you have a large dataset</u>: reading from a large dataset means the computer or sever has to allocate
memory for it. For example, if the function needs to read from a large .csv file, it is likely
to be very slow, or perhaps a memory error would be raised. Instead, you could use a generator
to loop through each line, and return it one at a time, instead of trying to return the entire file. It is
a lot less likely to run slowly or produce memory errors.
- <u>When iterating through a large list</u>: again, iterating a large list may result in slowness or
memory errors. Like list comprehensions, the <i>generator expression</i> allows the writer to create
a generator object quickly, without the yield statement. Instead of an entire range being iterated through,
in this instance, the expression will only be evaluated when iterated, and this requires using 
a lot less memory.


### Q10. Decorators - a page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?

##### What is a decorator? 
A decorator is a function that takes another function as its argument, and returns another function (Fordham,
2020, accessed 7th August 2022: https://towardsdatascience.com/how-to-use-decorators-in-python-by-example-b398328163b).
Decorators add functionality to existing code. This is also called 'metaprogramming'. The function
being used as a decorator can be called above the second function, using '@' (see below). 


##### Example of a decorator
Imagine you want to ask a user questions in an eye-catchy format, and you decide you want to frame
questions in stars. You can make a function, here called "get_stars". You can then call this star function
whenever you ask a question. 

    def make_stars(func):
        def inner(*args, **kwargs):
            print("*" * 30)
            func(*args, **kwargs)
            print("*" * 30)
        return inner
    
    
    @make_stars
    def your_name():
        answer = input("What is your name?")
        return answer

    ******************************
    What is your name? Olivia
    ******************************

##### Advantages of decorators

- Extends the behaviour of the latter function (the non-decorator function) without explicitly 
modifying it. 
- A Python decorator can make code shorter.
- It can make coding easier - if/when you fully grasp the concept! 
- Decorators make it easier to reuse code. 
- You can use decorators for analytics, logging, and instrumentation - you can measure what
is happening and record metrics. 
- Decorators can be used to perform validation and run-time checks. 
- You can extend and expand the language structure of Python. E.g. Flask uses decorators 
"to course URLs to capacities that handle the HTTP demand" (Radečić, 2020, accessed
7th August 2022: https://towardsdatascience.com/5-minute-guide-to-decorators-in-python-b5ca0f2c7ce7).

##### Disadvantages of decorators 
- The concept of decorators is not easy to understand. It can be difficult to write your own
decorators until you fully understand the concept. 
- Decorators may mutate your function
- When a function is decorated, the docstring of the original function may become inaccessible.
- If using a decorator you haven't written yourself, ensure there are no safety/data concerns.
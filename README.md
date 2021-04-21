# Py_ATM-Machine

## Table of Contents
<ol>
	<li>ATM Function Requirements</li>
	<li>
		Import Python Random Module
		<ul>
			<li>What does the random module/package do in Python?</li>
		</ul>
	</li>
	<li>Create Class and Define Functions
		<ul>
			<li>What is a class?</li>
			<li>How to define a function?</li>
		</ul>
	</li>
	<li>Define the main() Function</li>
	<li>ATM Process Creation Using while True</li>
</ol>

### ATM function requirements
The first step is to brainstorm what basic transactions are completed at an ATM?<br>
Some of the function that one can complete at an ATM are given below:<br>
<ul>
	<li>Input user pin for authentication</li>
	<li>Check account balance</li>
	<li>Deposit funds</li>
	<li>Withdraw funds</li>
	<li>Create random generated transaction id</li>
	<li>Account interest rate and Monthly accused interest rate</li>
</ul>

### Import python random module
<b>Ques. What does the random module/package do in Python?</b><br>
Ans. The random module allows a program to create random numbers by using the <b>random.randint()</b> function.<br>
-----------------------<code><b>import random</b></code>-----------------------

### Create Class and Define function
<b>Ques. What is a Class?</b><br>
Ans. A class is used for creating objects. By creating objects, the objects have variables and a behavior that's associated with them. 
A class is created with the keyword <b>class</b>. Once the class is created, the object within the class will then be called the instance of the class.<br>

<b>Ques. How to define a function?</b><br>
Ans. Now we take the requirements that we created from the above and create functions. We can define the functions to provide the given functionality of the program. 
The function blocks are started with <b>def</b> keywords and followed with the function name and parenthesis, such as <b>def getId(self)</b>.<br>


### Define the main() function
We must create the main() function because it’s only executed when the Python program is executed. Also, we could import a Python program as a module, 
but the main() method will not execute. The entry point of any program is the main() function, but the interpreter of python will execute the source file code sequentially. 
In addition, it will not call any method if it’s not within the code. This is why the main() method has a technique, 
so that the main() method will be executed when the program is executed directly and not when the module is imported.<br>

By creating the main() method, we will use a range to have all users to enter a 4-digit pin to access their account.

### ATM Process Creation Using while True
We will use the while True loop because it will loop forever. 
The while statement will take an expression and execute the body of the loop while the expression is equal to ‘boolean’ of True.
As long as the loop stays True, the loop will indefinitely loop.

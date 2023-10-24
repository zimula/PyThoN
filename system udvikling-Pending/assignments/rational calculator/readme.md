1. create a **simple** calculator that uses **floats**. 

**done***********************

2. create the **same** calculator using **command pattern**
    **CODE CAN WORK WITHOUT INTERFACE DUE TO PYTHON'S FLEXIBILITY (PATTERN IS OVERKILL IN THIS CONTEXT)**
    - a base class as the interface with an execute method with no body.
    - concrete classes (add, subtract, multiply and divide) implement the interface. Consider interface methods as place holders.
    - an invoker: a class with commands as intance attributes
    - a method to set command
    - a method to use command methods. 
    - commands refer to concrete classes.
    - later I will try to separate the code into modules. 
    *************done**********************************

3. modify second version to take and return fractions
    - requires fractions library

4. might add **GUI**
    - started
    - use try and except to surpress graphical error from getmouse() when win is closed.
    - must switch to **tkinter.** **graphics.py** is painful. 
    ************************done******************************** 

5. Rebuild in **html and js**
    - use selenium to run tests on site.
    - see it works with a local page.  
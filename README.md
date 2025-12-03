BycLogger: A Digital Logger for Community Use 


Members:

Balasbas, Austin Zedrick C.
Catapang, Dirk Andrei L.
Fondavilla, Janwen Topher A.


Description/ Overview

  This is a program that allows the students to rent or use the stocked bikes in the gymnasium where it can be rented or borrowed for a specific time based on how much they pay using their chipcode in ids which can be also used for identification. This also promotes the health and well being of the bsu students while using the input and storing the data using java.


Oop Concepts	

  In developing the BycLogger: A Digital Logger for Community Use, the team utilized the four primary principles of Object-Oriented Programming: abstraction, encapsulation, inheritance, and polymorphism. These concepts contributed to making the program more structured, easier to handle, and more straightforward to enhance in the future.

  In developing this program, abstraction was made by creating an abstract class, Rental. It provides the basic information that is needed from every bike rental, like the student ID, number of hours, and minutes used. It also has an abstract method calculatePayment(), which requires each bike type to provide its own way of computing the rental fee. Through abstraction, only the important details are visible in the program, while it conceals more complex parts of the process.

  In that respect, the Rental class demonstrates a good concept of encapsulation. All significant fields in it are private, so direct changes to them are impossible. The program instead uses getter and setter methods, which let it get a safe access or safely change these values. Such design prevents any accidental modification of important data and ensures that every value is previously validated before being used.

  Inheritance can be seen when the various types of bikes extend their parent class, Rental. The classes BikeRental, ElectricBikeRental, and MountainBikeRental inherit the attributes and methods of the parent class. Due to this, the program is not forced to repeat the same code for every bike type. Also, it becomes easier to add new kinds of rentals in the future by just creating another class which extends the Rental.

  This is demonstrated by polymorphism through method overriding of the calculatePayment() method in each subclass. Even though they have the same method name, each different bike type calculates its rental fee based on its own rate. Upon execution, this method immediately selects the appropriate version to invoke based on the object that has been instantiated. In this way, the system can have different behaviors according to the selected bike, without using complicated conditions.

  Generally speaking, applying the principles of OOP helped the project stay clean, organized, and expandable. These techniques not only made the code more readable but also ensured that adding future features requires less effort.




Program Structure
      
  The design follows OOP principles such as abstraction, encapsulation, inheritance, and polymorphism. The program allows students to rent different types of bikes, calculates rental fees, and stores each transaction
       
  The BycLogger system is organized using a modular, object-oriented architecture that separates responsibilities across multiple classes. The program is composed of one abstract superclass, three concrete subclasses, and a main system class responsible for user interaction and program execution. This structure ensures clarity, maintainability, and adherence to core OOP principles.
          
Rental (Abstraction)
  The Rental class serves as the foundational structure for all bike-rental types.
  It encapsulates shared attributes such as:
  studentID, hours, minutes, totalPayment, amountPaid and change

  It also defines the abstract method calculatePayment(), which enforces that each subclass provides its own implementation based on its rate. This class further includes accessor (getter) and mutator (setter) methods, ensuring controlled access to internal data and maintaining encapsulation.
Subclasses (BikeRental, ElectricBikeRental, MountainBikeRental)
Each subclass inherits the properties of Rental while implementing its own rental-rate computation. These classes represent three different bike categories:

BikeRental – 20 pesos per hour
ElectricBikeRental – 40 pesos per hour
MountainBikeRental – 30 pesos per hour

Through method overriding of calculatePayment(), these subclasses implement polymorphic behavior, enabling the system to compute payments dynamically depending on the bike type selected by the user.


missubibi (Main System Class)
  The missubibi class acts as the operational core of the program. It manages:
    System menus and user navigation

  Input validation for numeric entries

  Rental object creation based on user-selected bike type

  Storage and display of rental records

  Execution control through loops and condition handling


   It maintains an array of Rental objects to keep track of all completed transactions, demonstrating how arrays can be used to store multiple object instances.

 Logical Flow of the Program
Initialization
 The system starts by preparing a scanner for input and initializing an array to store up to 100 rental transactions.


Main Menu Execution
 A loop continuously displays the menu, allowing the user to choose between renting a bike, viewing stored records, or exiting the system.


Bike Rental Process


The system prompts for student ID and rental duration.


The user selects a bike type, which determines the subclass to instantiate.


The chosen subclass computes the total payment through the overridden calculatePayment() method.


Payment handling ensures proper validation and change computation.


The transaction is stored in the rentals array.


Viewing Rental Records
 The system prints a formatted list of all completed rentals by invoking the toString() method inherited from the superclass.


Termination
 Choosing the exit option stops the loop and ends the program.


  












Guidelines for run\debug

To run the program properly, you must first ensure that your computer has a C++ compiler installed, such as MinGW for Windows or the built-in g++ compiler for Linux and macOS. Once your compiler or IDE is ready, you can follow several simple steps to execute the project.
 

1. Begin by opening the project folder in your preferred environment, such as Visual Studio Code, Dev-C++, or CodeBlocks, making sure that all .cpp files belonging to the project are located in the same directory. 
2. Next, open the main source file of the program so you can verify that the code is complete and ready to run. 
3. If you are using an IDE like Dev-C++ or CodeBlocks, you can compile and run the project automatically by pressing F9 or selecting the Build & Run option, which will compile all necessary files and open the output window for you.
4. If you prefer Visual Studio Code or the command line, you will need to manually compile the program. Open a terminal inside the project folder and type the command g++ *.cpp -o program. This instructs the compiler to combine all .cpp files into a single executable named “program.” 
5. Once the compilation finishes successfully, you can run the program by typing ./program on macOS or Linux, or program.exe if you are using Windows. Completing these steps will launch the application, allowing you to interact with all its features and test its functionality as intended.














Sample Output













Author and Acknowledgement

	
This project was created by  Balasbas, Austin Zedrick C., Catapang, Dirk Andrei L., and  Janwen Topher Fondavila  as part of the requirements for the Object-Oriented Programming (OOP) course. All code, documentation, and design decisions were made by the author unless otherwise stated.
We would like to express  our  gratitude to the following:
Our OOP Instructor, Mam.Christiana Grace Alib for providing the project guidelines, feedback, and support throughout the development of this program.


My classmates and peers, for the discussions and ideas that helped me refine and      improve the project.


Online programming resources and documentation, which served as references in solving errors and implementing OOP concepts effectively.


Their guidance and contributions were helpful and had a big importance in completing this project.










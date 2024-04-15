# find_route
Work by : 1002062733 Jayadev Mandava  


Code Structure : (PYTHON)  Pre-Requisite : Python 3 installed on the PC.
The assignment implementation has Just one Class and 5 functions following it .
The first class MAP : defines a graph which the program will later generate . Inside the Class we have one function to initialize it and one to generate an edge for the graph using the input and program flow/conditions.

Def input_reader : It is a function to generate the full graph . It uses inbuilt python feature of strip to breakdown the data in the input file into useful data such as origin city ,destination city and distance between them and add them to the graph.

Def heuristic_reader : In a similar fashion to the input_reader, this function helps to process the data from the heuristic file  into a heuristic dictionary with cities and corresponding heuristic values.

Def find_route : This function decides which type of search to run based on the addition of the absence/presence of heuristic file in the command line and returns the respective search results in required format.

Def uniformed_search : We define and declare three counters for nodes popped expanded and generated. Use a queue for maintaining priority. Using a while loop every visited node (regardless of being visited before) is popped , until the first if loop which checks if current city is destination city.Every pop by character of heap pops the smallest cost city from the heap. If not check current city is in set visited and adds it if not. Furthering it expands the current city and pops it while incrementing the expanded city counter . All generated neighbors for the current city and push it into the heap queue . Generated counter increments for all its neighbors generated. Upon finding the destination city the function returns the count variables and path title there to find_route. If and When queue terminates it decides that no path exists and returns none to the find_route.

Def informed_search : It is similar to the uniformed search but in the queue there is an additional tuple to hold heuristic value . With every iteration , a small change of heuristic+actual cost is added . It takes into consideration the heuristic value . Upon finding the destination city the function returns the count variables and path title there to find_route. If and When queue terminates it decides that no path exists and returns none to the find_route.

The code section that follows if it is the main, it reads the command line, it passed the input and heuristic files as argument for find_route. Following it, it checks word count of command line to verify if it is informed or uniformed search or if its illegal with the expected command line format. 
It proceeds to print the counts for nodes popped , expanded and generated and the path & distance given a path exists. 
If not it proceeds to print none for the path ,distance as infinity and zero for all the other variables.


Instructions for execution : 
Download the python file.
The commands need to be prefixed with python3 always.
The input file and heuristic file should be added into one folder along with the pyhton file .( I have attached an input file and a hueristic file in the repository that you can use.
The program is now ready for execution.
Now in terminal  run the following commands.

Command for running uniformed search :  
" python3 find_route.py input_filename London Kassel " 
Note : Make sure to replace “input_filename” with the exact name of the input file added to the folder including the extension.  
Ex : In provided example with the requirements :  
"python3 find_route.py input1.txt London Kassel " Is the command for filename input1.txt. 
Command for running informed search : 
"python3 find_route.py iinput_filename London Kassel heuristic_filename "
Note : Make sure to replace “heuristic_filename” with the exact name of the input file added to the folder including the extension and “input_filename” with the exact name of the input file added to the folder including the extension.  
Ex : In provided example with the requirements : 
" python3 find_route.py input1.txt London Kassel h_kassel.txt" Is the command for heuristic filename h_kassel.txt and input filename input1.txt.
12. The program will generate the output in the suggested format.


 

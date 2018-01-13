#include <iostream>
int i;
int main(int argumentcount,  char **arguments){
	for(i=1; i<5; i++)
	{
		std::cout << arguments[i] <<"\n";
	}

	for (i=5; i<argumentcount; i++)
	{	
		std::cerr << arguments[i] <<"\n";
	}
	
	return 0;
}
#include <iostream>

int i;
// Copyright year Simin Zhai siminz@bu.edu

int ot=0;

int main(int argumentcount,  char **arguments) {
	if (argumentcount > 5)
	{
		ot = 5;
	}	
	else
	{
		ot = argumentcount;
	}

	for (i=1; i < ot; i++)
	{
		std::cout << arguments[i] <<"\n";
	}
	for (i=5; i < argumentcount; i++)
	{	
		std::cerr << arguments[i] <<"\n";
	}
	
	return 0;
}

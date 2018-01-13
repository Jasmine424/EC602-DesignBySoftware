//Copyright 2017 Simin Zhai siminz@bu.edu
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	double weight_earth = 5.972e27;
	double pandn = weight_earth*6.022e23;
	double elec1 = 0.5;
	double elec2 = 0.4;
	double elec3 = 1;

	double a = pandn*elec1;
	double b = pandn*elec2;
	double c = pandn*elec3;

	double ETB = a / pow(2,43);
	double LTB = b / pow(2,43);
	double UTB = c / pow(2,43);

	cout << ETB << endl;
	cout << LTB << endl;
	cout << UTB << endl;
}

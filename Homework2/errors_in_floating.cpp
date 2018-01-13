#include <iostream>
#include <iomanip>
#include <cassert>

using namespace std;


int main()
{
	float num_f = 1.0/3;
	double num_d = 1.0/3;

	long double num_ld = 1;
	num_ld /= 3;

	long double num_ld2 = (long double)1.0 /3;

	long double num_ld3 = 1.0 /3;

   cout << setprecision(22) << num_f << endl;
   cout << setprecision(22) << num_d << endl;
   cout << setprecision(22) << num_ld << endl;


   cout << num_d - num_f << endl;

   cout << num_ld - num_d << endl;

   cout << num_ld - num_ld2 << endl;

   cout << num_ld - num_ld3 << endl;

   cout << (long double) 1.0 - ((long double) num_f) * 3 << endl;
   cout << (long double) 1.0 - (num_f * 3) << endl;

}
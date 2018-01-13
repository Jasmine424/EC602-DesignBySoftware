#include <iostream>
using namespace std;

int main()
{
	double one_third,zeroish;

   one_third = 1.0/3;

   for (int i=1;i<100;i++)
   {
      zeroish = 1.0 - 3.0 * (i * one_third)/ i;
      if (zeroish != 0)
         cout << i << " " << zeroish << endl;
   }  
   
   return 0;
}
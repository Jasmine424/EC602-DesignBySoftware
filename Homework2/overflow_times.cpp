//Copyright 2017 Simin Zhai siminz@bu.edu

#include <iostream>
#include <ctime>
#include <cstdint> 
#include <math.h>

using namespace std;
// int64_t 
// int32_t
//int16_t;
//int8_t;
// uint64_t
// uint32_t
// uint16_t
//uint8_t;
//uint16_t;

int main()
{
	clock_t start_clock,end_clock;
	
	int16_t i = 1;
	start_clock = clock();
	while ( i>0) 
	{
		 i++;
		 //cout<<i<<endl;
	}
	// while ( i < pow(2,sizeof(uint16_t))) 
	// {
	// 	 i++;
	// }

	end_clock = clock();    // Timing stops here
	

	double seconds = (double)(end_clock-start_clock)* 1000000/ CLOCKS_PER_SEC;
    // std::cout << "measured int16 time (microseconds): "
    //         << 0 << std::endl;
    double seconds1= 1000*seconds/pow(2,8);
    double seconds2= seconds*pow(2,16)/1000000;
    double seconds3= seconds*pow(2,48)/1000000/(3600*24*365);

  	 std::cout << "estimated int8 time (nanoseconds): "<< seconds1 << std::endl;
  	 std::cout << "measured int16 time (microseconds): "<< seconds << std::endl;
  	 std::cout << "estimated int32 time (seconds): "<< seconds2<< std::endl;
  	 std::cout << "estimated int64 time (years): "<< seconds3 << std::endl;
  	 return 0;
}
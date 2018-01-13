//Copyright 2017 Simin Zhai siminz@bu.edu


#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>
#include <climits>
#include <iomanip>

int main(){
  
  double Rs16,Ri16,Rm16;

  Rm16 = (pow(2,15)*(2-pow(2,-10)))/ INT16_MAX;

  Rs16 = 1/pow(2,-14);

  Ri16 = INT16_MAX/pow(2,11);

  double Rs32,Ri32,Rm32;

  Rm32 = FLT_MAX/INT32_MAX;

  Rs32 = 1/FLT_MIN;

  Ri32= INT32_MAX/pow(2,24);

  double Rs64,Rm64,Ri64;

  Rm64 =(pow(2,1023)*(1+(1-pow(2,-52))))/INT64_MAX;

  Rs64 = 1/pow(2,-1022);
  
  Ri64 = INT64_MAX/pow(2,53);
 
  std::cout<< "16 : Ri= " << Ri16 << " Rm= " << Rm16<< " Rs= " << Rs16 << std::endl;
 
  std::cout<< "32 : Ri= " << Ri32 << " Rm= " << Rm32<< " Rs= " << Rs32 << std::endl;

  std::cout<< "64 : Ri= " << Ri64 << " Rm= " << Rm64<< " Rs= " << Rs64 << std::endl;
  return 0;
}

// int main(){


//   double Rs,Ri,Rm;

//   Rs=Ri=Rm=0;//remove this line




// using namespace std;
// float smallest32(){
// 	float a=1;
// 	while(a>0&&a/2!=0){
// 		a=a/2;
// 	}
// 	return a; 
//  }
// double smallest64(){
// 	double a=1;
// 	while(a>0&&a/2!=0){
// 		a=a/2;
// 	}
// 	return a; 
//  }
// // int main() {

// //  float smest = smallest();

// //  cout<<smest<<endl;
// //  cout<<INT_MAX<<endl;
// //  cout<<DBL_MAX<<endl;
// //  cout<<FLT_MAX<<endl;
// //  return 0; 
// // }

// //   std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

// //   // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
// // // Rm = maximum_float_value / largest_int_value

// // Ri2=
// int main() {
// float Rm32= FLT_MAX/LONG_MAX;
// float smest32 = smallest32();
// float Rs32=1/ smest32;
//   // std::cout<< "32 : Ri= " << Ri2 << " Rm= " << Rm2 << " Rs= " << Rs3 << std::endl;
//   std::cout<<"32 :  Rm= " << Rm32 << " Rs= " << Rs32 << std::endl;

//  double Rm64=DBL_MAX/LLONG_MAX;
//  double smest64 = smallest64();
//  double Rs64= 1/smest64;
//   std::cout<< "64 :  Rm= " << Rm64 << " Rs= " << Rs64 << std::endl;
// }
// //   // calculate Rs, Ri, and Rm for double/binary64 vs int64_t

// //   std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;


// //   return 0;
// // }
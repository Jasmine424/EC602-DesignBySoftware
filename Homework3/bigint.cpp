// Copyright 2017 Simin Zhai siminz@bu.edu

//#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<double> Poly;
typedef string BigInt;


// // Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)
{
	int i; 
	Poly c;
	if(a.size()>b.size())
	{
		for( i=0;i<b.size();i++)
		{
		 	c.push_back(a[i]+b[i]);
		}
		while (i<a.size())
		{
			c.push_back(a[i]);
			i++;
		}
	}
	else
	{
		for( i=0;i<a.size();i++)
		{
		 	c.push_back(a[i]+b[i]);
		 }
		 	while (i<b.size())
		{
		
			c.push_back(b[i]);
			i++;
		}

		
	}
	int w=c.size()-1;
	while(w>0)
		{
			if(c[w]==0)
			{
				c.erase(c.begin() + w);
				w--;
			} 
			else break;
	    } 

	return c;
}

Poly multiply_poly(const Poly &a,const Poly &b)
{
	int i, j;

  Poly c(a.size() + b.size() - 1, 0);
  if(a.size() < b.size())
   {
    for(i = 0; i < a.size(); i++)
      for(j = 0; j < b.size(); j++)
      {
      	c[i + j] = c[i + j] + a[i] * b[j];
      }
        
   } 
  else 
  {
    for(i = 0; i < b.size(); i++)
      for(j = 0; j < a.size(); j++)
      {
      	c[i + j] = c[i + j] + b[i] * a[j];
      }
        
  }

	int w=c.size()-1;
	while(w>0)
	{
		if(c[w]==0)
		{
			c.erase(c.begin() + w);
			w--;	
		}
		 else break;
	} 
	return c;
}

BigInt multiply_int(const BigInt &a, const BigInt &b)
{
	Poly aa, bb, cc;
	BigInt c;
	for (int i = a.size()-1; i >=0; i--)
	{
		aa.push_back(double (int(a[i])-48));
	}
	for (int i = b.size()-1; i >=0; i--)
	{
		bb.push_back(double(int(b[i]) - 48));
	}
	// int flt=0;
	// while(flt<aa.size())
	// {
	// 	cout<<aa[flt]<<endl;
	// 	flt++;
	// }
	// cout<<endl;
	// flt=0;
	// while(flt<bb.size())
	// {
	// 	cout<<bb[flt]<<endl;
	// 	flt++;
	// }
	cc = multiply_poly(aa, bb);
	// flt=0;
	// cout<<endl;
	// while(flt<cc.size())
	// {
	// 	cout<<cc[flt]<<endl;
	// 	flt++;
	// }
	int index=0;
	while(index<cc.size())
	{
		if(cc[index]>=10)
		{
			if( index<(cc.size()-1) )
			{
				cc[index+1] +=int(cc[index]/10);
				cc[index]=int(cc[index])%10;
			}
			else
			{
				cc.push_back(int(cc[index]/10));
				cc[index]=int(cc[index])%10;
			}
		}
		index++;
	}
	for (int i = cc.size()-1; i >=0; i--)
	{
		c.append(1,char(int(cc[i])+48));
	}
	return c;
}
//Try

// int main()
// {
//   BigInt a="999",b="1001",c;
//   c=multiply_int(a,b);
//   cout<<c<<endl;
//   return 0;
// }
  // int main()
  // poly (x, y, z);

  // z = add(x, y);
  // c.at[i];m,.

// // Multiply two polynomials, returning the result.
// Poly multiply_poly(const Poly &a,const Poly &b);
/*
int main(){
  std::vector<double> v(3, 0);
  v.push_back();
  v.push_back();

  res.at(0) = vect1.at(0) + vect2.at(0);
  res.at(1) = vect1.at(1) + vect2.at(1);
*/

//  for (int i = 0; i < v.size(); i++)
//    std::cout <<  v[i] << " ";
//  std::cout << std::endl;

//  for (double e : v)
//    std::cout << e << " ";
//  std::cout << std::endl;
 
//  //e = 5;
//  for (double &e : v)
//    e = 1;

//  // for (auto &e : v)
//  //  e = 9;
// }


























// #include <iostream>
// #include <vector>
// #include <string>

// using namespace std;


// typedef string BigInt;
// BigInt multiply_int(const BigInt &a,const BigInt &b);

// char &at(int n);

// Poly multiply_poly(const Poly &a,const Poly &b)
// {
// 	Poly c;
// 	for(int i=0;i<a.size()+b.size()-1;i++)
// 	{
// 		double sum=0;
// 		for(int j=0; j<=i;j++)
// 		{
// 			for(int k=0; k<=i; k++)
// 			{
// 				if(j+k==i)
// 				{
// 					sum +=(a[j]*b[k]);
// 				}
// 			}
// 		}
// 		c.push_back(sum);
		
// 	}
// 	return c;
// }
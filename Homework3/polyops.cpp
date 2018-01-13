// Copyright 2017 Simin Zhai siminz@bu.edu

//#include <iostream>
#include <vector>

using namespace std;

typedef vector<double> Poly;


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
	// Poly c;
	// for(int i=0;i<a.size()+b.size()-1;i++)
	// {
	// 	double sum=0;
	// 	for(int j=0; j<=i;j++)
	// 	{
	// 		for(int k=0; k<=i; k++)
	// 		{
	// 			if(j+k==i)
	// 			{
	// 				sum +=(a[j]*b[k]);
	// 			}
	// 		}
	// 	}
	// 	c.push_back(sum);
		
	//}
	int i, j;

  Poly c(a.size() + b.size() - 1, 0);
  if(a.size() < b.size())
   {
    for(i = 0; i < a.size(); i++)
      for(j = 0; j < b.size(); j++)
        c[i + j] = c[i + j] + a[i] * b[j];
   } 
  else 
  {
    for(i = 0; i < b.size(); i++)
      for(j = 0; j < a.size(); j++)
        c[i + j] = c[i + j] + b[i] * a[j];
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


// int main()
// {
// 	Poly a,b,c;
// 	double aa[5]={1,2,3,4,5},bb[4]={1,2,3,4};
// 	for(int i=0;i<5;i++)
// 	{
// 		a.push_back(aa[i]);
// 	}
// 	for(int i=0;i<4;i++)
// 	{
// 		b.push_back(bb[i]);
// 	}
// 	c=add_poly(a,b);
// 	for(int i=0;i<c.size();i++)
// 	{
// 		cout<<c[i]<<endl;
// 	}
// 	return 0;
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

// 	for (int i = 0; i < v.size(); i++)
// 		std::cout <<  v[i] << " ";
// 	std::cout << std::endl;

// 	for (double e : v)
// 		std::cout << e << " ";
// 	std::cout << std::endl;
 
// 	//e = 5;
// 	for (double &e : v)
// 		e = 1;

// 	// for (auto &e : v)
// 	// 	e = 9;
// }
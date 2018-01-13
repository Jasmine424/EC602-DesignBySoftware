#include <iostream>
int main(int argumentcount, char **arguments){
	char a;
	std::cout << "there are " << argumentcount <<"args\n";
	a = arguments[0][0];
	std::cout << a << '\n';
	std::cout <<arguments[0] << '\n';
	return 0;
}

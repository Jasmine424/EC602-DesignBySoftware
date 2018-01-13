//Copyright 2017 Simin Zhai siminz@bu.edu
//Copyright  2017 Zulin Liu liuzulin@bu.edu
//Copyright 2017 Jafallac jafallac@bu.edu


#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <regex>
#include <cmath>
#include <math.h>
#include <iomanip>

using namespace std;

struct Ball {
	string name;
	double xin, yin;
	double vxin, vyin;
};

struct coll_ball{
	double time;
	int idx;
	int idy;
};

std::vector<double> timel;
vector<Ball> balls;

void printout(){
	for (int i = 0; i < balls.size(); i++){
		cout << balls[i].name << " "  << balls[i].xin << " " << balls[i].yin << " " << balls[i].vxin << " " << balls[i].vyin << endl;
	}
}

double round(double number, unsigned int bits) {
	stringstream ss;
	ss << fixed << setprecision(bits) << number;
	ss >> number;
	return number;
}

double distance(double x1, double y1, double x2, double y2){
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}

void swap_v(int i, int j){
	double delta_x = balls[i].xin - balls[j].xin;
	double delta_y = balls[i].yin - balls[j].yin;
	double delta_vx = balls[i].vxin - balls[j].vxin;
	double delta_vy = balls[i].vyin - balls[j].vyin;
	double dot = (delta_x*delta_vx + delta_y*delta_vy) / (delta_x*delta_x + delta_y*delta_y);
	balls[i].vxin = balls[i].vxin - dot*delta_x;
	balls[i].vyin = balls[i].vyin - dot*delta_y;
	balls[j].vxin = balls[j].vxin + dot*delta_x;
	balls[j].vyin = balls[j].vyin + dot*delta_y;
}

int detect_state(int length){
	for (int i = 0; i < (balls.size()-1); i++){
		for (int j = i + 1; j < balls.size(); j++){
			if (distance(balls[i].xin + balls[i].vxin * 0.000000001, balls[i].yin + balls[i].vyin * 0.000000001, balls[j].xin + balls[j].vxin * 0.000000001, balls[j].yin + balls[j].vyin * 0.000000001) < 10){
				swap_v(i, j);
				break;
			}
		}
	}
	length -= 1;
	if (length < 0) return 0;
	else return detect_state(length - 1);
}


// Ascending sort function for time
bool wayToSort(double i, double j) { return i < j; }

bool regexmatch(string s){
    regex e ("[-+]?([0-9]*\\.[0-9]+|[0-9]+)");
    if (regex_match (s,e))
        return true;
    return false;
}

bool regexmatch2(string s){
    regex e ("[+]?([0-9]*\\.[0-9]+|[0-9]+)");
    if (regex_match (s,e))
        return true;
    return false;
}

double collidetime(int i, int j){
	double tt = 0;
	double a = (balls[i].vxin - balls[j].vxin)*(balls[i].vxin - balls[j].vxin) + (balls[i].vyin - balls[j].vyin)*(balls[i].vyin - balls[j].vyin);
	if (a ==0.0)return 9999;
	double b = 2 * (balls[i].xin - balls[j].xin)*(balls[i].vxin - balls[j].vxin) + 2 * (balls[i].yin - balls[j].yin)*(balls[i].vyin - balls[j].vyin);
	double c = (balls[i].xin - balls[j].xin)*(balls[i].xin - balls[j].xin) + (balls[i].yin - balls[j].yin)*(balls[i].yin - balls[j].yin) - 100;
	if ((b*b - 4 * a*c) >= 0){
		double delta = sqrt(b*b - 4 * a*c);
		if ((-b - delta) / (2 * a) >= 0){
			tt = (-b - delta) / (2 * a);
		}
		else if ((-b + delta) / (2 * a) >= 0){
			tt = (-b + delta) / (2 * a);
		}
	}
	if (tt > 0.00000000000001) return round(tt, 10);
	//if (tt > 0.00000000000001) return tt;
	else return 9999;
}

int collisioncase(int time_index)
{
	vector<coll_ball> coll;
	vector<coll_ball> colli;
	double tmin = timel[time_index];
	for (int i = 0; i < (balls.size()-1); i++){
		for (int j = i + 1; j < balls.size(); j++){
			double t0 = collidetime(i, j);
			if (t0 <= tmin){
				tmin = t0;
				coll_ball co;
				co.time = t0;
				co.idx = i;
				co.idy = j;
				coll.push_back(co);
			}
		}
	}
	for (int i = 0; i < coll.size(); i++){
		if (coll[i].time <= tmin){
			colli.push_back(coll[i]);
		}
	}
	if (tmin >= timel[time_index]){
		for (int i = 0; i < balls.size(); i++){
			balls[i].xin += balls[i].vxin*timel[time_index];
			balls[i].yin += balls[i].vyin*timel[time_index];
		}
		printout();
	}
	else{
		for (int i = 0; i < balls.size(); i++){
			balls[i].xin += balls[i].vxin*tmin;
			balls[i].yin += balls[i].vyin*tmin;
		}
		if (colli.size() > 1){
			for (int i = 0; i < colli.size(); i++){
				swap_v(colli[i].idx, colli[i].idy);
			}
			detect_state(balls.size()*balls.size());
		}
		else if (colli.size() == 1){
			swap_v(colli[0].idx, colli[0].idy);
		}
		timel[time_index] -= tmin;
		return collisioncase(time_index);
	}

	return 1;
}



int main(int argc, char* argv[]){

	vector<double> stime;
	vector<string> checkin;
	string line;

// Get the time and put it in a double vector
	if(argc<2)return 2;
	for (int i=1; i<argc; i++){
		if (regexmatch2(argv[i]) == true) {
			double t1 = stod(argv[i]);
			stime.push_back(t1);
		}
		else {
			return 2;
		}
	}
	stime.push_back(0);
// Increment the times
	sort(stime.begin(), stime.end(), wayToSort);

// Read input file
	while (getline(cin,line)) {
		if (!line.size()) {return 1;}

		istringstream ss(line);

		istringstream iss(line);
		do
		{
			string temp1;
			iss >> temp1;
			checkin.push_back(temp1); 
		} while(iss);
		if (checkin.size() >6 ) {return 1;}

		for (int s=1; s<5; ++s){
			if (regexmatch(checkin[s]) == false) { return 1; }
		}
		checkin.clear();

		Ball ball;
		if (ss >> ball.name >> ball.xin >> ball.yin >> ball.vxin >> ball.vyin) {
			balls.push_back(ball);
		}
	}

	for (int i = 0; i < (stime.size()-1); i++){
		timel.push_back(stime[i+1] - stime[i]);
	}
	
	for (int i = 0; i < timel.size(); i++){
		cout << stime[i+1] << endl;
		collisioncase(i);
	}
	return 0;
}
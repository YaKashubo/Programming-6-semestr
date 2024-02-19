#include<iostream>
#include<cmath>
#include<vector>

using namespace std;

double f(double x)
{
	return 8 * cos(x) - x - 6;
}

vector<vector<double>> SepRoot(double A, double B, int N)
{
	double H = (B - A) / N;
	int count = 0;
	double X1 = A;
	double X2 = X1 + H;
	double Y1 = f(X1);

	vector<vector<double>> arr;
	while (X2 <= B)
	{
		double Y2 = f(X2);
		if (Y1 * Y2 <= 0)
		{
			vector<double> arr1 = { X1,X2 };
			arr.push_back(arr1);
			count++;
			//cout << "[" << X1 << ";" << X2 << "]" << endl;	
		}
		X1 = X2;
		X2 = X1 + H;
		Y1 = Y2;
	}
	//cout << count << endl;
	return arr;
}


int main()
{
	double A = -9;
	double B = 1;
	double eps = 10e-7;

	vector<vector<double>> interval = SepRoot(A, B, 10);
	for (int i = 0; i < interval.size(); ++i)
	{
		cout << "[" << interval[i][0] << ";" << interval[i][1] << "]" << endl;
	}


	return EXIT_SUCCESS;
}
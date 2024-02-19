#include<iostream>
#include<cmath>
#include<vector>
#include<iomanip>

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

int bisection(double a, double b, double eps)
{
	double A = a;
	double B = b;
	int m = 0;
	do
	{
		double c = (a + b) / 2;
		if (f(a) * f(c) <= 0)
		{
			b = c;
		}
		else
		{
			a = c;
		}
		m++;
	} while (b - a > 2 * eps);

	cout << "Начальное приближение: " << (A + B) / 2 << endl;
	cout << " Корень на промежутке [" << A << ";" << B << "]: " << (b + a) / 2 << endl;
	cout << " |Xm-X(m-1)|: " << (b - a) / 2 << endl;
	cout << " Величина невязки |f(x)-0|: " << abs(f((b + a) / 2) - 0) << endl << endl;
	return m;
}

double deriv(double x, double f1(double x))
{
	const double h = 1e-5;
	return (f1(x + h) - f1(x - h)) / (2.0 * h);
}

double deriv2(double x, double f1(double x))
{
	const double h = 1e-5;
	return (f1(x + h) - 2. * f1(x) + f1(x - h)) / (h * h);
}

double newtone(double a, double b, double eps)
{
	double A = a;
	double B = b;
	double X0 = 0;
	if (f(A) * deriv2(A, f) > 0)
	{
		X0 = A;
	}
	else if (f(B) * deriv2(B, f) > 0)
	{
		X0 = B;
	}
	else return 0;
	cout << "Начальное приближение: " << X0 << endl;

	int m = 0;
	double X = X0 - (f(X0) / deriv(X0, f));
	do
	{
		m++;
		X0 = X;
		X = X0 - (f(X0) / deriv(X0, f));

	} while (abs(X-X0) >eps);


	cout << " Корень на промежутке [" << A << ";" << B << "]: " << X << endl;
	cout << " |Xm-X(m-1)|: " << abs(X - X0)<< endl;
	cout << " Величина невязки |f(x)-0|: " << abs(f(X) - 0) << endl << endl;
	return m;
}

double mod_newtone(double a, double b, double eps)
{
	double A = a;
	double B = b;
	double X0 = 0;
	if (f(A) * deriv2(A, f) > 0)
	{
		X0 = A;
	}
	else if (f(B) * deriv2(B, f) > 0)
	{
		X0 = B;
	}
	else return 0;
	cout << "Начальное приближение: " << X0 << endl;

	int m = 0;
	double X = X0 - (f(X0) / deriv(X0, f));
	double Xk = 0;
	do
	{
		m++;
		Xk = X;
		X = Xk - (f(Xk) / deriv(X0, f));

	} while (abs(X - Xk) > eps);


	cout << " Корень на промежутке [" << A << ";" << B << "]: " << X << endl;
	cout << " |Xm-X(m-1)|: " << abs(X - Xk) << endl;
	cout << " Величина невязки |f(x)-0|: " << abs(f(X) - 0) << endl << endl;
	return m;
}
int main()
{
	setlocale(LC_ALL, "Russian");

	double A = -9;
	double B = 1;
	double eps = 1e-7;
	int N = 100;

	cout << "Решение нелинейных уравнений с исходными параметрами." << endl;
	cout << "Исходные параметры:" << endl << "Уравнение 8cos(x) - x - 6 = 0." << endl;
	cout << "Корни на промежутке [" << A << ";" << B << "] c погрешностью " << eps << "." << endl;
	cout << "Шаг табулирования промежутка: " << (B - A) / N << endl << endl;;

	vector<vector<double>> interval = SepRoot(A, B, N);
	cout << "Количество знакопеременных промежутков: " << interval.size() << endl;
	for (int i = 0; i < interval.size(); ++i)
	{
		cout << "[" << interval[i][0] << ";" << interval[i][1] << "]" << endl;
	}

	cout << endl << "Определение корней методом БИССЕКЦИИ" << endl;
	int k = 0;
	for (int i = 0; i < interval.size(); ++i)
	{
		k += bisection(interval[i][0], interval[i][1], eps);
	}
	cout << " Количество шагов для определения всех корней: " << k << endl << endl;

	cout << endl << "Определение корней методом НЬЮТОНА" << endl;
	k = 0;
	for (int i = 0; i < interval.size(); ++i)
	{
		k += newtone(interval[i][0], interval[i][1], eps);
	}
	cout << " Количество шагов для определения всех корней: " << k << endl << endl;

	cout << endl << "Определение корней МОДИФИЦИРОВАННЫМ методом НЬЮТОНА" << endl;
	k = 0;
	for (int i = 0; i < interval.size(); ++i)
	{
		k += mod_newtone(interval[i][0], interval[i][1], eps);
	}
	cout << " Количество шагов для определения всех корней: " << k << endl << endl;

	return EXIT_SUCCESS;
}
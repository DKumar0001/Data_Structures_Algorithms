#include<iostream>
using namespace std;

int factorial(int num)
{
  if (num == 1 ||num == 0)
  {
  return 1;
  }
  else
  {
    return (num * factorial(num - 1));
  }
}

int main()
{
  int num;
  cout << "Enter a number";
  cin >> num;
  int fact = factorial(num);
  cout << "Factorial is" << fact << endl;
  return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t,x;
    double m,tax,tip;
    cin>>m>>t>>x;
    tip=m*t/100;
    tax=m*x/100;
    float tot=tip+tax+m;
    int abs;
    float fval;
    abs=int(tot);
    fval=tot-abs;
    if(fval>0.49)
        abs++;
    cout<<"The final price of the meal is $"<<abs<<".";
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}


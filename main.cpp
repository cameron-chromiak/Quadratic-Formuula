#include <iostream>
#include <string>
#include <math.h>

using namespace std;
int main()
{
    float aValue, bValue, cValue;

    cout << "Enter A value " << endl;
    cin >> aValue;
    cout << "Enter B value " << endl;
    cin >> bValue;
    cout << "Enter C value" << endl;
    cin >> cValue;

    char sqrtSymbol = 251;
    float bSquared, multiplyAC,nNumerator, nDenomiminator;
    string checkDivisible;

    bSquared = bValue*bValue;
    multiplyAC = -4 * aValue * cValue;
    cout << multiplyAC;
    if (multiplyAC >= 0){
        nNumerator = bSquared - (multiplyAC *-1);
    }
    else{
        nNumerator = bSquared-multiplyAC;
    }

    nDenomiminator = 2 * aValue;
//    cout << "-" << bValue << "+-"<< sqrtSymbol << "(" << nNumerator<< ")" << endl;
//    cout << "    ----" << endl;
//    cout << "      " << nDenomiminator;
}

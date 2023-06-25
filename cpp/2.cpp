///Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
///1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
///By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#include <iostream>

using namespace std ;
int main()
{
    int x = 1;
    int y = 2;
    int z = 0;
    int u = 0;
    int sumOfNumbersCanDevideTwo = 0;

    ///If the numbers (x ,y , z ,u) below then four million it will enter the while loop
    while (x < 4000000 and y < 4000000 and z < 4000000 and u < 4000000){
        z = x + y;
        if (z % 2 == 0){
            sumOfNumbersCanDevideTwo = sumOfNumbersCanDevideTwo + z;
        }

        u = y + z;
        if (u % 2 == 0){
            sumOfNumbersCanDevideTwo = sumOfNumbersCanDevideTwo + u;
        }

        x = z + u;
        if (x % 2 == 0){
            sumOfNumbersCanDevideTwo = sumOfNumbersCanDevideTwo + x;
        }

        y = x + u;
        if (y % 2 == 0){
            sumOfNumbersCanDevideTwo = sumOfNumbersCanDevideTwo + y;
        }
    }
    ///Here we added two because at first we didn't add two.
    cout << sumOfNumbersCanDevideTwo + 2;
}
///The result is 4613732

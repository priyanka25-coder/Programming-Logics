#include <stdio.h>
#include <stdlib.h> // Needed for both atoi and atof

int main() {
    // 1. Automatic (Int to Float)
    float a = 5; 
    printf("Automatic: %f\n", a); // Prints 5.000000

    // 2. Manual / Typecast (Float to Int)
    int b = (int)10.75; 
    printf("Manual: %d\n", b); // Prints 10

    // 3. Text to Whole Number
    int c = atoi("123"); 
    printf("String to Int: %d\n", c); // Prints 123

    // 4. Text to Decimal Number
    float d = atof("45.67"); 
    printf("String to Float: %f\n", d); // Prints 45.670000
}
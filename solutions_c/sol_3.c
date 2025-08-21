#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int is_prime(int num){
    if (num < 2){
        return 0;
    }
    if (num % 2 == 0){
        return num == 2;
    }
    int r = (int)sqrt(num) + 1;
    for (int i = 3; i <= r; i += 2){
        if (num % i == 0){
            return 0;
        }
    }
    return 1;
}
int rho(int number){

}
int main(){
    long long num = 600851475143;
    if is_prime(num){
        return num;
    }
    )

}

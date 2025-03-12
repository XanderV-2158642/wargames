#include <stddef.h>
#include <stdio.h>

void win() {
    printf("good job \n");
}

int main(){

    int val = 1234;
    char* char_val = (char*) &val;

    printf("%s\n", char_val);
    
    printf("%p\n", win);

    char x []= "0x5562be8dc189";

    ((void (*)())*(int*)x)();
}

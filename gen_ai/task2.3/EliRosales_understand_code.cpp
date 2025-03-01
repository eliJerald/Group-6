int max3(int a, int b, int c) {
    if (a > b) {
        //check if a>b
        return (a > c) ? a : c;
        //checks if a>c. if T return a else return c
    } else {
        return (b > c) ? b : c;
        //checks if b>c. if T return b else return c

    }
}
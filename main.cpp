/*
Arman Ashrafian
March 2018

SAP-1 Assembler

Intructions:
LDA - 0000
ADD - 0001
SUB - 0010
OUT - 1110
HLT - 1111
*/

#include <iostream>

/****** init functions *********/

// parse program by space
int parse(std::string program); 


int main() {
    parse("hello");

    return 0;
}

std::vector<std::string> parse(std::string program) {
    std::cout << program << std::endl;
}
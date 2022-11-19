#include <iostream>
#ifndef MYCLASS_H
#define MYCLASS_H

class MyClass
{
    public:
        MyClass();
        void sayHi() {
            std::cout << "Hello World";
        }
    private:
    protected:
};

#endif
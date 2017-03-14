For static languages such as C/C++, C#, and Java, we usually use **Singleton** pattern to ensure there is only one instance for a class.
However, for dynamic languages such as Python, we can't implement Singleton pattern. One reason is that we cannot hide the constructor.

Basic Singleton implementation includes the following concept:
1. Only one instance for a class
2. Hide the constructor -- make it **private**
3. Provide a **public** function to access the instance

E.g.

class Singleton() {
    private static Singleton ins = NULL;
    **private** Singleton(){
        // init data members
    }
    **public** static Singleton getInstance() {
        if (ins == NULL) {
            ins = new Singleton();
        }
        return ins
    }
}

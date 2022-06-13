// See https://aka.ms/new-console-template for more information

// use "cd [name]" to target directory with name "[name]"
// use "cd .." to go back one step
// use "dotnet run" to run current directory. (look at entire folder as one program)

// Don't forget to save the file before running
// The process of running may take a bit of time... so be patient!

namespace Generation {
    class CuteAnimal { //main scope
        class Cat { //additionally declared scope
            
            public static int count = 0; //static property member
            public int catID; //declared property
            public Cat() { //constructor
                Console.WriteLine("{0}th Cat object has been generated!", count + 1);
                count++;
            }

            public void Call() { //method calling
                Console.WriteLine("Meow~ (From {0}th Cat object)...", catID);
            }

            public void Call(int n) {
                int x = 0;
                while (x < n) {
                    Console.WriteLine("Nyan~ (From {0}th Cat object, {1}th time", catID, x);
                    x++;
                }
            }

            ~Cat() { //destructor
                count--;
            }
        }

        class Dog {
            public static int count = 0;

            public int dogID;
            
            public Dog() {
                Console.WriteLine("{0}th Dog object has been generated!", count + 1);
                count++;
            }

            public void Call() { //can be used for "object" of a class only
                Console.WriteLine("Wan! (From {0}th Dog object)...", dogID);
            }

            public void Call(int n) { //method OVERLOADING (through differed number of parameter!)
                int x = 0;
                while (x < n) {
                    Console.WriteLine("Woof! (From {1}th Dog object, {0}th times)", x + 1, dogID);
                    x++;
                }
            }

            public static void Bark() { //this method may be called directly from a class (because it's STATIC)
                Console.WriteLine("Woof~ woof~ (Class's method calling)");
            }

            ~Dog() {
                count--;
            }
        }

        // MAIN FUNCITON STARTS HERE
        static void Main(string[] args) {
            
            Cat c1 = new Cat();
            c1.catID = 1;
            Cat c2 = new Cat();
            c2.catID = 2;
            Console.WriteLine("There are {0} Cat object.", Cat.count);
            c2.Call();
            c1.Call();

            Dog d1 = new Dog();
            d1.dogID = 1;
            d1.Call();
            Dog.Bark();
            d1.Call(5);
            c1.Call(4);
        }
    }
}
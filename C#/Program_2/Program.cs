// See https://aka.ms/new-console-template for more information
namespace World {
    
    class Generation {

        class Human {
            public Human() {
                Console.WriteLine("A Human object has been created.");
            }
        }

        class Children : Human {
            public Children() {
                Console.WriteLine("A Children object has been created.");
            }
        }

        static void Main(string[] args) {
            Human c1 = new Children();
        }
    }
}
public class task2 {
    public static void main(String[] args) {

int[] intArray = {2,5,7,3,7,3,2,3,2};

try {
    int d = 10;
    double catchedRes1 = 1.0*intArray[8] / d;
    System.out.println("catchedRes1 = " + catchedRes1);
}   catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Catching exception: " + e);
}   catch (ArithmeticException e) {
    System.out.println("Catching exception: " + e);
}

 
}
}
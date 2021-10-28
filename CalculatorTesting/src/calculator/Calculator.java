package calculator;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Double a, b;
    
        Scanner input = new Scanner(System.in);
    
        System.out.println("Enter first number");
        a = input.nextDouble();
    
        System.out.println("Enter second number");
        b = input.nextDouble();
        
        input.close();
        
        System.out.println("Sum: " + sum(a, b));
        System.out.println("Subtraction: " + subtract(a, b));
        System.out.println("Multiplication: " + mult(a, b));
        System.out.println("Division: " + div(a, b));
    }

    public static <T extends Number> double sum (T a, T b) {
        return a.doubleValue() + b.doubleValue(); 
    }

    public static <T extends Number> double subtract (T a, T b) {
        return a.doubleValue() - b.doubleValue(); 
    }

    public static <T extends Number> double mult (T a, T b) {
        return a.doubleValue() * b.doubleValue(); 
    }

    public static <T extends Number> double div (T a, T b) {
        return a.doubleValue() / b.doubleValue(); 
    }
}
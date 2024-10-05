/**
 * Frank Madu
 * 
 * Shape.java
 * The superclass Shape and its subclasses Circle, Rectangle, and Triangle.
 * Demonstrates the concept of polymorphism through the use of the calculateArea method 
 * overridden in each subclass.
 */

/**
 * The base class representing a general shape.
 * This class provides a method to calculate the area of a shape.
 * The default implementation returns 0.
 */

public class Shape {
    /**
     * Method to calculate the area of the shape.
     * This method should be overridden by subclasses.
     * 
     * @return the area of the shape (default is 0)
     */
    public double calculateArea() {
        return 0;
    }

    // Circle subclass
    public static class Circle extends Shape {
        // Declare a private double variable radius
        private double radius;

        /**
         * Constructor for the Circle class.
         * 
         * @param radius the radius of the circle
         */
        
        public Circle(double radius) {
            this.radius = radius;
        }

        /**
         * Method to calculate the area of the circle.
         * Overrides the calculateArea method in the Shape class.
         * 
         * @return the area of the circle (πr²)
         */
        
        @Override
        public double calculateArea() {
            return Math.PI * radius * radius;
        }
    }

    // Rectangle subclass
    public static class Rectangle extends Shape {
        // Declare private double variables width and height
        private double width;
        private double height;

        /**
         * Constructor for the Rectangle class.
         * 
         * @param width  the width of the rectangle
         * @param height the height of the rectangle
         */

        public Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        /**
         * Method to calculate the area of the rectangle.
         * Overrides the calculateArea method in the Shape class.
         * 
         * @return the area of the rectangle (width * height)
         */

        @Override
        public double calculateArea() {
            return width * height;
        }
    }

    // Triangle subclass
    public static class Triangle extends Shape {
        // Declare private double variables base and height
        private double base;
        private double height;

        /**
         * Constructor for the Triangle class.
         * 
         * @param base   the base of the triangle
         * @param height the height of the triangle
         */

        public Triangle(double base, double height) {
            this.base = base;
            this.height = height;
        }

        /**
         * Method to calculate the area of the triangle.
         * Overrides the calculateArea method in the Shape class.
         * 
         * @return the area of the triangle (0.5 * base * height)
         */

        @Override
        public double calculateArea() {
            return 0.5 * base * height;
        }
    }

    /**
     * Main method to demonstrate the functionality of the Shape class and its subclasses.
     * 
     * @param args command-line arguments (not used)
     */

    public static void main(String[] args) {
        // Create a Circle object with radius 4
        Circle circle = new Circle(4);
        System.out.println("Area of Circle: " + circle.calculateArea());

        // Create a Rectangle object with width 12 and height 34
        Rectangle rectangle = new Rectangle(12, 34);
        System.out.println("\nArea of Rectangle: " + rectangle.calculateArea());

        // Create a Triangle object with base 5 and height 9
        Triangle triangle = new Triangle(5, 9);
        System.out.println("\nArea of Triangle: " + triangle.calculateArea());
    }
}


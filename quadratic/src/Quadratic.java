/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author cchromia
 */
import java.util.Scanner;
        
public class Quadratic {

  public static void main(String[] args) {
    double a, b, c, d, x1, x2;
    Scanner input = new Scanner(System.in);
    System.out.println("Enter A, B, and C value");
    
    a = input.nextDouble();
    b = input.nextDouble();
    c = input.nextDouble();
  if (a==0){
    System.out.println("a cannot be 0");
    System.exit(0);
  }
  
  d = b*b - 4*a*c;
  
  if(d<0){
    System.out.println("No real solution");
  }
  else if (d == 0){
    System.out.println("The unique solution is "+ b/(2*a));
  }
  else {
    x1 = (-b - Math.sqrt(d))/(2*a);
    x2 = (-b + Math.sqrt(d))/(2*a);   
    System.out.println("The two solutions are"+x1 +"and"+x2);
  }
  
  }
  
}

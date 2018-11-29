/*
  Simulate Lottery where you pick 3 numbers between 1 - 20 and one last nyumber
  between 1 - 7.  Price of the ticket is $2.  If the numbers matched is 3+1, you
  win $100; 3+0, you win $10; 2+1, you win $5; 1+1, you win $2.  Play this game
  until your net gain is >= $50 and report the number of times played.
 *
 * @author nmahadev
 */
import java.util.Random;

public class Lottery2 {

  public static void main(String[] args) {
    // Declare variables
    int count, netgain, price, play1, play2, play3, play4,
            win1, win2, win3, win4, matched1, matched2;
    Random random = new Random();

    // Generate the winning numbers and store
    win1 = random.nextInt(20) + 1;
    win2 = random.nextInt(20) + 1;
    win3 = random.nextInt(20) + 1;
    win4 = random.nextInt(7) + 1;

    // Set initial values for count, netgain and price
    count = 0;
    netgain = 0;
    price = 2;

    // while netgain < 50 do
    while (netgain < 50) {

      // update netgain by subtracting price
      netgain -= price;

      // increment count by 1
      count += 1;

      // reset matched count to zero
      matched1 = 0;
      matched2 = 0;

      // generate player numbers
      play1 = random.nextInt(20) + 1;
      play2 = random.nextInt(20) + 1;
      play3 = random.nextInt(20) + 1;
      play4 = random.nextInt(7) + 1;

      // match the player numbers with win numbers and update the netgain
      if (win1 == play1) {
        matched1 += 1;
      }
      if (win2 == play2) {
        matched1 += 1;
      }
      if (win3 == play3) {
        matched1 += 1;
      }
      if (win4 == play4) {
        matched2 += 1;
      }
      if (matched1 == 3 && matched2 == 1) {
        netgain += 100;
      } else if (matched1 == 3 && matched2 == 0) {
        netgain += 10;
      } else if (matched1 == 2 && matched2 == 1) {
        netgain += 5;
      } else if (matched1 == 1 && matched2 == 1) {
        netgain += 2;
      }

      // print the results
      System.out.println("Your net gain is $"+netgain+" after "+count+" games");
    }
  }

}

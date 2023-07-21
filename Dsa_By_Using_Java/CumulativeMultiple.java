import java.util.*;
public class CumulativeMultiple {
    public static void main(String args[]){
        // getting the scanner
        Scanner sc = new Scanner(System.in);
        // reading the n vallue form user
        System.out.print("Enter value of n :");
        int n = sc.nextInt();
        //creating an arraylist to store th n integers
        ArrayList<Integer> nums = new ArrayList<Integer>();
        System.out.println("Enter nxt n integers");
        //loop for reading the numbers and storing it into the arraylist
        for(int i=0;i<n;i++){
            int num = sc.nextInt();
            nums.add(num);
        }

        // calculating the cumulative multiples
        int cm = 1;
        for(int i=0;i<n;i++){
            cm= cm*nums.get(i);
            nums.set(i,cm);
        }
        //printing the result
        for(int it: nums){
            System.out.print(it+" ");
        }
        // closing the scanner
        sc.close();
    }
}

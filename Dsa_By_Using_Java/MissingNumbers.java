import java.util.*;
public class MissingNumbers {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        // Reading the n value from user
        System.out.print("Enter n value : ");
        int n = sc.nextInt();
        ArrayList<Integer> nums = new ArrayList<>();
        // Reading n integers from user add stroing it in nums
        System.out.println("Enter next integers : ");
        for(int i=0;i<n;i++){
            int num = sc.nextInt();
            nums.add(num);
        }
        // created an array to store the missing numbers
        ArrayList<Integer> miss = new ArrayList<>();
        for(int i=0;i<n-1;i++){
            // if the two consecutive numbers are not add the num into miss until the two nums are consecutive
            if(nums.get(i)!=nums.get(i+1)-1){
                int t = nums.get(i);
                while(t!=nums.get(i+1)-1)
                {
                    miss.add(t+1);
                    t++;
                }    
            }
        }
        //printing the result
        for(int it:miss){
            System.out.print(it+" ");
        }
        sc.close();
    }
}

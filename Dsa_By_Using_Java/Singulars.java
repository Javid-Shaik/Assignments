import java.util.*;
public class Singulars {
    public static void main(String args[]){
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
        // Craeting the hashmap for storing the values 
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int sock :nums){
            // if the key is already present then just increment it's count
            if(map.containsKey(sock)){
                map.put(sock,map.getOrDefault(sock, 0)+1);
            }
            // if not set it as 1
            else {
                map.put(sock , 1);
            }
        }
        // counting the pairs
        Integer pairs = 0;
        for(Integer key : map.keySet()) {
            pairs += map.get(key)%2;
        }
        System.out.println(pairs);
    }
}

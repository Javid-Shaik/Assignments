import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;

public class ReomveDuplicates {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        // creating a linkedlist and reading the data into it
        LinkedList<Integer> list = new LinkedList<>();
        System.out.print("Enter list1 size : ");
        int n1 = sc.nextInt();
        System.out.println("Enter elements for list1 : ");
        for(int i=0;i<n1;i++){
            list.add(sc.nextInt());
        }
        // utility function for removing the duplicates
        removeDuplicates(list);

        // printing the elements after removing duplicates
        for(Integer item : list){
            System.out.print(item+" ");
        }
        sc.close();
    }

    private static void removeDuplicates(LinkedList<Integer>list){
        // creating hashset for stroing unique elements
        HashSet<Integer> seenElements = new HashSet<>();
        LinkedList<Integer>unique = new LinkedList<>();
        
        // if the element is not already present in the set add else add it to duplicates list
        for (Integer item : list) {
            if (seenElements.add(item)) {
                // This element is a duplicate
                unique.add(item);
            }
        }
        // clear the entire list and add the unique elements
        list.clear();
        list.addAll(unique);
        
    }
}

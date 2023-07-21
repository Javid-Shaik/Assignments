import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class RemoveDuplicate {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> list1 = new LinkedList<>();
        System.out.print("Enter list1 size : ");
        int n1 = sc.nextInt();
        System.out.println("Enter elements for list1 : ");
        for(int i=0;i<n1;i++){
            list1.add(sc.nextInt());
        }
        
        LinkedList<Integer> list2 = new LinkedList<>();
        
        System.out.print("Enter list2 size : ");
        
        int n2 = sc.nextInt();
        
        System.out.println("Enter elements for list1 : ");
        
        for(int i=0;i<n2;i++){
            list2.add(sc.nextInt());
        }

        // Sort both linked lists individually
        Collections.sort(list1);
        Collections.sort(list2);

        // Merge the sorted linked lists
        LinkedList<Integer> mergedList = mergeSortedLists(list1, list2);

        // Print the merged list
        for (Integer item : mergedList) {
            System.out.print(item + " ");
        }
    }

    public static LinkedList<Integer> mergeSortedLists(LinkedList<Integer> list1, LinkedList<Integer> list2) {
        LinkedList<Integer> mergedList = new LinkedList<>();
        int i = 0, j = 0;

        while (i < list1.size() && j < list2.size()) {
            int num1 = list1.get(i);
            int num2 = list2.get(j);

            if (num1 <= num2) {
                mergedList.add(num1);
                i++;
            } else {
                mergedList.add(num2);
                j++;
            }
        }

        while (i < list1.size()) {
            mergedList.add(list1.get(i));
            i++;
        }

        while (j < list2.size()) {
            mergedList.add(list2.get(j));
            j++;
        }

        return mergedList;
    }
}


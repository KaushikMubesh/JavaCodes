import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;


public class rakul{
    public static void main(String args[]){
        Map<Integer,Integer> dic =new HashMap<>();
        int target = 7;
        List<Integer> myList = new ArrayList<>(List.of(1,2,3,4,3,3,5,6,6));
        for (int i=0;i<myList.size();i++){
            dic.put(myList.get(i),i);
        }
        List <Integer> result=new ArrayList<>();
        for (int j=0;j<myList.size();j++){
            
            if(dic.containsKey(target-myList.get(j))){
                result.add(j);
                result.add(dic.get(target-myList.get(j)));
                break;
            }
        }
        System.out.println(result);
    }
}
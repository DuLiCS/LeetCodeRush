import java.util.*;

public class L380 {
    List<Integer> valList = new ArrayList<>();
    Map<Integer, Integer> indexMap = new HashMap<>();
    Random rand = new Random();
    public L380() {

    }

    public boolean insert(int val) {
        if (!indexMap.containsKey(val)){
            valList.add(val);
            indexMap.put(val, valList.size() - 1);
            return true;
        }
        return false;
    }

    public boolean remove(int val) {
        if (indexMap.containsKey(val)){
            int temp = valList.get(valList.size() - 1);
            int index = indexMap.get(val);

            valList.set(index, temp);
            indexMap.put(temp, index);

            valList.remove(valList.size() - 1);
            indexMap.remove(val);

            return true;
        }
        return false;
    }

    public int getRandom() {
        return valList.get(rand.nextInt(valList.size()));
    }
}

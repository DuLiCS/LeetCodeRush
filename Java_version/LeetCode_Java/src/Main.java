import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        L605 sol = new L605();
        int[] flowerbed = {1,0,1,0,0,0,0,1,0};
        int n = 2;
        System.out.println(sol.canPlaceFlowers(flowerbed, n));
    }
}
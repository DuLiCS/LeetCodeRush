public class L605 {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if ((i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.length - 1 || flowerbed[i+1] == 0) && flowerbed[i] ==0 ){
                flowerbed[i] = 1;
                count += 1;
            }
        }
        return count >= n;
    }
}

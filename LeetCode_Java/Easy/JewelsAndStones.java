package Easy;

public class JewelsAndStones {
    public int numJewelsInStones(String jewels, String stones) {
        int counter = 0;

        for (int i = 0; i < stones.length(); i++){
            // stones.charAt(i) will return char at a given index;
            // jewels.indexOf() will return index of the char ( otherwise it will return -1 )
            if (jewels.indexOf(stones.charAt(i)) != -1){
                counter++;
            }
        }

        return counter;
    }
}

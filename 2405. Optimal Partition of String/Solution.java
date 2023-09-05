import java.util.Set;
import java.util.HashSet;

class Solution {
    public int partitionString(String s) {
        Set<Character> chars = new HashSet();
        int count = 1;

        for(int i=0; i<s.length(); i++){
            if (!chars.contains(s.charAt(i))) {
                chars.add(s.charAt(i));
            }
            else{
                chars.clear();
                count++;
               chars.add(s.charAt(i));
            }
        }
        return count;
        
    }
}
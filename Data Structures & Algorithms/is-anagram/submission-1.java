
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map1 = new HashMap<Character, Integer>();
        HashMap<Character, Integer> map2 = new HashMap<Character, Integer>();
        for(int i=0;i<s.length();i++){
            if(!map1.containsKey(s.charAt(i))){
                map1.put(s.charAt(i),1);
            }
            else{
                map1.put(s.charAt(i),map1.get(s.charAt(i))+1);
            }
        }

        for(int i=0;i<t.length();i++){
            if(!map2.containsKey(t.charAt(i))){
                map2.put(t.charAt(i),1);
            }
            else{
                map2.put(t.charAt(i),map2.get(t.charAt(i))+1);
            }
        }
        if(map1.size()!= map2.size()){
            return false;
        }

        Set<Character> Cset = new HashSet<Character>();
        Cset = map1.keySet();
        Object[] array = Cset.toArray();

        for(int i=0; i<map1.size(); i++){
            if(map2.containsKey(array[i])){
                if(map2.get(array[i]) == map1.get(array[i])){
                    continue;
                }
                else {
                    return false;
                }
            }
            else{
                return false;
            }


        }

        return true;
    }
}

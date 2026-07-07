class Solution {

    public String encode(List<String> strs) {
        if(strs == null || strs.isEmpty()) {
            return "";
        }
        
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            
            sb.append(str.length());
            sb.append("#");
            sb.append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            // find delimiter position
            int j = i;
            while(j < str.length() && str.charAt(j) != '#') {
                j++;
            }

            // find and extract length
            int length = Integer.parseInt(str.substring(i, j));
            j++;
            //extract string
            String word = str.substring(j, j+length);
            result.add(word);
            //move the pointer
            i = j+length;
        }
        return result;
    }
}

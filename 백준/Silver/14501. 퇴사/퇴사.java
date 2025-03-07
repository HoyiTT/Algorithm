import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[][] consulting;
    static int maxProfit = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());

        consulting = new int[n][2];



        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine(), " ");
            consulting[i][0] = Integer.parseInt(st.nextToken());
            consulting[i][1] = Integer.parseInt(st.nextToken());
        }

        // Arrays.stream(consulting)
        // .forEach(it -> System.out.println(Arrays.toString(it)));

        dfs(0,0);

        System.out.println(maxProfit);
    }
    
    public static void dfs(int day,int profit){
        if (day>= n){
            maxProfit = Math.max(profit, maxProfit);
            return ;
        }

        // 해당 날짜를 선택할 때
        if(day + consulting[day][0] <= n){
            dfs(day+consulting[day][0], profit + consulting[day][1]);
        }

        
        dfs(day+1, profit);
    }
        
    }

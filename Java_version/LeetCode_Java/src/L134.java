class L134 {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int current_tank = 0;
        int total_tank = 0;
        int start_station = 0;

        for (int i = 0; i < gas.length; i++) {
            current_tank += gas[i] - cost[i];
            total_tank += gas[i] - cost[i];
            if (current_tank < 0){
                current_tank = 0;
                start_station += 1;
            }
        }
        if (total_tank >= 0){
            return start_station;
        }else{
            return -1;
        }
    }
}
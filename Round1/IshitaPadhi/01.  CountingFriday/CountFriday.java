
public class CountFriday {
    public static void main(String[] args) {
        int fridayCount = 0; 
        int dayOfWeek = 6; // 1 Jan 2000 is Saturday (Saturday=6 if we consider Sunday=0)

        // Loop over each year from 2000 to 2020
        for (int year = 2000; year <= 2020; year++) {
            // Loop over each month of the year
            for (int month = 1; month <= 12; month++) {
                int daysInMonth = getDaysInMonth(month, year);

                // 13th day of this month → calculate its weekday
                int thirteenthDayOfWeek = (dayOfWeek + 12) % 7;

                if (thirteenthDayOfWeek == 5) { // 5 means Friday
                    fridayCount++;
                }

                // Move dayOfWeek to the 1st day of next month
                dayOfWeek = (dayOfWeek + daysInMonth) % 7;
            }
        }
        System.out.println("Number of Fridays on the 13th between 2000 and 2020: " + fridayCount);
    }

    // Helper method: find number of days in a month
    public static int getDaysInMonth(int month, int year) {
        switch (month) {
            case 4: case 6: case 9: case 11: return 30; // April, June, Sept, Nov
            case 2: return (isLeapYear(year) ? 29 : 28);
            default: return 31; // Rest have 31
        }
    }

    // Leap year rule
    public static boolean isLeapYear(int year) {
        if (year % 400 == 0) return true;
        if (year % 100 == 0) return false;
        return year % 4 == 0;
    }
}

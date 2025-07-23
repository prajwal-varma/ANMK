public class StrongNumbers {
    public static void main(String[] args) {
        for (int num = 1; num <= 5000; num++) {
            if (isStrong(num)) {
                System.out.println(num);
            }
        }
    }

    static boolean isStrong(int n) {
        int original = n;
        int sum = 0;

        while (n > 0) {
            int digit = n % 10;
            sum += factorial(digit);
            n = n / 10;
        }

        return sum == original;
    }

    static int factorial(int n) {
        int fact = 1;

        for (int i = 2; i <= n; i++) {
            fact *= i;
        }

        return fact;
    }
}

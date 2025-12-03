import java.util.Scanner;

// ABSTRACT CLASS (Abstraction)
abstract class Rental {
    private int studentID;
    private int hours;
    private int minutes;
    private double totalPayment;
    private double amountPaid;
    private double change;

    public Rental(int studentID, int hours, int minutes) {
        this.studentID = studentID;
        this.hours = hours;
        this.minutes = minutes;
    }

    public abstract double calculatePayment();

    public int getStudentID() { return studentID; }
    public int getHours() { return hours; }
    public int getMinutes() { return minutes; }
    public double getTotalPayment() { return totalPayment; }
    public double getAmountPaid() { return amountPaid; }
    public double getChange() { return change; }

    public void setTotalPayment(double totalPayment) {
        this.totalPayment = totalPayment;
    }

    public void setAmountPaid(double amountPaid) {
        this.amountPaid = amountPaid;
    }

    public void setChange(double change) {
        this.change = change;
    }

    @Override
    public String toString() {
        return "Student ID: " + studentID +
               " | Time: " + hours + "h " + minutes + "m" +
               " | Total: " + totalPayment + " pesos" +
               " | Paid: " + amountPaid + " pesos" +
               " | Change: " + change + " pesos";
    }
}


// SUBCLASS 1
class BikeRental extends Rental {
    private static final double RATE = 20.0;

    public BikeRental(int studentID, int hours, int minutes) {
        super(studentID, hours, minutes);
    }

    @Override
    public double calculatePayment() {
        return (getHours() * RATE) + ((getMinutes() / 60.0) * RATE);
    }
}

// SUBCLASS 2
class ElectricBikeRental extends Rental {
    private static final double RATE = 40.0;

    public ElectricBikeRental(int studentID, int hours, int minutes) {
        super(studentID, hours, minutes);
    }

    @Override
    public double calculatePayment() {
        return (getHours() * RATE) + ((getMinutes() / 60.0) * RATE);
    }
}

// SUBCLASS 3
class MountainBikeRental extends Rental {
    private static final double RATE = 30.0;

    public MountainBikeRental(int studentID, int hours, int minutes) {
        super(studentID, hours, minutes);
    }

    @Override
    public double calculatePayment() {
        return (getHours() * RATE) + ((getMinutes() / 60.0) * RATE);
    }
}


public class missubibi {

    static Scanner sc = new Scanner(System.in);
    static Rental[] rentals = new Rental[100];
    static int rentalCount = 0;

    // FLASHING NEON TITLE
    public static void neonTitle() throws InterruptedException {
        String title = "MISSUBIBI'S OOP PROJECT";

        String[] colors = {
            "\u001B[95m",
            "\u001B[96m",
            "\u001B[91m",
            "\u001B[94m"
        };

        final String RESET = "\u001B[0m";

        for (int flash = 0; flash < 25; flash++) {
            System.out.print("\033[H\033[2J");
            System.out.flush();

            String color = colors[flash % colors.length];

            System.out.println("\n\n\n");
            System.out.println(color + "*************************************");
            System.out.println("  " + title + "  ");
            System.out.println("*************************************" + RESET);

            Thread.sleep(120);
        }
    }

    // PROGRESS BAR FUNCTION
    public static void progressBar() {
        String[] colors = {
            "\u001B[91m", "\u001B[92m", "\u001B[93m",
            "\u001B[94m", "\u001B[95m", "\u001B[96m"
        };

        final String RESET = "\u001B[0m";
        int total = 30;

        try {
            for (int i = 0; i <= total; i++) {
                String color = colors[i % colors.length];
                int filled = i;
                int empty = total - i;

                String bar = "[" +
                        color + "=".repeat(filled) + RESET +
                        " ".repeat(empty) +
                        "] " + (i * 100 / total) + "%";

                System.out.print("\r" + bar);

                Thread.sleep(70);
            }
            System.out.println();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }


    public static void main(String[] args) throws InterruptedException {

        neonTitle(); 

        while (true) {
            System.out.println("\n===== BSU BIKE RENTAL SYSTEM =====");
            System.out.println("[1] Rent a Bike");
            System.out.println("[2] View All Rentals");
            System.out.println("[3] Exit");
            System.out.print("Enter choice: ");

            int choice = getValidInt();

            switch (choice) {
                case 1 -> {
                    System.out.println("Loading Rental Menu...");
                    progressBar();
                    rentBike();
                }
                case 2 -> {
                    System.out.println("Fetching Records...");
                    progressBar();
                    viewRentals();
                }
                case 3 -> {
                    System.out.println("\nExiting System...");
                    progressBar();
                    System.out.println("Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }


    // RENTAL PROCESS
    public static void rentBike() {

        System.out.print("\nEnter Student ID: ");
        int id = getValidInt();

        System.out.print("Enter hours: ");
        int hours = getValidInt();

        System.out.print("Enter minutes: ");
        int minutes = getValidInt();

        progressBar();

        System.out.println("\nSelect Bike Type:");
        System.out.println("[1] Regular Bike (20 pesos/hr)");
        System.out.println("[2] Electric Bike (40 pesos/hr)");
        System.out.println("[3] Mountain Bike (30 pesos/hr)");
        System.out.print("Enter type: ");
        int type = getValidInt();

        System.out.println("\nProcessing...");
        progressBar();

        Rental r;

        switch (type) {
            case 1 -> r = new BikeRental(id, hours, minutes);
            case 2 -> r = new ElectricBikeRental(id, hours, minutes);
            case 3 -> r = new MountainBikeRental(id, hours, minutes);
            default -> {
                System.out.println("Invalid type.");
                return;
            }
        }

        double total = r.calculatePayment();
        r.setTotalPayment(total);

        System.out.println("\nTotal Payment: " + total + " pesos");
        System.out.print("Enter payment amount: ");
        double paid = getValidDouble();

        progressBar();

        if (paid < total) {
            System.out.println("Insufficient payment. Transaction cancelled.");
            return;
        }

        double change = paid - total;

        r.setAmountPaid(paid);
        r.setChange(change);

        rentals[rentalCount++] = r;

        System.out.println("\nRental Successful!");
        System.out.println("Change: " + change + " pesos");
    }


    // VIEW RENTALS
    public static void viewRentals() {
        System.out.println("\n===== RENTAL RECORDS =====");

        if (rentalCount == 0) {
            System.out.println("No rentals yet.");
            return;
        }

        for (int i = 0; i < rentalCount; i++) {
            System.out.println((i + 1) + ". " + rentals[i]);
        }
    }


    // INPUT VALIDATION
    public static int getValidInt() {
        while (true) {
            try {
                return Integer.parseInt(sc.next());
            } catch (Exception e) {
                System.out.print("Invalid number. Try again: ");
            }
        }
    }

    public static double getValidDouble() {
        while (true) {
            try {
                return Double.parseDouble(sc.next());
            } catch (Exception e) {
                System.out.print("Invalid amount. Try again: ");
            }
        }
    }
}

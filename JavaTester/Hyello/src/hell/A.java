package hell;

public class A {
    int x = 5;
    public void m1() {
        System.out.println("Am1 -> " + x);
    }
    public void m2() {
        System.out.println("Am2 -> " + this.x);
    }
    public void update() {
        x = 99;
    }
}

class B extends A {
    int x = 10;
    public void m2() {
        System.out.println("Bm2 -> " + x);
    }
    public void m3() {
        System.out.println("Bm3 -> " + super.x);
    }
    public void m4() {System.out.print("Bm4-> ");
        System.out.print(" | " + this.x + " | ");super.m2();}
}

class C extends B {
    int y = x + 1;
    public void m2() {System.out.println("Cm2-> " + super.x);}
    public void m4() {System.out.println("Cm4-> " + y);}
}

class D {
    public static void main(String[] args) {
        A b0 = new B();
        System.out.println(b0.x);
        b0.m1();
        b0.m2();
        B b1 = new B();
        b1.m3();
        b1.m4();

        b0.update();
        b0.m1();

        System.out.println("");

        A actuallyC = new C();
        System.out.println("actuallyC.x = " + actuallyC.x);
        System.out.println(actuallyC);
    }
}
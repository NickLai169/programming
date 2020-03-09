package hell;

public class Q {
    String myNum = "Cheesecake";
    public void a() {
        System.out.println("Q.a" + myNum);
    }
    public void b() {
        System.out.println("This is myNum: " + this.myNum);
        a();
    }
    public void c() {
        e();
    }
    public void d() {
        e();
    }
    public static void e() {
        System.out.println("Q.e");
    }
}

class R extends Q {
    String myNum = "Hello";
    public void a() {
        System.out.println("R.a" + this.myNum);
    }
    public void d() {
        e();
    }
    public static void e() {
        System.out.println("R.e");
    }
}

class G {

}

class S {
    public static void main(String[] args) {
        R aR = new R();
        run(aR);
    }
    public static void run(Q x) {
        System.out.println(x.myNum);
        System.out.println("x.a();");
        x.a(); /* Output: __________________ */
        System.out.println("x.b();");
        x.b(); /* Output: __________________ */
        System.out.println("x.c();");
        x.c(); /* Output: __________________ */
        System.out.println("((R)x).c();");
        ((R)x).c(); /* Output: __________________ */
        System.out.println("x.d();");
        x.d(); /* Output: __________________ */
        System.out.println("((R)x).d();");
        ((R)x).d(); /* Output: __________________ */
        System.out.println("");
        System.out.println("My tests now:");
        R ree = new R();
        x.e();
        ree.e();

    }
}


package hell;

public class Animal {
    protected String name, noise;
    protected int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
        this.noise = "huh?";
    }

    public String makeNoise() {
        if (age < 2) {
            return noise.toUpperCase();
        }
        return noise;
    }

    public String greet() {
        return name + ": " + makeNoise();
    }

    public static void main(String[] args) {

        Animal a = new Cat("Olivia", 3);
        a = new Dog("Fido", 7);
        System.out.println(a.greet());

        Dog d2 = (Dog) a;
        d2.playFetch();

        Animal imposter = new Cat("Pedro", 12);
//        Dog fakeDog = (Dog) imposter;

        Cat failedImposter = new Cat("Jimmy", 21);
//        Dog failedDog = (Dog) failedImposter;

//        Deer doe = new Deer("Charlie", 0);
//        System.out.println(doe.greet());

    }
}

class Cat extends Animal {

    public Cat(String name, int age) {
        super(name, age);
        noise = "meow";
    }
}

class Dog extends Animal {
    Dog(String cute, int fluffy) {
        super(cute, fluffy);
        this.noise = "woof";
    }

    public void playFetch() {
        System.out.println("Fetch, " + name + "!");
    }
}

class Deer extends Animal{
    int antlers, hooves, eyes;
    String name, noise;

    Deer(String name, int randomNum) {
        super(name, randomNum);
        if (randomNum != 0) {
            antlers = 2;
            hooves = 2;
            eyes = 1;
        } else {
            antlers = 10;
            hooves = 4;
            eyes = 2;
        }
        this.name = name;
        this.noise = "huurrggg";
    }
}

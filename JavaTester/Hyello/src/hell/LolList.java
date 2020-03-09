package hell;

import org.junit.Test;

import java.util.LinkedList;

public class LolList {
    int num = 5;
    String pine = "apple";
    void hurr() {
        System.out.println("hurr");
    }
    public LolList(int num, String word) {
        num = num;
        pine = word;
        System.out.println(num + " | " + this.num);
        System.out.println(word);
    }

    public static void main(String[] args) {
        LolList lawl = new LolList(10, "hehe");

    }
}

class Meme {
    String meme;
    int dankness;

    /**
     * DANKNESS must be non-negative.
     */
    public Meme(String name, int dankness) {
        meme = name; //CanFix
        this.dankness = dankness; //dankness = dankness; // CanFix
    }

    /**
     * Return the lowest dankness value in MEMES, or 0 if MEMES is null.
     */
    public static int getWeakestMeme(Meme[] memes) {
        if (memes == null || memes.length == 0) {
            return 0;
        }
        int minDank = memes[0].dankness; //int minDank = 0; //CanFix
        for (int i = 0; i < memes.length; i++) {//for (int i = 0; i <= memes.length; i += 1) { //CanFix
            minDank = Math.min(minDank, memes[i].dankness); //CanFix
        }
        return minDank;
    }

    public static void main(String[] args) {
        Meme[] memeStash = new Meme[3];
        memeStash[0] = new Meme("Pepe", 4);
        memeStash[1] = new Meme("John Cena", 100);//memeStash[1] = new Meme("John Cena", 20);
        memeStash[2] = new Meme("Harambe", 20160528);
        System.out.println(4 + " | " + getWeakestMeme(memeStash));
//            assertEquals(4, getWeakestMeme(memeStash));
        Meme[] anotherOne = memeStash;
        anotherOne[0] = new Meme("Only Meme", 100);
        System.out.println(100 + " | " + getWeakestMeme(anotherOne));
//            assertEquals(100, getWeakestMeme(anotherOne));


    }
}
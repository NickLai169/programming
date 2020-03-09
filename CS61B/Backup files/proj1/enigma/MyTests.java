package enigma;

import org.junit.Test;

import static org.junit.Assert.*;

import java.util.LinkedList;
import java.util.Scanner;

import static enigma.TestUtils.*;

public class MyTests {

    public static void main(String[] args) {
        MyTests testing = new MyTests();
        testing.testMachine();
        testing.testScanners();
        testing.testPermutations();
        testing.testInverse();
        testing.checkFixedRotor();
    }

    @Test
    public void testPermutations() {
        Alphabet permutationAlphabet = new Alphabet("JOHNCEADISMWZ");
        Permutation myPermutation =
                new Permutation("(ANDHISMEW) (JO) (C)", permutationAlphabet);
        assertEquals("the size is wrong", 13, myPermutation.size());
        System.out.println("JOHNCEADISMWZ".indexOf('Z'));
        assertEquals("Permute A", 3, myPermutation.permute(6));
        assertEquals("Permute A (char)", 'N', myPermutation.permute('A'));

        assertEquals("Permute O", 0, myPermutation.permute(1));
        assertEquals("Permute O (char)", 'J', myPermutation.permute('O'));

        assertEquals("Permute C", 3, myPermutation.permute(6));
        assertEquals("Permute C (char)", 'N', myPermutation.permute('A'));

        assertEquals("Permute Z", 12, myPermutation.permute(12));
        assertEquals("Permute Z (char)", 'Z', myPermutation.permute('Z'));
    }

    @Test
    public void testInverse() {
        Alphabet inverseAlphabet = new Alphabet("JOHNCEADISMWZ");
        Permutation myPermutation =
                new Permutation("(ANDHISMEW) (JO) (C)", inverseAlphabet);
        assertEquals("the size is wrong", 13, myPermutation.size());
        System.out.println("JOHNCEADISMWZ".indexOf('Z'));
        assertEquals("Invert A", 11, myPermutation.invert(6));
        assertEquals("Invert A (char)", 'W', myPermutation.invert('A'));

        assertEquals("Invert O", 0, myPermutation.invert(1));
        assertEquals("Invert O (char)", 'J', myPermutation.invert('O'));

        assertEquals("Invert C", 4, myPermutation.invert(4));
        assertEquals("Invert C (char)", 'C', myPermutation.invert('C'));

        assertEquals("Invert Z", 12, myPermutation.invert(12));
        assertEquals("Invert Z (char)", 'Z', myPermutation.invert('Z'));
    }

    @Test
    public void checkFixedRotor() {
        Alphabet newAlphabet = new Alphabet();

        Permutation newPermutation = new Permutation("(AELTPHQXRU) (BKNW) "
                + "(CMOY) (DFG) (IV) (JZ) (S)", newAlphabet);
        FixedRotor myRotor = new FixedRotor("I",
                new Permutation("(AELTPHQXRU) (BKNW) "
                        + "(CMOY) (DFG) (IV) (JZ) (S)", newAlphabet));

        assertEquals("Mistakes were made: A",
                4, myRotor.convertForward(0));
        assertEquals("Mistakes were made: A",
                20, myRotor.convertBackward(0));
        assertEquals("The S thing was wrong: fornwards",
                18, myRotor.convertForward(18));
        assertEquals("The S thing was wrong: backwards",
                18, myRotor.convertBackward(18));
        myRotor.advance();
        assertEquals("Mistakes were made A forwards",
                4, myRotor.convertForward(0));
        assertEquals("Mistakes were made A backward",
                20, myRotor.convertBackward(0));
        assertEquals("Mistakes were made W forwards",
                1, myRotor.convertForward(22));
        assertEquals("Mistakes were made W backward",
                13, myRotor.convertBackward(22));
    }

    @Test
    public void testScanners() {
        Alphabet myAlphabet = new Alphabet(_config.nextLine());
        int numRotors = _config.nextInt(), numPawls = _config.nextInt();
        LinkedList<Rotor> allRotors = new LinkedList<>();
        String tempPermutations = "", tempFirstString = _config.next();
        String rotorName = "", rotorNotches = "";
        while (_config.hasNext()) {
            if (tempFirstString.charAt(0) != '(') {
                rotorName = tempFirstString;
                tempFirstString = _config.next();
                rotorNotches = tempFirstString;
                tempFirstString = _config.next();
            } else {
                while (tempFirstString.charAt(0) == '(') {
                    tempPermutations = tempPermutations + tempFirstString;
                    if (_config.hasNext()) {
                        tempFirstString = _config.next();
                    } else {
                        break;
                    }
                }
                if (rotorNotches.charAt(0) == 'M') {
                    allRotors.add(new MovingRotor(rotorName,
                            new Permutation(tempPermutations, myAlphabet),
                            rotorNotches.substring(1)));
                    tempPermutations = "";
                } else if (rotorNotches.charAt(0) == 'N') {
                    allRotors.add(new FixedRotor(rotorName,
                            new Permutation(tempPermutations, myAlphabet)));
                    tempPermutations = "";
                } else if (rotorNotches.charAt(0) == 'R') {
                    allRotors.add(new Reflector(rotorName,
                            new Permutation(tempPermutations, myAlphabet)));
                    tempPermutations = "";
                }
            }
        }
        String[] insertedRotors = new String[numRotors];
        String settingLine = _input.nextLine(), plugboardString = "";
        Scanner settingLineScanner = new Scanner(settingLine);
        settingLineScanner.next();
        for (int i = 0; i < numRotors; i += 1) {
            String tempString = settingLineScanner.next();
            insertedRotors[i] = "Rotor " + tempString;
        }
        String rotorSettings = settingLineScanner.next();
        plugboardString = settingLineScanner.nextLine();
        Machine myM;
        myM = new Machine(myAlphabet, numRotors, numPawls, allRotors);
        myM.insertRotors(insertedRotors); myM.setRotors(rotorSettings);
        myM.setPlugboard(new Permutation(plugboardString, myAlphabet));
        Character[] cListist = new Character[] {'H', 'X', 'I', 'R', 'B', 'A'};
        Character[] cTList = new Character[] {'Q', 'E', 'P', 'T', 'Y', 'A'};
        Permutation tempPerm = new Permutation(plugboardString, myAlphabet);
        for (int i = 0; i < cListist.length; i += 1) {
            Character tempCharPermuted = tempPerm.permute(cListist[i]);
            assertEquals("Character conversion error",
                    cTList[i], tempCharPermuted);
        }
    }

    @Test
    public void testMachine() {
        LinkedList<Rotor> allRotors = new LinkedList<>();

        allRotors.add(movingRotorI);
        allRotors.add(movingRotorII);
        allRotors.add(movingRotorIII);
        allRotors.add(movingRotorIV);
        allRotors.add(movingRotorV);
        allRotors.add(movingRotorVI);
        allRotors.add(movingRotorVII);
        allRotors.add(movingRotorVIII);
        allRotors.add(fixedRotorBeta);
        allRotors.add(fixedRotorGamma);
        allRotors.add(reflectorB);
        allRotors.add(reflectorC);


        Machine myM = new Machine(currentAlphabet, 5, 3, allRotors);
        String[] insertedRotors = new String[] {reflectorB.toString(),
                fixedRotorBeta.toString(), movingRotorIII.toString(),
                movingRotorIV.toString(), movingRotorI.toString()};

        myM.insertRotors(insertedRotors);
        myM.setRotors("AXLE");
        myM.setPlugboard(new Permutation("(YF) (ZH)", currentAlphabet));

        String tempChar = myM.convert("Y");
        assertEquals("The character might be different",
                "Z", tempChar);

        for (int i = 0; i < 11; i += 1) {
            myM.convert("A");
        }
        assertEquals("Machine setting should be correct",
                "AAXLQ", myM.settings());

        myM.convert("A");
        assertEquals("Machine setting should be correct",
                "AAXMR", myM.settings());

        for (int i = 0; i < 597; i += 1) {
            myM.convert("A");
        }
        assertEquals("Machine setting should be correct",
                "AAXIQ", myM.settings());

        myM.convert("A");
        assertEquals("Machine setting should be correct",
                "AAXJR", myM.settings());

        myM.convert("A");
        assertEquals("Machine setting should be correct",
                "AAYKS", myM.settings());
    }


    /** These are the rotors :D */
    static Alphabet currentAlphabet = new Alphabet();
    static MovingRotor movingRotorI = new MovingRotor("I",
            new Permutation("(AELTPHQXRU) (BKNW) (CMOY) "
                    + "(DFG) (IV) (JZ) (S)", currentAlphabet), "Q");
    static MovingRotor movingRotorII = new MovingRotor("II",
            new Permutation("(FIXVYOMW) (CDKLHUP) (ESZ) (BJ) "
                    + "(GR) (NT) (A) (Q)", currentAlphabet), "E");
    static MovingRotor movingRotorIII = new MovingRotor("III",
            new Permutation("(ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)",
                    currentAlphabet), "V");
    static MovingRotor movingRotorIV = new MovingRotor("IV",
            new Permutation("(AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)",
                    currentAlphabet), "J");
    static MovingRotor movingRotorV = new MovingRotor("V",
            new Permutation("(AVOLDRWFIUQ)(BZKSMNHYC) (EGTJPX)",
                    currentAlphabet), "Z");
    static MovingRotor movingRotorVI = new MovingRotor("VI",
            new Permutation("(AJQDVLEOZWIYTS) (CGMNHFUX) (BPRK)",
                    currentAlphabet), "ZM");
    static MovingRotor movingRotorVII = new MovingRotor("VII",
            new Permutation("(ANOUPFRIMBZTLWKSVEGCJYDHXQ)",
                    currentAlphabet), "ZM");
    static MovingRotor movingRotorVIII = new MovingRotor("VIII",
            new Permutation("(AFLSETWUNDHOZVICQ) (BKJ) (GXY) (MPR)",
                    currentAlphabet), "ZM");
    static FixedRotor fixedRotorBeta = new FixedRotor("Beta",
            new Permutation("(ALBEVFCYODJWUGNMQTZSKPR) (HIX)",
                    currentAlphabet));
    static FixedRotor fixedRotorGamma = new FixedRotor("Gamma",
            new Permutation("(AFNIRLBSQWVXGUZDKMTPCOYJHE)", currentAlphabet));
    static Reflector reflectorB = new Reflector("B",
            new Permutation("(AE) (BN) (CK) (DQ) (FU) (GY) "
                    + "(HW) (IJ) (LO) (MP) (RX) (SZ) (TV)", currentAlphabet));
    static Reflector reflectorC = new Reflector("C",
            new Permutation("(AR) (BD) (CO) (EJ) (FN) (GT) "
                    + "(HK) (IV) (LM) (PW) (QZ) (SX) (UY)", currentAlphabet));

    static Scanner _input = new Scanner(""
            + "* B Beta III IV I AXLE (HQ) (EX) (IP) (TR) (BY)"
            + "\n FROM HIS SHOULDER HIAWATHA"
            + "\n TOOK THE CAMERA OF ROSEWOOD"
            + "\n MADE OF SLIDING FOLDING ROSEWOOD"
            + "\n NEATLY PUT IT ALL TOGETHER"
            + "\n IN ITS CASE IT LAY COMPACTLY"
            + "\n FOLDED INTO NEARLY NOTHING"
            + "\n BUT HE OPENED OUT THE HINGES"
            + "\n PUSHED AND PULLED THE JOINTS"
            + "\n    AND HINGES"
            + "\n TILL IT LOOKED ALL SQUARES"
            + "\n    AND OBLONGS"
            + "\n LIKE A COMPLICATED FIGURE"
            + "\n IN THE SECOND BOOK OF EUCLID ");
    static Scanner _config = new Scanner(""
            + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "\n 5 3"
            + "\n I MQ      (AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)"
            + "\n II ME     (FIXVYOMW) (CDKLHUP) (ESZ) (BJ) (GR) (NT) (A) (Q)"
            + "\n III MV    (ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)"
            + "\n IV MJ     (AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)"
            + "\n V MZ      (AVOLDRWFIUQ)(BZKSMNHYC) (EGTJPX)"
            + "\n VI MZM    (AJQDVLEOZWIYTS) (CGMNHFUX) (BPRK)"
            + "\n VII MZM   (ANOUPFRIMBZTLWKSVEGCJYDHXQ)"
            + "\n VIII MZM  (AFLSETWUNDHOZVICQ) (BKJ) (GXY) (MPR)"
            + "\n Beta N    (ALBEVFCYODJWUGNMQTZSKPR) (HIX)"
            + "\n Gamma N   (AFNIRLBSQWVXGUZDKMTPCOYJHE)"
            + "\n B R       (AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP)"
            + "\n           (RX) (SZ) (TV)"
            + "\n C R       (AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW)"
            + "\n           (QZ) (SX) (UY)");
}

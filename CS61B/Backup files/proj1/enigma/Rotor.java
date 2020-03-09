package enigma;

/* Completed? */

import static enigma.EnigmaException.*;

/** Superclass that represents a rotor in the enigma machine.
 *  @author Definitely-Not-Nick
 */
class Rotor {

    /** A rotor named NAME whose permutation is given by PERM. */
    Rotor(String name, Permutation perm) {
        _name = name;
        _permutation = perm;
    }


    /** Return my name. */
    String name() {
        return _name;
    }


    /** Return my alphabet. */
    Alphabet alphabet() {
        return _permutation.alphabet();
    }


    /** Return my permutation. */
    Permutation permutation() {
        return _permutation;
    }


    /** Return the size of my alphabet. */
    int size() {
        return _permutation.size();
    }


    /** Return true iff I have a ratchet and can move. */
    boolean rotates() {
        return false;
    }


    /** Return true iff I reflect. */
    boolean reflecting() {
        return false;
    }


    /** Return my current setting. */
    int setting() {
        return _setting;
    }


    /** Set setting() to POSN.  */
    void set(int posn) {
        while (posn < 0) {
            posn += alphabet().size();
        }
        posn = posn % alphabet().size();
        _setting = posn;
    }


    /** Set setting() to character CPOSN. */
    void set(char cposn) {
        _setting = alphabet().toInt(cposn);
    }


    /** Return the conversion of P (an integer in the range 0..size()-1)
     *  according to my permutation. */
    int convertForward(int p) {
        int tempInt = permutation().wrap(p + _setting);
        tempInt = permutation().permute(tempInt);
        tempInt = permutation().wrap(tempInt - _setting);
        return tempInt;
    }


    /** Return the conversion of E (an integer in the range 0..size()-1)
     *  according to the inverse of my permutation. */
    int convertBackward(int e) {
        int tempInt = permutation().wrap(e + _setting);
        tempInt = permutation().invert(tempInt);
        tempInt = permutation().wrap(tempInt - setting());
        return tempInt;
    }


    /** Returns true iff I am positioned to allow the rotor to my left
     *  to advance. */
    boolean atNotch() {
        return false;
    }


    /** Advance me one position, if possible. By default, does nothing. */
    void advance() {
    }


    @Override
    public String toString() {
        return "Rotor " + _name;
    }

    /**Get method for _setting.
     * @return it returns the integer representing the current setting
     */
    int getSetting() {
        return _setting;
    }

    /** get metho for _name.
     * @return the name of the rotor
     */

    /** My name. */
    private final String _name;
    /** The permutation implemented by this rotor in its 0 position. */
    private Permutation _permutation;
    /** the integer representing the current setting. */
    private int _setting;

}

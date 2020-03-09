package enigma;

/* Completed? */

import static enigma.EnigmaException.*;

/** Represents a permutation of a range of integers starting at 0 corresponding
 *  to the characters of an alphabet.
 *  @author Definitely-Not-Nick
 */
class Permutation {

    /** Set this Permutation to that specified by CYCLES, a string in the
     *  form "(cccc) (cc) ..." where the c's are characters in ALPHABET, which
     *  is interpreted as a permutation in cycle notation.  Characters in the
     *  alphabet that are not included in any cycle map to themselves.
     *  Whitespace is ignored. */
    Permutation(String cycles, Alphabet alphabet) {
        _alphabet = alphabet;
        _myCycles = cycles;
    }


    /** Add the cycle c0->c1->...->cm->c0 to the permutation, where CYCLE is
     *  c0c1...cm. */
    private void addCycle(String cycle) {
        _myCycles = _myCycles + "(" + cycle + ")";
    }


    /** Return the value of P modulo the size of this permutation. */
    final int wrap(int p) {
        int r = p % size();
        if (r < 0) {
            r += size();
        }
        return r;
    }


    /** Returns the size of the alphabet I permute. */
    int size() {
        return _alphabet.size();
    }


    /** Return the result of applying this permutation to P modulo the
     *  alphabet size. */
    int permute(int p) {
        return alphabet().toInt(permute(alphabet().toChar(p)));
    }


    /** Return the result of applying the inverse of this permutation
     *  to C modulo the alphabet size. */
    int invert(int c) {
        return alphabet().toInt(invert(alphabet().toChar(c)));
    }


    /** Return the result of applying this permutation to the index of P
     *  in ALPHABET, and converting the result to a character of ALPHABET. */
    char permute(char p) {
        int tempIndex = 0;
        if (!(_myCycles.contains(String.valueOf(p)))) {
            return p;
        }
        for (int i = 0; i < _myCycles.length(); i += 1) {
            if (_myCycles.charAt(i) == '(') {
                tempIndex = i + 1;
            } else if (!((_myCycles.charAt(i) == ')')
                    || (_myCycles.charAt(i) == ' '))) {
                if (_myCycles.charAt(i) == p) {
                    if (_myCycles.charAt(i + 1) != ')') {
                        return _myCycles.charAt(i + 1);
                    } else {
                        return _myCycles.charAt(tempIndex);
                    }
                }
            }
        }
        return '?';
    }


    /** Return the result of applying the inverse of this permutation to C. */
    char invert(char c) {
        if (!(_myCycles.contains(String.valueOf(c)))) {
            return c;
        }
        for (int i = 0; i < _myCycles.length(); i += 1) {
            if (_myCycles.charAt(i) == c) {
                if (_myCycles.charAt(i - 1) == '(') {
                    int tempInt = i;
                    while (_myCycles.charAt(tempInt + 1) != ')') {
                        tempInt += 1;
                    }
                    return _myCycles.charAt(tempInt);
                } else {
                    return _myCycles.charAt(i - 1);
                }
            }
        }
        return '?';
    }


    /** Return the alphabet used to initialize this Permutation. */
    Alphabet alphabet() {
        return _alphabet;
    }


    /** Return true iff this permutation is a derangement (i.e., a
     *  permutation for which no value maps to itself). */
    boolean derangement() {
        for (int i = 1; i < _myCycles.length() - 1; i += 1) {
            if ((_myCycles.charAt(i - 1) == '(')
                && _myCycles.charAt(i + 1) == ')') {
                return true;
            }
        }
        return false;
    }

    /** get method for private variable _myCycles.
     * @return String of _myCycles
     */
    String getMyCycles() {
        return _myCycles;
    }



    /** Alphabet of this permutation. */
    private Alphabet _alphabet;
    /** it be a string... myCycles be a string representing the cycles.*/
    private String _myCycles;

}

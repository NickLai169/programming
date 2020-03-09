package enigma;

import java.util.Collection;

import static enigma.EnigmaException.*;

/** Class that represents a complete enigma machine.
 *  @author Defininitely-Not-Nick
 */
class Machine {

    /** A new Enigma machine with alphabet ALPHA, 1 < NUMROTORS rotor slots,
     *  and 0 <= PAWLS < NUMROTORS pawls.  ALLROTORS contains all the
     *  available rotors. */
    Machine(Alphabet alpha, int numRotors, int pawls,
            Collection<Rotor> allRotors) {
        _alphabet = alpha;
        _numRotors = numRotors;
        _numPawls = pawls;
        _myRotors = new Rotor[_numRotors];
        _allRotors = allRotors;
        _plugboard = new Permutation("", _alphabet);
    }

    /** Return the number of rotor slots I have. */
    int numRotors() {
        return _numRotors;
    }

    /** Return the number pawls (and thus rotating rotors) I have. */
    int numPawls() {
        return _numPawls;
    }

    /** Set my rotor slots to the rotors named ROTORS from my set of
     *  available rotors (ROTORS[0] names the reflector).
     *  Initially, all rotors are set at their 0 setting. */
    void insertRotors(String[] rotors) {
        for (int i = 0; i < rotors.length; i += 1) {
            for (Rotor r: _allRotors) {
                if (("Rotor " + r.name()).equals(rotors[i])) {
                    _myRotors[i] = r;
                    _myRotors[i].set(0);
                }
            }
        }
    }

    /** Set my rotors according to SETTING, which must be a string of
     *  numRotors()-1 characters in my alphabet. The first letter refers
     *  to the leftmost rotor setting (not counting the reflector).  */
    void setRotors(String setting) {
        for (int i = setting.length() - 1; i > 0; i -= 1) {
            _myRotors[i + 1].set(setting.charAt(i));
        }
    }

    /** Set the plugboard to PLUGBOARD. */
    void setPlugboard(Permutation plugboard) {
        _plugboard = plugboard;
    }

    /** Returns the result of converting the input character C (as an
     *  index in the range 0..alphabet size - 1), after first advancing
     *  the machine. */
    int convert(int c) {
        boolean didRightStep = true;
        boolean rightAtNotch = _myRotors[_myRotors.length - 1].atNotch();
        _myRotors[_myRotors.length - 1].advance();
        for (int i = _myRotors.length - 2;
             i >= _myRotors.length - 1 - _numPawls; i -= 1) {
            if ((didRightStep && rightAtNotch)
                    || (didRightStep && _myRotors[i].atNotch())) {

                didRightStep = true;
                rightAtNotch = _myRotors[i].atNotch();
                _myRotors[i].advance();
            } else {
                didRightStep = false;
                rightAtNotch = _myRotors[i].atNotch();
            }
        }


        int charInt = _plugboard.permute(_plugboard.wrap(c));
        for (int i = _myRotors.length - 1; i >= 0; i -= 1) {
            charInt = _myRotors[i].convertForward(charInt);
        }

        for (int i = 1; i < _myRotors.length; i += 1) {
            charInt = _myRotors[i].convertBackward(charInt);
        }

        charInt = _plugboard.permute(charInt);

        return charInt;
    }

    /** Returns the encoding/decoding of MSG, updating the state of
     *  the rotors accordingly. */
    String convert(String msg) {
        String convertedMessage = "";
        for (int i = 0; i < msg.length(); i += 1) {
            Character theChar = msg.charAt(i);
            int theInt = _alphabet.toInt(theChar);
            convertedMessage = convertedMessage
                    + _alphabet.toChar(convert(theInt));
        }
        return convertedMessage;
    }

    /** The method that returns a string representing the current settings of
     * each rotor from left to right.
     * @return the string representing the settings of the rotors in the machine
     */
    String settings() {
        String settingString = "";
        for (Rotor r: _myRotors) {
            settingString = settingString + alphabet().toChar(r.setting());
        }
        return settingString;
    }

    /**get method for the _alphabet.
     * @return the alphabet of this machine
     */
    Alphabet alphabet() {
        return _alphabet;
    }

    /**get method for myRotors.
     * @return the RotorArray of the rotors of this machine
     */
    Rotor[] myRotors() {
        return _myRotors;
    }

    /**get method for the plugboard.
     * @return the Permutation representing the plugboard
     */
    Permutation plugboard() {
        return _plugboard;
    }

    /**get method for the collection of all available rotors.
     * @return the Collection of rotors
     */
    Collection<Rotor> allRotors() {
        return _allRotors;
    }

    /** Common alphabet of my rotors. */
    private final Alphabet _alphabet;
    /** The number of rotor/rotor slots in the machine.*/
    private int _numRotors;
    /** The number of pawls/moving rotors in the machine.*/
    private int _numPawls;
    /** The RotorArray of the current rotors in the machine.*/
    private Rotor[] _myRotors;
    /** The permutation instance representing the plugboard.*/
    private Permutation _plugboard;
    /** The collection of all possible rotors for the machine.*/
    private Collection<Rotor> _allRotors;
}

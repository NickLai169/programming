package enigma;

/*  Completed? */

import static enigma.EnigmaException.*;

/** Class that represents a rotating rotor in the enigma machine.
 *  @author Defintiely-Not-Nick
 */
class MovingRotor extends Rotor {

    /** A rotor named NAME whose permutation in its default setting is
     *  PERM, and whose notches are at the positions indicated in NOTCHES.
     *  The Rotor is initally in its 0 setting (first character of its
     *  alphabet).
     */
    MovingRotor(String name, Permutation perm, String notches) {
        super(name, perm);
        set(0);
        _notches = notches;
    }

    @Override
    void advance() {
        set(setting() + 1);
    }

    /** tells us whether the current rotor rotatos.
     * @return a Boolean representing whether the current rotor rotates
     */
    boolean rotates() {
        return true;
    }

    /** tells us whether the current rotor is a reflector.
     * @return a Boolean representing whether the current rotor is a reflector
     */
    boolean reflecting() {
        return false;
    }

    /** tells us whether the rotor is currently at the notch.
     * @return a Boolean representing whether the rotor is currently at a notch
     */
    boolean atNotch() {
        for (int i = 0; i < _notches.length(); i += 1) {
            if (setting() == alphabet().toInt(_notches.charAt(i))) {
                return true;
            }
        }
        return false;
    }

    /** the get method for _notches.
     * @return a String representing the notche(s) of the rotor
     */
    String notches() {
        return _notches;
    }

    /** a String representing the notche(s) of the rotor.*/
    private String _notches;
}

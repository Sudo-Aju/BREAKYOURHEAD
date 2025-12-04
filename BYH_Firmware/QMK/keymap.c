#include QMK_KEYBOARD_H
#include <stdio.h>

enum layers {
    _EDIT = 0,
    _COLOR
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_EDIT] = LAYOUT(
        KC_C,    KC_DEL,  KC_X,
        KC_SPC,  KC_Z,    KC_Y
    ),

    [_COLOR] = LAYOUT(
        KC_MUTE, KC_VOLD, KC_VOLU,
        KC_MPRV, KC_MPLY, KC_MNXT
    )
};

#if defined(ENCODER_ENABLE)
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_RGHT);
        } else {
            tap_code(KC_LEFT);
        }
    } else if (index == 1) {
        if (clockwise) {
            tap_code16(A(KC_PPLS)); 
        } else {
            tap_code16(A(KC_PMNS));
        }
    }
    return false;
}
#endif

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_P(PSTR("BYH\n"), false);
    
    switch (get_highest_layer(layer_state)) {
        case _EDIT:
            oled_write_P(PSTR("Mode: EDIT\n"), false);
            oled_write_P(PSTR("> Scrub/Cut"), false);
            break;
        case _COLOR:
            oled_write_P(PSTR("Mode: COLOR\n"), false);
            oled_write_P(PSTR("> Audio/Grade"), false);
            break;
        default:
            oled_write_P(PSTR("Mode: UNDEF\n"), false);
    }
    return false;
}
#endif
<div align="center">
  <h1>BREAKYOURHEAD Pad</h1>
  <p>
    <strong>A custom 6-key macro pad with dual rotary encoders and OLED support.</strong>
  </p>
  
  <img src="https://via.placeholder.com/600x300?text=BREAKYOURHEAD+Pad" alt="BREAKYOURHEAD Pad Prototype" width="600">

  <br><br>

  <a href="#bom">
    <img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge" alt="Status">
  </a>
  <a href="#firmware">
    <img src="https://img.shields.io/badge/Firmware-QMK-blue?style=for-the-badge" alt="QMK Firmware">
  </a>
</div>

<hr>

## 📖 About
The **BREAKYOURHEAD Pad** is a compact input device designed for efficiency. Whether you are video editing, coding, or gaming, this pad offers 6 programmable keys and 2 rotary encoders for precise control, topped off with an OLED screen for layer information and status updates.

## 🛠️ Bill of Materials (BOM)

This project requires the following components. 

<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">Part Name</th>
        <th align="center">Quantity</th>
        <th align="center">Specifications</th>
        <th align="center">Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td align="left"><strong>PCB</strong></td>
        <td align="center">1</td>
        <td align="left">Custom BreakYourHead PCB</td>
        <td align="left">Main logic board</td>
      </tr>
      <tr>
        <td align="left"><strong>Switches</strong></td>
        <td align="center">6</td>
        <td align="left">Cherry MX Style</td>
        <td align="left">Linear, Tactile, or Clicky</td>
      </tr>
      <tr>
        <td align="left"><strong>Rotary Encoders</strong></td>
        <td align="center">2</td>
        <td align="left">EC11</td>
        <td align="left">Includes push-button functionality</td>
      </tr>
      <tr>
        <td align="left"><strong>Diodes</strong></td>
        <td align="center">6</td>
        <td align="left">1N4148 (Through-hole)</td>
        <td align="left">Required for anti-ghosting matrix</td>
      </tr>
      <tr>
        <td align="left"><strong>Display</strong></td>
        <td align="center">1</td>
        <td align="left">0.91" OLED</td>
        <td align="left">128x32 resolution, I2C</td>
      </tr>
    </tbody>
  </table>
</div>

### ⚠️ Additional Requirements (Not in BOM)
* **Keycaps:** 6x 1u keycaps.
* **Knobs:** 2x Knobs for EC11 encoders.
* **Microcontroller:** (If not integrated on PCB) Pro Micro, Elite-C, or RP2040.
* **Case:** 3D printed case or acrylic sandwich plate.

---

## ✨ Features
* **6 Programmable Keys:** Full layout customization.
* **Dual Encoders:** Perfect for volume control, scrubbing timelines, or scrolling history.
* **OLED Screen:** Display WPM, current layer, or custom animations (Bongo Cat!).
* **QMK/VIA Compatible:** Easily remap keys without flashing code.

---

## 🔌 Build Guide

1.  **Diodes:** Solder the 1N4148 diodes. Ensure the black band faces the square pad (cathode).
2.  **Sockets/Switches:** Install switch sockets or solder switches directly.
3.  **Encoders:** Solder the EC11 encoders into position.
4.  **Display:** Solder the 4-pin OLED header (be careful with the glass screen).
5.  **Assembly:** Mount the PCB to the case/plate.

---

## 💻 Firmware

To flash this board, ensure you have the [QMK Toolbox](https://github.com/qmk/qmk_toolbox) installed.

```bash
qmk compile -kb breakyourhead -km default

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BREAKYOURHEAD Pad</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      color: #24292e;
      background-color: #ffffff;
    }
    
    h1 {
      border-bottom: 1px solid #eaecef;
      padding-bottom: 0.3em;
      margin-bottom: 16px;
    }

    h2 {
      margin-top: 24px;
      margin-bottom: 16px;
      font-weight: 600;
      line-height: 1.25;
      border-bottom: 1px solid #eaecef;
      padding-bottom: 0.3em;
    }

    p {
      margin-bottom: 16px;
    }

    .header-container {
      text-align: center;
      margin-bottom: 30px;
    }

    .status-badge {
      margin-top: 10px;
      display: inline-block;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 16px;
    }

    th, td {
      padding: 6px 13px;
      border: 1px solid #dfe2e5;
    }

    th {
      background-color: #f6f8fa;
      font-weight: 600;
    }

    tr:nth-child(2n) {
      background-color: #f6f8fa;
    }

    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      margin-top: 20px;
    }

    .gallery img {
      width: 45%;
      max-width: 350px;
      border-radius: 6px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.12);
      transition: transform 0.2s;
    }

    .gallery img:hover {
      transform: scale(1.02);
    }

    hr {
      height: 0.25em;
      padding: 0;
      margin: 24px 0;
      background-color: #e1e4e8;
      border: 0;
    }
  </style>
</head>
<body>

  <div class="header-container">
    <h1>BREAKYOURHEAD Pad</h1>
    <p><strong>A custom 6-key macro pad with dual rotary encoders and OLED support.</strong></p>
    
    <a href="#bom" class="status-badge">
      <img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge" alt="Status">
    </a>
  </div>

  <hr>

  <h2 id="bom">🛠️ Bill of Materials (BOM)</h2>

  <div style="overflow-x: auto;">
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
          <td align="left"><strong>Microcontroller</strong></td>
          <td align="center">1</td>
          <td align="left">Seeed Studio XIAO RP2040</td>
          <td align="left">Main logic board</td>
        </tr>
        <tr>
          <td align="left"><strong>Display</strong></td>
          <td align="center">1</td>
          <td align="left">0.91in OLED Module</td>
          <td align="left">I2C Interface</td>
        </tr>
        <tr>
          <td align="left"><strong>Rotary Encoders</strong></td>
          <td align="center">2</td>
          <td align="left">EC11 v2</td>
          <td align="left">With push-button</td>
        </tr>
        <tr>
          <td align="left"><strong>Switches</strong></td>
          <td align="center">6</td>
          <td align="left">Cherry MX Switch Base v2</td>
          <td align="left">Mechanical Keys</td>
        </tr>
        <tr>
          <td align="left"><strong>Keycaps</strong></td>
          <td align="center">6</td>
          <td align="left">DSA 1u v2</td>
          <td align="left">Low profile profile</td>
        </tr>
        <tr>
          <td align="left"><strong>Inserts</strong></td>
          <td align="center">5</td>
          <td align="left">M3 Threaded Insert v3</td>
          <td align="left">Heat-set for Case</td>
        </tr>
        <tr>
          <td align="left"><strong>Screws (Short)</strong></td>
          <td align="center">2</td>
          <td align="left">M3x12 SHCS v1</td>
          <td align="left">Socket Head Cap Screw</td>
        </tr>
        <tr>
          <td align="left"><strong>Screws (Long)</strong></td>
          <td align="center">3</td>
          <td align="left">M3x16 SHCS v5</td>
          <td align="left">Socket Head Cap Screw</td>
        </tr>
        <tr>
          <td align="left"><strong>PCB</strong></td>
          <td align="center">1</td>
          <td align="left">Custom BYH PCB</td>
          <td align="left">FR4</td>
        </tr>
        <tr>
          <td align="left"><strong>Diodes</strong></td>
          <td align="center">6</td>
          <td align="left">1N4148</td>
          <td align="left">Through-hole</td>
        </tr>
      </tbody>
    </table>
  </div>

  <br>

  <h2>📷 Gallery</h2>

  <div class="gallery">
    <img src="images/img1.png" alt="Image 1 Description">
    <img src="images/img2.png" alt="Image 2 Description">
    <img src="images/img3.png" alt="Image 3 Description">
    <img src="images/img4.png" alt="Image 4 Description">
  </div>

</body>
</html>

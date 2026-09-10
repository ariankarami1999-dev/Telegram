<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/ijt8Md8on8Q18D4zjD70nnYTBCT3TLzuJhKB8uq4sAdrSlUud4LcRPZZCNBvVv5bklyru6EiMXnuIiPcbWqDkIjURsTmGxaF-MqCRC4Zu6wVJwTZmSQWMUW8-AK2vaE7U3xULs5MtFO8ZJW9jemgwHf4YF9n3wYu7QeraJ33vY19jbmk_bfN-7pIfmNRtYXLstWJrA7ZUc_rjxnRNBxpBAVdo7mvN8v0UPldqEftlc7ayKyeMlXpJ1iU3iQE3Vry-FOEPRls5-I0FHAh6Ymc9Xu5Y-A3_DMLedozNWblYOv6VY-i9TQ1khu5_GneA_kzeXlFaj3WXdmvcCm8DLqgDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-83243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه آدم خوب متشخص و جنتلمن بیاد یه کانفیگ لوکیشن کانادا بده به من
@mc_menot</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/funhiphop/83243" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم پیمانشون اینطوری بود که دعای خیر بکنن برا هم</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/83242" target="_blank">📅 14:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم پیمانشون اینطوری بود که دعای خیر بکنن برا هم</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/83241" target="_blank">📅 14:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=M8RiQe9Llku0V4sl82P6qlR6KxVixVUN-k5D3i0b_-W5KvmBsTWHL8LFQG9JriYGj46GKM4MY_GOtAchvuLhscYzPvRFegdNXF_V4XmJ_M1gf78rLEBbDxhQWSLH7EXQ3jt4qqqrBEgZksOaQODD2dNINre-8VPUUck6tay2GsLSD7Q4lKkpLczJdJ6ZO333myZj5OKU3Tz7rVSw2q7YbSGEaHWMLXSASp6bs__DJRKu_nWvOsSURE-xA8qILSva9VyiIBw0eWRtXFnDgyUX_dPbhmpcTQ9jBiC5ySjmbHFzyjLcdlwcFWtaYFPfz54K8eIwN9O1Fyfs1zQ3BrBh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=M8RiQe9Llku0V4sl82P6qlR6KxVixVUN-k5D3i0b_-W5KvmBsTWHL8LFQG9JriYGj46GKM4MY_GOtAchvuLhscYzPvRFegdNXF_V4XmJ_M1gf78rLEBbDxhQWSLH7EXQ3jt4qqqrBEgZksOaQODD2dNINre-8VPUUck6tay2GsLSD7Q4lKkpLczJdJ6ZO333myZj5OKU3Tz7rVSw2q7YbSGEaHWMLXSASp6bs__DJRKu_nWvOsSURE-xA8qILSva9VyiIBw0eWRtXFnDgyUX_dPbhmpcTQ9jBiC5ySjmbHFzyjLcdlwcFWtaYFPfz54K8eIwN9O1Fyfs1zQ3BrBh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl4eHbES-4IXGkM0mLy6ws4H9ijsWZ6aKEHc0JgqNtFyeGWa-5sydC2SXM0zT9ZwcmwoyCoae4nTkcqhd442gEB15oZBU0Xj6hBK6bWAMLC-Rs0JxfT-KTQeXFQ1Gu3hXK3JLNnMQRNZ4PprJte_lbcmSoMtsMGXUqW1Tw6-OPKhNYV1jCsP4qbCAyRpJ7XG2lbgXl82RnfwxAqQsPOOKr_NE7su9Yvr_bPU3-VCYtHuMoce-qoW-NPcZ2T8jAsR0HDV3tzzJLzpkkRulyMSAXWqbCEzCzvqwGa7hJ64Q7bZlkagrwPKs6l-SRR_30k1RYti5JscvODYYy0Tqnzayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1Asw8vYB5-QsFZbj3cuRiMoGzQVrAnO96-PK4oCoh_cWNNoxVDTkPfnz3x_lj0Bq0jiQFvZq9GT68dMrTpzDZyYVtoSFhzvOXUDWtw_QajEKRaaoAhypuSLWUbcdiIYKUch9gPci35UMxolA6910fRgjROEAr0aKX9ZG0vZqfCxvh2GmcQF_Ff7WDVzExhCGLlGVa-GGl9mgFn3-qKp_LURPL4kRfdbvQhdLRFXpXFt13zt7bSsOe56ZsDxaap5hfJ5ngmBgawZojzwwq3YbOqki157-Z2Z9QRLp467K0W5glX3O2sc-oJG1JhQYI9gZ8DlXAKj8-3Q6uPfAnfXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfiitZvO48q3t2rpKelRGTqOQ_H_km5MFe0eskMKHLTYY_3srOvI6pB4_RpgaDeA_FXKpBgS1gLEU-7zMlqlgFWgPLw3R9N8Oqjg50VQ1Q6RZyj8tiVy2buBpr0OGxYwXcM7ZzHi0AjpwIBIAdTnXcyDSWTl-3cyjqLDBCn5dRJs0KY5r4yPtNKiMq3H3BBhZja2VDJf9dbBN9rGQrYuJWOhTib1bXOQbTNxiFBgyb9KG_0ZbtuRHFnr_tkeA8gjl3ry2ck6oeDMaJpwiFk4NYUMoi9ouT1KpOhbXTKjZcboMg7T3PsvsH6xc_lx9xeq3vj_gy_Dz_eNzzoI1muftA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnI94se78g46my0gqxYLLxodGPCNFN8fV60S-NTBmg5eSDsjl88br_WV_MtYvdBa9C1010KrcDx6wTgF1V4-Pssv7AEu04Imz6T1_ute6PLAUTYwwXsN0g8zhV4zX0Oa_JPpMcjyNvPE7KwLhh3ZstNq-LOLeB4Q6G2QJ7LsIAZtlrtx46xM0cMI9SooK1kHYcLo3u7U9zEKMoLyEoaEu_1jje5ViWy0K4wieNM0FSQ-cQmfzG4YJMwGtwRlEJ1jJmg-fjYWiFuXyhBG-uf9mwC2gcqeY72PTLhNPktXydJ2FujHvXHNbYAtqG3J5VtEYrKkitz9FQgT74n6oBcw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoQzYd38-Syg85ROJLG609iU4IEuFOCpssLp42sExqCM4wdfXWlvUto6tNrLUv0gxezom2vlVUD0ErA2qt6JzXIzHfRHhazDAkXCh6-hqZgdqLA0nC3QcPAuWAO-MyOsjs5wxV_VsQ2Jgp28qrF0ba7F03QUEt3LWUZFZs5ocYs1GRXR2foiH5f8qU-c8Tzp01hm8SMb68eDnGUBQkf-8ffzPsIbwhRMZDF5vYywp3ZI2lvz1dJiOn54I3IqTPvRFF5UkuWlMKDplP_0zvTwdcmsexEDcnh1OOF3KG2SwpGx8jtwGUXPVECEhQruPWF04CBp8J0jTN148rXLLO8gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1nTzE9YedfMMvlCRdiapRsnwtlNTvtHGvyJcGstzupEbVE47CC5WirLTr75RqLgSWuvKBUTFDSERO3xQKXIgXt5f_OC-AE_QSd8SFo3-J50yYGtFgHbEa8Sy7wxGKtNkVVc3xTJlY93sq-K9vx51mktS5RBODztOFnlzykLpWiLDJgKTvIJsrLjII1GRlyh-cHuhiLMJsHGsOZ5As1zrwuzOKbVg2U75Lv-EdPh2cTBtBkY6phug2iCZZw4msJorBX1UsbeHw5wJKCMuY5OnTvlzoneX47mTkcbF43S9yIRrU4YlSdmQqfoSQCR_a-dHAFzvGoxg2HaHh10UyjOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ea0nAzRhJRbWidBVaOJ-gliincMH1yM4WM570vDX1qvZRPEKt6rwYXxXZkk0RzKegrfupftC6qDRYbCbVUFTbY7xxBMVhiedghT-GXPzFnnMf-xGwoVlVJAl_UXBGGaQ_uHGEXyNZEuzWD2qiZUjBNXHYP4r22W96xBDdIqtVPCGKNkTtPUw4XTQY8b1xpYaO4CS9o9EepBpTLQD79jHOuksnC-jzQy8l9TH-rdd0M-e6TbagDhu-U5djpn1XAigJRqZR_zUSt7f1g65G7HnAFZPdDdw4-dONVUUd-FcWGM67foRrp_3VUo8ZLA153g6pSkm9YXxiJ0oIfNpR9P3dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYkvA4mfl-0G_wYutCJYu_fP_J7JeslVRpFPFLWfPFE7eMZ3D1nrEv-XpzzpnXmxE1ukPmwu1Z5fFuASiQ39lFZowJdnD28OqxNaUJzPpKn8nrahU-PpxFyDc2UFlF6TCXU-RCzNd9ljdhw5EaZpJRaJdRSWRfxxKL86p7hhU85qM7r35H9z6patQWTT64hPsOvdCxaW3ptfvqzOKePfg-T2Dz6K_iusWtr1cpiqK98tLqePlw-lqXV3TBnc2zdXckez8ofRVabTHgT5Q1WJTmx4DdbrXV4FvOjgvPukIH3S9JoWFySuWsLennmRPZ3OUmlyb0c588NCZjqim8UMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-4-zBuMtxFm_OkeqxrFx3jkKlRMstMdx1Q6UclDm_rT4BkNZHfiL8j--zHKSZu8mvQpOkJADZxmnVI8JY4C5ipkup62xwL5UMD1uGpQ4CiJP7sXrI9fJfWahoOZFndwVYwts-lc1dp9uBk9gxfOrZGdWHxYviHcdLIgf3D2y7AW8NtX7M4dQaLkpJBevu5B-DRxbGcTJlBSHCEFAYy42caGH5RoKSpY2tpTrzKuAMXNrm51RnaHd_hTOvRdf0bckFBr9FbDpiXhNctoIvJ9vyafOiP2On3m1ujfk-CRUCU52FkkImygHq1HZqkZOIGddkR6wdu4YqP_0u-poFHiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GegdaabLeDFp_nQE8D9b0EW-qor--KgCsIlVqfQibmufTT0g3-sMzn9c4pdQqFqggP5SElqIZKhrzOBzhKldYhftQ-jSH9L9RNRDGXwuggiNeooF3bs5XjxPjHoe7zcHfe_BwwXEh71P0UV55dq3DjTL5RRju6cmo2d3mHBOHQQGO2P4c7X4v_9UOQnHSBYy35PSZaLgBBqKKvNIs7ZFLjA9B46b1J70Au-1LbyHqHGCPe_af1mkLzPsuVxwVxbnUr-WwMxZFsQP3fk4eHdrsnSwu1zm3ufpvA_ZAyg3UG8WJ0bPM4JmRSAoiDSFAcehzzbmJcTZjeA2ELPOt7LYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
19r
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83222" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGL13alN9WwojDm8aSj8GB1IRMeY3np-icinCY8f_TBQ85hv6GuUOCkGrKPX6XzAjiJlbfdfHdbkMMG4LcPEdHg-An-KI3MhTCiWQOlzekwYZW9kdQS544_BTnvFbWwVRobdSrwnam0cHWVmf5xR_JfkG6LVzRsXJGY84ijjr40HGUShd9IyCkT7lMZh7EufyrFSOhPZ4EeaztFjQHcO0v0BDZfYxy4A5qu9FQmXzpwmERsa0MDcpsKLZssrtI6e_3xDtcgslV83ql09e-CTnw7KMsZ_vq82w0UCvm3og3yIhccxMoi-dENXFmZHylSCpggwCcjNWdMJPEwsGUnMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=l4059wRbSM_ouOLpPgzHRBhs0sPtSJJk6fDF_mh9G9sVf3Swr2rIgNSj57Aq0BH_xT65cZ3G115B1n_igQ4Mchsrawnxwsm-CzLvDE11VNnAOca2xkIA4gByFMwk2vTYyeHhnB5IXTpudGIZRuBUF2Av8A4vOK1EDRnac6IY2_BBtyLYDgbaODEjY7NidEYNGH0-5VjF2MULhWrjdfrymZrKBqUuutbZZ3sS3L8Fm-oIEixRXEbcvqv8vnjLKugZ7URnV1CWgKup0ozr4X_l4kaMwvpoNG9NlKaYEhit9CZuabtjmFgz31o4-_9NY9U7pZ2oHoGQyVaZLae52q4R5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=l4059wRbSM_ouOLpPgzHRBhs0sPtSJJk6fDF_mh9G9sVf3Swr2rIgNSj57Aq0BH_xT65cZ3G115B1n_igQ4Mchsrawnxwsm-CzLvDE11VNnAOca2xkIA4gByFMwk2vTYyeHhnB5IXTpudGIZRuBUF2Av8A4vOK1EDRnac6IY2_BBtyLYDgbaODEjY7NidEYNGH0-5VjF2MULhWrjdfrymZrKBqUuutbZZ3sS3L8Fm-oIEixRXEbcvqv8vnjLKugZ7URnV1CWgKup0ozr4X_l4kaMwvpoNG9NlKaYEhit9CZuabtjmFgz31o4-_9NY9U7pZ2oHoGQyVaZLae52q4R5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=EpmaxEDJ2-JrBDVQjcTp7VwmwU5CO5vfoA00Y1ygE4CceGE6ASFxpNATgkEW7Q_LX147YWVAO8x3SdErsQe0oxsXp3qxec-oGZ0KhgW6J-hVAz1TCbrxXSSW1dlSxvzQfdxL0MEw5MjR7yPrh3TjYqkbDHIl3EjQX57jq817Ss7cFlDQAyCL-sCJqqT1NeIxK5wxFNGv_NB81xejhBKLHLRA-uGH8q1fImgcMLf7-a_uF7tic1P1tF3AAcCzF_rQmlfdkqO0m8enaPyrDUHZMuX7JhvByCSOkE0o6yFi0SQRJiFwssqsjwzn9j64BMDMCjPXBu-Y6g__8BW-Mmjuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=EpmaxEDJ2-JrBDVQjcTp7VwmwU5CO5vfoA00Y1ygE4CceGE6ASFxpNATgkEW7Q_LX147YWVAO8x3SdErsQe0oxsXp3qxec-oGZ0KhgW6J-hVAz1TCbrxXSSW1dlSxvzQfdxL0MEw5MjR7yPrh3TjYqkbDHIl3EjQX57jq817Ss7cFlDQAyCL-sCJqqT1NeIxK5wxFNGv_NB81xejhBKLHLRA-uGH8q1fImgcMLf7-a_uF7tic1P1tF3AAcCzF_rQmlfdkqO0m8enaPyrDUHZMuX7JhvByCSOkE0o6yFi0SQRJiFwssqsjwzn9j64BMDMCjPXBu-Y6g__8BW-Mmjuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnmJ1UX7y77fteeDhzwx-T-0eCI3KkD3tw6wrwIhBqp4adZRfeB5i6kWghYHZXxgPngf--pGV-2o2b72qbgK1v9CQIXqtxPWXaTBAO7uP6JJoDT7HKKzVNg1Wz1lJMcYug_xwS3zsiiqQg4PB3t0pI6GZPI2JbeYRqfICcv7QnUMecyDMRLXgAW8mU8ZfaTfnO8CUbwI4lKMv5NnfeKRYzaigyXIV4x8KjEonni2j11vRvfo4LsEkUpiynX0eTXioLS0yVxWYXbrjQnOtU31vfcbYMdnD4BrKxQe9x1hp4jAQxLMT09GLzH_rNAV5LWnadrFx6fXvuLJe5VStG9_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDfnQPRUdVyk-riT9gHgcEwHfcQ3v5wNq--3By8MGhBSTBjgGl5dtgxjY3BQxaU-lbr1YQctjPI8wu8W4f0pp0kbidvda3b_x7W3QHUeol0milph-7Xs5TwBpDVMDr2dxFB1uv6wGc9Xe9TTCXYtWoMHHQ31ljTGgJ1ubQQauRVeVYjoMuOF3kZfyLXf2mixVK5J5uEBGSoKeqNtFP1YQ2hXsvVDxzc9vYLCfpX-tG7QdZJbF7Yw3_iqeYA7XZKqeneq6yzPj8WePz7BGjiBcLNpIZd8z3vjkSSeKo2VBoBWAMoM6c-IPfKCxg6GgOcLioYd0J9J5E3WlekUJt0s3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuxqLug3ZueqqtuR0K9oFxdeRw-8NxVfPgQhtc1TPCWteWCMdnwD-_hW0hEK9fPm64z7X2CkP_bfTJYY7sI5t621nZas1qzLO3i7hiP08tWlFNtcedVoPixwALF2B17SsD42_BmFz7D06tSbM1AlTKwXV6LLjGuilrEGFT34Y_DFIOVhufcmFUQ3U7uXNUYpQZ9ioPQMkmD0PavFIHvJ07SSl2VQcZt-Pxx7R1d_g9RG0gR_56wP7UqDoX4tm0kg-jtXNGxzX0vq-5_QG0fx7FP2vvOnL3Hy3gzZJ4PyvHnAxhHm034kGHcsXBK1lBuO0i64n5zSWWHzMAswJ3u4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je6Db0AN_QItbIDiC7CTOodVPYzi1maUH6b8huagwRoYbhG_bCK_1MhEJvtGPbWaAtNp1hrtpFx2KyPyTvnELTXaQh0dmcejnCThohvdRUEARzcDEkVFheNqcmLU1ZpcUM81oVaBzkwZGfDrqV1Ssmr_Fk6ABIC6Ga9go4BhMjLTsgf-_xtT7gmHWM9KV-MIbgi5FxI8z-KBgQuYUGheR0cnMgtOjPjoxThATZ_MQxyMgv49QQmUAj-oDqXv4kg4QSu61ajgHt0GGAYzhBJyyLEYaWsBNp7ZM-fpT6kzz9JWtxcsalSqt6jp1dV4f-6oobtRLL-whGH8jkZxZUGmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=XEzjGEtrYnyZtJT64mmzuBfQtXm_PZ41h9VTKkOZj7rV8VXaVa65uj4WcgDpp__imjaIdBT-SGimwROPV7pLWf9ktcGBQqCLjw0kfzWQvcg3Txmx9A59VDGVaXRoCDpN7_L3iB_H0Kc2B89XMplzHn7ur8L0FaXVpuPbeFYPDjzHGm3S-Fb7CJzeHDoYr0SPspB-6vB5EQj8MpgneDSuXTT4j1td0HwjPcMJlsEnwTnXh6_wfU0t7D2riobQoAvQSupbXvwseBqJn0SNHjx7UASYf3diP3RivAgO-OQVtcEA2BnOfYdGlwwlATV43vmQ9Icxgh9Qif3Z0uryMPtZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=XEzjGEtrYnyZtJT64mmzuBfQtXm_PZ41h9VTKkOZj7rV8VXaVa65uj4WcgDpp__imjaIdBT-SGimwROPV7pLWf9ktcGBQqCLjw0kfzWQvcg3Txmx9A59VDGVaXRoCDpN7_L3iB_H0Kc2B89XMplzHn7ur8L0FaXVpuPbeFYPDjzHGm3S-Fb7CJzeHDoYr0SPspB-6vB5EQj8MpgneDSuXTT4j1td0HwjPcMJlsEnwTnXh6_wfU0t7D2riobQoAvQSupbXvwseBqJn0SNHjx7UASYf3diP3RivAgO-OQVtcEA2BnOfYdGlwwlATV43vmQ9Icxgh9Qif3Z0uryMPtZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=Xw0GPFGNpCgSjGzV4Yo1UNobLRZpcHaUOJ32QMIYcM4W077Rr5YkfVmHlngZQzp1TQBPr8gTHi3ERILvVpsxMU-E3Qm8Cf0md8gcrhcsGPW-Pr44JA157ZNXll4J0onGRCi-Jid7XiYZb-HDqi--SPofo4tUnB_smKAtx8KCGatAoiN6vHv4lvjhFQraYB9i-kyNBHkgDbzkJ4Cwhdv2MYQiZUS62vF_7ypDpnjDhcl8_70OSUGP-XHp1FQQ93rg9DVSg99Vd1HRR3d8P-1Cg2Wlch8aJwTIbz16V-5zuw_SGhLTYCCJJ9rSiRgWSRlPIq2L6Cbq6PP1ovBR7LRq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=Xw0GPFGNpCgSjGzV4Yo1UNobLRZpcHaUOJ32QMIYcM4W077Rr5YkfVmHlngZQzp1TQBPr8gTHi3ERILvVpsxMU-E3Qm8Cf0md8gcrhcsGPW-Pr44JA157ZNXll4J0onGRCi-Jid7XiYZb-HDqi--SPofo4tUnB_smKAtx8KCGatAoiN6vHv4lvjhFQraYB9i-kyNBHkgDbzkJ4Cwhdv2MYQiZUS62vF_7ypDpnjDhcl8_70OSUGP-XHp1FQQ93rg9DVSg99Vd1HRR3d8P-1Cg2Wlch8aJwTIbz16V-5zuw_SGhLTYCCJJ9rSiRgWSRlPIq2L6Cbq6PP1ovBR7LRq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnRuPapW74VfhGIH4RmTusO6PDNqam7Od1jwJK3VgE1IyPA2wrgYPqL7WBhipUMECfCysjMeP1AREK7TKzXvYiZZwdGKOAsozi0y8bmFtg2NEHOm59_7zs2Dc5q6ZMrKjfSTK4pa_z-4tH3CTS7JeKa8kpU-sdWf5v_7zsfu2AeUCVEz3qWdlaTARRkCh31kAT_ZCU9DBzlQhIxmrbCMb0lDGmLlDRrUanjvJTtfI9eEP3Vqr5w4e8FDBJTjez16cPRAIDei6dghPdRZXlbsXJMUE1e2pgaYDhhLMpaNWc0oePAO-dBkCSldetCPfQYo6yEV-YGbXbgULeTrfg35jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
18g
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83207" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ5VIxSxqxc7nREWa-5mF-OLog8ah8kHR4F9ucTigTLGj22H-hrkesWd8msTyhEhHE5ed_lhhTF-lmZ3siQGQ-WXlEUNQJwjD886F7w2eiW40u1rgQdWKQpPXX5d2QfW87YAw_8Urw1NJq3z6l856KAYcq8P1fukubrHBuayWuTgeZaVpCK6m0CC5eZjeVldBVvy1BU4Oq5-o-sqy149ZcKZZFDoF35u-MFBKx2jjVrXHO1MbaAEpDCFcGWYKqKGcllumGtQdkKrEaYPLSYv_Vz4wJvnNc8f_untELyyLmrAzp4v9dLuKRaKT-kqrD7T-I60y6iCO_drHZFh9UsP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRpvDdA6q-gwmD6f9cqIwfxt42z1dvksEXGQTeWdKTmkUlp4Vk3gP6BNzFlcJ0GDqDnA590SpyPfPuTE2KMCngO3QfrSqXdMpRNZ0VU3DNifChZI5ubLcoqjgWasD8vOgUBuYLmjVW-M16gyOUEZederx294HAkJDsQicJOB3G1S75PvVRx3ROTi4Xw7o3N6kGYDDrZGB1ndimNT8hybc0GeISfUp7tUmFAfeHCG0hy8qWWP8d19WO9QjZag3m-50MFBm_iLScyrssQSeCxkdcWNT3189ISKW1lqp9w8qyMbsvhcD_w_S9icbwLfTN0OuXyQZB3BQBhxROENkCUY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=W0nTfNnvn-O2MJtirn3HoPaWMhFlSM0ebfbup6WWZb2-StZqED_tY4c-ogGMqiarwCEgpFWjwnNyMn4vJiQH8ExOyKhkAfJJ8f7zYEEHOGhRKuj6kDDzpqxjBgkzzV1NnQj5xR6UJtIQpVn0lsr6gt4UcdvGDcucYa2SXYpbeJdjSNUutVpsNU2ZUEd_HSW7T9hK9daLkvdjujqikZwf7rZkKhUU8SkRQJIV-WBAbCd7hJS3RaHmgNc56RfOmWATXtGAApNBWx1trfTnnrEfB7j0Vv8zyAr0gc-wVACkzhVv-McYLpawvUYI9ex8Jkvt4ellp42p3nfZRvM4CC8tIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=W0nTfNnvn-O2MJtirn3HoPaWMhFlSM0ebfbup6WWZb2-StZqED_tY4c-ogGMqiarwCEgpFWjwnNyMn4vJiQH8ExOyKhkAfJJ8f7zYEEHOGhRKuj6kDDzpqxjBgkzzV1NnQj5xR6UJtIQpVn0lsr6gt4UcdvGDcucYa2SXYpbeJdjSNUutVpsNU2ZUEd_HSW7T9hK9daLkvdjujqikZwf7rZkKhUU8SkRQJIV-WBAbCd7hJS3RaHmgNc56RfOmWATXtGAApNBWx1trfTnnrEfB7j0Vv8zyAr0gc-wVACkzhVv-McYLpawvUYI9ex8Jkvt4ellp42p3nfZRvM4CC8tIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=u9WBUykGO81AjIxxkKhRr0mfv8nULRvWPLxMnW0NWltIoSTQR3q9_XazwOLNauVGz6lu8cQqGvtdphn8HIvPd3KrGJs0jwH6xj8mSvsTqW0eUxjl6mUCotP-OCsom-Wlik7X-Jaxq6YVt4XXeuLXiUmZh-DO3MXesQDNH1SyNzPmZdhsR-Oj7bP1ugh0sXd43NonAXUR6YA0sBd1TZwNIA994O_7TkWXQuQ7i1Nv-FfTKzPRiy6vDsvI07HOEI36PoJovJMZQSRi2ms2Jajwdo4FLofpUXWtglEYG0rfn9cKU2Bqt1NaeCRAFon-rHK5943UqikjbfCz5le_VvgATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=u9WBUykGO81AjIxxkKhRr0mfv8nULRvWPLxMnW0NWltIoSTQR3q9_XazwOLNauVGz6lu8cQqGvtdphn8HIvPd3KrGJs0jwH6xj8mSvsTqW0eUxjl6mUCotP-OCsom-Wlik7X-Jaxq6YVt4XXeuLXiUmZh-DO3MXesQDNH1SyNzPmZdhsR-Oj7bP1ugh0sXd43NonAXUR6YA0sBd1TZwNIA994O_7TkWXQuQ7i1Nv-FfTKzPRiy6vDsvI07HOEI36PoJovJMZQSRi2ms2Jajwdo4FLofpUXWtglEYG0rfn9cKU2Bqt1NaeCRAFon-rHK5943UqikjbfCz5le_VvgATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMMI1h72hmD68p11C2O74OWGSUJ-xoCD6xNwckdc2yk-DlxZ5hYllGZfaIL4_9_YDxH3brWpnpuo5NzzcGO1vfd_jyAMXDX1xMVu7xENC49Trtic5EkqhzTrhbXvV0cu0lQDYlDCB7zqHHdsPieAYH32i73Z5pnpIhismGDHAe9YFUgNf_aavwpt3-pzdpYP3d6Vgnbr_DcReYvyNagARIHi74RZuCy5Y_j_7xVV-1bHRKSVVIRRkXrBNR6hIVOyfw8okXljnWLYgKxJ2xpqEGHZI3maJ_N8M21ADReQYjpyAqG6iSJoUNXqaaFfhxQdzEoVVlbxoq9NLsTA-2aZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZj6C-SxsXHoW1jbwqG_NzJpOXa5FE9Aarmc9VgpwkzbXR4n1h3Wr2OfRDvaVrsp4qdzeQoKDieu4ornm2Lsjg4yvsSniB0pqWnCPDBbz6AFWj4UjIVMs7jhYQRObPaU6tyqFphIoXnvAab3LcD2yqnWAw8xGsNy-VA-Y2dSyZ4Ke_IZd0PSXTaFGUWdoe0ztsbkA1V8bUU6121EQ9wIjXy1L-EktwtJexAhpEn9n_SnB52nyruU_6Hd6TxUJJB8sBQobUVvxqqPArgz6InFQlCXbJAFT7QWyUoX-74auncgyJj0lm3jkHN2m8I98f5X-Nx7cs4dSPVQiL1fxVD-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMRS0z7OMUwQ_T06MZeXhrogCsouSmdawy3IVrgkZSGNXFIENtuxDYLcfaCNsIoLAjTzy-Az4T_njAQ02mLNW7K_XUpquNd0_w50H6DVi5l3mXyVCPetuUf9IaUO2o5ixZdD3yaEfCfDXGwGgbqekdCIl4GoTk9VRuP5vWvoBEmn44Y4TGb0o5Wm9HAKE_QJ5xjin29ZsKHzYv4kkoUL37XbKPdiW9TMbUv35f0DGXuiqt3_MGkSlYhsF1zVTPKYxMsn0GaLIniBr3lhAtRsGQnsjRmntB78jzL4jZ0Jozrv4JNvIayonLvsW_PSxX14xGXXED2cBvDz-HxmBEL1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTxf2e2K3r-i_kvR9JSUpB5fOuvYROPAKtf9AK-yckXfqOuXM6EXrYOMF0aHIfJ7dfhnweearYKCxJWL829fqaVf5NEv2Z8-01_IacXn67f2avB51zOoBeGl-HH3iuhHk-2FR4DNqvRewkyxfkJzjPniyE75MYYfUDp709cVHhZY9jM_KXc8D4hEHLjTdceMzX-JjY3ApHhc8AfLuj9ANwhFPsHhLXMi7HcYAI-iLhaAPOdZSB5zOWbUHg3WOlJH9LKcmTLXpre9fplqgoY5mvk6MkuARf-tShG-chHW0FhuglYVGkOom0CJJ9XcBXsUeHSUUhrVwH7xB9ZeyaGFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHxWWWEZh39oUR-HMDlm5DsMh9vRFrCvfLQacKEc6RZCWjrLsjBua8mt5byOow63V5gXJtvFO6NBawTvn3ToNbcKjagh5y0O1QfOhvcowBssrsUKCjV0NMLrkmVQSx5e_KlnIdS6zzrzjNiZFnMu9TheJ2O-3JWR6pYlmWZZZFyx83v8qHKZtHBvH0rJ3YWTQVUv0bLI8XhbpkblWMJV9BKILS5yLi5gnHtZFoWy0-d3ANZoroCzd_hAz0vzNu2BxNI0vHUhhLuoSUswZZSkOdodSbMZYdg8cY8YMsGNz1fkRiABs7U5xFuYp3kyPgVhkDgmxu-gq4CozwN-Ua7Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=ecIWOOqKkUItys_1patDZIpRym8B2s7pffXcr4v-oFjkye4f9RgJLUhTt7cGzLY6hQsYxVmktrOX0uvKkaObYdUNB7XNQrz3KuxYSIKbs93oOGxAu9i7vhMFvzUe3l2z41FtQ9f96u9WE5NzwNSJCSYEMuBmxeJ0qoLvKrk7a9rRCyGDVf9N51-3JOBrpOG-rHpyYsXXbmrHv3JgnxgsVLvg3oAN_Yzx0-Pa79bZFhxM40U5sOZOAKe4DwGTl6e50sSo2dOZcvPE7ARCsgsJEAw8CinPhtasJ5JLgrYlmYLrE0vZh5TjRqzt0jOxJKewi9aHgxn34v9G1vBHLyXUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=ecIWOOqKkUItys_1patDZIpRym8B2s7pffXcr4v-oFjkye4f9RgJLUhTt7cGzLY6hQsYxVmktrOX0uvKkaObYdUNB7XNQrz3KuxYSIKbs93oOGxAu9i7vhMFvzUe3l2z41FtQ9f96u9WE5NzwNSJCSYEMuBmxeJ0qoLvKrk7a9rRCyGDVf9N51-3JOBrpOG-rHpyYsXXbmrHv3JgnxgsVLvg3oAN_Yzx0-Pa79bZFhxM40U5sOZOAKe4DwGTl6e50sSo2dOZcvPE7ARCsgsJEAw8CinPhtasJ5JLgrYlmYLrE0vZh5TjRqzt0jOxJKewi9aHgxn34v9G1vBHLyXUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhFhOu1rJSzN15Kff7Gqb9U12Mp_PcvkDVeuFSaW9MRJR54p532myzXmvcc6tSdC2_S05mUn79GuHsSRuPKDRa3LRjV0_R-LSuuO2CdVS5OYPxaiY1xVVz_vevBhe18alCry9kUYITemfQrlQnJwsvNL4mZnTXBtlCxIANJaDIzY-JgGeZ3idTODNpk7qAFXonT9il2FRMzfr1Kpc1nufn7LtLzk8ywcr94a9W1IcYZXd7pRx-Ib0PUTx-eh7e8e0ZHjrsU-x8Uozw6DE1JfvFmrEXEax1Agn9zRC0IFyVc-bylPf44nRC4guP2cH2IG25_eA893fXwPJMXMzMIkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=nuPCGDdYW9ZuRYVLQlIyX5TIrm8eHgCjz87hJZBITMn9BQkLjfsF9oGETkTPu2WEqYeR7Tkur5WQ_UdJzsqc-HdOW42UpT8xVXX9iyFYMmeVnPhKdZa1xyLWg9QWI1SD5-O1mwAAOlzeASk29vtrMvSqVTzpVdOSve5F-ATnhuzsoSjVB707BCK0wEmM1p4FuEIpvu3U19YPoQvYe12w_zDut4wOQZZRZhvY0wsPpp2Sjllba1dfNZPJrJ744EDhdeDIXjconOrsP_YDXfH9gtEZgsft3KPeXltUDXfz4mUKuEon5UrhUfpGjii8ENM-aQ0AG-4hi0JxA0IRULzxXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=nuPCGDdYW9ZuRYVLQlIyX5TIrm8eHgCjz87hJZBITMn9BQkLjfsF9oGETkTPu2WEqYeR7Tkur5WQ_UdJzsqc-HdOW42UpT8xVXX9iyFYMmeVnPhKdZa1xyLWg9QWI1SD5-O1mwAAOlzeASk29vtrMvSqVTzpVdOSve5F-ATnhuzsoSjVB707BCK0wEmM1p4FuEIpvu3U19YPoQvYe12w_zDut4wOQZZRZhvY0wsPpp2Sjllba1dfNZPJrJ744EDhdeDIXjconOrsP_YDXfH9gtEZgsft3KPeXltUDXfz4mUKuEon5UrhUfpGjii8ENM-aQ0AG-4hi0JxA0IRULzxXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دالر ۲۳۰
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83185" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHSY9mZS5VskH7671Z3at8YznWAkRHEJkHJuKjytj5Y8fg1bsH2K_LnW29AjXuf2YfZqtvrl_5xj39cZEi4cvwnPmyctc5H7iAhib4BgplHgQmEOikM6hcMLhVPTMDU4tlP9FRI4c2_KWynWpjK-Wna2y4YoAKkMiQ7H5ZATeqg2TJ4lobu_4FXU8QbObTNdYM3LW4nuU-qvb4wWZBgCCAhogJy8CImpJO2alXeuddI-6s2jBHQfmLqs0Zb6cnEFo0qEGyk4zaJn5S93f8RBxcQvD2te_gVjMVz65BiWIdCtgwuPRFcT1Szvb9QGT9E_-Rk5okI_QXr8Z7k6MqH9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83184" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=fKI2bluX36WTbrKvPvTSaDeWzwTu0xfPMSKOi8SkbpfuyrdurlXI8tHM_MvPzeX1JenP9_Ioy7V5rAJ9gdRJPGoDoYVVIxdXhkwsNQPCAVmsp205YCoRuqkGIv8TlR6m5Iyh0WKRjPq9pa75Uz7lIagecsZBFSzq0TnVQCy9G6sn7Xj5pXcUum2MLJIv8LZHnTF8nCdh_k1R93VAtH8ZZY-0abNpgkCXTqEhwab41WYQzngMwnWIsEl7bX4wjmsTcBAURxS24c2lA6bDy6nEZ3mtI-Jx7xLJUqlnvPCyB4KHKG-UfKB2l9eSEHslmsaZAMu0DaDU8i7Nd7YP5nls1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=fKI2bluX36WTbrKvPvTSaDeWzwTu0xfPMSKOi8SkbpfuyrdurlXI8tHM_MvPzeX1JenP9_Ioy7V5rAJ9gdRJPGoDoYVVIxdXhkwsNQPCAVmsp205YCoRuqkGIv8TlR6m5Iyh0WKRjPq9pa75Uz7lIagecsZBFSzq0TnVQCy9G6sn7Xj5pXcUum2MLJIv8LZHnTF8nCdh_k1R93VAtH8ZZY-0abNpgkCXTqEhwab41WYQzngMwnWIsEl7bX4wjmsTcBAURxS24c2lA6bDy6nEZ3mtI-Jx7xLJUqlnvPCyB4KHKG-UfKB2l9eSEHslmsaZAMu0DaDU8i7Nd7YP5nls1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب سپاه بزرگترین حمله موشکی اش بعد از ۱۷ فروردین انجام داده، این وسط هم پدافند پاتریوت آمریکایی اینجوری داشته موشک رهگیری میکرده در صورتی که اوکراین بدبخت بخاطر جنگ آمریکا با ایران دیگه ازش بی نصیبه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83183" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83182" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83182" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7U7oQwbt9ffF-p1-lDseK7a96ytjn53cT9pryYbQDIetEP1fEkc6tjGpqrOSoY_X_4NQM-aI6FhQ-aULLhAIG_v4jjkTVQTZSknj6tm6mW2C_pDALMgR4kCPzx0Xy_u60FWf4BB5ivkkZKLP67mmr__c8eoN594AVAJGbhslME60fldCCatYFKmHHF1R3x805r-QrUwvO17wgvvcxZnCyAUKwaECPMm_VWcRFiYXawweJ_N7FF7OjCN13ubN-8gXhtn16wIzE-NXNnZUsoSRHe7ZVkgxgJyPDK3O36ur1nhnkVcKCYt5btPx0T9vqTOQAtsqwQztr7B03gVtdOPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r18
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83181" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE5Zd81ZiVB-WFjZHdkASn397L2BdrGmFy9SUkLs41eFnOaNLp45HHK5J3pbEUqERbbxIqAS3JGC88mMsUdn_Vgk-fibjRVhvVNhDEsuz_eKD17O_MwyHC1OaoHCrfr5Dsnf0Lj6_73zVXuXOPpa4VtyS12fSRKkErc98t__ChajgwZrRqULD5P73zO6S0R--i1XAHGIC2U4jHHSXHoc6sx1gST86HWWLJiOiyPm4i7fcH0yvqkYcFdYxuoiOrwFawQkRzazCYnD_rVZGY3DiupjRoDTDu3BvRVVtkvFDfvyIWcIUjqNlMFKUA4h7uQoVF643ybNJux6hd0jxZI9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ بابا جنیفرلوپز ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83178" target="_blank">📅 02:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از این موشکایی که میزنن اردن کسخل شه بره بخوره اسرائیل بخندیم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83177" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آمریکایی‌ها مثل نقل و نبات دارن پاتریوت شلیک می‌کنن
به زلنسکی که میرسه میگن نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83176" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من حقیقتا دیگه بکیرمم نیست چی میشه، ما که بگا رفتیم چه کمتر چه بیشتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83175" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83174" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83173" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جمهوری اسلامی هرچی داره تلاششو میکنه قبل انتخابات آمریکا جنگ شروع بشه و هی حمله میکنه آمریکا هیچ اهمیتی به حملات نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83172" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5D237zYmAznfutymGPnFe5Pvqz6OcaKFT4mTb-R-vgTTtygVkO2Q0TOIbi3MD-5BSfSQcyKmbZsZCltiTX9Yj579xPVSERhvjSgpIh_SN75_9VGnXbQ7spbckSqehWmwLaDSMSDA7vVt7I4rkgkrimXWHukYjI3WBSTl-58Q5lfOaFa2CDwnPeKYChg0YCplMzyjdQbR4n9ImQmQ2zvXTeALWckfb_S8anGmLm9JBjtWcyVe3tXZ6Y6IjNJvxXJzpqm0n8W56H6EPWPTPdXjVNBmTqiqsmRBIxen8gJEfOe9bb_cuFR0TT22KyMbxb_rlpyH47kyYcrMkV0LRDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیره جان افتاده دنبال کون مردم از کل تهران فیلم گرفته، اگه قوانین کشور درست بود الان باید دادگاهی میشد بخاطر همین فیلما.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83171" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار فرم های امروز:
🟢
2.675
🟢
2.104
🟢
1.696
🟢
1.77
🟢
3
🟢
2
🟢
1.26
🟢
1.56
🔄
1.9
🔴
1.62
🟢
1.616
🟢
1.416
🟢
1.4
🟢
2.4
🔴
8
🔴
1.5
🔴
1.3
🔴
1.6
🟢
6.7
🟢
1.856
🟢
1.57
🟢
1.74
🟢
1.495
🟢
1.28
🟢
1.2
🔴
1.52
🔴
1.736
🟢
1.925
🔴
4
🟢
1.43
🟢
1.89
🟢
2.485
۲۲ وین
۸ لوز(۲ تاش کاملا ریسکی بود)
یدونه برگشت
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83170" target="_blank">📅 00:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwygQAQQmTlbPtWby5rcs2imZjS32FzPP7mhg0Op0dYSLJww_KvEqsnPUgsaGnFESdLxCiW5Ddh7uXu_s4VFB6KFrWalUBetXPC7VnMf4fhk_oaWZgSAMBi2GR-1DYAkgCaT8zVcYUSlGbR-ZWqQecL5HVqSg50AE_YC6hlT-QDlrTpYNvfqBGFRPLlclnbTaLBsFQJ9PoUAFKM2Am2URJtq96DTF8Eaqav1lKn-wF3UO2nItRBBNl49nxQToB-aMQ4gDxqjhjB6jWgID2ViPiI6QpJ37q0gJfFNV-obW14Tkty9miLfTAlj9ZhCivF6IVwuTf2yk7RSFWQw1we5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایزی وین ترین فرم زندگیم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83169" target="_blank">📅 00:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از کی تاحالا پرس از بالای سنگین و استفاده از اشتباهات حریف شده حرامبال</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83168" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی آرسنال حرامبال بازی میکنه ریده تو فوتبال
وقتی رئال حرامبال بازی میکنه میشه کشنده، سریع و فرصت‌طلب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83167" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من بشخصه فن هال سیتی ام، چون مالکش تورکه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83166" target="_blank">📅 22:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واقعا فنای فوتبال عقب مونده ان، مخصوصا فنای بارسا و رئال، یکیشون جودیو مسخره میکنه که تو ۲۳ سالگی جزو بهترین هافبک شماره ده های جهانه، اون یکی پدری رو مسخره میکنه که تو ۲۳ سالگی بهترین هافبک ۸ جهانه، تهشم این دوتا که هیچ وجه اشتراکی ندارن رو مقایسه میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83165" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdBbFqZlz7QGZ4piT4fJMp828-jaukFOUaUTh2k4KUAgF-3D4J5wffbbDdCEVn9fz9U3T26L0Oc9-okPwh3PH61Bc_kCKU99e1L8RzSROY9FKCnB7ntWeziug_YXKui0EJMAnEN6SVwTqIDn15Sf1CtaayzBiLefNtXIdhD6I0rC4eE-2Spy1ODmF9XOA24Bt3WsuT13f0cQb5PyBkO1qxNGOtdet1nDrR1eGGULUnMSmvdVkX0LoysgD302hMjNbngpjYA6oj0W-49g_n9SUw0wrAJk-exOGco2S9kTH3s2MBOqfyRJKRmVPkEerOWC_SFY6n1g7F0k2knwjgRyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من فکر کردم بخاطر بارونه داشتم به خدا فحش میدادم، نگو باید به ارمنستان فحش میدادم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83164" target="_blank">📅 21:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گفته بسنت ایران رسما از فردا ساعت ۳:۳۰ صبح محاصره هوایی میشه و دیگه هیچ کشوری حق نداره با شرکت های هواپیماییش کار کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83162" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کم کم داریم به فصل شاهکار هودی نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83161" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کم کم از ارتشی که قاسم سلیمانی تو خاورمیانه ساخته بود داره یه خاطره میمونه، همرو زدن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83159" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXsLtvznOanxt9VZliAhSMhnnf5JUWNre_ZizQv5IdwgH2dGwVA070AQd3vjBBcQ7Vs_1WhUoj6B25OmEARMzatPjAtFfT-h2QQSA2-TEtWyXQ3UzMr8_Rioz95ol0De6Al40FAJrpezH6DQLpGxraKpcvFCKhk_Ev6FJ6Dwm3cfuWAksOzLSDwp2wjuKB1FRWHuWWnuNw-I78xTwW478GaIKqOQ2hJr8IT7QkYJHpJ5T-ml2Nr0POOphVZu42nm0eLrPTHmxtUvGoSoPOZcEZZTe8CpwTGy3HuD4AbLk7eUMrv_HqQt4WGcpvEcRT6Al0YLNKaBy6DljVlZi5m2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بین نتانیاهو نزدیک انتخابات اسرائیل و محسن رضایی نزدیک انتخابات ایران تفاوت خاصی نمی‌بینم حقیقتا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83158" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpguFLsaAcTsGJ_gnFuRHdep9TYLQNvc2fqKNszQoTIH18NBSsxB9UhpnYY447Mh81a1ZUB8nHRBfe0m5S9zTNdcrLNw9PMP5oRqZBCFiHnAwc8WCbAC7PDx8DGOSiBZJAJijwrZl9wl0CgL8N91AsZQ42oRLL1VEjTwDmEYb2QYWxYhQ4kyPplgPQ3FKKCZDNgzLuDcWa88Zn3bOdSBTv24Xlp4nrtJEyGPGkjoU5SeBVkKVKKTDWIqQjaWfBlD0LT9mJVca0yWM9fQjYvoqDZmpTiml3KmVUL-UvBc-zNYzabCDZeyefZvGn_uKcdWdDbqY6na0qf84atuAG_HiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83157" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شنیدم رافینیا و فرمین و پدری کاندید توپ طلا نشدن، دارم میرم اونجا امیدوارم اشتباه شده باشه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83156" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R817MB8YoeKkRd_oeXZucLKLBy8IWG_MmS9gdI_rgtyWxPAOReKxrlXJoyKiiexRGkgs1TuW0fkWGNxaFeEDjAfxtWri6P8yMjIwdYOcJNsR1mOfQdxAhFuoxRDGgpw6DR--2cKaiiZMyB9ZxYbiGxTB5MaWtdKa5anyv4l425MK6UmNmtd9qFKhgandjwxqNg34-HpMqPBaaFNF7n6fjyBgIsderl_19wVJGEUs9iKMtc5EWRg7pIfteb3IpjqoutWiR5bbcy_wy_vLYFBJCU-lE4h-2BRqKrlJxPqjy5PwMaYjPqxecPPICv4cUgfb5aAon1bZdbtt7IAKPHh3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83155" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حصین بنده خدا دلش خوش بود که یه دونه حوثی‌های یمن از محور مقاومت موندن که پانچ خفن ترک بعدیش رو با اونا بزنه؛
ولی متاسفانه خبر اومده احتمال داره عموهای یمنی هم تا چند روز آینده توسط دولت یمن و آمریکای جنایتکار با نوار مشکی به صورت جدول مندلیف برن رو بنر
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83154" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83153" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83150">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله اکبر سپاه پاسداران انقلاب اسلامی: با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83150" target="_blank">📅 18:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83149">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPtw8jd844G-77mLDHpY4Ccj1HQBOMxyCCJYTLSrzr4EzSdaPXZdOZJl48nZoNv7D2RallsgHC5FMATcF8xnXRXLFrQyUXW82VXhRiaIVDNKaaR1xoa1xPLIdg_RtW7TPKlNGl_pvXoTavzZD1J6U-epa_vhdKdIxfVn8Vtd4Bs4dJgJokVCTAiIuqlgHubZPAvHKGsR_h-iqk5OSEfmrHbpHYdin57qJ2W3UqEH-NlpFNEInr-AoQofzyRXnymOIq7RoHQTsairdOzL2qubHzcViePN3IwPOScjzO2kVRDM9QK1rUqitpfk9z-JwqCJCunBLCKkD1WlvprXcT6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اکبر
سپاه پاسداران انقلاب اسلامی:
با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم بیرون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83149" target="_blank">📅 18:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83148">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKElmenJdk_CI3e26qdyVdN9IskPAOGVldkNbx-NpunfCkWt4Zzow10rdpVqZzInLlSYSeEZqhkc55hPCIpwUjARjx9KZe8KwQchQTMM2zjuzkhERV2P_OUQLy6RsD-VfaAOLDUFmkf7HB3IHquJnGiD1CRnoc7LFgNab7IXaVXHyx89rVd0-Z_XEx5HcxLeV3QRzP8M6z9X34ldFFuGbN_vy0gr4FGji4Cx6lGD1gNTYAI-if6DMvNjf1OlGCUI8ipmMeil_U_EkM2zD-0EonfrrGEuagSbtbjJU_anxgkvT1B-Kk_hRHs5ZWy34ECiQHJ9IfkzHfG-8FQ-ik438w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه می‌خواید کامل اثر بالا رفتن قیمت دلار رو درک کنید باید بهتون بگم که با این قیمت دلار الان یه Gulfstream G650 ساده اگه تر و تمیز باشه حداقل 10,350,000,000,000 تومنه
💔
🥀
(آهنگ ای غم بگو با جوانیم چه کردی اثر استاد شجریان)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83148" target="_blank">📅 18:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83147">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5G_K4TMtKV_7yLnfSPA485l-TqO6Yny3ySfNb4RPk8w54NFlpIoN-oLqEhk196nIelw8DoltjJcfAHtVqql-3ZUt-DQ7TNfe6wBEaShpmI1_rL7mgf6pjgqslp-fgBWUxoG8K4R4ef3wqDekMuN4zRumSZdvnCxrT5WQohMeDj0odnSVuwUBndSuM_T5XEXifcJpaESR0kSqd2PkIVnnlknR6mWLH-mC6bdk0ByhcSAZKWC5og7kWWLo0jXmnsXU8cFE-XPb7uawRg_vs3cRV87mRfGfrhXgZ3WfxkquP2BqNMLY7B7QHSqahHDzPVZN8VcFe2pHn10cIKOA4Nz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داکتر بیرانوند حقتو خوردن ولی تو فوتوشاپ جبران کردیم واسط
❤️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83147" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83146">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83146" target="_blank">📅 16:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83145">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پزشکیان بخدا ما خواهان انحلال توییتریم نه رفع فیلترش</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83145" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83144">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtHfJ4H6UU_VxSVTKU0iqr_eGUQ0RFy70rSQQua9llR9ZDpgsVafzxM2zfEGlBZTK4fXwW1iyIYG3px3FI-KBJp7nnx0dCfbm1GhlxLfLZKPUfoGp7qVM-QlqXz9GYzjNdc9CP3ymzZi6mKe7a0SNLlHN9DvzHCc02xB5BSxuna5_m3g0sb5U7n4n3J9Xf5rxofBjSINtBHruJ85tEqFe1x87j2fFlI5ZNkAh1G_nGX28VzLaDg6ceKIIUq_kAqz8e0cPRU--Z68ixmVbNa7-JoWe8vXkW2b8_xVg1VsHCvVv3Jte97MmHO4MAlwzVcTwl_SQ5GdROSGnEydrkewcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج این تو کون نروعه رو هم بستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83144" target="_blank">📅 14:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83143">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWlLJB_a3wiaaoSxIeqEyer2w-iOOqbStSB0xe5s8iSrVoA4hTKyK7e7opf58Yoom-PAK-5gJQNs-ri8b0D-4Ojtz5QjatBwMRiMlNZYfIhezMEyJkOmP7pjhvXA-C7GRDQO07AjpXJ4lCJQELDN6_mVEhGkm8ZCB6-I5k4xCpGNUuksK5v6YSr1TxvT6sh6wEdhNci5MxPfQ3nYkBlGZbeEZ0JTtCy9xMaztq6lTVbDcsMOWfcGZHURVzLkzPF-RGvu-E2J0SyBAkyfgwfCsQi7qps5IvDzRqK8aYzRIgbOVH3NcfCXw3BaBwlXbbdpa-jkGQBf3xWmYEKSn6Cy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگانو بزارید بالای یخچال دست گوشیش بهش نرسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83143" target="_blank">📅 14:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83141">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سامان ویلسون درمورد معترضان به وضع موجود و حمایت از دلال‌ها:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83141" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فلافل قسطی ام اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83140" target="_blank">📅 12:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=emUlMzjKgl7REiRUNstCUtK-vY55nhWXncYisRgD1p16kqrMPutW9Zh8UsmJcOgoAyG0WeYbfFzsPMGX9UIPxNGiVGgtmSl8yC7o03z0CuKkUNd_lwEEcN17YN5eVKfAwfrTu9FQhId3ck5XP_RMxnNEw_4CvRu0wefsS7FsK1PQV49u87D434p-fL3hAwYwURyLYN4iLpMGj6TzgnpW0QP4EJ2iVQPiXAMvGExT5faJE1Fd3X3x_B1dsfIXYNXX4htzg8TMQxjAFVwFv3MG1a1O3-Rrn0-0hyau025DcNmDX1rRsDCNnuqmAhGoqJP5nQ0FetIOVUj71mK-EBprZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=emUlMzjKgl7REiRUNstCUtK-vY55nhWXncYisRgD1p16kqrMPutW9Zh8UsmJcOgoAyG0WeYbfFzsPMGX9UIPxNGiVGgtmSl8yC7o03z0CuKkUNd_lwEEcN17YN5eVKfAwfrTu9FQhId3ck5XP_RMxnNEw_4CvRu0wefsS7FsK1PQV49u87D434p-fL3hAwYwURyLYN4iLpMGj6TzgnpW0QP4EJ2iVQPiXAMvGExT5faJE1Fd3X3x_B1dsfIXYNXX4htzg8TMQxjAFVwFv3MG1a1O3-Rrn0-0hyau025DcNmDX1rRsDCNnuqmAhGoqJP5nQ0FetIOVUj71mK-EBprZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83139" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور: فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند. در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم. تحریم فناوری و فیلترینگ در فضای مجازی نتیجه‌بخش نیست.باید با فرهنگ غنی اسلامی و ایرانی در اینترنت فعالیت کنیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83138" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40085684e0.mp4?token=pXsPvK81KieK8iP883NJOvhsXcLuo6Tg1-84h5QsYS-VHnoDw6brup8WP3dGUvVesL_Sa25LV7VhPQahHdbQQ9yVML3EbWmlWXTJJnXr2eAwYOGjP0odmAHiKRW_xQwWjd0xX16SYE-NSBw7v_QEGPz_yzqz8UJbGwp04FHssPONLkB4z76h7zI9UNBqLwra7SDMzbEOP6o4iYLPjoml9jAArV32x1dtoLM7E3P_7bI8Br0KTDMaEaZpeX76Hi4QfnzH-E8hHHAWtBtEZJyakfM2K1I77bVFUl8-i3oqtwbbwIoEQvhxafwaOi6qX1YavwMWepaZrfMP-HuI33IQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40085684e0.mp4?token=pXsPvK81KieK8iP883NJOvhsXcLuo6Tg1-84h5QsYS-VHnoDw6brup8WP3dGUvVesL_Sa25LV7VhPQahHdbQQ9yVML3EbWmlWXTJJnXr2eAwYOGjP0odmAHiKRW_xQwWjd0xX16SYE-NSBw7v_QEGPz_yzqz8UJbGwp04FHssPONLkB4z76h7zI9UNBqLwra7SDMzbEOP6o4iYLPjoml9jAArV32x1dtoLM7E3P_7bI8Br0KTDMaEaZpeX76Hi4QfnzH-E8hHHAWtBtEZJyakfM2K1I77bVFUl8-i3oqtwbbwIoEQvhxafwaOi6qX1YavwMWepaZrfMP-HuI33IQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بخدا این چیزا تو اکسپلور من میاد ناخوداگاه یاد رضا پیشرو میوفتم وگرنه دلیل دیگه ای نداره که اینجا پستشون میکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83135" target="_blank">📅 09:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4_vnNlX5UzDHxPREzEICvcPz6N4_dAIpzBGF8b3k-n04NgTn8CWCklktPKpBqYV856zWFVKosT0ln8XQNMT6B1TfAcDZr0zlBWmIX13CgNb7BSyDxuvLfCoDkce_f02Ve6uDWIuJlyJ5j9zp_yTMopLUI8pw2f9L-xoOXavNsrVkOyGNak22iO02kKzv1n2hyJk9wiget08xwkYIE5pz3eX1IpjX8ZcOopeiIdYc-q3LoeyDFErbFlqSDh1bpRUDd-sV5Rfbsww20FTBurzGar_Nu0Ba-s-sWPLJ6-rRZyoJs1KCOFT-kYmba179RCsZcOGcQgreooCy8iw70CWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83134" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بنظرم که خلوت کنید آقای خمسه اس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83131" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=gBOv718PFIJkKO-2BlYuNYlctn12d3i0ZgDGLrn7p3s3v5V4VwVdDMwOnI4LMYmIqCbwYoIol8_7jqGLl0_At1rMXm9OYGuUY08l8z4PQh0vqNHR_RjCZDJ9QD0NquVTC2MmZ_nCr_tZ-bEs7bUoWFARcypU1eGbd_-5GKhRafkMSZcRlBiPxQqGaSwR1f4VA3ckmuDULZjhmgKh75foTMypxPqYg5qGGlqWUdEtNSZzx-qirTwzxSVL9obAUGLUALknEbmeqOav0oKS5-QZsG5c1pusV3cRxcCnmCMSxEVsAQNFheMGpiuVoq6zvJshMeAvjhj-WTHVNvwfAMJuWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=gBOv718PFIJkKO-2BlYuNYlctn12d3i0ZgDGLrn7p3s3v5V4VwVdDMwOnI4LMYmIqCbwYoIol8_7jqGLl0_At1rMXm9OYGuUY08l8z4PQh0vqNHR_RjCZDJ9QD0NquVTC2MmZ_nCr_tZ-bEs7bUoWFARcypU1eGbd_-5GKhRafkMSZcRlBiPxQqGaSwR1f4VA3ckmuDULZjhmgKh75foTMypxPqYg5qGGlqWUdEtNSZzx-qirTwzxSVL9obAUGLUALknEbmeqOav0oKS5-QZsG5c1pusV3cRxcCnmCMSxEVsAQNFheMGpiuVoq6zvJshMeAvjhj-WTHVNvwfAMJuWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83130" target="_blank">📅 04:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83129" target="_blank">📅 04:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=DZdi4abSzmumG0V52j8s5h0aCNO_CLiA19mplkB3b6_yJkjvZdBFE0JCJykjY94q9aW4KfJ6WwiiM78vzyQIIxABCDTjCVgEhPY52jjVNyt5h8Wv9r6UT8eCDyeURM-ALdrQ7M1KQdx8aunSWjDE0QjAlGVHufwj798rXoHAOPgpv-MRVLjy9TI29VpSL5Nzf-UgT5PlqxSHwyuNyb5HK_hMSphI0sYpjbGTRLm0Du5YPgQiS3iuktdKv44xKzwXWASmJ_vduE4f_BtLGqRRH_TQxkg-sDlgVw4GWP5jNXx5HoGFYFtBNqrb1ZpbCa0mmEP7MsPHBiJaJ0W_xgysKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=DZdi4abSzmumG0V52j8s5h0aCNO_CLiA19mplkB3b6_yJkjvZdBFE0JCJykjY94q9aW4KfJ6WwiiM78vzyQIIxABCDTjCVgEhPY52jjVNyt5h8Wv9r6UT8eCDyeURM-ALdrQ7M1KQdx8aunSWjDE0QjAlGVHufwj798rXoHAOPgpv-MRVLjy9TI29VpSL5Nzf-UgT5PlqxSHwyuNyb5HK_hMSphI0sYpjbGTRLm0Du5YPgQiS3iuktdKv44xKzwXWASmJ_vduE4f_BtLGqRRH_TQxkg-sDlgVw4GWP5jNXx5HoGFYFtBNqrb1ZpbCa0mmEP7MsPHBiJaJ0W_xgysKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که این ویدیو رو درست کردی دهنتو گاییدم
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83128" target="_blank">📅 01:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83127" target="_blank">📅 01:33 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/iPpBdl_bGmElwYHNK8VdTT7fX5uqFapEExHEu6Ob3WlsXHXfG53Y0eKpnuYRZNA32f7FI1PNKolYjX1s04Y7djVUGXqa1GMvpdIybzSJDztU8FQxTwCzmjZPXFcycaKzECMPxhFPJBfmqjskgBT0q9bfGOSFLM2pzLbzWvI5L5zEP6X1L7nqUNI9Oi_Gy6Yhj5tFmcC4I3Ida61sXCTIWRI6TaqkEDHkJ_HBwpjP2AkQ7GONPQ5Yztal5KNHESuTgfV_qjruY0yC9DIco0mnfGDl2APeJasIaAqj1M8ccTqPL7EsOovxi83A1u1a7pZI1_29orNrXqvATM7YEmEBrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 137K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZeHbhCal58avDcggu3Cs1YXXMoWoAuOhVhZ8FzyQlr2eOM0UXJH_JNQUeB1ub0iwb_V2oWd_hg6dz49U7owiFK1FuSSBErDETtOAEI7djK85AVWnLigXI5apjm4J6QlOQhMo9Y96_KBXx64OiQkdZGpxsOg0PldKMMTNdZyCAozz1M2HJoaDgLVWspIew0y88nHCDGmOcVhL9ikpvkSNBDjKXi52YyDb5CqOwNRPIOAe1xGgwrDKs5Pg87GY8-RlTjKzYp8XzBcqhg8vSZK0WfqBdztN5A3su5QbPWjvijelhqn8EgPwvkITpBlgRptf6F5_GgoUufdAvjIpXTqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJq6bFKIgeR0KFpeYkYOM2oUo3WzQJw-KgHgOyYeoiCiMqiixxQ7gSyx5RU3p367lLoQlZzcyiIPyLPuVpwVKZ5_B7znmBLVxBCTni2uySeMhSsXr4yIvCM1Arnt95ztP08xEmCHbjM52knjp0RH19dOyTbSjihd7Hsn-WypPQA0rBm8q5B9HRny6SZOkRob2WkQoB6WbnUZQm-QjpOsHnlXPNobQ06oeUAh9D2fS5L2HK7I5TlZTSH1xPmtNJYY8DWyrW1eWRu13NJilFUvJ2HQOU4T8n-eQG1xOQueGSe8Un5CpF1LomZtCesi_G2ijFNbIGEEe9DvdMsB3pEw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=AsvJOXO0wI1jCIfPbqmcdstf-RVcxNN9I35Jaeo9ulZ_BCJJUa2z2B4Eqq-K_h6wgZzjbZkhpcfJMwja0xIt04s1jjbmBjSIcgjoxQ3dr-gkljNkQDThKQKH-We78BVYn5Sk514Xr40FDIgZ-S45HyRAyYqKu6LuUREDiFMk6xi0x9oxH_aLgfTbLQ60cUXbyZyAcN_Pwr8Mq-Lf-TsmIrDeCKbzLH_zECjBs3Nw23DKkqjmXFXBZ0hpN8yPxT4G_VSz5LmVZOAEtEtbidgskYv7dFGl7_BFgWg1WL9B-EDrM-AkoZta7EqJYuWw546T9z8JA33IMppUOkCX9jh52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=AsvJOXO0wI1jCIfPbqmcdstf-RVcxNN9I35Jaeo9ulZ_BCJJUa2z2B4Eqq-K_h6wgZzjbZkhpcfJMwja0xIt04s1jjbmBjSIcgjoxQ3dr-gkljNkQDThKQKH-We78BVYn5Sk514Xr40FDIgZ-S45HyRAyYqKu6LuUREDiFMk6xi0x9oxH_aLgfTbLQ60cUXbyZyAcN_Pwr8Mq-Lf-TsmIrDeCKbzLH_zECjBs3Nw23DKkqjmXFXBZ0hpN8yPxT4G_VSz5LmVZOAEtEtbidgskYv7dFGl7_BFgWg1WL9B-EDrM-AkoZta7EqJYuWw546T9z8JA33IMppUOkCX9jh52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smx0FgO4i6sONhXdSTdOPGDSIqUK1rBeyUkTOXuvQPAIRJsdkrUk0mrQLNL2ufi-FUTUf2FSYj6gq3F9j0R6qGTG24Z-N9JwcTP58QUJcJXY1zDv4q4c3sVhlDGplxNILIz_8wouULtc3hAGggm9TltAsV8wGY_Wp-q8OlnKt212vx-_wpay68Op4rg4vpqUbJ6mQPAe4wkTJsUrht5oY3jGHFeEWyM7EMo2QolaZ6pBDJi4OOKFizPUDS76MhWPWovAMmzaOnC_f_x9BQpFlHjvXJ2z83APgSwUnFH3dV2HUyk-7tNdxkZEepoDIFymfl5HJJhplEwG-e1z6VMeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Oq0AOyCWuLKOLbQNu2KCHQV8B_KI1413NdsW4p4a77eZMly9dUxDM1Yox67IGA6-OwAmrFMRjxHoYau4ABWVrCoy6Zzgv7eHhBBI4-1lNgrD_55TrQVh2p7iKYg08APMh4sZ6098LKhh6FZGXRaS8GNWkrlWJLbXmhxQtvTt177ano21vhXv9apTHFj2w-8XwYOFrUcFV0J_vCejWliSOieADZRyEbDjGWg2SJ8bapqJS8I2PMKve9F-I154r7J1xbtXZYwukvzawVEnCiD_ShAGddknNnwg8he090SDGk1uEKbWYNHem1p7pOF0teYuR4UjCFDUyCsQv_OUrGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvCo1UfIFQt0a_0cCFAgkeMCENwiRg5-LnrfW8GtOk1ktoegdNDyKBUzhEfecj6LlkWqmfaHDeia8-RY-dFuYGYqsgSKONdkz2v6ywdBkWn3YQOfwk4ijz7kZzpyhO3O6q-N_kGM4hWVv2EtvRT3yhfs_6P1eSJu4GoNtrIC6YVuvlqviSlFm7gxv7C3o2Ef00IEXlZdh1oLcgyN9O6sX_9UbY_2VQ31ZpS5NA3sPsLpHia41_GuJWCprBrjA8wPw9KzaEVmmmVsBtQ9N3o3rSsnXT0KZrcChh5o1DYa92kUOMw22mcUq5rfk46O8DZTgSstpGKhXm2i6t2HM2wVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3mj4DX1C1VpT5QFzTfp-HakpEI54BXZG1eEWTDb-hN1C-ZDTJ_TI4Da-r1-XYBd3_bFQLnoHUihuUz1HyB9yfXud5Oi_PWRM0MJHCd_9LsziRhAxmNn_xKxnverCNQsJnpi7lLfi9JKyMNosMPEE55Ceq08b9N7Pa4BWWVjnGT3O-itbE68SOEsp5lHFX6v-cE_Q7cl-jNgJbaRzeSUO-niEOlkD-z9HWC26hlOcaIx5qY6o8pXOQE4ctH-gO5NdCX9OybaKPJN--5QqVh71JmM6QZ-SobivajIVLhxj1FSGO7i7gzFcFqbzbLFtrDCMqA5ZTLCb5HKGs04kgjoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9dcuKYa3rbhQPQZMBTqH-oIY8uz8dcS9P-2sFdu6WaB7B7-kmDy4B1Ku_cz9jbfvlHLo14IdwBuWTHbnjaIPJepMz6AQwMlXWrbtvHfaT9QO0D8maWhf5GscBBBO8_K8XukQI9zaiwHAZ-jgLR-hmHjeRzUCCSJlaXe0Y6NlZ5C9Wn5akNugPKnyTAWriF3Xq8fnV8Rwc93ruUUDfyeewmYOfEmHj_VW7uHPf53-edT24RUCTgQIjSNLACzg4yUfATvl6IYZoQU-xuf7dIxPC8ZP2TCxA9DElzMhsW-k9EIBDo9Ri8xTuyJTzjqmsCnyPVkQHxbmOumJDFpHsv5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aguEQQTae_ozx-L8_VKIEMw3MvSGw7jOXaY9lJpli8e-E0LCyNnm41Etz1kd1jPr21czJS9Oc36QCsk9Onx7j02LXdUg-P0yT04UhyOdn4Fa-Em13_QpRrwez0rQ_HXI2vSVtQpThllN9JYpmuNKLnbtmHyKBdpliF5ktryvtNo4bYSW9S8Ri6h2Ia5O-5DXF6pqP4rp-r9ifFDP3aEISZ1tl4ry_FAVg1SshCm6eOHasw_WC27-McuTKdscuZuYj1vpcpifX_hFuIJoREE2zcvXJ26MP-4HxHG4wfd_kWIKFTOKwUAoQg8jH9PykWpG_wzv19YoGiifOZHCJtQVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWiCgDLEL2Mrl0bWqL04ZwoLC1qIKd40_8FZs8zMun8lZPBLDqYop5PlpF8D1oys1xrQTMdhxaw_M7ZymECG0viLO9WcFrizPk1NMnjVGo0jnn20h_k9xwp9upn-bfvMMrmRJFjUDQWbaVeomtIzsc2cuNTiKyp6Z2Di4eDSnj3u9NIC1JAMHsE_eJU0pX1klZcZ0SR34KFXob3H_sFgVo96kCq_8EljbmTkXUgnUeXaSg9o7rBSdFxsgw7IEAs21XEQMtnvEJJEM47NmCP7oSgeg2DypqviVGPmk3JNS_GUFle7BED-UFQ459KVztFK6RJHw-UFwtmJCEAFEbuXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=WYes3syVnuxICe9KUw5HFx28pPofM8tn1bfY0v0RGWbQ_xvZ4L56G96QZ6zn6rVdg2Rp8f2GkQeHTQuGWU7YSMbohJ_uzJlIAuETfWVvOAkuv3VfvQiQEfsCjvknQwG84hsjt0IlAN8Mq5Vm_lMyY_AGtqm5atG7vL7YL3MF8GrRIxISN6uKztaZy2p4uZGdYKFZCidOLV27wxWaVR-tAYE62HSaXFTgLSxlxvZ9n2XyHlBscM-Z8u8XIX9lVIO0vqZm0KfhA1zrqb3_C-ajfrYNqVM7XhJl3kyA1qUp-J_5hIKYkUOEIoBVLJgVWXYpJv0M7n3vI4ZVyWe3TYvBSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=WYes3syVnuxICe9KUw5HFx28pPofM8tn1bfY0v0RGWbQ_xvZ4L56G96QZ6zn6rVdg2Rp8f2GkQeHTQuGWU7YSMbohJ_uzJlIAuETfWVvOAkuv3VfvQiQEfsCjvknQwG84hsjt0IlAN8Mq5Vm_lMyY_AGtqm5atG7vL7YL3MF8GrRIxISN6uKztaZy2p4uZGdYKFZCidOLV27wxWaVR-tAYE62HSaXFTgLSxlxvZ9n2XyHlBscM-Z8u8XIX9lVIO0vqZm0KfhA1zrqb3_C-ajfrYNqVM7XhJl3kyA1qUp-J_5hIKYkUOEIoBVLJgVWXYpJv0M7n3vI4ZVyWe3TYvBSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRXAOV7109wqDpJ6v8lnBz1BlHn7yUUVPyHGVzwQka3B1xsGBoVbxTlpWvHQ1GVtweKmeouoLZ4BHEjhCNhCeaLHXRqlBmonqvc_i2gkMuQkF9dUyVPVEAJnnLm0PosLPS8-pwErgPzHeCm0EB0m891tB55naSN8tEMOuhyWJYRp9QMarNc6qqK5e6nn4nGVMEdwnXA5LXC3j_uEyzBgTBI1B86sYA3T1HzfjUtvV3Ksz_PF8L08i4iovTpxF4ygz_H8yS8We0KqdmuVx2PuBeg-x9MOMh_HL7IbOnvmIn5Qfi_pQkkMpGXwfE27FkY-q99Aq0XRKikEXDl4-byxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89914" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGBqbSfx9Aw_Mvngd1I67n_dkmQhPPqJ5NM28SR2N00muBJC2MsBcGpA4vx51WNOujzXpvRUbY7pbQPq7NbsTv5rCktHTA6h2mxGltHne1_UIg4XHLdFPowIVz0WVONvKoBpzrvK9mfz7SGC20qUJesSEEe7t2ljIsEa_w8kwhfqT5UeCJgABjgSZkw-Jytq9tnXjsByoydq7cB8zPHKOsXvgIoCRkL3HQ7xuL4jpjT3cjvOu9R0NHJzZhzE8se2WzlPX6Mb8GHYYr68PcIeIT0Qe3N3L8wosu4xm7YhWJXhE4SvkMBhNz0Qc37uZwHt7Wqi7_RTlHhBHLJcOibAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89913" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHuu1WckMXtszxJRs8Euz1MVpw8d3zx7oAJNlUgl-aLikZPB6XwlN6Xn9ArqIbq2TpwYpiHpsSc9kFCt4tS7Hy9G__dPyNHFnreDiaPb7cCRZ9YOld--yzNpqO57WnAu7wrJ-RbY7l-jhQz9hPRP8PjWTf32THNJHDBtXLVnsZbp9PPV1LqV06cIhJVJlm2OG6gSPCjHaRekko8DmMfvr57K_wica1RGgTdQdhh2hx_lrHtB2dFAzS3HEWEJWiQx3-mkRyMdE-OWhjREgMQTieOVtt3vhJJGnMAY_h83MEjuXYZZfiY3Jm6cwtRpUbuF49TirHFrPVcw-XcE1s4MtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpqjjMr6U6dJOGjp0Zrl4aeqa3Fyo2aq-mFm01bAUt595Eh18My95_UkaFjfMyju-GmHbGgM9WYaS_cY9mBvfB5cNrrErEoBNbzluN7RxQZKCB6wi7Nvkx-4cpbbJeP0ji2NIbHXDEf1CmTpafkaM0YSsPaP0mCxPVgW9q9imMfuoNaq9eEt9xW1NLZPH7zpAEYEKYnWdDkPIygMoOZ8TRRcMphjZ7xumJ4lhmlKDxnhxRdJ7FlSlO72iKM2hp6WPalkBhGetpS7-dpXcJ3NVL6XOW_SsmsnEd_u6OCd9j4kYyKViaIVoeAymXWjcYLfBz0e2RdDnQgOz5SrQCpbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7fpWL11GKcySbZJeagIkXqIlHqFpy4jlwxR7RusWiUv4sTdK3NV5E1cdOLCVCcoh1lkEmnf8OgKk2BLJpk_mzPShPjX2HAEkkv6zxz-cPwDXNYix6R2nseWf7dveKEjrE16XcRo61lFXakTU1YLT8sxJhEyRoeUOU-SBuW_1EyNsTzyXtIOPr1gttpQc_mcsTHyb1L6agr35VWX7PO2IRTq-Vz3BX2zM6OWN4Y-rwd37OYk-Kiu9utOcuNQzjM1XqIXMenGvbvgpJOjXvVpEHn63A_OWTAjeH3T4RR4-qgU4pXQ8yxp1I4B6SrNBBUcEhCDrlfkUjJJcOAuHKjERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byDoCChs77t3LAGyd87kW6WiI79jlMfFLZeEjduTCMS6Rr1ENLYDTx-SZaCCP8TgN5_wIMDwdIpM3LQMDT-G7H6MNrGUMe7hzLez3Q3likZisyualgf7LPQc7l-eJLI7AX_ZAjW4i6AJZSXtAsf3bE1S_AEPVxC4ZUYPwK10qGOMCWaM98zQVMYoic8j0ezmKrRu1Ohq-gC9sjM3zpaB96RD03rIsArHF8bS1BH1uiNFQJ_To8kU3u0zTzrlkZCkKF_slCgZqBt_8whLx3Yv_ypLD-a67GnKcvru9ESEvXk0i8161sWj-yQZs--Fqxp3bMzMY2LXCHBGzFGLzsIBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldYrxxp93pYOQCkTQ3zz9S_us1FhYuSYTUVkHBRY2ZnYfSPzU0-D8lvU3tueiRGSjcICTgb1a9Xy780yoyFa-SkWy_f25Ke6mkyfDHtcnQUCq-F6dkJUt6kZsoeloAZxeurwKH6Tdatg2kbcxgxw2ZyJNE1vkJN0hFoumWeNHG6F1RweLyLEhQqUNjb7q9sAo0NkEx8XAaFy0xMQr7GNz8cmoBSJMhLtQpP3CfvLu_W0JRQ_92Ko1cjVGM3MXwaWLUjzEorFUmmQi0z9TS5BgNPg4b03PBzv8JT3Vpy5Y7uwYv9iwFYtIb3aNS_ekgaQbdL01sp7DbK7eDrN4DuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89899" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/89899" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN3q-KcblToFYZ0i2WkB8v0EOn7Pq6dm5zdd9yPnfioUI1yTjcR-TKEGX3IT6OSFh8OYj_ZA52BYJ5sMB9ZzhVycsi2KvFlbolph4meQqFhm7w4mllF1b8EWm5zmq8pwIAwZY_7izCgYBevtkNFjiLTBtzAYUa1g253HJku-C83p82lvMkINRmCqIKQ1FgAUz-UftmpU_l6vMf9aiKmx34fMm0L37RtA74ZZqKO2zD9dG8e9XBrdpJ5bD1nZTOQpOQFXErdpQcqNyBg2HkyoIJyOboFYGSxqPDYlHfN1pw53pF-AKC6phyxJowsNKBXWIIYrQsgeUxoX9AA_mVEvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89898" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Voxz5KUVhse25HD3FipBx0tmA0DdltZQHXEpHARBB6gEhXxVkvcwwQIN5Jr-1n4_ySCvYo-jvTkCwQr8RPAw8_zkUuOyjl2diEUZQ08JM0S-pfRJh4QTTalLEEI8m1DCqsR2g2UtHd24f0lR4Qd52elZq79QtT1LTtQAL4Cx4A55h-DrQEg2BwzrWKBe2VCxIrvgBjUtRdaWfJVsDvjnAw0WDY-Qf3JdEA2pj230Bf21OjjnqnOXq-ki5DZT9mLC_8-MSOAOfPrGbTNryTiy-7d5lDD-38-0PaHbFsGKM7L9y0Li5_MQmnXUZ-HQhSWQNuBkHvhjrNwuQfjfcDQJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvM3Ktmj3kY5pZZGw4Q5d2-PwIuQXpYI2OBj1z0hXJv61KC8a0pwlZpJWofdpNIyNKSnjLBbxgiwACSmWX7pIVSyRwtkMfiYm7SmoSkfd8vT-M48YR3vGF3JY2prR1-4nMZ7O52Qcjgdaqk0HO_EHc6WdIO-lCuRaPFjrVHTSO15ceUplErnVn5Gg_85ij2CMHtccwEC9vJdO3qc0CYYsD116t3w0_M21Cc5ThdoZJ-J65rgcp0AIF4ZA9qnc99wlcgO4XddsWvGhqTpHEDsEB-UcNX0lBula9aLL2fEXaFf4CveffxW0y57SihcnqRA85GFQdps1hptmOtCoMUA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRcbEOvEdyFyAOECt9lO_T4CMIMu192-hhpGl7ygzsuIDYoInIvKJQG8UnsApRexmrOd_0WHHbrX3o4TW6E6OBf-qbtgnSVDARTN7niux9YlPInNExEGArBDDhyQ1L6MjHJ6C_HV7_dPFi-Ez2wxXUIgI9k5em0QIfvmuFE_-mDViEpymJJlQk2XEJdhldkA-XQdaXy_0zPzKGVkhRzaeJ_5EzrQC0XQ8XjNWEl8zqs6SA6Hnoo5bAvzclCXlOkldnO2B6_9bEITX2Tpy8Z3lN_bHWAD_UKwdEi9SvUlyvSzkrj6BZxZjiq8QH77yWnXfL7vwFNkvFGT1VYnHEbFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=sgppP01ii6jLVJMvaN4H2Z1l6vhfal9HF2FBsIbzJtm98TeXMEjkdu3lWOtwmf3NCPnwZxOhuWsuld55Mysu5gstR1ZjGbfILtZcbL0BZcov5n1je21EJL58RRBPYZ2knDUCIH380HFLCDBIwbaiSqeGX-EOD2DhGapDnCwhffdtlDr4Vr4hBp1BOYwMZR-41HJLC5bcM25QOioAoi8iPx0nEidLFCdcp8S2r7uTNKtStsbOh8lXPSZ5moWBqwjECz0BiFXWxqiD6EYiLDW0hGmRIL4Tcx9jn8rYXOeS_n1nK4sc9RDexNWRmk2Y5YzJijLvMM42gXj0odT-Mz7RTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=sgppP01ii6jLVJMvaN4H2Z1l6vhfal9HF2FBsIbzJtm98TeXMEjkdu3lWOtwmf3NCPnwZxOhuWsuld55Mysu5gstR1ZjGbfILtZcbL0BZcov5n1je21EJL58RRBPYZ2knDUCIH380HFLCDBIwbaiSqeGX-EOD2DhGapDnCwhffdtlDr4Vr4hBp1BOYwMZR-41HJLC5bcM25QOioAoi8iPx0nEidLFCdcp8S2r7uTNKtStsbOh8lXPSZ5moWBqwjECz0BiFXWxqiD6EYiLDW0hGmRIL4Tcx9jn8rYXOeS_n1nK4sc9RDexNWRmk2Y5YzJijLvMM42gXj0odT-Mz7RTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=jM4be0pQddQAXzSiUUQwiaAzzTuDNwNIy8EpAEVPI0XVB979jJGGbqkSlX7_5-6WLGpe5tixjWSUrhZms-_tGBcJrj3WYZy-PsD7o3w4951EQsZS6Xm3hl34UygxVY_NS0OkAkD0cOIxC_tiYC5u7KI3OustZGA4jMM74i24UmvCDb2L1SUGWF6HeJNdjo76-YbJuoSPBY9aZipivzRPnk-u8JFAfKj3x2Gzne0EOysB10FWWwjWySUnwSdzNiK6WqqwmXZdXBwNVhi28d33yhuc_2tTw8GIT1ct0YnqpD5d_qkjZY7FbCjuvxHB4PhsnDI9lZs8L3tYBCNHZuuyd4AfhgRkRa4FX-REBOvkQAkmBCQgNcciyd0QedC2qfXp9FxC-nK4MNlm3bTAxch8wunXZaGskjRqBh7RZ37M0OQKp-gEIu14ersvK-tufcWtl4W8EaZZwFGqltSjQeVFyLdNp7MYJyV6uf63Zx5PEHwj6N0s24xHiDK4aqMttNVud3crGuEn3c--9vCu93o8wTENIZdfZ0HMJ7nZTNfiXFIhdyLSf74WW0LUGwe70-UT0sH6wLCwz1x734_JlqNH0Dw7Q-CoYTpSm3EQ3d4OCj1bWMvnPuXO9Y8ft7KSeUJ0vYI3wCOEByDtkO3orkh8e4ufMmHxe1mvdYiJO3dkq_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=jM4be0pQddQAXzSiUUQwiaAzzTuDNwNIy8EpAEVPI0XVB979jJGGbqkSlX7_5-6WLGpe5tixjWSUrhZms-_tGBcJrj3WYZy-PsD7o3w4951EQsZS6Xm3hl34UygxVY_NS0OkAkD0cOIxC_tiYC5u7KI3OustZGA4jMM74i24UmvCDb2L1SUGWF6HeJNdjo76-YbJuoSPBY9aZipivzRPnk-u8JFAfKj3x2Gzne0EOysB10FWWwjWySUnwSdzNiK6WqqwmXZdXBwNVhi28d33yhuc_2tTw8GIT1ct0YnqpD5d_qkjZY7FbCjuvxHB4PhsnDI9lZs8L3tYBCNHZuuyd4AfhgRkRa4FX-REBOvkQAkmBCQgNcciyd0QedC2qfXp9FxC-nK4MNlm3bTAxch8wunXZaGskjRqBh7RZ37M0OQKp-gEIu14ersvK-tufcWtl4W8EaZZwFGqltSjQeVFyLdNp7MYJyV6uf63Zx5PEHwj6N0s24xHiDK4aqMttNVud3crGuEn3c--9vCu93o8wTENIZdfZ0HMJ7nZTNfiXFIhdyLSf74WW0LUGwe70-UT0sH6wLCwz1x734_JlqNH0Dw7Q-CoYTpSm3EQ3d4OCj1bWMvnPuXO9Y8ft7KSeUJ0vYI3wCOEByDtkO3orkh8e4ufMmHxe1mvdYiJO3dkq_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=UIfvdOTOHFye8FmNXIuAqr0Xt93YkRSOLwFhFWlLbAvmqc4_nU_t87pllwTR2CZWL4skChirR4SsRic9c5BDan_9ZyhLiyJdccTHJoSZkQ23D5xf-i2Vs0dkABTjPpAXVKOzitno69XReELHsvN14oq4Ox3YyIrdzfEMUwfGLttQ9cgUjq3O0xfvbxOHHkgeGS13AdJQpIu9PFBuH7LvIsqhjTIzJXQE3gFDV7Xk2PEN-6-sxzA5jAogbSphIVAAyX71y6KV2h1M68_dQQUjoijLKzvNwp_nN5kDYfSjsHlwuNh_dYu6hwVqZRxnAmosoGqb3U0emJGfKHvtklowjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=UIfvdOTOHFye8FmNXIuAqr0Xt93YkRSOLwFhFWlLbAvmqc4_nU_t87pllwTR2CZWL4skChirR4SsRic9c5BDan_9ZyhLiyJdccTHJoSZkQ23D5xf-i2Vs0dkABTjPpAXVKOzitno69XReELHsvN14oq4Ox3YyIrdzfEMUwfGLttQ9cgUjq3O0xfvbxOHHkgeGS13AdJQpIu9PFBuH7LvIsqhjTIzJXQE3gFDV7Xk2PEN-6-sxzA5jAogbSphIVAAyX71y6KV2h1M68_dQQUjoijLKzvNwp_nN5kDYfSjsHlwuNh_dYu6hwVqZRxnAmosoGqb3U0emJGfKHvtklowjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YF4xhLHUHLSIoZoE5HEACZ2-VJASx_w_H3ZBd5oT35vBoR1lHChbRmkO0mX_TeNZ3SPNRxD4Sn6WjYFdsgrBqCcvOR94bb3RBa4nR-EgfSOFGoLaD6FFxH8f4gznFmVjwVphYTna0jam1-Cpx4IZPoFVenctxkYL_gJ095ATFpaDMbCxUNPM7Sgt3dJwWR_Zfinq5umc9ULL2-LlwXa8VRVGsZ8LL10RQ13diD3k8Mqn85p8uzW7Jc6Y2AN4UuwOl_x0yCr0hX2dCbcNnuHD3ApkE7L7pARMdMdBHEy799B9wD9N-65aEnHbIJ6t8KHipd7qcElrFGixNyxaRSY2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/89888" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksH0XXlzCXloAG-MP7saRpKzGIYTxhP7RSy5rBfrPHHLJdsQEQVPrnnJ5dXOddz5dQ3M7sUWl7vq0wO84IWILswPs-yIAyhN99x6hyVu5SITMqkHSKGjgGgAsJZAaNQ__20LxL8rHTMqACYOx87GUhJay2lgm2ZNd0-8xgqMCxaBOOKt90vYImdNVXjW1etE9gq9ZFo8DFqYAJt1uvBiNiLIC84qlDqgbbGaGeZXww4qAHjqc43wX0OuP4QyELr0dvTYS3RGys-bxYksr3C8wcqfHmx0CpZDFYhgCHm_Rh-NSUio2xGnfaB_9tVVvQFP-cJitBWiVrzuXpRSLx_wAhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksH0XXlzCXloAG-MP7saRpKzGIYTxhP7RSy5rBfrPHHLJdsQEQVPrnnJ5dXOddz5dQ3M7sUWl7vq0wO84IWILswPs-yIAyhN99x6hyVu5SITMqkHSKGjgGgAsJZAaNQ__20LxL8rHTMqACYOx87GUhJay2lgm2ZNd0-8xgqMCxaBOOKt90vYImdNVXjW1etE9gq9ZFo8DFqYAJt1uvBiNiLIC84qlDqgbbGaGeZXww4qAHjqc43wX0OuP4QyELr0dvTYS3RGys-bxYksr3C8wcqfHmx0CpZDFYhgCHm_Rh-NSUio2xGnfaB_9tVVvQFP-cJitBWiVrzuXpRSLx_wAhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=iEa-hE0P6GhB7muyjd8Lrf2YsRzkf9DaAFaoct6nkgEJYzSsdPmMQVQgRsSsywSNL_yOKvuPDTpTxzIFYRLjKMNbmWIipMAB8TT3_Qb94ywGp1kUO9qv9GGeB0WijX1swCczfr0Du_6LG7pJoKZ3kXb3a8CzuqpaT8F4KdS4mTQzmlkK-JKaYTCLIvciO00VLV6HIqfhi30OwE83EhSRY1vTWhMZaTUbr9xRovl64Gg4lAvKKl-shOgdG2H5mG4MMEs_rhyYG8RkRMP11cIBAJ4l74sHsr1cXNm-Gdn-X87fFk7VuGrJRGd69fkd_QDzZK7ldGBSZLmHpSjM482OWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=iEa-hE0P6GhB7muyjd8Lrf2YsRzkf9DaAFaoct6nkgEJYzSsdPmMQVQgRsSsywSNL_yOKvuPDTpTxzIFYRLjKMNbmWIipMAB8TT3_Qb94ywGp1kUO9qv9GGeB0WijX1swCczfr0Du_6LG7pJoKZ3kXb3a8CzuqpaT8F4KdS4mTQzmlkK-JKaYTCLIvciO00VLV6HIqfhi30OwE83EhSRY1vTWhMZaTUbr9xRovl64Gg4lAvKKl-shOgdG2H5mG4MMEs_rhyYG8RkRMP11cIBAJ4l74sHsr1cXNm-Gdn-X87fFk7VuGrJRGd69fkd_QDzZK7ldGBSZLmHpSjM482OWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idVmucEXXhDF-mT6Ffg1vjVZczrG8aUqrj4JO_g7HFoUA2Zy90OCnR2dzvoUoU1-6z49Sg5GETU4WE5Cgrs61PR1eNo6wUhy5nnkq_M6SfIUwW2UAkc4PEQIIxhcn-rj_LmM8XKq0dJkdQI9B-ilMDfr1oYxV3nNQpm8EOLxrx-CCFcPZplIUKg-ZzoSmyhM7xeg-pmhBFr2Q2z1R0O0nKd59yz6GuhchmEE-g-YY2OYWsG_gvPzI5QOtZjbP3CG5X468UTcHTWJmOoremoGrRYp5njq6xebR_RargD0aWJ5DH5sin3_LIJZ9EfMI1xaL0KvFV3bXYF607YWSgNV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvh_N6qD22EL6F1GjueGiQ54XkJEHqwFhyc9eXq08uLPlLx2roy1SDCjCRJffVw_3uE1cow8Eotkrd4sI2YqK7ohCY46Ozo9sJIg6vFQf7xpWuaPGE73QGKziQFbOJy3gxxzOcmAr7fnkYGr9Y1yCyEvAHXDI4SSJR2xQyET0l9Kg5fO21WHXL4OTvijdODHO7BCWSLdkax8GblJ4sFX_nmWs9XRvom8Gx7kjPfiFMmhK7lLjskJKMFoCNFojtJFBNnywb0E0Op1uBvvYT4212yF7z0LswRL_pMTwhymUJy07p_dnvr7ZNJsFQFdHJOZljAxn7N7ZvJ1iozEBTxpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNceR-wzbYmCyiVIV34ABBrUoR-v4tsGeOWZM0KWn8Bd2tKJenAHzv_OiDQCYAOasYXtXKeJzQAgRIu5jC-xDOSl_8kBvbVzqBU3yk-A-MqQK3Na90bMO59bDzF48cnr2fE2IBPsKNB-HdDjzznY0t0719C6B-q5Ni6LORCux-PSa599ehfjkJYYtMy6uMoGQQbRcPfSgnzKXNJBPsFFF7etpeQyfC8lEIH1LEiGaY3Bmb_s6SPsCTTyRMKHH5S2ZSGH3dFP2YYYManZO0yzgCpywAIpgw1fOGkEu6cr-7tV0C7D4xkFE1fAEKaSTcCoXQDYScflNfo5xeugyhHOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAVR2qr0si4SUDvGf8MGEytf3GLwiH-nQhePwBRoQ0YX66E8WzMylBLFF87WhFCk587hPFcnX965ll0OjOyEY70LUON0VxniYQM4RjVpkg_VSagYUHyHKvlqFt4posZ8hDUEJl-sXQmNNd20AiWivHkit1DhsNzLOK6qtPgMAba43mYY05_pos_1cxwhn5YmAVEzIrogaN1zfTiZBKkpZLA44dHb4JN-ELyCaktsU8xrsrdZDrHEysm23q6h4HxrUoMHXsOKuf-3pCv3yq-Co2JwmA96PZA73trdvjkSn9kk_wLgO3xIHV1Zbi_Y7Ibaihowc4GJf0LvSfao_Bp30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4CUlrLSSpq_rjrhJ1rurEPt0MnoaNHt7aOpReF4lLMUcU5-69OwiPWYvbiLVS4e3jmejzBzytPAebhC1el1oIZ54d-vBiV3G0ZbpNa-1ZgQMRnPUmhRcK3hxLYd1054BQE8nNuJca343DzpzNRfaVjyuZNQt0vfx-jxyIwc8CLekbioH3XboCZroM218ON5FZXo0XYGozqa8RXi9lU4XPT5TtwZjgWxqHt7-3z6yYP9WFrZzkc1YFNVXqC9ln5hEPZFUl3QtG7TunENDywDwJDE4SGjTNAU9aqLBRl37-7fgNSBi5iHzrgS-Q8CDBbofoVjqUGsGT9TUKrbW4EZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJPDBwWMN9XaLmx3ajiZKTa7FJp1oGKlrUccdDJNu2Jl6e1UNxp_fxFUdOGneEjPmxhcGlpbNFqBtneCsn2bjQsMCn4iCAaBFPaEuIX3RgzWE-YJhFuLu3y7jvzLBwINO5O8asqieGNdIvhOgxtAiv_G-JHU7LlX9igDjXhqQUmgBny6xznpt2zjtMz26KaZtVS5VyRdTSerAdhoT_u8v5ogcOHvrKqOt6jmPkfxRmy-9nraVz5FqX73ZL0ri8alw5unPERDSHS4rk1DAZe4M9uLnh9KGPjROBIKSNlL_MsbtI50X8btt2u_4uxiQvw6VHarkA73ToLYQUiWJJsimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-gXXk9PgOIsA8HVcmoY3oAO0lvtvHenNGuzH61Rsp8v2Ms1-WMTM0J1qsv9FHzQvJIR9Qjxz34yk96Eww3Y_Sc2Y5MoLaTqi53LonYQSY23xNqSO6a7ctCPnf9Qdzv4FrQn8FIp5nYBaCLxjbqsWznyKQjBAs90Q_uY_95pNP2udhkW1ccaZnz6AL3G-XeXIIzUTaoue9Ia1KOJukG9_ySlsopjuVjLFJwA7UUL48kdpKSmEcbQaFOwOX80iQRjOyj2ECp0L1DiW__ZjUSvVJFmKtskKPd_YqHfw-dcMJQYMxhfzpJf3_bBcZx-Vv0_UDr0rqcAQIodQ-w9ELuBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klyboOqUL3FMdgpblny6SkHjCkswMufNuC50voOY8Aj6eOwWncODOwOyhRXdCD0geL29kU9DqFVTgNKsd_I0uyv_kJbit6_mQepKudqQ5b-_ZGUDGM9YEEgP2uWD1FldlRTDm8dxefqorBcSxcGSq5i3vXXK5PocYxZbvTUU7LLz26cZVVS2yv-HJoUVPQqoibS3e6aJUsgRljDWRi0jvNYFCOmqZ2OCF8TjBdt8BQJtX--72lEubaOiXMPOR6Unx5YxXqUaR4erSnvF5hl8te-zWI5eQnRc0CFuinhEYo8wXCy0tILSzHfzFW9aX6Q3oN4DF293sQV0CgnCzhpBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek4_9ILdysJYSUBmRiN0juijyrb0NiE9vR1-xx3ca0rPGU64wpN6NjSjY582ByWif0xYumXFcsk0kt8dOT02gNn2JfdU9RY04Fb-yzuMcU1dc9xRU570lNzMdLe2Jhj0ob21ePdwAXIzhmGQt7GXeWLp5UYsURTRVuWYxfM2NfHvbOa2wzKuZFPkLWOG781dzgKvBjQnYX-itFU1696vCyH3NihKue-cI-WlVZAE4N6bdsgCV-bHnSdlX3woTASAVOw4WZ_dxxIPQnDvN2wV6-6OXLlG2wJXAZKE1EQ2zfXLEPCijWaeM2u_Mfs38KzAUdW13rvQKMIeo8LU5kINiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7fgxJzWqaaUB3Wyfocx4ALYSIH6N2VhxCYL-WzjTXVZC2LJl3U7j7kc7M0dm19lCSQluUpsLLcZMO4g0hFEKnoKS57YuL1P8VUq6SEv-6prfKILOvANHV33vohZu19bzsZgt4RJlyU4J2WdWaHRbuZE9wuQ7j1YtCGo5ScxaRKu0re9aS1WGeGb5lBKBDLu_30zDR7if--eITr0I3tgRprXSU78n16OfP-9-SPM3Vt3g2Q6IUXsJmdUa2hbUAvJIG6ieURRW99jzdMKdEUICriqBSSDJbKNQsmyaKn5Oxx4hiGspwLJ9g76INSAx7TDKBK57apq1IEcsfK2EABSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LihHPXRO3LZo7lHmq-o9b5ISiFnF7h7GOKkYWcWaVOXnQkfwPRCQhcXy7ETC0-WEmtMcRvUAF7zcbZkT2YqINjqcGhLI4dtPh0TX1GFhDI3M3LW3fmlhEeHLZ0P5XVurNRvhMGYhP8nLyuL6QgUlkpqP04dYXBZsvOOsy-0Y2FkTosGBj6M4bzj_s7vi3bJnO9AIEV8XmYOlVHKdBCRRk-4rDZIHWhyCQqoyk-D2hV3pnpFpAbtLwt1SBsvuGW2WakdFKF_x5i3E-89oVvWmpyNJZ0AZOJEU0obf2rFyFUs-O7gF-PoHZJg5smlKnyferPkxqG7RNFcwyqYPyas8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89873" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=mGnEsopJoPYYjtied3WdTX1xC00Q9D2pXanu0vZoVLA3J6-dIsssAPrzNu0q-0wiYBN_rqCd6SzhAUpvOvrlBBh-qdW7x8BTRaACb6NLv_Cim-nla-nzWM-IBS_kek6k5QWkpshRBGR9VDq8CoBSUJOcxWskZAZ846BWogOQ4-y2Bq8Zk99zRkyRBeLXNGiR1BuaNCIw97dREC0sb0rFGObu7zYVMZMhVpIThLfO4maPfQBpAeriMBEU2MblVp0HclGbpWg6JRTP9hpWStm-3MugOziPjvztR6gC9XXgZFaBYJRaoxdC0JBfXxF_YuzAkCPuCIvFjHb7-Lg_g94ZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=mGnEsopJoPYYjtied3WdTX1xC00Q9D2pXanu0vZoVLA3J6-dIsssAPrzNu0q-0wiYBN_rqCd6SzhAUpvOvrlBBh-qdW7x8BTRaACb6NLv_Cim-nla-nzWM-IBS_kek6k5QWkpshRBGR9VDq8CoBSUJOcxWskZAZ846BWogOQ4-y2Bq8Zk99zRkyRBeLXNGiR1BuaNCIw97dREC0sb0rFGObu7zYVMZMhVpIThLfO4maPfQBpAeriMBEU2MblVp0HclGbpWg6JRTP9hpWStm-3MugOziPjvztR6gC9XXgZFaBYJRaoxdC0JBfXxF_YuzAkCPuCIvFjHb7-Lg_g94ZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHMhpe1WwZM0EdSgJP_IpR-anuWyc5wxbxwx3SEoy3JuI4oiSvKbfcnAu-suD-KaSIEnDER99eMmjRwQWkTmdufEAYHB9z_SAMwLxOLCA0L0VyT5iAjZ7BypBpTknZ8B7UtVzAU4NrFZ1sg1UfLvoBuhf3EWQ7YkzeUCP_1V9eoKB4PqQOBHTiDH215tVxr3dmee6emV7rGUsuM5Q8T-j8TyabFCHuxGxGr62Q-B77DB6mAHjzoDYAKEI8-3DAuHb8dIh7dqC7_YP0-R5rAogorc3UBZsKBZ3TOx2ZyXBodpafaiYgnqVvNLYZtLTZw2iJWjF6hgNWpQ0aaUQQHr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8OcktYar8C5hsPcnVq_PPXWLm0qtwY_zPRLkEGm1_BhL2SP5D_gcxylCKSGtYUbAEC4dO8JF4GMeVz_ieCiNGN3Aw1kkZ6sw4XADEIIyO1Uegq-xXR6AuOlwA6Bd0iYo1bWT_FBpD8kotzufeAdR6ZKyAxOwFPjc5GhHbFDpmc1-_EYinVMS2RRNuDLgaqHr-kOxykjV7oLkVdhdWFuUKXWrnMmIX3MErBlWFRzu6YBZNAt3usPSFhkJXQmpJ7nN_p9BM2KS-0E_WKWwcHibJBgM6Onn9ALj7vJVgJ_05xYCncyHRlJ5SJHDNkVnwF6mRIn8t611rBjVGMxKi0yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpFzmKDiOLcvAaaY39A5LyF9eb9fpWhIhrmb-K3DFrA3dHgAcPEgvsABHbFViHHjzhb8Ku7zzAtwDiPv-b_7lTJXuQEgAaSNyYyIW6VzDhUvoSdjQfQ8NWXz0GkQNJkk3TI7kWdvHlF4QnLTm7Hus0lzgLeM9KNb3tOceGQJenxa1bQ4rSLveXD0g-YdV4IM4XVZ1kd3It07LKiMiH98R51wwx1VzJYzuBUKVEPOQnAymrjcs0QjFb2bsHw5wynxqolneO7RgIMc6qB8kR9UXOYUyxqh34AR_El4nrlWLr3CjEZyYo0ZRaGXV-ST4eNm2_JdYkvf6qZ3wThJtNBt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCgi_IKNRCu8N4q7miD0sS7a6qCdbbnzj_xucIdshGXBqGnxWApdMWwsnHoMf6nLQdDEjPDHQemZ0HVySZ6068HJV5im2cSYxPUi5hKKzdO0vVAyftnAivYxO6vFCvSBFjo6Ds-y4qvt1stNE4AgKdwdYipVZxM80cYAyV906A4nNGc-s9yCBs407LE_iw6Mbf9GcDUWzjrjMpB4D08c6B0lLvnwcoK30WiYWlVKnXPm2gqJEVxKSXGyHT_PkA94xQXKF1ZQREhokMV6LwVgTvWdiSZNpE7PnH_ih1zHb-esdJm-oP8sIJCn-AcMVv813rGLRMisUrBg25v0VufvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afGZslFm256TkmZdzQr7n_0Uc5Oqipvu0BSjslMhNvIxbqQty5IGylwSwCepLVAk9HDszWPG6ouAW654r7WTxfxTepJ9vb0MQVxoLASlJi6GDyAnSfHk5anSFq_3lg6CnDYkf3eABZ7hjBmhN3y3Y27gu1JO6OvRJDHbCgP0uBtRvKEmy0n77_ME8WsiMRPvKm8DX8E8FDkAsN-r5_9UtGRe-9yCI8OfzZ0FgCY24WLI1r50DF1DWVd8vLlm2C1zJVePm89PYVBQnQpwBVqLb5PCWE3R_1_SXJT4T4eGDn1OBQCNoVqCFdH5OLFgXMqpK2cO-yfxcGcG81Qx0mR5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g81NyykT7HNVA2RdbFp7Ks_c9bxKhblePdMjIgnc-KCOZduXNpUsK2CUA8I0aygeyFhzZstzwFhmk8uC-mGre6E4ocOw8TnKM2UVeMI72FoSj_bHRiU2TLzNOZvVDU7NxnLV12cOARpgh4O_gL77ydamlK4qB5ebYuVRXLx8eEBT0yXRBqdtpK7CADqYbmfCi3ul6ncq9oBuV_upk5Ho_XS_UgQWLgD7p_pFRedEoqIQYu5t23Z24AaiIM3uqk92ljENRmoknN7jbxXEkjDYEjY-zgAzhyq-OKlmhvUWnPDkU6zn3YnHLoia_9up5WaC5Xnw-9vNM8DeegFulmqLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY9IVQn_biQH9B5RkYyDWeaUbEoCG_9ODeX03fNFaXmdbNGL1Fri1aSIOZ-Pl1voHC0MDcW3cwFl0rfSasW9cv9fxWWDPKRosrEwPyCsvpkQi-zlBTMXu6FCUlHwL6vsyECeRDT0xR_hhXQroDh9Y8Bnq9FYHM_X8tg9cAp0L5zA4A7LkU-FPqSO6p5PX3eJMQIGHaWjHwmtDjiwC1QLwlPOjEgtlxL4vmC3f4RW5b7d7kCv97yfj9uDzq1dP_KQhrVT_JED2NRhdsh5tSZNU3sNqnKSS8-Ejyj-K0VdxQI0A_dPX0qyWWob2AgJJaQlU3qFOsjPWpCilpWzcozAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvhQLdrVuq1BNWMiLUWE7TWA8YAP7UhRYdBQkKjSMFMi6PUwVDNUX1Mjay2LKWqiWVUem1axwk4EBA1AYWHg5c8cFXGLeO8VeNF8AvnwTN_HaVxCWrI3kq9YX2TpChGu94Hdz_w50BUV2HnKDExjT9H1r2nDRGXYKwAUB_CDozqGgdJ4pH9rbEwOG-c4lD5EQd3A0cC51NVtGWkz9VvDRTBES3nXEWeC9wxrz2PwzQFj_ZUgsjtJKeQiORNoXCuDXxWWRDdilWZpIdMtKNG5hiahZRY6-W3c4v9ENxmiS0DNO4l1bcYpaxFNEpQu-ly5crdM36W7mKxktY-SJcbshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thryXvQLYDq6afy7BuLyeyUQMEbx74GIThLGm6hgDgTQbm0V362JYs1rYhGzdnMeRXU3sfT-V0exaCvXC2C2hzNpw__qK3mLN2dkuKcWEGFy8Dp-gZ2ob3dJo8RJ2hqs36BVBfUc5ATTd3bzZa8buVT0H-nh1b19yHD3CSFbbdd01fHJYMzk3Df13ZhMXf8QkaCoNGWn0haFR2sLaOIoaR_V7YZ_Lf5WqUQKYkbAtHt5Bm7adSrTe0y89RzSRB7gYJ0N1OD47gGUkeKN_q_isWNOOGa0guHP-1v-HZiU-2YUTR7H_kZO7h98oKgp5VakSCDjP05Rt0Y_1ziY-_8JxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTavk76mGDQ5ybLjXPBKCF-ck9WdHf68LJq7Zywxd-UYHI66tH-gWs4wgn94A7N7LUV-shTtIbg01p7-iaGx5zzhmAf4n7LarHi-F17oNwjcdghgZUdLFDqJhel83fOM6aZKXj19n2QNsS_yoshskLH-KsN37sXKNYAcjHzCcsgUrBkhfxj-PuoiaiBASSFHqjmZ-dNJ5dZfBfxFabRoq-hUXp0ZnuG2UVZyhALofPrc42zrauuScfLIEVgskfe_xKdkjDhD_eRmd17KZLu--L6cm2RQR3Yi6YSwIr-yNygERoVgy9OuJBVL3DGcPJnwphuF-S2laYGbQZyQAfXbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKpBMYIGiQIV_Zfue22ZxpMbv9LkvBfC0FpulLZAdE-6IPiw81JwiMSwVvxCbSdAzgvtIOTEjzDN0afEmrzsoZ7ZfYZmXDI53qEOxgI4HoX7vDZmdsaQQoUNXWW7h-_4N6YSNQH2eIRUPxblkwBa-ZN6rooDPaOS2A3WpaizdQGZ5MhkDH2fnpHEBR8fQwA3sheuZMFXab5XgsxG_mOUSrNh7OMURm0LL6ka2Hg58V7ntQrjf6hgBeKH0RZATSUqjScZDBcctadbCgq_vJllQDFDUvTjrjsIa8sfEFCsi0TN8-SPg8CixJHCJjr_EA79wAsyZdlpI4o9RsAu8cGIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=mTV2xVK72DX45crFRQJiP_KcGNu_MxUDmJ26Kd7oQhFRo5AulNVYsyvPjCiQZcJftkNrr58l7S6GMqHeV5JnIZQwv1PmexzinIfVcPwNMCOn4Owb3G-MIp_x-zltR00gPTORBRdnRS5R6ZK6CWLvRE6ySJ0OAElv8I4xwQoeOQkzZa4YtBpaYl0WDBLxOA449CXNQ99HzHh415zVbCkLVl4JoY0FEmtAO_f4ZyqnP9I73vF_6Kra_6II_gtqeODqnjdviSIeJ6FeaG9oH7OHBlqujBn38NMUFTZADPJts1mhk-PLo8koR1K0dxl9NovLr5NY0HZtdd6q8DxKSZDLqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=mTV2xVK72DX45crFRQJiP_KcGNu_MxUDmJ26Kd7oQhFRo5AulNVYsyvPjCiQZcJftkNrr58l7S6GMqHeV5JnIZQwv1PmexzinIfVcPwNMCOn4Owb3G-MIp_x-zltR00gPTORBRdnRS5R6ZK6CWLvRE6ySJ0OAElv8I4xwQoeOQkzZa4YtBpaYl0WDBLxOA449CXNQ99HzHh415zVbCkLVl4JoY0FEmtAO_f4ZyqnP9I73vF_6Kra_6II_gtqeODqnjdviSIeJ6FeaG9oH7OHBlqujBn38NMUFTZADPJts1mhk-PLo8koR1K0dxl9NovLr5NY0HZtdd6q8DxKSZDLqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوممممم بارساااااا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=SHbcECtUD1_-9Vh-qzC_mCWGa4O7wolMzr_b7ici_QZjXpDJPN9kbepahFcPdOnOzD5XnVsM9ks32VUA0E08XzHWOuHivGGvNkQ1STeb4luWFUexFSYCs2DK0cYjcTpfVNBbxISMpQssSAQicNq_IlZ8_q9LYJDQvbjteb7_0SQ3SzmxHBrg_oO45ujzEy-lNhBe7TqEe67F8-DV7A9iA54da_X6Mm4rFJyp3ijSBMceG5b0WBQCPbCHD50t5zlNJjw0sc9_oSWgcOaLxhrDH9ZOCTGqQ6AYVmW8SMotq_Eu3yQgIidLm_Ow7hw1sBS5qY173uVU1LDhOa-Tis0V2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=SHbcECtUD1_-9Vh-qzC_mCWGa4O7wolMzr_b7ici_QZjXpDJPN9kbepahFcPdOnOzD5XnVsM9ks32VUA0E08XzHWOuHivGGvNkQ1STeb4luWFUexFSYCs2DK0cYjcTpfVNBbxISMpQssSAQicNq_IlZ8_q9LYJDQvbjteb7_0SQ3SzmxHBrg_oO45ujzEy-lNhBe7TqEe67F8-DV7A9iA54da_X6Mm4rFJyp3ijSBMceG5b0WBQCPbCHD50t5zlNJjw0sc9_oSWgcOaLxhrDH9ZOCTGqQ6AYVmW8SMotq_Eu3yQgIidLm_Ow7hw1sBS5qY173uVU1LDhOa-Tis0V2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گل اول بارسلونا توسط رشفورد در دقیقه
9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFY0RcrzUoJN3dTkzYr77vy4_RBWWGaLBmsBpAv386gwHpboZp-6KglZgQoqKkR4-40uV1SYKZLdsWzs9-BuJXe01pBszTORXpmBmhkG5AmrkUFiTh-ku7IjsVPl9DVctk2az_KbA91CmyjjvzGI2RUy0cujPAf5nKqCUNz6xJ-AvU5NwGvkUjAB16nWGnMyNSbOC6sn1tBmxILvGBR0XWg2_UcaiEjb4ydVbyBWB6ARhun8bo8KRCn_lQ_H44bcWGtyKatHWAKYTz6bwS2Uu7LdMtxBQShjCdfU6fPTXm9-mK-HD88axVxmilhbDLJEhxdG2XJRPyuI-SvycudSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزيدنت ترامپ
: ایران ۴۷ ساله داره با آمریکا و بقیه دنیا بازی درمیاره و هی وقت‌کشی می‌کنه!
تا اینکه اوباما اومد. او فقط با ایران خوب نبود، خیلی هم بهشون حال داد، متحدای ما مثل اسرائیل رو ول کرد و به ایران یه فرصت بزرگ داد.
اون ۱.۷ میلیارد دلار پول نقد هم با هواپیما فرستادن براشون، کلی پول هم در کل بهشون رسید
انقدر پول بود که خودشون هم موندن باهاش چیکار کنن! ایرانی‌ها قبلاً همچین چیزی ندیده بودن.
اون موقع عملاً احمق‌ترین معامله تاریخ رو انجام دادن، چون یه رئیس‌جمهور ضعیف و بی‌عرضه داشتیم. بعدش هم اوضاع از اونم بدتر شد با بایدن خواب‌آلود!
۴۷ ساله ایران داره ما رو اذیت می‌کنه، آدم‌هامونو می‌کشه، اعتراضات رو خراب می‌کنه و تو منطقه مشکل درست می‌کنه، ولی دیگه اون دوران تموم شده. دیگه نمی‌خندن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGm3-GumgddWAK9cDMTvOSnJ58WqPd_dEdRKgiOTyxqAuGg29f2aO73e5XXutWERSAh-NVXKPPBRzHjQNN1vYk6fJWonMrmAAOY2-9DM1c8JdlLO_lbDmE7goOlsoYlk6p1Ckctg_nwfq7tdApsT-An07UE-i7KjRMznPpna0f_ZlRF7flyYiZwY0dI4bxuvIHjaKfjRFmmDM401FVOkCelaa5kIIyspXGtR9l8OBUEq_Vdvqd5M3NNF5kc-iIKu4takcvGUr9etOjkAUdllpsRgJ_nSlHpzmFydSsLcKvgKa54jj7spDZuc-FQ34a2LIj-vJM1jrSMxsFcg8g1t1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/89852" target="_blank">📅 21:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnPfDJjlyDdbZTvwFsS9mZzBpNtykcXqfm80hSWaLOMXjbtCgP-tw-NmT5HBzvdh7O-iIAIjlB14YWR_OzgYYO8fuz1BtNla5JyvHrYL0LNFiLxZulUQ3vOUXC-TZ0oWjSmThB0o49BHBJ815WzO60bl4S7_uL_u-TtlCvQzWvHjJSWjdJ_vBJJ-VSVuvwRkFmGNuAP8RBAVZt46bvUlyH4RJ6u8rsYesHy3NoWHr-2VzTClFbKS6Zw5kPrFhPwyPbQ-i9hXR0RJs3eqn7dHGMN61eziVy90SzysCk5QW3d1EH_OfppvzYNuDUvxrMOwLklruGQEGdu1vrupPjJqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/89851" target="_blank">📅 21:06 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
آرسنال با برتری مقابل وستهم صدر جدول رو حفظ کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/89850" target="_blank">📅 21:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=A2WUkxSAkeDhFgBCwBQQ5ZXIFi-neaFo4W9xnls6hQMmsX4H_I6D_n9I0Oh4wSyHPXccizX1n2Qm2ljJPSH0a_xXGaBoNMV--UmCjgCRggEQ9phiFUmsjqwrfsqF2q_4buj-QrKxBjkdbs-ArGSjqD2RjmYjGazugOMlM7KOP7rB7GxJdjYIX84YFFF7rJfHk5L00iHpM3XN2LDbiMsN28pq3bAL5Ol3mD5s9Nb88wkGBPu9R5SzdspsS8EaY7Z13ICXln6-rzCg_ey4NJXBpoUXoi_Dkd9kV7vYchCwP9HOFECUjojmvqj-EY1g3wRBC4RrQ-cvtaLZdSA2pzVWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=A2WUkxSAkeDhFgBCwBQQ5ZXIFi-neaFo4W9xnls6hQMmsX4H_I6D_n9I0Oh4wSyHPXccizX1n2Qm2ljJPSH0a_xXGaBoNMV--UmCjgCRggEQ9phiFUmsjqwrfsqF2q_4buj-QrKxBjkdbs-ArGSjqD2RjmYjGazugOMlM7KOP7rB7GxJdjYIX84YFFF7rJfHk5L00iHpM3XN2LDbiMsN28pq3bAL5Ol3mD5s9Nb88wkGBPu9R5SzdspsS8EaY7Z13ICXln6-rzCg_ey4NJXBpoUXoi_Dkd9kV7vYchCwP9HOFECUjojmvqj-EY1g3wRBC4RrQ-cvtaLZdSA2pzVWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
هوادار گالاتاسرای در بازی دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89849" target="_blank">📅 20:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57353990a9.mp4?token=tvrnn0v53dWL6o1dLOkSmc2fZq7hO3P95h9XHMfIANYsuiGddaazrfn4cabQ1caHXcbpJCgknh6OB2zxa0K7xntotJD_rPTrxNI-QgOoSeNe0zfZAOYo8LXSV5XY6-ABOQQUu2wbnf0OTh2P-UudBOonxremh27fzQM3FiMupBZesyEcrebekEihfGdJPcwyplWKTK5XqNaHPBrJ9U0tK3VTB2geZZkKag1B6uDLb1Ifm9fK8waAWIcJfmmEYqSqUNgUoO-Pzn7bqDm28HDwFIFdXjwyIB1DDVTBDRw0X21JX2yflM38KvzaOX4kGV6Uu1bAJ7xX8ZOwlJT8TkuxoK7eVWAzCJtfm6aUgGANq-7ZS3B8s-Xe2FJttuCPf4BQk4mTvPGcE-fyCMn6DYchXEP7uBpqRsp43VjpBwjp1IxyaKvqLPe6Dm9IazKTwsO3ZAMASKvwbE9HMG8JYfArPVyZTcrBSIxR8N7-5DGsI6_EulnACbHbodlmgo7PRSTnm2itkrha_G9hNas3ulw4NOrkadT8F3EP5cNSeRb1wMYw2zcbH9d9KwbUA_XAFpJ3GicJqEx8UwLFnhE8RvvzvyjgZ7K4NKcSDlPiWcl7EmfCO_vH1FiNldfyG3IdaprsrR9qBQtaX1aW_J7bi188g7kYs_ppvE0rsfupo9y9WqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57353990a9.mp4?token=tvrnn0v53dWL6o1dLOkSmc2fZq7hO3P95h9XHMfIANYsuiGddaazrfn4cabQ1caHXcbpJCgknh6OB2zxa0K7xntotJD_rPTrxNI-QgOoSeNe0zfZAOYo8LXSV5XY6-ABOQQUu2wbnf0OTh2P-UudBOonxremh27fzQM3FiMupBZesyEcrebekEihfGdJPcwyplWKTK5XqNaHPBrJ9U0tK3VTB2geZZkKag1B6uDLb1Ifm9fK8waAWIcJfmmEYqSqUNgUoO-Pzn7bqDm28HDwFIFdXjwyIB1DDVTBDRw0X21JX2yflM38KvzaOX4kGV6Uu1bAJ7xX8ZOwlJT8TkuxoK7eVWAzCJtfm6aUgGANq-7ZS3B8s-Xe2FJttuCPf4BQk4mTvPGcE-fyCMn6DYchXEP7uBpqRsp43VjpBwjp1IxyaKvqLPe6Dm9IazKTwsO3ZAMASKvwbE9HMG8JYfArPVyZTcrBSIxR8N7-5DGsI6_EulnACbHbodlmgo7PRSTnm2itkrha_G9hNas3ulw4NOrkadT8F3EP5cNSeRb1wMYw2zcbH9d9KwbUA_XAFpJ3GicJqEx8UwLFnhE8RvvzvyjgZ7K4NKcSDlPiWcl7EmfCO_vH1FiNldfyG3IdaprsrR9qBQtaX1aW_J7bi188g7kYs_ppvE0rsfupo9y9WqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جو اطراف استادیوم نیوکمپ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89848" target="_blank">📅 20:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89847" target="_blank">📅 17:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89846" target="_blank">📅 17:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saml34MyuTJ77qu6N8q5V2DhHGMTtGy2k51HQv9AvEkza8tcm8HwtIvjRdW00v1SEbKg4DjeXf2N9W3o4ArYmVPZsvZ1Hq2dL6gJqjeue7DWsPNwTKcGWORHyn0nZ_t00pD4Mt5wbCNER3l08l8oTDOe2zQSuk1Rq_x49HN4D8RGmhCVqUOT0jXEoWMxCToH2ob96YGLfu4L4sIsw-mZ2lO0jvneap7z00ATrMvc7PzBtHUjbtAwcQCKT2TZ1kU6duWVDT4EXgrK4ubWUoOCy3KNQuITqashz_S-VSoXEwPgi-YDct-VarWt8UAj9oiAQY_sHK-vBfr6wnb6z75ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
منتخب این‌فصل رئال‌مادرید و بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89845" target="_blank">📅 16:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89844">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxWJ8JIeFWImE5X53ETlKxMXCJkkMgLPHqYSUtkBr0BcbHx5XLdJ0MxR8Rc1uFEpNsm3SrsA7HgxPWXgdqYvG7gcpYH0s5jI2n0iwQqpt8U-dsLsOFgtgxRrBMKOkwpSEzFjmDv_6KZfJ2ro76tsqTXhOwI3upLSSgXf1C9yg71zFL7E2uBRc6mu_4kwWA8T53fep-PzjGQkqTFuoWgklW5IytObJAdmEGmNy4b0nKW994wR03snrm4NXM5_6Zn_JxuKCacyio3t_ftMBZAiQuaZ6XzR9q8A06U2lqokdESx7n1l9TYRtf1Q_hKUyqyNULvj0RPZW74mW9T0jHaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
هانسی فلیک در الکلاسیکو:
‏۶ بازی‌ها، ۵ پیروزی‌، ۱ شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89844" target="_blank">📅 15:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89843">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQG3tjyR-ybr7XiV8VyccfNqEDhP4RiYKIwaGww-iVRDYymYppZoGejhSFljkmckvIMhGAWDv08G2PPoTmJx8R07sxJa3yQqDHhTFFx6NTBTGz7GQEgoc77Nu6IiW5XijyaBXUVvp9c6PFUoRKLpIQ-v8EmAObM7CXYbUJBVqoM3TO5wFlXEtvDCbOFBdRGhHjkmt7IDuXT0ljYMLCzeKlQZf8OmPJ31Wq0jOPAIRewpZzLvM4Gx9YTcBV59WYmWe69L-3d6XFVZpE2jqdVLkMlFlNAThqSGEgpRTNwXuVn0Ld96nBiKDO5_81MsX45DXwJTotZrUsXSDD_56xbclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89843" target="_blank">📅 14:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
امارات اعلام کرد که با دو پهپاد مورد حمله قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/89842" target="_blank">📅 14:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89841">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T43hNgEikcxUoqQXrAAA5DDwyl64FpdC9OY4SZWUdz-3dP_4bwluAUrRy1l_hfyuYBs8YNBVhJPJKEDys_bZk0OCdbJ1VIs4rdVDvGb4go8RobRMQRbXfAeEe4pjBPrKncteBX_EQg13_kwcI39XIlI_FI7TgQKqIQ0btowPCnhXse1wVbU_wt1VdQnpfxwHbRX3obQWka4KA_mPEM8Q6wPI3yISYO8NB6pgdVjDptJNWqvrwyVEm0vGfclvjCBRXEnJwfZx_h6U2NiDehs7qwdaJlGXhP200iYquLQ91e0iDmPK_J_tpKJk6nDhYBJifqiU_OCLZpwcmphd7reu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پرگل‌ترین‌پیروزی تاریخ رئال‌مادرید در الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/89841" target="_blank">📅 14:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89840">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzZpC6mWSzxr6CJOMFEH76CdBKZUq1xthrcHKtLFj7thZX-TNHQzOOJYACNSM5RTn16ZsLial2mqQix-E1bCEBQtf08pUUMmhpH_lj2v9TfY0I5HCd_kdbv8_qmfLMSjlRDOlh8FQQ76-WZCZgAEwnSsZbnmvhJ1jtkq_wt7AlnzmXYy2Vb3SLXMP7QLVxOiLXSPWHax1IhoX5rNGGqulTNFoig4WE2_I7nRL9CmKLp9sJZMpMdUgRuUaWJTsxeYhpKUsDoUTufFjqV6UlC6M9ukPyF6vCc8E5Icv9YKp1voXnYXy96GIdcz5GfWwSDhdo_DmX-pKByuRofq-j8DNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
در الکلاسیکو:
- بیشترین گل زده: مسی.
- بیشترین پاس گل: مسی.
- بیشترین تاثیر گذاری: مسی.
- بیشترین پاس گل در یک فصل: مسی.
- بیشترین گل از ضربات آزاد: مسی.
- بیشترین هت‌تریک: مسی.
- بیشترین دریبل موفق: مسی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89840" target="_blank">📅 13:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89839">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Mmi1P6NR5X6NFCsvNu7WVJfUZA3-jihh7W_sT-NcYUpISs9-BRfFsoCxAP7P2M7TLjQ3S_GLbHJTzP8aInlQiM6BrRLonAUamgDdJR6aPWMzpwK6DsSN9-8DtH0OkdWHxAinKLKGcLAVUPlTH5qvb5Xg9xryS0B0jdYErKXwN4-bjA-m9zhVqItzznY04s6-jngzwtXA97wuFKAK3gbjoR8XScJaVvU_JdYLHpZ9aylmGPtepGztJgBCvtiMdjUdzjh8RO83WhWWZqBONxXf5x7joYrCqlCEHv-gOoQdP9K4dJW5sRgMVTBIlcZopEGzEq0HXB2nVVPK0hM6qoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/89839" target="_blank">📅 13:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89838">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiGp5vX4yl2mlD2-VeG7xwX_2khRoBt7Zft_7bEgV9UvthPDio9V-gzTKYterJg33elE9FciCdSL0zRpAH9I3mjAX4F-bxWRg0Zthx0KPt8HXKJVKxkXObfsMobcQ_yyBFqW_2gQsBL0jWOO24jGxjRIrjBMgtQYdvYiAv7CJy-4iHjVRDoPvoBcxhgCuv2t3xBF3jdb63-ZCc2PlR8HdtbWp5yWndAHq3wiWPtvaf0U54aqypqm0NryK-oYHS6h-mmuD4g0DvrKI_kbO-pndkZMUxUxQPY4EagLbpxi7ffjh3YEfVzUuEx6tYq3bvBq7TawP911_SX2QrgINxRJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین گلزنان تاریخ الکلاسیکو:
لیونل‌مسی ۲۶ گل
كريستيانو رونالدو ۱۸ گل
آلفردو دی‌استفانو ۱۸ گل
كريم بنزما ۱۶ گل
رائول گونزالس، ۱۵ گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/89838" target="_blank">📅 12:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89837">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=uRzXC_fRRirRfm6qA91-dEFWLsOYstVSwv3r61PlWpoN_Yuqt_Xetyi1xkdbTjTt4dRPbJXSxyAqQb6Emz3iqXZB_LU1AD7DoWbZ3p_sZ-jpuCrPSQRdfxfvyNiRmqyqyosmqmyi_NtKiRTmai8GbS5vBNZI84puGDpO9tk70of0feWbALXN2cQgvwlAISD_M-MWpOK9SGckk_wjmSYquJ0vCLkOWPBAynBBDi1rSnuyJQDcTnGstdu6NYJdng0hlOw6qZP8R7L9qNJkW7lsL93us8B-gTGMWWuth5GgAUcvX9_-Z-zxuUQ-0UpNV95oY9LNfVN4SgNoWjbNE2qN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=uRzXC_fRRirRfm6qA91-dEFWLsOYstVSwv3r61PlWpoN_Yuqt_Xetyi1xkdbTjTt4dRPbJXSxyAqQb6Emz3iqXZB_LU1AD7DoWbZ3p_sZ-jpuCrPSQRdfxfvyNiRmqyqyosmqmyi_NtKiRTmai8GbS5vBNZI84puGDpO9tk70of0feWbALXN2cQgvwlAISD_M-MWpOK9SGckk_wjmSYquJ0vCLkOWPBAynBBDi1rSnuyJQDcTnGstdu6NYJdng0hlOw6qZP8R7L9qNJkW7lsL93us8B-gTGMWWuth5GgAUcvX9_-Z-zxuUQ-0UpNV95oY9LNfVN4SgNoWjbNE2qN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آخرین تمرینات بارسا و رئال پیش از الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89837" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89836">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re21CgGS7ytcMTJySGq5dL7_wnUYaa95sD1QiFmSth7EBCAvXaLWFtbhVbQjs1JYnx2A15AfyHjtcqUAezsNvIYJqC99gourgE1zRlP09L7Uy0RYizbdurr42YIJ0_vhWu9wA-DKbdchxaOtIx3g0neaU4jg_7ZlBaMzSVZlYk7-Se3egvtwt_Kcryz1jOoCduQWyp9K9-GaM-e7G03I9Xml765CinlLV3NZ91NgFyzkXti2-_ToGi8JDVovdjWrG_eVfnCR5YEFb7C9yE7oUgDQhItUFfeBByf4HVOArzqcZnwNFE04eHllCeUdAnHflfXzqyqlzqeeq5H8Sk89Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه‌های فرانسوی: اکسپوزیتو از کیلیان امباپه حامله شده و دلیل ارتباطات زیاد اخیر این دو نفر همین موضوعه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89836" target="_blank">📅 10:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89835">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSJ3URzyhgwKtIerwnMaPBM4CIWrYZEgdpyDd-r2Zgy4a2K1zQArYtU7k8DZU1G8pkvxEMUVID5wxuLvbzYTbxYEVx2KRIQHn-Uif4pT6rffePWIMtAnesw0J1IaYK24uGYqOhO0jUM4b9GctT8oM9tycVVRMZuchYCe8wxfvSTjRFd8u2TLC24_G8hl6VRgbw9vqAXUvsdZ7L9FtyyOPIYYQnJM16B8_KSvtFoNi6BUuoGPG-9CgXuGOTVGdYUv215PMpzaF9EV2pu0R_OqDVbYeX2qprXSzbR2f9W0Zmlr8smbJoycuszJyBDpUvkk3j3TXqczpjYWYBbALA958Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوتین: پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده ایران روی میز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89835" target="_blank">📅 10:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89834">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetUnblock</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev1jCy4gqCzyxytTRZSEYehbZgCPsEqpP50R1SYU0-tq7v9BgvtI7ewmm1HylwIJM0wKYa9vTFTj6QwESaethXPtAx1eoCZAUUgb9WGYR8TQXp8OK4UucrOSb736nth2l22y1-d7hI5WX3Ume_bfECugT75_xgQ_gq_RmxrG3LT6wbFOmGMxFaQNzq7MdMkdmekIKXgoTzuqq0evDA-SLzvHWKbZQBuIVvhUZcziku8O3AiXKdn-pTqGjJH5LJGBypqE-iahbTjySK4-lvT7v68ggQ6GsSMbSfi5F26l6DAboAgoc7q4NBBRU_2SewDYYC7VwJzVqIDNqPEI6Y8dbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">[
⭕️
]  سرویس ها با تضمین کامل ارائه میشن، بدون قطعی و با سرعت بالا همراه با پشتیبانی کامل تا اخرین لحظه
✅
امکان مشاهده حجم به صورت انی
✅
تضمین بازگشت وجه درصورت قطعی
✅
تضمین کیفیت ، سرعت و پایداری
🆒
با توجه به کیفیتی که ارائه می‌دیم قیمت‌ها جزو اقتصادی‌ترین گزینه‌های بازار هست .
برای خرید و مشاوره پیام بده
👇
✅
@NetUnblock_Support
کانال مجموعه
👇
📣
@NetUnblockVPN
🤝
همکاری و فروش عمده پذیرفته می‌شود
.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89834" target="_blank">📅 00:27 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89833">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: ارتش اسرائیل طرحی به ترامپ داده که ظرف ۲۴ ساعت تمام زیرساخت حیاتی انرژی در ایران رو نابود میکنه و جمهوری اسلامی از پا در میاد و وارد مذاکرات میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/89833" target="_blank">📅 00:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89832">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7lXe1RXddXfYxOwRmuTODgM92GphmLIeGd31Un2KFs-XzCoD5l_ipPUZb-tv4KHAQQ5EHhgUuVQEOHas9Hf2Mr1EsF32Gx2a0Lx8RSlCSdl3-_0zFddehiijCuLWtlsh82eRmsbcVSQw9aGZ0KByzzQ0sLwkYHPBZZcl8Fu3nxTEhnjQAo1gWIEBwNxIaElxRD9nDIrV5C_pAYtzccR7iTiMRqVoHFdKGiUE6flxAKNG66RoqnfXbRy2pDM1uzlXiRlC52dz5QCIifsAM83bUDQoW7U9_pMk4bp89_FYaweGNhgglqZksr3O6vr5Nu5Rhxf1Y__O85faCcV9XxuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین رده‌بندی توپ‌طلا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/89832" target="_blank">📅 22:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89831">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800   برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/89831" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89830">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/89830" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89829">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تبادل آتش میان آمریکا و جمهوری اسلامی</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/89829" target="_blank">📅 23:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89828">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=JPFsxN7K2t7gIn6lyjm5ZByes2haCW8ScPuMafcjRmZE3fCsy11aEHWvy5bKfPgSd5QLYpD84ASxRI9B9KMgZH2arlKcgvUmPO64955Or8sDe2iu-m91QduNEamPzSZeEHzCcLHIYrotKPudWozYYGArbFAgrAd5icHD74HsDMLgbOBKPX18AvSfzkIDsPC0gmZfjbhZzD2juuFlken7Ww6wMbODBoWcWGbwg9kHPjouSUAJQo3zD6VIilYluQJ0piQlltwO_EIOuJUtBViD0_5ggEtGVqgWOiv3IEmb5MyVVaedyX6Utd0TtJYQJg9wBOW5FF3OrmILOmyM3dCg-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=JPFsxN7K2t7gIn6lyjm5ZByes2haCW8ScPuMafcjRmZE3fCsy11aEHWvy5bKfPgSd5QLYpD84ASxRI9B9KMgZH2arlKcgvUmPO64955Or8sDe2iu-m91QduNEamPzSZeEHzCcLHIYrotKPudWozYYGArbFAgrAd5icHD74HsDMLgbOBKPX18AvSfzkIDsPC0gmZfjbhZzD2juuFlken7Ww6wMbODBoWcWGbwg9kHPjouSUAJQo3zD6VIilYluQJ0piQlltwO_EIOuJUtBViD0_5ggEtGVqgWOiv3IEmb5MyVVaedyX6Utd0TtJYQJg9wBOW5FF3OrmILOmyM3dCg-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
شبکه خبر به‌نقل از مقام آگاه نظامی: به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی، یگان‌های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/89828" target="_blank">📅 23:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89827">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
اخبار منتشر شده از حمله امارات به ایران</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/89827" target="_blank">📅 23:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89826">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رئال‌مادرید به مدت نامشخص والورده و شوامنی را از تیمش کنار گذاشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/89826" target="_blank">📅 19:43 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 21:24:38</div>
<hr>

<div class="tg-post" id="msg-666092">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HDywXlcv_uMLTcxbmjuv_X4C5j8ZRRex8oUTFSwh-uZWfVT2gbqpeWXnAQCH7bptgCwlHD3Pz1CYFjNPI9PePoboqKzmHHB_ZdhfXbEIV0TOv6wduSteQdHGhnJV8f7wpdCYs0SrO1wmlTxDzuSM-UUbparJVsRnY18SIGwziIm2Gw8v1qPAMy2tZU7w944cuRrM_63q9BYn7oJmx7mmuB5M1KBw_ILt2nKYVKcsmVoOlIfRw7ARqAqEKu35Bi1CVPXjMU8GGM-PZNkqYB3RzL7hie_zXAhW9XjTVvonNGKB9I1Towva1sP-5AZgaTutmGwK6cW_LqEzhzAgiOP1Ohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HDywXlcv_uMLTcxbmjuv_X4C5j8ZRRex8oUTFSwh-uZWfVT2gbqpeWXnAQCH7bptgCwlHD3Pz1CYFjNPI9PePoboqKzmHHB_ZdhfXbEIV0TOv6wduSteQdHGhnJV8f7wpdCYs0SrO1wmlTxDzuSM-UUbparJVsRnY18SIGwziIm2Gw8v1qPAMy2tZU7w944cuRrM_63q9BYn7oJmx7mmuB5M1KBw_ILt2nKYVKcsmVoOlIfRw7ARqAqEKu35Bi1CVPXjMU8GGM-PZNkqYB3RzL7hie_zXAhW9XjTVvonNGKB9I1Towva1sP-5AZgaTutmGwK6cW_LqEzhzAgiOP1Ohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من آدمی نیستم که با لالایی دشمن خوابم ببره ...
🔹
نگاه تیزبین رهبر شهید انقلاب در  دشمن‌شناسی و جمله‌هایی که ماندگار شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/666092" target="_blank">📅 21:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666091">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود خودروی حامل پیکر مطهر رهبر شهید به  مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/666091" target="_blank">📅 21:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666090">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=vYnvn7z4HNWPVvMzsHC3_ATo6ZBistZewL9Cvbsn9oWBP1J9n2IKOdvxFqQEKNb-WQLogz0xu4lYarqQ3CMiKJ3H_9o4r_AQ4a8KOoKKFu1uerpx696Xtn1P-CvdkCaDg-g0QYtQGSb38h_INXJSapSA-jx8_0DU0A0TP4oWe3JZnee35iStDtLIaak_Q945pjwzWQNjOBzqIjzxn3imXkQtxTVi4vm1CWV3NzO63VeLxoHdv_DAs6lzlfBnTlrQxEVYdaYEkqpXbKB2SwXaFMo0OtQ8c3BXkSYOjaBrIB6m4pM90LmVJyD5BKIuz6niPpXIXRts_R5FUI3dgNEvvmS8hejpZKlg-Mjk1jixRvwOEqKeKg1t_rxQiNJgDLoIxJg1gZMF7JE2hsWdEiAOsvwrloQZ5q8XvvLlGMyJ92edpBSuuWYFa1Nh9KXPu-lHA3MoqM4VamMhcUpG9rj1gTWdFfhfF2o5FTYG-JE3d3V5xUq6OlSwxSsYSXZLMrE8ZJMl6PxfJwtcpZ2zrapC69C8eY_uHSnGPOv2DQMYRYdoSoepn4tu6wX3IlS3SkTd3rM6t90KrnA5iSAA_muZ8r40dln6eByEDqrqQC7eLjvv-C6cIe09P4J9c1FVhAJX2re072sQbpfFCmMq1MCLimgvXuZ4_b_sc_1-QOAvV34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=vYnvn7z4HNWPVvMzsHC3_ATo6ZBistZewL9Cvbsn9oWBP1J9n2IKOdvxFqQEKNb-WQLogz0xu4lYarqQ3CMiKJ3H_9o4r_AQ4a8KOoKKFu1uerpx696Xtn1P-CvdkCaDg-g0QYtQGSb38h_INXJSapSA-jx8_0DU0A0TP4oWe3JZnee35iStDtLIaak_Q945pjwzWQNjOBzqIjzxn3imXkQtxTVi4vm1CWV3NzO63VeLxoHdv_DAs6lzlfBnTlrQxEVYdaYEkqpXbKB2SwXaFMo0OtQ8c3BXkSYOjaBrIB6m4pM90LmVJyD5BKIuz6niPpXIXRts_R5FUI3dgNEvvmS8hejpZKlg-Mjk1jixRvwOEqKeKg1t_rxQiNJgDLoIxJg1gZMF7JE2hsWdEiAOsvwrloQZ5q8XvvLlGMyJ92edpBSuuWYFa1Nh9KXPu-lHA3MoqM4VamMhcUpG9rj1gTWdFfhfF2o5FTYG-JE3d3V5xUq6OlSwxSsYSXZLMrE8ZJMl6PxfJwtcpZ2zrapC69C8eY_uHSnGPOv2DQMYRYdoSoepn4tu6wX3IlS3SkTd3rM6t90KrnA5iSAA_muZ8r40dln6eByEDqrqQC7eLjvv-C6cIe09P4J9c1FVhAJX2re072sQbpfFCmMq1MCLimgvXuZ4_b_sc_1-QOAvV34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/666090" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb3a83365.mp4?token=k13itiEv2wqKTHC2vcS-KoVR5KeMpq8V4-LI7gaC6efcA4o89U1mJpNOsgTJShYaaTqnrNPu9ZvuV9PdAl8EU7MlcgoNpNgNu9Y6BfqEvIGNRTGKaERYewZoxXf36WDs04xTLnAxfl3GSJxX36ZR6sxDJEJHJhhvvrD5yDCnJPO1vrRyb2_Ld2Z3kghpkNpz--JGjDkGsTDmcyy6CzTFSf3Nhp5KEuL_8lQIiw6W9_Z0rveHU2GLK1GCMaPHW_x4kIlgsEUMRofic8dK-XGY_pXL6skBpEm2DAEmU9G9DJwGpuf4pVB5HjKwLmeVoH2N5PGsfiPJY4seIXQNhPlaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb3a83365.mp4?token=k13itiEv2wqKTHC2vcS-KoVR5KeMpq8V4-LI7gaC6efcA4o89U1mJpNOsgTJShYaaTqnrNPu9ZvuV9PdAl8EU7MlcgoNpNgNu9Y6BfqEvIGNRTGKaERYewZoxXf36WDs04xTLnAxfl3GSJxX36ZR6sxDJEJHJhhvvrD5yDCnJPO1vrRyb2_Ld2Z3kghpkNpz--JGjDkGsTDmcyy6CzTFSf3Nhp5KEuL_8lQIiw6W9_Z0rveHU2GLK1GCMaPHW_x4kIlgsEUMRofic8dK-XGY_pXL6skBpEm2DAEmU9G9DJwGpuf4pVB5HjKwLmeVoH2N5PGsfiPJY4seIXQNhPlaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه: امام شهید ما زیستنِ با عزت را به ما یاد دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/666089" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eb178548.mp4?token=iDEMt5UCrujCSuK7kfHG5ZjonqB-k7psW4HfmCurjuFtXhAxHIbjVxjwOaF0pti4mogIEzNDF0w92jOuBDgXaHmpPoRkPAgruAS0m5bf_rEIELAn80wzzwHBPv-ggzOKQvYjHzVkw_0Nt2Fod4LF9p4m1C3WWLlMsoIOL3lJM37ohCeZKU0AInlg9t4pgQp63kTF26z3YozMVoeKMfaZOt7DRo2GHfrJHVI46sXRCMsBUyduFgWhoL5yxPTDj9hOiU_nR4EJ6M_3334mGPTojcg_xVvNwiR30eSMLNy5bpEYyJ-mBK1TvhpLjw6uOop1HVhzXNx1BMwrcs6GJ5HPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eb178548.mp4?token=iDEMt5UCrujCSuK7kfHG5ZjonqB-k7psW4HfmCurjuFtXhAxHIbjVxjwOaF0pti4mogIEzNDF0w92jOuBDgXaHmpPoRkPAgruAS0m5bf_rEIELAn80wzzwHBPv-ggzOKQvYjHzVkw_0Nt2Fod4LF9p4m1C3WWLlMsoIOL3lJM37ohCeZKU0AInlg9t4pgQp63kTF26z3YozMVoeKMfaZOt7DRo2GHfrJHVI46sXRCMsBUyduFgWhoL5yxPTDj9hOiU_nR4EJ6M_3334mGPTojcg_xVvNwiR30eSMLNy5bpEYyJ-mBK1TvhpLjw6uOop1HVhzXNx1BMwrcs6GJ5HPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید عباس عراقچی: رهبر شهید انقلاب همواره ایران و ایرانی را عزیز و سربلند می‌خواستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666088" target="_blank">📅 21:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtyzjKDwnTM47MzqR12xlkiVU7rNPgQrm8cdW6dJXEr5NbR5JtSQb4cQky7Om7KOfH0xfh-7moMnt7nWBZsQAMhASh2aXI0kZDTx5Oq4ZdrMVQ9Bb3G9tf3HXL2RBJB-mo7NP8gFkwFuH1nUk1NfTRU3cgX2sBUPdfcV1nsDIAh8beERWAwbGUP3lNm7TfdIC_CwOCDzg6Zo4SnCM-EOER5V3LY7Jx_Ydg9yoG7dTY8Onrsj0oozoRpMvx6anxzC3Hj9Jbi7YtEV0ZuHvJk9JVEFZtAh3YZg6CEJVOAESfz2fP42kFdWlOa6_fpmCOP21NbQ5P3HC0j_iRGEfkeKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری برگزار می‌کند
کارگاه فشرده «عکاسی با موبایل»
◾️
تصاویر ارسالی شرکت‌کنندگان، در صورت برخورداری از کیفیت و استانداردهای لازم، در رسانه‌های خبرفوری منتشر خواهد شد.
#بدرقه_یار
ثبت نام از طریق لینک زیر
👇
https://survey.porsline.ir/s/3PHWMjxm</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666087" target="_blank">📅 21:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
مینو محرز: هانتا ویروس جهش پیدا نمی‌کند مگر اینکه آن را دستکاری کنند  مینو محرز،  استاد دانشگاه علوم پزشکی تهران در #گفتگو با خبرفوری:
🔹
ویروس هانتا سالهاست کشف شده و جهش پیدا نکرده است و از جوندگان به انسان منتقل می شود، نه انسان به انسان. در آن کشتی کروز…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666086" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNY4GPnDKPAqQAuPHFsssQhaN80zecMwjrDwzgOahRhIQq6F5afIfrK4QZoWNPHbzHaaJakLE6PDsWF0QVMltOM_UXhvLZEKwi6HkEjJgY0K3wldvTVRrLY8rNp-kIPyN-Rg9HXbnl3qYjUz7helGH7bS1Yvd96SG5c2Ry1xeIAuVJR3AzubORGTEebVULGIrtakwN6DaUYFZFenKMMarcHYr4sBsWg7lpx1zH2x5gc5LQu7kyhQ7ETv380mbo3fC39kmUmWlR-ueHH1H1_iSnhJBXp9wJLXtFD6qow4zK0stc5ETYLx0BeAY_7ZhlvzvmFihPoNt5uDWIqoypNYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک اتفاق عجیب برای تونسی‌ها در جام جهانی؛ تونس با دوپینگ هم نتونست
🔹
تست ۸ بازیکن تونس در جام جهانی «غیرعادی» شد اما به‌دلیل پایین بودن میزان ماده، محروم نشدند.
🔹
احتمال آلودگی از گوشت و یک رستوران در مکزیک مطرح شده است.
🔹
تونس در مرحله گروهی حذف شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/666085" target="_blank">📅 21:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
انتصاب یک زن ایرانی‌تبار ضد ایران در دولت آمریکا
جروزالم‌پست:
🔹
«الی کوهانیم»، فعال سرشناس ضد ایران، به‌عنوان مشاور ارشد سیاست‌گذاری در نمایندگی آمریکا در سازمان ملل منصوب شد.
🔹
سفیر آمریکا او را «نماد داستان آمریکایی» خوانده و گفته شناخت دقیقی از ایران دارد. او متولد تهران و بزرگ‌شده نیویورک است و در دولت پیشین ترامپ نیز در حوزه مقابله با یهودستیزی و پیمان ابراهیم فعالیت داشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666084" target="_blank">📅 21:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1594c4dbef.mp4?token=oMLPRmJVozlRj6N99nbKeoyhW0NNc1vJPtejeEWMlkWZtO78Wa34RhZ-0-PgAfwuNfgQQ9Ybf2hYrTQg-qMpjbOjtW26uWcWFQio_E86dur66zSG6BEWM3UKqmWdc2r0eFjxNz5YItUTtOPX__Ke4UFfcH9ai97yKKv2faj3SoMYzg-jYBjGZtmUrUfILtuBjr7ULwzZHJ0LptAzZ3aWh0VZWt1GebIft4wIpLX0rMelhzSSKRYMtqDPbh1Tjy5axtmtHyI3PP9NSsjA0GCfgQxfIYlkY4Vczateh_btFT9hHtvHedni4MdJ5V_BUzNZIyTN9aEu5Pr2Wmf_iHmEZGOYsuoqg2CmCHlNBv1HgUHFQtU5p4oX_pfp22yXs7e9aY0OezS_feU7yU5EvjqnUm44Aspuw21AELroBwgALAQQXMX-MWB0jZUSHXwEQpzM_EkLnR3HF3DWbVhvEJ1NhGLhNDf8WRyw55AatOfs1j8lJDI2xgczejx6jgBIg37jMlaopuCDSncenjcf6USZ9eFRje68srRgJ40KBFTxHfJryjjDnAILz5-UJCz0UdiJJqjnThkXPupBo-9H4eS9Py2_54v5JAAZsxfjLnqtr833SOoXZyIzc43kBd1770ux-wiM6UQ99pADXnlsWWjXNxQBbv9QgyhAaZ2Vn1VEE48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1594c4dbef.mp4?token=oMLPRmJVozlRj6N99nbKeoyhW0NNc1vJPtejeEWMlkWZtO78Wa34RhZ-0-PgAfwuNfgQQ9Ybf2hYrTQg-qMpjbOjtW26uWcWFQio_E86dur66zSG6BEWM3UKqmWdc2r0eFjxNz5YItUTtOPX__Ke4UFfcH9ai97yKKv2faj3SoMYzg-jYBjGZtmUrUfILtuBjr7ULwzZHJ0LptAzZ3aWh0VZWt1GebIft4wIpLX0rMelhzSSKRYMtqDPbh1Tjy5axtmtHyI3PP9NSsjA0GCfgQxfIYlkY4Vczateh_btFT9hHtvHedni4MdJ5V_BUzNZIyTN9aEu5Pr2Wmf_iHmEZGOYsuoqg2CmCHlNBv1HgUHFQtU5p4oX_pfp22yXs7e9aY0OezS_feU7yU5EvjqnUm44Aspuw21AELroBwgALAQQXMX-MWB0jZUSHXwEQpzM_EkLnR3HF3DWbVhvEJ1NhGLhNDf8WRyw55AatOfs1j8lJDI2xgczejx6jgBIg37jMlaopuCDSncenjcf6USZ9eFRje68srRgJ40KBFTxHfJryjjDnAILz5-UJCz0UdiJJqjnThkXPupBo-9H4eS9Py2_54v5JAAZsxfjLnqtr833SOoXZyIzc43kBd1770ux-wiM6UQ99pADXnlsWWjXNxQBbv9QgyhAaZ2Vn1VEE48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
​​
بلندترین آسانسور فضای باز جهان در چین؛ صعودی ترسناک در دل کوه‌ها
برای مشاهده اخبار بیشتر از چین، کانال را دنبال کنید
👇
@AkhbareFori_Cn</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666083" target="_blank">📅 21:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666082" target="_blank">📅 20:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=SiThNycKRj774S4jzi5XHgFM-HQ2BfFnL8Rp5EarxIkZgwzD2IwCcqdpFX_D6qAzFj4yzS5u434qS0WVyn2Oju6e-qA6yK2rp4XDf7DLHTlVVKpLVbkzpY7l3lGVz2lEmqQTdM5sB6KO7TwnpuKfVeHpAckG4YNEQG4h4l3Y-88_bePTYEuOca49KnsNgx3MuekFnf9cBK5MPrDuP_UOdoaTvXsfz4tJv882B0vgywZsen0b5vLwIeMM7GA-cDATUNlQNmd4iS1Vfx0YtlbGlsIysa_iE_tVc4BGZpQ3lq_6EJUYGO2ej1KvxZqN7n8lmgfaqw8CF509xx04r_3ViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=SiThNycKRj774S4jzi5XHgFM-HQ2BfFnL8Rp5EarxIkZgwzD2IwCcqdpFX_D6qAzFj4yzS5u434qS0WVyn2Oju6e-qA6yK2rp4XDf7DLHTlVVKpLVbkzpY7l3lGVz2lEmqQTdM5sB6KO7TwnpuKfVeHpAckG4YNEQG4h4l3Y-88_bePTYEuOca49KnsNgx3MuekFnf9cBK5MPrDuP_UOdoaTvXsfz4tJv882B0vgywZsen0b5vLwIeMM7GA-cDATUNlQNmd4iS1Vfx0YtlbGlsIysa_iE_tVc4BGZpQ3lq_6EJUYGO2ej1KvxZqN7n8lmgfaqw8CF509xx04r_3ViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: این وداع آغاز ورود ما به مأموریت جدید در مسیر تمدنی و رهبری سوم انقلاب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666081" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f93f1b0.mp4?token=KzM5VZ2OOMFowN0hqoyRPmRpFsxb-CGNCqriJcpIb0EUAo9GKJA-fQarSzRGjhLs5VjCSBZOQohiQAzhqbjtYX1KZdG9EHmZsNqpUgeOV4Jwz0Ec1cQXuehPzDi9qDGwMOKSRnP09-3Dc2qRIipQoolKTCqVRpyPsobW42O0xE-6K7MwFfPKhhbPPl2Wf8gelEkwldVu3Hc_5rHWluDzUcY0r4LGCgaPLk43fZGX_5bjbT59hwtNCFX8NEXDA-JjUjUI0RBCKCtoFjX7qpG6_SPSFsw1iaNz6ZFEdrmR9VYmVGvLnlVZurRTdJmaisYbboHYH9rn_pzqNzgRLscmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f93f1b0.mp4?token=KzM5VZ2OOMFowN0hqoyRPmRpFsxb-CGNCqriJcpIb0EUAo9GKJA-fQarSzRGjhLs5VjCSBZOQohiQAzhqbjtYX1KZdG9EHmZsNqpUgeOV4Jwz0Ec1cQXuehPzDi9qDGwMOKSRnP09-3Dc2qRIipQoolKTCqVRpyPsobW42O0xE-6K7MwFfPKhhbPPl2Wf8gelEkwldVu3Hc_5rHWluDzUcY0r4LGCgaPLk43fZGX_5bjbT59hwtNCFX8NEXDA-JjUjUI0RBCKCtoFjX7qpG6_SPSFsw1iaNz6ZFEdrmR9VYmVGvLnlVZurRTdJmaisYbboHYH9rn_pzqNzgRLscmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از خیابان‌های بغداد در آستانه مراسم تشییع پیکر مطهر رهبر شهید انقلاب در نجف و کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666080" target="_blank">📅 20:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4nGljLOgV2C47p8cFeTWjn7oiuTYsXbN8VDbaHntvUQfe_9wp6TNXYmp2nzwBjJpIm6EF3XvA16CgDdxI6NL9SCqbEMyq3Lb6ySd3WhIFsU-x0qolvDVe3epSFcVm-JbcLJiJkwGPHFOTVDvUex7fxBkQ2qJzACm84dNK16XBIi_E134IJQONdT_00XRCqBJ3cN-rFcveBmcBuLIq-stJU7ILmzV4YOweWV6GDj5aYj694d9S_Qxkvl3QRrAlgG1zs1bVOTAAEQihpVQLMCWlOixyeom7z5iXQUp4ON3YVFME21aTtvobBOxWThOLUHIbi7C8s5MWz9kfDU5lkttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق گسترده حساب‌های کاربران ایرانی در Claude
🔹
پلتفرم هوش مصنوعی Claude موج تازه‌ای از تعلیق حساب‌های کاربران ایرانی را آغاز کرده است.
🔹
گزارش‌ها نشان می‌دهد سیستم‌های شناسایی این سرویس در تشخیص کاربران ساکن ایران دقیق‌تر شده و بسیاری از روش‌های رایج برای دور زدن محدودیت‌ها دیگر کارایی گذشته را ندارند.
🔹
کاربران تعلیق‌شده علاوه بر از دست دادن دسترسی به حساب، امکان استفاده از تاریخچه گفت‌وگوها و قابلیت‌های Claude را نیز از دست می‌دهند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666079" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f7c19410.mp4?token=QuwH4cKZ583zcGEJ7kd5_f1ODQfQKx3LN8FsEO8X0g9s3KBFYQOwAIdjcUqIbwRUY1UFgBzdCuogjJxDWqXEB98waOPaC7jHAAa75rNoFTa8-EvuU1uKdaOey6YVvDg4j5bpjumS0-idAO5nKR_gCrajaU2Xcu22OZI4jVh7jV6x6dgmEvGKrlkww35i8mImC0B25AjimOV0zpE7wB1zOMP4u3JFabgcK-Crq6L02uKafyEBvAVxkI1pO3wFGF1oJ7TVMIEiWlGRUl3dE1n8SH2g3vdLgBTdjKyuTYq9bjDHS1X0i_FW7hYn6af_OxOr1-GDK4TQ_1IN-oQX7wU_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f7c19410.mp4?token=QuwH4cKZ583zcGEJ7kd5_f1ODQfQKx3LN8FsEO8X0g9s3KBFYQOwAIdjcUqIbwRUY1UFgBzdCuogjJxDWqXEB98waOPaC7jHAAa75rNoFTa8-EvuU1uKdaOey6YVvDg4j5bpjumS0-idAO5nKR_gCrajaU2Xcu22OZI4jVh7jV6x6dgmEvGKrlkww35i8mImC0B25AjimOV0zpE7wB1zOMP4u3JFabgcK-Crq6L02uKafyEBvAVxkI1pO3wFGF1oJ7TVMIEiWlGRUl3dE1n8SH2g3vdLgBTdjKyuTYq9bjDHS1X0i_FW7hYn6af_OxOr1-GDK4TQ_1IN-oQX7wU_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزیک رپ جنجالی برای رهبر شهید انقلاب
؛
خداحافظ وطن‌پرست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666078" target="_blank">📅 20:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74183e02b.mp4?token=AUu2Uo1qKh0VGNw-M6fSxZKSazVbd0WVl-x1iKFvkIMcAI0kfVoLAMCtrRbj93wZtdxKNwBuHH3JkXNxUzfs9Z5mFkQZKUJK0fQim0kEaj-KxSw-kf9UvqUtLdSWvN--CA1xX4l4M6qlyQVmg_m1-S8ViYC0I2B88UiJQA-oN4q5PfFdduHf2Ag85J8xhBzeXPNQBdcoLWRQ0JvE65GV45N5RJIDePLGknjX_Kr8geWced7J-8hB0El7mDjdtTm8KUGmoEiAy_UmfdlxZiCCNAja49uutTYWJq35hjXusGz0zMOy-hVJbxVQOXhNpKDG84n8cZPP7Q08L0IBEhkEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74183e02b.mp4?token=AUu2Uo1qKh0VGNw-M6fSxZKSazVbd0WVl-x1iKFvkIMcAI0kfVoLAMCtrRbj93wZtdxKNwBuHH3JkXNxUzfs9Z5mFkQZKUJK0fQim0kEaj-KxSw-kf9UvqUtLdSWvN--CA1xX4l4M6qlyQVmg_m1-S8ViYC0I2B88UiJQA-oN4q5PfFdduHf2Ag85J8xhBzeXPNQBdcoLWRQ0JvE65GV45N5RJIDePLGknjX_Kr8geWced7J-8hB0El7mDjdtTm8KUGmoEiAy_UmfdlxZiCCNAja49uutTYWJq35hjXusGz0zMOy-hVJbxVQOXhNpKDG84n8cZPP7Q08L0IBEhkEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ایندفعه ما برای شما با اشک میخونیم:
اللهم انا لا نعلم منه الا خیرا ..
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666077" target="_blank">📅 20:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666075">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادای احترام قائم‌مقام وزارت خارجه عربستان و هیئت همراه به پیکر مطهر قائد شهید امت #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666075" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdy19qGL04HMY_3pKFmT2Kc-BBh83TPj0T4i7p7ENYyA_t8qjoaS3W53WL53WwAVAUqDVG19cPjNR-ybwwmOdyy2QjCHGMluMCM9pN1IJomsuPfGbZJYKbfX_ljdbK7A4hKs6q-dlhzuP3p2xq6tb2yPCYkWt5Lynkz-OlOCLGYHQUoDFAXV2g9a6xD_Xf25JumTi--Sf22XpSUbOCVSUaiF-i042esMC0bDsNMlDWY5sbOFFPiddOOKGvRQvy8lz-YK2SPr0xnF6LPPssbg1orkjkYSAFF6Ghs6ZfKhDAneqzq3Nl0gIdi-H_GgsLAhieyw1jXKpfmbJjfgzFSUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیصل عبدالساتر، تحلیلگر ارشد لبنانی: چقدر مشتاق بودم که از شرکت‌کنندگان مراسم وداع با تو باشم، ای امام، رهبر شهید. ای عزیز امت، با شهادت تو ایران دوباره متولد شد و به لطف خون تو و خون شهدا قوی‌تر خواهد شد تا سدی محکم در برابر آمریکا و اسرائیل باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666074" target="_blank">📅 20:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666073">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=dy_VVPxwwHgOMfOp6KRjzS_p-sntVY75np38dX67n5lODxQiG7ONOhQOeko_cTduX5OtMOMApLgmhPGVqFOITmbqBgpAvTTuX7dElF4RQrFcfS_mh_otOlYBcZNOkdpxcP9GOTaS-RMvD4YjhQo_TKFy2thLfuxef1ruRI2sZW5D9AS3PtV0XV285fDWIrAWJILHOkM2Q8naDVIdEe-AjRMlAuzAlPKPZVthC5jFFlZ2X_YLj1rSglaVYMUIN1vo7AQ58TyUwbVwot-Xb1Gw1IbSpNGDSeos8b3rFWWdnmszaqC-ju3vhnYvXdUcvIj1FQSJRM43UobB8Q8H8IubmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=dy_VVPxwwHgOMfOp6KRjzS_p-sntVY75np38dX67n5lODxQiG7ONOhQOeko_cTduX5OtMOMApLgmhPGVqFOITmbqBgpAvTTuX7dElF4RQrFcfS_mh_otOlYBcZNOkdpxcP9GOTaS-RMvD4YjhQo_TKFy2thLfuxef1ruRI2sZW5D9AS3PtV0XV285fDWIrAWJILHOkM2Q8naDVIdEe-AjRMlAuzAlPKPZVthC5jFFlZ2X_YLj1rSglaVYMUIN1vo7AQ58TyUwbVwot-Xb1Gw1IbSpNGDSeos8b3rFWWdnmszaqC-ju3vhnYvXdUcvIj1FQSJRM43UobB8Q8H8IubmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666073" target="_blank">📅 20:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666072">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پیام سخنگوی وزارت امور خارجه در فراق «آقای شهید ایران»
«بقائی»سخنگوی وزارت امور خارجه،به مناسبت آیین وداع مردم ایران با رهبر شهید انقلاب ابیاتی از حافظ را منتشر کرد:
🔹
نفَس‌نفَس اگر از باد نَشنوم بویش
زمان‌زمان چو گل از غم کُنم گریبان چاک
🔹
رَوَد به خواب، دو چشم از خیالِ تو؟ هیهات
بُوَد صبور، دل اندر فراقِ تو؟ حاشاک
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666072" target="_blank">📅 20:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666071">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رازهای آسمان هفتم از زبان یک رزمنده
🔹
00:08:00  فرورفتن ترکش به چشم در جبهه و جدا شدن روح از جسم
🔹
00:17:20 آرامش توصیف نشدنی بعد از جدایی از کالبد دنیایی
🔹
00:23:20 حضور در مکانی که از من یاد می‌شد
🔹
00:28:50 درک و تجربه شدیدترین درد
🔹
00:48:10 صعود به آسمان هفتم با همراهی ۲ تن از ملائک
🔹
00:59:14 ماجرای شنیدنی از اهمیت دادن مادرم به عزاداری امام حسین (ع)
🔹
01:04:15 امام حسین به قسم‌های مادرم پاسخ داد
🔹
01:27:90 درک معنای حقیقی حیات با مرگ
🔹
قسمت بیست‌ودوم (اکبر)، فصل چهارم
🔹
#تجربه‌گر
: اکبر بابامرادی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666071" target="_blank">📅 20:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666070">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965b9bc9ab.mp4?token=btQBz0-LOj-57tbN8F827rP8DhIIiydjgxhCyujcWTcByTkkKr82zMsmHXP1CsFjwhOwP4FmF8uhh8KE_I6wBZE1obI0cIRlJw1-8y3MM7rJghmSw5NDlkdizQkkeu99beHLtqu-b9JAhQD5LXS6fI6KG_0ibXD_ruDDbdKwK3IcnXCn-hIBlUK7nf1TBrydTQ_IcxrAs-ijv37xTL2hJsD4MwxDNbe8PZCQH2G6uk_FGTkgbF0l7u6MToVM2XRYk9C5F5vI36V3piITQOsk8XRmNZY3hVrvHUSgF0uQbOEBrqCcncLgkNdFJ727RLOPCOW5uIvJ4tOdrWHT6gaZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965b9bc9ab.mp4?token=btQBz0-LOj-57tbN8F827rP8DhIIiydjgxhCyujcWTcByTkkKr82zMsmHXP1CsFjwhOwP4FmF8uhh8KE_I6wBZE1obI0cIRlJw1-8y3MM7rJghmSw5NDlkdizQkkeu99beHLtqu-b9JAhQD5LXS6fI6KG_0ibXD_ruDDbdKwK3IcnXCn-hIBlUK7nf1TBrydTQ_IcxrAs-ijv37xTL2hJsD4MwxDNbe8PZCQH2G6uk_FGTkgbF0l7u6MToVM2XRYk9C5F5vI36V3piITQOsk8XRmNZY3hVrvHUSgF0uQbOEBrqCcncLgkNdFJ727RLOPCOW5uIvJ4tOdrWHT6gaZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ارلینگ هالند اهل کشورهای دیگر بود؛ سوژه جدید کاربران فضای مجازی!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666070" target="_blank">📅 20:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
استاد فیاض‌بخش: خداوند فرموده است اگر به پا خیزید یاریتان می‌کنم؛ باید انتقام سخت گرفته شود
🔹
از غیبت صغری تاکنون، دشمنان جرأت شهادت رساندن مرجعیت را نداشتند؛ حتی در دوران پهلوی، امام را تبعید کردند.
🔹
اگر مسلمانی به فرض پاپ را ترور می‌کرد، دنیای مسیحیت علیه اسلام جنگ‌های صلیبی به راه می‌انداخت، غیر از این بود؟
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666069" target="_blank">📅 20:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXKGbGfl2tTZF01laDqPDCDGCglxEwW5ogMBMdUhkfIf_JHRW2H-ZbrOl13-pPdVE7CyIo03lm_NiNNgTcQiBh8xlszcl75fyRCkYQkmoWLb1lswzodr4HvfkGaIfy3Csvz2TDQCJ9NrZPF_m676xpopkEoWyj7GOw0z1BmN78DgVN9Q0jikq9u_po6mVc5WISiqXaHdRPNYN0rbvseiOp0wGw4i4BWpysg2Ko2r4xDqu7HwW-0XgYuVQ0evRc2Zpblis1tzY_SgCNs3lEZdiiPdaoS60rhzcdbFvqaIthbVJmFRylxyBKkVLJZV_ZZ6d8Sy4IArwnwolqIo3hAEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی داور بازی حساس انگلیس و مکزیک شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666068" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffcaee042d.mp4?token=rLW9hZPoOvBMRB-v0TjJVnNegQHAqkalfYEnz8tloxCjuvlONsIpPNPnq0cJllnXxCjhnj7HD9BG5bFojemouhXFTrpjtyvlqSCRZWvUHJ5XBiNhvIhCmRzOENDiEH2pi8_eG-_PcDAX_q1_TeKNfyxdNCcCwPU60_EenyiReRbQqZDYjWkvbA9O8Bf2NJ4GUl91aPCfKR955PFaYTyx4mSgtNnV8dnkbY6QKjzvp25sqNBUDoRZFUSHFSQkA2ry0BtQQ0TIeC8GRqP9ltSV362istBEeThzFipKaujbgQ7EH07WkRy5v-aoLAJgvRlAeQvBgSbU0xHQvUw8Sh19Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffcaee042d.mp4?token=rLW9hZPoOvBMRB-v0TjJVnNegQHAqkalfYEnz8tloxCjuvlONsIpPNPnq0cJllnXxCjhnj7HD9BG5bFojemouhXFTrpjtyvlqSCRZWvUHJ5XBiNhvIhCmRzOENDiEH2pi8_eG-_PcDAX_q1_TeKNfyxdNCcCwPU60_EenyiReRbQqZDYjWkvbA9O8Bf2NJ4GUl91aPCfKR955PFaYTyx4mSgtNnV8dnkbY6QKjzvp25sqNBUDoRZFUSHFSQkA2ry0BtQQ0TIeC8GRqP9ltSV362istBEeThzFipKaujbgQ7EH07WkRy5v-aoLAJgvRlAeQvBgSbU0xHQvUw8Sh19Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظار مردم برای باز شدن درهای مصلی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666067" target="_blank">📅 20:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666066">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: توسعه همکاری‌های اقتصادی و ترانزیتی ایران و ازبکستان باید شتاب بگیرد
🔹
مدودف: روسیه در سوگ شهادت آیت الله خامنه‌ای با مردم ایران شریک است
🔹
انصارلله:محاصره فرودگاه صنعا باید پایان یابد وگرنه فرودگاه های عربستان را از این لحظه میزنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666066" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666065">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
دفتر نخست‌وزیری اسرائیل: بنیامین نتانیاهو در جریان گفت‌وگویی با دونالد ترامپ توافق کرد که به‌زودی دیداری در واشنگتن برگزار کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666065" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666064">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj2Vvgu6QNcdFNF5UIoTbU1IKdNIBxw0-YRxfn-GMIkooUVncoXrdolQfsV3i2PKkgVcjoXu4q1_O0jn5benC9wPWY9ve8kvgKyqqDLCZG5wujYOLFfSR5Z-rI7vXI1beZemWVh89ajmm2uOFzcpnoXYG8iLAcWr_-F_9PRhNzxiKqGcRVimlsZVnRU6iE3S-76pOOa9kCgGXNtuhcL8s1OUhheH8m8iMoF72wicgmRjY-e98e1mnwp7tA2tfqZeJGCbOnFHvbkpVckkyI2u1JGGdidlt2iy4C0jWu0TyDOoP_0tCKG8sUbg7aMgFYAgu2gSMfD1Fjk-nhtXvAyxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666064" target="_blank">📅 20:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666063">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
حضور بافل طالبانی، رئیس اتحادیه میهنی کردستان عراق در مصلای تهران برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب اسلامی #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666063" target="_blank">📅 20:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666062">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb2931460.mp4?token=GpA5p2J9g6o7JxWkRjNToVUSkMtzhs361MgOBEHWo2RDOtW261ZzunQD9kVSOTEtwL685GHRtasDpDmicvu8xx04dgbYJ8x0NLKfNmziBztDNLfuGHwXu4fcMmAmwcJ2RUajXPPEazR1rWt4E4axOa-_Rnyrknj89teamvrxNyBVLsjVwbEjY3hsX4_fClMf0I7LE2l0XV2iIs4wZIcRXEkDLN56nQMLUN3gGDMxyXLhJB0X5c1uTY5u3kwWkg4r1lcL9iKOZKxRLbb0AFW1DOCwaSq5IWX-7Ivn1SBA2pyL6AXEyh2ysuzuedkKevePXgfzIPfx5E2sqNBFkkJ5jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb2931460.mp4?token=GpA5p2J9g6o7JxWkRjNToVUSkMtzhs361MgOBEHWo2RDOtW261ZzunQD9kVSOTEtwL685GHRtasDpDmicvu8xx04dgbYJ8x0NLKfNmziBztDNLfuGHwXu4fcMmAmwcJ2RUajXPPEazR1rWt4E4axOa-_Rnyrknj89teamvrxNyBVLsjVwbEjY3hsX4_fClMf0I7LE2l0XV2iIs4wZIcRXEkDLN56nQMLUN3gGDMxyXLhJB0X5c1uTY5u3kwWkg4r1lcL9iKOZKxRLbb0AFW1DOCwaSq5IWX-7Ivn1SBA2pyL6AXEyh2ysuzuedkKevePXgfzIPfx5E2sqNBFkkJ5jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سیدهادی خامنه‌ای(برادر رهبر شهید) به شایعه تحصیل رهبر شهید در روسیه: این قدر این حرف‌ها مضحک و مسخره است که نیاز به تکذیب ندارد
/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666062" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666061">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP9kMEuqW0ZwzW-qcI9VSwfpaeCdsNSl2QmsmYsSq-14a1d8LYegX6aPaeQe3-EciTmu3BbTQ7ugiGUFuapb21r7d03H2OyRmVVQ0gmGKPDpiPIssBkXi6AGEeUsII1VJBqNq_44WNi5d7wrI6yO6vBNtMWMHObY7Znj2zbuY0SbY-wf2Eu-vpmL_IfO9MxMQsUuRPKCsh2HfyP0a2iosTaxnYxmQiddi_95MYFM8bgNkx1ktTim8y98B1KVyisD6sPgrfOVExZkUol1TBQNGsjMRr3aon_lsFq0cY5LWAxM-2iFPuZwHXjRyr1jjyhu8iV-j-zNDfdt5_m1NMaLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت قیمت نفت
🔹
نفت تگزاس (WTI): ۶۸.۶۴ دلار
🔹
نفت برنت: ۷۱.۹۲ دلار
🔹
نفت امارات: ۶۶.۲۰ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666061" target="_blank">📅 19:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666060">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری‌های شانگهای به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666060" target="_blank">📅 19:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666059">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3a42644e.mp4?token=CQoCs0xaFPqYmPynPbUoy4nTc6SbE79inHd3NsZhIgafpUWHZ1wg0WKV7NAqjaHdAuR7cdH_Z2bobnFgrXkc060lJm4VNFOK0Ku6IhQ3G8DKpiP2PdxSKY08Bd5hKM-e28cN-T4vRVLsAKAqWDY2UJWyZ-2Evz2WmynnBuBvVlkSt-JO1WqqPug9ubcpwMRiJfsIzOa9Uy2Az9Is_5TUsH1136hEFU9RgW8mAwO8pC4wnuBEzOV_zexlrDZKq4HletLKTdqI7-9GKNFVMX5t8lfMg2yJ8C59Z5F_wsnWIgZ4SlXuYuMu9x1j5zDsh-PmkXIqrKgwqhWTEP2g5gQb8zIGtK0M4e8S8zvUe-BlwqhGfLgPmNGO7Q7hJDA9HC629GnWISOxuVIEbiA2LWgVb79CAQ9tNRWaFmcwr9HE3ZN9mjBqR_Ow-lm5YrgB6JGfPdcvsV1_gZkv4rJYGCYIXbcspx-xUwDZr4DdZYGT8-Tv_Uhir-9RMIl0gXbc6Ip2KdKTcq0_AoJaRUIVUgVPTSoU5O8sHo-R2LQOfSEca1fvg7Lpq0aUiGbnxPAfAEtqlHNvRD3YeJGcQF85_6ch5aR7_CNLuVhQBtbtMn4-INcPuo6ZYmq2w-CkspRb-YymkPCViU3DI8LsZNHxYSb_rjYKcRJ6NSCK_f7fJaIVuXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3a42644e.mp4?token=CQoCs0xaFPqYmPynPbUoy4nTc6SbE79inHd3NsZhIgafpUWHZ1wg0WKV7NAqjaHdAuR7cdH_Z2bobnFgrXkc060lJm4VNFOK0Ku6IhQ3G8DKpiP2PdxSKY08Bd5hKM-e28cN-T4vRVLsAKAqWDY2UJWyZ-2Evz2WmynnBuBvVlkSt-JO1WqqPug9ubcpwMRiJfsIzOa9Uy2Az9Is_5TUsH1136hEFU9RgW8mAwO8pC4wnuBEzOV_zexlrDZKq4HletLKTdqI7-9GKNFVMX5t8lfMg2yJ8C59Z5F_wsnWIgZ4SlXuYuMu9x1j5zDsh-PmkXIqrKgwqhWTEP2g5gQb8zIGtK0M4e8S8zvUe-BlwqhGfLgPmNGO7Q7hJDA9HC629GnWISOxuVIEbiA2LWgVb79CAQ9tNRWaFmcwr9HE3ZN9mjBqR_Ow-lm5YrgB6JGfPdcvsV1_gZkv4rJYGCYIXbcspx-xUwDZr4DdZYGT8-Tv_Uhir-9RMIl0gXbc6Ip2KdKTcq0_AoJaRUIVUgVPTSoU5O8sHo-R2LQOfSEca1fvg7Lpq0aUiGbnxPAfAEtqlHNvRD3YeJGcQF85_6ch5aR7_CNLuVhQBtbtMn4-INcPuo6ZYmq2w-CkspRb-YymkPCViU3DI8LsZNHxYSb_rjYKcRJ6NSCK_f7fJaIVuXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظریه‌پرداز آفریقایی: آمریکا ایران را تهدید کرد، اما خودش با بینی خونین از میدان خارج شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666059" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666058">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ امام امت به سلامت</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/666058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
ای ناگهان عزم سفر کرده خداحافظ
ای گریه ما را در آورده خداحافظ
امام امت به سلامت
دیدارمان روز قیامت
دیدارمان به روز رجعت
🎙
#مهدی_رسولی
#رهبر_شهید
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666058" target="_blank">📅 19:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666057">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دیدار سردار ابن‌الرضا، سرپرست وزارت دفاع ایران و فیلدمارشال عاصم منیر، فرمانده نیروهای مسلح پاکستان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666057" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666056">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه تکنیک عالی برای کنترل نشخوار فکری…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666056" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666054">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-XjI8SL_RXpkZ8CrmUblLUgNqGwtNZ7ZLF21wYykDydVYK2GXTUXY8ZuRuND9_EWO7ahtujSHSsJ6KTLQdyI19NNTZfciX15-OxnNc1h2OluK3BkvHXkPSOXiVxy1ROBJLnjl8s8Y9TRw45BinzoZvz_fLJrmCfVLfAx8sLufa5til2SLa8zf11apuC4hOc_toEGBBLQP-yX3HcdAMpRiadnmb7v-yc8xvzrbljxN96YH6agi9kmfDVF13JzklP_j2GXMem12cp8u2K-s1odBPgPi4wrdwa1E1wTD4lz_wsbNiviYOhDzQJaTBaVjP1QAyMWjFWrzFsVOmvviIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داماد شهید رهبری دکتر مصباح الهدی باقری به همراه همسر و فرزندانشان در کنار آبمیوه فروشی خیابان کارگر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666054" target="_blank">📅 19:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666053">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSQrEVi9keVDibfoGjDGHywNPCACx2vPzj76WFqnChbFrwbbmbjVChr_2pik4WJoNF3xLShvBkNEJSkvdp4I34bOFefuNWh4cqcmxdVn4TAK5akYvbi8jAiiyGl2nUy2GyutpfpMIWkeMIh59XwRiebI3ggW0tUYf6UFgKmi1Ol6htwFKLay8-6sdSMxsuAolEqoTEFky2DDl-hl3MtNMCwrwO8zd6-pflSAQ7anIRzmiWoaneRkEaCgA0PN_oUTbHHOf01fChwAafaSP_xxox8ENSvdfo7MeT3l49y1RtcKd_BSExu4fGz97RdocLGbVrJr3Oh4rIGWbI2sBxR3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار عاصم منیر با عراقچی
🔹
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان پس از شرکت در مراسم وداع با رهبر شهید، با سیدعباس عراقچی وزیر خارجه ایران دیدار و گفت‌گو کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666053" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666052">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4fXfNpaQblHBQ-YjJT8Ev8_IfWGqTXSCT6YvxJ9ZD_V_9NIkK92A8jux9qWaMmRDx_q6OrpT7KGOEwFw2vIAvYAXXgAwTjXQXBaaIMIhJO41TOKJNamVKuN2oW2HHaIMJrRbsmz4EK0J9FTbXNR1gEKCVsoCFMU64UdyEZyB6nEej1uWtj5Hq9HoE9UE4ZwlK0GUS-ArHi78k9s40eWjXy6AOZF-fJ7HnW2FyGlBxi96khiSRfFagRN658cuSovGPMYel5NLd0Da0Jncyy6g0y2r18Md_HTSvnbuQk35jWSiFd0CPpRU-GKobqJzVwR083pD6k_fsa0QjN1ADJ7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشتر به سفر خارجی می‌روند؟
🔹
در سال ۲۰۰۰، آلمان، آمریکا و بریتانیا بیشترین سفرهای خارجی را داشتند.
🔹
در ۲۰۲۵، چین به بزرگ‌ترین مبدأ سفرهای خارجی جهان تبدیل شد و هند نیز وارد جمع پیشتازان شد.
🔹
برآوردها نشان می‌دهد در ۲۰۵۰، هند، چین و آمریکا بیشترین سفرهای خارجی را ثبت خواهند کرد.
@amarfact</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666052" target="_blank">📅 19:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
جنگنده‌های عربستان حریم هوایی یمن را نقض کردند
🔹
نیروهای مسلح یمن اعلام کردند که جنگنده‌های عربستانی بامداد امروز با نقض حریم هوایی این کشور، تلاش کردند از فرود یک فروند هواپیمای مسافربری ایرانی در فرودگاه بین‌المللی صنعا جلوگیری کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666051" target="_blank">📅 19:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666050">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
هشدار  پلیس فتا به مردم؛ هوشیاری در برابر عملیات روانی دشمن برای تحت‌الشعاع قرار دادن مراسم تشییع
🔹
سردار «وحید مجید» ؛ رئیس پلیس فتا فراجا در گفت و گو با خبرنگار خبرگزاری پلیس  ضمن هشدار نسبت به تحرکات اخیر دشمن در ادامه تلاش ها و جنگ رسانه ای به منظور  ایجاد اختلال در مراسم تشییع پیکر رهبر شهید، اظهار داشت: دشمن با بهره‌گیری از ابزارهای گسترده و ظرفیت‌های سایبری، در صدد به حاشیه بردن این مراسم باشکوه و ایجاد ناامنی روانی است.
🔹
وی افزود: دشمن با جعل اخبار به نقل و به نام  برخی  مقامات رسمی و خبرگزاری‌های معتبر بین‌المللی، تلاش دارد تا محیط‌های برگزاری مراسم را ناامن جلوه داده و با بزرگ‌نمایی تهدیدات خیالی، آرامش شهروندان را مختل کند.
🔹
رئیس پلیس فتا فراجا از عموم مردم درخواست کرد ضمن حفظ هوشیاری، به هیچ‌وجه به محتواهای مشکوک، پیام‌های ناشناس و اخبار غیرموثق در شبکه‌های اجتماعی توجه نکرده و از بازنشر آن‌ها خودداری کنند.
🔹
وی تأکید کرد: تنها مرجع رسمی دریافت اخبار درباره مسیرها، زمان‌بندی و اطلاعیه‌های میدانی، «رسانه ملی» و خبرگزاری‌های معتبر کشور هستند و هرگونه اخبار خارج از این کانال‌های رسمی فاقد اعتبار بوده و بخشی از عملیات روانی دشمن محسوب می‌شود.
🔹
سردار مجید همچنین از هموطنان درخواست کرد در صورت مشاهده هرگونه محتوای مشکوک یا جعل خبر، مراتب را برای پیگیری از طریق شماره تلفن ۰۹۶۳۸۰ و یا وب‌سایت رسمی پلیس فتا به نشانی
policefata.ir
گزارش دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666050" target="_blank">📅 19:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666049">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtlLDRLGRjLPsbOTdUYZKsci5h-nwQQYZQo60EncZkuVHo9lAzNy2Bg_lxAt0QhOmSm89bB_URdKGxjPDku-qLeQ40KQ5hozK_i_k0xL8uSuUrqYYGISkJK26GyyVnHDlhmGmecnMlz-Qm-_ThMuoo2-qW99teRYyxakcg7wQV8PKVziPYLmqKOx_YD23tQs8M-xEBvzyNXyv91vkrGyTjTSwH2wlYT9wBS-sLdUz30DPOcP9GmxOf4-VPjmVGbt1ePQYe9vJtbORzCvA-U-NseGJS5em3JYcLj__Ein64J9IdhzDPo9HzX0W8PGIic5K78QDiclORL-wkQMxHmVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار عاصم منیر با عراقچی
🔹
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان پس از شرکت در مراسم وداع با رهبر شهید، با سیدعباس عراقچی وزیر خارجه ایران دیدار و گفت‌گو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666049" target="_blank">📅 19:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105522b658.mp4?token=eHNPOhQ3djK7DxX-zdgB8squiws_Av5xzFIi2Rzfjm_CP016KwySl7KSrVsyxfz5nM5y5ys204ZJhsjyPdXuS-cCcakPAZ6oLO7o9KhTXt-Jl-xLZTyaULq3BXf25QloUC0tWml39PsPKvDDqqKovoh--_mk1BNzH7CvyM4oiTJ6Gskbo6Jb9vDgNS7y163hrztHK3txY0LftgA73aslR2Ec5pi8Mn8nPMXJvrztU74GDCNpWtpfmoqCOu_RTGCm5DsTMNvCNbP-T5Hcvbws5sKEgyngW-aLPsLwntXsE3W06K_h1OCSGJ53fFGgJVpmfj-UmGMsPMURHCRJuTGkbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105522b658.mp4?token=eHNPOhQ3djK7DxX-zdgB8squiws_Av5xzFIi2Rzfjm_CP016KwySl7KSrVsyxfz5nM5y5ys204ZJhsjyPdXuS-cCcakPAZ6oLO7o9KhTXt-Jl-xLZTyaULq3BXf25QloUC0tWml39PsPKvDDqqKovoh--_mk1BNzH7CvyM4oiTJ6Gskbo6Jb9vDgNS7y163hrztHK3txY0LftgA73aslR2Ec5pi8Mn8nPMXJvrztU74GDCNpWtpfmoqCOu_RTGCm5DsTMNvCNbP-T5Hcvbws5sKEgyngW-aLPsLwntXsE3W06K_h1OCSGJ53fFGgJVpmfj-UmGMsPMURHCRJuTGkbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
خدا صبور کند در مصیبتت‌ ما را..
پک
#استوری
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666043" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666042">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqFoFB53H0fo5XSYqovF7F_gUEIGdy56KBYVC0OFKgBQh6cepUVB7llY0ApxCWluZw3ohRzduWPij_Sk5msv5MLju2Ku-jKFW3HqDrT2E9K6vpGcA1xdV4XADVhCwakOsrouzVWSY00VUXF1p_X1ZDKBekM0BRwu-To_IhlOeEoobdjfo2L-vNTr0WWKkgo0stdxsjs5HRY2-b72zrihJ63eTidfuDbs_rCm2HTHJ596LpUf97Ptg7iuKxLDjdSSe64-Ic5MlGisELVxKzoxSwAaGLy3Ee4Psi0_6zNzMfjPvSVSFmN2zVmPWUFr1Hfcacu7LUNkvcV-LAi7jYckMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متفکر الجزایری : دختر رهبر ایران را تمدن اپستین کُشت
دکتر یحیی ابوذکریا متفکر الجزایری :
🔹
آمریکا، دموکراسی، تمدن و حقوق بشر... دختر فرشته‌گونه زهرا، نوه آقای خامنه‌ای را با موشک، نه، با تُن‌ها موشک کشت.
🔹
این تمدن شماست، ای فرزندان اپستین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666042" target="_blank">📅 19:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666041">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
در مجمع عمومی سالانه مجتمع فولاد خراسان عنوان شد:
🟢
عبور درآمدهای فخاس از مرز ۳۲ همت و جهش ۲۱ درصدی درآمدهای عملیاتی
🔸
بر اساس گزارش ارائه‌شده در مجمع، درآمدهای عملیاتی فولاد خراسان با رشد ۲۱ درصدی از ۲۶.۷ همت به ۳۲.۲ همت رسید. همچنین این شرکت با وجود محدودیت‌های انرژی و افزایش هزینه‌های تولید، موفق به رشد ۱۳ درصدی تولید شمش فولادی، ثبت ۸ رکورد تولیدی و کسب رتبه نخست عرضه میلگرد در بورس کالا شد.
🔸
در پایان مجمع، صورت‌های مالی شرکت تصویب و سود ۶۰ ریالی به‌ازای هر سهم میان سهامداران تقسیم شد.
مشروح خبر:
👇
https://t.me/khorasansteelCompany/6485
🔘
روابط عمومی شرکت مجتمع فولاد خراسان
تلگرام
|
اینستاگرام
|
بله
|
سایت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666041" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666038">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b6320143.mp4?token=fTnBC1Jdzw87lOAfnUEZbQhoL9zWO7u5LZ_WT86icY_qnljAkg0Lr7Co-epqKW0xPw2IAIDg-a0hn9NDVuDk6JI1xS1_QHm1Vr57pEOln14Qb--_P0nJvkSqnpsl9-6dCZHwa3rsTYrrSqIIaV_l5P88h9QVPIrbi4uJx-vh96MRWEdJ8iJjLKJ0pjfO4wvpZBeBPRmwsCQn1KtTDlVKS2arfT8IcLj0ZnKs4PeqbPk5OoXOr7rurLFvFFb7H_EQsARPK1u6Fd2XUdKE3TmVtnNSauohW40h4dJWFQDKQHPp6zsaKpbG3LFzRKQ-0sRtXiWZE_RVef-KKuVpQXKqnVcZODmw0PemsQf1FFcNrIwTyE2pjIKOQNftqwLTAxPiAWnoSD8bZ8ypka91gXnX9ixE0-PZmTI_1OXWVh_duL-eZxjrtEcc0sl6Hlrqa9ktAhW5KcWvfCa5-ROovgZx43DYUWgk4efOU6zdL_dlb2xtlay7PEGHvCrz6cgwVdGezwIyzDBA_l-86rRq2d5ztZviu5glVNX-ao1saUT3vX4kEJEZbSJSoV-ic_fGXPL0mifbFwsKY8ERjT6knovK5nBxTVqx9SEWbpsOZRCZLzBZLwhidFQkawihSqKdB-24_qpGL3Kd81KrB5Xy3gFXmjRTvQWLcbq2emXMFiFR-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b6320143.mp4?token=fTnBC1Jdzw87lOAfnUEZbQhoL9zWO7u5LZ_WT86icY_qnljAkg0Lr7Co-epqKW0xPw2IAIDg-a0hn9NDVuDk6JI1xS1_QHm1Vr57pEOln14Qb--_P0nJvkSqnpsl9-6dCZHwa3rsTYrrSqIIaV_l5P88h9QVPIrbi4uJx-vh96MRWEdJ8iJjLKJ0pjfO4wvpZBeBPRmwsCQn1KtTDlVKS2arfT8IcLj0ZnKs4PeqbPk5OoXOr7rurLFvFFb7H_EQsARPK1u6Fd2XUdKE3TmVtnNSauohW40h4dJWFQDKQHPp6zsaKpbG3LFzRKQ-0sRtXiWZE_RVef-KKuVpQXKqnVcZODmw0PemsQf1FFcNrIwTyE2pjIKOQNftqwLTAxPiAWnoSD8bZ8ypka91gXnX9ixE0-PZmTI_1OXWVh_duL-eZxjrtEcc0sl6Hlrqa9ktAhW5KcWvfCa5-ROovgZx43DYUWgk4efOU6zdL_dlb2xtlay7PEGHvCrz6cgwVdGezwIyzDBA_l-86rRq2d5ztZviu5glVNX-ao1saUT3vX4kEJEZbSJSoV-ic_fGXPL0mifbFwsKY8ERjT6knovK5nBxTVqx9SEWbpsOZRCZLzBZLwhidFQkawihSqKdB-24_qpGL3Kd81KrB5Xy3gFXmjRTvQWLcbq2emXMFiFR-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
«تاریخِ جهان پر است از لحظه‌هایی که قدرت، بر انسانیت سایه انداخت؛ جای آن همه رؤیا، فقط زخم‌هایی ماند که هنوز روی دل ملت‌های مختلف تازه است.»
🔹
«روز افشای حقوق بشر آمریکایی» ، روزی که چهره‌ی سیاست کنار می‌رود تا حقیقتِ قربانی شدنِ عدالت نمایان شود.
#مناسبت
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bank</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666038" target="_blank">📅 19:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666037">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN8ugfq1IzZs1v2QgadYwzcl3gbWEMj-CGKDZ5b4rSTkZoJk76ZWF1zFIZfF_obph0_rysYVJ-A4paado1W3nUw6Fp17joMjgnjjVR_Y6wPTZvjUEQ5YQxRyiihdZqVNc_GVaHp_T-MW3hKhwUDJiZ05GNsCmpThlKgfFyUtzwV22fBxN9tio7S-Sg8915ddrTnjgm9Nbx0WD1rIvgpmE-YjVsZoGnoiFPGu8Kzd_XAIGvGzXTLLLsrYhFxO6bGY7cm5XfZ96RJ1rZqCHcKSa-53sIU1Q5nQSPUXrVEnZXGKP7YgYLSGZCrjBbR4Mvs3G-UH4ZPzLywjSYDLId63jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادای احترام خانواده امام خمینی (ره) به پیکر رهبر شهید انقلاب اسلامی #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666037" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666036">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7dd42f9c8.mp4?token=s5-vLd6iXs0sM9fCc2M41YIPzK6G7uOHISuKrc_YRBU1PaH2pSF3H3Ca0YH7h2ZDF1E3LzJH6vezhJGCSvWUAAYly4wWsl1_RAVfCISUr8Ditwj78-8gelCZlJXv2_tGol2EiVbJSKcmPeaZRKGjdbFYBs73BjA6X8JTcoSf_UnrFWtdSL2JgiDtHQe9HV5Vf9RK6aUNW2VnhKs_2tawScsiMD3-x-T_VAL5F438-DsGD7GVhLqXgvU4fF49jZ5QabTt1KUkIidesJXzoFH3nlgS47QmLui1vriZkpzlbB-Apw80wd6WagEtkTDrI-8vBm-FQYv5v0D28RnPM0lC8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7dd42f9c8.mp4?token=s5-vLd6iXs0sM9fCc2M41YIPzK6G7uOHISuKrc_YRBU1PaH2pSF3H3Ca0YH7h2ZDF1E3LzJH6vezhJGCSvWUAAYly4wWsl1_RAVfCISUr8Ditwj78-8gelCZlJXv2_tGol2EiVbJSKcmPeaZRKGjdbFYBs73BjA6X8JTcoSf_UnrFWtdSL2JgiDtHQe9HV5Vf9RK6aUNW2VnhKs_2tawScsiMD3-x-T_VAL5F438-DsGD7GVhLqXgvU4fF49jZ5QabTt1KUkIidesJXzoFH3nlgS47QmLui1vriZkpzlbB-Apw80wd6WagEtkTDrI-8vBm-FQYv5v0D28RnPM0lC8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید، دانشمندی بودند که مسائل دینی را به صورت عمیق تبیین می‌کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666036" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666035">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حاج حسین یکتا: خیلی اذیت شدم وقتی حداد عادل در مراسم وداع با دخترش گفت جای آیت‌الله مجتبی خامنه‌ای در مراسم خالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666035" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666034">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تلاش آمریکا برای ممانعت از ترور عراقچی و قالیباف توسط اسرائیل  روزنامه نیویورک‌تایمز:
🔹
واشنگتن با اطلاع از نقشه اسرائیل برای ترور عراقچی و قالیباف، به‌شدت نگران بود که این اقدامات مذاکرات حساس صلح را به شکست کشانده و شعله‌های جنگ را…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666034" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666033">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyFohy1PaEBcVZXKvwq8TFZQH2DcRO1pV2oc0TmLGsh_YB87YjLrnfSPo3ZmwsdhH-B2WqV5I4X_z-ix8QuJKKZ5fbdwIJThutb0FzERfo1O-hix12SY_ASygM2KnICgb_kcKUHT9f6ZDwxOmKexSXhqFviyYGtVtvh7u0bHjnyZXb6651LzaQrQaGEHS-idudoKQSy68JpvwDT288wBEgMr7Ef__8KuqmW3qwdEappWfsazJDli5G_sJfjZzw_DDtcl-OWY56UAvfg2oLXnw6djXwesdpW2mYFGvmaEt76JXDOdae7X0lXdhjGanisRMINReNJKhTbt9TQKx7O7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666033" target="_blank">📅 19:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666032">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دعوتید به دیدار
این بار برای وداع در مصلی...
🔹
وداع با پیکر رهبر شهید انقلاب اسلامی، حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای
🔹
مصلی امام خمینی(ره) تهران
از ساعت ۶ صبح روز شنبه ۱۳ تیر ماه
الی اذان مغرب روز یک شنبه ۱۴ تیرماه
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666032" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=rGJlttLotyGNspu_AcWo_09mhpeUD4WVseJTbAYY-kAPw-nKzn6bn4cOV602GHW_AYG6KYX5bsORw1S8QUjY4lNQQqQtTX5ILV0ngKwooyyblPX7sifp1s0cRykdkC9zz3AFMl4h71oUxEMUrFkNb03SCjBFoXN3JTuTf7pJRNIgGz6-QAXiUdqHlBrMzwpn8Cu0Q3_gfIuXxIaC2Fcs-79S0HDFu2W_v6MZYGshWgx6P4Cyb2W1totmXaea1GT5KvGM1VyohXUN0BfEtpT5Ec12EkNJOhUkU7msJsjPhxdhQ0MUSowrWgVe310ul66PlZx4xryCRIGRcf4R_GTQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=rGJlttLotyGNspu_AcWo_09mhpeUD4WVseJTbAYY-kAPw-nKzn6bn4cOV602GHW_AYG6KYX5bsORw1S8QUjY4lNQQqQtTX5ILV0ngKwooyyblPX7sifp1s0cRykdkC9zz3AFMl4h71oUxEMUrFkNb03SCjBFoXN3JTuTf7pJRNIgGz6-QAXiUdqHlBrMzwpn8Cu0Q3_gfIuXxIaC2Fcs-79S0HDFu2W_v6MZYGshWgx6P4Cyb2W1totmXaea1GT5KvGM1VyohXUN0BfEtpT5Ec12EkNJOhUkU7msJsjPhxdhQ0MUSowrWgVe310ul66PlZx4xryCRIGRcf4R_GTQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از پیکرهای مطهر رهبر شهید انقلاب به همراه شهدای خانواده ایشان در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666030" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893408b9af.mp4?token=iDCFEQxr-7EToVHeGB8yBOUFrt88T21dPBI2DMtppIKT92y1Q_Nzc6whLn_PUkhOsd5zx84OTto5aFRjPe27gS-dEXX8L3nSvTMLHq1Cvrb5_bP1YLAY5d-eItYsVwyF-IeE6MUF3Ke3qAszUwb2MnIEpzGKsTDDSOO_KKCbGI7uuNfF7wnDmBz6v1CPwjKXCuR4ikNeA5eV_fsPR5bMUdVSPRJbGQ2s9ASAqM1SfZFrlI4BkPauIILm7lprGiooI3gjsMW2HoyqWd4uqBALv-J1WJA2DL0BS94VsDP4fum_xXN4Q-eM2lITd7VPaGiub5TBXDf5MmytHrZqBlLOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893408b9af.mp4?token=iDCFEQxr-7EToVHeGB8yBOUFrt88T21dPBI2DMtppIKT92y1Q_Nzc6whLn_PUkhOsd5zx84OTto5aFRjPe27gS-dEXX8L3nSvTMLHq1Cvrb5_bP1YLAY5d-eItYsVwyF-IeE6MUF3Ke3qAszUwb2MnIEpzGKsTDDSOO_KKCbGI7uuNfF7wnDmBz6v1CPwjKXCuR4ikNeA5eV_fsPR5bMUdVSPRJbGQ2s9ASAqM1SfZFrlI4BkPauIILm7lprGiooI3gjsMW2HoyqWd4uqBALv-J1WJA2DL0BS94VsDP4fum_xXN4Q-eM2lITd7VPaGiub5TBXDf5MmytHrZqBlLOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی از کارهای به ظاهر دشوار را میشه بدون وسیله خاص خیلی ساده انجام داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666029" target="_blank">📅 18:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54cc7be978.mp4?token=qcrMd2lpBaw37NLRwSILPFOAi-hF4p94FtevYOaN81-OYxE8WY-DYQ7JhMuS8R9-0_K90K9gA1vOk-35n_p4hJiEpsS_8YbvdS7hbe-Ij0qCLs7gQXtu7o-5xbBYokmZcuGUXMycJwaJE0155ptJ76IQtKuXUUpmBcwHbBirHGw9hEAafiOeJ6dzfd7AByrYtBp73b4BPJ9nLTzzs40IA4uLQzF5dtvlxkTwItVq5JnvQ1PMgeMqRMnuU-vsWYcDd9-uH7SSN0ybAGz8kkIaxWFUVEuG7M2_64UJFRXTo28xGefBJhYcuERxmpSk1UKSlNGxKtnxLOO034VieXH8A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54cc7be978.mp4?token=qcrMd2lpBaw37NLRwSILPFOAi-hF4p94FtevYOaN81-OYxE8WY-DYQ7JhMuS8R9-0_K90K9gA1vOk-35n_p4hJiEpsS_8YbvdS7hbe-Ij0qCLs7gQXtu7o-5xbBYokmZcuGUXMycJwaJE0155ptJ76IQtKuXUUpmBcwHbBirHGw9hEAafiOeJ6dzfd7AByrYtBp73b4BPJ9nLTzzs40IA4uLQzF5dtvlxkTwItVq5JnvQ1PMgeMqRMnuU-vsWYcDd9-uH7SSN0ybAGz8kkIaxWFUVEuG7M2_64UJFRXTo28xGefBJhYcuERxmpSk1UKSlNGxKtnxLOO034VieXH8A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعه موسیقی «باید برخاست»
🔹
موسیقی ویژۀ آئین بدرقۀ رهبر شهید انقلاب به همراه تصاویر کمتر دیده‌شده‌ای از رهبر شهید انقلاب منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666028" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=HzzroHjPBD3ZSnKopPwtldhOt7aR699mPttsIeQIJxAv4ZCJl7l5FrKxwi5Q_x20Plhh5n0HaC6Uym1ewv0qIdwCTFjLMRtiV0H6tIA_bz9tVIRZOLZGVrdgwW0tKko3BHjTPWjnhHyq9q6cQYYA87NjDFRxIX610K9Vop1pMKnDXTEaI-Afp_kabHm9_7-WOnMISXrbdkdLYwQ9CDiRVwz9hcRqSWjmBMjVPT6z_dpkaJqNtAr3mJN-37YkHadEJFD5Lpr5yIV3PXQ8_OjrlNQGzBp_onLsDOsgnSDCtYPRYbLb6Ck8AzVDXMdBNCh56eWn6RXrPCOVyqd-nfF9EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=HzzroHjPBD3ZSnKopPwtldhOt7aR699mPttsIeQIJxAv4ZCJl7l5FrKxwi5Q_x20Plhh5n0HaC6Uym1ewv0qIdwCTFjLMRtiV0H6tIA_bz9tVIRZOLZGVrdgwW0tKko3BHjTPWjnhHyq9q6cQYYA87NjDFRxIX610K9Vop1pMKnDXTEaI-Afp_kabHm9_7-WOnMISXrbdkdLYwQ9CDiRVwz9hcRqSWjmBMjVPT6z_dpkaJqNtAr3mJN-37YkHadEJFD5Lpr5yIV3PXQ8_OjrlNQGzBp_onLsDOsgnSDCtYPRYbLb6Ck8AzVDXMdBNCh56eWn6RXrPCOVyqd-nfF9EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666027" target="_blank">📅 18:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e246b2ba.mp4?token=FfSJxOmq5juzfjwdf_o8BgUdFr7I_sLDqPUc0l18SJT-XpdMBTP5vAHTd6JW309EBSp_a5bVUU9F515eGsvDKtY7JYsAfL-F_4NUaQR1PN6QbVach0pgFRCUm44Tvgi38SkZRnsTNV3laZn5YGHxg-ECSs-rQFJGcfHY1iyF-bWXAtgsUiQhKF-M05t1ZwspAGjCB55CKHyHWJNeVRPtZBsaoydfJYETg964teF2z_c0Y9un1j3v8ICRSAAwuvUb0ju_I9dinB-B6QXlnae3ZY5l9Pfol6Qd40xlr_3ypW-klnfXEF-Ar-I3y7pQMYoK8aXFL4ecwpEKgln_pnS8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e246b2ba.mp4?token=FfSJxOmq5juzfjwdf_o8BgUdFr7I_sLDqPUc0l18SJT-XpdMBTP5vAHTd6JW309EBSp_a5bVUU9F515eGsvDKtY7JYsAfL-F_4NUaQR1PN6QbVach0pgFRCUm44Tvgi38SkZRnsTNV3laZn5YGHxg-ECSs-rQFJGcfHY1iyF-bWXAtgsUiQhKF-M05t1ZwspAGjCB55CKHyHWJNeVRPtZBsaoydfJYETg964teF2z_c0Y9un1j3v8ICRSAAwuvUb0ju_I9dinB-B6QXlnae3ZY5l9Pfol6Qd40xlr_3ypW-klnfXEF-Ar-I3y7pQMYoK8aXFL4ecwpEKgln_pnS8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگنده‌های عربستان حریم هوایی یمن را نقض کردند
🔹
نیروهای مسلح یمن اعلام کردند که جنگنده‌های عربستانی بامداد امروز با نقض حریم هوایی این کشور، تلاش کردند از فرود یک فروند هواپیمای مسافربری ایرانی در فرودگاه بین‌المللی صنعا جلوگیری کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666026" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=dotXLQ6pK0JY5KOXVQHRyQM_dRrcecWuETsm8j_9-OaQF5ED_TN926zPU1tS-k0wfLpo9SvE9cRIATHZIel15Vb5cSqmi_fjUVT01sJUoNp_g-fHrxLn_YJpNevC1wtm5hyEcZZCzH0SfdXmpztKT_4IUgkgUdIaKqxLvNL8gyNK__94PlP9yxO30b3w_3n8eOh5pCNDfFHhzVAmqtc79UBmKkxMLbJmY6qSJT-PcRm3E0ADcAY5tlsdChBcCB3W4UWqj5oUhFQY5cyflVwVhxrbfPLsW1EH0yrswrF-dqQg34bRy5Bpx0iQghMpHvkWH8D8aopCCfROUwv7QS1r7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=dotXLQ6pK0JY5KOXVQHRyQM_dRrcecWuETsm8j_9-OaQF5ED_TN926zPU1tS-k0wfLpo9SvE9cRIATHZIel15Vb5cSqmi_fjUVT01sJUoNp_g-fHrxLn_YJpNevC1wtm5hyEcZZCzH0SfdXmpztKT_4IUgkgUdIaKqxLvNL8gyNK__94PlP9yxO30b3w_3n8eOh5pCNDfFHhzVAmqtc79UBmKkxMLbJmY6qSJT-PcRm3E0ADcAY5tlsdChBcCB3W4UWqj5oUhFQY5cyflVwVhxrbfPLsW1EH0yrswrF-dqQg34bRy5Bpx0iQghMpHvkWH8D8aopCCfROUwv7QS1r7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور پاکسـتان: ‎رهبر شهـید در یکی از دیدارها دست عاصـم منیر را به گرمی فشردند و به او گفتند فرزندان حضرت علی(ع) هرگز سر خم نخواهند کرد
‎
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666025" target="_blank">📅 18:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=OFgMx6R3SpzexP8Mtkg0Y5FwTKdxWQVT8KthlRn3xxAxRaZ8P0z0__K_ukdrlFZZGDJfHxpiMJ4TlU1dZYDDd7JUIPPGKih3GPtofxwQY1rpngbW8SCP7Afkx8DC36XBENrLCf96LaWXINl6t5yAXBbDbJh7EVXCdIlx4EThWryYnA5SQgwk3mm5sz_3_Nqmkjrsi3Rf3bXQ9U0BwalFfpjQUJUd-eaiEJ7DDikvYLIPXzOWOL-_7sehXc2RVmpdyTLuF2rt7Opj8Q_t9bxBuDST6aDKDZ3bPPdUC8hiGvNSju7a08rGUQmDrgy5z4IOnKY3rgV3RNyOPzfkUaOo6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=OFgMx6R3SpzexP8Mtkg0Y5FwTKdxWQVT8KthlRn3xxAxRaZ8P0z0__K_ukdrlFZZGDJfHxpiMJ4TlU1dZYDDd7JUIPPGKih3GPtofxwQY1rpngbW8SCP7Afkx8DC36XBENrLCf96LaWXINl6t5yAXBbDbJh7EVXCdIlx4EThWryYnA5SQgwk3mm5sz_3_Nqmkjrsi3Rf3bXQ9U0BwalFfpjQUJUd-eaiEJ7DDikvYLIPXzOWOL-_7sehXc2RVmpdyTLuF2rt7Opj8Q_t9bxBuDST6aDKDZ3bPPdUC8hiGvNSju7a08rGUQmDrgy5z4IOnKY3rgV3RNyOPzfkUaOo6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری اقتصادی اکو به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666024" target="_blank">📅 18:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
حضور میلیون‌ها نفر برای مراسم تشییع پیکر رهبر شهید ایران
ای‌بی‌سی نیوز:
🔹
میلیون‌ها نفر در مراسم چند‌ روزه تشییع پیکر آیت‌الله سید علی خامنه‌ای، رهبر شهید ایران، شرکت می‌کنند؛ عزاداران از شهرهای مختلف کشور برای وداع با ایشان گرد هم آمده‌اند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666023" target="_blank">📅 18:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=arZWnD6bRKMvxNXC5Nx_kMsdSyrR1VSniDE5trUBJQOtQaH78cZtwHO3eDxUOuU4OCB6X-6me_oamLTx-qsQPN5WFOC7CZlidIjmXwzRU_ubtIJIrUaIgfJVip2QlTOvLmNYAkm5KBZqKZnekkkLYMvxI6EzQEYwpABXRCXJTeyS83mZYJ52jj-mI7vNKVPeQdhT-87tAY2UZ-MsSNIjC21ihPiW-vT0FtiZELPbVp2kR8oa-JZ1qePwWvlZpP7xX8QBBQndHUw5Lyu324IHWqO1rfMdWIpTFgXYYKNPe9iI28Y8m0XpTQEo2cA0s-SMdZnL77jqT9kmsAhGkYMpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=arZWnD6bRKMvxNXC5Nx_kMsdSyrR1VSniDE5trUBJQOtQaH78cZtwHO3eDxUOuU4OCB6X-6me_oamLTx-qsQPN5WFOC7CZlidIjmXwzRU_ubtIJIrUaIgfJVip2QlTOvLmNYAkm5KBZqKZnekkkLYMvxI6EzQEYwpABXRCXJTeyS83mZYJ52jj-mI7vNKVPeQdhT-87tAY2UZ-MsSNIjC21ihPiW-vT0FtiZELPbVp2kR8oa-JZ1qePwWvlZpP7xX8QBBQndHUw5Lyu324IHWqO1rfMdWIpTFgXYYKNPe9iI28Y8m0XpTQEo2cA0s-SMdZnL77jqT9kmsAhGkYMpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت تانزانیا به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666022" target="_blank">📅 18:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSMO9-bPeAgxhh_fAlQpVlVLf19bGdhEdVMM0_U4OTsED4lFAcVK8XGojhypP_IsBrkqvoB-pwcY9bRPIYTYiM530CPChwCo8HNkZEVsklvb0wqWHMDPIb-s3Z7-o94SgfysTB4TWfpLQ927MwZjE1CSAJcO7XaKx-s42QeWZCbkNK4tzeVQnIDw9XrMzFUEVimgW5NWRXlsmQsA_zvGtv-0VL1pOTaAC_TEpdlPAdnWH1Zs7JvOSmUChFhmB2TrInAL5ZAkMPN4Wvl-hYLGtQrHssIHCaPMUQnHPVGK3vvZAtI6xkNCdkF67xsDfEea5TZMEzWjQn_yaB2g9kdSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قله زیبای دماوند از دشت ورامین
🇮🇷
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666021" target="_blank">📅 18:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVfWfmPkhlIr7ZDThLCdlB3_6rSEHSkp7UtxMZCI7s76GeHmql38SOB2rJhWAu09z-oG70gDUE_kHmPTxPJdN2RTHGFF3fC4MmViLWLMaDaqbIR9EY7seMoK2BGwvzkUFrwrzBVAcZWzStMdeQiOb6YH7BMPPPmI9B9HofH3qWH6OXvlMT4x9PsoOJHSTk8sdqKCeLII59EyBabYAnUSj6nxnVYm3dROc2hhtM-4TlOtegSrynhQpiYQf2EtPThHkUeaPRuwrafdFM4OeDUztY3PaaZm-1lwxjVMEeOlJhGTi-Nn0lbrBmJYSGLdrrNy2adLbv_o8D0dvwx9X0a1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی مراسم ادای احترام؛ حضور هیئت‌های رسمی از ده‌ها کشور و سازمان بین‌المللی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666020" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666019">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=oq7-h-VKc2fJxdBbOnn2vPCkmJ8zZxz07d_1_YzhEmyG-YD4lVBDgoyZuy0Ju4jKj4Mj5nP6iGQxgcPmDNR_0XPjhxLt4uJEbIbOavLgrd0wgjCecZDmJPn5Cz_AWDdtIuUAGUsMPfd5vJ_fZ0j-9OnHiR8hNTuCh3rFwV4-d6D9lRjcxhq9ouHMpYJ_WF5ubFMA6BCTC22j5cdvu23QOrO3sCgGqxgVrNh1fJDUHRcuVcXltkKvRQpklwG6XXvx8buLmxTJTa3rewTAy4hxXVV0ydtPaVcOmkyC67rwtzktZ0s_jJ7mp_V8iwSx9UIsdSwz1g1kd8kg53blq88q9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=oq7-h-VKc2fJxdBbOnn2vPCkmJ8zZxz07d_1_YzhEmyG-YD4lVBDgoyZuy0Ju4jKj4Mj5nP6iGQxgcPmDNR_0XPjhxLt4uJEbIbOavLgrd0wgjCecZDmJPn5Cz_AWDdtIuUAGUsMPfd5vJ_fZ0j-9OnHiR8hNTuCh3rFwV4-d6D9lRjcxhq9ouHMpYJ_WF5ubFMA6BCTC22j5cdvu23QOrO3sCgGqxgVrNh1fJDUHRcuVcXltkKvRQpklwG6XXvx8buLmxTJTa3rewTAy4hxXVV0ydtPaVcOmkyC67rwtzktZ0s_jJ7mp_V8iwSx9UIsdSwz1g1kd8kg53blq88q9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشته‌های مهمانان مراسم ادای احترام به رهبر شهید انقلاب
در دفتر یادبود
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666019" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAZbsBXAtET8x1X2EwBKmK2x9gaEx63c9JrwiZulpabqCbPisdUBOwDsuuCp_zuUOnVwKTzotL0H-VfLRL_KWEOF-2Ki_FQNoWrpNLkBFNT-yMd9dCBnZO1JYg-vtoSi480M1oEoaeITDREBO7hOfCX6DtcDBztS4znM0euhhPwUdiqSCn5Relp9cJE6rkvbZA6iZe35dDDGJz79sUtN3OmfuEHqPPcoNmTX19UMVGtTBZmoaP5tvFWRIjzx2N6HLd8RaSjG6PdYKK_z8BNS8B8la0KKp2oOW237At1mYRm0lY8CWgowu_iFEaKqZuHX9r_2RwFcVXIG96nCW2oIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iK3X5g3_ey31TTSFSAhVkAVsn_OWIOBAR5TYgP6Y38z2lu0Qv1En39P-g2h7diNQlHYzCj467ifw7LKWp4QFJ8ggHssUtsvkcHdJv7V1pS7FLfACSeViB0I2VAK-SVEk1rrwqrnVghSFxeEFtJjfKvLtmdcufWyO83auG03IyLUON1AdttiATDtidNja9QSCuc20575CTJoIDP0xLNIuJkC5CeWywTkx_10hCkSyCFF_FsX85-RJY8oR_tMIMZaeiV6ovRU3hFff5F_njxdnVMII6ELmC0J58MuoOKw-O8krq156Mr9VH67hC1U2bdV673Am8-0g3ovfDWXRIeEKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBdLZet3Z6-01H0xwFXv_x8LGD7_172eQsrr09KlxSDUmlBmYNdhRgk2PtoURQFcm38kwzDlqUFkwa9lRzNopiXrVSQpBkf7pVNITtRj2CEqptmHGh-39i9cnmaV546H2JEY2a2ehe9-gK2ndxAE_TUzCr0UKe0wW7YzFk4pIVMhnD8Cp4voRtoMRdZuEWqrcR6iExMAQ7Ec7FjpALEHyOBLMIFhdx1f4Ypg1KpfG-LEI304cMR62mFZ_mFQrpY2no50IIkAtvhZuNxFboLoAmMnQycPlYDDlIBqBYBqsdnTHSRqie6IMQRLUk1UJnm0HxBssF02doUUARgIKTqBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVJQaCAiH0W2dQ0SKyY8JkiWAvtZ3L7Og8TsoOVGDxDV20JSzcQduBLSAeXIjDUtaFCzwVgkEIUgSPCZEYcSrVb5Q6qB3iQ5fUFmMv5I6uv6PDdjA4X0oVllRQ0oP5mQ-8G0LV9FD6i2a5gjA15zhq5dwIuZA6ckrNDg7ilCTFjjiXeR-Bxksx2zXivMjaRCgeFy9nM5R6Y8B-HFVFmbW-LVYBqcQhFdC3NG97QUubD1swkEG-z393EJXTuSpiBlHFCRBbiJ84wjDWzdaEQa1te8KP_QIObh0BC22EBuGFNmE_QUXu5iCA-C__Rz5dXRq8hSrxU9ZpItfDB4LjH5Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۲۲ ترکیب مفید با ماست
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666015" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
آغاز مذاکرات ایران و ژاپن برای ازسرگیری صادرات نفت
رویترز:
🔹
ایران مذاکرات با شرکت‌های ژاپنی را برای نخستین بار از سال ۲۰۱۹ آغاز کرده است؛ این روند که در چارچوب مذاکرات صلح ۶۰ روزه تهران و واشنگتن تسهیل شده، شامل بررسی خرید احتمالی نفت توسط سه شرکت ژاپنی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666014" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MqLl52wlszd6nA1CqTGJd3EFy1LgG0S8Kr4Hv6z6nh8Qfg2vOzU15X9zhqrbIOCXAmjOCTclINPij7AfpMYRHmxqKnpkR0UIuF5CD-9EfAfe-X9u0st_I8-QM8fAknXv3ZDvKV4mo-OmYLJvd6rhei-XIHD_ZRQX6l9LCAfd6wvO0XtLe108q2F_yABBmX8ErhQ37H6gf209nR0POvZ6NxP-nYnbAIDS5OBNwz5cn-AWWY_RqqATYrYcTbFed4Z-pCFHNUjYQiH5HAHvBWUB8Qf_sUfaoB1zRl2JcmL0LRmYgi9GWumlceDuMvypru5-TYzSNOkF65dVZO0_wjJGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MqLl52wlszd6nA1CqTGJd3EFy1LgG0S8Kr4Hv6z6nh8Qfg2vOzU15X9zhqrbIOCXAmjOCTclINPij7AfpMYRHmxqKnpkR0UIuF5CD-9EfAfe-X9u0st_I8-QM8fAknXv3ZDvKV4mo-OmYLJvd6rhei-XIHD_ZRQX6l9LCAfd6wvO0XtLe108q2F_yABBmX8ErhQ37H6gf209nR0POvZ6NxP-nYnbAIDS5OBNwz5cn-AWWY_RqqATYrYcTbFed4Z-pCFHNUjYQiH5HAHvBWUB8Qf_sUfaoB1zRl2JcmL0LRmYgi9GWumlceDuMvypru5-TYzSNOkF65dVZO0_wjJGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های قالیباف هنگام وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666013" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CG_z16Q9Uc5dzwOqgGW3mKYPpTV4rR99q0xHmqNN7SYTxnstb81X8l0dVFzjXX5Ie2NneFeODsCcJd-5W_Z2j8e0IoxjUjep9hFRylakj7EFJ5N3f-y8DEoA_QOes-6A0Ks4U8UeBlb2xTS-eMXnO_2ZA94D8IAvEUHwTIxA9aRxcNMsdn5Dzbjcm-mhEDZwDwOtWVZyLx_P6342Oqc4mtfEIybTjPUVF2IyihfizpSHmtuu13qCrKiTl5sZUGUCMQ7jRvki0AezrPcrHxg1w8FAkIMKylW-fXvwYtbbtXXzrLAsAlf4AbSM6VFTRaGSxn1HMLdCJ3jp5cn0ejKH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGYgN5nhi1Lcw2wqES36uw18UMifs6n8FaPbMF4GVqyOMp8jO4JLdXskjE2_4jNYXgOgTifPFh3DCBUeBWkf26-QIENK8mtYeuSJ7pPaf-IPFnbIdM_kUxbMcSUSr37Z1cqQDjRYjjb3VkAdZEHhe8Kmqqle1bp1zAU5AtHN8yLTRF-QUQC2YkVDCd1oNxIPGiFiWqLzUoH6B3RHbDqdXdHHIU2Td35EYEIfp5obcuNPKKC5DpIKDASeJFNJKukZsDy16WoFwlpkN4DmQzMgk-4zFN7H71KEaTMiFJM0eFKwcP3ljwaFH602Bbxr-3MHMPYs9Yltgb_llne8Q49mYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxl1wzGMB0lf9jKbXr-1a3_-Ea5bKKGBClxznCUJwW0TnuIoF31H-XkeMmy8rdkZvx9i3mPV8KjMnFPCJssPFB3sK-v_S6Xu4SxcWXJwqWfuPbnUnZbUI9P85nt66fnKmQrCIGEznkE8phGHzucs2g_6lxa-vRAKNDgXfkBRnpWN8c_ME5GPPlvdcWsA2hATM6LPjndxkKLZ-Hd2-q7BDOo2UbYtH4t5rBO7WML1x08cC4LGJC9jG0IqHgoXt2UnpVRfizkT0EDlq2oGWe9gJlcTtr-Qoy4UsnlLJMlg1sF3kJy7Mq3yqePEo6ciJDfIu2fG8ljHiGIK2ddUcvA4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4kxpHca-hrgDRjm-YDCeBJ6QcMxfhC_wFvAEvckAHcV5fAdT7sPJfvRpCwtGFeKK6iQdZKvcKGqhpGAshKj8-I7vi7vdGSa3FCaEinZvvyaJ6KWXiM12z15wV1UwTFRdDgDZGtJp2OXKFOlX0mmUbk8k9GAf0XVFRwy9rZFXOvs_gDV1ehT3DEkpsMHLDBr5zJjG84v22AMvBkIonvnRQBxWFa-iuvJ-7ZSMdKv7vE2SstBpp4xL-_MZrazUdEfd_SOCHNSlJRg63H5R3Z8diOKX5pO5Z8v5vOJONt41P3OEh8VySd4ymrsCoRtL1aK2Qw053Vwan6VhvNv0h_6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXxOft8cYxNK8c55IVlIe-iIuuGUK6RoFWlg-PEDtvxhdpkuwjgctmZxJ_25FSmkIERn8oSleMUihoTk3Abo06dMpW3f6J-tP3BiqbR6OwmAVFMqJlmZeXrhSJc00xIx0SEzo1vzNBRiT8ZNAEQBHrqWQsN-pKNNdwuFmkICkBaKeOJ3kw7T0Kfr-IYghYFA1VpvODIl-AyqOPMo_GQ9eqnUvBIUUGTlaQCFCel6FPfmKkIHb0aIsgCat3qw8-a491WU3mNoJTrwVY0IVmoGFzfWtDbvsmRSIkKyaZPzyVUC3ioIk9l37LEtUDx-r35OeU0QM3XD1MAdoSkvI5huxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEAMRL3MIQJYYZ7J4AtJ648sJ22BwCiShVyXWsws8dUiVOwhj2iwYMP42fP6WF-AKOCJQftXr9M4gfJoZV6zgLxm5oXC976aWFj73mAr4cQ6wVOV78xJkwphZfXMgpzcOcV7Z8lmjCNxq26ql0kBprvCqS1v0IO6YjJbcEbo8lorK3J8UnbVV1UMFjYH9qH_e5jfD8y_lhSx7DWdgeBvecrny9sl56FQxfjZswxD1mX4R_Sdqjzf6LboBftO2NuhLR4TDRpuOe0YY0q597K0N5myIH_bYQKcFcn3hQJKm6iWeUvlB2qbu7Cf1IcbIZZqKcc3DT3Qpiz4Mk79BkDfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O33_V33z2iTZSlQsQjD0NI6snOI6M7-Xy0BrCMFCtMDyCfYhJJzKdvB8aW-oye3tk9LmfE_zV494Cd_mK-hblxn3cnZNOF1oHw0LzlmvDUoJzkUb5BEXtyWpDoQkN_n6AQxFxhKEWsIdnHOiw0jUXpCcKVCWR3SOp7ufXq-ZWA2azqqDvc1JLv2B4ma2eA5zPJgrpuiMa7GQXLA02wyIu22oUKeApushZVcf8dQKFR888mLp4sb5Sv7FKKJViU1pSRa64NsaJeyxloK0CCu8_IlhFCxepJrQw8v4-p_j-QKRHquLNPJvU73O9iWs_HLZ1FbtKDHbR9bsfgrldVc5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rh-BKpuweUGQfR_8C-SH1AiBdMOtF8FBRHK1qv4zuDuqtX8wYb-9KhgbumxujFTZQbFMPWqHr6pRirOFPPbAg6fEV8Uymh0WESx4TOsjPmhOmwUnGvfmY3fXAxW8vSlhbHIRN1igmMmTMCS41_lCVUdwYW2XqhFgJHEOCxuB23Bfdv0eFBn46gzvwCMayA_NYutkRGap10zCDs-9JVcVlNCh9hwu2-4mONf1e5iVMCZg9QyHzBQ2xfCS-Xq0po7kDUoLBeLKN8CwfDEffkPYyPdujJYxkzIqJamDbSad96Dj2GAwyQ1KlcuaiqzERtcu8tCn3U0EK-sB0eRw_sa-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNQ-Sa1uyWCSALxMlo_ct8DmUUzl0I33wMF3LWULi_wfOGtWgXwSxddBbOW61zo7gRr83H6cOUWrdKvG510ga87FH1gsviRcD37G6TdKTDQCEgGFs7vGh7PpTAtH-MHY1r8ws7OUj7vHrlquZrH5H_SbbLdkmb1wyWzpcAohJtRdtwlc2Hc6MS5BnZtJ-3iFlqX_2vrWTunivSKKE7UT0GioceaU-A829XH23BqU_eRPFcaBvHTQzhESaTIOFXQOc_1S5Mx2kKddnreRmpFLpwHlT2EF87AhfS8nvV31XM_dnDTO-zxEBVq_FZ2ZZhbjKOIw198MbBUMt_Z985Ur2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqvkFnhhE9X7o5SILm-OpD-jMFTstDZZfMsBCy6cxj512ZK_41bmflgKPw7Pdr-oVpIEp8YBkYH3Lw9pAq51NYUD4SPtORbsqg0ChLbOilexKPk0N08uzizBfkEmf-uK5LWg2GTQL8o6LqaP-X2v5E4op1agiXyxyYGLJrtGPUkzxOFzXglfRTbDPXDaf055Irc4j3kYt5EWuKgoiAEhTNI-lJZCURsw3msYN041WaFlAd5twSs4Ty84-Nxv3eVCQmoUAAHFw4l7yOcG_D0lEU238UbAlYe0reJiDEjniMOw89r4gFkC7ranQ9oUIYuX5NBpXfuVO49ABCughY8DLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سران قوا در مصلای تهران برای وداع با رهبر شهید و استقبال از مهمانان خارجی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666003" target="_blank">📅 18:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=fk-9IZeGTxCkunJih09CsxQWPEJU32I3gAY_tl8wFjVPnRczxV45KAbLY9I9rEE87Z-tv9v_bgimmCw3Lcvfk3epBRxktj8bfHgG-moJfONn1rKePAYBQR4mST_Gv2zBHMGOwKxFDowuo_LKVi7yCRfLIfZ9hRb0QLN1uA-mmRqIO8fT_r1FbDAzPCXr-JXXzQrVopsXi2m5EGk22EQZE1bEwhnXgImLJEVS2WVDyS9dExyOmvMw-u4xgaBbS_VmbbBfjDA2pBZl1-yMoaehkMs97j3ycZIydH5P3Q-QEOE593qUtdBucE1lHO0-3u49dSWPjhS5KysRgOTY80UcdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=fk-9IZeGTxCkunJih09CsxQWPEJU32I3gAY_tl8wFjVPnRczxV45KAbLY9I9rEE87Z-tv9v_bgimmCw3Lcvfk3epBRxktj8bfHgG-moJfONn1rKePAYBQR4mST_Gv2zBHMGOwKxFDowuo_LKVi7yCRfLIfZ9hRb0QLN1uA-mmRqIO8fT_r1FbDAzPCXr-JXXzQrVopsXi2m5EGk22EQZE1bEwhnXgImLJEVS2WVDyS9dExyOmvMw-u4xgaBbS_VmbbBfjDA2pBZl1-yMoaehkMs97j3ycZIydH5P3Q-QEOE593qUtdBucE1lHO0-3u49dSWPjhS5KysRgOTY80UcdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت هند به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666002" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666001">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMKAPH1AZ-51a302F-Phxkdnao5CSOBhTTCW5ZVEVijWgrgTVXyBnjJWIDRsxqw0PiD_Szohi89Vc7aJVqA_EcNYhOaGs9w9O3_Zq09ov9appv3K5zjqVARViHrPGM02cmGdo5vCz_uuSqDjekGyibcR3tKdwCAd2eLX49QMt3Y8uKY3gEPLvwlS-FTT_0SSSlIsyT4DaYf68L2aA_jjak82T3mXMEDpXvKApbqVubgTGYADM1PEIWrCcgO3wqmhHevgmJg1EiP0_rr1rNEOZREJUrH_UFnfEd0jBAo8gFsca_wXCpsb-9qpii1H7eh59NyT5v6Di7_GAkR74EHHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاگرس؛ اصالتی از دل ایران کهن
«کالکشن بهار و تابستان پوشاک زاگرس»
«برگرفته از دامنه‌های زاگرس»
📍
شعب حضوری:
https://zgrs.ir/b
خرید آنلاین:
https://zgrs.ir/hz</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666001" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=WXllNUEfm5y8eUFJdiZjtfHZTasXaVgyOPTCvuRKsBYWqOLwoLgLOy9gcY_MmjFpwmfAiMFKb0I1PkGxDfcqKXoalSGG5ONoRWiMjEGrB9fqV--1uH498CrFo08jtCjuL3AtHWYHl2Trm5aQSE1ze2idxw-zFOXYvmCkzvQ8ABwjkshfGMLKmxvgYrYRe9-8bcqQBJzlT1tZUsby8Ybu2n7GbWzCefjUip9BuFr0GEHZWxJEC18oziWnS2VlxIv9HDbd-eHR_MBTVAcKhFvKy2gstos1b7_n9V8GwW5o-_5G2O_5BwvxrJskU3X19Rb-7TETfEi3nXX_z4nKxJECpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=WXllNUEfm5y8eUFJdiZjtfHZTasXaVgyOPTCvuRKsBYWqOLwoLgLOy9gcY_MmjFpwmfAiMFKb0I1PkGxDfcqKXoalSGG5ONoRWiMjEGrB9fqV--1uH498CrFo08jtCjuL3AtHWYHl2Trm5aQSE1ze2idxw-zFOXYvmCkzvQ8ABwjkshfGMLKmxvgYrYRe9-8bcqQBJzlT1tZUsby8Ybu2n7GbWzCefjUip9BuFr0GEHZWxJEC18oziWnS2VlxIv9HDbd-eHR_MBTVAcKhFvKy2gstos1b7_n9V8GwW5o-_5G2O_5BwvxrJskU3X19Rb-7TETfEi3nXX_z4nKxJECpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ دولت تونس به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666000" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شروع فعالیت ۲۴ ساعته مترو از فردا صبح
🔹
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665999" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7a7ff500.mp4?token=iIX2MQuHE1WrJsMFAP4ZH_AP2r3lB7GbPS2Eh1m0KYczDWjvR52MXlFJzSM3-FXZbkX9LMR7obxgOSR0pbdm6sDepbvg8DhojhGWHCyIJJeqjvh5yDqACp_lkhDLw81csV8c8VUVCafUc2yt3kudqS_exrtgkFjiN8bpJvJEtuuVddgssLuVpHkYoitRKMHe8lR-ygrDp9YWx23dBV0Q-rxHa6hqCnbG3DLMbNyGNBQih9Lzuv4is5JZnX_ja2eVSaQNwQx56Vt1XavA9eSOckRNlODl7h1Hnp9Azl06aJmjYs2M3Zsldt_oRGYJAIpvjXSoGvFFf5IvyS-ptUpYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7a7ff500.mp4?token=iIX2MQuHE1WrJsMFAP4ZH_AP2r3lB7GbPS2Eh1m0KYczDWjvR52MXlFJzSM3-FXZbkX9LMR7obxgOSR0pbdm6sDepbvg8DhojhGWHCyIJJeqjvh5yDqACp_lkhDLw81csV8c8VUVCafUc2yt3kudqS_exrtgkFjiN8bpJvJEtuuVddgssLuVpHkYoitRKMHe8lR-ygrDp9YWx23dBV0Q-rxHa6hqCnbG3DLMbNyGNBQih9Lzuv4is5JZnX_ja2eVSaQNwQx56Vt1XavA9eSOckRNlODl7h1Hnp9Azl06aJmjYs2M3Zsldt_oRGYJAIpvjXSoGvFFf5IvyS-ptUpYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665998" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ارتش یمن بیانیه مهمی صادر می‌کند
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور ساعت ۱۸ عصر به وقت صنعاء (۱۸:۳۰ به وقت تهران) بیانیه مهمی صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665997" target="_blank">📅 17:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اردبیل(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139ef7c55b.mp4?token=nnTUQZr5FH8mkYu16DQbNYN7vOAFyjhoYHb2mjue33Zd0iBWUPhdbLKNbdSJwFCp3kSwfHXz-a5MB34iQJTyjzYw2axJNCWgkPUJTLBbrwDcewtlV4BZriBgfPi6VvoHft1nHWzKx_Pnp7adyqqx40xfhqC6lEKmN4HsTsU8OJ3oIfU7EunfgPBsPboMcBLbqYgl6EtYkFHKmy6h8pvGec9--_0gN7fzuBdO97jSxo7SFVTibsfvwBiEXJ7BYHORfqN2sK51vy7LjTSPP4eFutDNIGw9t1JLQ2giiMvDYWIbtugLvAk2Ybhu0cXP0KvhuUkAZMiL4vZFiOX0E2oURoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139ef7c55b.mp4?token=nnTUQZr5FH8mkYu16DQbNYN7vOAFyjhoYHb2mjue33Zd0iBWUPhdbLKNbdSJwFCp3kSwfHXz-a5MB34iQJTyjzYw2axJNCWgkPUJTLBbrwDcewtlV4BZriBgfPi6VvoHft1nHWzKx_Pnp7adyqqx40xfhqC6lEKmN4HsTsU8OJ3oIfU7EunfgPBsPboMcBLbqYgl6EtYkFHKmy6h8pvGec9--_0gN7fzuBdO97jSxo7SFVTibsfvwBiEXJ7BYHORfqN2sK51vy7LjTSPP4eFutDNIGw9t1JLQ2giiMvDYWIbtugLvAk2Ybhu0cXP0KvhuUkAZMiL4vZFiOX0E2oURoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفرِ رهبر شهید انقلاب به استان اردبیل/ مردادماه سال ۱۳۷۹
🔹️
اردبیل، نازلی صَدَف، سَن‌دَه شَرف گوهری وار...
@akhbarardebill</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665996" target="_blank">📅 17:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
درآمد ۵۰۰ میلیون دلاری ترامپ از پروژه رمزارزی خانوادگی
الجزیره:
🔹
دونالد ترامپ در سال ۲۰۲۵ از طریق شرکت رمزارزی‌اش (WLF)، بیش از ۵۰۰ میلیون دلار درآمد کسب کرده است؛ سودی که با یک معامله «دیپلماتیک-رمزارزی» میان واشنگتن و اسلام‌آباد مرتبط دانسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665995" target="_blank">📅 17:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665994">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=dKw3iBYMXtrMU7Q-K5B90Qmhmu6WLbHinxASCe2fz3L7vYIkJI1PQfgQ3IwOvsg6Nc0cuamzp8sq03nUj-cFHiIkLCqwS4AVvPGsswKXi6UDvzW98uwrmOw5Zhb2gwu7XPubDnB5VTLYMW4WThjVm_XzCZgUJoOtocG5Qs6UpRwRQ35s6b7bqbO5ltFpvDQyAenf-9xRJ9XPOZSCBX_emN5wUE0RuXWnqSUkzAMrC8fQ0VlEBPBLIRstZEvZO_h4saDEPvRCsot3jeAVFnJiw0_r1IdPdEG5H7W9Mew5SvYoQ9nnbFKLYNakwjkAuOGXwbT0iS1czVpHsgTtdJyUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=dKw3iBYMXtrMU7Q-K5B90Qmhmu6WLbHinxASCe2fz3L7vYIkJI1PQfgQ3IwOvsg6Nc0cuamzp8sq03nUj-cFHiIkLCqwS4AVvPGsswKXi6UDvzW98uwrmOw5Zhb2gwu7XPubDnB5VTLYMW4WThjVm_XzCZgUJoOtocG5Qs6UpRwRQ35s6b7bqbO5ltFpvDQyAenf-9xRJ9XPOZSCBX_emN5wUE0RuXWnqSUkzAMrC8fQ0VlEBPBLIRstZEvZO_h4saDEPvRCsot3jeAVFnJiw0_r1IdPdEG5H7W9Mew5SvYoQ9nnbFKLYNakwjkAuOGXwbT0iS1czVpHsgTtdJyUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو ادعایی از حمله امریکا از خاک کویت به ایران با موشک‌های هیمارس در زمان جنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665994" target="_blank">📅 17:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632090959.mp4?token=t5xljek_o-E3aOqn9MBfC6_VLnPYLyaAqRjhmk3e4A6EfjvdkA9imnV4YheZWEszDsHB7DXQa-fEMjt6UueQ2CWvxktKiZqAnNaSlGv6ophCDfxGAeUmL-Tmzd4dzMHvg4P6O-usYlh56khgPSRLGyk3PKVrI1MmHiQRAPnkRyL5nRTMl5IFf_p26IB82DynbVfnkVqmkbN3szaN-cspRPVnXDMdILqAtZaRNI4hyA78Jh_JR97NuPM5oGkwHKTEkf6uAY9vBF98eVEq9cmB5CJ-evO4R6UPqd811gInYcL38dMzZcRctTuA1FIWblylneFTTqf42yf8so-OFw4OLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632090959.mp4?token=t5xljek_o-E3aOqn9MBfC6_VLnPYLyaAqRjhmk3e4A6EfjvdkA9imnV4YheZWEszDsHB7DXQa-fEMjt6UueQ2CWvxktKiZqAnNaSlGv6ophCDfxGAeUmL-Tmzd4dzMHvg4P6O-usYlh56khgPSRLGyk3PKVrI1MmHiQRAPnkRyL5nRTMl5IFf_p26IB82DynbVfnkVqmkbN3szaN-cspRPVnXDMdILqAtZaRNI4hyA78Jh_JR97NuPM5oGkwHKTEkf6uAY9vBF98eVEq9cmB5CJ-evO4R6UPqd811gInYcL38dMzZcRctTuA1FIWblylneFTTqf42yf8so-OFw4OLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
آرزو از پدر، برآورده کردن از پسر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/665993" target="_blank">📅 17:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DonzMTdA1phrUFV4lO8l1_0Zv8xlOoDHZVtjj-SgKR-uH7kXoWYc99JiBVPx433dMUEfCZfp_IehB2W7clvj5O5_RJLDcDT-2N3U5W4t4CwbujUppN-O7Mg5vb_9WFZrdWG9ktDMKHrb3mNQ1Q_vSL5XXYHFrhIFrwaa61p1qRSQvU40G72n6XmgcjsKIi05K-rmGZssN6cyW90qRfV_5YN3E_CQXxG8cFn6pZLElPX7lvQxpurnaTBc988eLDaVzsElPXMw1KwXMI5tIqp2T1PU5yb_K4yBcrOn0esZ6WnA1O-yyZPATFGlzp7Zl4uf2n3yJDMPwXE4CqtUDEoOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed8lxXXvQ_wp87gUXlobQ3HjqL1SnRvXJ0JQHDY9EGesGBv2bowuoWAD_Ww4P-A0bXasHq5qeqdhVZjFl3cJkRHEx21hNpfIq3suTfjMGHYoVqViXmnKIK7UlvZIuaJmEeCQE-evrHE0ETOguQenaE7HARKErLdxFh3HamJZAZgBAQCBkeyncSIYlCFXtMqE-shVHRzbEZ6vhrHGwRngdUwea9NfE4hnoTTXwauMVP10neu3nHkDn9XDi3HrbjV4sedmr0tgvAGlEsfoySmiPpSn165Qr3WFpjDDy6EgtqMtuE9j-NDStuQZz3xPv4k06w0uiIB41g5hQH5-hlhUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7xur1-E36Wl47vtsPcLMe5cyj9v0sifqx_Nbefnr9coVIykeOpsyQicrjwifPUhD4qyL8Gk7qjhTtW410gIJJLbbgS3KaDh8pPDizNyvPvPRqNQH2rdntdzpvnyCjRJE8QxhzdQnjyWErxwbPOI5-coCVdh5C8qmSyMneIvHBv-Jf6GmZxcUGURC5Elu2cGPPS43_sqoHY92rlF4OJXRpmyf8j_NVlAu7LdqkLIvtCTLiRg1U_-47aF3RUn-ekfQh5OyWpVpT21l3DLghbBMyArWIZSzkxvgnm1t1PMNAlEWzH6hKnJO-jV0y9vv0rRfTYWx4FfU-naceqzFTvOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3Om8mw1_uSL_hTxQITO8k7RXR664zkpdLcmPsxYEhW3CFgAW2l27h8BMjO_jezyAJiJ9zstviuxrekTqm-92IsMHudrpR6ksxtE4eKKW3MDsizXVLTyXQfHJor84GbJI2GRv34_-SKlumEbGkmAA8uuQR6eYQov8AoMi-9h6IDk9lRpPbbs77cmtVnpNACZEcf6DTNDdI1Yv8Y53rgvbmXyKZnsi0RvcSrZ-nblQgQ1bMSia9etxBVLLPW4S-KmdSv9kblCLlrchoE9ps1IQX1uCH2grBamdRGvTaRqqY3psESGJBtF1PFIrp4ZvFANHzQl25hc-irppGwdMp9kyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR_cSsUkrKedTyqriy-Egz5GPi5UZ5HJ8UkfmasBtjSpY-hLWUsMJfgkVGKa_x6QfAXk6tieqVVs-GxIHvVpLFlN5_KimlGTDozJC0k75hkrWfiPMVJF-3H9iORCmE3mxtGuW92LM12qi2p88FguRfYwRzDx70Rd9IltKMNPXEAOOg0tur4JvEA_kmzocgx5uqcU6LFZstU9cRsv_k-E4PXN877zXuKVoahu2Nvzh_qbhu9N1DqtOEkGE2QN7YWwTqt3l4Y4ftp9b3NNRIkFta-z4fq4dRo5djIm7VykFr5S5jAGySJfdovAj1HqB_XqmgQL2ITDWxGQaKVR4VfkbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گلباران محل شهادت ۲۹۰ مسافر هواپیمای ایران توسط آمریکا در سال ۱۳۶۷
🔹
عکس: رهبر امامدادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665988" target="_blank">📅 17:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c70f74be.mp4?token=omdGspvUc9_PrSr537ov9WdmzW0zFHrfvLN-CUWoiF5V-SkQ_AJl0UCCDm7KoTmkODbN2uAb3wHzrL9ERqwWqUSg080TJnniXyV96dl82gJlNITjsdFH5DOKFXZ5xuLvx1MRp415L95HxqDwTiRyIaDNEiK4RE7jN41_2v6Xe1F6lR8gotwopPs_BawmGXV7SC5J-LuVND82oZ3vYlMuoL495ZGwdtPmeemcvbGfSlTgusOj5ZIAz7wau6-U3Iz-0NcYxyHjE4FsFbwsjRdm3L7pdFqHGu9Jmi_ZNB324x_LAX2sTQmX0Ru_ZRrAZrjCgpUwAHbHTxVxI9VxhGAvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c70f74be.mp4?token=omdGspvUc9_PrSr537ov9WdmzW0zFHrfvLN-CUWoiF5V-SkQ_AJl0UCCDm7KoTmkODbN2uAb3wHzrL9ERqwWqUSg080TJnniXyV96dl82gJlNITjsdFH5DOKFXZ5xuLvx1MRp415L95HxqDwTiRyIaDNEiK4RE7jN41_2v6Xe1F6lR8gotwopPs_BawmGXV7SC5J-LuVND82oZ3vYlMuoL495ZGwdtPmeemcvbGfSlTgusOj5ZIAz7wau6-U3Iz-0NcYxyHjE4FsFbwsjRdm3L7pdFqHGu9Jmi_ZNB324x_LAX2sTQmX0Ru_ZRrAZrjCgpUwAHbHTxVxI9VxhGAvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665987" target="_blank">📅 17:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=Wxm3owcOm-KLC79Y3gqbpPHuT4PfCvxOy3uaI1sS0u9HndGx1eDvInBAXKDvAo6g6stdiKK7vcnOgHZXvdxZk7uOSZMNRJ4xKGR1a9H5Q4EE6mVi96w8HsYk2LfyTJlZvMQVU2zDaHljrk0sriyzPV_HyDfFe7FwvNiNH417THXMTRTgKh0FkUZAvWLBtrTwdQ7NKuYMl26bVK1aetRR9TZPyY8qRJU5TqlCevxMXsh2Q8Gn97YqLgTIs_Lk0mU-1tN0-UE3A_gDSO8TGXj5pIYabC2qgr0FtSeGWA9p7YVIQJkbV603pPtj-qOyICAdsIfBhFm9U933e9Fn0R4XMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=Wxm3owcOm-KLC79Y3gqbpPHuT4PfCvxOy3uaI1sS0u9HndGx1eDvInBAXKDvAo6g6stdiKK7vcnOgHZXvdxZk7uOSZMNRJ4xKGR1a9H5Q4EE6mVi96w8HsYk2LfyTJlZvMQVU2zDaHljrk0sriyzPV_HyDfFe7FwvNiNH417THXMTRTgKh0FkUZAvWLBtrTwdQ7NKuYMl26bVK1aetRR9TZPyY8qRJU5TqlCevxMXsh2Q8Gn97YqLgTIs_Lk0mU-1tN0-UE3A_gDSO8TGXj5pIYabC2qgr0FtSeGWA9p7YVIQJkbV603pPtj-qOyICAdsIfBhFm9U933e9Fn0R4XMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت مالزی به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665986" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2ac15614.mp4?token=YP8xUenyR6yWplhFjJonYtlPqPa3mM7NSIA0mWupDrTa9GEhxG8XJfrox7xhn0rBB8I0i0283_-cwoG80NepzLlF8UU_FLAK0bZ8p0ME2QegtaQO6M6u9qnGMDyO8PTPA8JMcEhxAddGQkC4U3X_izsvAt6_9y6LjMZev9wWxwjXne5SIBHy6wot04YK_gPtOrTuA00RS17y4MGhZOnyVsmQVRwBKahqSOh5h20ZA0zH2ZFCzQj5EyOjPIpC0E5qroYC2USxQGUFfg43b8Nrp0puNPD6eY2jT0w2J9XVhVhw0PAGTvNDaCrEuRsYFixlEDrnVwSBrBYc_yXdSwHX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2ac15614.mp4?token=YP8xUenyR6yWplhFjJonYtlPqPa3mM7NSIA0mWupDrTa9GEhxG8XJfrox7xhn0rBB8I0i0283_-cwoG80NepzLlF8UU_FLAK0bZ8p0ME2QegtaQO6M6u9qnGMDyO8PTPA8JMcEhxAddGQkC4U3X_izsvAt6_9y6LjMZev9wWxwjXne5SIBHy6wot04YK_gPtOrTuA00RS17y4MGhZOnyVsmQVRwBKahqSOh5h20ZA0zH2ZFCzQj5EyOjPIpC0E5qroYC2USxQGUFfg43b8Nrp0puNPD6eY2jT0w2J9XVhVhw0PAGTvNDaCrEuRsYFixlEDrnVwSBrBYc_yXdSwHX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نائب‌رئیس جمهوری یمن و هیئت همراه به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665985" target="_blank">📅 17:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=tj0vvdPV_3rM-TZWf0xa9tHbu-gtCK6mXvk4Mx6UbyOTS4YKJqBqxtCqVlb52vio0iBgARFy4tHdRD-LNZKcQMHj7xuKJb-3fba6ErWYePP01T6ejTGdBpzEvHU2lzBbl--kNbTVUepdY65XpqN7KvHEubIj4BnDJZg_41UqAsnTLLje-Rzzhv0ECTbPBKnW1wcXVQ7wGuyEABEeSg63-jldWRY4BW7LMxFZ2wVGUgPfyM-pvmBTpt28UwvsJXT2FKxAyvFjBlzNcvScGuqLpeTzRq3qaCRma-7YA2T6nhTmtpObO73MddjXK2ie5SDRVw8ce0tZT4CSHnjK8tZreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=tj0vvdPV_3rM-TZWf0xa9tHbu-gtCK6mXvk4Mx6UbyOTS4YKJqBqxtCqVlb52vio0iBgARFy4tHdRD-LNZKcQMHj7xuKJb-3fba6ErWYePP01T6ejTGdBpzEvHU2lzBbl--kNbTVUepdY65XpqN7KvHEubIj4BnDJZg_41UqAsnTLLje-Rzzhv0ECTbPBKnW1wcXVQ7wGuyEABEeSg63-jldWRY4BW7LMxFZ2wVGUgPfyM-pvmBTpt28UwvsJXT2FKxAyvFjBlzNcvScGuqLpeTzRq3qaCRma-7YA2T6nhTmtpObO73MddjXK2ie5SDRVw8ce0tZT4CSHnjK8tZreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665984" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=c6BkD_M06VJXn8nfERxCpfL5IXGVUydnKS3CagMRm_EmglLBwiOOr4eFhM2yaiouo81HveaoZUi5v4u7lLJjfOAcT06CMzwkLQs1WISFArSJsZe_NdMdtGkPZSBjeyA5DQG5E60cDwSahEovR4PgiCZZOiOlhK68qcuQD3B4oC-HiuArnhlufQl1weQnmY2-AsDAVZhXsO1wn5Ir0B7yhM84te3FD3z__x-xOGfs7ihldQddFYc3tzUtcrvnFa6CyZ30QX9JtEyd3lRuRorgGWdSNtn4JsViOcldws0RzpDlgIv50S4tZPLxvvnZOf12RoKZtO-FOoo2bK0cdBx8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=c6BkD_M06VJXn8nfERxCpfL5IXGVUydnKS3CagMRm_EmglLBwiOOr4eFhM2yaiouo81HveaoZUi5v4u7lLJjfOAcT06CMzwkLQs1WISFArSJsZe_NdMdtGkPZSBjeyA5DQG5E60cDwSahEovR4PgiCZZOiOlhK68qcuQD3B4oC-HiuArnhlufQl1weQnmY2-AsDAVZhXsO1wn5Ir0B7yhM84te3FD3z__x-xOGfs7ihldQddFYc3tzUtcrvnFa6CyZ30QX9JtEyd3lRuRorgGWdSNtn4JsViOcldws0RzpDlgIv50S4tZPLxvvnZOf12RoKZtO-FOoo2bK0cdBx8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون دبیرکل سازمان همکاری اسلامی به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665983" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtybezPfjjxaDhWd2wYSkwF2pE2DXBUoTygMOjCHDr1vNGQlu2k_vuUJBbUnGHbGsKbwhB3P_kQa9y4K5T-qM2L2w8k4-xlqsC91RJeY9Ge64x0lbQFPRLTrsa0dpWG6okFQXcrwaYXV8-XDWqcWuXMIo8ATA1InRBvW6ML09cNsSlRKwlYcHE7v5TQIUwdxWLhJbU-SO13pmMFrqW-sRcz4NKCjjUB92e9V6i6PnEd5edbjEjeEPJJtYwJbZJmCxLcfsciVTFmjEuY7hDYOgzyDXAZNh0V5b64uzdnbuwj2sXC1_w7hu90DX_lL0Lpcx-ree9aTpoSjmxaKlqGs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمانی مراسم وداع با رهبر شهید با سالروز جنایت آمریکا
🔹
سخنگوی ستاد تشییع، همزمانی برگزاری مراسم ادای احترام هیئت‌های خارجی به پیکر رهبر شهید با ۱۲ تیر (سالروز حمله آمریکا به هواپیمای مسافربری ایران در سال ۶۷) را نشانه‌ای از ماهیت جنایتکارانه و تاریخی دشمنی آمریکا با ملت ایران دانست.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/665982" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=dR4xTcta5nqWLmTNhhAyQTOrxi54VwQEyvgFAVUcbEYtvGeX0TdDS2K9gY4aValb26XOgIWfpyhlaHkt8NEAhM8AVmtIdb-CyC-ShFSs0myjIlG9PRHSm6QH9Jz-LY_-zAjNQHx-9SiDbXvWchCmQxcEIdYAA31hWWQsr77E3AS629oK0DaiZX4mCzMjsP-UY_KP_CIL0s4kLs2aA9DVzmk7gOg4OKu2FSyE33Jk_vF8Sn8uno2OLnR3FCBgwIyPpR_Z0RzQ0Fjg9P8E4VUaITIHcel9OwbG9kY9NcnM_Im94HVFRmDQzBHtfjwqvOOBF2oFjL5YC2eXhvjAE9h1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=dR4xTcta5nqWLmTNhhAyQTOrxi54VwQEyvgFAVUcbEYtvGeX0TdDS2K9gY4aValb26XOgIWfpyhlaHkt8NEAhM8AVmtIdb-CyC-ShFSs0myjIlG9PRHSm6QH9Jz-LY_-zAjNQHx-9SiDbXvWchCmQxcEIdYAA31hWWQsr77E3AS629oK0DaiZX4mCzMjsP-UY_KP_CIL0s4kLs2aA9DVzmk7gOg4OKu2FSyE33Jk_vF8Sn8uno2OLnR3FCBgwIyPpR_Z0RzQ0Fjg9P8E4VUaITIHcel9OwbG9kY9NcnM_Im94HVFRmDQzBHtfjwqvOOBF2oFjL5YC2eXhvjAE9h1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری اقتصادی D-8 به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/665981" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=CVX8JIe4XaV431FijnkwBcF5ASBy7HNP-NyPVmeqi_G20nfL_0slG4ZCWcd9Ts7gN0aIYmJGfKj_13z30fQ37Q9a7Yt8Tmt1wYUd6CV-mqbf4DRj24BDSXry32gFuy7lPQ3q3ee0DzjbIID_71l1MS5_Zvi4vB4Hqj-IIag5buUDxGatTi8w0yBMd4UVpITuQHQ2PTe3vE2R1gTO5u25xpUfNYfpFOafedmxoV-2R0s-rW4Db6v-s1rxJ_ylDHgxg_yB6Rf-Y96IlO8qUTRwSOC9aI-PyDBcKW2LQ0IfF1PxgxmqO3UNuRADVx5md8LQf_Ohr7IJqxwoygOnsTkRXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=CVX8JIe4XaV431FijnkwBcF5ASBy7HNP-NyPVmeqi_G20nfL_0slG4ZCWcd9Ts7gN0aIYmJGfKj_13z30fQ37Q9a7Yt8Tmt1wYUd6CV-mqbf4DRj24BDSXry32gFuy7lPQ3q3ee0DzjbIID_71l1MS5_Zvi4vB4Hqj-IIag5buUDxGatTi8w0yBMd4UVpITuQHQ2PTe3vE2R1gTO5u25xpUfNYfpFOafedmxoV-2R0s-rW4Db6v-s1rxJ_ylDHgxg_yB6Rf-Y96IlO8qUTRwSOC9aI-PyDBcKW2LQ0IfF1PxgxmqO3UNuRADVx5md8LQf_Ohr7IJqxwoygOnsTkRXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون نخست‌وزیری تایلند و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665980" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aceb48cca0.mp4?token=aw5F2uanrLuGUA6L1hGiK9EzAcedS-ct5yqp6FnPP7_RPldSJCufcNUEZEbnO4MjE35QkRYOQI4JWV4b5NQxfM7JH5ckd9G6NLhTiEPaQYA_mAfGl43s427vcai0wi2PDyKTOKXxmZ2ZNfyVKhTkykaMu81R2Q_Vg3vYNB5qIA_WAOTdgc9tsazXPK2xsuRdSu6g9BOa7R55MyWAJK0hWZbd_95wRv1mRPV-_ydGp2DHHm38Pn6rLY_Fj5LG5YsYdTkgXdGnDe0MEvr7xtLWN4kg4toJ682muUOTxJkMXtOFJ159pDY-PL-pn1RyWyBHBYnqxlKQt_2v8PSvxATdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aceb48cca0.mp4?token=aw5F2uanrLuGUA6L1hGiK9EzAcedS-ct5yqp6FnPP7_RPldSJCufcNUEZEbnO4MjE35QkRYOQI4JWV4b5NQxfM7JH5ckd9G6NLhTiEPaQYA_mAfGl43s427vcai0wi2PDyKTOKXxmZ2ZNfyVKhTkykaMu81R2Q_Vg3vYNB5qIA_WAOTdgc9tsazXPK2xsuRdSu6g9BOa7R55MyWAJK0hWZbd_95wRv1mRPV-_ydGp2DHHm38Pn6rLY_Fj5LG5YsYdTkgXdGnDe0MEvr7xtLWN4kg4toJ682muUOTxJkMXtOFJ159pDY-PL-pn1RyWyBHBYnqxlKQt_2v8PSvxATdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665979" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=nhFh7wLrMr3LDts-fh9aFZ4-WnlsMIO3-W_0FCm_0aNVTSKOzTTMdRlO5Ysq9XT75FxPzYMAUdD1w16Ji_vDgQuK_hfNSdIo7n_Jfst5FAiQQ5lKdzgIkubZLOpD2qH-K8oXGW0NgALlxBEupuZUFGGDhpqjB6IUP_Sa0ZP3Sq0txey34pFOmiRL-CiVt9wj4PzXxonZajxLOW2P9HpjYwy_FQo-pRf_6pd6qXHHRsvJ2u0UY_0i39k96mtbqvYMD_B4jmcymijERyIrcfwijrza-7Kw7aGPtN7BkfxByo_GaFi-SoPH3OmzT7gcnR0d5J2lScZjMgO-XqTO6HGhFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=nhFh7wLrMr3LDts-fh9aFZ4-WnlsMIO3-W_0FCm_0aNVTSKOzTTMdRlO5Ysq9XT75FxPzYMAUdD1w16Ji_vDgQuK_hfNSdIo7n_Jfst5FAiQQ5lKdzgIkubZLOpD2qH-K8oXGW0NgALlxBEupuZUFGGDhpqjB6IUP_Sa0ZP3Sq0txey34pFOmiRL-CiVt9wj4PzXxonZajxLOW2P9HpjYwy_FQo-pRf_6pd6qXHHRsvJ2u0UY_0i39k96mtbqvYMD_B4jmcymijERyIrcfwijrza-7Kw7aGPtN7BkfxByo_GaFi-SoPH3OmzT7gcnR0d5J2lScZjMgO-XqTO6HGhFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام فرستادۀ ویژۀ رئیس‌جمهور میانمار به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/665978" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665977">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665977" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfJsd4uYdZp1i8I98XlZlYEmHmVo36nUztPRvXV5_hUFb4rsHojVI-FI31AmgEQk6XjODdPceZpDm9QrjDGGNlZOOj9kOgmCajfoN6H9iULjzBBvEV862TO-6c1BFnh7bZm-7ugOwHZq97DZqQDet39lU2BlOQqXPFvphlHAxeMb0IcbYl1bcJUAtLd4b8NJ7PNKnnbLHkBGPUbD6pV-WnpcaPC3sRh-U0ZOt9Xhn1GAbs0vgAllhR6JgzUa5V9dRqdMVTeObwOjQX0BTeTb_eYVy6PSGhd-xXoNJITOt6SL7LiGEAdIP2K0ertB1ovWbC1O798s704a_ZnhkKoFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bx0QeBlR--7K99iqvbCI9W_kCr0pig6OD1N7R7OElvcCYzVcT87pv5Vua8Nb1a49upi7NQgwNEIHpAx4HL7PoYs5VAebeQB4H4RGVZAVcQdFXITEQxE9jnhiV4AUKdOV0Z-T4nHLwBy7pCDZcEpRZSGtPK_B_3sjBMrF0LAL70aaIMOFVA8-J8CKCJai5GQhjA9LnuJua7Bd4eX-8Vm8pEiaFYLrjn032soOa_AdiyJ9-2qTyxg1NkkyU7ZQF2qXY_rXh9oiBZcpPUUK_vzg3YJ2ySM3NQeFQG2WRoZSp8bDSJZobkqp60fL0hJz2lzz67ZjdBLR4qY9RQG5KyWDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjZ_ht5tVdr707yZvziKn4m54FA7tfJfhz6itMeEyuWnaWON7sxYWaknGOOMsf3K0oxiGzEp9t4mrBGDItspyIbuwcVId55xeGuHMk1jYFdZSBKrpVp-16hUj_5kRdLlOjVieSf1ixSrsJYZIrlBbzMSUCF6hfqEScFrUyfr3dGokHd4pUhhoMK7UsiQnbJxLMGynpAekH9UAFJ1dan1KOKwkYx6B3ZfaNE7oWF9rvxlAFg9PGFiHvWez9dxtSGu2o2uEY7HrYYIKh1mfN9Z9TVNwPipehl4GEvzyBEeKn__tYzKJuXkAB-e77Vt-Xy9mqxfRM4_flbYjsUgB-EBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxmnDIk7jZvA5Wl9ubB1RFI5OZJwCWGlY9fRBvfcHnf5DO35lKYe_ZMfmyxdaImSJv_SnPxIbet4WCCI515niU3_wZul5exaro4pTJ8N4mFofYCL0Y7HO6A37NsEr1ZG-LRw7mUIHspeSItQPxOxInAcMKg9cETQ31wTYwRVm2l_23QI_CFQHnsULLmyDZ5f-bMmklEQxEcVsBseI2EZpyFC9b1ETt0jOD4C9Xyda8dMuZw4yvOJw6qMu163wVUdYiktxFomgf6Hdp1CHLEpG4bame3CJCBUn68yq_ZdGkQDQ_oZ-EBwEBfwsm73xcs5A-36xf--heT7fuLTms32Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر و فرمانده ارتش پاکستان به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665973" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=Hw6eDKx1WTZkGukfaMlMHLZAsb-QD9MRZV2IlTaII9OEbD2ISNmww7T92HhKXR12FzxzOCtCPXGPMHIVNsKB8ULaSTcEaSUJqpFHAL_k8zRidQn3pEU3eDssd3daUCxPBzBwoHsW5ryVaE8WxECXwcA469z_zNRc5u0aXlQ0GPALX2Va5fnceyRjxlRToTtnz9JX2k3jW5Qnkl6zJO4BkDZG9YwFzOCaqcfrse-z5djj2URJ8ejDKdSIYjw0Icx8lgxpa1sQlS6B1niKiFxHWfsX1KpA4uigdY0jO-Wf1JO4xvn-1f_1t_9degzdfW5enDku9cNZfr_nmzuRHmfpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=Hw6eDKx1WTZkGukfaMlMHLZAsb-QD9MRZV2IlTaII9OEbD2ISNmww7T92HhKXR12FzxzOCtCPXGPMHIVNsKB8ULaSTcEaSUJqpFHAL_k8zRidQn3pEU3eDssd3daUCxPBzBwoHsW5ryVaE8WxECXwcA469z_zNRc5u0aXlQ0GPALX2Va5fnceyRjxlRToTtnz9JX2k3jW5Qnkl6zJO4BkDZG9YwFzOCaqcfrse-z5djj2URJ8ejDKdSIYjw0Icx8lgxpa1sQlS6B1niKiFxHWfsX1KpA4uigdY0jO-Wf1JO4xvn-1f_1t_9degzdfW5enDku9cNZfr_nmzuRHmfpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مدودف، نمایندۀ ویژۀ رئیس‌جمهور روسیه، به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/665972" target="_blank">📅 17:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665971">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e498694bbd.mp4?token=N67ZcvLYYeg0gTlXjVjwsAHFIDxMnswks7wur3Bo1fs6K_JfvvvrFRx9egJmG0p0qyR0V6-gAdL7DC6WxIiiJQEvKwi_1WrRRl3N9jdyWZH8QqWBqvHAo91NZJH0OxWjGLfbJbBm_HB8LpuWDPLFSTMTUmObEfJcEgoQ1baHQ_w48TbgeB_bsRu9Eb-tg4DJIXwEc_3GiPp40ImVXe4g_uJfOX8IRRUOfX_ccP-GlT4VZJnKWfJPI390MA45Nl_U7WAM_o157zeF3V--IdW-k4jzJr7vtaBtclqIUBkSJoN42nXFXfHJ1_xa3LNOe4cwjcRazYi1YgXc_UXrXy9t4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e498694bbd.mp4?token=N67ZcvLYYeg0gTlXjVjwsAHFIDxMnswks7wur3Bo1fs6K_JfvvvrFRx9egJmG0p0qyR0V6-gAdL7DC6WxIiiJQEvKwi_1WrRRl3N9jdyWZH8QqWBqvHAo91NZJH0OxWjGLfbJbBm_HB8LpuWDPLFSTMTUmObEfJcEgoQ1baHQ_w48TbgeB_bsRu9Eb-tg4DJIXwEc_3GiPp40ImVXe4g_uJfOX8IRRUOfX_ccP-GlT4VZJnKWfJPI390MA45Nl_U7WAM_o157zeF3V--IdW-k4jzJr7vtaBtclqIUBkSJoN42nXFXfHJ1_xa3LNOe4cwjcRazYi1YgXc_UXrXy9t4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نماینده ویژه صربستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665971" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665970">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fc63366.mp4?token=RgvftEqCT37NSa38jlAFoY8QL14uphudIh5eLLA90Z-VPxSB_JZEiDYh6P--ECzGpU1E4VppiCU7MPYv2n0dwAjPDksGPxhr9UUDcV9CimTO-30yCuBGA8f1zaSuNU-th87Ogxqyr3htfHLiqn1xdE7lGtL-PwN7LYD1F3Dro5v8gAB6Nm1YNuFSt5pK9ABbyiGyo3llIpj1_p-H_6TQTItsVok-wLsWseaXCJtmVNFQMvt7qChpAm-zbnvIzWF1OnjWU1Dy9ts_eEEiFXfuoMexk_dX0PrTDFas-BbI03rvvzlTDtv-hHD8QoIiy4MTeT6Kph9yGYUwZZK3dmDcHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fc63366.mp4?token=RgvftEqCT37NSa38jlAFoY8QL14uphudIh5eLLA90Z-VPxSB_JZEiDYh6P--ECzGpU1E4VppiCU7MPYv2n0dwAjPDksGPxhr9UUDcV9CimTO-30yCuBGA8f1zaSuNU-th87Ogxqyr3htfHLiqn1xdE7lGtL-PwN7LYD1F3Dro5v8gAB6Nm1YNuFSt5pK9ABbyiGyo3llIpj1_p-H_6TQTItsVok-wLsWseaXCJtmVNFQMvt7qChpAm-zbnvIzWF1OnjWU1Dy9ts_eEEiFXfuoMexk_dX0PrTDFas-BbI03rvvzlTDtv-hHD8QoIiy4MTeT6Kph9yGYUwZZK3dmDcHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نماینده ویژه کوبا و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665970" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665969">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c46ddd78f.mp4?token=euxHp_xXxKWhKa0NRGCCZ8201GvoxYwQxHjPwruEj7EUbH4a-VUN0r9UM1uzywMEkliSRvBH_MPnsqaMwW0j2MIFVqFI-2SV4yFpyYI4YSYk6YIYwYXVKMUf31vWaiWlFrNckW-FEMWAoHMQE5XKbTfdZsxohyREJGjETtjne440uywVNcAQSCY6ucKZzMHfOIOpG5DiR6do2ALsQwkWl4jRNmXCbGcOSr5xjtTaNG87bmJkVw6i6toAYrz7y-NJvaJxPHOfKnqFL4gUbKRRZRnEfJMa1BEVQXV2DHVT1FzTfx9dw_CSz92BW5TFbwYLYCIpY1e_y9v-O_hFNbOl3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c46ddd78f.mp4?token=euxHp_xXxKWhKa0NRGCCZ8201GvoxYwQxHjPwruEj7EUbH4a-VUN0r9UM1uzywMEkliSRvBH_MPnsqaMwW0j2MIFVqFI-2SV4yFpyYI4YSYk6YIYwYXVKMUf31vWaiWlFrNckW-FEMWAoHMQE5XKbTfdZsxohyREJGjETtjne440uywVNcAQSCY6ucKZzMHfOIOpG5DiR6do2ALsQwkWl4jRNmXCbGcOSr5xjtTaNG87bmJkVw6i6toAYrz7y-NJvaJxPHOfKnqFL4gUbKRRZRnEfJMa1BEVQXV2DHVT1FzTfx9dw_CSz92BW5TFbwYLYCIpY1e_y9v-O_hFNbOl3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از تفاوت رفتاری یک پسربچه با مامان و باباش در یک روز بیش از ۶ میلیون بازدید داشته
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/665969" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665968">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آغاز محدودیت‌های ترافیکی مراسم وداع با رهبر شهید در محدوده مصلی تهران
🔹
محدودیت های ترافیکی در محدوده مصلی تهران به دلیل پیش بینی حجم بالای شرکت کنندگان آغاز شده است و ضرورت دارد شهروندان برای شرکت در مراسم حتما از حمل و نقل عمومی استفاده کنند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665968" target="_blank">📅 17:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665967">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=YQ9kMx-rpPZuHvYeaehb0z9cSi4iG0Vu1EI7yPd2Ml7zCr-Fg4Suwtz3Q2pexxg234CfuGXStkQqGjlxNqf5owkT3Cdzg-Ppoa_POOrBkhmduMumu4pspt96vHrJsvUT3zU2I91B14Y8YiKcozqWmShkDWHWcZtJt9-h2JfFsKnSTW_qhPWU8temtO6JqBnZEmHxhSdJVKT6gVhHoXqfCwRbKPq1TGmPDVDhwvi_lWHXCdscsMLrkloOXhTyNifxgLdkzqoyk-wk3P-n-jLJIP61sJPuSJWt7WnXfJnSZMLkS9qVTC7ybe4v7YruJJRxvOMU4aYsGvZHhcsyoAcapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=YQ9kMx-rpPZuHvYeaehb0z9cSi4iG0Vu1EI7yPd2Ml7zCr-Fg4Suwtz3Q2pexxg234CfuGXStkQqGjlxNqf5owkT3Cdzg-Ppoa_POOrBkhmduMumu4pspt96vHrJsvUT3zU2I91B14Y8YiKcozqWmShkDWHWcZtJt9-h2JfFsKnSTW_qhPWU8temtO6JqBnZEmHxhSdJVKT6gVhHoXqfCwRbKPq1TGmPDVDhwvi_lWHXCdscsMLrkloOXhTyNifxgLdkzqoyk-wk3P-n-jLJIP61sJPuSJWt7WnXfJnSZMLkS9qVTC7ybe4v7YruJJRxvOMU4aYsGvZHhcsyoAcapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر آموزش عالی گوام به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665967" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665966">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb914d9b40.mp4?token=V1QycuO_5DX5MWZFbhem8VVZqIGTlcOi-qT0y7xVYL7KVGiR61Dp5jzdgc6xZWkjel10q_7TB8ACbHi6iVN6R3glePusCiFIPRM2ZHqAmJOMENyUHqaxVLV2LO3lRWN7jAtPz1JrgJ4cM4U2G4RfUjvTB-by1TIF70klJV8KDB1lS35dynKIvuEJwpkXmKEoGIY__4H7ByDAOSnJc9M43iPHV7QETvJuzkZ5pJqdCpbNFyNszshSkHWkMnRxRLNfvVjuAqYXV8EjZ-lvPc9CK7kwCP3snQLu9dFYPCFK3-ub-I6eznzk79a-EKjQQozUPSJiRvq4B4W3ipjflxy1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb914d9b40.mp4?token=V1QycuO_5DX5MWZFbhem8VVZqIGTlcOi-qT0y7xVYL7KVGiR61Dp5jzdgc6xZWkjel10q_7TB8ACbHi6iVN6R3glePusCiFIPRM2ZHqAmJOMENyUHqaxVLV2LO3lRWN7jAtPz1JrgJ4cM4U2G4RfUjvTB-by1TIF70klJV8KDB1lS35dynKIvuEJwpkXmKEoGIY__4H7ByDAOSnJc9M43iPHV7QETvJuzkZ5pJqdCpbNFyNszshSkHWkMnRxRLNfvVjuAqYXV8EjZ-lvPc9CK7kwCP3snQLu9dFYPCFK3-ub-I6eznzk79a-EKjQQozUPSJiRvq4B4W3ipjflxy1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام قائم‌مقام وزارت خارجه عربستان و هیئت همراه به پیکر مطهر قائد شهید امت #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665966" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665965">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce8a8ec0a.mp4?token=Lo_IwHKA7XryivlDPzEuj4AHq0WXp-RBDrcKMeZazrEBlnBZ_N2jv6wngMBg9S7Zwi6JMr8R6YiOTY3wGWhPr2N61q0JPiEdeo661gkIgS4ZfhV2BmGsB-Y3s4GGHsKSjmQgmJEUW_uNgQTEpWZD464Kwyimev3p4JCoOY6gpAvPDyOtoj2cbDfIqD9ZpmJFoioqH72Bd8EBzpXbHGsacPKa_zn5MJ64ILY1ll6O5CIf_B_IoXAszb7lWNWJWrlbNQXWSNSy8CopSzsFUmaX7B_2KO9QMaH98QPGZv5Z1x9oduQy-Y6s-lpDNlv0u7vLgNQ7AVDyG7q4p9gIw2X95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce8a8ec0a.mp4?token=Lo_IwHKA7XryivlDPzEuj4AHq0WXp-RBDrcKMeZazrEBlnBZ_N2jv6wngMBg9S7Zwi6JMr8R6YiOTY3wGWhPr2N61q0JPiEdeo661gkIgS4ZfhV2BmGsB-Y3s4GGHsKSjmQgmJEUW_uNgQTEpWZD464Kwyimev3p4JCoOY6gpAvPDyOtoj2cbDfIqD9ZpmJFoioqH72Bd8EBzpXbHGsacPKa_zn5MJ64ILY1ll6O5CIf_B_IoXAszb7lWNWJWrlbNQXWSNSy8CopSzsFUmaX7B_2KO9QMaH98QPGZv5Z1x9oduQy-Y6s-lpDNlv0u7vLgNQ7AVDyG7q4p9gIw2X95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس پاکستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665965" target="_blank">📅 17:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665964">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed2e29e6c.mp4?token=IEkOaP2CmJzC7BuTyqZyihKW7yuOi4mT7TdfwzP6QQQxOK67SK1teMXEDUoiRzRjBhMz7LNAl8BXseY7zx_30_JkYarXaaNN5ir6QMm6cD59IYF_R-8VwMDKtyKmDaj5Uu6hiegS6CBqc-kdpkamSkU8g241w5tE7f1AewMpm7P6Nu07Si8Msa9eAa1mtz1Isu4KKS5fkynEagSWnL83DtCIKUkuFid9BgcN7ru5k5uAkUweloAyAG01AK1SW36BxYFPr7ZouD7-MrFbO_VNwIJ0jb2zWsDu1L9vWBZ59cz_qJ1dYbE9bgcWKQQQpyMiqGdU2Z19OYSAE4fdOgsLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed2e29e6c.mp4?token=IEkOaP2CmJzC7BuTyqZyihKW7yuOi4mT7TdfwzP6QQQxOK67SK1teMXEDUoiRzRjBhMz7LNAl8BXseY7zx_30_JkYarXaaNN5ir6QMm6cD59IYF_R-8VwMDKtyKmDaj5Uu6hiegS6CBqc-kdpkamSkU8g241w5tE7f1AewMpm7P6Nu07Si8Msa9eAa1mtz1Isu4KKS5fkynEagSWnL83DtCIKUkuFid9BgcN7ru5k5uAkUweloAyAG01AK1SW36BxYFPr7ZouD7-MrFbO_VNwIJ0jb2zWsDu1L9vWBZ59cz_qJ1dYbE9bgcWKQQQpyMiqGdU2Z19OYSAE4fdOgsLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر دفاع ملی لبنان و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665964" target="_blank">📅 17:02 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

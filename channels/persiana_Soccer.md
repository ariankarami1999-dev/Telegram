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
<img src="https://cdn4.telesco.pe/file/mhddfIF3UZKE9MMdSea_W9XeWiN2X-PfYZhxvkIO5zXSVO0j1dOYskuhDb0HvGT6H_pXNGgNHXup8ueXqzWKJQ1eHL2Krx4VP6bjyjXIsMIuRw9fAjnwGYgQGcRLX81TlsJ75MS84c87V_-_rDfhcC0KLfLg-QSlotV7z8El8LuyXhnxM7QI9_XLHs155cLAD-dwZlKby8bV6DxTAm_cTuuGekOe4f1qbk88rejd-vwh6p4Tv7yZ8_YzbxUrGZ1WY2Wps145AhpkBs2xUr_CQcVQl4g3VCtMMrjMBJ9quHNIzkwzgpF4QjDQBq27NJpqpaYnzBkCCGh0Fxy8MBgrvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 513K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAQd_ESjnt1p9FIv1zkWHX-TB8K9os_vTr-KwD_C2-Aa7Bex6LntjKUO9YC2c2HkC4ZIxEgDiCnC9vm8JsDk1b00JBLye3lC5JLkOb34TNUuNx1QfzzdqjCfq4KUPK54tOeBjpxSUQOUJhbpgMuzBfcxdHA7RCpRY7EZXtgr4iyzKaTo816ctPHzm1Nq7PUCRIK2EkPRVYTbz0jBmspnesBl1sU9GYyFWkbXmbqUXe1RBpUu7EF_JJvreSWRLYFRGRODPutcKmkY5clYxG-u0ErrMqWaRDKqGSIfhGN8WaPvqusou7cB5VQYcVbtPUx5KP0QEBqDFFWxwRr-N5n1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-JQPybbvYNRB8yX6MUEbDK9q3p1I1z9k-Suav1DerDtapY00NqEFadKy2Tm7e_2XwIcuLjDSEFVglMzu3TuxxibJNa7EfX4zmaOViJ27_tBALy4nH2RImgh4ada1X7eJHYirHplKT3kg7vWT1fJZrRqXF4hvG2BCzdiZ0m5EnkOskXpoocB3es1JsG6-5_X3TN9O0jfYnamQcV4JqDckihwUZG6jVJfqMG3d9t_dVexh9JkJlXO8jWJhyQQJnWJESclIH4ohZgmzrq9n8qjrNJTMWgExdM7xXRubJTwYvg9oGTTOY6EvnKm8JW0y31uyL0UznVDCf-_ptP4EzAu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anm8LmrokRKhiTGpiTAGvyKplRmfhL9SHipoHT6_0hmfXTfEVdwjdcHCDvotxpb06rfyNETVndDXRcZq52D44bnhY3O-eX_qT4goae90YiORGgUMuSZ2a2qD1V8kZ-u16-43-wOIpj7SJ8ST3ikzwPGs0YYyauUbOhMm2vD3XxYSUHYEXskHbV-Sh7MmRxNXQpI3d-eeQdzQtpJTCYLC3ksGTP-4PQVKi5OOcUxiNf6Op-iITs5UhtLTeHNEGxSz-PtqRRtIPht2rp12vPFYbQOVVLkQMxriBDS9SRxwOQfzdudxjmm1MBjMljK3X3cgouuV7fUdMQZDQJM53cZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgJx4pTwn0hZEPrkjLrFgw8EAq_0puVgnZVknh4LU-Su00gtKd7rj0kXdMqbmJH0w7RWQ_mFz_Fbx5PXAoMs1o9TJNRBt3w45EKhtAwA7hJCQCUmkf_FNREqfpEWnj65CfdK9xLRqqbp2HfqoH89gYjh8I3jYLFHNa6wMaOtHzSOq30DqV_UHRUWk2lTObdLC9vzUyzo-Llmc2Qy0QV2ittrp4IEt3b5WyfCb6fVI0UXsCjID2NTClreBkrJlaMh_PakYst7hXhC_2yaj29pls-qfdD6rJ765GE7-yuQJXdnQwbuVqDKdl-LRiCBvAHTA9VSRElxSkma-OZ5_EV_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1IULus141wSHgXIgC-tYRosmDCCwIMaXqsvn7V_ii1LxU0IGrxdjCTq-f8-BTBb6fidt3HTz7vyqAhq_8YV3ZPUrVCVnfpWnrAbVLzOArqo-3n_DB8ah8nQTG49fGoRXxV7-AlT41g1exY3lEieItfqu2kMs58MdoUFDBQw4HCNvw8jEjC6I-yYDvvNWXjzErDLV0AU2xTzt0deX0RXjfM9scbyG4YtZSXjRSZ4jDhOlos--jhBPYL_RQcVIKVE3k1w-oJO0b6dnmmDWLmFLIEyHpGQJS528H9xlcHkny0aeNYnLAUXAZW6wDHLY-yNXsa75zjzgjAMU6qtE4vAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF52F6v7MPjLFZEnIFHIyQaYZ47YYdbelVpev4SLClFx-0oMFvnIheMP5F7_ORqmmsu5NbjEyCh6fx-1HKTq7_kuq5_4iMnSJ-LJUnhMmYLHKNDaZ9-VI2F22aeynrM8PTQ8WAm9uYoF2Ais1m3FQvoGfZpA_Aequ0DLTAV6ODQ-_98jceX35uTuRD5JJRW0UscxlbzF49OrbMkfHglF1xtIG6rVBaNtOWCmf3aVe_Qmr1lrMJJXEXHIgddJ1Wu1emZCtepgWj8L6AAZSce3CLADHxgisWFXYjxcBFrlWzuvc_BDpiVAMZc3foe3RISC7xmyQuQGePGaahPDJySIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKWegOwoJ4CXCU_tbjfYoXdjRwIJXC-t5SeEDfXthHvkHDfNgJcbZKVGiPRMLXXs7IEbLdfombzBhC0b4Chig34bpzSlC0sqiuGzr__BFr6r7V0nly_g24-YmX3La_If5qU_zafwIKIqTkW7DC7iv6GFBu5U7hyfr06b7ZsyAO2V1J81gVMGt3uQtVQnhrg91WLjlPa242_kZ2MnK7257bnsQBupTWsUAtCdfj_7CJjOocItVWtApeaOusX52FVKNtPUlUy3Yda-hM1EY7XSVy4Xp8RCITJgmAJfXgG9qrmZp-o-WjFtngu0OyHAb0MP0tl4ALF8mVhphnjwd-Vtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTTexaXUwQmActVJe3mYDNVRRlPdDESviz9N9cKZmNmS1_g5Ogdathg4LnwAfyP6RB1JNxiLwpbp5Lj5NWDCnsC5NUKqrIU_lBIIaZdmUlrQBwcS34-UmXqx5PvfjZ_qEbuzJpKHFUA8tAOCuMX8UzxXu1s3tExVnCnJTOS-basUlNwgmRxE5yLpzLxZ7lRA5AUFgL74_Uf4rT9RhGheyvtkPl6ptmyp1a_Hjc18mTHd_Q8CjAKPskqR956XRZlO3qzqeJWwD31t1nNXd9GrAMULldOtqpLwgXdpiaSM_kb1atS-krp0ud5HQ7iBV6q3oE_CjwTP82FZ3KW7xRQyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz4jLlajVE0Lm1qwN7bE2AOj_SmETswLgX5OhcycaM6Jdpvz5D-U1XbRrwOyt_uj3wgTZQJ32HhjrSOk0Sr5zdqIGrhRwrMLv4CJCDIfqgolGa-d9GpnaD0WxXuqaAn5g8ce3mUcWzQw94mstrMkVub3ayVXZ6jgovkM90_9Y6e_qSDuHnJooRtze_GoYwxr_-GfeZD7y1tpRaiP9FhhoAEVHInBFrhIfqY3wJFQDBAXl4X-0OXTQ5xJJ_tkt7d1nUfa2M4n_e6GRQ8AiQUerBx-I5RZZge6JHZE4d2K-42RdqlX353ckJQV2tsaTMs32jm2IA7WhZ3ewPWZ40ooYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlard4F-Xn_E8N2v_8xeaM4F1C5ISlyF-6a8vuXk7iIAF2k3k5K56F46i1sw592pUxBHkNPdBNCG8-FcWCVeHLQdKQGIU0KmS62cD67OW7ed0LiLbToIoAUZ3qHB-91ixY6prBzy-1WaT8wsSprpBJpLljUAt022KVAIR3vpE8XC2BcRSZ9KQxwBm2Dx09OjvnCk5cRUKxdsBPk5oLPUqsX5uz4Ge2m854mdr3kBg_ZaRyeJYNVwBQ88aKkZGIMEHbYEv20SDSlRWuhsFTvDM8t0E695ZujlX3nJX81fAEhDFNXifBnX-c-sGQwqgaogSKr9cuTgwQosl07McUEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBIUqCn7HQlP-up2dQ5125J3rkwF3b0alICRINxkAeLu0-KbbzNvzV51R_eh67D4F-WRKs4QSz4HVEZ9vy5cRVau18tkw8vChukmZZ4KeDRat7LJ5BMKKFFUeaESAHN2VoqnN-7wycUsOe218hsoKls_8nQOzaKry99SM8js5PE5SfLKLQxs0Pi-QPdEKD5RtLavPwFQbzSKEbXNtx1A1LtRAMU5GPrO6OOa8K7PFggY83eJzy4X1R660PmB2gQDMxM98NR2te9Q455YMAb7FioWjgwVi_mBr9Z8l4Zeqa6Y9FiUNv3Ajg0bLOHrao1MdzOnu0rYfwiqYtUNOlLtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw-0wEMO6p44o2rzBJhc0cValDcD-NwO9j6qaC_-sgxEAGfaQGdZMnkJO--o4b7J1d32lTYyiSZ1TssGDm5ukay1gKrQiNFlEcG7F2-PgSFIVGpDVqMtxqzXINgel4naz7f3H7cvTaR9fLmtGnyZzmOLgIsnknyuhvM5YOZQhd-Z6hKb2Nu2rdsBf6LT7q7Kk_dsOsKBFp8X4n2vaSSWiaCzOHe6qaVS0zJ6-NQtVhwC-lFKZDQ1H1BHced9q16ibiPUp3agVM24xCZYvGoxtxk7AOCXh4jdcHh-ljck3cFnEFmHoNMh0gN9O9rtg8iBbwXc_RP5StGD_qLV29bogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0qwlQJ4APseUIBTilNAHHYmuM1nVooCsWFvxV7z7X73UOxATSZWjT18DHOhN-NrJwew6fj6h-EoQ2R0KgGH5_AuCDEl13_KPnUsVA8PaY0xa07mp8XPfeRgGC4XT4OWg4PqMyU4uLvgnXfmCgu-OghdYt1Lt2bsLi5jSb72kfTCCRSF4qtPUI22qaxtQ076JGj34cbyYM5TuCXnEH182hFP1X2smXg_VS3aD3LcYsyCiKjnroL5oLULiRl4eTT60QCpJ2xiymxNY2Zw5r99RAvCwp5AxB3Bffp_hRGBokdkIcvyF_dG4mxSb1yfemWO_6K5F8DbOeBk7wgEKOZLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsvHhlDdalZDMgfuE_bfRKfS3o1mcELK5xabyI56KuV85hBNELOAYxyofkoYaYmblmNQPbWhUj73O2v3hWKkA3rqPW1WfriFszHYMZdQXxB3rg4oaDL-wUZZhlzbYoAyznLvdQeIfNp-zOzz1cvTYIVv5oNnLdMWlZzy0GOoXVItSyPbZsL7B-MDPeHcCS6wImuGWEaTtkfvSznlTlCIbbuY-8FcXHYeA9xoDG1Qy2tSGoIM6IpcovbQ428WlHeu6NLQiAv6GEG_6_sXCjFiBzTaE2kHRRmMdPWxTWYgExqQK0zmMKenTVwxhAC0oSVCuH63c6oLM3BcxMYHaThvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5pGA1QTNGWe_P60Eh59RtXzOOQVSlelDrjX-EmAoUiTMoLhRPT7OrA0rUF1x8PhhadoyfKh7DabzR-FS6AjUfJwghboMS0oIFxTva0QtZjRX7W43_WXeqZ3lZeqU23nzTQdMMQ50kuGtd4iT3LutISISThs8QP4Tdy2_4lg5lZXjhsjd5nljmRVmIXa7JFqQVutN-w-1cb32fbJc8ZJXJhnUK1ZzcC5qgOnYfo-r20OTFKjAdighcqP7sPX_9VdeLEWcD059Or3VU2p3ApHiAourVxcQPeqB8AQzls-TVbosW1SMXpueqxp-jNdHhz5SR8eI8YktlkZ7V7S_xvlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kS-OqDCwga4iA2I_evu88QFhdaIgNBBTLV5XnSKWT9OcDU_XryXe7gQCgsBETo4FYQV7Y3GvvP6U6lHoNTa3X6mvbuYH7igz34kWNb5q5GSg-Mr-92AtroKc79u3smVysQUbhCvC-yDXNMlZffhzIUX3FJ9QyJcDHQm9nm9plICOvEL-nZF6hqGU7BXdDFQOenIWcv9GKq8QSVsGIpVn8-lchyO94ohwPkqc_uRWFLNSeSnxWIHCH5bwZYFb5o2pkYBc65PI8sEaxWXhQA9sIXCNEEbiptvkVPh4IsV5kCXmGwanFKmYZyF7RZ85fFSY8DJVHcPMqrZ70OUE8rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpg0uvlB4SPhNvcn_FTjx3l6Q2wM9tjdi1DcgaUZ0ouPoS1HKhG5affL0mbqWrIjs4CUTB1fmlnxT5TK3M3mWNgQcwWh3ed14m5nhgYC7Z9mJoqAY3_wcUe5QZHQU_chx2hhDQc_AkvED24oe_T6e49BgQznyHEI4T4pt1gv6rkLKr5GBtjkOgNCVVcI2cZHX55_864Lp67zkEY6vccLpOKVBf8RQUeqc_GjhP-zD4v8_bDOKFURwHdvpxjotDF8HAcm6WdPGxQHueRpsG3Wypqc-Amuf-mz8y767I5cMjVPePm7gMogsDB9d-l6nesvGimtIEzk207cDl_weVfacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTkZcuUVIDXX-4BWkP7FHLxUD1qIhFrN0Y5mY5xZ2McE2C_EhLiEGaCTHzg7FdXuJlivYX4GtT49CSYYA5Q4COtj2vnhAYsr3r0tGjex5X7XLVnDeXEh8JJR3icqNIzSlUNSnifEW0xEnprf9YJqOu2A5HCweF2ZL9qpUAZmRnrPlWLAB9K7e_6jIsEG7rSPbXrZWeSNQ5cyYLUhYV1dYEnIDo5XMgIO5rJh2nb7thnuwkKDCFd5xDbAIpAljRaBShy_uqYglY2T06IJEsh9lv_8Po5R8UHQW34KWX8_9DE8WQxAAsIWBMbourh9VaHEqkJ7vQgnVtS0JGjUDGzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_JFtDeThjS6eBLbAF5D4dlklL4Jzug1pj7Cm2Eq3J1j-9HyY7vplR3TZzrfwbSLjJfCii1PMlqZ8XrqCB2xOJfqdJvAl2XOsk4UcBZzkLxK0C9OUtcI7-uaFIqWJUpSViULQlIxWBKvTdBdA5NvvxxUweCuho58B0Y65NUylibtoMNZ3gbXgdCk-6AY-9MX029AnMh0zzwT1PqKaHA8Z6d7rkotHV5BJJyq85HesgbzfUC2NZaB5XD0969hKliLsFwfMAyz93Jw15wkuW6gVe4S76sjeXio7OUW2XCR0bzzuyuc-pJX7V4nK6Me-kxjPHnJHUp_ACTR-SViiVMpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjFhuAenKQM89fzTmSfhmwjlFxnnUWDjiy35sgFHrh38DjSdqHRzzM1xmNQ8Y6NE8QJNnQfZ8x9VBViKhOauOdkX7CY0hdSwHf2huvgSzBRUCzjAtWtahyhccsQtzNYdL3thW1hSzG4nEw8Y-UW-PtGNku5L3iTimikbMZVx4oj2oWVjRQJbxeKi_q8AYeElinh6AkxRE832j8rjhOJOGhANfcJ6TPNvV5QD8FexoDVkVxUF6YCk0h0aT8Horz7vwpDh6wdYqk6IYWPaXJIKLiwg3u6T9SSI7BOQzru87yAFg-wz4VAKqNxoW10jy4WNBPJyJkaeDdYykm9yPLidUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPaibF1C3IoEkJUH-wRWYoluk_91G8ocvOFpNEQNQwbH_UoeV4sMr6BYeawcP5caaBZrs2Sh1WH0YLllxsLZhd8jyo2LZ_fFT5_qZSV0UB2JJjnPSK9M5hjmQd_RpJMDDIDzefUqS7juJcvnJH0u5QhA_-CZlULxDIi8z0lasvpBonwmkhFodN_CNYuAw1lYlZqwrGeOAGIQjwf0H399IOxnE6FDJhfPIlrFrPu376tZln4fzGwJqgUCUilVyMv2BHkmaNPvXYEDcbCAQQwPjQadaATdn-LXs9af7kIfqJd21PJu6UTnFHz15j2GAZ9F7vyF69s3kF3ttTJTlligVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoPlbqhFqECZq8hx09ERitieaXS7pSaNsoL_MLCGFBMfu1wlaI5AmT0DySCZQ1uTztSHpi5GkbOCvph4Xk664JG3Of__2iKd4KD8yQRpSkabOCwaIYu5_3bR2SvZ2i97afu8pweqDxOTtzrg8Bg4uEa3oRaCxViX55GTPH2DLdA1LaTZKDfxZww7L7STI1s7VV79MKa8_pg4qrhegzarw1Ysz_ERWKuF9JaLWOUO6MXelt4K0k4pwteovhfKQ2tI7-hFJ7JUnvVBXXBBFNFXGVD7v2OPzu4fqIZq-NMzwKUIW-OaV0PXK96G5kUtR7p5mlraxLW20uGBIBboNrRL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2MjEQTHVNucdUo0fM_-vOTYOutnugm0qdmMqdI4GVDylfNcs-MvpkaJwHEM2hVSInKqcX-Ow20mabh7pUK0ZpNT2vNqKnF7JZ-_ozf76kjwW3r6QU43vLqUqcl_J0m8TbSSLOgdkANXC4csKfynTXSGE4w2tkGjWZtHOUlWRdrdQy0EwgIoVmW-vGSLyhHjCE6i-1XdeT5xYZpzC2mAddMqjJI9NvIp_f0czhelpWO2iy2LLF1JPo5PhgGn1JKJ_oMSkmTd9cdPkpd7zBU9vcLq44Le09Beqaf8_WtD2NL3MTk-Ip8i057FOAtrt7htnXt27Qx2hLM9iQTG79i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXClf3SE5oPpS8Nf3kIu8tl2oG3cyNAnoZWngsvaoJu8tOsgGDgZw0BcgvMFboDWbDj9841y0waKxl9ZFtGarq000YtdI9JaRrAn0tvahFVczfxYO-m17mpDSacl3qeXlqN8zpecrm0AJq0FstzYpq4rqJxPjtqBvwgVW4eH2cZqFTBzBV0X_lZvTPdL1BqoLJGtwLt8PknJbrJBdb_QTcOyBXTJhNkWFxsvlli_-wBgEcf-JrUDasRZ5i6CI6T_forpCkRQUdH3Q6Mo-tWuHajDQwwOl0kyHKYCTsTUGg9iRFSB5khutU4gwjpwa6mERRY2OtPvKuN5rsK-EwiUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیش بینی مهم ترین مسابقات امروز والیبال در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
بونوس 100% بونوس اولین واریز
⚡️
بونوس 100% ورزشی یکشنبه‌ ها
⚡️
آپشن های متنوع با ضریب بالا
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25861" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bm-2gMgjfnEZ8SXV8OskO19KOPhjr5X72sYUGDI325cv51-Qb_BBT0Tme0IJtrLQRXicn3BneBKboRyDjjdLAFWA5J5FJzcOKNQP5Zn3dBfIMd75GCuWe9mQJtKQIWn_6yKwj6SXqA3NL7r7rAGnCILKhY__WspzbABYpipuwgpSfAK-pkY5IubsFZZIXSAuP1Ed8RwNiQoJzp9otgwjFPasT2Rrli9aocF3X8SBa4YHgXdWuzMMzpSzIDRLrnB-FBRAEwX6xb9TomMXlcAXsuAqh4e3Z0CMnLk6nKioz0Ry5K9qbY65jC1M61WCkDfBSBrkIfegPVTtFti4QEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLyYY9jpUt0IG1JhSmEO8iNm1ZytGtG7afvI8xFj2VlR9FMlGO9D3YOqrVgChsJX1XpO6yVyzY8F9oL4v9lqIutpwH89ENz-3zIcXiWy81FxzW-uFhoHlaD2B9VbyjvFjhhrzm09yOxfirNoyXS1DDMk-mGyYZ9MiJhtbulo2IJBPmVWhIXnpKt9xw9UwZUYs-USDVJxFmNuGUzxxomPt26DnMxGURSooZd3K5sAY2gQIEE6cgFQK3n7AVK3PH4DHTnIRLxX_qM51hyPEWb3MLYfGrielnfi7WtaFdIUILhjKKWit5LxJRO4ET2MsnCT-1o-T5PtBja897hript70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9hT6NWKkTiruRxQv-aUHKSCjcWMD7UdcDXdlIi2IQFSckuMJf9qyZQjHn4jjM8LTHnTap9MFqKyxwxBQK9YgeCOuZA-RR9JZDFLuje3eU0typ3crgu_WqbQYyV8wiGm7OHy1iFFubth5KtS6PU4IfUqtRKAbh2HEhyddoWaEaeub6hGtzuTndO8YZyDR3UvuR-UsjvwgwOgN1B3MFH20S5FYL0TvCRxg-xDAZgriMjf1n81fHxDzVfcfT1WtLtYjEOfvL4T94nUOaFYsLuPpuoRJfS5XnuoLwnowWnUNL3Hxey7oED6x_2dKrD6VwhNcy9ATEz2LrYtpLONB7N2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkAtoveEhhRVQV5kd06YMu8FcrHimQzz1lboRO6ksc-e1A3qBBkmi1d2N_ITaBwLgeEovP9f1AIiXYMukdVsT29FrZWtcbcqM49k__lRPN3BJv-ZhGULF2G_AkqmPVuduXY3qFtf55DnrqmU9ZhXt6gNWiO4py4P9MHPI-Qn6xgqXnlpyWjU-GM7CJ9rn5Ev85VcwejkOR-inJ9LIo5yNR0zlSAQbSwaI-r__Qy3x-1tdQrXTMdiV6R_39d_pxcgU7P07bvTI_ri12Rj0q_ucVVKhhWhORvB7PK_b9pZJ6wIVDlY49GzbOa6abeFPIIo3VjvyRpptrMM7jaIwr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjT1p6dZVHhKgCdYBLiC8VU_40q2Wg7ihPwT_cuiLU5LQ6b1mq8zfeqkL6oKr80IjyhhF0wQSSo8TCvQcL9CCbP_1Vte8KjYMnqzWy5Eq5hsNik9tYtoAV-S9hy1IoDw9kztAusjiIpK9VsGfoTjLiZ-uVRZ4a4l5Z9TN_fOrVf_XaAc2WWy9FaFZeHsUK6la-ZDXudgue4iLVgJZM-6-K2tvQlZRsWWnKa12_5OsaYLwEkekd4n2lPv9Mr1hfE4XpqcLGom1FiO6PzeRlyNbdMCRcjyITfxUIZT5wY4C7PIrhortk-gJ-ncyAgWemSnKWbm0kmwRCZ6RjN_6-0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeKQ0Ejvp0YIeLWK195OLoOUCH7D4Z5J-mOBzH9X6Zwl9M5j7pDCIS24e7sMADx_pJ5z1fj7Gyj0cPAg-gO-Rbh1DiYK9UY_ITJiUPqjOWorZ-rmVfQOIJVeUCFncBL7-S-UQFRXhpmHR-D4x3zpNYmOLgxi3g3IO8ibTs5gElc_TM3HYdoDBjbf005G1w5KcDCHPhDzdm5sxvRICbNW_-ofxqID3CMSB7EU7s1PRQp_BlOVc5fINRC0Gj08j3yxr1VuGiB1LH6bqlxasGwTv8kGStAvK0vX-zpFPZpcltlNKOACz1wRFvTMUfAtRixDsCtcD_y-5S7l6aCmvczoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlHEZ2BU8gHW554_9dxDtQRm80dMH1UXyQf39ZH_jwJ9Phy41HSOrnZhFru_HaUt2Ku_ckGA1Fncvm4g0jcZ-OKO7GNt7S_xQ6eKVaIee13JkpB6trA7MAFuCsHNMTJbQmA5FSM2MGoxwwoAaFygPQzQQcctcqbKsIoDN0q-ybVJoL2OOr2XW9MMI2fUYo9KTYnCouvp3Am_BEhn4MiKyCFtX91FKLowPaPKPY-DY16XMWbM0e_KiCT_FeT_4pHn0Vy9q86DTljNhVqMay9BTapd3w6jNCOl2h55z7V0jeWpoFDaNRJrIvFFAlmYG2GjiVWIsUAbz8wHANxbZ9kPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y92R0j-pejQ2_1viPMke92Ae3tCo1eLiUpif81NzqytgzZsMfy24bJZuK1HcN9H6wYXNW6cuSCDVtPQdEkie4AnBucB76qbPz2B54Vy3KGNaYljm_PDsJ4wLJxAFx-t0WXjbq7t9v1YxqxMjXupJ8kNpngPmxWa2IIsAGHCCTdN6XRgGU_CItW8abmtTz5A_-uefoHx7fcqVV6O09wcpOgoDq4v3cEr4GhJx9UWW81r6Y5nsDW8p-YmGvR4m_4FaYp9hwcW254BWR0BxSypmzBWaAAM8nx5jjOAVsCyhfHypPu2E9Rb9sygS5nQu9iWvE6c5BNfXXiOE2ZlRQZtHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-yOZ9onihAEX06rqIoyTRecYPyhggIEH16G332IquUyyOn3bPzwDJozXjJjb3fE3bMZUx7GwtM1AT9aHUi7x3Bj54ObVSSz-Iygs6MsCOJyZAbPu7zNo_VHcYaLG0x_LCUaZGjcIKPWtW7zpmO75Mm757PRoS9-UBSBaHjH_XRqPZ8DopP13STgzWjerHop7hN4zyDe4Td09dQW5lZJIRppLsUQ9e8Z1GlwwMkUyt4fNRUWEaYhGYH-RjmO95Y5YjDijrfM6zVkMv_5JEORpNHcrcqzdcWiIw3jumS3sIprmzqvZSsCo-s_i5UZ5C5RKfP-ca6oRXpsE-5-bFK96g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X90ThnyIr0eBFvjbofkpHwP0_8b3nf_Cy3eeAmzGrZLvQqLCXhmUGljqB_MGVKDZMfcQ_lSKg8aCf4nFntFij4Vo2ynXhluuLQTKx5FFIk8wzAXEL8nch_t5Pjucu9w_7pBgT97nufJ-XL6IouRipq8iBmEZN-5LPXIVSSOLv5QDKSdG8pv1Eh00QDui5y54pUQWtbjOQt2boduCh9FKxU14SVURk-FzFCrWDZWcR__xSYbxl2jAB3mYNZQHYK8zOnNMe7-GtAu2UTyIEY_mdoJTIdVs9OBohkFUkR5OL1PuP1AzZVxILxUTIFywbK_dua9WPwFlbwHgt_GEegmO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g75Tzt6mcQEcQAfRHyyXZQSa4pgnnSQd7c20Vei5jx4fH1EcDUZWh86MizYz-XSDCdhu1aFWBdLjoahupZbseW4Qw5R0T9BfsLECTS8AXcRFHok-7kLQUgrIbTNSIxyez6sP6fDeSfQqtcqbaIU53Bi2DK_TBHgLRCr5SfsenrhNopNwM0t7CmQOt-IJMuGtLE1VsH_x-afSqpi7TCZng5LKxlW7n8vIyBtue8k7ATLAIPkt-eOQNwNsm7BU9yHh-hhQWvwE22hVHJoCjS5iyp6drUJ8GmdjLfalFBF0qP7dbNe1Ld3e12zmNlJBDevn0eG74ewtl0521uZVgKUKww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXkrIJHkhkHYIW7iOyraXTw5ES45t5NiU133v55_a1Nn_E-fg1oxpltgEWqfqVm5ZgV4WXUzLu9lxxJ8Fw2amsaNWzD-fkwtcAMWbrdOKObzapcHCv4UcMNSlfGspFDlvwiyoMta9bhUwDfOPsfl67EtRNmoanKIAjsOoB2B1iSZQMjypi33TjiNlrHWzDsrmCAQxc5AyvVHqnWNmm8VHtBJjoxEtnYGffNePS6Z1s6l3uYbWStksKHlGrgsQoEyfKgGGhsRWjJdasgqWYitIAfPiebi5DteQZUg9mB7-pvjtkxWUTgwkv_3JakLrRrqIVVYd_lrIth1bvVeV381LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=X9TaOB5y4wKF8qZznfJiYWlWukqDq83HHoudTff2yUNFB-cxjijmSlq-x60zA4iaEAtHNUYaNH0I15iCgASWDjiMN0dTKLRqRJZMOSWLn_YqlVVYNdxllCuDoJU2hR8WrAmT_kb1QYluxbhmbB8OWK6hmWYH84KE--2OTXdvk4TDQ0RZRD6Yj5HGFodU23F-Q26OJzGc7OC-V36vpuS8NFTJOLwgtlHqHXAaG3znRXUyye1LIE1U7yAH-BGV31HR9v9w6rUFmHWUY-tIjvanEFoi3OK8q9evHKx6V3Gd7BKLelenjZH5GzO50FH1paaUBhjEv-dWC4Cwbb8MzcbOCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=X9TaOB5y4wKF8qZznfJiYWlWukqDq83HHoudTff2yUNFB-cxjijmSlq-x60zA4iaEAtHNUYaNH0I15iCgASWDjiMN0dTKLRqRJZMOSWLn_YqlVVYNdxllCuDoJU2hR8WrAmT_kb1QYluxbhmbB8OWK6hmWYH84KE--2OTXdvk4TDQ0RZRD6Yj5HGFodU23F-Q26OJzGc7OC-V36vpuS8NFTJOLwgtlHqHXAaG3znRXUyye1LIE1U7yAH-BGV31HR9v9w6rUFmHWUY-tIjvanEFoi3OK8q9evHKx6V3Gd7BKLelenjZH5GzO50FH1paaUBhjEv-dWC4Cwbb8MzcbOCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE4LBNGMk46R88y6UY66pNZRTyH53k2nMMlPLTqjPirRuisTY13X9vxs_i-Oybb-tepLNKNYFv6soHe3Elc08TA5gseHGlZOzx0tWV9ycFEbiEmeoA_ljGAeJDpKTqhK3b-T0FcKMAfjsHfvxB_qFkLYPdhg2-l-PS-al39ZNLQq5Sv3UvK5OA0kroWv3_KyeaOdt-V9KztqA5DVE9I9X5_IEvdMVJRQezEV8jw-NQYp_DR6SaLE_0seBNrn4LG2Jzh0s-5wtc0EPVXlJ4GBAZliYhmUR6Y_e36h-eDJVFfi5u9SiiAOncsQ1DQAfo7fOYrhnxeapV87Zc_r-Fgz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXRcUNmmu688GvoHO2iIqcYJmXxKYKmDkAAumTY361WffEa1I3ixjFomCyoLFVKHzeNnuUa83DPclPF8FZ2cHnWywDVeOe7F9ivinF7k9OixRZ_oSg94kkKEtlmhsUfvqIRmitBxmIRLbDPpYiY2711s3Wqema7Jfugk6HE5kWsJ2nlZGI-TwHtyPOizYopLJAsEP2KuiVF7u6aB1Fke48DOm03AZz3rl8H6EztphtRKBHxyNWpDAkoQLvwXyW0R_jbcKBSCX91ZkgtOLJAat1gVKdCCVC58vO57hWojIEUD73MM7gewMb6le6P0nsAMRTEAm0jshh0dNdFTKOTqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=KQut1FwQhVVPXddDRKlD6ww2KVdz6SFLCa5H404uFlNBaicgEMXMMe2YbDHZvSilT8S0A5rnlV-aQE09F84thJMz2DbHmGNlwpvkpTHEf4p6_mZ0EJDboZKC7c_t9y_j2eIeHJyXedA-cqxVgTJ2rDX1oPQnB82me_Y-55pghBOJjAl1OXP8dKA0KXxjJkVrd6cYFJgjFjKmLY2WqDB4dAONFTIiHqFyNazbRtisuQ3ItioqxMuhX5EaTWtc2yNWRxwWufPu2cS5_O9x1SC1KIcpGeQToZlCsmEMnFQoYKuQ_7p_0gftYRNY6MUFDxJl9oMMESKi4pV_94GbSeQeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=KQut1FwQhVVPXddDRKlD6ww2KVdz6SFLCa5H404uFlNBaicgEMXMMe2YbDHZvSilT8S0A5rnlV-aQE09F84thJMz2DbHmGNlwpvkpTHEf4p6_mZ0EJDboZKC7c_t9y_j2eIeHJyXedA-cqxVgTJ2rDX1oPQnB82me_Y-55pghBOJjAl1OXP8dKA0KXxjJkVrd6cYFJgjFjKmLY2WqDB4dAONFTIiHqFyNazbRtisuQ3ItioqxMuhX5EaTWtc2yNWRxwWufPu2cS5_O9x1SC1KIcpGeQToZlCsmEMnFQoYKuQ_7p_0gftYRNY6MUFDxJl9oMMESKi4pV_94GbSeQeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALCsBw45GfBpz71vruPfy5cMLagOwmz5gSKiCw2gGflsxOBep3lGN5QMTnR3xas6LTNGYnL9A9f3VHqt3cyfWIGdBCjcrQNI489py8yRqiZ0WkjzjvDzSWbD-phf0vZBUoosqNMHmuV9hREoeNZ58O_djOLeLLoXGqgFBXiZUIb2KwUbBt5r_Mb8pjq5d8h86tRai5kY8m1_1PptbWKNtJneRhsIPBFrwKu4B0khSrNc0F16VZZpOSWb9-CjFZ3zXjG7iZmHFzMNn_7qj5NnoynpiQwPY_O_2i6hhIpcDrKagfNvNr1GX6Ar9oI7npejc-czdeojS0PsjrTU83Xj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=IEEJhDxwFFhTbDT92hG4DbDekg_oJ3JdWFXUVXt9pd2U2urcH6HZ0yPqLrbgvl7-W7Qmm9KNheYBqgjHHMcWoH08JL-vD6EbDoB6IQS0hA0ElmR2ak-UIrqgZlnJcf83_khpkQRwOE4a6zrkIJ1KbACHjb-U-hGbfdIGmQtA_ERgOrw9nx_o57p_Ggcgs_rWZBfVkHeknYy3XFEYFX_KLEEggaUdjXIwjftWUA3z6PQvD3_U_LKnLuI33gJsedKjgw3UE7jmmTt-WhUSAUE1BljCJcR05UE2P7-G5DLyH9NSPdznSOSrd9xAgB6Xr0yvOsBNj0umjf7LBzEDP1yMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=IEEJhDxwFFhTbDT92hG4DbDekg_oJ3JdWFXUVXt9pd2U2urcH6HZ0yPqLrbgvl7-W7Qmm9KNheYBqgjHHMcWoH08JL-vD6EbDoB6IQS0hA0ElmR2ak-UIrqgZlnJcf83_khpkQRwOE4a6zrkIJ1KbACHjb-U-hGbfdIGmQtA_ERgOrw9nx_o57p_Ggcgs_rWZBfVkHeknYy3XFEYFX_KLEEggaUdjXIwjftWUA3z6PQvD3_U_LKnLuI33gJsedKjgw3UE7jmmTt-WhUSAUE1BljCJcR05UE2P7-G5DLyH9NSPdznSOSrd9xAgB6Xr0yvOsBNj0umjf7LBzEDP1yMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXn_i0WsnvkiOUPM5f1G9sGNe0hOgXo4afzN6Jq_1xH1caHB7tnateBCHrHWMiCprfDZvIAGjOOUonBhyF0c3ECgGybm6pwxqQPXvWjVce7wG82b0L3bZNHSNS6f3ptL49D5V3GRjjXXPxAfEvKEuzWSm0NDG8xM2VJIPrc9AxuDF6kj5Rc_psbJAqz00SBHL4dhu80GnvtKiuM-kQc_4_CpU3j22o9aiIgZeDSzGUHNILc53Qjed-HyaC5G3PwgJzVH6zzGLaJo1SHfhycGH-T_tOXYOPUh1XY4hfCQuoRm9qSZsvF5YSVM2KkWWn2aqO876xmrRCdLqWPPiTT1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6R1AHn7uovHQ9FzuBx9VwJeMkAdzCfIIVxn0fBeQi319Ol9b_ZvlI928SCrWOjMm167mgc1xWQITEPC_7T-LAcDbTA426BwZCXcTvU1g8yf9eJyp0H-_fBy5y7RcHOl7ZWDFOreQUyxPtL-q13sU3bAw5G6HhIoeuIYxjkTqjtugObKu5keAY5Ijb1ly793g4jFC2o9Tkwv3uSTRdLQYfUeeLfA0oTykcXGqkAfOm3leCnTLyVwM2mx5GRBjEvXMNvwM-8JPL2IKexwMVa1ZUFGyEHKI5JQUSB__wPDoqwI6WzPWGmFlwtFBi-LNhNbT3uJ7pEbfcjxIi1tUHEvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew3-_QbZbRZZ9TLWbbexfqi5RziWnWbIV7Jps179Ua8JDYRxqJisFgR58wkHPVeSlEI6T7-gJd84CVMRhGjuFkLWMMnuR5ONfw0ngZ3WsmTNQEXvJbafJmi45X8wnGt-rg84OZ9j1LM8eWzOQIvHyDw7qQhfLOFz4CpFrM56HPwBLSEvKwpRW3ZOiyt9pzWPrxnWnDsyDcKqbNKTLaS-XG8KbkIzmt8zwYPne3RPWODd_oWnK7OqdSn1QIgUFxVnHTQkBQOlWsRCSuJrJQr1CH0FQdCN0k0sz1Gbj66Zh_CybEwBYoSQ5L8tCr5lrie-EFkBmMt24zdd2wCDIET0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC1MAZh1f0qIKv2eJLWKLR0Q_LVot5qYrQ0Vk8rzHPW-7xBT1I0VFlDrLE6ppPPSXm-FMiWrKn4_B6-FCIOy3xvr4bfP4UUMx3UlUKIVFeOxigbYAGH931xkvcrsb6XylOtqXSVkNXrTMa7G-PxYJ4UPfbqX7EhApljIEp_vNn48LQ_nr1lq1w3fVLOXKl2-k9hhr1q12RAb6KxDnlmexzGHBDYNtirb6UP0KHB0sC6Bq5ZIndAi6_O1b2ENfJHPepfCw2YIxlAe875xZzXo7vWW6JC-s1A6fduvBM_JH573SFFOTDMJLnXiiucv3hgXFcUo2OKAe4UParhppy3TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Nv1HDBmXAB5I4zlhalZL85KAb6L6YTm7HlPTDomjTFb0WBUqtgZtwdACd6q4FAetwNIh02huwFax9H44B3Jhqu-Y9WDHHx_ItXYB0GoOtSgEfbnGPlSrK1xvZ-2JsNQB-RC_8mQj0vBt8YQgzRnB5ZLXuushgJjF0yTCcWoca9MEszgqc_Kc2Yj0HEjtDTQsGWdxgqhumexELVQRUo4Bs9fuMgBs7iulyCMB1T6awf87DEC7aSj1_YjT_XkAsnwRGumzeI_QA8o9-1o5C3I2phlyhbfgR3KShk3IJyWQf995mVkZIjAdNtH3JJ5EJcCxSiNw_0MBCu2TAWBcotDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFX67FDKhGyflSLvKz7lLpiq1XQCoG3SlZJxeBj6YUWWTwirme4mA7DQV-vZ93Lv4gbr6nwTlcDuzsUEyaPNinzKexkjWqDDswsoKE_0-EVeo2-_J3np8svLdQNQL31Wzxt2DR3VIv4brNjgeHYQdcZwcQHbgIPlofaY6jpMv3azKluVwR96SI_Rz4-j15sqcrnQblO06j1UvJvRA4ZxQIL5yoAMiETEJL7h9egQrEPUuUTFloGjKuDQTy92dohFXEI12mozhYVeArqmfousz1KQcF0rrvcjLI4sfcS7EV0LmGaRaKPlUzgOe8qHAps3frwB3N1MEdGVXy8dRXQwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh3TLQWPsuloxgE1162CBhwzQ3khgdSZPFhDaTqF5NOTscYsix-JHBq0JXekAinxI17m-Xql06UE5LUgtoQrOBk-lvrrQpPxjEib6VIYVB8Sj4ja7PvnvUfBPO5bYcyNu3bm9-oRU8GosfBL3VAPKV2crv95ITX1Nl3ntr07X3nrOpgjoYtT2bQDEoDMAvzgkDlYCXRQCSEFwzgBHSf0ccyVyM4NGXnJ4k-Tg2qwphv50Zhhf0n3tu9YK7E7T92Kn37vpGU6l1FUegTYauSekY28w8tIs9AK-Oar3nAvVSyHNXc9yC6u9UIxOjD5dILaCZxlH6Po65YvpHKyQsOkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRR2aMLEDGOIxKQ3-N5fR0OA0erHK8RlBTg93E9CC2lag2Bg4h5-WACE85KSzy8vB2Wv5FR-oIMROAsz8k-gWn4ds1kpIaMPIyGfd-Ut-4Zp9TZatD5ix5VTpOITyB6LHNJa2Rq6P2SuytcX1VXUcK7BHFNIxc7hwBhmB2HK3N_xrHgllo16xlsrjGSncfNNpXZleC3YBAyplnyL5HCNrBYdHj6IiiRAHo6vts2CAL6kkmQg5lAyLhw-9hzn-CVXHCL9_X3DDPtB3nRGSvbVm-v9E2NP7CaLtlHQOC6NFsfdXyS9zPflkVgvpbqK1-V0iUB7DVKb2DUFpc7X0MmZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOl7dwvCBGl70KEf6Pukc83HHTnP7m4Vnwg0yf841MrUBKypQc6gPSa3YPzhQQ0RLlLFdI9cI97FrbTfZ2stCTCb4lSHqWFqKviINtrykMUQizZKjhQGbJItNVvKAsMzf7FtGBXq4l3xPKk1I9irjGOw_8m3YIPV10HKIu4u1-qjN6oGEZ3AqSW_S6sg8haw-3gbzZt3W6OX_UaKOcW26XIS1Iogn4QrknI4MQAGnsPrYcEheTxU1qFTptiAfOaqdu_d7RvFCrwDTpM_JeXOQQh_nd_aj6FZiH2uxX9fBiy5viiNiYDo66v9VAlDgTyPYcpeQ0UKRkg5MpNR5UwouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhsk9ukwewLbWwxPpQvB54pLz27a1X52stWcZRQ7RWbrG1QNnJawkH-bbUI_atWHK_KSmoNOJk2FlHPBilIUmCQEBhkO17_aj6LIjLpOMn71-sac0F0pxruMbmJa_FTolKTD15nII7iGSY-LJuqcX3uDBlpmaQLO_pw97__OGmYMpoOi-CnN6w_yqeuqGx4smpKr6cn4vUKKHDvxQKrlpV4n0Rgo6IGfw3WelNgSL6FkDVPH9IY9vccQ2489gJbv1kLG05sGHDzYUzQGWPieeyDdmjI3bcThIym0Ipc-QGqAHIkqN47AN2gagvLOnVos8irwVvkGAJalXU3XTvm5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=hbArfXtnYUVNX3BE1NyquBUKezTmK54FCmb9hLyB9IRubvr1IFbWI6GBn7HbDhAyH1WBNiaad_XTWUv4rpmxh9fFmO4I2JFpSYXvazbSyxzXvQ_9zrU_cykLngQk_InzoE1yw5oKf9OCBk_vTFNxkiucXZNw5rhP4FN_TM6C_6JDPTimGOe6_K11KQgi4Yzijb_rWK0sOi5bJcmeUukXHmGb-9U0bM50m-UQoIBEPTNGzuMcaTQ1BO2eQ9JzzDXowrEsuoMXRltiwlpQnKt5BmrzTx3Zuaez1PQOsVi_eTOoTdL5_SQdiCt6BDVIZ3esjEKZ4OxS9Ssiz66iImEa4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=hbArfXtnYUVNX3BE1NyquBUKezTmK54FCmb9hLyB9IRubvr1IFbWI6GBn7HbDhAyH1WBNiaad_XTWUv4rpmxh9fFmO4I2JFpSYXvazbSyxzXvQ_9zrU_cykLngQk_InzoE1yw5oKf9OCBk_vTFNxkiucXZNw5rhP4FN_TM6C_6JDPTimGOe6_K11KQgi4Yzijb_rWK0sOi5bJcmeUukXHmGb-9U0bM50m-UQoIBEPTNGzuMcaTQ1BO2eQ9JzzDXowrEsuoMXRltiwlpQnKt5BmrzTx3Zuaez1PQOsVi_eTOoTdL5_SQdiCt6BDVIZ3esjEKZ4OxS9Ssiz66iImEa4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=hmdqp5X0xVSfFDvfWgCmSOJqDQg_K6Z2-NLVJoa1WrELvGHh0SL1Ca4nYSWgGcki6p4uGlnVpN0cmORTFGTuklClkWdmwacZlePtC_TI8XYZDG0yd2FiCczeAV4w68rSpB0slIoYuAO4H40xGEVcnpNcqUtcWuhpXFkO93pLuY5krdWU3l_OhkqELSj6y7uP-bQpMn4oNt41N0gUD_SN0MGUxZnFQgFUDX6nv6PLlNy5VZBfQIMFlBjkjHnZGt299xgyVZXMvuzt4i2rkW3CP-bGiilnaAN1RX972VkFmb_lwgVSc9n254mxEPjgZud-kKdWaKC65Hhmqkq8EGVprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=hmdqp5X0xVSfFDvfWgCmSOJqDQg_K6Z2-NLVJoa1WrELvGHh0SL1Ca4nYSWgGcki6p4uGlnVpN0cmORTFGTuklClkWdmwacZlePtC_TI8XYZDG0yd2FiCczeAV4w68rSpB0slIoYuAO4H40xGEVcnpNcqUtcWuhpXFkO93pLuY5krdWU3l_OhkqELSj6y7uP-bQpMn4oNt41N0gUD_SN0MGUxZnFQgFUDX6nv6PLlNy5VZBfQIMFlBjkjHnZGt299xgyVZXMvuzt4i2rkW3CP-bGiilnaAN1RX972VkFmb_lwgVSc9n254mxEPjgZud-kKdWaKC65Hhmqkq8EGVprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=jN29ZW1drtsgbndSH9dgpfqNfIWtdBtduM-MYVqLynkvT_E7YHvKn9l5iXTsDdxHybArLmyactzxixh5D4PgXqiWo_8CZp4XgW9oFqDRw-z5s0GijzZjZK7P9YYfTLIquYiM2c_xrtphCDuRS8-Cs7FOajqNaAQjdXayVML5a9UB2m0zpvQ5BKwGgKLiR0SXCmlib8k53PDyh09CnESOyrGMDDnrGAy4kHrByDU228rctkFfHr-024WlkvSWGrDKvzh76YcbM96TAN3_TRcr7ARAYdXbYM029Ohferg1Uc0CS3BEiSQWPu4kxHiPNxK_WAO3IlZCXgO5Rhagb82k9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=jN29ZW1drtsgbndSH9dgpfqNfIWtdBtduM-MYVqLynkvT_E7YHvKn9l5iXTsDdxHybArLmyactzxixh5D4PgXqiWo_8CZp4XgW9oFqDRw-z5s0GijzZjZK7P9YYfTLIquYiM2c_xrtphCDuRS8-Cs7FOajqNaAQjdXayVML5a9UB2m0zpvQ5BKwGgKLiR0SXCmlib8k53PDyh09CnESOyrGMDDnrGAy4kHrByDU228rctkFfHr-024WlkvSWGrDKvzh76YcbM96TAN3_TRcr7ARAYdXbYM029Ohferg1Uc0CS3BEiSQWPu4kxHiPNxK_WAO3IlZCXgO5Rhagb82k9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1x_DQRfEOPFBliuXK2VENjZ0dkQ0HYcFZ14FY7yxTgx08jEOhjh2Q4OApVRnAv05wtaZ2dhq--g7Hh78H3OYLzg-oDyxTeQUaHt7YIRNjsblRoXVS0cjAQVieSco1qvKtguhpU3cVLn4bjX0fNObdShEv6g0UMq-e8Dtu6FooajI4f4anPejdyk9EruRhISIP647i9fOCZ1nBKAHX_dWV0vwF9WhHJX5oMSuLk7Q-jGQxRnNfJzTo7zt7zTc9Y6H-vop3obEGQRNW-2KJ7LLtGteA1HbdNo3Gvx34vJGtAgy39KPcJpcmlRGYvSoxoPP5wBldGpZBPSRAoyDG4vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfzFIKnNTakwj2elfbWXLa4kC3IqgBwOdPR3haDov2txZqPdU9200mVepIEscS5mZPvP3oEZiobEdnesQWgoErvfKGf4fgOa5A8Pb11IdjKnmgdqOh6W1BnsjOqP-vNush3S28WC1RwOqEiTrpjezSRcYSyQqObwLt90EIOKDmruXtJ6RLKlPoj82maR3fJUzrR4Ry_CIS7H64TmwlRCr-PbHrE84Nwsi046VyjOhKMQtQORmH7CHMqk_b5uU4G-PSPpRA5VKAZCCT2fhyvl1NwQtxygu3PpwnLpWjn9qTFr2dNG9IxVA00wiYO0VjxDFI3Shqn7wPC014uLV5x-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-Xx8SNzU7xPUgbkmi8ZvdUtvkZaeoWbm7GvbTVirsmh59lAqwZq8jc-2uZdYgBzNpW1iPh4Pu0dD1whk9TkDqHILqTc_MtqPOKMz7dYbSVGdIJjkfLTVJ8Fl_WPVA-Z-vgKzp07mly59XS6Qm9YY8r5amswJorh5TZRim3Th54GXF-QH8zN-Fn35ZfKrmHgFP82-VUTbRrs6u2ev1wrcuCSj1WIxMs0dyj7jqVXVnh-Z4aD5SGnbJD9qqNhaUhRbeSiX12ro8UtFOk-FSnjkggbtEXMA3t5bgepu10b1si2BqnyEIWpgCs_C4zEGK9vIq8sg0pd60PYB-6iKBU5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=V5mGSqOdEFzF9AguxXOcGRKph06GWVEAIIzTULFEjR3ilFBQ1hWR10egQkhm0f8YENpGNb59MSCEBL5GVspw3a9-fYouQ1TuVKi7R0K-gBS0pOO7fv7ztytajPBp6zBbK2xFr2_w243Q7DpDPidu9z5vsrl2lRGHo9pO3UolVXo35Jl1azSmqBsPnExfpJ0P7zRaMqjA_A8KtDR_sDvdKQcDC5uLNMqfOiG8e6NpvoaczzA9vqn2n6YS9zE5xR4YvCTlpk0rXI1ogSlkdZrUzetK86RieHvFX3wvllWA1LkGZF7Av9WjbPJUxfXmmRBHvv3ovkXkoQdXS4LyFJjHQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=V5mGSqOdEFzF9AguxXOcGRKph06GWVEAIIzTULFEjR3ilFBQ1hWR10egQkhm0f8YENpGNb59MSCEBL5GVspw3a9-fYouQ1TuVKi7R0K-gBS0pOO7fv7ztytajPBp6zBbK2xFr2_w243Q7DpDPidu9z5vsrl2lRGHo9pO3UolVXo35Jl1azSmqBsPnExfpJ0P7zRaMqjA_A8KtDR_sDvdKQcDC5uLNMqfOiG8e6NpvoaczzA9vqn2n6YS9zE5xR4YvCTlpk0rXI1ogSlkdZrUzetK86RieHvFX3wvllWA1LkGZF7Av9WjbPJUxfXmmRBHvv3ovkXkoQdXS4LyFJjHQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmsZjLhUYnvf24Shk7oNz903Ffi3nUlbq-Y4EeeBdJJqD1VECF4D49nDHE3uwi0PlQ3kQGETPRiI9BwkrxIm5Yq6usE7sdsrQJNFa39iefDqstDTbzG-esG9qSUeCpzBQdOBgzo8V5ldpKC84t_z-X_6d-zrGcThn5e2YKZV5McVfBC8qQc1cU5Z0qrKOhxUplbwZ6vwH95SARsFhnX2gcAGab0xk4dwLy5FFjLFNzk5kFk773A1wxvNqadT8ENonCh76ZP1_uzDgPus9CSuQy3EIn3y0uVKu5y2PaIpRJer-SH1wljUeoBYGtFQ7CiXdwbj2LDFU2Oj0ptU9tQl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=AKRTSSB5s4N2Xp224-uIb0k1yu5CYu_gRnVpDQ1kJSgcd9MPeKYIFqsEC8eu79ZmP05T6Q9ajMqCBbd_p1Xf5MosEr4VWf0fxlZQT2B3ZPxK86PbUqpS5AsG6N4wZ26ryy8Z3e3MQciZsvAhdh5hBo5r1UceaHVcOHgQQsIt6lou29Dp8oKr4w0rxUuu_42vkG3eOaXHQdxvi3TF3GkA6sUwS1poLXfZ0Z3UZQNqdfrNItH7DrE7OYe929LLBb8jfn26hFiXBDczfuzOn8L7YrYSQmT-IBUX_XK1KUYsN7O2txOwlPJ9DlEpfBhsECRbceCOqi81_t3SHIwN68-4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=AKRTSSB5s4N2Xp224-uIb0k1yu5CYu_gRnVpDQ1kJSgcd9MPeKYIFqsEC8eu79ZmP05T6Q9ajMqCBbd_p1Xf5MosEr4VWf0fxlZQT2B3ZPxK86PbUqpS5AsG6N4wZ26ryy8Z3e3MQciZsvAhdh5hBo5r1UceaHVcOHgQQsIt6lou29Dp8oKr4w0rxUuu_42vkG3eOaXHQdxvi3TF3GkA6sUwS1poLXfZ0Z3UZQNqdfrNItH7DrE7OYe929LLBb8jfn26hFiXBDczfuzOn8L7YrYSQmT-IBUX_XK1KUYsN7O2txOwlPJ9DlEpfBhsECRbceCOqi81_t3SHIwN68-4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDsQHfNJM18s69k5gCCK9qrfTVBlcX1kWNL8ZiD3cvkFvPgiNleta_OwVw6DihS1AaxgntJ05NdU_ymuxiE6dmrvrnbiiTNAI3Jwu2po2RurRzZlv-jdEbWqXudAT4V1ekOk3bObyoOpqiRF-7Xnn8V2jjwNjaG3bS4p04D_QweUXNOGaR-Pw_zfM1Y4t0VvJpEXD-lB3A0xKVp-6w2wJNNU2ODCIGB_HmzSQSBuAOwVzIF4anZ2qmDLeveJGGIUMbjLDOKNmXu_LgEgkWGUC4KwMm4R6KqTJvVQhJKvx4vVUxFDvf1Rc4KjTazvsoQCv9zVZ-f-U3Kl-irXgb6b8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=U-jlrKbBHee0sbzwoLyQg4rmVdzsrGrBKKJPrzccQ790JXxSivFUfQqpbTQMcAgH_f0qfPuJPoFEfxutfDtnto9K08mz_CJGqc3Hu25nRKCP6MK8Ot4bbv6w1k4GTL_Gw5WVnPon0q3V53RUgODSxaokODIOKFM36CHobRe0972rfOwIvBB6AP0GtN1QtNtbMNF5O_PTWyo7ffj77_OUaGEl03qIjsO-lHg6qLqJTkI4octC-tv_Nl0MeNitZTEpphywj5FXie7C6yCTlEt0FCWtN2iTQqJrezvjO7I4GrkFwSXrWlWKyLDLB41gIstF0fK4tsTftEwkcglr3-gHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=U-jlrKbBHee0sbzwoLyQg4rmVdzsrGrBKKJPrzccQ790JXxSivFUfQqpbTQMcAgH_f0qfPuJPoFEfxutfDtnto9K08mz_CJGqc3Hu25nRKCP6MK8Ot4bbv6w1k4GTL_Gw5WVnPon0q3V53RUgODSxaokODIOKFM36CHobRe0972rfOwIvBB6AP0GtN1QtNtbMNF5O_PTWyo7ffj77_OUaGEl03qIjsO-lHg6qLqJTkI4octC-tv_Nl0MeNitZTEpphywj5FXie7C6yCTlEt0FCWtN2iTQqJrezvjO7I4GrkFwSXrWlWKyLDLB41gIstF0fK4tsTftEwkcglr3-gHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=nMb8Y3jz5bixEGy8A6OWmXOzpJVwbvBcEe7ywsNWswztQ_wuTgpVhmcly8kLbe8M4GtTzMWthvFD9nH0L5W1lFv3qdKF8d0e9IctX97LY-nEWC04elaRw3zssh4bJXv_Egx3OcNwQbYgxyAKWxwH7JSlmoY0WhEno2Kni4ySjdP-oGZxPLpnC6RXpen_LVfo33UxLTEDxxlilygBUS79l1jmPS0w3Ip5CL8Cdgwz5qLm_gdrtKkk75J--F14EUvaKPH9BKFB7ls65fEBRF2TlW9dp19HV2s6LoE_GWirHwgMXrf4Ezc-2xEpBBHLcPxpBUgQHMAaCt701eEWC_S45DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=nMb8Y3jz5bixEGy8A6OWmXOzpJVwbvBcEe7ywsNWswztQ_wuTgpVhmcly8kLbe8M4GtTzMWthvFD9nH0L5W1lFv3qdKF8d0e9IctX97LY-nEWC04elaRw3zssh4bJXv_Egx3OcNwQbYgxyAKWxwH7JSlmoY0WhEno2Kni4ySjdP-oGZxPLpnC6RXpen_LVfo33UxLTEDxxlilygBUS79l1jmPS0w3Ip5CL8Cdgwz5qLm_gdrtKkk75J--F14EUvaKPH9BKFB7ls65fEBRF2TlW9dp19HV2s6LoE_GWirHwgMXrf4Ezc-2xEpBBHLcPxpBUgQHMAaCt701eEWC_S45DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG_PsbPbJNYeWWrPdEPXcpWthxzS9wt0Ryp9vaI-5cDkpJEp5AGAqF8VCxDcidvMrRnviBGOISgnueBALY2lXYnCWhVkX9H2rK2wl6_Pke6peE__PG3GUBhheNIZ2k1if7lnyYdrIu8Aw4Pio9E1zCjuAdoyhQnhc0-9dQ3MrCWCpUvL3cqmmlZtft_mgM_7atuG4B71uD0Ju93PDk0CaDB63Yvs7iOUyn1JxTxiLs5YG0xL37KKv6yz4fxmob5GvBG5aFV7trS2lOrCyqdxXtF4kmDkIYS5xb9E3ZhL5EEQ18tanFc13kxjUC51fC-uA6Zh5Q-r6vHf-FKIQGm5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqKo_NwuOBN0H0AdJTPIRO8Wyf89SFWhobEA07YH_o_rZam-xQ2Ua3g7CxJByPM_Dkhv-lMlgqPk8RjROlpzW-1QNXO7-kpUeWwcyq0tPiF5LnONf_DaD-isu5aLYKL6qpL52RuX1w8YvEFeTXk8oLFPSLPxb4F3Zs45DfVMfi2xUZ0vZ0WTNg5jALxPCmsa7WGom5YUUbPWK2YmrkY3qpE9kmN1yyleqjecA7qTWrnkjbZrb6LAbAidsAeaXhtvbPQ8TMOM7-KMlPidYaHZJhZb2Rdw4a2qwLGnAXc0Eewq0iYANKCb4JMzV33e5cVlAJ0Pf6GVpIhEXfrZF839pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avTEb74d1cS0g_sQjDtBmMvBH33KM8bHzuEk5NI9vath1FsMnm4rveiRGpmQuwaEIgXOwllBcxvkWLzspdrylHhGrnnSQ0ObAMOXX8I9UGH01G0XD-CyrtrF-9bidVsG6f-APHa7ks9RdBLb4fpRUQYF5H65ikkQ3Pxvr1OTUfnIJoMc5qDiZPm2QNFEgplvUrtZBPuuRURbNHvgBy9IRAlzLSxS2jIGEDZY4ZUNd90a8eRMgJxb5Ym_1jerhbs1Vx5gi33JFQtG3VnlJqDO_DXlZGYxuYQLFXrnhc4RjVfxOsOXdCv5R1pPx7F7B2-kRdGqb6x5CypSqoGFSWqeHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQh6gnNzN5Q-tCNvSMD8tbMAruadfxR-6qFJJiz5vV5TljyiW7YVMBNrpUNJbpWUuYFPFfej254Qea-npzS5U99ibHrA5-TFAuima4LtXJ-IXkQzDGKX60dLhioPLlAwk2v4X-oCi7N5PMDlOnpOlYXjwpWxyC9N515mksBq8Wp4KwKzWl5PO9QmWLZPyvk-lZyjByxhEFRzwHAqH08NUrqBxUcmuPwTY4QgIcUUXlNrozjvMm0MVgN3FBXcgdrvk-vNaA4lMcTfwVdaBk9kUvpS75E8rwSso6XW4xUqzeKsyOFQs_Z5ri7nMpXKxeIMFDoc_-63rT6QVe8k-uFnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLPRLj7BLhAfdLfs6IyGXVzzsBCXBuiaLMwemYro4ZkaCOKyCJ4ZpnT2KXE8DbXoM3LJKfuqtTFgbpqKnMIKjpUp2yHKl5wAFEF5wdCJnidGDgS6PnNRPd8IAyqg_KhOcU-ypuMuoGExvTbAKv_T8p3kzGcktEJXX3RZixb2jSgOcUtkNujCb3jRtZrKxvvs_xwhI6_kyfq5sP-cAGNDebWopXQ2DAKfHbQbewdPwPly9c4rXXGZscYZlkWFJDB4udzRE7DhhBKvdWbzrz9l6q8PY9Nf44Iw5GQzqXiXhkJsL5Vs93QxJc1JEglcNRrLrMgBEaU5Ye01rfOMnyqy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

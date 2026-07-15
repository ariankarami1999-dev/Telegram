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
<img src="https://cdn4.telesco.pe/file/lFrN6vs2N8L2eKLbjCUVHztZ18qDw2l2LF2EwNurIJ63TcJWTpSmsyrcGSvydeVDd6FSZtgNUanLezaRCf_lvjRHViJDeMxQAyNXaU-Z6EQhV-WNqrBdosWID43fd533KHYGjtWghF5iMQRZYkryFgZ5BX9cu20WWdkf_J_zO111LXUvGYcnA_EuYYTzR7mZFxpaH_PtNTUpOsDTM99pBJsqOkgZFI9AgLpZrn05x8NFVwiYIsvsFWUXXwZMt7H8zKRJeyTI1Qa3wMrB7bCQmHq5YHb7Rwix7Lt20IVKmJbtfrzJgmVaOSAs4dzBr0gIggHc1qpg0_YdKbl9-vvH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-671401">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HegyA1Ea1aeV-BvMfRgAxPVgGLepJBOeoeXaTe1t8tlJWjbimRV-xiE8cDDFM3-MSlZ8xx1teqCDIOOyYRpU578wwxEY4WI5NK4A1JwevUasJbqSbKftXl9xbz4Up9LkH81eFwQrAXmDtkGPmC8HCKJvCyGl8EGYHEwrKHI33hbYjck4j0IK2Kwp-QeveFOEePP524oaZWwORDg0VTe_UG_8QTGlit3Vf0ImO8MiCSueeuwpGfJcXmcxrUPF6JaWOOCcdzKU5lIuvk-IZQpp0mstxg3eZy0uu4-_d0R8aa4DzoQ73A1IaXASBKytrP_A4U0Efb5bcMKZ9xpfbSMC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی که از سایه برادر به مرکز قدرت رسید | دارلین، خواهر لیندسی گراهام کیست؟
🔹
دارلین گراهام نوردون، خواهر کوچک‌تر لیندزی گراهام، در مراسمی رسمی در ساختمان کنگره آمریکا سوگند یاد کرد تا باقی‌مانده دوره سناتوری برادرش از ایالت کارولینای جنوبی را بر عهده بگیرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230598</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/671401" target="_blank">📅 16:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671400">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هلیودون؛ ابزار تخصصی معماران برای شبیه‌سازی دقیق مسیر حرکت خورشید و تحلیل نحوه نورگیری ساختمان در طول سال
🌞
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/671400" target="_blank">📅 16:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP-hK1dR_AVswq5vzpC1i78um-zqsTuO4o-ToSpT4QL7P1IglSrOJvGK1E-7l6yKr9tObfnXR25zdno2iAo8lYOVNmdApngFlz1Nkg-Fo82mL3jGbdpkW6tRx8ebn124Nd3_awvopZQIaJpmlwQo9lKRm6oh8PipwDnqPfZ_YQsPTkCksNBTulXfzJuXHUIzPhkr5QVkurRe4UeGFL5F4tz_bh_pa8s2xQnkkDYdhK1NPnYshmlr72iQvKd3UdwyBaZ-paEPTaRCtt24S2Rm90LvzvHIQajfADavWte5Ks18jlOokjdqCwbLD7L6ldfXvjUNra0VsbrgWrXD-nHAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور احمدی نژاد رئیس جمهوری سابق در سفارت قطر در تهران و امضای دفتر تسلیت درگذشت امیر سابق این کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/671399" target="_blank">📅 16:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با خرج‌های روزمره و کوچیک سرمایه طلایی بسازیم
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/671398" target="_blank">📅 16:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف استفاده از کریدور تحت حمایت آمریکا در تنگه هرمز
🔹
داده‌های پایش ماهواره‌ای «کپلر» نشان می‌دهد با وجود ادعای ترامپ مبنی بر «باز بودن تنگه هرمز»، روز گذشته هیچ کشتی تجاری از «کریدور عمانی» (مسیر مورد حمایت آمریکا) عبور نکرده است.
🔹
در همین حال، آمار حوادث دریایی در منطقه به ۵۶ مورد و شمار قربانیان دریانورد به ۱۷ نفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671397" target="_blank">📅 15:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رسانه آمریکایی: پنتاگون، هزینه‌های واقعی جنگ با ایران را پنهان می‌کند
کلش ریپورت:
🔹
برآورد‌های داخلی دولت ایالات متحده نشان می‌دهند که درگیری جاری با ایران می‌تواند تا ۱۰۰ میلیارد دلار برای مالیات‌دهندگان هزینه داشته باشد، که این رقم بیش از سه برابر آمارهای رسمی اعلام‌شده توسط پنتاگون است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671396" target="_blank">📅 15:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سنتکام: دور حملات علیه ایران امروز به پایان رسید
🔹
فرماندهی مرکزی آمریکا در پیامی در شبکه اجتماعی ایکس اعلام کرد «در جریان این عملیات ۹۰ دقیقه‌ای، مهمات هدایت‌شونده دقیق علیه سامانه‌های دفاع ساحلی و همچنین محل‌های نگهداری و پرتاب موشک‌های کروز در جزیره تنب بزرگ به کار گرفته شد».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671395" target="_blank">📅 15:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671394">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رسانه‌های عراقی: دولت عراق در راستای همسویی با خواسته‌های ایالات متحده، نام حزب‌الله لبنان و سازمان‌های مرتبط با آن را مجدداً در فهرست تحریم‌های خود قرار داده است
🔹
این اقدام پس‌از سفر نخست ‌وزیر عراق به آمریکا صورت گرفته‌است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/671394" target="_blank">📅 15:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671393">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: جنگ ایران باعث سقوط ترامپ و حزبش خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/671393" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌ ناشی از گرمای شدید ایتالیا را فرا گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/671390" target="_blank">📅 15:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلدان لاکچری با هزینه ناچیز؛ ایده‌ای خلاقانه که این روزها وایرال شده است
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/671389" target="_blank">📅 15:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRq640HP-2PpV_4m-f1UnhWybsRH1rz8YRYLFqIkLrUM40a2954VNQVVoErbHA7ts1Z8DGrPTsvodoo-nrxAhFoRIz0ZGudbDeNYhFIpecRfsI9S1qgYqGujq5uJkgXrDxLMskNb2QZcYHrx89RSybcYUU8beV6V4VJhpnzImyVxwszewWZzTwIWpxYneCWPNYyWyVsQfgkw0KItWbZ-KeFxTgFy5jz3Z8UqtYX53-Q1oPmT_Zf2yzBt3eFnzojXNk23yNZFJeNcYfNRWhMsyR3kCpZHzQQvAwD9PzTxZFsBIg15Co7khiMiaHYIhWImy0E2waCXTLKoFi4B7OxVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
تنها ۱ روز تا پایان مهلت ارسال آثار به سوگواره رسانه‌ای «بدرقه یار» باقی مانده است.
▪️
سوگواره «بدرقه یار» فرصتی برای ثبت و ماندگار کردن روایت‌های مردمی و آثار رسانه‌ای مرتبط با تشییع رهبر شهید انقلاب است. از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوا دعوت می‌شود آثار خود را به دبیرخانه این سوگواره ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (پوستر و انیمیشن)
📌
هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش به دبیرخانه سوگواره ارسال کند.
🏆
به برگزیدگان هر بخش، جوایز ارزنده و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت نهایی ارسال آثار: ۲۵ تیرماه ۱۴۰۵
📩
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
📨
همچنین می‌توانید آثار خود را از طریق شناسه زیر در تمامی پیام‌رسان‌ها ارسال کنید:
@Badraghe_yar
برای اطلاع از آخرین اخبار و جزئیات سوگواره، کانال رسمی «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/671388" target="_blank">📅 15:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عراقچی به قطر سفر کرد
🔹
وزیر امور خارجه جمهوری اسلامی ایران به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/671387" target="_blank">📅 15:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
امتحانات نهایی رشته‌های تحصیلی پایه دوازدهم در ۴ استان لغو شد  وزارت آموزش و پرورش:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های این وزارتخانه و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/671386" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_uzVww1ZThEHZ-K_39ifdH_JasFpM9u4McT2nEVBq1h0nCK621jpOkIJnGqJwg2LkGfkg2mioiQTbZg7xev7elghqWFV21tIm4QwlX-DiuzCR1SVPFUTZXCNXOqPV_XyQvnSg89u2QZwQXn3WZytErGvwcyimMpYpMi54RrbDrpDPGQQbIjVjdBw3SC5Kf0V5_5YMo6yGSF5OdwXAVf2owO7Fb0uhqfOMD-ZqM46rwPjoQQNTqh3l4FtwkDEFq0lRsmz10YRJRiZNIH2Lh8v8BuTSfK3IW1YnleAPP_S2xMhRp6DGCQIJB0UFtdI5tty_MyPweGeSM3pOFpXYH7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا از ضرب سکه طلای جدید یک دلاری با تصویر ترامپ خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/671385" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز همچنان بسته است
🔹
تنگه هرمز همچنان بسته است و در ۲۴ ساعت گذشته دستکم ۲ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671384" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سازمان امور مالیاتی:
مالیات خروج از کشور
در سال ۱۴۰۵ برای سفرهای خارجی عادی از
۹۰۰ هزار تومان
در نوبت اول آغاز می‌شود و پرداخت آن به‌صورت الکترونیکی از طریق سامانه‌های تعیین‌شده امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671383" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
زمان اعلام قیمت بلیت پروازهای اربعین مشخص شد
🔹
سازمان هواپیمایی اعلام کرد قیمت نهایی بلیت پروازهای اربعین اوایل هفته آینده اعلام خواهد شد.
🔹
درحالی‌که برخی گمانه‌زنی‌ها از تعیین نرخ ۲۳ تا ۲۵ میلیون تومانی برای بلیت رفت‌وبرگشت پروازهای اربعین امسال حکایت دارد، دبیر ستاد مرکزی اربعین تأکید کرد قیمت‌ها هنوز نهایی نشده و جلسات تعیین نرخ همچنان درحال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671382" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در آلمان؛ خسارات گسترده و اختلال در پروازها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/671381" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجاب استایل‌ها دین‌فروشی می‌کنند/ با هزار قلم آرایش و عشوه و ناز ضربه بزرگی به بدنهٔ مذهبی ما می‌زنند!/
تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671380" target="_blank">📅 14:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCinjjNgG1CTbsjah3Akvvo51P5kAe0cbllI-_SWySDPWWOToNguGyKeT7uJwGMz34Bv7bTJBCEw8ScekI7vUQD44y8W2SDKfY7fMgP3LWtO7OIf5QhPq-17sC4fXyOn16sRnQtjGCx4KPuM4H-QTBOewvTKGbqp9afgDmJQoUVCFqs3zlz-WL3GipIdybwlhM3i4G3UCNLfyfsOrqB6yjYASbvKn5ZaFMjUT53PAGLD6lDHBrVk3zalGJkj4bYITw_gqkNx37FBA6md8IVJDFANuHbwlgFHF_rWq5pjof1rz1-nOz5ijobMemPx-U8oQrN8u3ttJ9A3qNhj-yr3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شال مناسب هر رنگ لباس؛ این ترکیب‌ها استایل‌تان را چند برابر جذاب می‌کند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671379" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671377">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای اکسیوس: خوک هار جلسه‌ای در روز سه‌شنبه در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔹
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/671377" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671376">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دامنه
t.me
تلگرام به وضعیت عادی بازگشت/ علت تعلیق و واکنش پاول دورف
🔹
دامنه کوتاه و پرکاربرد تلگرام با آدرس
t.me
که برای هدایت مستقیم کاربران به گروه‌ها و کانال‌های عمومی استفاده می‌شود، پس از یک روز تعلیق و قطع دسترسی در سراسر جهان، بار دیگر به وضعیت عادی بازگشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/671376" target="_blank">📅 14:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0-_4Y7VDfGZaO3aHhHJ3xmA2fww3XxT5mUl9Mch0Umgi_SOV6o1B-pjgOnpIQDeqZV2cA6na5RYSg_c5XdwgGHCCJPGt3En-GkK0pysLV7X7H6Mc8zhD1KUwNxPe7ASYs5plUQHSTriT_ZU4i-tAzFR_rbpFg4Bwdi1lggwInUzi-5kjtkYfJuuXEMP3_TD7depmBn8nCZkFOB8-MLJoenmBhniRnftIgSiNNU_MoT02zzSll-j0_Yp3fELy1XklPXy1RJET1xr9BPU5l5dmZVAD64LfsagWLk5eM5KCB9x14evx0W4JrN7hSdENKa53uD9bzjchsYhGQWCsL0hRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Jgp4NHT6jR7SPlADT90iwXvllwpZxcEdyasRPctbVsE_Rbx-sK2F0tN8yDLScOlHm6ymCyT3lcWRH4VeTA2EjblnCbJHZYmhOroyTMfSNfxMGlNmd80Geq0NmLoZg1mKoztwRNMEsbXmNrO_YwX2ZikH3cWyvTiBwMcy3JWOmpqkSx_XKGnHGTTkJEowOI25SymBnVyEEMjJcs86TrhsQTIFi78FjfrsmYCGmwLp7y9MLLXWejslwNcVTcLQbxLQC3XcU5j0Xb8RnxrasIJotBzSAEmkvP4wwPVQYBA1fMwoYXQlLVJph0NBVNAhR00qLxTJAB6G9_vFzEC1_x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcNMNx1a4pw3T09mCbAtm305DIHOkTkcT7kIm0m6qMYRo8s492vyCNda3be_bxsFBwOzuH2f7UIFbPuyhuLQjGt_7mhgnsqexiE2O6cRPiRZAz6MLvtc4sn6bnf1yc_J9kzjZSgU2xbbHoQmU0ZdRIlu0BPtEqnwpAJu3IJm6tF3-ptACIqJXXJr60zWzxojfSTd3PXuHJ_e_0bvqsLseeLYE7upY_rEGKLw4vdNS_0oBHgh0VNRNx7-qKWcby5N9klej4IVZD7gPBCH31pgr-IVpoRRkqyGGkJ98ncXmV2gbt5HTy5FNyzhMzdK8XZJygrch61KtuJlEtIwhVj-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای جدید از حملات ایران به پایگاه آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671373" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1443322f.mp4?token=pHORpOk4JVg8UgaVVot2Q0QAhCymKGDwGeFeMcv_8y84mb8IWUGyCpwm_9OBQddHP7KmDxcyppI4qm40kXtl2kx8L7qMO_-3zjJQCYAC2ltfwG2Bmcvhivwkw3mjyYpk6Y1uyPMnF5wwJf0cyKeOgvhRsrrTh5CEkqp0qdNiIF2-5XNByp6KR1BGUSc3Ges3peTc1Eyu677gEzN2kfa1GB76LQwV2NiQFC-M8a9Q4Ruk5eVaHtqJq4nUvafFH_TTG7OU7qHHa--pAPyok7O5MwDLkSJBHataJo2gH9cEMpPlJTdMBUcsBPW8PBHBn2KFE5h0j9JCAQZsY2jTESFLgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1443322f.mp4?token=pHORpOk4JVg8UgaVVot2Q0QAhCymKGDwGeFeMcv_8y84mb8IWUGyCpwm_9OBQddHP7KmDxcyppI4qm40kXtl2kx8L7qMO_-3zjJQCYAC2ltfwG2Bmcvhivwkw3mjyYpk6Y1uyPMnF5wwJf0cyKeOgvhRsrrTh5CEkqp0qdNiIF2-5XNByp6KR1BGUSc3Ges3peTc1Eyu677gEzN2kfa1GB76LQwV2NiQFC-M8a9Q4Ruk5eVaHtqJq4nUvafFH_TTG7OU7qHHa--pAPyok7O5MwDLkSJBHataJo2gH9cEMpPlJTdMBUcsBPW8PBHBn2KFE5h0j9JCAQZsY2jTESFLgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر دوربین بسته از جنایتکاری که امروز صبح به دار مجازات آویخته شد
🔹
از لیدری اغتشاگران و فیلمبرداری برای رسانه‌های صهیونی آمریکایی تا  آتش زدن کلانتری شهرستان دهاقان در کوتای ۱۸ و ۱۹ دیماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671372" target="_blank">📅 14:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نیروی زمینی ارتش: در تجاوز‌ دیشب ارتش تروریستی آمریکا به پادگانی در بمپور ایرانشهر ۱۳ تن از کارکنان مجروح شدند و تحت درمان هستند  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671371" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTpeLGTbs5juPPUE5rRF09Z52EQQypDsQoor52koq3SjsfblkiV9dIyZyKjuKnDv9kKsSFMp1X30WKB_MYytVmnwo0jS5SIZzXcrtX6Set-pLSIM5VPX-HacZBoo5Vk1dtZFw2dLPiQ-sRxw5cewh5IuI3DSOeRl0_v0rkHPBHsxFHrOEQF4XCJT7f7xXW3OVV-6NZ0dZiwmYmHPknVphfWv81M3pl8p9wo7CiygHwWOZLGfTkVZguYD02-_9AMOl2YYaZupmVoiDV2b9a0tP9U8XwiIUI2cho_7iRBdTTFA2V11OG8qQEhBOqPpjQs0x9KEpqAjGWWDvlHMqM8p1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسم جنس پارچه‌ها واقعا جالب و زیبا
هستند
🪡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671370" target="_blank">📅 14:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تیزر قسمت دوم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای داوود سلیمانی که به دلیل تصادف  شدید، ۲ ماه در کما به سر برده و جامعه پزشکی بارها از بازگشت ایشان ناامید می‌شوند و روح ایشان در برزخ ازدواج کرده و تشکیل خانواده می‌دهد، ولی بالاخره در روز ولادت امام رضا(ع) از کما خارج و به زندگی دنیایی باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: داوود سلیمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/671369" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IojIUNruKxtjHCFwc1KDbM226aZGyc-5iOCR3uYeVv_uJsjaODhxvDZPAk3d_8uI55OeQxwly8Qp_4AnZH6ad6fNEuW5pAZXSScZ_uyz8Mmx_PZPx3h9YdvWgIi_nrvIwk77hZHzTQOPtEIb4PV8JqeGw1N11MSMcnJJOEkVXqVkR_M479N3QHfvqnxuD1g_o2Ejxk6E-PTPZ5mfQn3NCq_9aeG7vPL_TjAip-BjxVZCdGFXp7fiq_Z930hWHAyAmlf3pPeeCM9qzzpEm1EFFm-Yl6jtpzoZJ6FJ18wBQv7o43sA8_aL7Ncpd45tgDVkT7MOF4wEyREyRoTV5wG1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترامپ برای بازگشایی تنگه هرمز گزینه‌ای جز بازگشت به تفاهم‌نامه ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671368" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
امتحانات نهایی رشته‌های تحصیلی پایه دوازدهم در ۴ استان لغو شد
وزارت آموزش و پرورش:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های این وزارتخانه و با توجه به شرایط خاص کشور در استان‌های
هرمزگان
،
بوشهر
،
خوزستان
و
سیستان و بلوچستان
، امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/671366" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c58836f04.mp4?token=nLD0Pq505l2T8VUFC9BYN1f8Xrm51ANOdPrGNQw3mDIeTTjDmgfcnI4gYrWVsUDOZvPDiYePYzDxxNVIOZCCQWta6KixPE_OPdC7UPEXufETVHjHDUlLLFoPxvcemLtVShEfbJkU2i5BYFRls6Yeai17nBY0PbAQtm4IVK5W6jE02IetlEefbB8JABHSHTvWpz7gXovsrg3oGdw-HxZBgpo2_eymBnwtKX6-GnqmevaPURAFCb89NXt6llwWQnFzqvexbE-oBPE6_Iycwo73_av7XiewbQ-InmSxlUrVWIYA1NLHNQIp9a0v6ZyrV-25gBhcl7tSy_SoYc5rKXGinA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c58836f04.mp4?token=nLD0Pq505l2T8VUFC9BYN1f8Xrm51ANOdPrGNQw3mDIeTTjDmgfcnI4gYrWVsUDOZvPDiYePYzDxxNVIOZCCQWta6KixPE_OPdC7UPEXufETVHjHDUlLLFoPxvcemLtVShEfbJkU2i5BYFRls6Yeai17nBY0PbAQtm4IVK5W6jE02IetlEefbB8JABHSHTvWpz7gXovsrg3oGdw-HxZBgpo2_eymBnwtKX6-GnqmevaPURAFCb89NXt6llwWQnFzqvexbE-oBPE6_Iycwo73_av7XiewbQ-InmSxlUrVWIYA1NLHNQIp9a0v6ZyrV-25gBhcl7tSy_SoYc5rKXGinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش خوک زرد به پرسش درباره کشتار دانش‌آموزان میناب
🔹
مجری: آیا متعهد به انتشار یافته‌ها خواهید شد؟
🔹
ترامپ: فکر نمی‌کنم کسی بتواند بگوید آنجا چه اتفاقی افتاده است. در حالی که چنین اتفاقاتی در جنگ رخ می‌دهد، موشک‌ها در همه جا پرواز می‌کردند. و نمی‌دانم چطور کسی می‌تواند بگوید که ما آن را شلیک کردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671365" target="_blank">📅 13:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692f9b40d5.mp4?token=VHJd-bviYCTVaW8x_l1JO45RkoYY6dIfek6pPdDhU-Z7OFfqAM2MmXmh7y7387MVM1c6VUJ7_BfCn0tl_nn7tq9fZlX9VCGJdr9doLSou_5vsgBJ60zgRNFxUhf_0VOTj6EboD2Wa4PXrib8FekEk-Y0a_x4gF_FZfDQdnCLAGELDBeDX7OtQw6ZIjF2eFSa_lv_NqCCFaEMZKXw-xT1cfdpvvShiBlAmJlJOCT32vIvDQg-EiJQsQemunj3gQsOAwMUejpVK_nH_sNWz4-i4M2RW-Od-avyjHQKPwapwrWtCbkBv3mD_SJGZ2xKu8htVubsxhQUKjdf5QlRtDLk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692f9b40d5.mp4?token=VHJd-bviYCTVaW8x_l1JO45RkoYY6dIfek6pPdDhU-Z7OFfqAM2MmXmh7y7387MVM1c6VUJ7_BfCn0tl_nn7tq9fZlX9VCGJdr9doLSou_5vsgBJ60zgRNFxUhf_0VOTj6EboD2Wa4PXrib8FekEk-Y0a_x4gF_FZfDQdnCLAGELDBeDX7OtQw6ZIjF2eFSa_lv_NqCCFaEMZKXw-xT1cfdpvvShiBlAmJlJOCT32vIvDQg-EiJQsQemunj3gQsOAwMUejpVK_nH_sNWz4-i4M2RW-Od-avyjHQKPwapwrWtCbkBv3mD_SJGZ2xKu8htVubsxhQUKjdf5QlRtDLk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش اینستاگرامی محسن چاوشی به جنایت وحشیانه آمریکا در جنوب ایران
محسن چاوشی با انتشار این ویدئو نوشت:
🔹
جنوب خون من است که می‌ریزد. به یاد جای خالی مردانی که دیگر  باز نمی‌گردند⁩.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/671363" target="_blank">📅 13:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
منبع آگاه وزارت اقتصاد: اخبار منتشرشده درباره تغییرات در شبکه بانکی صحت ندارد و هیچ تصمیمی در این زمینه اتخاذ نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671362" target="_blank">📅 13:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آیت الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
🔹
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671359" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خونخواهی، طرح حاکمیت تنگه هرمز و اصلاح برنامه هفتم، اولویت مجلس است
عباس گودرزی، سخنگوی هیأت رئیسه مجلس:
🔹
اولویت مجلس بعد از رسیدگی به خونخواهی رهبری شهید، طرح حاکمیت ایران بر تنگه هرمز و اصلاح برنامه هفتم است.
🔹
برخی از اصلاحات در قانون بودجه ۱۴۰۵، برخی از طرح‌ها و لوایحی که نیمه‌تمام ماند یا توسط همکاران امضا جمع‌آوری شد، در نوبت اعلام وصول و یا بررسی در صحن مجلس هستند.
🔹
تعداد قابل توجهی طرح توسط همکاران در ارتباط با مسائل معیشتی، اقتصادی، کارگری، بیمه‌ای، رانندگان و مهریه، در دستور کار است که در اولین فرصت باید به آن‌ها رسیدگی شود./ خبرفردا
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671358" target="_blank">📅 13:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/691ec6572b.mp4?token=Ge49x7haPQPtCI80CapBd-spLM0PWZAobNdVWrEmFKGRy5XY8p-ctXauLeAbv9ahOx4SgmDlqWyQkJePbj347RTgK0mSPH8PhVtuS2GeAH3j1i6oCBca0IUqc2-_RQ4_NhNxiHrBZgG8r4ohymFij3uv9rDxxH3c2-GNwn1dZsGCU9-arSDIYPaYzQf3OUZtKG67zzUkSA6bdjjrGoodrjdLWkFoiR0nN_QJ1QBkdFFq6XKaWnl_F_S-BQLEag8_zoCn3TLA_zkh7eyizuni-m45qMc6y3Byd7SpZ55IvkCCV4b_mh4HLUhYtIakwE9b-6rr7qOUMkJmVWMn9eDRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/691ec6572b.mp4?token=Ge49x7haPQPtCI80CapBd-spLM0PWZAobNdVWrEmFKGRy5XY8p-ctXauLeAbv9ahOx4SgmDlqWyQkJePbj347RTgK0mSPH8PhVtuS2GeAH3j1i6oCBca0IUqc2-_RQ4_NhNxiHrBZgG8r4ohymFij3uv9rDxxH3c2-GNwn1dZsGCU9-arSDIYPaYzQf3OUZtKG67zzUkSA6bdjjrGoodrjdLWkFoiR0nN_QJ1QBkdFFq6XKaWnl_F_S-BQLEag8_zoCn3TLA_zkh7eyizuni-m45qMc6y3Byd7SpZ55IvkCCV4b_mh4HLUhYtIakwE9b-6rr7qOUMkJmVWMn9eDRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظه شلیک موشک های خیبرشکن، ذوالفقار و فاتح ۱۱۰ در موج‌های سوم تا هفتم عملیات نصر۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/671357" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5kWOVQRutFSfWY07DxKtET-crW0zr912mpCHin5Vrf1l2rVYVB_K3mpnyqZNM47H2Pz6iUnh13gGn3LRa7MnwZyVCZl8HKhI1U_Kl6_zHAB_5cQ6uj47rKu994S-va0hsz3EvksZgfvDadfFDMbbRuZOuUN2Qz41hcJYqxcn-YC0PSXTunXPUe6Noijr-jdSYe0nW8HffXUuLEqE4Lwdb0VVSkIL-wIjzxgNbxnNuSWOnlcn46ohP9RPmdlqZJYInrBmFvks5Q0jSG_0uYENWn1FK4WUrCQUuG-l1WiWoCVPS4MnoMayseV9U196XTH1mAFig9DjSXSkgZ9iRhNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHcykeZZ4tUFItBuKxzCqFd8sLarNUz1VnJ2RZ1qKtUtChg1Zz1UDOHJtdfybKpQC8Je2LIffjPZxoPfhXCasAdi5wES3T1gONUtzDx0nqLFrqB6CvLBhQZJVpekF2oew_UaATYvOYG7a6fv20nbO3dOSm61KfXKXQEJG2_r8LeiAthit-cM4H7aADRu5eecmRll_qTwRF5CUmJhfGmCfimvQCgzA9v4l_YFUjDwSqZi-s7ZCu2MBuWYyCRtevsg6wcF89ETtLJeat88z36bBbwU-TVn1h3gTw25zmgWLhJuwx5B2l30B-2av-piliHq10OUr8EZv-Aap9R5vwmjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8p6FbUHwufQ_Ao5VolVSB2eI5_FpyZTJmM3hmYgCCvIX-f-ENUHgTSG3cfmMBGkwSZxUPbBhH7DGmv1duVdI6iaCwbC7eXbPrZ9bKZ7wnbV4cIcPBcTdiriCLQkNnzEs_Bv3eAhNUhdTJUBEX6qlvbumLA9CamzaKxye7lcQfEq4XrFw8I_wNiNXziH89aULrUhJOlf6UPG2cONexIsMFRYoAXZmclTYRD3bq9-d_dKwz-HtoUHgmx5N2a-0e14nAfawp5HvtOqLqgaemoY0CfduN5BOGcVjC2TVUNtx6-X4S703MlCGt5enKgVItmedHI4X_EuxX0t2eOz5TbAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJaORypUdaX-x_1ivETu880TFb0p5GAo-6O7f_m40zuERkDSX84ZLGgYpgCA_mmCltDzL-_HS3dMMhrOQpzo0w5iuv1Hdv549vXwZK6o_isO6WJlgexmoY9OM25cH8IXivk6ttWE7p_0tb02QjhmEteUMWiv2PTpgN2lw_gDqtqNq4ORhzdBuRLfBWormkxiZVsz7eSL1EZYym1Et1z8KxFiweIsxNR4yAE0RIiQcI76bavXppU-xZa_oMuF7t6_DomzP6KQlcY72fVQCbqUE-rpuhs0HS1KNmZcSIXplstUJMSAUEUFXMzCRZPhRSXi_boN_0LmBd14AgczoZ1edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le1_8Uig97nqZgzNH8Ew132Zh9OLqv--h9of_e-bSPnrp99nDu3HpNvgq7U9er6yLdS0t4nd4HbTJua7ET22SCbxIl2UcAuggEoHrT1fmTkr-wA9ryoHgDqHlZYTvpUlw_KAJCqMhH70wyj1S20rmgLqD1gfiCi37ZGp2wyL1x52WQMSYriIodpkbFn0tCNHUwBw4807vpROUL1wrn3azUFxcRZquFJWdx7QnUYYaXs8bJZJaikQtfX5Sc9IgioeRgl8It1lQTn2K5Pl7MwEwh-OdV9u9c3lMy5uycaV7zJotfc-rLYN6z3mj29oae38K5SOemq4t6KHky81HwchMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_xa7q5TYzpufi22LIGurTtXQiP2EjPw6nmDSZbVer3VbMbyEpthDYpbYZO6Df3rGaV1ZwXt07gTblD8ojjx90sGrHJu7CDKfOzchonS-JQA9vT0aw998UdHr50AJ_ywicq4g5XXGrhf0FKGkEa826hzm4IqqC9v1rfIni4ucUmHo6unFNfx2oc-3GHnZ04VI2vpKinbPH_ysg6pxMuOzv6UCvQ2aSbW4cW8AZwwlxhg9ts8qaIA-whIb-UyBhT-ZtUMsi6naCWe1wcXlyzUeSVpBJ2uka4-YXkr-WjoJ6zKGg4DmlGMqSaDciCp7OjhoWSOjxgSI0aiCjfqDmxV7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شش دستور قهوه سرد محبوب که حتمأ باید امتحان کنید
😋
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671351" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laagSd3piz7QCD3hlwFVnK5CBeKY2ainNxKT6VMSfNZlC8G0KgwXIN7VRkjaHW86vxAh_9vEIdJI6EfQcYrFnXw56Pno0553-h6wGPTPNW3NqsV1aebrZtiYQbsjCX9YhU6WUEyqnreslPtYIPM_U2_ASM6MTYf7TpGN8gx7wdFPa9ntQvFM5wKRtpCP_B7rqA0GNjTB-JxrXQZzFYfupe9Nv0RlzB9oHr2sc4Fy8J-Jlmv2CW9BRNTbMfWj-izB2jg_1JhYsf6maHu6FnDWGqQUEItnU7i5gar65CEFKmZk40h83RnTU-rBXmj4lUn4XyM39487e6d3YdNB4b19Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ تیر ۱۴۰۵؛ ساعت ۱۲:۳۵
🔹
امروز بازار ارز، طلا و سکه نوسان‌های متفاوتی را تجربه کرد؛ ارز کاهش یافت اما طلا و سکه تحت تأثیر تشدید تنش‌های سیاسی و نظامی ایران و آمریکا و افزایش تقاضا برای دارایی‌های امن، صعودی شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671350" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f43adc06f.mp4?token=t7RzNq6SQ2o5qxqg9akzs0OhN4PYI4YNGdcVJYVXJIQV9pO47E6yXNt3d0xlrK8iKD1-FH3jCMS3TiY0aNkI4mwAFMp61E6QU-TWEp71xznIJ3muwAVnVJB1w3kzojX9UFolmbJZT8OzZ5vd5AIpsJ35B_B_aMCx1PmMZc2IrQXuC2EjTgRBvrw-E3vdKW3p_N0C2Fl65tLM376ibpo06bcUjgLRKP59t4H1dlQpgd80R2icGGmIWUpsnW-fBlaEo2rVXGnP9O8A1VVUAds3Dq3kf625i1h4vx4XPVVvzCLysHZHbfpX0hPF2UIwX-rUlRtjMxFWcd-6B3HiWSNBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f43adc06f.mp4?token=t7RzNq6SQ2o5qxqg9akzs0OhN4PYI4YNGdcVJYVXJIQV9pO47E6yXNt3d0xlrK8iKD1-FH3jCMS3TiY0aNkI4mwAFMp61E6QU-TWEp71xznIJ3muwAVnVJB1w3kzojX9UFolmbJZT8OzZ5vd5AIpsJ35B_B_aMCx1PmMZc2IrQXuC2EjTgRBvrw-E3vdKW3p_N0C2Fl65tLM376ibpo06bcUjgLRKP59t4H1dlQpgd80R2icGGmIWUpsnW-fBlaEo2rVXGnP9O8A1VVUAds3Dq3kf625i1h4vx4XPVVvzCLysHZHbfpX0hPF2UIwX-rUlRtjMxFWcd-6B3HiWSNBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌های گسترده، آسمان شرق کانادا را نارنجی‌ کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/671348" target="_blank">📅 12:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671346">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک کارشناس انرژی: بهانه جنگ برای قطعی برق به لحاظ علمی پذیرفتنی نیست و این مشکل حداقل از ۱۰ سال پیش قابل پیش‌بینی بود
هاشم اورعی، کارشناس انرژی در
#گفتگو
با خبرفوری:
🔹
با وجود وعده‌های سال گذشته وزارت نیرو مبنی بر عدم قطع برق صنایع، از دیروز بار دیگر خاموشی دو روز در هفته برای صنایع مولد اعمال شده است.
🔹
استیضاح وزیر نیرو به دلیل رایزنی با نمایندگان و پذیرش خواسته‌های آنان چه حق و چه ناحق برای پس گرفتن امضاها، به نتیجه نرسید و به جای تمرکز بر حل بحران برق، مسائل سیاسی در اولویت قرار گرفت.
🔹
همچنین نسبت دادن خاموشی‌ها به جنگ از نظر کارشناسی قابل قبول نیست، زیرا بحران برق سال‌هاست قابل پیش‌بینی بوده و ادعای کاهش ۴۲۰۰ مگاواتی تولید نیز با توجه به کاهش همزمان مصرف صنایع آسیب‌دیده، توجیه‌کننده تداوم کمبود برق نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671346" target="_blank">📅 12:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bdab62a3e.mp4?token=OGI3zY0QM1C9ZZuSa6zyeXC88SDT4i5aCvNyj9cPiIeBRN84r30IsovTI96PlWHOBMA14fW0B-jZnZlCeSkrc_gtMitZmwzEuh8UgZR7jdDSaRYlBrWsoKAGcHk4kHFOD1-fi6E2IndfSHZZ9pUVqwJcMWFKegZNuVNxEYGTGdgbsrCrz11yB5eeZ__foCqvaOjzuYVb1lutkMepW8Z4VQ9V0mnfpOs80SiQanZrrv3DmGi0aNMUepbEiB5-yvD3QwxS0Qqa0-OXJaTuIJ-H_t8Cgi_utNGr-ePbBNrNu3_0srtLedKLTgkf9qxaEOp5JpxhRFH8EpPWkNqgmUnYvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bdab62a3e.mp4?token=OGI3zY0QM1C9ZZuSa6zyeXC88SDT4i5aCvNyj9cPiIeBRN84r30IsovTI96PlWHOBMA14fW0B-jZnZlCeSkrc_gtMitZmwzEuh8UgZR7jdDSaRYlBrWsoKAGcHk4kHFOD1-fi6E2IndfSHZZ9pUVqwJcMWFKegZNuVNxEYGTGdgbsrCrz11yB5eeZ__foCqvaOjzuYVb1lutkMepW8Z4VQ9V0mnfpOs80SiQanZrrv3DmGi0aNMUepbEiB5-yvD3QwxS0Qqa0-OXJaTuIJ-H_t8Cgi_utNGr-ePbBNrNu3_0srtLedKLTgkf9qxaEOp5JpxhRFH8EpPWkNqgmUnYvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از خسارات وارده بر اثر حملات ایران در روزهای اخیر به پایگاه‌های ارتش آمریکا در منطقه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/671344" target="_blank">📅 12:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd6c5c54.mp4?token=hrZdj-fX8ighKlOCYddZRWQ80dWJI5RAagg62hBU0NgjIvd0movtmpVOU7oC7dAigdOzFHHJ1FBlumrG98TKVlYKYVNKefulVXPW8a-iD3nGeWTam_UlhqpH3Lz6gBriN2eY6I2mytIw6KWhuxSAFnXgJNYrjLmFRYSbaGlj0AmzDMzNhVP7G3ZGN7z3vTGtuSB7xlYKIzQfWahN2w7oMCh6vQbcL0yVCO1UGRzzoXSVcYJ51AjitdDt6CT_zOgvCw7lWyYFBPCnKGDhHQYT8qH-uyO2gLsIBN88L-CI5nYW2QXUcpMqrQNfhu1StUnVJgYdwJerGjvco7N4k8UDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd6c5c54.mp4?token=hrZdj-fX8ighKlOCYddZRWQ80dWJI5RAagg62hBU0NgjIvd0movtmpVOU7oC7dAigdOzFHHJ1FBlumrG98TKVlYKYVNKefulVXPW8a-iD3nGeWTam_UlhqpH3Lz6gBriN2eY6I2mytIw6KWhuxSAFnXgJNYrjLmFRYSbaGlj0AmzDMzNhVP7G3ZGN7z3vTGtuSB7xlYKIzQfWahN2w7oMCh6vQbcL0yVCO1UGRzzoXSVcYJ51AjitdDt6CT_zOgvCw7lWyYFBPCnKGDhHQYT8qH-uyO2gLsIBN88L-CI5nYW2QXUcpMqrQNfhu1StUnVJgYdwJerGjvco7N4k8UDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تاریخ بنویسید؛ جنوب فقط یک جغرافیا نیست، جنوب نام صبوری این سرزمین است که بی هیاهو سالهاست ایستاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/671341" target="_blank">📅 12:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شهادت ۷ نفر از کارکنان پایور و وظیفه نیروی زمینی ارتش در بمپور
🔹
ارتش: پاسخ تجاوز ارتش تروریستی آمریکا به ایرانشهر را خواهیم داد.   #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/671340" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مسدودسازی ۱۳۰ میلیون دلار دارایی رمزارزی ایران توسط آمریکا
🔹
وزارت خزانه‌داری آمریکا ۱۳۰ میلیون دلار تتر متعلق به بانک مرکزی ایران را مسدود کرد؛ مجموع دارایی‌های مسدودشده منتسب به ایران توسط شرکت تتر از مارس ۲۰۲۵ به یک میلیارد دلار رسیده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671338" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671337" target="_blank">📅 12:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwwcxXn852-ah8fPGSFBgLwbq04f731lci9SD-YLI78R39QUm7qGmpScc4TpU0TC91iONb9qDa9ULcBW8SC7dLK8rnQHIOsv3K6coau78H2lsK6v5olNmGGJlLxtXeLGdgHgzporhcYi5UjowV6raaGxtaTLabw4Z8re9Q79x1P47v1mwFgEsglP9TTbUaIWEj87hfeRkCLKEYBOUu22C9oW3aEGU8RAcQ6ELM0hkn4R_0Jmfe597MZ0f-3Ybmusa5Yhl-b8mrVZVUXc9jCF52nA1DHi37s-LpyemtfBbUsQA1CkAqHnxO32C1lFOqMLj6PbIN4Zk-0F1yt6p2aPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsmuT0hVFMzCcd53plhuZkcDVEbWb8wGosgDXpADI7OViDg65lX6JHJOF4j29HhwmhCEnZzDAV1CRLY2sdUairJpluFZYGhncR68JPFQzQ65RCGfPDppba__Sy6tp87Lg_7eevRxS4nw4qfkLMrJTmUBrZzcH44eo3Vfar3NCVQKXtxf8Pz_cWKGzWJ7N9AuKTTYAZsqMlmvtH6T58PHhWcYSWxE5uRSfVAk_tfACGHBytdiPT5xw3WkH4tRCUriq2M06RVaLEmlX0646seXa5elX-xjX-D9nVyiTTYmPPdf4l3dYtVrj1kLHmAesWlqIdhXEfLO9Dc8ET6KI74wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcPhUonx0Fc0xBBtYI-7avZsAFD_UAw8Hl186RFMx0VZgIj5MLdb-OioATvqt0DONPmndA6ftMj2CDAdHAVB1sk6asT-fuVJqU1hSRTKkBRxORunfts9a25KIGtkei3Iahhqe1x6XdS_PG51EZTc35oczjEtO5rul8WNdH9O08UrSye9s8igwOwaYoFJKfkEX2u4x7CNu7hunsUV2F8yVWwff-km2X-Y7Io0M8SUSL2C0Qqo9FGYlPCdxJeUk_V7tFZOGujJOoRx1-JwqmCs-skkrSCaJ9Hds-4ZHhdIsOsr6W5iloJhquHh4SiozI9mUfZoqCkXght8NbBuUkEJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCYw3OTwTwdvnuUHN48zuNbmb5DAwJpvCEj3sjYmRmtWM0UzYzhQ3_a2LubJL3TeYq7cgF0ouueQlKJT3NqxsuWnPoHjbettBhONQzfAtP6nqdT2m5skj_tKUvka_z1-YRR9tCRXG4gG14-r9k8D1E3yspD01hsXHJj2zsnhUgp7h7_PXFuAMKhKBIY48vkSutruhGcQEtxbGvdFtKQMEiWvjbi-Cm_6i15PWxe6Ed20XjAowPAVBIBhuFVhZ9hfAbC9hzUU4-fwxB7zlR4Cnb3p2b-uwkHIcfp5LOm_oso_cLjTphJfB5LIJXr1aMzcOcUVSxdUKajcpVHqe2HH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRILQbGvPmzKilgnBub7chRLq7dh_CutptQb7dbsFR6RBmneX_gEynMf6pwXpJ1x8wd4K86z4-Mp_T7CSG9elZPnb4qbzYhyu9-E3rDz7OAsX3KzbbE9nquptA9jgiW0XWy3cnlNf17gADVIC4e1tRVNyWGIDlj6-230nelFRcAJEBuhNPxrWqZooGMbjiI43P5Yl2YIZDPsiCoooxHcTqqPxlrY1W364QiDW_Gvksz4-lvH97PRbeoO2XngtL4IjjgpWSEV8SxhL0RQKmNgLpHPBYmc0mawZME_TWENrZmZLc70gJpf2uiV7UcabSEmgh0UCVQTHzCx2y44lrUYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRU0bsGloPqpWw2MU_AgQyTCU9PY5cmM4Kl7NV4kgom0XahbLyQbbCKl5Hav0RgqPC8Flr51Iv2LwwrYLOsdFoKT2H1A2lvK908uB1Wnsb-qqKLFkYzjDQLb1BmYfPWm4EiLG2hLOu_BvMkA9Um6XZFeCxosPTcwcvsBl3Xs2vsyizB1aUmI5k1TuM8ihZY6US1Nac1frMGOr2PKyWLWGK3i2o0uJKjG2JLY7uoM3Bu_lFS-WIV5Np6-BZLSYQUuoVhPCgdvCGeP3e2TmbAJL8mqn7m3BshEQJESELXiCaSds2hzNYhEDXQO7o_jlXNGyfA5vrgLHB6glhsdzUqL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-X0dF2UigedfME9Bue5dYu4eJaAWSf6MTtzuskH-IhQL-DgccbgZyr9fMkhdKEc-qqrU5Yp3yMgsI2YUjuWQAH7fCJlTTjVH7GbOKwXQEsLxYYJdtR4HjMvlSZTDG4HJQw8Zs4EaggZJ0XRa1h09QkPdzhbiqaGPKZrz75BtNxcW4BM1jiU5hBrg4pt_Ixyg_gxGo-oyuJ2g-4LFVI4ozkss0w6azTJO1GMdxpwsF4Mjbu-JBvGIo524KLF9DX8IxgThHv11gEogTnA3CKDgO5NMaetFovJ78as8J9chZkMB4A92NwweOhUJS-Es6jVFHSvQevx2AYxaP5XRsIfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4fRYdBuh15bLKtl1EpXK4k-H-Vxmy9JLjAl4ILB3riFlIYD74mM-4a_Idf_vc-y-bfw3yELiFl2yKchUYqyFvSP9LOBDZMU3gRcOFM6YO24kt66R8L8YaQ5hnpUEkxVA2kz1FtKv0WGNiE3Nos8cDeymQLaDp2E-aN_b5rnAXZewA8AFrkzN58508Tu0_nbzFB2aXJZO0QJisDphnZl-LYUBHjYUqLNwbYPpgmyu6s-Yy9cve8UXA1Vm2M7GhvEVqZqE38a2gsOowNmtcSsscVOqLH-fArceyZDsfilLT0bajqkN2E2bTSHgtW7s08-WFypN7sIJoGybmEkHe6Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGIfU6VhkP-vAkIwcpvBLUb5FdSd8bFHCQi-YbDXxwDiwfK5O_vZUiRZxyb4i2zmOiF-mU-q_l8s8FKuNA4bhBuPW5lkNYsTTyXmj4o6B3wjIR6HQ1h_gwQVW1T18S39iO-3ymkqirI_3IXnkpWQxrZrM2xh3EFE_LOLxPyDGNh2r1BESwiN_mOxi5g8ZEpCfbjEr1V8Dm7jmjdbOp_rtSMNvHS24DH3pAZlLBbyOdJqBOcbwAn-mBsCrdUPiA8iRdjA0bQtxyiEY78scpIrPJCPn1k83RawNYsI7pkUm9W75MnHpGYRpnDFGa1ZAEi4BBuFmdJU-oIfwsK5suVL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBN6HEkgGjMRDZe-xsHDqh5eJSpoPtGK4RufVrNg3RoR0qoRBrkZmQaCs6sW1WLnRK9f2u7W62zrJFLbWlh5d9DyCPN1DDxCnl0VSL9yimswe9bhUrBz_MDEcUThvpvhxCImEqLn3teUKPZWIPWntXHeVK4xxAuFkFKUmc8qGqH72_m0ld6vUHy8vETj2RUPKD5MWusK7UUR11MIh8h3jcIRIq50uVj8CVKXjAilIF22U42rk4rrqHtCXZ6dpeXTER6M27QizUBShxWAPRAlx2Uw5W6aWM4J1bETAfcaBLU2OMsIMo6raDhFZfQJj9SPVXxLrTsmkv15CFoZ3cNVbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/671327" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایش بی‌نقص اسپانیا، پایان رؤیای فرانسه؛ فینال منتظر آخرین مهمان است
▪️
قسمت چهاردهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/671325" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671322">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشانه‌های تروما‌های حل نشده چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671322" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muWuwceaRlHwAM_qrt_Oc9OoLvqhiWLmJKxuOHMmJ-vajLGLJ3RiNtbMFALhnDhBkUVBX9UD4ue7pBrLTBJGXh5BKXa5mdfzcNN1n-ahR49Sy8raFCO2Lts5NutPdp_evuMFYz3jcIgs2Jze4E1a7wWm7bi7Y5iChOXaO9jheMuLCs5WsDrMj7hXP_a1_41YG5w5e7St2wTa48AnJwqMUdmWw3qbdximOqNF7W-vQ1cKHtCaaZbDAswureMPm2uW3mqTEwFRzvas6Sq1wonJWUBNz_cwXo5U-vpdwVGcYEghB0LelPkmjbQL6-JhLGLRQxXjxWJjizOVGwRZ9J7guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی تدریجی با پول نقد
🔸
بیش از ۹۸ درصد از تعداد تراکنش‌های شبکه پرداخت در خرداد ۱۴۰۵ به خرید کالا و خدمات اختصاص داشته است.
🔸
حدود ۹۰.۳ درصد از ارزش این تراکنش‌ها نیز مربوط به خرید کالا و خدمات بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671321" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله با انگیزه نفرت مذهبی در آمریکا: کارمند مسلمان در یوتا هدف ۱۵ ضربه چاقو قرار گرفت
پلیس ایالت یوتا:
🔹
فردی ۴۸ ساله در مرکز خریدی در سالت‌لیک‌سیتی، یک کارمند مسلمان را با انگیزه مذهبی و با ۱۵ ضربه چاقو به شدت مجروح کرد.
🔹
قربانی که تحت عمل جراحی قرار گرفته، در وضعیت پایدار است و ضارب توسط حاضران در محل دستگیر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/671320" target="_blank">📅 12:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNLZc0NbOeYi9CvokCoDzgfoZsfQ-iauWqp4YEdXX1b-p2mXOmUUGbd0lsTXME3SQYOEp2MGOYcs6MRctC8Ksw7KliKLhDa6KSYEslq9YkjRzyyYXZsn-0OQ5KMeWgWPZ3hnbNnmHx8Awehr3so6bBGYP7b9YmxRoG74Mqs71uHplK-S6Kz-4Hy6U1_vB2n2wSQNiZQ5lk2WUdb7jf9GYRxQjjr41W5bHvM1C0TZfDJbY8glG1Rp2qPEALk_bkuDp3zOmhIQ_xkNkadmDi-TeAwR4e_0IJPv8l3O87vKZglp650eW9pkD8MLa8XvZYv0A4vjE4yCm4VpVspFMUK-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrV6bxAMqVOjn1IBYxMoCLFzbdv84ie8o7f8F1zt_s5kG-bj0vxE3S4YPY2esGZ3Z2gWetvyRZcsx7oEE-Tux46SGFBlU1Caxtg3qRBaEUNIihwnBYfzFqcvvNfVSfgEUrL7JgDXiXUpY-3JprMo4L0-SPmSAPHvzeuLlEhMnW8GxnAJvcqYuhhf5kCIITaMwnZWodYFBby5KljpfM19NuVD_AcRwWQB28MbQqGOrI0LWE5WoD6wDpeE3vnC_r-DQibFPoaijPwmCGczHAUWTEzFXnFk1rulV-ajh1rmynDn7VSvV6H3GQ5M2ANC0Slq7If6ZR8K7HePw7cif74snQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrkTNdm70ZYmAdsqm9QQFhYQ3_5hED1QmPF0h4L2QaHqvaFHuweNdcF5bzm8zPapRr7uVMerGn5TU0hUbZxqo1OVx8oPNH_KOmiuOO_rd5l9EaG8FG7hmN9u9KwB7p2ieA9lTM13zJH4qH87KhmAuejbc2iIVd7u0dvLXwjE0c33DOfA28gfvohOkGKRQaBI8eL8yzUqyxsZAEsjXttfq5G5ylKd8Htsv9uu0nKS3TuDiLJeipMStyeZIW7pdx6q577ZZn-tW-hwHRTb3NDBV0abPiMlR_1IuDVAhDOJzyJ0FsVON_5fooYbARzA0wmAVr0nd0QF7YNNtPJpEkM34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP6sX_U_vJFm1_dxJDv965v2Ekd3FgoIr-hQqImaiME2Ga-Xjf95_FmNExdOyxJeUZkTpTP0lQbTfSjwYl7WatUNM_7H0vzHthHs3AhjrRINwagIXCJGCvXSlnIFMSUQaBI4JArEfp8R_0b9vaRCTTUu2Dct8Fn53MCaJg7-qktI5oJLcpP-6b2gI0g9b9SM5mJLJaXKlHx89D9s91ldVkn2E-vjcwuUNHk61wNAp4LHccWdP2nf0Np1cjmzp4H6FvfumrgWup2nOi-hW3W4uTV6IxrukSM-bkhonFljnD_QmtEKwkttLV05c3OB9H17_EBwqUuxKK3TnTYjIuhjyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شکوه خیره‌کننده جنگل‌های هیرکانی
🔹
مجتبی صابری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/671316" target="_blank">📅 11:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله بوفالو در پارک یلوستون به پدربزرگ و نوه‌ای که قصد عکاسی داشتند، آن‌ها را با جراحات شدید راهی بیمارستان کرد
🦬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/671313" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWNtybIXePrl1byoiIRPbBkVQqSumlD_iV5cPzxUss7bKhZouiJ1dVCydiiZt8AvP97BU0tSBG84FxxpC5WT8gSH2fiP9j2RcFiCRtAVWU08SFuIApEtC_vzPElKLykHNzhg_pebCLc6hTjfPUT5nkBAwGOCXmK49ih_1dbQse_Uzwnpg3JwFRH5hIRi9iqmZwBrgel4KfS3Hnq06aY9Ly83PexqIIcNwojyImWKjjqLOtmdm4SHGCEYNTuRnt6JO75YBKYu1-BWq_phqKWLOiezsH9F_aj79Rc9V8cJleL5XtiR9uE0meXRXyzVl3YVCfrLwWMQwo0PHTcl9HykPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهندس نظامی شرکت صهیونیستی رافائل بر اثر حملات ایران به هلاکت رسید
🔹
رسانه‌های صهیونیستی اذعان کردند که مایکل کاتز، مهندس نظامی شرکت تسلیحاتی صهیونیستی رافائل، بر اثر «جراحت‌های واردشده در حملات موشکی ایران به حیفا» در عملیات وعدهٔ صادق ۴ به هلاکت رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671312" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آهوهای زیبا جزیره خارک که از ترس صداهای انفجار به خیابان‌ها و کنار مردم آمده‌اند
🥺
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671310" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بندر فجیره خاموش شد/ ۶ میلیون بشکه نفت از بازار حذف می‌شود
موسسه HFI:
🔹
بندر فجیره امارات که مهم‌ترین مرکز جابه‌جایی نفتکش‌ها در منطقه بود، پس از حمله موشکی سپاه به دو نفتکش(VLCC) از چرخه فعالیت خارج شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/671309" target="_blank">📅 11:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFDWZsRmYdzGKe1CTEbkIkKVuKl5awJFK7BRl3oN9k75GJvp9WLBqA0LhT1iITDOxTnZxdUxHrp54HL1ZUncNJuwuvN4cZQH-9oZR_05N1-nKrezvKVIhKzQfpfFOuNgluJtiVYrCqWyhXYbeGk0biEpEk65gpCap2Ma_vM1Hx7uk7fARhIUxprP_-L6URiPIudOCyLmr8DYH4uUcOpGYYGifF2QPsR59h25xdOvYcjio8tQZgqo-GS8Q3LRvmTt4qqKITil9vRjfkMYWLmUFzV74Xpdgw_8ITw3xcreW2HMnG_6HnL4i8rhax2oFIlkLceyHCcZUHqk5tKe5ceoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس فاش کرد؛ ترامپ در اتاق وضعیت برای حمله گسترده‌تر به ایران چه تصمیمی گرفت؟
🔹
همزمان با ورود جنگ ایران و آمریکا به مرحله‌ای تازه، دونالد ترامپ با برگزاری نشستی محرمانه در اتاق وضعیت کاخ سفید، سناریوی گسترش عملیات نظامی علیه ایران را با عالی‌ترین مقام‌های امنیتی و نظامی دولت خود بررسی کرد.
گزارش آکسیوس درباره تصمیمات خطرناک این جلسه را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230476</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/671307" target="_blank">📅 11:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX49HXaha9raM85hYX6kL_BxJtFYM01P1LNKH7ZACKfgK-2cUmG7WRHj3Yo9xzTddqfXqMz0KODxmvPPRHIBXxEtsj7xBSpnh1jqRujS0R0BETPd8A8vZS643OOD0GOgLORKAtoaXGrHnvPNRjXUknd68Z6-wjj0N501PQWbs8pmXmZkyTwsne05SFRvww89NT_-B3a45TBmbtaS62DZKtEkuJvDhkLedAstMBoAu-FfDfbaHKq5PHC-cElD_caCreMxxa4_XHY2vBsqVwZeek6tXQ0eQ4u2_N_QJ4oOHZYHUSlt7LCjoFe77RvN_9WrKAB-gRGorLM43UBsrPhQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسئولان با پشتوانه ملت، باید اصلی‌ترین مطالبه مردم، یعنی خونخواهی را در اولویت تصمیمات خود قرار دهند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/671304" target="_blank">📅 11:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگران بی‌بی‌سی:
آمریکا با تشدید محاصره دریایی ایران، به اهداف خود نخواهد رسید؛ بعید است جمهوری اسلامی ایران دست از تنگه هرمز بردارد چراکه این کنترل، مبنای مادی هژمونی منطقه‌ای ایران را تامین خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671303" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابستان امسال گرمتر از حد نرمال خود خواهد بود
رئیس مرکز ملی تغییر اقلیم هواشناسی:
🔹
با گسترش پدیده النینو در اقیانوس آرام در پاییز و زمستان امسال بارش‌های خوبی خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671301" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGUuy91IKpbsxcxppxVPjk1s43oFdM0EjAfCKrHmXxvYUly4Y5rAOI0z6hSEESRKqeN313ROjSLq8rH7ljJhWYq41KQyQigax8GmNn872RdW8KUdISdn6RZWrt8wVsIuHODYCvNqu0En_1uLZ04MEZz3xhyNbnwQf6sLcvcXIUtcIy1LH5CKpj8DFSbA27tyVsmAE8BfbuP8Ja-MGxLXHG929Vs4xT7iUnlmo0Ei1ePQ_tFZ9Jo-yYBQXEk11pgs4kPszj6nXvHJrLUgYVKQkYlHadUU_QhvyUUFQUTi4i13DrnptKDiORkh4ek3dqEpN9vHwjjx8LEvNytclr-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات سهم خود را گرفت
وال‌استریت ژورنال:
🔹
امارات پس از کمک به آمریکا در جنگ علیه ایران، از جمله مشارکت در اجرای ده‌ها حمله هوایی علیه ایران، در ازای آن به دسترسی گسترده‌تر به تراشه‌های هوش مصنوعی آمریکا و امتیازات ویژه دست یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/671299" target="_blank">📅 10:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8lZRiQeM31Qo1ceVZrmhDEB6TuBJxcszCuml3meoXT34fENGJ1aM9MFw5nGDvlVsPvoeATOJ-SRgr5bM5SYnO6L44nYVIgWHWh6pOclNECUApDCUDzxXVdTQ9vDdYvlkiiz8p-25gR_vcLRu3z7m3C-_lu7crHCjD9T1LlK5YF6BFpmG-wFJrawHPigu3aU5m6k526T0Zmb45k07tr0UMFokTzI25x2B-_VMbKnptVdUxBtyXXa7MXRhomJvAbvaub6tzHo6B3wrQFFVcMdw4gd2bBuMKCRspiI7qcvkwlcVp7izJ2EWx6ekNpb-eI3IAixgUbINzO_-mh5isPWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضا صادقی، خواننده در واکنش به حمله وحشیانه آمریکا به جنوب ایران نوشت: اینجا خاک اجدادیِ منه، با جون نشد، با خون نگهش می‌داریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/671298" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYgAkUusUAJFBfRk-Im4u-iDCRLHb45GlNXOk4fhPk8_5cQhbBhqwEyQ8TBuhZ8SFmGrEOUr6XHEqjDdoNFBS7Om4Wa9FgIBVN6LC2tRhujCurtZO614RPuKefNqv7tfzjNYu4qyidblRYB6kruvYgb_w06qQdr6tnL1puic08LUr7nk8oVwiLshEIVS-eALfg_SNJNpZ2sm1eWlMaMEgeXUCkTHu8r02n2yWNYrrfzDmNQM8q8RGz2h6W0kv_K9DWMZKP4p7ztzUfLT-1ZMJ1lL4e7hVwh3rz_4-Xzg2bnCZt7vSTQjmKiqWgZD28Bg9_vUsoX8tzQIizdzd4so2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا لیندسی گراهام توسط رژیم صهیونیستی کشته شد تا ابزاری برای تهدید ترامپ برای ادامه جنگ با ایران باشد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/671297" target="_blank">📅 10:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏆
حذف مدعی اول قهرمانی مقابل اسپانیا/ فرانسه با انبوهی از ستارگان به فینال نرسید
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671296" target="_blank">📅 10:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به پادگان ارتش در بمپور/ هنوز آمار دقیقی از خسارات و تلفات در بمپور در دست نیست
🔹
حدود ۳۰ الی ۳۵ دقیقه قبل بود که صدای چندین انفجار از این منطقه شنیده شد و حکایت از این داشت که جنگنده‌های کشور آمریکا به پادگان ارتش حمله کرده بودند. ظاهرا…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/671295" target="_blank">📅 10:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
قسمت اول آموزش سلاح جنگی کلاشینکف
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671293" target="_blank">📅 10:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671291">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0GA5zfrNjoKH_2HUORy3xHVslB6gaGYW_5oIh6qaHsSXktJ-bXBxMNyjPARrwaj7Nx1TT6umehxEVpeszidZ2bhxUqs2OCDH9-ssvP4tiGSc9OkFMjZkwCXTJkvD9CTY7XNsJzEVVWoksgSTbJXQ9vvBwHIpKbsEI2EcXouru_hrpcv7xnAC-hEB-ZQOzMXevKkE57fWvsTwK6yrLxQqJHfnaaQvUOFM1iIJ7bqdHea0ruEftpY6-rXQFNKkpwpYqHwJs3Y5xyPyMEMD3AXu2jdQZtMRDNBVNgiD_HIva8XjzObQylyULq_NJdEZKqyAWQjeE_Z6jA8b3B0Y_DncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف‌شدگان جام جهانی
/
نفر بعدی مسی یا هری کین؟؟؟
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671291" target="_blank">📅 10:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671289">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c819d1fb6.mp4?token=CIduZK8MvAq32yEeTUN4Tteyn2fffaIvhzSiLBfCou9svOBhDJ4gsHhjLGv_-uHIqSYroj3HvuKsZDHIBHU24nBWVaZeGZWEp28o0-6T2QqB11iCB0e5PtYLhXswVZ40xv1ui9krbefEBoSebkp7zvdyw0V0KrCe5YRxJjtSs0whnR02bHLrrlRwm_5D0ZqeMj2IbG_FIEc3tSkQLGWnKbQNL1phq2M2uQg2AaRmzuA_sfZ760rxvk3YdAoRQwjQmpG0_DN0VAh-J0MNYBp2k3t39Nq7U3_tN4SiudalAI-LpCR62gjKXvOinmaxSjrTYRTv7om964QTvCF8rXqz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c819d1fb6.mp4?token=CIduZK8MvAq32yEeTUN4Tteyn2fffaIvhzSiLBfCou9svOBhDJ4gsHhjLGv_-uHIqSYroj3HvuKsZDHIBHU24nBWVaZeGZWEp28o0-6T2QqB11iCB0e5PtYLhXswVZ40xv1ui9krbefEBoSebkp7zvdyw0V0KrCe5YRxJjtSs0whnR02bHLrrlRwm_5D0ZqeMj2IbG_FIEc3tSkQLGWnKbQNL1phq2M2uQg2AaRmzuA_sfZ760rxvk3YdAoRQwjQmpG0_DN0VAh-J0MNYBp2k3t39Nq7U3_tN4SiudalAI-LpCR62gjKXvOinmaxSjrTYRTv7om964QTvCF8rXqz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر اسبق ایران در روسیه:
مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد/ کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/671289" target="_blank">📅 10:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671288">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ مدل ساندویچ فوری و پرطرفدار برای روزهایی که زمان آشپزی نداری
🌭
#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/671288" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671286">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شارژ کالابرگ کدهای ملی ۷، ۸ و ۹ از فردا
🔹
تمامی سرپرستان خانوار، از فردا می‌توانند با مراجعه به فروشگاه‌های طرف قرارداد، از اعتبار کالابرگ تیرماه خود استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/671286" target="_blank">📅 09:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaauKcP3_KMlbKlSIHSrYIWMqGV4aKCFsFmipZp00lcx0uym9n6NXyMatTVS6b62Zkao7PuC9WGrR8TUqV-ipGcfmzeQQfBSD0jUbFG6eV7t2TC_kfcKkBq2DG18vsEIelunD8mg__36skO_-1Tpz9TTRIbos5DzukqWRtruFWZjD9cY2EPvEZqsOD3E0vNjfRXrM_oSeKxR3u97Qm6nWxINqdGcKz2YMThQoOei7ToePX8Dae3RdEnDOBmy8pExi4PTKX-YrzNF1o6pElJ1Q4XbMrVvW0RM6FDHBZPyXRYD_-k64O1u_cFA4cIgaZG2e6z5xnuE08TYBYV8D9y1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت جدید تلگرام با قابلیت Community و ویرایشگر پیشرفته متن منتشر شد
🔹
اولین ویژگی بزرگ، ویرایشگر متن پیشرفته (Rich Text Editor) برای کاربران پریمیوم است که اجازه نگارش مقالات طولانی تا بیش از ۳۲ هزار کاراکتر را همراه با جدول، لیست، نمودار و ابزارهای هوش مصنوعی می‌دهد. قابلیت دوم «جامعه» (Community) نام دارد که به کاربران اجازه می‌دهد چندین گروه، کانال و ربات مرتبط را در یک بخش واحد کنار هم قرار دهند و مدیریت بهتری روی دسترسی اعضا داشته باشند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/671284" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPJfXxatoDDYAVQfknJltvnWeBs7DVfu9sa2aqhXFu5hVPyHBQ0J-tF-7l3W34qJZUlldbaBK4nfaozFA2hLtRKbMnLTLbZV2i8ICcgmKHdcb_pN_A1OvHnzoKVqdnUyw1UHwObSCO29JbkEhYB0-rEC9VJ7MyLH_uKCE-9WTJ96ygMbJQsKfIRElV0cZXQiMBGY_n-JOXBzru9-zNZaIVuSZZD5Bw3ghoYHjOG4Idyh_RRrdD8jD5YheXGis9UNLPv64-BgrSfFXnTyLtqA0kW7UnZz1i9KZ3qENAGwZi9rio3zQbH_HE3N_NrLcONyh4x1WXG3o4hwJBkjpdbuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کنار
این علائم ساده رد نشو!
🔹
بعضی از بیماری‌ها سال‌ها بدون اینکه متوجه بشیم، آروم‌آروم به بدن آسیب می‌زنند. اگر این نشانه‌ها رو به صورت مداوم تجربه می‌کنید، بهتره برای بررسی بیشتر به پزشک مراجعه کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/671283" target="_blank">📅 09:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دقایقی پیش اهالی چابهار و کنارک از شنیده شدن ۶ انفجار شدید در این مناطق خبر دادند
🔹
هنوز محل این انفجارها مشخص نیست و نیروهای امنیتی در حال بررسی این موضوع هستند./ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/671282" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYci3H_kAfiIIFabk-Yuq_90K3_YkzfO-x_G0Z7xwgWe-1wvJv1ZqKxdFhaHC1l_cWS2PrXf6EOmrSYvN4m5Xsim38sw97O3yfDMmZ0-YE0CVbXqSEipnHFke96FoAIkFfGtWC-GJTjo1wLOv0XjLAiQjolrXb2z9wMiNG_haW_OMpZ8j2jxThVQ-fVVwtE7LjMIQVnJOEm0ybJPeDRm1tTx9BKdVpgVVH19z0FDgK9olcW2mNtjvugwGPyf5-_k06tX0rRnNBvvQlKT7LOkkmcqg6AhFLYVw1qqXVmJOXk2MaH03m5VVRas26CDZYehG1LXj5eE1PIXZQGjXHhprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی تیم ملی این کشور شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671281" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم فلسطین در جشن صعود اسپانیا به فینال جام جهانی
🔹
هواداران تیم ملی اسپانیا پس از پیروزی برابر فرانسه و صعود به فینال جام جهانی، در جریان جشن‌های خیابانی پرچم فلسطین را به اهتزاز درآوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671280" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
استاد روابط بین‌الملل دانشگاه شیکاگو:
🔹
اگر از نردبان تشدید تنش بالاتر برویم، به نظر من این ایران است که دست بالا را خواهد داشت، نه ما. این فقط یکی از دلایلی بود که باعث شد پس از چهل روز، جنگ هوایی را متوقف کنیم.
🔹
تا این لحظه باید برای حامیان بازگشت به جنگ کاملا روشن شده باشد که ایران توان تحمل حجم عظیمی از فشار را دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/671278" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTXx3qyxlWjEmCdjoF3kSKV-PUTdeYagk1k8zTps7fL8iUjcl6AsUXcgfUj7fMja5vdqvOmN-SKsACEEM9_T5052I1j_QkWYBpRKivrR53IP6yEwEcy6e6d_kBZeyaCb-V3j7VG9YuXyqCfUJwphMiXemL9nhZMFQAU_Auh9MCaVX6QAQRq6yJaKkhO2x45Tebu9c3sHtkMgNTzkeSKZk8WtXYlJpkm5Ar-C4dCkQWmTFsbV1DBWaapWENstGlPVXZYRC-sYTtQsCnzKMtelpCGJPE-Rht0rGhvYIsPV3uNfFIzxehRFt1D_IeHHAHUWohs-4vmEy2eRs-vFrO_LRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7yB9p9JtobnG2ejJok25YCduXXCEHXI5HDHBLmaVbwnGujpzhMP2wc9iJhsZrgV33tPOtdIZZlD4Se4fRBKWz17GHUVcUaYxyDm9yrvzifXwSoSpE2oTJzFXOJF-DuAkbFZITiF3eSjq_HsFf0mV8mTlxPWSsoYE701mzXWIKDd8bz4sueRl0TDekutp56JtQIM7rL-Z7gqlLtFkAcJd_SyAV23YLJU1xrng_vfd8FAnO2BHxWAKWLuBwILAxLCk8iKtIJGnUAvMYf5sYCn-m-E2J-VcSl1IClF18ZBQssKQlTOtEHT7rcmS5t1pyc-0XSz0oTAAochitU4FF2ARQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از یک انبار متعلق به شرکت «کویت و گلف لینک هلدینگ» (KGL) در منطقه «مینا عبدالله» که مورد هدف قرار گرفته و به طور کامل تخریب شده است
🔹
این انبار، مرکز اصلی لجستیک و پشتیبانی ارتش ایالات متحده در غرب آسیا بوده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/671276" target="_blank">📅 08:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdRRZioz8kbLGgqJMhdYm1VcFkiI5FbKFMlPwjDXsE6b4bI967PKEey-pkMUM10KSOAnL-d2FYxv4RupI5_s9FTQ7AEPiw2__pVC--4Hu70vwHlpx0YOa5moaxSGrdASQKnaJiatnkN6Qv_ALVPoeYWWVLzB37dw9OtHXx5omtLeDpxo4DcIOSW03Z8uKPfAY5bYWzvuT4h17nwdy_chSBj4sH8gDlq9ayrP8M7AiVHe9KcBAuKt3zdcxiVHSwrVTROQj79Cff14aW3z3aW03fV1vbhZpjlDZaCFrlQcXsS59AGJy9iBOLFtpiykCQsU_Z5RvokQAsfaqe0D47cW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های ساختمان با کیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/671275" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671271">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قدرت و استقامت پاهات کمه این تمرین هارو انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/671271" target="_blank">📅 08:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671270">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRokcArFZmfgZa9AMHRrb7zEL47_HH8fBsKIe1jEh2J0mckaisipCJ7go_fjdLluoETtdUnah-8RzkPr-v1a4SCvq3mn7__PiYtIbyYpT0_brKOZlbL_eaxi-qVBO0BwwCSq6fU4k6i6AmERpgNhcQTV6GTfE0l6rDoGWDOeWEK5L6xTHpB7-st2KULMZ9SAxvid7-cfEZRWEz68Wbn7CvGAwlYSyG2m4t1zE3f7fwGhMjSLsynpxaudzUtyS595wpGdENiaqPEijsh9mkrWp-fzFqIivpCGjaiYqPYIqwlmW1V4WVTuTcCIMX_qPRheaTqmTZ72zcc1XVc3i1bLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پنتاگون برای عراق شرط و شروط گذاشت: یا ایران یا آمریکا!
🔹
وزیر جنگ آمریکا همکاری‌های تجاری و دفاعی آتی با عراق را منوط به تثبیت حاکمیت این کشور و خلع سلاح گروههای مقاومت تحت حمایت ایران دانست و از بغداد خواست میان این گروه‌ها و گسترش روابط با واشنگتن، یکی را انتخاب کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671270" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671269">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is-uB0zPWtgWs8UvtDR7nb-PXQJ1FrsJPiKh045zdkScriJS_PGGG1Rj-tENg5fstcY2O19kdY-4I2A1PSJ51VOnHeYnhC8FMDRrLxDkczcn1XNhGr-ZSgIBMmBR3d97X9Gn3WCoSLSdC15MPSOO4Y1HAFMA29WuLgYwBp9sXBeVv70tIknAWCqYZJTZWTABJotBaePaq0QSyUuY343__E1H3QwX85-xXfL1ivOEppII3zbbx2OXYZAyeGg-epKGvlMNgCiLQotexIchQ_zUrGUFbP7_y8iCaQpfZ-zU4W76tpNE91amU1C4FlGa6f17NImYA1gvDY6NjlT5L-xWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لامین یامال در هر رقابتی که با کیلیان امباپه روبرو شده، او را شکست داده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/671269" target="_blank">📅 07:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671268">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIk2yi0HbRRLDdKGCgXYXv8Kv1EfyDAufiZjsarFQoIEcTq8HSIbFBxdMYT2GckSFVcF-205K15WJLp14Nw2E5fB4TqfdHl22ROcNkwkYVjahtPeoyVelyYTgmfC7sim15VkJ4QFNkJKq8SkGD5E8m1ve6_4uRS0CYtE2A2TT7oJON7Aiz3YybKC1qwXUZFs626CgT_YCZ-a2jCjBOQPznNXHLHiLT1B_NW7tA7AwDFX-jv3UnM5dmwcDTBu-AtibdfeUEVfUsqNlZk1dbx6Ng3ZyEUxf0MJ0XGVGdyrb97CP1Qk5Qo-yC2Nkz9QWrS-eOzkDZgYgfnJ_WnfnIAMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار افزایش تابش فرابنفش در روزهای گرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671268" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین| فصل‌دو،قسمت‌هفت</div>
  <div class="tg-doc-extra">زکریا رازی</div>
</div>
<a href="https://t.me/akhbarefori/671267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
محمد بن زکریای رازی
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «فرار از تله‌ی تقلید در بازار» و پرداختِ «هزینه‌ی متفاوت اندیشیدن در سیستم‌های سنتی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/671267" target="_blank">📅 07:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زکریای رازی و پرداخت هزینه متفاوت بودن
#پادکست_کافئین
| فصل‌ دو، قسمت‌ نه
☕️
🔹
ابرکاشفی که نشان داد چطور یک متخصصِ تراز اول، می‌تواند با زیرِ سؤال بردنِ پیش‌فرض‌هایِ صلبِ گذشتگان و اتکا به دکترینِ «تست و داتایِ تجربی»، انحصارهای علمی جهان را بشکند و فرمول‌های جدید خلق کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/_pAcf2fyVaU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671266" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J70BLF9BukfGuzyA8fonerFLDM4TFk0LqA4MDvqMzv63AtKBu9xxf6aL24YR7MFmnDlaqFVuBCUcxZRA1WAtlhlsulqlSU9vfjVqTkmB0fRiXnGFNu6P1jrUNYLfX5qs8NvxXtbmwi9whXEWXulcaME7Sp5oeDVW6O-SYIbD8iSJF1TASjNqhS95X4SFaQpzOWn9BXXHUEtGU5Xi6bGLqB2DI5bbsEdQgN1NHeWdGHH7V8S2hOydDrtqVtD3Jz-ptoLkpgRSQh50z8OyA5TzKmleys9-yYTqmAHyuPODQnggdVqcYVEO09KmKgk1jJqb9MiUQd4opA2to2pN6k3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۴ تیر ماه
۳۰ محرم ۱۴۴۸
۱۵ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/671265" target="_blank">📅 07:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
حوزه‌های امتحانی نزدیک مراکز نظامی جابه‌جا شدند
آموزش و پرورش:
🔹
تمام حوزه‌هایی که در مجاورت مراکز حساس یا نظامی قرار داشتند، شناسایی و به مکان‌های امن‌تر همچون حسینیه‌ها و مراکز عمومی منتقل شدند تا محیطی کاملا ایمن فراهم شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671262" target="_blank">📅 07:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۴/ پیام مهم سپاه به مردم کویت؛ مرکز ارتباطات ماهواره ای، رادار دفاع موشکی و هوایی، مجتمع پدافند هوایی پاتریوت و آمادگاه پایگاه نظامی آمریکا و سکوهای پرتاب موشک های‌مارس در کویت منهدم شدند  روابط عمومی سپاه:
🔹
مردم شریف و کریم کویت؛ شما به…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/671261" target="_blank">📅 07:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارده به مرکز تعمیر و نگهداری هواپیماهای جنگی در پایگاه هوایی العديد قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671260" target="_blank">📅 07:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
صدای دوبارۀ انفجار در کویت و اردن
🔹
منابع عربی از شنیده شدن مجدد صدای انفجار در کویت و اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/671259" target="_blank">📅 06:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
استانداری خوزستان : دو انبار غلات و آرد گندم در دشت آزادگان و هویزه مورد اصابت پرتابه های آمریکایی قرار گرفته است
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671258" target="_blank">📅 06:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۳ سپاه/ پیام مهم سپاه خطاب به مردم اردن؛ آشیانه جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
سرزمین مقدس اردن قدمگاه انبیاست و جای اشغالگران و جنایتکاران بین المللی نیست، انتظار…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/671256" target="_blank">📅 06:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۲/ مرکز مدیریت ان اس آی، مرکز کنترل فرماندهی ، انبارهای بزرگ قطعات و تجهیزات نظامی و مخازن سوخت ناوگان پنجم دریایی آمریکا در بحرین درهم کوبیده شد
🔹
مردم قهرمان و تاریخ ساز ایران اسلامی، ارتش کودک‌کش و رژیم عهد شکن آمریکا شب گذشته با انتشار…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/671255" target="_blank">📅 06:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سنتکام از پایان تازه‌ترین دور حملات خود در ایران خبر داد
فرماندهی مرکزی آمریکا:
🔹
این حملات هم‌زمان با ازسرگیری اجرای محاصره دریایی از سوی نیروهای آمریکایی انجام شده و هفت ساعت به طول انجامیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/671254" target="_blank">📅 05:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد  روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671253" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکذیب سفر نتانیاهو به واشنگتن
🔹
کاخ سفید بامداد چهارشنبه گفت که برنامه‌ای برای سفر نخست‌وزیر رژیم صهیونیستی به آمریکا تدوین نشده است.
🔹
پیش از این رسانه‌های صهیونیستی گفته بودند که نتانیاهو قصد دارد برای گفتگو درباره موضوعات مهم به کاخ سفید برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/671252" target="_blank">📅 05:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد
روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی با آمریکا را نکرد و طبیعتا اصابتی هم نبود، برای پنهان کردن شکست و ناتوانی خود تعدادی از پایگاه‌های ساحلی و نقاطی در استان‌های جنوبی کشور را هدف موشک‌های کروز و بمب جنگنده‌های خود قرار داد که رزمندگان مقتدر اسلام با پاسخ‌های کوبنده متجاوزان را تنبیه و سرکوب کردند.
🔹
در موج چهارم عملیات نصر۲ با رمز مبارک یا اباعبدالحسین (ع)، KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده و منهدم گردید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/671251" target="_blank">📅 05:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هشتم عملیات صاعقه ارتش؛ ادامه حملات پهپادی ارتش به پایگاه‌ آمریکا در اردن
روابط عمومی ارتش:
🔹
به دنبال  تکرار حملات وحشیانه دشمن بد عهد،  بامداد امروز، مرحله هشتم عملیات صاعقه با موج جدیدی از حملات پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه اجرا شد و محل استقرار جنگنده‌های اف ۱۸ و سوله های بزرگ تجهیزاتی ارتش تروریستی آمریکا در پایگاه الازرق اردن، برای دومین بار، هدف حملات پهپادهای انهدامی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671250" target="_blank">📅 05:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8efU9wFNN0lTy-aL35Pq_LMw_ILCJaYFBzLJa8vxKp5_Qy40BBtVsBqCGzjR0if1Luy8havLUBtiHr7pwc0OT6kIbli1mxYk0a-I4eK6-8lzBLbint9Lq9ui_1BJCIR_Fza6bxeSMJDjd1aBiwwuJsyi5L7QLTcbFKQFEGex0ZyDvSDIxR4iEC6W3pcR9jwCzbV1Uf2BN4ZUR3DRpyVxV1NlbhPxZZJ94rQeJBw8UpzxlXrSyb-UjOWUgdizv0Gv6YipvsVqvKgR8b_MOJCB7WYukyuvKQsCdYWR2mAiLcIt4u9CDUyPJxZqzkCFSp_qMZsS1qg8LoGfhV5CCGIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پهپاد ایرانی به منافع آمریکا در کویت
🔹
رسانه‌های عربی با انتشار ویدیویی مدعی اصابت دقیق پهپاد به تأسیسات آمریکایی در بندر «عبدالله» در کویت شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/671249" target="_blank">📅 04:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌کس نمی‌داند ایران چقدر موشک دارد
🔹
مجری: به نظر شما ایران چند موشک باقی گذاشته است؟
🔹
ترامپ: آنها تعدادی دارند...
🔹
مجری: صدها؟ هزاران؟
🔹
ترامپ: نمی‌خواهم بگویم. هیچ‌کس نمی‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671248" target="_blank">📅 04:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
وزارت کشور بحرین اعلام کرد که بار دیگر آژیرهای خطر فعال شده‌اند و شهروندان و اتباع مقیم با حفظ خونسردی و آرامش، خود را به نزدیک‌ترین مکان امن برسانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/671247" target="_blank">📅 04:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت موشک‌های ایرانی به اهداف آمریکایی در بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/671246" target="_blank">📅 03:54 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

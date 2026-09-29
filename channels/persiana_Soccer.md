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
<img src="https://cdn4.telesco.pe/file/K7JEMbDI4S3D0s75jC35Oj03MbfFijuxTTrM_EE7ZJpJbo_8AjqCY5FeA7RrNoqBE0f-eeVnLxlxIGx1789CaxVXtOYwTjPE4FcBfO-ayUQqf-QKPuFxbGic33ityymom9X4Kyo8spMShEFGxl_5Sa59n2-qdr9o-zxtKxNrG5_17xzk27m6O7WTeVbu77wU3XnmfKYNxsyV1-xfGs5TZ8Y4IQNJ1baxPs-zxdXTx8M2C0WdXfNaOs1_YykNChwS1dYpuabmAnor3QQD_rMcXO3S1e7T16BW06C_L0bGvwISZVGjIhdssU8jHtC1qvir9CDn5cBehWg1Hy7VFqjqzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 440K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNH_S6IcCbnSpxtk5ZQWdbgI7iH3STGvmZXFX4V7TlpWHBrlg1iMfGuZykkD_TvXxJRV-YLu7gvnStrzec5whycKkjSVZXiS0uqac5QYaZgrMCTimCFZh9CNI1z2daRO3drPchaJm3lfE1qYn_PkHn8rlGMJ6j7gfH5xE3Qu2Hv5ArrNhbKxoYdHfTnt-SOqlLM6nQb9EGQZnqHZQRkRWsHW4S4IfKHf1eiRN84K6ob5h6AEf-8B_nqLEsWRzh3x1TJ-v91HiFZFhOFfywmsW15usttMuMAyT8SjlfBfKM4viM55Oqi0XAy5H4oLFAl2WqGIb7GkeyeuAMqugQZJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQbyURrMG_UQBw0GT2IactvEwJGuDSiEyVafWD5M6Vk8Xu_gyKX6VlYIqyXa3U97SAs5Cr9RYSzgygWYhFZN1XlEbyPkDyYNaKMfZ8ShrhQvCBqx5f1S4Gycbk7zMtLrCeBHRI4tD496J-RJy5A6YWElDnVcBWP5AQlsg5FLYErwhKso7T9IyKuU9SHtnsnFXB9gVgmKoJH6ahrVSEE1kq4a994BKNkNnY3wh2_-rBRyVhWdmS7xgjbQhdkY_aQtqCHbmRJiyr9e7hiTMzEXc_68QNGaUQnrr-rkSnEIH5szHuSBFw7J2xdEG02-U0rHKu_R8TZpiMp37Qs_GGQ_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=szKR9roAXrGJy0ahB81prg8OiS9ezo6Vl6EKoqnSJ4ynx20SZKYiZhoWigTg62pDQwTu9zXHAHvUWL0yeomyzLTMYmgMyjVWveFZ3QUwpCGNm3bEJCJm5B1cor2qpa1MIDNAMF0m-hO-ZKGdLW3AwSANgugTyYkz7KJ03hdvgSAoxg9pMhYdOYb4J7cEYdOLhCaLG6SENZoJhU2eHbALQ_zRjPjeZk53bsws4GmNZ1ZR47BBZi1tXCLnD69a7Q5oYGIleWu8oECrjC7G3yi54REhHUxTsqUB8e23UgvU5sPZtU7lL_LbMgGurnrt6nm3ilcrnx78boUibxB8HWYAaDT3XoPExrOomw2lWXylj18_SlNWKIElwX6BnWIrvFTm3Ri03dYgC8XmH1uAiCIbNbmyuaV8-pijPZLoYJ_0cEBAbf5FYjWAw8cV2si4xSmp2j-7z_UpFW0KE7k0Ki7abtPO11hJzDrTWk1iMag9Vmkj-7Nki-iXQIauYMdinRJC-R7pvV0VbufBho_zutpg8R_9dUAh3YWXzCg5Q0Qy1ZQeM7cOQKiYSqcIxxYpkbczTKVo4OfF9xVnCYHT1g_qy4SnBvWbbJatgeOASof1D7oAGXarVflcuPeefqDPAQxZsNLyE1xjkZA17r6BlS4s1hI62lyObLki6txj-2GWDuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=szKR9roAXrGJy0ahB81prg8OiS9ezo6Vl6EKoqnSJ4ynx20SZKYiZhoWigTg62pDQwTu9zXHAHvUWL0yeomyzLTMYmgMyjVWveFZ3QUwpCGNm3bEJCJm5B1cor2qpa1MIDNAMF0m-hO-ZKGdLW3AwSANgugTyYkz7KJ03hdvgSAoxg9pMhYdOYb4J7cEYdOLhCaLG6SENZoJhU2eHbALQ_zRjPjeZk53bsws4GmNZ1ZR47BBZi1tXCLnD69a7Q5oYGIleWu8oECrjC7G3yi54REhHUxTsqUB8e23UgvU5sPZtU7lL_LbMgGurnrt6nm3ilcrnx78boUibxB8HWYAaDT3XoPExrOomw2lWXylj18_SlNWKIElwX6BnWIrvFTm3Ri03dYgC8XmH1uAiCIbNbmyuaV8-pijPZLoYJ_0cEBAbf5FYjWAw8cV2si4xSmp2j-7z_UpFW0KE7k0Ki7abtPO11hJzDrTWk1iMag9Vmkj-7Nki-iXQIauYMdinRJC-R7pvV0VbufBho_zutpg8R_9dUAh3YWXzCg5Q0Qy1ZQeM7cOQKiYSqcIxxYpkbczTKVo4OfF9xVnCYHT1g_qy4SnBvWbbJatgeOASof1D7oAGXarVflcuPeefqDPAQxZsNLyE1xjkZA17r6BlS4s1hI62lyObLki6txj-2GWDuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/30656" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
WePari
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن وی‌پاری
💯
ورود به سایت وی پاری (فیلترشکن روشن)</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/30655" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKaj14Ctp3bkHrHAXz-2uOzgOIVyDnRd3JGJFnMPe5mEb0tB78OBFTwmZfnSkOvTwZCWZ4ySc1KhjXhnKF0AgjRkltG3N_ve2u0JV9Q5KBVAWdHFJIBbn8kXAAjbpsAQTFh1FDUWP-FeaeOvLP7ifKZnonAmsZHs8zfHB6E2pp3ImuBA0C8q-HtA-ybXpN75MdE9j9EWMSVS3sAYpo6alkXHYtxtKIY-Qfjq3h9bUIp6NBXNXvXZVoADuKwuy3mlneyop4g2DFEm2rzKCP5GcgYTZgy-VNxdqpJj4XSm0nZqXQDFK-1HZA-tdGlEIrTOq06zoHw0xN9nStkdK10_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_edgTfAHjTT_iK3RhmsSytOi9sjVShZk7rvlVkHOqWxAeWPGimrwL9k5-g9tsb_EQhs2aZWiY2LuK_PINzSVJWT_uY5uTuU1e_W8TbeQ7Dih_URhlYuuE0tI6btB-HJ719ZF_E2SRK1t4H-toi_pDFh5jwEizF-ju5-UByggnWPDg0T7sB9EPT5QFNa9fkc-WWu-mApmJ6NBogta99zgV7TUjsfHmHWYnsPrL8MZvRWLp-pYk11rqQu3rHfAu683LmwR466brKgwjnkQoGgezn602Mw-XscEunbkeP83E6vIepIUOTwwNN3hJPXYnQQDxXCGJ8pbcimt88CRX7zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX73auPHm_rtg4wVxChFqiGDjs14Hp3DD-ar5uQyRz__aALrGkOljP0o-dCVyKzFv1RV8nYE4ZBN0WcFf4DsxWCFpTqQEbwq6paE_uwBP4fnkWoPYgB8cwZKwDGuTEPryBkhO6xd-SCSC6YYeivjhq8SSWDMF0xNSJHicxm1ty2TwglWJTDBCWDHY5aVHMJzXces3xKqerwcwxjNdY3Z0Y-5rNDLVfzJhLvtIQ1jf-T3BSPHZT-oHOlJnRPgw2EmrZf3TU1ept7hSZvdDY8_L93W8nx6bJVW120lvlfzIaS5F2M_CsJaDMZgFq7JEfsttMGru-06TilwmYTgrInZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=P7PK90b6U8214pBRy_cSK1-e2_5bZilMnNmW07CcjzmIrJU5Jke56ZgWhSzRXn0KZdsXCc-iQHOX89uVMPsvJGtlOyuaQGc3InJFsAt0B8qA9i19XWGTy2O-uKhF1NI0wtS3sCMv-mkuFifem0GWhFiU4JVU_md4BTe93IVjbozPBgmE5vVmveFDWnr2lVhQjssa_hN6esXAii3-b3LHeXz4_-BISyf-EEBXcY-2D3Q-7JHcjK6t7YBf9n3QX4AlMn8G84M_yiMBbTDOSCKCs_yDITqQxD3voPFSTFJVOFuLJPKLYOI7GYu40lKuAkkw3YQ7xva2vzwCi2Q3WY9N-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=P7PK90b6U8214pBRy_cSK1-e2_5bZilMnNmW07CcjzmIrJU5Jke56ZgWhSzRXn0KZdsXCc-iQHOX89uVMPsvJGtlOyuaQGc3InJFsAt0B8qA9i19XWGTy2O-uKhF1NI0wtS3sCMv-mkuFifem0GWhFiU4JVU_md4BTe93IVjbozPBgmE5vVmveFDWnr2lVhQjssa_hN6esXAii3-b3LHeXz4_-BISyf-EEBXcY-2D3Q-7JHcjK6t7YBf9n3QX4AlMn8G84M_yiMBbTDOSCKCs_yDITqQxD3voPFSTFJVOFuLJPKLYOI7GYu40lKuAkkw3YQ7xva2vzwCi2Q3WY9N-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgBEL7yp7a45IEfgoxw99zsaAYnVogVap2EYpFkk4wIJZlcUI_qZp0WpcO7sNM44NX6HLl6xhlA1665soPUYGPZ_jxQ_eglPAXqVO7s17k4qc1NSZIa7roxUyYPVHpltnEHZksOTvIELBqchvqt_z4908jG2olOKGKo5VEzN5Ukmeu8ChaLx7PRcmWe5umBY0x6SvwLl4I8n8uHz38AQaJs8Hxo6zwsxsxlYttKM5NZxTWPdjECrJngdcU7hazugjUE2km3yFVgEdAitjjqnuUnllC2AIJsGYegPGJUfPe3IkrZxbDu5NrRV1v0sKgziktpnwa3PjOweheLt6gub9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ToOKUxahh7efxXzjwLhgZPFKYlgtix-M9d57cpNgBnQI-a7RTCqMOG7oXZbyDV6Jl6cYIAcFSGvD-SoJnB_H_RvuSHXBF_T6mSY1EQwb7WlqIugC8LoZkCwA6SkAEOY-sa7incd1HyGJyM22ydWraiEfyUep8TlFzzONhL76BdmAh2DcAsR_jF9EAzNZS9PiNLVY-yXkWUaSEV7LZh0e4kgmgDIjSmSI6LnovMX2og5sDdHsaFlWAqUg9KcXm7JtQay-kJF0otB1Pz3P7JYtG9VbBRk7uGCtQ06NuzIEW_NIBgbC2Hw_kAc9a4r0Oz4pXT3LMtRVf2FjPzdmErlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPfKeYXYVrtFRP4dx5lwctmPwaissS5d0vsBNZQUrIoESPqtjHSIVpZiqSsK7y91Mhz7VpMcAq8ABif2afwckwSN5tvvCKYRL1smqjfRjWKMA-KEgPvmKUQGNbzGg01uwGYWRz03U26Ump1XzTxS_R3C30fvHepN5CVjVfvlr3gIY6QBI1WaUai11RCS9YRXOyILDrzDrKYgTTc3byD8gGTRHIrpalSpwaXBr86ejr7ppiQ9Er5LIniVzwAZV_vjCfMI9oIR9lpF8XIvQyrkWmuyJGZJ7UdoayzROuSXdUcuuWzJQrTwZLEDvKz3mNG6-dNZe2kFIcrPmPWnQ084kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=u86MCKNKrqRoPCbX6Ssy2QA_odwxMfcMnc0Og6JP7QY9irwyb7OzRttQJesGGAzyRGcZlZHTdXUuJ95S_1FbVI0viGSSKpZxY1_TTmpF_PpxkEKjNJBCrK_6OMw79KXxOYHB_tSvpAmMjxj1zofLswKVOU-8sVZvaQ2sub1Q4X6eVMCDmBYdJuXR_XZaX97NyMqzciwwclEdC29sqsYre5FfK3iK6-U9wzSJ-6AJZu3KkYVonVm-lh9_l6uMN_yW9P2OohwIwGlh_l4F8YaheuamLQAq3wj5sbREApLgDpiqBqJklqknZj1dO6OyT8yEeHgJ5aW0snMHe2KOkEUq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=u86MCKNKrqRoPCbX6Ssy2QA_odwxMfcMnc0Og6JP7QY9irwyb7OzRttQJesGGAzyRGcZlZHTdXUuJ95S_1FbVI0viGSSKpZxY1_TTmpF_PpxkEKjNJBCrK_6OMw79KXxOYHB_tSvpAmMjxj1zofLswKVOU-8sVZvaQ2sub1Q4X6eVMCDmBYdJuXR_XZaX97NyMqzciwwclEdC29sqsYre5FfK3iK6-U9wzSJ-6AJZu3KkYVonVm-lh9_l6uMN_yW9P2OohwIwGlh_l4F8YaheuamLQAq3wj5sbREApLgDpiqBqJklqknZj1dO6OyT8yEeHgJ5aW0snMHe2KOkEUq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=hmUNYoy2V0Iy8pkPs4eY1Zsg0IkZ1zsuWyN-0lo1MULsdHuIwkRPFkSMM8rC1eAcJNqBABeSwAgA37dcjm5xZCuVj55-MN6rek8gHrewmuL6h3jfqGHW-6JQVU7Saemp-lX9fJdL3QW9H5cnaTk6L61uTXq31gwVHFmMS7wELnuzgzv20zsR7IBEaH5KKreSWvmNZEKkh0K7f9R1AcUs2-_pqPnpY2O3KCDx2GhaYFQ8hmzMRXrMH0NDETMYQclPxGht0Z-eDSX2jbxBz2ZjOK94VqWR2z_5XCREofefbLpGbpVMIP602vNrGUB6AOWmydOg5mR0Jp5_WJC7az39LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=hmUNYoy2V0Iy8pkPs4eY1Zsg0IkZ1zsuWyN-0lo1MULsdHuIwkRPFkSMM8rC1eAcJNqBABeSwAgA37dcjm5xZCuVj55-MN6rek8gHrewmuL6h3jfqGHW-6JQVU7Saemp-lX9fJdL3QW9H5cnaTk6L61uTXq31gwVHFmMS7wELnuzgzv20zsR7IBEaH5KKreSWvmNZEKkh0K7f9R1AcUs2-_pqPnpY2O3KCDx2GhaYFQ8hmzMRXrMH0NDETMYQclPxGht0Z-eDSX2jbxBz2ZjOK94VqWR2z_5XCREofefbLpGbpVMIP602vNrGUB6AOWmydOg5mR0Jp5_WJC7az39LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Icr5xwQIqbclN9ge-D4nUuwGAd5vv8bLr7qoHOVoEf1Ad__Nhw3CZMyhCWu_YQu7qEaxVvLV7ZPIEIgOC7ZLM72FF6pxkoIahny55RR5tcMjC7vMp_P28e0UfhcHCjXGRSfup2zbkDwVB0UPcE7d1cQU-aB4lRzl7K460J4HQvt3yGB16ltZLbyKSort-Ou77rjPcrFBsMhcNUyu-nNoIKQZZ5_KwocQJ4H7nWWWq17-4HqPraob3x03BUxfJQKBHN07XAN6RUJYeN47BrSE2k78aBxsq3KKVrcgSBVNyKN9VZymCULQ4vpEYXf_94YR1Z4N75fkI_CU9BDTHqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
داداش فوتبال می‌بینی ولی هنوز ازش چیزی درنمیاری؟
😏
⚽️
یه سر بیا ایرانی بتینگ
👀
👍
✅
تاسیس‌کانال‌سال2020  اینجا خبری از حرفای الکی نیست؛ بازی‌های جذاب رو بررسی می‌کنیم و فرم‌های روزانه می‌ذاریم
🎯
📊
💰
اگه‌دنبال‌یه‌کانال فعال و رفاقتی برای پیش‌بینی فوتبالی، یه سر بزن… شاید همون چیزی باشه که دنبالش بودی
😎
🔥
👇
بیا داخل، خودت ببین چه خبره!
p6
🆔
t.me/+3P2wZvzhZbsyY2Vk
🆔
t.me/+3P2wZvzhZbsyY2Vk</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/30644" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3RV18_w4bjs5BGaLMizdf3_d-8RgaLezy-oPMj2JN7cxWqXBew1kLYN5a4qEZdNONtWQMLBLH4ufwJCG81HY5VeR_z1vc-G51Og5FC4gZUsJgrbvj_lDKYzmcfgtrasADFJyYCZug1tzRPincvUWNqmXWKGPsMc5rpIFRk-1KUwvegs7VCHKQgAL7MI-EYRKv0mTSI6mrSkJZmu1hSZO1bRjdr1-Fy7ULYFIU7lDJAMGrDiX97Ff_Kqn3hK-fWtL6hcEDqeK2oyefESRQD0ITn6x7QQlYutLnUal8RMkyiAZB_RWEIxUGDAhPqdTt99vzjz8PBSDbJIDxByMtXVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY6TjKE_4DCpr-qLG-FQGSmK6zLc47Hg0a-88PUSg7aALSYZptftbzTlqp_e_72VLT1pZhTAnurSbl-WIMtqq1OxGg9SKOelFgifzW6vdl8YnwbXZd4Sdb74MSQHsjJXY1Vjb7NW_lSKdaiDJEtg5pqo2zo8NZP-AnP9lw3DNThYXWe3QNMY9Z0ukw5XsyMdRJRERdmGd-_j8B1r-NGjA1d8MmgLBGFVc7c55O7SsbY62tuTEbC-ZzTZrIZ-5LKOq0jZgDOUWLHvicsNzG2dhoP1oMEBN8jAC696qwe1kOYZJZv76emwFsU1Hz-coHinHL-bAmKLwSHkH7bJ4UDv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgVeTZSK3zVwOWWcBL3zJJFeK-8Qo3R20jegFMH6VyqDTQgdxCBcPletDCy_xYw2LpYAy23RnzThoMdoUskez7pPoO6FVZ1JaHqeMwd5S-K0TaRCknG1EQeRCnboOvSqbaS4FK8dralCpsWBPEnSPKgXN4QyqeKGXnDZTsSgrZa5axmHFJ3C322MuMO3zOdminVz4Ov70MgqQ7HtHkbxbyNxyHpda0vMhEmEFGoj4e6LSLUXLwibklfNAdb6_6SRehKt85bjA51NUxY5RocBSguTzRiyb4fBmpTAdPNFVfdFBa8aTe4BIla1gHvfJQRq2gurohtw8tj_rXrLlZy1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=IrQgQv5KwdkrF5PelfiG4o6m5FAIOx9raYXZSHGD5xrCXTNq0A4WVwGl8soaqhqMwHF17Ul-b4eGC1XfOLoNdhtS9GtyLHo9Ym8rzClwRxtshhBD2fTZbhefRSrFEuHxFWmbar-bU1jn4-whbgwg7SjmYO-dmoIS1ZlemLebGgEjQ6mWS66FtrGOPUZTuw5Q8ZSvolwgV-seDrK-LJWc5PAQhXI0eLy0ag9B6BOu_wYcKwVTzYxWRwmtOqCZ3uHl_H63IEfAFhV6XJZ5Mv-7J2rAG8lkPjuFsTvhAWckmu37nL-a4PJsRB2ZMp7wRmTKEDAVGNc-nwDlKcONnojN3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=IrQgQv5KwdkrF5PelfiG4o6m5FAIOx9raYXZSHGD5xrCXTNq0A4WVwGl8soaqhqMwHF17Ul-b4eGC1XfOLoNdhtS9GtyLHo9Ym8rzClwRxtshhBD2fTZbhefRSrFEuHxFWmbar-bU1jn4-whbgwg7SjmYO-dmoIS1ZlemLebGgEjQ6mWS66FtrGOPUZTuw5Q8ZSvolwgV-seDrK-LJWc5PAQhXI0eLy0ag9B6BOu_wYcKwVTzYxWRwmtOqCZ3uHl_H63IEfAFhV6XJZ5Mv-7J2rAG8lkPjuFsTvhAWckmu37nL-a4PJsRB2ZMp7wRmTKEDAVGNc-nwDlKcONnojN3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYlQ9b35lkAGMhF0F0TP4XzauC1b_3QJZ6k8C1d9DJxiJvzy28PwOPsHu8qtykNbgVz9RU_NAhTI_kojBOzSNpfB02vpsNDI2G8EPJFAiUeKNRfX4QBmxE_1hl9GnMcJMgAfjCwrbJ3_fJoEY5y60HctGnt1IWft9HeQ8-G2NqqC-XA9hk1cloEvmH3OkGUIKM4-yRbfsL-Ze0nj6yHx_cVMukTxllBkaSK6pAllS2RwxTt2cTKRMKinhetdrIVi96V4NWnPnYmGdf-oYPdxqnR0UCgA6WWc-QFnmfccRzj1qO636OXp8nGHLd4JqV8c0KVLGfvSof2T3V6GN4-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=KQA8q-ExTQApYgop_WA4TmScXHEEjoB8B4T-8HpuqGy5Tht6RUQc_Rd60p9QOmlL4QaGGs7cu3LLgi4moGk8Xv0lDLTpiiaTSm3YP5jRPDajKkVa8HD64OO-IsqgXOJFumbGp_u_-l2uz36TtSoF-WakTFXFuM-0nS-rP-m-5QiibNGqzvfJ9BUUbzgihXnaiNlCzAisrGJHDf5OG7N4D1PmB9mSdVbY-V_GVNs7sOxBLKgClovJjmWzcG_gUrYcEt1wb-ZEdpPdMs20cjCfSWLfqSE2L2tq8DotX6b3ousl3CC7AXpj11alSvG-I7WaXEopGUa7giE5yDRBspm42miUjkp41sWktoFghV-X6KQm1S9CKDIq_WaKdrN6yagCzsM9C4DgbEK82V6_oYgADsFPLC8yPLidacmKyVbeUWZzgSeuGVAJAAZzN7SUi_nsPlCXhG3mvLQvQnADCW8GDgyo68nlcxhAsR6gphUWMnnu8uiMDp-Ycu--BOZnKqrShXacxlnZ2bFPxY3vymF3-UEWAhZ0s2PkH_AyvBFyaIjSa7ywWBLz2DEy-QS7istYjI_T0HUPJ7A3dKA62PsbsDNRAXR5lLXJQloZQ9PjnkWRxfbJcPQThwkljcwfSXOuj4n-zj3PAPgRqZo-Gs89OpXbEMzU3N9BcTmbFkHpa4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=KQA8q-ExTQApYgop_WA4TmScXHEEjoB8B4T-8HpuqGy5Tht6RUQc_Rd60p9QOmlL4QaGGs7cu3LLgi4moGk8Xv0lDLTpiiaTSm3YP5jRPDajKkVa8HD64OO-IsqgXOJFumbGp_u_-l2uz36TtSoF-WakTFXFuM-0nS-rP-m-5QiibNGqzvfJ9BUUbzgihXnaiNlCzAisrGJHDf5OG7N4D1PmB9mSdVbY-V_GVNs7sOxBLKgClovJjmWzcG_gUrYcEt1wb-ZEdpPdMs20cjCfSWLfqSE2L2tq8DotX6b3ousl3CC7AXpj11alSvG-I7WaXEopGUa7giE5yDRBspm42miUjkp41sWktoFghV-X6KQm1S9CKDIq_WaKdrN6yagCzsM9C4DgbEK82V6_oYgADsFPLC8yPLidacmKyVbeUWZzgSeuGVAJAAZzN7SUi_nsPlCXhG3mvLQvQnADCW8GDgyo68nlcxhAsR6gphUWMnnu8uiMDp-Ycu--BOZnKqrShXacxlnZ2bFPxY3vymF3-UEWAhZ0s2PkH_AyvBFyaIjSa7ywWBLz2DEy-QS7istYjI_T0HUPJ7A3dKA62PsbsDNRAXR5lLXJQloZQ9PjnkWRxfbJcPQThwkljcwfSXOuj4n-zj3PAPgRqZo-Gs89OpXbEMzU3N9BcTmbFkHpa4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWYtdOX9yMf5K61h9HnXvQFWWdt9G0lF8EDp89uoEBsT2yZYu7ZvvhsFtCx0opfyNsgg9DN9Vlt5FhV2sA-THxNG2_oWapxQKXXV9R8FW-IT8b-Pl3Skj53TAF6UA6y6HJCwecWtaTFkKa7in5ak_l6OioTV-ZcB0FUdpkwCKRQDRC-gmMmpXe4JLYzkOwtlBQLjcmQPZOC3yk6675-N4EAZjwTGw-vcF01XOY7--8ye4GaaZMtwljd0z_yVoCCtI5Vw1qyWN4NJMuQ9d91uJp8fOSJXzmpkBLTytfLEqaKWjofLq3hma824qeVYO2sKNrA6Pxbuwju1cxtYFuWLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXHG1ZBplroLpeabxZCPx-4KkJlSTj4Dyf3qPvnZHj_z4Mhrba6EBonCYNROHfQVv2opNjdLI5NcGM4vzlbqN1hI45f-EWeLn5QUYXzmUMZZDtEsIWmp6fHadYeN2CNk5uf8i_CG5J-k6tXe1xG2JpyfpxG9dl0Bl5BsiinuoNlDFsceeKHNEFs7H8-in6H_F6TZohqTe1hRp-FvV8TPTHyLo1ZVUqibwwxd3OehfTnYkoZydB16-u25rnz0QaygiaVjcAqFRLVZqy6BIopZR5W57vvkCgHYCTa9ObkYfzg31c8W63ODud0iCRYY1z4zS7k6jCsQ7WR483E4WCZHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=exgBbilKwuUIdViEYhvx73S4-dqs-VqTdvTGrbvfGTm1Thqf-XNk3XI6qJd49Ymt6LarbY6rVskKK7FSd3kHF4WAKG86XAZtGpt1sgQNO6hgU5EE6oKRqiZE9AZVrbPWTSzloQzUY4MXuUPm_Erj0M-MfYT5qfSgD0jFC1j-ZlYScyBmMzl4O-UhIv7idgXVcPNpe8nu2gkCN2IuBtuYEeDPgFRZnqKK4-8LxL0IIMIkhA3GKZFXzsWv3dazoc_gT08PQ_Q-UxkzviGVNd4xUa3Gwb35gotMcxnz-ZbvP-iOiQfxkluLK2bJB8QfrNR-eSdqbVS_lPcmpCh2BHYH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=exgBbilKwuUIdViEYhvx73S4-dqs-VqTdvTGrbvfGTm1Thqf-XNk3XI6qJd49Ymt6LarbY6rVskKK7FSd3kHF4WAKG86XAZtGpt1sgQNO6hgU5EE6oKRqiZE9AZVrbPWTSzloQzUY4MXuUPm_Erj0M-MfYT5qfSgD0jFC1j-ZlYScyBmMzl4O-UhIv7idgXVcPNpe8nu2gkCN2IuBtuYEeDPgFRZnqKK4-8LxL0IIMIkhA3GKZFXzsWv3dazoc_gT08PQ_Q-UxkzviGVNd4xUa3Gwb35gotMcxnz-ZbvP-iOiQfxkluLK2bJB8QfrNR-eSdqbVS_lPcmpCh2BHYH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPhoJbLc4K1t4Bi9EllpaSLNJf0F_lCJlp5mBSsxdpsGZB5uqZke2l1_ruf4pIYs1X-_fiow7_lKFjuGSwzlavnq7FTClK2Cpn8xJXcZrhmcUNhPmiXgdWURy_XNOPMe6NOgZIDbil8hFS5ZP3GQIGozZIAqijE8s67iprIxNECY9fLs-GxZQhQLarf2XQxkf7-Xpq88SY_DocuBCQ2sR0JBjeGKZk5jTOvUrOAPQiI7i7RtlUh1U-c4Gz72P16HXTKbFZqHMv20PuR7Wa0UeUT41_JHZQzyNbeHRwERz1pYuEn5HXpRkuOcoXg9xIXzzyjc437nN-8gup1r7rxS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWy-YdvDmTfPc91jz3RywZEHAGEeFtK19A4L1dP6G5n42-dTvWKoakGPEfB2HP2XYbbFPOBcL7BHGCGHzSDEGkP0bXd7K05YQnVHDDCFdcTTnVBgbuf0cwX0bEor2hpW-Oak_SogwLlJjSIJm3id9OJOHBaBuholZe7AvvNskm-hk6ILF9Xl-alpVLU636Ze_xCOfMS5IVe7Tee_iQ8qN8nWxwYgvTU0nRN4MCk5YUvbQnozNCEuIZzFizPcOE9F6gWwDyeSF9fXXxfkL4U5TdHU0qJ1kjWB1byzN2fmtMUEJK08hmTnfiWCS021_r9wTmaAnGr0JLrFIwQuTnUlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbj4JoSxJJj4U9Og02u9FtfN7V1pRXQyTq-74lPSbpUEhEqYN2DY9t7oSXXZnrG9IXZ6QW9dp8OdTfBwebdTChWi4aUjcgRVqQwKeSEVN3-tN_qWHCZYS3KUT_atKxp4NGW2t_9OjsrihALlZhhdSHLmZhOBJrXI6lInL8-9mrkCxsWkqNt7umH14ziEU6PJcwihC9awz5YoTK93d9I4ObkEkGp7HpR-Ce2CnD17UQJ2QvBS4zBWPf4PeOWK8hQLLQUnPfZru39B5lIkY__wTveThwC1kCITySLpN-z_ucElM5SZDIBgFc81yN1RJwj283QADTGHvTS5QYHdQva5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj82N7KtlFGFduJq2Ikg7ALvMmj69AyzO7QU2p14DKJ9zOaDim8xhxwx5r7zYmmAVRhVT_-HzoE9ydegElkhc2XWMf8HahiAGcPXypCC9nO8sIBwiaQ45UhzBeXsOdwXwHBM_7omYPZYNVi3REvIOsX5nnX6qaDf0gcwv4gtIu7wLLzUSCLdNKmrX6sW3WjGPB3zygZJ7aolm1cL-yJCpkFv-TNiA2kpa33mgoAJlWGvBMGmBeg4iv_WMPYjH_vKIH1a2YMR428KxHzesvOM2nZn1iPOlyJHlPodPEpxEDVSfAYHqS7Gd8MHpOKZictasj66wG1wX1IwuqfFoh_V2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj-N1uEIGS0AjGLav2io6ZRTIyALNs5Ly5WC2VvROcQsgmpNDKhsdF6MRezPIxQk97ID_-5CltxAjJechTXi-HXbLDvJNNnLs6U4X_Bn_9_pa1t6soyxKeD6BMLlIMStLIHYVvFzj5ekZT7uuWcjDPQX2pkh2RbZZfL6gJVdyqf0gh_tQ4rhCSHW6UYqzfIdZLb8oVUBnUcnz_AeshY9sBGCn0u_mQCvdKQ-wLlMxY6KqkQO-Xu9aAkiKMQpx3AUIOqVJtUp-4aHplnVUPzT03MfE4YhXEaigWixe2w2nvgDW2avNL1VeG7f_1mnqWEUelypRV_YQD_JM-nxH4a80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgGm4pEFXjGJyaVehHAsiBvvY58B-s1hfT9YfWYNRy3NBOIFbKVTHrZsj3U00geY2bV_dxyTEfhdxaldImZWFFBBTim5QhYLF8ARxIYUGHluvS9eZ_SyD4O8AjkSLXdJCIf_xiLhd-cktmVDsrZePPJXU-mT9_X36VZBRTgc-S3GtEEpH2B2oYpm7Qu_T0HaH4tcU4yUUllswEZWMgM6P7QjktFLalrw0DntnvIFHSdSQLYhCLuQIyxXBTj8CGkTAY4QWIpve1L0ue3JK828exTHga8KwoqgilehovUdhkpx_Mkh3j2-ed9xLg9HFWP5SvkgWOG65HFyO9FPbOtH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERNgPgdxVDOc9ew31SPNgUqvB7PArcWT-dN1MzrVPnpiyyM44aJx8WbH-LkG3_jhxyyFsPXSFwHxk5pHsvyK0zBcg73Sv0s6KUJTgvCaUVhuPri8TuX9tWYX_OoXrLU6_2P4-6QugnnRLxG8Fw_R0Jwm8LiTpcDF06BQ5MYTmxmZ2PHU4UGMbLeWJgv6YLoKSej_9i3kh08vM5cGDPAw7o8EQe76LMQqnge2TdH8IcrcZIumR3v67z5QNNgY_TzECXTqZhV-ZUlbj5WJJvATF75PJcOMZ02EeCJK-uYr3xMrpWZSrwkoDYCDG2TnEFSWisXHhbBVyb7dSUqQaOJv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCp2ywMX7zrPRAZP43oSCgX9yfhtgXLXJ1mZ6frB4sszk3gy4IHsLRNaWEiep0kwUoHU89kEz3DQ2xn5zxII4SKoVVOUQLC2q0I6MmZENwd6q8DcHYgbfGv3c4nupnPo4EHQ9aLlnFfl497SW-7JX1THosCrCEhdREk4bgv2V2QuV7L7KfaFxydTlM1mQf_fg22QBUlR5c4z6llR9sOOaXzVLEdjtCAuu2OgtaPidTEMYkZpXaOg-zsokzHTL-scaaGzll0qvPIdD3CdceIJQJS7EoYzxB_dMM7HDe42AAb7T_HPztScs3bK5dBq-XhX-gKr-OF4mM8G8gv3z8CcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3BU4ce7ENJIDS7n5CuQ19UvScgCnvr3RCDa4jBxSYYsg2Zr9Po7MkehTRoFDW3wV95UcjoJ-MYoCyKgmROB4jf7nLV6SW57tLHO-WPKrV5_Fs5RaxdO6trGbUbw2e52ivB9ZPkZIf9OgVF0R7JVwoNIiMKd5E5RwsjVMmlRYD-Nqlnj0uSZfD7aTml5TWXLdElHb3dFS39mATg89TGbN8KQEsZGUbTXq9I5XNaGm6HczFSfIKADWIJg3wp1zZtqebgaQ2FAI_SmTBtC8g5zIj5nwNHQmEBl0lmA6m_32dIVsox4hKWmHZm-KPf1o7K5JGF7CqbvctP0nHGF44MD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNWX8DMgiB6HVPpUBucP_M2bG7C7X3bv9NFIldgLIqqzpCN3ok5ODButtkRscQSLJtsm77lTfGKxge-gIlpOYcGetQDRRrTCMAeXga_V2IYbaPdlSEkHdUa_gvJUfchzrJeRnVxoUanJBM3FqwFeGKwZqy1PDDHPo-EGCe2DltYRE--KWGI9nBCTv5eihiGY5p8C5KOVdcO_926EV5dmJKQ-dNg9jDjwTLSn80IBKykWZEHnytWQYITT7jfffmlr7yh_txD0OJGO-150HP8cXxB0iLcfEvIhJ9UMKsLD5q9epNcuQUYW3diqd2PLh_T8K5LX-wWA4bJq5gofToskAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmsQb83asXGLQxOn7_zvrKByF92W2bjFRhLKrJCR3kHFcmVTnFTksucT3euhtK2rdRMZJVAE1ac7T09dh5h_2f-SIWZq5jw7T45rUxg8wmYtSRDIeOmijTkvc0iAKES_bTddYWlFUADoZTkyh54DiLmd1IF37ID2K646fcA457YfPnut7E4tg1hX4wFsvcfIv1cpAIJNqcYQ2vUmxGUUP4vM0rSnVyQJ4C_z5u7URYyxQmToFc8BXuvXS6QbdSp2ePEUViqYNNaXIB8QpEPKBwyh5cbp41ItwZk-ziERUTdCucj9FjuOsKLzfUufBRH7dpolptATiIKDEuzfeFXCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVDgQuOiRna9ncHCXXoS5wbois57tbjgEEPZgyHCyTobgRNmtIHDyc2KhR8ddULu4QifNtakZwxkO-cvqpXLGKh06EuAoqs6ckZLeYScpMrDxixZoiTH6iINDI44RjhU-BONdmnhFkwbXtj6D4_stfkY986-Q3CPTKMI-FWpGdL-h5jMMPnwWnA0_waNxeLtzRjz0Nhrq48KuVUl3TzHO5wBWUMF_pHnOLdC62RiZGeIuQz42hNczputpzV-K6nawrdLGfrsTq6D6i7b0LFEzml-4bXO79jTfN65z0ou4id32BKeP-obbpl13FiOSBUFPi1080YDH6UnjlEteSedRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7xKvK8gwRGsFy59cbVCWWLMxeFEwzoUbBD6DgfRHhPYMpoc4Nk_zP0K3M3w9ln5YklpQWfv0uqvDqF6bRdnukJ1-5W-O2JPrAUWuF-a_Hhu9uwD3qrbJI4qBBnwjdNp9nw1CJl8SwL8B61ml7zfleAB-tkeqUNw810yN23YOpPIw7Q_qXH-6f7ADpqrkUcsSmmMOWwsLH__l74z3ajvKLVVDq47SUAItg5udmhyEp1eVVh6W0KRpDwzLx8HZf2gmsceUVc7QbkKSovCVrlnei5fTBN1qMC2Q_VzrSRQNFrm6KKfP_9nhkO81Z0wfEcrpVUREt2-GYZnLwVv02pNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJV9vjhB_WUL76gK9Xj5BFdWr3B4U2hPptgOK8MLovQMjyKHtup08TOB7u81wsuzQUTrnmYHwLe1J7Ix8BPGcmekM1XEZUXAEGoAktK6ooa8mtwkIYZkVvAe-X3XdPWsRk_mwmqBg0F6MC3DzvJMH-an2gGN0lTF-Eu2Z17Q27Zhy5GzjptMBaH2gJwuJwEnucKPxZRYW_Z9sGswwayH8sD8Hv7AS4xG4CpXpHaBE5lT47haWJ7MQwHhNeWEGnZaa6Zfm8V5lP0XQfnQJZlJwDsqp8lxdcjE_R6U3sAqZB8F5Mb2lq7-5NS6RUbVBeuIJkpyEUQzqgxjRRpyvRpP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqJqOb3Q_qOuN3-ZLUviDMgFRZrVpsArrwQhjjDfjEPt8yC-o-LhEptPCGbU0J_EAiVNHp2_SvvqKvD2BzbyQ4yjzxPkUpYocED2h_HJV5ZGFPz--92ubok-h6_IOUVqBPRRVWUdDxnUm_mOxLMIDQY1p2H8DlwF2Yzct8utEhVDojXrst5SKKLPFplvMQRBHxpKHJCfOR7hE5Ryd11_udBbDJX6v719p-L0nm8_WlajXo8zccEVuk2une2WmlzFlb7rP5Qybnq2YjU9SHGFc5XDo-wOipwH44bfWI5jX2pvCdB7jWgPZUMh_lUFUofOWhcKK-DOgs8Lxdo0Pvd7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLtJGlMjil1A031bmZvhSrwRPSltoQiIo153zUM9cIrl0ytYGt-qrtqM7VewSNnX9310Uh0d8HhP4HMbNb8P_LvH_wP46T7wsw917nfEcKsUi3VEmUQl4b_NE5LaApct3MPuuxbyawTvAs3-2QgvTlOZ6GOp9jZ_TbXKDZd8AEjzIwv0wRPvDyrIXVZOBJT3-hfmTmNCJ9qU9k7WVVfuzIfLYQHY-fyp05UI17WBRMANwsjZbYbQAXqwWQEUqiN12gL9VmPsL6gG0WcFBCjKuNBJmHbdw5w1RCvziR8NrR9p-Is7Yn06dsMjInEvUAgR753V3J1Ij1AZSHyZKuMN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5lbHCpjb3qWGGdz5VahU8wHXBe45ZW2Br8LCZs_ZeHV9JStgVdWHYk9k6noej1eUs-nMjgvXS_LrQGLvGrokjFUPxhwhJ2qV1yiqJIoDBsJbZooIUZGQyF6mJcqUBl_bgWawYXj9IBeo9cs0dSHe2H1oBnPnk2Ctl9J7DjrMzYJzmpmrkdoKMGNzpgWnMjmCo7fg64EVtUNs2SSLzctlHPLH9qn5q7ABLz5J5oT5KvUOhW6g1RRItjRCAYc8PRjwLgKCQU_n-dP23DAtRuAv9ZjFViV4TI29YhIZSNVwCRZLlXFSsWeoh9Gxjmh5L_-lUbqF-L9YzUL4mjeeFEMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=hQtsiFzIzR1ustPH1vJ6f6ugM8sLMJzYNHcEvVcsoxONzfbMiRzbNhxnQpwAUM834_7eLkREvjCog5R6d1Le6a-zOi9DpX_aP4iwhILv-SIRjwCgxwclPK-NFTVK0eLbmAZqStfikFcmR-VTUGgiDSFJ9WVVeA5AQJp4qBNt7ShdrLe7fLj6sdS8kKrA8mdlpsvnOO3Y8rRdWq8-pdHC41UmtvHfYYpieDUBd-7k_r9TMG9HpyEBsFC_aLjuMpN1G84KC5F_HAzAQoRcYgi9hEX8PpPQo3BppDcTrAQm36hUmCtb_XXsIkZsGhf4Nfoad4Ytf5f0FAT86NYqoh2tAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=hQtsiFzIzR1ustPH1vJ6f6ugM8sLMJzYNHcEvVcsoxONzfbMiRzbNhxnQpwAUM834_7eLkREvjCog5R6d1Le6a-zOi9DpX_aP4iwhILv-SIRjwCgxwclPK-NFTVK0eLbmAZqStfikFcmR-VTUGgiDSFJ9WVVeA5AQJp4qBNt7ShdrLe7fLj6sdS8kKrA8mdlpsvnOO3Y8rRdWq8-pdHC41UmtvHfYYpieDUBd-7k_r9TMG9HpyEBsFC_aLjuMpN1G84KC5F_HAzAQoRcYgi9hEX8PpPQo3BppDcTrAQm36hUmCtb_XXsIkZsGhf4Nfoad4Ytf5f0FAT86NYqoh2tAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj2NN8cIXQs9NjHhKhlfV7tTh_oK7aSCvxjsOJxiZIecixmXO9gZJFf6EmN7djp6qU-MN60F7c66NwVuwQreQAkXIFSfRkEiV208kuJTqyh6oUHWUSyk7Gw9wxcDkUMefbhh_DF_l6RldtdtkIO1I4-kj1bRxEdLH4R8N1ne2MfwDDfKWj8h7ALuKiZW2JJuTU_8G9dMuyQvKWQErgTBTTrgBhbxdnXn10DSZokVhNcumIRmENb3QlmS0JcIefxeiibAn7svGYnKd6h4LYMR_oLOYmgLD3odrLA95h2nwpNKv9zmVlPNd1rchFZ6Cnql-4vUiVK9zVPk0DrayHv6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdDx76XLRvwEGjXwmXR0VDw8qtGmx_4ly8IPlZ-aSUw55xCpbA89UW9g8YN_FeWFb0uqbjHkB5fYUQekqbq1dOlHxj2CAHcWImeeQo3s9ZP7Jju9K7mCzhMNbPLyC2NAg3QQxAAZTxMhCl0D04TOTV0CDnrrs1vmeiiSVo1xYwlv19gWxQ6zpFcNFxi_Aru9roZENpeLt4zR98tlR69P0LEaudTtAFR99lxAzMJqooLEeIF5VZ3z9xD6Pv5Zrrs8KsE5eLXDQxwVcqUL5WiS1DnfqnG86Vq2j2CEgE3aNbzuBEbDq7o3rYQY2CFLIdZLDag7V4XKa-d-l4m8RNb2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA1jqvKS_AwEhJVarTPOG1IH0RK2-bT074XP52es8Fc2FgzA20F-eSYzQg3vut_mMcx8WxVe_fEwhsDxnsihOYGdW5hli4bm-tFUKaCSuBpGku4YiawKQ3ZkVD8SK6R-UqUAftt-c7vl5mS8NSRzsHfDfAq95O-rD0VwxYe1UXhLbGXsmGn8YEdwxtKua3es8QN1rh8YO7xsgIAuQiPwO5Us66mLohrK7Led6LaHyBjB3-IIF39bSebZbpFeobzMZftQVQmP9nTvFLnksjoe-vsyayutjNtZj9Sp8RIYZtIGNLh-rGe9hAR_ExeDnT7KVmhGvfWcQLN9zPQ_c6dLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP0M9tC8V_1lyrTD6z6J9Fz5NDCugHMcL2rEYSZrAtWVkoa-p2JRMrK1zKDQnT3SkmHhSaVvHz4chaskK4INhAMDCjuNcMeaCVfnTq4gMFSXMtr3LI5o2vUnQXLllOQILCpMCQ9-MZrYHYAjmCFxNQTZ-kgxqF9ZTzUeN5wq9rkmTvhcGnZAcZHAUCoBX7A9HRiWsK9u65c4XBzxRKE5Qj6JV2rJUa2E0B4jUxlyTH51yWqgz5X7KeMt7--9fugSwKHclrrQd3a51O8MJE3UqUUgu_KZm_ck3CN2acmYayAMRY9tZTjzXDfpsWP7A4tMpD_novIeyFni8luI5ZDaRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30604" target="_blank">📅 12:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDQRLxw8du6ZImIWI0DQr8_apB9d8GYHCTEuhhSWa94qdfucX-pOZt--v6Ep4ZQ9HBMUGhs-FjQ7BmDAlWPvu8uvQX4LZ_Ub3aAJn03KZhPt4q8i3wflhbZHFOlplfs7xeCQwXrwnCLU4uAFrz0SPPibtFsW9BaY70LdYqZMTfQiLylFjkEbnRolZMUmm4HQ3OqwzLr53CFTfTKqbQ1yMYQlLe_b_NVSbZiK7k6xVcyrVRfCmhyS81NA_mXquujbjCU-Df_To9Wt6yLR3P9L3Lqkns6PZoyEpnCteNwT0pwMTxVbyfCVIhZfoyVIGfZ2yK2l2Lr6Mbacr3xAEVwD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ2bmV0II0tafxN8Yzzg4eDFPCW_NRre8WL1pWUSVuNV6pAiA_SgxbcB1bR1jsWT5W39iX2gA4de7b2McCx3FVVu14oirCWHAHP9OjWV-6UaJOu4eufboFLEYhADtLmo3XCfGc08Fk5PECSl5oUyXHgozgw28qRpVVgCkFYWPxy915P5PZRkCM-WsPAFOQmOX794jGoffAODoUoQHOHgIUxwPXe46Gr7hMFqBMRnDFPnggO0HjG_gaN8YhkelA5-KPgEGNRMBPJw_BpvQ3U92xksnV83BnjW-6D8HGJjyDkRJ1XDqHWl5tu9mJp0FvaEcmkK_F8XUZlIzs_mo2q6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9ywPRccMBQS0z0Ui0ojgTNCNUZWBeB7Zj0LgTLiUvp4kk34jURrjlcHIqY03O9sRcEOUgKXS3qXaG3KPj_3TKtHOYU2pmrz9VvsSWSCdqqRQZITEbf94CZWKXANvzdlNTot3v-XYEluaIYc7z9eJT2LAjnP47Ap3ToYpiYMw3HVJJ1CmvoAz_JnS8KtuNX-ZPQSXtDjNyhBe_AwHhb6j5vZTjGQo3G4_dBoEEiVT0QL-CCxGyYY04ydFiLFpkq_4NApXk-3oJosZXkH4Tr8mzU7R_WNu5LhLdQ8LbT6lrha8PN1O28TE4b7XA7ohPnkYo9TGmqo__nxhem-52qyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkQ021lkg3ALzuygjsvXUYFRZ-SYpQdTN29kVQm9hLUc4OQxcrmCr6CNtt2xGcVhSUwKS8IVPeIs6xIjjiwN6HocWLRGCVn1DC6a3NVhLA-lizXbxBK_lUZJFjwrpuk2k0sWTYb0TiEW63_DKI2MAMYPPBQp4BY2nC2EibIKYs4OoEjnZNvSTl1vt4Tv89GwCoZG48-_lKIzeetc2XI0Joh5hzsh51cbaagIbOUFR7ws5VqHrWJbbgBj3poAe4s3fGgtZJnKkUM4rl7plMUBRoxkjuUOf4S1ledHVkx_S1xg1cEQSeTpxWc4YvL0_R1-JjdO-xxtWzVeSjphObwptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAVob6lUn_oMf4q_2OEdCaTTUGxI3D-w3xkFQu2hcysc-ZVIzzP7R2hdg6v9tuUIzxrg0OqBwPkoDUgtOjULT-_ykq4bKlWl_LklK77X8XcoK9XTmjYNclbftlZ1Quu_PDoRo-TPJ8nhkYKbOK6R3rPXOGLwaafbqgTbqZk_ZAVomoqXf1wRDSw3bdWeh2A2vqY73hg1azWPcybG0rMoHYJiqlVyic25g3khCnvz2oqlut8E0ThOxJYZ60Eodi82E5BJhm9PcdQZitkZlUncHtsHgidKFioNNtxydeCGtHcn9Q6NKRdKpme2SsadKBWV1JBmrzpzi8fs3b7MDjLCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
r6
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjhpvwWmKNhE21g04-eFfe4B6xS-T5AQiLtcyEj1uKSyuCpgnQmIrcuchDrRiTAmmFJxpBUPIAFFay5PFs57b2OpBotXFMy3lJkaUpHJgF7OBRXy_AkbetObzavGSsbfsJtpoWzcZ6aOIp4drssZeK2tko0OX1fnnshSWfh1PrvAFFqhYYT6aAoLgYsFf-sgspXFFEFpHhQ7mGSKU8_pLVJYpVQwAc-7rYJVkSfY72CdoHbNk6_0MQfaEkrJCgp_KSYQzBH4G6XrkmQddS13w4wEIzjcarffqUjrZxS7dU23HVaBm_MBBg6p0srZjM7Rl5kawSuUIseGTjnAxLIBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBQ2lknjxRq8LIH61ZMdifQyeTFFxk3pfLZm7gzX2i-jZDERus2ltytF1DzUfzAelMxXk3G0s3dwmYUspUgBLt6mt7eBLQnX_c6pDU184X9aVbta2Sp0id8KKIASzwJoLQEEI_MGUpDUQ9nUJ2o1B6ZtUFZdlXNfzSiUYxbHPTgKNkcweVvpEPqMnMijxNDLdWF6EHOB0IB14NoFCnFbdlHpLqmQasLFZjUu_V02I9c5LXAP8wloWVZlaqr39e8BbiK3mtDMKHbdCh1qvVklKtFy98zLazIMzbuYpoDJocvjgHnohzsbQqRQtPBBUNUwk4F6i8cyq71J8WofoxQkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-IiaaxxAQ0SjhvH4pmtxGti5dyZoxdfLLlEHlasjSVt4EPwKis6W6qIj7TihQ-1bbe5PMSLAK4qSzF_yfsC1atZs1WL8-j0c1mMj9M-lgQFTkOQZqp0x9u_cZMVR8K0SiS9vR56-VNB706CatgO5b5IEcJBej4H3y7d19yJvTh-RH6oWIWnKpn23yJ2XOFpPucMDf2QcPDM2tkX2T1ffVoxae2Pn3PuolkpxSsSnpsEPuAv_nMYvRZhQpOaeot2PoxFW7xJAQY3oWiJFM7HHeq-mlFGTQkKHSk-OLLlCC8FmpL5HHv1xhWc6WLK92tMsNJwtQeE1Lx8WZeeVicJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=nX2XgNf78yf_r2SRBrNoUo7ryaUqSnFSXTmu8xVHQ7LT4O3NwvDJFTrUfPTg-WLzKv8qRnkNkkLW2C5iByDs89kVjsZImoi32_YFEq8O9dSTo2kxOhRoatV8vG2miPMyDX1ljpHV1Z7jtjG5l29U9GI492yb8ZD82kg78ivwj1mhb5OYnbUaPvij4bguzb5aKnLaneK8Z0kfu56x2WTVPAbImXdtSKpkr2gGM9ss5Cr37wO7_AJMz_H2C3J7tiCsMCTasNgQZvXvVdCYHCPHkpvD-jb7Dco568j0s7UZdvv4201nU5J6Un1hIFFTA7ew47Xh9cACq5aA2tPqkR4lhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=nX2XgNf78yf_r2SRBrNoUo7ryaUqSnFSXTmu8xVHQ7LT4O3NwvDJFTrUfPTg-WLzKv8qRnkNkkLW2C5iByDs89kVjsZImoi32_YFEq8O9dSTo2kxOhRoatV8vG2miPMyDX1ljpHV1Z7jtjG5l29U9GI492yb8ZD82kg78ivwj1mhb5OYnbUaPvij4bguzb5aKnLaneK8Z0kfu56x2WTVPAbImXdtSKpkr2gGM9ss5Cr37wO7_AJMz_H2C3J7tiCsMCTasNgQZvXvVdCYHCPHkpvD-jb7Dco568j0s7UZdvv4201nU5J6Un1hIFFTA7ew47Xh9cACq5aA2tPqkR4lhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelLv3jM0LyKytkRJaM7ozY1og5_FqF-6ORH63j8OdTI4w6ykGo_7H2FsB--nSjCpYhDgOSPaWgBjE-5S9E86oO6O4KJqpIVycsSZkroA4wQvVB8KPLKbnw1uqcQVmdMFS8AziT0bpaKEyG__Q3Bdj9Ah7txBBk5Rp9zOLiZyhdjkcdtRJ_N-cmgjfgI6cZSfSLv9Z1rFLzytPrfO78x-lthDBlOaRsC8veytQDsn6BAxJYLHdESvjLVdhxG6o_1UM7LCg1u3E6ObQRuKo8M4A-7xoBd9YQKaLRgkbgBA_S9bcITPt_mwM-XCHC8AFZKS16qQO7oK_wb8ntcQ5PcDYig4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelLv3jM0LyKytkRJaM7ozY1og5_FqF-6ORH63j8OdTI4w6ykGo_7H2FsB--nSjCpYhDgOSPaWgBjE-5S9E86oO6O4KJqpIVycsSZkroA4wQvVB8KPLKbnw1uqcQVmdMFS8AziT0bpaKEyG__Q3Bdj9Ah7txBBk5Rp9zOLiZyhdjkcdtRJ_N-cmgjfgI6cZSfSLv9Z1rFLzytPrfO78x-lthDBlOaRsC8veytQDsn6BAxJYLHdESvjLVdhxG6o_1UM7LCg1u3E6ObQRuKo8M4A-7xoBd9YQKaLRgkbgBA_S9bcITPt_mwM-XCHC8AFZKS16qQO7oK_wb8ntcQ5PcDYig4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30592" target="_blank">📅 09:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=a5lBIii3U1XKuS9I4Y9wgQ1xsdvFQMeLpIbZ8naeW91MJ73lfDo4RsfgrqwuzB8Dy6tUltdH6IFdiuDqHcbb136XH1aQYLf9Glra0O9UUoe3t1g_DCbhICLw2WVW5_jEPHGxgmu71QGTmTQGUPgtPR7eJ10nT_pH9NU_KR8sjVWBj6OBgjOVvlY-A9hQykD-uLpthkgzEKTb5vy0YyVuEnt74HP2W7Xq7u5BzSQOFWGMU8DdkKdaYA3B3xtHSEWkvGM1pN0Asz-Qq3lBKH9n5GUIRJbYlgt_IEM9y8GsSDoG9zR7VuWA_pXCNdbyKyPjw0Aiwzv4ZBeLfZbqgz3sEYGfLY10gjI9TaPYHsYo9um369X-7wCixTBQH2K04QlqhuWWdEmqmyguvyr_L9K8iU21_OVNO1cf6ADilI2Es4IVhbsZ-k7Awhd4NpQlg5rSALMIyiqM1l2KHjsd3qFT67Kz9Ifuzo4ADhokIH4tnwG4hwOy18e8x352trbjxQepvQaDE43Y50oowpU61BG2fozBSJ45Zdbj2x2k40JI-OqDvxsBNbA_UWQdN2MtnNZ49e5KIuiaoG6wVO7H4WxhBYfvMSBNuyNcN6uScfDV9XlVB4XsaZT9SL9lXmexmbdnoLH5MsET3DVz3etF1_DrUB5CUdMagVORQSZ6c-z9T9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=a5lBIii3U1XKuS9I4Y9wgQ1xsdvFQMeLpIbZ8naeW91MJ73lfDo4RsfgrqwuzB8Dy6tUltdH6IFdiuDqHcbb136XH1aQYLf9Glra0O9UUoe3t1g_DCbhICLw2WVW5_jEPHGxgmu71QGTmTQGUPgtPR7eJ10nT_pH9NU_KR8sjVWBj6OBgjOVvlY-A9hQykD-uLpthkgzEKTb5vy0YyVuEnt74HP2W7Xq7u5BzSQOFWGMU8DdkKdaYA3B3xtHSEWkvGM1pN0Asz-Qq3lBKH9n5GUIRJbYlgt_IEM9y8GsSDoG9zR7VuWA_pXCNdbyKyPjw0Aiwzv4ZBeLfZbqgz3sEYGfLY10gjI9TaPYHsYo9um369X-7wCixTBQH2K04QlqhuWWdEmqmyguvyr_L9K8iU21_OVNO1cf6ADilI2Es4IVhbsZ-k7Awhd4NpQlg5rSALMIyiqM1l2KHjsd3qFT67Kz9Ifuzo4ADhokIH4tnwG4hwOy18e8x352trbjxQepvQaDE43Y50oowpU61BG2fozBSJ45Zdbj2x2k40JI-OqDvxsBNbA_UWQdN2MtnNZ49e5KIuiaoG6wVO7H4WxhBYfvMSBNuyNcN6uScfDV9XlVB4XsaZT9SL9lXmexmbdnoLH5MsET3DVz3etF1_DrUB5CUdMagVORQSZ6c-z9T9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بهترین گلزنان چپ پا در قرن بیست و یکم؛ لیونل مسی فوق‌ستاره‌آرژانتینی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30591" target="_blank">📅 09:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLjhbEa5y321DRcNqdFSn7wqE-t7cIINoaFD_DfV82rIq8QdOtkBM7TkpZzD95Pk3gIoC427G61UjHhHqM2av9H0ovL7MM-3WSPUOvS3e0VZKKihPqOLpeFupUu9_P0THhaiiHw4OnMLPDEPkcU6p91GqdCTvwIKg6T7_DLHdnrGPbUhBXTlDGCDlTYcIMSYO8R5eH99J2k_8NG565XVDJ1cLFr6x93NbBnyta_iX1QbZeZhAM_EaFXxLuIWiLNXijWv8FHy3cxCUpqZNYQm8zx1o-wd1gi9LddQiNm1JoxxdyabnmuJ6wqzrEmf0naBTQdNh0d-5602qdBwvkNE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqapRTaUmfSgPe1a2HwWeRokOAloU8ufyY2hdypIbjJ461ejh1tqCVA3OBhiSxxk4efJ0V3ckKRipg7X6C6xwNKEZXAlGZj8oBSjO_M4ObY0qigQkn_G6boaJr7q9kprNyL26p8ojTfJMMlV9Wcd7pFxs2yujOauD6XmkfCbYwLg8K8r4eQ4hzezMyAUCFf5uQILdi8JCi5burxIzq3kWz80SeOmro_U86LSdbP4KCunzgcYrsSj2oBNIXQ89UUUBUbz4Rc7omdUEg20T5X3Ju5idqh6AC06PEzJ-3L3rL7ExeGBrZ7zxUIz-NuZPRrih3YgrszOZ3KenfJKX-sFcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJI0Y8lfbzArM35M8rw7JmWlKl_VwaJ5BD3yeD-X6sXqWJpzzkyRij6Fry1B7X9bKiCbNbHcuBjnhRmALuLttKqCDKbxBiM9Wilfvhu7x9-rA_kdMw8ab8dRvIzNlbsox5Kv8ds5LYGM6kTmVMgksB-99-WTC9DiMU-CnWbGIRtRdHRRSiQ-6y7YA30qEW8XNQ_15cvysjurujI54DkGguA6cGDnkK2V6wmxjeNITPc7ZwXKiJkXAkeKeTk1ZDIlYXGqHKjF81uUydlnOPDHoA7kCNwYxtYMYY5yUumtgHxThOvGt-xkzPGl_xfIGRZlyYlQ-F5yt_37H5sxv2Ph7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy6gV8ZAc580m4xd5TeRkKwwU6SwH-m8UJmWdVp5FK493D2vlRFbPJU9jyz6arek_lehK1_d--Ej8ATMSBCkHiaxDQP1nxaLQi5HfOSlLqdsZHsbS0mIpZ_4d5jvyu-TRIOo8uxLoQzfoQv5zSINEfvq66DLQ_dCVoVdW0Y_YGoCXoYn0RyQwqMIrpsbqjijl34ialZPeGsaFOCrqDapnhN6mfOxXjpB06KVozjRaKTHdkEOWUgpP8dx8_nB6MALYxHwxAdI_xc-pb0k0C01lIQBaWv1qr3esSOBFcs8zzKw7LmiF1qwCptWjDNl6w3BWEvjikS-zNAlbhIo67iHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzSDoruKshYKOZ7hVb020z_PPuGK-T4PVWXquCq0sUEXF-VZsfNR6ItyH1uGJQf6u8fRuPjkgJFHHRm6q1Ib4CWHgrxKGMM6javfJDj1vc9gKaXEk8KmtX9wj0SC_s-5WMyJRIve5z6T7hRgTtbiNcnOcWoglhqUVmpMR-V1o6tqfSU9VgWQlxEiSU-GMJXuiBMH-iYLK_EF_vYLMZ0-vf8YguUrUHwM1AefIMMFW2sHovaIYjLQNDvzUJFQvedFFHBpDD6z99e4LaNZWPdKyHyZIv_mZuE3eORIdUCXFkgkv089dxVRx9L2U6LuPgLCfIae8BkfFu3J1DeQQMbzuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ_LCfD21M0LUxeyZrDUavEjOxMCmI8vEwa2cPcRksjGCI-1fMpGNZ8IM7ul-swlvDQlWmMub651xIJTIHa6NYs3yp-oN9NXuNfkvpiaCSc5i4sFE49TODHXgQZJvifWiw_lDScB3O8vNDs69s6N5mc5uYahu3ug0LNexO-OZC5oWmd2nCY7TbTkOG3aNgfFlnA6mg6z-ETNR0L4VEp9hUSS39VuTLdsCpWv9Kl2hOUH01xbTbTAl0txYKroGp4N24Re9jPVQWXXpKnuRDLAaI1LK1vRk1CQzVGlQqJpmt19Tt-FLlBkHCyGN6sUz1ichLrAh0F7YTugOKHLGBSy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6OiyXZPVsOsqvhmvX7XmO7c9uUIxPd_oJStaERfBvI3nR1wHU-sjTFOMZdVpr4EpWRgkaa3Qr6u1IofCtYXEOClUczARoL18pGT6wh_rRhL2PitIk-fSZVMpkmMcPWXQ7Pm5-S85UO6HTwkSJwOOECP9nmENG7MXxdGXoPzjHnyMzNf6d70OAkXBG4i8DajVKzY6GHf9caLMiySbfMHPwjRWvjs-WVC7zciOeEQWE3owhRutIKioZKzNgpMLwKl90lKOc71tZma4XW8Geg2WaJYjq2dkui35vAslZ81IaedmdHKw40H1SH5Co6Qhk8MnruKm3jg47-eLSDGPZ_dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCieTEOTfCakBovz5of0rn5PBwJvmnUvEqo3c9hxGEMnJMLYh0Eeg6p8Sbdh0g2dbNPkVU6rAP04fS-HX1-k1Ouk7k0uSxBqjavMkcx7ipZCXNBGRmIui9OCbibB5gTGv0NPjnlkYuavReeMXxUURZad1dQSzcvQO5G3mtp0iILv0TNBfrKG9NzZDZWqGpYWqCeCVh6lggvOColRAd9zi2hQdM4sFJJ-y5zT9QYmOeGOooF8Ar4NGfA0aAbISWXJmrkgq0ibxc0mVbvGM4QEMk_9CU0IvglNf3gA8g_ygEdXcl1JvPhQ6y6UXIElpOzLr_Dzhl4HetpbGEJq92jFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVAQrODGMO8YCOlljQYJm15abVZJKkZbZdyLmPnq9p9eogosVDQqbTQUXBcDq9-RI4b7sbqEJBRFq0gwr0l6p0eFfoT2P76DYrfoypCPz-Ig5K-YavXTia4qmxmXK33CGc2ZSTKWE_9qez5hneVfKmMA2GL_APxbTJRckWT1s5wUXG-sa0eDyLhFhfzSlkIRaU2iT4oamj_0Tu8kXzyPGYtbB5A1lGYATKT85r9pMTwvYkvFPxDigGHGH3LuCMU5AARGqOeoJnP6gF-OeJ_i3eI5KnQ0JUqd8pXZRa-fG9B2n441zJ-LmJstqrRumlWp_-A7A_EpiQiBgLkowjghPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgpZO4rjFpsDRyesC2ahRbBJKRfWYBY3cFdP9209g8_nzlEvW-6IHFSw8GCcNKpuhBYWGPNgvtvhn_tBwC5q-q2aluh0lH4O4zI_LMTvbHhzLZgXb0VYZkKUdNYFTMtgdngzT1JD0C2pn_kWGDrnUUIsTtSp4gcftLQzVifPUQz4FzHqM07MfYlJUbaVZ8PFkXbvwHHY4Fsrq8506zzvsTlWFKJXRLGEdE1PJb-QuRJdSQK0RF1Z_T7_JXI95oylf0t3GecjO5HkxTjr4oJXxIiJT2yssHvgn_WX2w9bEdqBK5ssrN-NzDRyUMprw-c6bB73Kl3cNNppg8Fy5UDe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUB1osuTE9o0ejTSDMTZlX-ZPx_QMw4AXOaeA3ejqd7J6XHtJdnaUykEPd6CgKQrs4kVyTxFiZ4Bsp9XtyvVnwVvptc8nPW9IxKEAfdeTn-bCGS1x2JaAQCYnAmRcR0L3ZtttzpHhgTGaPHVRLEzan9tk2YhXL7SzHIMdValW4GB2PFI2TlF0_PrLvXWI61GLKr0eqEAg7IOt4hz-WET5PgXxhTyQYfZYp7laVDevIlwytDPFG5fr8Xs4YwW_VuliP9hpIC9bPQcbBV16_S-Pe3r7gXy63p1m9RVEK2bm-yd4FIeBUkgiPsEHCen1DQka33FVBKxPGr6P-BYMxXrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKcOeEsX36zgbF_UkfzAV45MY9rC-gDA_088y_bfgt_FEZMnJLB2E3yfp91LRe7TCow-MGCZW2mXXudiPX8D7IhYCds0E2w7IiS0mF3N9gdd3ohEVCYBMtd01UOgQL1XLq28RbAxE1I--awJHo8Kx5MAW5fKjJw-o72kU9VJL0-Jz-sMWQuyA_oUQ8P6q8N1GiPQk4KMCOumPrNvavv6Y7ojPGB1UhZWn2l2wkpSpWI8x60uHXM2yqQ43XX4E8tcAiXHtPmxnjN5gJTQM7WLP8NvEt_gi8b6jH1vkktm080BZfhn83KmsCs2irhxbQqG2RjxqTzuUiU3E6Mm1EgBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ht671nL9Bkx7VX-_nUSyvFc76uvvKObL3IiE0aTF8xMtFCxpul7v--2TGfeUAyvCFuAPsWWhOAxlRVjMj85oCDN4TMUAxkaSvLsttlQYAGR0IzaGRyngechQjkQe81oUa6JMWLG4wuho3LuttZS6VZdOK4q7TLTlS6nq0O5pN04BMOZACOuKS9aBNMQxE_FbPn_QTf7JuRotEWPBtogw--1RgAKcjtjq6HxeKRqc_n2RmknKz7pxcLWSz1-hXE7oUiUeO4th57eFP3jZNyMBAdWnh_P5BTgXZdr1fIPhKY8Ky6OP3khmhbuLUp845Vh6afmRCh-Z9IWZLrYRSh-e4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyCkkh4SOWErFDf3GUioGxfxOKIlFLkCIgBJumpuOOeu-aLNxNdmmQab-FF4xF6hpZUU8IKdfiZ6r-JnoFLgx3JhkHuyaa9ZDrl4JgxSkZA9eG1pt5aNnqbFyn0Mr49ExvYd-Ef5zhjdVeLxq7gGi72behYaaSSFJCq-QGsdYCwLxDWxnLuKit0Wgc_mDTLhpVCijc6YMfRMh0LC-EhfErucrOMT693JIhP9QVHCcRh_QrYzPHHEC2K_SaLlTT3aUeo_n_CTvVGMZKiGmn20K9f39QZcVE2oT3SFBLOdVtCm6EwhtgCRXZmcotuVMFvCG6Aug0JEgozz3AEp9u0Chg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4_arnpABIWPHz76Wh0-yPVa6tgk-c_6hUdZPc5RSA3-GhEbby50sVka5HNhebVLqQ2KM3tm4EZgB7QaMMm588zFAgQM-PxyyIADwC_-zAZe5WyntB5FotAvVR4G2fYVB46qozCsstVaxXMI5pqMCTgz5dkHRNggbw88Oo5vSkWdombiXHbq1qlaju6VPwaD0B7eXplvJigf6Og_IOWjJTm_hETCf_J6OOPU9KHlW2abCip7i8tRbsdAOIBODYcoIv1QssN_WNS6KAfbvEbn-uJwMhypTmMWsPhWrYUkUnMsL3oswWj3pUPhH8B-8_D0J1npzmP00SwCgC0fCZmk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=IG3m3uTde7SJegReo5UZU8Yt7c3pqLlgIHHCmebVEK7a83-fQF1vtzhxhxe0eAlYmYscyGu7N384AUQuUB9v_cDthuwTDHfmNOt7DHTEZFy4SX739MsK6MZIWeXYC0YUobWO_rpmDiF3Tf71krf1I4DBVWGT0sO8EgdAJdhVritFBDkq-N-7uhrWatmblZ8AGkz5mtE8sZ-rIzeO31lZK860K9H0REpdSAZxoJe8_36pG4i9RUqC9X6xwz8O_QLh-r_KPueeOn9md2zQbXtWAGYlRM4igtXP5CLUtXHPZidJyW8EUTnV53eV9Eq7YrpMqCb5GdYK9y_hMxOQmSW1RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=IG3m3uTde7SJegReo5UZU8Yt7c3pqLlgIHHCmebVEK7a83-fQF1vtzhxhxe0eAlYmYscyGu7N384AUQuUB9v_cDthuwTDHfmNOt7DHTEZFy4SX739MsK6MZIWeXYC0YUobWO_rpmDiF3Tf71krf1I4DBVWGT0sO8EgdAJdhVritFBDkq-N-7uhrWatmblZ8AGkz5mtE8sZ-rIzeO31lZK860K9H0REpdSAZxoJe8_36pG4i9RUqC9X6xwz8O_QLh-r_KPueeOn9md2zQbXtWAGYlRM4igtXP5CLUtXHPZidJyW8EUTnV53eV9Eq7YrpMqCb5GdYK9y_hMxOQmSW1RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DveWfqVygsYNy3o-PM2ZRXotfysuRKZHfVqtp8fFuLsu4Gct6nDstC-EKCDimX1uxclz1iKq_QdYw1ZRBPkrKR8PpbGkinl4e7mqKmynQm0OhFXXBI0eMRukTgtkXx7T5GGvf7zelMhNUq4Pi4LdQku3dY4d7hmUtwv-C0IgnT3C7phBw44YNnoVzWvi-hH5XeC2W7kZOTSNcUJXFmgANVCkigCnqJSGeTuz76RhvBMUZtQoSplDYiQJ13ZFvOfHUuHy-fcWhoNKAA51NhL_xHtL93j_lcquUYAe9csdUiDCZqHg_oFAT9s4AZGokyTSJCac-mNUlk6W7CBi2px7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
CHELSEA. MORE THAN A CLUB.
🏘
اینجا جاییه که عاشقای چلسی مثل خونه توش زندگی میکنن.
💭
آخرین اخبار، قبل از همه
🔼
نقل‌وانتقالات و حواشی داغ
🥅
پوشش کامل بازی‌ها
📊
آمار و تحلیل‌های جذاب
از استفوردبریج تا قلب تو؛
🤔
Welcome to the Blue Side.
❤️
👇
@CFC365
💙
همیشه یادت باشه آبی برای ما فقط یک رنگ نیست، یک هویته.</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30571" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeMW6WIQ-cWKSwjB03voAzh9cOvp9PiXSfF13LcnrKsG80aiskc9vqBAAOhVMrlUixaRgaUXkxOMwWlJiYw345CNM-tcur5PJonLt4LATOdEBychcp37Qi8PLyhyDgvDoN5_Dn3J8lbuGLb2KOUAZ1-QKlWJQvjy1IhAlmEyF1uSKL0y9obxAMVn5_GAygSUIOMEy-PTpex2WJknjpXJA8eqCdxbgofZGW0MGzI1yfjo0ps3Eh_hnIn0lzAjUgYHQOU2dsaE3gu06TcyAjqBkojJKNfns57uFOhiwfwWi3ZcmrMndMympUqEvSDx1PwKTnR6fjD6OH9nvaGYuQ4fCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30570" target="_blank">📅 21:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxbaLdSWehhcqkdw6vdhC2YdBFI69zIHOACUOrCVbTW0P3fz52ynH6QRo7IcY4tRvYKC45MWNT_GaP4aPA1dAV_OLvTobWP3_UIJowHhBR1bqwrhOloeMeGDN20nunSVzHHVVNF4nbjBJDL0K1ViH-xRWAeubn48cAYSdAPY-f1wTHjc-DzRl4KPBAy5wK-ELHvVtEs8p2tvRVVrKUVS8goDCbFMooCsakJy9of1yVbmm2ZhjUhaZKbkAxsjAgEQB867RrX3HJBsRtHbS54FpkSKu9TBhOmHwpON7Am-eE_Qo5DmSjqlKdCcFms5aMMjdIDhwP3eg_WVihTYE3n8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان: بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30569" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efH4DZXc29m8cunVJVYU02BlNLxjCCY_EhZgwwM93F3vzsiM66reqfSqTkHEXVloujqcFU37laHjuzE_5afHljDJJFiA9M1YsEy5d2Yd_3ogFbYiFKsNpY0qZcfkx65opKClBk1wKZr4F83y5nmFBwEE_YYixi-0QzplzdzxePYziUdRxFUyXGimArrZ8J3LL0IOXeGLO8r8cZ5MqyCKZBgcYRqOYCKAy2x7Q14nYTNHm9Ki5rCKwHKAvjnLSg4XJNF8bE-qhh4zjY3nFkouKSzwRSGsT99tzXgnPHlLa5OYsrIYj6eh33tj6aWJgRRwh6bXrRjMdjwW3iKuqrRPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktMX77EPY7MmpJr-fOUzcOACc_9QOxWAOOvyo_NbXpP4hf0m5Zzyi9hVl6MJVGn2A3WAfyoGPZKcm-XgruNsMl4YcRzCFh-VsjRn_oDa1chEcOd3-cxmUP3jMYmp9ox2wvI-gX6DPHHRAO26Mqor1eQXhezbeGr1-eM-LDlnmUy2mlQfuUxmhLVgueA7SDv6YcdLLQkw-TClaqcCTEPVLvNFLpnsX4PpRuYWx2t4CHVMx66evGRiZozUEKKaK1RsFxxTWgO2Q3jmyhAJAh4lGJyRUbef1KrTbznr2kBRwjKvf8oUSikvcQx6D1tWW406YgRKS1iBOgovpX3q_sZLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1QWLB7DEOdw0BCRfHykrcXG4tSdeIa9Aw1pUc1vY4JlJ6jjleQxrGmsh3dX6BACpiQZdHkgkedjEQkF2WlcXpf3SBeX38LaZ1F_13vXSjHd64fTeRZfUJSwhn1C59CCAF-RPjcp_fMihsMS0kETz19rAZvpQ58uHlRhdtKxGrS4oOMBFkgL2HFnAu_O9kJgB-2LfLyv_8pA7SgXUmEqPr450iXncEDULJ6hqnRb5TyJWgG88Gz0g5hSst-WO_UUDd1lDhxkNno6Rl3OfMncV3-7iHbEFa-SRUDMtKG1EnHB1xwDxU07_-4TRtLD0LUbbn4QMe5SmdHDlIgcur8KpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTVjTLUBbkK9Y3zEhDs3UO3AqKYcV6jApatbsXyFMBdAr6AgN5SHKTkfisPnNGduV2pH4eBR_M12G3zUzNeRDD-nXqZlzWKcDeBlJPupj7IbHKTzoaAXYSUDGRhfqDk5spDzBDU2EsdqaONEOe8yRxAaPRvp68WzCdwhv0UsYe_QsLuajtiDkHNanuot4jyQYhsaum30xTkkOi0vuTbrdWv7dZYcOnuMr3-2U-O7J8rzZ6HnKHR08qbs1VL7Ld9UVHCf4xJYyvDoF2t9bTmpGQl_l7aQjZhzT8EcHkjinwvCjK79_gkc656mRO_QP2oKoap2o5bMqJNslsouusBMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxRhttpP9jtLqknlNo9gH3kWXXQYKPT02X-fmeeUqS_ZeNJhdrJtuItOynI4sHLR37nmsTHVRKwJxSpSF7P5NUgF-jMp6Ewsc_ayjaFcbZ53_iw0OiNqCjhNpsdgNH9zYxudOQJ0X_Gu8CQhqhqWJR1x3QG77AQdv7gaGUZECujPsl0EJo3WvwUz_vnmYIql4bwC42KJv0M8hcSAS7yXXm1vSndv4yT2Hk0Tgxy6RfCv1dtsAedGKdIokmkm593UNfKCjwC4LHnyyPxIydwMShVacPioA5STeKIbUk1ICmBXPfyMbADa8IVHTPdvd5pAFFoa1Z4C_oJASTizdThjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYlSdNvqhwAPms5soA3ctp2Ls6tm-T3b5-c1KkP_Xsu_kw2valzKVa0ji6dglBmk0MfEzkFKuF0UwmP4OycAdsZWjZcoxJlJEyJ4HAqOCAthbkOXZLEOsKPRcthPWcyi5WQI5noQkfzyjvET1agQh9DNsoS1Jzdmpz0ukBBWIYJyuK4_N0146Q_aa6L6NLOu85GbSJfQ8gHryFXOU9Zc76nKXYbuEhXDv8Nb1cZ_Li5zaDEOV0ry6_Pq_106Cn4kl96P6nrcGew30p9UoFRiXNG3Wh9MH4Y3tHm9YuQNUWSm_3tKnS_20nvh6-n5xYFrQlMuEaS6cBTLvSq3H1k2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbeQXk_lI5dhrwHOs6sMX4NTrg1_DU4ms-DRwHPNZcRWceapeDaKTgnV5wjnCarLUDzajv5Gc5MyJXxo-12OtRzSj-YfiescxCAjhXx9t2ZhjHBn96-BhskaKXxkVoS1qGcbzazR0pkiYT-QcKHpW2dvI_72DfRRQtVhU-d-WeZYON5xSpWBYo8ZM0ibe-VUSyBIOs19CeoCo-wU0Qc_iUn7A7y0hclw4yrbvdQM6iZq6rnNsiPtMw_HzV-KTdGJbKrNAdX75b15EToLkZ2QRFKuRFR3v8VVr_JV7KRAlOpKu2HQOv9tb95_cCg8pVfGs6tIOoYEyKH5PzweSfNl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Qee9kS26jtodthym41J0nKqD8KP5XtyELux1bBSkG9Q0nO7g-h3uR-WXe2f_n-pfIZQ_Io1LSsKn1u3ULUUaIFiWTalh3QUEOLa8HTWrLUe20r8OSjEcFqfsM1vAqQ-RIFiqHZHANOS0cy9moaW7hhn9w0cUkKB5h0GvWq21yLbezsv7oqfgW3u92N6BM6fyx82pIsNMT7Sj-sFEtloPUcgrzPXalI_XIj7Ww9q5rzjPVgGNuR4LFrPnwvDBhl0n0I7Qol_xqE-jb_dvJpfgsFK23BINd57IN0wH2QnmurclKDm-TsBA2n60k8ulzRl_C-_LM3ZYWpNjegMuB2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
فرم Vip امشب با
ضریب 2.
0 بصورت رایگان قرار گرفت, برای مشاهده بقیه فرم ها وارد لینک زیر بشو
👇
https://t.me/+laf8I3RIuq42MDk8
💵
فوتبال های اروپا شروع شدن و هروز فرم های ضریب بالا وین میکنیم
میگی نه؟ فقط یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و با گوشی تو دستت سود کنی این چنلو گم نکن
⬇️
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbGXjpLAAiT0nrcRjv8fsF0AY5XIe0kqyoG7FW4cUf5VuK5N3DjK8nz-3LHs5-2Tl7ILG8OHqk2MeidXdLeD-jW18vRm65-E_6fBs3cLulN_DTRIv58Lxig1rjdlZNe_qppKlvYDv1ZxLpLGtZhg32DmiuRNV-YHkTUwUIP-7DCEnXgU7KT-rLwi8Jq3_sOktU5Uk5-qHJJbDI3Vmaxn7r4-1Yk2jOrc04kkHkXnGVJ80nAo6B1f0p7llif_maj6jExIpSqmCVos7UHi7LHgz2Mk5HH3mWD1cNXydHujNQXFQu1IqChF6SnTHEhxS--ePO-udrQ0HcTedcz77Rm-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=M56i_1jOD-_LIdFWnU56bzTe520_9PCSQ7lTFuRQ9zSzq0UVdDLvqAW0eGaLlEA5A_49XkVuyzAGNp51UX6yPD6MgcWYyxKPxImyREUmcYEm92ocLD3eQBW6yIUpwDKyFx4E1K5e0GU1HQksiTzTaBh6kmVrtXtgYfOTzYu8rQTGZSg_0FuhYdsi-G01Fa4woj1cc4mmh-mTiRZCCHe0inDGKqL6vY4V5L6GVKJ0WMY2rE5n2Fw2BVxAETkrfigfoQ6Lvv9iZNRTV09lv5YEdQqYWgKv3yz6-Dzx_ZDkKqaEohIcKNFkG1PKUC4_xtABaLnAoZByHuOfHhs3zfqBTENgc894oFrZ-4_B-xomyvRqFJ8tk5DEY87c1rHcskcaKrBtsVhfKf6NHiOjEvL1uG6njY2cVVG4856r2DObxA2aCqsqwXZnlkvATJhYi2ioHYB_Z42IERsB0XzReyXCvTa6_19jB4TTaBmXJYLzyuc-6KBBGH-8TOfeOcTSyn09xZEuo2pTbFUAA_Y-IR4D3ZsawyFnVP6f9pUyPevDZRtwBggGqzVN2h-rQROd7Fl_LzeNfNLTG3cvoyT73DcCz3SOYGHRWst0h9Yf9sfNirkHKD0sUEuxdEvTq7Nlr8RhFwUiZMWfe5GfvgXucBzieUBG-UJDK2XtdJiOC21vTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=M56i_1jOD-_LIdFWnU56bzTe520_9PCSQ7lTFuRQ9zSzq0UVdDLvqAW0eGaLlEA5A_49XkVuyzAGNp51UX6yPD6MgcWYyxKPxImyREUmcYEm92ocLD3eQBW6yIUpwDKyFx4E1K5e0GU1HQksiTzTaBh6kmVrtXtgYfOTzYu8rQTGZSg_0FuhYdsi-G01Fa4woj1cc4mmh-mTiRZCCHe0inDGKqL6vY4V5L6GVKJ0WMY2rE5n2Fw2BVxAETkrfigfoQ6Lvv9iZNRTV09lv5YEdQqYWgKv3yz6-Dzx_ZDkKqaEohIcKNFkG1PKUC4_xtABaLnAoZByHuOfHhs3zfqBTENgc894oFrZ-4_B-xomyvRqFJ8tk5DEY87c1rHcskcaKrBtsVhfKf6NHiOjEvL1uG6njY2cVVG4856r2DObxA2aCqsqwXZnlkvATJhYi2ioHYB_Z42IERsB0XzReyXCvTa6_19jB4TTaBmXJYLzyuc-6KBBGH-8TOfeOcTSyn09xZEuo2pTbFUAA_Y-IR4D3ZsawyFnVP6f9pUyPevDZRtwBggGqzVN2h-rQROd7Fl_LzeNfNLTG3cvoyT73DcCz3SOYGHRWst0h9Yf9sfNirkHKD0sUEuxdEvTq7Nlr8RhFwUiZMWfe5GfvgXucBzieUBG-UJDK2XtdJiOC21vTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uATlD-VU_Px604ldxSSMJkUpGKmayMXiALaPwt6-UHKacnsX9q29Z4qjXvNVsCmFYKskPS5yN2Ap-YYJuS6DOrkfxt3Ff5dPpG3rptzzH7DXl7c0lsYePsJNjO2qPH_eEihYP5XzwVynZCw78YYyBr_0kl5jT_truCLkcMqgDqE24cWet2q0IYYHu8fRAgBk44TiOIHTgNgQQJnofNlMlxQ8G2m2AVwvNqGH2cJEdjigvGB0CYkicc3UsWJoapCZO99WKfmI1RNUHAmTWW25lDbapxhXAzwjYG-O-N5Pi5Zh6W6TEMGLbDjkg0yj36cPtDTFNttWddkJCon4M2DXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNHdQZo56mmDKOpo_vC3pLWxnI3VdhUi9YQHN9oTqyqe89tX1wZAhX4Vw_E83EIN3uCjcphvgfb1nKf6_Q36vje-SrMVO0Iyb8GhXlafx5gsyb0qO17JJU-UZTctAaz2cPeUNDQTYvJVGBDQs0haTe_S0MDHHQleSTtf2U2fUnv0DMfxOH-PysHJONVU8NJf-zXNDITiajgac3QPOlY-Wdp4nqLLC6G4jIwME5-PebTxOvzMJIYdyfkMHKLJHN43e0KgXQCC7RExGliG4W40hW0wmp83Fc5W9lMo4TQ53QFO4qpR-zZMlMbmRP9bqOLOBbT3Ho_3hjm-morqas-Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=gANHAqxg4XF_MRZIBNljkLbPJUjSFy6GVfQKYmu4TeWGCtCm26t-WhDgorCelcn85cpKx0rNu0jwgyla8RcDd_hcxNmZOHFG-wYDefDrmO9DkFWW51Xba0TvX_jOWAVQIWsrcStPx6uuSM8CD6Rjp_wcfiM8vgn84TmABz14JtJkLtQOt3gLoeSDrmPS9JOH6Ry7-FSKWpyzJShqkxJmlrAHRUG51ZtWn58YmcJcIPs8YkRYZ_fNU2D0BvPbDGVwWazrRBl6vTsUJwPGyuUGC15ihAtSdElDlt_ADYtfUx1dYEv4nR_9_CNkJffcrgFqbVPlQH-PPdTNuc6L_T7Lmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=gANHAqxg4XF_MRZIBNljkLbPJUjSFy6GVfQKYmu4TeWGCtCm26t-WhDgorCelcn85cpKx0rNu0jwgyla8RcDd_hcxNmZOHFG-wYDefDrmO9DkFWW51Xba0TvX_jOWAVQIWsrcStPx6uuSM8CD6Rjp_wcfiM8vgn84TmABz14JtJkLtQOt3gLoeSDrmPS9JOH6Ry7-FSKWpyzJShqkxJmlrAHRUG51ZtWn58YmcJcIPs8YkRYZ_fNU2D0BvPbDGVwWazrRBl6vTsUJwPGyuUGC15ihAtSdElDlt_ADYtfUx1dYEv4nR_9_CNkJffcrgFqbVPlQH-PPdTNuc6L_T7Lmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0oiiHGPj_IfKnfd6drT6KjYigQTywAaN_tgmwsm1Ef8QeH5PdGmj1v0CPseLSFiPIlenEueYw5ctLQbIofPpVn74S7ERt_S0tw83dG6DX8ax4bH1bz4N359zy_0Bpj8g2trO73OLEiHGPMZ9PpKd-3rcRjwWOyUlFZWWYBh5nNs7f_gdeJ6FS4diDmMbQXA7X1tDLMTO5snCMES1LuvHJvjxr1BX5OFRrBqpUVNF8omCZYw7PpTFDv8vhQRRbrgrURZTeo4ZWon5YgEaAGTLbi1Uk_WR1HtS2v8DZv_qqwc2V5mm2RApwOdvf8O-_VhZYMTB8HxEd_unTF6-3QySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN2EPusJVZywfhlpPBvs_UzP9scoFt2L024w-sMkCXt1io-MPqFoEezNmuK97n8sGAhYhPkLIiKEIq33jL0D6FuOr3XFFGI_GgtmAAMcgfD4Iaznn9T4A9vvSS3HWiV3m2yHSUuUjjJU-HuWjZeWFT2QtBo1DU7gcRzW33Od7f13fjFy6nz07I1Ei2SOQbjCHL-ZD8USkUx0fFvrg-6Lh75q5nja02kFoc9u-LQxWRzaf_Uv2Nqgvjgu4o4LiFPT_e7h7xUxRTrC4S_fu__L1xDq6ex2IO2OXhWdDAHfupO1fR07wixKOPE9mrfnOiPlPTefO8y5_tnPYQ242CwZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBjHEGpZRtgQO18dhACz7TBdLIkQXTaz9IYotudr1qIyjxMa5SI8WEvhQ49CEHX1x8DOt_cUzpfnQPHTPoyGkJ_AqLNrcjiHP2BZ-2UepDpuC68UffUDEZV_w_iKQDBb7OBszSGXyLPT7ip6FBv7Wiy3Yoy_JnBZNWD-UMU0OTbQX581VRURksCOalEvx-Rm1MJ7LjCjygMMvJBlGXkAyBO3hcEP6qmbLPPFrWM3MJR0q6MoaEY5kDUgZJlfN2LBVbPx1l2lZAux_LSyadZ550Qh-MoV4SrJZFOLNihoovg7E-3V-EYc3fcQrOiMpVnHkau7FgfJ2NsyMi3zj2BqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf7h4-zGTqKybXJqTAoLitcqY1Ge4l-_g5kJJuZwDBtbVApoFdwwJpNo1r56qzaG3zs3ZLlYJqB2wP7rIN0zzgVWZTo2vaMYiwB3P_flNFNmzUKjhzquy_aCFUiMhrgQ7v5gAPLlHPxbXuqY4aJxIfM2LmPyYuvOhs5_lPlBRWlDeuMyNPArP-Awzbp8_6nbKzrrAwesCcrnDuyl3A4hSoEgT_xZoAHOkOsT5T5vCL35Brvsxuk9Jerex7rwDhNHc-H4nrFLAKZtwss9sFGBJnavB_lySuKFGzdQYvS8XnpR4Szip_0zrqeqvJome5O9LD59OCMqBic3K34go_BqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOX0inKqrQy-FFeJ11TI3Nfmp2bx_7qhdI4xMNsQy_cVyIomFrvPiSgyxU6yG74rMHLsVy_Ll15dvyc9VfF-eJbVzcoDTEs9aevTBjVN78-nwnIOUOMuE1QXYNhSAFBeH26fPxGbDswIJCXXtaAjiCIDuLW9517ietfRFTp7Wt8wFw-xlzY7q-GH2dF5Uaz7YkwmVxvArZZRNh6kS05TdwjJsddH2E0Shra1fz8BhW9wccL4QU2Lqw0dWB2_c-0DN1SljxVOiahlJGh0S89WNYlK2JZEhYIFkQO5y1tsOcQasU2Vv7Tj5b8ja6cp3VX_r2Notu5F1HbFPdbbYqQeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

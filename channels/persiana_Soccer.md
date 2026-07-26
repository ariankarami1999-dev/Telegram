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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 586K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 16:05:54</div>
<hr>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElJA7r2XpTHYq6qzGDo4YfuKN_aUJTuyBSAmC-XqXYOIZxL6dx7inq2qQ0Y8Y6ubt-jwUNEgzPEmm2fFLPYKROYVAlxOlNgSwL3i3K5ruxrJysN25oznwcUBzrK-gWOVzVfSTPEB-Yh96YUEVMOuhlLjxBAFKzEXd9Tlu-ZPFKOoo3yfgwnnPSVQzLDI35ZGU6XWD8ecy-gGix0E2_lQcK65AvEiwig5eDE8KT2mPB96ehN7fHhnxlTQnqrQpgYyVkIS7MQljcOfwZSmgk5_j2GadpUTiaJl1kKeglxRXX3jUXbR-0PhoEt_nuwGOY0ctxW9lOs-PYFTA9PmM1Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8HVOEFgsqTdh6EGiGM0nhGO_JGjDm3vImg-gyyb8Ac5tAT1lw6x4Hgt9lDvltZxdufEy-0mro-E6gj6rUDvKhYMtTtUUtbGUddymyAMqIJzKpJOSWyDWsz6Fy5eyEc06DfveAuHknXY3UfI5cBfQ45u_YqA9t9K1ejwnhcPGMxgNOEgnXcZkJdLkADLyg2dJ3lax3wAhi_EXe4SInJ9fH3aAZ8-DgLeHzgAFP1ig-xcBNObUpatafKXkKQo3d6Dz0ZUc7tkciOtpTvgvFLc18g3sQJnthy7OTXPqZ1Nl3ypxI0bPpRirQZwR0lfnEfc7UxAFpIuKCb4_6YkR_FIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myEUM4LfVoGAktSpz__EHsRUJGm-jbzTAeaCzIVL_kElalS6SI8qrXSGDalGv5XM76UaGtwqXiLeC_bcmB6JoffKHuoLINqAQ8H3OrF9bULvuOFK_eFibMsRWrakoX4ksok-f44RHDv3NBQanfGVrKDR6FhXXuVe2NsnrBp-nGpYuoihTyXS3iBs8WNSB3eonbMhB0D_v2DDsc57nsa6c4mHyrwN7-2Bne7gQTAb6-KuvxpfAHzEwjTPlRT564mftQ-QEAGKZYPkyh_5r_Uz734xacdV-nXhDpxZU_835oy2f_FNMlhTXQGXeiBvT3QmIOgprLUs5gyO2PgQ91zJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn6a1eYzY7IAMvsK7-_3lQB8CDdM692rqGEBTMlN9MJrUBsqso91MPF_koMSl4Xm1kG1SuAkDBmSUMm_ISKCS7G0TtmF_XvBueiv5ACIzyn5RPy1ZYtv3edgv6sJGCD_na43TUosZmk3gc9IPLqpN3BrPuA-z8vmz8JmZ1x0Nmuc9kttU8SWXJagQS99HuIp5MryEmAp4Y6nFOTnFZilFlDDLNp7RiV0M8oiNarubpRhFjfvkL-28bAt_NG8AKjUoQj25uoySe4M3VJEKwq1dfqx8SOTGRti1T_H-SXqyaBPI-BTOYmf0TKPI5PKjqRRq7TGBKuremOmbUhQJtq1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYi1qd0y94-tUhZZ_LDlzg9JxOlwB2-qt09RFb0IR-L8r0CfMAl_bP4gObtynSDFG8totKzSTiVR6UTPWpm1aP0s60ZimT_Lv6JB3VJVJBrgxzIFUYGWLlWMD17PUcFfrOFMPqXm4PJqN2jBtz-PKZ_PKTRMRkxGaDsCpatbO0paljPn9aActhnAAI9txAJ4x8MjFvy4EvpjUaY6u5Ih_J8NY2_y6dm9RSfLfX9r-7kZiXVu3Txbrd9MhN2NhkafQN8gshh7pvxwtssnCgYMhPkTEM_lSgr18kotCvwMkwPIFPI169SoNqqc2jR5hUOPTSf9GKQVu2HiOcfhvU3O5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuC6yZ90xYW_VDFyxdjZ_6EVQeoT1titII7-PxI3nCeaBrfiBRZuSKR6L2i5r-zOdUVxsLa2dlY7yj1gNWCb-mX8ohuc1wm7V6Wr53w5g6RTfKv2boGznc8Tdn4p-CHRvAgJ1jKV1J9VPku8f4zyfllVk_s9607WrgKYnwmhutBDdsODHk9vFJR8aV_BrrwNiLOY_V4wH5wHp-Sv1MjG8ZOmyha4XKY8QHc3hB5C3S5VYFFs2HnRBb--upnWj7Tdygwp061HPu4QAWJKC0rpVV8CVjsQI58FIz_qL8Zx5h1bvWmuCxyLGtQzW_tTBHFTDT4r09ZJw8_TW3myefXafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f10IkFTZeAnG0mQW9KqpyZWCcyHI557L3hPbGBSpdaL0hB8Xs5W1KzTb8jvqEfqx4ayPhp9YjkZLSSgHXJt2X3nA1xxL6t2hHmLhraFTkc4131Cv_Xo1HsiWTJX3m02l0-OzYYOnW0wiInvXosq-RQJX4odDkbsx7WvXhtUYVIhGr_lj-FVN81zFz8_zweL9A60905vC_9gdTw-KLBBcL-OAY2GGoQ8bny1XoGk9ExIGXKfkM_Eh5f0N07a0SRZrWc-W4WL3aKDVGFKffwu0BURKJHFnleX0F4svzOnneB70jByud3cySovsdaPJgLHjPdjZHF1gqbFrogGaNj9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_2XYAWcZ6-9bsLS50OGFaaQVpEr_QXGe4L8djHhp5jf49KotNjj3xlOb6aduNSfalLai7VfNg9FGXO8d7LTdfqUOVR7MQNBHC7b3MKYsdbX5-Jovz8zNkzvttgcw48R8Xp_aGzlXXFSL71n__COuGxuaoJgPVNafELt2x72N1PgBl31GSLxnXmcygMDNCD4gT-vS7bzfjONF7xeBq0vbaavsGckLG5b2BtZQq5uxHCFVfK8D6QotcIC0NXMlMlcRCJR90SwT_i8PKHiAdR5joMneqft86RJrDtDtY5DQP_jDfTiS_7fgo4EoUhhNTtLG-rvCLfWbupjGu538cmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWwuJTUf98mouHzKY_GVZ_-IvaWVMs5S6bE1iYKjUi1qulLhdGtkLmz7vmIycghjTBAt2tZNIRYx6PeHcbyHAPO32Fu0X81Q56qqGpJuQMk8EiLnq8NRevfwJbVTAsnm58pPVeY5EhKVW_rz19BwPhYV7HCIFkuFILbgGuuG4FrdHvs2Ex8JEz-DdcSL5mXqu1dumDlDUM9H_MwGgKekjjAW-iH5_vPHZOXyeKV_tQHzWWjhS_zIj6UO1pe8kwEbLVBTWCZYq8A3GYupmYG0XFnCsj60NYrLbByMkPKwdqD_fgTF1TFHFlf_Vmf5aZ5gwuk4DSytooypq_pKAPAnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9X6gOLn6kpt-86pKG3WWbLK13wG3ZgGS96-El9WGsaMYr8P9QLLdEm0wnIQ7OCBBUF4IcVCnobRkrk--nnCfOZ7pUKLJy7OOyfGWGXCf1cgJh1tmNeyBn8q5qgvXwVc5qMozy4PxaxoahnDV_kL767V62-sfbR15fjjqupi3t0B1RQtO_fPAVJZo6E9DM2Wtci4S4UDtnLzC_a3m4FCxLHHYAmNt35x39K4p9OPv7B-11H34jOKNEmH2bdtMgmOVpooV5m66Auby57VoEEXfAiguMrmZRRjySTt29BzzZvfYoPPcrfsSVdLM5UpHsHWK6_qFG4ddSQ02rXiDHyjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWW3GF9MWkjS4dPreOUBx3gyp2rJh2CzbvbykEucx6f0A-u7dfDf2HYgelLMODa5kOl9GN2Kkngkx659mMVty18KZH_eLmNd-FoeofBQ5a-fFATsJI5d3GcBNEp0AfOHnDQ_KchmsepeEzIJZLOxAKGX4q5IcaGSoA3Lq_AAtLc7csaRnDbVr9NSzXIFoGo_PmpZkKs8PN97X4LGFZagM7r3HzhTd7My0wVCdT7dCCi4I2bJ2-fokuNX4336z-0uo63zBjS90wDSybWzuPyBi4qgJW1lmvMrM10r0U6PW32E9hYvTrh-O2npUE-GdYM5BsCneJ8pFdwCHDAUN6vOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlbe0LozYbzoGYxo9d4gxRQOpFnISs5buboi1oDCcjGE48dy6ZWtxQzX83uqYKXAsQqfaRxDLYdltci9_-AlIt4b3nCtiqrYligbIxijkIbOq3JGu0ETY24fev23-sGKJtYfebJF8bLjIk-3M7MVR9B_JQl9iBskfp9o0F9XBEsph14KG7mXZEpAj9jyY3S41_EtIwkSgtvpQbHbqghMQwysCcyDoqtpGi-vUqO3U8KTktJev1HLQHsJaAn0HwaY_tKtlO7U0koYjI1465uvCMFP-aveujf1-akagHoBbYiS_fTYWeRYCYLmhmQIfhX5pxjOZzv3hLcQF9ADu-XQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvQ5Gz_3tBlyImysuBTtGrz0h4qzim1kQZNHfN187S_07R4Deb0Y1snYQ6WKKpP9OS4LQBIPoh-0xTZ593bOfFfmA5CfFG3YBvyLvfoLZsaCujC_K1Qh9KXDeuW_6V2D6tVqAXlvh9jfIGXuGb3_vIs9nwifRgE2Qd2xYOwbz2A6gaTJnXs_DSJdlKiph8o_GCsJZ3d7aoPMpS8gkKrd3kk_e1xnHdbIfsz4K1EiEWty9EdYfCkACezl8_BlRZhwAc4yDce52uLLURhwys-0Qj9LY1etS3WZ8ExFEaY5qTWiuVt5PbSGN5bQQVW8xEOhlzTSgsW1x5mu89aBuk9oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgWqhqSaGo-LfI3qw5FM6-oJ-nQkrqvzt0vB_9qnnwVzpwAZ8YVB2U-Zp-jNP1j6UvXhIFgiH6hNQETBwrmEMHiA8ENYPDljpmVi2RtAXRDd9OvIXBvC2AYYF6ozxkwID5BlswDCt2hVg9ETWMxUJz3VczYnlS4DLJ_iXcTnTs0bAtZhn3jyQWbTf9X4vXn7F4pCBXi0Cetz-C8K__TV4djt6hs-yfS-37X1c9Z0tjkz_FaVnq0yQ4I4yOnX7SZJrfs4qgAM1WdgKMfX944M4JuHY3sPUO-qcSRnRYShHVQ_AlRu5TwDkLHm1Sq4B55149VTMFwhpzt8rfsioo_Lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9gPe1-SD9TcaKDeboOb-ZCmQdBISlIC-en0zloiPu4Le8xW-NOxTh0NroLnSy5dUa_QmFariyrQKctyzPSQBoDkwuTViFmPhPaVX-4wjBE_ugWplrwfKjQWChAaRWUivTpNI7DmUBak-7mmNK_3vAfBb18fmHPqXwIQ3ZFTnj2gzztUv6g-Nldtj_wJPLcFJnB1VgC3HZgqSDMofPMca5KqxFHi-M9FfzEIEifvABDdiCbppRZb-Vzx_4bjzBPcdxTGyGNO34AgZweH8kf46Pi6SykBzisSKjJrKD-6gt-xgQz4I02A-bEkD3c4ktaj_0VUTGiAXpwt36swDBoPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=ZB7XEjeCKYXWl50EaRXxc3YA0VOZy7-VXuJ9owHqkt6r-GCe14xAGBFjp93C_6t1VPG5JwT11hpNhayNt2xlDsxJ_u_1lQWHlHZnr1jmcnSTtnM037Lw1_3ndPxxZ2f54_W4-qq6RlgABFmjLN_eB7X8YFhTge24LyUfyU_CBrS99KuoM_hQPyRqefGFhhpwjR0GvbbBK4HqZGjkn77vyqkHz5tzeeWGaZWI5FRgjxzBa5l7utn9cWj23yB2M2o2qINn1Aglw8AAKhp1utnrqvwc_dHll0OYeRdSZVNuNUuj76NBh9Af-5F3XbT5qYW_EB2fqDQfeXZGLBas7rubsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=ZB7XEjeCKYXWl50EaRXxc3YA0VOZy7-VXuJ9owHqkt6r-GCe14xAGBFjp93C_6t1VPG5JwT11hpNhayNt2xlDsxJ_u_1lQWHlHZnr1jmcnSTtnM037Lw1_3ndPxxZ2f54_W4-qq6RlgABFmjLN_eB7X8YFhTge24LyUfyU_CBrS99KuoM_hQPyRqefGFhhpwjR0GvbbBK4HqZGjkn77vyqkHz5tzeeWGaZWI5FRgjxzBa5l7utn9cWj23yB2M2o2qINn1Aglw8AAKhp1utnrqvwc_dHll0OYeRdSZVNuNUuj76NBh9Af-5F3XbT5qYW_EB2fqDQfeXZGLBas7rubsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EztPmifa04GU7LGWHegSKmSW253IM4rzYlzoxBGrqiLZ3NMj9OQ7EILvBj8VC5PXY8qAxaibnMcwJbK-_2IohvejQVA6lH9Py2jE44rqO-51uVqdNtIU4odx9ehlp8PpqoLmFIUMoDMcix9t6ZisVp31N-b8zc4TwY8Us7XWKYFKXCOF6af9GYx9LRp73rK4Y5VrFULaURx-txZ9lehHS7NWZlFgJgnfCqpMfFrhu7xZe3_sX7XQSNcdoADhrVO7wYOczD5I1WsIhcxdzvc9Y8_L1ibyI2DmGPj7Tgh91y0BErwxhJlF7HlyY2CfcVom9lFMQmWUaK8A9bRFbGegtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0gkcsoePFttTeAnGyY6O-MQW8mWDNAKroL-4MnBkO-MymUmefHMPv7jxsKvC2kH4egNnsCwKq5AQBFVCkDHDUdp4HUmFKU3pVltYhUD_9tHZUsRmYYoX1JxFNxv0fsOA20cwld2l4N94kIT5Jc01T4eCRboIbj5U35EyenKVI8B9wib5isHIm_g24hcnxyfNbRJchkufURqmStj4awrvWuM_pwIsvergj26_eem4J9C5s5B5qQtGZC3vUENjchF28M8v-M5bsKw46eW6tAcy1PMF_fMcRPUP_qHrJcVvhGtU1QHLhaPZiS9S2SxXHblVNEWlZjCW5JHLQSYCOHvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKtHFfc9L6vmxVDxQcUmrgir8zSFpmhctka0Al5d0YsxG94UUkTz1xIUu_NiqZkOLeQOT9Yn2VkeCw01PAs7WdGMHobwKikefLKLLrTq-Lq2pE_3J6_BcjYpcrg-UvrcVmq5d8o3qSlqdwAp-5Si1Zq-Vh-pa6WgpLex7TXkkdAjKh37oZRhoRIDF5bcujqLEe2rlIypMrF7gI_Crco02EH9g4ekk_HKs65n4V3rWosV2-Y4P5zfmZAeJGFdtbBJ3kxTnenUHKVAK9dQNkuirgQaW6KIUXfG2I8QyVExvUIWzhQSzMlbXSW1ph8PCrgBy_ZQGKpNiKa7w0ZlMcRXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNtllsD-TYIE8U3kqcGqUz0R0LnZwB5HAH96VKqOiA4xVYRqRQ_2jVQ0A1KdKq82Dol_3lIXxb488TvmORs2TQnJKS9NDWExaWs1eSD3MlMBeqw6L_4SC1ZTtQtp1jUkTb7Cqa0keDL_mvrkk4K31v2cJH_Z9VhGCtM2p4JLhvP2wbTJc3n5vQ9FtgABopFRPlJKOzX0eQn2fAhgu9SKojIlSg-hCGo5Anir5-bgmrkfNicqszgtriQKY2L42IirbZcEdXkX6sEzOr6r5XtKI1hP6B69h_7K6TZkGwhzXTzSy3hMFNCDZgF4zChbFqg6iIsHr-KO47UAXZLyEuVRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYeCK1b7ItmqNRd6TvOIWbiuS5jzoMxx5NzgCKdAFtGeWJtz3ew4jPZhexv5l0tCycT-BH1WJ3MmCHwfVASWV7tjG12WpnTmogyVqG_vK4h1fX2mc6RhWyu0e83qdWc5niY9GHEZ6iwzzXqVxu660ZVzvDGfWYwsHKETBEzBBincQ6AtkQCR7o_mcWZmW-dcs2c9j_afhUCalb-NTlX5b2w2MsKqTtJ5_7yHZ7rYuNP3zLPIDbDxEjL0w3wUFGWX7INHs2sB2I9xkURXLhKy4Y9WlTITjGPX-utOuc7GeiL9gxzV8-p1SzvrHwp-ewQypqwaJEG71faKlMgiXK-gOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSg2Os_kysdIlSrufcYKimvAYaZFO4b1gPnULHaxel4gWwCmjFiQwg2r1RWC6mCevG2SQInLv5aeEyIzxGBCbVCIienzV-ba6OPqMtspZzmJ-mGJ5baO8MffFGLAj8_2FOPygvllAp6ORq_7v9d_lnltmzGn3fbxhbAN3Etl7EOLrgIWzCd_UL9R6WCoCyTZ31_N4GsnZAN3BHonfWctTLUY9FuKLIOyBvGJDORYgbn9sO3f95Ho7NCMByiMGsvpuOJPgOYo3wUxQELeRA8VPzy4rV_Njyt0FPiyFGxXsQ5HvFHvx8JjVrwe1UCPADpK0A25WrqnERDF3V-N96-F0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxdFxEXldWOShJUS4jkDAsqloPmSX5XLJjm6bJdYHFYRD8VnhaZVUBNrQVfsPXMP6ZFVUpbR6K6mKhMdx00m8NhUmIcwhtrSU-ogZBHphG1Nu0z8qnEv1n2sbXt560Gv4fLv3jLjbyjAQV808SpYMSfpewvzegCA936ogIlSXqq_noOeSu8p6_zO_NgtWCSf-vX1G4kgebtQ7PbOxxrDsBcFVeNwUseJgQlTiZyVNU4ahy1Sxtc52x7qvo7-8JJGV_tr4hy8smD681yfsS_YL_2fBn7ph6f3JHmVKUrClokh2HSN8rDT1aQnWqBjcLzfSQgA6If2-CrAk2OTsOpIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omc_dI3-IYzo9551HiYleI9rNr2IX1GCmtQZQ_0ImL7UR8Dn7WIZeyhUyVMm6QOkJF9l99v6lGKE2fah3tPBY0W6gAYnjgCExbTeaYTS2TJra-B5wa_4ulDg1y5s9brCAKF7tvjt9lUtLGA8EsW-39JHebiba4LtPZb3PkEUT-Uxv2RRxGwZB-YyP86TohR6ebx86SIPGaR9vkQplpy8h5IzbnNEU2tCg690rdUH1_tniULPa6kcaqjtEjrV7tlWtDqmrJpfF45_Uid2oVrhdB9Sp0X4DJ7CJXDV0BgRoPmiIFT3W-R_-yKhPK_AxTjtuMwPrUMNNe_udod1vwIIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4ygcFJLL9S7MQLEHH-G44D1Siou7EchNuePFdwrbeYlX1mMKbEzWzsJSsoJoZyWT7mQ7Wlm4RsHnv9dMQcp5Evcp4F8aIBt6LhOj7wqrlf8s_Slj9ae1vVB2L2uX1Tv3_oOPWjEEvUx3ACkjnMyWwcO3qN1o3zLpc0bJR-4e2Cxo3JuCKiGcPCy2CuHt1G6Kc2h7mcq2z0qIwbnb-HYdwEFdeAjB07N6S3A2kyauNIzFFbn79m3KLE32MwMx1FboPqYM4tc8KvpDl1pgqS_bXdQqVfUkpalxtafaLRcbm9milbRsx01Ci-E-ynPJ8MvnNNEcC-V93OJSDTBu0h0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj5p8GLwK5uVcAapUZfwbK24B9AmmXJniqJk6DrbOp_UvL3bcYwMvwWhIkR12xH8Q3k-sgiLFbaZj6CuoICZ7xa-ra00m37Egpl2-0Eo4qZTpK2MBeijUp9nGL-FkMJPgGfvvEly4Nq6V8XkQRE-mnwHF9dfyAUoAi-CZAzWeuqWXcxMNc3H4n2vDGS9-b8kBQoFRt8IicEwChBQiO9nZlHUMlykRToZROTmw4blzEbm18abTr1gbD09JRqkSgUjs4KLZhJgPAOlfuGULBMTW_WiIALDHCU_MVDRjHYso7n0F1U4d13dTQCFK7RkeUQurDouO1vLTRMlls2z_av4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttaHtsxyLJkgitcQY8KwFGAXrgr_BbGJCt2DXDPeF-hoGT_3WzJ2uQ-fyvroM8p1ZxNFwlvMcXFvDHMr1aEZJfNdddrejxtCcDiZ7ef4mQrAD_KKclv9d7rsD3daAFOtii6fwcVfvFZRW3CXbQFL7nI6j43cs3TG4GcjyJEA-RBL_w0nqLr-iqaoZ3_GFc_QblT_LqtPs4y1VeVYM83_w9ONki5HcnqXcHAJ6_VlKz7AEZCXC48YzAfyEFSKz4dqVFQXT2uyNBZpaVC-a_s2USBC06DGPJDaSADf-aZV6K2FyF50rvVp0jl9VvDDWXVgNXbgQu9iMuuJeGmGc5_FaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpAf1i6zNkzZOPQleg4mVVQOgBeTpedCU3wfCtubdKEStomJDtVmouLokOdoB-TZJ0CyWAnDHcXjB6ZVyG4HLCqisb7Eiplan0PNejR9ltuQ7Y_cjR8hlxa6nQajEwfAlp36qPvK8R9EGervjprnPujaxWf2CCMz5qqtxblCtEktzcnWNM3kVZuZj7wWM-aFP7V5w1wLqq8q5Umc1zeRo7EZm2W1akyjA4pICHXk0RHxNp9mOaXHmwM4VwbNuFde0_pxNfgdtbzCf91LYcjAH5MSD4rFpOTfXOVRV7gQ0PVcSXNTMqg54z1wwTZpahVhsHONrdCDvqKdcSXnXS-6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ9iN7OPQAxUXhvlfIw25gFCdG0zkOGNQKEMvPReVG9JPkcUkZIvWJ8cbDdNWTjCjyWnEzbrvwBaQ8PvEO5kmncMi1nEeshogjsW9HjIwCxy7cHj8PSIH9mYOSdws7qZj7yenTFvZWJkFGjufh9fK26mwNy6GNC1r5pvKUD45I41pOtWej9bNn55X2_b6w1eES7Tn8JRLy_tulZTE3JkEx65T6exMGTTyt3gC0Rbg5Q0FcH-JXfVQJqDlT6f_uJR2NE5IjuMi_LXikiwfehJx147da7MPzCJ8-gHHY7lm1iwmx1piL1vXpUkw31C90VP3_BBCXfmbi7io5veMHrXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNj7SxD1WTY-haJvr64p1-7Ii0txy6XhVV5_78k_0gZdNoqE7JXxoT_5-6HdyQH_GrUeA02aMk6m1iohTXzegXQt2ImAEb5mSwVkrrZOK4uT-UXo5FNnJ2QaC-aq9oEEm8ZCqLFZRpThYDbKZQyKTFHzkrLCjU47E4pPOGE_pfDzufpn_eRxAzEkpStMaJDDHMcbuGsRsGGYBA09IHYG4jy3S86z9D4QvbC3EwRO9nzW8Xe0-2upHblwtqvXkok7Ls-gWJjp2ck7dPKEo5M3bV9epJKRTGP72PiQXDzdfOm1LvY0a7PGii7JzmhbQsbS4zjMUmQrFS1DKFwMytR6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWq9qCrONl4ybumubB-JTeW0xiUi1t30JS7tyMx4mzBMnQVHMlG-xwZr2KSYtR_VqDPveAsW9EZUC1nSgU2lHbN3BHIBRExKlU6s1gIpG45rGbRHchso9ZgC-0GBVfPR4Df0ZIUNa2uPhVsXfg7PIG66Vgt0q0lvWLHl-dzlC9Q_dmI_3fbH3fubizvZokc7Me0jbyY2cHR8_LEFCmF4yvOgsSMDZ2deqOunhF4Hmklo9tsEOxX8nkfjMK1eukdNFM2uh_bswUw-2NtsqaiWEi45G67P6LfF_5aMjR0XNgpqkLOIT8cmQb7sGtFh9HZtEKOZ7UoHYedrInblE1hTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfna1ZBdvomWFKRroDP_6hrITsLnC9RJALBhiTt8W_MP-SAYrNukNF32OqX2-ncHK2KRrsfkmFtD-E-SWPlBQhcBzYGatcXN_2rOyfmlhigFbIMpCC8ux19zSacpPVj-9Tt24zn42-ydNPR4YIEM5mSrDXJgAc230YnwiHz-ThX2E4kbZJM8KzKPKMzgjWW0fastXJIci48eCOVEEdfV7OQJJZm40wXfu9hkX0uH7n-oDN--ltlWUvEgspXMbVjOChHHk7shQiEbPkAPoOut4MZIwS5YgkxkH2STHeFTwA8bxcMqmHdX4svefOd5tDDymS7o1xHZdZO-3Ql2mXvE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVWtyC1Ap9GZAW0Tp8X0N5r3RXGW_QXulZpUQahRUpUuEW1VPOyAGqlHBP80HFpxd9yOug2ZF8WcjkGOJvwWdz7Vt87d9nL-lwGYEe3PnG1ksy6HVEK5Wd7NpD8kdSGiOo3q_tTgh7GDaSttgGZvmP6H1p3D6qvC7TUrMkBPbFD5LvGf5ltmrUMQAfJV3FfsT15O4eQLP2UTW1thKcg9inOHWNGzNVnGNYU3q9gZGFXLiPIuk-_1W2JON3fWXKzlQxmP5w7Azn4x1U6wH9A6Jtr0yyGLlqWojXKdoGDmurQnvvkPG-MFT_B-IokCOJKlnJYu0wQfKNUlxhbc50zUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=OikPD-1T6z9HcmBVE5bjAWWyVAH6FimQQ2hkfJX1VKaunTTcbw1HgFqQeUTVxUjqyiOERrOfQQPB_TI9B2FJwjsqVcsZAZabKVSOl36EICLVdfRc4I-0PCigDKVvOBsMMZXVOLv17CpZaCPNvHaULTu6kvrxFD3fU_ETwh5mTh0NayeAwrGu06jKrWF6AfqOuX1EvAMZJ5VRwb1xOAXl0gLybmbFni1Sa2LbZrCmFEOVmjZjzzn0NGsrC-LvJJKpWXv8a51OGd4pcJsqNzzqUx46Zs9IQfallz9BXVY1Z8KnGaMI2xX8gD1ONW3pDcEZKfVMxZY_8uV9IuTPmWEk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=OikPD-1T6z9HcmBVE5bjAWWyVAH6FimQQ2hkfJX1VKaunTTcbw1HgFqQeUTVxUjqyiOERrOfQQPB_TI9B2FJwjsqVcsZAZabKVSOl36EICLVdfRc4I-0PCigDKVvOBsMMZXVOLv17CpZaCPNvHaULTu6kvrxFD3fU_ETwh5mTh0NayeAwrGu06jKrWF6AfqOuX1EvAMZJ5VRwb1xOAXl0gLybmbFni1Sa2LbZrCmFEOVmjZjzzn0NGsrC-LvJJKpWXv8a51OGd4pcJsqNzzqUx46Zs9IQfallz9BXVY1Z8KnGaMI2xX8gD1ONW3pDcEZKfVMxZY_8uV9IuTPmWEk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3PdcZA8Vb3ArCnLaQPm_fiQcsOg0pOSSBsLs69je7ZaHEygry7F73cwPPVX5ySFkfBwwm2rMUbutB4ug7nZrETt9OxkeBWiynfi-_pTFZHg8bfKf_XC29DkRfMHAC5tnU8S7QfbjiopD6XQM-j9b54HVBNhRrgg2avz1emF9SrEeNGM6UQ131guhNWQULMVjOV14_s7OmF5fO0U_U0Qm0nafyCKtk64Rld1Xj7oGEg0ktJh5QR8CLASf-gmPzml2AcAJsF60s0ACDOLQmzyA5HVciDAibg6hpK8tFcr3bN0uMNLpXZ0K86U1LyUVXpSKySriHuN9U2NB2AxEH2fGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2FHTduplU12L4GXgmNIB9-kXFggSzOlQl6TCpwjn_ssDSp4W-_MoR1jxrRlOm2W3yoBmzIOFpd7BLMW4Bo6inKCo29rPTYB3mju2CQ6s5MaP6EsnhaY88_jkvU4I1KfWaF83y1xac48upCQnsLrW7R3SwrPG6h2MYPryfqdaPdiXc5weEBLNn4ixl-Ts-AXaAjN-wT7JccEqNZ-NluwemQoBJr6tnylvmF9PpNlXsnD5gI29rZuBsp4qGRNh4woOh9bpWXc4XHoYp9-7AbCSlvVBCQWXGKahJUthOeQR5blk1klprlQN4bO7vRGH5w_w5AoVWZAnpXixITmBWArYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBYw3KgDCKInMCR6UHCdBf5efX9_tQ1S2zwGTU7W91XqtfUA1vazj83izIuB5oDdGOwtsSO3eDxosfjGDmpJrNLGlDLul2dHOxv_xWaki_CSMgSMlASG-1aoR2ibDR-Zw5EkSTmsog6aqGENtzYCuoVQqUdnNdzEzCTGT0RjFCFUcNIieyLyqFXsgDC16FIu_dZX-g3tXsuYnv7puKAs4v3XFwTna09v1fkcY7yDzUkMoz6ozC5b02hYZAd9AH7t1Ee2Cv55j_2ueZOsnsDU6CZE67mId-SA-57JFpXhiB2IRB4VmSXrfLp5sEYBDZLD3z4RDeBYtWXurPBRlnbPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=LM4cmNBTCYcqVmfMyGZFbq1Xm3gpd9YMKnOywSyBfGH-Qo2LaN0lWNncgf7gp1gKXUZTOgXDRzkWKjGS14pppcRAtrPltR3nviPw1tF1lEBPrWb2jt9CJj2p-da1kHlDMadkHJwO1L3-lA5lbX4e3n3FLdKYSBtXIMYZMrNA_PoQF1YgC2MgbspSfE6su6y-D-9iYyYI9PoK4exgpRPa_g-x01jr50lDCZdp3FyMdqsF-UardzS36Hzr0zl8m-2JbVicFsSHxTzpSC0xGhus-8f4voZr0mO-dPHvYFonfhqzFjHWHfYLxJbBsb5MWInXk8UWvVA6iJn70cNoPZOEtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=LM4cmNBTCYcqVmfMyGZFbq1Xm3gpd9YMKnOywSyBfGH-Qo2LaN0lWNncgf7gp1gKXUZTOgXDRzkWKjGS14pppcRAtrPltR3nviPw1tF1lEBPrWb2jt9CJj2p-da1kHlDMadkHJwO1L3-lA5lbX4e3n3FLdKYSBtXIMYZMrNA_PoQF1YgC2MgbspSfE6su6y-D-9iYyYI9PoK4exgpRPa_g-x01jr50lDCZdp3FyMdqsF-UardzS36Hzr0zl8m-2JbVicFsSHxTzpSC0xGhus-8f4voZr0mO-dPHvYFonfhqzFjHWHfYLxJbBsb5MWInXk8UWvVA6iJn70cNoPZOEtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxnGDt0WphmOaMzafR-Bu64_IOIScTniL2a8X8DNnAgIb9ZBJmteExNCNkuZ0Z__7cfdjLtfZTeDUzXjk0W1xL8c2t6-pK7lKpIM0mdhHcbuqWYgh0OduHSYjq08n4r5K_G1xPq2nae41QUzd9iUJorQJYd2QkMNC7NmyAI1njTTN1l24MjU5n_BgUEGwtYPktqa1qUeahzsu2N1WwLKUnj5NmWrakiQwdps8aqi9yCQxWghU9yHkzEAFrS4JuuBy7NONF6tP6rkV-Fuv-DMVNW0-bQS8a-26NPzZseUB242Re5gFJaD7B1L_bB_-DRWg1-lunM31MY6hK3ReYWB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=NOBWynPNAcl0BVSjLra-XY5mC0602IQdyk8FTMbjkda7qVTlPrWxBMBDaQiG_m_qCUgOjn_QPIxAgiTkotXi-7-F6W-KnB9K_kdhBeqwbhI8b0b5hil0_oXRg0OnCGDaOL5-BLXAnuye86Et9BObYV0zrDcLH1D3P-NokAogWKzluO1kzgO50Z72QyaURyn8XBv8uH51WP7lgbyEOYfNsQFM38WZlIXT90FlgQCB2VAbGUDA1UYhVGY5URb4EkkBbcyldi076VTC9rovuvyg5Oet0gXhKvwQA1iU8LK7QCbGL8tUdsc8kE3YrexSxXSSTxeJQMbnoYRpT6NOPZ_0aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=NOBWynPNAcl0BVSjLra-XY5mC0602IQdyk8FTMbjkda7qVTlPrWxBMBDaQiG_m_qCUgOjn_QPIxAgiTkotXi-7-F6W-KnB9K_kdhBeqwbhI8b0b5hil0_oXRg0OnCGDaOL5-BLXAnuye86Et9BObYV0zrDcLH1D3P-NokAogWKzluO1kzgO50Z72QyaURyn8XBv8uH51WP7lgbyEOYfNsQFM38WZlIXT90FlgQCB2VAbGUDA1UYhVGY5URb4EkkBbcyldi076VTC9rovuvyg5Oet0gXhKvwQA1iU8LK7QCbGL8tUdsc8kE3YrexSxXSSTxeJQMbnoYRpT6NOPZ_0aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujaHOxu7FOzO2TriH-VnS5QWYsC7GK9wjgD6zYc2TwVkvzxLd9K7yII9vuVEUJ5Dh3gu9KMc50IChgzIKZFEvqST7NiN_VnHYjKf-L79x-JozssKsL2XXWdwfX0YbfhXaMKcwV1THxBOWazFnAbC_-UAcUUqgYPerfMJX3_oWZlu2-rDoiRBZpbbBWbY7ugaT4ZKYScvZTAI1RwNwouHNnb5uhclzwVtPb6w_Q-_-7A1gUCZ1UUBNtkW5xwAM6enfn_j24aPi_UjFInj0I_6yzvnVmptc4pFu5i425tmlp5PJh9O4CWjWPpwICtO9NsIGa0kl22UiESEgGrQ7di6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7iCUSiQ3G-2mOhJtHkh5xI34UcNxbdiQCnesU5TePxuoPRDhmmFMGjcMrrUUcLOTQV2UJy4EuQTUvv_esIbfcbl06krahzqD4ueYWHDBAVmnZoqmx6XC4r1sAHOJE_jIkhcotWkIAXy8CWD4UyJqbM_5e61bnevoxsYA-EFpAvyijuS3pNGlkFOPqV_pCF4I8qxBHHBNvk4oo-lToubT26UMDb3LdRxUNKtmmyF6C9LO6VVqXVQ2kOWPRt_U5OY-eKYsT_ADME3LAGEHhr3VrgvrTSQgm_CPrUGnThnD_14Zak6omzkZHrYszh2cMe9rTFxH46Wz3ZxDeL2zkMSTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTUcc-f-spn8zl4fG48pbGxsEufvRn1FlgpfBbl3Z4tMMLLoj9o8JspYx-dt4JIfnTxkf78_2yL0_GlASg6GbMtftEbBcXiLLWTBKGrW8poMON8m-24M72Jv7Ew1ImopOGJqETzQVQqRs5ar4NSXEwPj5cQrlgX_4eBJFmdJSS5GAMs6-0ax7hP39KAlilBsxOG5f8tNxY_esTSz7BeRIJmaXuVDjHkLWiE6hNl2259Z4JA9icGyXRZemiit0XVr687sCnyjiHC-AkB5lHjZRApBjUL8oQLxF1Yw6r0rhjKhLYwvjEO7vYo9WsBJHrKKIpQcQi_QqueubUr1Q623A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRR0ENtRZ_KmkoQT4J0uDKPYIUX5kvCfV2Tns2J9Fq57xg7KJzPwOBT1vEW0PwORnpbgi-EsG3MRb2kgiev2SEHQNV1MCHmhAaZ4syTGo-jVid5Px2pbwRJMEC2BP8ynEVB9XUbatikdCz9i9rplbzcL6IgZz3CcjAlToeIBujIq9zI1XtuAAhT1K-H91UTnzHA-Z-WYWuC1rM0e2HkFA-PVNkoRH8f4wshFIiP_KNdkF3AQZZODiURdVqpPo53_TlQ-PWZGsQe_JnfNk4WpL211uBjG82xwXklAC7LdVALEoeJIZsEIThETE7abXqmcIlJFZaCymnLK4cPjc8Ja4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
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
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq5-4nc-oLdo5Wif_1t8o_fr6ilF34xVXKjppBkXhfPSwZEvMdEQYwoL9W-YgiuZTOUcd80NjQVNnTefPnka2HxK0CtTqF5Y55ErI9_JpBPwZNGsVWbNZ_zV9xx5YRsOtX2_XwSLsancVy9ufwMWNpF7ZRw3D3t3oTKkh8QfayR7GKb2EUxne4y71HtXfAEQFk12AFogHtiV8GiatHLgBFxEuFy9CC0brjdv-oMLbEiDWyDr6C59BKgXtbysOsWXY2jevg1NUEzAnZPcBR9Fpmxg8AlHWobnv2f5rQql2dAhacMFP-saJdlQDOt8p74d8CgACVGO60trfNK-1fARKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq0TngpvpS5CzVtV3EoVACGwj0vGIJKDOVkDln-V0PRWgou4CRGu8c72VrIdpY4L57N8Jp6vHW_MbNjjDwRLR25KPCmWYIj9kt9L2USTpQgmV9IvC8bRzpF84O5GyTe1ZqQHLvNXoqwAckkaUBl7hFteBrfllhkcnX5bVAD9IdQJLMi_fHntGR5TzPDDARl7MibhMuFqRMkYIZrnaIk2Cl92ctI0NRvAJHCTdzx0tY09PHI_VPpoWWRBCL5ydcTYsYe-Z-ZHqNq_Z2fzPQdSo7i49iZEE1y27XDpL33vPyd7u6S3kfylhwy5gRg4KsqSGOrXjHN3m3t0az_LnmIl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhoMxDgFN0Md6VSR4n52ObnnBvcXLc1UfcE41Epkq4tFbxt-83pUWZEQUM_7PxYX14cjr-Fuww-u9sQ3MsQyssljaj4_HhOmPpKOZkUgrW4fd4JHbFjBz6A9c5v9lhEFSnt2Ko-NMroQQm1ibjiri7m3JxOmwBFwUv8m7GQRx7whtPfdhbpP7GjyOEKoI8z-44O54Jo04r0tW68mBedus1XeJqNhw_SqOckzwyZyUrCvJipJ1rZiZXsDy2w65RTHT_CcqOMrhO5_eqGG9KTl7VUHzKUInO8CWcT69cdZODGCN5Js8SsrHFaj6NfLtn0n5rcHEN947AeX9aavD0gR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw0M8xH5FqhLgyxV81ppbfN3LOqOvmKIuAYTClHB93Kn2dfhzc59-h7Ai1O4hPbygHR57oDY_FI9I4o1EXu1auBwAmBj1GvvbTronbXd1tcSdWRkGbVZ5eYJerlSu6mdZ3h1IBhuBIJ9LwgtEtgbjaEAtOWu1q0YRAxdU5MQwbxmIYMaA0CPi22s8vY5YoZeY38V_naK9_uvecasJLD7lgCOfCiVz1Fe0B0deGaEagqR7e8b_r0OpOmCyWHJV_RKQ-S9c6SAOErAiX8JylK59qsdX8u8SyigLzMZkLFMsqiLmfumQkx5910rKKgB4JWTrmQtBrMitWNyjCa_U5AvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=WB-dSDx1hdMdKkFk4ClAtwVSNIwng29QF7cwTif9PtMFQ8X-jfUZNjHJTfx1xOJ2mVISm7HzKzvzbGtXXhGWElzP6IXkEQmq89RXLOOwWpwvsLNY-eWDK0PtofQlvawan_wxv_K5RUigdVrnFs0yrXcv6sTWe0QNDXX03aPSvI9NpKt3ZTzAkitVKeZ1Lux5JG2e0s-nwtN0s_0mtm5skMxydV7VImPkzrEfFNM558moreuYBhkRkzI0tfgN8a4uYCdwFgV-5UA23F7XtAgehKS8HDD15Wb2M9cN8fbTm0usFTCok8osSW3ULmcUMsYik3JwTTwqXROJDeIaRxMmx2AyfyO33uskiIcnBPi7jg2u2wHfRgyEdP3HmeOo5zKFlBRQuAtoR2Q1uqbn6BH0EZABmKrWc5ZBL0xXwYQUXUCdJR4t6YGFfp2rH2vW71Wis3ui-yqkB-MDAJNQNGnBI2i7TmQUpOdhL0ZOV9Gw8gUkHb2FKTMqE4kJyEWD69tqZj5SWqidp9Zc7SHMhkcW5SdToTj-k-1O3TmD8S99jekbb-SlTTGIhPAOPtUYABgEnOB8DwGdMfQbQsTZ-M82AqqcPPRBETUz9cjQnl1M4zGsvpgXRK67J6xhpBiQUQCDPBSM75Pphw56BTCaQMCGeF6I9H7EsMGjhPgQBs_1ba0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=WB-dSDx1hdMdKkFk4ClAtwVSNIwng29QF7cwTif9PtMFQ8X-jfUZNjHJTfx1xOJ2mVISm7HzKzvzbGtXXhGWElzP6IXkEQmq89RXLOOwWpwvsLNY-eWDK0PtofQlvawan_wxv_K5RUigdVrnFs0yrXcv6sTWe0QNDXX03aPSvI9NpKt3ZTzAkitVKeZ1Lux5JG2e0s-nwtN0s_0mtm5skMxydV7VImPkzrEfFNM558moreuYBhkRkzI0tfgN8a4uYCdwFgV-5UA23F7XtAgehKS8HDD15Wb2M9cN8fbTm0usFTCok8osSW3ULmcUMsYik3JwTTwqXROJDeIaRxMmx2AyfyO33uskiIcnBPi7jg2u2wHfRgyEdP3HmeOo5zKFlBRQuAtoR2Q1uqbn6BH0EZABmKrWc5ZBL0xXwYQUXUCdJR4t6YGFfp2rH2vW71Wis3ui-yqkB-MDAJNQNGnBI2i7TmQUpOdhL0ZOV9Gw8gUkHb2FKTMqE4kJyEWD69tqZj5SWqidp9Zc7SHMhkcW5SdToTj-k-1O3TmD8S99jekbb-SlTTGIhPAOPtUYABgEnOB8DwGdMfQbQsTZ-M82AqqcPPRBETUz9cjQnl1M4zGsvpgXRK67J6xhpBiQUQCDPBSM75Pphw56BTCaQMCGeF6I9H7EsMGjhPgQBs_1ba0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6bBqP86NYleb1jS_vl05QSxli0Xb-2UTN4krHyPaU9WL8HLnyn6O_wLw_XH_P-HgRPg0z-5wbiKNwZCaDxM-zg0I5fitfBYCvfXzkyKdnhA7ljeiiQqwJJqdNZTz6IhKjcnAD7jqVG_adMtbivDhgu4PaUo2F54SwSkeim1IRfKOeHp8qVjrGNi8aHsf7vCjQsR8ovvH6euwb_5QmVlhFkFBlhsmOuAPlTPCbPfecPwAdP9AHzGD7YKVALaLSRxJWf0TmyBf8d2AJFPSL7eB2BQWMMrxcfA3PggFkWVGQkUZGFsD2trqI1JP43LFK21jXotEAAB-o7E16LTwFFYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OafiDLbwzph0DT9NZCPWBS6O6198Osokn_rdG0a75FgZz0U5Q--iThLDCQnEuZOMuDTm802tqRkSCZNXwkBAiZTKEN0g7Yg4dR735E6h11Emen82iqkSJDAOKKuMmDC5cAm-NSB5bht3auJovOobfN1oJKmPS9oHiVhNt3b82BHsTVB04k7XDZiOj0zr2y573_4CcBjz85K2-NVnAia0Oyqm3o9phAiAG0DQZo8diAdBNHKcwgFS6E-spoRs3Gvoj_T9RQqg2h4cXRWhCSfeAb7CaJFiHRx-6UB_K74X_aldXH_jHktUd1zFSVGY0BgZJ1qd6ej4wFTn2BavZv3OEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSqwgwBnMMnwA-KMRy9-hQptWfNKjDbBVy63aKEJEiTPaoReGPmibnoSIDLJYlg-VwdI7N6y2rci_UO-Fr3UxjmrPsHiJ6KWoCXG7WOd8IoT_iyPR5nBwBjACav9qi090kU_CSQaHant0BAhTpTV_UyyFFVdojUihHGN9n7kdUGjOkcv3O-TU44gGwBc6XByvP4iqm32izt3oNh6g3O9Cqk8C6WcxSRiJs2uMOKYwuPBQSODAMS4cW1-sXCcTzXHTCANyD0MZFIopM-wZGKwT_2EM3J1EOdTRSkn5cNUpa7tAFAPgP4eCX0eQuDRVL3sFuBiFkO9zec9R-y7LwGMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP1MBMd5q3QoGeYonyybl3vT5HL3vcM38tJJl2gKlQ_7fkve_41osshv0nUr0uDpTuQJwJjgCu3dJ0WF-t5-xcsGpyuGa67k9qPTuMp-CxQfFrdawGwEZ4_J0KEAzumP7hqep2Yf9qAOPlDVeV9Ds-Q32BstvFmDWhrIqrE4XSPlvfHImt3LeNdxT-mYNDWDRqXqkH95r9oz5rnBpG28D9JUOJ152XtnBewc_lXFW-fjozVHtYYGJHVxu1m1T3---zCbuU2FJnd0fh2Y_73CqeKmoxj6c8dniUu-HKxGojPeqKFD7UQtuNAIKFecvkTbHOuUWb_AzfwYLwy0TjRNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhroxCz-Q6WIFulBjv0Q759nNx0Oj8Mrogac668QZLbzIYNL8bfomO39Och7rGHYHXTaJN7TWFyIP6xVnTOwszulOECkvyIXRHnPkcucm1thHt7-K5o2Ox1ESiJiuq3tv2gKvqpgeg2dH3Z5AthtXnW2PbMwDgxZewPuKPLJRJIJydsAeBu0_iZJ8z1wzozo9lXWiArVw679-qxUBFFht1CjfmrnnGnbNhB0l91E_AP106I4frtp6YrVxa7qj7Ts3vrrnqziegI1Wj79iS3kfzj1i4NIvyCz7ud_EUmXv12_jsjhuAfHY0JriZeraWZLc1PWw9xiUo1AnQDTr7djAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXMb1tf2g1iL4wDNbQULk7Z09qlu_oIOveFPDsTjrrnx6_YZ5TlVwIl5wijzmn3INzDadQk8ewpc5cv3KjGCDj4W7hlcHUPo5PWxkvgc01IwXCYTqvQ-rtLv-dETaEaXO1Y__4B0AzypTYK7hFjlbDrG1p_8KaNk6aeYIg8oLW-Co_nAFipNMB6hqzGXeNO5apwzpnwSKbc-676RAVrtXbs0HgKIENW1K4yTvrPGoVWwoEV7ZcHpalC7lUduf-fYEkYOKHyOFyyoOhQAhFvRN9h2kIEBZSBX-SzcuAjVvTY62Ki0PC5UPGy8VRYz82NwicTigS1CWgIqzeyMfPUwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=nrQ_kvDsL5-eLxbkMtJCuMvQAQnTvd1PzvEAujSNj89u3VommRCUWKHO4WZuuAjiOGDa76B48tNyzlHzsqx5pcsWHxRpAfK_5UY1QvjekjWxTZPBjsFaRCBL9c_K5l9juhJRH5cS6B7ucM4LgRuzJfkLn_XCWrkoqb6bvyBGru3GebC4GWXBplRmWFvFcPbY7Fn5Y25A5K4H8lBs01UWzPW_FabCdxiZYbxn4fIoT5chpsn_hJZUQzoI-jiQL5BPWjgkdroLkS3cDTl1wRli9Zga5yaYSMYK6nqCJNWUmsC5ULuM7r1P4upepATwKzRs8zXS0c1dvfeIfuQF_thU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=nrQ_kvDsL5-eLxbkMtJCuMvQAQnTvd1PzvEAujSNj89u3VommRCUWKHO4WZuuAjiOGDa76B48tNyzlHzsqx5pcsWHxRpAfK_5UY1QvjekjWxTZPBjsFaRCBL9c_K5l9juhJRH5cS6B7ucM4LgRuzJfkLn_XCWrkoqb6bvyBGru3GebC4GWXBplRmWFvFcPbY7Fn5Y25A5K4H8lBs01UWzPW_FabCdxiZYbxn4fIoT5chpsn_hJZUQzoI-jiQL5BPWjgkdroLkS3cDTl1wRli9Zga5yaYSMYK6nqCJNWUmsC5ULuM7r1P4upepATwKzRs8zXS0c1dvfeIfuQF_thU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcPk2R-wovRQVz4EI_Rk7IpSH61raoxLB3VfFNMkq8S2P0sov8su1EveO7j_y0lJazGwxOV6GvBuPo3NgM6uwpTjDU2hJdMEerIY-CWzuySKExdaedkhZuvVPYyzRepxuK_5QKLVxGS-wODZdceDMuQE9QrWOqOYX40dJ_CaOq9-oRtHXJ5-xUiKlcmeq7Le334rRgfSnyT9Mly5OXSx2BG7qe4uGAalHSf8xyQGED1SNn-uxqR4Ry7qOPOqab872McMlb5y5v34_3AmW2QlKJY3zu7YmRwRtIqwUItpkxOqODVbTpnHUiqAMKL2IrFIHAi3UBXPRI6iVC2-e4mrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuUGcsb408OP5y4FiorUYfOxSWkqJDfWncKRytuBya6xQwQsL-AxZH2GUyQmCjbQkY09FNi3m70cA7mJQWZfTYC9shendrRt4NY857vv06kwGjpj43kCfbNDBOZMRQRpn4ob3Rvx_aXmwuYeEOq8zvNtQNE7K-HSqJr3K1ppi72YG4pKKS_md7wJoTUjt8SvMVdV2qn-6lGiW35NJ6hhnNm2J34uiSTj7waodGE9SplUDIPHjxti6dptLMdYOl728LtiRiVNyypyuo8OLyEa_bbwSUcsq8iOJsPN5Xv2KMBq9oy_KlWspupcmTaAi_-dPxc8ISu6PeV7MrPj5lGO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDUVggvekO9pYdvcw7l84UAypy8zdDjhca2i_BqAU9oqr2zZ3cOgMgNlhUZNxKYGK4PuRhnsP4zGKjLOJabuhhrUrI5C4wOU813UCNC9vf1iA7_07egC5VVweoAIzFJrW1s-UOYTXNTfQTNCCTdZ6XIQM2uhXHikyzoyLeH6kkHIAgutc-lH4yoaGcpd4i7MTyEl13C3QqJZo8KRSLTwrg2doWFXvOZ6uoILf95v5cxXC1F7PFVH6Ufv4eGdlZHgs4jGCLrb--QTaUxE20UaL5nNJgAw6RIWOOZ_Tgq3eOdUG8Iq_3BfvN87C9RnslWtG5P1nJFFGwdNTi2Ge9ImqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRK5CIiMBpAlpYtsMCptJbI9I_qMbL5GOJdl-GUy0KBsIDnc2sOI23-rrsaIgQ7SG2q1Sbbx7NLMfBbZcABP-FU4c0T35bUoaD4q4nXmzVnalmTPv24AkAw4iYFT68vvyHGViRQEiV8JgVnzz4tXeSavU3jfrNthGoL2Fpl1tkYrUB14vWFNJcIGgVh5ctZQpZ3odC3kGVOGMj58m5mkx0IFKaWeb-r_QXDmV33bGzewzhZctGkEdGECTjX68mq6GsAvGqkp4DIiXSSbYgeFbmX3HpyhetsBZRxLD8g0GzM4uYo4X68PGQpP1fUSRKkZRTIitGdcy470umMkgD52sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDbIDShLxBXXOn5aiZJjlW20DznnWJgixZyQOjFSVYVCgaUzfC229Dhdap-Kv0lUjOT4Hh_OgsX8bxGLL3Mwk6z2oRxzB_VcISqnNVWftn5Yd8uLmGFvf0cKm9vdSV5ofBZdzLUU7GcqXR9nH0IGzPpjQydBuUhjfmgE79uj3OYiTjl1O6Q8EVdemGZ09J-0LYTpEOg6uH6gkFbpr2Yf-mk0SrVrOcIa29OGfbdD9s8Y6sePb0zknRKUuH-_ah_HueSnAzqelaOjE2lL9-tCLsx2PnitW5koESPvY80baqDhwZ_1MwqyW2gUE_BOxgTfxlyxJSEyOY1j7jvBQy0QFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGA6BxD0EJ-wIotJTB-96YRh0EmYnEr6gPva_-4YJwvNbBNddKaFcO5tvkkcSuRZ1gnbmfWSsLA7sNTQ0ib5wfXlMwq9pR18MQUUa3-iEOZ4elCQgzt12O_x0gT_pUvHMaMR6BaaO7pPVgdD4TC4Lqf36CfnHGQr8SKNLPiYtUsPRRcwiTwXCCfa5RFhTXshVDxR6tuX07Zs1ghTiwVFnZVtuFw0ZZp41To5i_7gsizgtqLxWuZfEYDEKmEeKZ3QX6OYhJLuOvqhR1vhim3inG3Ftj7bAM2vCB3R1C78Evae2tm92pEZobdIr2p8Mjp4XDvhlGmyGRuj7dNw_iLioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm9gWaoukaqJ0_l8McI1A7X5vC_wi7RAUchp8ZVGkmDjZPKdcA4vuL-93iybvTO-SHfASToJluCN9auBIq5VohcVP4M62IZuK_UZy3h7njdLwRBQkTDnPJZ8c8QZZJXWDTy0oeNsdbsREO_zQs6wqUtrik-qefO2UMyyFukZGO66MgD9ysD0JYvXjDycKweUdyvglGXTJYlmnxMJImQxDdR7TiZPxeWd1uYjfwNBlgcL2Y56_DIfpcXAkFnYfeC45Z2K7rOzW51ruuhGveIiKTmP-byHMx3G9iJAzR8EzpAWwqqn01l4dAPQ_Y3Nqy7LP96jpZocpN6M8kkmobet4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/relooSlOj4_dz3UU9bBh7WUwBwa7UW0lvC52QLqqUfb4SC9D3IqiBESEAlApGWZOnOMvjYdh0WpdDmEOCNA0m5TQf0fO0RLnGeRM2V9DC45WHLd8--OVmifOcZKYq6PIen_xlT_eLK8fCa_8uTcFepDp9N5kObFwSvzr3MOcOmZ-u2DnFJAhQkg_8i4CCXjdOiHy-8LHaCaAo7JGXPt2FagdyRlTi33yzB0k-cTgxNpsXUm75LXqMfr0B_DQ8p4wpewE1-iMh6dWAlkpr7-KoTQmEGjcdkK1HLoWwhKl7b8Qw6k6zo0SHgK_PGP8HJaaKCqJ4At-OCSD9eGb_zzpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs6QYMjA4TcMdROMr98WF9oPwqQ3Vn1EOWKusc2P5aBD-wkQrCOWzzaGu37vQDgvKsl_6UFvs4SaTFLXDsEAU4bip_wx7vSw9GuEj0gjd_3wFJLv3biMM8hK5CRj6x55iMfhjevwb7_tMg-Rb8A9xO6PtWL6ueHQfkhu-C7e4oYIUu_Ro2s_U4xfsvQYewXg-bZM08zblFKnlFB7CApuOkwcw_dcldux73sQTq6D_EDDbip3yfajZojsmsZUBvc3NnBTtSmDYkfuXco90ef5EweE3weWFcw-9rulLBbr8KSbJyZGFmYuWMSKL0ar94rpq7_-emL9LcIMfUlhHq6daA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laLSayibTa-4gwimkK5AkLp-8vu-vmAiA9zPDoQ2rPfygd735GNcA96RcV_XpLz6Dp-n9oipqjU234yHhbYGUBnubSuQc9VpCpctN0l4xRJ17LrDdFGvvLwmShrbCMBsnXpI5SOvmPsUF2R_HCgN9Mm6k5t-MmHv0k0942as8Kjt5lyMxtLygiOBz4B6z5Xgu9OL7GrP2W3CtwS8ZhBVxYdbJNtpCONew9ta3fU7HpGBUsjv-EBm_7rjl54VlP_eychX46e1h0wIb8_5rQsPfLnaYmX61DbvzZPFQmWkje3TnS3PdmZuDrDEZuuQhMan_LG0m_67YRJeEXaqK5m-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=sYPGtnBDqr86I_4wrvnlnjTaSXXiQuPwF4frXE-nf3pC9v94Jsmzy8dugpnSEm1HOC1CCLShq0Vc9RmzhSEYIg8f37iQR95g6ygMsHDaMUlINgf-mXbBFAMuHfHNly7UjDG3NSOPan3TDzzTQsMM-f5zcHRTOzSN0dSITuFhuoMCbHOSaegxwadvDmA3rRbSOWKQdw2xIyX8FLIDPu4dfMDK3Wi5Z6SXIwk6b7gWJmwYT22dCCzdiiNB_FggbkDi7W4wpvhEuExq8U7orhD7rJPOfycYgwfLaIXPxxSB_p23NGU-_EAP7NWVxpteqkGbAwBC5dvQE84z3xOjCbIx_H_J3PZ7kISulXcgP_Vjtp5NefjdUPZQ6S6jVRflNraFLyGyMJL5ScXz9CMkZ04OT90otbki-P3kKeYASowbLCvJRlg1vCDpO1aaHPkOZaTs1PRJDTh9hNns_RCla5LqDtUGdTPmTzkoKuNon87bbUZLojWs-TeTYsIdS5_Ml7lrdon3WU5V_K7YfQXSmvJrQfl04kCHYEciyoDzSppGAzzatL6tWO96U8z7uGgKkaNt9xspqediyT4cltFC_ewToPwcZdhV9oGTwjFPvRmTNE8Pe3u3Bj5VgPz9hOJNGeaUoYxvrKPo-3DmJan672bRhfFttCNjE8jzjTSVIpDlT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=sYPGtnBDqr86I_4wrvnlnjTaSXXiQuPwF4frXE-nf3pC9v94Jsmzy8dugpnSEm1HOC1CCLShq0Vc9RmzhSEYIg8f37iQR95g6ygMsHDaMUlINgf-mXbBFAMuHfHNly7UjDG3NSOPan3TDzzTQsMM-f5zcHRTOzSN0dSITuFhuoMCbHOSaegxwadvDmA3rRbSOWKQdw2xIyX8FLIDPu4dfMDK3Wi5Z6SXIwk6b7gWJmwYT22dCCzdiiNB_FggbkDi7W4wpvhEuExq8U7orhD7rJPOfycYgwfLaIXPxxSB_p23NGU-_EAP7NWVxpteqkGbAwBC5dvQE84z3xOjCbIx_H_J3PZ7kISulXcgP_Vjtp5NefjdUPZQ6S6jVRflNraFLyGyMJL5ScXz9CMkZ04OT90otbki-P3kKeYASowbLCvJRlg1vCDpO1aaHPkOZaTs1PRJDTh9hNns_RCla5LqDtUGdTPmTzkoKuNon87bbUZLojWs-TeTYsIdS5_Ml7lrdon3WU5V_K7YfQXSmvJrQfl04kCHYEciyoDzSppGAzzatL6tWO96U8z7uGgKkaNt9xspqediyT4cltFC_ewToPwcZdhV9oGTwjFPvRmTNE8Pe3u3Bj5VgPz9hOJNGeaUoYxvrKPo-3DmJan672bRhfFttCNjE8jzjTSVIpDlT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ou2gEPTX7aqjiImQgFO80NGtaPfB4RWbmiBiYnqny_fTt63fJDEUH16FExVfJrsN7HfGXKHaGg-mhnvo_4KWfBR-8HXpZIx3t43KyqZgyELmsJt2pWSYbVOvhi1l4Y_cBLXv7s-guh7p9t6g6xfNQN3wozW1t44J8zxKGPT1L-39CgiUyfdq3-5voNCViijsR0hlksRD4KVJBWGfJY5p1nI53FgdBDC9NIoXFOb3tHar_wSHki78G-AyRStkyEAV85gXl4-mlLt7ETipgLHHdwP_tvJeIw57e6ixn1pDPNGu3Plp6vMRDEiDMe8YAATd8VyfQbZGViTXxiEcNt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN7c4XElpl2PZe7iMh-n7ekn35qAAXmMbQQCfFkCOCMqD4POI8Mz4kNI0Uwd1KgtNaqfygOZdPdABHRNxoC9R8nNcH83GGKtFKoO80AgIZdSoHrG0hgTnCqWjQxAh5ZAPL9HM8bR_JQYmeo_fcfiiHZe-Dsnk248FdamBjDcAn8FePEX4bwS1zvV5ncyJIRPJ9NgZoeNrm_G_oVRiJkzyEOZtqmx2HG2Pe9VCnKUC6czXOsCfqqxD78SXNE_J0O7kR77rFlOScS6wzuK0AQE9kSr3cB0QNjlm00N63T9KgARV2VCDfOfLGA7AOf60UwtnUb9V_QiufBh5hu8-5p0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snywYiTWCxpLU_MBd5yGrQ-vT2kqmbJy0IdFszWrW9jfJwfl8lRD1VUC54Q6mWlddNRO0oPxNsF-yMTRm2iq8FnH1en3m8IHPHN_CvHUcgVakZjF3wYDSweH1zgfRzD43rD6XVBkOOl0GWJ0KoonC4rpWWk8k-ZIYpJGVZQS_e48IUNieLorS1gxQQy9eJ2hC3R_KXBkmbzFmEsmpcqnMii5uKkPl4pdmUXVZwKnEjfDa_2VRGDQNF4hHLHFrgBmoecDzXt6ys-zmQpl92qfDkWY7nn6MIuDdfWTClPYiwYesUT4ldo-4PYMuX9ug5RIsZSqt8oFG_j9YCaljM0_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7CnuN0YeqemS7gQXbluwYW6nTYoFL_mCUVBTyjm-4SeuBxXoa6FWkrQAgFG_NSuALjfBix2yp6yFT2S--jPgImw76FqATR1yMRfNa9WHdnSfKh03tHuEAejPj1seTK3Eyq6Y07oho9AwJ4IrNdes2o9pdvZMHBvV211TbzkSoMB-MIEEBfrAUvp62hDNO5eEER-undp_yqGWInfL3hoK0uBdREgd5cIp6MouZEAZ-7PDDH_1d3YeYFI5vjBbjE6zmrTpQUDGXRsNuTJ8LRlMyoy4uTR6mBSPI2hqjaYboVuDxE7Go-bDvI3w28gzP8-zoVkLu68siBGww_dypICzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDFK0gWWTVu6BNLffL40OFj73DpqmVbdFRztPV-RM900G606nB8wngy-985ARysu4Ey5l5TDfOMiwSWcH0lmW1-GeUba1c6fHy-ZaXRlf8cFVgVaxcTfk2w37kV7fOrEEgHGL3KR4z9Xs-dcjB6kCWxHxD2_LtFD_GYX0l7jXvP7s7GgfI2qH-3pTBk2CDytY4IVGJuGxZHe3F2Kw0CT1AQzn73kqd7Zbgijlw_Kfb-PYgNYoIUux6M0slx30MvaonifC69o8m0URzzxBkMGkcPKmEWzbYRs6rq1QM4AOMDPZ1ZLGO2Ep_URvW8zDGKYwZqM5_gV3eQryax2VkJTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVI_ywMLU5lFuMb6CdLgbJAglgTv3JjjCvj659n0YLLyHz3leoRhLVEZygaPWkA5WPK7HkBnLmtk1pxbsy4PV4LiyQZ2oWuJAuDWNtBpnle_KAIBJErvDk7AJJBTKa5gMhcEwrheYzkgtucdYerio5jF-TJeixnNaDSoMgoJL2fS0ipIFd8eTFVgCtqfBr5NH3oheCM6tKnAdk1EFJCINShI_LCq8nsp8-90oSvyN3jFd2bxh6D43hcJYLBTQOZiiMC9OpgCPohn_mopUb8T5R9GP72cr4mRxFLExLgNGPBE9UQze-bN9K7GyXcMLmPQvhhBoV9Y9aC_7JiubXjFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsROVTJu60XHFAEhzRVWzhSXcsL1RtbOxhSCUfThwchS7tmeynNngi3O5vUwFIXmYuXr9y4GuVBcM2URpJlrKY-OnT2Jz8QfUZrjeTFcIPBl0XUoQmqWHEGSQZa81TvjL4T5yViyvYX_Q7jQlMcaKlM7K_-P7O2lGKSlIattgFjvGlOXVxScm-0blpl1MATADXEbFYDup8Eh_gz2ZrZPXOhqEy7CKmc8nA5IAykVUv4VflMxLuS1Puc1lVJlilSbygi7ZKjt59NNO_TVndGFgTCP6W_4YhXzA7-s9wB42siL0BuubZTkdBpNiFmYMOwGUDoc7TISiWleT5qaoIfGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=QP6NNqxzTy2flDSgHSAKbS4sOo7FWd3T-giZL-DIheTjSUdBRS6j0pWyx-83XPveXxwPI0y5IYfADbPJL-geTc3YxkzYlXxd0U_QaKfkG1-1I-4h34qe_e0qoH1e_amXpdCjjigbAWfE4bWr1ZbLKWqI2SfZTkurWA_RNVcicZAGBk4EWoOLjfovplx-VfwYOx7rbmubYFZnBrCcQotq2mZ32KEuvpt1XpmamJzPLqcuVtARzMukDs_xM4N83OcLD3IonJCJ8KAvthzbXvXL2z8aagCD1VUDSFVnXahlEsR_X3U1WdMUp-cMvbw2BgdoOVKW7Z1Q48R9GOOK6ZWOGAITOOb9q4p9HuNWBaWtJ4ExcRKe-stGmhB6y4XBc5Glo_86HedX8wizNjGdgv_FsOXh80-xnFZzNsUElwIUydfJcuKCqExtPGJ1_14--ssTYp39AdCj1YhjuRCJE8fNiWwg4A2D93hnY8pKfDX3kXDReRD8jePJIpDzFSgOOpOWv_d95hCRDaoNETe-pBNs-MUTm4yyW8Kiw5k8bYTXBuRt4y7yVIeDFYdfy2Ujo1xgCaNm-4DJRBJLWt-G4e-1cFp5sD09GzPBlpY-Z4398Vm2umRfRYgdPRDLZvXt2FU7vVvkHLl-gM6zI4n49WWNxYVYg55fKV4u3VlL-GBpTvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=QP6NNqxzTy2flDSgHSAKbS4sOo7FWd3T-giZL-DIheTjSUdBRS6j0pWyx-83XPveXxwPI0y5IYfADbPJL-geTc3YxkzYlXxd0U_QaKfkG1-1I-4h34qe_e0qoH1e_amXpdCjjigbAWfE4bWr1ZbLKWqI2SfZTkurWA_RNVcicZAGBk4EWoOLjfovplx-VfwYOx7rbmubYFZnBrCcQotq2mZ32KEuvpt1XpmamJzPLqcuVtARzMukDs_xM4N83OcLD3IonJCJ8KAvthzbXvXL2z8aagCD1VUDSFVnXahlEsR_X3U1WdMUp-cMvbw2BgdoOVKW7Z1Q48R9GOOK6ZWOGAITOOb9q4p9HuNWBaWtJ4ExcRKe-stGmhB6y4XBc5Glo_86HedX8wizNjGdgv_FsOXh80-xnFZzNsUElwIUydfJcuKCqExtPGJ1_14--ssTYp39AdCj1YhjuRCJE8fNiWwg4A2D93hnY8pKfDX3kXDReRD8jePJIpDzFSgOOpOWv_d95hCRDaoNETe-pBNs-MUTm4yyW8Kiw5k8bYTXBuRt4y7yVIeDFYdfy2Ujo1xgCaNm-4DJRBJLWt-G4e-1cFp5sD09GzPBlpY-Z4398Vm2umRfRYgdPRDLZvXt2FU7vVvkHLl-gM6zI4n49WWNxYVYg55fKV4u3VlL-GBpTvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMbbpJQUVhncDOTf9WjYFwUpIhD9mWtxw7E8qXRTFFf2jSOld_zpLsWsfSEdX7FgBdxIL5kzOfxEYUR3KHT0dASqKTwUCAy_IugZsfd3o_2zrXmnGFKIdTQN9ZiMItIM9LlPMdzmeMZuf-s5wsGuVic3NJtaqvxFhc-MQ4oIUJPW_MyoIaY0w795qPaYhQQQuHu8hglVvYatcMV3IFJKwFTFMCDmoujWrNqsuy_bfe47YFiJQaWaJvxp96sblR324Oq3EQyaz8HIx6DDJd8YGLUqFrmZAgeLcCMq9ZSn5qnDLPJuCkM58kc7lZYjkwfNQ4KKhIkW7uaKkeWVw-U8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5_wowuzb4q_QO__J04giRyfNLrnapdrzGz9EyuyfIYFAx-WNWtM8me9bKzU9N0eJYYFXXoSoe_wro3lMyUKdoOQL_QwBpkOMDRwWm3JckYNCC5mK5B3LWGdrV5U39CIVbNvx6nKvmz6BqZnOKf2_XGbZhdMgzjjDrh9bMJxR5AooDC257k9lv9ZMBSXg1jJ1Z9aPQFVkmGee2r6G_zCXdfXp2mVsvDEQwlWP7d-By5oEjZGyKAnLLU6Hgr0vRDg-cqnjhbqF-tSfWh94-phT3M1YqKD6AWrj2D8Hp2FGur1fAmugylfH1ZDOGhA3i2vuNzjsmwVPqxvu3mWavd3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mrw9L3QErMGeMHjumr2h9NNECPrlxBaNTGYU1i3wA8XPdgC4HRMsUkcpPaYSCrW5kbIVtmg7I8u_2dvgvd49qnF-aJYRWD3KqBmf7Ot27X1ePaTx5ctjRrC_mggw-q8rstEBUSzbTAOj9-eMjVG79PSsmypP4HQKsHY5ZNWFT6LZzm9vT9Lf1Pebt2fhu4JR9O-Rmbau98ZscFcY2DZjVLmmDRu1tpml7IZZVgcUYo1HXvQKyfxTUAKjPRRGojFqa6mqjrYSFUWq986oYpzpoiJc0kQ7TuTVMuXkpuLbs9sgmC7byfe05naB_WPbIplzlFxJyxMrbNtNeeP1BsREeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9mwWsw4Rwq09xN51pUXc4kdoQdyioX74ODnLVKhHuU7XYB8sG9NzbAO4qDYNgmgI-dYJd36UeDvwzxtCErtVdlseFQCLPfF-YduMmFkAmXa8uYj_95_fOhoxFofWNLS3meKZCox-QcKeKgDSlYTdNKu_ph9lQhb6Z_yvZgECv23EExQOwG8VUN4LYALWj4HBiTnVPSkIJcDEHan9li3P3_NNJ5NfwxX1lX7RnLVbuKDxYEIGCIyd3Pfh_RO9lKO57IrnDS3ID78jrq_EeuL9K4_ZFSF4cCj8R5yfv_Jqn1B0EZ27XEqVOR91c9yuy5VxIHiGoMOltWctc5uT-fEiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdLk_XtztoDJc1A1gryE9NojcqLZHhwLqMhAo5iOP5cHZWFJg0NKk3zOK2Yzpapq7ZFWHQY8t3k9SHAL8II5KJacXBtthXYlHKJ8FHh8Z56nXOo_ybhVETAOkeON_GSqyUeZihVEBnpyvR20PnUFFHGWt6GrA0JPS3rDBZQd15CKEizpGPSB8B1tcMgti0rSfSX6DLZIn9-yKkwc2ebQhmCPhqU-Sinfh3UQ7GdqkeUGlgt-eRhSLiF7C_JQALiLb3OsSEbcjeyOLjRq5Wm2P2Q2-kc2tUqQXfq0w3OCgKuu2zRt2WwCiUIMpE0kUzrIFxGd0Pxc9aw07zWxAmHcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhRNa8kI5fFdnURD9Yk6OW4t9qs6rnhGXPqwCpyL4StqSSv1aTNHN3LG6m4MRmL2s_jEGPwydCBeCodQl-vS9rrXOA7ZluI-bV5-pwz4xcS0p2h0laXVPUXh3JaDhGq6bI9_S8dZbLzeTKlOxJiWp4qhrTN1lKqKeacDOEWTJNtQJbFgyBtNqwT5hBZZTCwFr2PDkAm_g-A8ChEyYJAMPTA2NXSfVPGrZkQfXG3BGpSAV356dD9kj8dAH-T8k3OJpYTlFdfjcvBJn24cnKI7gyq3oCF8KCifAdG-DeUn3Lc4Ej6plXs6Fi5OFuECAMrC_ufhNSkciRLsPcHDRXiv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS0WxcO_XTLNdjsBujQTXq4aRLkbPDYusvwjz8y2Gzz6qJ-_Up-qdqXVslMlnFLHBvfGEXI3WNdl5onyHGHcKidR7ffay5pmJplYTNkv1wP0TMDqB-4DwIu91uZ-i_yCqWlNr80zmS8OhAVfOG6htQCwT7-dm63sHe468xYwCXC83gERUklK51H4i3H5akHWhlYW-sfR6dHCsh4x3klp2-qS2h6t7QdPDTKfIEHVmzT8-FBO8iBgWL09gbrEMuuBC8e17T3DZhmCs6JlB3mIJAEqqkIxjuSVjZg6alCAvLny2LlbDYix8s-qfY4SgYum2QmtLRolYkZNQ-n0aZf7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joJmFPWAt_aE9vznp1sy0DSftn0IG9Iks-TwXTx_MPtqL7b6_ThRQndL1PtViyLeYJj87zfiw_dm4f0afqgiaFNEmNIbyBgcutpHS6_8EtsRWzEu_L589gzlchrT_ssfKo1p5c4qzq_9hWcUMqkK4lwaoAlVN5gpL0wl_i5UxKWqTFWCmUeFG6iNA5U3SXwdxYExPtensuKAHR3-OtzR6e6SwBnagpGhMbKJNrnf5oC7QGFeRFaBlY3bMVBGfZ0du206ehrrl8AWl2X89OWo71TYzrC_PDM3ntqaG0HQSb_JMWgkXOaLs9hL3_pvtBiYliz1VoiiB9cO8wlN2lR15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdO5RJZ-DkWCh7fq5hG-wsvyHIfn-T_JXvnEjWMqXleGoTTPxmFD7j2Sm0Zx9xZjpkm4-mnuz8ODZSJ24SRBkDTefy3UhJ9OTAHppqn3E2BFeiDP0zhU44Ctb_tHrKBoFUMxcDwy5W7UlviLi_A3bunwPqi81eThgbOI6u5ZDEAkCcHUpB-WXHJ3YNfwcXf1xUsRMzi0Z0oGPdz16x7jE3lju77qpqxMu3axXseLXncZb5_NATiMoV8OK_CcRwIhc6kwTMtgr8FiY70-03w_KkoMvOMAkpLDkXECMHHWaoZ2qVbRNMrpZi2WO7-K8b1AY2XsUYxCM90KxK1NwHPPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHlSJCJjVDutlRl2MUT1-p08m3gq_1PhEGk2UXelwehC_bdyR_1_hlB7VJLCSOwezSCWh0b90x-QidlN0UwEBDh1rpvOTWtK1M-ViaXZqGenNVAOsCK6FRMl2WJ9UY4hjrlOItKmtFRTr9VUis6vP-9sa-vrv0OhscOrHmUxlVncjC5r3_b-7opTjYf9D6RRsGq8qnnaAuOhqjsbmsdPk18apxVSw83GTAEAHMItrAf_6EjKc2BRM9vUOWO6kTp15hPn8HDYQ-xqXRGnAD5z3wugRAh_kT4fWn8cvuk8YhFyouSMPPkZlhLHC-49d7dz5Nr1O8jfsnf0i3otH8-PpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv826qesqMxaFmJTfR1PNA7VmwKTwXFDpxWmqYoCzKLDX7t_OT8nWibWwbHP-eSa4_71PxRGg4kJkrcwcY08pk_bCKxsyPKTZ9X8R9wxDEWZIkdaJFFwqQr2X3AlIHkINSMhN-7AB7WPh0Rwk32-ciEc2FoNXxjTvsEmP8OhqHVeu3cu87FU72e-u21SvQ8-x_9nQK4XHSVAdmitNApaHXskL_32HXCgNxS_KglEti4_O2hpApNOVHVNo5lSplJFRZwjUmGq5E8bZEP6dYUFh_xhmhyVv63XN_WQmcL19Ksg0uIyAlaO_aRkZ4d7YMx99f9AtzQTlooutZxHRvcxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs_SV7RBRoVzrZSB0-EZpV8OZAAbq6NchMP8q_ElRyaGC5xdrdX-p3bdeEGjcLhdp1iN78jiSKSE_CiDUUFzwIXnUmr43R6i57HXoT1VLNau4XoRG7S7ypP72lQnpHaG2m9nurM5QXUGrnroukatTrdjKcxVt9m71XTTvycgngW16gXgGaV_oyv9i53disbc1dE7ilwnGeGT_Fe1uxJ22_lNRGILS7_ptHGjAXACApmpdxHJ8kgTNsD67Og_Jy__HSyZrCMiP813t3HKImW9VT6M33OzhC0-ZHT4VodgIqX2Ap0wxOYZSnmDxUCyCOPEHSjuYuKTj1m7yjyre4pKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEPOUCgdwAIUhl1iIXqKirKo7JnJmrXZ8P_WzwX3fPgEcckiA2dc5mZtN_csLtKXzEZ2Mc1DSRuTBGHfVqDHDByP1SzDVnzFKpHS3bc0ShFNlb0rE-KEuiiKsfLRgie7Ew-YH2GtnfJ3ee6Egv7z37MC_tknyOFmYMKScIPGbZz_qmTQw2d7Kk3YNis3VyJu83IGWQVg_fRKptTfX8HgVVYFfTpMNMDMP_ySy5cGwtr2Dl10XhsC97s1NOynejGC3yAXogbaUw-CTwW-1-UhPNfehGg0987X3M5RJHZL3DxASmPaxK2sdOQyF32TbIE0yOtdf1I9wgVWhPUasD4iMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=RZoLarQzPIpRkg0ROGDLxIn5fyIAnWhWatEOsuPSfGr0uYclh2LCnR_NPt1M3xumowlXFaw4idPTHT2y8cSc5KEj1uus_n37U8MHH2XetBsmxHUiV0d0iC_Qmpvs1nvBDU4IPfl7r01wYXdaYCBvfRxWvP0fu8uhR14efwLI6vCoojqPSusE_riQYG4ysqRhCirgoB9l6ZCjAynM4y98YA-WAtn1Q-NtTc3jcrsiMVzhlIhn5sQxBO7pERg-qN7jkGzgllLSgeMTc_FQK7S7bHCh3vrEPhiSPLOGZzXUy-muxFb4_vPzATlZqzo-7SfTgE8MXmjpTbdw2YTbNhhueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=RZoLarQzPIpRkg0ROGDLxIn5fyIAnWhWatEOsuPSfGr0uYclh2LCnR_NPt1M3xumowlXFaw4idPTHT2y8cSc5KEj1uus_n37U8MHH2XetBsmxHUiV0d0iC_Qmpvs1nvBDU4IPfl7r01wYXdaYCBvfRxWvP0fu8uhR14efwLI6vCoojqPSusE_riQYG4ysqRhCirgoB9l6ZCjAynM4y98YA-WAtn1Q-NtTc3jcrsiMVzhlIhn5sQxBO7pERg-qN7jkGzgllLSgeMTc_FQK7S7bHCh3vrEPhiSPLOGZzXUy-muxFb4_vPzATlZqzo-7SfTgE8MXmjpTbdw2YTbNhhueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0jFLY1wDPQAiSe4HW6VC8f_on1kVrmW66jjHvUQl65mDo5I9gv9ei3UgtgZDUutOScLsnswyxtV7fFZETmmGILqOpxkjHYd-qQxtcCogJ_SwZOkL8zItFwGWO9OY86HiDIknVOPsqu2uNWnueatZDNWKb4yve_l5cCvbUSxKoNIhznGZuZ5_Hikv2QfjCuDkCzhz32iYRFcm6Ct3NfjGIcyYpeJ2rEi9v4XL_5kiIiVzrmem0KyP3CvH9dHKAD8lYGxQg-zcpa1RX0keo11KeZy0NcWqT0YpUYtl_9daJn1dnpTot9vHDGuq1_TfhOrpgztW99hfMo-YbFQ-X0RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHTNyh0a6jHrCOSZx_JTmRL75ujSicc_0zptGghlpa_FV9KsY6o0vTt_05XB-ad8F9JhTwUPHdHmn0XWCn1t0YgN9ypvHiElJ3QrMqEtUCI5mYgEJt1ZRrYqcvnWfpRbg8b09UpyKSbzyB0_GVGiArDlEOCc-QOwFvTHFIBYdUC8fvaigJ8FcAlCQAFXODKZzDtbiHN1STA-a6byitAy7kTVoq99xppUvZrE85YLMGseer4PtV8xkZ3JWFUcgAeWvAu8xMZb08RIer2Mea5RtvQVU-NNFFIWKuVQdHgcxA3-VUbMZZzQ22ZLcl3AvjXCky61BDvP_AGfK9XEedjbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

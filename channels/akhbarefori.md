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
<img src="https://cdn4.telesco.pe/file/EO0nGAgN7y0ioDz39dUd0ETLm18aF0ymHcc-WZ71t5mKinEnKubP5tVyT7PcYd8JKmO3K1r7i-GimMyqfB6KgF0fX0llHfYhQ6NZP5b6q6OVkvCRtYqtYtt8HntatS85WMWU3m20-2bZhNVe_6ltm0NRtpOSsQrM7D1lV5jAokEjNkfjLUxb5O3uzHbuZtp51KFFTBjNpZcSLQk438bWS_FVcXALVyVDHC4FaTWPu_I-DpHtQsaDXnPJv3nNVZ0WbyMbEpOHo5S72a23iZnfMCY6Dq4l1AHYmHB0T3eGBwZ9hkQrfQHFlW7CBbAN_k3XwpHj0_QbrBKrl5_52LX9OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-673618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
فرماندار بوشهر: صداهای شنیده‌شده در بوشهر مربوط به فعالیت سامانه‌های پدافندی است/ فارس
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/akhbarefori/673618" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آثژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/673617" target="_blank">📅 00:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
معاون سیاسی و امنیتی استاندار هرمزگان:  در حملات جدید آمریکا به استان هرمزگان هیچ مصدوم و یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/673616" target="_blank">📅 00:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شنیده شدن انفجاراتی در شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/673615" target="_blank">📅 00:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پرواز پهپادهای صهیونیستی در آسمان شهر غزه
🔹
همزمان با تشدید حملات صهیونیست ها به نوار غزه، منابع خبری از پرواز گسترده و در ارتفاع پائین پهپادهای رژيم صهیونیستی در آسمان مناطق غربی شهر غزه خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/673614" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00e162db2.mp4?token=KzqKUVameh21VjAGzwWhKZ-Jf90LpYkLdUKy6m6yxocaw2mBJw3oix5g5saoFUOqk5JUi7RR2SwrN0gDw09SADqq-U6w1YNyKc1Umc57lYOqcTKZZYcT5KDXL6ldZWSMb8x7Oelpt8mo9WBoADVCyeZzlX-NlB_VWANVmGdKmxM-dBPPvQJffssvTtJuE_MxeEfscgcnz2_OQR0HSQHMxy_f0siYoUDWq0o1vGeS3SZD0OnN9vXapX1ybKNgV14tbBgHkvqyKMIbsslM4TQnI0H3dAsMMxAJmKnBsClttHeNRHSTi0AfOu8nTTUmaY6lxZZmUV84UadTgTyY8OhUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00e162db2.mp4?token=KzqKUVameh21VjAGzwWhKZ-Jf90LpYkLdUKy6m6yxocaw2mBJw3oix5g5saoFUOqk5JUi7RR2SwrN0gDw09SADqq-U6w1YNyKc1Umc57lYOqcTKZZYcT5KDXL6ldZWSMb8x7Oelpt8mo9WBoADVCyeZzlX-NlB_VWANVmGdKmxM-dBPPvQJffssvTtJuE_MxeEfscgcnz2_OQR0HSQHMxy_f0siYoUDWq0o1vGeS3SZD0OnN9vXapX1ybKNgV14tbBgHkvqyKMIbsslM4TQnI0H3dAsMMxAJmKnBsClttHeNRHSTi0AfOu8nTTUmaY6lxZZmUV84UadTgTyY8OhUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله: موشک‌های ضدکشتی آماده هستند تا هر کشتی‌ای را که محاصره را نقض کند، مجازات کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/673613" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن صدای ۲ انفجار در اصفهان
🔹
دقایقی پیش صدای ۲ انفجار در شهر اصفهان شنیده شد.
🔹
هنوز علت دقیق و منشأ این صدای بلند مشخص نشده و تا این لحظه هیچ‌کدام از نهادهای رسمی و مسئولان استانی در این باره اطلاع‌رسانی نکرده‌اند/ مهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/673612" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
رسانه‌های لبنانی از حمله توپخانه‌ای رژیم صهیونیستی به شهرک «لنبطية الفوقا» در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/673611" target="_blank">📅 00:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: لحظاتی قبل صدای ۴ انفجار درشهرهای چابهار و کنارک شنیده شد، و مناطقی مورد حملۀ دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/673610" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فرماندار بوشهر: تاکنون هیچ گزارشی از اصابت دریافت نشده است/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/673609" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/673608" target="_blank">📅 00:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=u-Ty-zh-O0ZqLkZ3HlWG2cdCPuCB_tw75ymiANouE9mMxdPP71BXp11B8plhVCosxrGvcvPviEhaYBd0sJ7Fc_oES-6Wi_sa97EC20vo1thqjV8SaJ5W8oSKBoGlaDn9dQEZVUFKHb79XOK0VeIyiQmIHQKm9TK5M4yeY1IjcqUYUNa1VNyRJfGOnwiEn-nKj09fufHg52E6d65qrtkl-NlkR4N0VC5g2uSm8JvkdvHK2tOMcP3nGJ5iCG0lqAyjHWA72kDBWYiS6-tuM9uPjAFK28Ic0q_Rsp3pey_r1rwcOfubLPDGIAGLTXQe9jUG1sdFlgC8AL28IDfaFSJIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=u-Ty-zh-O0ZqLkZ3HlWG2cdCPuCB_tw75ymiANouE9mMxdPP71BXp11B8plhVCosxrGvcvPviEhaYBd0sJ7Fc_oES-6Wi_sa97EC20vo1thqjV8SaJ5W8oSKBoGlaDn9dQEZVUFKHb79XOK0VeIyiQmIHQKm9TK5M4yeY1IjcqUYUNa1VNyRJfGOnwiEn-nKj09fufHg52E6d65qrtkl-NlkR4N0VC5g2uSm8JvkdvHK2tOMcP3nGJ5iCG0lqAyjHWA72kDBWYiS6-tuM9uPjAFK28Ic0q_Rsp3pey_r1rwcOfubLPDGIAGLTXQe9jUG1sdFlgC8AL28IDfaFSJIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده صداوسیما از استان هرمزگان: در ساعات اولیه بامداد امروز، صدای ۳ انفجار شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/673607" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در کنارک
🔹
همزمان با پرواز چند جنگنده در آسمان کنارک، صدای چند انفجار در این شهرستان شنیده شد.  خبرهای لحظه‌ای حملات امشب
👇
khabarfoori.com/fa/tiny/news-3231914</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/673606" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چندین انفجار در چابهار
🔹
دقایقی پیش صدای چند انفجار از حوالی چابهار شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/673605" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در کنارک
🔹
همزمان با پرواز چند جنگنده در آسمان کنارک، صدای چند انفجار در این شهرستان شنیده شد.
خبرهای لحظه‌ای حملات امشب
👇
khabarfoori.com/fa/tiny/news-3231914</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/673604" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
وال استریت ژورنال: آژیرهای هشدار برابر موشک‌های ایران جاماندند
🔹
موشک بالستیک ایران به واحدهای پیش‌ساخته در پایگاه هوایی موفق السلطییط اردن برخورد کرد.
🔹
آژیرهای هشدار قبل از هر حمله به صدا در می‌آمدند، اما اینبار پرسنل به پناهگاه نرسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/673603" target="_blank">📅 00:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شرکت هواپیمایی ایرفرانس تمامی پروازها به ریاض و دوبی را به طور موقت تعلیق کرد
🔹
شرکت هواپیمایی ایرفرانس در بیانیه‌ای اعلام کرد که این شرکت به دلیل وضعیت امنیتی در خاورمیانه تمامی پروازهای خود به ریاض پایتخت عربستان سعودی و همچنین دوبی در امارات متحده عربی را به طور موقت متوقف کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/673602" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
همه سناریو‌های حمله زمینی به کشور و نتایج آن/ نیروی زمینی آمریکا احتمالا از کجا وارد خاک ایران خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3231685
🔹
آغاز جنگ تمام عیار یمن و عربستان / انصارالله محاصره دریایی عربستان را کلید زد / چه بر سر ریاض می‌آید؟
👇
khabarfoori.com/fa/tiny/news-3231838
🔹
آخرین گمانه زنی ها در مورد احتمال مذاکره جدید ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3231846
🔹
حاشیه‌های یک عکس در مراسم بزرگداشت داماد رهبر شهید؛ این نوجوان کیست؟
khabarfoori.com/fa/tiny/news-3231705
🔹
جنیفر لوپز فاش کرد چه چیزی یک مرد را برایش جذاب می‌کند
👇
khabarfoori.com/fa/tiny/news-3231848
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/673601" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در چابهار و کنارک
🔹
خبرنگاران ایرنا در حال پیگیری منشا این صدا هستند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/673600" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
قلعه‌نویی: شرمندهٔ مردم و بازیکنان هستم؛ ما می‌توانستیم مردم را در جام‌جهانی بیشتر خوشحال‌ کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/673599" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔥
خبر منتظر نمی‌ماند
با کانال خبری ما، تازه‌ترین اخبار و تحولات را سریع، دقیق و بی‌واسطه دنبال کنید.
📲
عضو شوید و کانال را با دیگران به اشتراک بگذارید.
@Parstimesnewsiran</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/673598" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ایرنا: منابع غیررسمی از شنیده شدن صدای چندین انفجار در بندر عباس و قشم خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/673597" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U49ukol5rcIhCMsysmt0LzO1aVDiO9rFZViQbSkNKuYLYyXyQib9RJ0dzKaNhLZ7A9Fx1YuyJtURGfozFDVBe-4V6xl1Q3T8scfb-m22JY3wvHMuyF1iH_l599o_FpKfzZigneLkBU4vXb9eCrkNwuKwltlU8OQTAPxXpx2LFvhpNtB84tVxAICqNnEl4D993sD5iETpUXTs2SCvfwW0rBMxN35LiaA8tfhlQ54vcv3Y0zo5GLZHHhYEBYT69LWojWR7xKleBK0MTrcOAyH1I048JK86RNNvHsJAWKyUHHlNdxTP0QC2qzDmC4lEUzwqoKjOtvzWcwlM0w8Dqx6hGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/673595" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673594">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ائتلاف سعودی: ما از کشتی های تجاری خود در تنگه باب المندب محافظت خواهیم کرد و به منابع تهدید قاطعانه و با قدرت پاسخ خواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/673594" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673593">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای پدافند در حوالی نیروگاه بوشهر
🔹
دقایقی پیش، صدای فعالیت سامانه‌های پدافندی در اطراف نیروگاه اتمی بوشهر به گوش رسیده است
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673593" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673592">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: صدای انفجار در بندرعباس شنیده شد  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673592" target="_blank">📅 23:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673591">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvjAO4p47PaZ3mkfvqlJj_z6Hu5o5e610GSdfkbzsicmTfpMnW_y6PkWc_XIjqeJklTmFhmxuestBT-co9nh3pqHg6GWTTd3vWjLkonnwvYT80fuoRE_MhdDJ7Csg-1Tc2IIAC9Kuw2cMHspPkX50i19oTehf5G2ORB6a4LnlNU3bh4GGx1HKnAlB4nmRHEtjBiB0VtNKHtxGWlYXNaQsiEEKK4lRcRRyZ-MwIjMVG9t1B528sdDqhOafIQG48DC1WqcL2Yd0djorYemVcsiZK5FQ1wPEMO56PFplLKLXOi7qREFfFcd76aUsig_ClIe7CmrpJHDYMNNxBx_zjT4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سنتکام: امروز، ساعت ۴ بعد از ظهر به وقت شرقی، نیروهای ایالات متحده به دستور شیطان زرد، دور جدیدی از حملات علیه ایران را آغاز کردند/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/673591" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673590">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ایرنا: منابع غیررسمی از شنیده شدن صدای چندین انفجار در بندر عباس و قشم خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/673590" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673589">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: صدای انفجار در بندرعباس شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673589" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673588">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سردار قاآنی: رژیم صهیونیستی نه تنها مقاومت را متوقف نکرد، بلکه مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه خواهد داد
پیام سردار قاآنی در پی انتخاب خلیل الحیه به عنوان رئیس دفتر سیاسی حماس:
🔹
با عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های بزرگ حاضر در حماس و نیز همه رزمندگان این جریان عظیم مقاومت اسلامی تبریک گفت. آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/673588" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673587">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزارت خارجه آمریکا در  یک هشدار امنیتی از شهروندان آمریکایی خواست درپی افزایش تنش‌ها در خاورمیانه، سریعا ایران را ترک کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/673587" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
یک مقام آمریکایی به آکسیوس: ترامپ در حال حاضر بر این متمرکز است که ایران را به‌خاطر نقض‌های تفاهم‌نامه و اقدامات مستمرش در تنگهٔ هرمز، هزینه‌مند سازد
🔹
علاوه بر این، رئیس‌جمهور ایران را به‌خاطر کشته‌شدگانِ اخیرِ سربازان آمریکایی نیز هزینه‌مند خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673586" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مقامات آمریکایی در گفت‌وگو با سی‌بی‌اس اعلام کردند که در حملات هوایی ایران به پایگاه‌های آمریکا در ماه اخیر، نزدیک به ۱۰۰ نظامی آمریکایی مجروح شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/673585" target="_blank">📅 23:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
جاری شدن سیل در منطقه نورستان در شرق افغانستان براثر بارش باران‌های موسمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673584" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3864aa1d5d.mp4?token=OMSIYjtOSCarHiVKrL0N0qoJtPW7e50jK47RGEyNwjyXVdSTEFrjEbIgR2DiNGNAVcbn8NGQ1NDX-8NEU0UfzgYSnsy9V0c7LWAwo0R62lFjvCDxpyuOdJhVsc6gWflhplyY3nyGdsYdJVP0vo_EH7coxjeaWT-VvYX57l7-LBj2Ved2XRCcMQ6AzF8xeaOPmLFoYCCti7vB11MY_6G-JD94-6XmZ0xMUgt91shF8bpTSA5CZFelPI2QJISloTmDxvZ6QOJ-Dcdvas2UcAhv6iCoWa_7nRfa19gZr2nf-nHVMi9EBAfjQHs4GgGFQcdaHEVwwM4EWlYMwScYrMWM0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3864aa1d5d.mp4?token=OMSIYjtOSCarHiVKrL0N0qoJtPW7e50jK47RGEyNwjyXVdSTEFrjEbIgR2DiNGNAVcbn8NGQ1NDX-8NEU0UfzgYSnsy9V0c7LWAwo0R62lFjvCDxpyuOdJhVsc6gWflhplyY3nyGdsYdJVP0vo_EH7coxjeaWT-VvYX57l7-LBj2Ved2XRCcMQ6AzF8xeaOPmLFoYCCti7vB11MY_6G-JD94-6XmZ0xMUgt91shF8bpTSA5CZFelPI2QJISloTmDxvZ6QOJ-Dcdvas2UcAhv6iCoWa_7nRfa19gZr2nf-nHVMi9EBAfjQHs4GgGFQcdaHEVwwM4EWlYMwScYrMWM0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله حریدی‌ها به «زندان ۱۰» اسرائیل
🔹
در پی بازداشت یک حریدی توسط مقامات رژیم صهیونیستی، گروهی از حریدی‌های خشمگین با تجمع مقابل «زندان ۱۰»، دست به اعتراضات خشونت‌آمیز زده و موفق به تخریب بخشی از حصارهای امنیتی این پایگاه نظامی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673583" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=i8KBN8-DICASqlGW_MI-zsgD0rrc_ZAWQeaPBZyvXUqpJxLZMrCYExDNTH20LxB9JoVX8oQGakTGVY4HApPn2b4xLGaO2wHKs5ESbeO81UKdqbLB7PWK2iy8VuarghfRA2kpIFpk9Tsve12yzhhEyBdkb7NIUlWHF2cqVUmN2Ng_dO2U0aI-32EfvQ5CJk6StchG7Vu1jRhRuAkhWEmsng755trC55uqI8X6DBV3kkrW8AHge-kfj0l_sO7jkxXE-YUmVfnK4Oyl2TovpHlfCC8jYxmknPQXPcggd-TNInUarCqM3Q_tCT8G0-zu5Je8-orK8wL9HrtO_QNM4sBZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=i8KBN8-DICASqlGW_MI-zsgD0rrc_ZAWQeaPBZyvXUqpJxLZMrCYExDNTH20LxB9JoVX8oQGakTGVY4HApPn2b4xLGaO2wHKs5ESbeO81UKdqbLB7PWK2iy8VuarghfRA2kpIFpk9Tsve12yzhhEyBdkb7NIUlWHF2cqVUmN2Ng_dO2U0aI-32EfvQ5CJk6StchG7Vu1jRhRuAkhWEmsng755trC55uqI8X6DBV3kkrW8AHge-kfj0l_sO7jkxXE-YUmVfnK4Oyl2TovpHlfCC8jYxmknPQXPcggd-TNInUarCqM3Q_tCT8G0-zu5Je8-orK8wL9HrtO_QNM4sBZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673582" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673581">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از حوالی سیریک
🔹
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست‌.
🔹
در ساعات گذشته برخی منابع محلی از شنیده شدن انفجار از سمت دریا خبر داده بودند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/673581" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673580">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی در گفتگو با الجزیره: گفت‌وگوها بین ایالات متحده و ایران ادامه دارد / انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673580" target="_blank">📅 23:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673579">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9FdMWQsSA_Hd-ofMpDuW5-6P14Fq6G8E6o0WBbMdRi-mOv6KTmm9ufLGVuBH_HyYwZGBoC9QykKJnUGsXrhGwGPDXiILc22FOO9qBx44VydhmstHAOS_JV2FjiY1yh0JHACp8IjjwFct97PseG42RGBN_dFMpwS-eqLTogCpnsB1ONLGcmM_hkJSzvFEKsHjas7JRrdiY-2YLzbfht-smkS3N8HawPior3GXOK4Z1MiDeuCZeRfAjc4lpFrEGJWQ5GMmmNzB6m3xi_Pku2708R2CDMWgyRy_7XId9yI_4YhV5JGUDV9PERaexXjWgwB1cfw8f8EkIYohLdCY8ruiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ می‌دانستید که بدون دانستن تاریخ و علوم تجربی نمی‌توان به یقین رسید؟
🔹
امام علی (ع) برای رسیدن به «یقین» چهار راهکار بنیادین ارائه می‌دهند: ۱.بینش هوشمندانه: شناخت جهان از طریق علوم تجربی. ۲. درک حکمت: تحلیل عمیق هستی و علوم نظری. ۳.عبرت‌گیری: درس‌آموزی…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/673579" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdXXcAMWSpzx1rREl3d_5y2Ctv2fBwiuhqn-nPCYlLAzBj2Y2Vyx_D9P-AFtwpXFXIV6JHJnR2jDd6spiAQGuEB87m49rkhJiVUqfKp3TkTOdR2-2aO_ORtXYQTtAZ9ZtVmlT0ReuH2GpE_syNfryuusV9METfYUXvqynRKioYuc5Xdb7nMnnOj0aTjNcTneoU3czQR0taUj9TcgI60KfVoZxSfDgX2EmbyIhtjA-nQtevCgZHfP5PKuFZMXBOB-GLkIYV7fR3EOTfhr2eNLOKlmqYSI5XJHI7BfiXBd-Glfd62etDf88CGHNJQoiSAVAZt444iJ8U4rwnOtJXqLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKJe3CtLZtnFGZ3LX7YGZVAlEQYxm5p5LWzwHVwjEWGhdGUy36kumqtFIiEAxzv2zJ5eRmzN0O6q56mPLytwHIAWyj-Ho3Y6Lh0s2Atawn4OMpCf_W91mMCM49xh4jDGtAtBs87yIwF9N0skzHZ1vNlT1gusQ8Xt_GRbWqYR6nA1DFL5gouPW83gAZvFFkmVG7lAMXwU_fZvLEw0VLglUWqAMj5p3xHFYAp-8H0nIX8i6KdtuLRbnitXgvuy_Jp-LrVFmcQQn5vfqhbBQZmqvzPmZ3Z339uv8tQbXFP3nnQaOr8aCxhjzMErPdqyaKOcajemTw0fjlcUQifK5grMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yx_To2wmzXTy2FY6U8ycEFFdXctYqRtR83ox0CFpViYVVKKj20lFb8lPDPl4G3ErUlqZ3UEKhd5DRDl0NYXCRsxUBO6f0tfv5Ikhl8Z9jUu5_SaA5oT44LgGl3ooqJt3QIru5FeJrYf1FbT-HrDj8zayiEN8Q-XN9szkQ1WaiEtQ2H5gzc0c_UxyutW6qCFUAbxItYlNMTeKraXUb9oBXEO_7nUBRULHbAq4PGETCUuPJQWZeqcHiuAs0kyOiLeM5oTXDDTOTcR593lhk5jQOWVXeM-rdZ-5f0-yEu61AYqvlcBQwQSHD1vexDGmYLbZwrsLwufVJv6rqejzugnZuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لباس به‌جامانده از شهیدِ جنگ رمضان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/673576" target="_blank">📅 23:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673575">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgjUnJIuMoM9hQcRJgiUuHRjXpxOzpdkb3QSfMrfYZayvUuZe33mIc8Ykc8CRuhtc4Jn-B6kaBe-UvEUTyepOovsAssXdx4X0NOAR7oRr3A0fwEQUlNgqVQ7QJcJefn-FnmB_OsjPpMmIGUj98lyuegUTbi-7Gcr9Uif7myDemVjDmwVETxIl_vAURwh-uAaJV4b-ZqxR0iA6cmvs3b-P30AmX79-l05ARUiUOO4dzAhRXv3xxZJfzKR-GztS9cRN_7eMO0S23VMnBlBMuMi-5RCTlmXRxBYDSDPEO0bWCzPrExPrYNeqnMv1DrrNqDcc-RgLubwYlFeHTs7eWoaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کاهشِ بیش از ۳۰درصدی وزن بدن با آمپول‌های لاغری!
آمپول‌های لاغری، داروهایی هستند که براساس مکانیسم علمی شناخته‌شده دوگانه GLP-1 و GIP ساخته شده‌اند و با تقلید عملکرد هورمون طبیعی سیری در بدن، باعث کاهش اشتها و کنترل بهتر دریافت کالری می‌شوند. این داروها بدون ایجاد گرسنگی شدید، به کاهش وزن تدریجی و ایمن کمک می‌کنند.
این آمپول‌ها با تجویز پزشک و به‌صورت هفتگی تزریق می‌شوند و با آغاز و ادامۀ مصرف زیرنظر پزشک، می‌توانند باعث بیش از ۳۰درصد کاهش وزن در افراد مبتلا به اضافه‌وزن و چاقی شوند.
اطلاع از قیمت، نحوه مصرف و عوارض آمپول‌ها</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/673575" target="_blank">📅 23:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673574">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فرماندار بوشهر: امشب اصابتی در بوشهر نداشته‌ایم
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/673574" target="_blank">📅 23:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673573">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
باقری کنی، معاون دبیر شورای عالی امنیت ملی: وحدت بین مسئولان وجود دارد و دوگانگی که دشمن القا می‌کند، دروغ است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673573" target="_blank">📅 22:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673572">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4BKt7sVB8ybrVXNo-4tY7Ly-u-WlfPkF585Qy9gKrXjQnrqoM9A3Fy6I5eg94oh0La1IE-HbLQxHgBjUwi_c5E8D-ah5MzesUMZsmAaegPIQTKN3ByyQGRxS_aicY6rshfmYlDRp12j1-3WtfD-VWWkT4P0RbJ3gXrAw-t5k_MgZXlUFnIG7XmrV9ZEMV0WnP-GnLFUq7N8b0murJnHelzTWa1G6_7lcfuxh6h1HvXQmnwNV_QGc4gOE7pDFBHy9EZAPvPpsp17WdRS_0mwUXtjjhE0z1vU17kpEh_SRoAf3eArpSjX5ojoRzosOmAtfwFMvPDDziIAnRcwiu2xkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار نوسان قیمت نفت برنت در ساعات اخیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/673572" target="_blank">📅 22:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0860ebe2a9.mp4?token=fgBbyj2Zqshyo0oHOeD1sORj1LF3_qzhYAkznTZ4iUlGD2eaNylxlXA5YZjMQRTA4wkwQ0tB0E_FM52UZDcDvGtTpVoyUmwprTRMATnKsJFEEqS5Ow6Dlpo4n5W2o_SkBAx0sXVdczaK1HoVHky809XacklCFL8P9J7NinRsQczbcwXu_-WG7hXOwYTQS7lMC5tcE3MM9q3LqTNnc536w7HYiZtKSOBcJNoH2owjq_bmJw3V3eGgltLSKIK9yP9gufq7fAVAaGfNbfiJqpDsCYxBHZqgoSHVPAgeyHa6WuAmhZSrMBXuHWNFEnmkKDhKAwcR2D07olOTvRTXx64BLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0860ebe2a9.mp4?token=fgBbyj2Zqshyo0oHOeD1sORj1LF3_qzhYAkznTZ4iUlGD2eaNylxlXA5YZjMQRTA4wkwQ0tB0E_FM52UZDcDvGtTpVoyUmwprTRMATnKsJFEEqS5Ow6Dlpo4n5W2o_SkBAx0sXVdczaK1HoVHky809XacklCFL8P9J7NinRsQczbcwXu_-WG7hXOwYTQS7lMC5tcE3MM9q3LqTNnc536w7HYiZtKSOBcJNoH2owjq_bmJw3V3eGgltLSKIK9yP9gufq7fAVAaGfNbfiJqpDsCYxBHZqgoSHVPAgeyHa6WuAmhZSrMBXuHWNFEnmkKDhKAwcR2D07olOTvRTXx64BLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری کنی، معاون دبیر شورای عالی امنیت ملی: وحدت بین مسئولان وجود دارد و دوگانگی که دشمن القا می‌کند، دروغ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673571" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673570">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ffb0ad7d.mp4?token=lAE3p7IBEgdZWBdxDNxQuYEk9k_yq12bB6TEQPtCJaLJbUCObeOM_ptifrhkJNCj-IsbaZ2Yly1N8Nbb5GPs4kX9klSw0jaL1errEcTkMhhZZkg72wci0VfSLiBRQPiLHgoF4f1WvR9utI-xcBMWw6O-mpZFA8BTl7z11dDeetBrwlTo5Oqn5Ngbiey5jht2tVPTPU8s6FAZHQX8MNTTZo_V4ygO2oDs85w1soWvFhEF7hpSj53RMtv5i704rIqz4uAq7BXdS6aNXMGIxI80doiQ1pVLUUln9iKwTQ42xiBAQgC61M-DtFPh1-8qwSpTieGrWSlcvkEpZwqou8xsrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ffb0ad7d.mp4?token=lAE3p7IBEgdZWBdxDNxQuYEk9k_yq12bB6TEQPtCJaLJbUCObeOM_ptifrhkJNCj-IsbaZ2Yly1N8Nbb5GPs4kX9klSw0jaL1errEcTkMhhZZkg72wci0VfSLiBRQPiLHgoF4f1WvR9utI-xcBMWw6O-mpZFA8BTl7z11dDeetBrwlTo5Oqn5Ngbiey5jht2tVPTPU8s6FAZHQX8MNTTZo_V4ygO2oDs85w1soWvFhEF7hpSj53RMtv5i704rIqz4uAq7BXdS6aNXMGIxI80doiQ1pVLUUln9iKwTQ42xiBAQgC61M-DtFPh1-8qwSpTieGrWSlcvkEpZwqou8xsrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باتوجه به افت‌وخیز حملات آمریکا، اقدام بعدی آن‌ها چه خواهد بود؟
باقری، معاون دبیر شورای‌عالی امنیت ملی:
🔹
آمریکایی‌ها الان خیلی محتاط‌ هستند که بخواهند وارد عرصه هایی مانند حملات زمینی شوند که ریسک‌های جدی دارد.
🔹
اهداف آمریکا در یک چارچوب مشخص نیست. ظاهرش این است که در حال آزمودن گزینه‌های مختلف هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673570" target="_blank">📅 22:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تعطیلی ادارات منطقۀ سیستان و کاهش ساعت کاری در سایر نقاط استان
🔹
به دلیل تداوم گرمای شدید هوا و وقوع طوفان گرد و غبار، تمامی ادارات منطقۀ سیستان فردا تعطیل و ساعت پایان کار سایر دستگاه‌های اجرایی استان به ساعت ۱۱ محدود شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673569" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358d0a6f1f.mp4?token=hzlHVRWWxkMUqc7cY474HMvyLY7ldu3hf9LJGfplWk27mjndNv1ZihDDJ_ODRI_5IA0arAOIi7iSDKMsiwyYul31hrMYOGCCZ8X8EcIweQUINFhW661Qu16gBf9a2xEOILe6HayRL8FRt7k4JEVA43kspfR9oFGUZuU7zl5l6rZAI5_5YxmhGRkMts0UV1or2SkuewMH1CEJMScao-t4Ng3eucovLkP2Fb-hIGPj-sYRkKQzJgIB2zkBrsPf_rFBDU4BWFsY_M-kRDmIXJX0oKokBrcVY1wFczl7CLPmeRmW6OZ4V9LAj2Y_nAXklFECHxO2jzlPSGbilELODrNu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358d0a6f1f.mp4?token=hzlHVRWWxkMUqc7cY474HMvyLY7ldu3hf9LJGfplWk27mjndNv1ZihDDJ_ODRI_5IA0arAOIi7iSDKMsiwyYul31hrMYOGCCZ8X8EcIweQUINFhW661Qu16gBf9a2xEOILe6HayRL8FRt7k4JEVA43kspfR9oFGUZuU7zl5l6rZAI5_5YxmhGRkMts0UV1or2SkuewMH1CEJMScao-t4Ng3eucovLkP2Fb-hIGPj-sYRkKQzJgIB2zkBrsPf_rFBDU4BWFsY_M-kRDmIXJX0oKokBrcVY1wFczl7CLPmeRmW6OZ4V9LAj2Y_nAXklFECHxO2jzlPSGbilELODrNu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری‌کنی: آمریکایی‌ها در مورد آزادسازی دارایی‌های بلوکه شده ایران هم کاری انجام ندادند و نقض عهد داشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673568" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTJibwWFlhCFeKkKlcRxtMAhj01kEp8PcFH81LF0w6iKBPyzR5AEYyZalhfRDdO48-nj8Nf5QF69sIEZ-VhD8P8AVgS0j894P4g_4xAt1_VqHsQ6VqIwUnz2RZf1wSDUpFgBaW6u6g-eehEOmgiPZWSCwu14DskwK9PWvgOxPmRdmLFtx9Ifd2Lb4xjpRTT-7D0DoKLQS_Wx1qxi7nR8Ojpht9mgMoTjcjAL8Ygg_SClf4Ng8_4wHAcXa6To-ZM-x74cC_CLfZlJbqKeoyGv-51bbq2Kq10UCfFRDhuqtZVDRbXglcACE_ZupoqU2Rowm9HFu01-l06Y4nFOXra-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یُمن یَمن
🔹
نیروهای مسلح یمن با انتشار بیانیه‌ای اعلام کردند که بر اساس راهبرد «محاصره در برابر محاصره»، محاصره دریایی علیه عربستان سعودی را از زمان صدور این بیانیه آغاز کرده‌اند. در این بیانیه تأکید شده است که این تصمیم از لحظه اعلام، لازم‌الاجرا خواهد بود. هم‌زمان، برخی رسانه‌های غربی این اقدام را عاملی بالقوه برای افزایش تنش در بازارهای انرژی و حمل‌ونقل دریایی ارزیابی کرده‌اند و از احتمال پیامدهای اقتصادی و نفتی آن سخن گفته‌اند. در صورت تداوم این وضعیت و تأثیرگذاری بر مسیرهای تجاری، برخی تحلیلگران معتقدند این تحول می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه به نفع ایران اثرگذار باشد.
🔹
هشتصدوچهاردهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/673567" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
افشاگری روسیه درباره هشدار ناتو: آلمان یک سال تا بمب اتم فاصله دارد
سرویس اطلاعات خارجی روسیه:
🔹
یکی از کشورهای عضو کلیدی ناتو نگرانی خود را درمورد تحقیقات مرتبط با سلاح‌های هسته‌ای در آلمان ابراز کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/673566" target="_blank">📅 22:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f4d8f724.mp4?token=PGBILAnIlb1t9cYRMQJ3NcVY0fGs3wX_IV7UOqemh-pYaTTyVTcl7TZtjklbwYTGrmOAdQOPBxlNLlU7xSnWzEn6qYy34bujCiWGTLfna3-fX4mOc0UB_V7KLSGn1m4IlZ0lpXwJNwqrLcgwsil_DuXlhB8DBD5ZjOmSPrb7KR-u7HvCQvIE_nX3QnTs_GvzUqB6PhfjU2zpS6q4QeOneaM5uR4RMCCuWWasavuCj-I97spHFXGoGDhhL7V9Oh-033wc2H4-HoINRUy7bI0WaOWdeA-RNLtkq6vaWarQ8Izy3acTi7h2oOjF7tyQ8rPv4YHr6XpTVOKrT8NHV2OA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f4d8f724.mp4?token=PGBILAnIlb1t9cYRMQJ3NcVY0fGs3wX_IV7UOqemh-pYaTTyVTcl7TZtjklbwYTGrmOAdQOPBxlNLlU7xSnWzEn6qYy34bujCiWGTLfna3-fX4mOc0UB_V7KLSGn1m4IlZ0lpXwJNwqrLcgwsil_DuXlhB8DBD5ZjOmSPrb7KR-u7HvCQvIE_nX3QnTs_GvzUqB6PhfjU2zpS6q4QeOneaM5uR4RMCCuWWasavuCj-I97spHFXGoGDhhL7V9Oh-033wc2H4-HoINRUy7bI0WaOWdeA-RNLtkq6vaWarQ8Izy3acTi7h2oOjF7tyQ8rPv4YHr6XpTVOKrT8NHV2OA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر حضور موشک‌ها در آسمان اردن از دوربین یک شهرک‌نشین صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/673565" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb36943633.mp4?token=YAcnQTxp8LGMANS3QEU9mA_MR8skM8O68HSFCfGiIH_arjjKwDrXSS6C7e4w2-XcgS8GoEDYBivSst9Z3fuCPXuBfOv-GzPuJYGYRNZllJABb-1EEIt3F0OLeDyJiahrHcFJYcoe2Ed3-U6IUDOQ5CTjTnC6X61EUn7UQzdAqVFaA_U3x4CXw_Kc9KmGkbgKjb_bAlc_IMozTUtRgxfc8tukrv7c40eiZilNes7mlysicFPcvTayk_U-fScHKKt3PEi78HHp4Mb2FKIDp_5VU7tZF_3_w7mVv-X2c3TFYfLTwb4hhfvTalzSTKBC0IQKpSkCdWzMeLBTwxsj4vg0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb36943633.mp4?token=YAcnQTxp8LGMANS3QEU9mA_MR8skM8O68HSFCfGiIH_arjjKwDrXSS6C7e4w2-XcgS8GoEDYBivSst9Z3fuCPXuBfOv-GzPuJYGYRNZllJABb-1EEIt3F0OLeDyJiahrHcFJYcoe2Ed3-U6IUDOQ5CTjTnC6X61EUn7UQzdAqVFaA_U3x4CXw_Kc9KmGkbgKjb_bAlc_IMozTUtRgxfc8tukrv7c40eiZilNes7mlysicFPcvTayk_U-fScHKKt3PEi78HHp4Mb2FKIDp_5VU7tZF_3_w7mVv-X2c3TFYfLTwb4hhfvTalzSTKBC0IQKpSkCdWzMeLBTwxsj4vg0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ای که پدافند هوایی در اردن فعال شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673564" target="_blank">📅 22:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c85e19207.mp4?token=Kyex2tA7EUGnq-Kuja6EBOf3ZqM6HdYwkJH3UPp23cHPdKPhp4pSzpRs4L06B_aSac8WXsFrk2IkC6D20cWnWJh_k4qCeQuPf-vGQf8wzBf7izK82_ZoShuZauLdp6cf4SvrYfqUFXsfPDUn1fINL_OnFWVHqdLvJ9QdqJK8a-QyinKFpEKFsbNVom30rwhfpOQ4J5EubkyxBF46puxo1-8DJiwR6uXaJwo5v9a6QCIyfExtWtjkLPZhRkDvXDa7KMkRzA2n_8h5Gk_s-TbXMhesdegX4lz5BZW2gij3_FxM0rIADxtBYZYDkrRlFKTCf84nHvBnNRsX4teS1A4chQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c85e19207.mp4?token=Kyex2tA7EUGnq-Kuja6EBOf3ZqM6HdYwkJH3UPp23cHPdKPhp4pSzpRs4L06B_aSac8WXsFrk2IkC6D20cWnWJh_k4qCeQuPf-vGQf8wzBf7izK82_ZoShuZauLdp6cf4SvrYfqUFXsfPDUn1fINL_OnFWVHqdLvJ9QdqJK8a-QyinKFpEKFsbNVom30rwhfpOQ4J5EubkyxBF46puxo1-8DJiwR6uXaJwo5v9a6QCIyfExtWtjkLPZhRkDvXDa7KMkRzA2n_8h5Gk_s-TbXMhesdegX4lz5BZW2gij3_FxM0rIADxtBYZYDkrRlFKTCf84nHvBnNRsX4teS1A4chQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری‌کنی، معاون دبیر شورای عالی امنیت ملی: جهاد تبیین لازم است تا دشمن از رخنه‌های ابهام در ذهن افکار عمومی رسوخ نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/673563" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تصویری از موشک ایرانی در آسمان عراق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673562" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEnhWjcIcBkkS_Z4iJYHKDhAIfH-WvqEfgELUQMB6qRcjhzN1qfeOX9Cu-OfU4X9F-wM_Mk7eFdrx2-_lTCTPiPFFr0a-wATHrate0LmT_voLDtawaU6W1ihY8zVz3B5t8OGmmMRJ-_f8aMYB2nYZcdM_7vouwccbG0qD2cou5z8UB3exqar7Uh_Ak21FcQ0CuZFGlaje9kyNA08C4LZ4hYFc1x4t9oa8yjd3agDPxlCiqkXjbX0pUe0faxQdXTLDnjXFzi0XCq5L4K9SNV-iYgyPGjBx2x3lmN4VWqMs_EA5dyMvZztb5Wl505Xc1UOTX9h9YZJhx-8DNUq6sKMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک فروند موشک کروز دشمن آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
روابط عمومی سپاه ثارالله:
🔹
یک فروند موشک کروز دشمن آمریکایی در آسمان رودبار جنوب در شب گذشته توسط سامانه نوین پدافندهوایی سپاه ثارالله کرمان تحت مدیریت شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم گردید.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/673561" target="_blank">📅 22:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=T6vzWaxNehMtKHmDIpcIq5e0Eyan2juyY8m_6C3w00A9L6Y_D4VsmPrwAt1CzRE_dcgPKvXPutYGXwLpOKMvORndvxtQMSCaq5PFykcN8BkD_sKeL9KmrmOtUlNMl9OLJfZqzIDS76YSUgWpEpM9dGKlxnlwVh5vFBXwfF5-Vl3fmoFPta-UN6Ityqqq7wrf-KhYM9yxrkieoUiviiaGPMdiJBH1QAGq_ABvzhRyXkoiRjRHBxlIq2_fm5yc6-icpMah0TS-erPfGOspPyKPXhynFqO_8IAzj-TfxONjPAHkD_tAgFqOJYeGDVqZ-5v_m2SvLNI-d-RY6OXNIiyvxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=T6vzWaxNehMtKHmDIpcIq5e0Eyan2juyY8m_6C3w00A9L6Y_D4VsmPrwAt1CzRE_dcgPKvXPutYGXwLpOKMvORndvxtQMSCaq5PFykcN8BkD_sKeL9KmrmOtUlNMl9OLJfZqzIDS76YSUgWpEpM9dGKlxnlwVh5vFBXwfF5-Vl3fmoFPta-UN6Ityqqq7wrf-KhYM9yxrkieoUiviiaGPMdiJBH1QAGq_ABvzhRyXkoiRjRHBxlIq2_fm5yc6-icpMah0TS-erPfGOspPyKPXhynFqO_8IAzj-TfxONjPAHkD_tAgFqOJYeGDVqZ-5v_m2SvLNI-d-RY6OXNIiyvxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری، معاون دبیر شورای‌عالی امنیت ملی: اتفاقی که به واسطه حضور پیکر رهبر شهید انقلاب در عراق افتاد، امری بسیار مهم بود
🔹
کدام یک از روسای جمهور آمریکا که مدعی ابرقدرتی دنیا هستند، مدعی حضور در کشوری از جمله عراق است تا ببیند چه اتفاقی در حال رخ دادن است، این به اصطلاح لات تگزاس؛ بوش پسر وقتی به عراق آمد، در نخست‌وزیری عراق یک لنگه کفش از مردم عراق هدیه گرفت، و  بچه‌سوسول نیویورک؛ ترامپ نیز اصلا جرات نکرده است که وارد چنین عرصه‌هایی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673560" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673554">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0pwbUopv_x7OzDrwSaAhtksq7nMhsY-sL-rnn3SfracCyursq5irb9zroNyGzzPmn-66wxgy3ntgxrA8Or6aTxPn4G1ChyTGhjWESTzUetFxw4pq96UE3b_KrF4hYe__U3Acj9_unCJW41y3CbS27n14ykkcKuUyK10mqsiuCzp36fTrr_orWE55Co4c1CCYZakwHDTB5Fv1RkQgIvk7pNphSZDi4UGw7cQ4CSQQ3mdHFDpcE8tIXzAqe32d4t7kUzhwM2aTGHJ1nR6ABrPXK7Qv0yXPzS_7FRrpUbSOU9c9s_LKtJGLiGxRzhKBhs1IuWxZ3GA91urqXI9OOiyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_lNyz-oOyslDkzWwHCao12Iwzm7MG5KNZPlDDYMsE34JGk6Q8jj4T6VUWZVtOf5Xg6tlVe6m6gJUVEmtwtuVx2m_0bqXELltm5RZaU8K-3uCHFJAscQz6F7UNUxg6sMmvRjJenUzmuVD7JpawUyNrM5mZhIlnGLbQCcmNJHISKI97RtC8J8MmH3eeQIip0r8m29pcvuFXYZdRBEQq_w9nLUn5EixDVh1wzIEyIkaLLt8Cmhf-xh96hMG0d8OEvKzPiZMCSuVETzmmQmmpVPz0Z1g34x00NGRNzMLAj6uXZ66NSsDTKeN0N52WHoxMmBoPCBWvyGld0tSW3QXt0URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k47iwnc4OK5GWU3aV4pJqzonODitlioI43ZCmxIPzCoZdZZOCrslXa1dTPDUcnb6uCiojmx88xefte1AVUlmO8TszSoowiskNlhL8HOniY1E5BrxOhMdiM8CVrIoNUtZBgNUxLRhSHDotPQngqfK45-uc69B59Hiw7TfRREemo9kUCrmO-uG63VBDYcm967RGV0G4qm37D8QYQngkIf2IqGlwTgSEPLj3xYwbuUbtayC_YCeV3kE_AUy9Rz9ZBJ4Hyf1V0JSmq18FYU6pPgz6SNoSrZba6E1-BScTrTWfCa-G8q6er5br7P84TIdDY_gSPN7aajnB3-Gmy0zlZDSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8qkZEQ5o76a7-Wram3oinJXhf9S_3F8VxUCTSI7YhJuFHMXb12eTGTgooYhksycvKa_jII2tX7-J-B7D-sK_H3sQy9m85J7uGuVWgknKg70rJh70juyRP5qVYPWztPLL9aTYAaoAKl-vmPtxbYk8tnZvWqNavwfIk1HI_Nbv6Gi5b5NiYrLfS9oHRQQUZy06H_Dtn06RUc7uoIkwscZSJhp_bGzCh9FS_CER6bPko-prlP-aPyWThgeoL9sZehA74WhA2P86C2odQG_u0jbmxYf12pLuuLLQfwmvia1wl3-U0VJ52gUVFIU0JqhpGYAf0hatiVi2qbvnok_E0DqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMBsLktkH2fjWOZ1REQfQjU4Ij0KCc99zTxUeXX_LgLWcewAa_4QB53YSGSwGLgPjqfqxzu4hGL8y1U_7GnVN0u-pPt2TPbrjLT-MdilZ95w-DA1nTnVBw1dYa2pzfyISQWYzgWZQ06Tul7T9IARdbV9ViF8167MgTy-Qednn-ZmPxML0f4zFpWXlKXyCrIvpTuG-2j1ooYPtg-WDLuFxhMw2lOwRXg-moukuOKO3b_QBxN_HHKcdJ5C2ZO07WusBKn2Y49J2J17Y4ZhO8rwTlWJg1Gv5XlgNJ-sFs0Blw57byUpDGsmPZrIziJOO4BqvJVqpeuNyA-rTwiUoJ7abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN7eROPVPPhpZouaSv4LNu5OXSpZOVgCiUhDzt7VvAqmhJEnDXv2f5AdvZYIlLZyWggShiFZBherdA0EEMGk4himjybZMLGGFwYdsVw4PlGWPueI7fKCIx56jlfUJeeG-uGyiF8HGw5ZS5NOH44EBJKNTMuSCe4MmR9zBFJemyuNMIZ_Gd_viBOaFFEhgOO7_3Fx1JBfGP6qanjlqNviQ15ggiWNiW-Mf7vsTbe2V6D29jyVfCLbolET1cvA9IVUxoN5NSBMLGvgVsQJEshB67aBTspbDH68cYpv3XJ7XUmgbE1qhU_Jh8B3dIM4pCZe7aaqIdVXMzQkE9pUuhzsfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نصب پرچم عزای امام حسن مجتبی(ع) در ایوان طلای امیرالمؤمنین
🔹
برخی علمای شیعه هفتم ماه صفر را روز شهادت امام مجتبی(ع) می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673554" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e770738336.mp4?token=DExLzKhgXF06HP2JJ2je5syZW8y6OVb9X8tBNBGg0zC_KI96mjLeBKN7sleAA7uTqpB0Ds2l0C6sWdwhHlNeFe7rnfZfe5Tl9BKfLDFIyVg_RHguEf6qX49izGuGrB5WBXjEk76PQeQhf_NJEwJc6oDlgok6u6qE1706SsdR0clnUMlR_hZTqDuLzEUHB_QHXucquzDDXBpFWfN077OJCvlfoGzb2qs1mRqdZYjEwYscDkt2362lb6qmfssXOFaGc-R48_b16o3Ba-eRGS0OjsPLGVDXugr4LLlv85s5LqSvM557OpUX7uAyaTN2PR5xKfBKXJsgvnBp-7VOVtfFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e770738336.mp4?token=DExLzKhgXF06HP2JJ2je5syZW8y6OVb9X8tBNBGg0zC_KI96mjLeBKN7sleAA7uTqpB0Ds2l0C6sWdwhHlNeFe7rnfZfe5Tl9BKfLDFIyVg_RHguEf6qX49izGuGrB5WBXjEk76PQeQhf_NJEwJc6oDlgok6u6qE1706SsdR0clnUMlR_hZTqDuLzEUHB_QHXucquzDDXBpFWfN077OJCvlfoGzb2qs1mRqdZYjEwYscDkt2362lb6qmfssXOFaGc-R48_b16o3Ba-eRGS0OjsPLGVDXugr4LLlv85s5LqSvM557OpUX7uAyaTN2PR5xKfBKXJsgvnBp-7VOVtfFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تطبیق تصاویر ماهواره ای سایبرالکترونیک سپاه و سایر تصاویر ماهواره ای
🔹
ایستگاه برق در بحرین مورد حمله قرار گرفته است. ایران ادعا می‌کند که این سایت یک مرکز داده C2 ​​و هوش مصنوعی ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/673552" target="_blank">📅 22:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrlP5yRQwAnNSnodOeLnGVhK3LFEs-kzoIMWQ_BuG8h-WDanf_NqYUjO44sjOKW9vq-VPhG3D9gUakTMnUXCnf3fqX7rrOQZ0LcJ97GB2YIPwCLbe65_gsCH1n6iqmdxmJIBFMcVHa8TKXvIds0M2Ve3s9hrwla7qyWugiiwEFaAIT5kbkoYG5LdYSOaSLEfIjIHT6q98Ihij3u_DE4-CHgRufIhOdmBB8-ac4AvOeGgRoQcRomTMmbohFAu7t2dBXWA2XCkTiasA3c4vSZOoXVd--wRmcfCmLriq5x2lYrRLubwQEnkoDMj9FgMwZZN_8roE-qOztxrvDaXLEVbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از موشک ایرانی در آسمان عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673551" target="_blank">📅 22:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
امتحانات نهایی پایه یازدهم تمامی رشته‌های تحصیلی، در روز چهارشنبه ۳۱ تیر ۱۴۰۵ در همه استان‌های کشور، بجز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/673550" target="_blank">📅 22:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/673549" target="_blank">📅 22:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673547">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AplHrrjkVDQ9v9F7rLDZR_KOq-S_70pUY8BtrHkyEMqWSBkh9WzZVklGYPtvqO3YE4mP0vlqWU9lRp97Lrnomj9-IlzdjVodR0OTqq8QDVggpi-_WrThhBJstY1g5RLkWkjgxK7wHSg8qSD3KuTHIrg_5Ys5tHsOL-lJ3mla77LUhnSlkFH99Xs3gWKNFZka96jOnZoZ3B4ZstoezqGRxcKwOjMsUnprwyrkAk5nxsN81EuT_xNBXW8LIpgg4EvuNfPi6cr1C9UkOJEFM4MdGoA9d0Dz9fU7xQWmeMh39uqqFHPdlwncTC4VETsPjgaumI89wvD8l2yjgzg86J4eQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bee633326.mp4?token=ZzglwbVQgpWdJDbMncQOIWduvdeUnbBBMxzERH7gA12mojQCMMViI2fVedMc5TvSBGvsREL5f9ZOfKeYMMoQVE-TkQxMEdgypsKT5n11Wj-vmuOLjxUf4luefPwx3TGCUzKaC1XB9gm8TB-7eRJOA2E3h_QtUdcKaeBAtO__MUlNed4nSzH3jQDzPHtbIeZz4MgTOmntffO9cM0mtmQ7_9vKT6oABRw3Csxr_0nGIF2OI8irgKffsO39q8Q084BsR31T7UgMMBYt3rMqaKVpw6wCg5X1dKDIMjk7nRt77VS2Hun3Z22MdYrCjtQWTih8MMcL5RdbAgzxMzwXV-4fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bee633326.mp4?token=ZzglwbVQgpWdJDbMncQOIWduvdeUnbBBMxzERH7gA12mojQCMMViI2fVedMc5TvSBGvsREL5f9ZOfKeYMMoQVE-TkQxMEdgypsKT5n11Wj-vmuOLjxUf4luefPwx3TGCUzKaC1XB9gm8TB-7eRJOA2E3h_QtUdcKaeBAtO__MUlNed4nSzH3jQDzPHtbIeZz4MgTOmntffO9cM0mtmQ7_9vKT6oABRw3Csxr_0nGIF2OI8irgKffsO39q8Q084BsR31T7UgMMBYt3rMqaKVpw6wCg5X1dKDIMjk7nRt77VS2Hun3Z22MdYrCjtQWTih8MMcL5RdbAgzxMzwXV-4fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر مواضع هدف قراره گرفته تروریست های امریکایی در کردستان عراق
🔹
ماهواره‌ای از ۱۹ ژوئیه، منطقه‌ی وسیعی از یک اردوگاه تجزیه طلبان و تروریست ها را در نزدیکی سلیمانیه در منطقه‌ی کردستان عراق را نشان می‌دهد که به طور کامل سوخته است
🔹
به نظر می‌رسد یکی از ساختمان‌ها کاملاً تخریب شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/673547" target="_blank">📅 22:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در سراسر اردن در نتیجه حملات موشکی ایران خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673546" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZgozSmPZ43npa_g4xuo65-bIxGyyrKOJS592wKWXtdcJ0CsVBwDrPEYl0eVFe1LKcZv8V988AgWyhuzrCMJX7-GSfGfnfvmyV-L7U_vmVKySiiYU7X1SFknHfbvgc_Lgr1i5J66Wj1g3cZCo-c33S4YuwQeyTn4LBySCB42hbmTQlkN186GDllCWQdCM90HXwOhrY096Rh8KPIa2BYpPV8vLxJE4EhifoBp5sPZMrIYDNCQMTDrAxGzX1leWSBrTb6hRCPAYDVmR4S2wlyA1WDdmREJvIUcpuhIU6115K-tI1T8748AmMDy5w9XMda8pLt8rujBH3zgEZ8c_dnDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏍️
موتورسیکلت بنلی 180S
✅
پرشتاب
✅
طراحی مدرن
برای مشاهده قیمت نقد و اقساط روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/zsx
⭕
⭕
⭕</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/673545" target="_blank">📅 22:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/673544" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
زمان جدید برگزاری انتخابات شوراها مشخص شد
سخنگوی شورای نگهبان:
🔹
زمان جدید برگزاری انتخابات هفتمین دوره شوراهای اسلامی و همچنین میان‌دوره‌ای مجلس خبرگان رهبری و مجلس شورای اسلامی حداکثر ۲ ماه پس از پایان قطعی جنگ و منوط به مصوبه قطعی شورای عالی امنیت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673543" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شبکه اسرائیلی کان: شیطان زرد به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673542" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
گزارش‌هایی از حملات پهپادی به مواضع تروریست ها در شمال عراق
🔹
منابع رسانه‌ای گزارش دادند مقرهای عناصر ضد ایرانی در اطراف اربیل هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/673541" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d0531940.mp4?token=DrIkIjydUPqiPMwR521QobyBdc-Sc1VKow2KomySLNjuCye-48Q_tlo2ssK5MJwn2DKgCwtKXbiCbb8w_UUGsyeULjW14PeI82w-WIHnR6snYlZ1wWiwtwkGsztZlVguuBpEnAUlnh3otWQXcUnBF0gTvZ7qNujlMraKUaK2nyWsOy6zts5sYyqgE-NHF3lgtj_8ZEnOz462zrIEzFbQQkJCrU2Djy6C79VltPqo1qdoBzBrQqn-T9Pz5pVtESUP6xKcD55oYSezisWr2ZjfhFHhuON9nHQri2CtetCDBZdDH-aloDX8qhl8NkDW_ef2hhnLqpyz6WS1HP1eY-zGtwxnjcK9MR_tY96o_7Pu8AVxJKh6tex5Gs4A4L48eWxSFdAGzHKOYaevVfGQ1_IKA2DWzTS3_petpbLf8TT5CmqY_8JKLnfLcekz2GeS2aHcFjrBOH8g2wEXBSv7tlag0wkupto3N2HQnzEKxOrxDMIJPjE_ulLRLQy7pd_25Vn5sDUnRicL535qO3WPYOHlPOBJzb0tqbp6lk01EYEdfafi7orNdJo0teek5QBdnhk0ZDYnFT1136YRUW1LuUgSTEPl9fx20OiRZRSGk6G4O9OQ2H89TgFykPGU8qws2ZHH8B1KlUv1m6MHz6zv14dFl2FfW4uLfGDfSNIB3zQjvKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d0531940.mp4?token=DrIkIjydUPqiPMwR521QobyBdc-Sc1VKow2KomySLNjuCye-48Q_tlo2ssK5MJwn2DKgCwtKXbiCbb8w_UUGsyeULjW14PeI82w-WIHnR6snYlZ1wWiwtwkGsztZlVguuBpEnAUlnh3otWQXcUnBF0gTvZ7qNujlMraKUaK2nyWsOy6zts5sYyqgE-NHF3lgtj_8ZEnOz462zrIEzFbQQkJCrU2Djy6C79VltPqo1qdoBzBrQqn-T9Pz5pVtESUP6xKcD55oYSezisWr2ZjfhFHhuON9nHQri2CtetCDBZdDH-aloDX8qhl8NkDW_ef2hhnLqpyz6WS1HP1eY-zGtwxnjcK9MR_tY96o_7Pu8AVxJKh6tex5Gs4A4L48eWxSFdAGzHKOYaevVfGQ1_IKA2DWzTS3_petpbLf8TT5CmqY_8JKLnfLcekz2GeS2aHcFjrBOH8g2wEXBSv7tlag0wkupto3N2HQnzEKxOrxDMIJPjE_ulLRLQy7pd_25Vn5sDUnRicL535qO3WPYOHlPOBJzb0tqbp6lk01EYEdfafi7orNdJo0teek5QBdnhk0ZDYnFT1136YRUW1LuUgSTEPl9fx20OiRZRSGk6G4O9OQ2H89TgFykPGU8qws2ZHH8B1KlUv1m6MHz6zv14dFl2FfW4uLfGDfSNIB3zQjvKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آژیرهای هشدار در اردن فعال شد
🔹
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
🔹
برخی منابع از حمله به فرودگاه ملک حسین در شهر عقبه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673540" target="_blank">📅 21:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1953e66d3.mp4?token=btSi5D9ZJCDTUJ2jKN46jZ3pnA9QaUXMX13AKLTVCMQuEFJ9mzvfWkLDjOnmAnDrl4k5J1vEXxvX7PpGMWHV87QSNdIlEVjitWPjT6d6bagAfPmr_5MwCZQfuRQfEp4ykDV1ZDn9JN8nRg5Go_b_4iPq5YpKUO_rTV_C0WBAZkZ1wmS_Wvab4kjFg4A3upJV-b46VTqWjjg95PCUAy2csO9XC9nyfXbYv2TbGbvy-ChXX-xDMt7-vD4woVWCi_hEeUrDrtAN1Sugeh9hykewPgDvbjuE_MSLRIBIIiGF84J36BQnOmwCCk92TJFMqipmwaO4P6kxoncChnWsAXBbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1953e66d3.mp4?token=btSi5D9ZJCDTUJ2jKN46jZ3pnA9QaUXMX13AKLTVCMQuEFJ9mzvfWkLDjOnmAnDrl4k5J1vEXxvX7PpGMWHV87QSNdIlEVjitWPjT6d6bagAfPmr_5MwCZQfuRQfEp4ykDV1ZDn9JN8nRg5Go_b_4iPq5YpKUO_rTV_C0WBAZkZ1wmS_Wvab4kjFg4A3upJV-b46VTqWjjg95PCUAy2csO9XC9nyfXbYv2TbGbvy-ChXX-xDMt7-vD4woVWCi_hEeUrDrtAN1Sugeh9hykewPgDvbjuE_MSLRIBIIiGF84J36BQnOmwCCk92TJFMqipmwaO4P6kxoncChnWsAXBbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای اصابت ها به پایگاه هوایی موفق السلطی اردن را بین ۱۵ تا ۱۷ جولای نشان می‌دهد. یک پناهگاه هواپیماهای آمریکایی در این تصاویر به وضوح سیاه شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673538" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: افراد نزدیک به شیطان زرد از او می‌خواهند که پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرد
🔹
ایالات متحده آتش‌بس را رد نمی‌کند، اما می‌خواهد که مدت بیشتری ادامه داشته باشد و ملاحظات بیشتری در مورد تنگه هرمز وجود داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/673537" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مهیب در بندر ایلات
🔹
رسانه‌های رژیم صهیونیستی در گزارش‌های فوری خود از شنیده شدن صدای انفجارهایی در شهر بندری ایلات، واقع در جنوب سرزمین‌های اشغالی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673536" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/673535" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45d5722c4.mp4?token=LSaoe09XD95SuHG9vVSFq5K0AD7FFlkrYYsKJ7NqdPoyZK2dd9IHg6htE0VqXVD8CdK_EO4mCefmu-4P2eaObHBXwG9vwvjf4Cu-PM-2nYnvRxhqZ-UtD4JcQ126E_92QIbMDKdh5kE8NoK1rJa3AhFSKXrJ17L2ZezldME-gd09OXURj40Ho-4Wne5hZo2ABRbqf9CHl_VUrEeI9d3zGTSFdImb_xarQfdR6qeHfvPUQRZIjaSiJ-qeokeArN2x8QfiNUOI5BJm8J2UQz5iNovQwzoPtMK93EFwF-ryfDa-iLzv20v9jnqwSo4UH_msqdfWLXgMa9IPd9FbbmiJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45d5722c4.mp4?token=LSaoe09XD95SuHG9vVSFq5K0AD7FFlkrYYsKJ7NqdPoyZK2dd9IHg6htE0VqXVD8CdK_EO4mCefmu-4P2eaObHBXwG9vwvjf4Cu-PM-2nYnvRxhqZ-UtD4JcQ126E_92QIbMDKdh5kE8NoK1rJa3AhFSKXrJ17L2ZezldME-gd09OXURj40Ho-4Wne5hZo2ABRbqf9CHl_VUrEeI9d3zGTSFdImb_xarQfdR6qeHfvPUQRZIjaSiJ-qeokeArN2x8QfiNUOI5BJm8J2UQz5iNovQwzoPtMK93EFwF-ryfDa-iLzv20v9jnqwSo4UH_msqdfWLXgMa9IPd9FbbmiJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاددان آمریکایی: هیچ‌وقت بازار انرژی را تا این حد تحت فشار ندیده‌ام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/673533" target="_blank">📅 21:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGUCcvjYktX1Xk2nx59y9hlvev4MVFrP0eaumjb1KZT7qwxQkFYZBkq37ZVBn6QGOjWhHzS0d-EpOG3DjA7rpVXjKyUj4fpejzLvl4q1qgEwxKmhc24t5cai1EQ0ygJWrDnrWvxPxgGzo2aNmDlrUizb4yYS6VWUC1sKVJkeED0dx5SYR0FdWgTaBhBkrChqmOajui8B4Oti0NxuLhwiTJHr8rqT0RE2XtHylcDAY9wyz4oBLpD9bZQWXupMi0fAwXWg4ECyXztNDI4KLsT7_kQbhNYkyFnro0kL3IV3DgkfwfcuNeE6D8qte3-wd_pgpvg467vyyEFNWNwck-d_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد
🔹
بخشی از پیام رهبر معظّم انقلاب به‌مناسبت تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673532" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a83345d2e.mp4?token=STrczDjYSwwZVOYlmK12sWYQx9WCpyGDA5YiX7y4453uXXh72bNcDjzofkOiCcxFvF5NbKJDuPqNEfsa6RFIcZVJKdKFsDTtxOhgtEhSpzYdpr8fiufOG_pzfLEDwB_exDiOUu8l7dK1e_s2RlXG8Q98cZeH4BpgB6rmskbRy7WuXzl1rrrBPEqK-4TDhEZ-_2vQOs6sGjJN6Put5pWDaOilw_5jfzJlviC8_XrJb3R0kpb0goJ4Vj6zGLzKhbhhobtuFOs-QRnG143dI0vMNqufLnU_RO1lqFuKaafK7ps2YFBs5BOdTvoeBP-lGK48hxcyuXqQDhJVWAeObykKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a83345d2e.mp4?token=STrczDjYSwwZVOYlmK12sWYQx9WCpyGDA5YiX7y4453uXXh72bNcDjzofkOiCcxFvF5NbKJDuPqNEfsa6RFIcZVJKdKFsDTtxOhgtEhSpzYdpr8fiufOG_pzfLEDwB_exDiOUu8l7dK1e_s2RlXG8Q98cZeH4BpgB6rmskbRy7WuXzl1rrrBPEqK-4TDhEZ-_2vQOs6sGjJN6Put5pWDaOilw_5jfzJlviC8_XrJb3R0kpb0goJ4Vj6zGLzKhbhhobtuFOs-QRnG143dI0vMNqufLnU_RO1lqFuKaafK7ps2YFBs5BOdTvoeBP-lGK48hxcyuXqQDhJVWAeObykKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه اهل سنت میرجاوه ساعت ۴ صبح توسط افراد  ناشناس ترور شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673531" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شیطان زرد در مراسم ویژه برای اجساد نظامیان به هلاکت رسیده آمریکا شرکت خواهد کرد
🔹
کارولین لویت، سخنگوی کاخ سفید گفت که ترامپ در مراسم انتقال نظامیان کشته‌شده آمریکا به پایگاه  هوایی دوور که عصر سه‌شنبه به وقت محلی برگزار می‌شود، حضور خواهد یافت.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/673530" target="_blank">📅 21:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKoybwM7XJ4a9uOIH9Xm88S6JMXNNKwyLiTl4qEHu1XzTO8ndQu7bdggb1O_vcSS-iUiYOlwdYaUpgZob6851LSvGowy5tbQ37wJv8MsmYehBf0kaNglPGe6fiDn6RjTwwFomPp8s6qTEhwuDTFYnXBFllnpWFf3GXPCKCVauXj2eEhCFjIR39Yxb4N-h4FDz30HXCrxa92TCWRpb-_DlDGo_TeROEinO1jtHVmqhcXJiyFHt4G2B0kfxS1LqUGziQwAYaXbn1-OYRLX4493w7Y_NhGgIOW1OornqlHaDYex1EmFLfI0NQ-GM-Ca8QogvH3G-v8cwNPwWCn-iLbZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند در بین برترین‌های جام
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/673529" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
♦️
حادثۀ دریایی دیگر این‌بار در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه‌ای برای یک‌ کشتی در نزدیکی شبه‌جزیرۀ مسندم عمان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/673528" target="_blank">📅 21:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1297577a.mp4?token=rLVaGe8skcieUi_cd9hv7-KgWk-cqRzlFvQaLHQhmPTn1xLD-i3309K5Fx2IlGyZ_dARyBSioP2sWTzvXBQqZY1SmPwOW__PdVnoafJgaPa0bM-Ts0FqNJzKh0SOzfxBJwsABh3OgnPGXTMknYdIkq_4F2c8L6osJlEM9mhgFF5NLt3KrMeqYkp7ZOYYd9H7vJxf0SG11vrJLRzrkES-QXDOdCOMcEBeWCeIyC0SOJkW3nDdnWOUSsb7EeKh6hORKjNYlqELruGm8PHvRyjdyWfzVh3PwgA6E4o92CyLIvd58AiFnwgkhzAIVhWCqaotzAqr5TyoUNXIOcwHkEpuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1297577a.mp4?token=rLVaGe8skcieUi_cd9hv7-KgWk-cqRzlFvQaLHQhmPTn1xLD-i3309K5Fx2IlGyZ_dARyBSioP2sWTzvXBQqZY1SmPwOW__PdVnoafJgaPa0bM-Ts0FqNJzKh0SOzfxBJwsABh3OgnPGXTMknYdIkq_4F2c8L6osJlEM9mhgFF5NLt3KrMeqYkp7ZOYYd9H7vJxf0SG11vrJLRzrkES-QXDOdCOMcEBeWCeIyC0SOJkW3nDdnWOUSsb7EeKh6hORKjNYlqELruGm8PHvRyjdyWfzVh3PwgA6E4o92CyLIvd58AiFnwgkhzAIVhWCqaotzAqr5TyoUNXIOcwHkEpuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناگفته‌های معاون بازاریابی و فروش گروه سایپا از هزینه‌های تولید خودروهای ناقص/ چرا خودروساز با وجود ناقص بودن برخی خودروها، تولید را متوقف نکرد؟
🔹
معاون بازاریابی و فروش گروه سایپا توضیح می‌دهد که توقف تولید در شرایط تورمی، هزینه‌ای سنگین به شرکت تحمیل می‌کرد؛ به‌طوری‌که در صورت عدم تولید، حدود ۴۳ هزار میلیارد تومان هزینه ناشی از عقب‌ماندگی تولید ایجاد می‌شد.
🔹
به گفته وی، خودروهای فروخته‌شده هم‌اکنون تولید و در کارخانه موجود هستند و تنها بخشی از آن‌ها به دلیل کسری چند قطعه، در انتظار تکمیل و تحویل به مشتریان قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/673527" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f99f42ba.mp4?token=Tv8CHeErATZ74sy0CzTHPJlmcJQSmJ_rEq6Nd6EA-4GL679nc3cBEXJFbOaWpMq2dzChvxRSt7JhIDJQyvTS9J5VHt-bzO-SozMUIpNxH7NnosGsjTZfHbmAFBFMptHhKtocR-E1X2sdIt4Usx52fFnrHBvLNwkiv24ASVVVWComPg6-AKktwfPiyFtpoTx8LvoBXa-LQSw7M9yg8yWbegOnrgBKvALjdQnaJoAr6oXx6B7R8J9gOFqYVff_u4ORIOF3dPRd06WTYhKsuuL6WInQxREforlUTCgSvTa7F8WcB5QqncJwH6Do-yhi5Lxm6zdacI_8vpYv205RwT81Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f99f42ba.mp4?token=Tv8CHeErATZ74sy0CzTHPJlmcJQSmJ_rEq6Nd6EA-4GL679nc3cBEXJFbOaWpMq2dzChvxRSt7JhIDJQyvTS9J5VHt-bzO-SozMUIpNxH7NnosGsjTZfHbmAFBFMptHhKtocR-E1X2sdIt4Usx52fFnrHBvLNwkiv24ASVVVWComPg6-AKktwfPiyFtpoTx8LvoBXa-LQSw7M9yg8yWbegOnrgBKvALjdQnaJoAr6oXx6B7R8J9gOFqYVff_u4ORIOF3dPRd06WTYhKsuuL6WInQxREforlUTCgSvTa7F8WcB5QqncJwH6Do-yhi5Lxm6zdacI_8vpYv205RwT81Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: مشق شب
🔹
ژانر: اجتماعی
🔹
خلاصه: فیلم از مجموعه‌ای از گفت‌وگوها با دانش‌آموزان دبستانی تشکیل شده است... کیارستمی از آن‌ها درباره مشق شب، تنبیه، تشویق، خانواده و مدرسه سؤال می‌کند و از خلال پاسخ‌هایشان تصویری انتقادی از نظام آموزشی و شرایط اجتماعی…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/673526" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFwDkF7-T6LKLvoaXS_Xi12t4-P8bLZdNluYgay4Qaj4yW_5Gfb6b-YeYkD-B36NI3ksSBcPRHCA2mWiKMZ0haYjw8v4DDqJ2zC1qqGhhVGqZO1-Vw51WHZcl_q-npvvNlxlbjDCHlLQQWXxJRkqgdTHoQ3GsN2GyMBH-Yl5h6S87I2T0SJ0HTXecliV7xxzDte-W8b66Q5r1fJVICdCUj1dpzqF2QKV5SKSfru5-InGzn2PUSGQBD47W2ZIuSZfskvN17m-rqybH0jPd5uwBXAlXJL7ZvsAu_VIq-njT5CQusK7tAWuV21qWcxyakXiIn8ILxFM0c9JZLQx0kLlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن‌پالیسی: برای بازگشایی تنگه هرمز، ایران باید خود را منزوی ببیند
🔹
ایرانی‌ها مصمم هستند که کنترل تنگه هرمز را حفظ کنند. آنها این تنگه را به عنوان یک «برگ برنده» می‌بینند که به آنها قدرت نفوذ در اقتصاد جهانی می‌دهد، درد سیاسی داخلی را به ترامپ منفور تحمیل می‌کند و همسایگانش در خلیج فارس و دیگران را مجبور می‌کند که از نظر اقتصادی و سیاسی جایگاه او را بپذیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/673525" target="_blank">📅 21:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای
رویترز: حملات هوایی اسرائیل در تاریخ ۷ و ۹ مارس (۱۷ و ۱۹ اسفند) به دست‌کم ۱۱ محوطهٔ تاریخی ایران آسیب وارد کرده است که  ارزیابی‌های یونسکو، شامل میدان نقش‌جهان و کاخ چهلستون در اصفهان می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673524" target="_blank">📅 21:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ae3f6528b.mp4?token=dQ_Ag5TymGTXJXkTVwnnVDOeR0lZv8zgOSBLb_BtVXyo8uVKlHWn32HTSJdI3SNFh67ZLpDLXilzBnnIHrjji2VZvGKkSJa_3HS6-pxOCgVxdmXGpST7DGkCFRjHL_r-iFzWo1EN1VYcg0xiJc6OFf1shoxq5Lp1pxtBSjPAygWF1K79Ye10gsV8KT6E6TmkN99-r4ACuLXz6VSe2aU3r1X94ePGUOTzySazwlVxCE401RAylUsO1ADJwb84Vi1BZRzhNIt9kfdM9Hx_AMOj1OTGZcWkpvrW-7yj_OobN0X33ebVm53P_9jsmr1-yjYLDOCohGEbQ-0B79XkYWKlyZ-sm4MJ91vSBM_aWkxfoyT6vtfbClUZX1K-EGElN5eAzepEkQwWceuYgv3QiXdmjzMX-6dAi5SoDfMgVGlrFUl1Tb5t0XegE1ypeQprKNkzrtKXCreigr8KhvKdAfuMR5nCpAFApqGX2PbKyCNeKdguL9Lj0H9o9laEi9AJlYP0htof68Y4BAthFYm0EczrhgrM2NzsTZ3fdYdAG3QaNeH-L_x-iZUTspZiysvPFEwSQADY1_h2MaiTqFknevul61Q-IlEt52mQfC4RIPlzo9wIJMriIw5UNqteVPnJ9SXycN_Vw1HaPsJhIFhANovhFwxfIuZUgjGpXeUNAOFjlp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ae3f6528b.mp4?token=dQ_Ag5TymGTXJXkTVwnnVDOeR0lZv8zgOSBLb_BtVXyo8uVKlHWn32HTSJdI3SNFh67ZLpDLXilzBnnIHrjji2VZvGKkSJa_3HS6-pxOCgVxdmXGpST7DGkCFRjHL_r-iFzWo1EN1VYcg0xiJc6OFf1shoxq5Lp1pxtBSjPAygWF1K79Ye10gsV8KT6E6TmkN99-r4ACuLXz6VSe2aU3r1X94ePGUOTzySazwlVxCE401RAylUsO1ADJwb84Vi1BZRzhNIt9kfdM9Hx_AMOj1OTGZcWkpvrW-7yj_OobN0X33ebVm53P_9jsmr1-yjYLDOCohGEbQ-0B79XkYWKlyZ-sm4MJ91vSBM_aWkxfoyT6vtfbClUZX1K-EGElN5eAzepEkQwWceuYgv3QiXdmjzMX-6dAi5SoDfMgVGlrFUl1Tb5t0XegE1ypeQprKNkzrtKXCreigr8KhvKdAfuMR5nCpAFApqGX2PbKyCNeKdguL9Lj0H9o9laEi9AJlYP0htof68Y4BAthFYm0EczrhgrM2NzsTZ3fdYdAG3QaNeH-L_x-iZUTspZiysvPFEwSQADY1_h2MaiTqFknevul61Q-IlEt52mQfC4RIPlzo9wIJMriIw5UNqteVPnJ9SXycN_Vw1HaPsJhIFhANovhFwxfIuZUgjGpXeUNAOFjlp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
🇮🇷
تجارت در مسیر خدمت
🇮🇷
🙏
خدمات حضوری و غیرحضوری بانک تجارت در اختیار مشتریان قرار دارد.
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/673523" target="_blank">📅 21:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرصت ویژه سرمایه‌گذاری در منطقه آزاد سرخس
با ارتقای جایگاه حقوقی منطقه سرخس به «منطقه آزاد»، این محدوده به کانون اصلی ترانزیت شرق کشور تبدیل شده است. فرصتی استثنایی برای استقرار در قلب فعالیت‌های لجستیکی و تجاری با پتانسیل رشد بالا.
✅
واگذاری هفت هکتار زمین ، کاربری انبار با شرایط
۶۰٪ نقد | ۴۰٪ تهاتر با املاک سهل‌البیع ( مشهد/تهران )
🌐
https://amlak.razavi.ir/panel/auctions?page=3
در سامانه مذکور به صفحه سوم مراجعه فرمایید
مرحله ۱۵ -صفحه ۳- شناسه قطعه ۸- بلوک ۱۶ - را جستجو کنید
📞
تماس جهت هماهنگی و مشاوره:
☎️
09153259470
☎️
09152005111</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673522" target="_blank">📅 21:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42e93dc5e.mp4?token=kYKOO5v9aKgeJcGfli0JAa5Z3LOVi7ViZkGThc0qcJ1gxY_0MkTuXkzdzaeEA4fizIUeMd6e4ndmo8wiLdGqu-4saXesJi92k61xl8FC1ynjJXdWlCpKEicTUOo62Yjy460iPLxZTz6PEGLLEuCQfPjGFHHr3esmC5zPPtL65_MCv6UWMdG6CbzBKW_RuwPskmCQ01-C2KNSaJ5mlHRhhga4JE_ZnrsXdZ-7cfFr8WPwWLdJcJEZMaVikPPgKjUO1iZXDzX4jqUm8bcO1UVBiA0QSGFa7pDf3tMsWMmCUgcdnXn1kYrrQXsbYnQW5TYnDOYhvoRVEUkv1Mr7CdsiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42e93dc5e.mp4?token=kYKOO5v9aKgeJcGfli0JAa5Z3LOVi7ViZkGThc0qcJ1gxY_0MkTuXkzdzaeEA4fizIUeMd6e4ndmo8wiLdGqu-4saXesJi92k61xl8FC1ynjJXdWlCpKEicTUOo62Yjy460iPLxZTz6PEGLLEuCQfPjGFHHr3esmC5zPPtL65_MCv6UWMdG6CbzBKW_RuwPskmCQ01-C2KNSaJ5mlHRhhga4JE_ZnrsXdZ-7cfFr8WPwWLdJcJEZMaVikPPgKjUO1iZXDzX4jqUm8bcO1UVBiA0QSGFa7pDf3tMsWMmCUgcdnXn1kYrrQXsbYnQW5TYnDOYhvoRVEUkv1Mr7CdsiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد از مراسم تشییع رهبر شهید آشفته و خشمگین شد
وکیل سابق ترامپ:
🔹
او واقعاً از حجم گسترده حمایت مردمی از مراسم تشییع پیکر رهبر شهید به‌شدت ناراحت شد و در تمام آن مدت به‌خاطر این موضوع آشفته و خشمگین بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673521" target="_blank">📅 20:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
آمریکا هویت دو کشته خود در اردن را اعلام کرد
🔹
ارتش تروریستی آمریکا اعلام کرد دو نظامی‌اش، «تایلر جیمز فیهان» ۲۵ ساله و «ایزابیلا گونزالس» ۱۹ ساله، در حمله ۱۷ ژوئیه ۲۰۲۶ به پایگاه «موفق سلطی» اردن کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/673519" target="_blank">📅 20:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673517">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از کما، یک روز را در برزخ گذراند
🔹
05:20:00 شرح چگونگی رخ دادن سکته قلبی
🔹
00:16:10 ورود به تاریکی و سکوت مطلق با شنیدن صدای سوت ممتد
🔹
00:26:30 کشش در تونلی با نور سفید و زیبا
🔹
00:35:00 هدایت شدن توسط مادربزرگ به سمت دنیا به خاطر حضور مادرم کنار جسم
🔹
00:41:30 ناراحتی و بی‌قراری اموات از شیون بازماندگان
🔹
00:46:10 ادای احترام و خوش آمدگویی توسط خانم زیبا روی غیرقابل وصف
🔹
00:57:10 اهمیت محبت به حیوانات
🔹
01:06:00 تردد افراد شادمان، میان دو خانه نورانی با لباس‌های قدیمی و کلاه خود
🔹
01:12:00 سقوط به دنیا با قرار دادن نوری سبز رنگ بر روی قلبم
🔹
قسمت هفتم (مادر آمد)، فصل پنجم
🔹
#تجربه‌گر
: مهدی زنجیرانی فراهانی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/673517" target="_blank">📅 20:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673515">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxGbQJ9VZNPCkNVS8liBVr3azmDAP1FsG5PQlDzUBOQKG8i-9-IxJgmNzC7ulpEGoN_E8bZSRG2cUaZ462NN4FWnLJts9U_Px3X1PhvbMALSyNoOL6sl-BfvrqEZedS9-cAOmVV_jF6fWnnUgPwWHTbqZQTKRQdhJTbEGKr9IRC47ga6BZzHDr-dQntlkJ2xHUm0Bz8ikMyeb5XhRqyfdTM4UcZHrAiVXdeVQXYvDuLbL6nqn3SkAmD9vMw9P_dQe0codjhWeqoujynY5RQGaFeAKedf6BZbyJbEeFBjE1vlE1cZzT6PfrLHuIOrs16jixJZr2PPT3k3aZlxraDdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار مدعی انتقام چندبرابری از ایران شد
ترامپ در پیامی جدید در واکنش به کشته شدن سربازان آمریکایی در حملات ایران مدعی شد:
🔹
هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این عمل را چندین برابر پرداخت خواهد کرد! این دستورالعمل به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دنیل کین، و تمامی فرماندهان ارشد نظامی ابلاغ شده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/673515" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673514">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان از سرگیری محاصره دریایی ایران، ۷ کشتی تجاری را منحرف و یکی را از کار انداخته‌ایم
🔹
ما همچنان به تلاش برای جلوگیری از خروج یا ورود کشتی‌ها به بنادر ایران ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/673514" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTLBe-Idnqb3EHhKg5D08563A1cVQSwkAh5NluPc6vpSPp2I-u-899BJ_A9ORCf4SPp6P32Qh5ZNtyKXCqpp9V-ELJ2-iEkay1I7MIVgb5NNi_YjEJ-8QJs_6Rc9GT06TfEljnF5hmeiBsnGHOGH_fM0SGyQ1Y1FPaU0wMmkdDlNXbA0xOxeNIJ1bXTTdAjI-REizgf5L8p1QAs3RK3q8EsZ0u5J2MaU_2ER1QNhrpLBAlz7hBjmT-s707Zj6fW2sH7rJeGb7X-mXsioB56HyRww-K-oVFhjekzD0HM7Y1uh6dlFHO-bA34FVQB91QofVswfVDhclTF86J5k8sYrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/673510" target="_blank">📅 20:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRikvdKPuN6DEz0sa9mOQndYKqh4RyxnZ2fhmTYpcSm14Kwz3LPdWrL9lxGhQl8vpXUhAbRMeD_l3jI3Q1B7wlUFR43CblhHWj3cT5pJ6VN2881RrjfLzZ6qQICySEm_bGGRLhcQtSxglX0VSTl61vwjQv5j8WsYZoWnemIUJ0eTa8IcbC-WaPcg8UcMB6dq_icbSGcErKIXLAu15ZfgdhVd3cqKTVRHGol96QL-9qzcEquIGyiotCDjM8AnCgMbkT4-N2V_bwAd6L7uxMywLhFb1ABTPDJ8OTwB8fv_hJUwgi0UMD-UMiFxcq5wt7rdabUuWBax_C8XpZvlhucVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZYSIvScN3EtJdbC-ujZ-Kh5d7srjw94YINpPCFnm_9tgiPmpHm1Fb5ZaTaLYoYQidqI0hCHGcxhlK1I7zjDlVFPQh4ajr2dBpj9rMrg1ISOk2kBiS1AWyOXKoZee31FLyctB19YurAOzl17E3NgF9WBZJJdmf-Gge8wzAtCwOuLtmf7TegbSnfwO57dFJSINKZOHIIlS7RRXMfGJ3RRyzFl3Bydp9qstV3iOTNA2HR81IplKroIde4I4pKwsOQDX4C10GQCuffSDmPXKK1Zi-h6Ei0nvjr3CmUN--tquOZADQMxxiuZJQTcbtriM0FPvggHyuxMKiXGJc3OKQMNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا محبت امام علی(ع)، معیار شناخت انسان‌های خوب و بد است؟
🔹
«جاذبه و دافعه علی(ع)» از ماندگارترین آثار شهید مرتضی مطهری است؛ کتابی که نشان می‌دهد عدالت، حق‌طلبی و شخصیت بی‌مانند امیرالمؤمنین(ع) چگونه دل‌های پاک را شیفته و اهل نفاق و منفعت را از او گریزان…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/673507" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673505">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoyE43U8rGJuG5rUa97NMUnFRhZDXsEEQFOF5PisePOHL4uz0b7V_nZzp_xG8oouH4_Qn0hgMPL5IXjbrTdTJAYEoAQSRA_bbTgZmBrlx85D0UQOuO2ErWpq62sCXG1TjzWR0SV7iWPBeoaP-Cf6WS4A_CmLidsB6QFKzSgVavZF4xErN32BY6_5nLd9ZQYMg1rgYa-XP1rkUD-DW6Yjn8JP_SoCZFf5BZXddRKGH6Q_D1gG__0bY4XvfdSHTtwFjP7A2fkpIq0l1e0PSiOG4gv68aeAzfvVxhPz_QsbQl1uMakiRJmfT07_Z6JwgqgrLeq4D8dpAcOu3UVi2k1Hww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار نیست همیشه فرصت، دوباره تکرار بشه...
💎
طلای اقتصادی اجرت از ۳٪
🏦
بانک طلا بدون سود و اجرت
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
کانال رسمی ما :
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/673505" target="_blank">📅 20:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی:
🔹
این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/673504" target="_blank">📅 19:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1rP_0ad9YLiZY1iEY0MARaHfbZYBGEtTw1raun4hLaZjtuLP1AClJq27oexlAY6S5xFnfAlSbP6I34TCDaSjVVOx4cAL-Rpd6HLDh_4lMAbHVI-XNNFX5PFMKDp6BdZcfSTPILldTM1iF2bpBGjjRmWDMOTzofqE70XmZVmqiNVYGSVlFq5FJlt2iNjwFpA9hQ8JeDABuJ3LkBpyktc2VWLPGjqnNyRDszoIqx3OJaC9QcnvWQzlK6LFniJ4BytaMpm4KMuy9qm7qLaloOV2qreLHLYXvdPOvbUDjN2xy6lPu4Hpn42D3pCjxzsQyseVZIGPvvpPhgt02HuA9-jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه بالا بردن جام قهرمانی توسط رودری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/673503" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شکبیر سود ۲۶ هزار ریالی برای هر سهم تصویب کرد
🔹
مجمع عمومی عادی سالانه شرکت پتروشیمی امیرکبیر با حضور ۹۸.۳ درصدی سهامداران برگزار شد و ضمن تصویب صورت‌های مالی سال مالی منتهی به ۲۹ اسفند ۱۴۰۴، تقسیم سود ۲۶ هزار ریالی به ازای هر سهم، به تصویب رسید.
🔹
بر اساس گزارش عملکرد ارائه‌شده در مجمع، سود عملیاتی شرکت با رشد ۶۱ درصدی، سود خالص با رشد ۸۰ درصدی و سود ناخالص با رشد ۴۹ درصدی نسبت به سال ۱۴۰۳ همراه شد. در همین راستا، ثبت رکورد سود خالص شرکت به ۱۰.۷ همت و سود ناخالص به ۱۱.۷ همت، که حاصل افزایش درآمدهای فروش و مدیریت بهای تمام شده تولید بوده است.
🔹
مطابق این گزارش، سود هر سهم (EPS) نیز با رشد ۸۰ درصدی به ۲۹ هزار و ۹۹۹ ریال رسید و پتروشیمی امیرکبیر توانست بالاترین سطح سودآوری در تاریخ فعالیت خود را به ثبت رساند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/673502" target="_blank">📅 19:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfL32QXcdVh2aMtXVvoxcmqPsGWvpR32qthSAJOCQ-36aVPnE2gQHlTFM-eNJdxf5tvcavkmFM9XZGf8lOmQUfWPRtjJc16uNCUrcUG-cCYbQeYer05cGJp7-5gaxGKSkMQy2iTM9DAMk3-DnUPDvusZysDLTB9SkVlJ4ln1JD4DTe5SX_ryUQt0FOA2vCh-IWyVJxqWgUiTm4wX7CudmRWiMTiHJshadiP4uN-wNGwXV1WWHteZuoJMWI9corRRBl594ofPNioExui_ss1CB5QNZ53Q7B-AwVmd3sZWjQTjXQj7616Lyao_rL1QNdlpDWgOfajdtg-rEIuKTT6Jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVj6w9rhasU9Ezh_7_8uXxi0DbpWrIXpqT79QSt9eYtAnzc_VtVOWNux5-osFL2CnLMivl2P1mwrxRWinM_KEoP3-NSMu5YbS97mffzZmfED30VMhnVUEC_Bi6CdOA-8C5NFx-IyWtt-bnoJZqEBo7mjZ8ngTmginqCIhGLP0PA33ZKUVLa2W8vVI3OECbqnpLDhLBFvpNWqFJaBbsiAUTTcIlAlM5MIKyHo4CTmBaQfPq2l_zwfXU4KkiRpdDk5Q10HsF6xKJ7Onbxkmld0uEySXteAfJuoSde5oLh-VlAWFk0B5oaoxrBx0EFlsKZDTjT7ONLtlWAMMzBnnGVuuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری از سرباز آمریکایی که در حمله ایران به اردن به هلاکت رسید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/673500" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmrzwxy7sMG6bj70bE1xkOD7TmAbhvL8wwjrEbdOByeMgZ6LgQudlIH_wPlC7PVWmn96nSF6mppOjEN_6S6m0X4TGojFFiRuOOZg8ah1Tvm0Q_5FIg9t2TgwNMnNQQSJTEotAygslpYLOrCx_rIIFLgejSZU-YDZ_wBU6uF5ZzH01TduvchcP5xqvNOLg1rIse67gE35Y_cWyPQaqxvDJhd-0ijWkQqh1FX4a8U9zidfhBpdqSBTLMtuIA9zXU7uS2c7kx_R1M01JVMwLZH78E9uBGltn_iLNFST8UrEzM5GHAp_RvuHglAP0ZOx_mojAIv4OuZhhmzY2a-DoVzC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ‌زرد: بر اساس یک نظرسنجی، اکثریت مردم آمریکا از توافق با ایران حمایت می‌کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/673499" target="_blank">📅 19:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توانیر: بین ۷۰۰ تا ۸۰۰ هزار ماینر غیرمجاز کشف نشده وجود دارد
هادی سفیدمو، مجری نظارت و ساماندهی استخراج رمزدارایی توانیر در
#گفتگو
با خبرفوری:
🔹
از ابتدای سال تاکنون بیش از ۸۵۰۰ دستگاه ماینر غیرمجاز کشف شده که مصرف آن‌ها حدود ۳۰ مگاوات می‌باشد و این میزان مصرف معادل با ۸۵۰۰۰ واحد مسکونی می‌باشد.
🔹
بر اساس اطلاعات به‌دست آمده، میزان ماینرهای غیرمجاز موجود بیش از ۲۰۰۰ مگاوات برآورد می‌شود که معادل با ۷۰۰ تا ۸۰۰ هزار ماینر غیر مجاز کشف نشده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/673497" target="_blank">📅 19:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673496">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
جنگ دریایی با چوب و پارو؛ تقابل عجیب نیروهای چین و فیلیپین
🔹
تنش در دریای فیلیپین به درگیری فیزیکی نیروهای نظامی دو کشور با استفاده از چوب و پارو کشیده شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673496" target="_blank">📅 19:24 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

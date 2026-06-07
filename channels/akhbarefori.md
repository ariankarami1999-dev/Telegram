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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-657067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmdcbpgna3sizeURQ_m7gc_VfMILsIkvOoc08daziw1n3I4JPXL-iBxbDyrFUp0ZtxztGFGZG5Bq3xI-JMSfdufd7wBdJmGTK2FPFpkC3ZCrGmE_uTZ6nfSaxCNq6ovM4pD-sMeuHvpwCg5VXvdEOkBbqa8d9k28M_hARZHchFf6HO-4K1xNviEXaaFjkyUvSJaXLbcTE_ZeiEK0ypcGs0dqp_dFSHMgzqhQ_fMIPEJZJyfvRCpYHUhMr0Hw-ZwWhxZCCrQ-Y7lnA1TZ9qLk8dXrxvxn9fkHE3gindGEOZiJ97yKNkFDEy5dj50AVBv5WrYkXlACwgdcyJTLtmRDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:
‏«وَ لَیَنْصُرَنَّ اللَّهُ مَنْ یَنْصُرُهُ إِنَّ اللَّهَ لَقَوِیٌّ عَزیزٌ.»
🔹
قطعا خدا کسانى را که او را یارى مى‌دهند یارى خواهد کرد، چرا که خداوند نیرومند و شکست‌ناپذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/657067" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مقام ایرانی: توافق با ترامپ در شرایط فعلی عملاً ممکن نیست/ حمله دوباره به بیروت، پاسخ فوری موشکی در پی دارد
/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/657066" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657065">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/657065" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عبری: پایان تماس ترامپ و نتانیاهو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/657064" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxiJocgQHzLPSvGsPzO9Q4EwHeAWhhBf01hddU2jcJTrRB81XqWIPxF08MvMGa3bC_FM36zHMOIElXa5qMZBbI7GEbhocNQN1NxIxxdt9fPar1fcKFlUGoJdsi6vymXNYDdHMOt2MGd2DbEqCDfuSGIADEkvKq0IaxA9yo6baV4kbMdC-h9TFkL69IdZ2bm007Om7htZKwdr0ad0jCwtTcKRvVDzzF2ToE_wekm0dBsJpbYe4PcmEoWkL5vibFax3Fwqln0jdComJ8f_1zaHymOroaJxf6siTvsxNF_Sr-fWYEvz9-6wE6-huffbwwLr7SdWBZBKPvJ3F3XVnvgSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: شلیک‌ها از آن جایی انجام شد که ترامپ می‌گفت نابودشان کرده است
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/657063" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657062">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قدیری‌ابیانه: باید صهیونیست‌ها را موشک باران کنیم
قدیری‌ابیانه، فعال اصول‌گرا در
#گفتگو
با خبرفوری:
🔹
لبنانی‌ها برای کمک به ایران وارد جنگ شدند و بیش از ۳۰۰۰ شهید دادند؛ بنابراین باید به حزب‌الله کمک کرد و حتی اگر شده، صهیونیست‌ها را موشک‌باران کنیم.
🔹
وی افزود با توجه به ادامه حملات اسرائیل، پاسخ ایران نباید به تأخیر بیفتد و حمله ایران پیش‌دستانه محسوب نمی‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/657062" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657061">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/657061" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657060">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سازمان حج و زیارت: هیچ‌گونه نگرانی در خصوص وضعیت زائران ایرانی در سرزمین وحی وجودندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/657060" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=BBi15bIs844XKG5_DvjjrIvCe_UclzhGvKPwBdRcmVy1Ib0RLRr28TRw_HaZN8_LTVb5MA0hkNjCWbKD57PwsgHnxsFOUsO07aq-MN1QlPyyzJ-NwnMydlI6frl6TznoZJxJuLx2B2kyOap21JfrxD8RTAVWWDvoi9RxCH6QEosflT7qKK2j_OgMet9TMc51ZhqW7jzajvdYIaQeAyPlP8t3QtbiIwqwlRLnhSUxQtNtYPFmNbQH5rQ6uXQgPt1EBsTJskGvecE7_0ExEPKU6ztN3w-KJeeQBgfaC92z2Tqx2rQJVlV2zotHiQpqMypvBLZZkSpZuKm3HdviX77Tow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=BBi15bIs844XKG5_DvjjrIvCe_UclzhGvKPwBdRcmVy1Ib0RLRr28TRw_HaZN8_LTVb5MA0hkNjCWbKD57PwsgHnxsFOUsO07aq-MN1QlPyyzJ-NwnMydlI6frl6TznoZJxJuLx2B2kyOap21JfrxD8RTAVWWDvoi9RxCH6QEosflT7qKK2j_OgMet9TMc51ZhqW7jzajvdYIaQeAyPlP8t3QtbiIwqwlRLnhSUxQtNtYPFmNbQH5rQ6uXQgPt1EBsTJskGvecE7_0ExEPKU6ztN3w-KJeeQBgfaC92z2Tqx2rQJVlV2zotHiQpqMypvBLZZkSpZuKm3HdviX77Tow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657059" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657058">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کانال ۱۴ عبری به نقل از یک منبع سیاسی صهیونیست: نتانیاهو باید به بمباران ایران پاسخ دهد، حتی به قیمت رویارویی با ترامپ
🔹
متأسفانه، به نظر می‌رسد احتمال حمله قوی و مشترک امشب اسرائیل و آمریکا تقریباً وجود ندارد./ میزان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657058" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657057">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مقر گروهک های تروریستی در سلیمانیه عراق هدف حمله قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657057" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PWLOH8rbwMe1quezcPw8MkOdYVlCfT8gZuaP7Htg-BlhTujOAXx2HB_8HIyhgMKDlVkeZQlmONs6JWkhxMxIt79a2x-7sawsgwOurN1ENOpwDOm5ochMTcXckAPuzYbesHqp6IAMPb2m4p5htThsxuZI736PTUWJ3oCR_La7AC7mnfnyq1-yFzBKuIbVRHzhTEEoDyjde6NAC2lAT3RmtYmAK5ZvkIlIriAUsX2Gc9YIFxEd6GHcGSi84IJj_I0fE7kJq_nHh06343vq7Az6KmkkTgmJ0zy3GznS2ScmzdNz135j8S68WU4HQJVIbtBSqas6rFLQad52T4Jh330Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز عملیات موشکی ایران؛ ارتش اسرائیل تایید کرد
🔹
ساعتی پیش ارتش رژیم صهیونیستی در بیانیه‌ای رسمی تأیید کرد که شلیک موشک‌ها از خاک ایران به سمت سرزمین‌های اشغالی آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657056" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: تاکنون آمریکا برای اجرای حمله علیه ایران موافقت نکرده است/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657055" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عراقچی در تماس با وزرای خارجه انگلیس و ترکیه و فرمانده ارتش پاکستان، درباره تحولات منطقه پس از پاسخ ایران به اقدامات رژیم صهیونیستی گفت‌وگو کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/657054" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مقر گروهک های تروریستی در سلیمانیه عراق هدف حمله قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657053" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صنعا با استقبال از پاسخ موشکی ایران: دوران عربده‌کشی رژیم صهیونیستی پایان یافته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657052" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
کانال ۱۵ رژیم: پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657051" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
القادر کربلایی، معاون نظامی گروه مقاوت نجبا عراق: آمریکا باید عراق را ترک کند/ سلاح‌مان را فقط امام مهدی تحویل می‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/657050" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🚀
تو را تنبیه کردیم حیدرانه
✨
انا علی العهدی
#امت_منتقم_و_منصور
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/657049" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
یدیعوت آحرونوت: ایالات متحده پیامی به اسرائیل منتقل کرد مبنی بر اینکه بهتر است چند روز صبر کنند تا ببینند آیا امکان رسیدن به توافق وجود دارد یا خیر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657048" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پروازهای فرودگاه امام (ره) تا اطلاع ثانوی متوقف شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657047" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
دفتر نخست وزیری اسرائیل: نتانیاهو به زودی با ترامپ صحبت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657046" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684792f89c.mp4?token=FFUDTYR1wNtNzgAP6xbgTDqLQj_nt-CA59XpWFRVF0gaN6RdTO4fGio-2Rr8jq8Nf6W2Z2NhoxWa7D0TM5-D_mPda3OS6Gt7mzMqwrHsbDOatcgHNqIcnBCPsF_ZcDHPDFocy7_0jEp4dHEvcP4_OWFziYaf_1EFg1dSE6xvi2dsWFgAgAOlsho8wWMtQPnzmEBfiOHEBRmXostNBSaAvg1XnNROSZ3QRzj1YwsFkNSwlVuWfnqjAmHUot1RP7zlQ-t72Y3bhzJJan6HaFXuhcp_HVD3i8yjL2fGG-tGnFUVIXu2QxYTEecSo4_oBwtH15oDmrHIDcX4r9xvSVSm7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684792f89c.mp4?token=FFUDTYR1wNtNzgAP6xbgTDqLQj_nt-CA59XpWFRVF0gaN6RdTO4fGio-2Rr8jq8Nf6W2Z2NhoxWa7D0TM5-D_mPda3OS6Gt7mzMqwrHsbDOatcgHNqIcnBCPsF_ZcDHPDFocy7_0jEp4dHEvcP4_OWFziYaf_1EFg1dSE6xvi2dsWFgAgAOlsho8wWMtQPnzmEBfiOHEBRmXostNBSaAvg1XnNROSZ3QRzj1YwsFkNSwlVuWfnqjAmHUot1RP7zlQ-t72Y3bhzJJan6HaFXuhcp_HVD3i8yjL2fGG-tGnFUVIXu2QxYTEecSo4_oBwtH15oDmrHIDcX4r9xvSVSm7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی مردم بعلبک لبنان از پاسخ ایران به تجاوز رژیم‌ صهیونیستی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657045" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVxp-fI6uvcvn1p2X1X5DeSoxCE-pIOJeye-lINpCkLAZ8ZWzsvuYxSFDYMfs9HoVz4Q6RKgMs_iq7W6bYHkY1HYfJmHw-XHcEql9bwU4EwNFn2A3Bt4EMzOExZS_OG67xqDQ8TvRiRUERnfsFVDfHiyBT-vhGZLwALtPYVMJrnT9EQ7br4U69QZx-Wcjjopxc7uoU8O5R2Yh35_e0l6fxJ6WX3aQ6WevUN2SMQDH30CLK6uuhA8M2v6SckIMqTWUVGuXaiYt5n1oS3yMjEv0QkPAxKGaBEbeopAANZAjV9Aj5sWE0TJPD4YcJ7ito-2M1k4Af1ds4nl2hIvMDdqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره ضربات دفاعی ایران علیه اهداف رژیم صهیونیستی
🔹
وزارت خارجه اعلام کرد حمله نیروهای مسلح ایران به اهداف نظامی در شمال فلسطین اشغالی، در پاسخ به نقض‌های مکرر آتش‌بس و اقدامات تجاوزکارانه رژیم صهیونیستی و در چارچوب حق دفاع مشروع انجام شد.
🔹
هرگونه ماجراجویی جدید علیه ایران یا لبنان با پاسخ کوبنده و همه‌جانبه مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657044" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سفارت آمریکا در اسرائیل به همه کارمندان دولت ایالات متحده و اعضای خانواده آنها در اسرائیل دستور داده است تا اطلاع ثانوی در محل‌های امن بمانند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657043" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
القادر کربلایی، معاون نظامی گروه مقاوت نجبا عراق: آمریکا باید عراق را ترک کند/ سلاح‌مان را فقط امام مهدی تحویل می‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657042" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=g9tjUV7Rl-wkpbL2XHJuNhQg1WuzhPV5EvcbyX2AyTJkTqcUIM0rxXq9rb-ROejz6KeNyrdyV0llnrKHXFwvuQCN-k2RdznbGGc0hBnFT-LF39NmgZRfYA3Uclwcl1CByQGHqz4bGhpIuRLrfh19Os6X3xcP8h7__TyjWU2JcOE9kVE3AL8oVD4bXtSSDzOi7tng-xImemi6R48SbQ9G7Ke3aNowimnTgm7nZvKee9MZWc-SjXjn1jf5mARNjck3-IthTfDHrMiW1eO53x4aQcfqeYYjWUFg6p4kb6gyiAHCcrcF4wJ30jUyvHLidaC7mSIFgDENmA3cMs_dwkaC-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=g9tjUV7Rl-wkpbL2XHJuNhQg1WuzhPV5EvcbyX2AyTJkTqcUIM0rxXq9rb-ROejz6KeNyrdyV0llnrKHXFwvuQCN-k2RdznbGGc0hBnFT-LF39NmgZRfYA3Uclwcl1CByQGHqz4bGhpIuRLrfh19Os6X3xcP8h7__TyjWU2JcOE9kVE3AL8oVD4bXtSSDzOi7tng-xImemi6R48SbQ9G7Ke3aNowimnTgm7nZvKee9MZWc-SjXjn1jf5mARNjck3-IthTfDHrMiW1eO53x4aQcfqeYYjWUFg6p4kb6gyiAHCcrcF4wJ30jUyvHLidaC7mSIFgDENmA3cMs_dwkaC-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امشب پهپادها با شعار «لبنان را رها نمی‌کنیم» راهی اراضی اشغالی شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/657039" target="_blank">📅 00:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df242f4b0.mp4?token=Y1t2X65f2ZC7gn_ZXP7ofZglaZ-ZabjkFqkXEkjlyeAEIhFJJTZewrn3Llh1g-ZpbxlfPZi7TOOEfmxGCwC6ORIL_EPPkx7xs4qw7B_V5Dm2efMhZH8IEB-8KvJc_QR-1w1B_-f9xNjc-pgbrZSqm5bfPw5xz-OK6sEVdpvzteRxIH1gCc4d5i9iHSBTjf6Z6fJLGUZGQwS0ZANQ2sMpfAwHSorGoUdxtk5eGtHPXc-3UJbCjmDZRGMN9dK0pYJ9wh8oOA2xYY0wcvzQuty59BApx-BAN_LMo6BJ91FvvT10jSFs5O42K8mKaOmBwZ45jnpT5-wH4yHeGOIY7P_cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df242f4b0.mp4?token=Y1t2X65f2ZC7gn_ZXP7ofZglaZ-ZabjkFqkXEkjlyeAEIhFJJTZewrn3Llh1g-ZpbxlfPZi7TOOEfmxGCwC6ORIL_EPPkx7xs4qw7B_V5Dm2efMhZH8IEB-8KvJc_QR-1w1B_-f9xNjc-pgbrZSqm5bfPw5xz-OK6sEVdpvzteRxIH1gCc4d5i9iHSBTjf6Z6fJLGUZGQwS0ZANQ2sMpfAwHSorGoUdxtk5eGtHPXc-3UJbCjmDZRGMN9dK0pYJ9wh8oOA2xYY0wcvzQuty59BApx-BAN_LMo6BJ91FvvT10jSFs5O42K8mKaOmBwZ45jnpT5-wH4yHeGOIY7P_cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
در روزهایی که خبرها دل‌ها را نگران می‌کند و چشم‌ها پیگیر حوادث است، خداوند در سوره‌ی محمد(ص) سخنی دارد که برای چنین روزهایی نازل شده است:
▫️
«وَلَا تَهِنُوا وَلَا تَدْعُوا إِلَى السَّلْمِ وَأَنْتُمُ الْأَعْلَوْنَ وَاللَّهُ مَعَكُمْ»
▫️
سست نشوید، خود را نبازید و بدانید که اگر در مسیر حق بایستید، خدا با شماست.
▫️
سوره‌ی محمد، سوره‌ی استقامت است؛
سوره‌ی آرامش در میانه‌ی اضطراب،
سوره‌ی امید در هنگامه‌ی تهدید،
و سوره‌ی یادآوری این حقیقت که پیروزی پیش از آنکه در میدان‌ها رقم بخورد، در دل‌ها آغاز می‌شود.
▫️
امشب برای قوت قلب، برای آرامش خانواده‌ها، برای رزمندگان اسلام و برای پیروزی جبهه‌ی حق، سوره‌ی محمد(ص) را با تدبر بخوانیم.
📖
سوره‌ی محمد؛ سوره‌ی ایستادگی مؤمن
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657038" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657037">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای آمیکای اشتاین خبرنگار آی ۲۴ رژیم صهیونیستی: «در طول یک ساعت آینده، یک بحث گسترده با حضور بنیامین نتانیاهو، وزیر جنگ، و فرماندهی عالی امنیتی درباره ایران آغاز خواهد شد.»/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657037" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657036">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf12cfa85.mp4?token=eDB7jZ30vijKSrqQpaFh8lD0UGcqPl992vZ6_B0Naf4WrPPURE-ZZBlrKVWV6e6cy1K1KV0lv1oIQ-nmLxAghncueZsSWrwX0CyP5Tuz4X24se1PEN-x-tVsZ4tW_AtKG6w6tjZFE64jgHPeFi-P4yNUUo4tlkWnDbbusLqwAkk9muiftUtFsB3oXIDIJLn2wfubTS26n9RwwLVjY7R_Au_b_psdu4D0kmIBvI5RsjiKaz0vzHpkEFVgOfTqNkAeIwQoucS0ja4iqINHKxmsaQ3J1sMlnqt_lbJdSYW5K_JUokiWw9bt2oqV2da4t3huDdUVsZJneeyTegUDZIq-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf12cfa85.mp4?token=eDB7jZ30vijKSrqQpaFh8lD0UGcqPl992vZ6_B0Naf4WrPPURE-ZZBlrKVWV6e6cy1K1KV0lv1oIQ-nmLxAghncueZsSWrwX0CyP5Tuz4X24se1PEN-x-tVsZ4tW_AtKG6w6tjZFE64jgHPeFi-P4yNUUo4tlkWnDbbusLqwAkk9muiftUtFsB3oXIDIJLn2wfubTS26n9RwwLVjY7R_Au_b_psdu4D0kmIBvI5RsjiKaz0vzHpkEFVgOfTqNkAeIwQoucS0ja4iqINHKxmsaQ3J1sMlnqt_lbJdSYW5K_JUokiWw9bt2oqV2da4t3huDdUVsZJneeyTegUDZIq-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه تی آر تی ترکیه با توقف برنامه های خود به خبر حمله موشکی ایران به سرزمین های اشغالی پرداخت
فَإِنْ قاتَلُوكُمْ فَاقْتُلُوهُمْ كَذلِكَ جَزاءُ الْكافِرِينَ
🔹
پس اگر با شما جنگیدند، آنان را بکُشید؛ که سزای کافران همین است.
🔹
بقره ـ ۱۹۱
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657036" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657035">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تکذیب حمله به فرودگاه تبریز ‌
🔹
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است. ‌
🔹
دقایقی پیش اخباری در برخی کانال‌های تلگرامی مبنی بر شنیده شدن صدای انفجار در فرودگاه تبریز منتشر شده…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657035" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به شهر زیفتا در شهرستان نبطیه در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657034" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">و ما النصر</div>
  <div class="tg-doc-extra">حاج محسن طاهرى،كربلايى محمد مهدى طاهرى</div>
</div>
<a href="https://t.me/akhbarefori/657033" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/657033" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وزارت خارجه یمن: پاسخ ایران معادله وحدت میادین را تحکیم می‌کند. محور جهاد و مقاومت برای مقابله با هر تحولی در هماهنگی مستمر هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657032" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a7d5f654.mp4?token=M3KIcA4Z_LZHEsXocKlZ6qhV-lWXCNyIOkbH9Y0BQblQKNzngKAb-Cuqo6VNJNrEhXnegW9mvl4sqF5u6mAJSFIaYRPYRDyXDUniLyt_Bl6n0BB6Z0tYDUvBeJMaoDX6tJxILrZSd8wWPc2FgezL1RQoCxyxsLUUBJRFZ35zeZvVF45xizXVrWWVTEw4Yh-NzTJDC2nM34Jcgreg3eethJyoOK-6meHsd-QssfuOrUCn0SENHbWaH_H7ZvbSwhZssrAbmZY2vU0c9YmQyJwjhcfrmIsEmYTqyP5Easz7X84InkiSbxQmkCTqTd3Xk3zUcq82XY-K4Q772Mf3fTQXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a7d5f654.mp4?token=M3KIcA4Z_LZHEsXocKlZ6qhV-lWXCNyIOkbH9Y0BQblQKNzngKAb-Cuqo6VNJNrEhXnegW9mvl4sqF5u6mAJSFIaYRPYRDyXDUniLyt_Bl6n0BB6Z0tYDUvBeJMaoDX6tJxILrZSd8wWPc2FgezL1RQoCxyxsLUUBJRFZ35zeZvVF45xizXVrWWVTEw4Yh-NzTJDC2nM34Jcgreg3eethJyoOK-6meHsd-QssfuOrUCn0SENHbWaH_H7ZvbSwhZssrAbmZY2vU0c9YmQyJwjhcfrmIsEmYTqyP5Easz7X84InkiSbxQmkCTqTd3Xk3zUcq82XY-K4Q772Mf3fTQXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهره وحشت‌زده خبرنگار صهیونیست اینترنشنال در پی حملات موشکی ایران؛ اسرائیل فکرش را هم نمی‌کرد که ایران پاسخ بدهد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/657031" target="_blank">📅 00:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657029">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: دشمن با میلیون‌ها جانفدا روبه‌رو شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657029" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657028">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuw7V7PUYD7tIVp54SMh7XBQ4Mr6RCkMGv5LapJ_GB1Oy8gEGSEqMS0N-FrC0xqDhXkoNHzbEazDO0hIrzEvH710X0daqHsxD75Hwkim55Q9EuF9S-v7u83h2CtpjJ2aVyElkO0_79cEKgzKDz7C1T4NBI1iDYEAC-PLbrkYk2BUUsSbXczRxLglB4rdRNLtvBFaHETz7Day79xuTIl10BfjFgpCf3de8FimT_2IHzOmkDb_kDr4BmaFpGpaK7f1ziLjFfCZIuTmicjsSqB0A_QinCUyNHga8vRSwcrdGs-_6v2ByuGHCT2XVh-qz3Hh382pXs5L-ltK0dgbDuN3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در بیروت: همیشه در کنار شماهستیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657028" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657027">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یک منبع نظامی: موشک‌های ایران آماده‌اند در صورت پاسخ اسرائیل فوراً شلیک شوند
🔹
اگر اسراییل پاسخ دهد، نوبت بعدی شلیک‌های ایران، پرحجم‌تر خواهد بود.
🔹
این منبع نظامی خاطرنشان کرد: ایران برای آغاز نبرد گسترده در صورت پاسخ صهیونیستها آماده است و صهیونیستها باید این هشدار را به گوش بسپارند. / تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657027" target="_blank">📅 00:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657026">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
کمیته‌های مقاومت فلسطین ضمن قدردانی از پاسخ ایران به رژیم صهیونیستی، اعلام کردند این اقدام معادلات جدیدی ایجاد کرده و بار دیگر معادله جبهه‌های متحد را تثبیت کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657026" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657025">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657025" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657024">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40efaad5ad.mp4?token=Is3jxN_QZQw8JgmGFi3fOrAR8WDyFWzESzgxeTgkDROU9pVZpxzwun717aNuClMNOv-yeOSN1tKGBsp694uIFI630rknwhRoXMM8vGFuRopckYTwJbv8-1SPaD6zZ1-PnBE6XB0rdNcabnwSKqkPX8t1TXMGhLAqRH7kLmL0sR9LDxnV2wVlJUVL4vmxc446SllAu7ZN5PTSl0cw7bMzmID9AxZ2Y1cMFcI2gxsMIszWYMGO_6fCe_xsa4vpgVyTQwnW4uOoXTARpvwG2xiGooTGYOVjCleVPOGE5NISh3Kwk_5i1yD5zdRXyrGQOGK6VM1JA-TF-RLdjn2y75jfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40efaad5ad.mp4?token=Is3jxN_QZQw8JgmGFi3fOrAR8WDyFWzESzgxeTgkDROU9pVZpxzwun717aNuClMNOv-yeOSN1tKGBsp694uIFI630rknwhRoXMM8vGFuRopckYTwJbv8-1SPaD6zZ1-PnBE6XB0rdNcabnwSKqkPX8t1TXMGhLAqRH7kLmL0sR9LDxnV2wVlJUVL4vmxc446SllAu7ZN5PTSl0cw7bMzmID9AxZ2Y1cMFcI2gxsMIszWYMGO_6fCe_xsa4vpgVyTQwnW4uOoXTARpvwG2xiGooTGYOVjCleVPOGE5NISh3Kwk_5i1yD5zdRXyrGQOGK6VM1JA-TF-RLdjn2y75jfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار کربلا: جسم ساقط شده در صحرای کربلا پهپاد است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657024" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657023">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تکذیب حمله به فرودگاه تبریز
‌
🔹
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است.
‌
🔹
دقایقی پیش اخباری در برخی کانال‌های تلگرامی مبنی بر شنیده شدن صدای انفجار در فرودگاه تبریز منتشر شده بود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657023" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMbDnwun9E2SFJ13943BbSRA6t1oDBvvhYYO6gTkYy4-jxqnC23jQbxZYSKqfaBTzAWdxx_STCE1RecAJ_5LsnIsuI6katpBMzXyAeZKGxTbQ82TfH41jQaYWHyi6RmSpE-pRqzm9dT_XFRan_oadPhNZqiAci_UZTdDhqYxcWOHh0YBK6Vti49pmCFo2aPq5Ae0dFXXmjcUZBT7H8IKQFpskBoCgUZxvKJmWoEuL6C_jKNzw7rxjmk6e40425XcaghQHfuFrY3K4BarcEpJVwkKxOtpiI70eyMwAjq79h7fvh0NO5OaoyjQRsZzZ1VBbvzYHy1EqVZmVoAcX2QZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
در این زمان که امیدی به سازوکار جهان نیست
پناه کشور ایران به جز امام زمان(عج) نیست
✨
دوباره بازی‌شان را به‌هم زدیم بفهمند
که شیعه‌خانهٔ مهدی، زمین بازی‌شان نیست
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657022" target="_blank">📅 00:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh7f4MATNV3AclPakwePhOC4UgTYHeyAOc75Cvj4-5yq9pDYBn_9nr4CACiB7ILAcYbV-dAzHLbMRw3X-BT2BZk6F437knCTJjEgdOM1ehN5UMSclhvM-umzXeKebj9j8L200_NZZBhbDd7rX9WOrA-k6QOJqh5CK6BcY_3Df4NW0wWMD6gLfR5mzKrZGgyf8UvtjLfhVN3T2eXJet0fxYu8kxFfTAcIrn2Ae3PGqEotKJtNGMfCNfoJ62Yqf_-L0gpvXLACBI9tdqlOGp-cM1SF5073rQyKEU_pfWdLwewXvwxvqCQVZV2wFggYAvsETfsoy2BAEXoVZl1ENzR36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده رهبر انقلاب در شورای دفاع: صدای خروش ملت ایران را در آسمان تل‌آویو بشنوید/‏ادامه مسیر فشار و تهدید، پاسخی قاطع‌تر و کوبنده‌تر در پی خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/657021" target="_blank">📅 00:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
یک منبع ایرانی: هشدارها درباره نقض آتش‌بس را عملی کردیم
🔹
ایران بارها تأکید کرده است که دوستان خود در لبنان را تنها نخواهد گذاشت؛ این تعهدی است که از آن عقب‌نشینی نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657020" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657019">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd77c7956.mp4?token=A47tDTt5Wz-Yzpqi2Ff_EtGH9wQzXlJzsml0ZF9nx-vY3haqPZOza6joVQyOtNyaCl0WLDJki9JSoLELaO1Rc1rt2bStn9EC85VqKWCJ9mqcFEdNuxfKvB22B9f0hg59nTUUeGTZ5krfRwgYvaTjj7STmCmB_sn6ZSpo5Dc90cUwonZ9su-aW6VKK4f935EisxhRv8NsknirDpDoUGbWqIoKwGrSk3IyAlJiRFQj8NYrexw15QT7-iTJ6oEPyi_vJbExBW7fvSLbvbj7WDMn4Vj159ZsZ4dDHeTFPhfIdMjFErF4X2U24_JfxN63Di1RIsuf3BoI9cdykTRoSzQwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd77c7956.mp4?token=A47tDTt5Wz-Yzpqi2Ff_EtGH9wQzXlJzsml0ZF9nx-vY3haqPZOza6joVQyOtNyaCl0WLDJki9JSoLELaO1Rc1rt2bStn9EC85VqKWCJ9mqcFEdNuxfKvB22B9f0hg59nTUUeGTZ5krfRwgYvaTjj7STmCmB_sn6ZSpo5Dc90cUwonZ9su-aW6VKK4f935EisxhRv8NsknirDpDoUGbWqIoKwGrSk3IyAlJiRFQj8NYrexw15QT7-iTJ6oEPyi_vJbExBW7fvSLbvbj7WDMn4Vj159ZsZ4dDHeTFPhfIdMjFErF4X2U24_JfxN63Di1RIsuf3BoI9cdykTRoSzQwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات و اهداف حملات امشب ایران به سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657019" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657018">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ترامپ افسار نتانیاهو را کشید
🔹
با نتانیاهو تماس خواهم گرفت و به او خواهم گفت که به ایران پاسخ ندهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657018" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657017">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162802ccab.mp4?token=ZuSW95r3dtfCT3gBUkWtVS_EnC0365ofHWI1gPQxeKX-MBy5TA9aegvZB0zsoBrzwOqpokiUVCdV6pD9avmz1X_ZyFXViUkdj_N2ZY8lp3USwNZ_o71Q1ZxM8Xg51I20aQX5sqU6xTddk_FxX79qVPA_d4dDjRDnYrXfKZWf14zT11YqoFtY_CtfliSYYpVM-gyzeMMMu8e39yW3YnwItYGA5fn1-KjndqCsddQzFkPfG_THTcQoyRxJWEmZus_U3SHdZyA67gl-8r8gtQujB0RpxbwDv3lS5-M8uo0F-gC--DEJ1R-sIa4VndbjAYkJQKVe2n7RipZ8ERw2Dij48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162802ccab.mp4?token=ZuSW95r3dtfCT3gBUkWtVS_EnC0365ofHWI1gPQxeKX-MBy5TA9aegvZB0zsoBrzwOqpokiUVCdV6pD9avmz1X_ZyFXViUkdj_N2ZY8lp3USwNZ_o71Q1ZxM8Xg51I20aQX5sqU6xTddk_FxX79qVPA_d4dDjRDnYrXfKZWf14zT11YqoFtY_CtfliSYYpVM-gyzeMMMu8e39yW3YnwItYGA5fn1-KjndqCsddQzFkPfG_THTcQoyRxJWEmZus_U3SHdZyA67gl-8r8gtQujB0RpxbwDv3lS5-M8uo0F-gC--DEJ1R-sIa4VndbjAYkJQKVe2n7RipZ8ERw2Dij48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در فلسطین اشغالی  وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
🔹
سست نشوید و اندوهگین نباشید؛ شما برترید اگر ایمان داشته باشید.
🔹
سوره آل عمران، آیه ۱۳۹
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657017" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657016">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKKgl3WLHlunI_60jlnCn9VUzxONO7lO7jnANKlN9qxsRd74CIsBcIuOxfQgSnXOQ4W7GB4VoN92xxqF7Qo8UCeixjFAT9bVdgXi3BfHSMu-Ntz6ft1QRqnTgTfhFGlL96RsdF3AcaZJbmuKXXBVlpSeDPrTRPZiUg5OpisV-MXMtnBRH8JHS7TpxjlJKy1exvoMpiexvYQSBU9Sq2N4SinOvnx8POR5fwl7tpzVNilczhXfwEe3K0UfpO3u1Fkhuuc5z1u5xEenbc16KVMlAPy3vBldHUqnc6AjvvXDtJ4-wchyP6gAew4vHS6eUY-jRfu12FlBwKZEjGM2MjS62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
עוקבים אחריך, אל תטעו.
تحت نظری، اشتباه نکن
#WillPayThePrice
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657016" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657015">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ ایران خداقوت</div>
  <div class="tg-doc-extra">مهدی رسولی و محمد اسداللهی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/657015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
خیابان خدا قوت
میدان خدا قوت
جمهوری اسلامی ایران خدا قوت
ایران خدا قوت ایران خدا قوت
اینجا فقط ما به خدا میگیم ابرقدرت
🎙
#مهدی_رسولی
🎙
#محمد_اسداللهی
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657015" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657014">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ترامپ به شبکه کان:ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم
🔹
«فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. دیگر نیازی به هیچ اقدامی نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657014" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657013">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منابع عراقی: نیروهای امنیتی در عراق هشدار جدیدی در نزدیکی منطقه سبز و فرودگاه بغداد اعلام کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657013" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657012">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پدافند در بخش محدودی از غرب تهران فعال شد. این اقدام به منظور افزایش امنیت و آمادگی در برابر تهدیدات احتمالی انجام شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657012" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657011">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlmwwZYtvRqv_TfwNuYjYwY31yh1EZbq7gl_P86eI2thqcTCkf1MCr5LHF86fFqT3_z4MtyAfC9b_uPSjnSpXP6iOV9r6UJ7KOtlvE2dBeunvT0NcSV_e1--kOiExnv8TJwfRPbGZ_CWPuVJro8cI5aFWWZcQ2rgnRtdoNsbhP1gy9YrSJTYqBwtvJn6_f5zHmuRUcOoGFzWo5UQLtcyYc4rBIMRqOkwL2LfC34-JibBk5mm-HcLONgKEJqPyoTMawr-g1PBuzbTCfIAbC29CmJjSezT18KXtX1yDIPXIvvMJYrNwV8L37H-BScxg8RiGqXCiOHwuEUDQai2WOhoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره و تسهیل گری در فرایند اخذ وام های بانکی
نیاز به وام دارید اما در میان انبوه بخشنامه‌ها و فرآیندهای اداری سردرگم شده‌اید؟
کافی‌نت آراد با جواز کسب رسمی، اینجاست تا مسیر دریافت وام‌های معتبر بانکی را برایتان هموار کند.
✅
خدمات ما:
• انجام مراحل اداری و پرداخت وام در کمتر از ۷۲ ساعت
• مشاوره و بررسی شرایط شما برای انتخاب بهترین وام بانکی
• ثبت‌نام آنلاین دقیق و بدون نقص در طرح‌های تسهیلاتی
• آماده‌سازی و تنظیم مدارک مورد نیاز
• پیگیری روند درخواست تا دریافت پاسخ نهایی بانک
📎
برای شروع، پرسشنامه اولیه ما را از طریق لینک زیر تکمیل کنید تا کارشناسان در اسرع وقت با شما تماس بگیرند:
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
کافی‌نت آراد؛ پیشگام در تسهیل امور بانکی شما
🏦</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657011" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=c-y_oLdUPLRsQywk1oQNyE5liksf2wSuu0pniGstFIRL4-N07O6bClZ6kuVh39l3jT-IK3wgLAU4tA5sdEcTHdLSL33RNw-UxroDbwOixFRuiMj0SqAk4GSYMKW-mAelaTh7uGnJp54HICI75wVNwbpgVe4m6bRaR8eWai70xcKx0av5J4X2Ls1SBks2Y9UK4RhyD4PD1QzmSstXFWaS8EQ_Fl_nMFwqXAQhGlJq7qhgMednn7uypNPjVrX59rO2v_-ria3ITFPz7EnSR28R7F58CHXa8YQ7w4tQomgj3zKMhUy7N9ydRQESOgrAK41UxAjlmTq-5bywsK4SHrkkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=c-y_oLdUPLRsQywk1oQNyE5liksf2wSuu0pniGstFIRL4-N07O6bClZ6kuVh39l3jT-IK3wgLAU4tA5sdEcTHdLSL33RNw-UxroDbwOixFRuiMj0SqAk4GSYMKW-mAelaTh7uGnJp54HICI75wVNwbpgVe4m6bRaR8eWai70xcKx0av5J4X2Ls1SBks2Y9UK4RhyD4PD1QzmSstXFWaS8EQ_Fl_nMFwqXAQhGlJq7qhgMednn7uypNPjVrX59rO2v_-ria3ITFPz7EnSR28R7F58CHXa8YQ7w4tQomgj3zKMhUy7N9ydRQESOgrAK41UxAjlmTq-5bywsK4SHrkkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه این‌مدارس در ایران است؟!
ویدئوی بالا به هیچ وجه از دست ندید.
دبیرستان دخترانه هوشمند مدبّران برنده جایزه بهترین سیستم آموزشی خاورمیانه
"مدارسی از جنس رشد و شکوفایی"
🟢
این مدارس توسط
دکتر علی میرصادقی (روانشناس) طراحی وبنیانگذاری شده است.
✅
همین الان جهت ثبت نام در آزمون ورودی و کسب اطلاعات بیشتر به آیدی زیر  در تلگرام پیام بدهید:
@Modaberane_Barsa
یا عدد 4 را به 3000909030 ارسال کنید .
توجه:این دبیرستان ها تنها در تهران دایر است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657010" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حزب‌الله لبنان: ما تجمع سربازان دشمن اسرائیلی را در مجاورت قلعه تاریخی بوفورت با موشک و توپخانه هدف قرار دادیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657009" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اسرائیل: آماده شلیک موشک‌های بیشتری از ایران هستیم
🔹
ایران تلاش کرد پس از حمله ما به ضاحیه بیروت تعادل جدیدی برقرار کند و ما اجازه نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657008" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بعد از قطر آسمان عراق  هم بسته شد
🔹
الفرات نیوز نوشت که در پی حملات ایران به اسرائیل، آسمان عراق بسته شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657007" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی:  اکنون به شهروندان اجازه داده شده است که از مکان‌های حفاظت‌شده خارج شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657006" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAdSlpeGECkEQO3vElXN5C1SpG3DXjd2dTd7dIox2UNlsgygHWf5NNJ23Nl4RUchs2tkb6aRBpEyDMfFjONBpoUcSoTx4pd2CK90j5RIYVNuqt1845TJn1ecBdrPu_1EaYNRh2bVkYsc94pEGLT4RuTxVN8JO_x3RazABeZQwWudZIag5h0XH5dwitwHlkPZM_rqC5JA3-fEYsdMutS6bBD8asOg9gPxTNEzvW5OPZgI03jj2bCDgqd497puZMwG52WsV4-StSUQnVFsupWZGnVzva8bFIT_jfQaFG6-_vINOM84nJ1BBh9Sk2xRu8VjgS8iRjMZFoWW9KIwOe5iPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657005" target="_blank">📅 00:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAgeoCWbkh8e-q5XTsIgsq72ywaAQcIzNSrjaZD220Cpkv5AGBBLzMrfMfW8AofWnVMsd3WSAzSlqqisoKYwWTKyq8VxjlmX5bV-uA6uDkk5SqBfXKcYUnUrJwPNG7EqsG37PowvcxYdbOJy5AjQUaXSOh9GNnkOa4FBJZzZUSZQSbpXSdf30TEOI5XAMovA8IISu4K3Kx_8TP_xb9HNSr4myPHbkehyBYnkwtCpZRjjltuCp0XWiXVrVHFgKBJ79uieJwi52noVMh7_lyU3y2lr23_ncmDEfCz55Z2wzOyMsRH1ybZ0ShaEKCOViX49Vhqg85MFuPFCS3Z6QqzlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک پیام برای سید مجید موسوی و اپراتورهایی که امشب پشت لانچر نشستند و قلب تل‌آویو را هدف قرار دادند بنویسید
👇🏻
🔹
پاسخ‌های شما در خبرفوری منتشر می‌شود و به دست سربازان گمنام امام زمان خواهد رسید
ویراستی خبرفوری را دنبال کنید
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657004" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUV-22RHziRvRlmZEimaWwUd--mBGD5XSy8JGoefFlLsF9Jmtu4-HbWJnBUh0Fv-s1EZsDre1NBSpfgNKIGVxJSRxGoc4QLzphjSJmxN2qnaFvTL27wfNZHdfaAjkOUwb3Iox0XND-eWyoDdjdj8yOS6Ds_8r93N_jkmRnnq3aEgxSieo-H10BhwC2Wcplm2RFFLv-2oMW4ptzDBi0g2qYC-Mpces5mnmDaLO9x_EVILskJ9nrBr6LVglwRiDHc0bBb44S4djW9Nkz7cgtVLT_eOrNZ73M9pO_AcTK5Jm0xKPOFzbtw7K2LYEMVDQB_F41cGzf-cdCc1HdwmVApfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشته روی یکی از موشک‌های شلیک شده سپاه: ما درحال مبارزه با فاسدان جزیرۀ اپستین هستیم
#جاسوس_موساد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657003" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
هشدار ترامپ قمارباز به نتانیاهو توافق را نابود نکن  ادعای ترامپ به شبکه ۱۲ رژیم صهیونیستی:
🔹
هیچ‌کس در حمله موشکی آسیب ندید. اگر نتانیاهو پاسخ دهد، این وضعیت ادامه پیدا خواهد کرد و ادامه پیدا می‌کند.
🔹
نمی‌خواهم این موضوع توافق را از مسیر خارج کند. هر دو طرف…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/657001" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی:  اکنون به شهروندان اجازه داده شده است که از مکان‌های حفاظت‌شده خارج شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/657000" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5acc5df7.mp4?token=mqQjEU5oggHfsCNl5SR1ZRqhKCIBSkMcJT-Y08v7W0KSx3rr3cnyIekNdQkr0N_e_LRmzAevYFSx-xdc3CAQFEohqSnAO98DlYgBbh4dzS4J9qsyU6g1DOI0eaog90k-USCX3PskmHD-PE-hTAN9j5wF1FgP05PiP6n8iXVRKLiqV9upmfsx7XmHJyayAblgA2MMO_g01Lrg8Cj2fYp1YtHCIKMlQiBaGslLRqJR2F45JYFLf3ZP4ENR5kkeHON4UuDTcT85ypw-fZWOlc6fFT1sDP2qjWD8UxwV_iLWgcLe8SWk3WnEAV68GnkMLbXSaEhWVKweeSk06mZPlmc86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5acc5df7.mp4?token=mqQjEU5oggHfsCNl5SR1ZRqhKCIBSkMcJT-Y08v7W0KSx3rr3cnyIekNdQkr0N_e_LRmzAevYFSx-xdc3CAQFEohqSnAO98DlYgBbh4dzS4J9qsyU6g1DOI0eaog90k-USCX3PskmHD-PE-hTAN9j5wF1FgP05PiP6n8iXVRKLiqV9upmfsx7XmHJyayAblgA2MMO_g01Lrg8Cj2fYp1YtHCIKMlQiBaGslLRqJR2F45JYFLf3ZP4ENR5kkeHON4UuDTcT85ypw-fZWOlc6fFT1sDP2qjWD8UxwV_iLWgcLe8SWk3WnEAV68GnkMLbXSaEhWVKweeSk06mZPlmc86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده خبرنگار بی بی سی از بیروت: موشک‌های ایرانی موجب خوشحالی و هیجان لبنانی‌ها شد؛ پاسخ ایران خیلی زودتر از انتظارها انجام شد! همزمان، حزب‌الله هم رادارهای اسرائیل را مورد هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/656999" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b452e02.mp4?token=TmXJKwd8k8IQIZmXZfzYA6gBeMe-ygxCvWI1wY_lErIuXFEOlC1J4rtVZpK-l-PYYW-O99TOkM4FfV7DzCAYtLKVy4egJKh9TPxoZFSJgedqoCLV-1BTHzfXwdzpM48YE_JQQvWnXaHpuj5SJKQjfsOrzuX1xR_as0CCuechwV6eQnCNMg3jBxq9srYYLIcLSez0UU2G4Bvlj74qc8DBuJC8guar0kr8M5DwQ3I1xgg9ILhwww8JzR8e9O-GRJDXk9_WPimtMBjVvD6rBrpDl8fJvJTVs2DF-nqbxiuM4C3r-xHXcpeUcbKlF2UfuTLSmwWW_kpNUtRRVE6aGtqU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b452e02.mp4?token=TmXJKwd8k8IQIZmXZfzYA6gBeMe-ygxCvWI1wY_lErIuXFEOlC1J4rtVZpK-l-PYYW-O99TOkM4FfV7DzCAYtLKVy4egJKh9TPxoZFSJgedqoCLV-1BTHzfXwdzpM48YE_JQQvWnXaHpuj5SJKQjfsOrzuX1xR_as0CCuechwV6eQnCNMg3jBxq9srYYLIcLSez0UU2G4Bvlj74qc8DBuJC8guar0kr8M5DwQ3I1xgg9ILhwww8JzR8e9O-GRJDXk9_WPimtMBjVvD6rBrpDl8fJvJTVs2DF-nqbxiuM4C3r-xHXcpeUcbKlF2UfuTLSmwWW_kpNUtRRVE6aGtqU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: صهیونیست‌ها در صورت پاسخ به اقدام ایران با ضربات کوبنده روبه‌رو می‌شوند و حملات ویرانگر علیه رژیم و حامیانش آغاز خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656998" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گفتگوی تلفنی عراقچی و فیدان
🔹
طرفین در این گفتگو درباره آخرین وضعیت روند مذاکرات ایران و آمریکا بحث و تبادل نظر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656997" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ترامپ افسار نتانیاهو را کشید
🔹
با نتانیاهو تماس خواهم گرفت و به او خواهم گفت که به ایران پاسخ ندهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/656996" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1eb172af.mp4?token=szHxHQbmpHn9Ifdpv9o8uQ4ZM1h06uedR-qG82GwXRIoYk7pXD2sTqXBuwmm8b2wO7Ue3ZFXceuuIfzcST1w3Z75RAAPiC9mFcduPr5txLkIDICfdktuXzls939VrAZc63CCxwhLnB7WThEvrdu0OcVE_ZsTaLPO0pOU2WhMWwozpjCmQl5dBMglczv9pYleJKZzGH6MJh7eZ-gFGNkUCzXRm9ZhoaMKUgmGEYwWureefCpkYwd1-mNrVn7IP8nG-Kx2jnKD5blejMiGZhASWi1KXMmGpbAPR5PvtuazFWvsWN1mkObR-VtovFE0Fq-jScPgrUHQ0WJk_tcCnn5YYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1eb172af.mp4?token=szHxHQbmpHn9Ifdpv9o8uQ4ZM1h06uedR-qG82GwXRIoYk7pXD2sTqXBuwmm8b2wO7Ue3ZFXceuuIfzcST1w3Z75RAAPiC9mFcduPr5txLkIDICfdktuXzls939VrAZc63CCxwhLnB7WThEvrdu0OcVE_ZsTaLPO0pOU2WhMWwozpjCmQl5dBMglczv9pYleJKZzGH6MJh7eZ-gFGNkUCzXRm9ZhoaMKUgmGEYwWureefCpkYwd1-mNrVn7IP8nG-Kx2jnKD5blejMiGZhASWi1KXMmGpbAPR5PvtuazFWvsWN1mkObR-VtovFE0Fq-jScPgrUHQ0WJk_tcCnn5YYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656995" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بر اساس گزارش‌های اوسینت در شبکه‌های اجتماعی، دست‌کم سه موشک ایرانی به اهداف خود در سرزمین‌های اشغالی اصابت کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656994" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33e8867c3.mp4?token=Mzy6j-Dd4txuV6BLRmW5Omcjg8b39iLwUbSi-kaSh6TALMiOOT4z2bdxArf643l3sBIHM-nKildpB9C0TdCVDTrQ8beJp28cMxNZjqJ7cMV8hI6pztulTL3zp6cSZkfHY2ZWGaSSdqzbYnRsT_OuEmncp6pMvo-6aCF0kuubU3G1ca1qQfwNd1WzGOuQZbzyPDtIF556WpoZU02NHeBuExjbL-BSQl0iRA6Lpyhy_zhAXPVwyBmxPC5KKyfG0QK09nObUsJ20AGol7GP0N9klE0boK5rkXMmuF8IAKcrX1usBsh_eXcxKJuTy-I-irzgImJipf9v7UskmZnWsh26WWVcB502ofhQM5oLxCXreE3NnAtz_XtZL3xJEzdtGozBUyMS8_v38aALxerMYGzgoPa-FjFJqdpFgi6AGtreSGsng82Urj27loswaUmYWEoNJQhjXXq1D-AT0LSl58xj6AebDqCNM92PJutDCfG0mULN06XUfrAph6f9NP3qsJ4AMILCk7aI03KZvgyFWqNixQwbYIL7VNyc2QKxsHGDTUOJjPiCJlye9FXkyeio5KttR-7J49GdBhWzYQVPCkXC5436ZHSDms74UcHYKjeZl9EbOUtXGvOyp6WD02MN27Ee359-WJSe49WyyAZbbMbe0HwBs7Pftwa-iwlPpgdaSmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33e8867c3.mp4?token=Mzy6j-Dd4txuV6BLRmW5Omcjg8b39iLwUbSi-kaSh6TALMiOOT4z2bdxArf643l3sBIHM-nKildpB9C0TdCVDTrQ8beJp28cMxNZjqJ7cMV8hI6pztulTL3zp6cSZkfHY2ZWGaSSdqzbYnRsT_OuEmncp6pMvo-6aCF0kuubU3G1ca1qQfwNd1WzGOuQZbzyPDtIF556WpoZU02NHeBuExjbL-BSQl0iRA6Lpyhy_zhAXPVwyBmxPC5KKyfG0QK09nObUsJ20AGol7GP0N9klE0boK5rkXMmuF8IAKcrX1usBsh_eXcxKJuTy-I-irzgImJipf9v7UskmZnWsh26WWVcB502ofhQM5oLxCXreE3NnAtz_XtZL3xJEzdtGozBUyMS8_v38aALxerMYGzgoPa-FjFJqdpFgi6AGtreSGsng82Urj27loswaUmYWEoNJQhjXXq1D-AT0LSl58xj6AebDqCNM92PJutDCfG0mULN06XUfrAph6f9NP3qsJ4AMILCk7aI03KZvgyFWqNixQwbYIL7VNyc2QKxsHGDTUOJjPiCJlye9FXkyeio5KttR-7J49GdBhWzYQVPCkXC5436ZHSDms74UcHYKjeZl9EbOUtXGvOyp6WD02MN27Ee359-WJSe49WyyAZbbMbe0HwBs7Pftwa-iwlPpgdaSmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم الانبیا: قبلا اخطار داده بودیم...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/656993" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
گفتگوی تلفنی عراقچی و فیدان
🔹
طرفین در این گفتگو درباره آخرین وضعیت روند مذاکرات ایران و آمریکا بحث و تبادل نظر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/656992" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilvwiRAM0_c7Nj6K4WPNUON3KlntbaaVu8XQi_hLI09bHQ_6V0575ggqjA7F2eGG_f25mz6-JdmKpEqyYkpUF48MAei7R4Tvtqpsxdr831t0wM6qVzQ3W3C_ReuLZo37_4GMBWlU6WnaKeU8Ushf7isP8N8-alGpzcUOEMdWT_KMvPR9OYoIaA-ODq8eKbZ-US0f3q3ro22SinoGYs3IqmzM0yTY-f5BMQvNc8CJHQ_SyKPvNM3TtWOzQqmglJL_bE__PS7TxCnso_nY2Jis1ZZMeLdOiFOf-oJFI3wJsEQAoueGvLFWe6uers0phrktXIWbv9WH3sE4Meb5XN_CfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
You're so scared that you're digging your own grave
🔹
از ترس قبر خودت رو می‌کنی
‎
#WillPayThePrice
‎
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/656991" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
آماده‌باش نیروهای عملیاتی هلال‌احمر در سراسر کشور
🔹
در پی نقض آتش‌بس توسط رژیم اشغالگر در مناطق ضاحیه جنوبی لبنان و با توجه به احتمال حملات دشمنان، نیروهای عملیاتی هلال‌احمر در سراسر کشور به حالت آماده‌باش کامل درآمدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/656990" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ ادعا کرد که از حملات امروز اسرائیل راضی نیست
🔹
نزدیک به یک توافق با ایران بودم و حالا این اتفاق می‌افتد
🔹
ادعای ترامپ به فاکس نیوز: حملات اسرائیل با ما هماهنگ نشده بود #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/656989" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f9652347.mp4?token=R7JuQPf56coP1gHBasbadRrhN2xcUpeT2HsUTtVjgJ11yTO6HsjikfW04B1R7Rzrp1tn9gI5EQXra8YJrYa4CAZKlLdj0uFQZGlBcyFfl3SKNRwKCjSqfTZ5f1AMdGohevkmXPtjNK118d2B5kKS0s2w77IznHfIjrhLCIJNbIYgW3nn0qbvsNAlGFZoCnwDsY-tLqbH25CjCEtnPm-flISaHJ7S8NSUCjv63stFDyETtfkFH_oCx6H1uIshMsuXzWxPvveiLci4tlbA-ybn-2d8fCSDpi-yAlaRMXKRNTZwTvhaGHIP9G8jKoKHsNRQnY2isoDmdNWBgZDWNOUCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f9652347.mp4?token=R7JuQPf56coP1gHBasbadRrhN2xcUpeT2HsUTtVjgJ11yTO6HsjikfW04B1R7Rzrp1tn9gI5EQXra8YJrYa4CAZKlLdj0uFQZGlBcyFfl3SKNRwKCjSqfTZ5f1AMdGohevkmXPtjNK118d2B5kKS0s2w77IznHfIjrhLCIJNbIYgW3nn0qbvsNAlGFZoCnwDsY-tLqbH25CjCEtnPm-flISaHJ7S8NSUCjv63stFDyETtfkFH_oCx6H1uIshMsuXzWxPvveiLci4tlbA-ybn-2d8fCSDpi-yAlaRMXKRNTZwTvhaGHIP9G8jKoKHsNRQnY2isoDmdNWBgZDWNOUCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در فلسطین اشغالی
وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
🔹
سست نشوید و اندوهگین نباشید؛ شما برترید اگر ایمان داشته باشید.
🔹
سوره آل عمران، آیه ۱۳۹
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/656988" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک منبع ایرانی به رویترز: اگر اسرائیل به حملات موشکی ایران پاسخ دهد، ما نیز قطعاً پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/656987" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: ارتش (تروریستی) آمریکا در حالت آماده باش است #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/656986" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سخنگوی سازمان هواپیمایی كشوری از بسته شدن بخش غربی فضای پروازی کشور تا اطلاع ثانوی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/656985" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عملیات روانی آشفته سگ‌زرد: می‌خواستم بگویم که توافق با ایران روز دوشنبه امضا می‌شود. شاید سه‌شنبه. شاید هم چهارشنبه... #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/656984" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عملیات روانی ترامپ: ایران به میز مذاکره برگردد و توافق امضا کند؛ به دستیابی یک توافق نزدیک شده‌ایم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/656983" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
یک منبع ایرانی به رویترز: اگر اسرائیل به حملات موشکی ایران پاسخ دهد، ما نیز قطعاً پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/656982" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بعد از قطر آسمان عراق  هم بسته شد
🔹
الفرات نیوز نوشت که در پی حملات ایران به اسرائیل، آسمان عراق بسته شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/656980" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
زیاده گویی ترامپ به فاکس‌نیوز: به ایران می‌گویم شما موشک‌هایی شلیک کردید؛ کافی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/656979" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای اسرائیل: ایران ۱۰ موشک بالستیک به سمت ما شلیک کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/656978" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
زیاده گویی
ترامپ به فاکس‌نیوز: به ایران می‌گویم شما موشک‌هایی شلیک کردید؛ کافی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/656977" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193dcdf4cc.mp4?token=XsUcSH6xpqeE37soK-eWMzSVawvqjC1iPjM7LSKKkD2lB0D4lipDsns6wJ4sRScN_v9nkZb1sl6EAywTCUV1ljSy3q6tf-jT4B2TA6YZjB93OL4RDlnik0wrrkNe2GI9BifTn2LDN9GMqBNE7zlp3xaQpar9uCabBqkEGC5CCT58V3yhtoQjKoi-Vub6Q9nR2uijbGMw-CvzFbrvZZUykwUhiUCjD-AyqCvOEVaEYYTfM_4NT_X8uqm5a7Mw_osn_w5Hg07V55ESkXGnFZ7jYDu59s0QUlDHnNL29zgtyNEsmD1Nm2zCW8w-mKUZ7WDP4V8jdpY7LPInPE_Kb5zb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193dcdf4cc.mp4?token=XsUcSH6xpqeE37soK-eWMzSVawvqjC1iPjM7LSKKkD2lB0D4lipDsns6wJ4sRScN_v9nkZb1sl6EAywTCUV1ljSy3q6tf-jT4B2TA6YZjB93OL4RDlnik0wrrkNe2GI9BifTn2LDN9GMqBNE7zlp3xaQpar9uCabBqkEGC5CCT58V3yhtoQjKoi-Vub6Q9nR2uijbGMw-CvzFbrvZZUykwUhiUCjD-AyqCvOEVaEYYTfM_4NT_X8uqm5a7Mw_osn_w5Hg07V55ESkXGnFZ7jYDu59s0QUlDHnNL29zgtyNEsmD1Nm2zCW8w-mKUZ7WDP4V8jdpY7LPInPE_Kb5zb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان انقلاب تهران امشب در لحظه اعلام خبر حمله موشکی ایران
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/656976" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هشدار مقاومت اسلامی عراق به آمریکا: هرگونه مداخله، پایگاه‌های شما را به آتش می‌کشد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/656975" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83835975f0.mp4?token=lv6xE_thcfOVuohMH4CcWdSjNCVSa-9y5vHzBDF1Kke6uCRjWtmHXiXTa71BCA8vfIbZu3yWoE059ndz7Qdakgh-1eVwvE7nZyYG3XAArAX_rub-xis0oUAXq83I49fmwSDViZT7U9ABm-S8OnYPM5de65EfYUo5rIHQLoGWYOJIkEiMTOkqJFp47CoObOpJue1tbiKCKHtzIPdo_AZbe7_uUK7CvB9oa35lWL5NNXf7CWkhho4W3_VxIvqofpZwD0guVzODvfy0VSOx1ySVnmAwjSlPX9OmtKtGbQsOHAEse8HoBkLmv2k_XGAh-cc2CBnmR3Du5zbSUR1sXV5klJ3gSV0_78d3mUx-Vxh8T67bQpdbNnhmKrQzhMQ2hyewWVD-7qGe_NR5uXfgkCl7J9Jsd7PnuxYiU4E9aWgTChJVIiLv-1bGFNFgVHiPPEgHYtU8K8BDX1CmlSMHTgW1tJYmWtz7BLqe2epzX1OV47HOFfSWzP38TKie9xhhkOrNlTuUwanjdkpQ45bnXgabjvXoaOTAnzNa5qD4fiuO_mO19l7sjWZznMxq2MNzZ2PWRSQG-hE_nqGKKtUo2QTvU3VJPVoXWyRUQVIliXNr47PfxNYASwhs4WYhl1TZ9un3VkbfhAZMKsdP87WWIcGxyal008Fd_xZf7jUTgcwdMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83835975f0.mp4?token=lv6xE_thcfOVuohMH4CcWdSjNCVSa-9y5vHzBDF1Kke6uCRjWtmHXiXTa71BCA8vfIbZu3yWoE059ndz7Qdakgh-1eVwvE7nZyYG3XAArAX_rub-xis0oUAXq83I49fmwSDViZT7U9ABm-S8OnYPM5de65EfYUo5rIHQLoGWYOJIkEiMTOkqJFp47CoObOpJue1tbiKCKHtzIPdo_AZbe7_uUK7CvB9oa35lWL5NNXf7CWkhho4W3_VxIvqofpZwD0guVzODvfy0VSOx1ySVnmAwjSlPX9OmtKtGbQsOHAEse8HoBkLmv2k_XGAh-cc2CBnmR3Du5zbSUR1sXV5klJ3gSV0_78d3mUx-Vxh8T67bQpdbNnhmKrQzhMQ2hyewWVD-7qGe_NR5uXfgkCl7J9Jsd7PnuxYiU4E9aWgTChJVIiLv-1bGFNFgVHiPPEgHYtU8K8BDX1CmlSMHTgW1tJYmWtz7BLqe2epzX1OV47HOFfSWzP38TKie9xhhkOrNlTuUwanjdkpQ45bnXgabjvXoaOTAnzNa5qD4fiuO_mO19l7sjWZznMxq2MNzZ2PWRSQG-hE_nqGKKtUo2QTvU3VJPVoXWyRUQVIliXNr47PfxNYASwhs4WYhl1TZ9un3VkbfhAZMKsdP87WWIcGxyal008Fd_xZf7jUTgcwdMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ساعت به وقت خیبر است
پرچم‌به دست حیدر است
این باور یک کشور است
ایمان ما حب الوطن
ایرانِ ما ایرانِ من
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/656974" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ ها گسترده تر خواهد بود و تمام اهداف امریکایی-صهیونیستی را در منطقه در بر خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/656973" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پاسخ دادن حق ماست
حقیقت‌پور، نماینده ادوار گذشته مجلس و فعال سیاسی در
#گفتگو
با خبرفوری:
🔹
شرط مذاکرات ایران با امریکا برقراری آتش‌بس در لبنان بوده، اتفاقاتی که ضاحیه رخ داد نقض آتش‌بس است.
🔹
برای این که اوضاع بدتر شود و مذاکرات صورت نگیرد.
🔹
عمدا اسرائیلی‌ها این حملات را شدت می‌دهند و ما هم برپایه تعهدات اخلاقی که به لبنان داریم نمی‌توانیم بی‌تفاوت باشیم.
🔹
شاید لازم باشد از ظرفیت‌هایی مثل یمن بیشتر استفاده کنیم و از آ‌ن‌ها بخواهیم پاسخ بدهند.
🔹
پاسخ دادن حق ما است چرا که آن‌ها آتش‌بس را رد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/656972" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909daa1c5a.mp4?token=DrfTTsS0q2oChdwN9o4s8x2wVtYpqJ7TtjuErZ2DVBtYVmdq6wMG8SqayS1TYr3BmcalrazCb9aBlohvUs0JmZRT4DLgzezlqlVMIVde9rgXRsAce4gJjNcZD6XMmLUxoVcYQ_ZZdVFnnDmkAOZ4Bn70gk3fOir8FSkJj35TKehT1NDNwxKC96mTl9EpwigrisY-aT5jbaJRBH2629iXMIsgq5B6l3TU7VMVKwHvw__3OlNe1JFOLKkB3Kb3o1stmbzDMa_dLNXla1xTK1bsTasCzT612NRYghsEbXRvUQ6gFnlOJ86fY5g9IDxYHB_CfZczOYiF7qiGePflKrGlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909daa1c5a.mp4?token=DrfTTsS0q2oChdwN9o4s8x2wVtYpqJ7TtjuErZ2DVBtYVmdq6wMG8SqayS1TYr3BmcalrazCb9aBlohvUs0JmZRT4DLgzezlqlVMIVde9rgXRsAce4gJjNcZD6XMmLUxoVcYQ_ZZdVFnnDmkAOZ4Bn70gk3fOir8FSkJj35TKehT1NDNwxKC96mTl9EpwigrisY-aT5jbaJRBH2629iXMIsgq5B6l3TU7VMVKwHvw__3OlNe1JFOLKkB3Kb3o1stmbzDMa_dLNXla1xTK1bsTasCzT612NRYghsEbXRvUQ6gFnlOJ86fY5g9IDxYHB_CfZczOYiF7qiGePflKrGlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی در حال شلیک موشک‌های رهگیر کم‌تعداد خود برای هدف قرار دادن موشک‌های ایرانی است
وَأَعِدُّوا لَهُم مَّا اسْتَطَعْتُم مِّن قُوَّةٍ
🔹
در برابر دشمنان هر چه در توان دارید از نیرو و قدرت آماده کنید.
🔹
سوره انفال آیه ۶۰
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/656971" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سپاه پاسداران اعلام کرد: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/656970" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ ها گسترده تر خواهد بود و تمام اهداف امریکایی-صهیونیستی را در منطقه در بر خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/656969" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
روشن شدن آژیرها در ۲۴۲ نقطه از شمال سرزمین‌های اشغالی
🔹
طبق برآوردهای جمعیتی، به دنبال سومین موج موشکی ایران، ۱ میلیون و ۵۲۶ هزار اشغالگر باید به پناهگاه بروند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/656968" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">فتح می‌خوانیم برای پیروزی جبهه‌ مقاومت و برای یاری سربازان امام زمان (عج)
▫️
رهبر انقلاب اسلامی در پاسخ به سوالی، قرائت سوره فتح، دعای ۱۴ صحیفه سجادیه و دعای توسل را برای پیروزی جبهه مقاومت توصیه کردند.
⬅️
صوت توصیه های رهبری</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/656967" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zu5yUIFSW7GMyfi5I3TcAEeBUpARWRgGu2GugHW6A1JDwID_qfgNZqjJZsU8JT6dr3rWiu14KFpJW32V0zJ0UwUBmhXqjKn95XnWd2eU-J0m_s7HN-z7DujglW7VHu3RGsz0m4tD3JO0Gx2franJ-_ijwAd2BBwKzHcwvRlVQHVp0pHoB3pJukEfqqusGAAu1l9LI2PdhK04eIqOHz1f3ZSqpFQ-4CBhKC3_bAno3_hvA-8VuTxkB92g_qQ-pTa6X6JKkqvauvA31pHrin19qc4-ttFWZPxkke5D8MY2UMYB_vpXlTevVgGzlrKLbQoZ1duggpweIwjmeNtUNRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله خامنه‌ای به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
❤️
رهبر انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کردند.
🖥
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/656966" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlIe72awErrBDqiKrF4eNJIl0LDPTr6ZkdsZXUYYXRGPt5Tm0Tm8BwIsybO_cltFrqkbh3jOmeUvdomRDXpUCpPfff6h361zrZXlKef2xCUE2HxPOX6Ey0ht-bBsEVue2A332o8p1pgrXNNKPqzAZH0uD98u1LzVjB-sqZzHQaJQmrAdD-dVFs3wPECN2mck83z5UC_Cw8rO2LgOF0O3RZCwvomplcu3p2LptstToSnSMRoPFLsCb_QAslZMCZB6MRqoGC7wkyHYpUbbq_20GvJS-thgRS1mL0tmxEunLtjhRC0fygWZBpMhxsz7y8ESLwlKQeCuQVtw8XLfPSJJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روشن شدن آژیرها در ۲۴۲ نقطه از شمال سرزمین‌های اشغالی
🔹
طبق برآوردهای جمعیتی، به دنبال سومین موج موشکی ایران، ۱ میلیون و ۵۲۶ هزار اشغالگر باید به پناهگاه بروند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/656965" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم صهیونیستی: صرف نظر از نتیجه، ایران ثابت کرده است که پس از بمباران بیروت توسط اسرائیل، تهدیدات خود را عملی می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/656964" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3oEaGAklRc76AHJMNYW8YIL0oGK9Y1ftZzR_CCRLvBn3rv6btKHa8AUMtFHcw4dxRzKNEcZRF2qy9ODZSUEi_oKsoWKMiV28M3cDoBYyAd5h77CyVgNtzW7X0foXj-f8mPBnacW0mpkYF9Mg5Mi9ncmqxL5QYWvRNliJ1U9e5vb9H_XU3PaLZ4zJfRFynDPbY9dwv7CsCOYDbetysSoltwnoZDM5186N1byYLHQOifCsjq2XT4NdwCYFszmFSpQV9s8THM4T6IK9CKIvFYFI0AvqM0OUUYbf_98P5ISBKWHUZqOAjnx4uMfDyvkvIbsPHl8fhrM4UKCfaRuE6Q_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزیزی: دشمن فقط زبان زور میفهمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/656963" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

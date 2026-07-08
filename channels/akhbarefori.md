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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-668463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه‌های هرمزگان تا اطلاع ثانوی تعطیل شد
🔹
مترو و اتوبوس در مشهد رایگان شد/ ممنوعیت عبور خودروهای شخصی در خیابان امام رضا (ع)
🔹
بانک‌های عامل فروش ارز اربعین معرفی شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/668463" target="_blank">📅 15:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حمله پهپادی به نفتکش امریکایی در دریای سیاه
🔹
دو منبع فعال در بخش نفت اعلام کردند نفتکش «یاسا پولاریس» که شرکت امریکایی شورون برای انتقال نفت از آن استفاده می‌کند، امروز چهارشنبه نزدیک سواحل روسیه در دریای سیاه هدف حمله پهپادی قرار گرفت./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/668462" target="_blank">📅 15:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awSkiV7ejLPB4rYItFxJqo55y5K7tWwu6U6gGlZTg_R5UwLJVHJHAYJDaZbATEsQ1zdvd2CrjTLwP07vbRAWWlVQHjZw1bEXY8-aLXM2qtjDs7oyRbN6BWIUh7MUNYNh8uaFUWZ8nu7WMkXUEZqmjBo1cWrEBfnM-U6IjR3Bygwk-Qh9ow2lKnTCjbgtpwNvTEvv7Mu2umO4YqluXXMvImtiQf4nLaPnPTlPoXHpXyx_3mjcIoyWs3-w93dsYGs790vRdPtEU8luekiBhy2sZVBE4CUGXKXvdMzGXc0aGVYhL41WpQqmDN8_izMAv-OsnewH_HVJG3yEsfb_Cg2-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترافیک دریایی کریدور عمان در تنگه هرمز به صفر رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/668460" target="_blank">📅 15:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1999fdd529.mp4?token=Rh6-JilyrY3KgN2UhBNxTOc2GIveMSGeiweI9U-zXkaQEKie6xv-5seVqGtETwabWgnodkejJKh3KxSee6dlFhSnC8H58ZdMbHgRzr_4-wvDWPIybP0ZBulTqp3-749ocJmmcfqI73BUKKVvdWyosCThCz3mPWCVYhEB42Cgpt_6B1HiRDQlYhNDOoiwsE8qnMzEhviJoBUgyb2Bhlkh6a0zQfgXYgCm7IYUBng_h-83qLPAIEDukd8oF0cAcb0JPOS8OP_j_VlRfqxARtFy8puL6Ksay1CEgogSZseCTlecE_klZ4QPwaj90-iEm2Lf5L_8eN23WgAkeN66CcbAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1999fdd529.mp4?token=Rh6-JilyrY3KgN2UhBNxTOc2GIveMSGeiweI9U-zXkaQEKie6xv-5seVqGtETwabWgnodkejJKh3KxSee6dlFhSnC8H58ZdMbHgRzr_4-wvDWPIybP0ZBulTqp3-749ocJmmcfqI73BUKKVvdWyosCThCz3mPWCVYhEB42Cgpt_6B1HiRDQlYhNDOoiwsE8qnMzEhviJoBUgyb2Bhlkh6a0zQfgXYgCm7IYUBng_h-83qLPAIEDukd8oF0cAcb0JPOS8OP_j_VlRfqxARtFy8puL6Ksay1CEgogSZseCTlecE_klZ4QPwaj90-iEm2Lf5L_8eN23WgAkeN66CcbAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر دیده‌نشده از حسینیهٔ امام خمینی در بیت رهبری پس‌از حملات ناجوانمردانه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668459" target="_blank">📅 15:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بازدید مدیرکل دادگستری استان خراسان رضوی، معاون محیط زیست و خدمات شهری شهرداری مشهد و مدیران دستگاه‌های اجرایی از روند آماده‌سازی مسیر تشییع پیکر رهبر شهید در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668458" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تکذیب شایعه انفجار مهیب در شهرستان روانسر
🔹
فرماندار روانسر با تکذیب شایعه منتشر شده درباره وقوع انفجار مهیب در این شهرستان، اعلام کرد این خبر صحت نداشته و هیچ‌گونه حادثه‌ای در این خصوص در روانسر رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668457" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه المیادین از حمله پهپادی رژیم صهیویستی به ارتفاعات علی الطاهر در جنوب لبنان خبر داد.
🔹
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم مجاز شد
🔹
سید علی خمینی، سخنران مجلس ختم رهبر شهید در قم می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668456" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پاسخ اولیه سپاه به تجاوزگری‌های آمریکا؛ ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در منطقه هدف قرار گرفت
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
مبداء هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز به حاکمیت و سرزمین ایرانِ اسلامی، هدف مشروع نیروهای مسلح خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/668455" target="_blank">📅 15:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z437mOJC8YYuhK8LjA5JSaTD8xSggURq6uh2oAvGBTRU0duVfFsfIuwISDEneCBaQsgrbzTzMKsrEh1W9kxhX49rhSvCaygwIRnp2wTt-yeK9Qdh_j8zRGRz8SECrwc-vdPmh-AezN7qH8ERLHgfKpl-2Obx1ZOQU5PQuZzU54rureRM13-yE4UD-67Nz58cdaa61kU7ywKJrouoV1bi1ep-fLOpA0PYmDdxc6b4Of0VgRzoipb_ckQ9ui0QXrgIFPAJr7ZJZRCTc3n75stbvzrI2Bu_QHA56WCySvGL9z-t-3AdPLXUqTLUDhNhzvGeJ6vQMBjQklI0wS7dLbYbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ووزینیا محبوب‌ترین دروازه‌بان تاریخ اینستاگرام شد
🔹
ووزینیا، دروازه‌بان تیم ملی کیپ‌ورد، با عبور از ایکر کاسیاس به پرطرفدارترین دروازه‌بان تاریخ اینستاگرام از نظر تعداد دنبال‌کننده تبدیل شد. #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668454" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کارشناس نظامی لبنانی: نفت ۷۶ دلاری یک رؤیا برای ترامپ است؛ آمریکا همزمان فشار بر ایران را افزایش می‌دهد
روی، کارشناس نظامی لبنانی و پژوهشگر ژئوپلیتیک در
#گفتگو
با خبرفوری:
🔹
کاهش قیمت نفت و بهبود شرایط بازارهای جهانی، فرصت بیشتری برای آمریکا ایجاد کرده تا تمرکز خود را بر ایران افزایش دهد.
🔹
در شرایطی که نفت با قیمت‌های بالا فشار اقتصادی ایجاد می‌کند، قیمت پایین‌تر نفت می‌تواند به نفع راهبرد ترامپ باشد؛ در حالی که آمریکا و اروپا در حال ذخیره‌سازی انرژی و تقویت حضور نظامی خود در منطقه هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668453" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qferdQZm8-PwI_SjpZD0o_zhc-iZOuYfGcy3AbjkZ-NKS2imvAWmZ45jslFv-GNLETBD4YRE6y6QkeGTviRT7OCdJkrar0Tr39EmN98D43BkHrwkv-V_T8CjE0EPvaYv3kZm1QybGiM4Ng-Z_dVSnnoVg_fIwzLfRZYMVzOnXu-PGOktqglCG6nt3wfHTke-N26F8EEQAsO0vq3qMCkL7eakYdxdmsCjYPjw4hXGDxK4zLpi12WwCpB1zsrvvwGysvrDs7D8kJvuk2N8Kpyq0BfsJrAX4FmWsQPqPSnnHMWjB3r51d0Xe0HfMaWBHsep---QafEmkl40aTD2JRZnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سازمان راهداری وحمل‌ونقل جاده‌ای اعلام کرد: هموطنانی که برای زیارت و مراسم تشییع قائد شهید امت در مشهد مقدس حضور داشته و قصد بازگشت با اتوبوس دارند، بلیت برگشت را در اسرع وقت به صورت اینترنتی تهیه کنند.
‌
#باید_برخاست
#بدرقه_آقای_شهید_ایران
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
‌
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668452" target="_blank">📅 14:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4F-bPZWlAmV7EHchV8Ps1aS9FoEpQW5r2xjX1llgfwOZSiVPQWKf-Wj5qoBu4ngch8A1cMnraCKXEbjrnwWxjEdlEx7s76nJEaJ2t2-ELo4Ia2-9XFfb0P-fPq1Mavs4CdelmQ0Tri8wfV8AHWGQZ-5sdfJXLdSLGK1PVrFq6OuACBpSYhb51XQqu3AiAiQIhQJ3K8U9QGCgJT822kuudNNjc158q1t-JKRbeiJRp5r70M0QNW6RqUn-EfFhzA8TSEju1imyVxvH1Jd6eyTFGIyqnKV_0F6ZsGB0qFEIZGsn1VwWP76IVxGUHKzaSAOcvVjmj2bQrD-UbzulU55eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری هادی چوپان برای رهبر شهید یک روز پس از سفر به عراق
🔹
زیارتت قبول آ سید/ برگرد دلمون تنگه برات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668451" target="_blank">📅 14:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f601f8bec1.mp4?token=FRnKHcch3YpIrSc5ICMzPlReiOkx6LB-3oDkldlToWYcfXwLPt2-IbAIOzf4nfaOo3ulzUWY8m_mfjIg2MvLB2D4J9jA5tv4GxY4KrCzx67llltvPxgpCoLC5Q6MH_XxvPMUmI4dAlZgo3ZBDUZLmdTqHYUrojG9tunxdhyWkPnnhllZfmWmFv_4NQIs0h_AtGPj8SkputiFCaY5hSowdpyak_KsjbZhQ7Sn7G1ltF0jYbg2eWBaFsGJd8IXtTv1GAfvUO5l7HFNAM4JHaCgXPQnghdweQz8GALZ0fVkkFBWlFErPQ0rnXs5gBjrnEyj3K8VNkKrOY8qSBn7CHN6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f601f8bec1.mp4?token=FRnKHcch3YpIrSc5ICMzPlReiOkx6LB-3oDkldlToWYcfXwLPt2-IbAIOzf4nfaOo3ulzUWY8m_mfjIg2MvLB2D4J9jA5tv4GxY4KrCzx67llltvPxgpCoLC5Q6MH_XxvPMUmI4dAlZgo3ZBDUZLmdTqHYUrojG9tunxdhyWkPnnhllZfmWmFv_4NQIs0h_AtGPj8SkputiFCaY5hSowdpyak_KsjbZhQ7Sn7G1ltF0jYbg2eWBaFsGJd8IXtTv1GAfvUO5l7HFNAM4JHaCgXPQnghdweQz8GALZ0fVkkFBWlFErPQ0rnXs5gBjrnEyj3K8VNkKrOY8qSBn7CHN6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره رهبر شهید انقلاب از اوایل ازدواج
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668450" target="_blank">📅 14:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فارس: ایران باید پایان رسمی تفاهم را اعلام کند
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف، بندهای متعدد این تفاهم را نقض کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668449" target="_blank">📅 14:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آغاز مرحله چهارم سبد غذایی رایگان برای ۱۸۰۰۰۰ کودک از کودکان مبتلا به سوءتغذیه از فردا ۱۸ تیر
🔹
عمان و قطر خواستار گفت‌وگو در جهت کاهش تنش‌ منطقه‌ای شدند
🔹
پروازهای فرودگاه مهرآباد و امام (ره) به روال عادی بازگشت
🔹
سازمان دریایی بین‌المللی: ۶۰۰۰ دریانورد همچنان در تنگه هرمز به سر می‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668448" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT8pcvTlhGz78Simok7VMhufyeX8AOXpzAIjo99R5KXunVFDGVJiccNUwyLhexpmCKh0rXa79tJIoX9LFs_ItE7n5ckzVaTLcWCN3tT9oG9FtAq-unN7QKN-JhCXdN-FvAxjau1Qoh7fc39mHnr2NMTNWjsaWbHp5EH87Uc0FomFoxbqOFdAOV3sBpVvVWNee5oqMG4uR9agGq3phb2AhE01ECUSGZ68IjKSDaQaICGxaCtWf1OyB2QrAt8vpMXtVZvBbZVe8X1xeA8T4sXU84WK8xrUEBbizVzaF-Ju2r2xg3yzuF7eT3l6cibp9PFQ1iqQH5UXv6XJt5RNE9qo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۷ تیر ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
ادعای لغو مذاکرات خیلی زود در بازارها قیمت‌گذاری شد؛ دلار به کانال ۱۸۰ هزار تومان برگشت، طلا تا ۱۷.۸ میلیون تومان بالا رفت، بورس صف فروش شد و بیت‌کوین هم زیر ۶۲ هزار دلار عقب نشست./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668447" target="_blank">📅 14:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
جوکنت، مدیر سابق مرکز مبارزه با تروریسم دولت ترامپ: حالا که تفاهم‌نامه با ایران عملاً مرده، دوباره به تلاش جهت یافتن یک راه‌حل نظامی برای تنگه هرمز بازگشته‌ایم
🔹
مشکل این است که ما این تفاهم‌نامه را امضا کردیم، چون هیچ راه نظامی‌ای وجود نداشت. بهترین گزینه این است که به سادگی کنار بکشیم/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668446" target="_blank">📅 14:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید انقلاب: مراسم تشییع در کربلا از ساعت ۱۶ به وقت عراق آغاز خواهد شد
🔹
همچنین زنان عراقی برای بانوان شهید خانواده آقا، در شهر نجف مراسم ویژه‌ای برگزار خواهند کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668445" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668443">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMhMr1BPG2fPII5fxh-kLQYherqRnnmxWtF1YFItV4WxdmcK7zIser_x7WHa0gdKJhlcL6oohY9mRUc7EGrdO7BSomyDw2DkPV31SebxyIW4wnp6nopbTcUMpWyVk-_jeL1fjJub7_KYoPkAGeu-FyK-KuGP6TL-CSjJCkMeCC50sO8hqIgzp64cMIWxU1euwscNnpW109Xl22gtL9BKvJp7BMm3_cpfPNmmATZoXgBsyGeKZZZ4zQxz96Vz6429FKNFvOuTJKVkkr_M2Q_KUxoYNeWbxzsCyf6YSnH9XwWYthyQlDR03-ZCHEm4ejyODEfyhmme5GqW__2MZj1RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiZqMytjMFCM_es6w3G8rtUeEw-zATZZZKA07jGu53KsHEKMHacHqSo19bXsvM6xwHh2urQ323FaP--uyc427uXvwBlTZi5y0IfocMsJ3J2Ou40NwtDfMZjUfSnAhSq7t1zx2njTVEyOHBbI40Lx5XcaEpElZECh7rhJZg45n7pNcVVE9BOdK_8HeGruafm0ZfpGxlMcm1Am-XKYM6KRXMyIYknV0yg3_SeJpXZhrs8w35gWIfG9P1SZSbrILKhait_SVX1Wy_p3ZWLY5XMmhkl_rkykZY9qs_ZdysCv9SzBB2zBfS6Y5ngk47vKEULHVfFNn7LrdJXBYQopp4TvsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاظمین میزبان پیکرهای مطهر اعضای خانواده رهبر آزادی‌خواهان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668443" target="_blank">📅 14:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668442">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e7e33c2e.mp4?token=bzYEdvOKw2Tx2Ygrg314OOacWg_MMATI4tQXROVsCYkFwbpQro-Togh26oTGa-BVZ58EGlwfdiXYUqaQevdSHC64ricNL4qi5R5bDycbnJp7KLQ9L0HoFd4ZnKI86lsothHNYi8msBnG7-e4fSNPl1tH4_u_b2AH0cH2BwQ0z6ipdLfzUSzSpsvUqn-LIlFp8OLN__QqG8UB-gb7TmCrKEmIMHiwr_-OqPH3QgarA78FyY8KeHeDYptb_LSM_3lNBguzPWIVvdmHTMNOvzjp7bfUX-SGpg8OsYyvb0NLNGg4aESBP_qfWNBhGvjCrkouj7PE3jjJqzLLAERs08EkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e7e33c2e.mp4?token=bzYEdvOKw2Tx2Ygrg314OOacWg_MMATI4tQXROVsCYkFwbpQro-Togh26oTGa-BVZ58EGlwfdiXYUqaQevdSHC64ricNL4qi5R5bDycbnJp7KLQ9L0HoFd4ZnKI86lsothHNYi8msBnG7-e4fSNPl1tH4_u_b2AH0cH2BwQ0z6ipdLfzUSzSpsvUqn-LIlFp8OLN__QqG8UB-gb7TmCrKEmIMHiwr_-OqPH3QgarA78FyY8KeHeDYptb_LSM_3lNBguzPWIVvdmHTMNOvzjp7bfUX-SGpg8OsYyvb0NLNGg4aESBP_qfWNBhGvjCrkouj7PE3jjJqzLLAERs08EkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه پاسداران در پاسخ به تجاوز و عهدشکنی ارتش تروریستی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668442" target="_blank">📅 14:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668441">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سازمان دریایی بین‌المللی: ۶هزار دریانورد همچنان در تنگه هرمز به سر می‌برند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668441" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جزئیات حمله به بندر سیریک
مدیر بنادر و دریانوردی شرق هرمزگان:
🔹
بامداد گذشته دو اصابت از سوی دشمن آمریکایی - صهیونیستی در ساعت‌های ۰۰:۳۵ و ۰۱:۳۵ بامداد به بندر سیریک، واقع در شرق استان هرمزگان صورت گرفت.
🔹
بر اثر این حملات، یکی از اسکله‌های شناور بندر سیریک دچار آسیب جدی شده است. خوشبختانه این حادثه خسارت جانی (فوتی) در پی نداشته است.
🔹
با این حال بر اثر این حملات یک نفر مصدوم و برای دریافت خدمات درمانی به مراکز درمانی منتقل شد و سه نفر دیگر نیز به‌صورت سرپایی تحت درمان قرار گرفتند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668440" target="_blank">📅 14:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پیکر مطهر رهبر رهبر آزادی‌خواهان جهان پس از اقامه نماز، بر دستان خیل عظیم عزاداران در حرم مطهر امیرالمومنین علیه‌السلام تشییع شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668438" target="_blank">📅 14:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad4b418f2.mp4?token=fKoy2kn6A8t1hKlRXH9gj__7zNscc66ZQToii9xo6N1tMnz30AG4pTkeKD5aUqQdAzOXPulqKAttjfvAh2fpvmrIoQZAFurSN2HeZij6jLke4Yb6hdB2J2g5K2HwNAWIyqOLEICkZoTcZLdAyubSsGJGfGHUTB-9tRZ9RP9h34VjXOpCeIlRaSLY4AdENQtlQfsgZglorfMF4Y-WKmfRE75sPNRB9gX1af1eJc2wwoAk_gz_SwLKvNf5FJX0j5yVsH3A2FhgBdKdVHaNoJJiXq0VMXvrEUhA2tXYYGiidVutHIk3RAHxAiARehPsAvyvBGg6xsValzCDEtYClCDXmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad4b418f2.mp4?token=fKoy2kn6A8t1hKlRXH9gj__7zNscc66ZQToii9xo6N1tMnz30AG4pTkeKD5aUqQdAzOXPulqKAttjfvAh2fpvmrIoQZAFurSN2HeZij6jLke4Yb6hdB2J2g5K2HwNAWIyqOLEICkZoTcZLdAyubSsGJGfGHUTB-9tRZ9RP9h34VjXOpCeIlRaSLY4AdENQtlQfsgZglorfMF4Y-WKmfRE75sPNRB9gX1af1eJc2wwoAk_gz_SwLKvNf5FJX0j5yVsH3A2FhgBdKdVHaNoJJiXq0VMXvrEUhA2tXYYGiidVutHIk3RAHxAiARehPsAvyvBGg6xsValzCDEtYClCDXmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین در انتظار استقبال از پیکر مطهر رهبر آزادی‌خواهان جهان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668437" target="_blank">📅 14:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf19da4a75.mp4?token=qJETX9lXDGyElRxTmpWIawiDhfKv3HrDmycY8AKd_PsJ8nqLyRdGUpXDeMwupSPPo3I9D_qB6Q1MG04id1yagne2uFnbedNbWw9r5Oo68I1e67juF0wtSJI4WXt9IrcoYOPZUyDfkMeA0fMvIHVNiZreo8OgkkoRHVS3JhuQhJVW0sGCVJH5kplI_4szaJ0aY1ryz749yZPk-cd1NhF2VHo__-Vpj8_P3Lva5Sp4BMe8diUwUC9wGfan7slOinCP5aCXTTQ7buUBb22EkRkzFh4Ih83L8ywf6PrKY1U4fwY1qToglBD6AdmoLAe9SivamvRPV2byC79d7EBbApiFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf19da4a75.mp4?token=qJETX9lXDGyElRxTmpWIawiDhfKv3HrDmycY8AKd_PsJ8nqLyRdGUpXDeMwupSPPo3I9D_qB6Q1MG04id1yagne2uFnbedNbWw9r5Oo68I1e67juF0wtSJI4WXt9IrcoYOPZUyDfkMeA0fMvIHVNiZreo8OgkkoRHVS3JhuQhJVW0sGCVJH5kplI_4szaJ0aY1ryz749yZPk-cd1NhF2VHo__-Vpj8_P3Lva5Sp4BMe8diUwUC9wGfan7slOinCP5aCXTTQ7buUBb22EkRkzFh4Ih83L8ywf6PrKY1U4fwY1qToglBD6AdmoLAe9SivamvRPV2byC79d7EBbApiFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر هوایی صحن حرم امیرالمؤمنین (ع) در روز تشییع؛ وسعتی که با حضور بی‌سابقه مردم پر شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668436" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ام از فصل چهارم
🔹
در این قسمت بخشی از تجربه‌ نزدیک به مرگ خانم خدیجه مبینی که در هنگام خواندن نماز به خاطر سابقه بیماری قلبی به ناگاه روح از جسم جدا شده و موجود سیاهی را در میان اعضای خانواده که خوابیده بوده‌اند تردد می‌کند را می‌بیند و برای خلاصی از شر آن موجود بانویی سفیدپوش قرائت سوره انشراح را به ایشان توصیه می‌کند و بعد از آن شهیدی که به خاطر شیطنت‌ها و حق‌الناس‌های دوره نوجوانی‌اش در عالم برزخ گرفتار شده است را درک می‌کند؛ نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: خدیجه مبینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668434" target="_blank">📅 14:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزیر مشاور در امور خارجه بلژیک در گفتگو با شبکه الجزیره: اقدامات ناتو درباره تنگه هرمز بر اساس یک موضع دفاعی انجام می‌شود و این ائتلاف در جنگ مشارکت نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668433" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6077988b.mp4?token=tkLVDp4mU_cnAKCqr4yoXxtrd6wTVnIf6DyQVqC8i29b4ROgJ836CcFDNStaE9jz4-MSelLAK-gGUTDlWd54kUOeCFIr68hfYvFy80srfamgrbV1miTkZc2ww59IC0u3ttoiRldt6FYkaQt4kHWtRSXyj_pY7oUL3FDNQCixTG7lwupNyzidXABmwsQCpHWQrvTcQYCya4lMV3Z2VH8-WwYMjGDLUX2RPZ-U_sTv3blsFHZTSibCIaXcZYfXgnqbHqEYLL9-gXn6VLcOzM-rYOYqDGHUZ3gTXyD1PNwT-3zgWLZ56yQ0khsY_JgUwpjuCd8ytWQU6RSifHPPIcU_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6077988b.mp4?token=tkLVDp4mU_cnAKCqr4yoXxtrd6wTVnIf6DyQVqC8i29b4ROgJ836CcFDNStaE9jz4-MSelLAK-gGUTDlWd54kUOeCFIr68hfYvFy80srfamgrbV1miTkZc2ww59IC0u3ttoiRldt6FYkaQt4kHWtRSXyj_pY7oUL3FDNQCixTG7lwupNyzidXABmwsQCpHWQrvTcQYCya4lMV3Z2VH8-WwYMjGDLUX2RPZ-U_sTv3blsFHZTSibCIaXcZYfXgnqbHqEYLL9-gXn6VLcOzM-rYOYqDGHUZ3gTXyD1PNwT-3zgWLZ56yQ0khsY_JgUwpjuCd8ytWQU6RSifHPPIcU_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی‌ای که نگرفت؛ ترامپ، دبیرکل ناتو را نادیده گرفت
🔹
دبیرکل ناتو با اشاره به کتونی سفید نخست‌وزیر آلبانی سعی کرد توجه ترامپ را جلب کند، اما رئیس‌جمهور آمریکا بدون همراهی با این شوخی، واکنشی نشان نداد؛ صحنه‌ای که خیلی زود در فضای مجازی دست‌به‌دست شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668432" target="_blank">📅 14:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شهرداری مشهد.pdf</div>
  <div class="tg-doc-extra">29 MB</div>
</div>
<a href="https://t.me/akhbarefori/668431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖼
بروشور اطلاع رسانی تمهیدات شهرداری مشهد مقدس در مراسم بدرقه آقای شهید ایران
⭕️
مردم شریف ایران اسلامی
برای اطلاع از خدمات مراسم بدرقه آقای شهید ایران در مشهد مقدس ؛ می توانید از لینک های زیر و یا اسکن رمزینه های فوق اقدام کنید.
🔻
بازوی بله
⬇️
https://ble.ir/MashhadTrafficBot
🔻
سامانه
#باید_برخاست
⬇️
https://bayadbarkhast.ir
🔻
کانال اطلاع رسانی مردم نگار
⬇️
https://eitaa.com/mardomnegar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668431" target="_blank">📅 13:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NehZ7Lii4VVTLsqT6MxGfSCCKazouclVwoX2kY0_99ajN5_xigqu47VnYxn8BfP-nIwlYsRtfg_PV5otbdABlExYIX1gXTfHcQf68sq7qbfJczvA1i6OQX_xO6JF6dMERyBSSXJPqBStYgmrtB02meR0lPMcTWHIWlBujV8PKCBWOdFGoinc0qNRNd0-q6h7IU9DdafLanAPhyRbymFCZAheg8ScHJtg_cyvmrhbdIg2a5O3oGfw7eijB58qyh2M0d4lElgqmTaFRsQVXT7Fh9bXPkGAC7cOV_wSeRhtdaQUAA-DidwMQSo8-neVE0mDL4fbjzPQ-0Vyy-qWUBE6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: در برابر کسی که به امضای خود و عهدی که می‌بندد هیچ پایبندی ندارد، تکلیف چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668430" target="_blank">📅 13:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تشییع پیکر مطهر رهبر شهید انقلاب اسلامی به سمت ضریح مبارک امیرالمومنین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668429" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef70429963.mp4?token=PJqTr95A_eRxefB68xaMQeN8zjwjQNO8N5IE4nLfYGY9UbnK_WtucMagDhwXdAqAjsshEVIcZr93J7n4_oY1db9C_uBo0Rug9lsM0Hkk5lfMv7rXxDh-ZH_6Gu_xbtASwL723MNd9OtONdLjvMQtFHvO8yoapvzuseMnmISGT9HZ7VHZvPCjlDxEdj76qG19X_v40_LOsLpYgd3Cxq6w5hV25wrxpy5E9tLiTmM2PAXYjfjeTRKiKlGQHI2vb9FyUTMfEQsLN4jR3T0MlAYOx-mNyn48jVizxekZuCxOUUTq7RhKGbAn99adL-xtjUSuis0kLGm5zGYkC3ClNEE6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef70429963.mp4?token=PJqTr95A_eRxefB68xaMQeN8zjwjQNO8N5IE4nLfYGY9UbnK_WtucMagDhwXdAqAjsshEVIcZr93J7n4_oY1db9C_uBo0Rug9lsM0Hkk5lfMv7rXxDh-ZH_6Gu_xbtASwL723MNd9OtONdLjvMQtFHvO8yoapvzuseMnmISGT9HZ7VHZvPCjlDxEdj76qG19X_v40_LOsLpYgd3Cxq6w5hV25wrxpy5E9tLiTmM2PAXYjfjeTRKiKlGQHI2vb9FyUTMfEQsLN4jR3T0MlAYOx-mNyn48jVizxekZuCxOUUTq7RhKGbAn99adL-xtjUSuis0kLGm5zGYkC3ClNEE6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید مقتدی الصدر، رهبر جریان صدر عراق، در مراسم باشکوه تشییع پیکر مطهر رهبر شهید #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668428" target="_blank">📅 13:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=Vd0NoUjgOZIIC_2rgp96ch8syFW8QSPssRu5jucGVrkLMIuKCvrOKCtN80nukZO2w67zy3nU4rIxqdCq5pULYn2Ygt8_qHI3uROb-MIWODxCvIg4Cj74sVygYfVP2q2o7eHj_keD5CHa1kb4M4PwsD2-Hnh3bVQCM5kYy95dmoaKga-rU-sM757kMsfefYMnTX6gYVTM4WzoxXz71O9k8hlkvm4PTVx5C0LAQ3Vnht4MRzpgXw5WXX3c4WgOsYvVxTLwwf-BHlVG8FgarV4HA7XZ79sAzkTm2e5isUk6clA8KItHvdHGJKAEW0e1VX3Uk-x_a__ZHbjIIgfQ0t2Xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=Vd0NoUjgOZIIC_2rgp96ch8syFW8QSPssRu5jucGVrkLMIuKCvrOKCtN80nukZO2w67zy3nU4rIxqdCq5pULYn2Ygt8_qHI3uROb-MIWODxCvIg4Cj74sVygYfVP2q2o7eHj_keD5CHa1kb4M4PwsD2-Hnh3bVQCM5kYy95dmoaKga-rU-sM757kMsfefYMnTX6gYVTM4WzoxXz71O9k8hlkvm4PTVx5C0LAQ3Vnht4MRzpgXw5WXX3c4WgOsYvVxTLwwf-BHlVG8FgarV4HA7XZ79sAzkTm2e5isUk6clA8KItHvdHGJKAEW0e1VX3Uk-x_a__ZHbjIIgfQ0t2Xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اللهم انا لا نعلم منه الا خیرا
🔹
لحظاتی از نماز آیت‌الله حکیم بر پیکر رهبر مجاهد و شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668427" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oukPYtxomwuiO4s-f6HLmRWQRnRSndIr2K88WdDlye2ZTvV0LlovqIA5ky39LQjuXiDSN2JiMDZzRg9p_W-MgDa07lQSMe3xDmfcHFdxSp5r7jJk8BvG-U_qTP30IGYjB9gelC1fHJiwXb2FG67bh_08BDMabYQ6r4HkOhVpuYbSRloTX6vnDfwL1foC7sm5IVVXyKX-hpmc2d1nHb-BLzdfk68ZBLOrOPbD075cpywKTbrBRn-lWk2UQ0exYOpYdQ2-jq4ShbbQj33NDbWEJOp8ylAaN--KGsE_kXE0gvPzxl3BJsgpnvs4GPKmBQN-I38ofSeO5pn7KQM7hrqBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل نظامی سابق آمریکا: حملات به ایران فاقد استراتژی است
🔹
دنیل دیویس، نظامی سابق آمریکایی، حملات اخیر به ایران را بی‌نتیجه و فاقد استراتژی دانست؛ این اقدامات نه تنها ایران را تسلیم نمی‌کند، بلکه با واکنش شدیدتر مواجه خواهد شد و تنها تلاشی برای ارضای بی‌صبری ترامپ است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668426" target="_blank">📅 13:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae065e1633.mp4?token=BYYLrdlVe4i6MDtX9sZqi324opr2SEaR6gT7p0lyz15AUZm9Bq5yjq4b6wsb_sFtPp6u0jHYWr9dFeeh6o5j88ihKXR1h-zsL0ftF7V3sRJuRoAU2mOdYTxrLgeU1-YQ_wCGTyrR--_kEh8l6InENTD2u7pJiG7TTMFPpmt-z29Pk9yy0nwB-R67Rxzgc5MwFhogb6FT0M25komylYDKgDmWGGCLLcbTut0xjYyjCArWDHxbZIvcQz6e-pzoPK52PU57u3KX6Kvm2eRU8b273ztqRncYh9rqEWLDjlWOgT1ABT-Oz37aWiBzsrE1RSv-CE_NOkwwugn9C39k8soWu1KC841v2nnk55rRNdm0bjBJsSCH437xZuKCVUcEh9kTKQznrbL90hRZcCBwovy9CNfIUgJIbHqOxngOYp9NPhjZhC7MBQM0bJ3BceCkt7zNQL2ZuLvnt8HjFEEi_PIEBKC4FArcZZIN-sxI35x4ceG9tm-RIov5OZIZoElzxBDURFKeVHP6JtdJPH-gCyy34TseCh152L3V6w0UDVe2h8_CUOi90WDoS3oi5DYkDjffixW8NvMA05ruWkVKAGWW8m3QxYR9BK3n_66i3gpexTqKKJJUDE9LNNKkiL_jYt7Jm1eLQLTeFEJRoQWol5hn-6fh2VVc8IDRpFpGgAkECRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae065e1633.mp4?token=BYYLrdlVe4i6MDtX9sZqi324opr2SEaR6gT7p0lyz15AUZm9Bq5yjq4b6wsb_sFtPp6u0jHYWr9dFeeh6o5j88ihKXR1h-zsL0ftF7V3sRJuRoAU2mOdYTxrLgeU1-YQ_wCGTyrR--_kEh8l6InENTD2u7pJiG7TTMFPpmt-z29Pk9yy0nwB-R67Rxzgc5MwFhogb6FT0M25komylYDKgDmWGGCLLcbTut0xjYyjCArWDHxbZIvcQz6e-pzoPK52PU57u3KX6Kvm2eRU8b273ztqRncYh9rqEWLDjlWOgT1ABT-Oz37aWiBzsrE1RSv-CE_NOkwwugn9C39k8soWu1KC841v2nnk55rRNdm0bjBJsSCH437xZuKCVUcEh9kTKQznrbL90hRZcCBwovy9CNfIUgJIbHqOxngOYp9NPhjZhC7MBQM0bJ3BceCkt7zNQL2ZuLvnt8HjFEEi_PIEBKC4FArcZZIN-sxI35x4ceG9tm-RIov5OZIZoElzxBDURFKeVHP6JtdJPH-gCyy34TseCh152L3V6w0UDVe2h8_CUOi90WDoS3oi5DYkDjffixW8NvMA05ruWkVKAGWW8m3QxYR9BK3n_66i3gpexTqKKJJUDE9LNNKkiL_jYt7Jm1eLQLTeFEJRoQWol5hn-6fh2VVc8IDRpFpGgAkECRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر مطهر امام مجاهد شهید حضرت آیت‌الله العظمی سیّدعلی خامنه‌ای
توسط آیت‌الله حکیم در حرم مطهر امیرالمومنین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668425" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974c274e02.mp4?token=mhRHalapi4GuljRjDfVlKNspQ3upbkrcj46iazKXR0bPiXWB7jB2EFyXhfgbmiWbEgL9eYjflDcUhj1O9lv4cQReDycELSneik6dGDAW9JGJQT_dLnt5JdIoAj1ylnkQMTQoa6NM7H32cElxHwgg6yPgW3rqvVF_MSXNKHJ7y-VsPzvQyjYczcYeo8XIj6BlY3MW_fZhQPqDVsjU0zJ66b3zyPfrTrjR5dKbpxtVHWehHup589yvA-qLdZ_MBLHXdWbB-EzD9FJm1qAixIhe6KLbaImvAeV1cYoJW9exKNbaWO3VYFf6ci5HK7Qwsw-G4_1gRUkD4tnjSOldvg-wVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974c274e02.mp4?token=mhRHalapi4GuljRjDfVlKNspQ3upbkrcj46iazKXR0bPiXWB7jB2EFyXhfgbmiWbEgL9eYjflDcUhj1O9lv4cQReDycELSneik6dGDAW9JGJQT_dLnt5JdIoAj1ylnkQMTQoa6NM7H32cElxHwgg6yPgW3rqvVF_MSXNKHJ7y-VsPzvQyjYczcYeo8XIj6BlY3MW_fZhQPqDVsjU0zJ66b3zyPfrTrjR5dKbpxtVHWehHup589yvA-qLdZ_MBLHXdWbB-EzD9FJm1qAixIhe6KLbaImvAeV1cYoJW9exKNbaWO3VYFf6ci5HK7Qwsw-G4_1gRUkD4tnjSOldvg-wVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریادهای مرگ بر آمریکا و اسرائیل در حرم مطهر امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668424" target="_blank">📅 13:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668423">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4LZysGC0FIURRQPsd3j8sgqel2tWXXiLhmEBrqLc0fNDnzBqV5tZR6vca5A_7vBs-WYuX3tlXfzfBWogn7vgQGX5LkjP1PZsl9vKlfCX8uIOjb9i24WSE-ZrKUms9PTi8Bxl4afKsT7pCL04LWZhzZ4rxESkVxaKgQpQD9j0Eo8bqhFm1ytjdxb-gaBO0YUrquMBVK7ct5eCfVZ2Umr3-ChKJUUZoHmuyGyOFX4maiBqZiSaHtxygm9p0R3b0AatA5UejrRaMY3z-XpflIHTxXCiQTi_RtmZA2oW-rGx5rZ-xBevzGiPNArpfk1go66x_JGvJo9MCsG0zRxyPY9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: تشییع حماسی پیکر مطهر امام شهید در نجف کربلا، نماد درخشان برادری و اشتراکات عمیق فرهنگی و اعتقادی دو ملت ایران و عراق است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668423" target="_blank">📅 13:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔺
آمادگی کامل مدیریت شهری برای مراسم تشییع پیکر مطهر قائد شهید امت، حضرت آیت‌الله العظمی امام سید علی خامنه‌ای(ره)
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
بازوی بله
⬇️
https://ble.ir/MashhadTrafficBot
سامانه
#باید_برخاست
⬇️
https://bayadbarkhast.ir/
#مشهد_یک_شهر_یک_دل_یک_بدرقه
#آقای_شهید_ایران
#بدرقه_باشکوه
https://eitaa.com/mardomnegar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668421" target="_blank">📅 13:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITq52cJK4iy0W7YHSlB0lyFITFnpR7b_TZrk2wu94iAsKw_mcGLJLeoQuzzyZOmXaFTAlwrqr_pUW_RlEatUjlrL-y4Q2azDaikRr3RYfvIzKLTUzaSX8ajNkEDtgPt_NLS-X0JZrLMEk88wAV-3dvNpZzmCp-9XEmsekmeQT5zECAMLqFha6RecSLiKfMy1aSrESK2ZsSJlkI4cU3hGgUO9QAQ4w8etvn_sFKerRXUfgvmknN6z81aZdoSlAur2kpt8gjQ7NW7zGl0ck3nrxwKkmajg3x0MV0-1YW5RAT0p4R9Y6-S4r238GZ50Iut1pzf3MRM0fI975OA7ypP0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تقدیر مدیرعامل
#بیمه_البرز
از حضور پرشور و تلاش مخلصانه همکاران در آئین وداع و تشییع رهبر شهید انقلاب
آیین تشییع و وداع با پیکر مطهر رهبر شهید و فرزانه‌مان، حماسه‌ای بزرگ از جنس وفاداری و انسجام ملی بود. روزهایی ماندگار که با وجود اندوهی سنگین، عظمت و اقتدار ملت شریف ایران را بار دیگر به رخ جهانیان کشید.
مشروح پیام:
https://www.alborzinsurance.ir/PublicBlogDetail/5058</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668420" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کلاس‌های تابستانی دانشگاه آزاد مجازی شد
رئیس کمیته امور اجرایی آموزش و تحصیلات تکمیلی دانشگاه آزاد:
🔹
کلاس‌های نظری دوره تابستان سال تحصیلی ۱۴۰۵-۱۴۰۴ برای رشته‌های غیرپزشکی به صورت مجازی برگزار می‌شود، اما تمامی امتحانات حضوری برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668419" target="_blank">📅 13:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب به مقابل ایوان طلای حرم امیرالمؤمنین علیه‌السلام رسید و زیارت امین‌الله در حال قرائت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668418" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7301bfbdbf.mp4?token=lbG-Mn4W94LnGSnyQuJCLDhlbYGHfiJkJZpTi-fWu1ce8LSp128MIT4CYM-lEhDGzxEbAPvoIolBtS1oHA6uh9PpNmezSjNyGHgj1tBRenM_P-ngtK-1ZHOL3hJ87edqvPNpMV_vSp4sgxbQDCDwv4F_nsRQVwoFiLxTd_lLTqbgzLOlrmwouYHY9MnAlaRyupYUxZHZMgSpNdxmR6MRmmDYdrxOvU76Qer537PV_Yl8yAYND_Vr3iMNq8dz3tMav80oaTBRoifLSuIBi2DKH00V-7OFvZ8LUuJnfC_xyzKcs5bRz_-HVdSkF-AUN1DtERGiDk2_FJpAHZWaO4iefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7301bfbdbf.mp4?token=lbG-Mn4W94LnGSnyQuJCLDhlbYGHfiJkJZpTi-fWu1ce8LSp128MIT4CYM-lEhDGzxEbAPvoIolBtS1oHA6uh9PpNmezSjNyGHgj1tBRenM_P-ngtK-1ZHOL3hJ87edqvPNpMV_vSp4sgxbQDCDwv4F_nsRQVwoFiLxTd_lLTqbgzLOlrmwouYHY9MnAlaRyupYUxZHZMgSpNdxmR6MRmmDYdrxOvU76Qer537PV_Yl8yAYND_Vr3iMNq8dz3tMav80oaTBRoifLSuIBi2DKH00V-7OFvZ8LUuJnfC_xyzKcs5bRz_-HVdSkF-AUN1DtERGiDk2_FJpAHZWaO4iefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فراق یار؛ من نمی‌خواستم بره...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668417" target="_blank">📅 13:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668416" target="_blank">📅 13:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb122964b.mp4?token=X4oHtFhCKPehatXO0eRS6ONpZZQFJHKC1cDntg_x-NpMsnMPuiWWf5Y35TeZjWGsJq7dXbUlAAbWVa3uwL4GNeDdkrEaW97GI1WP9ah7pGaCcp3iqxl3gZxQ747ULgH8_a3XamXCaGx28gOSis0LKSRWITdgASkcc5YMJHW0v_dtIaUsCg2s5IYroP-9Amfiv5StJ4XB5k267iP233fbVUIEjLshfbV1DXu6ABRtCImWaH2Lc6yQhMKQ9tMEzY30ru6xFzGQLy6KsSlQtNKIbQ5z495JCwiFNoHwzPLld4bAalLSJWJZYx7ArcwCNQOiOVQvKrdKefPqoyXdzSlV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb122964b.mp4?token=X4oHtFhCKPehatXO0eRS6ONpZZQFJHKC1cDntg_x-NpMsnMPuiWWf5Y35TeZjWGsJq7dXbUlAAbWVa3uwL4GNeDdkrEaW97GI1WP9ah7pGaCcp3iqxl3gZxQ747ULgH8_a3XamXCaGx28gOSis0LKSRWITdgASkcc5YMJHW0v_dtIaUsCg2s5IYroP-9Amfiv5StJ4XB5k267iP233fbVUIEjLshfbV1DXu6ABRtCImWaH2Lc6yQhMKQ9tMEzY30ru6xFzGQLy6KsSlQtNKIbQ5z495JCwiFNoHwzPLld4bAalLSJWJZYx7ArcwCNQOiOVQvKrdKefPqoyXdzSlV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکر رهبر شهید انقلاب بر دستان عراقیان در حرم مطهر امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668414" target="_blank">📅 13:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تصویر هوایی از تشییع رهبر شهید در نجف
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668413" target="_blank">📅 13:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
اظهارات تناقض‌آمیز اردوغان در قبال ایران
🔹
رئیس‌جمهور ترکیه در جریان نشست ناتو از یک‌سو مدعی شد آنکارا برای کاهش تنش و ادامه تلاش‌های دیپلماتیک درباره ایران و بازگشت امنیت کشتیرانی در تنگه هرمز تلاش می‌کند؛ اما از طرف دیگر از مواضع اخیر دونالد ترامپ در قبال توافق با ایران تمجید کرد و آن را «قابل تحسین» خواند و برای عملیات مین‌روبی در تنگه هرمز اعلام آمادگی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668412" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFv2O2oSEqw7BuhssX97gqPa36Llh9ay9Wk1_e2oHUGKBlwTCj9JB4X4JgGIHfvYJWki2sNRlfFxFUkvumbD9rgmYbPv4XW0CdOjaEWK-BRh6_ZGBHa1vlZTlRVFlfl7-hsZLSwo9IxYTH-cSbiHCqLzZrDvFSZbqYoL3kplX6QxyqsRpmzpmF7XVFhCabWeRv3iFN7bfo_r7WxSh4hpNxbyV7rPpF_zAD34sqKXcTMjxWY3TLr-E7LFCck7BQ1ijYtqX8eRYGijj3tnqH-8oQ7MXrxbz6sD3Yu0nxtE1Jc43UDlGFs3ECsMJ5E1WhJMkNQV5DnDFk0124Jn0NmALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین نماز بر پیکر مطهر رهبر شهید انقلاب طبق اعلام قرار است در صحن انقلاب حرم مطهر رضوی برگزار شود.
اما با توجه به اهمیت تاریخی این مراسم، اگر این نماز در صحن پیامبر اعظم(ص) اقامه شود به دلیل وسعت، ظرفیت بیشتر و جلوه بصری کم‌نظیر، می‌تواند تصویری ماندگار و اثرگذار در رسانه‌های داخلی و بین‌المللی ثبت کند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668411" target="_blank">📅 13:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
احتمال حضور ۱۱ میلیون زائر در مراسم تشییع پیکر رهبر شهید در کربلا
استانداری کربلا معلی:
🔹
تا الان ۸ میلیون زائر وارد کربلا شده است که گمان می‌رود تا بعد از ظهر این عدد به ۱۱ میلیون نفر برسد./ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668410" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668409">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67392e2838.mp4?token=oHZnW_jeC-18lwrToIdHIpPRuM9uiRiSxz8KWz4AjpN9PRe0gdopY58RR_wxTPJqY0uV8Rz2h6P9ZrWPSfrYCG0-Nu9qWSAMbeMJd8rYY87xkGMK2wFwsd4iswFiX9aNNX1zbwh7VSFYnUX6FfL80mqF-48Xa44ZljaOW_sW--mJF4Vo2XsxuOfKv4TCA-KSIRcDDwNpS4QWZ3Ll-SsxWMJ8iCHaQtUkZfnzL-U4N5NGOxb8Jw-7z24tfVHu8LCoSMH8OQqNiUp3avid7vF1cQQJ2XbdxBK0knW6FD0iWY6Iw3MFVvMEXup4PnB1iIKSQU0PkewL0Mgj2BDzk_40gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67392e2838.mp4?token=oHZnW_jeC-18lwrToIdHIpPRuM9uiRiSxz8KWz4AjpN9PRe0gdopY58RR_wxTPJqY0uV8Rz2h6P9ZrWPSfrYCG0-Nu9qWSAMbeMJd8rYY87xkGMK2wFwsd4iswFiX9aNNX1zbwh7VSFYnUX6FfL80mqF-48Xa44ZljaOW_sW--mJF4Vo2XsxuOfKv4TCA-KSIRcDDwNpS4QWZ3Ll-SsxWMJ8iCHaQtUkZfnzL-U4N5NGOxb8Jw-7z24tfVHu8LCoSMH8OQqNiUp3avid7vF1cQQJ2XbdxBK0knW6FD0iWY6Iw3MFVvMEXup4PnB1iIKSQU0PkewL0Mgj2BDzk_40gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین برای استقبال از پیکرهای پاک شهدا آماده شده
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668409" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668408">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcde05c907.mp4?token=QTqq5LoBwl_CY-3wz49OpYKV-_JAORok2LOiRFKJqxGsnDTNQhUCCmV9N2mcER8a5BSmdIpqfvc4b8ZC9P54Srh8MfLvDO_ovM40z8RA6Px09iiA-uEdxaxPMohKacijKtQp2zWXH7dBaayl4_ow5rYqehNNqjBhpJMzNGxZuZaFza94lil9ZtTvt_a0PKnV1PZV3DFREO01cLgGz6NcGqHbC5ivQkmHsYnrPbrfNx-WWCfH5SMnJ2tHu0ntzZhVICNaomRUDIM-QXhJCombfnioz1ssFYQcj7BgGVuUin5k1qQfstWoKdrbJOUeGuigmwGkZ6y-z8dZtg6tegBJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcde05c907.mp4?token=QTqq5LoBwl_CY-3wz49OpYKV-_JAORok2LOiRFKJqxGsnDTNQhUCCmV9N2mcER8a5BSmdIpqfvc4b8ZC9P54Srh8MfLvDO_ovM40z8RA6Px09iiA-uEdxaxPMohKacijKtQp2zWXH7dBaayl4_ow5rYqehNNqjBhpJMzNGxZuZaFza94lil9ZtTvt_a0PKnV1PZV3DFREO01cLgGz6NcGqHbC5ivQkmHsYnrPbrfNx-WWCfH5SMnJ2tHu0ntzZhVICNaomRUDIM-QXhJCombfnioz1ssFYQcj7BgGVuUin5k1qQfstWoKdrbJOUeGuigmwGkZ6y-z8dZtg6tegBJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر امام شهید در حرم مطهر امیرالمومنین(ع) #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668408" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hop05qpgSmbKqTSg5TQ7ObL9t_0qxKDEWCmEbqitwICC9-8AxPuVMHweKuiq1zxJOaVSEbT82WNWhKuMVN-vYNO1cqb2Sg9Vv9KTkMOEAtUeh0h9T6Prmo4LU2eo2KvmdIfUGJ6Aq1uY9lHEWDiKrLocPkB2vA0mscaoWd0IYyO6ahDjZgSSQ210497YWgPsLOxBHgUPTEj85u49IR6BeYZUhTQ0X-0mhmg75tT1nkOn3oMA6qVV7ksQa4N7fYbUkGkWXhivGYgALGsiZMFnbGN2nP98yik5MmqVMi3BuJGmRIGCExVf_fgJkZlSrw1a72Ur5g0KDMl2JRiBQaae2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0VT2iaxxVElUxfINfhYsbnIF-Tvar_GIEvb-zSWz2gy06QbveNzPKFm2k0QiWU9s3wfRwSB7SDYYyXlt32m3BUbKNr48uezgPn-XVGqWLxexP5nDIR98SMbhNxpNSMuPGh22yAaxGMOR7PHTWU9nqAKC6EKGAazJ_1fU67vncVuiCysFVnP9ru1XIjhibUXwv0tWk3Gp4j6VRapBgNbxEdzOI2CsZUnRK2u8NLK-PeTRGIJ6Oo1bCvxlD-jk0mvTD6n0MmbpjazEcvXYyeA9sqomGtgEY3Pcryg2pR1WlAvoxIA_QdPX2rKKdAB2_IKzWETmSYsUv7Ga01RSE-HUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcClvOis0_Uqa3vLBzqVb_I6wQ8FWwiW6lwwSH4ObHPhsbSk3gA_6JT4ztXKg4Hvs8APZ6Yq3RL39X7tP9pUPSWBEHr3uLISeDvBjPbhIj1bq3J7Bnwzw8RaqfAqWALizMLqFWk071iszMn-2Y5o7W1T3ne_mcNsvFxclvnudC7TgwYbxQrxCIdb_meWifa2z8u55CUMWZcGMpnSnV-nv2kfjz97S_DTsyU5PaTzDeIZPVByEC5h-YhkLawd8wn7gICxubKQ7colxymdiA8mesGcgwuMzHQFFLy-hsyRBOg5T3qGRM2yiQTryc5MuCkxvJ7CYfq6oVqXM0hNQ93f0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARI9Cjys3KDK7nk1EnLSJA1mE7wEz-E9JrvHA5DT1_D9ZjhE5HZ3heOGWw12u9QV2o-6K3IqbBUKrkmX24ABcwX1Hp1MwYiOBCd53b-u7-DuvYPiepfXWIfGdeXqVn16zm6Ms1zAir6e9Y4DyXqEwwn-xBO4IXAfQilyB4Wuw0U0FKQrohVul-HRfJmAVXTJrsHZTNzGlKbIaGJ9dEQO8BmQdWwaPJVnyHBLxvlQXj9ED11Ngxh7upDRZsiNPo0mEb4LUxzVso-oPLsC7lpDCybzzDw32kzKIFrxnBWOWq8LV8vjygb_woPT7_UxOjEEV0r728VizY90ydM1Ldz8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7dfYbMhQmZoiV1H8syZ6sihDKv_ueZcoPAR0FxzFQroop_NK40MzqlTYZ8FffINMGWrfOEAsfycupavfNvU-Ty_8NemII92ZmFlF9-QB2VxA2f-T6PLb_RVDAlPjhcMBjerLbf2nu6VKCaRdsMlb4OYTIkH0Dw1ZU9sr9LhjICmc312USKaqOaGrI_zkStARwKWeJH1subfl-xp8wd01yEyzSXz3b5FieilNNc0lHfqhAg7J68MRwX0I0L0TT_I9eTVnTeZeT_DniCdGxCahPqXrIcMAune3phNoxKb5Bepdz1BzpI059wpgj36F5Kv7m8etynL3NyJl2t9NY5i6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTypkbUVOMSmejQTUimfnnU_D7xOHb1PsZfouwBiDExqZqpoBxXsX3kvfdZ57Qvx_wFbjwToRXkfZU-YTvBYTYHICMdIRv3XY873fh65sAocbb-3x9yuvszNy0kpGXx4IaE4RQVRMle_pkqLJM0NJ0b5s1PyvdgnK2O_fqHx58O2tFEzhzjsAvxP7e92m_hLCaRIDG96jN_eQSJEYWzNgSzViMKau-Um0ZvV7ZVAud2fpSThZnrMBmg5K41sYkSi9ZX7hLRWMecE1nILZItwjqtevq0wpJhGgwkFFNYXlFVf5m1ZpN5jHgyUb1skS0wi-8EyKgZmEJEGpo_FM45K_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAQpvDnymVcS8jzQ-9PlqtVg9_P0Kg835F0cK5g5H2Q7LgMazHDMuuE7mHxFKpKl5sD-9WNZLV_yDuaf025fd788KVZq7n8l--5j_U5iUqD0yJtArN8LUqCq68QqWy4UIj_7MsQx_-FaGcItlBq55zWqq1awiY12uxAWOzt2y6ddWsXyRFn8jHNLvY15MwSyUf8G2Xv89RzjKmQmLRTKoLKxwQ-24ZXESs4ppV8ZDBUCuNUOvMb8g9Xd3ZBoMZATvCxomMJW1YY-eUsWMP9fJSotnwGCoUmn4yHATSFrPDE1Fvg3FD4t5iHXh6v2ZfBFnBL8oBveg6-9JffpCYMB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCZu3waBlVdO4VW5xpfB1dLhehY_Skok8pZBrGj9kme-GybqPyFEhIsYSzWKrBCnZsCgbWuO1FtE7FTAR6I4C5n0QfolYSA3HWZuwvDMUpspm2ECGWFDNNF3PCDGWNU0FnU3RyQ9GEwfD3clgeMIbxcHfI9wn_byI6m55cOk4-GT1NObDisdAWiKJJYw4AuMOMD5pVYgUKc1s9648LUOqCvHl1OTxrifxrsAykXqzZDMvFb-BuVMoDW4MGyPGIxsRh3VMJsLkjXaeGVsP-ywjyj307KfUgWw3vtW91y01h-hW9TFZL0NXgO7wTE_nQthaojBlK0MV3Rx7c9sEEHS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5xaYgpz7_3RvQPddzCN0Zb50_ceTIJOYwyf0K3YB2RgWu0wKqsH2emKKlYuHUwOeaAPxSM-yQ6k6UIKs_PBn0RN7Q2xYCvulQ82yuloBr0_9oxhMrfnqQD5qkY4uBfqhUmc6R5E_Xc2TDFnqFY_xy9PuYzKsJv7T_6UZPzKFJ8JUdRUHwh9hrtNobC1-NEecBYvJeSpqZD6GLFDaoe_evpkq_u3j0u684R75TkjjY8nZBqM5huFw3U6qoYXPMwXsrCv39fKuIlUWUU8xrTaSP5sNDvtEEBiEKLFCshneZxLP3E1Z0FJUFcnqZTDRwEwFqX1lBFxMEZe5Sqth3GCdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668399" target="_blank">📅 12:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آغاز مراسم اقامه نماز بر پیکر پاک و مطهر رهبر شهید، سید علی خامنه‌ای (قدس‌سره)
🔹
مراسم اقامه نماز بر پیکر پاک و مطهر رهبر شهید، دقایقی پیش در حرم مطهر امیرالمؤمنین امام علی (علیه‌السلام) به امامت آیت‌الله سید محمدتقی حکیم  آغاز شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668398" target="_blank">📅 12:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8fcb93db.mp4?token=Btqa0a8WmMa4h2QX1FMJ8klXpD1L13I8QWTrgB2-_QeJu_2HsSIr1ldmDudCeDrmVeziaRpTcsEFhEJhSw8o8XuSIVVIjWuNOn6YfkleaG189y74K2RCNKg6MD_JIwTPJJdnHugo2dsEy0bZHvCdZOzg1Ijm8pJ6lgztm0En3UEr_50k3zsvxttGv3HThVVQpfHZjIFnAoqyg__SV25vP3rUMy584rHppS4kiQTEgUW6ZIicC0eNS0sTolJkVXi_EPbFa3sppbGpMjuLZx97IfA4-rRYnM6Z6fcYfGTul8H1OfpQ-Hjg9lpNXIfglU9C_jr-aflU14VT5WG8ByfNnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8fcb93db.mp4?token=Btqa0a8WmMa4h2QX1FMJ8klXpD1L13I8QWTrgB2-_QeJu_2HsSIr1ldmDudCeDrmVeziaRpTcsEFhEJhSw8o8XuSIVVIjWuNOn6YfkleaG189y74K2RCNKg6MD_JIwTPJJdnHugo2dsEy0bZHvCdZOzg1Ijm8pJ6lgztm0En3UEr_50k3zsvxttGv3HThVVQpfHZjIFnAoqyg__SV25vP3rUMy584rHppS4kiQTEgUW6ZIicC0eNS0sTolJkVXi_EPbFa3sppbGpMjuLZx97IfA4-rRYnM6Z6fcYfGTul8H1OfpQ-Hjg9lpNXIfglU9C_jr-aflU14VT5WG8ByfNnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر امام شهید در حرم مطهر امیرالمومنین(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668397" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=laCB2DTFa1uy1EMCT6TbNM5tvRHRz35CB_x9Fxro4kWhQyxhHnb1e6ZNRqTQq2H_cz98MV0BGKjVwRzsMjzaKbiLbPUGdSJrAuFFhFCXjhA93831pgeGwTPftkr6DRJaKkwBoO4veyayfcD_laHH-TX5zYZBm_o0HG5JlLtpdToas-ygOd9JdjAtGzTc2CPxdP6j-1_3vRiADVA9eEQ56T11g8wjAEQZaB0P6k9Oq6dDKnhB1ob1SA0PRCGdQjVZrVjTrtDsz4JFCX1QX_keb293AmEtNywcxZOJIwCA8twUMqN6hJZZYpF3nYJuWC-1u7d1ZzxVvDCSwyh0BRE-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=laCB2DTFa1uy1EMCT6TbNM5tvRHRz35CB_x9Fxro4kWhQyxhHnb1e6ZNRqTQq2H_cz98MV0BGKjVwRzsMjzaKbiLbPUGdSJrAuFFhFCXjhA93831pgeGwTPftkr6DRJaKkwBoO4veyayfcD_laHH-TX5zYZBm_o0HG5JlLtpdToas-ygOd9JdjAtGzTc2CPxdP6j-1_3vRiADVA9eEQ56T11g8wjAEQZaB0P6k9Oq6dDKnhB1ob1SA0PRCGdQjVZrVjTrtDsz4JFCX1QX_keb293AmEtNywcxZOJIwCA8twUMqN6hJZZYpF3nYJuWC-1u7d1ZzxVvDCSwyh0BRE-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریادهای «لبیک یا حسین» در حرم مطهر امیرالمؤمنین علی (ع) در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668396" target="_blank">📅 12:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEWFTfeq2T1yNcfXx6rlF2em3tyHoLC9kK-6fnopqQ7MT5yxur8kg7I3K9bdVYJDiwahjMdrPMSv6uEtVXfEcWFJlTEuvPnO72lZxmlVSwQr67d35pbdAfNNxKbzDa7vAURhUcwOkHNi5QhNmcwR59O-bVrRsVRMiPCNCj4kj7AUVaehsb0NOOxI_w6V9UmNo1OGm23xOfFoXAtcpNdRLF1PXag75TrDRlTK2KXBftBaAYA6pakwoIFZbAXqc942ZvDkCa8SLOCbfIVW0dVvLlRMSnVe2iW-zYxKEr3TIfL9rQIn06PNec2HpWkw_G8GLprBFr6EQm5E2Edwz09aEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛ «بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافی است آخرین جمله، پیام یا حرفی را که دوست داشتید به رهبر شهید بگویید را در قالب یک فایل صوتی (ویس) برای ما ارسال کنید.
▪️
صدای شما، بخشی از بدرقه ماندگار مردم با رهبر شهید خواهد بود و می‌تواند روایتگر عشق، دلتنگی و وفاداری شما باشد.
▪️
فایل‌های صوتی خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668395" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af707f0d.mp4?token=fYxbHk7QSOKJ5UPoijNvJN_v-tQFHf5bo9-BVp2U2-qpq7heKBcEoMbZ6CAfx0YPsoeWnbz_GsHrvHnOeN_5lRoJTrZtzl9Ot_67M6FeYqL-FdCS6UT3X5EVlCYm30b4P7NMr8ksk78GA_rK43zyKI9OsIoLa_8GB28_gx5PMFTyy-_OKFzTKdQfySaxNWn-JWBvpxqszYiiM_7mIZlYsCwjJEqlPoexudTxHm6ysKYxEjKhWRE7tuXi1in3r3PnDdh7e0YT2Cchk2uIKZNxh3LEhlyiVPQviz0q05AZUXU4IZBcaMp6guEpDGCyz_uF-D35C3Vrhua1nvHqUJhEtCqHe3YOSnMN1nlXNaz6aBca_J5iS7wXOGozXgw1GWfMmxaL10yjYThH3840ZSju3AnA7U2sQd1zzXtqBvkT5rYOm8KeRHQHCtLMj4E_Fjps4T49kv7BkKoVt_ZxVYsLgjhWRgcQz7qZpnH341eiAhYl8Bwi-4DVR-sUWxAqrQAzXK44Aqx4FwLpLUN3_9hFhnhtC6nKJrxNv7WhM-H3ci2qXUhnmLCzTcLq4dVb4tLce758N8Di2ZJ_j00aUu9p9vmI9D4hl-1TC8EmjdsH-1cSPt3miw72votzIcwVHKP5k01yb6DSHa-HPzq66p28m7iR-2oFyHlbbn9zbra7F8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af707f0d.mp4?token=fYxbHk7QSOKJ5UPoijNvJN_v-tQFHf5bo9-BVp2U2-qpq7heKBcEoMbZ6CAfx0YPsoeWnbz_GsHrvHnOeN_5lRoJTrZtzl9Ot_67M6FeYqL-FdCS6UT3X5EVlCYm30b4P7NMr8ksk78GA_rK43zyKI9OsIoLa_8GB28_gx5PMFTyy-_OKFzTKdQfySaxNWn-JWBvpxqszYiiM_7mIZlYsCwjJEqlPoexudTxHm6ysKYxEjKhWRE7tuXi1in3r3PnDdh7e0YT2Cchk2uIKZNxh3LEhlyiVPQviz0q05AZUXU4IZBcaMp6guEpDGCyz_uF-D35C3Vrhua1nvHqUJhEtCqHe3YOSnMN1nlXNaz6aBca_J5iS7wXOGozXgw1GWfMmxaL10yjYThH3840ZSju3AnA7U2sQd1zzXtqBvkT5rYOm8KeRHQHCtLMj4E_Fjps4T49kv7BkKoVt_ZxVYsLgjhWRgcQz7qZpnH341eiAhYl8Bwi-4DVR-sUWxAqrQAzXK44Aqx4FwLpLUN3_9hFhnhtC6nKJrxNv7WhM-H3ci2qXUhnmLCzTcLq4dVb4tLce758N8Di2ZJ_j00aUu9p9vmI9D4hl-1TC8EmjdsH-1cSPt3miw72votzIcwVHKP5k01yb6DSHa-HPzq66p28m7iR-2oFyHlbbn9zbra7F8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید مقتدی الصدر، رهبر جریان صدر عراق، در مراسم باشکوه تشییع پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668394" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزارت امور خارجه عمان: هدف قرار گرفتن کشتی‌های تجاری بحرین، کویت و دو کشتی تجاری سعودی و قطری در تنگه هرمز را محکوم می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668393" target="_blank">📅 12:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دریادار سیاری: سواحل ایران را برای‌ دشمن جهنم می‌کنیم
رئیس ستاد و معاون هماهنگ کننده ارتش:
🔹
نیروهای مسلح ایران در کنار مردم، آنچنان قوی و مستحکم در صحنه حاضر هستند که دشمن می‌داند، با پیاده کردن نیرو در سواحل ایران، به جهنمی وارد می‌شود که دیگر راه خروج از آن را نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668392" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏆
صعود سوئیس به یک‌چهارم نهایی با عبور از سد کلمبیا در ضربات پنالتی
/ آرژانتین - سوئیس در یک‌چهارم
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668391" target="_blank">📅 12:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT3dN_HxyVYwaL7wCBczxQtQmslTpnSgE4GMxCRMLNaDfJBOxqlnIYZUSnf1d7GINapfcY7RH9Cxw2B2aGCsI8eZshcF87vr3w90GjlTnyIBLfh_laSugOgQxC5s4OgqXA6YGxiLXy3FzIUP2gM78ghx_kX2En-zgE_nrskNeTRP566RoSUbFElfcaIhDxr2_qXdu0L0qT-1dboBoThX1WKh0BSCnIkN01HjnR9m4kHES39gzi-zoewb1nZSQnKCp7TSkVkxfYlQQdy2ZXd6od_mjjLNP5TyfOasOZOe81kn3NBQ9oyn3bOaGjISw4iarwbnpdGcfNV5kcr4uDtleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ما با قاطعیت بر حقوق خود ایستاده‌ایم
رئیس‌جمهور:
🔹
رفتار دولت آمریکا به عنوان میزبان جام جهانی بازتاب‌دهنده سیاست خارجی شناخته شده این کشور است: زیر پا گذاشتن قوانین، تحقیر رقبا، ایجاد موانع و فریب‌کاری.
🔹
ایران چنین بازی‌هایی را رد می‌کند؛ ما با قاطعیت بر حقوق خود ایستاده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668390" target="_blank">📅 12:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEnk3sc-R6G1s7iFtxoL8ZjvYHW1LADO6frkBRQk2fkeTU_kCeSs7hXR2HNGULV7leHUooWq74Yei-dreUTveLw0xc10ILLcMGQ1yH7uQJTKTvWscPYPdjBXMg3bzDNjBQ38_VxKdtCT0ofOqbAD-32Fx8rkZD9u2zjR2x9JOSvQsrfhBJDgTGxjnc9LVYGPv0L8wSZAa8is088K5HUGYHUslQucmm5I0bH0RFOmsWWE7wFSesrQ8bp46sO335yO3emln3nyggu6deRGP9hhBHVRT1WDYpmoscldQYRoLbO3pGC0hN3S0BKkFGA78uw8Jy3yqUmSCxopQvjWDT0tjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با کاهش ۲۰ هزار واحدی به ۵ میلیون و ۲۹۱ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668389" target="_blank">📅 12:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CclCP1W1kgOCDFYt7w9jsxovpvmCf0EKYNrUiQIdNLWbohGh4xGcZ9zLQlpwxCdVQ35l6iUNmRkAxHAbs7DNltY7f67sM2PRPWAKcWgpj21TX48X-FRBEANfsKFC2mygKX5c_GDeV03qJEpRDDNyH8FIJqfEvh0XeeSQZ0yglZN5B1aD-AN7GRHNcuj4wruk7Xp3Jtw3UWUz3z0ii98UcdatYIGJmIEgwZHBD5VBJWxmryPOmgXLQUo1WAf3LxjaeYLSOyMJWbBrfkUzANZeRV0ZrIi6PeapSmo0BJ7vStkGmyiRIRnRuIOT8KSv7gg4IBRxtySAY7Hg3P2Am2OTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی در جوار علی
🔹
مرجع معظم تقلید شیعه حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای زائر حرم امیرالمؤمنین علیه‌السلام شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668388" target="_blank">📅 12:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی به کویت
🔹
کویت از مورد اصابت قرار گرفتن دو موشک بالستیک و ۱۳ پهپاد در سپیده‌دم خبر داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668387" target="_blank">📅 12:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287e3f1a5d.mp4?token=io_BdJxP54CVUucwgTNkTTet7pBXQLIn5NlwwVDVtIjmzlAt3C9YvrVlmaJKERqf_WiuCrZFYDZjFWF61AdL30QDjMKr2nLLc7qMjJKkSedHKVjLsOfuTH0Gi-lSONG3f-6Gkg4r9RIU_D2jxJqtzYKbv8ICjJQskH5oN4lPEDkUG0PXFOngYypLdtL8cbwPPq3YwPqg30DVf0cd5mRlNfVaTac5boKJp7j3CsNx_GI4NwfM0Ov6BmpeUbwgw6l_b8C7x7lLh3UixmUhhv2hkvHxCC2Y3RwRKFKpOeXZrHcm8O3GyMs-DKNQRXADpes4_EenS4WxRMiMYo33OE3zEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287e3f1a5d.mp4?token=io_BdJxP54CVUucwgTNkTTet7pBXQLIn5NlwwVDVtIjmzlAt3C9YvrVlmaJKERqf_WiuCrZFYDZjFWF61AdL30QDjMKr2nLLc7qMjJKkSedHKVjLsOfuTH0Gi-lSONG3f-6Gkg4r9RIU_D2jxJqtzYKbv8ICjJQskH5oN4lPEDkUG0PXFOngYypLdtL8cbwPPq3YwPqg30DVf0cd5mRlNfVaTac5boKJp7j3CsNx_GI4NwfM0Ov6BmpeUbwgw6l_b8C7x7lLh3UixmUhhv2hkvHxCC2Y3RwRKFKpOeXZrHcm8O3GyMs-DKNQRXADpes4_EenS4WxRMiMYo33OE3zEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع میلیونی رهبر شهید مسلمانان جهان در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668386" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd097f4d3.mp4?token=kCJx_GB14NFtDyThf3-c1nb16cAeDn6JQ7CykMkLJC_qruL4GWXFHAkWH5voHfhtW7ByzhAncCW-DhZs_XDkYg3jHZxKZ9oTK-89jhA8CuSqv3bEUpmhW6eRNKcKRI07fvY74ymTNXNVU-b3jR2mJgwkspFa4bGVj6eQ3G_Q7xbe0ITtFTweojqrt5qBxSew_3u18fuqJmAf-xS_vpxZ1h6fajJvBBTiG75g_JAXVMqE-wNupkTuVtsO0l2c6Xj5ktgvn4y_779o8P22qwIpk1yLMTByeldnaa9BSYM2UULO5Ukw_cF_Cg7F-8Rep3cLZfvxUMRwqR5nKKUh3mWwlIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd097f4d3.mp4?token=kCJx_GB14NFtDyThf3-c1nb16cAeDn6JQ7CykMkLJC_qruL4GWXFHAkWH5voHfhtW7ByzhAncCW-DhZs_XDkYg3jHZxKZ9oTK-89jhA8CuSqv3bEUpmhW6eRNKcKRI07fvY74ymTNXNVU-b3jR2mJgwkspFa4bGVj6eQ3G_Q7xbe0ITtFTweojqrt5qBxSew_3u18fuqJmAf-xS_vpxZ1h6fajJvBBTiG75g_JAXVMqE-wNupkTuVtsO0l2c6Xj5ktgvn4y_779o8P22qwIpk1yLMTByeldnaa9BSYM2UULO5Ukw_cF_Cg7F-8Rep3cLZfvxUMRwqR5nKKUh3mWwlIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متبرک شدن چفیه‌های عراقی‌ها به پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668385" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668384" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ قمارباز درباره ایران و توصیف آن به «سرطان»
🔹
دونالد ترامپ با ادعای حضور در لیست‌های هدف ایران، این کشور را «مردمان شیفته و بیمار» خواند و گفت که باید این «سرطان» را در مراحل اولیه از بین برد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668383" target="_blank">📅 12:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ef70f2e3.mp4?token=T1Qe3TForGwJTdshgAI_vn5ErC4DHb6bi9R1uuHfSBtOBdvpPDUIVGntNtyBT-2hOEbuqDI9aVLg77cXrxQMl9jLtyvqf4Kbbu_9vFmni6_GUjzZHaCUcbSZpR_XCKEuIzMREWPD5u7HmRBY7gRfjSS6C9sph6zYZvMgmSDNF68uKGH4FXj5PHqKHhvFq9-bTg9nummo_nYRhirdf7oeTBSAbtAggDm0m1CfT_MmPEN_ExDBOdtarALWwWlGzacUD_DmYHWqeFr8Y-C8LuMqEn3MG-TADutUp_iVcbTt5eGSssbp2hA0R0QYW6iRaWYnbFRt3i5fHWqWhdrOFeVxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ef70f2e3.mp4?token=T1Qe3TForGwJTdshgAI_vn5ErC4DHb6bi9R1uuHfSBtOBdvpPDUIVGntNtyBT-2hOEbuqDI9aVLg77cXrxQMl9jLtyvqf4Kbbu_9vFmni6_GUjzZHaCUcbSZpR_XCKEuIzMREWPD5u7HmRBY7gRfjSS6C9sph6zYZvMgmSDNF68uKGH4FXj5PHqKHhvFq9-bTg9nummo_nYRhirdf7oeTBSAbtAggDm0m1CfT_MmPEN_ExDBOdtarALWwWlGzacUD_DmYHWqeFr8Y-C8LuMqEn3MG-TADutUp_iVcbTt5eGSssbp2hA0R0QYW6iRaWYnbFRt3i5fHWqWhdrOFeVxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ قمارباز درباره ایران و توصیف آن به «سرطان»
🔹
دونالد ترامپ با ادعای حضور در لیست‌های هدف ایران، این کشور را «مردمان شیفته و بیمار» خواند و گفت که باید این «سرطان» را در مراحل اولیه از بین برد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668382" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
طواف پیکرهای شهدای خانواده رهبر شهید در کربلا
سخنگوی ستاد تشییع:
🔹
پیکرهای مطهر شهدای خانواده رهبر شهید، صبح امروز پس از نماز صبح در حرم‌های مطهر امام حسین (ع) و حضرت ابوالفضل (ع) طواف داده شدند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668381" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INLl9Qmd77vkGElh61Qy2i8T-zdrT6s36Vk2QsOPcJmPN2UYPioCSqLZdvOkj2luAmqLwfFWeOXqjCgJsxDY8Fhr6zKQMfrYXJOvI594v0oMSaQRmFnE_SzkzB9B-joaplGUSUWstQa4dt6Enz0YS2f0AnGmJ-GbhVxUFMn65gbp00RAlbxIoE9kHusySFwTllWAjjImo9l0eSlx8C4pzfuuX4Czu7QIrsstCo4UHJWPmgc_SnWBfwp4gl0OV0BEOARSRDWxpWTlWN-QqSxfeWe3aLUrc0R1Z7hCg1jhYQWflmV-SVI8Qree7c4zJjqE1LgnN7ZWVD0LaW-ClHQW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وَتُعِزُّ مَن تَشاءُ وَتُذِلُّ مَن تَشاءُ
🔹
تصویری از حضور میلیونی مردم عراق در تشییع پیکر رهبر شهید مسلمانان جهان.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668380" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
کامبک شیرین آرژانتین مقابل فراعنه و صعود به یک چهارم
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668379" target="_blank">📅 12:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668376">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff55cc771.mp4?token=NulTJ4VArvz5fARE1KbZbR-P-FlOxBb3P0yzML2eRrvOMjfvyNCwoPd3qNeGrufERdLliUpZvEAREV-UP4RsVttM8AmH6OCS8D74TheUqjMivVEC1W2vSeyBhgvwgfHV5ty5xegqq7NNTZ-f6i1VWseMEIM5B1IDsyvHaK9_WZXdYj2MN85PFjp3YZRGW_73KhnQ67JiP-IKUTUpyPIGOqQjRpIgDQ4xUN3FDogrNfhgaX-NzA4IbcqoU7We2gGKNGgeBhybaU0de9GQ5FyirnFfeb0wLk-0qDPPHCvGw-koxKdI66ynrBSE0L5qICkJfVQEbn57xLkEGWp5I_wpTigVz-wrbxkFJDpeFObFYK2lncCKi9knKHL_71Or4XnWUk4EJhlD4V1mI0PNJgOP8iG2KqtsKChFEg3EI-Cd_SMpVb16vZKsJpNQHZ4neI466PcjwWCfAyg8nOT12GI-i4oHDHleLea4qTKrXVM3TIioF6QBcJekdTm69EAhL3woAkIdIV9EpM42WmuP_Md2wFSittjTGnca8PPr2U19rzRGg_vsFecDlC38zwBaTYfZYO50Jp6SLnPhUXorEcGIhnCTuRggvz_s9yn7--BitSnhXhC-VJejVX7QloQMauRvgB4qDcYfepBD6dl2A2t6LESerfx5ysbAsBSMyX93c6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff55cc771.mp4?token=NulTJ4VArvz5fARE1KbZbR-P-FlOxBb3P0yzML2eRrvOMjfvyNCwoPd3qNeGrufERdLliUpZvEAREV-UP4RsVttM8AmH6OCS8D74TheUqjMivVEC1W2vSeyBhgvwgfHV5ty5xegqq7NNTZ-f6i1VWseMEIM5B1IDsyvHaK9_WZXdYj2MN85PFjp3YZRGW_73KhnQ67JiP-IKUTUpyPIGOqQjRpIgDQ4xUN3FDogrNfhgaX-NzA4IbcqoU7We2gGKNGgeBhybaU0de9GQ5FyirnFfeb0wLk-0qDPPHCvGw-koxKdI66ynrBSE0L5qICkJfVQEbn57xLkEGWp5I_wpTigVz-wrbxkFJDpeFObFYK2lncCKi9knKHL_71Or4XnWUk4EJhlD4V1mI0PNJgOP8iG2KqtsKChFEg3EI-Cd_SMpVb16vZKsJpNQHZ4neI466PcjwWCfAyg8nOT12GI-i4oHDHleLea4qTKrXVM3TIioF6QBcJekdTm69EAhL3woAkIdIV9EpM42WmuP_Md2wFSittjTGnca8PPr2U19rzRGg_vsFecDlC38zwBaTYfZYO50Jp6SLnPhUXorEcGIhnCTuRggvz_s9yn7--BitSnhXhC-VJejVX7QloQMauRvgB4qDcYfepBD6dl2A2t6LESerfx5ysbAsBSMyX93c6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ماندگار از تشییع باشکوه رهبر شهید در عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668376" target="_blank">📅 12:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔺
آمادگی کامل مدیریت شهری برای مراسم تشییع پیکر مطهر قائد شهید امت، حضرت آیت‌الله العظمی امام سید علی خامنه‌ای(ره)
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
بازوی بله
⬇️
https://ble.ir/MashhadTrafficBot
سامانه
#باید_برخاست
⬇️
https://bayadbarkhast.ir/
#مشهد_یک_شهر_یک_دل_یک_بدرقه
#آقای_شهید_ایران
#بدرقه_باشکوه
https://eitaa.com/mardomnegar</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668371" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668369">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUwzEJdFykIBNqctLu3IKrLMSZLso1MVXgL9WCCJdRdVOJPGHAE6gUZcNoK4mI-kp_znSuvBwMpHLuFu7JL61jwyGPT7E3OQ0n778Li_axSDETVwvht6JS-yQBq8xcSi2-dEdBPOXKxJXS8ShvCPX_gDLFqWSqvzbxCx-YNgGvLRsqHY3NTofa8c25fKZKbzpw-TkY58vvDbkHhwLCBITF_uz-6O4MZm5RPpqdtnI56pKIfN_rabZ-iI_2GgMtexc99Aw_HkprU-Fa__VU0GJBnX43FpFKefGbSr66wQXsjFssqOguIQ1vXSvdaHdUUn-aGkGBlb5fc8hFrIDBWucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkOq_HA0J8SNrIh1hA5EoeFUwaZLH4xjp-phdXcZbVB0RtpkpiZlUidY49XiEoqvDUfv6ZyzL-YjpTtFneCAiUX-vumleJi8LAqExD9j0BxF3fufB02g6Dnis5d_SWB-L5a5ejMEeyhajo3THFpJFlSQt0nDZ3v9dcFU45TUGpgoEI_NCt92NL4evUQ5W5nPrR2DlsoZ2OwmyzJA54k-XqeclaOqHdSwTj1jzlfIWVVR8CcO9ox_BnSknlkEPfODPJLJuT82JG17ad6veHc6E9y3bOU-RFcx6eutzdbI38Koy8EFgn9LbgdOnq2A_BWbqWZGR5PFWQdYAGhHno-tIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
هم‌زمان با آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۳ جایگاه موقت عرضه ارزاق عمومی با هدف تأمین کالاهای اساسی و رفاه حال زائران و مجاوران در نقاط مختلف مشهد و حریم رضوی مستقر شده‌اند و تا پایان مراسم به ارائه خدمات ادامه خواهند داد.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668369" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668367">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نمایی از پیکر رهبر شهید انقلاب در صحن حضرت زهرا(ع) نجف اشرف
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668367" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668366">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLG4HnG6uPyzAO6rmI8FbbeDu2lgFusFOSX1j4tEf5afgpkSKcq5WJ7VVtMxrRnnXiozKXbLbDvYxcQXkTZV2f7pb6BpgAXUA0XeVUyJefvpUEvgek82LXLzmiMQllDC4rURS6q3OJFz24idIRa5k1IBGprg4s8yKfMcc8hTa1uim0yDsnsF16YN4aEv_8egG4MjkJFLBdo5K3es0C0Z2h4iQdxCqXuyhDM5tt1pPZJwcc6rpQCYtrtGThULDoQkzv2hcqi1SlendqCv212c9rbv7wLDctrDEgFrvuJ5DDICE887t49NyLj0uQYRKeJAdGWpkA5D0T7Kjf7hoxOGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: تفاهم‌نامه پایان جنگ با ایران برای من تمام شده است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668366" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ترامپ: اگر ایرانی‌ها سلاح هسته‌ای داشتند، از آن استفاده می‌کردند
🔹
من نمی‌خواهم با ایرانی‌ها تعامل داشته باشم.
🔹
تصمیم گیری درباره ادامه مذاکرات با ایران برعهده مذاکره کنندگان آمریکایی ویتکاف و کوشنر است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668364" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f690664bc1.mp4?token=NlkB5d-hFMnhPUGbbqSeNarB-8o44GF71BB8GVLdUdA_MLEa3Mfj4QU_7kUx_eRO1upgz5NzsMOfIkG2yolKmCwtIU290lxt_BhtIZ_YhuxoXYCguckao1hr3pPIaZF3cCJ0Vp2GksfGhItwNvj5SIDYW9nbz5GiHK5Qt6CfPgRSExEoYGgWWwQpo0qyjdIy0ehRx_JNlYqlB_9wOmvNXpidX6-hb1t5IYrJIB-6XwVfRTb5F2elkeUPuzOt-V88QffqY9DrTwAzxGoREmdt_kpmxwQTolEdWbfn1vDrMJVIYZQhduhUMf2W5wCzzq4FZyZNH0lR_8uwmRgymfPYmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f690664bc1.mp4?token=NlkB5d-hFMnhPUGbbqSeNarB-8o44GF71BB8GVLdUdA_MLEa3Mfj4QU_7kUx_eRO1upgz5NzsMOfIkG2yolKmCwtIU290lxt_BhtIZ_YhuxoXYCguckao1hr3pPIaZF3cCJ0Vp2GksfGhItwNvj5SIDYW9nbz5GiHK5Qt6CfPgRSExEoYGgWWwQpo0qyjdIy0ehRx_JNlYqlB_9wOmvNXpidX6-hb1t5IYrJIB-6XwVfRTb5F2elkeUPuzOt-V88QffqY9DrTwAzxGoREmdt_kpmxwQTolEdWbfn1vDrMJVIYZQhduhUMf2W5wCzzq4FZyZNH0lR_8uwmRgymfPYmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریادهای الموت لآمریکا الموت لاسرائیل در تشییع رهبر شهید مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668363" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668361">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7141ea513.mp4?token=ZSy1bC7Z-FKMudbF8cfdnNHolgNwnh4QalKlaWQhvgAh7ISza3V8WMXRv4FQ4gxrMoMEZbby1orHCwPYtBaMbp3h9zwTnP4b2PNcm_U_7drBV6kgd_9N5_SrL-CHWXdtwf6_U9OwC3Xf3L8jHhvLTpEEGaU0-XGKeDpLe4hWrZiidYQ0EUIGVt9vA4LuZsxmi-8coVifCUQ2FcPKK-6zRaUBpcCjOTYrfICDWijMRz0Dd8xlIUmmQr5FXzeUgx5cq9S4XEG_G1c__jn1DtK8WlOJ7TE6GOqP9d0mHg9HsRP38VLAWMqi8nqhxDcnXjIdY9eMGeIMXVCvnhBewugyEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7141ea513.mp4?token=ZSy1bC7Z-FKMudbF8cfdnNHolgNwnh4QalKlaWQhvgAh7ISza3V8WMXRv4FQ4gxrMoMEZbby1orHCwPYtBaMbp3h9zwTnP4b2PNcm_U_7drBV6kgd_9N5_SrL-CHWXdtwf6_U9OwC3Xf3L8jHhvLTpEEGaU0-XGKeDpLe4hWrZiidYQ0EUIGVt9vA4LuZsxmi-8coVifCUQ2FcPKK-6zRaUBpcCjOTYrfICDWijMRz0Dd8xlIUmmQr5FXzeUgx5cq9S4XEG_G1c__jn1DtK8WlOJ7TE6GOqP9d0mHg9HsRP38VLAWMqi8nqhxDcnXjIdY9eMGeIMXVCvnhBewugyEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: تفاهم‌نامه پایان جنگ با ایران برای من تمام شده است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/668361" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne6yFgmbs27jri2vFrJtbF2S_fd1fEDIPx0qxfYjnnWG13giUm4gi8cM9BdKj6eVbh1A8EaCtEHYHiFhEQx9BL8nKixMtRc1p24ZgEo6Mw0jmkvYRlfQSJxvdjv4RkT_7bmbYfcGmSK4ozAZAQ-ebBfwX4nYiJ3Z02mi6v90n4BGZOYBrakV6fXVD_xSgn0WYzAFyqQbRAkL21lMqCfgLTSCpqCMpG6VdDhD84MqSwpCszq1fVswVqsU702JGXckdEG00TNUAnjMUUdlO9WRl2xRrh2wtdZIyKD1YqnU3roAWMpzHkxkIH2VyyWI4_y_WgFSImwGwfBDVUzyd9naFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8GV1XYP6jlMVNnOSIqBn2vo_mBzmZZ401_Sp1pg-dD2mg3xPDaRuatfevfN-IgEI68X9szzyib-UVW0b894NiXpsxt6QFPLK6NtI-o5sSyqeBoE8_6dqCrU82TcDDNFvFSZdCapZW4kc0IYK2OtLT6lJE0DsTGSvWunDdvRIKoqGme9dGa0LjVWJk1eaNH7n5J6F23fHBeZNBfLgSScO-8bBBKdBSYcMegKQCfCKGwUq3MnqLi3w3-Wvk2QzSuoAN__AbKcPEiGunSZpTcYxJPk8YfgLFTPZGCEaOeexlrDIuI-oOj84lTcJ3kAQ0mnCzhfYfGhsALbSGXkuOzS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvuvJT0D4Sup6VgrHfRcrCS4H7CDjRwsRDIbFsDGJDjZxK7qtVOL5y5LegH-7377au3LHKj6xHy4mE1GfAd1cH0vtLryRowAfSoi2f5oriwaepMov5d1D7xstD10R3pDPBzmDzfkOh4m0mh_tgO__4_gYWbPAVXNGA8O6Dd5NP3nTXe35DH5CYdPb22bjVEtt9Be9ZmAysdzvxCE8uE1719Dkzjo9h71kCTHrBgnTI-4gTj_e99NGCQyL8nZ_JWRjCrUmEdyJPNt7RoxBwjNGq3Ht2Xr46-J_WQODClIXUvnmCb6IaTUdt0w4zkVYPnTCyxmgB23beYPSv3Dp24CTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر پهپاد سرنگون‌شده در شهرستان خورموج بوشهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668358" target="_blank">📅 11:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4a364b31.mp4?token=BOuaYegyK1dlSvSifKUrh-XMGnxNIkAAQNo-HvzggX1t0fABvNUlwksopZvQDGMlyMwTYGoFP9c9k6jDOyD3LOm1Yp69nNnU_OU0OZL0KVZRj5QcjlvQmN4lCqYnDLd4WzvPGyjYRDlLE3IwxKL4-WBMxQDD6estzlFUSYq-AHy01ih0j1Wd-AASHcQBp4WjqC-GJCwscv36v2L3VPV55VjrTPmsCI5Y3nejfh8CR-WAs0puwKTc29s3jcLfSxymgnNo3Fy_ru30078sRfHQcQVbWgScYl_xvve7Hj_7x5Os2mruSPrKFf6MIDSZGx7rAARuMs1EWOR8byLuhpVZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4a364b31.mp4?token=BOuaYegyK1dlSvSifKUrh-XMGnxNIkAAQNo-HvzggX1t0fABvNUlwksopZvQDGMlyMwTYGoFP9c9k6jDOyD3LOm1Yp69nNnU_OU0OZL0KVZRj5QcjlvQmN4lCqYnDLd4WzvPGyjYRDlLE3IwxKL4-WBMxQDD6estzlFUSYq-AHy01ih0j1Wd-AASHcQBp4WjqC-GJCwscv36v2L3VPV55VjrTPmsCI5Y3nejfh8CR-WAs0puwKTc29s3jcLfSxymgnNo3Fy_ru30078sRfHQcQVbWgScYl_xvve7Hj_7x5Os2mruSPrKFf6MIDSZGx7rAARuMs1EWOR8byLuhpVZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از مردم عراق که برای تشییع پیکر رهبر شهید مسلمانان جهان آمده‌اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668355" target="_blank">📅 11:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=WwJLGKXtGC9-xFYc7GxPmSwN8kpsI3gyZKMhs7MEES-HxWJv04J7r0oVfQwwfoiHM5K6bdSsT9bFT_LY8E_pu6Pdr-dLQdLA5SVCAAOBcNVhfoXUZ1XO4Btbcx_my32k1VcBmtHNuJXcx-RwB5frU9GTj0gLseM3k389YAitW2DL68CPppfqipUT_eHOTo3uLFA-JAn_QE0G9ZdVH73iSmA0hXu0RnLq_ZE0VFzGYFowQ1vlkAjWQCq7huhA5-uH9Vn13a3a6kveIo743jAHEnAivURj4MbNqi-f7GcdMAdrJ9DUSDpqnM0wmE3VAwn1bHFaRsqIIVKFY5V3ORVLwKu_ThUVRGmw6Q82yUHKpKbH5jcCqMfvq5eimQ-dJjYROna45Cc-s_ou0OYtitv0YacEeh2gmKznb7tvdas39NHg8_oICJh6uQA_AKKFSgERuK-ZaMCOyB1buPvg9KLjP82GekRfUgTXtqnScbPadWQHKo3hcs-EPELyVb85EDWyDku3oLekSNnfEjPqx5KEmORmjanFAg06jqwI23N5tl-aY1K6Kx558aLZ7cpsqqBFAR2dLAsH5gUadwas5sQM54arpWPEujU5nCc9_FG6ULo8V-It1_FN1ZdfayvoT-lfZBYfWsg8wmf4UdkbDhQOPJVFuEETHvq4gJrSGdRiydY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=WwJLGKXtGC9-xFYc7GxPmSwN8kpsI3gyZKMhs7MEES-HxWJv04J7r0oVfQwwfoiHM5K6bdSsT9bFT_LY8E_pu6Pdr-dLQdLA5SVCAAOBcNVhfoXUZ1XO4Btbcx_my32k1VcBmtHNuJXcx-RwB5frU9GTj0gLseM3k389YAitW2DL68CPppfqipUT_eHOTo3uLFA-JAn_QE0G9ZdVH73iSmA0hXu0RnLq_ZE0VFzGYFowQ1vlkAjWQCq7huhA5-uH9Vn13a3a6kveIo743jAHEnAivURj4MbNqi-f7GcdMAdrJ9DUSDpqnM0wmE3VAwn1bHFaRsqIIVKFY5V3ORVLwKu_ThUVRGmw6Q82yUHKpKbH5jcCqMfvq5eimQ-dJjYROna45Cc-s_ou0OYtitv0YacEeh2gmKznb7tvdas39NHg8_oICJh6uQA_AKKFSgERuK-ZaMCOyB1buPvg9KLjP82GekRfUgTXtqnScbPadWQHKo3hcs-EPELyVb85EDWyDku3oLekSNnfEjPqx5KEmORmjanFAg06jqwI23N5tl-aY1K6Kx558aLZ7cpsqqBFAR2dLAsH5gUadwas5sQM54arpWPEujU5nCc9_FG6ULo8V-It1_FN1ZdfayvoT-lfZBYfWsg8wmf4UdkbDhQOPJVFuEETHvq4gJrSGdRiydY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر رهبر شهید انقلاب اسلامی در نزدیکی وادی‌السلام و حرم حضرت امیرالمومنین علیه‌السلام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668353" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03d027047.mp4?token=cNxeltHiOeqt1P7vQD2mSqC02iUZgwvpd4UomiKkZIpc98_2IYPSdNphH4eKknNSZrG1YnKw-Hghi88PCxbJUrRAI_5jquLzwkN1eSpAziHcRKHWgNEHYW4YmIpLY79KoIHCNrTwxlcN9Zy2X3XNvzJKBwUrrXovCAL8HhEro6jIyCXGWQsydUp41wTdPn1GP5Oq9ViCMp8xkgeg08C7BEfPJkL9J5t0vDG9R5vfu1RktP-8d-2JtvsNFfHgxTH7PIMR284M0HShbaEFwljDuf6uatj8HkCSin0CGHhRYJkZZreR89Ip7CFmcrC7Y2v_2z2xYP44oMqK7PFAL_D7SlvzGjEALJ3Xmi3PnLpwGiKqpg1onVC4W_w5pL3-UAwHC0uuOsN_u4Ajx71ANnFFOWjwHk0axHRZJ6G8suBUGE3bKBflZcI_7lh5MrvsXOLrHDz-khQBes0CfP6bOvwmzfkIsZYMhce2HJ_teOJR3OVOz6Be1ZxS3kFslLvwJOWRXZ9me4085d7JUbG-Dks9HBDmdHKW0HcBsZhsXApbQUfGScc1uQBPATvYpcrffrD5s34EjgVfhTIFIBQd_O05xwS2P_OPfcOXoaEB2cydMRJchhKJ0YM39tPmRcvYYJJD4ejUgq09qtaaYoJLDAOx1b-TIKfygrTxgZHe0rzjnQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03d027047.mp4?token=cNxeltHiOeqt1P7vQD2mSqC02iUZgwvpd4UomiKkZIpc98_2IYPSdNphH4eKknNSZrG1YnKw-Hghi88PCxbJUrRAI_5jquLzwkN1eSpAziHcRKHWgNEHYW4YmIpLY79KoIHCNrTwxlcN9Zy2X3XNvzJKBwUrrXovCAL8HhEro6jIyCXGWQsydUp41wTdPn1GP5Oq9ViCMp8xkgeg08C7BEfPJkL9J5t0vDG9R5vfu1RktP-8d-2JtvsNFfHgxTH7PIMR284M0HShbaEFwljDuf6uatj8HkCSin0CGHhRYJkZZreR89Ip7CFmcrC7Y2v_2z2xYP44oMqK7PFAL_D7SlvzGjEALJ3Xmi3PnLpwGiKqpg1onVC4W_w5pL3-UAwHC0uuOsN_u4Ajx71ANnFFOWjwHk0axHRZJ6G8suBUGE3bKBflZcI_7lh5MrvsXOLrHDz-khQBes0CfP6bOvwmzfkIsZYMhce2HJ_teOJR3OVOz6Be1ZxS3kFslLvwJOWRXZ9me4085d7JUbG-Dks9HBDmdHKW0HcBsZhsXApbQUfGScc1uQBPATvYpcrffrD5s34EjgVfhTIFIBQd_O05xwS2P_OPfcOXoaEB2cydMRJchhKJ0YM39tPmRcvYYJJD4ejUgq09qtaaYoJLDAOx1b-TIKfygrTxgZHe0rzjnQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیده زهرا حدادعادل: من سال‌هاست که آرزوی زیارت امام حسین(ع) را دارم
🔹
امروز کربلا میزبان رهبر شهید و شهدای خانواده ایشان است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668352" target="_blank">📅 11:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668350">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
شهادت یک نفر در پی حمله آمریکا به خوزستان
🔹
معاون امنیتی استانداری خوزستان از هدف قرار گرفتن سه نقطه در بندرماهشهر، بندرامام و حمیدیه توسط پرتابه‌های آمریکایی خبر داد که منجر به شهادت یک نفر و مجروح شدن دو تن شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668350" target="_blank">📅 11:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668349">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b63329ee3.mp4?token=hMnZi9A4fGlTAfEKe-oIAbxEJtRxahEHwYIRtms9hgQgbYID2rgJtdkwzTO3EizsZJpDfGdwECeUyAt2ewXtdTEljpxjCzVOlabopkwIpm4R9bfRAw1v__cKXfdDup3ftrfWSky8nTLWIrLNK9uINlqql1_CVQJwFaM-yR3j0SnCIbcsMIMblwuh9DBecOkfwFiIAhDs4vJoVCeHzh-jWBe1B0zZ7aVIIWT4dcFBDxiz3npHTdViodqGFmKRYaUffiSm91yjMYxb1RIvvotTDdN9psSDZE48yPLo0E2xe1icAk5TeFdveIEZhzEzeUjpJNZhgGC1S8QUPaYW7SFcrlEP7D7-CqFg9Snl63Kh7R6ODEHOwEh3NFiRovJVjbKBpdZ8d-fK16wdTpP8bLCDKNcitdsz1KtbMwSutoLmJ0PQ3BnKfy-pzmhlWw3jmaacuslg1nj8OIfe5vaplpsf0y5MOVMmmHMq4XkiudT8C4IV_c5we1bVfXEkxfXBLSvUmP1iFNSgUTZrrQoDO9rWhjed7a86DoK-Zzzz09_SR_aUQyF6uSanlyZ-wRph9QRgG91j5iAcHkIuwhq7Iae52zMYd1Z3vpaavcQq6M-wDPEewU2HKBlmrpy2KSfHwRX88cbPSn-XaBZRKOJvBhFUYM7EOJaV-wvadiliVuutwbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b63329ee3.mp4?token=hMnZi9A4fGlTAfEKe-oIAbxEJtRxahEHwYIRtms9hgQgbYID2rgJtdkwzTO3EizsZJpDfGdwECeUyAt2ewXtdTEljpxjCzVOlabopkwIpm4R9bfRAw1v__cKXfdDup3ftrfWSky8nTLWIrLNK9uINlqql1_CVQJwFaM-yR3j0SnCIbcsMIMblwuh9DBecOkfwFiIAhDs4vJoVCeHzh-jWBe1B0zZ7aVIIWT4dcFBDxiz3npHTdViodqGFmKRYaUffiSm91yjMYxb1RIvvotTDdN9psSDZE48yPLo0E2xe1icAk5TeFdveIEZhzEzeUjpJNZhgGC1S8QUPaYW7SFcrlEP7D7-CqFg9Snl63Kh7R6ODEHOwEh3NFiRovJVjbKBpdZ8d-fK16wdTpP8bLCDKNcitdsz1KtbMwSutoLmJ0PQ3BnKfy-pzmhlWw3jmaacuslg1nj8OIfe5vaplpsf0y5MOVMmmHMq4XkiudT8C4IV_c5we1bVfXEkxfXBLSvUmP1iFNSgUTZrrQoDO9rWhjed7a86DoK-Zzzz09_SR_aUQyF6uSanlyZ-wRph9QRgG91j5iAcHkIuwhq7Iae52zMYd1Z3vpaavcQq6M-wDPEewU2HKBlmrpy2KSfHwRX88cbPSn-XaBZRKOJvBhFUYM7EOJaV-wvadiliVuutwbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های سوگوارانِ عراقی در بین‌الحرمین؛ لحظه‌یِ ورودِ پیکرهای مطهرِ شهدای خانواده «امامِ شهیدِ انقلاب» به حرم حضرت ابوالفضل العباس (علیه‌السلام)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668349" target="_blank">📅 11:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668348">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVWaUiW93cflstsRI3tU5Yiyks0itBocXzqGVnH8eWBoigpXao8CXwqv4hFcjZ1N0qRUQjxwLSCmcxViNk67T3cpYstNgsphFofFNmSZozGXCW29Qz_K5EEqorIMjbdBLXpwBdX_jzRu34jZoN5FcV7ftQFyjQM2-EbZdEmP2MchDVNq-m7-D9Fn9_m4UZCcBepOTRv8DuD7hq7sr6FJtxEVrtQITngh_zb6uZeBZ6G1HR9C2_wnv1hT_dA73YKbMDw94XeJctGIXPW0yTY75DBwRjG_YptZF11tqiY8duZbgfscg1uWx7XjHiTQR8h-5B-I4EOZBCOucYlWWYPtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر نوهٔ رهبر شهید بر دستان عزاداران عراقی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/668348" target="_blank">📅 11:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668347">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📢
فوری | شهرداری مشهد یک دستیار هوشمند برای مراسم «آقای شهید ایران» راه‌اندازی کرد
🔹
در صورتیکه در مراسم وداع و تشییع رهبر شهید شرکت میکنید، شهرداری مشهد یک راه‌حل ساده برای شما دارد.
🔹
شهرداری مشهد یک «بازوی هوشمند خدمات» را در پیام‌رسان «بله» فعال کرده تا زائران و شهروندان بدون سردرگمی، خدمات موردنیازشان را پیدا کنند.
🔸
این دستیار هوشمند چه خدماتی دارد؟
✅
مسیرهای ورود به شهر و نقشه‌های ترافیکی
✅
مسیرهای جایگزین و آخرین وضعیت معابر
✅
راهنمای پارکینگ‌های اختصاصی مراسم
✅
خطوط اتوبوسرانی و حمل‌ونقل عمومی
✅
مسیرهای دسترسی از مبادی ورودی و شهرستان‌های اطراف
✅
محل‌های اسکان پیش‌بینی‌شده برای زائران
✅
مراکز توزیع ارزاق عمومی
✅
سرویس‌های بهداشتی
✅
نانوایی‌های فعال نزدیک به محل مراسم
🔸
چطور وارد این بازو شویم؟
1️⃣
اسکن رمزینه (QR Code) روی بنرهای سطح شهر و روزنامه‌ها
2️⃣
ورود از طریق لینک‌های منتشرشده در فضای مجازی
3️⃣
جستجوی عبارت «بازو وداع» در پیام‌رسان «بله»
🔹
این سامانه با هدف کاهش سردرگمی، مدیریت سفرهای درون‌شهری و دسترسی سریع به اطلاعات، همه خدمات را یکجا در اختیار شما قرار می‌دهد.
📎
لینک دسترسی مستقیم به بازو:
https://ble.ir/MashhadTrafficBot
🇮🇷
روابط عمومی شهرداری مشهد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668347" target="_blank">📅 11:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5jduUErMcwsxq8lNFp2Cz9bd9YP5OwOocRCjQUts52dy8WcY61edk9jnDvJAvFg7qo4I_eBFgDEiYsW4JG2h2KJYzsf-Zsk9rctiCaNYzSJP3lioBI2blUd33x3J8XBwiO50TaeB5TOPZCXzL6hlts5ctnCZGPgFspM8IJUYgTko9H-yz5YSE4v41VtLTHmrR0oIJrfYYp4b9ri_ZJEe6hQbEDjLhpqcMwzh5TNbwuUqEN2SLOKpibT99GHgTxIyLHOI2ttfUfnpj7iKmmbpwiVJJPff7oW4i1c6LTHW3y5hCbuxo7KBNCaWIZsI0rc5F7ifwrowYN2Hc2TshRicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
آمادگی کامل سازمان ساماندهی مشاغل شهری برای خدمت‌رسانی در مراسم تشییع رهبر شهید انقلاب
*هم‌زمان با برگزاری آیین تشییع، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد با بسیج ظرفیت‌های خود، خدمات گسترده‌ای را برای رفاه زائران و مجاوران تدارک دیده است؛ از جمله اختصاص ۶۸ بنر اطلاع‌رسانی، فعالیت شبانه‌روزی ۸ نانوایی اطراف حرم، استقرار ۶ جایگاه عرضه ارزاق عمومی در حریم رضوی، فعالیت ۷ جایگاه ارزاق در مسیر تشییع، خدمت‌رسانی ۱۴ فروشگاه شهرما، افزایش ساعات فعالیت ۱۸ بازار میوه و تره‌بار، فعالیت ۱۲ جایگاه عرضه میوه و تره‌بار تا ساعت ۲۳ و عرضه نان بسته‌بندی در ۵۰ کیوسک نان قدس رضوی.*
روابط عمومی سازمان اعلام کرد تمامی این خدمات با هدف تسهیل دسترسی شهروندان و زائران به کالاهای اساسی و رفاه حال سوگواران تا پایان مراسم ادامه خواهد داشت.
#باید_برخاست
#رهبر_شهید
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668346" target="_blank">📅 11:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6669419bce.mp4?token=VqFBIY5K891oHrd4Zb0Uc_0UFlxjWiMBj3E8-ndXkiufR9SJwRRRqshOXA9fUSfoNcwhFdd_h848SNJJnQ-KI3ENKpU5_7aODVsRGrfq-UZC-Dwnj_tqtSmLkO93SMIIxyNd7ufTT4JwYcTcXaNVTZb71tdmL1uVYaStcmc_UCcI_tyYpGZSdZmZy4GPnf50DHzIun4Yc0LxAz7i0E1QOa5-NQkrvC_vxN-EYd-DK3Dkjv05o9_ONpw1hDoDvDE7cB6q80UJ84yJTpj1R1uSgEwubF7lDY-d2qAQtMfuhPwS6pNNlMU5lQj6QOtGa-fDrAm8Y3E8qTFF-uQlVwWKUWOO1nf3x3YsU-h6tigFRnYJxgVhWfTL0WGA4tTswc7ECf4Q9TX6FkwrXMzeq3jv1mLNwlinFyPl7CJmnKRxGQ7e4AlnPqEsNlla1mwyuB2qckiCU3AVHKr455gE5m6yy2jI0gWr52GLd5zphpMchgL8zLoAGHRw-llsOkMha5D8Qua8xyMl06wmziI6P4vGJJIImHIbQwPE0IsdUWJ6jxVkS2QxmVtdgcsam-DOSFFjdm8TB-5RN3V-Y5deNaWYvwteONGi3Gyyl7orWnKmJaQhwf7TosBAEHtork54j3nWjyyQO5bdGjGgsq8hrSw0mYsqchy0WOavVGaMWj8ioQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6669419bce.mp4?token=VqFBIY5K891oHrd4Zb0Uc_0UFlxjWiMBj3E8-ndXkiufR9SJwRRRqshOXA9fUSfoNcwhFdd_h848SNJJnQ-KI3ENKpU5_7aODVsRGrfq-UZC-Dwnj_tqtSmLkO93SMIIxyNd7ufTT4JwYcTcXaNVTZb71tdmL1uVYaStcmc_UCcI_tyYpGZSdZmZy4GPnf50DHzIun4Yc0LxAz7i0E1QOa5-NQkrvC_vxN-EYd-DK3Dkjv05o9_ONpw1hDoDvDE7cB6q80UJ84yJTpj1R1uSgEwubF7lDY-d2qAQtMfuhPwS6pNNlMU5lQj6QOtGa-fDrAm8Y3E8qTFF-uQlVwWKUWOO1nf3x3YsU-h6tigFRnYJxgVhWfTL0WGA4tTswc7ECf4Q9TX6FkwrXMzeq3jv1mLNwlinFyPl7CJmnKRxGQ7e4AlnPqEsNlla1mwyuB2qckiCU3AVHKr455gE5m6yy2jI0gWr52GLd5zphpMchgL8zLoAGHRw-llsOkMha5D8Qua8xyMl06wmziI6P4vGJJIImHIbQwPE0IsdUWJ6jxVkS2QxmVtdgcsam-DOSFFjdm8TB-5RN3V-Y5deNaWYvwteONGi3Gyyl7orWnKmJaQhwf7TosBAEHtork54j3nWjyyQO5bdGjGgsq8hrSw0mYsqchy0WOavVGaMWj8ioQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع باشکوه رهبر شهید مسلمانان جهان، حضرت آیت الله العظمی امام خامنه‌ای، در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/668343" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668341">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
لحظه رسیدن پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب به کنار ضریح امام حسین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/668341" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee3060ce4.mp4?token=FaujJAykEovnCFTRNcIFEdTPZfvWnxxwanLIL6QgklLKJbDJEEl5fv29dmFX2RMPGJkJKFjsEBNZ9XzMSSFjBrWXmnTdGiWEXZlwLl_hYXmDZRLzTLXIvhYKiuOwznF1vVmkF5tFpfEgvwVL3VW2mz8UeBaz8Q_mc9KgXhGRo82WcfZVcW3u_4_mj9_a2J34m8IzPZFd8VVu2un_mAknPHTMvv1Wz1pav15sH4CoBwHombvbvQKo4v_Fl-GRsPKQwfEEHas2A44ily5iE_lZIoh5K2653rt-0eQrYCkEwOep_FNItZZfulrLEXAcXqdZAzVcTzx2eaQDRQkO7DPEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee3060ce4.mp4?token=FaujJAykEovnCFTRNcIFEdTPZfvWnxxwanLIL6QgklLKJbDJEEl5fv29dmFX2RMPGJkJKFjsEBNZ9XzMSSFjBrWXmnTdGiWEXZlwLl_hYXmDZRLzTLXIvhYKiuOwznF1vVmkF5tFpfEgvwVL3VW2mz8UeBaz8Q_mc9KgXhGRo82WcfZVcW3u_4_mj9_a2J34m8IzPZFd8VVu2un_mAknPHTMvv1Wz1pav15sH4CoBwHombvbvQKo4v_Fl-GRsPKQwfEEHas2A44ily5iE_lZIoh5K2653rt-0eQrYCkEwOep_FNItZZfulrLEXAcXqdZAzVcTzx2eaQDRQkO7DPEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود آیت‌الله سیدمصطفی خامنه‌ای، فرزند ارشد رهبر شهید بدون عمامه به منظور احترام و تعزیت به حرم سیدالشهدا (علیه‌السلام)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668340" target="_blank">📅 11:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8c11fc5b.mp4?token=s-wbyq8ZU1SSu1MtChHTxVIKouYFPK5Kpz2YZI5StsQUeOlSyPxru-nxDEvBnlgl3vY-Nffk7yrE9laWBDrOUC8RuA71tIZkSKtmRKKUuzy0cv147di7WxNeeU5X927bIRekXegeoYBNtUoIjBWmme0fHO-2Lv_JYPgRHepCxIhtKLPjT7pwUMA0dQvAdSyaV3mlo3zFzdQlIAuFxieuyGRhvMovfaAkF8P-SIQ5Xc7IkBGUvTXrkFDrN93RdDiVi1QB6RGa8mM0hNtEQf6nLcvKB_Vfq5p8bSgNpovijMgR1bmFSTmPAYY-Pc_tcHLVnse7pr1YN8epgdU7fYM-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8c11fc5b.mp4?token=s-wbyq8ZU1SSu1MtChHTxVIKouYFPK5Kpz2YZI5StsQUeOlSyPxru-nxDEvBnlgl3vY-Nffk7yrE9laWBDrOUC8RuA71tIZkSKtmRKKUuzy0cv147di7WxNeeU5X927bIRekXegeoYBNtUoIjBWmme0fHO-2Lv_JYPgRHepCxIhtKLPjT7pwUMA0dQvAdSyaV3mlo3zFzdQlIAuFxieuyGRhvMovfaAkF8P-SIQ5Xc7IkBGUvTXrkFDrN93RdDiVi1QB6RGa8mM0hNtEQf6nLcvKB_Vfq5p8bSgNpovijMgR1bmFSTmPAYY-Pc_tcHLVnse7pr1YN8epgdU7fYM-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزله و شعار مرگ بر آمریکا توسط عزاداران رهبر شهید در عراق/ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/668337" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
مرقد رهبر شهید با نظر رهبری معظم در مسیر زیارت زائران خواهد بود
تولیت آستان قدس رضوی:
🔹
رهبر معظم انقلاب فرمودند که مرقد شریف رهبر شهید انقلاب را در مسیر زیارت قرار دهید تا زائران در مسیر تشرف برای ایشان ذکر دعا و فاتحه داشته باشند.
🔹
ایشان با پیشنهاد فضایی مشابه مرقد مرحوم شیخ بهایی موافقت نفرمودند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/668335" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بوشهر
🔹
صدای چند انفجار در شهر بوشهر و مناطق پیرامونی شهر شنیده شد.
🔹
اخباری مبنی بر حمله به جزیره خارگ نیز منتشر شده که منابع آگاه مستقر در جزیره، این اخبار را تکذیب می‌کند./ مهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668334" target="_blank">📅 10:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CobVvmmisJ6m--IaF9iHgAx-y3sTDgpbHujBDems4mBUhmNk1DPa25pw36SsxDnbueNt6You-CigoxsNyH7yPF-6hRxSVlNTi_kWpSh9l2ep7IzY1TrIxS-GGX0vFoJnZPPA2Cn9c_wrt5D7zFHFEA8_-DPFdwsWxVdd8cOZwdUQ00REThtBkTKYEJDitrm3thHPMhqXbbqwbEs20_aOK9t6m1iR6rjEf-ndgRP4y1D1im6Ra5M2GUKcGi2-Hbwluh8PkyZW7NhIz1qQ1MgwIksQMLFUA1ViU4f2T2evCzsyp3coeqhJDukVG5_K6ALb4tXMAfbpLKN0-vcZTF1knA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2rqytgyBXapvOuZKA-fmcOaiEKx7ZxJIM6G3ziNMX4CDhLAv9UqcPMrWRlsPDDzcv5mHaT46zAzt9c5gplvdz9-9eePbk9ySqxPf2SfJhwNfbTBAdYIGiDRcMJ9T3URs6qGpn4RF-gzG1sfMPNb51Kg423Wzy2pS9xrVBdn0a4i6Q5wC34SAZ3VjKSvxmIZte6TT3H3bNnuC17BppBLqQh4Y1aOV-JGpOID9flh76AgGWKBkbOB0XSd0mBRmqnL9V2JRbydBnvFg1FY-grjGTGl_g6YQapUqxOwphin0WLwUKjFJet8h8s8zQfsQR0aPvLnLW4BOrl-PSZoMYlszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRF4ndwPbSQdYt5VKh1Mz1Z4JNsgccF7VPXzmhnTCLU4BqOx2KgIvG4_dKfbYr7GKb26Mvr9O9MzEAdW43dSeWePPB-M779MFFDEtmKrgVAP7Bo2fcCQPpfd_eJhQT0XSl4YtRQxpyzwjVI8-hszfDHq9GRqgKy4bpT2XsqKnoUL-0OO7M2GeoQr8XOUEH9-iViV2-zhy5F5mppJwPs7rP5ro-MHFzEZGfcPyNIwVVJgm1q3ZdQLaIY6zssTsvly-TZLCT8EdxrMoNLPARzlCF857_r746Mv_yKPWvOSBTX_vZ2ahd2R4FvUtFAtEUfsTeECMPw6aiCgmjm6R5eAjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از تراکم جمعیت حاضر در میدان ثورةالعشرین نجف اشرف در تشییع پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668329" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
زمان آغاز مراسم تشییع رهبر شهید وابسته به زمان انتقال پیکر‌های مطهر از عراق به مشهد است
استاندار خراسان رضوی:
🔹
در صورت رسیدن پیکر‌ها در روز چهارشنبه، مراسم تشییع ساعت ۶ صبح در خیابان امام رضا (ع)ی مشهد آغاز خواهد شد.
🔹
پیش‌بینی ما این است که مراسم تشییع در مسیر خیابان امام رضا (ع) بین پنج تا شش ساعت ادامه داشته باشد و مراسم طواف و تدفین در غروب پنجشنبه انجام می‌شود.
🔹
تصمیم بر این است که درهای حرم بسته نشود البته طبیعی است که درهای رواق‌ها و بخش مرکزی حرم در هنگام تدفین بسته باشد و  ساعات بسیار کمی بخش مرکزی حرم و روضه منوره بسته خواهد بود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668326" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شهادت یکی از پاسداران منطقه سوم دریایی سپاه در پی تجاوز دشمن صهیونیستی به ماهشهر
روابط عمومی منطقه سوم دریایی سپاه پاسداران امام حسین (ع) بندرماهشهر:
🔹
صبح امروز چهارشنبه ۱۷ تیرماه، در پی تجاوز نیروهای تروریستی آمریکا به منطقه سوم دریایی ماهشهر، پاسدار «محمدرضا خزینی» در حین مقابله با پهپادهای دشمن و بر اثر اصابت ترکش پرتابه به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668323" target="_blank">📅 10:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3295ff058d.mp4?token=sgcal03NTlOdBgwWYBXCyzkq-W0Hvcown0oe27MKAs7SilXbAXGfXm25DceWlyuZ3M4fKw-ioT2j0016L2XXsn1AdWZyqLQfFDZHf1WG-vLGINH6wZGktaVHDuefVI-cJzW9uUxvdkWwnINoRSlmfbimBvNyXMX84q1cdSfxLH7_d654AeY--8hA61b7gfDye0H3RvJA2QJKsM_D6iAHvM9mm56QeDRweclX3NI7tk90A-9pYSd5Xtuq2Kw2JT0jyRCl57Th3zYdNSJ6OZbI-nxDjDes8oRmyU0fxxoFZHVMXVZ1q6Lbrf7M6c6MjoB1ZQxQoAdCBDNsE5JYE3wZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3295ff058d.mp4?token=sgcal03NTlOdBgwWYBXCyzkq-W0Hvcown0oe27MKAs7SilXbAXGfXm25DceWlyuZ3M4fKw-ioT2j0016L2XXsn1AdWZyqLQfFDZHf1WG-vLGINH6wZGktaVHDuefVI-cJzW9uUxvdkWwnINoRSlmfbimBvNyXMX84q1cdSfxLH7_d654AeY--8hA61b7gfDye0H3RvJA2QJKsM_D6iAHvM9mm56QeDRweclX3NI7tk90A-9pYSd5Xtuq2Kw2JT0jyRCl57Th3zYdNSJ6OZbI-nxDjDes8oRmyU0fxxoFZHVMXVZ1q6Lbrf7M6c6MjoB1ZQxQoAdCBDNsE5JYE3wZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از حضور پرشور عراقی‌ها برای استقبال از امام شهید/ ندای لبیک یا سیدعلی در حرم حضرت ابوالفضل(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668319" target="_blank">📅 10:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS3JdDvabxioK6BC1IU_Apo3qiHywNyFFuj6pdJ7o8Wm2apR0rQuMWESqCygyuPVNgPytOVBf4Zwv5cTjn6lAUzqAXYwpeom0oNJgFQ8PMkcDDSCvdBy2sOxtsSrTHwNa4lwLSmAdAOkgOarbdOjSRT2Qqzq5xDEeIqhX2XvrM5yBqHq8Xe35DsPUa1Mu5aRUIfBVwOlJi59GC2Ca9Z42GCVF0CgEpOZe-lQlHH4NDrsfOpQ62QzvxliphFDYlmCTyPiGn5uCXhQqB0yC0a4iT_RQeL2oZ4GyJfmi3Pzb5Lq6OmZqCioS5VM_El83a4IMslmdmju7Lq0EoZ8abbFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
۸ نانوایی منتخب اطراف حرم مطهر رضوی در ایام تشییع شهید رهبر به‌صورت ۲۴ ساعته فعال هستند و نان گرم را در تمام ساعات شبانه‌روز در اختیار زائران و سوگواران قرار می‌دهند.
📍
محدوده: اطراف حرم مطهر امام رضا (ع)
🕒
زمان فعالیت: شبانه‌روزی (۲۴ ساعته) در ایام تشییع
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668318" target="_blank">📅 10:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa6L1SfwlWb4cZ28IinscVr_p52m-8YjScYd5jaZSTGoS6jIqjLIxMmir4s41oy6RU0Q_ww0RDRAuj1Y-ocBMhTzWNJnAHu-n3fgxoGlP9F5RcrIpD1tcsjg8hiMY_jeGNd3J9qgBeoJDl-dpDbC7y-Qz2ktK_INvayymlQlcmMLXK_kSMS62NRA3tSbHu33Mahw9RdnLZCxqucR-NMMMYRQDfSDhjQpyS39eZeQW8fhBqO6w-pix7MLTdBzP974afax2EN4iZz0ClOp2P0s6peMlqcITWQ-h0TRn-LRmLlydJ7G-gNFXN7307Mi4-iYHgv9Lomxisxr6iXIxiIt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره حملات تجاوزکارانه آمریکا و نقض فاحش يادداشت تفاهم خاتمه جنگ
🔹
آمریکا بامداد ۱۷ تیر با نقض منشور و تفاهم خاتمه جنگ، به تأسیسات جنوب ایران حمله کرد.
🔹
لغو مجوز نفت ایران و حملات اسرائیل، تفاهم را بی‌اثر کرد؛ مسئولیت با آمریکاست.
🔹
ایران به همسایگان در مورد همکاری با متجاوز هشدار داد.
🔹
ایران حمله را محکوم کرده و بر اساس حق دفاع مشروع، مبدأ تجاوز را هدف قرار خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668317" target="_blank">📅 10:15 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

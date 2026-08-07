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
<img src="https://cdn1.telesco.pe/file/HI6F6IYxNpaOKj4ubYDULz9EitsUBImKchNvMHSkAnqkHwXY9Db3BsnsOVbjvd8pc0SQ7yLlUMCvaWeKIUwb3kSXCQ_zuiRS_qusbGoZj4y1mvCG8oEPHYnd6y8vgJUK58kgH2c22csOH2a7JnY2XX-TJ00C3XbD9CdhYSy56u__0zABYb2ifUPpj9KhZJzbdiXH-W7n6i-_RsWx-IQe_7ogaz92y7HDEC0Un4W511GEq2QOsmvCbGj1jHLhdulUwJ2B0iYXEOcbuE-2dcHx0-fY1ygPdKIkvy47jkPYfxGAB7OWAohRcBlZqvzr2S-6wby6NXWGDf9t9zLmJRqJzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 20:12:26</div>
<hr>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A279OVn37hr9a912keblF_XW6ftHCLnYKtf97KWC6BYu9Za2mIOJ69184iyDR5oJIa6qXL9sAOj6oaccdD1XGXpMA16SOFVoZl5vgyH9KBxRh87rAk0MvaJQiJ1Qi0t-tD0owFKwoA39RY78HB_0sdcjVBsFvRy_j1YsvH-jvLY4sYPgrd1xkTDbRvwcNyKzVX8RWNn1pLC8zKaVL-dpYU5yrcetN9ZShxLfzSA46D4M_6pLFOFylw60AjbhZuJa7P5i-0FFkR-IeytRuZvtupP8ahbzcp3yxxGKjymz1L_ym3foFNQzHAkALFW0GnAXrAx6hGIOUsp29_8CR7C96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVRpgRuiAq-sFvFBdmZJ1w2mLiE1_0D9q_xE3V8PhDmtQsvv0fZ9EOcWQ7_25BEu1LyEi9Vxbns1MmbYOPHdHI6VAtuMxqAxnE92wWs2cCoDVZRvT0w_1QXtIRm3NaKSGFF9qlC1a8Xl791B_XhaTJpbd1XkRXEHCJXtIo_ElbsBeM0pXM51t-YlE8T5U3T1TR8bqLbzi7fCtZ2G20rhWOtPQqqcDt9Lz_ZM2Yc1XwKKjwZu8Qlb_9fOFqGfOoweILglKB5R9a3NZKgNowx-MUMO2P95tZrGSicSmxKtSrpyvhwP-eS4l3WH59QrEqvCTSGVGfuB1IuwG7D8U5RkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GK3KYhy0deeBaD0STSuIl7EITF1ZCWJpU9wOG-VQvzPQdMcwSjQtyYbXN-RW-gpD2uCiWWspOp81xAB5OlJYVdnap82sUms-t5GHfs0RNd-xkgnKQksYj6FLAskbjJpJ2mnd_xrdEAC4_JUuxulvYVi3iYHmUrHuIka3gQZugiC-Uk3uU6dHRdR10d6QXCcUdqXg2sKwT5FN2ZA3dyUnFwfx_UAlC6ydoiytZS7AGfGNOa2m6JFCzJ_MrQrDstFsAP06v5vrcc_2zoBZ0QKTdPCf8pz4AE-pZuwdHyxXQdIo6hRGDeVg7rLoNdZDyUHZPaj8aV_1Kb1v9hJNKRyWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jdk8WjW2mLfQgc1_RwAmhrng1NVLkDxqVwuPajelw-SVmtj9u3AdQ92iIXPdpe795DMfyFuFWSm3YhLl9cfPG1Pmwd4QwldAiSgAp5eJQyVbkdSZiag99-6BiLvWRy_PCFDJ0bWBgVtR42VhVtzaeAjfWqENmRB2cocFUuwDdewTBdq3IGWe-O3B0ANUk7pPrt7kQVqgVxB6WjZAfTGF71QsWMeW_AJNSt1xwqIyPE7FBC8EihblAQ7zW8mSiTrqUpRH4aHvMYjJNUT8ib5Upc-3-UdT0yBl0PyNUizb2JDu-u-FhodR_GlPocgY2_FkSRWgLmRVkJ2t12F9X6-Xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTI_FiCVWqWbQHnH6cSAv_h4x5lde4Oyhd6zEK8E-7DtcIvlnbjTTuPSWdL4Mwa8njGC9vYxpfAFEJ7nisLi6qSsZu5UU4LJX_t1FXQRGYmIGUrgREa0CbvQ0F08zWvF1jqq1LA0i7oHQ4l5sCImJ4mYA5W0SLVv4QYku6mETxIVudvUvnKQyxvRkLsrjld30lQvuFZUxt-qtF-A8gMiXcbs9wXcpuJXlj7OVEjxgBAbzTGc21dUG6OHtqZEv65jFPKdaEc0y49kMWkrQwP1kkN4tG0nczv8P8VTMIhl6tirq4Jr8N_NcKOVeNNseiPA0Bi9AuA62VD6UgsiqC4Chw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjfpKmTL56O40h2wwPaIOlBeXy_JN_kvBmPf75iJHlDQzzzgQJhUHh2XUMUDZ3u5vL4PJMWRrmEotOpfzeN6eBy2YfDYWtjDG0VrMN0zUppAf-lKe2e-QWSodBneR-pwpO1pnRS-g63OViFj79v58_IVnS_h4TBPPovEAB88KZGGccIryuaQGfrJFDBGpNCId05-6mYntSs0LzD_OPB6ZNNyqzqFrN8iw7qIDn90pr4VOtgAlMXcWA2Ebk9T4CGBU9Xm2XLfn2Eox8xC_r5kBHfZJRJuw6V_ubWGS4bxEtGsZmCkQSYfmlHMjh8zrIRFqp_6ZdwHnVJsylXyxJJXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2w7bejT7DNp3PB7wTTBfoYl_WfNsAUpmdsngirX-7joADQna73ab65pv6qCi1-QrTKlNNKIury15zz2_zgSLaWn2WXhdb7vSUxvVvXyq_6CrXiUFLA6KBO1RlazZm-pCppAUyv0iDdmB36DBZp4Jg6CYYzfe6LaBekpnUAIyMX2SuadVikgfai9buEoKE53pZOw-ynVXC-U-kAag2W9B_ayD_Xp4F7jWNZw6YyYX7I2h50UAlny7FD2txQ8lfsYWUapwfyiYioWbIiv2R0TElVAfFtBLJq6-suanCc2e-kALO_OxULcVe8P6rlb9x2Y1OxQSBZGIOKaR-_5vCVKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BjbjKL7li4vU6TkClzQlPXkV38iOS1hHIPGWH6EdjMQJSzgAx9Lc2YJlv0ScCBPthpzd6XzBvwwaogk7utZFi49EUWKesnFd29IDVT38fEijSIn6ShF8dt_MFGI1Hdy2ZLpZX7XkeXLBugEjFzPjofqCLwBr2uaSHuapnc6PTGrALDWKthPoman88XSRpHN1kjtcMXyxMUh3HhumqrZDfJEyEXlis4O83WRGdB-WlhHFpbbo8-x4l_UUMfrNMU8V2mfuUhwwf1K4zcJcjep87HKa1oVU8dBZhXDwwtvSq4ov6Dvw381rk8P1NuXf9yKzcSIauUQiFlwsW8veRb5Fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ofgdUbcanDG_LObAAL2RfDHPHxy9M8xTYmrc-WsXbmEGeZEbKk2bEEyBYagNgov6-doP_GJ2Hf_DCdQ1qwldTK2YMHZqlkfvM7FSwrXgmAfuUKWuJ2OuRLhG8mVY6BBHY1qYNZCKqRxpuVYm_pkNZQsaSHVFDgRQOZKe4qbtsbohjEqpsii9HWiyrs5icL7cry1X14wtL_YR8bUKgpqcELcSDvOKchqZfYAwYfz1r5Dt346Z2lcKS-ydS4TjagdHcgOhx_OX2TJ9IV5tZsM56y1C0pFYWu0u8Hr-Yac-sIiE2GNRFG7leba23D40KJIsA4FYNQ14ThvRTQNhORDUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSXSwMSAOdMKvn5S4ZYw-g9igY9_Xps5-hUiZT-g-q5-GSjgrQjMWULH4p3b8YJNqR3gzX12O6VjWXnFZFRhI2ktEpU7QzreKVU0iedyNryEB8yDtq9vw7GsFRJP8Q16fah7rTDqj-kt8Vs6PvDTiVs451-hHpKfeAaTnXgKOQEj1xFme8eJrlCy9Av1cr85oUpzAiEvACTXTwbZqm5k063sMouvsMAu_BM4J-W3ODpPOq9-DpK73Yda5iGUWlFjRKwPrcrU72e5VtHHr_6is168ArUqZjhy5PtCoD0Alr00x2nh8ITBleosvH1O-OzTrACZzKeAbNLz9l_mHkzUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/saClK4WeqpBmsU7vtm4CiS_ki7_jR-eMiz-dE4KlEOtV4k_vEoU6lo47epwBMl7ILAaylkDdNRsF5M0Awp0PRQFQW0P6yZdsqPHrQfXTgPrqL-bSED4IcCniJKtMTCptqOm6yLv1460ceSm0VmRlSv5HX8AQ4Rh9rA07D2LLF0MuVap9ih2kMvKWWS6M202evBmnRPKCxC0RafMCENN1Pe_BWJaiEoG_eEq6EzG-Bwa6SaLzx5etHt6--Hae8ZYieAZeSrS3YW1EWBGyXHic6Er-j2gxpZESCZQlmLhQuq51F5RXMfWYTIDcVl6-wT5nNIewrPqaeHzfZUdbexe47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OON-PB44jjpB2Mkshh98_onqJRvBiAur8FXLeBEJodnLjdHQPi36xTQZCo059Ut5-B84rntUI0xRMLAB8GDsMR_HNN2c43J6TAt6ejB0Jpr-E07VdsxYCTUxpbpvzBWB4J7YQ-Mof3TRhhTiMgmfeOPpLd6Z9Q4sbg7SOyLAHp-gFfmOcuOkE7AlXkRp1LY0jPOcBMtK5tzd8AO39P4rpYnV02Q4SWLxk49NcFNRdwkyUUR686szJ5sS1aWCLRo0DanjDLQ45QDHx02Epvh3UmX9TURyVBJYMKpIJ_g6y2aVrz9w6U-xsvAJ37IvFxkgm9EMh4YZHfXztm95WUW4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzFKXmdgPA-0KM21IThMN1X40l61tLXkO5ntX_V_s58QtnG61S-wXoPpDmmfrp9d_s4F1brluaZhe3yrwWvCtDXZrUfP6fgN49n2IH1GmyckMchQIVUegaIuAnHL-FjVoD-BJAD0qzLciFyn8E-XZ_Fm0YlsYtbfcdL0DPtvDe_Z5WWByDAWMXW0oPv5HfytMpHLV6icBEEXfGSR3Hfao6pjWobnBU9qnbKQwMBcroLmq9YfVFf-RGCgjw-4kxUKuBkD7Yn6W16hb18dfeO2jLFAwZDa5vz7J9zY70evIUXCqll2t7Pf_tVUk2kp82ar7v1gg6QgdzaAAh7H_-RM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUZ3anr2uQzFzB0B9jx_BpclpxLWFg8zzbJxNGebYZxPvcYqRcb20-ugbrL74sQqm-yUjtKCyhr_06XlX5O3lQ6OTBjBvXyj6HZ4AQVYc7itSJjrko4NNfyQaiE-_4iNY0VvRs5NsGOJBW0gRopSlTK5I5dawd3XWAqhIH2dBVQzrtTx1z0faTP4Zae-GKsCo_npB4_-m5Bx6YGQeyh6wfmYk06m3o6HseB5AzVPbVyEw4kjH9mv4KlRRaVn-VrODPkCnsitcfXCTzZt8FwNxamgnljqtqD3W3oxFBtx90E-UJZYHpAd2cdVxUMZq0ekXOgJDKIed-hpBCuVGkyuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vxaTsujux4ezuWcdEgTe1Aa9aebtQH6txcTQn3YMprrWxPGo2VtcH9_a_8_oZblgRa59eoa3nPqbevayNdKBBAon1m7YzWHDDt1b2SxZowV19o0XzRUdYWMF69jRpE1vZXejDyr-Rw4dTLFMXs0h8icblWQzRq6MW5fyZ08kBfFVuS0uKCIcIcrup2efLYPf7kh4A9QDTm8Ox38d1e_bKVNKa9vdj-_fVBLWYYpryX-b3LA7hpf6ErE7nhgafXCJYle7yvcu3vhKuza-4zhvsjeHcpiiLME1Cg5CpdUgxScX9T_oum9jgCCSFQAICq6pj1U9cTH-f7aQFtETrqOj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkOgwgPWeF9-0n9wZZmgiFIVSdGRFj-21Zqb-Q-XqfzmJf4dM-wSNcOFhqq_5Modkk6xAhiIZYMlA7r7jMtrUaXJQti_esksLRTL3rW77gCWTxjHQ3CWqd6LPl30d_w6fwdin-9lOgi5hE8AG6xy0HEdxTN5OG-MRh15M3Rg-SBhnjg0fbJB-4D-e0WQC_HvrnwAYHFk_nD5bQ-x7ZB9Eog-XsZVGbvxkLruyuEud8dsa9WIsN0YpFukZelvOBeMvoJB8SZgc6xIW6ziTnUjMPLiENUbPHD0_D_idtip6739epyJ5RIm1eO39fW8u95MavakQt1MY6zMmQYsLHiU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvheV1rsYBfccYfK3IJh6AoNwyTSJ74BYTTpAX5JZRMpB1pOtX95pq3qYFoPSMYytN51-QV147035ZKtD6YIAswdPaQd_lVyRl96jTsIZN1mZZMSdDk3CTX9lZYAI4Cr7fANHCuUSUDimZhVjCW56wk2vhtHvGcZuGK8eMEnyw9D0Ul26D0TjoAWjgxsBY4vhlLSM50e1GCXyIf2d7zmaKwPVapDIHTrHRxe98XX049wSm53lUVzCuW9Bxtdx_bOniJaZ9bWOGKXw4n_4a-tNCWNfi60SEU82_s3MC7nno9s7EPOyTmdet5NNzfN8Y-00dVEO6sjl0vz4ocNTGmx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvZaVbnkk18QICSEwDN5KC3PK8_VeAS7bdk8kmIb7BNnROEHNfOYl7x1ONjifIFMogzpJztgKQU6rE-klg0qgHeoD71f9ozHyHRBhH-Ba8jCUVxyrPpsr6W2XzBE_4l23P6pg4wxv0HsiNUINsIgEzXXvJI5VzhFlXv2NGjWJp60fsw0CI8_nBKJXk72YHiR4QAvx-KkQAvaaQYAjfCP1sdU8f5eOR1Wt0tQrr_jYaXSSs00ynFGX2dZEBo2HtC16DhJjR7neVpleWMnmpURV-V4ECePWEGTnYkiYKGI3uAJo7wKr1ZpOR4ixB3F9iQSBBA2KZzsWLCgRZMAYDQjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cNNEivsQesHKRYOuruBB4QISmwhGkHZ_TFrj1NSSArVhhBg6FGx9xZs8eVHoz_d8K6tbreEjDKD1khkhca31_tc2D1t4OwpYhnqcrFOJNGgFeEOUZz3TR4dtAdXeJFTHWVsWkcSKZpMauw5aFagMavDskfyHnzrnskyvTS69MolvJbTHFEthOEyPKkAZW25tr8kziQZ5lm7u6nvfwrnzmzhx9tJ18gf-7AkFBFru5b13vBba-b8lX-V_dJkcHUvc6xFe87ZIqJ5TWDOJEICnCaDNikc9e_tRZBsB1Ux5KcG5H8cDaHs7LA27lJe8fBpli7WDXdutM5L1Coz49gUDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avfVHG2k03S6bkKatBj6qaWJd6Ow4A3tTY_h0dvnuzyGxO6mqBvLuiVjVGjsY0KYl5Nodgz6sHvRLgLoyBFUJNzuUollP2GEZ6WMK3MrElf_UtCKptHmRlzW-WBKr4t5pbIPdM4iDd4rlWQS15Hi8BhqS1SGPyHVjcbpQGI6GckYE7ZlsWnAEMXPCUeDnExFuIu2MYVfyYPd3UQN7zstJhZiSEl0okN98oTKNkSuyG6ywKXTuGCckHfVRc7fec29R06gDr_R0ADZEOtsyZOrUpYCmhfS0Z2kSox_OOTBzQnRqQaP3TPzxzBO-qn_cAIvxKz6TaxnOUKsZAMqp9tgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmed-eBhYMDTZ8J0wLDlX7sL16ThYd1XO-Zx3wfGSXXAhedVSl5rHDi8lkqIrw8ZZyaPWUHDXLMcknceDDDsQBmxNfGhupk31Fgn9i3mxI3ODHDoCds6B4q_Au60QXJgF_HWp0cL9kgskt27V342CrW-3PZdGZ0tphYgNIpWaHJ1GwHHZlUH4iQnD2Bp8pBW-_GCPjTgEiDbKCLK7L4GaMgsMchu6U0omphyN3zw3JGfu3aKehZ0deDzrri3PQvVaPGpyEOi0q6stvpSQVNZpqhYqqU7fdQ_EfLE3T26UjNeA9bKBMDROSIBREYw18Rp0-t-HxTY5WLqEEuEoDG86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJBFRp0Nc5rDm-UCifnP0FxwyY_qhk2u5-yGqB6_YefciMEcWWbWOz1PhCrZKCX6RSF6-nQMjYn_dYKLcGgj_cLxVBEYMA2hCtBC9iuJTvTJ8iwQlFfVzdbD534GVA4hs3aSaG7aLCx52IgncuHMspZb4SHcBvrFL7T3qaJrp6boddJNbgOZiZVfreAhJqDiWAlqSwanOfVGVSJPXG1YLfe9Z1iUyFlX72LZZGOb0YAomcL3-I01vARk5thOdYn_9qMkakmi0tGzZeE7BmutdIPvguIev9ZgM5Z2WcvNL8i1lpYJHgKkX5gF2vOQlajO99K4rkBdgWkr3D_bK8thbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kA9XwPuXdu0lldWipHkAE0ONoLmHZ3IU0Y_5Vqff_zvg-2TtKUudKORArlL97UX3DgvsYepvvepx6vcaepauuEN62dY1yaiNSZI938yeY6ibnhSGNI2fxGjrC-Npk1dFeAmq22sw3ANL8JKN4oaND93_4oilAIfAsB9XyJCSqUQlCoqvDh1qs533q5SEtXvthJusAbyGpB7G29xf2yH_DLXuiKi2XFfP6YLJmJkZmj7IMJOzP0N758K8TrYiojuxFBarBBEcMD2SIki_3OwrqEf6thH0dB2dOURQMqZAmaZUYDWDdJ8-AaDroMh35e8J1Y5OpquyegWH-6DkpIBf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M3HTejx5_sW4rNarGx1iXqi8c1orpPVAYUHv3VJCogdAxUywR1Fco3BCLm39oFrBeUXXL5nvmdvDF8DVBIszhJnxWFcYF1s26ocnBtuyl5QbKxTjIGBFoxO9pKv0SLrjS734zv1uZsy-6nBpmXYlICr6p--mdYWELM3CVESbHUB_MMpM8J7v8sp8Oa__CtqwhaSm_-3nETLd4OSgFJXQk41X5l4EpcCOcD9TfHBRD7_pcIChZ2ILk9o5mZGP7nTrAi_OsqcKRjc5fsPD3SD2Lc8bopp5W7VLLdcAjMi0qx9h_kGf9DoMVQoR3gSdTtmOAFn8a1nTNupPLUZYpxbgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OPyIDJeP8z35iLRmCb_P0jxVKa9pvl4mWycx2qSrSY3Is3SCx8JjUZaXb1PxClLsFZKcZ1BNkPrfjEmNSqaimQ-SWrhcaG3IuFaatM0k8xTv3Ekr1ocpmEnOR1jCTN_iMOTpMAlAkZRp3HUCo8KIiYN5K2KQozZ_uWpdRdyO2ImYVP8osTmZz3OfYo6DHyUxsP66XZWzQtANeFLkoxhc4yK8hHeADNhVBVXapI7NLcgRNlcohNkN78Qu-aosz5Nw4UhXvhvwOoUJ9eZxoSyqMfBH4HCF2U-zsV9pOehekVSqbaOhi3J1i8QhaAn5XseUjgVqethHrWMv6z_ZPnnlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T8eRe9oVapxvjDvOnen2iSTRjczDx55vjaSYfykOq4AGrT6gHBg1-0vjVMrS4pxrHrfFONfdK8iq_BNlrLhNN9A5E4ECp9UTWISTRVCfM6FtWUzLFNPbakM4ty2R6TMT9FwdK1cgqppSBE-Ux7O9G-2ykPFAEplwbeuoPpQWwr_xAazQMVS_e8aVMyO3qcNtas-wFBeWvOa4vjSjBJdQoXLIw2jzAvuSum-d7EOvWcnLd20yItUsTAatn8W9cvMbK-h1jaw-1qH9kAYLd40T72T6kVfSf5XORQdIXcaOFN0sc-PKbz437Fmvp6CymnPMYJ6hpcX_C0GFLDcx8C46MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7rE4vajrwCFCn6P0fUpscO4RyB9oDkLeDaB_Uwtp6qumTj0Sa8xZp1xdCJFAPH9qNEinRaQATJHQVSmy0JZVoSDlMGM43-XqHF8qrEc34pl9KDOo6zqRth6Q4d6u9ZPvp799ENz38Ty5Irbz2pteWIE4bWncOsU5-WbzIfAQnNnJIJZ-xARveLFO57qfrmY-JJ7rhXtnKCa-3iidnVN01ELWdA51dXxs6pjXT_DkvPQryKX-SyPoJdxkuYB2vBDBeoAy2Q_WLI9hbw06x6cqShz0-K6ThNHeYyvN--fxWqcNFO5NaGmKeOOXgO0OW5w-bmI7ep9y53L1sVWbtV--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3DDRV2Mfj8auYclSDv0GidkkuKHn8aIY39QMyVPgiqZ4k25YRMlPz9ZaT-YvucnHPkdfzHyUGMQSSsZu46tW0rwguC0yCgoYn0Y3FmnawV-SHxacrA-KOu1DEZ70X4jdArL0FbrILekiq90YSHgTVqBfL_U48M-Ia18V59zH5PSBciYfJKGFedNwaegIaiGZvT6FtabWtehO-Rasy4rVSOdmVZ9lx9mvTzXlhld3EzHVR03gyicmRsIXIE7dfad-byplBY4_5qOoY-jfW6Iak345RpVxhOz0bXb33ChJiqDEnJifMfeu8eRIyt-dd5k7EdKvKbb4AhCSeq62EfRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTZQljOd6lNUZhW_FGOJ8pmUxZhICNFPAVs1D2N0Z2ir-aWxi3bMhxxjhc_O9IrRALOgZYC690h0-TKrV3OQRfmmLAtenVq6LE_pqYrdZcK_7kF8bYeH2VRwYKpKHbd_7jz6UP1QyGnde9TiJ0c7IeXClVDI_B7VZfEa4CkL7X9Qk75VHHGGjelum_A2VcJkL-lpNK9Vm87J86Ig996-SS55EURrHXsPUt5TMGbDyfvNf-yIk0MJdMuPqejakh5ZxsyrIDVFhMP_k_JArPrDyWZl0wMLoHF9cRMHIlz0a5cyRcUFiv8R_1QRMjF5dXCEFN4NPXyZt2wCNoF6r3w6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBcU1Q_wdlMUnzW4eElMcYVP4XbezMJAkqsQqnPoRUwakN18qcY8Q-wY1Qv4NiwkQgY0F4onvIjsrG3t7AqK_fx8B-D5bV75kHrNMFORSpbHCacdGho-X0A5tuXezCTcW6nnndo4XLB4-vUiZFRJNRVDNzyPJqxGjMEz1XPOXKlFs8tlFtZ_SXUW-BvQD_rzgdIzHAUakHrWWLIdlEmQQcT5ncEYINiSjcqHJPPUkEP5MEIxDRPuVJIDeMfPrzjKIxJ_K73lG09KZksC6HsLtBnZo_FtiDSBaOnlGSmhrm_Ua0XNjDiPnj-z5Xu_oOjH6Q7Vl5-YUszknQkw7MC8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNpjO4JqZDEpF440TJ-KkF7l7UNSF8o-sdhjvTJAq5o-zsiYN9ApxqZ87yb6y2oGnds3eB0fu1QNDVBp0FOij7_qHJlTGsyqPMRTExjdL-lFX4QxEpctJh5tmErKoo4OvSnEVEmy-KzBT2wd51tlM_6eD9aCDH6YW2rx42hHe5igdJOjzfLJxrShOY3AEc4sdPjsHE6JxoD-CRYT7HZLJhyqr6KrlOE2XY0TRYFkXYJZ_NPQOAHFsilGIHls-rdl4xIIu5652Pyu5h80_4qgvUfDaTmi-gkQ-ys5hUBMhaRqeQ3bbqBgERQrD3yxQp4Yi8KIIVUv4FsWGGjZVn49Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZmnadiTYBJFs07He-uY2pDRE822UMHyKTpZJzAiku5aKh_aBS7Y5R89c6Nip0vPqf7IUyixneDu-cDiT7GwyY0PaJG_qk_RZKdM32v8m3ZktVF6cSygLCqwQ50hZJF1VBMd-1Q5BC0CSEHcKJ-kBl_qGPzDreQ7fT2WGx1uVlHStDPp77uEDtyiJMhCb8zch39-6bFe5mAo_0sOZ7IrPR10sLxhAOnBFl5AuGKdeW56HI-q2k8xzvjihvrvaQunXa-HEt9j-nC-576bljaGxt76ksAjlNReG0tJaiRzq6wj2-wHTD2cDx2Ii7L8pYUY48GESS7niyegzB-ehB7q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1YEwaAXYpok5SN5vxaa6MARorMaayXrJlYcLXjn2p5525ByZ1Pbpe2XDSxXbwJOCo4Y7Z1ebbkvT5QSbiENjVkWa5YIIeu6bNHFCork2BVRu0PNu5FuTTRcw0eD7A29vmMAzDIDpIZ-URM1tqgaHBUyYFK-ewZye61Y5EQaG2-htjfQtY6Tx67xzDhmNjz_ehzyAOXnR4ez4Vu5B8uW1gYjV484_KtOvQc62FTXSVZdIakNKCe_oRyvgE2ATpggRXgg36PBbsVSmNkXcTB0VJ1VtjuvHCTb0ex63tIQ8YWvsGW50womcSbogKvyXV8BHCNISF_JrDtu1CpFh5V7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M77ewCvEoT0UB6nLl7c-mvshvcG4uDN8AxK4v34OqjMFXah1WF5KjYoXKkkoRV_QxnNwOg9Xa8EkFoxlon_VtwHK8c0Y8LdapKRuk6O6EikxvqaMjtI5aXf4w-YOCPHgjv0M1IS3vo5zpMtaGWOb8ZpTw1safxi3x-pXSe9YTX9HOQ1EXRDWo8JxckqmTCU2t9IlGLdIlmYMtsQ9p-jKn2oJHxKHWDyc3I8IsI92bTUGQ0atoZPSu5gqj9BvBI932_5bW8j6tIwTnAmMykLitlUx8DF_WwoJn7gIWe1_7JLwGtprMg0h9gWU0sWWTatuHkMj1MbeM05rswfZ9001-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIfFmSo30pZ5UEn0Apuil2vSG_SQVYYyM-XwRUlcQr01f6RNDKOBui5J5F5AYW5LwaFXTvywk1-XAnKoFGIXDNmV3DT6qZWW4j6qIikIp_ui3fS09s-klGMkguFEI290vYuOpRccVJOEqxlLy03FmYGf4oUPh9qGUjVlQUEqmPX6SrzMaKwtq1JzYess_W-KaSEdv7_1SeCiqC3vCt4F8JQxgkhd67A-bQeiUrn7f4r2gv356OdcuGPiU9JCQHcSeDI6l0Fnzol64j0v2eIbyvbkhmB3a4ShV7m9CQC3twm4JOVHCbJZK6uV_AoGv_FmRUi8m5Co9VMYiV25by9QuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HcBwhYpdrOKBILOYArJJRfIzLdKYRb3Q6uhUb6TGSFdLHgOTB-MSOKUxcNFDKaIwXRCAmWoWtoGIvgffHd_2QbHyep41yp_obfyAadWle_RUSFh3PGUmaP6w7xzFkDvCJ21Y_CpT8JkAA5NCL3wJwyZQWdxM2R6ef3wCCVtxe-gUEIOv82W-5jyPMcOFEvX-Lqldbqo3TLMNJBItkjxhwCZ69iyKuYcvzdtlD2Fa7tYd_xxUSkIyr8Q7SsYAA0MNXKCS_MjIv6y0vsBR0hclHV8BKqYPOeuPcuHS2WnWwNeOppk_Hkz9wslPatDi3KOL4YOZxlvzxIKxq-q5SEVjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0w3Ud9fP2fR_DPyHaoa_LUTdAGzWrI8zV6gcls813s7ZVh3JhzzZV-0xmMS5F3ZPGfMRSAj9c_GmWWgrPpeXNBKHJZO3WweS0N1Tagcb5B_rMM3HDsTMa5J5hrP4-qR7CIL4NNc5pEQbGEV3zn769B1jKpeqtDwOSMNLXssRAcKXQvz9gyk46mWz7vGcOXvVejZP6dgMNQxdwUrnx0Zq5MGeeM23aenhGpnIyBXD_jxwMs6cjOu7TT2TojBMVSmOvPIoSTa2YvMs2vCunMQP7bwSTNFO6WT8vIFXK0UD_o149lTmJBP7M6NAIDvXmr_Put1hHmT7wPEjRrwH2JTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IW07YStjKnvcqFLsXK_SKlU7CcLuRcNLr08E0u0ibz_bwS20wfglKXQRdxzfX-QIyP-DQHA6iQYJFvyZYTxUi6h1mXXk68fCSKs8WMNxz6SGepzGTqkFKtvBzpi-wj5wDf9sNIO7wXKmFtI25R8y9QihCM_bTqaVhhR0BYt1Q9pdcOOvutPi7U4TojCEL_Hd_zElv4NBTQD6GBrf8DrTsIKil9rYEQyt4_VuIgTooOuhRt5NlK2vVLav75QbFarE1S6Ia7XdXv9RZRybKRcuXwN2eFukdnUnWEYfxEgDJRQFvVDngUjwg5wTak4ZYNp2nv0d-KStoacuzCzkvgT1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vj3_-lB3Sqv_WI3Dd9OzL9rQaxwUQap6JXQP13GL_fG4taGDk--r9q31R0yNNHntK3PBv1m0Qe0aWR_P2gcIGs0ppuxNvSaW6b6exzrb66f2XyZyEVaxRsFy-IrQRStWZl1NXmHdVzJzQI6ih14pW0pPw5HtkCpQhuUocMYSgG9WozwXb_wDIo_R0ECZKMc5sI9vmhATkEMQgD1lS_gOkP8LB6JJ9ZDSNJKP84g5IyDuXW_8dP-NKRcyi5D7kyM5G3FRTbyMtYr40-LALqO1kKwz4eeXdXKe84K5VjiIoFI-FQYfSHryKC5O9NxcU7xgLmnas8jWu8aNudQPHW-NCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhxP8VE5lUEQCq9tvuwiBqeX00jkWwPLJfUDlBEonBf8zDA1uEQm6whmNDMxpkz3Fi4VbHEPAL6ssyB1cLGky-30b4xKaqC-8pdBrx8n34qGPpxe7YTGrtLP6ofKGdZIN9rO2Fs5yDBoTi9FG-47YPoW5OQkfJI0fAno09AOUujb2wQ8ezwypPPBs9qZf73Lf6i7--dSKeUYRju5qpsVgpIkNh-Q8JWfKjqOx1GZSYK3EyKd62kEVtrJf5h6k-hGaqmmErQn_KC4HQmg5JMGl5iQJJ7mXyCQUyL88CWEZMjG3uwHhofhnidTEoPgXE7YTTF3z__FhOA-ILnyP7M6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3V6aQeM-dPwlarPxI9nv-ThrdCDEdYE8Nr7ZMUeiYeEiGUuM-wrN6ueIgoiQiRg0xHEZ280h1lL2Fr7xr_0DXCQpwMLlc8YPVV1_uszOpUGqWEygkWt5TqhgpTWOlIYUAJOWw66DYp6GfaYXokqU0DEHnk6vUzCV8eLaZ1HRb_TLAMBJgwz6BZ_sOH9O8jwujuyINDQoZitw8bMfnrsXdsh3By3d9GWKAsA9LCckzY-gawqXD-sNRxKRtTo_3ZHPsBW5L8E8urvkpfzI82EPhILq0ZOWvLIkzVykefprm2UliHg7I_BZ-m3JVox1zrues1oQ33zyCmQvIa59R-LCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/srUfA691DFnSVpTm-XcWxmrvHKHd2vnR0-vUr80M0jmwq1c55TLROS1qNF7UdByWwkF84V732durF0I8rRfBp71yyMhKm4jbRufTgL2P_uQpTJz3CA0JeMuJk2XsZP8ZJHMX8u9kIdLmloIDMvd_KNS8SVtQQJ7OtsevHlen7lIZt_v5xezaH9p_DU8qvWuCa4zsRVwT0eAIwYWGh0iyfZ1ClpoBrzlEy-onQbEBPRdcl-w_xoX-5bwifbS63KvNKMiW0YopIAMsTiYW9NxBGokiiDfllseU-LrX_xRNnY_9yAMS5UHwrJrPFfSuCUKu3vjnA-gvG5eNYRAncidpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gu2lrvAqZVeX7IRk-fR6XK2nFc6y6kRMjM_hM0An6sylhdm_nEHClVxt2DyZkdonnCzkI0c24yYmM3JXGb2pEtQLZwk9ESYaDknQ2X7RsevnLI_v3E1QhD8fdWveO3ckfX2_Ez1CHudHAYWpZhwD1LgwWlQOJ5qEW-Y9op829qSvM5irl4RpuBdbxs74pKWOKmUhQ3ntKrskSOBdowr1hiNB-ANKpythRcnL8wvSfNw3FpXSWdZkoyEJmx_i2KNUh8B6aDxoULQgrIa2Y0_hlR3KkgkLPmC40JXf5KfgRqJqGZkvP9U7ATmF_DLR34rqD3oNVrSu42LZE_OapCPoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWX0c4Pfn2lDAmMqflPo3VkiK3KfgMrR5sGbEvcMauW8XSHe51CF0XNab5GD7Hr10qXSqUAE1fdrpYO5LEASS0Pmxj3ZuT1GEx2SEovt5fww5WuCfhMab1uNkXsPS0cFv0pEnaO0LihJ1_4U4-ucz9yPtywc39bN7wR6nNc2GjWaiVQJcz7tj8yoscZum-C0CutGaWyxRwAcSRDlv3olPOwcr5UFIDWoXUUfa60mwF1-AC6pFZAppBxmJ9waeh6fsT_Gn25Gy4Ul1L3yyhl9xJHuXe4lu-vTSx-BN_JEEgdtcLTkPnGCDBILkLanSKZvopfUF9uXUovKvSzciQskaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxhJi0-WWJ8z9hZmd5ZDq6mjI4YsZINYVz2C-2F_zLO2iI48kaJqkxb7k5Ng0ET-CWf0hA9vzDIIDnH2xTzeGrNzdtg1FCUhSkrNxDi-rHlvbk_KssnoEUN-DsmgroU-TmCLMWSTDArCdHcMLqiBaev0gkq61TFZrbQ5P6hGpa5qU1Bwok_wPnLRTimlG-I9PIe2-oqx1hB_kuC8DHQMs8WvQyqAwJYI-LiZmHyHf0DgkRcn-bIoPLrvttMx0By_H3-yETVP50Kg1l0WNQqZYbAo_E1iB5s814JN5vZp6BzBH_BTPaDbUKuLfSEzWKLLW11Gogghfso-Co5DFpKSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-WLOdtVu2hZ6GC9b8nowCE7STqtt8u1S0ymj3TQRlYENUbO-4H5tp8vIgRleSykxQHZxUQEI09pIjGzopvNBoj_weeu9C0X0y8WaiQc4FR8FphloXU7fVAMx9SMv1VcJ94spoKLtWsRizMMenP9JgZ-1yBKHhocixGKW9dbXTHvw_chz_h0MdXJT5ksUiZozzHpaRXNkWfLm1e9B1xhJGidFHZIneDd8qjCaDKsWwJvW9_BeI8Ncjd2PnQWGoj8FqUFKwxJccDfCem34GWOU-ybwDUiwodKqb066QbXGBHJzUsD5b56KCG-t5Z71HQwyErzJNa9QSCdu1wSbWGAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iX05LIcRlQSkwYlG816bYNI2DCec9VUjoQNyMZL1UV72HzPXGNyWzYg-8VcYc13PdHXbDxiVVzcwhESUaqFy9gHqE36asGZ5rI1x-JcNTeMx9vAQcpSnC2QFlpDgEhHn5D5NjKVs3-EalTROR1Xr5bXLMZg3MbCMATzXuxEBcov7YegduUNoVvciUFK_EO99cVm2dj6iqbprW8acloJEW6tFqTZNKBZfNLxXdoaAOG12jhx3SDcf4nnuOHwFs21uepgjbHphm7avx7GV0YJtyXehkalqBseFJs15uE5byWujD2t_tM-HGjT8DBGNVPcVVdgNEF3tkADv-hVuxqR-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOKs_TyW0I19KJmdmG-EzKAncNlN8942DEkPqzS0rzkADvlcPBLgIte8bYy7_IbYb6uMLjy775jniMc9KtHo-vQ9tGsHyKRd3Fz6BvsBnwMgwByf5EUZ2Ug8Nq3hT2lPLZUeqzRsa5Wa0eK4axbiFN-IrjOy3bGCbDiVt0Sg0iAF06zegfdy-5_ycGvzcQS5x4Nlqa20o3qAj3cTJo_mRsem5dXynbpttvmHJ1K03ng3lFQqHV6t4xdAyxLJ5TOh6Cc6r0_GsC-ppfCJFuYgJkDbSoRkUgAySlEIxUhh85joU5d0hg8088eP1aUzML3oo6gWFC9ZntFWhyrDsrB8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJIQy9XEGU1Hhf1wW1O2WDpo0TQNK099WdhKcezkLM4kjLkUUYHFczQZFYSIKEnkRxVU45slr9ei2OK1u0-DQOg4aaLCzpq8CvIVI-bxLxQrgc0FVcqD4FE_Rnz1ywI6sY2oD0FeUH3h7pz5UHvD5iZrC5DQw3Vqt-xHw7AGjH7JsmfSfYQJ1HOFFv2hHsDNvttCvC72vwSSB9Dt8A7KRf0M6oUKrYXKwnwjEQijeFUOSqycclOScb1pJTuYTzmBAgPfLIe8tr-a_Gq87SOPEgCeNdcFkPRd7iXaNO0yUtF6ZCtQCgURofkIqa8-S_HLlisj7m7ec-MPqSBDTbfTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfwfVjI3rN8CzbAZeiO_9ylOLcNkLlfG0J_OnDIvFJPPKujwTsjfQaGCJbXyBjDaSSCC0s4HCk7dnr5mFw3uGTx3H6hOonW1EOsXthbPX7nXl6iqn5vD6DhVQKzlGWk8hyoNG0Sefc9sNnBRml34J_dmbvnF4Qus_J8xRXZp2WO6Y3bqy243Hp2bi-WUfuPanyoe-K7t9DxzdAxjbn5cwdkdPPSmO4UUVUqNh-W_t_SrOMFq3_XRqb_5u5v4s2rYwPlGqheLKi2KvUM3EMAamf9Vs83NDCw6QC1YUJ2LOVtTWmyVjuD5PAF_pxFz0_AojZMMHR01ozySME_X2PFtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iV0OgC-MP3rm2rT0BLUFKYijtqB4xVz72PNKk_D-61jkTi7xCQ4KQ0en_8xkT2FE7tvnPc1KIc5ThDwdhQd4KWf4j9jMSbo0lNjSVKtWm_r_h0ueBCvyYYEZia-arlodtbmFlXlSjAthm9ymwEAwAxZL2mb_N6VYn1BxZVDzrPsIKYYHzVl15LNxTG5yUDzGl4XYdx8pMRb1iHknTTCGhQFg61ul6KJopoObF66jC9IUSGyaxCHvthmMC1adsvRhDjBos3IRUA-hN1EWMdXKoPyALi02pA1DVFfyf0het5nnlHCCjL3b0k9XL4ocY9RtE2dz0-SGN9DBQXNFJiSiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IBbzLHSD1LDu2ILx78y3k5BGN8S1-e7itEaqYnKn9m8OhvqCHf3mNRkoCj_zuaFuyCPaEyCnWeuHt5WGDfdUBbIrTTprTifRj4kzp7fdWtrd2wD0Bjwh2GPl9QouAxAWnyH9ZBiNkU8rAnwc8yk6EvSZxULQho2Hr-bRb47aRqleVNkRzlk1GhWy9hlNeXCIoQmIjxP-rNxxdwF5kdEIiq9vz4IGxij4XGQb2fBcBX-KWUuw7yNPbbd9E35nw-K8hqy7jkgmYTmFoj8xKi9Q2V8_EXgWegUUFgRPVTLe1WwJjRL7JxwGjO7LSGE_gW3AlnPtweywY0k5CAZ_qMlKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDheyXleZKRbarZmnv5rUTEhuy-j7kZMsMD4dCkkIMsdYOYtcYcWcY97vcNENImvAORYmfG18C2dMYIIqYKGhJSZCyT7KYPsnfaC27KaiVn1UMgKH6ftPx2114i6h57BKt7buTNQdPxJaRn-TTcvcQwB5G7A5Xy2C89lYSzqfMOCNs4JtoN6ixNYuG-t8SiGzLlO7El98_TfXXy9BoIBD7gxizapZeO4_R2zwcA0YFWQDGYBGv65YPr9aP5bcXAk__Ju9oYc1kgtiUyGaGjegpFPt-cFX_QIjhohaIDRNS2cIHEG4u2e8wROLc6f5SePppB7YoS8AlnxdGjINlZJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KkFRs8hKpH1cps2DbDyJ0I4OX6pme_Y0wvXe5ctkSOdxBCdjACd_egXKVU4Wjpz_3PqPWc2-UKOagTRRNvT8g_MJLOiVALXtEnhV-kTu1JZg4B4zMhxz0CkiwU5xMvL8AJa6VfLRrHNnLDUJv6tyZDpYVfU9ZWCgSVH0NeHyGnrMLxl_fAQGWZ4-v1-buSAAfdPkdImmCbXgcQ7LSMLnpdJ9vTZQtNfdUUBDiH4k3Q5Scmqt_2RyHGy9ilvrIhJJKDq5DYSkeHnCIk6yt-Efv25QU8J9HyRl14ujMSCtmQ4_1Ez-z_9u0pgm3qiPgZ_epbwVzlejsUsGlsIc9-R2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpVsUTFgq7IOoWnNWdojchQIi9E-fuEupslmuJGjpWA60CwHAOXe2iuwxzfSlDl6QBd7b6MKDi5ucc53kw2zISwjd8Suw4u9CfvS4E3ztCu0VyC9bZG4dgQ52bT2vq8SkMAvRMXQWE9MPyGE_uWkhD5t3rqegorgV13YlmIz3uoiihsMpWbj_cP6eylq1ojKeIVQBoN9plElZpWOgqcAEbSPhn80CMsPC0zrcTjQ_H-6Eq7yhui0JM5iCgwWmQ7PU3M96pf99zXXyTGAnDNN9QTjeJYuafUXlK1Gd_ZSS3CKvFqawQARiWJ06WoN3yCz25KoAwfJWXxT-0PJ80FOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gq19wtyE7EokC9LU8C_g8NVdqz8HQ_d2Ud55VYTDaabYPuhUymJBKT2FKG-7copcmNFPu53Jh5oMu3CJ6PmeKc36VSQG9FQaWCR96awwZ5rRkSonboyg8-fTCO3mKY7dd21K9-WIqo34qhY04sq-2nRVfbi9t6ayXfamqBq63FGvsjq34V3x-OJhPq3U9q93UHgbiUzevfu3ZfNmuI289QLbLwb9zwQ6K2SXb7iuYUHSM0k1Oa4l1Nx9_3qmzVk0Kjrft0EQH5GlkIZA3nwvqPetuDshbEhda7UNIl5Ux3JqsmrrrMZSIkB2Lsab1haOStvRZ44aasRgxDA-coSknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SuEvZJpPyKabmC7Mu6pmM5ImZLevF_sNNGJTjyexWoKtTnXVg0HedpkQ0GBqVVIoMKdtb64CaiXGIn8EHdicJ_2CNbaG_Fkv3XS4nmRZp5X7RMzSF4fhfn-Qu4__-lY1tpf6fCzx2rbGRhbVjr7L6tSjCca0lao5r94HXFSMUEL_H_3tZG5S6vOfvm9FlvHwfkPJNLe2QipQ_vSRJ-g9A9N4TMLYsWCEZqZEF6vq2JKgSR3MUUBb6b5D2XGy30RaDUDL6_2lT5ib3uQFFaVlr9fJwiCn29x8_5KcfOF1CIfbE0kV3SKzlZb3CT3QQS6EO_s0JEF5j-JYltg4Eiol7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jeb72tux1pgByiRvzbMW43eDk6b1fsfi9rrDRfTyb8P8hmQJMcc-oPTUtBUDH73O53U90tKbe2yDetnf4BeykAUXCaj6NqeUSnSXNenhiG7l3O8pn1OrLlFPOvSKxfgwm7B_hoFv1ql2Gwbd6_wZbOhyXZlrDfNv2VvOLvnPLGGlC_DIoY75uy9LHNkPs0VjuuwYlaz4UnNQ0KN-uYeJyssMAMK_89QZ3naKehnbM1bSScHzCjZJqL3dN9q0OE5_-dpBv53eaTLkoCfCN1aFksFy6ddjckPFqoqs_Vk7N707tvx4-Fz3Gjpx5jZqpEuwE9Sv6S1cTrrw5krhw0E-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUaXT0-TTFf5IFnEzZndJFEvZbi97A_IsoVdx43W7nXOIcJHvrM1Cg5a-UNUVckv7jnAxVK-hVci7BATPdehiJ-snVEmkPQu9lL5-20mKK7NU-zMMpqtb1RJ3nTZ15spy7nx9XKDjJn-QI6ZG3ih04Csg0AG7rFnA7E41PCVc-GbvIQU2RvvKlnmdv9hVCncJt8VJbtCA3RMYLlJl36ecm7_ydqsEx7jFx6DeJfxus2Z_O0NFLGFGamWS0pvINKxkRNQBgv-vBtwZLUPB2wepbxIjvj_or-LaTetDt9z1no3n6XcB0IKIHzEDAq4f3fRv3BaWSnLoTC4HZB_mHE6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IeP4Gt8HyXNrhxUyW6Z_BTJGefvNnZ9ihdnpER_-kzWb_Ej-CSfQ2ZXday_1SFxbZTTsyF8SQfM8_pmK0ZTMbvlFoXPmQIRQX4KzdCgWdo6APOuziAuNhiI0feUwoAlaAzohfgUUzuq0j_7Dei0kvHKR0t8RifslyWVNmeac8HHVsas6yV5dkDB7po4YNkexSJcjupdGBNc4nrqjlXsMu8b6v2o2QZWKjLuPBR5Y04vkXbViJ3hrWbOBs7TcDLlNOvz0iF8K7sITs-O6tepOyUjBHuenKv8q-qU96LelTdbkCYz174Cyjs8FNUJg9d6BTQRKkhC2TAn_k0WNotViKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZIctrFf1cAaY126gHG7BtnfddoY5aqYRL3x1nnvKUQmZkcWdVTAwt-OKJulOYAmdWprCa33Zd4oMP6BnXQMqaX8YSqAy-jj7bNa-OhUptCgn-Dna5YwPyBjjuS05-8BiY6ZC42tyUIYaEtrKFvy-pVM-zUbh9ThSFwgZTmCKWlD6f08Cf5eJZzW_2fBac0mc17hj2WZdUXokWKJ_tDiw5UZCiKtgIblHhPYMT_G4EkKk1ipq1sVUUBMFjc1ZRf7Ofd6rAJGU_QAWSbfCKvlDap0iXGE0LZG_pyNat_JKVo7BFTAWKKQ3XEKrb32HMljClw6U_npGjQpUF960cntXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lv3qJiMo87VUC46m2vw8b5wdZ4RIdTmND4XX8YfbUpXUtUSQb1JvP9uHOXp7TrNzpt_px80Rm94YJ7lF29OjcJeEHK-ACZCfJpVSft5v2m3h6iI8KDhl7Ty0rCNwAQDac-dLNMRV8xrwKpbI7HUPbWJpbioX83Ae4l5yn5-22XodLK1aZD6KClQyIwGUJVIUoI3SmpAtulRYdA1XmfwMcfVlA19_k6bVfyDEJcDcNcsSbv-Qtsw2pwX-I-kF2DdR94PuOSQcNsplZwSNwABm4oTPzAkk9FN95LVfQjkuWMmM_MlU7-8SzGRwf8-iEVGfd9yjms1rNKhz7PApYPmX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqlTCT3x-Px1GCh8kD0aj01n2W1k9qLZ70Kgi8jZCmAFZSYeNzGszwJjWtXXEWCOe9EUkf7JjVSoFcxA3zLLSAAzsWoPM3_JMqyjStdeFzjrxJs2Wv21ieAb0pXONwWYGBWjUqlaV1-rVLFUly8D1zvoHFD5UIyL0Rl_p6P_f4UwaFRVTbj6lfTB2Awq0-bxl2TFc1udkyMVGaQ-RmdMMpHICmjVOS0sBwTEVS604_nhy9ksGuHHdbrd6oEBlKgXx8UKIDXkTqP9LslCDl1xom8cI0t21lrZNy6cmOYjCLOHwFni6r8tTXF2FD6fIIXCsDuC0YN1v9oHuOgo_Y6aRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMKw3Rzsq60lX7qkPWgOe4haCnbMwhyPWrC_9efMg09mdoJnRLPOuWvwC8Mh0xaengmUqtLVc3_roysyhVd_9w8winB-QIDFY_JcvHMkVkpbPJ_Uurv3bP5zGlXOVaDaZI08aLaYBxhUTZhScx24WN6OUo1svVu72BA6ii7sf6pjz46IxBwIqQeBiDmmTHUThiluYNPP30uuiCYJ9pzzNeTG6derfvvJPbdHZXBuPUUhhKoJsuXvKcBdqjAwl-9CJ_gNbarSdui09KmcPwVoxWwHUbYU_qeOyf7PRFfiYGnwBFwvr8xwL3RwUTv-XBURxxZ7jPZVL4TvHpiTdvvPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obXN8CoZxXAOo8J9e8B0sJf4qw2qwu7-FI5ERwM94-E5oY9qq9Pygn_BJ-l04w4tQloyOm3rRvRP_V_9n91BQgUXRa6rTbwZ7bOdAWY0g9oB5SnFX1aWgSE07DoT_V9-WTgXDFaPkR82ghCqXjdiIAzhTQLqC0EZwEjjDNUjKnas7MnyyqtYsgSjvRjkaSoG0qyvTVUQwfe_ZTmAtmKpBd-8VhjSBL3sE1a0QCr4qm3Xz5ipBxfToiM-gZdyprv5KZzvdfqle4UuqWkKBaC1vEV3bAZ6DPWf-hiE_I6AjJGwEkHrCpWvc4nKHRMz8A2WFTYH_FaV-7WEcE4lL4RV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPciMYSMXMUOHHizFM474ExdtkraJQqddvjrPua4scYEtQSgUSm7l7-mEHe6_qJrzcZGRqyXwW7P1oXByna_5UEk0yh17kxC7LAgqCS_6ZAD_fnMUeFZziwk4qvgNB-RUtVwcpEfKMbY8Wc7VuvgAce00sEv1oVknJ0pGXHe4boiloh_k3wZkuEXnjKBI8jSEB_rb-YOFS0JyiMwLmdny5E7p9T7uKPwS1eTpZWrBHWdcXOBonH8bvNO2yfGfvpiFj72pmcBCq8Nh0b0TnFj8R_8aNXrKtYkv-xu505IZmyOvwjU6QgaT3kAvK6OCuHQ6T5fw2bh3mRuM-uOP1J-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ctfyi2sx7AgEYAoJJyFesEaudkPogJHE04IkQDluKswYcYE8vvHgQe2xyQugpRTxWZkGXr0uFqHCNmYsdYtnX74mcUconH3thNELwUjvOquKtSVDgoFgcAWlIVk9nLg4OZe7_aeyL83tWozHtuehlWAlZT6ssDRNjTR2X6_Oa3HA0_tpiyjQ2kHXx40Bqw_PqRsEP0AJ4A9L4vR5tz5USAEoweroRJHpKB2II4AGI_Dps5_Xboa-NhYlL1T7a5ZMHoCRA0sQDkJ8QjDr7hZAk1lpl4rUXcoqnlUbAE5D8TsIfUOKUvemAGH4giUdJJmIBOiUaKhu6eGLskU1pX251w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p40WdKMKslx0WsJXBQeuk7mGIU4k7wCtCAT1JREuhQk3wOZflPz3qund3F_w6oCY7jQX52vm-uWUuBdYLJLNsvRmjKjiQvdZPCM-fmqZig1B_tyIBs-lTRtVfmD-IR72Lcwg2su-RvXRg3PBj7WSqJafEPog5MHIt7mROXIvBplcpiD1mNi5vvJOHCIY9z25ISWDz4XS-YdA3xqZWSBxeeLLOq0vVuc6CAXH4LeGMcfMcLgHdz4jWtuD027OGbolWZcQ4s8mAmXwgMZMttmkURIQ-bkXWT3ttW3zl-YDSKH39B-loLO0rfKzkfHNAlzx2Fvyhn1WjltagpGzz9EhlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

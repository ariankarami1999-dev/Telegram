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
<img src="https://cdn1.telesco.pe/file/m7wW-2D2_usuxWS3mOdnn2WN-dgOnfGTnxkXOct9qStea5TtIrHob8bnETgyq2O9JX8qk0lx6SFARFkmd-rUfzWkAEjThzrNhOwArnUATS1UoK1hSMSV0CzGHAIrYsL3uSZkkR1Jp1grkU7e97KiOqtQBq5s4-eFuM_U41ESc0WzwflzGZaHNF9VETi7-Dm_RmYyv8WySbOEa3DQFMla6AhcfnfqprNPf5Eq4YMO4e8nG_wop_DrV4YGgupuGirtfMOyL4g7Bg3VvUtkmCjDTtN4Nw7cyoxLcBuvV_L6ZDtBnSuWNFs90diYRWPhooVndbjPrckrsIu6jH4ODGbQvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 99K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 03:43:59</div>
<hr>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sx_-3cHtlnrHWm2XM3mnsNa3WF4_cP1KdgJPbncWdEyTlVH0wixJJfg4ezDqQHk7hIgSMS2tHLtRvOB3-xB4iM9l9jp8fzBsf-NE0cYqZQzH7QIp_jUJ4N5V8UQTIn_L2aWwioAmBh6XxGv1tGDdhBlWC4dRPo3xWsocQdW3G7eDLYb9GxpIV18Rm0gRykySj06YBiwu-pfcmBOzbMQyLOWdomTesTknKlgb-seG5JTdJl9p7srgL9zP_lCSL-tU-xWW0_nHGyQg8hodjHaDBxOLEOuzbxqlqRMlqRwfhuLhbG9t_wsAegzlbFVVh2umcNwO0WP46KUwGcZ_l0cBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dbB6vmI9Sod8o_i31hw-yr0AID5m4W-zwL2A8HLWwnWpqAn9Zs3VqYPv4Qo1Ql6yEJ4GEjVle7ruKGLPCvwxgZPK4ULOq6NIjuCHWA1H-28pkbYOK-onzUZvndxDgYr30hS3o57THZ_xa91cEGQQkafwHa8rORKsF7NzA6kpQdal6UQASn-CfMK6nnDvaWf0sFlkUH9quEMG5sTDyUiacIgpEDoMyO7XatZZTBHMZ9UxS0XKAzZcRSN4Gcl3RYTtutukW4zkkDQhmuA2V4bH0ovsxeJhBwX0cok3Oax7nGHAAd0cIT8ryJ_sEPN50zLxGvRXWPX1sbMNRvaZpF_33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVrVwJv8nBrONw2f8RCVFoReLtshbpwhyqrbq7N5zn-BYWuUvOk5Sw5NVj49za9zC0ExNrJI5fVtKOjrRyOEF2CJjWCM_3i2iHeXDcQcaEGmeofgGdlsr65v5yIn-XE_6qtBwou4uhM1qj3j9sZaCLrWs-3XhklhlMQezTb1Fpxod7Ba8elpsFZ0kyj0sw2Mp7qbSxIMXFyCsmUiwpniShi7rdZjT6z1I6vQMer7KuWZifm9JXIn3dCePuTPQiMUqSVyZ_unUCuo9DaEswTtffMEmdrehKfVcnmMerpafxvL1Dg4VbBYy-siBW0zMWr8IcVMbEcIk5tsVh-aT8j0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از ۸۸ روز قطع سراسری اینترنت و برگشتن دسترسی‌ها، هنوز اوضاع اینترنت به قبل از دی‌ماه برنگشته که دوباره دارن واسه همدیگه خط و نشون می‌کشن. انگار باید خودمون رو برای یه قطع سراسری دیگه آماده کنیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2426" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRe7Yyf40KF5kZTsloM1B1g9NBwa_Htftorq9jHMAyAULi7HwcriP-uy_6vx0GfTxq_unCyYuvUYfxg_ikWdjFZUHZd_su8mUSp5Zf-7SRqNezv4ezdiCjna57yJNL0b4x3JpR8j53P7YCwuCh_PEt0uu1oQhG-LZZmloApkVlI6WU9EJHhMjumfi--r_-kLlB6_Zar8BZTtoSsaY8enx3L5HW_XyWlEst-y5IrbDNZrhVUc3xBE8yXf8V6FupubcE-yq1qy1N9l0IICP0s3XSIUZtBS1WElSaJlnuZlPZTFT8YHzG73NVi_5G4v-1hiiikJATrvPhGAbJ33Ys-3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه
#نهان
یک راهکار متن‌باز مبتنی بر Workers کلودفلر هست، که امکان راه‌اندازی کانفیگ رایگان Vless و Trojan رو بدون نیاز به سرور مجازی فراهم می‌کنه. این اسکریپت از داشبورد مدیریتی، امکان پشتیبانی از چند کاربر، ربات تلگرام، قابلیت مخفی‌سازی ترافیک و قابلیت تغییر آیپی تمیز از داخل پنل برخورداره.
👉
github.com/itsyebekhe/nahan/blob/main/README_FA.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2425" target="_blank">📅 08:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPSQ2sGb9-jSqYyxR739qHtLQOjaTmg4ZbfOHZm__j7bGGQWQwpR4kwd9SlBwPN5kHzAKm2A86JUB6je4-z6uIta4ovqVJyOgN842KGzNZSj47qXW3DodTmnS-9V9b34w7VTOfNRRIvaY57hpQ05zsRrIuOkDSWqOAsAxOg-zgFEhCOeG4V980yMqczaTSqHS2N7g6uIN6T6jyuxkGwrwiIZQ7RXVqyBCqUKhAeVUXWHIdy7y-2NABMXq6e7_dxzLrD3eTz8oKw7jqknXobsww01qCm9SAhn7-oeJrKO-vkukPsZdgrqgP-z-SG43jQdYuSk-PWhUiQVQbrpM7Uttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه موضوع حادتر از دستکاری DNSها هستش و هر روز ابعاد جدیدی ازش کشف میشه، هرچند سرقت ترافیک تعبیر درستیه. همینقدر بگم که این مساله اصلا درایت/اراده‌ی زیرساخت برای کمک به کاربران یا چیزی مثل تحریم‌شکن نیست بلکه بخشی از پروژه‌ی وایت‌لیسته، با هدف قطع مجدد اینترنت در آینده‌.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2424" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EATcLjQDgBRB5psTks5O9S38HFROI3LcjxMDugCGtZhCz6S6d9jWvmdJ0y0XqsCmHEYs-iuhrXi_l5sC4ZG6yGgFHvcJaQNdf40gcSF6eVhdyrnTY_FofpTM64s5VJ99S1BFVQa6Q78IIeNBIoGuzlho0mZxRTr3tojss__MH_ql-DfdeeRvaPT2JiY9EasquApwIL_02EnafuYGWIxPsJVMWomMkYeVf9Bn_URQBOKKMEJlQ22mHaayUXtvPNqum2Oo2pSCX9kA6n0h07KUGbfJUqCO1DY1DN5-rLBsU0ucElnBUqx_S2kc_4V9iupKFfi10R_3R70QO8mNMNjurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GenyConnect یک کلاینت متن‌باز و رایگان برای شبکه‌های خصوصی و ارتباطات رمزنگاری‌شده هست، که با تمرکز بر کارایی، حفظ حریم خصوصی و مدیریت دقیق ترافیک شبکه طراحی شده و ضمن پشتیبانی از هسته ایکس‌ری، برای اندروید، ویندوز، لینوکس و مک در دسترسه.
👉
github.com/genyleap/GenyConnect/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2423" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvwjXE78inR42n2A4f5zZCbMV2hli-_DxtfsEGm6_3gEef5Wqi1H6H33rWptT9XjcmZGoA7xuPvILfp9uDG-9Z8wyvXLSztQ1icWxlEcuW2xULky1erHd7mgTDVc2k9mgaqKkhEpSiEEOJ7hb2_aFO2Hn9mHWv54Yjw2Kibp54r-Moxm4PaHbLPYPCqCt_CKar26W1zaWv-1DtzwBYbV_UO1TsqUKr-04XSuAldP10T2L40bMYc4eyUgMt6ym8p-YNgUXOTyVtb1AncZtoWBirhFOKgPr3CgQz4qbu5m1XFT0PSdn7UFGl-dambXMGoABe6S9_o5z8Ec-V0U8m8jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه آیفون از فیلترشکن
#شیروخورشید
با نام AzadiTunnel در اپ‌استور منتشر شد.
👉
apps.apple.com/ca/app/azaditunnel/id6776486891
💡
github.com/polamgh/AzadiTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2422" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8rdBRu1ENIFWB3ewNOmq-NMZ-wuQtKkNM-qvEs39zakTGb3d5SBN-9xtPykGN0qUiHGCVK40FOe3iZta_WAAtDep5RG-dQFTCDuNxczDKS3BA8iqojLCgZZ0zWKlnWk8L0uA63a0U7OOFXgfpj-aD7sN23NAElld6vkihj5IhveiUJMxNSXs2MuJ7RWHeyYCNuKdHjOqgGsTqnrF8hCQEjdVJihG3OepH4Qjc-rkkawQ-XYkZg75V1DWu0H9cybm5CYEXhucf3NnyiAOZJgEC8WdAQzukNxEbvF9Z8TeIS8gyCdUwtOks9laQ8JZYdve-tVVVtRQKfMVbu_7nnEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن
#دیفیکس
که برای اندروید، آیفون و ویندوز روی استورها در دسترسه، قابلیت Health Monitor به بخش ترجیحات اضافه شده. این قابلیت بصورت دوره‌ای وضعیت اتصال رو بررسی می‌کنه و اگر کانفیگ فعلی از دسترس خارج بشه یا کیفیت مناسبی نداشته باشه، برای اتصال به یک کانفیگ جدید تلاش می‌کنه.
اینطور که تیم توسعه‌ش گفتن این ویژگی از قبل در هسته برنامه وجود داشته، اما به‌دلیل اختلال‌های شدید و ناپایداری اینترنت در ایران، گاهی قطعی‌های موقت شبکه رو به اشتباه به‌عنوان خرابی کانفیگ تشخیص می‌داد و باعث میشد اتصال کاربران پس از مدت‌ها تلاش، مدام قطع و وصل بشه. الان استفاده ازش اختیاری شده و میشه فقط درصورت نیاز فعالش کرد.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5927
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2421" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مرکز ملی فضای مجازی اعتراف کرده که "از منظر فنی، قطع یا محدودسازی دسترسی عمومی به اینترنت، به‌تنهایی مانع اجرای عملیات سایبری پیشرفته از سوی بازیگران دارای توان تخصصی، زیرساخت مستقل و سطح دسترسی بالا نمی‌شود. این دسته از بازیگران، با بهره‌گیری از مسیرهای ارتباطی اختصاصی، لینک‌های مستقل و زیرساخت‌های غیرمتعارف، قابلیت تداوم عملیات خود را حفظ می‌کنند".
این مرکز اضافه کرده "به‌عنوان نمونه، حملات مشاهده‌شده علیه برخی سامانه‌های بانکی نشان داد که محدودیت دسترسی عمومی، لزوماً به معنای انسداد کامل مسیرهای نفوذ به زیرساخت‌های حساس نیست. بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، تأکید می‌شود که اقدام قطع یا محدودسازی دسترسی عمومی به اینترنت در شکل اجرایی اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است".
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2420" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!
©
DigiHubAI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2419" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محققان امنیت سایبری یک آسیب‌پذیری در Visual Studio Code کشف کرده‌اند که به مهاجمان امکان می‌دهد توکن احراز هویت گیت‌هاب (GitHub OAuth token) کاربران را به سرقت ببرند. تنها با کلیک روی یک لینک، مهاجم می‌تواند توکنی را بدزدد که دسترسی کامل به تمام مخازن کد کاربر، از جمله مخازن خصوصی، را فراهم می‌کند. این آسیب‌پذیری از طریق سوءاستفاده از مکانیزم انتقال پیام میان پنجره اصلی VS Code و نماهای وب عمل می‌کند و به مهاجم اجازه می‌دهد افزونه‌های مخرب نصب کرده و توکن OAuth ارسال‌شده به سرویس
GitHub.dev
را استخراج نماید.
این حمله همچنین از قابلیتی به نام «افزونه‌های محلی فضای کاری» در VS Code بهره می‌برد که نصب افزونه را بدون نمایش هیچ هشدار اعتماد اضافی ممکن می‌سازد و بدین ترتیب بررسی اعتماد ناشر را دور می‌زند. گفتنی است این آسیب‌پذیری در دوم ژوئن ۲۰۲۶ به گیت‌هاب گزارش شد و تنها یک ساعت پس از آن جزئیاتش به‌صورت عمومی منتشر گردید. مایکروسافت این آسیب‌پذیری را تأیید کرده و اعلام نموده در حال توسعه یک وصله امنیتی (fix) است، همچنین تصریح کرد که این مشکل نسخه دسکتاپ VS Code را تحت تأثیر قرار نمی‌دهد.
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2418" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFsnKozsNzKic7QbeB62uSx2VdvCGwz4I4HifYWYDzspJz86ci_Mw3Zp7-KqicogyZxLcKF3ZnnGkhOrCUMCNV1xoDHvH0SRQdLV1sG1M24WwGPZLNGVX7kAPTLvc23dmPqzMQdIEmE8dRBIcPY3_RTPgTkLuuaFBxddZFo52HjfrtJ5gb3M_h4feDA2luMorFg25wYT1lCZU32nu_GuxMte2VLI3huxtt6e-nieBLhvjGWFyTX6RvgRknalPZfZa0giOnqzTYdyIxjwEmLA3XTQbrMnGrGO2XejMH0xyIY9WP3UQqL_ZhZYYGfBIWXI75_gBdHum-AvN6S9fbV0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر RKh CFS یک ابزار رایگان و متن‌باز برای پیدا کردن آیپی‌های تمیز کلودفلر هست، که از IP تکی و CIDR پشتیبانی می‌کنه و در نهایت نتایج رو بصورت رتبه‌بندی‌شده برمیگردونه.
👉
github.com/rezakhosh78/RKh-CF-Scanner/releases/tag/v0.1.4
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2417" target="_blank">📅 08:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صرافی‌های دیجیتال نوبیتکس، بیت‌پین، رمزینکس و والکس به دلیل دور زدن تحریم‌ها و انتقال ثروت به خارج از کشور، توسط وزارت خزانه‌داری آمریکا در فهرست تحریم‌ها قرار گرفتند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2416" target="_blank">📅 08:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بامداد امروز سیگنال تمام اپراتورهای تلفن همراه و همچنین تمام سرویس‌دهندگان اینترنت خانگی بصورت همزمان در شیراز و چند شهر دیگر استان فارس، همچنین شهرهای خط ساحلی جنوب کشور در حدود ساعت ۲ صبح به مدت تقریباً ۲۰ دقیقه “کاملاً قطع” شد. به عبارت دیگر هیچ دستگاه تلفن همراهی آنتن نداشت، هیچ وای‌فایی متصل نبود و هیچ امکانی برای ارتباط حتی با شماره‌های اضطراری میسر نبود.
قطع برنامه‌ریزی شده جهت یک اقدام امنیتی، تست زیرساخت، حمله گسترده سایبری یا مسائل مرتبط به جنگ الکترونیک؛ مشخص نیست در آن ۲۰ دقیقه چه رخ داد!
©
iliahashemicom
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/ircfspace/2415" target="_blank">📅 08:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_MQVFN907sV-y9e6cbE7ggO18KnO9fDz_JxWHBgY2VooOE20-QQCS60XfcR7n52qkIIGeEmyQU33EbpfCF2lTkdvlRZOzGYbHo1niai6h-z0847KkGM-aGXyxomVLLLMKmue4L-oM8bfN5i5rK6AnUng1JcZet8RhqS9u2Id7_RMzhcs9NUiPIVcrm2YpJDXVC4YvcspJpsf_4KfXHTZBZXZ2C4yIpWXkE2bq2vmsBqfhDI7hz8JfPi0njbO4u5Pfj-nXC43YlQHzB7DhqdyzIJm1hbIekhuOf2j5wFC2Tu4Nb-a5nuyb09927cUdC2G0LO9ym1bk1pR3O54sN2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۳ از اپ متن‌باز و رایگان OnionHop که برای ویندوز، لینوکس و مک منتشر شده، موتور اتصال برنامه کاملاً بازنویسی شده و با قابلیت Smart Connect می‌تونه بصورت هوشمند بهترین روش اتصال رو با توجه به شرایط شبکه و میزان فیلترینگ انتخاب کنه.
این فیلترشکن از روش‌های مختلف دور زدن سانسور مثل Obfs4، Snowflake، WebTunnel، Conjure، Meek و DNSTT پشتیبانی می‌کنه و یه اسکنر داخلی هم داره که میتونه Bridgeهای سالم و قابل دسترس رو پیدا کنه.
👉
github.com/center2055/OnionHop/releases
💡
t.me/PersianGithubMirror/5793
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2414" target="_blank">📅 08:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb5uOWMJa9yG-gL6xCJ8TM-W-JK5z3CJZZtKA6FcA10GyuteAEB2quSBvNwzLcWvGoBJ0RvqTi-0h4DCL_7UEnuC10QwQwynF1YMxCzsX7qLUS529EIjMnwL88oH08QPWnLvGxHR3CwN8CR8cC_nFdhgJdSHQQI72ey9FQkDCQ-LfWmy2L6_F-F-xA12BjOpztbUMospW_glw6zVfRx-mJ-rjgDbEwdMx5LDViRgpYIhJ90q57Ml8vNlebch3siqYyh_3Xt2bKaFYyAZHCh5jgODGpDqrpFbcDKnSCnL2tF5Q78FAgg9uX-0ohlcIk2KIHS4L2cQuMY21tXbB2OsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی جاب‌ویژن درباره تاثیر جنگ (و البته بحران قطع سراسری اینترنت) بر کارجویان نشون میده ۵۲ درصد از پاسخ‌دهندگان اعلام کردن که شغل خودشون رو از دست دادن و حالا به‌ دنبال یافتن فرصت شغلی جدید هستن. این آمار همچنین میگه نیمی از اونها برای تامین هزینه‌های ضروری با مشکل جدی مواجهن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2413" target="_blank">📅 07:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بر اساس گزارش‌های دریافتی، اینترنت بین‌الملل در برخی دیتاسنترهای کشور مجدداً برقرار شده است.
با این حال همزمان محدودیت روی بسیاری از تانل‌ها و پروتکل‌های ارتباطی ادامه دارد و بخش قابل توجهی از این روش‌ها از دسترس خارج شده یا با اختلال و ناپایداری شدید مواجه شده‌اند. ارتباط از خارج به داخل کشور نیز همچنان با اختلال همراه است و بسیاری از سرویس‌ها و مسیرهای وابسته هنوز به‌طور کامل در دسترس قرار نگرفته‌اند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2412" target="_blank">📅 07:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/ircfspace/2411" target="_blank">📅 07:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وضعیت قطع اینترنت طوری شده که همدستان فیلترچی که روزی روزگاری با هم عکس یادگاری میگرفتن هم به شکایت رسیدن.
یک سیستم فاسد همیشه به سمت فساد بیشتر میل میکنه؛ در ادبیات فنی بهش میگن فیدبک مثبت. یعنی سیستم هی فساد خودش رو تشدید میکنه و در این مسیر بیشتر و بیشتر از آگاهی تهی میشه.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/ircfspace/2410" target="_blank">📅 19:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vu0THl3HzT_bFFRC-Mt4nA44fBX2tWIhzdVk3r6w-Hz4MueiIHcPiEfLkrNBehnKjiuk14a6pp_cJNUEv-b4i6wZQ-bpGjdT9d21TzclBwWxyXSDAwF5XRPMR64saDMAMFQv6IN3tIhkd-40pdQaI0_iB4mfnn50jeSO-AGkEJi5-Oyz2N8n4tjXZqjeDdZQ-EFfOgryJD1GAWad1CNOqQU20cWF-CWSc_XTK6AdU5AlajZTpaDllcEKNQyilFFif7KPeSnSXv4IiCTEm85x-bcYXkYfQpk7s7HtAOFAQ9y-mIBBUxp2KXl_2s5-iVYRV4K6pI6ZPsNQAXRjEcX5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح اسکندری، عضو مؤسس و عضو شورای مرکزی شریان، در خبرگزاری فارس کمپینی با عنوان «گزینه قطع داوطلبانه دسترسی به اینترنت بین‌الملل را فعال کنید» راه‌اندازی کرده است. این کمپین طی پنج روز گذشته تنها حدود ۳۴۰ حامی جذب کرده است.
در حالی که میلیون‌ها ایرانی برای کار، آموزش و ارتباطات به اینترنت جهانی وابسته‌اند، ترویج ایده قطع اینترنت بین‌الملل بیشتر از آنکه همسو با نیاز مردم باشد، نشان‌دهنده فاصله طراحان چنین طرح‌هایی با واقعیت زندگی شهروندان است.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2409" target="_blank">📅 19:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nCwlYH7_ENhJxhu3mbku3bS2_R_ofcjTJpSmRR0WCaTz6Cih3KqFCWgD4kGk9YVLmASM2S-PtZ9lcxmsc9Bbn3yRFS53SVeadLKIWhrkya4xlEh1sFz_ar4Vq0-ADzzB3vNyaEAO3VhQvjoD0pH9oVt-keMmgybbiRMwWYb9LRvdvPKPbagNogvt4CN7XN83KSOqhXfW55NDijwedzSPmyCBDxnW-keElHLuYqziK3IQdxM1NELQtNf3eOCha2T36mUd8AyaTV9N5ArkUwtv6eE9VVFv9lAttLrob9Aj6y5GteEqDqKseB7h0WEHClwpPXemkGOmytzvpAN5wAhXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SenPai Scanner یک ابزار متن‌باز برای پیدا کردن IPهای مناسب کلودفلر در ویندوز، لینوکس و مک هست، که با تست عمیق از بین هزاران آیپی مربوط به محدوده‌های رسمی، اون‌هایی رو پیدا می‌کنه که هم پایدارتر هستن و هم کمترین تأخیر و مشکل ارتباطی رو دارن؛ تا بشه در کانفیگ‌های واقعی ازشون استفاده کرد.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2408" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJPiaN3PyepMh6dwrMGJUUsirZkJboMLIJOsse5IaTTVGIj9884YKGk9R2q2-Nh65b0_cKHZU5ECzH3wUXSbzBBkWqU69vQzYiblx9mAUWfAbkKzURD2X0O2IMj-NV2udKtOi7AiTu-THIZ8DhO5FYctHIwtu6uGSgbq4fCIjuOe9268lyqUKbZgq5pj0U8u7Fv0l6-ee6QTlPFCzjEEvSnAPz8Ba2K3mJyJd-cwsM_LaxrqhUzObOwZzb6e18FvRshBmQ1DnCA-hW6qwjX1oFWaL7_jt8fGX2lCDIuM0uTAoYy_dh9EN-1rjKQu55pAmrEpjaTsvo7Bt_SzHGH4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SpoofGUI یک نسخه گرافیکی برای SNI-Spoofing در ویندوز هست، که از هسته‌های Xray و Sing-box برای مدیریت ترافیک خروجی استفاده می‌کنه. این ابزار در اصل برای اجرای یک مکانیزم محلی SNI Spoofing طراحی شده که به کمک اون می‌تونه مسیر ارتباطی بعضی از درخواست‌هارو به شکل کنترل‌شده دستکاری کنه.
در این برنامه کاربر می‌تونه فرآیند SNI Spoofing رو فعال یا متوقف کنه و وضعیت اتصال‌هارو به صورت زنده ببینه. همچنین امکان مدیریت چندین پروفایل مختلف برای Spoofing وجود داره، که در هرکدوم میشه تنظیماتی مثل آدرس و پورت اتصال، IP مقصد و حتی SNI جعلی رو تعریف کرد و در نهایت بین اون‌ها سوییچ کرد.
👉
github.com/ZethRise/SpoofGUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2407" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lj3dth6AxOsPX84BdmE8YjwZdm-bq-7kS7IbkXXybL2jVWEYu0I0Q1waD1YJjDM73F0WbJGoRsrlDoh8Nm8yh4qZ0D8-YUD4mbmp5007GNHkNvWIuTbphvy4oO-rrZAU8DE9mOXBUTTZk0qx2ogrceUtfNI7UrL5emFQoUQ4Fj7rF5EY-Ybjqn62KyioHGqLYeQ3_cGIUggDaxwHlCSGIrjwFJ08DThStKSV2Mys4vac8n-yMo7JUX_tALN37cQZs8SX8QPAf8hRdNGQZZnITx2z18g9Q_Mi4DXV0TX4-Cz_pXl3tZNc-0IPjqL0qw5QOnhV2b6-EWYANHTLKGAiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر CrimsonCF یک وب‌اپ برای اسکن سریع IPهای کلودفلر هست، که آیپی‌هارو با L4 TCP Handshake روی لوکال تست می‌کنه و خروجی‌های آماده برای Xray, sing-box, Clash میسازه ...
👉
github.com/amir0zx/CrimsonCF/blob/main/README.fa.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2406" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9n6q6hWpIbnEzdzv8A3cT9Ou8VteS5PSt9gRPOvYNT8_8XvxA4JEsofol0N5gMtdcqSEBi1x7maW-25buTRjl64yJT_X7_avIewY2lyFj2NUEbVgU_1k6XZJUQJ_bRnB9gJVNYCvKIBLE3Dd1PxgHdFITpPtJ1hdAhlzL--P0jIpJONgX8a1usudbLnsGWEreCbGXBfD8pOCX2WgWzcpvTySdxI7OMgSe2v_7tQ7ZsfTiLe2vqD77noZwJV9B0-8X08X2JQABcJw60ilE6kbneGt2HiE45TNtUPdQRhAfKOMq6wAjBW6_E3bzma03FVLQ1BYykDY1VoJUR4PPLwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتماد به نفس اگه اپلیکیشن بود
©
mansheyeh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2405" target="_blank">📅 10:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینترنت صرفا برای توقف روزشمار نت‌بلاکس وصل شده، یا هدفتون برقراری ارتباط بوده؟
چون با هرکی صحبت می‌کنم تقریبا ارتباط پایدار نداره ...
©
ArashNalchegar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2404" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت. انگار که درب ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشیتون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2403" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تقریبا اکثر IPهای خارجی خاکستری هستند، یعنی در هر کانکشن شما مجاز هستید حداکثر ۶ پکت به سمت سرور خارجی بفرستید؛ این محدودیت به شدت سختگیرانه است و تقریبا هیچ سرویسی نمیتواند با این محدودیت کار کند. به طور مثال برای کانکشن‌های Https صرفا میتوان یک ریسپانس ساده Http را دریافت کرد و  شما حتی نمی‌توانید درخواست دیگری بفرستید.
برای بعضی از IPهای خارجی خاکستری مثل IPهای CDNها و ...، SNIهای محدودی سفید شده، یعنی اگر شما یک درخواست TLS با یک SNI سفید به یک IP خاکستری ارسال کنید، آن کانکشن سفید میشود و می‌توانید به صورت نامحدود پکت ارسال کنید! به طور مثال با اینکه الان تمام IPهای کلودفلر خاکستری هستند، ولی اگر شما یک درخواست با SNI سفیدی مثل
www.speedtest.net
ارسال کنید، کانکشن سفید شده و محدودیت ۶ پکت برداشته میشود.
در حال حاضر SNIهای سفید به صورت وایت‌لیست بسیار محدود هستند. با وجود میلیون‌ها وبسایت میتوان گفت عملا اینترنت همچنان قطع است و صرفا دسترسی به سرویسهای خاصی امکان پذیر است. حکومت برای بهبود کیفیت اینترنت مجبور است بسیاری از دامنه‌ها را بدون بررسی دقیق به لیست وایت‌لیست اضافه کند؛ به طور مثال الان تمام دامنه‌هایی که در لیست نیم‌بها ثبت شده‌اند همگی سفید هستند. نکته‌ی قابل تامل این است که اکثر این دامنه‌ها را فیلترشکن فروشها ثبت کرده‌اند (زیرا قبلا شما می‌توانستید صرفا با بالا آوردن یک وبسایت فیک و ثبت درخواست، دامنه خود را در لیست نیم‌بها ثبت کنید). بنابراین فیلترشکن فروش هایی که دامنه‌شان را در لیست نیم‌بها ثبت کرده‌اند حالا دارند سود خوبی به جیب می‌زنند.
این سیاست‌های بستن و وایت‌لیست کردن اینترنت موجب رانت و فساد زیادی شده و شک نکنید که خشم خدا را در بر خواهد داشت.
تکنیک SNI Spoofing باعث میشود که یک SNI فیک توسط فایروال دیده شود و کانکشن سفید شود و محدودیت ۶ پکت ارسال برداشته شود. روش اولی که منتشر شد اکنون در بسیاری از نت‌ها بسته شده (یعنی فایروال SNI اصلی را می‌بیند)، ولی طبق گزارشات همچنان بر روی ایرانسل و بسیاری از مناطق حاشیه‌ای برقرار است. روش دیگری که آن را Plan B نامیده‌ام، دیروز (با تشکر از دوستانی که نکات فنی خوبی را متذکر شدند و باعث جرقه ایده جدید شدند) با موفقیت تست شد، ولی به ۳ دلیل فعلا قصد انتشار ندارم؛ اول اینکه بسیاری از فیلترشکن‌های رایگان اکنون وصل میشوند (به طور مثال سایفون به راحتی با فستلی وصل میشود)، دوم اینکه همانطور که گفتم روش اول همچنان بر روی ایرانسل و بسیاری از مناطق فعال است، و سوم اینکه بسیاری از سرویس‌ها مثل اینستاگرام، واتس‌اپ، یوتیوب و ... به طور مستقیم با MITM در دسترس هستند.
©
patterniha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2402" target="_blank">📅 19:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینترنت در یکی از بحرانی‌ترین وضعیت‌های خود قرار دارد!
اکنون وضعیت اینترنت در کشور به یکی از عجیب‌ترین و ناپایدارترین حالت‌های خود رسیده است. در حالی که بخشی از اینترنت بین‌الملل برای کاربران خانگی و شخصی برقرار شده، اینترنت دیتاسنترها که بخش اصلی زیرساخت کشور و میزبان بسیاری از سرویس‌ها هستند همچنان با اختلال و قطعی گسترده مواجه است. همزمان بسیاری از VPNها از کار افتاده‌اند و شرایط اتصال نسبت به زمانی که اینترنت کاملاً ملی شده بود، برای بخش زیادی از کاربران حتی دشوارتر و بی‌ثبات‌تر شده است.
کاهش شدید پهنای باند و افت محسوس کیفیت اتصال باعث شده دسترسی به سرویس‌های خارجی و حتی داخلی با اختلال و کندی همراه باشد. از سوی دیگر، گزارش‌هایی از بروز مشکل در گواهی SSL برخی سایت‌های مهم و حتی سرویس‌های دولتی منتشر شده؛ موضوعی که می‌تواند امنیت اطلاعات کاربران را تحت تأثیر قرار دهد. همان‌طور که قطع اینترنت فوری انجام شد، وصل شدن آن هم می‌تواند فوری باشد؛ اما فعلاً روند بازگشت به‌شکل قطره‌چکانی پیش می‌رود و همچنان بخش زیادی از کاربران و سرویس‌ها درگیر محدودیت‌ها هستند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2401" target="_blank">📅 19:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توی یک لحظه دسترسی مردم رو قطع میکنن، بعد میخوان به همون فیلترنت سابق برگردونن میگن این روند تدریجیه!
مشت‌مشت خاک بر سرتون.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2400" target="_blank">📅 15:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XirNjywhdzw83SRBr467PQV8Uovvaap0zdGZv-gcc1j9cenbX96zCcBkWJgptV3DWUaeHjt3sGPe5ggPBdgkRqF6MBb8us6uzQ8yIk6PHoj4k6nStU2DLkvznNFY1ZQvq-W7Xf4IbTXLNHQUavyxloIUg6m4KQgIrGWNieQcLnuS-7MknGiw7Ct4BPoctSGi9wHlbYgKyICfZ2kw7MGYlMTqOVRWMJa-LAQ6RfaH6kOeOoglrPm6cp0uA4DTrU-WmHT9cD7bDzd3Z3DvI9LdDU0ctCanUJyuMLzUiRav36VKunxBQR0_lGDHYr7-xf6eYpLEIDY6jx10zdWVLs92eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جدیدترین بروزرسانی از فیلترشکن رایگان و متن‌باز
#دیفیکس
فرایند دریافت کانفیگ از API بهبود داده شده، متد CDN Fronting رو به‌همراه اسکنر داخلی به بخش روش‌های اتصال اضطراری در قسمت ترجیحات اضافه کردن و همچنین روی بهبود عملکرد، افزایش پایداری و رفع چندین مشکل گزارش‌شده در نسخه‌های اندروید، آیفون و ویندوز تمرکز داشتن.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5676
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VoWtMpj9Mbjy2Kliz4Gvu6TLE_73EzThjsrc3perKiJwAHcCHKRO4OrU90Z6nh5Fgn98qlK0GHHi2rPCLRbtfhwjmcfDasjHveTuKEUo5xTn-iiCBxCh_UHtBHtVd5wMKX05FD3OOF20bsQ2eHoyO_WJNmgCAlnJYoj_XE7bE9jLUvkCmRFBwOoRZsX47VcS7ozeKD-fwB32fV56NTFL-jtsE-DfkJiyDjuFJ4WohZRc0Qnca8GdenLMOuGzcxVHpYNQz0hyEdIDZzR9wiliKXnXLT1nllmxcIKmUNqzWyxB05BETOeKa8x7HVbBp0SmLOvAvOXPymdltlFN4oLzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از کلاینت NexaTunnel امکان پشتیبانی از کانفیگ‌‌های Xray در کنار Stormdns, SSH over VPN, WhiteDNS برای iOS فراهم شده.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این اینترنتی که وصل شده داره نمی‌اینترنته ...
©
okhtapoos80
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJwmbAa3DoOvZDCLltnHakhC29bF3CtWtK2372zIUr0YMi8U6eMDZBePstyqeMKaQjVPkW9Q_zLhAluN1u8F5J_L1v-p666i11YQKxyKxjUM7yz65Zs9qVbHZdVDgDfVpl-jgNly5WYtYLR4kzrWVpFg_cBPFpo763RdXpVKajf3NMJBtYTBqRH45O2MIlXkk7xRVeMoRPNVrONNZbT2guw1ZeC3DGVHyxUsPpzX3W66fo1e03Hq_3jOjcmS_-Yc-Drp1IFlhk-XKYtfapwn3Djqpuiqhu395tw84ukp31a_WtfPs0f1LT1orqxJP0b79ECWN_CGc2TAF4DyWAZxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که اینترنت در ایران قطع بود و تیم رسول جلیلی موفق به مسدودسازی Signature وارپ شد، اپ رسمی کلودفلر بروزرسانی جدیدی داد که حتی رابط کاربریشم تغییر کرد. آپدیت جدید این برنامه الان روی بعضی از سرویس‌دهنده‌ها داره کار میکنه، هرچند امیدی نیست که در محدودیت‌های شدید بعدی دووم بیاره.
برنامه‌هایی مثل Oblivion که بر پایه وارپ کار میکنن هم تا زمانی‌که هسته‌های وارپ‌پلاس یا وی‌وارپ بروزرسانی نشن، کار خاصی ازشون برنمیاد.
👉
one.one.one.one
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بعد از وصل فیلترنت یا همون اختلال‌نت، اکثر VPNهای متن‌باز و رایگان دارن به روند آپدیت‌های منظم خودشون برمیگردن. تجربه قطع کامل اینترنت در ایران احتمالا به ابتکار عمل بعضیاشون کمک کنه، تا بتونن در شرایط سخت بعدی کمک بیشتری انجام بدن. به مرور سعی می‌کنم بروزرسانی‌های جدیدشون رو اطلاع‌رسانی کنم.
👉
t.me/PersianGithubMirror
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بعد از ۸۸ روز قطعی کامل اینترنت، جمهوری اسلامی اینترنت رو وصل کرد. فقط یه مشکل ریز داره: فیلترینگ انقدر لایه‌لایه و سنگین شده که عملا فیلترنت ۲x پلاس رو باز کردن، نه اینترنت رو، و همین فیلترنت پراختلال رو به اسم بازگشت اینترنت دارن به عنوان دستاورد دولت تبلیغ می‌کنن.
بماند که جمهوری اسلامی میگه اینترنت به وضعیت قبل از دی ماه برگشته، ولی ترافیک شبکه حدود ۴۰-۵۰ درصد کمتر از  قبل از کشتار دی هست.
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F7FZ24InHskx4458sqFJf33H9iLqPxfC63JclBax3plU6ANlJGQB4oMtRmDGmEW4HiyCdwRdDehHl4GUMjUX4xzhEzA6hhlSyX22QJs2ou9m5m0OO71SRxGZSer5bIx_ywvHVx7Wyt5jDPVGx5cDc9YPqLsAeK1BzqYMaUWHHjgOQlPm5PT3UlWwCk3Xlx3LXzWpGe5ajLoGTMwebnnU5GhE4ZhoHCE6LmO87aVQZXSu6aohUkaeggV_fQkC3I33V5QJOQA5BRV2naQw5sD6REQ6Ow5B3wtrpX4JzPaPTb_RxhEq-y-FOkoAT4IbbPIx5wxeazGBf0QFJW0nj24LUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N-uTPYjCaABq6ZrGlfCjmZOFdsLsRTvKdZbGXxZSVZiG0Q6UB9ltOaY_OezpPNKY6qfP2pyarkBf9lOCVexfcifqNCLx2b0DW64tI6y1J7HyXfVTs7S4_fTpe7B-lnXf8KopAOWt9C7LFkHcw7STjinLsBuD8_Di0WichEjDJVuHhQmUNAsf8iWMqxNcZs9hrGCTlcBlWMNWFjrkKrjx9vWFKL56GPzh7ksQClfpeImLvbr_Fh6DcW2oElnTcTmCz1FnDtkNz4uekoW0KitFGEtyBBLbcpVyzH-eZxDmBK8TRhvuYUQ2YB_6hmih4Nf8HYyZwP5rqk35OdnO-yjz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EkLMUsM2WDqEjEh6NAtKupMxUF6grRqH56d0NHxyIpnrRwtTkN6aAcOdOSNrNX9BWODip1BvphUzJ2ABn5FyWd7pAOsh583aCRJ_LBT-iMXLNY5fFjzKQsaYbOA0Q1DXc_9JqqRUNb1aMAhvmrn0r3LJawRkuTA6AO69K2TWQ70r7XezcqKyV-z0ThhLgDYX06ferLJK_TxR9Ws5dftsgvIoPV7k9zMkroq4R-aZ-NMrGrgTAaONKWhw1TMyc0Lh1b3_7MWuvXp6PoKrjPnLJz2m-4d-lOiSM9piD5mXxwEniyvQuZRr7TdFFRXXEMCiwYRWoYD3QoJgfrmDRYDrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZoRK3MUbGeMUPuiKCqXiY9-sSt-4mOL6CiZJCb7JFRS4biPejF7hrhg7_rrvh3CpIBcKtmz6467Rzpdc2FghaGJO4HkK3SvLXophZVZfk8a4ED1lG8dBpknTIgtcBhv-5DzNrdHNKKBvur7IeIwpUogCalTcmKsRL0Qaso-I1jEGH5Ag0Zs7kW94KFP167s09EcEBEmnc8n-dhh46x0_f59hUL9GmaIuAeWTvDNFinpG-aLG63gRG8nITRDn8fLBNzBkx5Gpt1hUb27jvdnUY3eld6GPJTs2QlAAs8dBAzK2HLYN04QMZ-Ga7pVktJlQ9TUUQsQXlAoO7VI4J5AKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfWIPgC4youX4tiqJuEKyy7jdpP_--X-STJpmVKU2MT8-I-N-N-2x_VpKop_iDQBOJzNWgM5JEzFfBDIE3-PeRrt_sVD0utiFSzuxXKkfH7UmslIpLrvGbSTCGT1z66nyLXF_h8GDJXRg0L2ZUf7BR03J0YJYhhXSWS_fgRFNrnXOS2WacOYrfg8Hmt6ptDWGvf8bKJI30_l7O859bNYBdEn3By261TTZ6iiEZ8pkQllbrlyADUm_113Y5YtEgm5N3cqHR4hFQ8eEPEBjBbZ2W8tPIWIYo8Wh9siNcVX3nwZBzVRRoP4maNdWnB352z_Qm0akYqR1PLdw7vskn3MlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4Sg_MH5KOtokAI_SOIVlz7RuKCqaul0SvpomUUm-ubrM2MPKzq7gPOn-GA758QKY2lop_M4B3MOidrXTmKebGuJW52SAwqmGKF81iAT6xaEr1eKTT144e8Dkl056e22Aa_hHUocYyvxfRM8TlIEoW3YQDYbX3EnZH9KY1A2Ma_MHM8ZV7GMc8YbhF-6OF03APq0KVhTZQzVrZKeQso2dNQza1DZLnEcKvXyB-hV2djSo2f-6NclRG1xGEaLexGLy2U2u9Fzvu5oUXQxe_4PeIwFbNgOEG6LGqw-PQ2IvncZS364ZrO_sCITdhUg08yieHvLO8kXV60VtNHXeGDuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OArmpKaWcmBk5p5oKLtNaN_AxALw1XGb5x6eP1Cx2y62trZwv6tryyITCsuzVdxT3YqN4KxD83R68cQlRX8MPXxeSx16fuqW5ui6YOtlDFldDzCmPytttdlQHmiPIp3MnaRBYq-u7mk-ID6pEFa7D4j3_pMtoGi1Qr8COea8oOtKd2cvST7dPulZR36OI83CNSeZ5MBDK56oMELGVyD-6EiA7hcd3E7FZ2IqNnCn20tVAnkIgOrSdhWRl1qJkVnsQLk27yb-P7E-VfyQ1xEcr3zxbHdmtNpN1S84P6d3FObXY7whCCcTh7BSSN_iX3KZ3G9Yk3HZpOoki5Camc8u7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G43F2mvJnGdoeLBUNb9KUm-fTfLzckIbRYMPOgNulBwlMlLaqBOL_Q5XmsRjl_20pbgb8gBfVV_WPIqEjSTms2QHkPS5QLmUIYkscrnc35Y1T_aRGDuGMvqDHJWWQzMadHwMsGG37_hs4XBdwqy_tRtyNSuvD6FpdJoTF1zFfjHeJRWj-x7JdBdpAhYg--4GYmLsJEFSVZLx_b4tLQ29dk9nTNX8EpbqkWDG0Yo--DqHe2uhVPnQ-97YxoMJQrGxa4b1th5iKXGuzy5lyO51imV1ArvmVEkQECA9pYaaWgM2RQM47nMaFSYUbGTHOdQ6ZyktoqfQ_TX0M509qAA6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAQla9hhcwDRIVl8z8CnlyoBwuKYt6J-DNxI5xh8MbQ1Vh39GTdndHKMyOOQwE9TzRS38_GC0MYo8RRmSv5XFJrMK9D9a8D_KKKWj5e-cSi1cpdu4ZjYgJdwG1iipvVZrI1VnfQHBRZhAg0zr6Rf0CLztoXbyxxya2l6eK78TZ8yykLdUA8n4NSyYMmhsco_i-ZZ9ziUU0gj5P-tMwvwfOeYX82paP9JvW5W1s1NiYyFoJ1GQnJ9QcmFkKa6Wg6OAY7AB5sr2MP0Su0n_eop_-oLGAG83tCmGRuQCJD9xLfkZauelz8jiYW9aXVyTH7h0kUhAQ4PRrWj66sSCLypyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=QayLqoEbOfhI0NKC4KnEjK9VLv8Mr9UL83XFEMbG7gPNH-VRHxJGY_Rn-v4kTfmLzticUrp5JUBvNmCMQbyX1k6q3OVOMHicHdZnOX_xK8WgFu8Ps94m4GHKXZa-YAWzfLstpjkx__Y6A83Ko7qHFSBNour6JE2q0DM4lAudHv5K_TLtuL72GMvkKAdZi46EMmIWKMWzP0O78ZM3tyyNEBioxavOngQzWccwSrJJ81G4SXbrakVTm4vKCHiPB9e-mZLZB-Udj-rfCeEdy8rEbWXMEldMIleoZauphVDZNfmiKiBZHUn6E7QQ-LlbDZ-SVfmRiqOarfX34atTYPMo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=QayLqoEbOfhI0NKC4KnEjK9VLv8Mr9UL83XFEMbG7gPNH-VRHxJGY_Rn-v4kTfmLzticUrp5JUBvNmCMQbyX1k6q3OVOMHicHdZnOX_xK8WgFu8Ps94m4GHKXZa-YAWzfLstpjkx__Y6A83Ko7qHFSBNour6JE2q0DM4lAudHv5K_TLtuL72GMvkKAdZi46EMmIWKMWzP0O78ZM3tyyNEBioxavOngQzWccwSrJJ81G4SXbrakVTm4vKCHiPB9e-mZLZB-Udj-rfCeEdy8rEbWXMEldMIleoZauphVDZNfmiKiBZHUn6E7QQ-LlbDZ-SVfmRiqOarfX34atTYPMo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcQFNOw6tz1FA6kP_UKiFCynrjBw9rONXVQ335s_oaUmRHIEdP9csT2tw_TwNadPQXSHd5wkNz1SYh8z9VXZ_9MiAXaJafmpIPTsqnltPq03GLUGBWYDh7WGg-PVwlj76sDY4a_ArVRoACgpytXmmIoKXCC_V3MOxTTerTxHxGZjeMDLNv9y5cOOzQsLbUjm6K3GnW4FuKKYEpTauOa5HxOAC_IedrTsYmOSYY24yHvxU5g3J56VPfgMGPlpcO1eNrLjPPVomqgNQC8I6sZeBTzeSN7Uom_5XFkkWwwPCpx6xo9zWTIaeXcawb5dNRxJKZalTWX-zYuFbm9fQ5BJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIpsARNoXNIA3bQV0syb_NnDWLuuj7dY51fY7hu4bUxfyBzrv_iIhSaZbADyPEi9Tl0qbAJj8ycEP3hkdcw3-rOZfKqSEFmZEYjLnPCMCzX-yp968GXb8_-N4zHD3iMgDNSWi_HSQtVnQRu0vXmrV6K5YvOlQ3LqvpT4zGI-P522J1tE-YVlu0yflJukrDKsjNr4jeiT0fyatm1gkTjvDxJGjlCjGWKVrhqVEy_22GRKCkChkULD5Lwe8J0lxT7DDRy90aXf9qGlue2IyI6GaoUFvoFZllZ8fTyKGWfSE4gfcs948_4GgIIWrcdXZ4_XguRc9Odxlqt8QGbIb0O-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nwd-IL22-sAPjdbVOeQDs09gCnssNikUtKJO2LrXimV8irj2pAnt1pLEzn7xuioQ_hvd14YGH1965FuO-zO-6kb9FZ30ivc9vbkO39sQrXY8q5ycrGKcJqSo_r4kN4otmvOOUJn3KNuWu-9Np_-xgIdfXEpDgP-l4HvmIg2EwYR03bz_vBsG-2Pe5KBJByok2mWYW6mhjSIcNWeOBDdrttLnhOw8M8BgHvFxd3f_5zErv3N1LEN8U5V_0LoU1EE-7LDNS9u5bCKuVUVjZ1jcvltFRLZvMQf38NM8-wvaPPXzFZcBMnWuV1g0xuREE9UpIUlyDfSaBLa8nrWZxCOS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AwYmzuGZWqDv40xSW-3R5bc3Qs8lwhk0npLCPYULozuoH_7pnquvbZZPqeWgaq6JIYtODt-gy8GiRJG31gbn7g1trKcrysjYqwqth7nlLNJd-YRRJbuQgw23W2EBDIuLAv28Qr4Y8Uh-keiJuWXBTcz9kPIATKNtEg5vguZXZdBJttrhdQ0xnXS0OJZp0u3sEdq4XgXSWjjHBa_1nflr3suzIGBVG1YJkriXI3603TfFBcAJDRToXB0md4WYY2wodnBsXOKOjMpMrQGCMSDUJK6nd9sU4pDT7SHynJWR4xzRPC0IsF_yWlnz_E7Itno8GB9dKZIFiz4iPfLcZbiZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XthmAXkHcjiMc2n7uGdDpAan9PNZ3JN1Iw54Jrz5gEnAdKIITcQuHx5TPOf-1PXPKth4GcOATt5gZuK1GtitJNtUVHn6RYOc4Q31g9r0zm7CZ25NqE-HI_pcVoKUu6sDYCC5gtpOM7JUAZtKSKtTq5Hq77Xks0Z1tBgko0yOEi6Wq1wkeUCL8-WC3JnSYLEJD3VRYWX6eY6HPiR7DduFNEYBeE0sVI3FaNt6bDad4Le_oMOqEjD8bA-3DTXSC739HQPRETEJIC0JEUvEe6EhtBnU-zXCUAlM7QmKHEBxREEh5tr6v8Q-aIlpX1G5HLAfM5GpHmDwqTW--XUuib8yvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0DJyJSAvcwkD8QwwNiQvySb95uy6E5EdQR-LZsu3Dg9EbeLEVZQRQulpp6u7WqB1MYA_NjxuclOUZ2ZqetrGuM-iAVhyJSQSPV8dUurZDc4PAtVbvNx2JGDfbPd3GUyp3ZYinjwp7Xe72y0Ve2YQdIPBZ551eomJbqvb9OVzGOIHcVz9DGG44PNQGHCVo3_yqd1swZKU-_lO0YRFF3xu2YXWzs1WfEkL0c8VoNpM2ol0iJbqqNcY1xU6vkwt54tijTSCcDqx0mp9Rr3nyoKWj0MC_kLw-Fa-o7tslTS-7dQNbWOc-Tuz-2QgakXwbz_hjFg3C_OXAFcC4OYcdL_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kc6r9fcUkydskHPBg7Yxyfy1X3k7X4KGAPoMptJGhmQ761Hx3bV5stpb3PhoP8TePNxpR5gWaOcDY4aIUmuCrsrrKPtjDLKncre-JMuR20mKjZOEGU3yb7pstgSqReQWDshQeQqVMIeNhBXG8hmTBPG9LuilX303pWl67y4VCflMdU6cqBEhY7y1qCAUgWS5nVzLlc6KJOhqSFs6QnIHpL_K51gg6skRK3Z8_iGcwAwWaD0SDbZA7PyIMdFGUrzUIbwaYDct41oKg00kl-msWBx-rsvQWhLsQdAnC3rRg2DjIEQtuAukdVbb5fDYOuNBSYo6RrmOaHciuA2QjgyHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqyijf5dYjH8g_zV_7-Fy8HdSURy4d4RSrL-2GplvbOe0tncsGNyef5A5YYAZoUoAziSYT-PDEhbcYHtp5fxuHkINbOdMlLx3yau0zTRlv9gbF585OIj0zdKqZdzFU6nIGakvGLWuhBMhlo5jAlUxKRFVWBe7GuYxmDO_g3I9wmlkt613fAorjvl0KH3EfQ1Gqc_4dPALb8kkE_6HyZJJk7k-Cu_dimSnKUxleA40SNOnyIEVbC4M_v_bGzbIdTAK2613C_G0wXCedAIkJkrEzBKR9Kc7AlqQmyeO_TPlQSb3T1ErFhimgKFxrOEjErNoM0HM1FVnl22MI9aJHQZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7gl_-3nNvRBcjtvnVQfvFu2d2Z_qBHtP7P4_8oUZUUGGJ6NwwbA5XVVVyR42bicyT1gwznqcemmOXsoUz3Y5G1Meho26liU6b5aSHodNnbh9e0hZ2UX8j3vfffyqgTwAPl3KxVM6rm5TcwG6BStwXT9duZ0WamZajd4mvOKBv6kYNlYlw2XsuvxzaVxhakf-E5xiRo9ssmqZD3-UMGn9cbo6F7sxPBXOZ6jflqYJL1Xo7LZ6dMl64_HrEggcCDREuf8izaHz0XIYdEeoQTs70liXk99f-tgv8BldH4-P8so3YkJQbnUvKcAhMFa_MyxQyLMtti36PVPiExTh5D4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/av4OQ58EsSvNXsSpbF8FVI0uzBQL-i7N2a1khlzS3W0_WFD6pL8tUXJHuYch0jwn2t2grtP1CCyRu7dINWgZhpmipE4MnzEUlAHIGDfndWFuM5MMGqR2E8CyD8YwCS2Caxs8B2WyiluxY-tP1aJ6hRkqbsORIluQTmUuvmRAtV-FOLMvV3JkhC8r1b67vygz9In15xL31K0PVP9DTxNxFS7KtNdK1pxy5KzRhhdKDp5-nDRvMqqVGmQiddxoySEULdXF1qV4p7QE0bTOZ5bV0HdgUEWEDKxIUWWo4Pu_aj7MPeB4KNvpDXLA9XRGtVAc9N8Rn8M12C-eXj87635-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQGvxDUNnNRAjYdH6K_NZPICUPJ1W-QFUxFPac4Azx_CIVEPPXLu44eVJyZCkqN5-vO_cmrbtpDvHA4pWFzGkp5DzNdtoAyPF3A-WqKYMeljDZ76LEWvKwsNJHkEJHDcSf2STIX_FrjL-TUZzIiJi_YzEF6YZs_HcBMUHJuo7a4OUfGmCs--o6Z7uvl-S0v9BUNPnZxKvGS6ETD8guDRrfmAHpvfvroQTwsdo6Z3LyYB8CWtfoNKL6ifkIjU96VuehwgzLzs30ClUMAjxoFRaiPz1nla-eZ6LX9BndTCWbBf_MYHXaiIQqBIPw6lKZpGbQp13-twfGgRH2dlNbnhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/keg_plTbgR4ZuBh8DdK6JAslK3ouR5PCpzYHVY3Je45cVx2zixfV-zE1tUaYw9CDPCkTOLpfw7pPmgm_JoAP-Q3P-10Qr3JDdOMaRRnBht4ag4BGER8FBvjdSI0fWXO4FzTF3iVY1lLQZBKsHdpdQMKn2zd5UdvIkiEHnYjrU9aZtifvsHB0_wK9XVFrWukNgHa7d0En9wCtGPwa7VoKzea84U7atrDmiyYnJ6uOnnbOV_0hB-jjRm4erunLRMGgttsF6Z9MGs0Z9pOYeWcvireWkqYCLziVRDYlOwlBZJ4NmCJup8msCPivPVPskiT5-NvCr8nyGKO9YR43K4MbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g0IaMIqgQrVgzMfmMnRHpZo6q2te4nXdbq7B7ALIKv4HeURMpqz7fxOwx9f7Zotdd0w27ZLMT8zb7NfbaDaDwD4wbnMaIDWE1hqy-DNTrft5Qeq7abqHgpcSDSDz-tB7gfFgffJfyignshvlYq4FzzB9VI3S3CILIn-Jz4SvkL1fYwarAuLA6HeSI4cFwstwFtfl1J-RZlucoW5PaUClnZFM8LdMnSdI9tjwxOfMVmcM_7Fd2cjaTgFonul2L7_AedM_arTKj9ojHVKNviMvqdTv-JWq3OvoqwGwp1vWX6qPhfcR9k9xUD0v4hCsREUWaATnKqXzXGiMkGszLAKRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4-PgvNHCqB-I1iBPqyDgWyRsr20q7d17rXO9Pu5eRMLFDao7zrkbM2fN6vrNZLx1iydxjcJaXI75etoJZyFDgh-hdqoBnCsjNGkndeJ02z-yz2pkLuxY18YiStNty9k_2qNBEHUYh7Vm9JY2hnOkxRtD9f0IJUC9mWGszdk5A9p5O8KEd_Gsuh45ZYc4V8sa0OUWkBcwpcJOcSxk2o37castSl9enq1pEg7FfycgOgRhSxorireeUHaObhJKSO4iDlqGNU4U4unCKSq9OcyI_bIZlLxmizgM2iesDvaoShOqJjYMY04G_vmJb-8o_CRuPepjR-9RvN942Gebpydiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X5pOPDwyE_VMKjJux0cm3f_fGu1mPkCgv2dysoCTQnkvnrMH1kGDK3NTjxSAbuFnHr2yquCgw6eMkWDWnP_sts1krQlUzPMCakGTl-1jBJbsTGwhlQlAIHWMUzAQSRQNh4ybrY4yETVcnu29it6uOD3Ktl7W4_SqCiEnqSVxCeE27AXetHfurcE-2cFUu5lC2xuA1eCFsXqIDg1JRSqJaeDiQ4Rwun5ycjVqPN7J-XJcjggnTeOUXZyS-tjcD7ecQOosRR52MR5_nDqV5hKmL1S5_B-p0Lv9Gd8EfE4qEjXAJwNy2YwUOUNvZW6Qao5xeO7ng9RgCTkkn7uP--7mGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVaeXC9rAiwQPFf34yGI-oq60ZnZ2w22Pzo7cPGJcrvqdkMJ2RIUuP_xxTuEetptcHRORM29Gg5BD60GVH4fS8cT2-8n1MEZbFM__adwmqwAg3pPPSHcanxYOtGrN_XAVvPM9rpaFc97Cgz2E0YDanxSz_N0VMjUsWokIJc8Ij3Fr3iIp035ewYVIFRJ2ySCF47G2Vf1n1EOSisckNBOAzsRig0zzKVvzB5xdQxNbL81PEp4yl2cA331bTYiMsW00ObgPXcpLoKP-FTuDBGBbt6qd8KsmzZvxC7oZRw1DdsbN43ZEcmBaYZeRd1DT6inPIUCNSLUe6cuUx_GfZde-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYd-exS5H3cptPhnfAzDVe8ppzzafJr6BuHyfTnGCebi__PgcREm1uibh-nog-C3UdJoeT8VHCmEsWQocXqoyqfu7meemuKCOBHIRuZJNGweqv2MxmCoy_2oUYihVMo8KHs4Yiy04aCPFt85RUWaIqganfIo-WcMJkfXB_jDGu4eX7E81xUPn1mNKZJqKckQVWzbpKpG_3G4FoDIGZ4EZVo4TBwbOQGLTJjE4tYVa0ordqSBd-U8eMtgTw7wwQgvRqRS5DwlUzkB1S9MIQndGViS_-pxHs92v4NAvOwrZ-QxAZ3pM3ipeLxPia8WP_Oe0QZg5HwD4LgXCfZpaXavpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cXlhc5-2kCeJi8uK6Q7Zy5BpLs2tMcHruoNegP2ua_uXjxemhRo8ctNMFuXmUqAG58W0-Htzh1ZalIOSKEDePtQHclQttA9b421k_AQvg5JanugDg13xnHH0w_EMaIx5iihUGmeeA1BBm_JPHtj3cg4l9Z7QTi3pp3olhdLZD37A-lTYYWI0ujQAX_jIr9ZyenOZAgPAH_Y43bku1mEDN70haRG3-9s3TAElzSCpSpu8XVVWzpmiBfKnevjsDklklRI-TbWsolubghiel94KBSKuSBElEy30zObChPdCbRkQaaT-NPswfjX9Mkz35LHAsP0tX5nI--0k52yjjRsJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAVf_c0jBB02cuI2pbNeaqySJzcRpl4rwqYlwvk3ZwE4z8NgFdFEfIhFMrZdGj32we0PPr1VJy8wIiDg_XmVvL9CJzHwFSUcxFMtL1GiFWxXqzVM06n4ZvjTrGDzch1jFJ73aH4wJGa6SU_qPJ9kQj0a9S0R6o9q9Qyhu5FrjtxQlqoXGzJpgk0w0QoUqWkFrPD-hlBjdBEq2WjNU0jyIPBd1vEVMqm5XazDmw7_EX2ZRGxovF-XaX2bY0TvqiK2Oi0gIK6hSwQehHJu2sNgL402rHDi0rd3jN2RUiPKC2GQSEiePjR3s-kiXtjWG44LblavJauuOxq8ke59LrxRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eE1dW8SZOH-VgeMtLgqtrrvm42ZnQEO1Zd68Dk0Ow8o1YqN9dQcfEbFCxq78MFOZ2D7CMGKIK-FemuIJf6UBg24FYlL2-1xIogWarXWgsxRnFZOOJ6k3va8dJmomJiO9yf0-IHKWLP6Hb5tC3Ujd-zIZF0biH-cSDvZvO8JF6dxYuDw0rY-n6by5xt9pCYmvahxi8x0NBJuMWMcmqZ-Zvu-TKmU4y6TGWm32a8Gm7-2t2z7jRaGBLkURTCN3g2SGeOYP-_C-Md9DbgqY06FxIEtSIHK7JmSiA4SIKPOa-HZdLloxFhYpgQjN0iduZDmsh4sBPV0OSxPTjebWaypH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qZ8emLWtk-vht4AW0Nqv44e9TzvpoeuBYwh9aa91qx2VCD5GmeKfhJFuzyInmEOgk85Goy9PE-gXiT3AYUeV2uK5aS8wqKvlAiqWR4HMZepzQ97yY5mGmL2IJ-c57qZpjh0dnsBTIWmstfeykxB28ogjfmYEKxLG-vnNRctw5HHpWutvQikMnsAml4g_eEI6F0gc3Ei9DErG8QdHbUP2YOzPyHKjri4hBuXH9VbEv5V5gktiVrsMIm8WS0Cbzg13TDNjykwTbzGURrIeOlbw4_PC-p_38Q6GR1cIa9MgNe7Z2CoGSI8xbZ2aI6hj14k4H_qgE1cLzFgYvBstNMwuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAEI3CNm6bcOcBkxA0SQ_3pEjRpJ54Ve-cxeb7xJ-1LUgNe2i37nO_Ix_IlADRIqldujBKIeb045MftzkcH2mTVXSNkKYP0YRHwpGo1pO0SPFP-NkJLBvzxNAlB_yYXA5Hhsi-l5FuoJYeGuLWg8WS9blpnYv_YD1yYSGyVUE_le9zXUoubKt3fDg4wGTGSZchl6UCdsM0duQwKSdg_SqnvEV-rjrcruSt2c7QfHSEbseKjrX6LJGKAPByaknz2r7WuCDyWwn0keTIUx31hd7kSe0bng4W5YlwtKcrKjxfmxCZHEjvSPrR1UYXORCnrlT_A8cZt7VcowVY-lIp-Tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAEko6cIpzjghj9hVaPlzIXoYzJLN15H7VZxRHAumxB8E1kroEUm-vjVyhqhEQwZh7tzuxlD3Mnwt4RS_o8MFCmZBy9Y4lFEZp0ejKFBo9YG7Ijg8fC-44oBrhKQKRpqVhKb4DCQsuQxU3xbXjHyb5otvRgz1yKKrV9O1iWcWjnSTTafvORnIl-tZsMSJrEg2kYLU0-IueX94yBX1t6S99LEI31GMrDU6K54Y5GZJgELj35Bsge9oN_wWD35IIZHWuGku3SN7xOn8H7MAoPiEJhvhU0aBR6DC2-TCXV3CaQN0PPp1jOY65aaRfwoJ8Hf75HZTbvshjNNIYd309Ms7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4OoutxLXwT-oGWxhnblV5ynzE8twCUIFGd8sR6XMtt2tk7QWDWPNi2W3YKrN54cVkrGtrz3kDZDjWa2j-e4hXNYH_KzAbqApjm-p4aVcbwiJKWa5kNYcno8yWN_TG_W8xSSqs0eh5C9tEmeQZnWbdo193y_sKHAH_JlshEQWnU1RJ7zyk2W5SIzRAizUFhGU-0jNCgv-sTLBJejRHUULJ19PewRXLUeZC-PCWfVii_VE7WkgmfZEasVjtTDcXp2rq1UFqpAxjJ2OrFwHUq7zhQ_EhQMFhBwNzcEd6VKcBPcDhOnK47hYywQeKOfQZ0IL3vJueprpMB3EhrWX1W_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJuoEUlPBIGcE_d7v2wtHdaEl5jfkS2xbR2rxjv3-AAgCqvsFKsB0O64yt_fdcZIiUqRJQbH1H6S9RKEr-FDYfXf5mm96IPPcEhR-Tmefaq0YLejk2LYP99k1de_5YX_HJS0NvKS3Tca7d-MhBQ3IUmvwHFu4VsCECcx5r0o-iZ2RxsRmCNDPxWJI8dCYHAkibpx8VIKVqWLgH8g_nx9-8Uq2lMOkQFwX5nhnz0zcoPbCTSR1Tpg3HLWmZJYJE4u9opMwB8tdsmIr9okdeoK-BIBLOCOaDEXdHnAfZIu1XWn2yNTz3b6a_weB7F5sXBvCDuMZSTEQtQF-EX0i-IwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R39GNjlEkBjYI4vr0fXyZ3Tip6lXKJCREfn_2KoxkyG6JBHAZxLHK8Z7sVi5RQT1slqS56WrwX5mvLRCXHizABhab90EH_hTSwIU67Z8dVzWhJxS4MQlIdZt33_Ag5Zw6AHhhYbI-3P2o64XvWKMXtE-C5Opey6Fx0EitDoXGFajUF5kE6il4NZ6aIImoWKma4nnxDpSM28JaOVIw7i99p9t-l-x1OcA8CCbXzkvKEx6FOl7KXZAh_nNT4StF0j7Nn2ZwAzP4NeNEtdNHoavw2XcsDoI---EOWzdexsukUEAtXZNq5xrfP9XL_D8gzbQF7PvnjpduUE9Q_KmajHNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlGAvRh6Rqgu8TxlUcl-UAOq7xed1qu5s-8cPT7pCMXJuaedfSN8Jbae3xFudbAclk9HorVsPPwOLFj8SWukNuiS_ilULej85P9drw_gYYPYnAInHDXKzXEhHh-urzv4Wu5JnQEhEJaV_feSGcTr6X_jY52UhQTzieeiXIjnZ3KIazap0qs7yqacFXjS3bwQOwc2yFmx0W1-Hvaecl-jjna0gzF6317NEscR2lfr3WPNjkEF8yCySOOhs7vByFXfg_9vmsxieNK066UOZ5PexVvQxQqbkZNETIqGzc-nX0lZCgHZ_2V8nWNPMTJVncg-wEhNywY93VfSx5bczQUHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O07tCGPSAbWj2N7Y7KaM-Fx10LS11OxmxeVQuVF9HJprArjTgiKa83JzuVhdq-hPfYK0TALkE_xK1gvTmAxKBYp3yn1IHIME_GIlYl1BKhMIqp3i9U-NTRQ8gumFy9s3jX63csWDtUnyrnJqzzjW_VY2XFmj_It8LX24p_rEonTtP846_moTL0e3wuCDp7tFuEIzQqIP4howuhMFcQ5x7S1Nw-DC-yaPaW_W03VsrI46vAJ1sIhRAPOxS8HOpLFDxZyp1hEcoYQEMgJNc1wyzYc8dlEWYnZqeZ1EGXvG3R0trzv8N9re7gnrZF2-Q8l0UITvuox6NFhdxaS-X9DQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

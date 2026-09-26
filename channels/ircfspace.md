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
<img src="https://cdn1.telesco.pe/file/TUie3eNwIr4Ynf2gYCtNesULEVHm1XMfc2umXjRxkt_bFdBTBlQGzpZdR2yvy6Vnl_-XLnQpx_WhvZmcPcmOta97QFm1AlfvzlcrGCG9Uq90jXrGLHmeCwuggYpc0rH-Uc12uaTwN_2v4iC6Pkibb8Pk16xAYz-Q4X_hiH8ixD9n_1odbny28tUHy5_Muu21xjn9WIItnb9CdvwxjHKk6z115Pgu54KeMga_1mJLJkskuZjgwfn3IYi6qdeO69Wj5vHKhh5QXUAyifHHcwcYPo8LI0SHreRotQQz64FZeXuTQddBCHWoRo1kXxZ5RAnGjwsUZ7dquFDQPATXp9sllA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eS_4ohfhKllaclyMIFotjvqWJZ_1Hb1lgzWH82AEIFCj04SnKbqB0sjtYNjQWQPTJlL6m1d_ixpUlZ7vKrIiVLNJo5hMuiWdmHwU9rdIhyu1bQAjc2nKYtE_kEt3YxS3sBQJDLe6p9Ub650Xq7hI6E0qtc8xwF4IMc7OLEeEM7ptCD9HKJkBO1sPbUINv9K4tG53P6oV4CQJ_4k0e9ET91dFYUjhurJ9U2VVC5x1vz-1kmN3vlR6bBJAw41URjm83KZJZCi9Aa2RA1abi3sGV3x6-5Eo_B7zCjuK9SLOo_ye-wIW5Q7uZ2UJptB2omgm3N3Z8MqRLri-1lKGJrAhVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oz3bfTaPpNuKtqaAYoEZwGI3CmyYsMFqo6TQ5CBuxoyRWM8OEvMZPa34QqwI350sLZhjAslpmaORUoWxGkOOsT3DPHb_PKWBuLhJdC46oSLiEB3OAHpk1c3WfAw7QXNm3plDvXG6cAd5eXJYPDm9N6ybq8ER98mkFRg_G5Yh8WV65A8vC0CZii_v1ijucTHuG3ekAYnCsxpyJiW7sc5l1UF81yo5yyjUNElea6vA8zkMaje70VaqksWOahA_TJ21wgNUtu5NlskEgaEPs8rs1Z8Q4rpTWhVkRhuDHtbL7yQKXibyuJoZsq09Oaxarxg3a4UyTz8dQEznfQfMAd-hZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rmRTypYmVLCo9FO7AXUrRNey9BeTdd4t5YD2REuxo3OrV6J4b_1xS4FPzZyJ7C5N23YjawtXr7nyaC3etcgZSyc9iRbW5aprMBP2I9RHVFBbGxJHMRa1ingK7cJeUvdaqgYr4NzbVpQkfvwJ-dnEeqKZyoTNLd_XTkWKPMiaH_Yi4pm-ZS1cWkYNe6jRi7oH7uEsaCOiSetPOZqLRXLvmmdej3L2eT-VMKp4_5pjjAgxDzLVywjGUOScB3AfqDDTcToYjQm8iiJezvbdpObjp6ENHpLEvKhsvjRJXsGuqy_bZMSfXVimI1_gIT5dWJlopvwMqRGin4OkfvECpLlR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzTSLXO0fFfD9_0cauxe5G37vPJYPBfOb-wqKOIr0fEqGj9AgpIaTsWGyJobkm1XswScNv3cXx3IgdNsLgvx4hLRTiqJIEDU6lTzfoh1fBn2ci-2dq35W9Uv5s8oeoLr89Z1TqoyqjRsKq2d5o0zjc62gV2telqrJxlZqadFojzf2j5BqP6N4z-eDhH4zkQerWXj0SRFCD2nw-7kW0tNtTrg52EdOXAqR_QAoL7NPB1EZKaAxdTN81KgG5ZLvNKOuBMlCDfXy70uVqh_ORDmGflR4dVz1n-8p7fYIqAzt4pxgDEaTUV-8-_HnY52eR_k27mHuzNkNuOHuxf1Xk8szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VMDJNbouRp1UgUxLoUcRmvOe7-lgoXjYh12AMSVIert7Pjbnl_XoXI2fTLtV91lvequNoza_9I2r1Aq2X__6TBBcqdHkpGyE9wvXVyYd1hmxp9IQ3EzF_n3l-D0hJY2cmp3t1iJt6noFnN_7l0g9TSAD_AYXKMws-xEltksGCDwVogvsmWs5_KxNljjr1hy92_H716PauzO2I7ptb_9Dp9Jx9641iY5zF_vWxjJTNAaJ-1nMycXZpv-PyzwlAOtugNNhkmkm6Ldyv1fhYPK5b_hUYXsPOnemQoc5c2LJhod3N8CkI4j90I6r3XsgxdLQItZDjSrBHWLbyxmw7uaA9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEMZ87oljbhF-9X6LbuqASyDpgrGCvyMadvjWe4H0SiGmeALxlBjA8BGrr-KXVBov0J_WKa8OWmFy_0pX_Esxpl61P7zdW2sKNLDDCkjaM1-A45FX1NRjkWbat7AoG-T2MNW84PQSJEpk5ZMgEc782w2EnXLdpfBRr_1IwjOnUPCzF8V57xvGf0oJj_1LYm5chinfkpGBlFfUNLW5c-XcsMWi81FW_4fbXgwBtSZP11ciB_Ny4DzLDJYCztQnrf0PJzoUOlTa9eR7-7wZJcRmczfRw3yYXHcojyUAYB0k6uPxL5QdzgZRZ7lmRKspknl8pQPCQeiegbZHBmHkaiFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWHVr3jsW7jT5VmwWcADx7zQcNbtLkHv_53OaGW7W6XGDhBqFDFsiW0-k1F2ct_7UhZpcztxVQCU0fI1eERYC7yiWgGgSTrXXlRI9Lm2KudHDroZKuimulZrlK4KyuwkzpWJCma0kDNwtnQ-oSu6d2T8RTZFOUs40OzaXR9aQ72FlVq2Eai_TE5g1pm4KlbibeSoeyfY504gCw4N-1yaKv4vcTuJMcq76YZzPCzx1PlYbODMKgEStaJjHpJ00YNiLvJFb7fpxIeLoETJFYHLqxae12DatvNBfwRiwKQuFjwly17ZJHluieooIenReXzqINBdxA5qf1YQBs4e8UB3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKGD7uUIo5vdGdpLa2SD5WmVps2HTABjKqnc5oJPPm9XDigrXYi7mfX5QA0r-VybrCPpe1B8Jkgza8A8dA_RsO_uWubYYgnyEbCTqwAih60jQIi7iZchcGK4F6GdFMF2uWDp62FY0-Vk1KE8Kj394saj-Ng3Rbnv13NoHptCHAKhCQNbNnxBfq299AEyLfjklhnwHo1tx4zufwO-PZSkBsFl3DDER8zyFqafLB9sd2klxYoePaDKnxFNBK8GTFVC_l9N9jzOcdvOqjGR_67KzS-DH13VzxrE82w-QJeBJwrI-F-ml3a2kzk5hFdUtaWO1_16W5_wQ6miKFipvIGL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyQkC2s_rBS9d3s-MS1rmf7WT9nHjLUMvKoZ6WSsPw3LfP7F_TzqU9eA2JPM0__o5hy86Tn6NlQZn9aNLishQWIM1MdB0iUoqOi8sQtXSfbwfA0UQvyDwJkeHlfmY5Iuu-PImRMotbej8_nxhKWhDDDjXR_277sd2bBY1s9O7YrB7UKGIBQ9HhsmOeTRQKXaE-EzMEM8ug0EF_6pbreRwfJgT0soiVLSe6-Tr2Bf_f7U9c5-_H2pG7L-EUydmuS7PNebXZ0GJXWcc4ducLRzjYCekwg7tGeccgTu1MtSq8bMlmMfWV0pr4OFpJsMuGGjZOVCGMGJ3uhVH98ENhXEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QYQUt8QWTwmpVJuZYCmuYKfbPCoW4nHmD-O5uzMKZMfUXuLTuZaQ9S7xz5rGTOWCTGs6h7IwjdK8ho7znnqyvsS1Wzguvymds4r-9cTQbcq6iLwU6RpSP-PjIaNIAdMvJq2h0x6-cHySD7d4ZMMNr5Sa9tZ9-8sVHauRm0R3sYBIKL212DKdbp7b2yZyLJ4X_d2mbjdt10wYO6T-oRJMSJ8rI5snlxh-DzO2TTU6KgwsTC8m2kk0tQyFHMqeIgoKJjS8dO19FoXR6yO54krMh6Gw-UQu2_h4LXjVZl_YlBsmiPpn2-RI0LtP-ugxetZSc3p2Hn0gqYqO4ZqfQ22U1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCsEMdyX-SQfJyhaKNDeuyl13OgzBpvcTIfZpHSV-ey7f0bJckv-o7brJWDxDcPvYcjkgyDIOxmtDjbD9Cnlhz-hbUqvMgh2-_IfNXj01dMcKKqqHtnkhw4d47MukhWHN1Z3VzrnKK7HLSacGSU7EdrxU9667jGmz0aatZLf6ykL-PbZdfloPVOkJU6GPl2uvrlsE7vEWx6bV81TuxfZQ97cR15ITdYo_WNwrv65K0emzY3ixCjQEY2Ty0yzBO-i3JUNKTPTIQHU4MXwxGPUSQHEzt1t-CUFwXGZrxycvwn6fAxMH75nEr7YAHKIJPbdFB5-ZGd_96XdvxJlxr3zNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IgowCvY4GeeCzaqQGNJplx1PIpzXT5W0dIHVj8DSJU0ABMa-a8u2ekhGGnXtgwt95ofDoEApguJWuHs5GP5Y49W07peStyRFrCDAtKj8VGf3nrF26fshAKJGYJHsyLa3GRVz1NoN77boTD83Zx7cAC6SuP9Paj6DoG9I0spBB5596XCpKY2FPSi_j_BaXurjcWKNxD0pMYShLwaE7IfiSzYD_MaL72udlTlDcL_NdE1LCLCi6nGGpGu_g6RXXI8cSFh3og6eXlAzhh1BdbiGFx2azDdt7VCrgLgAVm_E5ZC0jFspKCQj7HVYLvNQA9o0_2QdQqSpATnlNpq_9Y6sDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bqifyw4hEjqfmSydjgxHxWk1TqRU9B9xxTAs8bh356RRPqsKgdAnm_N74usknyf75UJzedGsDv1rD6jkmNGveFjtTRPRfTRhlvSizg8Wbs20Mr0tAJE3xUnw58ch9BGOieBqqxDor4HOOzsQM02wP16Fpes9CSjKudD0E2iqmNMTwfSaMRf3Mfyj5nLhmmLqx6e_HiDbHVIaCTwVKi4_hd5SCWBzLMdCXAGRk6JlHjLRWJJEMtQNDPkDlu7LiJ8lWDpQ4CUJ1z1h456zdAWVfXy2zzDNgOiHY8XgYizPiEMCjtSwBqnMiUkMNv7ei8Z-3IY5uLarytYwvf0JnHTkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dBPTv8prr_8F3QIi_MC5LsVn5TnV0iGEI1BnQLXB3P46GKSF6SzrUFMHORGsrhjRRaXMvYxoEo-Pb-gU6R87tm27GDMiGreRv-YLZxLBoJ9ZKOa1MVwsca7huxnTqm0DWxDthu6KWZRUJajsmB21J11iV7xLqRsDZXitI3Nngs0QjcCDYrk0EUogS02Nj6aNwabNBzKhP1bx5nF6w-GL4XrCgce73F02OAhEQneBiq6k-yd-ce4saHOygdO0qAmp7JwTlYB9ehHj5i_19oyShtTANnwGReqFXl3C6ujsLkQvMGRE8S4VZu31KClE5Z2vYI2lhsViB8DKlrVNziqcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1NzeIBOJ0qv8LTyJoy4KnlpNwoZNhxCLukMBqZBAn5fImdtVszEBYFxtujKYAIyd0x2hBaEfbzw0GbpKqwUOpsiulOuuyc6mPCGQbqpoKZcGs6Om4_HFfxhO7VOhtW42sQl-p8augbLVwQiGFLMNzMogXu2UNG5rWrDI_vWAtolwdDvURZ0dgNgvwHwxHwAMsVn-1dKK5mqdh9JZRJP-caFEeOQ9Ybda8tlGliQv26AS1DCCgmSQvDFaMs8M1yvdV1kn9K3NonqZuN5JM5Lcz6QNNI5g5X4AncbGeDg79qfPyYFkkZyDoaphddxSVrQewkXJrEN34FkiQf_fM_YEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLKKxz6ywFWeePryQFPrylQR70L9djaXIT-d_5Yj9X3nusoEVVIzClFDbr7pLXW_iiwjK0BghHXWmwdUnJ8yKQEKm3Zm_Ot5r7mMapfiV7TUrTlMuht4Nj2cmsHknwaIT-hzHh4rG0HyIFE8aHC3T17CpJo9QvdjfPZSjQe8_mN0T5kOgNJ5OsOINqGPgkxalowJYcxrg1v_2EbjIuzTYWiCS86NWwHyl_x4Aps77gzKSu-4TC4zg7KJVQeK6w0wtIL0nixPA_3HyzuQ8IgMDD-iFyzkB0EPzjkk5y3zo1JP4q48ODsK-xnt3eBdrldN44ZgQf1i7KUMJAxMQhR_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2pInR4deuX6IKz9IPnleqlWH2nhnRuGu-Rv70_A1jpN6XA3tkkCsONz25QcU_C2Ax4cDLKpCEhu2Bpiu534eY-YI-42SDL2AEMYv9uOpVGz_fRfWIrKmZ5OkS2c48s7UBlVDdPh2w_cCtVxIFFlWoBpg1qRY_vFSfa83pB4fk360Pj_KUZ9l-pnkvuYnh_m_B2TGpB6sEvSzPs_EF_BFFC8-5g6j2-xZRBCSyOMTy0B9o8GH94oV36IR5QdppVsEDlZDFPVSki3iKnXUUjFwZ9SPUupEov1XWFwF3p2CL-GM126TQRkWUPoT7a42jP_dLXUxkNl8eMegPHprRVPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mrdgZyGGdxaXG1ZDrlLL-fdBm3uyRVB9Vw-eiCFIYD0scAbsm7g0tERsCopktBvY4wUD3OkHWao0nvB1IwCQ22ocZVYdZ4pNMCUAifkGBIAJAy1J0H6OL1Cf_B-PiI6DO2g8a3xxt5zNv8oHKtj8uLdQ39RRa4Z4L1BrHj_UeJ7aVasc3oXsslja5n-WbYTkn6IeY-DEhGfw-YuLhEnHk5iJ8w700TY9pNawlZdDlb2aYWrTbgMY0ptV345hf6T2pMpMc97HmusgJhnbiTFUlBhcDHn_MMNgbQwiufbAqLjJlqbC4P2TzdMYH13gbJQPDbx4-SjKOMvz1kCgE1BlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6RhrfLfQ-wdIOZX-HZ_aXj6he0AC2mE2bNuHyLWoylk6uVd7B-Hmz4bsjOeZEujVqQyEXqmC_zEX0KY6ulox09VvDrdseYJo5y98VY7AwrxyibVzXepeeuqPlI6llis4FOUOaAYvsh9xrLZ1lyP-MwBWF3JvTO-pZ-UENAsRP6PLL4xV6SFsVKQHXDRFUSoM8l5EWbD-2u91O90UWt49ju1VaGSsk-zuZwjM9oGQIafezc3Kl-aqnLpQFH5FJcgDkpGYIDL_TH8WELccg30o2C6-denYkvhm0l9GGwMm4joJR5JmGs_z4ye38THhbeJ-5XYvEpo5PyHU93ghp7nZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYdcuhn5K7xsD9i8CiN8nl7WqfN2VTsJFFKPLnzcNsXmeYOtscBhFuhqgvMuPI8gUGBQn-fS8k5vB0_5aL1fDZw145_g2nGODqxxuK_e9BtvSjRTA4X9IPNf6ipXRkIjY1ZnEZUvAaCz3RTgVHhpZFAAZB_p-S83zlrOa62zbQeGEQo29KSjfqBfZzC16G0FM4D0rM16o3ip_T6qimzyqYVv4GocvAVOxs6VHbsKM_8xlzZJr-BNShlzu63uxOUY2Ujsz197OmJb4zwyRMR7jhZyPqbMQ351vn7HNODICo-hqHT8hNW48LgDhXAK7CBPIimkDOAba7kpOYxfGxOXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODqToUuYyB-07SmaI1ArsdDskfR9pr0gjdV8JHc3dQBMA7dvvTUxEGgFUDFPVuFr61gUU2k4IQvBaaYSRWEgHu1bfqET_PikM2YfC3li0wJiMjThdPNcIUp7TQW0yK1ALnK5yQv9uxsYzRsFJfjh9gn-LkR0jOSb9KWom-G_abealzS-yU8MxwlzMWOr88I9OlOkmdE3y7VAe7OqbOl0SA8YQbKAELJd-8JPjyHRRoYIyOhE5Ct2CyYT-tJ0slsL-dgUIjcWqXklMxzJeIJiHacK8UATpaXtjJpxetjSfBI70kOTJ-QVUz-WaNthFof-LI1I_ba13DrQz-81F-HBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UaLhLIRQlnlRNuv813v3BKq_HcDrkftzQZXXIH-W-SOz6rjYqONFOWfD6Eo5UADEj93Hx5uFZceMGhSWq2R2dVedRPbIM5KX_QqiY7q_AhTi7jWZQQDM8hNU8bjC-42Es5Oge0AfSqHff5sf2XcQoDKkZDprSHHK2eNEcy-tl-B7uKoOfRzK5SzoT-cgn8zi6GsPmYySbIYfkV1A95cbOp9scXw2Lg0cPRD0ABk2732iAkObmJV3oD1yuXaMpa5UE3A6OPxVgmnYa3eTeKBSvc4j8fzqaWNGXYI-M-lQ9TZQacBh8NKW4Ub0qEb8AVV42aOyX5bCVvjoZsCNGqV3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Azsf4C64st8sIpUfBJhVY8TLJ7BcbrGckRn3Z6sjqzgHTRn5D7DPheWf7kmCUP_6_IWZR-8B0NQc7NKmgkqhcyf9izrpMeX7MSYm7Qe5wrlf1psMwLS4OxgTea4eNampZV9Pm4uyLiN7GZR-SbVzIEhy6QOai5jktQn1nmqgDAY4WEFSBC-YhrhxcQEj4PNBNyI24thduN5bgUNAqDpw6VhYSRlsXnaFHejY5DtDf1Wg2AGXJ5oFJCdg5iY4fGz7n2kRF1dpTPGYBlyJM36jBCd--HwJ4xS4jpSdupocCxQvUXeu1amfiquDzGadmi8dYRjSiGkpPTF0epffMT7nDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1NYJ5PEiQBavX8ha4uvDV6rKR4Q5rkIZ1QTzdnHlKce-EDKeTPn7n0mmxlAZFWTgzK3ZGDX0zcTu-3vWeQvElbc87Kx6qNzo3FKy0lXa9CYzG4lSQKQXwngr0DEcvjcA3OJf4Fr1dIZKz8edPsHI2nT0hxrhu0zR3giaNcLdiWfX07CmA-IWaB1x7ZZ1dM6hIL4cwM_JeP4XaQzXvd3Rz8B78RBE1IXt7pW_Jooqb3XULXOPa6NdTKZ34tqG7Ly4-0xMYlZ2iZy5QZb0EtDXBHQH0vQagf_0AbZhqzhR-bLFvBVvG40nSPjkd_Q_wHWIr5okom-qWTNwk9dowfqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BxPmOFE9mpoM5IgICsBVCJ7ikQbVChAo_JtUfPA_-7FaAy7CZGwvRMkO1ZsEapfKhhKKYGXVv46i47CPtZHjC_VzlBgmDkELrSZw7oK4DKhVLXWM52WfEdd6lrr0kvfzCr6pNUJTST_o_CA0HdkQPFoVTmK-MAiT1nchq4baeOBUauFsFinnRLW4m36w4qYjfB8vsfAVzbjdFOcdz-FcMu55ifCH2nmWmjpmR1HT1BEg-AoPfEUY1qE07NgG7Y3Yq9xe3iXkAtbfE4-E8XeFD62T-ecuYVb6Epm4KHasyGfBzfGsTtrkwFRueRzIdTOY0xNsETnE_QuW5MqdDMdFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2kJ-SqkedYEG-2iBB9-fgOsPlQMnzvXIlmrD-VGrMCNAjsyRTzYgIrcgBv6EGXNZNrN4bA_V1iolWJkMzH-XAwfN27_C8kGTSRomCuO0b_bq2obcgPXMQHLwMSrVdgSr0LvhtTw1a3HMYydo5y7oY-HsUBLlDYuEMsOH_ythswfZWZarEEXmHCd7OV8nlX2mkTwJjM_YWdQl2v3PA2K1PdyVS9Z3OjZj-9nECorFeDYWy7C3GqiK60jIKa-ca2CXjQ82o-oHQbyyQ7roJElOrpi2iSPq9vq-w_OXD9b8pktIO_U5MEUge6vkmLr2qZyZ44PPKRzyC1CdA6BtatG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/endThbY3IEiCLYem-ebBvrGyxUZr9FBWAaWy1xKy7ncnR5ZXMFNGZgtR75Do-MYiDaL3Ok8bhIU6sURmAwmV90CTqnfFRjnxb7ljB5R6LMQYvYX8wpEsCcX484WsnmFvQoKtbEvfKEg-DZbK_IVKZ0wz7FtGr30MZB_s7ul_C4VeRPBzfnaw8iMRoQ4QqkZ-O21VAa5akPiOhQNdFBCQblaPwqqYWkdbXpEoPS0KeJZ_Woj-qKsGdqCguD8g2v9eW2tY9ZmOESvYBkxEF9QH-WrcxyhPk8HECaWvvxsbee23qceyBVTWf4nO26LSvmgHPOae0st-O-7IzZHKStgFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6uhDkP5EEx5sAQPMn-38y9OTNtPLXgX5E9ZMJXa8s3AA649JXhtbeKwc7s-1kgdHwVbmxnlOaS2nAbUuce9LthUte1jwwzgvJRuN6eEJsd6BkBCHdsHqQmvLtP9DMhkY9zK7kwLzwntiUjoAPGKKtiIf1mlJVKgPGQEnTBfy5iWXg2T0FFCRq00sJ0RgSSIyt9s5kYsmiUXAQUu5R-MBPlarG3loDGmb39gD8Bl8Nf0WgSroZkeMvKGjre9mJnrCyHFbed5FFoVrVftShoJEpKnYABa_faRdlWKEz1sVy5BEPVFApweeylC_rFgMzygqNnnmTSi4NLyCMzjhbsGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/izMR8Q9uZ48VNjAh6E16QcPI7VDTpryk-wWs6BK0n0VJFq6ehwx91dpNDt-34esWtx2oYx0r3E61V9x_PIeS5ejSEnUvKJealtX4tATR4GQPFjjld8sFUxbX88_7ApwEVAi-CKE1jeBHgE1Jouq-A8ceAblrWflTUi7udZ4fal8PDwoXMs1e9p1i-46DYT_yutby3hecb1nwgnNC5tvpfHmHjChD_EN_TvoOoMerlkkVxBCtE59sofLiay0y1sEQzTu-eGLGPhrkwMhufaNthce0A2V1xvHs0TJ9Y4XzS4AWKia7fJ-F8OiGWVwKeNF3DxBewLFn345WAF6tN7FtNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4ug8DL_C8EEMj7y5iq11elcFDsnszwmVwSNDfNXMWz_VvVg6ZFNMXlVv5OBOFtvdIxR4MBqvZstKu96a7oTYsaRSyEMxww19Rqs2HVjv1-eFkiCo-Xpy7USOvMHgR6llxvlhO_dfXYfjrPes4mf8i1hGcrJtJ0w5ynXrFJkwC0ntHUd10OZu-6OwrcLdZrcuEw9oPZMQ-AMyi_C8F3XaGoY5Ztapdd1k8ou6i-XUW3Mz_LKpJKHok0-3GoHYmkPV0CQRaRh4sokmNfXI1zDE0CBP6UYbzLomwRJlOXqJjxBk0eHJs-7Li_GIpTIaiyRRQI9FC8RjrwN3xLvjvCQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vc1MMA3O4qj6BJ5bzamiZXAC-WPOEjWVMoNZ6ehW60WDn7S2vetEUuHg_4e6bZFegB1pz3X4uQDVwFrehrAH2Xk9_DaI1m4nMNMt1aQ0eiG9KcgtR8_EobZ_3ZheF8q3FWTbncI0oEK-gNaHF3T_3cU7Be2E8SVhR8tQUJCxY1OY28kAY7JarmtsHNLp2gFR8zUE2tK9ZfOPofyK7OU5P1g_2FBX9JcJKFXQMsr73QumIMr1j9gbh1NsGd1tLnSVHPQy6vFWX9BlqvCTVU5BsFW5qqxRwtO7y_RVnnrQLJxAqX1a3TbQymXhuqFjpFurrataXZiAa_cFcSh4npBpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRHbax0XvzdXOL1aS03PpCsF6xwrFEaoUU9W8Om0DUDeBDQfb6bkrjE06RNBmIC4X7JCfkJzDUFiWsNx5ikh-tzE846pLRsHIyZL8PMCKyiMln6uBxN9tgHHrVG6mLeGdVBBEkiSQjAT2DLfjTPvqqaZn8_tSt9kk_71fLqNh5ojKJkDOJ3se-G8z8Q9h4S6thoghiPtdi1XpN4VU1LDI_NWJvu9knoC7z5zTWk2IVbYvFCgpvzw5uV1X_8FdKbYrQyyD8iloVI6JDLikBMxdMCY2V-MyrAx2Hvg1nL1I2tx9EBY1-Pjt8gWPJWnaJxwHXeVLwhSIF-wzSWQrVbsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htYF-wW2KeUpLTmFa6O1Brh7HkFNKgaIIlR94XQKrCaI3zZmk8PRScdxxLANmUOMVSWsv26E0BurdjRGyepwloYMH1tJOxbo268vGn2SmI_J9zZg-YmSxgNsgJnmx5AFuOb1Lb4sB-MOFpdoDhkGdxDWdsXPdlnYjVfrNgUPvpnvzt1R-6coS5_l2L2rAiDt7EGbUuevcL1-rjulBUmO23C9NUIV9Jd2UFvWS9QRuNwcT99bHFgDpeKNd1wR_5OMI8x2TC7auw2hNRC6cZwU3zOTFw65FxicEvfMWpTMzy7xq9V2U5cxBgEobwKKXMVr0xebjIw3SecHcAXLti9-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UffKbv0YAPW3o-Fw4ZFRKeDccbyTJgTgBWfv5XC9H8EXywu2-e9kg3jaY4pFArxFQfch9KZyfg2hcEmriszmtsnmXgFxbvTwdsdQ9lwhSS5YhA6Az9eSABBnOcRUjuC5ssrt4vGCXCt-oJa1ofx1os5IyWXmnG5Ug_CE64sw_819_Iv1bur7hVwEDhT1p-h0l0JNCEqpz50hYeYsJUuc9YsHaRTTmoV9IIT-moiO3J1GM4pYgdybtoBsdEKAAdAz2uC3oANOsCtIVIidpHnHvFpIhIrUCKutZQJd9dTUFfOMcmas3nY1-0ig7_Rmn-6vB9AJWHnQWx0OO5okLL9msg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amsEBYflxFnkW0yEQnphwxPVRo907igBbY_-wiMuETC4IW4NGkYpzyedN03dJPOjcm3AW5iq5x5cTkhxcteLeP47kxEfTZupJ9GYquWPcS_3TbtL8Au1K2Wc6jXuLlSaNsDar3gb0CwXTXoyzfk_SJKBZs1xztCpcB6cC3AOnZg65L55DjMXTK_MY7ZJf_Fpnx4oeBZtMrjU0EqKbsWfG04zQNgMdlR488ktZLCni9OMhJwQUfIjvaHhxIZ1_WUL7dIG2nGdDpKzRdjViAmwTcZLhNulnLHqS3rMl9dTapNeBI8QwAQqQStOqsXQEEiMJh4eK2bPOdsLg-ckc8hMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKWmq3y0M5sIa-qVzoTO6ppQqQWrCHLn0eknYyO8jfbDYF0DLbVWdjVQTiwEyiQeylX1vMZuK7mcrqia1_imm_DhNpuVtqdYFvEmkqDtYx-2HA-uaIRsRWhViKlOd0vqw6ANX-WzBKvQaur5LLuqOFYUuABAZZ45gtqFSnF9q27J0URRTDbhSd0NBNGjbNvXieVaZg7UiM6Oitkb8-8vPhv1bnHiWfZaByJ8xgZhILjHxFE0onwatjc1XAc-krKH5eqFqXZx8yqqndxQBg2yMvUYg8AdJx7bOnpn8YpoRUouuH3BEMaK26-2ARwHLutXuUvFydwxYcF6AdNXwBAaKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8ammKxvBILNcr8PHrdzGGrLlCubtHaGk2J-CF-37_f690TDw7vcJt0NDvgm81UAUBwEbj4uzZEn03xCmz5cYvXYRA7pDJsV-Lz27JP0SfgfFc5rDkZotTaJypLFBHEFceyUseOXAO-s3ZhIru4gc0DZlkR2fvjvtcayUsu6hK_H22PBpigZ5iqcarBIfKfK22-B1kSaJadoQjNkfMfbk4blqcvs9FXA1-NkBDYYcortw9X7s_TK1MIQe0e9JTtPrvZ8zQC_szrR3yFSGf7OhKURYAlSXPqY8BSGTjdDPNqslqZgUegr7zpvJMQzGdk3Op0aZTQ28fLXxq_9ZIMp_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4arwlXw3rXXPJLJbWdtAVEhymLkrU44ynT6R-W2jcn70lSvtsTNBM8PkNlef-eHcbdcVXnioCZzU7mfLsi2wBtkBEySVnXIMWHsraFOQcou_0nJrRRHiPGUmpska4PklUhdcFBHlHynJhlw4S-TD69D_hfrsjOZbSRXkDs6SwT-oMiww9SUIlBkQwxPsHKkFbO0ojdjaJyRiFp1stz1WN7qGdcMQ4BLEMESfuNrfHEBBfcTZ8OGuo7HeZIYpAkpibTPEiAt0Yq5ILnUXbcSfbjy7i76voj1E8HVq96G2Q24ZJ5xsGtLqOA86fWh2Jwrq64iNq-umr0WQfJkV0mVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKNC-u7duTb9BhEXd1BkeqT4iL8aFqMGCifit5yP6Ft2ck0cZsS4lK8vE33mCQ5QyRbmRpUDRuuUji1BckemJDNeu1FS-O4BCvXRfvRJuSPAUpUm4-uo8qx39L5BkLGiA8opVfkgpsabBqFn88w98wFfBc0ua16q3LqnZOwg_5g5WPNamUbrzaZH6qY-eBNtl1cX7wsHpYSLsocv6P3KU1MbTwjox_DikzCWi3tBc7egJoycUo0EpgbUidYAoUNbWF_ZnapZsqukR51qjNPbHbikmrgW2sklXFcZq4YS5P6zD16dm89KpD5XriM66v7c5eW6PZHbUNgLXobEwnNR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1UnVeppBRPbDQ4DDvzQVUyj7n9Lw7rcj3Dtp8hwSsSLRu-UKbqeQ8e5pXXwH1Bu6JRKbHyqUhZFPoabCZI5vtfbsnT-58TEvLsgkJ1aloI1C_fJHIbiNbaXLNECNvY54JCx-3Kp-02UUOrUP7Z0Dgnd5G32cuOuVwtAR0_EUlD2EhEp7bbVVJGz_kGfu-902wgIlK5Z3_XokOWdf9kixkNrHQoCU_cvUX7DyO5Bk7hWL_Cg9hPwk9srO0kDTLRjemGpmTwA5Umq5_eKlt49nhn1o3Plk0DmJupoSCRnLi346kIZTS-I7FhFot25HoUjzPE06i2qzHYIJkF58czOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VM-xhCDBDC8fy0JyViTluv07rkB3K--0GiMKjclFQomU7miyAoZzynfdgKMBWS2Ue5uixSslQhJxPGxvD0_toCYrppK66bqvGjNRuf4dKfY0ut7wvGSs-jh6JhZ7pgslx7pfAc8wWed8E4sQgS6lhLgeGuFnQ0enfPBqGumKb583q35Gzat9aSCMBzwVtWuICtGHDNqI9wa1PM5V4iRfoHh3QJGHWZL9rXrDv5XfJTCQ8Bsq007EKql4hD61bqf8emDpU_ki28l5wwVafOc2x-qIYDBYLsDaHqlOeYbM8uJB2P6yFc7ogyUhkklA5JO428Iqq98N8aC9e92lTlBeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UbR8Yra3YoeZJUdH29qYSQ0kzaumi1q18yPkV4Vj27U4ELtF7fREpgaybcSodrWJh0G052YosiUwIoLQ0fEPB8lNSLbziKms5SyghvP8n04RHlLYrB4YBeMUSsIJz3dhMZOQdXMY5A_ZahuVxgTA18ZpDj582JOKjLlapNjPW-ocfKnRA5THEEj3hHzF3YoDymgRxLu83YDzMlj-cGYLKWRYWkQTdnS55iALhepYcZcTtAEsc7J8Meu_x2QfVV6kSPvqbdGlxUVGktpWAtr-ce6JWdKnNv7JJmKHvIB5unOaDA_tcI7xaUsv7kxt4gGRVD0pVBlUcQqAcbvc1RmQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhrbuVEgREuCg1Sm2BkDn5NlrZ1oZ1RwtsjYOYRRCD9i3Qct1VcgxucRM_9wQDCMtZkxx8FU0C_eYVjoEsiB8zOFC6omkrqcJkF4pbCmYo8cMZdcxwaHEiYvt8h2tdU__ZHzGmSDMq7gWsrWlpsiLtTtsNczphlEpQB2BIlS4BQqiCUxmjE5htSYdmjn9QL-TozFKT7-_qoaQ56F4FF-FEQumUp7Zb6pfakfBFQPLn--_fFCI9YczzWdji1UJgyJUuhqs7gU993UPTRuEnci4Pr-u_P9YiaMfOcI9rASj1OFXsOdF_ktnnKHveX0UZI847h1n278fV8CLJiYupsQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnVeM56i0KuudovFu9AIdEAxAScXjkyB8vRReR-B1sBc4Ov5UO8a-c1XFffsn87hMLjSk1_8FhjPOtUKHHqRYCoLIZudIQWHBvjE6pMcFFPQcE8LWLArU5977TsICpHc25aj8fXkpcgog07ULlKD0r7g-Y_tKRivPC1WJC4H9KPtglbnFHns2XAFojszJq00UHOKivSwb-3GsUSCimBK0sMpRpLmK0-TbKCZ0Egp3yQ-xKxGXs0Yr1ZVEz6kjRTcDZy-uZUh9XGzbaKMyjYYIKzkOXv5itT2oCIKTRQiqMIa6dz8hHU9uNh8X9FlWZgWRriIH_P8X8IGhqC_Z6Lr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJpVcwWOR8-vSN_jOi65ZG0s61Fl_X85fAj26_gFJEL0NZ_tBpdWMHFKNGKdhfUGm1AEnRUAM7hVZJR7jQrVKARfGSswD9ER7dkGe07AaI9GjGfTtVloIXcoDis0mpj-05JqmIrOYE5if9V7d37dl6DZxQpLisyh9fD-iz541t6_jS0Afjh1FrcNQQAow2es41hP5wF7_NL8_iqlcuSkwBkz6OVIEGkAKLlFaM4Re1y5ff689xt-tv6KxxBDpn_wejn4fqnRv-XOvyPtc1Gvgr1p5jSN6CtQpQaHNuDJgUOUeFVQy0jFBHlhgivLZr0VGExh9QFByGKHpxXrmbP5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fax76ShZTjI3DpqttCttHVd0vAzL2YJmOMCxaxTj0z9-OG-cauJqxDx0w3xwFlr3W8xGrrelgNYEC0AvarRm4B6yPraUbuPvsx6IGsURi5bWi9efMnT0GkM0OYFJ5796DjWHiDbFkwdGb_lYH-stSXVzreHeFCqjN-ZFDVH4otYkSXxdqihFB1rxujbn12RUY66LKbBYLYyMUmBrofHNyvbbYKsLs6MSCVTUyBhWEXuww-Cep37D0yWOeRckiXQAK2t9jIXDdQ5Yvf_yuAdhWpDNOv7cchtyyhmzITHUT1RlSwUAVcD-r4Um_1APu_SO0WFqOSc9DowQvsgtlT77_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEdTickSpc3uOlUaN-cyVKI4fZEXMd-Eq8ZXMXpx0cf_EOlkb9xDjp7nfE5Vx03ayU3DWD62Dobp0B_wzU4fvf2cxPhSHUz_d1TNJ_sc9XgbIKcHWmJ1h0s2nzBw3g5lHRgcPT0DERvOvAtxIinONRYkSCw5jsFYukQg4Dx4Em7W5f7sXyzBG0rnEhioUHiUTf-UXxLQuaWlinU4fA1HC2job_p1AuGbiCxFr3TOpbw_RaKUzj05EJ95ziO8Ds3QXsADP8wzUCDuP1IxhLHyyUDgNT8Yt6SekifELa-sbK0B-c-Hdu9TknWGkM6GaKAQNVx7Yo1Wc2ySKrmn04PtsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SEZ4T0leYgsGM5tWITiA1bSnusqAj9i4LkLaizGbq94UCB239wmb8Eq5Cb9f1MPi6HxjIVVJyCEDEKf-GKVoj4kZWccw8rxEQwBgcGXPfJqAC2h-6xizVS6oa-N0GPz0l834SVazKY5AQnVacaNg820DVayx3SzENn354kMz24HZymXWFTd5WsbZHhcolAz3VeLQzjflEoD_Q8IeCUn6cm8GOJwYg0ve1KucjxbE8aa6x_R_lZB4sdBW5yrrnR6LCanoNZ-TWIaUMIxQiqCOqeHmLEMmrNv5CF0n0YBafAfDEyY12Jk8hPHdq3L2zLOg8meSRCzUU4gLVcH8MUkTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHz2ZhbFNilrL4wG67hOCJE4wVOWYxaiUFVid7XU6fyLydcuVqFwoP2MbmqImYeiUJXBdOwtV8O7JF11MKerqgzMly_FqhhPfwxiX3ftsIi-t1YulwVPF6gVXYvbMtFeNLOWIS_OYxULkqCkQV1ecpVyhwzScLJHyElSil3_Fbw1Gl79psHMOhqke4boMDP256bVPCMrCR3Re39MM8kwbH0_UL2TzoBd-ByxD6wT-KSdpE42c7JWv_OB1dDAJM8efiZSOYXdoEfsgxqWpu8RVpBPXW9Z_0Q6n5ipGhkn0gLeIJAyHWGUGfXAgNmIG746_93pjFo2YV7Au8aeQGkiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTiz4Z92f3P26lX1y-SfTlDMO2xXbtD5leJbVhQF64Ghuadu8T-kQyEsb7jdrot8ZTgjQ1w7cNVHpQviXXSMnatQHz0CABbVBcNdNuTIfn8dqvKIpAxP23hp1YKTlAv3bKd0wSsGUn_w0FpxmvOnQ2x0-O7XnejHGmQbsEQcgLVS1bjheDGYknVp5TDh0K-tVI6Iz625PNM3eqRmtFnHBTZ7sl4Gj302G8bHrIM7AvqEa-76b03p9Cq_xJ_5eOiBmx-_VAaACfVzITR4LvIoTe5EH1Kwv7PNNtCJIhsYYsBL0CA0h9dSYxew_aJIb5crvRHkphRTywATDt6-Yjnz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=nz9wPF0uy5HNF3jR106lO3dmugD7w3SvtRJT6KMoWdUoIGYT6UoSBiiBmZPIKfYEoBhjdWFEHr7HEfRFlk-lieCneFlhWnUONwhU9QCOwFwK2aMfSnRbeKh_TqUu_hoY1EA24HC5mwfAnB462lwOFASiTIaJEWEs8suEhZyRZF2J6ZjAxsKc47yFZZ1KDq6VZWYCoc1rw22nWWB_SvCHuphpbfx3aE36ZY0zV3881ThJKYnh9Tg_vLBs2oEAHOYELHkjIKq6IpWh0cgPRufo-uHvUYvXciYQ4UlVAjqxnHXUM1cwa9mZ9YJx2PMwnpiuIrobKVjvw8rI5dn_0hKUCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=nz9wPF0uy5HNF3jR106lO3dmugD7w3SvtRJT6KMoWdUoIGYT6UoSBiiBmZPIKfYEoBhjdWFEHr7HEfRFlk-lieCneFlhWnUONwhU9QCOwFwK2aMfSnRbeKh_TqUu_hoY1EA24HC5mwfAnB462lwOFASiTIaJEWEs8suEhZyRZF2J6ZjAxsKc47yFZZ1KDq6VZWYCoc1rw22nWWB_SvCHuphpbfx3aE36ZY0zV3881ThJKYnh9Tg_vLBs2oEAHOYELHkjIKq6IpWh0cgPRufo-uHvUYvXciYQ4UlVAjqxnHXUM1cwa9mZ9YJx2PMwnpiuIrobKVjvw8rI5dn_0hKUCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kT3aCA48Hrhk2nzKk3ipsDyolpcqKt1YUjdrUVTHbtKqZ0TeVAxSubXv2o24EhfodB4PdYK_COQyILFs5D9VFHd3LnqI2ktuYoV1BtbjNkbeF6O9CZV3qPQeaRh77cMwVKL59FDVtRfAsh8KkWQ7mGB73dae9GoQuGH7LRVVCmQeVic4_0schA_GCH-zCJQKfmktIIHLt9Ps8VTzewcgK6bYi-ceOu_V47fhIexG5c8tuoFEkaM9UqTFyEimJ0LXgElj6BQVQs0Wx9szTzMrzogwsNI-hIX-KetdOEP50A7xETVtuHS4azFKjW3AeYa2knz9TCy3PS4XLlrh1k1Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4O7XvEJZ9yib8uWiFrzb14aE7gTQfFMya75t1ySAFuIKDqdlJtmEWNl1pU-YekLyEpqZ815bD2TeiTJDfVyRuyYSTdEQ5FzIqX3Kf-wdIgNqAwksNgUgkBPYHdA_-1iBHfedjDRkFj1oPF-yXPC9rAGHK5hZToSH0PpgBqGN5xehk3DU7PFbOggoRSWpGqsn4o3d6ibmgnVQZHWu5-WpsknnNuXepKNHrAlxD9q43tOhruLWXoccdYJSOEZHWtjS87NMIGAFhOvEn-MBUslUEgD6tCxZPr7wiTKlJc-asYiK7gWHeyZRjHL_QFJ13JjJYJ5tpIyu8bGwL5orYYS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_uXWE31_49nzCItJZVCmzK8iOb10y0UW8VESBGoUdnTaYvzXYLB5JY7Db2Q9NGXBFTAyPoDCEhjpUIfq-O_k-xq_f-Sub4a8NUD6-n9_3Vh9K8DBctBwH6CXdCk5oNx9RYUifYKtLYs7kxEIZ44KBSHwgfX1N79pVXNd2hfHmaznU2DFk37MHn4uW7n743oHKLxoGI6qTDqfyaw2Wuc0N9ERZYaZiShWhc9ECkn8gLWM0SHGD4VnziKz7CLtdhLhNWyG2Ge2QJweZ8MaeZdWaut7LSrtzgXXLPb7uU75KjMdtlBC-xNpSJ6DdIbQCoie8iHjwRYZWGXW3FlCx7b7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/altfT7uoNGJ_2CN_tDhNBHCFzmZGnvQggtMe_EF7zMKyO_vByIOh6UrWBsTfJNSDjdqCN2h3FvN8qob17KKJ5ubPu8vtpmHU7b1T4PQloGqUDWm2w_7HrwBhWFLNtNE42rhmdtunylpgHRMWCexM1Uee3TQuDuAa1hfArdYSySbi4FEBYTvj6hG3PZptNRG9jbsNxJHGv1q3ai5qiTORspJQxIDUkvU90yf2nHTCt-nus12TIJ6AwF8m5lc-cOY81oVRDrXSJxOayrpWmi-3AcyEHdbNdt-2DprBzpIUChkz-NaPzoecZCF2Iv-GC31kFfIO1Oonp8uE_CSExtaj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVLMXBzQvBKZbQNCc_SjN1yWmOADxplZmurqeJaWPzCZ-EK75jUaHI-9s_R3t8siS0twfTD6cXOCzdAiRIEkTyFgKPt6gjWvisw9WZKwbvq6AYMa7keh72JImnlG91x2zqNGJyq7EDhEarVVINOs49EDLUiZ6XT6o8lUclcJmJIkTjZ5VXGBpK0yDpSBDdU2pD8KTo3pwWk1KX1cYiiPOCAy3bIkIf-hDVaoJroKLzA1EsTMruLyroFARIinemcBwSTc2QX8ri27LRZdy69E9fDOmV1Ov_WcnY_2UX5xbKDLZvSKPAfXa6CnAweVbsBJQpZ1k2rqgmIH26d8-xHrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btZlecxX9Hsox7rsQ8gb5jSta9_6eMd4FU_olGc0dgNn9S-NUI3FeHqjRnvaE7L4ugu1eMf0fV24pwkOskm0UTPSnoUo8Lg8d73LNYUceHS1K59rSe8-sXyQgjeWgnuMmYxLoP-JU6OPAEMbL5_2T1lC2LUvViCIEySJ873dh-jj4eMXeM0537K2QxhcP5cCbeJFGYzJVt5aHIke-DbRpuRn4KMfV_kx2rM2kEOg4wjYN5Z3i52nIgJ-HGWj04XuGus2ngwcXpL3104yHHF7Hz6FHwvqMX4UxEnVen7FWjk5nYgsKaQpAXsXiCrNu4q-duZjmY138ivodti8py-mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJnuQBSJd6tZULw15W4kwBNCrh8z-P9DdpCqxF-4ANkR9xwzo-KCpQwsWSMhlyeob0RI0KZptsL99ZHpTuPhUVWiMfyXccmrsLGqg_pDRhFekXT5AUuW9aRHhncZYAkxdSz1z_-Dr-oW6kgT8h3KRXqfge7Pi2kT_bpG7Wzz9yqAqXGwAujEQ5ZGodLV1l3qIL39c5cGcXauPTCu4tY72xMvSOjq-_QbjDo1gHwRc-lGAp1Btp63wAuKCQ1VBtgsbyKB8fqqlIkP-6_zprVTknhKHrx-iEva8J6E-KzZ2tSKGPf5-tYWlxushEE7XJWQWIZF1ouHMa749BrUPvXUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqy8Tazzl4ufNLET_DP4iMEmnCCQrR2-BVOKeI_ksVQTaG-GrsQ_W0i9WJwCUmmqtFMz5ZBT5vgCAh-OO5jXVcmue2LZlrFbAJSy55-hwb13ExyZHluflGe4ZetY2AZHfKVDoJgX30Ps5RTt0N52Q4OjxkMxqZkU8CgF0LNiRWNEWEGRc6y3Cd_MF9YCjYrATVKA604x1CzK7ktYTk6DVsTicUGiKtov3UdjSOvxpvGrg-o4DCSBtfTs9-7BNBofiwlyxc-_4vpr66Rl8BNGnsnd9QpnsDBKfzBIBiugSN7Lqv7R9klXYXWkGMfTgzSNmWY9ZW57JCa59JdsEVR3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ouvimwbeuKzecfyrD4Wypjsp34cTO6_Sbf-klY55eMBszSlDKCbKULJ6rg3hCx_jPZoyAxgelKAYMf_NNfSx-TLTc5gNC1SBjT-RPiThlYFBbrdT-yw-CN25dPE3SmMhuA092_jqLHx-tA4B2wXh_vkA_NEIowP4xXkJlQrKroxw8D4HEJBGkLvlZx7bAqPG9-ul5ngXtk8U9dusn_z5Ioxf9Q1YfUDWMkAmnIJ-68KXIl_rTXODMQjVOGnD8K491OiugVCnAgROi-RmATqfVKs000d1vSS9_cH8eFtQRcqq_EimY9rYxkxXvWOWIAh8AoZ6Itqr-upGQuClgQb99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UERdYnRq5nU9uZhpJKj9mSVigdrjx8wcekIAEixM_TYaRCS2sPP4FLuved44KBClrichLkS9Up97O5zxiOnK7dniexujv50auI2oOZpnr6seRT5vdmgq762Ff4L2v1y_ZgrcpT8iRq830HGy8HfesCZa5BwP6sdGI6fXmOql0tx48iUGizY8MH25cCz3OnfE3eEsOAPN4zZCUOZWJEI4T9v5vmlHzWrhHLwZijoQs99SB0zLYHZkPrY--BbYwctDKjOUDz0hLvrBMcD8PUrKnPga6YrIFfB0QN2xRevD0jQ345uvxzXYeQayyvDRLNtRBFVfpxqal6mIXcLCRqKvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYvG3tn7sCRtDauygtO3N7hYA8qAI5A9lOs3CyPeaByHDCCBmhtEwJ0Tdha2uWq9wpW_09BXiVzFLPN5-G8Sa7-ztefNHiuQlbIyQBVTGHZVBI1w02dOUW8Ndn9uw-_xLD56YTc05R87A3C59-WtMV5YFMadNUbn3fckvjzgswm3Riw85swSjRqnpnl2fyLTWDgCPuQ2IDtc_YCK4CDOlo240fUYiUlvAXbkQG8PbvWhh8VXkT_YLXnbSbX4vUyQMx0OsJhy32EtSUcOylCZQ7aYetyJ7xnCKFP_KQI6esaqnn_siKDG1cxonX5TDVHLhHv1E0Eo6-wZcU2jGklnhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DtxGPaxcZ3qJz-OQThaHgt03WuxII0CWhLgMI9ChSn0wqti69CihulHaeoW6LNrewXXXUs8gptwx3BN6TaFnsfeNkcq2d17k2k_xU-SPU5DUObOfsjq6ZyxRJHJEFI5L3vuKhfvf3kio8lGNo9-ORNkPgUbG20Y74hHKcxXlYKyMm4HaknmDDzBuZb9_iS2zFdYSGxlyCJDzSct6GKnzBZRdF4u7hy7czB92bNu9W5sHvWm7J3liPKky2BcsXaRBmr8e1jOUNT5nTdUIlW76_XTGFkiwGxIpKTvftDZ4JpzDRLYSkPy9qsqlCwc7CsZyzJEqhOj-UJ2PaB1OKSi-NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iShg1TNt1IMkFUWCU-9k2PSXi6L2s6RVs1IGIp-SEsYOEKwaI-5_uGeEfQFsnLrVb_VwR5pFNVO7N4zs-RJ7KqamKvcsQmWNNWt8f4MTv1TkjuWg8TZlOyXcLEcNY5fwmu0ifwC4sMEMXVIYAJAWFu5VxXNREueAnR7DCsHi3YyYfBz17dRnBylRpiiLni3OrnxW7iisRKP8KTGtlpQwKKt4YAXLN2TtEZ5BwB45U6kg6lFiqCxiSJjMs9qUeeR8GszfQJHwlmPAbzRCEVckI4Sfcq0em3PJ_E-e-VZo3Ou3KrspyO_IVSrZpKVOFIrY_h9oxzgyz-eC3x7cmOGQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zafc_-Kv5xORVBVDhZrYb44kUSdaBE2T3w03saMv-xNfJixIiKVVO9SAxbQRM2rjybKKM26HyXcNFhJ5hiAvPJa1FD3JXHEDPBtvEAdQgnO2nntKUhzVYMTivzI-w8pSnF2kN6lyF5qOeYHtXrmOQi41oaGG3E9R2NVqeD5gGLWF8vu4fnXlSOlC6M0I7Xl-vbbbcv-fqnb3RV9HLnS4GwWDrIC8IUN3arBCKkZMA0RfGOcWJhu4LUDEmKWNlDp9Hylxnnf8lgAt5JwkKEeJRpPlEks3SOf1ocFlVuTUuf4nyz0jr1q5BEQScPKYUuxT6Yu3eclrWEOY5wexhfQ2iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUCHiRVyeXUszC7t60cX2CAw8NJdZkzkBr2lquC_sxW2TE4LPovgUNXbYzsFEU4p1vMWnZ5EatVS5o6SJOy4_TLCJy0aauYOSZTVtXHA1hr9XZdLfglZUuWlheWLhRSbw9ilbMvmKvyWX0ofmB4t4hXWZT8GTrTv09-DmMZpo0DSCivX3hpxjaWEOeuBmjkYIhLi_GY57ix2VkcNzntuXNZZcUvWtbkgJPTaHR2GEvF_qGpw49DBr-ek8vRkDs7fDkepOCkON8kr_a9y3Frcn_UrlHdJ2QKpOxSXeJcTuWcvNBJdfSvXCjBmhGLXeLLQLvdahu3raeJ-a3ABXT4NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L88WEu9s3y1S4uCLtg0KkBjG2VfMlPATNmkeGzGjoAwgtcvfuHQ5s9oHnLc4Vym2Uv7HfpBxaOAxRc0UowHyMgF3iMF-lpLGr8G5-Lu8nfmArQ2tZ-qhz_4qUjk3f2Vk5jboWtrEBtxdZEbNxFuXPRflDGXcqxvt4UtGZNmBpRxiDaIki6G9RSYsVyQLZv2_8n2sOEF7wBhuxmu5E6knNEp4Bf-N50oK_xDQn92HdWlnLcyMMFBb56wvkNO0DcDzLhJ9oxj_lKrtSWkG_szySaUBEQw3ia6lztrdoI99qmim5eLEAEkkpv_fId7l3pfARDXzjHuUQEQWoqMrnhpnJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uzjO6eSSef-Cfz9GRe13DTsijDdJ9Dt4V8lkE1qnGNoRlqlGAHuD6YziIOvkHyumnCq3hWHWdzO_Uyr1uwP7RxJ0fFsmTRa_kZY1Ps1pmSlOOrqq7cw_edeQyvVRuxk2G1EwGBeQx02_1JeMiBFDNtOo4jhbK1gxrch5AORgoUXZddaw3pm_zgR_MpAVC6R8K4ujHVqch4WA1OUj2gRnmzCxFgFlcIuNwrx4_GYV_HCr9f27jT840WegHdYyxItfBERw_Z4vfBTE6DJRvSapOjP55sifsjIwkIxuh2_WtIEZ8b4yK4NaFJjiAz5EqXlyMZLwh6tR8O9C4BJzO1bJig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJbBD2_3L-Zn2dMb6uE6_RSh5jLm7Zs0sdv7pW1Jnm_ORun3iRC49mWCXEHRIijUjPeLyhlkZWCSfjn07OPQOZemcFmMh__PhVgSPxKq-zgHKtMd1KxDDQvSdqA-g48rheXiJqfbm0I5bBQipmxzv2HiWtvL2IbBmIuRfSbOhWH3KU9XEz9O6sU8Q11YtTCrxL4IoBYZ7AXO-aMtJUGJi22vFqJyYK3WJ3cKjETSynGCCMFBl7brzglF9Pf2N2RsueS1HQ1IZhoZJuZcNtQpJ7tHlj_LwT6HOa0QxzOU2Ft7p-G-sCWHwgJDYrgSDau0ArCdNX5IPVIAQQBAXDfhoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ui9B_1pqG9rTIKgwuadAkhQ23qJv4b5x22Enyvbk6HdxrjeCW6gpHwwbGwjQSZvAbqSmBDlqxdCFyAhrgCHWa9Cwt_ZAtzEh18QFXm4o4Tv2I_OGuPO2lz8Mt12Wlv4gl2NR9-VkbJ5j9OeBRbO1GEoYDiRiAg5LU-1XWusQzd_ZBAnsp9zhouBj131aSZB2reIAi6SPGZVZ0lZ8BZYUC1mNpuVpF-ORJCbKTZzYaypzwWCAMOkt7kvBpNnbF9IY1n3dw12Fhde5MFobkoIyhPQxVRuUPX9F8xyJ8hUgvQocaIghM_hE1A4b7FxyidnlQpO9rTIka1Q7jmYnrCvkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-AgFUZK-5aE-nZJ3_MU0u3NuGQiqTKd44zdqcVufJeZG60X7XgxkuTtBHR_-7cdgZ9rb7Eneua82bW-Rz4WA0hFswGua5HqoTVmsoqbMSyQh9-ASldmc_8xuJP3jg7PKCWUS-kDXw1OjJmbjNpT8MzTVEYuhWeUFOXRzXdnR4eQCQvVJK1gmLZgYb3ZmYf1JMS9TJEZqdWNPa5r_QEhD2o8FUS741ZtP1nYklc24RjKb_2snMgc6jO5vKlsYPEO8eWDXrH4QUQqhTri9gLHi3xqm9xe5CVXp3xa8ojcBdfBnagypvyhDGRFRPIpheOKgqXh4BzXNtQSdL-go5t_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwpgCLJSyLeziVXy8laj-HHXcT3PRtDQS49-Ba_FmqJtrykzW9yI97jzFuZDP0EPqCqI0Cxb4haPbAf_zhOEMFTGZvI-lGltSdxc7Vg_0KUaM5pUAPCBnr54STAV1xj-mpgaJeu2MVVm9cRvExOPSQN6W-Sdk4SNsSJHvWog1C2WUKPOSoPX-LgZ6SS0WxvzjoAKJ83mxWt-9mQlrDzxyc_TvNWxg-nKUoLuS1CEmhiLZWiDLxMv0o7cpDpUuPpBsCtaEUCueY3ux3vH1oH_C17v3Oy1xxyA1Wghm-AJ07N1k9TpFfUb5qLQaAVBE2xEU1yeEt4u9Ap7Txu2_tFNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oic6Bw5iOBECmcwj0sNIlhZUCjgYseSp56MDptryND_3ntTxglcZYzjFmF1O_RmUh4QbiUJ1tpkhPY6Q7qqty3vkOBr5VX3mLtvw85UeMZyuz6rZWvht6EkjVGlPw1LQ7BH5hK5WRqYIuVZhC66stbBAX_ssiDU0ZwCRA8P-g1GokoxhbEY3ZtbDzLqDjmGikzgdPrYQBvZVMwjA0Qc4VLxQYM8BTWoWBh0wguz4UwAXARu0YLnDT7eL9rwmFX4fatGe3vX-KN6cr94WXIWJ87WcKM7Un3UxRMmuKU89248-csbAZn2BEM7Ou17DByzka09bRhiMaDpjXtKFEeKSXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPMiiJKwWrM-nyKkrsP_WiulMK6fK_-OFN2V4oqNO4NKKVOzBSbVEqWTyLkLGgbLYjYBhgKRUC6PGp2N__NvBOZx-Ou0P2G1OtQZMoxS8dr1sMRaNtyO6rcsPoXdTH7_NHoK_AitLh6piyqmCIOPWl0calVyAnqRe6G5d1AcvCyksCCkk8oqFInbyBXWZmFAjeYcxwwARdwI2AC3fPWTxYQAHzda1uPZfzsCyd7dD2X_rgoNVQvBe6MdIMJrGGCBinB5cFJA0lhnmQA7ezMVe3764BzBbVp2oXuTgP_PtNfChoKU13QHMMzkec5bi3i44gXCbzwHDjZ5PsljEMRWlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RuqyUwmxkMdMB-jd1gt9wR0aff3YvNTJ5vq56xiGaDbnFwgbV7kvCgXyXMnVPFN9lSPT2jR2AfFql85LfXLQNtfTfo7lLUWeF41Zbr01f5XlVuIjppYXktQwPdYJeDkxhR-OMu6s2IOsbxia01sFtU2jtQzYIy-O4wUUrdpcf1ifISb844KYahc8Pi61arpR-136lug8CaAD1GmTSE9aXLryJH4LZzQrrC23S68cHReNf9Vr5LfyaolLGCSU4FU7iQ_RP6nMum5w-CQx0YluiHLl9NWvuA-kIKsawu7JEuOMV2_q_aspje1IJ2N4V0tDSujIoOd_c46-LsibtDmBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVpv5JVV4qPSPsVkVr0oQAOqk1M_PBNhY5FK1184BfRMIGsp-ZePLIZcGEWTbl7xzjHckfu8hGvHLid1EkaIrBR-xbXcRGWBe-AZx_Qf0eZmeS4R0x-WP4vjPFJ8K1ixSUUrg5xUtoi2pNbGil4J5N4MmgCcapD4W-EmqobTgjVA38QavaKLFghwZUJgRZWyNWK2MKuRSe3eiE_QS0ifWFisXIbUSXmb4xQOJEJoEY9vX3ec2LmP5d6JFhBQBsH5kZc7BfPmMIanndHDYIu0iPuB5Gw0o4ExYdKyupfgUaxiG-7XmlQ04eLItcV8HlGdwx8Z6uEw_zwvGUANPBXrhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcyRlhw06STAWvnGOzwhBvDdI9C5k2sQspAVWoFKgv-GgOK1r6aVMuwLHjtjQcwN1BmGB0Do391ElB3Oe8LocH5pd3RXoUUyO-L971i5iy_uzJ4QmpvzNgnDmixFo_GKsfbGftHQDOkGn-3ecsEmjcHPRRMMvOuUs3LL2xLjnbiWJUr_q1wrDYTgZseu9-dBQ3RHfKIayBCqNsgyJLMH1Ns86ZxezAA666Hh0NeFXfWjjA6vSz8FiES8WxFA19eQK_3Q3YsozuO9wzQJrZxHMUawiIpJ1ipRFZDt38LVhYRKeZuuJD9Y36X4MBmFm-OGhVW5mPkv8eKJ97xXmV9jrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOFdPqmv2mnDXcar5azl-QPrF7lhib3zzLuEKKH7ktvk3m6NBvDWrnAZXJi8oMqE9FYcj4DHXdpv5jB7KNN3AQbY9cFC8yRtjyEFUmMpAryBMBexd50UG1G0j0DVa1plz-_nt8macH8cdQldH1W3DRQHUUV01sCAQKJBVULmySK-Q6ikVD-UR8bnhYYA22kRHBJUuwd12e9yJZN8RnIY2gcdKvY6oUtnDu2dOckOyCkrYwvM-B2cpgkMVc9P03yMAfgt-JeDSjLDHWSqGjbYZoYml3FeiXSrsLM3h51CFPLRMQUorgk6W-O41iziCxnQOHzm4xcMqCJn4dX359zH9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAVXdPpwfc4kOmP6iqJUMGm16fiWm3bli9fv6E3kB1Tl6iIhvNVQ_60twLW1G-cSYBP0U7fb0fBPwVME4Zcrl2Ggb_57bVALZXsjwC3UOrP6swKvRGM1CvbhskRljyFgxGHnIR7SFW3WWn7iYQmP3K1IjOgHvsdHxRgFgHZD0RcEKqz8zdbscGBG18rwTn92iFa1eC2Q6hOSMCqsOzEiULs04YSpHRyyWIJ2JxrApfbkc2aqnQJUNXBbdXrGwa3OJPBTlN1myUwgON2xBbYAQoohdPy92jQxUWpm9xlDwhoKL9E-0ujFR6PVIMytf1LWT2pF-aP7eQVRrlU9SbJqIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

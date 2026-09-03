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
<img src="https://cdn1.telesco.pe/file/lvHY29zhgXybTrGp8iHXinG4MYHwVSYYcBt9Sj8gECY4jeVftFkH_k1oddSiMP3-_QfJPvf9wuLS2MgLq4XUHNlrbk6D4cmlSL0zcBZgofCKwoJpUZ7okgg0V9mHe9ATQpTFUhPUV25zldeh3vmAghEeEHKNENID4WddL1fRQc3kvs5U3IUKHqq7Y_51zpYLitAhnOIH-MWbVos7BD3rzLE6COmSjjcRkDMRSBdmUJ_H3R0cnm6wAga7JouE68C-2yoaOUJgtBD5GjQKTL1v2FNQYZrwWI_q6O0iyugwPvqcqDgBYY0uyeHU26zqilD6mY5dFImGHiIC4ZrQQZgNsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 03:54:12</div>
<hr>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_XD531afGut-1Rk7pQS0UyQwwuqfMC0toiD_Mms7bvgnuBilZlSVOqWKDcaWPA2is68uyXjiVwOdkvvjhv0-tjW9MfOukczMp9wCkVJKE5LDkQKH2RqwSfVnl-yvf2ss0f4IQ078jv7ehwAkfM7kNyeuV0UtO9Os1ZwPBtUVC0LV1jsbuAbT3XLx_FaC_cGyt5dGVsnmm9GtH9Oguk3d-dFV_utVbh-lxiuPK5mddZek5_z0F0C2dQOGhVWxWqbYGHxD8nBzuZFl8MLxEGmRlA4iZjYXHVzOrhPSqJJasLZQQcMmOx8qq2rm-yF_tWGLH5O0H8C4TN3HiRE0oh-Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rqj-ah1oniy923uMEPzgR0WKR9UyYtdpr3l-aUqIMXW_u9R1QlXhzR_KceyYbpAlQeBp-x0y-QBiduO2r_zfCsZTOkotzCZzWnJ7d6CKQb-siZ9EdaR64KJ24kxUlnM2nNJ6yalR11h91SuaGt0IajIPh1fi7yi1H5X4Gp-ql9TP9Z1iHUR_aCEtvyNdo0CgHNKYMUOSPzXVtzKcwqQOH8ZlFISv1WFodvAVnUJf9PrywCMLR_nRSnM48UhT-zuoC9NcTpZ24JdmZqKSfMVLz2mnWacLAasZMq8SY8BEBT1GtCTPtCZFJoM-ZMqaYC5caED1OqW7PINvwKzHffEzXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VRkMAkFtq6jpG_NnF2BG0q5MfFaz3E82RFIJohYPfV_JHd44CWnrPpSEjFff6KpZhuR6n68Z-5SUQa8CBrkTumoVrZVh4dWlM_VSZaT8J92UDwmHHDFIMA-NGzep5aFtcjy4mVLNutM1KyBjV23aEGxxyYjt5VOciycAZhxaKvq3qCnU73-8SBssoR2uENY_IdNmKs1UA8tNxpqelCnm3i0Obe51bbM6vqYmR9cmmp-G6S8OkFuwbGoZKjDxj4A-_ykcXgkPtAhFy7GuleWci4svMZ1GCcQVF6hcAPBxdF00YvK9dGCtKAC3DdqPp5xcwf1b9nkBamG9yG1jn929uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/by2MBqjlXi5Ji6Nm74mxkCWLphyQnC3vKHoAVec6R4iHI1OQTd5Uc_RfLsjpJEvfJfpZY1XhXGOvua7xuCEAHUcC1MJ1J1Z7_Udi7yvWI95lOO7ftObyMgpXveBFsfzgV_hf2CbsMnfmvBGH1KKyJM13CvbCumcIkKsZd2qkXEbxkHTs9XqV7hA5uhvrsOKGpNwNG5SgoEYahSi3ThbjD5rcf8RCleXrYxQZSvQIaNze_Ka7Ko5uHpiZlmN3ZVSUgSD0rvUpFO5MdE8wlJhFX7w6K94uuPT6A-f-egY2gLlTUjG-ty7KIs3SsoCJF6R_lAg1UuhggMU8xgkadsS00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVsSpA-YJY5jrKcAPb_Vk1sZL8prjofJFuiuZCmlHr7vRQm5WCr8dBtF7_HYwton1DHk3rIiAu1z9SxOgB1FWpCXdu_QbhVphJI8erAL9FFpJONlnH3ceT4_VyC2PLuWK3LJFU6CIzrdvTAFMMaL9pdREu5sBhSrAIYzItOAmoiVjq5EfI2IS_sMBrkmysmF90p-mi2x5B-Z_lOJcJkt12U1AK0_RjTlFs9tXGDz0Ovat3NfCu4NGZZS8TEbgXEC3VUZBaKiK9knIwRhqa2XW3dUswRG2fA0FgpN4VEB3AJcl9Dy0Dpx0GhPEeg21I8Ii4ZJzDtjiKFg8brg5Y_ZlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B7oT9taNAsE8FFLkV9w03jem2d7pox5XS5GCGRaJJE4AunsJuUcC8mO6IAj48PHtawXna4vXLXAIJlcaVX2nexya6VxdvoVAdEgnywcRjW9tYBHiFs-TNPVw7g1nLbA4IVKyGqahnSeYAUWIjTsp3OYgdHcHyZs2l8GaohUl_j6WW9mXrDv-teFawYJb3SSmtG3sMLkLYxo7eUS_bO6zGTLX4aDSR433Oaj3AkTaRqIdAm3zETFgt7S3l2rFnKGOcwjmgtLUDGcyJ6gW2g8h9oAmJw5Cf4l0Mqb6PIK39Nl7s94yELeVSjyFTBFKJRvwqvruXUNkoLz8g_cX8U-Kpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGmb5Tbbuife_maPB7inAA8yYJaMmuv93UGPRGRDYV8eMleJ6YB5zE8XdXo40wjje70qwiZrA6eQlvxIFyoLrTMtEjwQh5C-RQKVuOgdlU1Jc-kzrA3UhLv6ZGmub5PtQ-onje1SXkmjSzf0dZqAkSdynnHecqic422Zd9nrL4ZDEj-1qjE-mWkRY2Y1fxS9MhwZvEElVvG43DiR4Ar-B6EJ9uSODBiocoZX3Mq_Kr_xKOb8bXUdeFjc_s6aMcfAhG5l3r_TXrtvhM-Txxhu4zOKV7nxG_9J9N1NxXWdgsxNc_NIoM122jXvcWyTYBAiHBDz7HThfin5mGM8bYpjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXu2RJrKZbbr5NbBVmUVbNf62RfEF_GRMmk9wDI2a9TnHO1Bn0cjqJlOmpA2skEzlOKULzBUQF27X0ppjqFyHTfaCUvdVRGfIrWY8U3HTP_3lnA8N-oqntcf1R5sNhdISJ2ryXh8GoaaqythkCeAWEn5CNakrhWOA2X9snegW7Mywq5lXw7gTp8qcSaBzDfCk6unYM31CSWNX_nGtSuIV4q7aMlhxLUcr3fLIZAWDSYKg2xjW4DgTRVFaDH-DSyhNGXsF5k02VP9tmiZPsRaSVES57VMLABGjqfaRlvIbPVevB3tvf53hkrOtrpSDsG50n1Sh0Yh4T8H6PH3Xp0Msw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAlaoC8S_qGt3jEmM54DIoNM5ZNdvrNM6huaXAgO88pBhKrDIQsgLgVMtLS99TYyW-81cY-o-jlIS8s2VCxO4p8OW63quv08UIFW6LP_0HLEmcfLWsd2h6aLX1V90LWU0uR6KUMWsyqBElaDzHIFMawiaE8i_GqhyPRVTQq6qpKzp76xhZx9192JrUWmYckGY1b3DP79X4ssb5MiMuJ0aW6wV9GITzuPiJfI8ChPOdd3PMGqQ8m4yoAMgUUdl2PgqlZdIP3GHRSQPS9RhOzVuX_p2UrFo9XdoqB6DMO_y-y4FEcKu9MVSG1xhCQEcRcFYZRr7NHPV2cfNDaPtmG8Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X513UFCPt59Y_eEL_Y5XyKns0wFA6cl9nq2YTXotkJPDxE2QuEYR_0FeixH3nQokfLguGCHJ8gibGnOaAbSqyVaOGJKH8goTc9oCI1_PpyD1ZHrVhca3HaO5rl7WpYdJMuSmBWQorMxfW7VPxHph5_jmnhKJEtZiEzd4jsKlHGQ1GdGXTHPw8CyvKk93Ll1bUrf_najcl7r8eiAlZ8r3oBNwWHzoXAFnj5jisbMcIb0nEmzC_hIsFWldBwYA4wAm5ICgQB3FNaaHzRqaLKVBT1g2Z9o5IH5lOHRtugHx18aDIMpM36L9KTjoCDEEiWgCtmHSXd1FtqrZAuMpMGc0eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OnqPT2CgXgz8c4GUh6nVVsUDpaCN6UsLC0FI5riTLevFwoylMA9kTc8vqlFauu8319Dswz3OEiJYHSM4SLOq_HUvXQPbAEKFKztb7dKG6aeS1i7QxLEPG4Wg4hihdE4qcIKc7N6TOxg7tppx8UGkXqHq3wA45WTyU8LwNWFofHSIq796hW86f4_RLfkgAXfTQ4CQgL88niGq6A-NcKs-XNwISniq3zZeMhLdOhSqOYMpuJ92cf4fTs6ilex0ATx9RVWolc1ybSL6F5DJkJNvQSn8c24tiPU1kSYmL4r7a8Hc1g6K38n5uXWfxSf7He9eJrx4-7NULL1Xc9iSNWoGqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYYge7XTLCIV8ZHY4dtg5geUt1nP27JZK2FoZrIwH-_j0f2nKz6TXpH8Hoe0OTpZ8_BgmsconhoOQpzrwKsAiF8PCOMfFKhKoxGLbf3RLjd8zU2SuRBVBmx63YMzn4Xq4wp1EwZe93gCXn4olr06JTxMXgUiahGa-i9HWONF-gC8Za_Ts8jwpXFUSC8d5O0T_inokE6zGsN2y0wFZr2hJOoH-H7HSq-6g_8NJkJeXKNoE-BPu7hASdUBidvEziPfwqZR3lIQm_vrUphpW5Tf9W49Egu4M2nkjm-ZhrqEYl4Ua_MjHU5-XonJXrHJ4qyoZFsqGMAsn7NhMlbux-3Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKYF-2vPY_a3VBX7WqAuhJczmJrH5LpoiYmkro2OXMyNpDPM2uq4AkC_OG0KYiUIMXc31GoUTBlrbC340YD8XFj5IuQnKtTNx3hEtxY-LPsJA0MYyf5hNpXS9oKguXoCjesHx0DZfhHqSb3Skl-Nr7rg9PcJJ4FBKnIiO4uaav4gokJfzy4gYz76AfcswjHrKuad_4hiKf6r5v0L-b5y_FrLk-dBuCi7OGfjfwxziyIAcHVqX4NQFN0qF-7T1R4sHEG1QF4O6i4BEghaGUUYDLxphJ4IidMT8KY7aVxXyMjP14irNogoe2d-bHWJ3Vv_eqohltLpokym89voB0nnXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UFNPaH2jx_UbXfw5SNQOfx_T6ohmdNqNYw_t4vdQ3ZhbEcdnlzKxz2UPPly4qfUFhxWqPOmOREBwOaRQURFbRYCqgOSSm_JUPIwzxqhJy1odXRc8S-0tWcKLn81UXAROah8ir1tB1QgLhtcpjzS00Z_fXjAZeu_FEYCadTV2aY3o1nN6w3Ivx_e6iAdN23oJqrrYWJgdtyqRbCCtFPdfkCfMDF_ns3Zu-Di_okEXvIIdaqhZYV_Vf0whiq-AePoQFkQ5JQC-5DoPzxvCpsXa3GHvjsr_hQAKtkiitEVkDezI1c3NsNEeaRhx_6aciAL29T2lUsQ1mq5U2QjfcP6iOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=pRN598EMU92mCYO479nA4EaAVeF09JnntT0bCZF6dIyUrw7Mmq43RR3g3B9Z2ya_J-u6QVxvkrCSiMAGA5pu7eEyL_5Fbkk8JORMuCo4Xsz-CqXIolIVLRDjTR7BXhx96YIYdeF4emIMvFJttM1tHQMQNNDNXRr5x5803LjKycih2VxUW0HrF6ItnACbmRDK51aXKEBEjMsuaSonR_9boAzXgOCF4-PhreqAo5nMgdyetE9NNDkyz5FRQtgkn0Rv5trVrG-UQ_f6t4wVGWcfMULb6TP24TPm72861rdvqDUk_wxRrMIdCAp78Xfa-jgCsLKk_7WY7WtZaRWHWZLJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=pRN598EMU92mCYO479nA4EaAVeF09JnntT0bCZF6dIyUrw7Mmq43RR3g3B9Z2ya_J-u6QVxvkrCSiMAGA5pu7eEyL_5Fbkk8JORMuCo4Xsz-CqXIolIVLRDjTR7BXhx96YIYdeF4emIMvFJttM1tHQMQNNDNXRr5x5803LjKycih2VxUW0HrF6ItnACbmRDK51aXKEBEjMsuaSonR_9boAzXgOCF4-PhreqAo5nMgdyetE9NNDkyz5FRQtgkn0Rv5trVrG-UQ_f6t4wVGWcfMULb6TP24TPm72861rdvqDUk_wxRrMIdCAp78Xfa-jgCsLKk_7WY7WtZaRWHWZLJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RyQvMFYRnR4RarN_HUWvz_2rhxS5AKyNZwNVLanBM1xAQWxfmNXTqFUMqYE-QO-KcoOQaDWnz4MN6bgueBZnLtRqEeJlHEQlErh3zGTJX_gkooz0wDzHPcIk4dVCtyEBee4VRSrTUoArhlZsAm0AudsM88d_8pXB3IF4-ch1HjRxOXCKoxHXP7LPKFv9_iFbU337xen2LDDi3IdwmPH5-6BtXCyaiQWcVXtsPRE4C3N-rTUWwehhC8Wyp6W1GY8UEV3hnRN__rHL8ipiTVnw0V5HqRD5WGEP5xafWZ9YWPsCM0Cct7j88UxcJ2kqUPWDkhff3Uzz54IriZzT0G7Z2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kd4w1JqtDM0UDmKyP393gl-7jVCqBGGY2Gl9XsdE3dbrdsQ60OuUJIFao9MliajSrtpthGMumrZ8B0sWG4ERT_dhDE_DlKBVl7vwStBQDkOMFJZoSWCx71svq5Ebv9Tx9fY-gCRJD4TvScFTIcMffu3HpDXrOJGb2w3P63J5EX9VyppG6y571U__lWUy_2aEbj9zOooHkn08FprS0SEmUG20VUAXBHWbpOxf58AO5O67g_RvW9Zf_OdvSaxfZRaJxeCvhUkvb6La6EQ8TJ-S3ofGk5umXwA6KrItIHqxkaXjFGdG5E8UuK8x9Xi3rLmnqCBi-dRmtxTsSHLk7PSqXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpOkQIWxqUAmSMO_4LUmE0z1sSh_imwnxtUfqqzsyyTx_4kkFiblMPd9Gp4C868IoVzJ3nU-H8NfvPCs8PTq5TBNvFMeSHhGPNvic-zWy4261bmvNQENCcKbE_T0XDaEBGlNIIwX4E_NuPTkfxsny9dXgaqcU5nbh6yWYxuv2A9a6qGgEFNWxBgsaCklBrO-_pkXeDuNyOGtXf7YcsdMjdl4UxC0pOBEtK1bFuXXfdQJNuIGL8q7UHl5VQi9l9wgs_CeUIgwabkRW7ulOOWEYc83X5VEU8dwPuzctIz_62Qs6sx9LZDmvDtOtW2Uyy7Vg1BBVWzKsD71hLKBEjuxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SDNQn1WvPacf6axsWAMTQL90jVfrvcPIFpHJ9p0jj88oJ2eaux0DQDP-_gFuYNOGjS6USIzCZP3YFJZVQJLvIbGQ-0iVwQ6j5lmgaN9OValH4P1qi7bEBNkVGxLowLcTYGS6inO7WgPDJ7zWcvGmiGj0xQ_uodonN0eNlJ-u9M1ZhYawFsTl69PulXl5fAOu9DLtkE-Gx4ePxIphJXmdH48CQl-QsfwWbTw43mhIsutz150ru5y2CG6fwADos1huJDX3B0cEsL99flG7OHM74wdHhqDeyvnye0Jev9pc_1ytQ-C6nycddcIqG4jodop1exVwfQFCd0oCzHlU5s9bIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-Z0V9lKxWSqydK8wPl9_8CgFyOQORe5WkHzbscvOlryeVL4o5d2RHLXnIwDiUIryuV8sNlSBzEn8kTsT8L1Fn-LLJ_MAu7SDCo44BjmqV4ua2A8ELvqDb-9B3RCzePsBti2egemPkvS4KRDRSMPpqIPAxw6Lnwqf3kiaArD9nVh5NoG_ZjyW6kO99e6E4Izr9SBIXZXMkqzjJ1WbDr5_P2iQ-5lRDDZSYgLl8dwr4xUfdVcNxEHoogoxC8orU0oFO605UwbHkXqCGcgMq8hUiWpCbUjxKqvGw3qbw7-iQHyFFNN5760FVxYLoAd_d8noXLKsS5G9-iTeHBR4ToF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kIz_kpoVOyHTolC-0TeBA7zp73Q9nUzf_zhnRICi6LqhNRrbIWz1uD6NpLmqqd4fK9JLdth_KfDkPhEbpFjsPjs73IAhQMp-ZWQ1q7WiqkGKwuT_v_jvoEYvl5oug4Vdh7dQhuhNEH7gnKMOR5Qp0mhZCo7H2VOjvcIVZszMn-IturgCmvKt9tW5CBoZnzfN3fgek-sJ1HNopkpMrRr4dg8WT2aQ01VStje1HqmdTuYNt2ETbQ_psaXvJBJhpzv0fq9B-rV38mshbPgnKGhtUHPkNTa15du1v_RYtfMX7vtf7ikG2pIhfqxklhHfFpv2phyRUNzJtWN2zwPc9CPzKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AdZ61rqyze-abXO66ncxx2Llv1k3vYVhboTZ0bMUGQcdiT9OEP5IPDhX77BIUWg_z6pFYYz468eAojvoq1z5Un3Cf_Efkp0CAIatywZk_2J_hC0TJTL8kbLrR2tnnNgaJiYCvJvcazMZp4qPTp25CqPD3arYmbZ_mq8nKdsN3km6www4z6mZnJjt7jYqwcNJYPQmyk26iuKHtQvbRPgqYxf-KSsIPLY7xOFRrDjNskba6T6dUYIn9zxpI1uQtUXQwAZZ_gbdhhZGMTevlgWyyv4qshqOs7erBeWQt2zew-EMxY3c1Tq3HqNKeL-Qim7T3o5UVPxL_ceHBDTZTRtN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFYPI6MDQI_I-P5IktpmEdozUlVRz4L__j39JhQrkjBumebPt_mbEEx-q6h7rzUNCdgBBe7-OLyYx--t5NUzdSw3P9D_V9dtfdaRH7GvBAVKZdAY9WKC2qfmag6ffqdj5HPHhRHn3RUq8OsuaDm1A7Ck-qbcqe9TtlBngFYDLTFNmQ2maX5sSihFaDVjk2lZ3ovx6lmC3Lz-vMIOQzWJcJg0GANvfgn0jPeGWdKjWx9X-rOcPWPncV0vgdFlXomRkGwAx2v-IigVfddjtE8C9FB_hQ4wzLKPe-3Bk2-nwdkRbkcL4lvOTLT4cCtehdn4ndwe0Fcr5ZYUlIzp33Pdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXMMKXg7vOzVVKuwdSN0Jcnbxn_up7FlXHwVyQG8kGMFJlG2IGp-zD-wA3-KRbjq211RgHe5RQTBeu5IlUPl3zRnaceYdsigLuNwo7zXCu5OTP7DiXMzRwkcU3hXO1kgjYHgqgRIS2aXwacQfEb8_bdoS6tXIb4emMKmhpgBSpvKPAGRLcwlrtPKNmAHkNAwscwn8eMJUvJ9t_m7ODKajvBbjs8LCaFdsL_30gDU_Pz5cuootQlL5djUUJ_tsPSToMhI1_m_VqhlLEvsy-kCUVpfQ03BmDE0kLAK5dfyWTssC2pbtORXAw9iWAGPd8JEazJ-F6kdiBNtkf1NTATuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hTXV-X8ptJAgejSuEGFLOXApBbwRhBeA1HuseHs6uwc9f8QE5Qu5kAr4mAv8hsDVhqYw-5VCv7KdxlmR6dtpRpqd0oZq74ePEhP5B7A-lFXxRqFmBvCtvGoucULgPJJL3QUCVM54LMEDpuSYWeWcYA9_uo1iHsgB_qAD8q1wUWCPBP5G2I2eMpTv6Fk7ORjvLojSlq5sXkm_uO4UbkB7jBj7athds-zZ_Y34fw4wX7taJaaPZ53AmP1NVbelvs6Klnul7frp_8cFDmlIkUizmIcrDvbmdcoxq3PSU5BL90q43LdHdvvj4iETIvaB6t59x20Bsf8YdNcIIZKy95I42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjawY61GuzyxR3y_kIVFJf9On_rtqDnjE-xuEbXyPle-RtK5E8X0q4JWaHZBIDCkDH3KulLY9BR2Ctp5sHUlRfje4tQqBy5DuOMXuOSMDBzkZ7vRHv1j_YcQvVHWvnfWUMmGA6Dy_KbpkyIRKcon3rAYjQdEYq9TX_2CHIYxGOqZd3jMkp4UWKqBLGz_BsStHKNST_ld6ty8oGWNFtcQhHLo56b_6rrM9_Xb3aTbb16CYxD2bPcrewj-pduiVphTs1IwoZWoW6VhDquk9EWPH__5ej0Ri7TRfO9OM8rr5rUqTHnRZpLL6sjT_JmzvVQ0lGadXhP6WneYnRGkTVMJkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMbUY8YAlLdJsbekWehLq32SPt2OsPfSY78_d73nU6ViXesJ1oSa62KugedbGPnoEGcKeqd7HCViwIp_Sz91Y5cFp4d7A_q2tRFdzIjkXquqNOb1Bt1cm3yIWI8QGXUhEC_T7huWvHYgfblS5JGMZMsNnN8N0HzapvIQ356k2Sy6wSIqQKSE5h56ypp0BySHQQEV_k7d_ikWFgRbYkECp5BMSzXp64-h94dDbCNyrdGPo5tJg8VgXSokIH1qwhebizX6Qvqc88YcVg6rFSZvst56Yim-vwaVFPJ8FGAbUcHj_H9yEo5XwqQcZUzNzfVoxDQgCrwTST-gSYpucmaBiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxnIJ6lWzPUjgA94lT-pQRUW4aNBmkcvp7tVnNU5BcAXQVmqh9kbY8TvejgNdymcfCMIdkJMwGHIw5tvTS7h6DKiqwAYFqY6wh5kuguK_HDVVaokJGYcBX-CuFZlMXYqng_2m3hx4kywtqTeXoCqCbyvVq2Q4wlItgrzil7fxR0O0Q3gCor7Cd8s46JQhT_abhydbVbuwsEvXr6c31SZMEZPI3ukdDOaggcniN33OhcdpcebZzQeExrpNubt5FH0mca90bADsCaCba034vx9byH6olMm7nUl2PwB0mafHfnjiuOvyPuL3z-S0VLS1Mo2RlrDdgS1l_3nSZyGAbH8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYExXT510KCpu2QG62AuXuuxiFg4fpE8H9vM1Z1gB-J4a8mwlO--XWbRTjkEJAtKEjBve3KemynOs6hiDO-hBKNdmJ7bJbAphiGwMbzgHFeDX80ytZmKPHlpUjkWW2whLggrqXfOEXcQL37_e4-uXzdKGAEq_H33ErDjwcEiZHYah8lV0DV6FFEYlLiRmtGIVlvzobGo0lUBHBT8Dur_bHlz9lKMy9B4XkR_b_Yu2FKsuHKqGAxTphG2BONCgOnFJ_CFonPa1P-8p1Z8SZ6dKV9WvF0SFmWmQgQaAlk5KtPv5hAIaQtqKDDaZ9Ca-gLshkFVD14QM4TYpq69Q86b_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V8AftVe4BAdRxVRPQstGLLauYjHCESkkYleg7-TefVnR8B2ej9k3Xs8o-VSMHl6ip-9Ig52y9CN-CFVsU0fs45dv8pEm3_T-NXDBt7gb0uu4uoSaScHWnWMwbF0mthpyZT-4eQulFkEh6s43HZ_KG7wKwRBL6yFXgJizr0lw4lQ1z_duiml7IdERSxS5RliDL8HYppX6aik6oLnEYc_iLM6La7vGh3uIpMo3LJIOG_f4X1uSNZZz9qT6e9t1Fg59ViLNDCz2GDM5wVxCogIfglzACRWc5zLYbzKiJELLfR2CkNnSIa1NNpBhj71sVDVrwQRI17qPGz5tTdiMf7xtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcndB7sWMvo97rR7qdeGZhio-0weHdAWRCi4EZYV4B69y1E58en4lGlLZffjTjzx0e5KYMpNyYt1d8izAGnmP6YbMqoBrq29-HFLg5KFxDX_JrnZUUxDGbM3X9MQ1vYOfpIwEtP3TxejerwTrpxY-yg0nyg2-LbXqfwf1CQsnhguX4duXJ7ULuSP3XMLMLyZW6sZSTOe-VbHvvTyVPEAmByh-aMsw0Bfs-5sDL0n-M4-gXsPczl3tk2spuZp8fXIjq6p9dQWpm2ZeIme2k_Ad1scDyOaAjX6SzavKn3c9TBlqEDroRUnIlPIqOTOoqcqpZcUrTUSilFuUoQNKgMQxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGI0dOgdARXS7QfST0gSiLllan9GSD1WHC-hIj4MChAoyZsZvty3frC2WsJ7aRB9tcFnloUAz4ZH2-VXKbKsL5cUEBcXyYpiHfr5RurqKkUJD0RfkptdjHPr5MS8AZLSSk7VoZjgb84dO3WvrcFItos_yKZEOhBpc3EsbBvl28qXZyYMx5wTzBC5E1q8dg4P2bURE90UUGo_e6hhiOmhBEIpx3D1CuY0LeHrstf_Wm7o_GL1GhhZZB_vpiSSiZbnA_EOOnB2IUqGtX6P52e9lUHyFWyEYYEY6AeetX9OLFDk0Vgj630iR3UPeHnKF4JrFRTOA6ZcvY4D_1cjSDg4mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNbHgnVk0kXU0hBg-iTNYBYZ-itlN6sS4kDgmfOwz313_H9ROIDErRbAry8o0o85DY033wfu6CDhatXnBLshegkKLQftJWaLiELqXfar7rVffvF_p3Cpn2RTePCdDw_9txb7GgdL9Pls4f0eHn6F0fYPZl_CLKxU6KVx0581yUHGdSVBELHbwtB6L4l8_QXTxH-QgvauAb9E0Z9CuvDG3u5hPypEsotNTD--I-HZZASQNmAVuiynGLsvj_MWnPFIHKNk3cKOJQhTpjUDarFywo6FSSRJqwLkyQ-fBIPwEN-zz6oegY-gM6tKWBYnal8e-gk74LLeD_26G6K4nCBKEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OFhrLAGJD7_Ks30h9usNMdPHuavGQAHWadF95ifusb30qcH2JAd-HMIBt8aX2_W_hw3owIGcPBvj7Fcr1LSCIknfLP-2Bh64DHIOUrPQeNrRPi339r0wPZquSqE3V70RLbMnlCeqIN-O5Yxjmy5uj9G3oQrgr-42j1iSqbmO4YgiH-j26lqs0NT1a7DDLlZothoCXpudmFrYLRBRegTzQaulQ7CUMtGN9muATzwn303ZA5GemrB2y4UIKSSHX-cJ8fkjNKGIXNPzazIGR_uAh7EJZaznjsH1DlqDHLMAckTylpvJSUlAsT1rZ6nC1dQdmUTSa6GH2JDiTE9DhYdKTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hfmEhhPsI2FB6uEv5815Mr46h0MW0WrFMSWNYs_wmBns9Mh3CQDh7cDsRUXbcWcMgQZ6weIq-4_vANR6JKyeQb1_MoBnCn8BLuzCjxZ-9tyqRe9FA5ZE90QF-qvRQVxEKjW_EX-SSKLwgo3FPVDY4fY6cPSg8F2hqnMcgt_VNJO3jHEeCSH-Ja-Uk6VSEmKc_6R8KWiz7J6n5zj7KBMfQgELeRl5q-bAaNgY6pWCQmrDdfg6NL0IKT3j5k9Odcf3zRfHpaZwMx2lWwxzouzqH5N7ZIFD-4TelfPsbP5gnGZ3NpKZVMXSdIm741mPUHT0UDUXWfiNq6cavVQMFH28MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ER_P-wrExbAKkZNu0XNsPkpAIL1z-G_7YJgLHqWpB8PZTE0T83YoxKyliyLIlu9tgSXHSSLzTIuY-dVX2J760Mt6_TdqLRkb8mRUrk2KJBWiwIWhEHz_8JsRDM82vHSTeJp6cmGgYpTIG0K2t7tGhUCeh_xgrC5f3tHJd5-1EQOJ7s7FzHngZZOJuhA2F4yeNC6zBJCx9WIKGkPNcYXQdIW7uawyq-dembdSvUQqZec2Twzk0wi1oxEANSaqil2bvS7YJGwV7TqAnLF48W1lZYhDyY45ksoxftRhmt8sLLlSVOolSFh4gL4-CSZ1yZsr3yBsOgnhDKy7HqntgygI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YtbTC4LXaIlH6MCwpQClNMbLHWyyopYK6LZds8sdUdbM6PDsbYJStRf2yN-SYaxnuPn3_f8dBP4__q_sQof2hbUnmy-gsHtnv_tLoDXEvgs9v2FrnsJy8RN-xI_8PkxdO-wOuKHdKZBhcihDoUIFhCAhV42uNOC5VCUNsDVLHg692-6yaxY3lPxm3q6kjcqLun9ZL46XNbApoOw_lthZCbeHj51F3eSdf__Xzw5QQQ0MVKhXmYFnNQbcgIa2Bxv3ti3FTRyH6Q8G-yWSjHELrC9L86oX-ekDS3ml_hi0F-YsvLH6DY2lzag1iAH3TaSWlPmcwxvXBAqq49-yzbhJmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRjxBSPPLKFJDrBX5v1UWpICJ1_oY2gnqmvh41kM5VM2nXTkXv_pCn6QqRA_ewXR7YjyWdVWg4bPMiczw4RK3MYCVHRTRYboKYZjgmm13QffMKZE-savhlvI4UNz5BPZlS0kPeluo_lHU9JF3SQPAoq3E7vRsTkP-I12s6Tkb8DC7ec1LClOXaT_1PluegIVcJgk362Vp4VAwPBRmWE1Lz2pWJJO_myT_Hu9Hw14yRi-jQ774Htrg-sb2QDuM9SYyjrGD9H-4rzx7H93AJdxtEJslUgRJAytC0Fjj0952ts4GrvIPWokZYBTG6tc26BE2wS4Yt_XV-dOkUmjePhsdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omIZJ5mMuV-7nb59UvUOfad_EtxaN7vESr3Shcret_ljVVcsb-5zPaGbOn478VnJHqexAwu_JiE6kcEvan2ovqmP93-Q1nankqIiEc_snheUYnR3HPDCPwuJPjkCbKGSfa83FoO5vGDgkwQvA_J2r_H1LwGsYmTr71McZTtaauIz20lLAMSMeYM5mU-6PDcbwLBby6_tTOyGQYm9xNJx1weV6tYgInAKp_cJMhLMTjF94nt0jd2pMa_TtG8DiXPMoOZrncnsqsYjTpE8ElSnSQpZ1AR83V4qey_EidiUIHZOhBIcNYcNiPVrknOThtG9RVi7zFTabQ-0ZdNvjs6qbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XqHcsQTRkHkTbNxbgOfHnxOtYFkbUBWkayWz6yojwdhINDjsCmgn05NlLp_Wq63dw5pAD2R1ElfjEmIJ45bKVa6Mq7F3gN0JnGrqJ_xdjp7W9LGEmql4kfLLhonRGCp_FyXhqNhTzZ4-t-P4X8mDTwEpmCzHuiZtP8yPt1z58x1ROE5NUTsx_1gP0g1OJ320Q63WnC76Bt6r18WLMIRvZ8lOtsAVDaP2UYSl7IQUJXF60Jq4DDbxbb5S-Y-X21gvUvO7FFmoYR4KXrlYyuxmv7a-ym-e1GwOCEx3pwSMmag0AWAZdzWu3lM8a2oK7C5yO4fWg-3PW8ksrCXQyLM2VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M3UVCupIwlSSFxGECE802KEUzDXhdHNbUVtFmA_KVaGZGieql6VxKelgBIEbFUdVN27VRhu5974ERbJwaj8Jq7n154Kx4zv8sEkjgegUUkh6dC6Jq0a4uW_zrVCIH_6Sk5O4_0LVyYdyFczJplTP1s3lrKACH-9C4zWCW0-lhZsAPeTKSAGtj-ULUZCVd3DeMj-8OM72riVKXp0n6MyDq2bNs6wu9IkYVo1zT3RQyUHVdGqpH5aKrg6AFc3XGs_FWjjWSSSxv7P8T46s67p4aFEKYOOZZ6KCyVt710C5RKYXD3LLWbMB8QZonR_FdXozUztY1cpGCT88LDVZKxjUkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtoAt8sx5Rtd1w3ARk9nubAdVFlICaMQXZQbmGfygVfYNA1RWFkFj88-sTWCPHBH9sbLpPHFl-QrP0bg8hpRjXz1ZnM1Kmv2LlosNmChpmgbrib0CfuZyM2qBEpKVYWaK8rZO4deeEeFUjNUkNMuPrWL4Cu_dR54j9XvhqflzHA7PCN535KbCLyZdTshKswmECAVUD4j8WG48VsLAr7uQ54HOEnpCGAy_OmYphcX0g5Lep5khOI2modr6IYucbiXuFmrcCaIE0B3Oc0uO2BJc5HRMxyPQwYhBh-z2Np1_16nh8NkJ7tBK8NaGlQoO6DAdDgkw8lhz4d51HnqJ8PHBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLaZ5B8jDdiQnjY8wR83W_Y7IGj_eHliy2Ln08Cq7E9B4dB4hNyPMC0raDDtXol3PENkQop-KepZstrDf9LezHQf5ametqvNLUnsSpWu4qOYntv5H8oGy7j9E3JMUiMmpTCg15sM9bUqrsNqU-H5wTt0JwjSlhzk6wPP-3roMJyWUa-twlMbaAeEFNwrhfTHJOtLG1kcOkDCfUOesenifJ3JbdnuLSoD2GfgVeU4J5ibRxp_EYFkyP7v38y2c7pfiWfIU_FMc_VgHMvgvlYKEja5vFs__GHBURjlTw4WX0B7t5FfxeWHHuQBAzzW4pk-icAH_dIez2pyAr4WFD0BvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIknAU-ier5nlGqyW6cnCbp3l84XX0Md6hHqf9gn4OWs_J8188Y67Okyi_6K7e6G5Msc2MD7LuCkUsDFPCe43J3fiELcLbaACrQhzsI89bhsnQjpcsHsqS1O1uPNiobqbOwi8tkEgiQlys4TDG6FthPyTsH_HEqSl74bDBeXvDgoDzd300p4axh_1cFMt-QZqJxCj6l1f8OWYrOfysSK77Vr4NsFc9yx_uyv82vu0hrQ_21oMN0AFaT2Fmj06lK_f6HOkqDdLCpHKRayeC0cQBHGgJLJuwzjh931mnLuQQxQgBxBJ6iG50jetMJsxcaNVblncWUaDQfV_0jPVFy-VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8_JEyK0MyM4rGEUWMahdwzW7PLZtZgqomVyAV1nqAxLxTY1x4sCNCFxccx-4DwoRVfqKv5GIP53YGe7QO3exNGuanUpznwnJ06ZnoBFOwIqwP35YnlJp_Dk_WnbvwcbPhMdT6pSpQxPXDMkDw742SKj9oCablcBCfKOv-9f7Z2VrEyzFWJBByPycvaEA1kLHRnII4-CZKEG_GxUMTteUVkMXRlMI20CN0TnSOrCxnTA8sh5Ht0EDnnjds1-MMXk6F5MT14qBa8SlhszeT-0ff-A4mK67x6h59f1tsg0t5MWgE1kiYzw5Dt9heHg6xLWenS4ByPCnwWwMrjoZCkbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVEFKGz-KAD7svs6HaBZgnwFQ9PuZXuD0N_V-CUJ_e1knt8PQo34jF3FJ2S15SFMsb4JP1ER72qCeKYOg0W43ldkq3D67QCupeTBm_TIk9vZdzE7vlwMoDCLFMS_8skYAinbzU3lq5XC2lM-XbYNIgea4FSVKCiNDic8fDv9lQk7NbdxYNCPYDwp-_6iYKVfVXh3rEbGo6OR26HLQERZ9c9v-9XpxgX2zocUKfQVKXIcHXFb4xV79TdXrmVjXIQdn_Bo_-XZjO9OPjSyFiGz4SrrUeoj4aUFXP5yuCZwgBe9057Alh8K3-VYjQCEBXO2MOwN4TNDwCVfk3VCkw2Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJOyrQiIdlOhwGwe-PEUCG_wJ6t-pXDETKXRLFsqq5gV2iaKE7jXrBOWPxckiBbjl7Pa8f1wub5BgkA4EPwLeg2eQA1bsx7Ni-dw_BVa1SjVRSlvo-o-GgnN4oVaE7vfRir2bdy_QiKSwAJzeCt8gh2g7oJ71cPqcObUr3nj5DvPe0TNJx41DoO6SOLSbB8ajfHn3g5aMZPmg-gbrb2UXVswg_K0_dN0SAuMerWD3v0APsqOPFS4T0BYcez28AHM53hWfFrc7FLNVnjfHEv3hPzugFOMFaXV7xqTZOQ5NkHdQ_K77_V2SmSTnXf4tRELMbV8eA5kTYj3Wxo4vWihYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ek-WUJdJ0uNNDnyCgQibSDKDsVTf-8aqew6iMdFRrcZ7t7yGgQy1ftmLLzoGBh7SMLhaP0Q9u6QA2wjhRMW3v5XpDVKXDDOYwl1-lhw5cuZ9tb8nJ2UG3BL5WrqIUo3tV-_VNZb3-DRyffh7tdIXow-2vXymJYAKoENHDnbMCZGsXkwRXNaytoajP_ety9oK2I85jlJpyUQq9DpqolNlCG-5V3GSj-WFcgP8SEjMZ7pOucefrjqGxvhv95IxXNhQ8sMLpReOPqgQQ0EoBevb3fkGGTHXt2wTd-AgF-fqyAtkzcjNW5loSfaU3shmNCjB9qQySumnc_GIQ54eUbIetA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OrnosgApRZtygifZ3gOsaxIkmTePQA_BnDpAH3H4fdU0y8osSGga-j2FrH7uAwayciYNVGrrwZ3oXBnSpu2NQvwwygDj5eMJWP06DzLmn9nzPo4JZvdQvMr7sspdwLLYkuX0eKSajLn_I2IzVIWvlUQqVc_7n-MhZSeKbpyXUAj5A-8-FTGmB4kgY-pPqtEKw9toHRD6lCvIzDfpsIuUKBpbAfzMepTkPVhch3__RHmJUqewnnysOMpGVP-KBxWMGznmRdgSUfx_JO49CIO1XaIuQCCu4IdhbywQIVKfuRmy9iA98h7RCJrF4z-BFhyLBLOid9Ih__hmH5S_azWrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LyAX2l-RaJ3gZ7a5joaVzqTABMHCPN-VfTBhp5kYRQAyKw8NaXt6VNpAwl-U3nE6v8UNDSz3qTSzsVrled23yhP0DuuqJx6qadrFtHms1s6QWCVtU0a-KFs-uESx5X0qD0lSYvbwLYh5t11uaXq-2YIxfHiHq4qMdrhTT2Fg-5u3zzXQ22PI_0v1m4lhh9eQoGxyLwUpvh5GOjqDgEq4EZda0tvJN0lDuZvBCPLRk_vQHcK2BHYIJMyxG7HegKhiZ7FF0EbThI2lWn1lRHfViHVHLWZOk3Wx-hUIJoad29wB91HYOz80U6oxT1ZZOn486qrz7pVk5BMVbGzTfS6Agg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8MV6F5rNrgyvmPtOlyfqXuYhecDBzH5AS9Jhw7ZrtQzlZX6YlUwNeUL_tO6H64xG-ZGJi6wvR3WSdjmeibNR90k4ZdUiipH6vfG_XHJ-lUeB52KvYOdnT_X0OuLNWSSd1JFberqtTulukzlu2IXyPZf5X5XyCdqhqY3wK2EfFRn-uuWE6uf1B1WpNbn9tFHlo3r7MSLpT4RBxI7K2MiiXdeE5A0rYHZ9PQSj1a8YNrdKYONOXh8_KwtgRlcb6MQSc22xV_IaSBXdp34nq6QgkOZahucj3kBYNQYg7VVm_cuZAK71f-kAbO9jKKP4j6o279nbRd82d6OkG663WiEoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WyfrNZNJ8_bA_YyNRZWnagrTR16DNf_Do57MQlhspT6Ou8PMX2MXPJieIyCGmfPA58nmv3oDLqSAVJjqxkpJKCQor8lX0vavZ9jPuuSx2qhv7XyJvuSXP2gY3ITBZheVJLByM5HU6ggfYwc4WvBVOb5hZ5dKqIR_GJ1LYNARBePCxcrru1RETVE0-Ql1XJqCet8CmrotcOGKKDBtuMJTNcVz_nuoHuFlcldU2q0fYO07z5UmIQj7RnT4-2h2ZTSHRh48y24MhHOEQyiNzgxzKKSrSD0H88mNaZr7Bum_QuCGwo4UQtU--6D0O1F0eXmgPKqwj_Rinx6pD8xV5lyrOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STkpfn8nUd67YmfNKq2svWQdvYHg3wWsfwK8fmFKc6_H4JgGtbkbJ3ihvjSWe3-TSvJ1z-K_6xh_eFkcj8UcwYpgnK7whCdvD57iRaiJOeiYeCyBXAJverI3DFIVFl9OW-bqC5bCWyAAZhrjXcC_Ql71QZDvXhbgiNV0lBI-dTnnH1vg0ZpPwxOu8_ARHkyn9rlcKMa4ZMfDPAKHtHv4WYJyeUSoDwFu1QeA_sYFB7Nmaj0wWUBX3h3-uEAOzknKKJvh2ZGpe_JBEt7260wZXLBJOX2o61jp-IBGUsmNp1ZNnOq6xyA0H6clbM7LqVdN3TZUde7V3hEOKtSYQfkCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZaBpIWqD9XEIsA7tL85I5wLIgBo4EKoosb2lMlHzWRPTg7UqUh3WB8FZn3lScFguqCq-uFjQ6LTmAepBDqAqwANskoJB0Fb-TX0upyYVLvqqsCPlquZcm67LKFLgHcn4zcbV9wF4a-yAjYluMn6VqsTrLBIgu1CZvHIoLTA4JKFBeggLj-ZjhB5pnrIxjy2dIrLv3F7ELB3R2OfFov8EyuC_F69a3wN-1w7MBLYnL3o-2co09-tV_A3BkJeNGH4sjSmufffCusbIz8YJT1-bEBnb1JFir8H1Fukp2FQD291kekJuf2n1GQo7KI9txKieA7lmFx-ZmxJ1ycuPQ5fCDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGEw0m4kV2qSZZ4t5PcYRccCwkJw6Yh_SWjrgofBF2Hl-LFwo94gy1Lj4W_i2cjgICg76pEQEadC5kNr7uvxRRmhu5jgXAfogV4fQAHP6KrtHiBK30hX3OIQFZElBFUR29F034ePlZD5DNZR8AJMPNwwZekOWmmgeiLaLbR9ST6oH1AiVq3VnBtR4wlShY6klK0pV8cI_0B9Fz42iKE2BN9yuFjFULMgvQzPI0ghi-2mh7UfHGX2y6ZhGmSNFmW0BmoscS0rABgqL3Zv7odd9KnHYlUKU23hTNTJTaLIs92BtB_1fxDBDmsy1jhjVQdAUy2vllyFAB9kHEHdPIqNlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSQOjnYYqEhrXrnayP7_gsuAdm0kTPMUR4PDZLDYfAwLXlEWfageniQxbCERX_ASRp0PPkyMYxWcJJaCZJTQYxTbn9dnMIBSMU_8lL3pStOJMH0kOCeuWM5V2dew9ZCmXcWGuV6cCBJ3FfGorxj3jlbzNr4unH5MtgC98LWIrxI_diznmSAVec_PM6tFMW7A0pGLPUD7GO2yeF4gl-ycSl4sXlzeXcFAVlYGtdhG3CCk8QCJTam1KRFrWXsBYEMQutmEV-gbPpPBizn_GSaGLFznjKfHbY49uAK2kpLDrIf3FEa6lB7u3CxI-9wr2OAEVPLAMqina0pu-IdR1_XzJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjuL1objyncocDUPlUh6LT-zARGxQFrMGNqCFv1tOuvm9QrgKkzDGexckHSaoVT66DbUlo79l32SCMxy_BOZL0dkQdTFrJL6vt8rfrXH8YGlpU8q4NjNAe5bVsWGyYeVFGZLbu7t9qiODx-3uMPfjDORu5bLnO8_xIi7rFQqnxTzwGXzfOCGQXWR-SX1DjU7c1i4wK2KOpeTD2udtQDA58Cu5DGeO8qz57di23uFVm87IkFPLCp1dwuS5x2uHF9UzTsoQELyKQ9hPqY-_Ugur9SzyfeFAMQxe1_fx12rlgX_H4_NC8NLm8HJqtsZOyc07vxhvI3CXvHO7peYAfRryQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TbL5gGc_MpCECKUj2HLV1hhDtq1tNHwl8WxjQgQD33_KYnlVOytf9T_kshMnH-3y9LfTXtlu5cVGCP6y_7McoZgvF9X39ULnVmsnIu3W2enPRmpABnKkBaExmeP4ojPJnfmKBYVDTyMVmwRYTkwggfy2BUo8iCempOxwGRp7rfLg-Pip3kOCKQO6_p7r0BXJXQgYtn9vOz6m_9rore_V1lTkL438Jcld4QzuHd2DBFxbzvOgPF_LRNCMXkRDzEElmOgWYQgTPkL5DO8XPmjq6voq5PLkY3RnIPHWrSqp2MBw8N1AxbRa9o2nb5P41HH7_dYHEJMXa7yqKQbv3W5u9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mbu9Fr7Yt1MRG-79t_HuzeU5n1AGLZ5gxk3Q1OwBzRzmhXDuWBaQTn5trIQBh9RTEYfdDZO43gpLC2ql0LRkwbAMdeYeQLGAcdP8xFEmTO3Hp-orFoWidckW5wajrUZ2OrbglF5SIuaYXT2yu59TyLwfUfKTZ5tghIWHiiRXtGO6gdeTOmgpAG5lNJzf6JqrbZOu9eqM5tj1bG4lBhKI-DxVIEezor-UY52tkfXdryQUSUwYTIPn5ZMcx0mcQXj11Z9taaoFH2_Vi_AmVsldqnZGRBF_sU3UikkKVLmrLxamdGvOWxalhJpbujTCFG2u5UjvMjflwinms4uYIGtZJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EApSKu3EIZZArKEHyy872bwz7iqzsruMk91wyj5fgtC2WUrtvVoyCgP4FctregOQy3psTqAmf9e2p6kU-usqe-dgGXBra34Ryh3PiGZNxcj_h6jeGYetiwacKp1rZ26jFr-9jlzzc7R7t9DzwlibbsnmI3NOQHZagf8VmkfTxKoljof6PtHoGc2-CBAjZVvBR0vcKGr5xTOdusimG5eEkndzHaXaF_apN_vJOGsZeOFHqcQkfi6tKyHoHH9c-pVl-7SDjyTg-GdXCUcrlLYW4619yBOaUjFKBau-kLuBBBK7D8eOESH7KIFt_j62Ux5QJf_bgdFhSUl30MdAF31bKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wuz9M9ck3Wm3rqYAXM1pVDNCKkXqIHRsfxTEH0vj93ixKzxcAf8uKvLp-UcJFDqZBXjVNYjPbDHBIqjNIr-hk8HY9uMuGb5Eb_GzzqXkUvf05g1hCoPYW_M_L9jjosd-lgleKI03dXHM5e69e4fWAuuvWXoU9cqVGbiuCYtKclwE7fDebneeNYE8kuY7OLXFL5Gkyhv6fJ8KCrr_9olZc9jKLBHLCMGEwwd7FWhZ37Jsz21m5FXDHiXQSrEeEnVXm3ApAWyhcT350gDU6ZfDkOPBTG5Xh14w5RzfxI7B1ALiShzdHs4M_4wX6MWo9ir3TkzdnDBzc0wZr1YZdUEipg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDASkXyk7rLv_AhOguYJPQ-TzP7qJY_m8nEF5R1Q-JWTbXfTgcvbnVJgZbRlHw7-io1y-JyQgeLCrhuGX2tPejHK9UrpBL55tTdyT1roEnApC3n14lnmGL0tTCpFfjkcQQpQX1A6JsaY639eEefTql0dktJYJHlOlGwS8VTuElg1M85Bgaqi6TvXYo2iBVu7wb3rz1hxg2X-GDSGQHW9tT95fjxWpixPkA3l0AUE-T0yeG75QCtGfKSLmSXGqwrSh_NsXS3bc7Fp3oDpmncMFqdJuBNUrpsOp5btM8s9XJj1EcoKOCcwcVY0V_Hu27w81Twgk87uCXKp6EpJAUulNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClMkI8g1Zx6q-h32xmvFYvCMNLynzor98KvF7vIPVvDU3t6-ouHaw4NfGMBeRXECuW--numd2gn8LJOdF9Xj9sYC0mhPjlBeBadm3plRWm3stoe_ClzCDfVbWGyNT9KpJxnAt6uuln21K65a-1oVaDSVl2at06UkrmkPk0lawKuwL_8l-YCNFwm4z1W-C4CDUNNu-9ZQhCONwTZiWhPn0O7POJ5eJi3JHWwVMAVCikAmomWSBxtB6xuvUVxTSDoN4XAw8IGUN6VCgqQRri4b4o_4rFKfzPSh7PcFxCMWOepVwwqahyw7QU2fSuVySTjXY-QkkcgCRP_oLh5SIAn7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XiLHkcMG9chNTk0FVK8RCYgHMwcsZB45jrx-uzQjsAXvik7KhrSsNBl3ZgKf0AIgpw6apo8VtBh88nvwTnOUqL8LTB_IC633rBlZZ6Rxv9K5bubwhwIyLDPoCfAbjh24HQQBycHaHat7xSMH7GM9FNxNgaIpDiJ1e0IE1T9zCP3dYGnwiTnWcpNBjFjZF45KqvUVJ_ecHjs2fJMFgPrCxsUwUtiq2igf9Z0EsAM_ceEJzm7iwPos3kyXMYYD1d1Jgg11eAyigHH9G1fYNewiVsoO1dJG3HAgyOvkbNHF5japcLcfLNYxnLwM4tEZkimYeK6f02jo4hGpS3CbHQjBSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHqsY67Jg49lhC9cIO4HL7QUxPrCkjs1kk6gG7zboc_uU7DF_hDZZ-Z0ywYlViXqF8LuZf2TyQc7_XQCSmj5jB_4KJ-mOHQpM9eGOk6fRDmLnaGvf22wDNqfSqSb2wzA2pCE9WuwdARNbEMRD8UTtpbygneC8i5CiimssU9ho5_aLDyae3YUz_mKGslFhp8gJu4kqBDmkF938wOVe0c3uTazGP1JKYLBqr9atrFiF8pfvYS6Ky_JIlXseTsHJbZyb32swjhONGTz0qboGLjw8iMRWPSL8bL_BJLM1yVexBhJdSH4O6OERqF7NTh7p9mtCpXTESCv1fNNrSAWNZDNiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GrKCDx-JCUbH3KI8VaOl_0TweqAwU3mgksa9Ei91Z3b9oFOO_ArPHwDgZPt8Duq4nphhkYc8ZLWsfUABN5xLQZM2uwBoo1k_vBJmQe7KXEYlMwmg_tXQg2FqShWVD6zVN9NCTdBFM7SwaPwW9HZ16MDiw_XJWQk9K3J_9YBqUejor1zBw49GLJieWUVCfrExmaEOME_jUnLsw4YtCmwrLcbwgSzKrSbvMdWe-FRsTkCGSc-mbo4MYHR2QL8GMtH2fb8zk0PgjFCSqLMufRv7Z-N-acB4IIEYTvyLjF5Tn4qdQGxEFUUpQA7gMxLDIaFgfqO6gbV8Hn63qHEl_4a0Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHX7S1hzbVohER1Ffj4RLaJ1KEM6JX_7zZ1j3UxNAk4a0l03pdK6UPryl7M6y8LI7HOfua67ofWMgUS9A2XRqYvIo5ema6Nj1q9TzKanVVEqVLLRD7cZblsqOQoKJIb63KO2QqMYIhFrghXwXRBbG9QjL4AY2CT2RNv8WgmG_9kIKGexYaGAWwMhIoIrYaykFO6OSegZyDaXVW1bD2X4qtp3mlrhPy8M5-zY_vk3cBl5Vok1-ccxgJv1STNcZPYV_TD9n_YtIpp1-tdECsr7ISxUyZyDMo-WAnv-hA6RycLdg_ljSbkO-IE1phTzOuju-tJrxZHJNhrMGf1_WjAvVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6fgahJUdqedkk3x5oeGycNdL-YKH39n4owjxuhBdAOQzDxyGxHY3LOlGLjRtHWlrKJanUZD0IndHmIltPJnQFCfl5fXqecmlinnLE_MtsJ950iPU3daUxl8Y2OOjgMKsWVPs4hySxQLwo5iOWwEk1hZwmLUCr-Wt1ea1VjmaYhGkUq9_ImA6elGXqSlcXeXhrWx9u7hIa91tqfFOAYIsQF7ZIjM6cTDe3YuDDVf-DJzUdaGTEM5buEywG8FBZo7hwv5CENDa1MTTsL-Bk7lq7MFfYh6pGQwpG4z8bjJOrPnZy2EdRHXCv1H-IrFxDEtRerp4iyEYymV4I_3cA1uBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMtC-Mi7evhEdlipPfOG3fgQGEF35yCMX0P0IODgU9mRsLr47dJvmrShQidcfq0X-USYzE6RXsHSFANUY-CIaLpYkr0r2U8kFK_e77S2GRjepV12joD3W-1Yd7VavItGnhEhsoNnZ6njrx-sg5riEl8RbsjCPCWfykAgnRr6e_88IXADD6nlDj_WNTglvcVLzVI3BtbzXHOVlQwPaR0WzzxrkdF-ga9-rgbXlaUyYwC97kJNyt_bPx6wZJMiIjYLXjIrP0grChfS8LFFL850ksjFU206WwsOGErCpGUX8vOq2uHYSdjBAVDiaHAlxW9ot2Xbi62JHj2w-96P9hH-Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwGx5y1_Kx5MsOTHtADa7Re1nUe9I8BNEVmvNmNsa9aiRrPVrcMoadTtfOC_1nMKvy0VMIjQ8OakkHLwGATY8dnG-t7ZLhTt5edyBdnOMOkFNJ6swk_T2AdVRofhQmRCaBhw9RDJPxAFUSIX30ShmNWiXyiw2DMPmq7h0dv4uhBkYP-oP4t_sfTmgTGNihT6BzHLhEr2oNO3JyZMDcN5Ib3ii4xMF8YElSDeEi9iAwIXb1H-UInMS508bpNuTfGECq_9IESGKF6098la7FPgl4mC0BVJJJVAskC6ujR30HrptN8J9ExoLX4VNE0NUyKalfJ9fKxpKwpxCW39AohfoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gW_hoXjaktQBa_BA_GeqIxDPzyzqdkjhCnIq5gNUIQwM_4kjqQ-UJnuDDOnqlyXq8THEqeSHPI9VRVa_n150CeLsVyzZS0hGyUIJR48Dj_FZo6NAPRWjMZCJvZ97mbENG_nNe-dAa6xFAWG9TvXHfYWe1VFGwd1HMwj6u5gKlIxUJ5qSxHnnsAsXDSFeiJBpXTK4dtMY-MmOO6IZO7VZjXV9pqMsK42KDgyubyBBwjpC_KR4Ia4B9GXBGsOzJqCtlSLdOhqWycIJhsFggWUPKRh_SfDsR38eE0-zD6rJxtXK21-acicHGBN1vEJSRRxEWG7eEj32mDrrvl5aBmp9iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKzH_2baXnuC2A8dl7056c_u3-8rrLQ7-NnFUo3Wqm8xTaWW16V5DF0Ci9FLnHtQO5wmu2jvBYoZdqdPy7Pl8zXjj2OJhccKuoLwnLNR4Bvmh8QcbWwFSpGUxScrupFKzHsq_k8VrfSldRIwJbazNYG8OIN23CD7q-UkMy2fbMxHc9m5g6iXCtMZrkxMw6rupOWa2Rb4lwGYI5O9WGRVFZykVu2zlrvSw8vZvgxcd-0pXXnGFhmf-LQaYI9hmvkmfxjA8HMCHONbdo8TSxez-SNNQvu3qfmDBAdrmnXASHL8J9N-EDjLna2fZsa4Bp4YH6WQaMRI2ErwnxYpnZl_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VL0LpMg1XlA1gcmEqFuG_1XYIosZvN-VoZUBk2d_K2BiVDZYN7Y2DrFh3x1NFeGbii_HTgIdsZ0k7uVcTJb4cJio35jA8VSigcFRuZpPQyKnJAPAKTxJzpCdRvn-_iuJOYaMTIf4kT1Tt5Rr7U2BeB139ztIOwRK-tKzwZFtnIJWtiKoRLNbW6B_48vW8FrpPKzX2e2dlrlymdhVE6cdhuleL0_Y9iCfAEtYM0UtwNK4x02QtS5bLPqn_I6zSxkIJkBsbGm5EpMSNpXbTFrLlXaYCS95mTMr0N9edWFZ-Y4EArNZ_XlrCKixJjGFwEZVuhcUC1K_ZUKsR6Xg_BdWpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

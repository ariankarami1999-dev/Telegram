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
<img src="https://cdn1.telesco.pe/file/URySgZHVjm34xSw1fVgbisa7Amx3Zqj2hzZAXh6a98zBSS0b2mdfHnEKwb0q_uvlugunqyL-8fXPRM90YRgUhkVdi_I8WS-mpvpenb3_FZgs3dXG2zzfpampIgKH-ilmfBdUGT86iJZOV1ci82FeYoBwYaPxjBQBunb_CnNWdAI-_X98FpJ3lLy9OWqpWiRBJ9JmkazotvaMoD6F77fwctWp76GMGDOeupfADTNzv-GtIG8VFg4cjB1RTxJZMUPEOkgO7GgahpQVAwu3nuG4v7CJsE0VRiv6SiWUNJEEW5Udb-R54tym0qvkn3sah4xBi8jRT_PasSAueLQnxSORfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UuP6UcOWeRgMZ56yL1z7LyVKaPdM9Z2wKSwgw2X8M65R5__vVp_ZING8yjl3XoONIw3B0QV_qT7e2BZ8gwH4SZ_D_FzPE1ePrv3x4ZaXCsTeYaYV9d4g2uJcQ5t61MNgkXM36cdPVLHKNa093WLdE4Ft-YdC4rtubYNBbskJ39qq01EboK5Xqxh8UXCWoL-wckGuEBEUyjKuM5Y_eyvcGhNGg44IYgsAWatWbn6eEvbVOcghrb4v-we0mBZtfTBAjqWCKYoswCXFu4fiQ5oqI3TP9lXlDsz6HMwHpQTHdXQFRgC1hKU5ezHpaeKqPzehPiWMpjFRI-QBZ9fozznlFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YaYB3LSt5GE0grsFR7hA3Ctv1wX3rpGIpEOmJB_fD3oPmdohtvUy-vgch2GWlXn61t5BM0XYN4mAj94xK9tRoqJeBsSXZwxk877okA-FUibMw5bJ0hakW1Jo4hiM4Xi54VaBJkuYakaJWhPtYMCvTb5GPvIQo6xvo2ZxMgXYBpVZeFYoM4iHuGIr9XLyaumtNOuYDBNxaY4o-0wjodXmQisbsmBFvJjUg7cSdrq1mANPcFMJsOX42fhUWPE7_fCPNQzFzueAD33JEcRZpNw0yph5MbFWup59NONwJRgvssfJKiNZMSOKmF4zZyBz5EVpkGTZJDDszqEpPr03AG1ZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7pvziRjIqOSRD3NPcM42vQ07c3MRHCx_2XWJB47GA5XZzcVWFHo9piYDPAPzq2lM7cUzXfB1QqqEfJqOWtilDSRm-l1l3Brna992gGU7bWeQQ66u9KEtinqkLN8pxyfeZSBUFBqBZyKTWqH-rdvkSbVtQs5f539lKe5GsLnRDxe9rRyCZjL_7UhtfIKk3qOj1kszoEI3UcvagfoSO_5tFV8_kaKy9bf9fkYz22wufyQ1ZWFTUKrHFzhi76777FnZLIERmzUo07q2rCVFMBJPm9nxM-sAoNDDUH63G5f6iqFmS3KVSTZFjDkEZ8h7eukMXEwqRk4d2j6amADnSrS0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EynBMKdGb_T5WorHzTG2-Q9rsVvbnjfdUBCW5gcVMDcq2TD19Vex2hKaeFeve0UzxPZxgVBzHettWJnTS7sohDo_eeOe4lIoXOfQNXARJoS0NfbMokajjMdJtIpsWFtduMw8uRQiYiFT97YcD31juSdvu_knfo3VqJMa567AI8V_1pe90HyNbe7kl7F29aq1c2J-oUSgNo5w1m0eh8tupDP44X5J1XNeTTm5fqLyuBz1FgiI1flFBY2Xz-ZLgU_y0KD1Yedf9173qy7Zm8UsjJmA_JmjWTH_Q8EOjpI_UuIYFJyYscZgRKgk4TdKQYD0lZOrjQ5Lh7jLBNigY84yqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6lghpxe4ndaLZCd6WMs09udWEaenBuHijxqPLEtNBlhFhT5LMbtzazUPObFwOn81jWHL6GiXvUURwTRSsyiD3zv8V4nt8VgJajp8mqEASyx2ECNWNSmqkrMvjhniL588oK9H-GEVGZdBbJQJ65PK-P88fmnRCR8tFKuiwqTUiIFL3H5LQWbArohlQkJmYb5Lq-YhlabbxQjAwbbhQbRM-uMZajjmVHwEAHC-VQlAMhKiC-s512sgKlrg-VhnZidt93D3gFjMc_cNIBiYH7aueztQOXYlxdJcpUa4PE9UqHTkSBbM2fXCYiAMZXulmxPdvtufCDkANk-D2AUOAHMSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lkwUJORhFq12Gc2_q0Sjyv83yYFhulKPHfrSaCwznP8pf5lkx5Qtt0YEarws0DClNXKcGMCorkxmldICxOCUjDK3R6wRtI0bcmp-XVOVT4FKs4BGaAFVaniRPVZqGzSbiyY3uywoeRi3bMpn81U1klyuNX5TAQTOMEJBZBCOJnbuAYZiQoHdv4zjxPkbf4ioXH5O_IF9lta5cyiJ_Yi5oLBeYw3DSvT3hBGWPklsfsL4L5PfoYAbYWwQYBrIep4iUHuTFz3QptsfkLZ0co8Xc38RV_WnaT3t7B9-liWpaaR2JXLy_OQpLk8tDetlxJXOen6x2XDFsphJDO8kwbuSBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyQKldGARhDtJACwAlcBBQHZcdNQ6G7ri4hDNps1aPRLStdQ05lylkuqm7wRNeK5S0ARwQpKUFgnymQaPa0updfwjZYjAoElOInqsQ_MpkhTycMpOjVGeP1pwNlLzssKHLy01zybzVypYk7qacGxtHh-dbEsVfjDZBu6a_9bCy74rSYWbn9mB50xVd6q4bfebIrOTMpM59lOuLmJIgSwAhi7Rpqz9_yq6uH8ivtOGpU0sIVcsHdxKsh3opRsgvPLvlPKxoxCKrF59NhobKgpy0BfSiTwDQhLzag37z8onLw8pH6Bh48cxwwfdIwP32tzf9snCLI9PUHudiQfxzVGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JBkxKBpVXNp9ebwCTDMLkq8I9jJBExND1QJdQog8yVuQmfb7HmlhTzJ1VvS0at_XBZQlp916MxRBhv5FVLnkuJNbKc9JXylFN-uio8gYyg_pQTejS-LwfL0aMomFZRBW-GHwPvfRm20JGfXKmMEOzV3xYTZkw39dQZKQYVfjElx5uBTcmBrz9EXMkhG-MG54C5m-BBClOokDhu-3rpDRKG0qkZepweOgtTLWspAX3ruDsAU4kR8rIbKISCEQeD6S6O7T-7b2ygP-3_9reZqe7pJ2GN0l54Nbyy4SUJnaHkjEkRUOoeIBu-v3Nr41fesf0oU9lU1AUA8qIOLdpkWqiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oGmf5YezLu3GZ4rvk01YpNcWxY1mCBxHsjqtp1aN6SBxL9BreGFpomInjnMjAm_0bJVcOyK3RyU2AvORrKa3_tvgfu_0p5nZRDIseMCUhON-NPhb2Ibxhd-hXsyqJFfTszzfgLchJX7V2vJDPNLIWaNyomHx7tSsOminM2URA-1FK0Af28c7zPJpYfyb09q0HxUtfRoURD6rP-UuNKGzczyZW73qRuLyHXeZavRbkR18J9Ylx52YwWHR3ldFAvHRpnehprbrcb4PYM56I4ConzRq2_H8jP7jRBBdOfR-PZ_7lOfXUSRy5_rTEoQjRXe67ZNt8S8qTj56yFxtV4tLjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=iRjof0GkA-bKRUw9gDZyJSFrmqo4HJjs4vlJ8FJI0WmU7uoPPop4-zGROzj09-opZaRpcr7AkX3sXtJJv3MSk9EqMWQNAqLn8JAHt1d5oD3U5Y02asGwqdnVilhxxCUauzZaWpnIseAj8QIr0dkK0oCqFXrZLh1D-jRKRJeSfs6EVw_cOVrjwaAVpr4twwP0iaVC8ZiAM6tqL4QM3aZ7d9hnFxuRGMFS-5rOHTJin3FcAdLIovrdd_mZ8w8xIr8ted5GwXKk_10AalIWf2xwjk1r8PTtIk1RtKhL5TCuiIRWAkvPvRurUwFJ6ZR6ir-lqtBEcbjG7zzxiK_u4J4mAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=iRjof0GkA-bKRUw9gDZyJSFrmqo4HJjs4vlJ8FJI0WmU7uoPPop4-zGROzj09-opZaRpcr7AkX3sXtJJv3MSk9EqMWQNAqLn8JAHt1d5oD3U5Y02asGwqdnVilhxxCUauzZaWpnIseAj8QIr0dkK0oCqFXrZLh1D-jRKRJeSfs6EVw_cOVrjwaAVpr4twwP0iaVC8ZiAM6tqL4QM3aZ7d9hnFxuRGMFS-5rOHTJin3FcAdLIovrdd_mZ8w8xIr8ted5GwXKk_10AalIWf2xwjk1r8PTtIk1RtKhL5TCuiIRWAkvPvRurUwFJ6ZR6ir-lqtBEcbjG7zzxiK_u4J4mAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ml9QI-VMR93Rd4S4hX6Ah3gI49Xlr9dHUr6rmXfQARJidyYdB1Ev5Ey8yDy-V2SHBpX93fm2fnTSSNYaQKz5mcbbjuoSW692JK32nfkTz1cFV-rwhI0ZdGIdnLChS4p8mKeulY8WBtqd4WJYVGYn-KUHE3sUSL9sjyagdMnocE9CX2XSBD727PfH_OwGfmTMe9mwr6gP-H7fmznDd4ugyaJusM5Wkzy1eJKIjjfBuO8_QTDVSP1XvBZy5uhSWMs2kfETxSDoPkrAY1WrZfr0z6PTKRnDLI1Sl0zXJZtPbD_E2SjslXpL2whv8RK46bd8W5mOqVLZeq69uy2MHWnlQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qoX4dTjsTQb9NUmz_2ynjv1tO24V5lblVru3T8N1igyHybPKKT9NuDLOpHPMnU31ChLqvSRv8OLGzZ2OyaSIQNuGFmsacyOsiJdjL72OwYY4IHsLUw2GNIZ07dizfJnQVJf9FYGqRBb5Od91tf0qFGtrgPwQgb7ksh8IdFpHPVL2-ZLnWpE5gnHVXkqZpNlaYQB1GOmzPCMCQRfpJKPXMRZHBE1g9hIIxJY2MM18hGqthrwILFBnSMJ7V0u_bBJ-ZQPV9ENEVqeCSOO5so-7sM3g9uuAXAsLOPYc981k0Q4f78bw9LHnrtAbvTW1hOJy2aWSEYgA-aQ9KSIDvBwGYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2gg0GlVD2cFKMkvRcS4XpRnh4VdJBPxI75CCWXAPhzUBQ6Spup8-9KN7V93NPCyo9DRRMq6jvLJnKgwm63pGombHI5WD0CVvO9HBv6Bp-ldAUw3Al7SyfQtupKOUq_NDHNlqCV6aOcsQ-kq0dttF-XMgrgk_jbn66FsDJlnYHWmAEomPgjsYE7McMVucbipCSl9QUtr6t5RgBm72frPQaJOtKg33l6oXMaFfwDujzT2U_ilyKvrFUOtJ80lBDoQdytf_IWqdaMRhP8WJ45bH4TKaJBLW6WuKNBW_9YlzpxHhikNxK1KXKoe5SAGiEIUJ8ENchTvQjVI4wR3egH4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dOA14iHyytppf00NXdk98vX6Nx45WjOrd9gOvdPdey86OMp027GObWdE93wckPSoUFY8poWvtEBdvHMM2idbFM67xGZmtPDkRqDMCA8lisZunrCClMh7d15hZhV1P614ZB8CqiVnZv3NY8T3CVCan0auifdYu-DOWSuCcPqCgWmsNwFgleuh6rdv3vQA7YLvaoAaS01gcJC1TRO38V09Z-PrL5GXs95g76kjjr32cbBh6tJKz5OteJ3AfS0dEKdwj3qiMRj8hEA9oeu4nFIrHqDIVa28jGW2K-COe2AJrNlda4UItrKjTVp9f99uSbDZSI6nB2V-Ko33LDRrKVzK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRermE4DDeQJMXHJJcOCekJbDmb0qfDLmA-gz_LXHKSYG_KAvdEPB6eHNXyLg-_t8Nz3LBsksf7qnQ0mKEjMtm7qL3_OCuNg5CHOjUcVFgt6fHl8759ESNkBs6AilUnuWHAh0BMNGYQjICkDpQ1EehEGomZwqCuZowpuqEmSaEaKK4GRrH7iVn_qtUhW7WcCS6LYlZ6vzlzaZEeaQnVPCfgtzgvQ9Mg293vlY9TMJJ2z0VU00lmLB4kkqxdmQ67TYttUlbm7TzAFCpAwhKH18AgyAb123kXM4F3Aks6A9oc4uZ-PVYz6TeYc_a1HK7I4XMJlrI8rR7uMTmiJwEvFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgWYhEOggWALUyKqD-3c9Vn3Tk1SRHqdn2AakKg8eQ_vB4TXtUZw1dQrKdto7zGu7IBIIWxB386Pv5S5SKVMx0nvM5Belx_bVlWkUd5fJMcGNDoNmndGCBInh4xymQpECNncqndsRlGkVySIkjy08kVa5WI6BNOLN1ssrNbB3LOIvJss9-JasqSC7nGHzaN9rtziwb97ozJH9SsmAIZkZzGLSSiW70FdXrnoEcAFOmw7sy3xdbtzPHMKQ6Unh1EebQmlzD9q6BiTdckssOetvx4nTUdACNlc1tu85PWK2oZmU6uo2kHUEN_PdE-pgjujsrgE65sfooQu9LXCduxgVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jxFl3710hoNga-PtOljLClwfameirrygB-jaEr8WSQfVbQaKzS6t14vCo_ONErleZc8eu_72SDme80SaoARGBvKhRZ-gNjupYR6QF69pGl954TToZrrbc0kyToDojb5uYyD2Pgtyn9qXVzvB9Wx-F_UfCuedGgOhaw3RYaIlNj8kvS2lnIT422dhybbtAbStzz-rbf9Ysr881krTIbsG_MQTfUL4z5G9diI6ofxg__mBxD1wGGT60BM8vmxyPS_1Of3hDU9TxaBoj6pqhdhj2tYsOdq1SKmcW26mclAw19fDrerjNnXAtABZ3jAmSnDbrha01Gxh1jpCoMLS5ejBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/opnJ6n0JSnazlgZmnbvgSqytUZvoSu3i5VnqL4bEwQKAtlfYO4DlBUHVJeRGGhSdRh6kmkWvHY6an60oSK6FiBKnJA5nE9JTEmgE8TTb1yppBY5ycWe9E2L6uzwit9do3Aa_v8rwXOHLviPRI5T-zbUAbSW-Pfznw35P_j-Hu3U53Aph_-3wecmV5R2TNc2t1jouulYWDw_Xs40tZGE8rSNeRvXeybVEDFZ0n4aeeVqEsXQvOzeqKO2Z-w1-OVxJapV8LE4w0etOQn8nliBtg5-oa8nM73sTO5jvReZdBs6kH5bhqHgJq_8Auk5yVGg3Lw9Wr9XgjCfZJppZ1n79Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jweF6vIscRJGF3pX3RNxB2iAxhxp3Qi1OHHTR6PBBo7ct1TfEV9nTnmrtC_PDk5ZdZGsq_8DDdIcllA62uu2WU43axPe7QE9-AS2OD9lRON4OHfWpEPyf4WMFHeFBLj6L8zugVmZQ9G85oCL3JqoCrlYbttUTZ8tpVO_Tax3_-c0PdV7VkdHTkUVm6hlNTvfCqcBWAGHmKCF14sEPZT-WlZrfvbxi6UYttaMA_rKSbVcPFhE-2PVxpRdYTPQo3IkRFyvo5GcuHI4-IwVkio52B82y3QkQ06_jm6cdXsuL5w8tCxJH000dC6ni58GJB_SGG3QatF17x9jrxAs8SbEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJSXQjSLOQIk2FWr77XXvDybRVX4eM35HHT4C71Ta7vayzEd5JqCv4lVMnomJziiV-UXyuTWzIE3t1KXNyXsJfae17DmdFylja3OwD7U7X3ocoA1bHoF9slgihu0zPXDqSGUWHnu40-cHnfNyDvmWP2gg4QEXVaknW-t8VjFFjNSyewzD-Jhir7ydJxp4YXC1t1xAfCQapewho357RLz9UeXfHl9mxPI_aw8Uo54ebhtKlH-GMP-hGilLQvT86P7BTFqJDg-kckLhA3BoUyO--sIuHsd8d39mAw_1-maRJaoug62OkIW1G5G4hPejub0lWUgTQpgIeQdbUuCV-ecOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bffjpW0SxGRmuxUdnuz_3O_qhyKFeBNEdczH4_7DlrXYidRE-Knj2SnFNdoGULzmqFZf0isLhgz6GfcTmILycXAG3r6lhVciXf5zTO3QwGFIjGtKzCkct5Uf5MYYGz-tvdXdeu0V0qBNTkd4yvgzURCxIQ6OzsL-rjGWqNqZj9I5AOO4K0hoME9OZ2qXbY-yXfOOXG8QgdJpdX3F3EKlY4IuJgn9NLtN2NVWgu-hSYksf5xsPoDvFHPkeXsWMV3TsuS4Su8T-Z4DTdLKhGlwRRiaxOkYDReosCRHH2zpSUm7wEROVvOd0B469ZKUBirVyIrMOtcYRP3U2T59Rlui6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NALyySLAOagbcgxmo5fRsbI6WeYyEw8GYy1jGM7-p1M6FuMTKhoBCnOI9XpKtxkmbnQXrDAtrFQtZm151Wnw4BGkbTMZ7UBu8xJT5eTL-vKTFZcdE8EcE1tjoWIsWdcBO1cvQLdG8kedFiUlR9nbCke6a6lSuhXRLNf5OiAnvHmcD1np1qx22uxXipA3SgxB5jor1MAegQq-QInIzJwV7U5vqkbVCYN-hxguPt_P8IGsADmIX5vUJAY5FmD-59saAj7D7wy5CjeyW2RtGQ3eFdTAKhjfI1s2kbiK80o5Zu2m0zVqO--yUYrZYUz5Wsb-hcHP7L21mOlutHnqbh2IiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJ7CrnybANV_XhJp7ou71DNC0dbefrjzmjyKYqAwAj5HJ-xaEd09jylEND8OdGBFIFOER4XKvfurdoqq4wm_N41rjR6uFCgTK4ocbkhzUQjbAyVyrEKnB2y7UgsT4AV_-umFFTEIBVCOzK0fcPBzHH_ix9jE1PNUXG-zoTNl69fOdPxUOt1LHz1QkFYga2KtMGOucxOdrgH_DQUtKqF4jARpOjuAe1DdvU5UhmvoqqlssltphL_7aI1RIzN1p-ubm9hhZfnQJUcx7hjWC2Meg_GJCKwi9lRu26intNYI35Cg_jCv7iXuUvPT1dUAUr9elpJQuXtjE_ViruFTDcvHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukxREkbJWnG1j3GxAniRvMbMR7uDt4D28Yq82Vo2nmZ5Vwjt8Jnw-OpyEOsgQo758Cfb1f66UWWyJzQK-DHNYqOhfp_jsx_HY5MkCGIQC9ImZI4m1kHHrio9LLm3Ug6YsozbEwi44muy_urCTfSX36eeJMbJ2uAqrsmItPjvjki2N6iBqLt4H_rT4MdIC9DRuK99_5YhpUlhz-Pn0lRqvdblzCu-15h4NDzbder__L_cC7YAACJwiSwIzwKlaEEZl0wkpKlQXtmLuw9dxrP7qiGSTeAH_lC8ZFlUrHdswKHGu2svwVobfHk3xL_Bx9vU6YpQ6PpTjWp7jR31oVKw1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2Xdf4E0QmevDCcDcbR-Q5ElZwXNtRC-ptJ2cxfsVqAZo28S1-bjoPeKw4HViLHXCuJfPVd0bXwLhe8HlD4LOEcQmInAWoKO9o2cxNYvnel-yFeEDuwhDIVgJr3YJj_Ltk9S1SdyUsNPD5AT5xyomBN2fj3dHCYYUOvTfs9VK6GX6819zF6WhJ-Ut4iHHkoXlBXbQeiHjQNSR9GgBZ9THbzCHvFZK39TAYcqkEc7HicfnpuHbQ_nGX81lL-B6m4dB77f11FDo6tIF_TXzu8Zo85oO1EoDH410mSO4ilRb-ryWTSlbvGwkKr7h6RDGwk7SuEoDX9UMstvU_zo_Q4cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uokWkx-wRs06Twio9DVCn0gc8jAuQCT9xpS40WCvY1cia-xPNI3Bym8fTDWmvs5IqppGxoLKB8KTsJZGr_r657UXq_gIz6ceYxZdT-zJ0nsL5BEnZOMofRHmdQWuYSkrNsRQ-7F26s-0HiPhPqhhhiOFhR6OkBNhfGHIbyUhhsbeBjk3J1K6g4SsXRgVfBb7I5mqGVWVq3MtWYNlGxS8YcFETOIDXBOX31NTxgYNFPGKVhVNY7gc1zS7EUzXxwoBP9X6bNWaoZFU_GIzN1zUcVmGUsrqIcVFVK2mQpCjN_Xh8suSH2bgY44IwDbqMNoKF5Hx3sjilymMz4OUFLG9aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EB-ChoDq_SJOWXyRJa4iBhRkbnMce97suPRrCw-V_ZvqKc5U8bigm2xwLdLTbsO5TEHDCVIAcFeyPJ_EArVL0TVZZtZS1nC8X4E_EuIm_18IIDEjZPBRb6oC3l6nMwp_WoQeRGMPaQT4sWltou_-szJdKUR-y7rodQGWA7SfeMTA9KYct60KURq12UIGxk9W9yvlu3OBBsgbE8ZvJSf5zF2VPop81KJkP_PeiZtd7td2htv6y-FlHSw353IS9AVm5svLBtoQ2Pk_leyGfo-dEMT1wWGidJKWq0f6tc_uFqpJW5f7yPGSRJR_A2YycvVZQQ7FAMAkjtc28ou9bp1oIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UwmdP7cO_9tAHmYyvGLGGJkVx6Rv3QUNtyRLTSUW66smZYaDrYhoImeLli604mlYGzx6CuEJOTBwCJ2KrSHU25ma3VkcsXArs47v6p1P5OXA2tZtd62q38GsWN6UxFHbQ-8cx_2nl6HQXQ23H4fW1yoEuMEi6SeFw6Ehc_Dn0myC1BUeAUTesNpFZJ-cRhouQM_fcs4o8AKUvUxiNzz0q_W8UYrhTgkDyy9QXm5B89lHNeLGSyzF3bgErC_1NFBXx8YzQEJVMRpfE4O1r807LvhLpax_C2LzVIkOqUop9RJEenWeb-FghLhvGPmhRMAY4r9WzHtwSDtjrQQdQQP9tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FuhQWUWcVAprJ-JS-MGi72rIi_uHPLIEVW354EPKbuMaLRfemazqR6KWRvEu_Ch8asPzGcNfgV8T6chUnZ8wOZlwTnz6op9E86OQ4mcxvOqBl4NSh46rczEefP5f6PTRi_wDpqd7x28xvH2WoZBU325pMmGY1h5zu8fWnfblTJtOOa9AB8W23dPUrW_yvbbvUdYvhaOISSTuq0Fd4Hze_r_djjn4UNuelQzphXhYsp-jdSRq6aGs1cBoIm1YCYcJBMiZ0OrFdk3txys5AMwyB6zaeFZGcQ5fyZs4WgaYYVPmvTeU0QzDLVP3QVkWBBqTlxQcPl9gFOoyiRrN00iidg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MgcHj2BDbbJ48WQH8dbsL4MvHRNn9kzAXMsCUd5eAPKsyzo5vGWKx1DgRRWoFKdD0df8e5aa_6gkvS5L6D7GIze1jUaN3G5E3AgId_pdJpiJNhHDpZTjQvBFlqf_-JYgiiY3CxwsDHkkNBNOTTDNLFxEnp7SP3gBYGlODRbLN2nLZlvtmS3EI2U6yRDIy0ipHDcaPwxjW6pq36n97VESXis-CVsIgZAnZLMntz4OMQAU9LmaJ177CWYuxHAQD95A-a8HGGrwdKI30Ph7auvBAv-jMXpFGAthAKQnxz1lMhiBH_WzLl2e6X2XbsITkBo1wSxzT4FaXAw7_6T8za303Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_MSc7sKwhRljhAC4gXkdGaG9GX67wYA8tsJMs0UNH9fKedx7M8ekAKiiSOQYCJLIZsghCx20v7ErPHqp5dL1xwC3IEmd3ILxXk3uU1myikFS1fUK0ybVzxcqORmx7C3XxF7jrXGMBrrG4yc4A_BArpY_voVlJ67nHcu5WJ7-K03YAZWEU3RJhoN3arvv_7SHvf1cyELVM-aGCnSyUt44bLLxY8qZUykh-pMnc0b65CiHyX-rHOWv5uCim4ZyS6bRtj8LNwTQDuAcwhmJr443i-oDXJ3p6jU8S2iA38f6BFfc5WS5kjCoixjhk6GoIq9e-E0lqoVrR7vvi5P-D3-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UogX_51nZUQTYft5qkocgbmTPaYbUVCC7OOjo-lRWn7B8ImJIpGmzkM_4daC8GPGNuRPCUxJah85nL7R0lpnklUm9k-RGEVFP3ADgcS1rqu2zwnjC4W8xTR0DZl29RTsZ4jL75UzvnrMus_se-_HbKHvl2eXizxHKmqtx_2e3H-Yk4JUCJhI1EzXbXzlBteMaNOHzbytbPPD12f1VQNKodc7yS1IDrK4BV7yD6mMhruYPS0SUfSrXRL60_y1QwuwakPCMNDVIfxKF6XL-EWOl8RICX3zCf13w4svpf0gQ8rIeAG2VBXSlb0Vx5L4pKTIRETNvYRA0k7GSkcfeLOocw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVd_XZYr188in1qa4m52C8U2Oxtq9rhCnlTXIsFgB685L6cSxlAbwOWWBhHSj-MZjvrjqS46N_sA1WTA7p95JOc0XfkPTGisq7neGE0PGjFiQ7PsKPEdrK9j60vCO3J_DmBqlSZ4nf7lAxt6ok451h01HkiBSNUK2KzVZmXi1PV5zmCCmbxS3wtGDF_xwuvSwFjOyKMC3CZjPBvX32Tyz0DAli8lopc5D7w1Yn8gcgJ437vAQst2ModfvVqUlqtKDfYMlvGrMoPbKY4_Ysc1UAcqCXj60jO9e4rfBUlc5Ddw4AcXg7LO4SJLsqnTqXTyPwm7sKwwgHyIEQcjXoZ43Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MM-PBCt8eOHwslXtyQQHDyBZ1YxIWoyKUOMCR1GmvZiJdL31TjAUIXOrqGs7dR6JzMi9rwiRjUuZLjRwsmqf78jD5RxgytQm9hG7AwThi5-pWOz-7kQvGGNg28wck5TxIZgA6cdoeRfvnHsnuTTj2R2VOazFSGGth4aF559wcQnU1oNmnyu0lpl7XcESw0Uw-z06zbPySL3Fs41HuIGnSEqdpNkUl0CLJLLbuamZgKH-VPGtkP7DbVTCBl1R3cD-marfLGcvq87oDDNmYm-Q_8SG9wjehT3TCZxlqXmH436Bv-crgCdOL1c7WH0yx9J-524KmKOwsRQnpD5X9XOzsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAhC5kGbWkVvQEIa75GQdGNWn8XDmD-eMFIyKEx9VTN78C3enpVR8BD-ojhYhVuDS5kSov59SoNNWnaw7eXV3-ZWb8k2fFnSolGjIoXfFQOmgNfZ5ecFRE9ugtF8ZJatqMCnXkSn11lBYVf8-1VcmMI4MKaVH_0ZeRwyl04YUWYh31LXock0x2dRxNWWRYMbvnH1c9ceP6_Lqh0LrWRSDYuvHXOwOahLIOwNOKJbePrwWrh8uslgT9XlJSMrcGKpUfJZ07-0moUh-E88jWdbWWbpIzN1mNrbr0UK_FVyL9MbFrVgKlLDHh3ckWBMLM1YgOiss0kTnn2MUAWBZADzVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ua1J68Ozd2QQHLII60yqGjaLqq4inM-rKPKZVYWllj7FAaEy0tj8fqKeD0ZA9-AM-r2NKLif-z5QPuNY9UkxGbWb_fCt4dw2HQG7YDZHe_x5unEPYdu4zbPr72Nt8i-V7D1S3kdxnMsQY2DkMvZoGcCFXBSN4qU0BBnnKyy9WHo9DQdmh4OrhvC67OH09IxU6lUm8JzbllRicIFp8e3UrZJllAtLHQjU8X3AKbWscX8nGZ9AEJo25c9bcSvgIrMT7LPgBY4pPN4gS8StXu4XWcfV5-VAK3CkDogI3ZnI5nIbo8vtNPz15XeSpaKC7f-xNp0-IMmojmLkD5SRBj_mMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ0IDxMJGEojuA0qBYD8tmAEYb_X7ZOb_MGADBvaQow_7jxvkVHzZoPo0OSzG7H1je2LPtikY2VpV7DB3KJm-alBePl_nhWOupHE4Uh_7LSVdLw3syDXHvIpltHgww8Fil7zGLFkX1L7fvD7X2Gq55kYKAhCv9edKqcnF_lqnrY_yDj7yAOXK0R-oSfVqzAOwG-vZJuM6YKlB9Jo3N-o81Ud1HEJCL4QlrX4cnkH-NvReMjOH1Ani6uAzdUw3JJ-lYOzax2ELPZbqpftX94vx_EPCX33GKfvNljRX51bt-oSdhUVdl06spW-tKYZkpBtZ5r1LajJ2bCKWqfT7hX9xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/soY6LXbTxd-NL0WmxmZ_PNI1xUWRhcGlWUhoIpUO_pLWl96REGWV0Br0OF-DEh-P4Qeqn-r4TAruPEpaupJ8auna8hZ4gxIy_bBWD_zts4dFZeHl5y60sQhHjWRGtb0MUDCpfl-BfGTRILAgbDhQBnnHINUx_HaMxPu9SQXIYfEMuRUVKF06Glm-zovpfgTWERnL4GcqmkleV2U4X4IxMKn6m0fv0Eg0te8WW38QTKkR8p_isOSCKIfaJ0Cbt2-hU2qBPvMdWwYmwuWSJ2ibf07SZOPnmqktL4XoGSDH7nOAXvxX013W9mMsvVh555Sf5sV2MpjbY-dK1pD6MisDaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UIHSVbMzG6JzrTon0xs6q8DCEYBWOA6xlD179zsEjpVTb1PwM9dTD0NLfnn76J_dvqqFnraOkpYOHeDDBTJeDLub64GOB7sDuhXjpZ6oPsKBgeaadJr6DwlFaJy2McjNtP6VNJRe1AsFJ6LZbaievVtHQEd7vfC-zsyT7eOezDFi2pEMgI1gmpTqKj6xQdjFp65GQZmj6ump2tK5Rn2KxtwRVjvp1tUVjjzxoBoiIHOsuoA1_O6JfwL0lq573LLLi_8NEVAPq3C4owq-vyODOCiqJadJlNAcYikqQOjsCctPv4j4HLHmGykBNI53lNT32_evimrG6yui9XIxWgFb7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/og8zjgJz_9y6ZM5n_7eHSsZujg7uytWnl4IwhpEyUNgf_fpuNN0bO6-2WAlbm4eXcWdn6eHBV_zg_0KWyXRlq5lgecC07gw6nwqXnPgnL6pbqOJ1gqI1xVH5cb1xbcGoh5ZfiATFOB8k5XSEXrLs5RlqUVtAKegChEWEiv6QcMyYXOXUnFMN5Fp7CV0TyTy-tNYWniprQXtpOKbaJhL1Ll8IZKRsSssFTxNTHZHo3QT6MqhXWTRdAJu5zqnTrKbNB9-gTIfqgx_O30tEluV6_ukFo1LsCAJfX3sNz8TJE_zoEtbk0Gs8B6I922cFBl_FoI_h4dGkvVbJ-ViL-XRlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QKyNXCUPkHNeiwgKAhH1mrAjGf2QU6AZI5BrIqlFwvv9mlS9UvKEiflMlB4DYICmQGpwq7cOo-DuFYO5BhAACy9XhSfkePY5NQxQ1P8QmMctWIGZ0LDJ_LvH8REpKuTMLQ_onUfgn7WRfQGIy14VaO9roAw9cYaakcjStjnShzvsqvudBqTlnzjYjUm0vkfaMDDypJiYGVvsFyu9VF26rQRHXSdkyuZ1TAlu3lcMv6zRrGE1tT-YAPIvWWCcHDEwqh0B_2BYJFREWQSy5aQca5qki7cuyZkyRjUsd5RhLtoo_0jifotDu_FeO3o7UwHELsIknpHlGtITMwa5mOFrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODPJ7ihLQIfxtjLW4HmsLbwTlbxc5mxvhYmlroW_xHCz1bM3ocu13kaxdgmmhTkPLFQbID6XAWTxhjFif3ItjVo31tYd1c3cNGtKiTa1nZF4Fj3t3jVAl8iQqGtdgr4vWjfHnruy8L_WpYJ_Y0u2OAsptYUKE9OXLmlQRYNAgJTpE_UORsOhiB9I4ARko3GPpUTVHGQcv6PmHvEFfHNFkDoj1ONKB_jIEGuWjozeVjeObNTaTlI7ud68yrXl1KEsQZWBDeNJ8XnlaC4AOzQHuUEMbaygAXUc-gAKtD6e4DaqUAXfNeyEGgL7nC3hg86r2OzkQ0UdHbC_xKVrH5oC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-SaIcCrCPO3df-UJiL4FzsdTvfRZlavmr5LcW3GtnDi9PNsa9_WUcdnLObeCXhVzQHdpliUUkC31cA6aFYHsYYNqXQ8B_O8cXpQ86vhqH6laeXFnDMI9gUPnsEO7_if4F3OZt_7MZQ0zbypWyNuOQNPC4tKO4OBcLERpVdOzJ-Arr1SCQkjAESIxzjoRVeLoTXNkULfj1Ovig93tmvNUwoZZgsXZFh6ILtumlgVG9TSpBnQr_xzBT-1Rgt3YETeb6C-QJsFJFm07C3S8ae_GS1TYDMMdDdnznqrLqQxksmAI9NeelC9nDJ6ueqt6vyDo9iT1BUzE-qRv79dtPZvKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIk1b_4753EPjURiMLssjfH75hJ1s4n49pypUGpyI87goZH3zKpK3YliQc6f48dmJKvXJz-ZxdnJVJMhKJgn2cv3KAXtUxuW4EJzTNEfpx6qfvYxF8W5Oob6H9cTvqJtJsEhpIaKvhWqt0dkUAylgEEwCyjuONjFRx3EurOw79OSF1t0nxdMe0fc3VgVIxNKX1QUCiFf3pirXCbaPQze6hFhSh9vkIKj-wmZCznBDogob9nBfgcrvPLSioJbYKS642zwU77-roxD4y2pLRp4psuUCQyQwiOu29Qep_-i9hruoMKf0i0wKAwT4GC7SwMJ26Z_Tl7QDxw6Nl8JNJDQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARSA9ihvhBmty7X3Opyib796e0GC7_TtwP9D2baTzEZpAH7KRhq24WTilRZH3kcgsYtmtywdfsVTLo_oKVi3G4nf-l7hRYJQZNyS0_76_14LyREl1lpdOBuSYXc82TUVVOz4TfrwUOcSLj-362-Si93b8f2BHoun09H6BrYI8zdtyjC6xIsBceSm863bHE2ZX1XkEAe1aduRYof6IOdi1YaiY5_9m7AFW0VrA6QX6zjJfLH9VW8d1wyMU4479_LBOlD_Fio77uz2Ua8Go8vqZx5nU0-EFrUEZGObr30XWw7Boa8ZZRk-cL3UAYCy20JCtjpBTYE39pjCtbr4dsNSsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MGYjG8eqwQzf1FXk1WgO-unuW8uCfjbCaBcwQnYF8aw65t86aD7VqjcCamgZn1Lkz_TtyYuxNuoPVGkAiyAr4yKkt05wk1TPv02FraKahR9cmYXAf5KfDOsOj1mqegB7lRxzoQvh-KMHch7xGWYhWlafvT5hfaxaoGfAsLDAf_j-xONPm20pMoYvTHNnYath0XhMpLdp46ysYIDu0EpOt_zVhYQMHWB5aIXtDeiBV-BpnUnYWORg9n2N07ZoFHHqGwtdEX1o_E0j_ULnHlQ9IBoyF5LdN4cSiJiTug6Y_CL4gBgDqW3S3QAOBE-sFyoiykg7AEgaXhhe55_QGDdhTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtQos9QGzLgejxKbx3dhFr2rPkV86VU-J08JLyzobIxze8XSom7uiTKP2RTlq1YT7hRY-b4kjGuQ6xwuHc1uvDDvJE_1qhKbCKqfkq2PpWywEoDDLTKEJpdTcYHKWUjnjCAhh3j64Hp2q2jDDPYFzbJdvfBMC394AGDFw7ugdl8Faq4tPAcAc6b1Gq2gOx04CYJ60jIW7YUbVCb83YCK6Di_6UoS6DehBCDc-ml_9zBbf5vjVO1o18HSwE6X89Pcqhe0FNn0k0hNLTA-kwkxGP0HXG3DwJamHub9DqLhqKW1FzG6WgEzbtBZL1E6m65EQzYyI5CSh54McplDlqkgkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tXbzRK-U-PdNOROlO4RzEpixRQVlF3xCO1Lo1ZJpth_Vohb9283UJ9eA1R6WLuPYMHKH7BD_4goJo2-ePI7lHE67B_5ZHdVAGHdpXMrXO4UL40JlJWcitqYbdS1b4tqOpS8PBdFL9lcZt15SVBxHf52tONvjwUuhcmXuIciWdFewWF0zQkb76K6nWUVoyPfyWeb4vOJmkyjaX0uCv1e9lEXMND-kaPTWMj_RSoB3W5nckzlgoYbP5tVSd8lR8Tuy68hHM1shkI0KdvT_RBzFiSK-dmdKJZZ3IdFjrAphOpaB8Sj8JZdlZCbhwQ8msKsTgmpjx18VbOMLmx2TFX5bmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cj2qiUZApBNnc1y6j3PWPaa1PQ3ACkUornxRiVs4gOnuwvWTIKZ2xZhuCSS5sEYf8u34y-6eWwe4jdBOV9813tEUFPCiCRAB99J0KIcURLMLUU3zN_btvjL7i400gcKs0-QiOSukFXeo9rPg8bs4MZmxXQCkpsbz4c75xd4UNHctsYk62YcTj1jIlQkHu9T_zVQdvzq8Cd2PAuL7WfkHcmzv4cVdNuCjNbHalYgDQrZSyVd9BGTcNajgjfS6YDhZmGMPjoxdRSI_QyMqgNQXzWiQwOxFELgRvdPk8u5ExbvpM2QANZE7zfXfFmCs25GXU1GKT-s105b3dWNUtVnkSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrijfJW-I5VQbTlVpM6L0jFgDztlII0ifC4DsAkfF3IGOvyOsckmN1g0kgPytvtYG8Ma6a-j3oc_sbfD0QM9U13mwKoFo2GBr4sKITeN1tNt4lJQZ-ZU4kIp4gyw8wMYNF835X7rlGlKZ2B3yXHnoY9ywgSxBPmpqLjV_j6-o8rbE1Cp-bBE4clNEEYuNzeZywE8LU83-oBJZbCllm2FD6vNNNz7tpjNZaBOjRbntD62YlVvwlyWy9kXypQYJDeqnzW-bwaL2-elF2Fd5dO0xn0QSmYsU-kk4e1nFKDEgiD_89ssLh9ZEiWevm7wwOvavgf63VkiDzAXEM2EaHph5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhqS8GpOP9rHKwzbcvm2zGuAYCmwzbkRGyBuX6ae_cUAPwg1xajCtnRXAbgd5qJ4iIWm-L696PwK5CxlgdbEhN3ZrJEpaEqeTd4_s-3z4M2hIeTavJ49IcTV5YFHxFB0yV_7boOrM0HbLCCgPAJlGOGQf8r6sIZ7w4XuNBkzkgM8wOQvLQakNvmxUyY6u0oyt-bsqofFZmP98L3zSaFipOVsEXfcOg3thJ3o5Vcnr3X479b9qObsHBNH5MUHF5oKbZeJiEWDU1jTHlwPxKDjpo4iSXGxhJFqJ48gxAa4KDTw5HMedenvoTQCnx6ucafMebDV6HACiwbz5ZTcMfl5aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W354g6u-LxF3j8H893dobSSi6FlkS27Jq83B03fLRVPcK_Fjy0Bz-iy2wif6hUxk7Ys69t8TQb-3gSpuv5U3tkqz7UMYOj2Mxxi6sSLoikSPWfSOljWaOXtG1l4E_a5rTNutJCBHDGOHg3OLgB7PjZ8cagX171DSeO4-rvD_BSpkcuR6sJtGZCLPJxA15rBUMkgghpeGgXWKBXb9DXA3bxkAN-dhqVhmbUvpq1q5qGFKppUeilZVT9yzYuF0s3X6cRPWOp0uhe7707CF-tvpsf6NEORHskXouKHuy2MgIlY-AhDNrUpRryF5YLQ1Eu3z-LmneOJzf3C4XU5KT2xyTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lWojjrJ195CssM3MrhFE3ktBDWtc-8wgQk8x9zHopv0pO7rPXQmM5tOQqbltJQQB53vPzbcUgKlstVvOpa7Ow9NIdr5f_IXdoPPjqPocIcpzIC_u8mPgyxpsm6nKRQK4ClS0BFgIrqKWslN5GyJcSF_sFd8JWwOXqGG_9n6JPgacw6XilhEPKgHvF8667VJUPDsDOUd6LNpeAvPwaldZrUaqfqOK4Yv-y8J9ToHUjUTMTGvLfT_5p2K-KRIEwfF1dDRblOVHUgouxMuooCij3JkAE088jq88lEIExlyuEkU5lk_CNujFdVFwaoR-LC6U7b2gwaJNWtcHaUTXf82S5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vcp0dcb5Y9kq3iPL2lzrAz0c8oTxieQdhnFsg2aVNvAaqjsDSnMAZeq3birY99Jc7TOa-XvWTcWAE-ENYTqIDT2NkeBCt60VcZwXDVj2GbLvGaxJyzVxT5xy_jhH3K1dku7bo1nBaLm4Iqt70ONGu4DA2D_Z-P1ukmrXBsDv3PIsbWiNMKxDmIgeJawA3mT8OlxAI9bPWvpg4WAYcmWcFHYXg0YXUong56UF4SE-V-8SNOkb0xC28Rj2omUw2Nn3nQINaW_0lTGDuIS_Iv27eIGTzjIbJ2IN5uV7cS5iiL1TL7_KWszKQuMaGE4HB8WFNTmjDD9ZvuT3MNr2cKbQmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VKCQp25t3-LMD8zHM_p7ASKr1yAlUwkXWi3WPOf_3KeoGjXGVrAz9G1-I9H1dy3PJixEozuIDKV74rnQ4XvWH97cwoE4wWa4O_9KH16fMymOj9rc3kFmibcIPaD6PSAmYR6u3e0Oxhx5yuEaBnF7gh8t1cm2FWOMd1NSxLMVaPPqU2gU2PIUjFMc1NQAAiB9WPQWzGNfLLDOqS-tfDshwvViKkY4NgdhyaroBQmZCxEISusWZ-niKwjD9IUOTGdCx7GJId19jGHmU0pXXXlZGbKS23Gws7EJMQ3vxPKVMFn_5wjau-Rraz0d8DdSf8WqE1Iit0SRcxDSLK_b2RmN7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGfTXHRA5ICFfYGomfV38T-zeqCY9xa5NRZz3qDuT5fTceYlur_qvlloIy_hJKTRsKCQuuC-7Bg3TXIGuw_RYKSeGm6GLsYo3XUEeNf-mH4wiShgxuX-rdLpwhuAfQ1uigFfFSO1zxdxjw-Skaq6yjRz85nIUecJrQcPQAU46m5PL5ckZTb3_gQrMR3Ub3Xil4lGdmeRhK_QilvwRVo7OWzmCjKM6U-w_HcX96HBH_2UiJpch0GBgXX54KtPRb_4uA0NqkmBndrVioQk4HcjuvkW4mkMJ1EEK0lilXoYCnPxaO1012-sx7G6LTeQD5p01chx6KxdUl9KulYONtrMXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PydBsxvn7fmna7HXFbHI205_KwhZnu6zsA9bI38sHbP9roCViTv7SZLQ37WCBnqr6aqJvwFLwHeavjXPepRqwGN7LaXcSsr_AsdVWV33xElzLf71-lSrVNJchvddde2DxdeHsDz7LjnnYcPmUJUnWfgfj1MCRf8J7NHYn8Q-lg0NJUgzOZV115VY4MJvryvxpKND67zga8gm-aa3UclwZGfi-gq-7mHve9-wNYgN1g8RfNmrz9nrHOSeUmqmOKHyKVoQmpTknH9dkNbSymBxPmWRqYX4NU_1WGY9vHoBSVfBpazRCQj52FK9POV2Aa7aDrAE3WqGqnV37Pak9gxe1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7TBOaPJ2dcrk8E-ucbb_3B6wAgq95zl5PPL6yS0aLdtPLaaTbmV9D84XDsv4IOKnpQBeGENGluLph9XUXq9OU367-4AbvMmBXrHiZcqTzDxHlpxosv148SQTzxMA4PX453sUS6_uEcyshDjrIcV5wUtQC8rMbSNE6G9YPfA1jTIqGKEXwX-c5G20-lE5yzn6nCA0Ew9FjWQmZAg9R77gnDHAqKdaLkOCtiK8VPer55B0fQiptEC0l63LymPxRbS5XyHqCkxAHsF0zHsB-0iMNongDiH4fJce-Ro5-xFYNUqk6gxq3IAkrMhEaQZl30H_J6HR8jsg3E8Q8T0A33LWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R3UGyoOZg6EouN1bWRywmYiLp2es5VmNyqJEWiud9IgiyIIga-Gy2ShkViPPcwIgE5dZaNXykCtdzQpZeVcxr7rlNqquQk5STGge02rOWXYigD7ODU2RNFG6yrngvYbWmX0aI_NcKONyy7omhbbF33UnuzYpq8wdCv__BhEYwi-sbkG0EvPwsJAUZnEShGP-dkb4B6Ko1ISrbbLI4iSasAmsW4tSGyQbyeVZvhiYTOBfXXLqy1-9VbhezJN0XyvsLnWdjPXmONL3E3bO2y0ty971BCBocDcrLzLJFD99W_ubsLZI_bi0OpZCe-1D39i3yqK_wmmrDbIfhvO6T8wjZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PArQue2bqdHgAPPSKm7SJo1awC2FU5Y71mANXsiZKZLXocxNnhNcTD2xC4MO12B9nUoxJKJ2pbPZeo9rjTk1S2I2Qnh4QZpyFp6Jb9sGNzxtfkIsaBtyK4EdKl59TyFcfmiz_yUrJLa2_ZmgL-v3HMQMuFO-mlVIqb7vPnshweWop0iIF-7hxod0oXKN-gVayo-812d7rqV6u1OprCJoZy95KzGi2yUW_9GT_KPuHuidlUCSuD2SGkiGOjcotdCCB_sgjxogWFsLFGX12V0U1vYe1TQWvP5gJKslaZm1x3GbbCRUtmwiGdiOuTBaG2W7k_YO24NePwvFJYpXd0CV3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUSUmQj7WtisNMisneN4lOrIi4sEEKrV--lglwHvYY3eMTLU3KwyoXzhoMQyCkLijvwzxO6Gor1ltsgmB4FW9kBwRyGuDF_WC3dk1L5ZxDu3Yaz_yZYRrot0c2DwelId5T-IwLwvNoM0xNHdBV0vCXUN0lEGGrKu0pfxWuh6HYqVI-MKanxYUVU-btS0H7nCL5arp6AS2kJWuthbsnmZ2hyXEEtXEGK6V_l2mncv4jF7XYSxiZiCE8V3tTAykt2Ckzzq3QHQ3D9IEjEkMUYlj2LzWKm1lXeyi6F2_ad4G3gzat8SIarkcDt5T87RHResJwxM1g0Yo_nlr8g_lWKhyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e8hXwz6B7nxIZDGG75qok2cs-FPe5_ZDTMewJsahv1Qg2tOYzM8rUJrfiVDYaaBWwO_ODJIj1JUoicPwiYBp7bfYZCQzaodmKUNDByyr_TEh7g1woFwXbuGCqa-NhU0Re6yb4TqY7XYbydfKLrpatv4fn7zrwEesNrY_ctgRX6LwSUq6AcCj07ddSyPaH7k6xjC3pY-t4eufn2X4lTSZ0L43e-nwPFu0Gg461uJQxYY1dXkfrD-SyH4xb9tTlp_srrhMrQHexbgcaORMLtHb2IGwF39iD-bKnXgFdGlZYcl5ew2X5o_0XKxtnQFd1t1XsfM9VP3znYRQYmlpjTeawA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6phfzLtCJWKqj7cnZsgfpbewtpapANOb_cRC9M8m-m-SMZ5rltLCBkv4TGgzNvpokZpdLvwIdd5VAW1yLDwBh-KQ5ewDGKoFjOD-jWDhU7B1unshdeoJ6WU-CWHxLDkg8tR6PDKjTRNiaOaZp6XwNnJ2k1DFGfjKLM36ZVE5Dx-t1enAcHje2ObLtkMLCJNUEW57DvBRYRFDvyP9nk92gkt5BX9V0b4wn2cR3hF5A9KxiKI2UYtaydm_T7k4Z7LTy_pvNeHYNc6yRYXuFCys6VqanWumzJdhDt87WQ1eN3J8HmIcArdJ1LUwR8oWNOQviDPWhavCbgLf2UjhkbfwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhaGZ8jMdLGZxU5F-vW-aTkBTMGTTOuBtimX_feT7yDwIxDVULdZPYHlHn_7-TaEG8Ii5CG_bogG8WZ_IfriSnwaf0Px1ZzdOZk-6leB0WZvaI77MV9mUjEuA0JBwO73IxWDFXQRtm7ZY9V_cyf6YgN577d378EsGUMMm9uJzR77ILyewNZv9XdnnvtqKnSC3bV9aJRrXO3Sw3To7vBb7Zp2lvh0Hz-TIaP3NYa75nQ1fOu4Xngx2fDqu_tXPIHeGoF7Ph_iKbfZPKCLyNO1-YbXOVxOzavsOq1S8qBJ9vMKiWoqZdXjYwzslCEZbzyzd1xf560yLn7p80OWBUDSCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q03dwcI6GJX_r_jwJyJzpsoZq7mozfvVh3BLRRr1zH500IUgKxorELUW1KFktOqcZnRSoh9W30X2MsJGIBV2DbGQEvr_fp7tNWXJevYg2sJiLmdatlUeiAFwr8LS03FY43oxLepoKKfthBsTOR_IQjT8uOd0OLFMXgooXmORxbr39G-lBaAGtGehiM4C_5Mn0Wrkto-lhlGLQ2VFQuWmw6Lb8qtV77q6KZJ9BDKkTFSZRs8d1BTGg74df46qygJF4fpESnxFz0MTak9XUmBCDhQD30U3Z6GomtdzfRUrwDTHYUqrsWwzHz3ntCM7A_49HoQqyE-FSylKBS3Qu16_TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTMGfD8RfN4LxMVMC1npi0-9MSCIXzoEdWyw8gLV23bKZbftRF4JoLI2KbjE0WbT-qtQ0hgTV8E42fpzU0nSMUdnZbRpvqBQeZhf6vfTfose7WtMSUsfukPM8e-j4GyqGxZFrtCYVe6vaoPqLeswk6IhwN0BKS_gQGgH_6J5U3B9GTVN4JFBKYoeRV6IDUQQjX_F69TK03ogWAaYvoDZUQWueDPs4IUM5JQu_CjUCcKWKUwiaebO7Dys6ieKUwmAYFyIGLIKckagOiqEV1X61J-qbMaLN9r51nDPRAWx1a8gpdi3CDfpSjV_8uqRoVxkkNft2zVN5O850vnkdvmZjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYRI9ndcc9j6ZVW1P2F3kpnH95LrUEqhG46PyO_c8HHF8EFnQtociWIkmkuDjPpAlFKvHaReFQMu6rrxYxwnl33_5F6u5HU27V6tePNnGf5nCSYB4XIRFFNlGygLs4uZIIMLGNiDXNh56EgmKXkSd-Z2k1vqfg9YvAUjdsVuGMlO5hAtdbQ6iIl9POGJlvEq5xBz3tZ92YIboWyO9iHF-VIJc3ixTTFU-jMVYirMsYlwe-Sf6mswBO720h1iiqTb8bp8UvZwsJGT9Ilh1MnnDnjbyZQ4O7enDjBKv-zjc1goqBKz44ygBZBdUhbFd1pvohXkIdo7pIl35olDKCIJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgZ5WEI0vFO0tYsFci7aQoQk_m_6O4mfIJlPOoHxmUnU0Fyl27ybVkYGdwSi2A3uA_Z0pRUwrPAWUHkFp0o1l207LYhE21PGdqhgjOSaGqpnONdOGkucpzl9NGjofW8opLbstL4jbKUSG5AtYqQXaJaTOVQzMdtHTLDz9hBb8XeopSq3XA3DEJGqLkERBEtrnITV8UAu5ZFUnzXQAbqY8bNCVGTk0Qyp9uhkYCitX6mMeYb3u1mBQ-7CBg46hKXnrp67IyGIY6VGlDzGvgB5gmHs0Vb4f0Eni_mvogrnD0itYLyiKq4dctPMEJ6KYxohYwFfR9c6B4GaC7AtA8SS7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_vB0ORTL-b3ttqqshM4ROp4WTDWKXd_fiXm0Vu1Swt0Y2ROjZtg7YQ8taqmaiQBpUTdusDe3kktPxexZZfz6-Pmw9w637-TZ4V9qPLWzWGwx1J5H8AVvQufVaO6TqiJTrxwE6Q-iLHH2nuLYXX_Y81kEocBqXYA2SIZ-WzXC7k2erOZSlspA6z8t85z0XoICE1pold7KEGUKYHEJqEmkucKFxMrAMj_6ixVm1--2RE-7XeL6FPUW-UncIUsXiDT2LEpMmyoWnXvLOn37R7nc5NOaDIo77FUDMZp6Z5d9CvJYteLFvR4tEDJeP9rcFzh0T-u0SwXU-oxoB9zKCyj8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kp7LJS0QdkTb519Coqt35I4NlM_kjeye2LmdGwDIA414ZuWzf6ygm728TcKNSn8N8x5d1Kbbbvnc2lANGivDi46xp3d9_m0FE4XX8O0AIN9RhU5pHBj2GayTEpoZegrSfdY5sMwGwewkVHo-6XNJIz1V-oDEtAunwUg-pLyDX4h0OrM_Tk63pBU5d-NLCe0fgQNhgwyWXte417PDrHpLr09D2wt-DUmxB9yfUBVomuUn0naPdYf1KT_6adl5BugZhFjfXzP1QGcUZ2JRVBWgjNs-oDVisQT524UkdJQQC_JtEgds07v-FU7KNswQSiicDwb9t9ZimcTinZQ0q_YMTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JualkAMiSFQYAafEe_O8U8cYZd9j4pauHXNd14fcm80FPKWEEJb4soz04F7gkn2Afn9P3Ny5e6qVvkhXzuXG8D9KPh9sYa8lP149ejnlotRva_bvsLiuICqb5beXmaT4BLkOcyjfQarvgFwXtgWmtQgg-M1GjEzLqFdfhWZfqbJXsmPm6s1Iv2D64JVjRDuCoNzHLoFfR_TJ2fSS1cqktYCDCbUWMUcvnQZIDaICyptYpTVqSfirj_-A8rLmQ37hVCd4K37Oh-_SX7peEvPcWhGoZVHTORoBk9cIU7LrjV8cJVa1YZ2f1R11goE37vPgLM0jfL4SOGW1L_67skCnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

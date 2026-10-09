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
<img src="https://cdn4.telesco.pe/file/rhoWiHMht30ahx5HEXiP5uxmubGRIbglKgm3mnyN1Y5S7kRS8bLfLPRdwLvzgQvYSLguewlpqTQj4b05VGbnbO62dMwWYzJcNpUN3XGcq6DQGOhQe_DxtAcewRjvOTE7AYZCZFc551vMLFc2Pu_Qy3j3UCNzO1fdd37Zr1Kc4Foi5l1WkApRK7aKTjxvXqSCimIMeiX_tigXVGqSRF5w3Be5VlVqjZKREziPRaNjC6sSm7-E8gaCxWSOjBeMdH52NlKiZ3MCNQBQTrlzoParRHhNVV2zZPy28Y3E6gg9xlbhoFL26gmb_PYgAOfbu5xPxC8X805KCrL8YUSd2B2R6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-1936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAkP31AxcsbL44dSTp8yMsZZVJgXMk72zSNXNC0Liy3GDRNlTMmkSfsGvv_uw18Pinkxprof39wSys6paTSKSy2fCSHMBffZATNfiD8uBUwVXkkL7YsOPrvPybgnCs7GcaCpOMPRlSqmomyprpN9v__s8haZm2PjtheLBz4jfQc5ILBxPQSmZaTrbkg-X9LqtjzMZMjrWxlr9MwGLeRgVhcE_2yFGv7CnTegbBRcPmcX5jrpF0eDQWmXerLmoAEO5cJBoGt30EKmpz3OUK4sLQjUsOWUDmEX0DNJtmPC4-kk96xdUir2Nibz7i-Y109sdFCpuYnmvayDjuzEmPhTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
ساخت پروکسی رایگان با Cloudflare!
⚡️
توی این آموزش یاد می‌گیری چطور فقط توی چند دقیقه پروکسی خودت رو بسازی.
🚀
🔗
لینک ویدیو:
https://youtu.be/8JytQZ1unz0
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/whitedns/1936" target="_blank">📅 18:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALHoTsXGXYvBa9EhxcFjzmg4NHQuM6_M_TU0nWQSWRt3NGDfcGGrBSwYPWrCcPmlUUIAlxACx9vXuZYEVYmphv5gdbFlF5J5kSLTvme1mzuDe3HfT49GtD_QmzjphagJ0Hy42WUh6ZvvFgDAUA9g7C4RSHQ0oan74leYPm2TVJG4jD-nv7KZ6-8ubMm-wayNdjFAiNvxx6gYcgHNjCkM7r8YtEsHbXsrLX0LurG7qrsUsaC1fLLryT4eGTBn3l45O88s86GEjt_7LOkivXY50-3dcL0B6WNXzEKdbN17k4mEn0yr2T0ghtav5F7CoquPYKslv4XoGGvl39YZlPGELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی ویدیوی جدید رفتیم سراغ CoreForge، یه اپلیکیشن کاربردی برای آیفون که از روش‌های مختلف اتصال، از VPN معمولی تا DNS Tunnel، برای شرایط متفاوت اینترنت ایران پشتیبانی می‌کنه.
🔥
از نصب و تنظیمات تا قابلیت‌هاش رو بررسی کردیم.
📹
تماشای ویدیو:
https://www.youtube.com/watch?v=yPLb4z4nF70
📱
کانال برنامه:
@coreforgeios</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/whitedns/1935" target="_blank">📅 14:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.3.10-P63_arm64-v8a.apk</div>
  <div class="tg-doc-extra">73 MB</div>
</div>
<a href="https://t.me/whitedns/1934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/whitedns/1934" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P63
منتشر شد.
تغییرات اصلی
:
۱. با تغییرات انجام شده امکان اتصال به پروتکل MASQUE-HTTP/2 روی اکثر نت‌ها امکان پذیر شد.
همچنین پروتوکل جدید
Wireguard-Over-Masque (new gool)
اضافه شده، اتصال به این پروتوکل به شما ipی غیر ایران میده، در نتیجه برای دور زدن تحریم‌ها نیاز به چین کردن آن با سایفون و یا سایر کانفیگها ندارید (نوع HTTP/2ش رو اکثر نت‌ها وصل میشه).
۲. کانفیگ‌های اتر (warp/psiphon/tor) را اکنون میتوانید به سادگی از طریق exit-node با هر کانفیگ دلخواهی از همان منوی اتر چین کنید:
selected-config -> warp/psiphon/tor
(برای برعکسش همچنان باید از قسمت add proxy chain اقدام کنید)
///
فرگمنت به طور کامل روی فایروال همراه اول حتی روی IPv6 هم بسته شد، در نتیجه فعلا تا انتشار متد جدید امکان استفاده از Serverless-for-Iran رو اکثر نت‌ها مقدور نیست (همچنان برای دسترسی مستقیم به یوتویوب برای سرعت و حذف تبلیغاتش میتونید از Mitm-DomainFronting استفاده کنید)
///
با توجه موارد بالا پست
https://t.me/patt_channel_x/166
هم آپدیت شد.</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/whitedns/1933" target="_blank">📅 04:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EW240iaB7FRhxf7NuL0p3jxVr0m_EOQ6X2KnaiQm4JSHXZ7wZIP4LwbRRqCO1JBWPMqhCJnns3NcvF9pdZTd0ivndS-AvmyQFH1bCcHCRKHV5SFKmomGjFkhb2i5wKrtpBhY1-_B_DUAKA__0Su3IkFMpikvUuyZlRXo61hRaGyqEhDkqL2pkLudLlVH_EDx1pNT-VlR5HDHFAd2-9ATAornzoTpvyLUbaOapHlNsHzZ5soGo02kzIqgVOJF7IFnXGf6tJPMJIQpBpHycyHtZfDy2iHTf_cMwe6K12PEscdHVunalyPO1Kjbuyt4t3L5aN_OGYL7sGTZxQHGkvNA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W8n5xKJPnhc56tjDjaUcfK1pf2XwY3_-JpCyThdoWJ-UcDlzfYnNjUoeDzSXNwxzxauiEJN7-emJkwYjnFAvY737EToDbNffrXwO9V1zWJPj2uqh2i8NfnUVksG3-4E_4HRu8jnj6wJes0VhFnnuSlhCfqCywLIGYVOWah-Bx_hjlUuhW7n_I_N1zRJWmO7LLAOsPcHqkvcASLCF7bOludpj0eNgaqDrbhPM1jqDN1QOqN4MlbYnwUoNX0rZgZ30U927bzScoZVtZwdlhNqFv7xwp9q1YrPARUneij_qhcsAmEiLbh_BD3daP-8n6zc5Jhqqmcu81V8rapaNLeqyeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این تصاویر هم مربوط به تغییراتی هستش که باید در کلاینت MahsaNG ایجاد کنید دوستان گرامی</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1931" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درود بر همگی دوستان عزیز
😊
یک راهکاری را یکی از بچه های کانال پیشنهاد داده
اسمش رو نمیشه «متد» گذاشت، ولی راهکار خوبی هست.
میتونید امتحان کنید امیدوارم برای شما هم کار کنه
مرحله ۱ — آماده سازی کانفیگ
ابتدا یک کانفیگ از هر پنلی که میخواید (مثلاً BPB و ...) بگیرید و متد Fragment + Fingerprint رو روی اون اعمال کنید. برای این کار، نصب کلاینت PattNG لازمه:
🔗
https://github.com/patterniha/PattNG
مرحله ۲ — آموزش اعمال متد
۱. کانفیگی که از پنل گرفتید رو در کلاینت وارد کنید.
۲. روی آیکون ویرایش (مداد) کانفیگ بزنید و مقادیر زیر رو اعمال کنید:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
۳. بعد از اعمال، یک تست بگیرید و سرعت رو بررسی کنید.
⚠️
نکته: من به تازگی متوجه شدم سرعت متد افت کرده — و به نظر «فیلترچی» عاملش هست، بگذریم!
😅
برای افزایش سرعت این متد، دو راهکار داریم:
راهکار اول — ساخت کانفیگ ترکیبی (Chain)
۱. یک کانفیگ «اتر» با قابلیت سایفون روشن و پروتکل WireGuard بسازید (نوع پروتکل برای هر اپراتور فرق داره، نوع اتصال سایفون هم خودکار).
۲. کانفیگ ساخته شده رو در کلاینت، از بخش «افزودن کانفیگ»، گزینه یChain Proxy رو انتخاب کنید.
۳. دو کادر خالی ظاهر میشه:
- یک اسم دلخواه بذارید (پیشنهاد من: «فیلترچی احوال مادر گرامی چطوره؟»
😄
)
- در کادر اول: کانفیگ BPB که متد روش اعمال شده
- در کادر دوم: کانفیگ اتر
- بعد دکمهی Save رو بزنید.
۴. حالا سرعت رو روی منطقهی خودتون تست کنید. اگه کارتون رو راه انداخت که عالیه؛ اگه سرعت ضعیف بود، برید سراغ راهکار دوم.
راهکار دوم — کلاینت مهسا NG
۱. کلاینت MahsaNG رو از گوگل پلی دانلود کنید:
🔗
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
۲. همون کانفیگ BPB که متد روش اعمال شده رو کپی و در مهسا NG وارد کنید.
۳. نحوهی انجام کار رو به صورت تصویری براتون میگذاریم
موفق باشید!
🚀
به امید آزادی
🫡
@whitedns</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1930" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!  نسخهٔ مک ForgeCore از ریویو اپل گذشت و حالا روی TestFlight در دسترسه.
🚀
📥
دانلود و نصب: https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید: اول اپ رو کامل پاک کنید، بعد از لینک بالا دوباره…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1929" target="_blank">📅 08:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/whitedns/1926" target="_blank">📅 00:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVX6v-hfYS-CGS0KANAsTfaqTiesZrnyGULELw3QhdepFR7YgoLTY2za3i4VyfNifXsrHP802l8XcYtrtfX4x_NntBFbTMHlAaWvrRCi9_mHWdTTMTJhm2JCEXmIY4qaiPrHIxy-d9fp_q8szTZN3shrEUBbCb4JmR2lGfcDSwfVp1zCPsbJcmwPUt5Snvxii-htUGcvpP7d6ZNOPMSjTP5m4C5H3INpsKbsekdUh1O6UKCm_q6srIUTy9_BXlZ7dPpu6f-x6M6E5O031iAe8yR59vqvAcCpFIAKSLS0ZoJHDwhJ8qzg4wSyB0kAEAcQmqFzJxQzQ6XlX1JDG5af2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/whitedns/1925" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
آپدیت مهم WhiteDNS
فایروال جدید، ترافیک DNS بالاتر از حدود ۶ کوئری در ثانیه را محدود می‌کند و همین موضوع باعث قطع شدن بسیاری از تونل‌ها شده است.
برای اتصال پایدارتر، برنامه را به آخرین نسخه آپدیت کنید
👇
📱
دانلود نسخه اندروید 1.6.4
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.4
💻
دانلود نسخه دسکتاپ 1.2.4
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.4
⭐️
تغییرات و تنظیمات پیشنهادی
🔹
محدودیت نرخ ارسال کوئری
در تنظیمات پروفایل CottenDNS، گزینه Query Rate Limit را روی ۳ کوئری در ثانیه قرار دهید. ممکن است سرعت کمی کاهش پیدا کند، اما اتصال پایدارتر خواهد بود.
اگر با اضافه کردن Resolverهای بیشتر سرعت بهتر شد، گزینه Rate Limit Counts را روی Per Resolver قرار دهید.
🔹
تصادفی‌سازی زمان ارسال کوئری‌ها
گزینه Timing Mask را روی Light یا Strong تنظیم کنید تا زمان ارسال کوئری‌ها تصادفی شود و ترافیک شما ریتم ثابت و قابل تشخیص نداشته باشد.
🔹
تعویض خودکار دامنه
اگر دامنه سرور مسدود شود، برنامه به‌صورت خودکار به یکی از دامنه‌های جایگزین دریافت‌شده از سرور سوییچ می‌کند؛ بدون نیاز به ساخت پروفایل جدید.
🔹
اتصال پایدارتر
پاسخ‌های جعلی Domain Does Not Exist یا NXDOMAIN که فایروال ایجاد می‌کند، دیگر باعث حذف Resolverهای سالم هنگام برقراری اتصال نمی‌شوند.
👀
محدودیت نرخ ارسال کوئری و تصادفی‌سازی زمان ارسال به‌صورت پیش‌فرض خاموش‌اند. برای استفاده از آن‌ها، تنظیمات بالا را فعال کنید.
🖥
برای مدیران سرور
ابتدا نسخه سرور CottenDNS را به آخرین نسخه آپدیت کنید:
https://github.com/WhiteDNS/CottenDNS/releases/latest
• برای استفاده از Domain Rotation، دامنه‌های جایگزین را در ADVERTISE_DOMAINS قرار دهید
• مقدار ZONE_NS را روی Nameserverهای خود تنظیم کنید تا سرور به کوئری‌های نوع NS مانند یک DNS Server عادی پاسخ دهد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvQ3FOObrnpuCAqSp9Y8LHsgViUY_L-aJH5GWRdkql8u8EOJ387aLUdyl3CnqqNK7SLH-Kc6rOo_W-UHOHD2uZ4ZiqaUi44ETc7RbVl_ELr-msJh4SkL2abj4C-rka6VLc64eJzjf5TSJjPlOVWBIJ6xLhIMqxl0yxQJhsDi3OIYULl2w7QF9m7L2UGW0Bs4gjC_J-h0wEm_4xNxxu1P7lKVU-MOIV-UxxusylKvY00d5Xy24xfQvBWer_D95cS9cr78j5ukmuC37HACnSv94JnGUjntRPXpUzyMDz-MgIolo-SL1n9rNs1thLLMnPM0zPFKaTXcLwNS2TOr2jNuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/VSilGm9EZT8jSJR2-BhFiNxt37M3XRBT0Q7teQd2NnzuQgzCoq-Lx1Yoy50Q5pW8EzaY-w9nwWXUDEA4Ez0pXkyf1XChVwJWULylc_VZCpPqwQoArabQAmXQDzThtdVXL11y8b13M2RugyRLb2D2MuCs1M2z2hNpMS7UlWwMhoBlU7dlZLOls2D7etlPQym4K6TdFPjPzwht-xHPad_Px9YwrwjOivR0PtmYhdZLA1z33gYFUok7OLHbO9PShubTSnsuWk5NvQ7DxfrToLlvIVK_LbroGZ7Rmy8BSlTaJL_E1aPsQwASNkcy0p_Z4TWoNoC6WJFzKoUp_rVNtuW_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/efCrbqzdC9OZJd-jcEGPdQj-fpRnsf49hXkhF6ITDE-uo-ylx9-XyOztGArjW5rWifV6gqPYaUgRtqQdizNKrVq6jzVIMzcngj_Quofz-M5Mrp6XfnA3TD6B0l6Ho2uGC_0kddh2r4s3Fg65qcDV-6P5gM8lZ_Z0vBPdAVYVbI7s8vdBQ-ECLdXABgWF8S07gB8TrKfIW2ufQK-jkh_TF2M4aJCsqECIltfZvs0VPt15rOmBel9kACCoQnv-v6PXliMnbxFPGmhf2OWfoRqY0gRMb1eorhHXNE7yx2BaLRAcOTih2MRPF9Cz5B1o1VfkWsM0BbxS80s1TMzbMMu2GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ggNB306EM8ixLBFOvmUNyV06O3hFdNc7n2fxQVXUAxDetdR39XnrQiAmVuxTEqhMC8BbMzNAWR1c42CWqmlN0BpuV22s8ZmT5gaqag1MZm4Hz1ldHZyIrq1e_3r7B5d-cKQ_viOOmi8DsfHQO2RoJh0SvNr5WQYct-Kkk1ZxaFCg0XBsCcGOU5Jz_zY9UCPDvUF6RgwGx6GEh9AA-PzbTA8pXzbpl5r2v1EUZJsjYrz3E_jiNU_b1V515433CaNzLiW5jgHJeeasC5abAzZye1SCuQQpf92ti77ZHANdmWgO4qrWItcWLB3KVZpYGQ1QsG82w0yzUt9JzgVlWl8Bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KYnVkznrS0ETqgEOj208A8u2eiF5D2od5d6E-QnGgbpZtoU8s0VLooH5LXumENQpAHgrGNcOPLOe_VFyheIhYjK9Fi4XpV3ywpEuWxLUudrpIoREZkgSoNz4woqHF8SjBCYZ5BOHk9INTyzjqKp5E36zf9ECuNdr2i1exUvVLfoGR6Cgx3WYULzrVHT1bqorA3d7LeX4765GnaX98uAieJAuHIGbmnT5SyiMafnIcU5gieqVu5MY6KQFwes5CQ6y1imrbOgjk7cmQ0gJQ0gZdE4FAARypRDBB7vy1fHzXoghxA_Gas8evYXQGj5CGiPihSVSFS9PClzBZcFzeyOYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ap4bDeFimleTHFwpQHEEl8W_ZumXf326CyQLc3Yb8HadWkn1OXDnG4wKQS5WbeSQJMdHI9oMV0Q2qTAmDOD1xD5_DHFczF7GUwrV00V_ndotpaXwr4o8AONr4nWngXVGqA58OJ1xrn5xttNZ7wPsq3gZ0tV-KLSXutx49KdqQoViI_JecNky_DUwE27nnWJeFHH9HAc276SHZJoeGOopl55s5IM8YnyuB9Nc8hZT3c43bsr2mLcXrsyy36LshHOVvI6il2-BtvP3hklup1YdAWRHPVm4qKLvptcapj5DDTr7gKLM_AvjFG77wK6uz5MPJvWnxsoYP_ELLthjYzCv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ocTE2eZs_dWrU7wlGfcz6cyOIi53C0_QfJSWGiQVB7Ol4QNHgMuLgbRAW3n3G43vQATXFLeSY5YZuzNZoGsHVMgwss5-_FzblZUtwtw4e2Z59FMPOGIyGkvc31N72sytiU9pbDuza90bJeExoqRk2WZSJ1W4ZQt-sxg53brlG92kbVYJOVmvbi0-VuYlUhpKwwgxczwS1LTEuO9XBw54n2duaaafHjrnLdpbicCrm3vsdZd_YwIZZ52_rn3g0a1zPrsusAsq6Zt-Z815YSD3SZFaB0juGvYyIOKLkCgP6NxLWwR1Sl383r2A7PLlY1C2dMUOaht_kXFla0_vc-3gig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQA9y7o3YI8ra_i97NAANnaW0UyEISgMc5-KXaQVQTq9BaN279_tlcreXGWvfvG-jPF0HPIaxJHcyNz0omsFe7u2OCp0l96k6iO7ed1GWj9O_fd2Va0MMww5ee3qvXeOK3OBU1b_o-EPNHB1YltBzt1uL6yer9nMMHoIUYF0c8dsHEMfxItcKy1vOGvtoZZzXLLqYBEgfdCB6Wc8IbHhbeEtAFV1El0XYLqSJw_It3GQg6bxuZPY4Ds0UTOh7Ordm1yybZLE6-UQzL7RxOxGO4ZoTRLG2BK_mpoJNoW6_7k8yToKM-jDfAx4NzZPi3Tjrnw-Pl6cBjGN-vuRrxrTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CwLCKYEZJtE_hpYq5G46X_FMXPl32YbNY_bQMEuTW03ChwJuiVYyJmO0jcg5oBb3ol7-SKADCnSG5FfbvoOexZxBxr7DtBbyEPZ938yjbPN6sUbMStOaMpgYe7fyUMzLyxG_YNZPUwsM95JNsHjw3Dp-F59XFbXDdn2ZQshloGJ1SIkoMIvz90AWlDM71TF9a-vZT5pwNVoWrqqY5SG5EXrpuZcDrTHBp8cbWB8M5aNYZC-dOwx10CZ1yDuHIT2_6j69XJM4liNzxd6doZZBTjN-u9OjlbKlG6Kg7ZYVe36Fij0dqSPDVy5lnEaeFSQ8VYmpYWXhyD7Td6HZ7juQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsLBgVBnc7Kha0uZukYgdRj98XEIua1Rn2bLhkfMuTu6i_toYmohP6E76_YsTB9uPc2GhLJRf14keM4XMlRAXdMNaSDEDoIKLDfwvf9j2W1pmGVG-ZhwEBXV3XMtS7m1IVIB1JEGIVdXLr_DUcK9aS9f_MJbLXUQvhJ4Jmc6wOq-k5qNK_0jUvvbGVwTbuVeFoVTfuaHeAVNFDOV3N3KF37hZ7c3mYr1K78hwCga_rgmX-6c4JuMAfcLu3EyUcnmZHzfsEintRRErYwHDf2Yc-W5DkvcngxU1EgZwShtu3aBRi1VGXwmYwQ053FZ7FAVhymBSNHmrlNA96AG3SAeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt56QY0kVDXowKFWClBVeCCgn7c6nyeyMt51ssNNME2nm2ddHrRocGSnlcRGpJDcLKLHo87lqtpqTD0dFarDfG7_CNdqOP5Y9Zxat5d3Ly88Zkvy7DNHuNyUy-ViWGz_RjjFbVvIYCF5ReN2Vbdh0BaAzeP83eJmUNuUx5VVw65oW2utPt1DJx6VlLi6HP_AyMHjyWtX1r4j6a6RSfnUjGckb9cP9E6eQqUeXAiMdm1wgge0oJQ5TBVycOnHkZbIvNHvov1BXKxy6Lf0Tc8BFhfLnUwOIO7hI3Q-2Sfcu5p8fi_KlJef_dYxzhH1WMSd8nMUIUEystwn7nogLVnqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szVef4UvHtxbO21ziZf0_MRdXgfjKPbG1NroSJJpqSKEzum2IBHit5sPfwFn8e0kvKZOKE14z6VyPVxfMS7WpBXyczX4F6PRdWV0DTO4O1GOVqzs1qfmFL1eyk7t1PDhB0MK2yaIpHSkGBTH16sCXdwODfHquz5yVbulR5LmaxqprCckUPLG7vVkN53vhZovGELoKYf_RoiCKA8iaVRObm1aVuRjdXE4oDFZaA-20sZ-FOuMnNg9G3P2vAhip4XvfaVM1FzMnLzxdvHz26AfNvxokG-hE-pTP3MdBisr2e3ti8evifc2anb6JDh1IZuv4AfeKT5_2xu0Tpsj16c49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gueJVKVX4RYNEQWQ2UzpdMoU1ZB5RC3qiR1gyjijK_0lb4Yzr-gdUNBJ8IpKAt_oB8_kX1t-TIfBN847fQB26APK_WTqx7uA-RVMP9IqGzoj37ZxapAXmP2vIj5nRx_JA4KPQ3k86k0px38Z2YvJEJlSAyED_-Gw557SogJgSIkU0v1R0f3yymb8KGo-LoOgwpUIS4kRdSiDqIl4Z9fKLu_Kanp_9226e8RAXIJ-urqXWTVOegZbAMpqPJtBWWU5es5iQDNGvHEgGP7EnrMpj4CPQ1sUiEyhe8ZYV_EwvpPm-gHUxtRhskdwW8rL5TX8sZnlAYgjt1hC0pY515-6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pEoAHIikgB8hUtydImGYole77bIzMiD-kEF4jLMt2Wi831E_mYoNorl_-SFrPpu4t-QxX1d8SceSo6UCxOnFUnXYqrDP0Twwd7rgnEpoW8btx0sQtnBpczv0lAkffXn4Z_dfiGkDHL4qzqzHYKbYbS5cxKZRwMqY4TMSrMKO4FdbM8tN5ifnd3rDaGaMlUStE2N2lWkhUWY13KXKCCfs48Xt0nkwo89j7gDmCCJ5FEvz6tAo1PA2MSE7ee6bSpNfwX5HgSk2yPAkjzg9F5Oq9SZGbxaEHpC3KiPIEAI0tmoqeZy7CDu9zHVqr1Qhr3s2J_-hxUGA5PID_mQF-irbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/s5Q4bSdi4RDF84n3a_WNpaXmQZWFS_5iWw55ebj2Fkmrn5qMg-b3NDiAgch-FJ6DuOKdpEjRXJJp_CGHrhI9xM6qy9A8qBBPLzSZQSsDDzMo5raOMmirMb1MWTQTi5XLK-ntR0maGjQNkmIXxPMYmlJQObyJZtBW1n84Iqhl7zstrLKllbfHSssmOnSJ88DNISrgsfMG1qtD6M_tYsrQKpmt8D4t_833mVEynHT-qxHPtDyEeIFR_jClNwTz9KBOoPfFYQGxgmngXi5UEegIwtSAbI3CsaicI7L2KeSmV2Ho0gIei5ppVDDv0h5vHqE28ByUmlR-cMxh_vfB2iemDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aHoxPai61p-Z2c1yvbgHa0ho5ZR5iKB0G1bmUdpDdFV0wQ2ruX2Zjts40X_XjKbXj_dkgLwIvC_8FlPWlyPGV-klXDxlywNO09GI7Ez89tXV45owo0xiqrGhNxrMYhEGbTLKHH_6E2ZQS0fCFwZU8LSpO0CQiilNFVcJ9DaBfr-VVXy_USMfR3cpqdRvNsf9jSamYh49U7Q-YSg7y_anlfLiwbOu-5CsrXIUgrqyQVwOOK_g62gN0-GsXLUu8TCFzC7i9-ebS1WpTQAUXb0pAvoJPLr0CoHpCv6p1puYp5dkw8lEYkc16Ti4icg2m4ytLvc68kU1DxWjREAde1IYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TvGokqLsUFauXcA-6sTbllCrujjMNgRHoBuWzTUZDY_794JEOeqsUGZ1nImUyY9G4eDIwa1jtBRmKFriSiavmqvurqenTcXQ8UPLIA6ubz5B5WDJEHgeXE4ROTUgygI56T6CXmK9ucGaTbK6ThnUfQOWlgSpvrTX-CFJgiWqIGtY1S92tOs0S9Y7FEa3mIl-SOfsnmXY4LDGJxo2NbY7gFQ1MCx4A3LOo1fLlV0eGZD9Zqjy8EN7u4qYrFzkaDfHzxaVoIDLmb-FnfOCrjjS6I_E-XMGnTb5O47s0YqM42VXZHrjkBH6nPFcqfG0lXmZuV6IKPgHXFoPCSNffZINOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFOYhbGM5oQYB9naZ3tO4SBoAA9o-83eKVHHvwjmUkd5RGH4JIN1haOeMc6oWJ2BEtJOMQdh8BWH-2lyoZBzofAPVgQnVCq2Ts34vLboMZC-cM4XTQ60x1KvCr52-RLm3ieo_m2UTZpgn2lxfwGBiJqZ2zg3eTW6c2zSvpllnayU5mm9UldJkYZo0G1h9yUPBIGlFi51Ot5rVY4QRTXG55WLm5pe4oVJLm2mVgObX6mU3RItEJPJfS0k8mvV9dVq_GQxNKVrXbg2ct9JlrTuZFpooBMO9RerWYoW_D_tQkGtGjhe7iqllqaK5xNkIP0qJMR81rJPBdxc5TqUESeGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BQJJ4NHaY5aA-WO2m9-MhzxOvAOlweq6q3lmyKvqYrysXi_8ZAE-CgyBe0tL1PFBuSG6NEEPo8WTpH4ZSUPDJnzE0IEQWYA65lII0i9bHk0LfHWwXA8_yzcw_XzUdx9qcH82C6tFzUvIC-KIzJyee6JOOked0620DDs7jEyhvH_Gx9w6bf3ml9kiKaCsUV3hvk1YZKer5sEBYIaXQ0lqPdEnAR8xA4_bFyD0w9PxMKVsM6pvE22XTVvSrCORRx6_1Y1RFivAfo6gkCNTqTC5jcqOYVnce5pYWhXOuEGuEF7zEPA7WXj3XqwWPEDsvzx6OQmpc-BSI06gMx9KvM24gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/nGusV_CqdYfR3MiLzpFa4ttkuxa9qAjjY-B5uiyjVTec_yKG-2fDh6eU-SWKHxeJ1K5VA-baBcatSGEGpb4SBmrcOaIhD-L0z0VbnGMPzKNlrCoOHsfmi91F38eM5iCf0waA9_cg5O69GhvcwaitSPWv-l3Fj4ooweJBF-3NhnmwWbficeMHvQM_Y4ov_2BEt8aVKZfPguZNxnkwlNv-v7nCds2kZSq_Ia8emGlJOrOtCbA_VrJNYGUOihwSNv509ZSZlDO0XjICM8S5DnFk9oqRTkLzE4VWU9ANJENGbtzUG3bRVioxTUFXHz3Uuo6vvLa0Gauc4vrxgCmhp_m0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/GOFOkF0pVf0s5_SUBVbGpwXqtJjl3Yobs_n_QLQb9HHDEG_Q1wamTWv36M6UXTxbc1M-J1R5Z_J5AKdhc6E6yks-EWPwuHxflCuMl2GBCFUUAESM6dpKRjLMqTnXc2WjKee8yCLRSjG3n4mQvLaI_aX9GIXvmtHSA7r6ilUh4dKZhDaJOiLZZcm-ktyLcaU4KFM0dVbKyvWaNONISpcc9Ph4xKedSIMzxNZMfJOBQr0GssUgYB9prkYwIMiRJaThLzLuPFFqEGbgwHbyLtdSAdKSoGQSXptvKtgAIsHi5xvp-2VVNpZMQKBh8DELMtsVIR8syK41LOzRTYBCXL-qww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dvldEZJbYGfms6kIk4GNenKVS69tAiI1gJBHak6wVNNxiv_EVEM7H0YMMGacIBwNql9R9dxqWzrkv9sWDvJUZ3pV6KRSagpLpU62fuuS8uIS7ovXzQPToGCaDmBBQD3k8nEzC1sCZdKJD5IJTu90VrsjW_gCMW4oE94yl39XkkV4AS7D6X-V2rsfRvGd1nwcCNkhhj4yGn0oe-Ktt1AVHY1r5L8C9iWwn5uCgbad4xpBOLjrqfHlNkC4GbiXhUC8bqgJTytX9uEQ74533avNqYlNIpUs36Rf2py_5UvY3eDx0-9UAGDlOWWQ-n-uAAm_ny7CwBR5xcvZHCllDXsobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mP0AqrNxLRMUvRZfVOHASyeEyw7BPH8qoEPXMEQwfwjPMGyC9mS6X-1nKuNCr0FAbDLTHRMEZG88e7eocbV4TnDvU-a0u4D6DpEUc4ZBEHvpz9EcIcnZICk42hWuXf8VKp3-NLIhUHFeX0SvDU68H45QGq6HtxkF0mOy3goqf4iXCSM663nAHijhFVbhNuFeqZehKL-gtHs76YcylpXtC4vJg8unyc-gOAE-MFpvSMDjOxAtNgNyR2u5uIqHA2Isn3W756IQVuXJfQGXoI0JJ3Gsno5XkeMPCo6zXqMhmWmfTpjXPcZ_lZhPt3UGZe077J7M-wOGBicHDxk0tmRrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lv1LDmYt72_OcxQKP-a93ollICZe283YiLuKSwDl3FxjWhm6VFfFzcntNAY2ST0bPD3KhG4tDDiME_SrlAfWQyTTt64RC3okDc9DgBHvhG1zTdiVSbei6gAaxrreHslzet4QsMyYkvb8bZSOqcTPnaYtg-x9y9c7AzMLPhgaqGIulsx4wdoDOoB4BAVrpAKNLbQZzJwOUuydEjFRFbBEUc_fObDY3o_Qxqc_XfGhwqBxivH2WuIOZH1JECxu6tSSwPHic-D2a_WHQ30jeSlHcDWqazJQkz8Z8uSMO5mpe0TEjFcT5ThsSaJaS-X4NMqL-JK3vFagtXxKX_n2yjch9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgsWEinfEsFHaJVIvX_D9R9W7QtwPqOynkD_n9bU7sSlTIezBAiAOYvqyG3vkugn5bBOzBoY_e6VUJCQYb5i-20iy8UFTJIu8wsvonXeDdhiqthuFTZAG2LaWYTJEHvcZWnj4IEKcH2aPj4AUvWw7wIWnu2ROOTdF3DA82h0rw-IqGjDr5jlOfzsdXTdTQm6Z5YYLFBGJh83l39GHb17PYr_OMGgincMMAGy2EAT5wq7AeVx3ArUBHvhKVsw7m6QDbelHoxPQZa-bWYQoDxY73BA4MCPyeBZ864a7uPbu6qUp_p1Chz9tnIKYo7sw_gNMMa8Srvss5ARqbhALpco6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aGClMiMPmEbs4naUM0USBCWK-oMWomIauQn1YxMrn0zPbVcK7iWq6H-vq1t4bq1ZewVMzHJCMVV6eN0wvQOMckUvXCaFcHcX4MtPanF7uNjEf_JfOEAFvy4hCnNynLm2kOxgNus6tfhbUEmivaY8V-oA_9EnkV5np3zOCAsYRKagYsJDjSd_hOInn-QhEQVwnrMLfP2GGxSyuUei4QxKESEYnPwygQ3O13ShISrUWAfhp2q4iP1fQcU9AYKuQZSqyzIwLBGdtifdCqI5mI20dmtX4d6NZAsfsus21QYDxRyLrFSfU0ZQNInuxKB4gcSXaF0sZxiZW-YSnd9HlIoUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EGc4TdR-6RCEAPNhClrjSVQc3oukX24BIA-95rRJi6uTn03VVSfN9ja801JsNIGuLRxwaFw9d92ZGDSlTQuyidvdf477A1eAB3VDmyisqyU3hGcrOrzTUayqRvg85TOT1TB_BjRhljNU4mV3yKYy-cTHsdMr0j4dTTL--m2Bxcv1dgKsxPM41zWIF0kKvjb1qsaEvRBccYG1TcQNrs3VE06YTutB1pb9q_-ryZ3A19SUqVMmu9umrn1yEAJSsdFPihOqbg7ORuW29egxea9W22GGLtWXxxKjTgAzbX3sXc56NXiN2x91E9lVde6BuzNMtXrKYGkjKf7kDjjIzTGiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5xBR5SaobJMHJOKbEtp-SUIe3yJ5yaNA4iNSNGHamwbteV8ywtFh_ytHMbniahTucQh93JFH2tFwXHvagaJJihd7l27vqOaa09uSOCrU7gypnqgIe3pKBnG_Q2ztVjYzMrs9z-_RM6kTs8P405NkT79cnZm-N3RXtwf36SBNRdla0MScwdMKy2QjibWliTtnijTRTT33D_nOeVmQzogN83gVGYNorygOFXs7BMRaAwwAlwOPNuu_5smZY_JwP2aiCKRLqlDBBRSvJxPIp6Q4qIlKpm7mnP9MwAXa1cbgY30ri49TQ9_CC8FvsvOrLP_l9UOnCdw9ICW7ITvks7Xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kklHWDUAwSGcV_mpFEQiNT69BlCsqdqWA4VlotQjlsPc9DwwPUf1iatS5-GnHtvof_AwEzKnatBCvhsHkFUZVfUs8XmPFreyF7QPi0a27iU6NYzwgh_9lQocjaN9NBzV9bqYrTpt_HIU-PjsI6JX1mpjoh_IaQIE2ePn7TYt_EJGyvp8y3cvC5uEfVH9mFyt52IKbpb-wHern2qWjYXQ-7k7-BhaKUy_F5zDuM0r75ellQtZUtcTw-nKTq_hCdxEkAkFXOm2V7HSKUuSh_1-290-1nY1jt180ThLLdJ-6wok8evzCfrXlEWiOZNh7r9w9kAK7NJOTr2xrWoyftk7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FGl1BgMYp69pV-snc9Wj0WoSdwEVSGvDgwjh1A-b4X4ZbMbaV5wYocyzRxndk7p_1QHAO_i6cFkYAIOYPpMxNw4f55VQG0Qlfm7f78tsp7dhR7wlvx-eHNB5Hu3eemF4S7CaDt30YPdBiaZBKQ2f3ROQKQUpllmv0tFC7CX8-shrKK9a4xgMcNhl9p1wyF6kzvErYNEziLzJ-J_SXKp_b66Fr-tw1djIoJuLX-e1pSwnhGhnGC_t-OoREx3tQmFqIxZRmGm6eCmB4b0hlLEEDBQvXtVshF6OEfEJx9cH4Q5EpXKjZ_-IQEoZKB0PSEo_EDA_1TootvhKf88KRpZO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aM5J_GUvHGmiPM0S8UBw8joVCCAEo5xEdstuI9ofsvAO6Pbl1wy8MTEf74nCK2zQQ0MKG4k0iSmAalqMU6dE9bLOSF-xO1Erc1X_4jM1nD2k9c-JLIZP_LOzFOdr4us49hvbtTry8jz9bwApRhT0t1tijy6A2ywxDsq5CdMaD3unMXvtxgi4VAjsX-ArUvBXwayufRgIqCVUF23ag3iWagSGg56xN9zqXQZqEMCp7NiiWAmQNqCg8wCinqQBrtoRbFtHeUXtqdbM7aSRILxSVUrBejrKAn7zGp53UOgD9bsq4Fw1EtTIu0Kxu8H7vqNeHglt3klf1y9S_kSb6uac0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SWRqqxuhbJzTCh4vpOyPPARBYCrIfsP2ci0ebbxxqzZ53as2th2jb9O6Gboh-8w0DLzeXEqVQ4BHc-PwbB6fqZSkU_BEvtZBU215CfQ65pGJ4Y3DjnsTNaU33vF_KApI8xA1HIPppIUred0vxzdXWWl7BNAXfxnX1sJaAPTpwwJV7PNPYjnW6rXvn_SK6RqN-unsD7bI67Ii2KyZQqMniNSpq8AsLCZqTg4Zg1MKN0jHR5dU1afi5bxnXIlLoxy0g1P0IQVLzij62T07yjC6aYGTWQ9VdCoderX50_fQkAh_cIRMKmOxyreHR4Wcq7UU6daBzobh8WVNlc4Wrq0EMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeJdRf_LmCGzrBybEwKRGK_jFTka5r53e1VJMMwb3Jpx2Rmu0i1t3JtvOhTJ_uVEYp-3zt4lEAliXrrVRqWRV1C88YveJCkQtQQCbGM-BW2xERTZIJzcO5Er8-6AQiQLNM9WoSC7Bvtk31SOKE6F1Pnfgqd7dyLi-S0v4GIz8kaANWrl1fCuqexDLGw9szZVfQNR5UGwkWppCkUDsEhaUqlCX68d7ze0OaPUnrCiZSDmko4HsC0-5XKuXKqeLZlL4qsJhZfBmFYeCmEE1mC9mIUmxLNvSc-tb8ZSODXheTR4alqxDFlGD7UKT08WKza8CrHy9nf85R0r4IpC8tWyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YROmkTec5k-_9DoCzTpt1EocDIQLq632OiFusjKSj11lrt0MzyiRBgmbrg8k1kzKLV7rsS8XTahYZFy2sfv_iqpEEYAJLGbvnjIgVQeMqtumK58dh7lfqLm2igoAH8eMW8ULuEDeJpkMdTy5yOV9-G7XLOUY5zH--NEA6fxcGkJikHK7Wip0gGqT1ubFm9SRfU03Mq_9uvqHEqI5iGMe9u8uQQ8b-AJ12USzzhehxAkF62ry1mrpNRjHTKyOZFKhxSzcsuoQdbwQzr37CI_nSq10Ma_uiG0xefBUhifijSh9LgtPWOxEMY6AOd6uoB2uVbabWBialW1v4R__hPfvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C3AXiNMszsoc9-9d2R1CcPK-u7Cb89K3JAEPLQcjieKquADjNkfoMt8LvudFrqKhNFmUmCCJ4EqwEubWppQCAF8R-mo5_O6KeEB4JcK4xoBaUldVe--f24fmEEI-vg6EeQ8-swN81u9Fc_nx16LRTEFLfmrKtFDlOsHiNriVOd5qpEfEjXlmFRHmZQfGqTzO6c_Cbs6_02Z-4CAPJi80FslHTDGG__K0b_OGXnieGpwq_wAPBwEJGyQv0C7vgznK25Muo2LMqWDpVjX5BaMUMCn7YW3OD4YoRaIe4DDJ5qh6M8YXnXgQuo6539SrEptnCfN7x7XqDELgr8d2WiLT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Q8SwGpSmAqw20ZHHU1JvTnj9DKrq0gBZO19J09kILkcfYvGjuzxP5l_Hgt53nG0FaEKg8vgTTcxilb9epBDEeuu-GJBXZEesLdzamRNtZJVMmuuxeem24aPhhL1awcnDMxHqKGKAH3VwnALtvYc_gQ7e7Idb8UEKfBkcGi22QIpmL1HfOCnr-GcO47WEEbVGKIyXyfA0ymU5v5WTGiA_kULdGAl8gZug6_aSO6SZDmVn8wGpVBQJQUqV-4pLv4ofmlXI24so8mfiM-TxNsX4Sd6rodxq67hnKa29dqF87enAAl6WKGIPaQQfwUWbD4Rh1aF8ohoHNUo3q41q1kRqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cF9oJrazqWCCt_BOR2LfrCN7J6170etF4X__d-LJq_TmXnsT4FI1vMDj5Cst7WfBZkv1rpFvFyxazHiCPrKP4veA7GXO479GTA-2CouD-U-kqTsKdmnFVZzPHq2n8rzd7iXzYyiv9M93Z8w5zjX0kOyMr6LwgfhOXxx1oRqhYCK5tNhjlkAiN5Fqt78G88js2t9Xe4XT67j3FXVgpNzU0S5eBuncqH8pGgMMlSX5IbJqNAtF7gKHbNYNUeDneq-HVqEMFCDgvqt3oN1s9M_ZF6mLTAirhfyFyDZ3DMB5Wesyap1HfChA8Bd44SRmywdNlC_ZsRbhAPy6Qz4fzFPIOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YC-fP1ndq0gxeZyEOKT2W_2ufeaQRS-Y0Z637WjKZMMIKo9GfBs4tNcqevMD4y0_naqU7hwR94UFoO4knwCD5xcnbzSYsfVo-cDxJhSnQDFhyVtwEUymmFGCdIn7Ho2mRNaQcxJr-Apl6B4BkGAUy2SVyWz8_F-RP77oweyevkTjG4GObktbNwaoNFVzVUKnNbKQupX4XvgjR37WvG4ocC676hvAsM4EDXftGruslHQbHP5xFsuZQQUc5Kr8tp8YOahYWfhJDDG_lqKbL4MZoSYwMBTs-4weKaJ3eQ0COSmiC16kpYd2ChqPf1huqhG1YIhdia3fEukpcoZXuOR8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vxomHXAJbRTf6qcraoAbSX0jIeT7f2HtWxUbEn6PDJTi43k5vZfn-ftQS1rjhTPvgNFSqa7R2pQOuxlRxH3kq_bwOjO0CdSQ5l4ykND_j-iGhQalsW_JWdpcpdJCahPTdBfJZYjsIWEqUJ4ujA2wE_zQ-knE4lAuuEY02N1i4oUg4Lig1kukMMSqAohidCHQz-oT6I-Vm5aKzPuTjxm2Xpidkn9plxILlKBvGJVRRXyfxFG-tvjtPopzLjwxrgRF3OrYg8oGwkAbfm6e8f2bTPJ--zaiW0CHbkX4rMycsrYHFwYQnax-bocbhpL1UTBbaCGxzNLLOPr3-Ky2jAxrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XIQQb-7yDqUIGx5B15AhI7sMMDR6O4g4LUDokLrAhPBxyjGNNoujBn_bqt1-dke1nIpaTph39D_0v2uyNDF1ui5spfo2cAeTHO21s2ndizE4kLb4rALWwv5qJCYzaNS0P7tS4VoZKKP2ofwO8F322AKJKYnVXJkk9rxI9Siq2C6gUTQ_u0ZonBWwqq26nfRXGSnGriAvcQ3sR9lYpWIP1_Jyqf88bySiZbEovUvRPyff0QGccOp9ic4xLakTtuba5KrcefWeaJ1pTjkT9PdHjJ55GFsO_pfWNtuDKT5VlFtiQKoeKNsIpdyruxMjWht0pXi2IOoM1yxyuAFdXHuLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LrGK2bDZHJPyAf0f-JFpZ6L6Sa7jsIresXgK4iN5GzmoKrorQAfbCvIwijuDnsHizNJnvijMA7OhkPZ1x_mmayLpBkTB5-Nnem1YpzMxswliLqosLU2v0ccCr7Z_d2iXwl5nr802TRV7eNOX2SbDEOR0PN0WKuy3h3iG1jOeEpYqllIp7luFPwouSyR7S8ydC-YBqSsbhUw20hsp0VFraIfjggg-eGTXiQ0bhgTqe3v3kn5hUsSpqPL8w39JT9RcwXlJ8nxN5iSkob6NNt3thWXrSAJkL7JWSNdhAJpFFXikdl6KROYs_01TNKprLxYXvbkJgZtxj4M_Bnfak3WQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NX8cY4YrPwHmWq3aLoC02LJlRheDpRWSadkXhFBEHfLtrwItTdQKhPJtG67L2FjSdRCu7S145EOs_CSFVIR2TkBwfDCtZRqL1x_9opY-vDQCJKU_13B4Rp11FFiV2VLauqBct5eQIY7RFPDmh2dmGvimbewSiT5hbVbnzYKwR5gv6cKQLMDwzybKjL-g0Ae5ol37_-PBtXURQmytr6oO4Q-1Ii060lEqAhEnolQrpIhcwxfHN8PdIN4gQKTfnEX6sCo7gfabNag8BImeuu-9OMdQR9lJCJcc5rowrFgnTC3-vM2jqL0IXLbxtAuJqDHxP77iB9IGuHJ58iL0S2IvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

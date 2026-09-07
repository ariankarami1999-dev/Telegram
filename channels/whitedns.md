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
<img src="https://cdn4.telesco.pe/file/rS6RCEFuW1PXZWmyxL9LH4hksFuaqOEuDnCepdXgfMWm9oz3hmJLMzANIv_2zc1rPhXKBzaHdgikO5rClYjZvSxa6qEjavuy6H7cW8_rO4iHZZKaI2amn_SzCn6ktmwEwIdn2s_vN7sbDuv6Ttv5afB_MFRq8Y6IEF_2U3m7HlJdCo83ORjf-iIhrc_e9MkGFrgf68Wwtn-ERGNZ1-rlOgBZlN4v4hVkK8yE3mo_L8d34EG6S_2RGpY1TdM2CMOcYvDTCKs4-aThPObG5EEexm66nVyh9zr00A5R7x8GJQ_6qkL3x1X3CZ2noPTmgKSEyWwlULSLsF5p5gQoDSNaCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 08:58:46</div>
<hr>

<div class="tg-post" id="msg-1737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ65G1L654TaUSfHIjaInvT2Wir7lvnlKv3NKP6Lg-h-_2LwWqiF0Az0bnAOf_A2BPFmgWojhLS3G8vhezwRAw7p5hxy0W1-XAntkxEQo71ZHRlsaIyAGpLwU6O9Bo3fflQ5ud1YxXMLNhVxJOLwxkMHlPrEz1EzzTjykZLhTuHDaofJliF6LJ6kpRrJpD-MjAEf2iu16O7HO1can5MIJfVrr6wlqkaM35Ac3_sMkNoqTJjV6gdacAyK1197RjB4Sb4V1tnMNBtnrnxZ79OL28bNYIfpr5m59IipkHHdqK1UCCQ5PsPvT14Lu6j3yQGg0CiqmL3TvKZgthkRmxvJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
دانلود ابزارهای WhiteDNS
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
━━━━━━━━━━━━━━━━━━
🤖
ربات‌های WhiteDNS
💬
چت‌بات WhiteDNS | نسخه ۴
🆕
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
━━━━━━━━━━━━━━━━━━
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVPN
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/whitedns/1737" target="_blank">📅 08:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از دیروز تا حالا تعداد اتصال‌ها چند برابر شده؛ از کامنت‌هاتون هم معلومه که این تغییر رو حس کردید
🙌
جالبه بدونید ما با فقط ۱۰ تا سرور و ماهی ۱۵۰ دلار هزینه، داریم هر هفته به حدود ۵۰ هزار کاربر فعال داخل اپ WhiteVPN، رایگان سرویس می‌دیم!
این تازه بدون حساب کردن کاربرهای ویندوزه؛ با اون‌ها، آمار خیلی بیشتر هم می‌شه.
😑
آدم این عددها رو که می‌بینه، بیشتر حرص پول‌هایی رو می‌خوره که تا امروز به فیلترشکن‌فروش‌ها داده
واقعاً ممنون از انرژی مثبتی که بهمون می‌دین و وقتی که می‌ذارید تا تجربه‌هاتون رو زیر پست‌ها بنویسید. همین بازخوردها کمک می‌کنه بفهمیم کجا خوب پیش رفتیم و کجا هنوز باید بهتر بشیم.
به‌زودی WhiteVPN Desktop رو هم با سرورهای اختصاصی آپدیت می‌کنیم تا کاربرهای دسکتاپ هم از این اتصال‌ها استفاده کنن.
🎮
یه سورپرایز هم برای کاربرهای WhiteAesther و بچه‌هایی داریم که دنبال سرویس مخصوص گیمینگ بودن
ممنون که کنارمونید
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/whitedns/1736" target="_blank">📅 06:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ما سعی میکنیم هر ۲
یا
۳ روز سرور هارو عوض کنیم تا تا جای ممکن از فیلتر شدن آی‌پی ها جلوگیری کنیم
.
همچنین کشور های دیگه رو هم اضافه میکنیم تا آپشن های بیشتری داشته باشید
❤️
🛡
سرور های اختصاصی رایگان، امن و مدیریت شده توسط
تیم ما هستن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1735" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید. امیدوارم همه بتونید به سرور های اختصاصی وصل بشید.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1734" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">36.1 MB</div>
</div>
<a href="https://t.me/whitedns/1729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1729" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOeKuHRpql27oXoWtFXEZWlixjVJtzmK-hWJ9I-2cotKZsaSSvAamZ0-DIFYMloUH_4DRogspakzNbC3GghwfKuAqlb5H98uffMWeqFhFg9StWD3nJD2B1uACVGDqAccIIRt8nFs9UB9nT4o3H6jFme4gPxl8sZaqkneei4a3XIVwfAsSadwTU5ogavYjhF2nv_9F0vyx1lTt6S4eMt-ns7cKBAyssYhdsDUCsW2vk9K1oHPW8E1Xda-MEZd0urQD8U6guN11nZGm8gcqyAHg821mh9aaGio01vLaXeCjQGwvPv7mwnEiCe8UWTZi5tTNc_gLN0R8hAwaVQqFj3Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
🟢
توی این نسخه ما ۱۰سرور اختصاصی WhiteVPN گذاشتیم. همه داخل فنلاند هستند.  بعد از تست کردن سرور کشور های دیگه رو هم اضافه میکنیم.
در صورت فیلتر شدن سرویس ها، سرور هارو جایگزین میکنیم.
🟢
توی این ورژن، اپ اول سعی میکنه به سرور های اختصاصی WhiteVPN وصل بشه، در صورتی که امکان‌پذیر نبود بعد سرور های عمومی رو امتحان میکنیم.
📱
دانلود آخرین نسخه از گیتهاب
✍️
دوستانی که ورژنی که دقیقه هایی پیش فرستادیم رو گرفتن، دوباره دانلود و نصب کنید.
❤️
نتیجه اتصال رو برای ما بفرستید.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/whitedns/1728" target="_blank">📅 14:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✍️
یه زودی یک آپدیت جدید داریم برای WhiteVPN روی اندروید.
توی این ورژن سرور های اختصاصی WhiteVPN رو اضافه کردیم. برای شروع ۱۰تا سرور اختصاصی فنلاند به صورت آزمایشی اضافه کردیم.
اگر بازخورد ها خوب بود، سرور های کشور های مختلف رو اضافه میکنیم.
توی این ورژن جدید، اپ اپل سعی میکنه به سرور های اختصاصی ما وصل بشه، بعد میره روی سرور های عمومی.
خیلی زود برای دستکتاپ هم آماده میشه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/whitedns/1725" target="_blank">📅 13:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
نسخه جدید WhiteDNS Clean IP Finder منتشر شد — v1.4.3
این آپدیت، قابلیت‌های جدید و اصلاحات مهم نسخه‌های v1.4.1 تا v1.4.3 را یک‌جا ارائه می‌دهد.
✨
مهم‌ترین تغییرات:
⚡️
اضافه شدن حالت اسکن سریع
Fast Scan Mode
🌐
اضافه شدن انتخابگر شبکه‌های Edge
Edge Network Picker
☁️
پشتیبانی از سرویس‌های مختلف از جمله:
Cloudflare • Cloudflare Pages • Vercel • Render • Railway •
Fly.io
• Netlify • Koyeb • Glitch
🎯
اسکن هوشمند بر اساس دامنه‌های اختصاصی هر پلتفرم، برای پیدا کردن IPهای واقعاً قابل استفاده
🔐
افزایش دقت در اسکن‌های Scoped با بررسی معتبرتر Certificate و پاسخ دامنه
🌍
اصلاح تشخیص روی Port 80 و جلوگیری از نتیجه‌های اشتباه مبتنی بر CDN Header
🚂
بازگشت دامنه
railway.app
به دامنه‌های شناسایی Railway
🛠
بهبود منطق اسکن، افزایش دقت نتایج و رفع چندین باگ
📱
💻
نسخه‌های منتشرشده برای:
Android • Windows • Linux • macOS • Termux
اگر هنوز از نسخه‌های قبلی استفاده می‌کنید، پیشنهاد می‌شود مستقیماً به v1.4.3 بروید.
🔗
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.4.3
@whitedns</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1724" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب
https://youtu.be/h920xIQCMP4?si=gjpsrzgky62iOy25
@whitedns</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1723" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">موقت :
دوستان گرامی ، اون کانفیگ هایی که ما توی ربات
@WhiteDnsChainbot
می‌دیم خدمت شما برای
"exit chain
" هست ,
توی v2ray و بقیه آپ ها میزنید و بعد پیام میدید چرا کار نمیکنه ؟ خوب معلومه نباید کار کنه
روزی ۱۰۰ - ۲۰۰ پیام اینجوری داریم میگیریم ،و نمیشه هی تکرار کرد ، خواهش میکنم قبل از استفاده از هر چیزی مطالب کانال را مطالعه کنید ،
پست زیر را بخونید خواهشاً ،
https://t.me/whitedns/1608
اگر موردی هست که سوال دارید و جوابتون را پیدا نکردید  از ربات پاسخگو بپرسید
@WhiteDnsResponder_bot
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1721" target="_blank">📅 13:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">📦
WhiteDNS Tools — Downloads
━━━━━━━━━━━━━━━━━━
📱
WhiteAesther
• Mobile:
https://github.com/WhiteDNS/WhiteAestherMobile/releases
• Desktop:
https://github.com/WhiteDNS/WhiteAesther/releases
━━━━━━━━━━━━━━━━━━
🛡
WhiteVPN
• Mobile:
https://github.com/WhiteDNS/WhiteVPN/releases
• Desktop:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases
━━━━━━━━━━━━━━━━━━
🌐
WhiteDNS — مناسب دوران قطعی
• Android:
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
• Desktop:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases
━━━━━━━━━━━━━━━━━━
🔎
WhiteDNS Clean IP + Resolver Finder
• Desktop & Mobile:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
━━━━━━━━━━━━━━━━━━
🍎
CoreForge VPN + DNS — iOS
• TestFlight:
https://testflight.apple.com/join/DRkT6zny
━━━━━━━━━━━━━━━━━━
🎓
آموزش‌ها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVPN
https://youtu.be/yx-jFqv9pYM
🛡
آموزش کامل WhiteVPN
https://www.youtube.com/watch?v=tm0ls3r4ppw
📱
آموزش کامل WhiteAesther
https://www.youtube.com/watch?v=cRfqxbDY1Dg&t=1s
🌐
آموزش کامل WhiteDNS
https://www.youtube.com/watch?v=tz8cj7HzHVI
🍎
آموزش کامل CoreForge
https://www.youtube.com/watch?v=filwdiPKN90
🔎
آموزش کامل اسکنر WhiteDNS
https://www.youtube.com/watch?v=N5hKuWXp37w
━━━━━━━━━━━━━━━━━━
@whitedns
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1718" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E6z1Lbr_RD8ggMfY61nen0hONmcG9lg1PNK5mzEG2_OzR3r_eObNZbxlRZ8UO6VFnAmJn0A257QSd1XD_jlsBfuzWunYKvXGnhD6_EEDvW7t2u_Izn-v8s-kIjK79bdxpsqh1kj3Ck5xlGUF6ObNsKMUsfqQGXPEQTfp2kmRtCV32jL83jolXEXdIdlAb66PjGKyc4qCvZIihudZl_U-BQArcansW9D0139v7Ijta-9scIOI6MN9-BGp3ho_QsRepAyse8zsOvSMJ963x0pBNdvJeCA0tLx3sDoeBP1iX1T_D0Y2zQWHsbWuqDgVBmGE4pjzjfkSAZFM3gM3eflMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/whitedns/1712" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/obuU_z9rVaXnR7wr4zpjqulZau5LWxUAA3ii49uyRAcQbgoOLTGcLOF9Bp9gg9t9Chw4UOsC1kdFGpfSLB2mr4GbntJcL9J0dQgq03T5bmaceDsGrv1symPELhTd9P7LhClTo064skATf6zhn3IJXk6UA9LXWl-L6mXGuCxxuenZALOME4cHgcy7apLYFpt4bXpKmfyXFYxUx5bBE1dfQ3lECi9fKh8hKAVeGIoFSqqR0SSyZwQ01gFsAkfRAtuiQ3443aD6OPEpc9_bZD2w14ewI9fCURxHQcP0IAspIFjpaFAXl8N4eh4VrLYRfUMeJrowcNBRzjmyANbgawKpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1711" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">WhiteAesthe Desktop 1.7.1 — حالا کامل فارسی منتشر شد
🔥
🔥
از این نسخه، تمام برنامه فارسی است. نه فقط صفحهٔ اول — تمام تنظیمات پیشرفته، زنجیرهٔ خروج، جستجوگر دروازه و پیام‌های وضعیت.
اگر انگلیسی بلد نیستید، دیگر لازم نیست حدس بزنید کدام کلید چه کار می‌کند.
━━━━━━━━━━━━━━━━━━
🔤
چطور فارسی کنم؟
هیچ کاری لازم نیست.
اگر ویندوز یا سیستم شما فارسی است، برنامه خودش بالا می‌آید فارسی.
اگر می‌خواهید دستی عوض کنید: بالا سمت راست پنجره، کنار آیکون تنظیمات، دکمهٔ فا را بزنید. برای برگشت به انگلیسی همان‌جا EN را بزنید.
انتخاب شما ذخیره می‌شود و دفعهٔ بعد هم همان می‌ماند.
━━━━━━━━━━━━━━━━━━
📐
کل چیدمان راست‌به‌چپ شد
فقط کلمه‌ها ترجمه نشدند — منوی کناری، ردیف‌های تنظیمات، دکمه‌ها و نوارها همه به سمت راست منتقل شدند، همان‌طور که یک فارسی‌زبان انتظار دارد.
سه نکته که عمداً برعکس نشدند:
• نمودار تأخیر — زمان همیشه از چپ به راست می‌رود، هر زبانی که باشد. اگر آینه‌اش می‌کردیم، «اکنون» سر قدیمی‌ترین نقطه می‌افتاد. • اعداد لاتین ماندند — آی‌پی، پورت و میلی‌ثانیه با ارقام فارسی خواناتر نمی‌شوند، بدتر می‌شوند. ارقام فارسی فقط داخل متن‌ها استفاده شده‌اند. • اسم‌های فنی — MASQUE، WireGuard، DNS، TLS و مثل این‌ها دست‌نخورده ماندند. ترجمه‌شان فقط گیج‌کننده بود.
━━━━━━━━━━━━━━━━━━
🔍
جستجوی تنظیمات، هر دو زبان
Ctrl + K را بزنید و تایپ کنید.
فارسی تایپ کنید یا انگلیسی — هر دو کار می‌کند. اگر اسم انگلیسی یک تنظیم را از قبل بلدید یا در یک پست انجمن دیده‌اید، لازم نیست معادل فارسی‌اش را حدس بزنید.
مثال: هم «مسیرها» جواب می‌دهد، هم routes. هم «تونل کامل»، هم full tunnel.
━━━━━━━━━━━━━━━━━━
⚙️
موتور به Aether 1.8.0 ارتقا پیدا کرد
چهار مورد که مستقیماً به کار شما می‌آید:
۱. پروکسی بالادستی با یوزر و پسورد — اگر در تنظیمات «اتصال از طریق یک پروکسی محلی» را با نام کاربری و رمز پر کرده بودید، موتور در نسخهٔ قبل رمز را اصلاً نمی‌فرستاد. درست شد.
۲. تونل WireGuard بعد از یک خطای داخلی بالا نمی‌آمد و تا ری‌استارت کامل برنامه برنمی‌گشت. چون پیش‌فرض ما WireGuard است، این را احتمالاً دیده‌اید.
۳. حالت WARP in WARP کرش می‌کرد و بعدش دیگر وصل نمی‌شد.
۴. یک آسیب‌پذیری امنیتی شناخته‌شده در یکی از کتابخانه‌های رمزنگاری حذف شد.
━━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
ویندوز · لینوکس (deb / rpm / AppImage) · مک (اینتل و اپل سیلیکون)
از این نسخه به بعد، وقتی آپدیت جدید بیاید خود برنامه بالای صفحه به شما خبر می‌دهد.
━━━━━━━━━━━━━━━━━━
💬
اگر ترجمه‌ای به نظرتان نامفهوم یا اشتباه است، همین‌جا بگویید — عوضش می‌کنیم.
@whitedns</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1710" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎉
نسخهٔ ۱٫۳٫۰ WhiteAesther android منتشر شد —
برنامه فارسی شد
بزرگ‌ترین تغییر از زمان انتشار .
🔥
رابط کاربری کامل فارسی
همهٔ برنامه، حدود ۴۵۰ عبارت — از صفحهٔ اول تا تنظیمات پیشرفته، اعلان‌ها، و کلید تنظیمات سریع.
زبان را خودتان انتخاب می‌کنید، نه گوشی. در تنظیمات ← زبان سه گزینه هست: سیستم، English، فارسی.
چرا مستقل از گوشی؟ چون این دو برای خیلی‌ها یکی نیست: گوشی‌ای که انگلیسی مانده چون همه‌جا همین‌طور فروخته می‌شود، ولی صاحبش فارسی می‌خواند — و برعکس، کسی که گوشی‌اش فارسی است ولی اصطلاحات انگلیسی را ترجیح می‌دهد.
🔤
فونت وزیر
متن فارسی با فونت وزیرمتن نمایش داده می‌شود، با فاصلهٔ سطر تنظیم‌شده برای خط فارسی.
فونت داخل خود برنامه است، نه اینکه هنگام اجرا از اینترنت گرفته شود. برنامه‌ای که کارش نفرستادن ردپا از شماست، نباید برای یک فونت درخواستی بفرستد که نام دستگاه شما را ببرد.
🔢
عددها
در متن، عدد فارسی. در مقادیر فنی — آدرس IP، پورت، سرعت، مدت اتصال — عدد لاتین.
آدرسی با رقم فارسی نه خوانا است و نه قابل کپی.
🐞
دو کرش وارپ‌در‌وارپ رفع شد
▫️
موقع قطع شدن: برنامه هنگام پایان نشست ناگهان بسته می‌شد.
▫️
موقع وصل شدن: همان موردی که در ۱٫۲٫۷ رفع شد و اینجا هم هست.
⚙️
هستهٔ Aether به ۱٫۸٫۰ رفت
کتابخانه‌های رمزنگاری به‌روز شدند و خواندن هدر پروکسی سریع‌تر شد.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
💬
اگر ترجمه‌ای به نظرتان نارسا بود یا جایی متن از کادر بیرون زد، همین‌جا بگویید. زبان چیزی است که فقط با استفادهٔ واقعی درست می‌شود.
@whitedns</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1709" target="_blank">📅 16:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLIlT8Y7Cjo5BSExh3v7cm9pwZBj49ip-PREkLiYI4YgrdtPFCikVQhTQT4DsBllc-XIAtXTjLQLg6fI7sfkGnnk06DkybPA0X47E1mpKW-yFFrOvAGc7o3tzfEDBd_XEosEAUGoAqx4ex7Bc5-cynA--uCGCV76C8s_SDfZ4nOjCKe1jqfRglf-WuHuHR3aU20rOFHNnFsdNzxjsyXi5YB9yU_YSvXpxmr6y9wywu4H974EIYdm7WDHWVxEMtftp9dvIAn48euFEMnYszc6wGF8-jMb9eCAG2iMFQZWdOl_9zMic26EADbdHuHoX2gnv8Cya4_n17_tHGAi1T6IBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
این هم یکی دیگه از تست‌های موفق ما بود؛ تستی که با همراهی و بازخوردهای شما، کنار هم مشکلاتش رو برطرف کردیم.
👑
بیش از ۶ ساعت اتصال پایدار و بدون قطعی
به‌زودی ظرفیت سرورهای اختصاصی WhiteVPN رو چند برابر می‌کنیم. این سرورها فقط از طریق خود اپلیکیشن در دسترس شما قرار می‌گیرن.
تیم WhiteDNS، یک تیم کوچک و با محصولاتی کاملاً رایگانه و هیچ درآمدی از کاربرانش نداره؛ تنها پشتوانه‌ی ما، حمایت شما از کانال یوتیوب و یوتیوب WhiteDNSـه.
❤️
ممنون که کنارمون هستید و کمک می‌کنید این مسیر رو ادامه بدیم.
به امید روزی که نیاز به هیچکدوم ازین ابزار ها نداشته باشیم.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1708" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/whitedns/1697" target="_blank">📅 18:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1695" target="_blank">📅 17:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616b32759e.mp4?token=AyEAHw4pYq3EOmH75V1UHl99OToWJU2UdwjFtG-y3O8GG0PycwIwDEZhSo1-C903mQUxYaQ631Znuw53x9Qaa7KWzfddSyNlHfdv9D0ijRjyHQCrCPTG7KfhUPqfu8UUVo7VwkkwCBYnn4V2DthH47lkunNelxIn_bSdqbAN82ew4nqqMPA-fRrZPSlDgapVYyfa3ol1OCaISuHOCwpMrvkcFnPDSmrnM-IJL5S-5ekHc_qfFskGGmIYKfhmTAQmrrK8S_9bD5pAuLxy-DljWFvipy739fv9etvBrRrUGjsm-RJyHQx-a9wxEAD1BqXlxas8YQxUkdl1vWqA3CmNPVb9y1doldAfd0wgmLk0N7xtvt97lQNfCQb2QIlhaBDqMXqGuTuJd1906fOvsog894C7gfZiVqDyCG0lkZmbHG3kt-UwjGUFyILFYiXqne1Odx3MyAJqQzemHVUO_nLvCS8jQNBc1hOe6L7yxOSEg5kW1cFMlSUHSYeebes4OUE30QuMRHfWTpQwLhUwTXWlEW9J1H7i7zCVN_E5LBTiJP4Jul1xxWBTDwa92VnpyaHIKIQaa1MiZ81R4agDOzEzuCItVx32s6Wv4n16ly2-eT7Qn0QGZOw1V8-idLsgE1aHEIgPgGQG_1YH0As7sTEu43RJ-f2wLP3yRqhnw_75X34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616b32759e.mp4?token=AyEAHw4pYq3EOmH75V1UHl99OToWJU2UdwjFtG-y3O8GG0PycwIwDEZhSo1-C903mQUxYaQ631Znuw53x9Qaa7KWzfddSyNlHfdv9D0ijRjyHQCrCPTG7KfhUPqfu8UUVo7VwkkwCBYnn4V2DthH47lkunNelxIn_bSdqbAN82ew4nqqMPA-fRrZPSlDgapVYyfa3ol1OCaISuHOCwpMrvkcFnPDSmrnM-IJL5S-5ekHc_qfFskGGmIYKfhmTAQmrrK8S_9bD5pAuLxy-DljWFvipy739fv9etvBrRrUGjsm-RJyHQx-a9wxEAD1BqXlxas8YQxUkdl1vWqA3CmNPVb9y1doldAfd0wgmLk0N7xtvt97lQNfCQb2QIlhaBDqMXqGuTuJd1906fOvsog894C7gfZiVqDyCG0lkZmbHG3kt-UwjGUFyILFYiXqne1Odx3MyAJqQzemHVUO_nLvCS8jQNBc1hOe6L7yxOSEg5kW1cFMlSUHSYeebes4OUE30QuMRHfWTpQwLhUwTXWlEW9J1H7i7zCVN_E5LBTiJP4Jul1xxWBTDwa92VnpyaHIKIQaa1MiZ81R4agDOzEzuCItVx32s6Wv4n16ly2-eT7Qn0QGZOw1V8-idLsgE1aHEIgPgGQG_1YH0As7sTEu43RJ-f2wLP3yRqhnw_75X34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✍️
اگر WhiteVPN فقط با زدن دکمه 《اتصال》 براتو کار نمیکنه، میتوین کانکشن هارو دستی تست کنید و بعد وصل بشید.
⛏
این ویدیو ۱دقیقه بهتون یاد میده چطوری این کار رو انجام بدید.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1694" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX8FI6o-7xBR0nAYhq78pgw8rqorPm8mc1BKTcvakxautZnKncXH96Mu4xax2F2mC3EJmE_1ojQ-VTAZg3ZadU5G9hh_Q310dfD5aQLSCdJ3FF96IsNus4s90iFmx06dLhVKo0DHjYbbo1TwLN5A1vVtVdIZN78C0uUyHIGcGcJkkX7Rsz5N0Yv3yUDtW92870CI3RRu4RHzFioUi5Xl9pmXNYhABdrqzZ5_ZHkeSskEI5sS9Tc5rgh_Af1ChEbdBjARNZeX9SIU3NkQgCpAEakyho5STY8LkAcUEd9aI6WywxXzpEIQsbbvXTqTHyVz25qYK5Y7U0fY2z3iWZk_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
ما تصمیم گرفتیم محتوی متفاوت در زمینه تکنولوژی داخل
چنل یوتیوب WhiteDNS
بذاریم
این اولین ویدیو متفاوت از موضوع هایی هست که تا  امروز داشتیم و توی این ویدیو دایانا ۵ ابزار کاربردی
و
رایگان هوش مصنوعی برای تولید محتوی در موضوع های زیر معرفی میکنه.
🎙️
Speechma — تبدیل متن به گفتار و ساخت صدای AI به‌صورت آنلاین
🎨
Leonardo AI — تولید تصویر، آثار هنری و تصاویر خلاقانه با هوش مصنوعی
🧪
Google Labs — آشنایی با پروژه‌ها، ابزارها و آزمایش‌های جدید هوش مصنوعی گوگل
📸
Clipdrop — مجموعه ابزارهای هوش مصنوعی برای ادیت و ویرایش عکس
🎶
Suno AI — ساخت آهنگ باکلام و بی‌کلام با استفاده از هوش مصنوعی
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1693" target="_blank">📅 11:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1690">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DJxVhQyJWK3xg1ywiuSvPRWr5hBnV2-5V0UFyXfiZN9obVwtNC5hWfSQzUMdyM0DZsks3gH12ajNPhJnqbwb8YFYr6_2quk9bftGhtPq3TIJ7kPVgGZdiU1Y2I2VePyVJn7VeNhOxCsg9XrSHFxVr0XhrinIZSyBP2KM7QuwJ9ENA9XPDIqS3YK_CgpMg2I1NXTMPu0G4I9M2MCniCmJbovXag8f9OcRL17_g-6DvV24ghZCrqQfbqIChaEYofz8kgawVbLevNbn0mg_iGZiMm-Jm4c3q4U_KlnygVGiQVz3UBiiD1iiuWQbhSL0JJJ7vxyPG7YrMt1gj_QAL6fqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1690" target="_blank">📅 11:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1689">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚠️
اصلاحیه
نسخهٔ ۱.۲.۷ منتشر شد
اگر نسخهٔ ۱.۲.۶ را نصب کرده‌اید، لطفاً به‌روزرسانی کنید.
🐞
مشکل چه بود
در نسخهٔ ۱٫۲٫۶، اگر پروتکل را روی وارپ‌در‌وارپ می‌گذاشتید و دکمهٔ اتصال را می‌زدید، برنامه بسته می‌شد.
بقیهٔ پروتکل‌ها سالم بودند. فقط وارپ‌در‌وارپ.
🔧
چرا این اتفاق افتاد
در نسخهٔ ۱٫۲٫۶ یک باگ قدیمی را رفع کردیم که باعث می‌شد روی وارپ‌در‌وارپ مرورگرها باز نشوند. برای آن رفع، اندازهٔ بسته‌ها را به عددی تغییر دادیم که این تونل واقعاً می‌تواند حمل کند.
ولی آن عدد از حداقلی که پروتکل IPv6 لازم دارد کمتر بود، و اندروید این حداقل را اجباری می‌کند. نتیجه‌اش این شد که ساختن تونل رد می‌شد و برنامه بسته می‌شد.
یعنی رفع ما مشکل بدتری ساخت: قبلش وصل می‌شد و مرورگر کار نمی‌کرد، بعدش اصلاً وصل نمی‌شد.
بابت این اشتباه عذرخواهی می‌کنیم.
✅
در نسخهٔ ۱٫۲٫۷
حالا وقتی تونل نتواند IPv6 را حمل کند، برنامه آن را روشن نمی‌کند به‌جای اینکه بسته شود.
نتیجهٔ عملی: وارپ‌در‌وارپ فقط با IPv4 کار می‌کند. این محدودیت واقعی این تونل است، نه چیزی که بشود دورش زد.
هم اتصال درست کار می‌کند و هم مرورگرها باز می‌شوند.
به‌جز این، هیچ چیز دیگری نسبت به ۱٫۲٫۶ عوض نشده. تمام قابلیت‌هایی که در پست قبلی گفتیم سر جایشان هستند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1689" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔗
نسخه جدید اندروید whiteaesther منتشر شد -
🔥
1.2.6
این نسخه یک باگ مهم را رفع می‌کند و بخش زنجیرهٔ خروج را برای فهرست‌های بزرگ بهینه می‌کند.
پایین همه‌چیز با آموزش آمده.
🐞
رفع باگ: مرورگرها روی حالت وارپ‌در‌وارپ باز نمی‌شدند
اگر روی پروتکل وارپ‌در‌وارپ وصل می‌شدید و همه‌چیز درست به نظر می‌رسید ولی هیچ سایتی بالا نمی‌آمد، این همان مشکل بود.
چه اتفاقی می‌افتاد: اپ به گوشی می‌گفت بسته‌های بزرگ‌تری بفرست از آن‌چه این تونل می‌توانست حمل کند. درخواست‌های کوچک رد می‌شدند و هر چیز بزرگ‌تر بی‌صدا می‌افتاد.
برای همین بعضی برنامه‌ها مثل تست سرعت کار می‌کردند ولی مرورگرها نه — مرورگر بسته‌های بزرگ می‌فرستد.
این باگ از نسخهٔ ۱٫۲٫۲ بود و حالا رفع شده.
⚡️
زنجیرهٔ خروج برای اشتراک‌های بزرگ
اگر اشتراک شما صدها یا هزاران کانفیگ دارد، این بخش عملاً غیرقابل استفاده بود. چهار مشکل داشت که همه رفع شدند.
۱) باز شدن صفحه گوشی را قفل می‌کرد
اپ همهٔ ردیف‌ها را یک‌جا می‌ساخت، حتی آن‌هایی که روی صفحه دیده نمی‌شدند. حالا فقط همان‌هایی ساخته می‌شوند که می‌بینید.
۲) دکمهٔ تست همه تمام نمی‌شد
روی هزار کانفیگ حدود شانزده دقیقه طول می‌کشید و هیچ نشانه‌ای از پیشرفت نمی‌داد. حالا دکمه می‌گوید چند تا تمام شده، و همان دکمه متوقفش می‌کند.
۳) فقط چند تای اول پینگ می‌گرفتند
همهٔ تست‌ها یک‌جا فرستاده می‌شدند، یعنی صدها درخواست هم‌زمان از یک تونل. تونل اشباع می‌شد و بقیه به نتیجه نمی‌رسیدند. حالا دسته‌دسته فرستاده می‌شوند.
۴) اتصال، لحظه‌ای گوشی را قفل می‌کرد
اپ کار سنگینی را روی رشتهٔ اصلی انجام می‌داد، دقیقاً وقتی تونل بالا می‌آمد.
🆕
قابلیت‌های جدید در زنجیرهٔ خروج
مسیر: تب Routes ← گزینهٔ Exit chain
🔍
جست‌وجوی کانفیگ
بالای فهرست یک کادر جست‌وجو هست. بخشی از نام را بنویسید تا فیلتر شود. روی فهرست هزارتایی، این تنها راه پیدا کردن یک کانفیگ خاص است.
✅
انتخاب چندتایی
کنار هر کانفیگ یک تیک هست. چند تا را انتخاب کنید تا روی همه‌شان کار کنید.
⚠️
تیک با انتخاب کانفیگ فعال فرق دارد. برای عوض کردن کانفیگی که ترافیک از آن می‌رود، روی خودِ ردیف بزنید نه روی تیک.
🗑
حذف از فهرست
بعد از تیک زدن، دکمهٔ حذف ظاهر می‌شود.
⚠️
نکتهٔ مهم: کانفیگ‌های اشتراک واقعاً پاک نمی‌شوند، چون اپ دفعهٔ بعد دوباره اشتراک را می‌گیرد. اپ فقط آن‌ها را از فهرست کنار می‌گذارد.
اپ تعدادشان را نشان می‌دهد و یک دکمهٔ بازگردانی دارد، تا کانفیگی که ناپدید شده با اشتراک خراب اشتباه نشود.
🏓
دو نوع تست
هر دو دکمه حالا بالای فهرست هستند، نه پایین آن.
▫️
Test all — همه را امتحان می‌کند. روی فهرست بزرگ چند دقیقه طول می‌کشد.
▫️
Test selected — فقط آن‌هایی که تیک زده‌اید.
راه عملی برای فهرست بزرگ: با جست‌وجو چند تا را پیدا کنید، تیک بزنید، و دومی را بزنید. خیلی سریع‌تر از امتحان کردن هزار تا.
📶
مرتب‌سازی خودکار
فهرست خودش مرتب می‌شود: سریع‌ترین‌ها اول، بعد آن‌هایی که هنوز تست نشده‌اند، و آخر آن‌هایی که این نسخه نمی‌تواند به آن‌ها وصل شود.
📺
اندروید تی‌وی
تیک‌های جدید با کنترل تلویزیون و دستهٔ بازی هم کار می‌کنند و حلقهٔ فوکوس دارند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد. از این شروع کنید
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
اگر مشکلی داشتید، از مسیر
Settings
←
Diagnostics
گزارش بگیرید و بفرستید.
@whitedns</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1687" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نسخه جدید
🎯
WhiteVPN Desktop  منتشر شد -v1.0.20
این نسخه بیشترین تغییرات کاربری چند وقت اخیر را دارد.
سایت‌های ایرانی دیگر از تونل رد نمی‌شوند
بزرگ‌ترین درخواست شما بود: لازم نباشد برای باز کردن بانک یا سامانه‌های دولتی، وی‌پی‌ان را قطع کنید و بعد یادتان برود دوباره روشنش کنید.
مسیر: تنظیمات ← سایت‌هایی که از تونل رد نمی‌شوند
سایت‌های انتخابی مستقیم از خود دستگاه شما خارج می‌شوند. سریع‌تر باز می‌شوند، و آن‌هایی که آدرس خارجی را قبول نمی‌کنند درست کار می‌کنند.
▪️
فهرست از قبل پر است. اولین مورد، کل دامنهٔ کشوری ایران را یکجا می‌گیرد
▪️
دیجی‌کالا، آپارات، ورزش سه، دیوار، اسنپ و شاپرک هم در فهرست هستند
▪️
هر کدام را می‌توانید حذف کنید و هرچه خواستید اضافه کنید
▪️
محدودهٔ آی‌پی هم می‌شود اضافه کرد، مثلاً برای شبکهٔ محل کار
▪️
چسباندن آدرس کامل اشکالی ندارد و بخش‌های اضافه خودکار حذف می‌شوند
پیش‌فرض خاموش است. آپدیت نباید بدون انتخاب خودتان مسیر ترافیکتان را عوض کند، پس اول سوئیچ بالای همان صفحه را روشن کنید.
⚠️
هر چیزی که در این فهرست باشد با آدرس واقعی شما خارج می‌شود، دقیقاً مثل وقتی که وی‌پی‌ان خاموش است. هدف همین است، ولی یعنی هرچه نمی‌خواهید دیده شود جایش در این فهرست نیست.
🪟
یک پنجره، هرچند بار که کلیک کنید
تا حالا هر بار اجرای برنامه یک آیکون تازه در نوار وظیفه می‌ساخت. دو بار، سه بار، و هر کدام یک موتور جداگانه که سر پورت با بقیه درگیر می‌شد.
حالا اجرای دوباره فقط همان پنجرهٔ موجود را جلو می‌آورد. مخصوصاً وقتی پنجره را بسته‌اید و برنامه کنار ساعت است، که از بیرون شبیه خاموش بودن به نظر می‌رسد.
🐧
حالت تونل روی لینوکس
تا حالا فقط روی ویندوز کار می‌کرد. حالا روی لینوکس هم هست و رمز را از طریق پولکیت می‌پرسد. اگر پولکیت نصب نباشد، گزینه اصلاً نشان داده نمی‌شود، به‌جای اینکه باشد و همیشه شکست بخورد.
🎨
رنگ آیکون کنار ساعت
حالا وضعیت اتصال را از رنگ آیکون می‌فهمید، بدون باز کردن پنجره:
🟢
متصل
🟠
در حال اتصال
🔴
ناموفق
⚪️
قطع
🔌
پورت اشتراک‌گذاری روی شبکه
وقتی اتصال را با گوشی یا تلویزیون به اشتراک می‌گذارید، حالا پورت را خودتان تعیین می‌کنید. قبلاً اگر پورت اشغال بود، برنامه بی‌صدا پورت دیگری برمی‌داشت و دستگاهی که تنظیمش کرده بودید به جای خالی وصل می‌ماند.
هر دو پروتکل روی همان یک پورت کار می‌کنند.
🧪
تست همهٔ اشتراک‌ها در یک اجرا
دانلود
ویندوز، مک و لینوکس، همه از این نشانی:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1683" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Kf2usYB-WKD_03ugif05LEW2c_7rBEEt1FDVv4AcDREggGBNbVceF19HHp2Zoo1LTDLT-yVtZ1QGe5a_Z3QUNA3uZBMEGHM-iyXX3IcxsR7B7b6_Q1leezZv-urFTIAj-_Ia7r2rFqMFxZqT-tco-B1hKJyNN4NyrgKO7Wu7JGaDkxAyjoA-kDideE6y-P4vUmTrT4SmZwoiIKWzp3dQs_HRqvLOREbZSQ2Q6IfTNxdEDLuGTdoKFXvuGybITdRinZfkKoywjsFFyMwWMBuBXwDneRGSlzdaZLky2S5S92d6S-MOnXXvazffQ6lrRR2ACfMW2Mm7zCKsLsMQRxN4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
نسخه جدید WhiteDNS Clean IP Finder منتشر شد.
🔭
تغییرات اصلی:
🟢
پشتیبانی بهتر از IPv6
🟢
انتخاب IPv4، IPv6 یا هر دو در ASN Scanner
🟢
بهبود حالت‌های Fast و Thorough در DNS Scan
🟢
بهبود DoH / DoT و مدیریت Timeout
🟢
گزارش‌دهی و مرتب‌سازی بهتر نتایج
🟢
بهبود Nearby Discovery برای IPv4 و IPv6
🟢
بهبود نسخه‌های Android و Desktop
🟢
بدون نیاز به تغییر تنظیمات نسخه‌های قبلی
📱
دانلود آخرین نسخه از گیتهاب
📱
تماشا آموزش اسکنر WhiteDNS Clean IP Scanner
⭐️
اگر پروژه براتون مفیده، توی GitHub استارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1680" target="_blank">📅 09:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=U8khiUwLVamReJyWtnn_ZbaO47EjBTGiLRVtm9MKPeWIE_ZMM669RN6shapCzeG6KE2RXukeJkQ9U0MhdMqhsQYDxD4Qac0jE_M1CHLvTxS5IUIYET3wGjwjMWjNwoJVxqJ7w_ePBENnRf_Z38-XvhM_P_6AwWyUK1GaIZ19rcxJ1OAhMx3zs2jlENZX6Defo5uzHhJVHCsdtlXWE4UKL6Q1-NO4-_leDwkRZpV0sZvGrprhu4eiQzMRDMnjMqkn0ikMUhmko4-rlbBksX48SCGdGotBMgeUS8-TJcutCPBQaIadu2ZHye8fTWXhdSrVWR5feujlIEvXAsWbe9bvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=U8khiUwLVamReJyWtnn_ZbaO47EjBTGiLRVtm9MKPeWIE_ZMM669RN6shapCzeG6KE2RXukeJkQ9U0MhdMqhsQYDxD4Qac0jE_M1CHLvTxS5IUIYET3wGjwjMWjNwoJVxqJ7w_ePBENnRf_Z38-XvhM_P_6AwWyUK1GaIZ19rcxJ1OAhMx3zs2jlENZX6Defo5uzHhJVHCsdtlXWE4UKL6Q1-NO4-_leDwkRZpV0sZvGrprhu4eiQzMRDMnjMqkn0ikMUhmko4-rlbBksX48SCGdGotBMgeUS8-TJcutCPBQaIadu2ZHye8fTWXhdSrVWR5feujlIEvXAsWbe9bvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اگر برای باز کردن اپلیکیشن های
x.com
یا اپلیکیشن های AI مشکل دارید، میتونید از داخل WhiteVPN مسیر زیر رو طی کنید
تنطیمات > اتصال ها > یکپارچگی TLS
Settings > Connections > TLS Integrity</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1679" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1676" target="_blank">📅 10:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
🔼</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1675" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/whitedns/1670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/whitedns/1670" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZs1uzJJqoJj4Og8qjRn7EtSH88VQ8ItRE3naHEqPemi1RjOvb7zNZBg4an9wwDa5Oy5s2gql9x5Q4A2uvkW2IMEmcBHhqtfs8_eHPIFLZo8nEtHpc0Ee5vfvWw7P_WQXPJtio2jd_2yStRCz-AOnvc40YBQfvt4ZcxAq4kR78MsP6ha7rMhTiRNp6zDd62JBpE7-MYWUxC3p4suxxy9ahr7lKWNa43Yx5N-s7mRUs8tV-YcFxkbPER3iOnuUMIyCoHZXX0SIw50xxPUA1IW2URF6ii9XTB9nYXoEZqzMA7PCCxGDB2BfOeejfqGg0hGpDB5-KMzubcDHGjZeaXKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/whitedns/1669" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AcFKv0lfAVA0kcDw-AOwt6_KOYAnF2Cj6e_DOvUkRXrZPr81vQkpKUZU2ZQ0JeDPLH1MeDV2kUVsSASsF-xaXAQU4azWB3AKFpKsxjtW2fvWkgKtM6jme8CaNPlcJlr9ANpAY_hViAlfNd4mJ97brVCM5puBm4HvCq66ivS5UufPyEeWl5AuFw4654Mmi_DetTThdNz85vGjGL8YNbUTU7ukDKutWq0r-yI_heASdhxZTEHGra-4nPqNYyKuWhcmwTe_dqQL-Zlqajm8tXvfXb6QNsezmfn8t2HIJ80d2JBDN2Erct5ngcAMDNOyrAZUkgGN5M4qf6Xb0R3X0W2SVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه رسمی و شفاف‌سازی مجموعه WhiteDNS
دسترسی به اینترنت آزاد، پایدار و امن حق طبیعی هر کاربر است. مجموعه
WhiteDNS
با هدف تحقق این هدف و تسهیل ارتباطات، خدمات و زیرساخت‌های خود را در اختیار عموم قرار داده است.
بدین‌وسیله رسماً اعلام می‌گردد:
۱۰۰٪ رایگان بدون هیچ قید و شرط:
تمامی خدمات، سرورها، کانفیگ‌ها، دی‌ان‌اس‌ها و آموزش‌های ارائه‌شده در چنل رسمی
WhiteDNS
کاملاً رایگان بوده و خواهد بود.
عدم وجود هرگونه اشتراک پولی (VIP):
این مجموعه هیچ‌گونه اکانت ویژه، پولی، پلن VIP، یا سرویس اختصاصی فروشی ندارد.
ممنوعیت کامل خرید و فروش:
هرگونه خرید، فروش، واسطه‌گری یا سوءاستفاده مالی از نام، کانفیگ‌ها یا سرورهای
WhiteDNS
غیرقانونی، غیرانسانی و نقض صریح قوانین این پروژه است.
هشدار نسبت به کلاهبرداری:
اگر فرد یا گروهی تحت عنوان ادمین، نماینده یا پشتیبان
WhiteDNS
به شما پیشنهاد خرید سرویس، اکانت یا پرداخت هزینه داد، سریعاً او را مسدود (بلاک) کرده و موضوع را گزارش دهید.
تنها مرجع رسمی:
کلیه اطلاع‌رسانی‌ها و به‌روزرسانی‌ها صرفاً از طریق کانال تلگرامی ما منتشر می‌شود:
🔗
کانال رسمی تلگرام:
https://t.me/whitedns
❤️
حمایت شما تنها از طریق معرفی کانال به دوستانتان و اشتراک‌گذاری اینترنت آزاد با دیگران و تماشای ویدیوهای ما در
کانال یوتیوب
و دادن
⭐️
به پست های ما و همچنین boost کردن کانال و حمایت از
گبت هاب
ما  امکان پذیر است
کلیه خدمات  WhiteDNS همواره رایگان در کنار شما می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1665" target="_blank">📅 06:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1663">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔥
درود دوستان عزیز :
با توجه به رای گیری که شد و نظر دوستان عزیز
مقدار حجم روزانه کانفیگ های ربات به
4 گیگ
تغییر کرد
❤️
اگر از این خدمت استفبال شود احتمالا به زودی سرورهای بیشتر با لوکیشن های بیشتر در اختیار شما عزیران قرار خواهد گرفت که هر چه بیشتر امکان دسترسی رایگان شما فراهم شود .
بازم تاکید میکنیم که این کانفیگ ها فقط و فقط برای استفاده در قابلیت " exit chain " در برنامه های whiteaesther و whitevpn است . متاسفانه هنوز یک تعداد زیادی پیام دریافت میکنیم که دوستان میگن چرا این کانفیگ های توی v2rayng , hiddify و .......... کار نمیکنه
.
⚠️
لطفا تمام مطالب پست زیر را با دقت کامل بخونید
https://t.me/whitedns/1608
لازم به ذکر کرد در صورت مشاهده هر گونه سواستفاده از این کانفیگ ها لطفا به ادمین ها گزارش دهید
درصورتی که مشاهده شود که کانفیگ ها توسط افراد سودجو  در حال فروش به دیگران است این خدمت به طور کل حذف خواهد شد - پس خواهشمندیم خودتون در حفظ این امکان کوشا باشید
ربات :
@WhiteDnsChainbot
ارادتمند
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1663" target="_blank">📅 05:56 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

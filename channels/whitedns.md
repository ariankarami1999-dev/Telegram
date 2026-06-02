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
<img src="https://cdn4.telesco.pe/file/MeWK350V5YzRzsICEKnp8077cSqYZiArl9azmBABIXSm10N1sLeJ4DoRjHYRdGdoC4We1MuK8O2Coc-vvu1zKhWlc7P-gjPUtWCFoppVoKCmPTb-PDSBbG1LZNOgncjjSHMrA588GPYvk7x7v-27D_NWybT39MoNlgGW6ptXPtFStoyEahD0qkmV7_jW_mAhEzqY8zakzaFLlqB0YGcHC-UiYMVzO4x_Reh-QdTA9un3B2p39w4nFqRs0r92KgagGE5oy4flG6mSUzsCRj8cJ5xQGWyMDooKeK4dnP9xDXYlOYVl8b6stFkCjVFTShC_3tXlRL2oT1Y9Lt4nAZmE3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 104K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/917" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان نگران نباشید، ما ۱۰۰۰ تا دامنه خریدیم این مدت برای سرویس های DNSTT & MasterDNS
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
لینک ساب جدید
http://sub.iampedi1.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
نکته، تمام آدرس های قبل کار خواهند کرد. ساب گیتهاب و تمام این ساب ها و ساب های آینده یک محتوی خواهند داشت.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/whitedns/916" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/whitedns/915" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69013b2789.mp4?token=nMPSfDQwvzVR2baSqgYluKzwax3hVHxOVwnpkrB6nevvPpn2lC0runZVQ6GHOhkiVOU9ejqw0vbBJMdPCoFvAcirDkXLXI3gldaqik9ZxIw6ToZkgPvn-8rJg7WhTn2EgzlxZFZ1YQ-la02BKCuYhyiQtlsnGzHX0eKyeqLARDTzsZBR_gycMp6AdQpzX_OKRJyQkNW16FeCf4oIMsY5cBgqzFvh6EjJaMvxYC8s1ss8UIulZD7B4qBpByGPt7a0U8j59dModkjVqs2Kd4pcjMROmINOkdem78z-MX971Gjwug1Q8h5hpaN90Mjxr2Yja_OPmVI68UpJUrW6-EqryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69013b2789.mp4?token=nMPSfDQwvzVR2baSqgYluKzwax3hVHxOVwnpkrB6nevvPpn2lC0runZVQ6GHOhkiVOU9ejqw0vbBJMdPCoFvAcirDkXLXI3gldaqik9ZxIw6ToZkgPvn-8rJg7WhTn2EgzlxZFZ1YQ-la02BKCuYhyiQtlsnGzHX0eKyeqLARDTzsZBR_gycMp6AdQpzX_OKRJyQkNW16FeCf4oIMsY5cBgqzFvh6EjJaMvxYC8s1ss8UIulZD7B4qBpByGPt7a0U8j59dModkjVqs2Kd4pcjMROmINOkdem78z-MX971Gjwug1Q8h5hpaN90Mjxr2Yja_OPmVI68UpJUrW6-EqryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آموزشی فعال سازی Fragment در اپلیکیشن V2Ray در موبایل و دستکتاپ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/911" target="_blank">📅 02:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلام خدمت همگی،
دوستانی که از همراه اول یا سایر اپراتورها استفاده می‌کنند و اخیراً با مشکل اتصال مواجه شده‌اند،
بر اساس تست‌های انجام‌شده، به نظر می‌رسد در روزهای اخیر روی برخی اپراتورها، از جمله همراه اول، DPI سنگین‌تری نسبت به قبل اعمال شده است.
به همین دلیل پیشنهاد می‌کنیم اگر با اتصال مشکل دارید، گزینه
Fragment
را در تنظیمات اپلیکیشن‌های زیر فعال کنید:
V2Ray
FlClash
Clash Party
Mi Clash
گزینه Fragment می‌تواند در بعضی شرایط به عبور از DPI و بهتر شدن اتصال کمک کند، مخصوصاً زمانی که اتصال روی برخی اپراتورها سخت‌تر شده یا کانفیگ‌ها دیر وصل می‌شوند.
اما توجه داشته باشید که فعال‌کردن Fragment همیشه به معنی افزایش سرعت نیست. در بعضی موارد ممکن است باعث کندتر شدن اتصال اولیه، افزایش جزئی پینگ، کاهش سرعت در بعضی کانفیگ‌ها، ناپایدار شدن برخی سرورها یا مصرف پردازشی و باتری کمی بیشتر در موبایل شود.
بنابراین پیشنهاد ما این است:
اگر اتصال شما مشکل دارد، کانفیگ‌ها وصل نمی‌شوند یا اتصال ناپایدار است، Fragment را فعال کنید و تست بگیرید.
اما اگر اتصال شما بدون مشکل و پایدار کار می‌کند، الزامی به فعال‌کردن Fragment نیست.
به‌زودی آموزش ویدیویی فعال‌سازی Fragment برای هرکدام از این اپلیکیشن ها ارسال میکنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/910" target="_blank">📅 02:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اپلیکیشن‌هایی مثل FlClash و Clash Mi چطور کار می‌کنند؟
اپلیکیشن‌هایی مثل
FlClash
در اندروید و
Clash Mi
در آیفون، برنامه‌هایی هستند که به شما کمک می‌کنند راحت‌تر به کانفیگ‌های مختلف وصل شوید.
فرق اصلی این برنامه‌ها با بعضی از اپلیکیشن‌های دیگر این است که لازم نیست تعداد زیادی کانفیگ را یکی‌یکی وارد کنید و هر بار دستی تست کنید کدام وصل می‌شود.
شما فقط یک لینک سابسکریپشن وارد می‌کنید. بعد از آن، برنامه خودش لیست کانفیگ‌ها را دریافت می‌کند، آن‌ها را بررسی می‌کند و بر اساس تنظیمات، بهترین گزینه را برای اتصال انتخاب می‌کند.
مثلاً وقتی شما لینک سابسکریپشن WhiteDNS را داخل برنامه وارد می‌کنید، برنامه یک لیست از کانفیگ‌های آماده را دریافت می‌کند. سپس می‌تواند از بین آن‌ها، کانفیگی را انتخاب کند که در آن لحظه بهتر کار می‌کند.
آیا این برنامه‌ها هم‌زمان به چند سرور وصل می‌شوند؟
معمولاً نه.
این برنامه‌ها معمولاً برای هر اتصال، یک کانفیگ یا یک سرور را انتخاب می‌کنند. یعنی سرعت اینترنت شما با وصل شدن هم‌زمان به چند سرور مختلف ترکیب نمی‌شود.
اما برنامه می‌تواند چند کار مهم انجام دهد:
کانفیگ‌های مختلف را تست کند
کانفیگ خراب را کنار بگذارد
بین کانفیگ‌های سالم، گزینه بهتر را انتخاب کند
اگر یک کانفیگ قطع شد، سراغ گزینه بعدی برود
مسیر بعضی سایت‌ها و برنامه‌ها را از پراکسی عبور دهد و بعضی‌ها را مستقیم باز کند
برای همین استفاده از این برنامه‌ها معمولاً راحت‌تر از وارد کردن دستی تعداد زیادی کانفیگ است.
فرق FlClash و Clash Mi با برنامه‌هایی مثل V2Ray چیست؟
در برنامه‌هایی مثل V2Ray، معمولاً شما یک کانفیگ را وارد می‌کنید، همان را انتخاب می‌کنید و به همان وصل می‌شوید.
اما در برنامه‌هایی مثل FlClash و Clash Mi، شما معمولاً یک لیست کامل از کانفیگ‌ها را وارد می‌کنید. بعد برنامه می‌تواند بین آن‌ها انتخاب کند و بر اساس قوانین مختلف، ترافیک اینترنت شما را مدیریت کند.
به زبان ساده:
V2Ray یعنی: این کانفیگ را بگیر و به آن وصل شو.
FlClash و Clash Mi یعنی: این لیست کانفیگ‌ها را بگیر، تست کن، بهترین گزینه را انتخاب کن و اینترنت را هوشمندتر مدیریت کن.
حالت‌های Direct، Global و Rule یعنی چه؟
در این برنامه‌ها معمولاً چند حالت اتصال وجود دارد:
Direct
یعنی اینترنت بدون پراکسی و مستقیم از اینترنت معمولی شما رد می‌شود.
Global
یعنی تقریباً همه ترافیک اینترنت از یک کانفیگ یا سرور عبور می‌کند.
Rule
یعنی برنامه خودش بر اساس قوانین تصمیم می‌گیرد کدام سایت یا برنامه از پراکسی رد شود و کدام مستقیم باز شود.
برای بیشتر کاربران، حالت
Rule
بهترین گزینه است، چون برنامه هوشمندتر رفتار می‌کند.
چرا استفاده از سابسکریپشن بهتر است؟
وقتی از سابسکریپشن استفاده می‌کنید، دیگر لازم نیست هر بار چندین کانفیگ را دستی کپی و وارد کنید.
کافی است یک لینک وارد کنید و بعد از آن، برنامه خودش لیست جدید را دریافت می‌کند.
اگر لیست به‌روزرسانی شود، برنامه هم می‌تواند کانفیگ‌های جدیدتر را دریافت کند.
این یعنی استفاده راحت‌تر، مدیریت بهتر و دردسر کمتر برای کاربر.
خلاصه خیلی ساده
اپلیکیشن‌هایی مثل FlClash و Clash Mi برای این ساخته شده‌اند که کاربر مجبور نباشد بین ده‌ها یا صدها کانفیگ سردرگم شود.
شما یک لینک سابسکریپشن وارد می‌کنید، برنامه لیست کانفیگ‌ها را می‌گیرد، آن‌ها را مدیریت می‌کند و کمک می‌کند راحت‌تر به گزینه مناسب وصل شوید.
این برنامه‌ها معمولاً چند سرور را با هم ترکیب نمی‌کنند تا سرعت چند برابر شود، اما می‌توانند اتوماتیک و یا در حین اتصال کانفیگ‌های خراب را کنار بگذارند و اتصال پایدارتری ایجاد کنند</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/909" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه  https://github.com/iampedii/whitedns-sub   لینک ساب برای Clash Party & FLClash https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/908" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/907" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ما هر ۴۰ دقیقه ساب رو آپدیت میکنیم. شما هم یک آپدیت توی اپ بزنید تا بهترین کانفیگ هارو بگیرید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/905" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/whitedns/904" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/903" target="_blank">📅 13:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/901" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آموزش استفاده از FLClash
ممنون از رضا عزیز
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/898" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚠️
برای وارد کردن ساب باید به یک وی‌پی‌ان  متصل باشید</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/897" target="_blank">📅 10:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/whitedns/896" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcdPOMuRl6kOBLsq3e9U-WSGhb4xbBZQkxZ53utVX8p9PbjRpTmehcl6ST4x4hh5Jm0fLP3Iw62RC0q27N7ocmYWproxYAcrZbgvwq41y3SnGQiHGm4-diPEpobxS6OZuaKe-GplXy-ahVdSqbe_bvshcTIfPVZx6e9RcbrAf8UY9mWlFuvcitFcgyGj6djwxrBbsElY4uirob6_TDz5XgI2W9HinQZcxPs_pwj9Qau5ckdix9fLWsUY-UAZSPt141FjggWV7lLFovEn_x1-3MZi2TFDifgURDp5UGKKVEflIJ0ayXAAaV3iFligHBR86RPMXZFatSi0aGchjpBf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
http://sub.iampedi1.live/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلودFLClash برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/whitedns/893" target="_blank">📅 10:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=vHA5J6bEuRpW7naw2mjPkSvLp8sQgMw5NxmOiHcKRTmCmB9d34j9kDLojBcRiTiWu-3TLWmL1pS8cB38LRN0SrTKuOf71cspzNP3EkUm28cFkXC2YD992Iai7T8fD90NTgsmP8cdpb2uayPWYu0Nvn9YF7fFS3ZlYq0WvUZZucBb_9y-8xWB1ds9UZkic8S-LbdvM02wz9OxltTC4sroM50pg8R7rPy62p91ODEg01K_DPtG1nSI_qQ5jJK5oMKeRPgfeSmwt2hrq_sSKMMdke1pTgC_NXTI3FTKeYqsQZto_TtQ5i_4HVTypdciE2qkVK3kf1GPVMd4eSAin_LEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=vHA5J6bEuRpW7naw2mjPkSvLp8sQgMw5NxmOiHcKRTmCmB9d34j9kDLojBcRiTiWu-3TLWmL1pS8cB38LRN0SrTKuOf71cspzNP3EkUm28cFkXC2YD992Iai7T8fD90NTgsmP8cdpb2uayPWYu0Nvn9YF7fFS3ZlYq0WvUZZucBb_9y-8xWB1ds9UZkic8S-LbdvM02wz9OxltTC4sroM50pg8R7rPy62p91ODEg01K_DPtG1nSI_qQ5jJK5oMKeRPgfeSmwt2hrq_sSKMMdke1pTgC_NXTI3FTKeYqsQZto_TtQ5i_4HVTypdciE2qkVK3kf1GPVMd4eSAin_LEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنین کاربران نسخه دسکتاپ می‌توانند از قابلیت
تبدیل کانفیگ‌ها به IPهای سفید
به‌صورت مستقیم در داخل اپلیکیشن استفاده کنند.
🚀
Tools > V2Ray White IP Generator
@WhiteDNS
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/whitedns/885" target="_blank">📅 04:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEUAnPSn7D5jIYh20XSUOMHFy1nGOyf8U4mq0_IJ6X-FmJc59JOJwjL8KKOJr5HCrQ8r8Jub01U_fY_5WQxRmtT-LKIp9rKa6bMzUWB1CE2j3hzGiH6OFin_nJbglskqoh9Hr5qklSjdHC0s0dhacHhf31RwoCjTcK_imxkXEDXCGIKmtFAsyjng-9B4QDqwVz2WSDoBjhoh9po_7Mx7QGZWjOFWse7hVLL1HpDpCFd37i2Xw77MKb_haLKSIHpM1PnzoKXHMRnUUeKtfAYIwkmECggKL0v9wk3KzmTJ4ECBvTUKI2gU35iFeU0abGNZvi-muiOeRUYeQo_7Mx9ZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/whitedns/883" target="_blank">📅 03:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سلام خدمت همگی
❤️
الان تنها راه اتصال پایدار و بی‌دردسر اینه که شما یکبار اسکن کنید، آی‌پی مناسب پیدا کنید و بذارید جلوی کانفیگ‌هاتون.   متاسفانه فرمول یکسانی وجود نداره که برای همه کار کنه.   این روش رو میتونید برای کانفیگ‌های رایگانی که از ربات ما هم دریافت…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/882" target="_blank">📅 02:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/881" target="_blank">📅 02:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/880" target="_blank">📅 02:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nan6LzFp_8CBB4kJHn1883NE5xbkWkUYiBGzl_2kAk83MFLIldJ31vy-fKxDkLB48XjbRDtrYTyCHEdNtwMxY3ojY7CUUnvDFjeafu5gW6xVqLqeI2j0J8OmPLE9WKZTZlCJEYBsEpfljXy8wxpv9kMq8z-i0Hyitb0RvlaViiCvjwdEsnit7-Up-s5V3MSXnQ2ELjN8DqYtABvj12nPAUhGsbpTxM2ELNU0I_mfGv2VXwVvXNkKfC7DaxZYCtfliDC8_RJoYZwXaY1RzJtsheI6ml7pFlnC1pBSoBiLJAqpT4_gmMkngLI0Xg-BVcrSEj1domD-nWZ4VBy5Mq_EWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شرایط سخت و روزهای «خاموشی دیجیتال»، تلاش کردیم با ساخت ابزارهای مختلف، آموزش‌های کاربردی و راهکارهای ساده‌، کنار مردم باشیم و کمک کنیم تا حداقل دسترسی آزاد به اینترنت حفظ شود.
اگر در تمام این مسیر فقط توانسته باشیم یک نفر را دوباره به اینترنت آزاد جهانی وصل کنیم، برای ما ارزشمند و افتخارآمیز است.
اولویت و هدف تیم WhiteDNS همیشه ساده‌تر کردن ابزارهای پیچیده و تسهیل در دسترسی به آموزش بوده تا به هموطنانمان کمک کند وابستگی به بازار سیاه، واسطه‌ها و مافیای VPN کمتر شود؛ با این نگاه که هر شخص قادر باشد ابزارها و اتصال‌های امن خود را بهتر شناخته، بسازد و مدیریت کند.
امیدواریم هرچه زودتر شرایط بهتر شود و حق اولیه و ساده‌ی دسترسی آزاد به اینترنت دوباره به همه‌ی مردم برگردد.
از تمام اعضای تیم WhiteDNS و تمام وطن‌دوستانی که در این روزهای سخت کنار مردمشان ایستادند، صمیمانه تشکر می‌کنیم.
دم همه‌تون گرم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/879" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuYLOEY03exCuXvC5W16Ha-j-I0pHusafhLlsnT3ZDEur5jc-OE2whzLuLKY9sjIYGF8iygDhBxss_Q1zGJf9mhF-vnrief2lhWCN1Z8a2A4lh1z3vPwn6zsCRjwIHIm1upPzaRL2z6wBtcRtynrVQVgksHIHlTkgi9ckQdzRU3xmcwm3c8f5maKKsST1SnWEo1_Xdeg5xcM-mnCr7tgno7gt_Z2nuSW5cdTJdoa0HlVznWVTMOpHzdwyj9iFxkz8AZZ8SssiywWB8Ie3yQj7FobKr-jr718MoWnyzRDdL55IGin-Qy0fOdGrhrlYvXwuVNPVowiwQI8qw86g8Ve2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/whitedns/878" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر  - آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن - آموزش استفاده از V2Ray  - آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی  https://guardts.ir/f/6f56591f7b7a…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/877" target="_blank">📅 10:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#موقت
ارسال شده در تاپیک سرور ها
سرور اهدایی از بامداد عزیز برای MasterDNS  قابل استفاده در  اپ WhiteDNS
🔑
Encryption Key
aaf4b6-@JavidnamanIran-aaf4b6fff
💻
Domains
: جداگانه امتحان کنید
b.bamak.xyz
b.igoii.org
b.namad.xyz
b.jnir.my
b.irdmc.com
b.javidnaman.com
Encryption Method
: XOR
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/875" target="_blank">📅 04:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/873" target="_blank">📅 02:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر
- آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن
- آموزش استفاده از V2Ray
- آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی
https://guardts.ir/f/6f56591f7b7a
https://up.theazizi.ir/download.php?t=ecabdec17d6cbb16f37a13fe28c724cdb591
😊
مشاهده از یوتیوب
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/872" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-linux-amd64.deb</div>
  <div class="tg-doc-extra">19 MB</div>
</div>
<a href="https://t.me/whitedns/865" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnGHs0G4atInE_9qb75Tod5wc-dsPY4UNlZh3sOS_KYLJXGlQXvifXdhHQvwrniQT5g9FmUK42jZBw_lP_PD7O8xyKSUuWWsazJHo_5Gp5R1KKD9_hTLPI3LBTwGKPlW32y-yl6tVcQfqC7TarWDH_LR7AMVcNa268i5MXNrqPT9xppQqUnABy6UEjbsvmJ1yBPinElXK0rJN5vz3ESr8W4MRdHwA7k4_5dQPVjavlBJ2oODUpWitHk2aYUvRG9hmMNoXcdp_o_j1kwBv9yhk_6uzeQPYKKuiGVBcgH7dUgR3KzIqGaYMki1iuyen6XgFhk9lBKzdhytLR2owuEmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انتشار نسخه v1.0.0-beta5 اپیلیکشن کامپیوتر WhiteDNS
⚪️
تغییر هسته از Sing-box به Xray
🔴
اضافه شدن امکان اسکن آی‌پی‌های شرکت‌های زیرساخت ایرانی. با این قابلیت، اگر رکوردهای A+، A یا B پیدا شوند، می‌توانید از آن آی‌پی‌ها به‌عنوان سرور برای کانفیگ‌های خودتان استفاده کنید. شما همچنین میتونید لیست خودتون رو برای اسکن وارد برنامه کنید.
⚪️
بازطراحی بخش کانکشن‌های V2Ray. این بخش حالا برای مدیریت تعداد زیادی کانفیگ مناسب‌تر شده است.
⚪️
اضافه شدن امکان Speed Test برای کانفیگ‌ها.
⚪️
اضافه شدن پشتیبانی از پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، Hysteria2، WireGuard، SOCKS و HTTP Proxy.
⚪️
اضافه شدن قابلیت سفیدسازی کانفیگ‌ها. ابزار جدیدی در بخش Tools اضافه شده که با وارد کردن کانفیگ V2Ray، آن را به کانفیگ‌هایی پشت آی‌پی‌های سفید سرویس‌های مختلف تبدیل می‌کند. همچنین می‌توانید لیست آی‌پی‌های سفید دلخواه خودتان را وارد کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwkWetzneuvQE8cooQmZ5MN00Y-phVbGI94nazm3GLYoZkU28IeIyGltWcsW-5Vze1GAAmCnOm1EobnYgrWRDvRfa5T1mbt5lsdKwris0WXBebZyWRwjbbK5wLirRurMusshBMCUCmSclWQ3hHmgUiQU1ydlRpWGDDyoWIe0Bw1hptXGYmqEh7vp-oHNpf66xUvd2sVadqJZHrJajoPwcLuC3S2ofDwRSYIhgzChD3W-bsvbBJVHj6XLvctEo58WdjnnmWZNBB40yWjbwRuMZOuMkSfXTjVkR45Xrg_0wf45Fac0oqDei9OclrZqjVDJ80u-usG1kyx5JFbBJa1ZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/whitedns/852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vi3K6FASIajb0UAkWQkQXXwI6eD6tXMRdoDfMfuhjtq5gQ8oHrDuFDD8SR4fCBFuFkMuUscE4Tf8PFHwwYq0MyT6WqR2MUH08aarfNcMZVVYQ7DOVmQlivxJ5095owQW7nZXV7pXYB600pb5e24tolCD3EJl73Czzi4jRxxhCuz7tGQ6UvEqlf0p2ImwsWEJElHJ5tmPgLujEDHfwCWhaS2dE7IBxy0Cz5BIfSc9ef-JZpv83y0xwz-krdp-nVBBljxy3TBIlioRvImVmBWDqSdWnQkoPgu04eNNfMyNwosUcjeZ6mxpsnhgcGD4njSLyBGtfSn8d-8jZ00mBQf98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ckz--pbcUurN2_fIoOKhWbqEJ05AN23HbGkBAFEGyr-eFm5KFpPDQ-HJUDabY3C4TkzVj0ipj1gi9o5twZ3lX7rhzNE7vrGTNQQd-qn2bD8XaCCnROjIbkrc5nkx8dZhpIau22ycYt8Ip_DpaXS59suglYAO8UVGWJ-AUbEzAFtJhpWLG89STMGmwK1jfsUqQMi16n4v69ZjSpMpqFM1npIvRs2xylABZl3qSHoa23EdNNLfPUGtX4fS2DUov6VTBbjdaOAybZCpBJIg6jFl1jJBpyzdGyeJjmqwGQ5R0fgsee0G9ysQ3YCfM-IRiLVXy6uynHdh34IAKHbP0yT5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/whitedns/841" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ELMrzwYCXI6az0cJEDv1iYV8lI675Bg7G0sZZm0B4XT9AtXMH1QSc7E-UU0vNqGuOXS7RSi2c3HaQnUSARVBrd9y7KzkiEy9dVmq6AC0Do_lzskht_8zhw1pGOGxSw7Cc7sVGH8nhLjYFv8ti5BtzFjhUurIorCeJMhzq5OPjeGcDnHfj2HjIE0Y8KEnTtLA-uqEUH5ok_OdAoZ_H27d4VBdaJJC5uPf_OZNt_72zhnbA53fC1-BllXgHJFYL9XFk00N8ukEkDrwWz9d6ti5Pb7zAwgyY6YkdBUNYS31wUpIlDRNByCf0gtyWdDO4oaOUT4NSDitzquC-Vw-6Ncgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QbgjCVupwHf8m8pFKcVtrRtdVzq6wFlQzINOjxr92YQnzdl_xE1ZS76SN-TuSaXHLk47VNUEojdMuHrQkQRUcFCROUxJliRWXeG1BUrM1FzI_ly1EwFwe0aBkSy0oP7nXTKnIpM9u_Vq2Ro65gXDgcpDULJtwAsrLhRMymLgByx9UGlDFl9fIyhvmAboWXgNz4YLBj7o6D_QjT19E-sd2gv5xw44A0wCLcIrgin_t0ZfkrO7R8k0iHLr5eMDyL7fNUea83KeRsZWIs1_DPKPTmqtgvzcfnJhl9MrjIU3Q15aqJUvrzCDPhA-JpYcrS6093y-WdX5NFkm42Gp5xkNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/geud5g-KAKuSER5mIx5bhztvL6_srd_B50jzIWW-OZ-TgfHCZdtO21j2SMjbv07JQ_-8W6J9kfTzWJvsQUyE3_ttRCBwxVCYr222NVAFvvpBC5NkTOhovFyhovUa_h-WpadNjs3zWU0Fh2YlzJXyIi8RAL_FOVkh77ILBKw1BnAem2qYRfviQKs-dodr4-fmK5PV5_6GweNxSJD1xV3l_Hray5L6jdN9tU2VOengcBt1EmDSNmQ_xj2GKuPK8aaVJgeKt-263S9IdWSa-iRPmcv78Hn2WOcOyXjluJnGL_vZv4OXLJX0OcTBAyveMqN-rhmzH0uQov7oQbiodv5nvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z14FGaeywJUzcJlz6BPGYOw2J98LFsAAbhJXR4Z1tFnRzK3N5t3f9c7nHgX6pxhztlQRT6WC9rlDAYAf2Y2NhsvhePh7jrOijyTPMYs2ZPP5Ue22mEx329T8YylRLBvPvg9p8BGCAF_c8M2Gv2z_ksnHEiA5CuTokuyczLiNb39QGQ5bJG89Lx0oIj6URInD_KIopXIKAwYr20iOxfJno-9g7kqw5mrAi3PKR9ZJfqdcLBe1l4MnfdtO3a1HftUGTkQK7e0uY3yOrfseswP1zzTugGzLyna9MEmvWk1iNF1QR7eVMOIhPpWeYvneexKdhelTxuc6E_Lt6L1VBHeLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HQtyc108efUJjTK94YiQ8T02_I9dIFr3qyzgXd6-SHWDr9kB6OkE3iMI2bt9fxU_rrEo0kk4sbTHT288N8i9O9RJ4i9cy_zVFG2IuKtUDE9W3w678PjdayuFwQOk-BS1Kcv7ZAsD1iMUrDfSpFAwaljapzVAbiJ0GiQCXQnQBhQUJREmlkNdo0VQ4aYy3qgFp-50a0Xng0QaB2bHZ9LrdwzguJefvkdS9LE7MGpmj0SCNSM4zYTXtgPXQuUtntYlTNaSD4mj8dh-228HKh3BK2AR84xVZjiZv_bShPavzD2fkBfc0liM1PQwjWF3vhQlBqbZ9zHLBUsMeegDHs1RpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ac7SHEQ4fJ-V1kBXc_cHhs8qVrRXeYqH86deh2vkrwgBumP1W7Ww88JhEzqLecAjuuYSGOp_tuVAqvABvzhcceSe9qsqJJQkd5Ve5kiOeT4CVprrc8d_CJPkurhLPdVAD5vY4gqGpBmT1lqBwb_V3VEjcgycsY20aeZKzEUNtWG7c5LfKX6Uj6oPKgV2ObllgbT3vcgIWebVMEoiUcJxmt6t1zNFY8dNqKduU3q0hEwaJssm4q-57t3a11W2T63m1iFXTk9-0F1U2ALS_hRMA81eo2IwvVEUJeUoPcGcbUN6WaiAMdSXAeRKOw0JJXnP-48vr9HAt35WfppYC_H4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/th0-vYUO4syyUiOinDuQzbcZRqsnTaDM_owWkPwqiIeWEyE6AoDPMVJZSvbPksHFCGPwq_w8ELO-VD9YnxQUGepAK8tWtQTMjI6kgktyOtWKIHr_NEp5ifU-aOligiO4fKCwuUTZA3sS92UFbbNiqGfrDLbKmuI6qc4618N9t7eQbdtrM-WJLRZclZNo0IzhD82XTGyHwMvxZzXyGdkAqRrbL1qz100EJhQv3d7-FeXU72FBlMDZEhVOnknvVkJ9ScJ_684jnZZ5H_XWbgW7QO2LU0ozDweiEeYbs68rbdLUOHqn8o77bG6jElOoKLP3VBNyLbkEA0NHD1wbUlt_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bsp_dzgBNCCmLVyUFcUmaIvj-02C9UwnqC3HUN90y8aO79MUgssANHxN-VZyQu-13uoNv_7WOGnPJuB4iTryaILl7Qv64J-TaN6ly9ZxW_6rrE3yEJ02OX9iHiFW6UnMdgVlseXzdPdoy3QQOjKUglkdtJvFEw4SFpKZ6ejsvPfQibMGJ-EUJtYfHBcxviPl2dKE7uY_H7WiNxnXJ2U-Hq7m_Ssx0GOhc_1DLJt9-D5BUWe7wUU6XgTSwPs9_i8BMQOHyYevZ1C50SbMSUkXf7yTNRBTbEXegcme7bajLiGTJuOWnPksfUiIjaHmLW0h2CYwjIsMgcQQc4xsKyVVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/peCkDtKYPTbAshgE6aJAVZkqDKShGh4uUf-8bu_12ueIRMKChLSVAFgg7taYG4rHnw_ewVRJK7XS83I9e87E0lSR-MdttZ0WhYIm8Vz8sCJvVaf_lGy3dKEB6MtwbF9kIgY2ECinDe3_OI39xi-aqjgujT-OBfed6jX8ywBlgqKyis0Wx2iV3J7Uk9CKeOeiANFEzEk82g10jCt0iUZ62ejEgrqyLv8XuKuRhBlZ__Q_Xmvmyy738nWJVv2_YgWe0OZgUXXAhi4ukqMPqEGZtU7ICTuyziro2ZTmewEFgZ3noxB7u66fGXOOK_7bM8pQXnH4ZsDSCLW7uDxgZRn2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBRMNcFztiXDl3jEh4Ca_XnTkNrXJR0cJl_VruDOcTE7Ydse-D09SBwyTM30X9uhEEB4WRFd7QPNZ4uTo4J0mm5lnpKXTCCgITn4AFBaSeuwmiTPAcqUUSN0EdN3OwZDDdH0EbamGtbSQSTadLABt7p3zqzBBj7JVdAeqLAx2SiRTbh6PPSZ8hObNOpqeh3A-X5AvFK0dlH_HBbO9JWOIkdmHe5MvOp0ldI8yIiSS6P84w4Jv0WF0UmpJ_ift2LUp8m34WY_o7pbOk4SmklHdEO2TBRESx87_HcfhJkUB9bnWQR2AAEO3Pg96o0bsGPoxubn5vq9wnUxFFnV90Adug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-linux-arm64.rpm</div>
  <div class="tg-doc-extra">24.8 MB</div>
</div>
<a href="https://t.me/whitedns/820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستانی که از نسخه اندروید اپ WhiteDNS  استفاده میکنند.
برای بیشتر کردن سرعت و پایداری
، میتونید با وارد شدن به بخش ریزالور ها، یک پروفایل جدید با مقادیر زیر بسازید
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
برای کم کردن مصرف
، سپس وارد بخش تنظیمات و پیشرفته بشید و‌مقادیر زیر رو تغییر بدید.
Upload Dup = 1
Download Dup = 2
اگر سرعت شما قابل قبول نبود، دوباره مقادیر Dup رو بالا ببرید.
توجه کنید که این مقادیر فقط مناسب اینترنت پایدار هستش. در صورت بازگشت اینترنت به وضعیت قبلی، باید کانفیگ های متفاوتی اعمال کرد.
ممنون
تیم White DNS</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcfdJR3qT0LfrgJktcWSFE30qmIIgs7PQDdru5fNGB2EIfaCuSWuwgZFHhljfgGGyOpxdQXzLM8TLvZzgzLUmHU1gCt5PGKOLdjMhpfll7v1TqYW9M8xEfzBE22cSJ6xt7S5UesAbEsSEAh3ulOmmd0gctykIAMqxl0v98MgeQEODixuRIPal1_wU9MRp4iIUY7qz4k9ksmzi8LEj1esEHtZHtzFGwpixpftDzHYnwai8OWKlo7rxTve-GdirYNP36iT6ruJRspDXLBTqMmPk5icbV-rV-wivYX-lIg8vYPUjufAFoM1Vn7gAMSAOiADzQtCMDPCL-mSQqYB_47Ssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4
با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.
در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription اضافه شده، و ابزارهای داخلی برای مسیر‌دهی هوشمند، مسدود کردن تبلیغات و عبور مستقیم ترافیک سایت‌های ایرانی از شبکه داخلی فراهم شده است.
اتصال MasterDNS هم پایدارتر و کم‌مصرف‌تر شده؛ درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت حالا تقریباً شبیه یک VPN معمولی است.
✅
پشتیبانی از V2Ray اضافه شده است.
✅
پشتیبانی از VLESS، VMess و Trojan اضافه شده است.
✅
امکان وارد کردن کانفیگ و Subscription اضافه شده است.
✅
آدرس‌های خصوصی و داخلی مستقیم وصل می‌شوند و از مسیر V2Ray عبور نمی‌کنند.
✅
سایت‌ها و آی‌پی‌های ایرانی با geosite-ir و geoip-ir مستقیم از شبکه داخلی عبور می‌کنند.
✅
تبلیغات، بدافزارها، فیشینگ و ماینرها مسدود می‌شوند.
✅
همه ترافیک‌های دیگر از پروکسی V2Ray انتخاب‌شده عبور می‌کنند.
✅
کش داخلی sing-box برای لیست‌های قوانین آنلاین فعال شده است.
✅
MasterDNS پایدارتر و کم‌مصرف‌تر شده است.
✅
درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت تقریباً شبیه یک VPN معمولی شده است.
✅
سرعت اتصال بهتر شده و Packet Loss کمتر شده است.
✅
ریزولورها به گزینه‌های بین‌المللی و قابل اعتماد مثل
1.1.1.1
و
8.8.8.8
تغییر کرده‌اند.
✅
حالت تاریک، Scanner جدید، بکاپ کامل و رفع باگ‌های زیاد هم اضافه شده‌اند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Defyx VPN
🚀
یک اپلیکیشن VPN مدرن، هوشمند و متن‌باز که با Flutter ساخته شده و با تمرکز بر امنیت، حفظ حریم خصوصی و تجربه کاربری جدید، دسترسی آزاد و رایگان به اینترنت را فراهم می‌کند.
🌐
🔓
🔹
متن‌باز و قابل بررسی
📜
🔹
رابط کاربری مدرن و روان
💻
🔹
تمرکز بر حریم خصوصی و امنیت
🔒
🔹
مناسب برای دور زدن محدودیت‌های اینترنت
🕸
بروزرسانی جدید
⬇️
GitHub:
https://github.com/UnboundTechCo/defyxVPN
📂
@whitedns</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Orbot for Android v17.9.4 BETA 2 (tor
0.9.4.8
)
بروزرسانی جدید
Orbot 17.9.4 (2.7.0) برای اندروید منتشر شد
📲
این بروزرسانی، موتور Tor را ارتقا داده، روش‌های اتصال جدید اضافه کرده و چند مشکل اتصال را برطرف می‌کند
🔒
🔧
.
✨
تغییرات مهم:
• ارتقا به Tor
0.4.9.8
برای پایداری و عملکرد بهتر
🚀
• اضافه شدن پشتیبانی از Shadowsocks داخل خود Orbot
🌐
• امکان استفاده همزمان با پل‌های obfs4 ،Meek و WebTunnel
🌉
• گزینه جدید «بدون پروکسی» برای خاموش کردن سریع پروکسی بدون حذف تنظیمات
⚙️
• بروزرسانی پل‌ها و ابزارهای دور زدن فیلترینگ
🛡
• بهبود DNSTT برای اتصال بهتر در اینترنت‌های محدودشده
📡
• رفع چند باگ و مشکل اتصال
🐛
📱
مناسب برای افرادی که از Tor برای دسترسی آزادتر و امن‌تر به اینترنت استفاده می‌کنند
🔐
🌍
.
دانلود
📥
https://github.com/guardianproject/orbot-android/releases/tag/17.9.4-BETA-2-tor-0.4.9.8
@whitedns</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPfc5Tb3zdZ1HN2AdbEZNLVGPzpSZCMf6patVlvmpxs3Oc5XKAOXtGHRHo_76bgbFFH-QkpgF4RNpPSoUeDLHWPu0t8FX1vsPbFQgtcn5to8wDWPyrOyBHn-6Q57ksmG3Ux5vPaO5OY2Us-WXI_Yc4dyz9u9IpHp9A87ljcakp-8MJbmcq5yUwpejo1KOy4fQzdkqymIgDcGlC14eb5cR51WgZ9jhVAWs24_D29fejP9oyJzxduILKU_BqXC3UkBqez0E7gzLgf5S_9yJuBXjkUyHKfz28L7UOweFZPZubn7k2Ub52Vk_1gpP6ZVpG-GCEzY34hRbFbUMl1OOTk-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای استفاده از کانفیگ های بالا میتونید از اپ v2ray یا دیگر اپ های مشابه استفاده کنید
👆
👆
👆
اپ های قابل استفاده:
npv tunnel
happ
nekobox
MahsaNG
v2raytun
v2box
V2rayN</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayconfigs_with_WhiteDNS_2.txt</div>
  <div class="tg-doc-extra">30.2 KB</div>
</div>
<a href="https://t.me/whitedns/805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">115 کانفیگ تست شده دیگه پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2ray_configs_WhiteDNS.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/whitedns/804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">141 کانفیگ تست شده روی مخابرات پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUcHvSXUo28hD2YffmKPeugXc86Kft4agFhDByV__uzq1Pe_lbgchY9PJFgx6hIfHb03b1sV76i4XfVdi-EZspYT91gHWCNBDbFBJrzr2FBzO4OaNQVBb-FxfXhFN33kbM5aHEqL-rFjxzBhO1xThoq3fcSPvx6pWcCzihSgoiVm1bXIBsMDJTzN22-OufYpTBE491ypOvdzuYMTnyNSk8rKwmiyURkiCpYn4ZD5FLZS87IMBj5AP9KW6s8NP3GgK7vqvsffXlNjyRxaG6be70VRgL0ZGsQQ6zxPgSam9qZx6VpYoyoSENCSXq6l9vc8QqUEbe5GBqhEB_xdBnEw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_6AlYFUC52vzvb5Nl4n_F-dF4VSe6zwb8JftRujFNXBJQU5SHMB_qghjSb1YbPI5nmM0hCt0yhqd5H7TcAYogPmj3wMqSi9lM2ZECuIfrjbranl_Y5csus3ORZ8ZROHkLb2uC6CSNI3InT-A8aJwOMIim35BqGPQxgE6kXLbuw0zd-hod-wfMWKnyNMDIc2Xme0kWkIoYQXYm1HS1zh0S44vS0uW4DiGQ4SpNn4KWeQrVQhCKZ7cbAZB-xz3HiNUFSjRxAAYuQQLL7Vg0Cl2WpBma-9W9hh3SBd3ctyXVL1RjdNGVTcTUdKQIJ_ufoQ23mXmWcKsLr48CKEoz-NvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">“}
سلام خدمت همه عزیزان
❤️
امیدواریم این روند ادامه‌دار باشه و اینترنت به‌زودی برای همه اپراتورها به حالت پایدار برگرده.
برای دوستانی که فعلاً به سرویس‌های دیگه دسترسی ندارن، می‌تونید از ریزالورهای زیر استفاده کنید:
1.1.1.1
8.8.8.8
همچنین بهتره مقدار
Duplicate
رو کمتر کنید تا مصرف اینترنت پایین‌تر بیاد و اتصال داخل اپ پایدارتر بمونه.
حتی در صورت برگشت کامل اینترنت، سرورهای WhiteDNS همچنان فعال می‌مونن و می‌تونید ازشون استفاده کنید.
یادمون نره، مارو از کمترین حقوق شهروندی محروم‌کرده بودند. فراموش نمیکنیم.
دم همگی گرم بابت همراهی و صبوری‌تون
🔥
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoISYcrRQQzGovFo3CC5JEW5ntNnVUWb4I-vyq0LAMC8KA2IpULibnGh_8p71SGe3Q1y4cq6TR0rbrWw52s629kBAcEwJ_f4b9oFJx_vPFTL7HNJvUCLa5A8CNuZ70IxKyoMvSHyDNowu6qmvN18mxvJ2Wp12q1r24zYZX2EYBhp7xzPx1tZDJpBdDzQqFh-ioOnpAKvDDJd_yP9dcj0TyIXa3Wseq2B_ZsbcCeIYumfW7Rju1V96wkUfjr6rqOFr8fGi56DqYi9E9l_wO1eA6rgIX1A7ep51Tx85UaPVOhDosqTUxdqGemEAArqTbUJ6MR7z9fzQeaSHohx6RRwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZZJOHeybeCuDYJGh7VQOmTjaX5A36exs0_tEfsNMMoXKjN4wN9TA75QyxesIgbbqaAwLnjOCKd9g944cC8687qg9aj54p7jbrmMlzy6x3G1WCck05vZh3x5qSFq0S171WNGwguUqe0Qo5AaGpV9lFAhJ0DgrcGI5MN9mYKacn0vQvbHvN-gucevYsBAb5VotEncw3V07i-un9pILxTRqfTGKFbdNZmcP6WAGX9ozaStvaxb6vsc7CMpcj0aS2p6tFVUYqmTUX4xH-54RZBq0CuJVwU9oNTg67Y1mgm0y7z3XTeDxGMgNzvoxNTpyza0Ty9rzawUHQiP8LBQcn4xnt2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZZJOHeybeCuDYJGh7VQOmTjaX5A36exs0_tEfsNMMoXKjN4wN9TA75QyxesIgbbqaAwLnjOCKd9g944cC8687qg9aj54p7jbrmMlzy6x3G1WCck05vZh3x5qSFq0S171WNGwguUqe0Qo5AaGpV9lFAhJ0DgrcGI5MN9mYKacn0vQvbHvN-gucevYsBAb5VotEncw3V07i-un9pILxTRqfTGKFbdNZmcP6WAGX9ozaStvaxb6vsc7CMpcj0aS2p6tFVUYqmTUX4xH-54RZBq0CuJVwU9oNTg67Y1mgm0y7z3XTeDxGMgNzvoxNTpyza0Ty9rzawUHQiP8LBQcn4xnt2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXMN1VMcjLwrTLce8nwkt5guAqLf-FOjTJZqtskxEWaxjMrfZshzg7oXgGbozQFcolKqAjchl08agR7Bm--HREq8gncEAP86tSFBWOd1aObTxHb3pA14KcZsWijVpkNgN_tVsOJGBmC1IPhLft5rpfx07OPdo77qDAGQwnHQSnfAYa98O4jH_sTjXLpe4js-BDhfjRFof9UCLIPPdITXNhJpaWnugs0caNhjfGhmvViUogholdrUSduZs0dmG1kW8JezW5xV1NnKy6ffkhotEdkAPiU1Yz-y4W76HxTAlEfS6rj5b_nKhTsHp1K5c4BrteTFHjbMUuTMcsZagHDBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💥
موقت
🚫
دوستان :
اگر سروری دارید از جایی  میگیرید که پورت ۲۲ نمیده اصلا خرید نکنید
ظاهراً یک عده دوباره دارند سر مردم کلاه میگذارند
داستان داریم به خدا
لطفا اگر توی گروه های ما کسی داره کلاهبرداری میکنه با ذکر ID گزارش کنید
@WhisperInHeaven
🚫</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXgBh3kzcLwJzp0CO15LwojjQssRbFYxFFFlhz1pekIn2Uf5XbIevlW13nbmGN_r2vqHzNHsV1fRBNrzI9FLQnvfAR2xfPuh_hn1H4w0qBfiEaaxIzK7hSYAOsAt7Zqz8h_VKvYATXp2kr8OB0K-hCwgb4UY8qIV1mCMGuH3jr1sbUIyKetmSdBCxH1SnNWA2MlmqoIG1Nz5QMUfycWFvC38RGK1onmnf2dHYt-AaCrT4u05SDNC32vONq0dVC7SF6Fak6VKu-pGbh_JeFXeaHcvP1CoDStFQJ6_FVlV0EqQFmM055617R1Nu20vb5bvGXdN23wC_dbaPJrIoH_Pow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Quo2Z_H2Cu97JARdgKnNFdadZXyuZRwAmfAiQY3qCyOsVekDDujHQq9eCRSdxkOJuZB1xmqTmnSNNV-RCLKyvQIqxXyOcDx-iPPX-ZvDLQovPNDim3qWw3jiwsVWOfWSIPaw_-KzOYQMu20CG-_EjgJCEnc94Omgs7therrE1NSvPZWzCGRK8UWcunb5rKBGSj1HchFBOvCGzMOjqb8DOLPgMK7CWzm_IB6MtqmFVKRtm1qZwzup7cl-I0cA09W3eMw_Gp9wfRVFC9Lojr7OoEEZU5U3XeOjerfyoa58GBRSYX1lKGEL4GlKZjA5CA_VOtQdN6Z1PKkCXB7b4BS48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
پروژه جدید WhiteDNS در حال آماده‌سازی است
♨️
تیم WhiteDNS بر روی سیستمی کار میکند که کاربران بتوانند فقط با داشتن یک VPS و یک دامنه، سرور شخصی MasterDNS خودشان را مستقیماً داخل تلگرام راه‌اندازی کنند.
هدف این پروژه این نیست که ما به کاربران سرور یا دامنه بفروشیم یا مدیریت کنیم.
هدف تنها ساده‌تر کردن فرآیندی است که امروز برای خیلی‌ها پیچیده، زمان‌بر و فنی محسوب می‌شود.
در این سیستم، کاربر فقط:
• VPS خودش را تهیه می‌کند
• دامنه خودش را تهیه می‌کند
• DNS Record ها را تنظیم می‌کند
و باقی مراحل توسط ربات و Mini App تلگرام به‌صورت خودکار انجام می‌شود.
سیستم به‌صورت اتوماتیک:
• وضعیت DNS Record ها را بررسی می‌کند
• اتصال دامنه به سرور را تست می‌کند
• MasterDNS را نصب و راه‌اندازی می‌کند
• اطلاعات نهایی مثل Domain و Encryption Key را به کاربر تحویل می‌دهد
در عمل، کاربران می‌توانند بدون درگیر شدن با دستورات پیچیده لینوکس و تنظیمات طولانی، سرور شخصی خودشان را راه‌اندازی و مدیریت کنند.
این پروژه متن‌باز خواهد بود تا همه بتوانند کد آن را بررسی کنند.
در حال حاضر پروژه در مراحل نهایی توسعه قرار دارد و طی روزهای آینده نسخه اولیه آن منتشر خواهد شد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb1_gJhrs6pWymCFv1EUZJlFUB-dwDwL9JYeWJ2WEGm2dbIFe9z1C4LcLNqOfgs_N1VdXBvUi7ZVdMN_5-MJcwj9KS3N43_FnK87kggj3FVbJtbMTj79DMGfCtOGbYYA5dxAOkJ6UzzPDFX8OhwNZpWx9sfSwSoq37--6VayyZCEGlFLPBDoSmS2MwYyrowFgHkNaHkz_jA4oVixt3wvLCMSv0plCeqrNrX5wyCZr-urYZZW4hRFoQOZPmrAS3gMF2gnuYQgcDGiNd2pvv38uhyAcP8DT8-dHLoTcMicrFrdo_8muQgTTk_6MV6gxoEG5M716AZcgusB_He6y4OQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqoXvF2m12j81USssRxAxUZOq8eB75lL2Byv-EioJYEWbGALOOSW85Uw7HZvh_ulIV7D0gPvDDc65RX7BviS-CMmbInRVd2hrwG19RfFRWOy8iMCV9U_JMgkW5MsFPN4gzO9uroB_3isSfRwuLkhqRI7R9JrtP4Ks7k3tJohxj0ETgP9VQdZ5mRer2rBtS9ud5ryBXXtSQcs3mjW3-DrWaXrz2orAuZg90lxd_BqldsaJ50edCTqFWDjX7bvfLGTiH5VCIAxIh_jky1oRzsSYg9Y_7FOrzoqr9A9-WcSIogFggdAs_GcITNMYdVsXZanO66ZIfyOram9ltEveDgocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش پروکسی و تانل کردن ویندوز
در این ویدیو نحوه پروکسی کردن فایرفاکس با نرم افزار WhiteDNS
پروکسی کردن کردن کروم ادج
و همینطور تانل کردن کل ویندوز با متود جدید آموزش داده شده است !
لینک دانلود ویدیو ( داخلی ) :
https://dl.toolschi.com/view.php?f=9f27edab8159500e.mp4
لینک دانلود نرم افزار  TunnelX ( داخلی ) :
https://uplod.ir/75m7wx9r6c17/TunnelX-v2.1.0__Whitedns.zip.htm
لینک گیت هاب TunnelX
:
https://github.com/MaxiFan/TunnelX/releases
امکان هست که آنتی ویروس  TunnelX رو حذف کند. در صورت نیاز اون رو به لیست نرم‌افزار های سفید آنتی ویروس خود اضافه کنید.
منبع تصویر کانال اینترنت آزاد
1️⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDmLW13_JUCiGCyvt8sYD6GSDbILN1NWFckfLd8XjA72rEp65EDwLjFzF7fqhDaMp4ItCiNip_3p8r0Ug-7GWS398iA--kN4svFa6bYAYktcZvdSFAu6hogFC5nICQhVatwdg3vU18vkj9b9S0KYV_4EMxfrG7D5k_XRIOUW6-rez888GB5aPeD_dOG_REGlF74-r0RfTnu7V6LlpQbDNL0nGtGClErl2zRHe5wcZ4YfhPjkBV-gUt8-r9vg05G3QGkgVYtwrd_Z55oEKN0-As_krDnINujayLYJttHXJwoAJGEL1UhqLAttJTQsR-oFQLrLMd0ZRhARKHIiiTCx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEWIA2TMzmxkJFtMjl37Qd4Mh3obhRhPs0ACSS1mX5rNc4O_TAquORRopqvSTZ2k3PKDEXcwPcNgpdgJbLtR0KjWZSV3kLAtHqqrbNvbt0CXz-nxvy4rifRrfZTR5OLBR6i87eDUvbA-MlS7Px-KEHsew98h654aQYRXfGAz_Uc6WcLRGeGfw1yrRk6a1NnUw39H9dUaBG0x53E5UjcJhNr1oRnL7Fo3bC-VfaqUfbLwlU-FJrr46ojz4Wdl5fq0LRSk0mqk1FZ8HDCIoLbgnzE23Q5A-wrYGxpErmLmZ2X4WEDykv5HSp62JZfEAwnBiLvJwBjo5AIo4AxnlTWrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGJPSkNrKPEWefboZlWVJrSi58sfcue_EU6gFyRcV7zyM9tNvP42dZBJm4WdKmuLgcNgwEf-KkYnYBBzGvZvwZuof1CYRNKiMUQSBvhcL9n0SEMjG46Y2HYpzmARqypmCNYt2MH34E8CqnFp31wrPxoXcNZG4r3voXTOtAuTsIdCBdDKjtEnOsKWyu4JKxWR8GsFH4vwWJB9kw0ajA9p2coe04tMEsM48HhRD4eQm9qb9yVncnGlNZg51WbQFaYZKmfVI3k7hrPEiI3IBcmlmgmyZ_LgtjNq87-sbtTm3-6B2P2qq6-ggUiuwYFQ84sUL0Md-DfFl6IEKFI19Av2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیا دانش فنی زیادی لازم است؟
برای راه‌اندازی اولیه کمی دقت لازم است، اما آموزش‌ها طوری آماده می‌شوند که کاربران معمولی هم بتوانند مرحله‌به‌مرحله انجام دهند.
اگر هیچ تجربه‌ای با سرور نداشته باشید، شروع کار ممکن است کمی سخت به نظر برسد.
اما بعد از یک بار راه‌اندازی، استفاده از آن بسیار ساده‌تر خواهد بود.
هدف ما این است که این مسیر را تا حد ممکن ساده‌تر، قابل فهم‌تر و قابل انجام‌تر کنیم.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/771" target="_blank">📅 07:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آموزش‌ها کجاست؟
ویدیوها و آموزش‌های مربوط به نسخه اندروید، نسخه دسکتاپ و راه‌اندازی سرور شخصی داخل کانال قرار داده شده‌اند.
لطفاً قبل از پرسیدن سوال، داخل کانال سرچ کنید.
برای پیدا کردن آموزش‌ها می‌توانید این عبارت‌ها را جستجو کنید:
آموزش
سرور شخصی
دسکتاپ
اندروید
StormDNS
MasterDNS
Resolver
آموزش‌ها مرحله‌به‌مرحله منتشر شده‌اند و با کمی جستجو قابل پیدا کردن هستند.
همچنین داخل گروه اصلی تاپیک اولین شروع همه چیز رو توضیح داده
https://t.me/whitedns_group/32380/38590</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/770" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگر سرور کند بود، مشکل از اپلیکیشن است؟
نه لزوماً.
کندی یا قطعی می‌تواند دلایل مختلفی داشته باشد:
- شلوغ شدن سرور عمومی
- ضعیف بودن Resolverها
- اختلال یا محدودیت سمت اینترنت ایران
- کیفیت پایین مسیر شبکه
- تنظیمات نامناسب
- استفاده تعداد زیادی کاربر از یک سرور مشترک
کیفیت نهایی اتصال به سرور، Resolverها و شرایط شبکه هم بستگی دارد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/769" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چه انتظاری نباید داشته باشید؟
از WhiteDNS نباید انتظار سرعت بالا برای مصرف سنگین داشته باشید.
ممکن است شبکه‌های اجتماعی باز شوند، اما همیشه سرعت عالی نخواهد بود.
برای مواردی مثل این‌ها مناسب نیست:
- دانلود زیاد
- ویدیو با کیفیت بالا
- وب‌گردی سنگین
- استفاده هم‌زمان چندین اپلیکیشن پرمصرف
- انتظار سرعت شبیه VPNهای تجاری
این روش بیشتر برای دسترسی ضروری طراحی شده، نه مصرف سنگین روزمره.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/768" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این روش برای چه کاری مناسب است؟
WhiteDNS و روش‌های مبتنی بر MasterDNS/StormDNS بیشتر برای شرایط سخت، محدود، ناپایدار و اضطراری ساخته شده‌اند.
این روش برای مواردی مثل این‌ها مناسب‌تر است:
- اتصال حیاتی
- پیام‌رسان‌ها
- دسترسی ضروری
- شرایط محدودیت شدید اینترنت
- استفاده سبک و کنترل‌شده
این روش جایگزین کامل VPNهای پرسرعت تجاری برای مصرف سنگین نیست.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/767" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استفاده گروهی با دوستان و آشناها
یکی از بهترین روش‌ها این است که چند نفر با هم یک سرور تهیه کنند.
اگر دوست، خانواده یا آشنایی خارج از ایران دارید، می‌تواند برای تهیه یا راه‌اندازی سرور کمک کند.
بعد از راه‌اندازی، اطلاعات اتصال داخل WhiteDNS وارد می‌شود و همان سرور به‌صورت اختصاصی‌تر برای شما یا گروه کوچک‌تان قابل استفاده خواهد بود.
این روش معمولاً از استفاده از سرورهای عمومی شلوغ پایدارتر است.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/766" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هزینه تقریبی سرور شخصی
هزینه راه‌اندازی سرور شخصی معمولاً خیلی بالا نیست.
به‌صورت تقریبی:
شروع کار: حدود 7 دلار
هزینه ماهانه بعدی: حدود 6 دلار
البته ممکن است سرورهای ارزان‌تر هم پیدا کنید.
یک سرور حدوداً 6 دلاری معمولاً می‌تواند برای حدود 5 تا 10 کاربر سبک و معمولی کافی باشد.
اگر چند نفر با هم هزینه را تقسیم کنند، هزینه ماهانه برای هر نفر بسیار کمتر از اکثر سرویس‌های VPN خواهد شد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/765" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مزیت سرور شخصی
راه‌اندازی سرور شخصی یا گروهی چند مزیت مهم دارد:
- فشار کاربران عمومی روی سرور شما نیست
- پایداری معمولاً بهتر است
- در بعضی شرایط سرعت بهتری می‌گیرید
- احتمال پیدا کردن Resolverهای مناسب بیشتر می‌شود
- کنترل کامل‌تری روی تنظیمات دارید
- هزینه آن معمولاً از خرید VPN کمتر است
- می‌توانید با دوستان یا خانواده به‌صورت گروهی استفاده کنید
ابزار WhiteDNS برای همین ساخته شده که فقط محدود به چند سرور عمومی نباشد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/764" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چرا سرور عمومی جدید منتشر نمی‌کنیم؟
وقتی یک سرور عمومی در کانالی با ده‌ها هزار کاربر منتشر می‌شود، خیلی سریع زیر فشار زیاد قرار می‌گیرد.
در نتیجه:
- سرعت کم می‌شود
- اتصال ناپایدار می‌شود
- سرور گاهی از دسترس خارج می‌شود
- کاربران فکر می‌کنند مشکل از اپلیکیشن است
در حالی که مشکل اصلی معمولاً فشار زیاد روی سرور، محدودیت‌های شبکه، یا وضعیت Resolverهاست.
طبیعتاً یک سرور عمومی نمی‌تواند هم‌زمان برای هزاران نفر مثل VPN اختصاصی کار کند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/763" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وضعیت سرورهای فعلی
سرورهایی که تا امروز توسط تیم WhiteDNS ارائه شده‌اند، همچنان نگهداری می‌شوند و تا جایی که امکان داشته باشد فعال خواهند ماند.
اما از این به بعد برنامه‌ای برای انتشار مداوم سرورهای عمومی جدید از طرف تیم نداریم.
اگر سروری متعلق به خود تیم WhiteDNS باشد، فقط داخل تاپیک «سرورها» اطلاع‌رسانی خواهد شد.
تمرکز اصلی ما از این به بعد آموزش، مستندات و کمک به کاربران برای راه‌اندازی سرور شخصی یا گروهی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/762" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تمرکز جدید کانال
از این به بعد تمرکز اصلی ما بیشتر روی این موارد خواهد بود:
- آموزش استفاده بهتر از WhiteDNS
- آموزش راه‌اندازی سرور شخصی MasterDNS و StormDNS
- آموزش نسخه اندروید و دسکتاپ
- آموزش پیدا کردن و تست Resolverها
- معرفی تنظیمات بهتر
- رفع اشکال و راهنمایی کاربران
- بهبود اپلیکیشن و اطلاع‌رسانی نسخه‌های جدید
هدف ما این است که کاربران فقط مصرف‌کننده چند سرور عمومی نباشند.
نرم‌افزار های ما طوری طراحی شده که بتوانید از سرورهای خودتان، سرورهای دوستان‌تان، یا هر سرور سازگار با MasterDNS و StormDNS استفاده کنید و اتصال پایدارتر و اختصاصی‌تر بسازید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/761" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام به همه همراهان WhiteDNS
از امروز رویکرد ما در WhiteDNS کمی تغییر می‌کند.
WhiteDNS از ابتدا برای استفاده با سرورهای MasterDNS ساخته شده و همچنین از فورک StormDNS هم پشتیبانی می‌کند.
یعنی استفاده از WhiteDNS فقط محدود به سرورهایی نیست که از طرف کانال معرفی می‌شوند.
هر سرور MasterDNS و همچنین سرورهای سازگار با StormDNS می‌توانند داخل اپلیکیشن WhiteDNS استفاده شوند.
تا امروز، در کنار توسعه اپلیکیشن، تعدادی سرور آماده هم در اختیار کاربران قرار دادیم تا شروع استفاده برای همه راحت‌تر باشد.
👇
اما در ادامه یک سوءبرداشت ایجاد شد:
بعضی از کاربران فکر می‌کنند اگر سرورهای معرفی‌شده شلوغ شوند، کند شوند یا موقتاً در دسترس نباشند، یعنی خود اپلیکیشن WhiteDNS مشکل دارد یا قابل استفاده نیست.
در حالی که WhiteDNS فقط یک اپلیکیشن وابسته به چند سرور عمومی نیست.
قدرت اصلی WhiteDNS این است که هر کاربر یا هر گروه کوچک می‌تواند سرور MasterDNS یا StormDNS خودش را راه‌اندازی کند و از همین اپلیکیشن برای اتصال استفاده کند.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/whitedns/760" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">White DNS
pinned «
سرور جدید WhiteDNS   Domain: v.wdn.best Encryption Key: bad99364093861634030e96f11fe3132 Encryption: XOR @WhiteDNS
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/759" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
Encryption: XOR
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/whitedns/758" target="_blank">📅 06:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/754" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLXRjASjafbvTVfzAPhCQyjvYD_CZvtH7hkJTXCcxFZ0_ksBgtGMhT0iA7Nf0CVaUbHMKyKAXpNF72zBRlBExRikYNIZjUEVyLfHACUy_NyYHt0865qWq3TVfRzLxbv2I6bGu00Z1qkPwdjz6Qd-0ChuYOJ7w44oWhlY7aGUYF78quIoEf43bvBywPylKBKHoFfAaCZ-FN_YzzFebG00M0tYtwO3n2GcyVXMmWyLT1VSwUsI9HghzOGFVJeoEGoiHwv21e0LMX2Dki08lcy9weDjADgnaM7Cy8nlkL6s1e5d6dzKEHmgsy8zMYS4hk-nf8XluRrxeAwOzeFyCGoVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/753" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompythash</strong></div>
<div class="tg-text">سرور ها آپدیت شدن
دقت کنید هم رمز و هم دامنه تغییر کردن
سرور StormDNS اختصاصی چنل Pythash/پای هش
StormDNS Server Configs
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
@pythash
Domain:
v1.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
@pythash
Domain:
v2.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
نحوه اتصال:
windows , android:
https://t.me/pythash/74
linux:
https://t.me/pythash/81
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🌀
@pythash
🌀
@pythash</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/whitedns/752" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/751" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/749" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G6N38xJjkZuCZHQOfL9RSk5_ozYvwPd_j_yZfj2N_IH7AtH4gpy9kIy9JvFtoNcwI7RvUEij4T6aTMEoxtCp9yxEl3Hojc62oIY-67i4zDTuUklho1PPx4RW1bMlFwetV03CRryltXbuUuuaDJxMC1dl-uhfrxFeX0eyY8sIenL8hnuYt57_RzLEyxDYWE5Y3nkt5YqORsmVc8oWfFmYfDExaUXegzMtFAC43EyIAZae68oeOK2ztKbiz3BBEzuW1qT89SB3FQvOIy7s5u4gwAXTlko9NS4-_ss4FGSObUGRjxgpq1mpEA40_me6zPAvEPYUDcKNv0Y8za7x9gkLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/whitedns/748" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

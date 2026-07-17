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
<img src="https://cdn4.telesco.pe/file/jJlm_qvRkjMq7zRxVJFrq9bS8879I03DxKk4umhUr_2DvabyxWY1ZWaC5gD6t8sL9MwgMEApnxPdGFIO5TTys4o91YehjyBKXAJrK3htMUtWEmiApgTI9UG4VzwFz8sGbJV4HvRYPcTLtA5a8UIAJq57pqynZtv2YLuPI_ct2kjzO3MauGOkUfedljYU76P38gEhIpdlKZlqVkLB0qj0n0DBDhdDhFKDUcsP1moMI-HmoWPgIZo1epcsiyDN55niVk1k-GDkNn-WMxxre8plxq13Deh3FB8CyDEc6MDLN0bRyjGbZlMm69Z4HtnhW0YP-CbJkUMt9ALTy-MRmWeXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 52.8K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-2779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
آمریکا با تحریم‌های جدیدش، صدور گواهی امنیتی (SSL) واسه سایت خبرگزاری فارس رو مسدود کرده. این کار باعث شده دسترسی کاربرا به سایت مختل بشه و اخبارشون هم کم‌کم داره از نتایج گوگل حذف می‌شه.
پ.ن: من می‌ترسم فردا روز اینا واسه جبران بیان سایتای ارائه‌دهنده گواهی مثل Let's Encrypt و اینجور چیزا رو تحریم کنن و کلاً همه رو به فنا بدن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/iaghapour/2779" target="_blank">📅 16:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ-v15iDgbqZfyPx0y337yU_lr5BgaveXnDuhtMt4qH_kxsSdl8ecqHPVIk_gQkoWc1Vg8aPSaT-bw7Y6uZiFvfCBLDOfrFp25zmBrJTQmpL-zpiAUzZYU4GhG5aLrf2-nW9tZwvSB_CEkWctkqKYqzAE-M0bMDE-qXgoHN_oif596-ZyU50IIz76y4xb5xU9uReX2giMtTWzbJ_dM9JZaaZpmx2k5-fi7TlqMQqs0AzGAtphIRjb3RHtmWUZ4cBI799ftiGF5zikWhfrdvrHgKT8BIV1ExJCPPm2sHkbi29nw7I6d_JMh_A22b8ql10OKFFvGRb0KIzGYagh4AMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
فروش ویژه سرور مجازی تک و چند کشوره
🔥
👜
بجای 6 تا سرور مجازی،
2
تا بخر با
6
آیپی
‼️
✅
با
check-host.net
سالم
🤯
تغییر آیپی و تنظیم PTR از
کنترل پنل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2778" target="_blank">📅 21:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APmmOA_HIdYQCbOF4gkHuT4CeHK96h7IflH0RKZLvHP9RtBsgo45UCrWR-mS-cjqItJ8iE1xXs3ZRvYoVnIiA8GgKFHzvvuhY907-kBeXLc1teM2LDCwP97Al5h751Fku-SwbgxeFSqYMPE0iO6a5SgXE_VtEDEdSP__FW0jMDGEWq43LI1HXLN0rdQzce94gyOJhBbf4A7E0ZC6GYujP262C8dAz4PL7-YFnzCDjQSnD3UDT6JD3Ctiax7l2tPgfwR2mCNrV1Xrro0hZSjgV9VM9JlnFL1UCP2R90CrgtkqL2TUTEON7malSISjZ3tD41dTlrEMl3rFSXBfx0WM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره یه روز لو میره که مسی اصلاً آدمیزاد نیست!
یه فضاییه که اومده زمین تا کلاس درس فوتبال برامون بذاره و برگرده سیاره خودش :)</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/2777" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🟢
بچه‌ها، یه سری از دوستان پیام می‌دن و می‌گن «سرور خارج گرفتیم ولی پینگ نمی‌ده و نمی‌تونیم بهش SSH بزنیم، پس خرابه یا به کارمون نمیاد.
یه نکته‌ی رو یادتون باشه: اگه قصدتون تانل زدنه، در بسیاری از موارد مهم نیست که بتونید بهش SSH بزنید!
مهم‌ترین چیز اینه که
سرور ایران شما
بتونه سرور خارج رو ببینه، بهش دسترسی داشته باشه و پینگش رو بگیره.
👌
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2776" target="_blank">📅 20:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دیگه واسه چی غصه بخوریم؟ از اینکه حتی نمی‌شه یه آینده‌ی خوب رو تو ذهنمون تصور کنیم؟ از اینکه هر روز باید با قطعی برق سر و کله بزنیم؟ از اینکه وسط جنگیم؟ یا از اینکه تهش قراره آرزوهامون رو با خودمون به گور ببریم؟
🖤
خدایی دیگه چه انرژی و انگیزه‌ای واسه آدم می‌مونه؟ اصلاً نمی‌خوام نق بزنم یا فاز ناامیدی بدم، ولی واقعاً یه جاهایی آدم کم میاره و رسماً می‌بره... کشته شدن این سربازهای بی‌گناه هم که دیگه مثل یه تیر وسط قلب همه‌مون بود. آخه چرا باید پژو پارس بشه آرزو؟ چرا باید یه ۲۰۷ مشکی بشه سقف رویای یه جوون ایرانی؟
😔
خدایا... فقط بزرگیتو شکر.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2775" target="_blank">📅 19:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad Hasan</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atUw0J8mZevGx3SvwPEYBWDhy3vrzw2dbEAD9qjz6U-qS6lCpqIKdWi_3Wc8cbBMYn7QhsbQTjSK8LIHwsrqFm-rk9G3P1vCaCgn9YgpGPiCU1WRQQOR9qPFz9T80eqjeebd-GGtFj9ZIirQLV2-hkROk0co3BwldEiWsgHvqW2Fy4Qb80MUm9ywb5JxQeYbfbdvCBYxrogUSzZvBtSclCtNV0NotvgllEnkH7YpbiN_88FE2Fc45wS3lNVp8pdmAFp3MfUk2T7yoZRupvMP6eVeILkQEy00NIeMA3-VIAy_jXt8HBUXDYdnDqqqfp8V2InifZnuhnRAN8ZoIZrr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فروش ویژه اشتراک‌های هوش مصنوعی
🤖
✔️
فعال‌سازی سریع و مطمئن انواع اشتراک‌های پریمیوم:
🤖
ChatGPT Plus
🤖
Gemini AI Pro
🤖
Super Grok
😵
Cursor Pro
🤶
Claude Pro
👻
Kiro Ai Pro
⭐
Telegram Premium
📌
اکانت اختصاصی Gemini AI Pro یک‌ساله فقط: ۹۴۵ هزار تومان
❤️
اکانت اختصاصی ChatGPT همراه با ضمانت
کامل
⏱
فعال‌سازی سریع
🛡
همراه با ضمانت و پشتیبانی
🛍
جهت خرید همین الان ربات مارو استارت کن و خریدت را انجام بده.
💸
@SubMarketAi_bot
📢
Channel:
@SubMarket_IR</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2774" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgyCgX2ac6hufV7a6uR6BcJrqTNOy3G9AR8XQXZSQLlphdKuYma0yVdehmqziA8bKOCN939vNNGBmEUa239zQoxpF1ylySGqtCi9-ysujNLLOJtCeXvzM_Q5A5ejyjt7E_zIqD-_QC5_bOy9opRvqSgC1RyV_mahTbUPsHsCTwwbIRyL8h4F3sW_tGGbzB99PpSjU8V5WoDPWUIUEotVwFmEMzWbgtOfDa5BlHMiBrW6_9t9ZpaCeGWgk4LEoi7oHQw187k_i6WEESbafVjrR7NGfdnlH80FDrB3HulFZYs0FFhSrkNTEuPM0ywzuJnoDz6rMxoWsB8OnRIgpC8J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دور زدن رایگان فیلترینگ در ویندوز
با
UAC SNI Spoofer
🔹
اگه دنبال یه ابزار بی‌دردسر و قوی واسه ویندوز هستید، این برنامه که با هسته Xray و متد SNI Spoofing کار می‌کنه یه گزینه فوق‌العاده‌ست. این ابزار با مدیریت هوشمند مسیرها، بهترین و پایدارترین اتصال رو براتون ردیف می‌کنه.
⚙️
قابلیت‌های کلیدی برنامه:
📱
دارای حالت‌های اختصاصی همراه اول، ایرانسل و حالت هوشمند Auto.
🔍
تست و رتبه‌بندی خودکار SNIها و Edgeها برای پیدا کردن سریع‌ترین مسیر ارتباطی.
🚀
مجهز به سیستم شروع سریع TLS برای همراه اول و قابلیت «گرم‌سازی مسیر یوتیوب» برای پخش بدون بافر ویدیوها.
🔒
تنظیم خودکار پروکسی سیستم
🌐
با قابلیت App Bypass (عبور برنامه‌های دلخواه از پروکسی) و نمایش لاگ زنده.
🔻
برای کارهای حساس استفاده نکنید.
🔗
دانلود از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2773" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3PXs3KPGiXNyXDNHRKuJQD7LsDK30T8yj8NavqFmTuRkOw5Ec3VtmY22EvZ7S-YR3VmiTcmUC02Go314a6jJNuxZZMmjBcmqlLxWfI9wK4L-hiFKltJeZZn_EwsADPZRaSuaqEphAVL3tnVa1i50sux1NoBXQEJPqosyeT1TAIxaF7ubIkczE1ZE-rffozFediuGfg1JZDjCTgFCDY6LgUq3NUnZTQREIp_O6dE4eDoh6bhlddSMrQ-ZBMNEGqhHlgfQ0wkCsVd8Wt6IYYedGzjK4h0dNm7-Atwc9YI_0Vv9jMyvKbIJqj68jiSWe9q7C7pQoJV0Fo3lnZ7zeVKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
انتقال بی‌دردسر پنل 3x-ui بین سرورها با پروژه 3xui-mover
اگه تا حالا مجبور شدید پنل 3x-ui رو به یه سرور جدید منتقل کنید، حتماً می‌دونید که روش‌های سنتی (مثل کپی کردن پوشه‌های x-ui و cert) همیشه جواب نمیده؛ مخصوصاً اگه دیتابیس شما روی حالت PostgreSQL باشه، پنل تو سرور جدید بالا میاد ولی کاملاً خالیه!
⚙️
ویژگی‌های اصلی این ابزار:
🔸
پشتیبانی PostgreSQL و SQLite
🔹
بکاپ دیتابیس، تنظیمات و SSL
🔹
انتقال خودکار با SSH
✅
جلوگیری از ریستور اشتباه
🔸
بررسی صحت انتقال و لاگ کامل
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2772" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avf4px2Moi9VURrPju4fxsOwTfAeAy3J4b6u_n5DP9Vh0MXeSWWWuquqpaR9CfBghmQ0aDbBoSHQT1WyWXVXVuU4mM15pJ1TExQ6vyU2AfcaxoMka3Jv9NQA-hau24h-bXARP_wmzTtXhNIF79i8ogLhQq20OYyl9GmfdJGFHCwvIvueYyeQa8046NLbw_NjFqIqQhq7qQOiLP_r-QKK0ftK-90_3WOh-iGe0t3jQY_kosTKdnTPmtfLuxaMRH693XORpy4xaI8CylcmmYyfEDw5qPS1FV7Tmn24Lie4YpU_85in9cOgAUoFwmAz_k63oZm2AlABkHi2vMyikGJHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توجه! مراقب کلاهبرداریِ فروش پنل‌های رایگان باشید
دوستان عزیز، با توجه به پیام‌ها و درخواست‌های متعددی که از سمت شما دریافت کردم وظیفه خودم دونستم که یک اطلاع‌رسانی مهم در مورد سوءاستفاده‌های اخیر داشته باشم.
متاسفانه اخیراً دیده شده که عده‌ای افراد سودجو، پروژه‌های کاملاً رایگانِ دور زدن فیلترینگ که بر پایه ورکر کلودفلر ساخته شده‌ را به عنوان سرویس‌های پولی و اختصاصی به کاربران می‌فروشند!
ابزارها و پروژه‌هایی مثل:
👇🏻
پنل BPB
پنل نهان
پنل نوا و...
🔹
تمامی این روش‌ها توسط توسعه‌دهندگان به صورت
رایگان و متن‌باز
منتشر شده‌ تا همه بتوانند به سادگی به اینترنت آزاد دسترسی داشته باشند. فروش این پنل‌های رایگان نه تنها یک کار کاملاً غیراخلاقی است، بلکه سوءاستفاده مستقیم از عدم آگاهی کاربران و بی‌احترامی به زحمات سازندگان این پروژه‌هاست.
✍🏻
هدف ما از انتشار آموزش‌ها در این کانال دقیقاً همین است که یاد بگیرید خودتان به سادگی و به صورت کاملاً رایگان این ابزارها را راه‌اندازی کنید. هیچ دلیلی وجود نداره که بابت یک کد رایگانِ کلودفلر به کسی هزینه پرداخت کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2771" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVyyR-oh6sNxDjNUYxO79hRVfAl_fQao6Ke_T-7chY7U2Uq-dJGrCodSeGOYtjeL54P57jgpNOygAI8UYxELVD3N2fFH9HsJZQIjolsiwvGsNe8MakrTvjR3QM9vyRjQv7j00VZv-5AdmfU6wgfTbylFqp8d1T1gfuyGoofvEGgaF2zdWGh7IhXwhPHgCs90mZCi5h_SqWKdTj6cBSjafM-sWmkpBqFrBk6-i8VVitFZm2NsG-kwXClWf2QUkPdjEAxHMEzXSbUxSN5zC2_ZxttOiNizjdyC_s9OZtsEUniZLzS0xa-sZoWz0D5-9GnOIWlGh7Kwj7zD0T1bGDE50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازگشت بانک ملی به مدار اصلی؛ صادرات و تجارت هم به‌زودی
بانک ملی از امروز بالاخره به زیرساخت اصلی برگشت و سرویس‌هاش پایدار شد. بانک‌های صادرات و تجارت هم قرارِ ظرف چند روز آینده به این بستر اصلی منتقل بشن تا مشکل قطعی‌شون کلاً حل بشه.
این اختلالات طولانی‌مدت که از اواخر خرداد شروع شده بود، به خاطر حملات سایبری سنگین و پیچیده بود که تو این مدت با کُر پشتیبان مدیریت می‌شد. در ضمن بانک مرکزی اعلام کرده چک‌هایی که تو این مدت فقط به خاطر این خرابی‌های فنی پاس نشدن، هیچ تاثیر منفی روی رتبه اعتباری مشتری‌ها نمی‌ذارن.
💬
پ.ن:
البته با وجود این خبرها، هنوز یه سری از کاربرها میگن بعضی تراکنش‌ها مشکل داره. از اون طرف هم انگار کلاً بخش وام رو بستن؛ یعنی مردم این‌همه سپرده گذاشتن به امید وام، ولی حالا که می‌خوان اقدام کنن جلوی وام رو گرفتن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2769" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0bUucEP-iQ2EItEohRkNUzmdUokw_nZqNnHs8_yaDeB5BLHKpLF293NPWrRNWSivqgrzdn-bMcqDeiJRZOf1USvkEsueGarNS_4hb6z2M7B2R9WY3KrK280iClACh30NVsKwUtYHW5qh4C213FMXtd-PqBwGViaoSv7fqhUMPgRtrNItxIv5p8T5v0VRCIeCupu665ms8OFIXnK7JueJZg2Jg7Bba5ALet9fLf1S__kOO5pcsbvfBbLdzKjSuuF_sEz1nUvZHL8A4hY-CIEqfQRCsoYry8nXJPaOANFwW6F7JNZLXsXUhGY9cebSQenqiJEj2PdNph0mbgeUz2wcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دامنه t .me تلگرام دوباره برگشت
امروز دامنه معروف
t.me
(لینک‌های کوتاه تلگرام) ناگهان از کار افتاد! این دامنه توسط رجیستری کشور مونته‌نگرو به حالت تعلیق درآمده و از کل سیستم DNS جهانی پاک شده بود؛ آن هم در حالی که دامنه تا سال ۲۰۳۵ تمدید شده بود.
گزارش‌ها نشان می‌داد که این مسدودی به دلیل تحریم‌های وزارت خزانه‌داری آمریکا رخ داده بود.
🔻
این دامنه مجدداً
فعال و رفع مسدودیت شد
و اکنون تمامی لینک‌های کوتاه تلگرام بدون مشکل کار می‌کنند.
©️
Behrad Javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2768" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ0EmWKaRnxnaCQd19bsydroLX8zsJnPPakbtrhRuBh4aXodJnG1s9ZD6drhbK7UMd47FHiCX_tFEsFagAwqR9ohWeRSIfa1TkGViCnHpLPb7hF8z663Pyww22MjgBOcVBJ-49foUBcBP-a17mlPWW3mrZlWSyyOUzgl0rd7pHNpsl6oUSZlcPvRVUEh0a61RmKaQcQSXllPDyGW83T04XLViD_Xh790J1ZiH561hthnlOCrrXVwcU-Y9pGOiP34c-UUYwZh9oLqTW3nhHqjottWAfvc-6HFKfaL9nag6wylmO-7Y3mYQBV70nMcRGCrwRisg7rhccq7ZLuJdEp_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بعضی از بچه‌ها خبر دادن مثل اینکه کج‌دار و مریز
IPv6
روی یه سری از اپراتورها فعال شده. البته هنوز دقیق مشخص نیست که این داستان موقتی و بخاطر اختلالات شبکه‌ست، یا اینکه واقعاً خبریه و دارن یه کارهایی انجام می‌دن.
🔻
از اون طرف هم عده‌ ای از دوستان از جنوب کشور پیام دادن و گفتن که اوضاع اینترنتشون خوب نیست و قطعی و اختلال شدیدی رو دارن تجربه می‌کنن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2767" target="_blank">📅 13:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuSagUooUc7Ux7GBummxm_0rjDSdjURJLDd9Jeu7P2yxxcarAdJ9tCMxIW93oaLxVmfBZlNBh_AR3aFneVvZSF9cQUN029IQ5Sc-GJRxFJdPy8iace_Xq5SRTa4IoAW76eZO2hAxJ0WlTi3osaYn3MS-_Zw6EIdxr5vKjwaikeK7QFLZWHRWydlA9QNK6XA5r7H3P9GyFQTMhfJx1Hn-quJGglCr8AQQVAM3vj74MU5esPKvYtOw8cThn1R6kSy29JXnJL-Llzob5SGaYt8k97gZDh5S8ZWxVi_ep4E3ShomS1CiwKbYO03pF3jlre1Nbt4sCxHma_GFfz6nVByKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل معکوس با انواع پروتکل (BackPack)
🚀
🔹
در این ویدیو به آموزش صفر تا صد راه‌اندازی تانل معکوس (Reverse Tunnel) بین سرور ایران و خارج می‌پردازیم. اگه به دنبال روشی هستید که ترافیک شما را شبیه به وب‌گردی عادی کند و کمترین ردپا را برای سیستم‌های محدودکننده به جا بگذارد، این آموزش دقیقاً برای شماست.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/iaghapour/2765" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">متاسفانه به بیشتر از ۱۰ نقطه از کشور حمله شده که بیشترینش سهم بوشهر عزیز بوده.
💔
شاید خیلیا در نگاه اول بگن خب مناطق نظامی بوده و به مردم عادی آسیبی نرسیده، ولی واقعیت اینه که پشت پرده یه اتفاقایی می‌فته که آدم تعجب میکنه از شنیدنش!
مثلاً امروز یکی از بچه‌ها می‌گفت توی شرایط جنگی، حتی اگه اینترنت هم قطع نشه، کلی از فروش‌های ما کنسل می‌شه؛ چون مشتری می‌ترسه و فکر می‌کنه مثلاً ما که از جنوب آنلاین‌شاپ داریم، دیگه نمی‌تونیم بار رو برسونیم تهران یا شهرهای دیگه...
خلاصه که فقط بحث قطعی اینترنت نیست که به کسب‌وکارها ضربه می‌زنه، خود جنگ، ترس از خرید و این ریسک‌ها هم کلی به مردم آسیب می‌رسونه.
دمتون گرم تا جایی که می‌تونید از این کسب‌وکارهای بومی حمایت کنید. قبل از اینکه نگران بشید و عقب بکشید، اول با پشتیبانیشون هماهنگ کنید؛ چون توی خیلی از همین شهرها و استان‌ها پست و تیپاکس دارن مثل قبل کارشون رو انجام می‌دن و جابه‌جایی بار بسته‌ نشده. پس با خیال راحت می‌تونید از این آنلاین‌شاپ‌ها و سایت‌هایی که توی این مناطق هستن خرید کنید.
🤝
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/iaghapour/2764" target="_blank">📅 16:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2762" target="_blank">📅 21:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام بچه‌ها. یه مدتیه دوست دارم واسه تشکر از اینکه هم تو یوتیوب هم تلگرام کنار ما هستید، ماهی چند بار یه هدیه کوچیک بهتون بدم.
👇🏻
به نظرتون چی باشه بهتره؟
🔹
اکانت هوش مصنوعی
🔸
کانفیگ فیلترشکن
🔹
پول به صورت کریپتو؟
البته این وسط دوباره درگیری‌ها زیاد شده و فقط امیدوارم باز قطعی اینترنت شروع نشه که تمام انرژی و وقتمون رو بگیره :(</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/iaghapour/2761" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2760" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❓
سوال یکی از کاربران:
من یه سرور دارم رو همراه اول فوق‌العاده عالی کار می‌کنه اما رو ایرانسل نه. چطوری می‌تونم بفهمم مشکلم از کجاست؟
💡
پاسخ و بررسی مشکل:
دلیل اصلی این اتفاق برمی‌گرده به تفاوت سیستم‌های فیلترینگ (DPI) اپراتورها. تجهیزات و محدودیت‌هایی که هر اپراتور اعمال می‌کنه با بقیه فرق داره؛ در نتیجه یه کانفیگ یا پروتکل خاص ممکنه روی همراه اول عالی باشه، اما روی ایرانسل اختلال داشته باشه یا اصلاً وصل نشه.
به جز این مورد، چند تا دلیل مهم دیگه هم وجود داره که باعث این مشکل می‌شه:
👇🏻
📌
وضعیت آی‌پی سرور:
خیلی وقت‌ها آی‌پی یه سرور روی یک اپراتور خاص شناسایی و محدود (کثیف) می‌شه، در حالی که همون آی‌پی روی اپراتور دیگه کاملاً تمیزه و عالی کار می‌کنه.
📌
مسیریابی شبکه (Routing):
مسیر اینترنتی که شبکه ایرانسل تا دیتاسنترِ سرور شما طی می‌کنه، ممکنه با مسیر همراه اول متفاوت باشه. گاهی شبکه یه اپراتور با یه دیتاسنتر خارجی به مشکل می‌خوره و باعث افت سرعت شدید یا پکت‌لاست می‌شه.
📌
حساسیت روی SNI و دامنه:
الگوریتم‌های تشخیص ترافیک اپراتورها با هم متفاوته. ممکنه ایرانسل روی دامنه یا SNI خاصی که برای کانفیگ استفاده می‌کنید حساس شده باشه و ارتباط رو همون اول قطع کنه.
📌
آی‌پی تمیز و شبکه توزیع محتوا (CDN):
اگه ترافیک سرورتون رو از پشت کلودفلر عبور می‌دید، احتمال خیلی زیاد اون آی‌پی تمیزی که ست کردید روی ایرانسل محدود و کند شده، ولی روی همراه اول هنوز جوابه. تو این حالت معمولاً با اسکن کردن و جایگزین کردن یه آی‌پی تمیز جدید مخصوص همون اپراتور، مشکل حل می‌شه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2758" target="_blank">📅 21:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قشنگ 2 ساعت با خودم درگیر بودم تا بالاخره حسش بیاد بشینم پای سیستم و کارای خودم رو انجام بدم. تا اومدم استارت بزنم، برقا رفت.
😁
دوباره این داستان قطعی برقا شروع شد. رسماً دهن سیستم و وسایل برقی خونه سرویس شد رفت!
🥲</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/2757" target="_blank">📅 21:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c87H37YcWoKZVQAKrRasdjfGw6j-sBHKbiGnDGSqBH0hExDUQOh45OhmZ_-mNvDkK1enoE4u7r-p1l0E9dW-uxzhKTRAYkPT2QFa2XW9e44fuJoR_kcu4oNO5aHNY7pinjm2B-O4X0rahaquBDgRCjRvZNJI_en1EOgeg3C-35z9lkIWU5XR2dnmwXfr1Zm9uu71B2brWCQpIAvT_zofFZ6xwCg15JqXGvRQLoDVLwmZicEOW8S7piLw-W92RMlCPOTqE_dutTDcltEb5D_rJ8KNIfEy8RMtdmk16bl7SfUkHsAWZYvlpkm-hgM25ocvZWHAj_RCKpRsOcMfKfHzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
دلایل ناکارآمدی و خطرات قطع اینترنت برای امنیت سایبری
🔹
توقف به‌روزرسانی‌ها:
آپدیت‌های امنیتی سیستم‌عامل‌ها و آنتی‌ویروس‌ها قطع شده و دستگاه‌ها در برابر هکرها کاملاً بی‌دفاع می‌مانند.
🦠
رشد بدافزارها:
محدودیت‌ها باعث می‌شود کاربران به سمت نصب VPNها و پروکسی‌های ناامن و آلوده سوق پیدا کنند.
🛡
بی‌اثری روی حملات بزرگ:
حملات سایبری پیچیده (مثل استاکس‌نت) معمولاً روی شبکه‌های ایزوله انجام می‌شوند؛ بنابراین قطع اینترنت جلوی آن‌ها را نمی‌گیرد.
🔌
اختلال در اینترنت اشیا (IoT):
دستگاه‌های متصل و هوشمند به دلیل قطعی ارتباط با سرورهای اصالت‌سنجی، از کار می‌افتند یا ناامن می‌شوند.
📉
بحران اقتصادی و اجتماعی:
قطع طولانی‌مدت اینترنت، زندگی و اقتصاد مردم را فلج می‌کند که این موضوع خودش یک تهدید بزرگ برای امنیت ملی است.
⚠️
خطر اینترنت طبقاتی:
تخصیص اینترنت فقط به عده‌ای خاص، باعث ایجاد شکاف در جامعه، می‌شود.
💡
نتیجه‌گیری:
به جای قطع دسترسی مردم، باید امنیت سایبری شبکه‌ها را تقویت کرد و در سیاست‌های فعلی مدیریت اینترنت تجدیدنظر اساسی انجام داد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2756" target="_blank">📅 15:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2755" target="_blank">📅 01:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEXASA6uOdcEi0pNUkHeV6BJQ8LL5k8Ojow3VDmoBdxROZeZAHTF_GP_CvKQuOQQ7UggLO_JuLSt4TTZm3qppVR6fOdhKjnFyE_3Ti_gYaYaU0iUm96XwYuewGiG4DMz0RKfmv0WRFeyK2GvucZIMlg3ILYx42fOFShazutm8ifr1Lbm_-XBY_8UCRsHDP7jyjQXo1T7oNEb4cSgG-NX85sLCEgaNkdi7o3skjl7DogKp5yO_8_-u6s4UCmz210c_lrs-Vg8l9BTdSrkL6dG0zJG1AOkhln765UfxrWJ1yPufvS_uYmLMsfZ1b98aCHaejbsd4HCzT87jQo67loyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
قهرمان گمنام دنیای ویدیو؛ چرا VLC هیچ‌وقت پولی و تبلیغاتی نشد؟
🔹
بیشتر از ۲۰ ساله که پلیر محبوب VLC هر فرمت و فایلی که بهش دادیم رو بدون حتی یک ثانیه تبلیغ پخش کرده! دلیل این اتفاق شگفت‌انگیز، شخصی است به نام Jean-Baptiste Kempf که از سال ۲۰۰۳ به این پروژه پیوست.
با وجود اینکه VLC تا حالا بیشتر از 10 میلیارد بار دانلود شده، او پیشنهادهای تبلیغاتی چند میلیون یورویی رو قاطعانه رد کرد تا این برنامه برای همیشه کاملاً رایگان و بدون تبلیغ باقی بمونه.
🔸
اما شاهکار این افراد فقط به ساخت نرم‌افزار VLC ختم نمیشه! در واقع، تقریباً هر جایی از اینترنت که ما در حال تماشای ویدیو هستیم، روی پایه تکنولوژی همین تیم استوار شده است.
انکودر معروف
x264
که سال‌ها استاندارد اصلی پخش ویدیو در وب بوده و همچنین دیکودر
dav1d
برای فرمت جدید و بهینه‌ی **AV1**، دقیقاً دست‌پخت همین تیم و جامعه متن‌باز (Open-Source) است. غول‌های فناوری مثل یوتیوب، نتفلیکس و تمام مرورگرهای مدرنی که امروز استفاده می‌کنیم، همگی در حال استفاده از همین تکنولوژی‌ها هستند.
©️
behrad javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2754" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
نوا کلاینت (Nova Client) منتشر شد!
از همین حالا می‌تونید کلاینت بهینه‌شده، و قدرتمند پروکسی رو با رابط کاربری اختصاصی «نوا» روی تمام دستگاه‌هاتون نصب کنید.
✨
برخی از قابلیت‌های کلیدی:
🔸
ظاهر مدرن و Dark-first:
طراحی چشم‌نواز با زبان بصری نوا و گرادیان‌های نئونی اختصاصی.
🔹
رادار نوا (Nova Radar):
اسکنر فوق‌پیشرفته و یکپارچه برای پیدا کردن سریع آی‌پی‌های تمیز کلاودفلر.
🔸
پشتیبانی کامل از زبان‌ها:
سازگاری بی‌نقص با زبان‌های فارسی و انگلیسی به‌صورت کاملاً راست‌چین (RTL).
🔹
مدیریت هوشمند:
دسترسی به داشبورد زنده، روتینگ، مدیریت پروفایل‌ها و سابسکریپشن‌ها.
🔸
قدرت‌گرفته از Flutter:
فوق‌العاده سریع، سبک و هماهنگ روی تمام پلتفرم‌ها (Multi-platform).
📥
لینک‌های دانلود (نسخه v1.0.0-beta):
🖥
macOS (Apple Silicon)
:
Nova-macOS-arm64.dmg
🪟
Windows
:
Nova-Windows.zip
📱
Android
nova-client.apk
🍎
iOS / iPadOS
TestFlight
🌐
وبسایت رسمی
📦
گیت‌هاب پروژه
نکته مهم برای macOS:
اگر سیستم بلاک کرد، این دستور رو در ترمینال اجرا کنید:
xattr -dr com.apple.quarantine /Applications/
Nova.app
👈🏻
نکته: Nova Client در واقع یک فورک بهینه‌شده از Karing هست که کاملاً با طراحی Nova Proxy هماهنگ شده و رادار قدرتمندش هم داخلش ادغام شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2752" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3GQ33s7S_gtVsVo8_yEUM929n5KjKP2mCg94dKNYg2exVWqPMxcu5x2kifUxspmPBNxjh9OHTSCw7qpF3Qs4pPRvwLb0s6vfYLf-Pqbl8YyLLOWrRvyOpWhIX1hKhlKdwFWtBAmhqA5v1A8jUsFjFUbA8ER7wqFMmApzlZNL3NtPCbo7SmZMaUqw_-Cvy9ZdtLgpuqjskFDhsbaKQAsX0j3MmwqgV-F9dQ8TkXyZidCh59L8ypw75MuQnOrpD2xxbUmcWOg-uQFNJzpjlvuiX4SN-7Lq5Md0-SVhzTGfQZzn_94p_ITryXF8afaFVM1-LVtdh8aMaaTBG4vUv2kAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بعضی افراد میدونن این چیه
😊</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/iaghapour/2751" target="_blank">📅 19:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/iaghapour/2749" target="_blank">📅 20:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg9IcjSNvspMTSwTrrZqvT41-3mt-a-MJ8SkgN6dz2DWCQcp5DhVzrE_JjsVk7i2shtGpqlI8WsEIZy3FSLOeYFwMpnmHEO1gfZoUwjUFIno5cO_1IjTo3s7UtW7oPCWErApr3d9WFummFCobTiXOoBfhDlxpuzwebiU2RyBWG0_7uQae1SYwGaeB4G_vVdFvlcMwt8KaFJUKEyRnRwRLADPsfmlwaZXoqMBY4P6nKL-mf3-Iiey7QWNReTOmW5GyR99z-t-PCGMv6h96cInDxYY7jdCZ_nYerPGYcp5O2T15itAlZkRtStT9N_UpXSDqLZcs6Zx-3tYS60IFWoFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مسدود شدن ناگهانی پنل‌های رایگان روی کلادفلر
گزارش‌های متعددی از کاربران دریافت کرده‌ایم مبنی بر اینکه پنل‌های رایگان (مانند نووا و BPB) به‌طور ناگهانی بن شدن.
سر اینکه چرا این اتفاق افتاده دو تا بحث هست؛ یه عده میگن خیلیا از قصد رفتن این پنل‌ها رو به کلادفلر ریپورت کردن تا بسته بشن. یه عده هم میگن نه، خود سیستم هوشمند کلادفلر تشخیص داده و بن کرده. خلاصه دلیلش هر چی که هست، تو استفاده از این ابزارها همیشه ریسک بسته شدن وجود داره.
💡
یه توصیه خیلی مهم:
بچه‌ها، واسه ساخت و راه‌اندازی این پنل‌ها اصلاً و ابداً از اکانت و ایمیل اصلی خودتون استفاده نکنید! همیشه یه حساب فرعی بسازید و با اون کارتون رو راه بندازید.
🔄
آپدیت جدید پنل نووا (Nova):
توسعه‌دهنده پروژه نووا خبر داده که کدهای این پنل رو دوباره بازنویسی کرده و تو آپدیت جدید، مشکل ارورهای مختلف (مثل همون ارور رو اعصاب 1101) کلاً برطرف شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/iaghapour/2748" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2747" target="_blank">📅 18:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک تشکر ویژه از همراهان همیشگی
🌺
دوست داشتم از این فرصت استفاده کنم و از تمام کسانی که تو این مدت اخیر که درگیر محدودیت‌های شدید اینترنت بودیم، به هر شکلی پشت ما ایستادند و کمک کردند، از صمیم قلب تشکر کنم. حمایت‌های شما باعث شد تا تیم ما بتونه هر کاری که از دستش برمیاد رو در این رابطه انجام بده.
از دوستانی که کانفیگ‌ در اختیار ما قرار دادن، تا عزیزانی که اکانت سایت‌های مختلف از سرویس‌های هاستینگ گرفته تا ابزارهای هوش مصنوعی و... رو به دست ما رسوندن تا کارها لنگ نمونه؛ واقعاً ازتون ممنونم.
و یک تشکر ویژه از دوستانی که با کامنت‌هاشون و دفاع از کار ما در گروه‌ها، سنگ تمام گذاشتند و بزرگ‌ترین حمایت رو از ما کردند.
خیلی دلم می‌خواست اسم تک‌تک شما عزیزان رو اینجا بیارم و شخصاً قدردانی کنم، اما به دلایل مشخص و برای اینکه برای خودتون بهتر و امن‌تره، از این کار صرف‌نظر می‌کنم. ولی بدونید که تک‌تک کمک‌های شما برای ما ارزشمنده.
دقیقاً تو همین زمان‌های سخت و بحرانیه که باید کنار هم باشیم و بدون هیچ چشم‌داشتی به همدیگه کمک کنیم تا از این شرایط عبور کنیم. (البته بماند که در این میون، کانفیگ‌های میلیونی هم به پست ما خورد که خب... بگذریم!
😄
)
امیدوارم دیگه در هیچ زمانی دچار مشکلاتی شبیه به این نشیم و روزهای بدون محدودیتی رو پیش رو داشته باشیم.
دم همتون گرم!
✌️
💚</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2746" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gop38LN9j-oxMIMKjf-xhrK6L39zhP9RqotXyrueX1BdHplvXatcqcTSWQDal_3FbLy5vNGlviM7TDaoCEUL5G__x-ZlLC-m9ZppLqGe38Y06xyyXRdSBvLD9URTtVFmz14JvYrnuSvZ_EVWn0O7WhYeLhwnuukFITGuwi9XIrBi3I-c5C0_FtcwQ_WCcJi-AuHGLU6RKdfDgZzS2CsfJ2e6V2LggSjosR6vq7gESCTb7aIYBcy0rqz0wFoerodL5NkUEOO0rwwO3l71LCqfk2e9B0uS_CVfrzz8NEb5TudCV00bIvThrp7ceSq-bOkuwwGx8HRDIqY6mqKNglqinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن سالم کار می‌کنن هم به چشم دزد نگاه کنه.
اگه خرج سرور و هزینه‌ها بالا رفته، خیلی روراست قیمت‌ها رو ببرید بالا. مشتری ترجیح میده گرون‌تر بخره ولی بدونه دقیقاً داره بابت چی پول میده، تا اینکه یواشکی از حجمش دزدیده بشه.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2744" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4GyKkRTYazB0CUXp999q3vVgeUuOOD9V_QMOPGP-NN-d-_H3Hy15A0M5f2DFUmEgy5ituE6jWr009tN2ftD7LCajGwXhkFt6tn7-9MzxnxUEFV1RoZjrlooa5LNgLDmDV9m5BckUjOuAgdlOZyCtywjRzBttcE_LvZr5x8OklAfHgIIo4yCxDJqRJK14WKgu0c8x5S3-BF7xjccujmwKvbDKjxhrGoAZMCjDrH5I9JJ1arIiKf7Kqk2ue5DpqA55JV3yHB1cmIhNAYA_OzTI2zA8TUF_PSB06npeIiakH70m5_-7tuEqjBfYYjMuv22L9gBXkqtyEWoiSK_lQuX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.11.0 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
-
🛡
پنل ادمین با مدیریت کامل یوزر ها و چت ها
-
👑
رول owner برای بالاترین سطح دسترسی
-
⚔️
رول admin برای دسترسی محدود به پنل ادمین
-
⚙️
دسترسی به تنطیمات برنامه از طریق پنل ادمین
-
📋
بخش لاگ برای مانیتور از چند منبع مختلف
-
👤
ساخت یا ادیت یوزر از طریق پنل ادمین
-
💬
پاک کردن کل پیام ها یا ریست کامل دیتابیس از طریق پنل ادمین
-
📖
وبسایت ویکی سانگبرد در
docs.songbird.website
-
🕑
نشان دادن آخرین بازدید کاربران
-
📡
انتخاب Songbird به عنوان سورس Remote channel
-
💨
بهبود عملکرد قابلیت Remote channel
-
🔧
رفع باگ های گزارش شده
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/iaghapour/2743" target="_blank">📅 20:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX606h7sz7xHJXYEdOz8OWLMUMMowWZfHgViFRTDu6DBxYq4On0uFWdOFUCtgeM3CjyGczbaEdnXFfSaoKvT9wQ2c2rXPbAqf8PkeaZ1p4ddKJz32LP5XBXfXqFjm0JD_KpCWjM1exeaVSBVclRd1gwzvagOmqqq5k1vOW5F5Ad3CMn_HumMt0yQFblFEgiFrb6LR00AAi6O5PoatIkrGPh5o_5XhoCg-1pnrVVQINVfDzFfHCKjQjUTZSOeQWBVEfEi2J9wjqRV1hwZDSS61TYbOjj8WiRE4K8FKsR_uSr29MvujTN4LSALrzgz3oQCti682I6ynOk_Z6p6miOsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قابلیت جدید گوگل سرچ کنسول: ردیابی دقیق ترافیک شبکه‌های اجتماعی
گوگل ابزار جدیدی به نام Platform Properties را به سرچ کنسول اضافه کرده است که امکان ردیابی ترافیک ورودی به شبکه‌های اجتماعی از طریق نتایج جستجو را فراهم می‌کند. با این قابلیت کاربردی، می‌توانید دقیقاً متوجه شوید مخاطبان با جستجوی چه کلماتی به ویدیوهای یوتوب یا سایر شبکه‌های اجتماعی شما (مثل ایکس، اینستاگرام و تیک‌تاک) رسیده‌اند.
این ابزار سه گزارش جامع ارائه می‌دهد؛ گزارش عملکرد برای نمایش دقیق کلیک‌ها و میزان بازدید، گزارش اینسایت برای شناسایی پست‌های موفق و تحلیل روند ترافیک، و بخش دستاوردها برای ثبت رکوردهای جدید و پیگیری رشد کانال. برای راه‌اندازی این سیستم، کافی است در سرچ کنسول یک ویژگی جدید (Add property) ایجاد کرده و پس از انتخاب پلتفرم هدف، مراحل تأیید هویت را طی کنید. این آپدیت طی هفته‌های آینده فعال می‌شود و یک امکان فوق‌العاده برای تحلیل دقیق‌تر بازخورد ویدیوهای آموزشی و مدیریت سئوی محتوای شما خواهد بود.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/iaghapour/2742" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzodN5GPiV1s8u_b1WH5J07ro1CzdT08RdlSLDnETfwMFJSMRJ5Q2JiRChoswl053-kpZ7Q6aasUFt_fv41oD8Duk7luV2LAtBi6rpkSQMDjCf_6PAq4mW5meO_ntGph-cXYBpMGM-hIuKelKpvtetoln-578X-zzHkDbgsgsQWBvm4nDif26gWrBqeFskJRBR5zgZS1h1xUqE4DVWzPjYFLZpekWfin0itajuuu5-EWhKAyMPcuxQLTsmXK34djiFgl0xYL6CN98360kFzWykU-FNgj-_20V8gf3P7WacipHJtcXWZx1TO70hv-yKFE7pO5z9rc4go0YLzvPnHaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اعتراض ۱۱۵ هزار نفری به سونی؛ دیسک‌های فیزیکی را حذف نکنید!
یک خرده‌فروش کانادایی (PNP Games) کمپینی با نام «Don't Kill the Disc» به راه انداخته که تاکنون بیش از ۱۱۵ هزار امضا برای توقف برنامه جدید سونی جمع‌آوری کرده است. سونی قصد دارد تا سال ۲۰۲۸ درایو نوری را به طور کامل از کنسول‌های پلی‌استیشن حذف کند.
🔹
جزئیات این ماجرا:
🔸
نگرانی معترضان:
به گفته راه‌اندازان این کارزار، حذف دیسک‌های فیزیکی به معنای نابودی کامل زنجیره‌ای از مشاغل (خرده‌فروشان، توزیع‌کنندگان و تولیدکنندگان)، از بین رفتن بازار بازی‌های دست‌دوم و نادیده گرفتن جامعه کلکسیونرها است.
🔸
دلیل سونی برای این تصمیم:
همسویی با ترجیحات کاربران و رشد خیره‌کننده فروش دیجیتال. آمارها نشان می‌دهد سهم فروش دیجیتال بازی‌ها از ۱۳ درصد در سال ۲۰۱۳ به حدود ۸۰ درصد در سال ۲۰۲۵ رسیده است.
🔸
نظر تحلیلگران:
به دلیل سودآوری بسیار بالاتر فروش دیجیتال و کاهش هزینه‌های تولید سخت‌افزار برای سونی، کارشناسان اقتصادی احتمال تغییر موضع این شرکت را با وجود این اعتراضات گسترده، بسیار اندک می‌دانند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2740" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🟢
دوستان عزیز، همون‌طور که قبلاً هم اشاره کردم، کامنت‌های یوتیوب به دلیل جلوگیری از اسپم، به‌صورت دستی تایید میشن. چند ماه پیش یه عده شروع به فرستادن پیام‌های اسپم و نامربوط زیر ویدیوها کردن و برای اینکه مشکلی برای کانال پیش نیاد، مجبور شدم تایید کامنت‌ها رو دستی کنم.
تا الان پیام‌ها هر ۲۴ تا ۴۸ ساعت بررسی می‌شدن، اما از این به بعد
هر شب
کامنت‌ها رو بررسی و تایید می‌کنم. البته در تلاشیم تا راهی پیدا کنیم که این محدودیت به‌زودی کمتر بشه. از درک و همراهی همیشگی شما ممنونم.
💚</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2739" target="_blank">📅 19:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B41Jj21-EwYYywBuA2ZTp7tKoK6aef54e6xIjvbMOrcuYzAVU7z-llSVGG5DXoMIJo1kjmhh0LEFq31qcn1rELICJ-gwMkXjiBMLhXfPuAbX7_CpuZARTT6lSKa2sn6TPTuv6N1Q8ZW5GRT3Vj0zouUjt9qtOTyo-EovAptC4DhQ9h6rE8pNxS3nkj31Lzt8JuLFGjzKs30ulPUmsmq5YbToWDt3SBSdafSSBSlVxJIEq3DGfcPW8dVjhtSPn90jcWGaBTiefoERFBZtk4LLBnmq2yFp7LHIjlIJ7J2HAdJPaJq9q7uoMNTcCOeR8Ee3SWErqUffHNPsuE5BhGm_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استفاده پنهانی گوگل از عکس‌ها و ویدیوهای شما برای آموزش هوش مصنوعی!
گوگل به‌تازگی تنظیمات حریم خصوصی خود را تغییر داده است. با این تغییر، فایل‌های صوتی، تصاویر و ویدیوهایی که در سرویس‌های مختلف گوگل (مثل جستجو، مپس، ترنسلیت و...) آپلود می‌کنید، ممکن است برای آموزش مدل‌های هوش مصنوعی این شرکت استفاده شوند.
🔹
چگونه این قابلیت را متوقف کنیم؟
خوشبختانه امکان مسدود کردن این دسترسی وجود دارد. برای جلوگیری از استفاده شدن داده‌هایتان مراحل زیر را طی کنید:
۱. در تنظیمات حساب کاربری گوگل خود به بخش
Search Services History
بروید.
۲. تیک گزینه
Save Media
را بردارید.
۳. در همین بخش می‌توانید کل سابقه جستجو را غیرفعال کنید یا یک زمان مشخص برای حذف خودکار (Auto-delete) اطلاعات تعیین کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2738" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGo-ZYxsfZUwJKeXerShzoq4W_FtPjrOV8ND2MnLfv0EdHUdfMzjY_Y06AEyOVUugvJOJFR8uBzFjpg-5LnSrVxuAGR4BiNoeZG09vZOmPWi4Q0AZV_tTJibuzTTojQwYsnnVn3jI9JTX8meCOPse8DqWtEtKkwO0e-eVHFJ6XnxtBZSd-Es9Qc5VKDsrlVc0pX2xUIFlFd9Z-wjKmB8lY5wBMszyw7JiFLkK7rGyZiMM5mu5npwyDBgjknR9EpvyTJCQVMbNy4zNuSVvTM6sEf2Yy-hZNkc2TPRkASnqOuBPq1Aw1inZafqlCw00XdZLe3FES55ioXAgrk18SEcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
معرفی پروژه Iran Dev Tools؛ حل مشکلات در سروهای ایران
قطعاً به عنوان یک توسعه‌دهنده بارها با چالش تحریم‌ها، فیلترینگ و سرعت پایین دانلود پکیج‌ها و دپندرسی‌ها دست‌وپنجه نرم کرده‌اید. پروژه متن‌باز Iran Dev Tools مجموعه‌ای از اسکریپت‌های هوشمند و مستقل است که دقیقاً برای حل همین مشکلات تکراری برنامه‌نویسان روی اینترنت ایران طراحی شده است.
🔸
منوی مدیریت یکپارچه لینوکس:
شامل اسکریپت نصب Docker به همراه تنظیم خودکار میرورهای رجیستری ایرانی برای دور زدن تحریم‌های داکر.
🔸
بنچمارک و تغییر هوشمند DNS و میرور APT:
تست زنده و تنظیم سریع‌ترین DNSها و مخازن سیستمی (APT) لینوکس بر اساس کیفیت شبکه شما.
🔸
تنظیم خودکار میرورهای برنامه‌نویسی:
شناسایی و ست کردن بهترین میرورها برای پکیج‌منیجرهای محبوب از جمله
npm
،
pip
،
Go
،
Composer
و
NuGet
تا با بالاترین سرعت ممکن پروژه‌های خود را توسعه دهید.
🔗
لینک ریپازیتوری پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/2736" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5WNGyE0heirE6_isnsEJTyjbKWzwXhYAi7Q7DyZo8o_7a4IA-y-Kcz8SNzenFvxUiZfQ1gNedilIO57EnwsUiaEUT158Yf7peVcW4UIaDy6_8zMzDL3zmJjJApEDdsIQ4XQAVvlGYvRqQvMw2aXjBtwjq5Sl2RLOrWT3pso-xOlZoUnBdMmaRQFvRdCfBn8_5OKd1XKW3rsXDSynvd6u060PmaJNxITjN7MUlUP9SqJZTUfgl1Y1EhEQtHgfsSdHvKAJV8Q78taEQULlUDirBfXWsd8QwpW6AY5O4v3ZxohWZ4GB6Ggylum1C5LueQGr7za1K0F2wBvBu11m27jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی (GRoute)؛ کلاینت سبک و مدرن اندروید برای عبور از فیلترینگ
جی‌روت یک کلاینت فوق‌العاده سبک و روان برای اندروید است که بر پایه
Xray-core
ساخته شده و با ظاهر شیک و مینیمال اتصال به اینترنت آزاد را بسیار ساده‌تر کرده است.
🔹
ویژگی‌های کلیدی کلاینت GRoute:
🔸
پشتیبانی از پروتکل‌های مدرن:
سازگاری کامل با VLESS، VMess، Trojan و Shadowsocks در کنار ترنسپورت‌های پیشرفته‌ای مثل REALITY و TLS.
🔸
ابزارهای پیشرفته عبور از فیلترینگ:
مجهز به قابلیت
فرگمنت (Fragment)
برای دور زدن مسدودسازی SNI، سیستم Sniffing و مسیریابی تفکیکی (اتصال مستقیم سایت‌های ایرانی).
🔸
مدیریت ساب‌سکریپشن و وارپ:
به‌روزرسانی خودکار لینک‌های ساب، نمایش حجم و تاریخ انقضای اکانت، به همراه امکان ساخت کانفیگ
WARP کلودفلر
تنها با یک کلیک.
🔸
اسکنر اختصاصی IP تمیز:
اسکن رنج‌های کلادفلر و پیدا کردن کم‌پینگ‌ترین آی‌پی‌ها برای شخصی‌سازی سرورها.
💡
پ.ن:
در حال حاضر فقط نسخه
اندروید
این برنامه منتشر شده است، اما نسخه
ویندوز
آن نیز به‌زودی عرضه خواهد شد.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2735" target="_blank">📅 20:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxgG_9UHbxWlsKUQDqBgUsa3I04KzCVc6Ij-REjYDUcXdiTRhJnuTMQzcesQsx7bZNXhL81yfBJFyvw3pe6qYfBHKXMc4cpHOQ5WUNeiqMYv1Usz6Md_HAKufppeDmm2jxQDxt6HoKt6d2cIzwoVU8T9hwFazdx5ykg-y_96ZlFon3kveUA3lgwD-m47xS8Kqzr7jVyV4NtxPsBbiIsloJju70nAWklqv_bb9K54qSsyQ5hTf-vqQ8ynHfb4oo3PLQ-c4Pv2tNoDSEMXa2f_IMKFWmJpFHYLQar5FGvrsB0FBxhME7ioXZvruEqLCZf0Kvi5hdivSVPejvYEotN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون دانش فنی فیلترشکن شخصی و رایگان بساز! (با یک کلیک)
🚀
🔹
تو این ویدیو قراره یه روش فوق‌العاده راحت رو بهتون معرفی کنم که بدون نیاز به دانش شبکه و بدون سرور مجازی، بتونید فقط با یک کلیک و تو کمتر از ۵ دقیقه یه فیلترشکن شخصی، کاملاً رایگان، پرسرعت با قابلیت تعویض لوکیشن و ایجاد کاربر با محدودیت برای خودتون بسازید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#ورکر
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/iaghapour/2733" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚠️
آقا این همراه اول قشنگ داره عجیب‌غریب حجم می‌خوره! اول که اومدن نصف بسته‌های خوبشون رو حذف کردن که مجبور بشیم بسته‌های گرون‌تر بخریم. بعدش هم برای تست یه بسته ۶ گیگی خریدم؛ منی که بیشتر از وای‌فای استفاده میکنم و ۶ گیگ برام ۱۰ روز کار می‌کنه، چشم باز کردم دیدم بعد دو روز پیام اومده بسته‌تون تموم شد!
توییتر رو که نگاه می‌کنی همه دارن از همین دزدی و حجم‌خوری شکایت می‌کنن. ایرانسل و رایتل هم همین‌طورین یا فقط اینا این‌جوری دست‌شون تو جیب مردمه...!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/iaghapour/2731" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qavHDxVnZ2svSXmi-MbspuksVNz_mKc-mHhXGCemGZgW5ZriZafdOkQY5Yx_RdpkoRxonjYC6CRCWt4xojq9lDKjXB5oSaAWqvX6Em0eJwt9iJ-mRqsfviF9Dk6RpSz2J1cpSjpesw-qMVEvuZ2PAHEjh-2mZhHs5EbyW3KHjc30ngWuVQBpIOPHaz-bVn5b2DkzEN7SpFatx8yTQHjIArv8Fd-DKuSDpH0CJ5-66gr7wr6WogGg9zFLXoL6TKbO4OMv9elQ9ZNisrE_dJU1p4ZCnH8_gIrsbGSAgcNwNwuE3UM64XLF5CEnHydq7DdfOtj9mneEx27FZN2qxtdsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ری‌برندینگ بزرگ سایفون؛ ظاهر کاملاً جدید و بهبود دور زدن فیلترینگ
سایفون (Psiphon) پس از سال‌ها دست به یک تغییر هویت بصری و ری‌برندینگ اساسی زده است. ظاهر قدیمی و سنتی این اپلیکیشن جای خود را به یک طراحی بسیار مدرن، مینیمال و شیک داده است.
🔹
مهم‌ترین تغییرات در نسخه جدید:
🔸
رابط کاربری مینیمال:
محیط برنامه از آن فضای شلوغ قدیمی فاصله گرفته و با استفاده از رنگ‌های گرادینت ملایم و پس‌زمینه روشن، تجربه کاربری (UX) روان‌تری را ارائه می‌دهد.
این تغییر ظاهر نشان می‌دهد که قدیمی‌ترین ابزارهای فیلترینگ نیز برای همگام شدن با سلیقه کاربران مدرن، در حال به‌روزرسانی زیرساخت و طراحی خود هستند.
🔻
دانلود از گوگل پلی
🔻
دانلود از اپ استور
🔻
دانلود سایر نسخه ها
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/iaghapour/2730" target="_blank">📅 20:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hedioum Tunnel Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.1 KB</div>
</div>
<a href="https://t.me/iaghapour/2728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
Hedioum Tunnel
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/iaghapour/2728" target="_blank">📅 19:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA5oQ8NZuVeunq27jsXChI40O-2DuaU38RvHKQRHJkXKRLuXhagJ23gKgLEdzLXl_r1x-2mQG2pNwg03CCUvqOc01dVEZrrU1-iazyzzdJRBFHzipzlOCqIlx35wS_e81gCDN8WJDTtPpUBXlgz_JGI3SJ0StEhnUkQW-Lz7k24lFZpR_iSlIUqh0s3zTU-EIAY2Ylwk3xyMiMRFd8v61NZ7vubFNwpwa2DcQMVKssFi5Hl5wZIogx_3M5t2ZXeJCQ7wgg7hJkLytA3APFQS-9wqaCOytvuLU4-ygJ_ONWSHKUwAlQyv2wzyRj2eHJIBjhuhdkFy7Bm3DYUDU0Nhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش راه‌اندازی Hedioum Tunnel: تانل مقاوم‌ در برابر DPI
🔥
🔹
با پیشرفته‌تر شدن سیستم‌های مانیتورینگ و DPI، خیلی از تانل‌های معمولی این روزها دچار افت سرعت یا قطعی میشن. اما تو این ویدیو رفتیم سراغ یک راهکار قدرتمند به اسم Hedioum Tunnel که به خاطر مکانیزم‌های خاصش مقاومت خوبی در برابر تشخیص و اختلال شبکه داره.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/iaghapour/2727" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXIId25-X01qEJY2FZNCYLIsV28DCvEUC2F95hCwSLGF1zVFMJ1UT1nEdZq9TK6nEoBitThFwSjqfHCes0CCTfv1Dd08zzVqzAawWiGVGkNUlCWxqiRwNLrbA7t-YfXI9rIRCGokSWqQwJnS9EQb5lujZhM9hKu8BG5AfazyqT0Liyyvoove84DTW5BFZvNmCrYz7gODbuxv3IrkX-7PSk-18jMrSuHaQtC9T6wsKDty_vmbRsGfDg_gQrVvrMXSfFIyvkuPxFvTh3RBzVRglCQpSkWQg0cLai1zuWCYbUqmSMgiWsIUU__yRTUGw4x-LCZqokzHXk57_OCs731Wtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ارتقای بزرگ هوش مصنوعی پروتون؛ Lumo 2.0 با قابلیت تولید تصویر منتشر شد
شرکت پروتون (توسعه‌دهنده سرویس معروف پروتون‌میل) نسخه جدید هوش مصنوعی خود را با نام
Lumo 2.0
معرفی کرد. این نسخه با تمرکز شدید روی حریم خصوصی، قابلیت‌های جذابی مثل تولید تصویر، حافظه اختصاصی و جستجوی امن وب را به همراه دارد.
🔹
ویژگی‌های کلیدی Lumo 2.0:
🔸
عرضه در دو نسخه:
مدل
Lumo 2.0 Max
برای کارهای پیچیده (با ارتقای ۲۴۰ درصدی عملکرد نسبت به قبل) و مدل سبک‌تر
Lumo 2.0 Lite
برای کارهای روزمره.
🔸
قابلیت‌های چندوجهی:
امکان تولید، ویرایش و تحلیل تصاویر در محیط گفتگو به صورت کاملاً رمزنگاری‌شده.
🔸
شخصی‌سازی پیشرفته:
اضافه شدن قابلیت حافظه تحت کنترل کاربر، تعریف پروژه‌های رمزنگاری‌شده و امکان ساخت دستیارهای سفارشی.
پروتون که حالا بیش از ۱۰ میلیون کاربر در بخش هوش مصنوعی دارد، هدف اصلی نسخه دوم را جذب کسب‌وکارهایی قرار داده که نگران امنیت داده‌های حساس خود هستند.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/iaghapour/2725" target="_blank">📅 20:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLdI_JfZpGHdLK2PM9ITJYJbS6DMRQa25eOPzriaIVWq5Ch5MclRQRt8A4byfKtoACykNahlp8c1rbBRJbMBkaUsu-WjKVka0W80oPFfb8rPXfcWxhSFqTmvf2HiZcXG7fsC1FCN3HVTupuVOfn5n6AAkYAsNgq0_HIjXUB0KXbgiOH4AaOAra3FoTyAveaBN9ja3Z8H2I9NWEOPTdRGWMKK98bbik2E6ByYPaA4HyDTWmuN_rK9rjzR4cOo_oSLCBIxjAcKu-2wxWfjK1cipTZ2Fx67DXvKXb21J80nyrkzz5FHYyOsNvDNzGJ-MOCD31_qXDa1wbJffNVjYIHEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افزایش بی‌سروصدا و ۱۰۰ درصدی قیمت اینترنت فیبر نوری مخابرات!
شرکت مخابرات در روزهای گذشته، در سکوت کامل خبری و بدون اطلاع‌رسانی قبلی، قیمت بسته‌های اینترنت فیبر نوری را به شدت گران کرده و تغییرات عجیبی در سرعت آن‌ها به وجود آورده است.
🔹
مهم‌ترین تغییرات اعمال‌شده:
🔸
حذف سرعت‌های نجومی:
بسته‌های جذاب با سرعت ۱۰۰۰ مگابیت (۱ گیگابیت) کاملاً حذف شده‌اند و سرعت تضمین‌شده پایه برای تمام بسته‌های تمدیدی روی ۱۰۰ مگابیت قفل شده است!
🔸
جهش دو برابری قیمت‌ها:
هزینه بسته‌ها بین ۵۰ تا ۱۰۰ درصد افزایش یافته است. به عنوان مثال، بسته یک‌ماهه ۳۰۰ گیگابایتی که قبلاً با سرعت ۱ گیگابیت ۴۰۰ هزار تومان بود، حالا با افت سرعت به قیمت ۹۰۰ هزار تومان (بدون احتساب مالیات) فروخته می‌شود.
🔸
گرانی گیگابایت‌ها:
قیمت هر گیگابایت اینترنت فیبر که پیش از این حدود هزار تومان بود، حالا به نزدیک ۳ هزار تومان (و در بسته‌های کم‌حجم به ۶ الی ۷ هزار تومان) رسیده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/iaghapour/2724" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGDYkxDyc2rWifuyWolsl-n2Gl6pBp3E9g8o5sjXdcwYIPUj_waDQL-NI0LhuDr6SLpyMu5CPeo8Ts9fssaFM54RqNoBQKytraFlTVG2D8O0os8IXwQ6J5FN_EmeXC-KsWrN10mmFRGOSlEypGZA3x3uRgznBIHBOOY2M88DAXCKMstZ7WbFpF_klP2ZgA92npyu1LV0aLi0rcq0Y28_enbNPNajvx0_jxjXxayxJKgsA_1L9630DapstgCi2_nJHBK4At3tJvRBb4kK50UQWTlOatdrtTw015Wi9gIPT8pf8qqD8tR1JUeikX41932cj4INzr73R0OdnEY09Vk9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پلتفرم متن‌باز مدیریت DNS با دامنه دلخواه
با این سیستم می‌توانید یک سرویس ارائه ساب‌دامین رایگان روی دامنه اختصاصی خود راه‌اندازی کنید. کاربران می‌توانند رکوردهای دلخواه خود (مثل
mysite.example.com
) را بسازند و تغییرات به‌صورت آنی از طریق API روی Cloudflare اعمال می‌شود.
🔹
ویژگی‌های کلیدی:
🔸
پنل ادمین و کاربری حرفه‌ای:
ورود با اکانت گوگل یا ایمیل، مدیریت کامل زون‌های کلادفلر، تعیین پلن و محدودیت‌گذاری برای ساخت رکوردها.
🔸
ربات تلگرام یکپارچه:
امکان ثبت‌نام و مدیریت کامل رکوردها مستقیماً از طریق ربات دوزبانه تلگرام.
🔸
امکانات ویژه:
سیستم دعوت از دوستان (Referral) برای دریافت سهمیه بیشتر و قابلیت ورود/خروج دسته‌ای رکوردها (CSV).
🔸
راه‌اندازی خودکار:
نصب بسیار آسان با یک دستور لینوکسی (Bash) همراه با گواهینامه SSL رایگان و بکاپ خودکار دیتابیس.
🔗
گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/iaghapour/2722" target="_blank">📅 20:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
وعده وزیر اقتصاد: بازگشت عمده خدمات بانکی از هفته آینده / اطلاعات مشتریان امن است
علی مدنی‌زاده، وزیر اقتصاد، با اشاره به تداوم حملات سایبری به شبکه بانکی کشور اعلام کرد که بخش عمده خدمات مورد نیاز مردم از ابتدای هفته آینده مجدداً در دسترس قرار خواهد گرفت.
🔹
نکات مهم صحبت‌های وزیر اقتصاد:
🔸
امنیت داده‌ها:
تا این لحظه هیچ‌گونه اطلاعاتی از مشتریان از دست نرفته است و استفاده از سامانه‌های پشتیبان، مانع از بروز مشکلات جدی در حفظ دارایی‌ها و داده‌ها شده است.
🔸
تداوم حملات:
پس از بازگشت سامانه‌های بانک‌های ملی و صادرات به مدار، تجهیزات جدید آن‌ها مجدداً هدف حمله قرار گرفته است؛ اما به لطف سامانه‌های پشتیبان، بخش زیادی از این حملات برای کاربران محسوس نیست.
🔸
اولویت‌های شبکه بانکی:
تمرکز فعلی روی بازگرداندن سریع سرویس‌ها، شناسایی منشأ حملات و افزایش سطح حفاظت سیستم‌هاست. با این حال، راه‌اندازی برخی از خدمات خاص به زمان بیشتری نیاز خواهد داشت.
پ.ن:
الان ۲ هفته‌ست که بخش بزرگی از خدمات ۳ تا بانک اصلی کشور قطعه. تو این هیر و ویر شایعه هم زیاد شده؛ یه عده میگن هک شدن، یه عده هم میگن کار خودشونه تا جلوی بیرون کشیدن پول مردم رو برای خرید طلا و دلار بگیرن.
مثل همیشه هم هیچکس راستش رو نمیگه؛ اول میان کلاً تکذیب می‌کنن، بعد میگن آره حمله شده ولی اطلاعاتی دزدیده نشده، آخر سر هم که همه‌چی به باد میره هیچ‌کس گردن نمی‌گیره و پاسخگو نیست! تو این بلبشو، حالا بماند که بانک‌ها یواشکی جلوی وام‌ها رو هم بستن و طبق گفته بعضی خبرگزاری‌ها، سود وام‌ها رو از ۲۳ درصد کشیدن بالا و کردن ۳۵ تا ۴۰ درصد!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/iaghapour/2721" target="_blank">📅 16:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_TtInOmnPxqAxqiKsW7snX9dLOCRxKQTJxRFO0iQrqRtNTN3zl9zouKVQ3XiRf_Nl5SV9Ya-lwNfTlH2HKhLUuSG6X45kBZsZRGnBR2Rl8QF_Iso4SJpEa5u8rMpppwkQNhvgARM3a8x-egzerw8AOYnLhyx7rGeA5D_UsRkA5LiUSarlRzBTTaXB47Dx064J5gBLD-SGVllkDsNz5KIqDNl7KbkMCDTJ2Lv1eEQrYgV4X-olX1jKIs_2nKbr6u1r2zfwmbHV4mhAo8LFY7Er0sYylEF6q2GDPd7hmIlDWZepJDBwKf2DBK4Mcj_Pb-bi1FAQkLgNOLNmf-BpH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های سرور ایران فقط با یک کلیک
😎
🔹
یکی از مشکلاتی که این روزها خیلی‌ها باهاش درگیرن، محدودیت‌های شدید و اصطلاحاً اینترانت شدن سرورهای ایرانه که باعث میشه ارتباط ما با خارج مسدود بشه تو این ویدیو قراره بهتون یاد بدم چطوری فقط با اجرای یه اسکریپت ساده، تمام این محدودیت‌های شبکه رو روی سرور ایران برطرف کنید و هرچیزی که دوست داشتید دانلود کنید یا نصب کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ایران
#ملی
#محدودیت
#سرور
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/iaghapour/2719" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0qQNqWYn8PGvQCSTSDTBz3Es5t_kPm_8Z7Ow4w98BSqGA8rVTU28QdOrleSV5yfxDoP3ys8f32tohmiuerFH6F_ZTYZrrQ8sAW8zrkbLOrvauu4vD0JWxMiQLgPLOtXXKR0btjtEM8fSjB74RVp4DdDyMUupUY3pdjZhtMbROBNz1-HRJFyqqC_RmPL0NKuUpccdVZwNE4gkQ8LSzia914mJkdgzWVju24Tn0CjX7JCWIkVKbgDQaf8Rfrc2sbfBNZ0bpheWfnPDx5AUFyRonIkK3p2zt4S7wjcGA_40Oz2kZZccTtfM6GYywvq0zZH7tyDcobNYzHmld9yqTderQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔌
قطعی برق و سریال تکراری خاموشی اینترنت و شبکه موبایل!
🔸
با شروع فصل تابستان و آغاز خاموشی‌های برق، مشکل همیشگی از دسترس خارج شدن شبکه موبایل و اینترنت دوباره گریبان‌گیر کاربران شده است. گزارش‌ها نشان می‌دهد تنها چند دقیقه پس از رفتن برق، دکل‌های مخابراتی (BTS) خاموش شده و ارتباطات در مناطق وسیعی مختل می‌شود.
🔹
دلیل اصلی این اتفاق، فرسودگی و خرابی باتری‌های پشتیبان این دکل‌هاست که توان روشن نگه داشتن تجهیزات را حتی برای زمان کوتاهی ندارند. این قطعی‌ها نه تنها دسترسی ۸۸ درصد از کاربران به اینترنت موبایل را قطع می‌کند، بلکه باعث از کار افتادن خودپردازها، دستگاه‌های کارت‌خوان، دوربین‌های ترافیکی و سایر خدمات حیاتی و شهری می‌شود./شبکه‌چی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/iaghapour/2718" target="_blank">📅 12:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm9qOwcPuAdIvQYCu1AF6YOYfGWVOMIJaGvq1NRlmnsNe38pIo-tWAJKcZKDxaFYCeEGdITZB4g_c36MN9qZ4Uslzlw4w72CbQXVtnzVOyoXwKu9UEaHHqBl1wluxOShmjhsWdfrkriyRB55Q7-jt25du-hMfcck2MSL8JnlUo_cnHMGxpAp9ZdMg5WnrSB-jODDqnplnaMnQ_S2ByxqxWNOrzXau48cUyvHz4mMHDPHCfDUoS0tHkADyCSjwAylLRgNTy-BGvunMagxj0FbW_VDy3uy4jId0bSNBvp084UL51S5bAyrSUPdHvwV90dJ1UZJn51f0ypnpyiHCg-zXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی اسکریپت ساده EZxray Direct Server
یک اسکریپت کاملاً خودکار که سرور شما را به یک مرکز Xray با پشتیبانی از ۱۲ پروتکل مختلف و ۲۰ پورت متنوع تبدیل می‌کند؛ آن هم بدون نیاز به هیچ‌گونه تنظیمات دستی یا دانش فنی!
🔹
ویژگی‌های کلیدی اسکریپت EZxray:
🔸
تولید همزمان ۱۲ کانفیگ
🔸
مدیریت بکاپ
🔸
مانیتورینگ لحظه‌ای
🔸
رابط بصری جذاب
🔗
اطلاعات بیشتر در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/iaghapour/2717" target="_blank">📅 17:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hy0O5cA5EEy6rUeYS7WwMUPo087EmOgODev1wxPXA7UCKwu6hcRL-Zs7QxQz0krjIP-0ZGkAEWxp8nTkbHhbAla43vDIMjd9f9zITpu74_s30GrEXbjFcrcZ5PCgfqTsIQLdLx59l_4ipFd_G0cErhpXQDpBMTrO-tpfvGe7V2X5UeoZrhsVb6TVxRnpr4mYHGBY1URUGDMtjEW5IxrNC77OWuBIetnBy6jaUk6zSBMshBvmWY7OeoSpkVCUqA-NvDtFKmABCUXFyjcP_NAdMefiw_gPgoFQ3ZYcSaNmr0rWzW7QGT9yzoF6vsrDiGmX2Th73YSR4GWKW6hkM2FLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqV8nfwFllOEkgGlIWVZ7SJnkEu2xmcpNQLtIUxU_4pjj-6KHaDw19DujLcry_85gG-2f177-HpG2gJCemhk-zuYx4ZpWMwS7Yb6isI_AYi993mqxVCVCZS62JiN7BbzX231Uavujww5mETyzS70v7Ydc8CdGLzl0J82dGlPcSZFZMgBca_aPRGx9gHkOzDfKM7AMzsbudl4nD7ltBTvYXq3dAJs64CtDsdZDlrKs46eJ_M92UY8uDYdjp3hUnOzXqkqSalR-FiP14imfbsZtG4yu0cOt10eHxqNPzBB1QYMZUjpaZtCfsyw6gTEjJdyA-YZDjoIaG-duC-V_C3MbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWRg3cRITUXt3k_Ge3y3bYJ0nkQTV3dvL6utiDiyml5dEhy-Z2aOTpVC1xAvziO1A4eFGv2sKaT0MjM_l0r8h4Pmz3iPDFLMsoCIRjmvu4X9THBJKvorkFm9BPQ0DGuIXNUsYFHwjGNpd4laRRDXGDnUd-u8o9DVrBiPIQYdyjBTvDge6GHqdAsfe_VIPd3Yl7Lru65U79QNh_6BZbTJ36tL5DZExB5P4BdRtEcv1T9RifMxf7oFWMEZKtmNYqlBbnWW-GsiN1WcMKRiQleP3BlfikS5HkN5BSfgwHEyOKKAf4iHv5bbT9yOwasMcCfDjd73tRqLzN4mXWslE6c05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6IaZ4JlEc9MNC1S81w0eLxiZZdg4Tfxhn7hxS7xEL6o_6fZPm5-eZa1nZ4XbZ2S25GAG5_AMyBAEDpl3cPDHyGIWWhykF21cc6Qd-9tQ_hTClcb9AQbqMI9op4oj1k4YEb-4kaHEprVP_1w8BcjwWuncFpOpE85Tn_FLLYDsOTxbDK-yToxk493f2yAo4-_ZI3Zr9OnYKBcQmXfKwjZ7lSErYFiakxz6rfe_IIz2zzL2SLO53osQfZfc-0yWT9NJsllVvP9g8taRMJjfrIhgqqx0Q2AyXgMW2e7exH2_fJs7F36lPyk8AIQz-BbwH2Ni1Eqm-4JwUcaD6dv9efwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqYnj23O1WmSvLvpFm3LB9eMR3etbWgzCdU9gnFYlLBgJwVsSTHVXR8pb4PSOuX_L2Vs8huETs13MPF4byiP1VoyBvF5Q3tzE-yOi6LQJuYd7HyB6NsYCRWaEUedHyb-MW8_-KS3nFoPlcHW9O7kzamcEvSuPjjIOlZQAA5uR5KHKDB9NFjCphHVMMEWVUiYoMzeShnkvfsppktvt2dMlfofWfZWdBlv6J9bhob5De5U4I5zpF-CLMXuZCNIBhqqPxxwSphHj1oNn2kigjPDyIwPZZhzXAXKWBlcRinbBuZotJ3pS2xxa9L90EiUxamBVk2cXR4aexwahBAAanGT2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همراهان عزیز کانال
💚
همون‌طور که خودتون هم می‌دونید، پشت هر اسکریپت یا ابزاری که توی گیت‌هاب منتشر می‌شه و کار ما رو راه می‌ندازه، پشتش توسعه‌دهنده‌هایی هست که بدون چشم‌داشت، دانششون رو رایگان در اختیار همه قرار می‌دن.
من به عنوان کسی که تو یوتیوب و تلگرام فعالیت دارم، همیشه وظیفه خودم دونستم که در حد توانم از این بچه‌های متخصص حمایت مالی (Donation) کنم؛ مخصوصاً اون عزیزانی که واسه اولین بار اسکریپت و ابزارهاشون رو در اختیار تیم ما قرار دادن. این کار اصلاً لطف نیست، بلکه یه وظیفه کوچیک در برابر زحمات اون‌هاست تا انگیزه داشته باشن مسیرشون رو ادامه بدن.
دم همه‌ی توسعه‌دهنده‌های خفن و کاردرست گرم
👌🏻
اگه ابزاری کارتون رو راه می‌ندازه، دمتون گرم که با یه تشکر، ستاره دادن تو گیت‌هاب یا حتی یه دونیشن کوچیک (در حد توان)، خستگی رو از تن این بچه‌ها درمیارید.
مخلص شما...</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/iaghapour/2711" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDZWhEMcK84mo6gRCGUtFfJ9HCDz67SM_U6nHrNWtAo9jtQZa7KVovHTkEJ4WjWd_9UZrmINliRRt0-1oMrXwoaT16Z4pROTLq5BgsryJNyT2-6fGXymeMsvEJQlxem0zGmL86Q8E9dNH3XOVezQ72LI-1FOLCZ44OfnhqOnzv3tBbtt07iGnr9xbqD7OoN-wmlZjtExg4MVC4u9XcqFmvux4XGv-yoG2L0Gv3GKZDEy_p5NYfjubOy0dx3-LApR5psxipaW420Ynv81zjBmGO8eH65r8F6q9yNHc9IKZZ5ki9MjgZkRq9So0SvgP1_85R-6rP7A5dZvUlXwHDJT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Defyx VPN؛ دسترسی آزاد و هوشمند به اینترنت
🔹
برنامه Defyx یک VPN مدرن، امن و متن‌باز است که با رابط کاربری بسیار ساده خود، امکان اتصال سریع (تنها با یک لمس) و حفاظت از حریم خصوصی را فراهم می‌کند. این اپلیکیشن با بهره‌گیری از هسته قدرتمند DXcore، از پروتکل‌های معروفی مثل Xray، Warp، Psiphon و Outline پشتیبانی کرده و بدون نیاز به هیچ‌گونه تنظیمات پیچیده، اتصالی هوشمند به همراه ابزار داخلی تست سرعت ارائه می‌دهد.
🔻
بر اساس اطلاعات منتشر شده، نسخه جدید این برنامه هم‌اکنون برای تمامی پلتفرم‌ها از جمله اندروید، ویندوز، iOS، مک و لینوکس در دسترس کاربران قرار گرفته است.
🔗
دانلود آخرین نسخه از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/iaghapour/2710" target="_blank">📅 18:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG8SbTSY4xfBmgUYO_K8LoOWfIAOF4l6c1yVOFEfHH5OGbOxDdcgvdoVjyeoT-8cnOCmpbRGFZrC9QW7gG8UntMvR0ddrtVKMKETavPM2pnORTigRbMcN1B7ZGyk4bUoqoYncOBLJf_Fub3ovrR0bHe0DMf4vNDUiVRrzvGcl_uo5--bnope9GWhUOJCuC4o1FAgjGJCfHFgUWOF8Uo8ciJBwgLvtvyAiBVmTXGujTfP5PbVn5t_k_qXFJd0jGbJ4AxdvCrsHkk0gv_gJ8sdFz8GjT3M8T6SRVxhTuBFpUbrbKudqGr2C5wxOacxaATU71HDrb7SjcZ5_DS3C4W9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صرافی کوینکس ارائه خدمات به کاربران ایرانی را رسماً متوقف کرد!
🔹
صرافی بین‌المللی کوینکس (CoinEx) با انتشار بیانیه‌ای رسمی، به دلیل پایبندی به مقررات جهانی مبارزه با پولشویی و در پی گزارش وال‌استریت ژورنال، نام ایران را در کنار کشورهایی مثل آمریکا، بریتانیا، کانادا و چین در لیست مناطق تحت محدودیت کامل قرار داد. در حال حاضر تلاش برای ورود با آی‌پی ایران مسدود شده و حتی در بسیاری از موارد استفاده از VPN نیز کارساز نیست و کاربران با خطای عدم دسترسی مواجه می‌شوند.
🔻
اطلاعیه مهم برای برداشت دارایی‌ها:
کاربران ایرانی حداکثر تا
۲۵ سپتامبر (۳ مهر ۱۴۰۵)
فرصت دارند تا اقدامات لازم را انجام داده و دارایی‌های خود را خارج کنند. در این دوره انتقالی، حساب‌های احراز هویت‌شده (KYC) فقط امکان برداشت خواهند داشت. در بازار اسپات تنها امکان فروش (بدون امکان خرید) و در بخش فیوچرز تنها امکان بستن پوزیشن‌های باز وجود دارد و باز کردن پوزیشن جدید ممنوع است. همچنین اگر وام فعالی دارید، باید هرچه سریع‌تر نسبت به تسویه کامل آن اقدام کنید، چرا که پس از تاریخ ذکر شده احتمال اعمال محدودیت‌های بیشتر وجود دارد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/iaghapour/2708" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILV5xWwJrzQQ8Ef5W35JiSNLYCpZEd5OIuEX8lDaRIJUUvO7eg2Iy44rJMXcyVbNwk8hUBZotLxxPH3Hciayq9qABZLsikiAXUliJip2knGuylHqWRRSisOp9joFZArK-cvyhR2es3pBk8NV8cUnufvafPSZxmFTtdW-UAlPj90pXYNfI2lMD52_Sn1sbtdf19AOUFV2Z-VSSi4ddz5fDvPXJtcNmBHAcp1sjGT57uitHAynFkNeSi4EjDtdR5O4aH7o9ex7o_S89lc2PgieruhxkLzPeUJVdiOmp1zo-BRgeTqlpYtD_Jxcbdj8crwaPJs8VaI9QEMdapIxLTfT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بر اساس گمانه‌زنی‌ها، انتظار می‌رود بازی مورد انتظار
GTA 6
با قیمت پایه ۸۰ دلار (معادل تقریبی ۱۳.۵ میلیون تومان) برای نسخه استاندارد روانه بازار شود. همچنین، خریداران برای تهیه نسخه کامل‌تر یعنی «آلتیمیت ادیشن» (Ultimate Edition) احتمالاً باید مبلغی حدود ۱۰۰ دلار (تقریباً ۱۶.۵ میلیون تومان) پرداخت کنند.
خوش به حال اونایی که توانایی مالی خرید دارن. )</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/iaghapour/2707" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">domains List -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.5 MB</div>
</div>
<a href="https://t.me/iaghapour/2705" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دامنه ها برای به ویدیو بالا
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/iaghapour/2705" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4OV1hoVTzlHCRRu-DEuJ76r148gaT_li4ZgcISOpbPqVaxU1xcU8UW8uq7e8QA7j_QnShRAum8RQSB5ywnP8wolihdMhMLf3mcOB3IKP_VCEI7ynFinVkysFaeBbTfRr1CYm_Yx0_2MYUV5fCU-YpklHZf2v1fiRoL8uPzzBmTrw5cw3thYM9Xf-ADBJyE77XW4nSBODMT6E7qUixmUlPCUf9jI5rFei3iVQBPvNZLSg6koHKlNiqHcq7Vbz-KVNUccQXToIu_WnHrpWfLmm0ZKlSHHDRH8FDPZSEtnRhHJ0-xhASAWYlF2susGPHuNhtq8u0yfzOqgi28wJLS50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروتکل ریلیتی رو دوباره زنده کن!
🔥
(+ اسکنر پیشرفته)
🔹
خیلی‌ها فکر می‌کنن با محدودیت‌های اخیر، دوران پروتکل ریلیتی (Reality) دیگه تموم شده و کانفیگ‌هاش از کار افتادن؛ تو این ویدیو قراره با هم یاد بگیریم چطوری پروتکل ریلیتی رو دوباره با بالاترین سرعت ممکن زنده کنیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ریلیتی
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/iaghapour/2704" target="_blank">📅 17:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2703">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0dMMuiRqto3eymz7sLBhllQt15B6BEOxc-Emr0N650T6rizfrVybVGVJtJLDSWutG7uxp5X4Buu9rPbPyEPW4AtLtBisFIiFwJBLYK4YXIZbBUROb--hS0PhVce_7a1M6Y_M9AjSlT-YOYRDAUWeKjYAX2clJSn0Kni2Z-vXUWM8jDMqSLNwOirLkqyymk2aKtueibMP1dSURA83_3CF5ikM6V4ROHc-mAu39BOE9LfebXFbVzbhM0zFOtKt4BMTuH36Iw847U6yFJNU49QoQ46hVMicJe30Rjh4eWtK6JAkVWkeOebjUJmZeQx2huQDoIu3iiR_DLDo6CYwAOQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
خداحافظی با کپچا؛ کلودفلر و غول‌های فناوری به دنبال استاندارد جدید
🔸
شرکت کلودفلر با همکاری توسعه‌دهندگان کروم، اج، فایرفاکس و شاپیفای در حال ساخت سیستم جدیدی به نام PACT است تا برای همیشه به دردسرهای کپچا (CAPTCHA) و اثبات ربات نبودن پایان دهد. ایده این سیستم بسیار هوشمندانه است؛ وب‌سایت‌های معتبر پس از یک بار تایید انسان بودن شما، یک توکن کاملاً ناشناس صادر می‌کنند. از آن پس، مرورگر شما همین توکن را به عنوان «برگه عبور» به سایت‌های دیگر نشان می‌دهد تا بدون فاش شدن هویت یا تاریخچه وب‌گردی‌تان، ثابت کند که شما یک انسان واقعی هستید.
🔹
مدیرعامل کلودفلر می‌گوید در حال حاضر بیش از ۵۶ درصد از کل ترافیک اینترنت را ربات‌ها و ابزارهای هوش مصنوعی تشکیل می‌دهند و ابزارهای امنیتی قدیمی دیگر پاسخگو نیستند. با اجرای این پروتکل جدید، هم حریم خصوصی کاربران به طور کامل حفظ می‌شود و هم دیگر نیازی به حل کردن پازل‌های آزاردهنده و کلیک روی عکسِ چراغ‌راهنمایی نخواهد بود! / دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/iaghapour/2703" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVaWauzuJO0rNIqjEhPOhTiive-F5vqfC3qF5nfhuCkzTcsQPSVegfFwInz1AS49K-Gh2XiY2bahDLIo0Bx7lwgQrbyQr775juLPqhOkF16Ey25Uad0JfxhKdW_Wxt3lbTuNhlhHCe4XU4O0wDpI-PfGfKRox-jv7FhG9bOvtOusG2p7RLp6F4tRDgAKnIRaaaKcCWy68qB1xmDopPMRSeGePSq5cXO8Cv5E2VpWLxEqo9_rZVGt44enRsHNLGDOyEgXoQff0fRHN-adMdJb0egEzCMh12lXTG82ikhXZz36g8bP_SbMLwxRnigyfRsStwO-1jkI2rBl2E_rOWx-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سقوط آزاد پلتفرم‌های داخلی و رکوردشکنی هشتگ تخفیف پس از وصل شدن اینترنت
🔸
با بهبود نسبی وضعیت اینترنت، کاربران به سرعت در حال ترک پلتفرم‌های بومی و بازگشت به شبکه‌های جهانی هستند. آمارها نشان می‌دهد فعالیت گروه‌ها در پیام‌رسان «بله» ۸۱ درصد سقوط کرده و ۲۷ درصد آن‌ها کاملاً تعطیل شده‌اند. رشد خیره‌کننده این پلتفرم‌ها در دوران قطعی، صرفاً از روی ناچاری بوده و حالا مردم کانال‌های داخلی را فقط به عنوان یک پایگاه پشتیبان برای قطعی‌های احتمالی بعدی نگه داشته‌اند.
🔹
در همین حال، کسب‌وکارهای آنلاینی که فروش طلایی خود را در دوران محدودیت‌ها از دست دادند، برای جبران خسارت‌های سنگین به تخفیف‌های گسترده روی آورده‌اند؛ به طوری که استفاده از هشتگ «تخفیف» ۱۲۰ درصد جهش داشته است. این آمارها ثابت می‌کند پلتفرم‌های بومی برخلاف ادعاها، هیچ جایگاهی برای جبران ضرر اقتصاد و کسب‌وکارها نداشته‌اند.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/iaghapour/2701" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2698">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حمله سایبری به شبکه بانکی
!
شرکت خدمات انفورماتیک با انتشار اطلاعیه‌ای، دلیل اختلالات گسترده در کارت‌های بانکی را تشریح کرد.
🔹
جزئیات این اختلال بانکی:
🔸
دلیل اصلی قطعی:
وقوع حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت.
🔸
اقدام پیشگیرانه:
این شرکت اعلام کرده برای جلوگیری از دسترسی غیرمجاز هکرها و حفظ امنیت داده‌ها و موجودی مشتریان، خدمات مبتنی بر کارت را موقتاً و به‌صورت عمدی از دسترس خارج کرده است.
🔸
گستردگی مشکل:
با وجود اینکه در اطلاعیه رسمی فقط نام ۳ بانک آمده است، اما بررسی‌ها و گزارش‌های مردمی نشان می‌دهد قطعی‌ها گسترده‌تر بوده و بانک‌های دیگری مثل «ملت» هم درگیر این اختلال شده‌اند.
🔸
وضعیت فعلی:
تیم‌های فنی و متخصصان امنیت سایبری در حال کار روی شبکه هستند تا این مشکل برطرف شده و خدمات بانکی به حالت عادی برگردد.
پ.ن: بابا ولش کنید‍! بعد 2 هفته اختلال این حرفا چیه میزنید؟ مثل قبل همون روند تکذیب رو جلو برید. بگید که ما هک نشدیم و قطعه سخت افزاری سوخته!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/iaghapour/2698" target="_blank">📅 19:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2697">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-OLqMefqqri6HKSZjQxjfkX_F1DHcLXOkA_asiO7komDdY9QC83y1Wb8_qsjsFr1jKxCKNt6HMcGKtUp2sCdTDqBiyf2ndNApQlSHRpnowJZMKPLW0szqq86sGCE1SeQ4bdKVBPONtt1tFiiR-9nuOazNIC9Vv3cRF01exfQXZ8PIa08Hf5-N2-plk3m5_U9e8C7nJLTzM91qCUyglE9KbHX5gfedSkHk9dwN-X5TGnblh7JFH3lNleWp2yQqrLVVsEXbGqtOQzpK6xeC1pwLOZNHW0NqrwzSg_qYtN6Y6ouJH-Pw2XNum6p_CIoYag98eUYN-q8-Je_K5Y6YhM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
چرا فعال نبودن IPv6 در ایران یک بحران است؟
در حالی که دنیا به سمت استفاده کامل از IPv6 رفته، اتکای شبکه ما به ظرفیت محدود IPv4 چه مشکلاتی ایجاد کرده است؟
🔹
پیامدهای اصلی این عقب‌ماندگی:
🔸
کابوس CGNAT:
به دلیل کمبود IP، اپراتورها هزاران کاربر را پشت یک IP مشترک مخفی می‌کنند؛ یعنی شما عملاً هویت مستقلی در اینترنت ندارید.
🔸
دردسر همیشگی کپچا:
چون درخواست‌های هزاران نفر با یک IP ارسال می‌شود، سایت‌های خارجی شما را ربات تشخیص داده و محدود می‌کنند.
🔸
مشکلات گیمرها:
گیر افتادن در لایه‌های NAT باعث خطای Strict NAT، افت پینگ و قطعی در بازی‌های آنلاین می‌شود.
🔸
اختلال در دسترسی‌ها:
بدون IP مستقل، راه‌اندازی شبکه‌های خصوصی و دسترسی از راه دور به دوربین‌ها و تجهیزات هوشمند بسیار دشوار است.
🔸
افت کیفیت شبکه:
بار سنگین سیستم‌های تبدیل آدرس (NAT) روی سرورها، باعث تاخیر در مسیریابی و کاهش پایداری اینترنت می‌شود.
پ.ن:
دنیا با میلیاردها آدرس مستقل به دنبال سرعت و پایداری است، اما ما هنوز برای یک ارتباط ساده، درگیر پیدا کردن یک IP تمیز و عبور از لایه‌های NAT اپراتورها هستیم!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/iaghapour/2697" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2696">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXsSu5wOlmWx4SFOKt8koc4xAuf3-c0WW_FaFKhdBacVadOyzswTs1iMDrLBcDRfWpmF-XRqU66WwnTSKXcx4Clur9e3CjA7jJ5vC8Qe68pnSTtJZ7YgZ6TXzcX0EhH3mnl8Pv2XXeP7hJFqJERJcBMyY4QbAsPbn75FcTOQQ7Oue-QSNFrm5S3HaC8g2y4BNJ0azJc5722pbBMTdhXtBDxLJvEL7HyWtcHojTHuRkoSFhmh2dY58b8RijCv7SXlaadLWBxA1Ep1yieTGMFjCJt8Wc7CHTwtgt9HyzkRZ2RRcX20wra56l9SdnpOK4HpWlBL4XOwdujSrTQQ0Y7_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بحران خاموش در دیتاسنترها؛ اینترنت برگشته، اما نه برای کسب‌وکارها!
پس از گذشت چند روز از قطعی گسترده و مسدود شدن کامل ارتباط با اینترنت بین‌الملل در سراسر کشور، اکنون در حالی که اینترنت کاربران خانگی و اپراتورهای موبایل تا حدودی به حالت عادی بازگشته، اما گزارش‌ها حاکی از آن است که دسترسی بسیاری از دیتاسنترهای داخلی به اینترنت جهانی همچنان قطع یا دچار اختلال شدید است.
این دسترسیِ قطره‌چکانی و عدم اتصال دیتاسنترها، پیامدهای مخرب و گسترده‌ای برای زیرساخت‌های شبکه و کسب‌وکارها به همراه داشته است:
🔸
فلج شدن سرویس‌های آنلاین:
بسیاری از استارتاپ‌ها، پلتفرم‌های خدماتی و توسعه‌دهندگانی که برای کارکرد صحیح نرم‌افزارهای خود به APIها، کلادها و منابع بین‌المللی وابسته‌اند، با اختلال جدی مواجه شده‌اند.
🔸
خسارت‌های پنهان و سنگین:
وصل شدن اینترنت گوشی‌ها تنها ظاهر ماجرا را عادی جلوه می‌دهد؛ در حالی که شریان حیاتی بسیاری از کسب‌وکارهای دیجیتال در دیتاسنترها مسدود مانده و خسارت‌های مالی و فنی جبران‌ناپذیری در حال رقم خوردن است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/iaghapour/2696" target="_blank">📅 19:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/iaghapour/2694" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJT8yG80RIoQQCbtgr35YELNUnxFuOkvhpKzBYZ_HViLbpCWlkLDEOSF8tSvVmYtUAQRVtBzlEWn_o_IbHtF-bWzOAu0bS7U5ENGRXGi_CX3SvwH5pbK9q8dT3X0Sxggk6AYk7RCzmcZQ-deW4GFlzxoy_18i_7DmSY4c-14fRlhZ85F1OX191MzPbD6cDuGNdqDTMOPY3YVd-oYcOOhnh3S8eFoIeVaactpFdroyiVLNPzLal6WJQKhTnP1npv3X71M5vM9StZl7wQhn9ExlPJ8o4qXyguo2cFRGNhb4hvVDdXZPrup55ACGOsRW3FQGenDaFdaPKS6OhxwLsBTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند.
در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس /
ircf
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/iaghapour/2693" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi8WyHkyQZlsgkQDVB1QZ4SCnEl1_w-n-RbH67xgFxwcUPXhjpTRFOfRQO5GKuchmngSx-qPCfA8Q0eQ4m8mfF-h4jmi3mUFhofCdW-LGPrJB5pAG4Ub1P1GOwrV3SqeEL7MGtC98XTsl6tuOzbVrof4uwi5HkytV3q0BfMlYCSajo2Acy16le3PCmDAqNj02kXGrCHKHMSXGELYCWq1xXOvgB769gsadq42Z780UoXLHGmqAkKrdS3blWnn8V4183tq26nP73ywhutKAgqS-uQFClKfPn1TvXQiezX34ZwKwU3Tl2rJTM5VMZGHgzK3e50MIhtte1ZvwrHb5Q7bLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش 4 روش تانل پیشرفته و مقاوم در برابر فیلترینگ
🔹
تو این ویدیو قراره با هم ۴ تا از بهترین روش‌های تانل زدن رو بررسی کنیم و یاد بگیریم چطوری تانل‌هایی بسازیم که در برابر فیلترینگ پایداری خودشون رو حفظ کنن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/iaghapour/2691" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
دوستان عزیز،
ربات «تماس با ما»
چون نسخه رایگانه، به محدودیت ۵ هزار پیام در ماه رسیده و رفته رو حالت تعمیر!
اگه تنظیماتش بر اساس تایم‌زون باشه، اول ماه جدید یعنی 2 روز دیگه خودبه‌خود درست میشه؛ وگرنه به ناچار نسخه پرو رو می‌خرم تا دوباره در دسترس قرار بگیره.
🥸</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/iaghapour/2690" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/iaghapour/2689" target="_blank">📅 16:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌐
مدیرعامل سروش‌پلاس: فیلترینگ و قطعی اینترنت به ضرر ماست!
امین شریفی، مدیرعامل سروش‌پلاس در نشست گزارش عملکرد سال ۱۴۰۴ اعلام کرد که قطعی اینترنت و اعمال فیلترینگ نه‌تنها به رشد پلتفرم‌های داخلی کمکی نمی‌کند، بلکه نتیجه‌ای جز عصبانیت و لج کاربران ندارد.
🔹
چکیده مهم‌ترین آمارهای گزارش سالانه سروش‌پلاس:
🔸
ریزش کاربران پس از رفع محدودیت‌ها:
با آزاد شدن دسترسی به سایر پیام‌رسان‌ها، سروش‌پلاس با افت ۱۰ تا ۱۵ درصدی در تعداد کاربر و کاهش ۱۰ تا ۳۰ درصدی در شاخص‌های فعالیت مواجه شده است.
🔸
وضعیت کسب‌وکارها:
آمارها نشان می‌دهد حدود ۷۰ درصد از فعالیت کانال‌های فروشگاهی، آموزشی و تولید محتوا که در دوره محدودیت‌ها ایجاد شده بودند، همچنان در این پلتفرم ادامه دارد.
🔸
رشد آمار کاربران و پیام‌ها:
تعداد کل کاربران ثبت‌نامی این پیام‌رسان از مرز ۵۲ میلیون نفر عبور کرده است که از این تعداد حدود ۲۰ میلیون نفر کاربر فعال ماهانه هستند. همچنین در سال ۱۴۰۴ بیش از ۳۰ میلیارد پیام توسط کاربران جابه‌جا شده که ۷۶ درصد از آن‌ها مربوط به چت‌های شخصی بوده است.
🔸
امکانات و تغییرات جدید:
رونمایی از مدل اشتراکی «حساب پرو» (با قابلیت‌هایی مثل نشان ویژه و حذف تبلیغات)، توسعه تنظیمات حریم خصوصی و همچنین افزایش جایگاه‌های تبلیغاتی پلتفرم از ۳ به ۱۳ مورد، از اقدامات مهم این سال بوده است.
🔻
پ.ن: من داشتم میخوندم خندم گرفت این چطوری داشت میگفت خندش نگرفت؟
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/iaghapour/2687" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2685">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEH8CTGcNrNJlKZMDp19G0gSEFeJlqJnk6qghSOO6WaARRukNE6NNmUlxbH3Y2wIl9AUPRXj_cH3Nrd-LgNZKCJOmSUUZ3zn6kNt-FwstJSQLnq0wwcmq-xqYt82uLmtCorWMuzx7exYykCMGdVJUoidT4YGoTY-S_uYfFMN8N1PMSoGyDuW-inlOUNEhsUi5ZiS2lpQ9c9anPdXi6vNoP4cRRxbmnQEsiIrFC1Tl-S-wfvpr99ZIF-SZ-qvUY-MkPU83BklubidqhWe53jRsyc3pVD6fbKOH3dedoQHDOu2XMR4Kb8tGcAJxxOfrVj34Cv_mjGJOSKTSWxt90kulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (NovaProxy v3)
🔹
تو این ویدیو قراره یه روش فوق‌العاده برای ساخت یه فیلترشکن کاملاً رایگان و پرسرعت رو با هم یاد بگیریم. این بار رفتیم سراغ ورکر کلودفلر و قراره از اسکریپت قدرتمند NovaProxy v3 استفاده کنیم. تو این ورژن حل مشکل تماس صوتی و تصویری رو هم آموزش دادیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ورکر
#novaproxy
#worker
#کلودفلر
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/iaghapour/2685" target="_blank">📅 19:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2684">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQLd2EW_vqKKKBvWGs4Rw68VW7kgMTf78r3CFWQLCDf7hyOzHzwA5neU06vGKf6ktgMHLAHeMnO0IUXiNekh14wkFnZXmJ0brKRqL0azZFyiLW-8yVdo69BwPMPBQQo6LaYgEQEe2Bs3N3IN4elHvjg7dxm5SLKzUo8744OscY71qHT0w5PsiW4j1_XZN4axjFbUcAix5RZcOVYIKpSmKszP1DJUQdF6bHDQEKb52FrqKS8XSMm6VU_9nQzXpTPUZLrKt6AnuH5vU8-wpZCRliBXiJ-4Nj7v3OFWIeKcbl0KG4U0F-jmiMiQcEMNxtgouQvmF1Vl-Jjq3Vmo-1Mc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افشای ۱۲۴ میلیون پسورد و ۵۶ میلیون ایمیل؛ آیا اطلاعات شما هم لو رفته؟
پایگاه داده سرویس معروف Have I Been Pwned به‌تازگی آپدیت شده و آمار نگران‌کننده‌ای را منتشر کرده است. این بار هکرها مستقیماً به سراغ کامپیوترها و دستگاه‌های شخصی کاربران رفته‌اند و بدون اینکه کسی متوجه شود، حجم عظیمی از داده‌های حساس را سرقت کرده‌اند!
🔹
نکات مهم این نشت اطلاعاتی:
🔸
منبع سرقت:
این اطلاعات نتیجه هک شدن یک سایت خاص نیست؛ بلکه بدافزارهای مخرب، پنهانی روی سیستم‌ها (مخصوصاً ویندوز) نشسته‌اند و پسوردهای ذخیره‌شده، کوکی‌ها و داده‌های مرورگر را دزدیده‌اند.
🔸
خطر پنهان:
از آنجا که بسیاری از کاربران اصلاً متوجه آلوده شدن دستگاه خود نمی‌شوند، این سرقت اطلاعات می‌تواند تا مدت‌ها بدون هیچ ردپایی ادامه داشته باشد.
🔸
اقدام فوری:
همین حالا به وب‌سایت
Have I Been Pwned
سر بزنید و ایمیل خود را جستجو کنید.
🔸
راه‌حل‌های امنیتی:
اگر اطلاعاتتان لو رفته بود، سریعاً رمزهای عبور خود را تغییر دهید. همچنین برای جلوگیری از نفوذ، حتماً تایید دومرحله‌ای (2FA) را برای حساب‌های مهم خود فعال کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/iaghapour/2684" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💰
مدیرعامل همراه اول: قیمت فعلی اینترنت با قیمت واقعی آن هیچ سنخیتی ندارد!
مهدی اخوان، مدیرعامل همراه اول، در مجمع عمومی سالانه این اپراتور با گلایه از تعرفه‌های فعلی اعلام کرد که هزینه‌های سرمایه‌گذاری ارزی آن‌ها کاملاً مشابه اپراتورهای منطقه است، اما قیمت هر گیگابایت اینترنت در ایران بسیار پایین‌تر از آن کشورهاست.
پ.ن:
جناب مدیرعامل! اتفاقاً تو این مملکت خیلی چیزها هست که هیچ سنخیتی با هم ندارن؛ از کیفیت اینترنت شما و چیزی که واقعاً به دست ما می‌رسه بگیر تا درآمد بالای مردم منطقه و حقوق‌های پایین ما! از همه مهم‌تر، بین زندگی و رفاه شما و واقعیتِ زندگی مردم هیچ سنخیتی نیست!
اگه واقعاً کار براتون نمی‌صرفه ما هم راضی به ضررتون نیستیم، کلاً درِ این اپراتورها رو تخته کنید و جرم‌انگاری استارلینک رو بردارید تا ببینیم تو یه بازار آزاد اصلاً می‌تونید باهاشون رقابت کنید یا نه! واقعیت اینه که سودهای کلان این اینترنت انحصاری (پرو) حسابی به دهنتون مزه کرده و حالا با گرون کردن‌های نجومی و پشت‌سرهم، به هر دری می‌زنید تا جیب مردم رو خالی‌تر کنید. وگرنه این چیزی که دارید به ما می‌فروشید اصلاً اسمش اینترنت نیست؛ هر وقت یه اینترنت واقعی و بدون فیلتر دست مردم دادید، اون‌وقت پولش رو هم بگیرید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/iaghapour/2682" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPReIFxOLRg8JpzL1vTlRWE7xS8CCojBNcMXgHPuqAZ2GuOl7JvaJu7u0RiLOP6HpLBL8HZ-kTNIK86d8jw21aYD-J7v7LMfhcy-CH1xK3ThFEo4g2-VKyGZxhb_ABh0FWctFVmDNMyUkojUZsgr6Hk2XhqJHg7ZVd7Fo-iFjwSP3AZxLJs3sfnCzBbMi-2B97UwPyE7JykFr_hkgcDgSXfb4WfR7T5ca31hbO3tdJjOLVWf8LWj88mABdD-Zj4PWHDyeGMNWkG5QaYsA9drT8EdutirH616LVj4nbYav7sVU_ODRlSB_wOWeIkpG4mLTS_O7OWXKTjxjtFXj34gFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار خیلی مهم: خطر فریز شدن دارایی‌ها در صرافی‌های خارجی!
بچه‌ها، همونطور که تو تصویر می‌بینید، صرافی‌های خارجی یه اخطار خیلی جدی در مورد تراکنش با پلتفرم‌های تحریم‌شده توسط OFAC (دفتر کنترل دارایی‌های خارجی آمریکا) منتشر کردن.
⚠️
تو این هشدار صراحتاً اسم ۴ تا از صرافی‌های معروف ایرانی آورده شده:
🔹
نوبیتکس (Nobitex)
🔹
والکس (Wallex)
🔹
بیت‌پین (Bitpin)
🔹
رمزینکس (Ramzinex)
❌
مشکل چیه و چه خطری داره؟
این صرافی‌ها اعلام کردن که سیستم‌های ضد پولشویی (AML) به شدت تراکنش‌ها رو بررسی می‌کنن. اگه مستقیم با این پلتفرم‌های ایرانی تراکنشی داشته باشید، ممکنه حسابتون محدود بشه یا حتی کل دارایی‌هاتون رو فریز و مسدود کنن!
💡
حالا باید چیکار کنیم؟
به هیچ‌وجه انتقال مستقیم ارز بین صرافی‌های ایرانی و صرافی‌های خارجی انجام ندید. حتماً از کیف پول‌های شخصی (مثل تراست ولت، یا ولت‌های سخت‌افزاری) به عنوان واسطه استفاده کنید تا مشکلی برای سرمایه‌تون پیش نیاد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/iaghapour/2680" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9IQv2BDtpRKa3xuJZmrnRw54l4OwZd11kjJz6keDYaAZBltOJU2wJSKvEScPIdiTALp78vU01JppHMMIwDkOdKEOCWl7sArjE5F7_yQSycQ6dwNe7MUb5cIv9TubUzQayCqwBTTSNfVtADEscjQXYvlZZJiftorqJYrfMcvY55Qp7-TXPFmbwSMzVgsfhLqOCfnPc6nNVcvn0FHtzpTMvXcVfOeH9ct7nTb2vdckTTYeZyYZyre3AtDweIc-FtJD2Uvkb19h8rXMlfTfQo9yPLfwxknow_YS8CkCLrOASlm-15oWrVguP4slxT05no8ub6b2T0vOC-QYpEy9o1PMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش دقیقاً همون چیزیه که نیاز دارید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/iaghapour/2678" target="_blank">📅 19:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
دسترسی مستقیم و بدون واسطه به اینترنت آزاد
🔹
کافی است آدرس subscription را در برنامه v2rayN/v2rayNG وارد کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
— نکات استفاده
👇🏻
۱. کانفیگ سرورلس برای اجرا نیاز به هسته Xray-core حداقل ورژن 26.6.1 دارد (حداقل v2rayNG v2.2.3)
۲. سرویسها و سایتهایی که ip آنها به طور کلی از سمت ایران بلاک شده با این روش مستقیم قابل دستیابی نیستند، همچنین از آنجایی که سرویسهای خارجی ip ایران را مشاهده میکنند، سرویسها و سایتهایی که ایران را تحریم کرده اند نیز با این روش مستقیم قابل دستیابی نیستند.
۳. در تنظیمات v2rayNG دقت کنید که Enable Hev TUN FEATURE فعال باشد و همچنین پورت پیشفرض 10808 را تغییر نداده باشید.
۴. از آپدیت بودن فایلهای جئو مطمئن شوید (قسمت Asset files در برنامه v2rayNG و قسمت Help-Check Update در برنامه v2rayN)
۵. برای تجربه بهتر پیشنهاد میشود IPv6 خود را فعال کنید (در تنظیمات v2rayNG تیک Enable IPv6 را بزنید و همچنین در صورتی که از اینترنت همراه استفاده میکنید باید IPv6 را در قسمت Access-Point گوشی خود فعال کنید)
۶. در اندروید برای عدم تداخل با (dns و sniffing) کانفیگ بهتر است Private DNS در تنظیمات اندروید و Use secure DNS در تنظیمات کروم خاموش باشد.
۷. از کانفیگها تست نگیرید، نتیجه‌ی تست ارتباطی با کار کردن یا کار نکردن این نوع کانفیگها ندارد.
🟢
به گفته یکی از بچه ها با روش زیر میتونیدمتصل بشید:
کاربر اگر فیک دی ان اس رو از تنظیمات برنامه روشن کنه سرویس هایی که آیپی ایران رو محدود و مسدود کردن مشکلش حل میشه و سایتا بالا میان.
⚠️
برای کارهای حساس از این روش استفاده نکنید!
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/iaghapour/2677" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✍🏻
دوستان، در حال حاضر بیش از ۷ اسکریپت (شامل اسکریپت‌های تانل و روش‌های مستقیم و رایگان) رو در دست بررسی داریم. هر کدوم که بدون مشکل جواب بده رو توی یوتیوب معرفی می‌کنیم. اما مواردی رو که به هر دلیلی (مثل محدودیت‌های دیتاسنتر سرورهایی که استفاده میکنیم و...) نتونیم خودمون ازشون جواب بگیریم، داخل کانال تلگرام معرفی میکنیم تا شما بتونید تست کنید.
ممنون از حمایت همیشگی شما.
💚</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/iaghapour/2674" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واقعاً باید درِ این بانک‌های مزخرف رو گل بگیرن! سالی ۳ بار یا هک می‌شید، یا اپلیکیشن بانک کار نمی‌کنه، یا اختلال دارید و هزارتا کوفت و زهر مار دیگه! آخه مگه می‌شه بانک این‌همه بی‌در و پیکر باشه؟
😒</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/iaghapour/2673" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3VWdif537vG_jRtBXi6V7vge1Byd1xBQFi3jX0UEStmmdy1ungHWn7sKytzwdeBbCaWXoifVnrIKgicP16Vs9IcPzSDQ4AQt5OTFqSFpAa_gNL-tN7uiR_iAa4mKq6aL9X6uibouue54kwCdhKABklcujkqiV2jqlRRPx-WxZanpSGv9lJ6BwiqvuZmN6dtTgncOGsC3zzlvwghyI4L9ufKGcAD2kCDDNIkHBYlYnzUA5mkFx7lROsuMUa65pRF62kePD8JWJFgiD8q3H6B8r_Ha_i-uWK9-I8PdplAFAEas27ICmrf4-OyE1FBqFLB-HVEU4AvxxeaLva-YU1riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
درخواست حمید رسایی و ۱۱۹ استاد برای انحلال «ستاد ویژه فضای مجازی»
بیش از ۱۲۰ تن از اساتید حوزه و دانشگاه، و چهره‌های سیاسی از جمله حمید رسایی در نامه‌ای به رئیس قوه قضائیه و فقهای شورای نگهبان، خواستار ابطال فوری مصوبه دولت برای تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی» شدند.
🔹
مهم‌ترین دلایل مخالفان:
🔸
تشکیل این ستاد ناقض جایگاه «شورای عالی فضای مجازی» به عنوان تنها نقطه کانونی سیاست‌گذاری است و یک ساختار موازی محسوب می‌شود.
🔸
به اعتقاد نویسندگان نامه، رئیس‌جمهور صلاحیت ایجاد نهادهای فراقوه‌ای با کارکردهای کلان حاکمیتی را ندارد.
🔸
واگذاری اختیار محدودسازی اینترنت به ستاد جدید، با صلاحیت قانونی (کمیته فیلترینگ) و دادستانی کل کشور در تعارض است.
🔸
ایجاد این ساختار جدید، مصداق تشکیلات غیرضروری بوده و تنها باعث افزایش لایه‌های تصمیم‌گیری در فضای مجازی می‌شود.
پ.ن: جالبه تو این مملکت انگار با فساد و رانتِ کسی کاری ندارن؛ اما وای به روزی که بخوان اینترنتی رو که دست مفسدها رو رو می‌کنه، یه ذره آزاد کنن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/iaghapour/2671" target="_blank">📅 21:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkau7uSR6etdZoT8yZJWZHvus1p9e6AdNu9JUAYdbDJ4ofqKGWal5poxDWSyz1sU3cKgGrkNMTwqdinyVEuK8WvxV1fK9YNHvQ2KQVC3ULLYejpTqVe6DdcgjrXkhvPPnegGBY3n-gSrCIr3PiLJTvXrNaqyB--OPvnFsY5iSQTtPCsRUg3N7mF3CqN7Le0FmN7EVPLzlCBsxOAjatmWt4kOmxXQ0K--pZLjt4q-8PqgpxkxUCH9PRDxvjqq2KhXu5Xibn5MMSqSCvKzzmQTGQcWS63Szcc14-s5zgDaa-NLPXLJdJf55LxuqtSBm7Z_0IBKl9ioeQITEvsA4n4NsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وزیر ارتباطات: محدودیت‌های اینترنت شفاف و زمان‌دار می‌شود / خسارت روزانه ۱۵ میلیون دلاری قطعی‌ها!
ستار هاشمی، وزیر ارتباطات در نشست خبری خود با انتقاد از وضعیت فعلی گفت: «در عصر هوش مصنوعی، دردناک است که هنوز دغدغه وصل بودن اینترنت را داریم.» وی تاکید کرد که قطعی اینترنت در فضای غبارآلود شایسته مردم نیست و سازوکار اعمال محدودیت‌ها باید تغییر کند.
🔹
چکیده مهم‌ترین صحبت‌های وزیر ارتباطات:
🔸
شفافیت و زمان‌بندی:
از این پس اگر قرار است محدودیتی ایجاد شود، باید مشخص باشد کدام نهاد و کمیته آن را تصویب کرده و
دقیقاً تا چه زمانی
ادامه دارد.
🔸
خسارت نجومی:
بر اساس گزارش مجلس، کشور روزانه ۱۵ میلیون دلار از قطعی اینترنت آسیب می‌بیند.
🔸
عادی‌شدن فیلترشکن‌ها:
استفاده از VPN که در گذشته قبح داشت، به دلیل سیاست‌های اشتباه به یک رویه عادی و روزمره برای کاربران تبدیل شده است.
پ.ن: وزیر مشکلی با محدودیت و قطعی نداره بیشتر داره میگه شما که داری قطع میکنی بگو تا کی که مردم اطلاع داشته باشن :)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/iaghapour/2670" target="_blank">📅 21:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlZYpz3kbEAq5UoVTcaFOqbup12m9kvekCucxW2d2vqvCiACw4iqICgjHG2_ywTBjfOVFYIZOAR3V8FfQwxtkbGP9vOE3VVNd5LboQsGVk9JAJFWHCBibUIyu5H_zIPg3X-dyvY1pYVCsARkIcAe1S8aE1NzC1r1VCWcjIR8-1fmo2pmLwxVyTapowkZJk5UV7gSJ7J3mpCOnhdBai3Y91Sj8tm5WknFvRFY4wCXjxRX-HAs0EUnS4sPbu7J2HePJIE6EKLRLbAW-FTInlBqlFA0a5Cre5Gc8VLpdXixK9im4cfTt-NaWMceYRq7UyCmExYJLWxyNjiCRfI-8_YFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای ساخت فیلترشکن شخصی با ۲ هسته در پنل پاسارگارد
🔥
🔹
تو این ویدیو قراره با هم یاد بگیریم چطوری یه فیلترشکن شخصی فوق‌العاده با استفاده از پنل پاسارگارد بسازیم. این پنل از 2 هسته Xray و وایرگارد ساپورت میکنه و همینطور از قابلیت نود هم پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پاسارگارد
#pasarguard
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/iaghapour/2668" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=GSPLsygm3DhfezabMqy9w1AAk5l3vnPd-4wREJ55e1BD37Y2Fd6BQrOAwtQt8C2TQQWY92H58VTu5BUuAU0awhc9yV5oCVLu3jCgXsb5lgz2j15VbEKJyo_pSTJFHl0wOhxQ0dGAYpulnsJd_6_uyU801fIR7vw5VdtuR6NudmbliGz05CGcsDkKKS3XpCS1p2cVC53CKD54etswTlXiI0_8Am1OsC-sCQnio4SEIosgvakmOLQSvfzp7aDPu4buRbhVjN0I_6Qb7EhnUspR822fuG3b9nfEQZ9pEboWU9gREit8EhDVYlq3Uh3a-A46YZBBILw75QmYkqu54dmWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=GSPLsygm3DhfezabMqy9w1AAk5l3vnPd-4wREJ55e1BD37Y2Fd6BQrOAwtQt8C2TQQWY92H58VTu5BUuAU0awhc9yV5oCVLu3jCgXsb5lgz2j15VbEKJyo_pSTJFHl0wOhxQ0dGAYpulnsJd_6_uyU801fIR7vw5VdtuR6NudmbliGz05CGcsDkKKS3XpCS1p2cVC53CKD54etswTlXiI0_8Am1OsC-sCQnio4SEIosgvakmOLQSvfzp7aDPu4buRbhVjN0I_6Qb7EhnUspR822fuG3b9nfEQZ9pEboWU9gREit8EhDVYlq3Uh3a-A46YZBBILw75QmYkqu54dmWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
چرا عنوان ویدیوهای یوتیوب یا زبان ویدیو برای بعضی‌ها انگلیسی شده؟!
سلام رفقا! جدیداً خیلی‌ها پیام دادید که چرا با وجود فارسی بودن ویدیوها، عنوان و توضیحات کانال رو به انگلیسی می‌بینید. یا اینکه حتی زبان ویدیو هم انگلیسی شده.
علت چیه؟
تقصیر هوش مصنوعی یوتیوبه! اگر زبان گوشی، لپ‌تاپ یا اکانت گوگل شما روی انگلیسی تنظیم شده باشه، یوتیوب به طور خودکار عنوان‌های فارسی و حتی زبان ویدیو رو براتون به انگلیسی ترجمه می‌کنه.
🛠
راه حل سریع فارسی کردن یوتیوب:
👇🏻
در اپلیکیشن موبایل:
🔹
وارد برنامه یوتیوب بشید و روی عکس پروفایلتون بزنید.
🔹
آیکون تنظیمات رو لمس کنید.
🔹
وارد بخش General و سپس App language بشید و زبان رو روی فارسی بذارید.
👇🏻
در نسخه وب (کامپیوتر/مرورگر):
🔹
سایت
YouTube.com
رو باز کنید.
🔹
روی عکس پروفایلتون در بالا سمت راست کلیک کنید.
🔹
گزینه Language رو انتخاب کرده و اون رو روی فارسی بذارید.
🎙
حل مشکل صدای انگلیسی (دوبله خودکار):
اگر وارد ویدیو شدید و دیدید صدای من انگلیسی شده، روی علامت چرخ‌دندهِ خودِ ویدیو بزنید، وارد بخش Audio track بشید و اون رو روی Original (فارسی) بذارید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2667" target="_blank">📅 16:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4YNCSBVODKDsgIve4U8KtJZ5QiqniodrFog91qFL6KHeEPo8i3NO-RFpJL5DTZVAEfmQYYvo0XGHyeTkHnKAB_3W5mY0UEm8WRocCdFJEQEC3mWMwALL1mirzukf99l--MhdGiJW-EEjsugl_SmEEocKzUOgngyIxlkhr7AYvbGAU9DSnaU4HG5LqEO8c_o0vv5nVxL5AsyJwpSjY3KJgSWfNQ9NsTmwQbsDQPlOAkoAZ9t2ryKFaJYEY7TZpIOVYLTGbjEqVqy-BLZyhwW02TcQYdcGXP_WPNm-N3SccV4cT6Emn9A0YMXzaHhqZk3TMYhsRSClLx6Br0tA9Z1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پولی شدن پیامک فعال‌سازی تلگرام برای برخی پیش‌شماره‌ها!
🔹
تلگرام در جدیدترین به‌روزرسانی‌های خود، سیاست سخت‌گیرانه‌ای را برای ثبت‌نام یا ورود کاربران در برخی از کشورها و پیش‌شماره‌های خاص اعمال کرده است. طبق گزارش‌های کاربران و تصویر منتشر شده، بخش جدیدی به نام
SMS Fee
به اپلیکیشن اضافه شده است.
❓
ماجرا چیست؟
تلگرام اعلام کرده که به دلیل بالا بودن آمار ساخت
حساب‌های جعلی (Fake Accounts)
و همچنین
هزینه‌های بسیار سنگین ارسال پیامک بین‌المللی
در برخی از کشورها، کاربران این پیش‌شماره‌ها باید هزینه پیامک ثبت‌نام خود را پرداخت کنند.
💵
کاربران برای دریافت کد تأییدیه مجبور هستند مبلغ
۱ دلار
پرداخت کنند. تلگرام این پرداخت را در قالب
خرید اشتراک ۱ هفته‌ای تلگرام پرمیوم (Telegram Premium)
ارائه می‌دهد.
پی‌نوشت: این محدودیت فعلاً برای تمام شماره‌ها نیست و تنها روی اپراتورها و کشورهایی که هزینه‌ی مخابراتی بالایی دارند یا سوءاستفاده از آن‌ها زیاد است، فعال شده. خوشبختانه
#ایران
تو این لیست نیست ولی اگه از شماره های مجازی استفاده میکنید باید حواستون به این موضوع باشه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/iaghapour/2664" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه چیزی میگم شاید باورتون نشه.
مردم الان بیشتر از اینکه نگران جنگ باشن نگران قطعی دوباره
#اینترنت
هستن.
کسب و کارهای آسیب دیده تا میان دوباره سرپا بشن اینترنت رو قطع میکنن یا اختلال میندازن و....
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2663" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9iLAhnNBC-k2kKfHnbMiZGSZI9j7PEs5znv2Y3X63b9V4TriWsTkCGKQtQtb7da2VqsOgle7dmRokRi8g6kjPWBIAmuRI9ETqkl1TSpYHoSpAMvxLcS5pc6GZ2qP45USIBIFCc9B6Z_L2DVnmXGxwjs-aAT9lJNHy5kxeP57wkGoaxEN76gqvzmdEtWTLYR01cPmHnY8yRc4t6cf3rS99Q8TDyQcVTvp2M1H-avFapdJjDroCPXlcLA83SlmKxVIC2ISZY_5KfFenAeO6d0QfRNwXlNDyBl2aTpdL4MEg7mcLPMKYVIxiU78_sbmo0qUknKjZACwe7i03HzEBNmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیرعامل آسیاتک: اینترنت دیتاسنترها هنوز وصل نشده است!
محمدعلی یوسفی‌زاده اعلام کرد اینترنت کاربران وصل است اما مراکز داده دسترسی کامل ندارند و شبکه به وضعیت عادی برنگشته است.
فقدان پاسخگویی:
پیگیری‌های زیادی انجام شده، اما مسئولان هیچ دلیل یا پاسخی برای این قطع بودن ارائه نمی‌دهند.
⚠️
مشکل اصلی چیست؟
اینترنت کاربران با اینترنت دیتاسنترها مسیر متفاوتی دارد. در حال حاضر کاربران به سایت‌های داخلی دسترسی دارند، اما
سرورِ خود این سایت‌ها
در دیتاسنترها به اینترنت جهانی وصل نیستند.
—
نتیجه این اختلال:
قطع شدن اتصال سرورها به ابزارهای حیاتی خارجی مثل گوگل، کلادفلر و گیت‌هاب (APIها).
— عدم امکان آپدیت، دسترسی به ریپازیتوری‌ها و سرویس‌های ابری (CDN).
📌
نتیجه:
اینترنت دیتاسنترها قطع است؛ یعنی پلتفرم‌های ایرانی از پشت صحنه به جهان متصل نیستند و زیرساخت فنی آن‌ها عملاً فلج شده است.
پ.ن: البته از وضعیت دیتاسنترهای دیگه اطلاعات زیادی در دسترس نیست.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/iaghapour/2661" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBhUj8P9N1wVDtsnuX1zishUzAC8ROyc2EVh8yhpETe4FaBL5MNhkhHFxkKjW-ycqfMv5cgHHt3IyqmZtRBW1kFV0vpp4dvdfJ5E7jVPidzNZue22ZXIXEojQgBMrDNLwaDZT3rFWyDsc9h3jEWuYsLyE_V1ITBOnaG07Fe7eKGW5tZijT0c8ALNDxhQB0o--mzXeXdXCVWODHzg3lQ5G-oOSbi7SsNO3Tnz3wbYcKbrX0fACA7uCkB8jZFqsaLXgnBnWVCDsIkfZOggTs4It08GuWidr8b1wxa_sCktlhfTLjjXhaoSyI15O4YdqRMzBJxO3UkIGRnV_OzmSyrb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرقت بی‌اجازه ترافیک کاربران؛ پشت‌پرده دسترسی ناگهانی به کلاد و اسپاتیفای چیست؟
دسترسی ناگهانی و بدون VPN به پلتفرم‌های تحریم‌شده‌ای مثل
کلاد (Claude)
و
اسپاتیفای
، حاصل لغو تحریم‌ها نیست؛ بلکه نتیجه
دستکاری پنهان و بدون اجازه ترافیک کاربران
توسط زیرساخت اینترنت کشور است.
🔍
لایه‌های فنی و عملکرد
روش کار:
دولت ترافیک کاربران را به سمت سرورهای خود هدایت کرده و از آنجا به مقصد پروکسی می‌کند. کارشناسان این کار را مشابه
حملات هکری DNS
می‌دانند که پیش از این در سرویس‌های رفع تحریم (مثل شکن و ۴۰۳) اما این‌بار به صورت اجباری و پنهانی اجرا می‌شود.
امنیت داده‌ها:
به دلیل پروتکل‌های امنیتی، دولت توانایی دیدن محتوای پیام‌ها (مثلاً چت با هوش مصنوعی) را ندارد و فقط می‌تواند ببیند کاربر از چه سرویسی استفاده می‌کند.
⚠️
پیامدها و خطرات
خطر مسدود شدن اکانت‌ها:
ارسال انبوه درخواست‌ها از چند آی‌پی مشخص، پلتفرم‌ها را حساس کرده و ریسک مسدود شدن حساب را بالا می‌برد.
اختلال فنی:
این دستکاری باعث قفل شدن مداوم اکانت‌ها در سایت‌های تخصصی و افت شدید کیفیت VPNهای اختصاصی (به دلیل پدیده تونل در تونل) می‌شود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/iaghapour/2660" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAXTydaR9edDIsziG8SHPYhr26Y6XOU7QZle3PlVdWfgbbmlYvp5-MeejuigHEikuPU3IG3Yu3cDevKhnqFsjwBJoPaxjF5kJwDC9QvPOoZG83DV7bAxS8dCYzNOCdmHo_NK9WwdTQH8dVgOvkKJzpZFBH6N1fKAQczIHM0oS2jOXhj2j3b-B-CSLu7XZ0j1xgR6pabJNJTVZrRdLxD8TilKzGWP4NwBFnhanfx0baydb4WHschs6HNQvJ75ZdYgTl0tPO6zJP4B8f02RT3Upu8xLik5FbRnm0-U44M-z6Bm8ozC_mcAbwXiLrOQDmZbnBeb27wVB4DFiMW6hKkkNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب خودکار داکر روی سرورهای ایران
اگر روی سرورهای داخل ایران داکر نصب می‌کنید، حتماً می‌دانید که به خاطر تحریم‌ها و اختلالات شبکه، باز کردن مخازن داکر و دانلود ایمیج‌ها مکافات است. این اسکریپت متن‌باز و امن، کل فرآیند نصب داکر را خودکار کرده و در انتها به شما اجازه می‌دهد از بین ۶ میرور ایرانی (ابرآروان، داکر آی‌آر، لیارا و...) بهترین را برای رفع تحریم انتخاب کنید.
💻
روش اجرا: کد زیر رو کپی کنید و در سرور اجرا کنید:
curl -fsSL https://gist.githubusercontent.com/ShahinDadashpour/35892443c09d582e53b36d09fb5a5df6/raw/install-docker.sh | sudo bash
🔗
لینک سورس کد در گیت‌هاب جهت بررسی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/iaghapour/2659" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0ZE75tkQ_jSU5t-HN6o4_JklUjzfizwY_vTWmsElV61Oydk4zJIwLnPF2LYDUuSGgEtVz6UDToZNTxJQIUQtabVdZV4_5h48Gh5Pkv6ws6MSJoAbx1f1fIwN0O5xb-YyuRDfMk5rkQcKzz866DSJiCSGhr0AyNdb2oWyQDDgGVYV0hPz3VHFHPFsyv7TWm2dTet8-ddd_M83zY2col9L8R_LqF7gYls7GFOzpnx2kFoolJsCCVo0nhRtI81pZhwQP4b2Y-Un_h9K0GLWnwZe0rT0J6IrteBFHSoDfpG1OJedlBc_aiUcTN1bzMeJ8zQMTi0gcleKmL1yNU1MXl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن بدون تانل و بررسی روش های موجود
🔹
خیلی‌ها فکر می‌کنن برای داشتن یک فیلترشکن شخصی حتماً باید درگیر دردسرهای تانل زدن بشن، اما تو این ویدیو تمام روش‌های موجود رو بررسی کردیم و بهتون آموزش دادم چطور بدون نیاز به تانل، یک فیلترشکن پرسرعت بسازید.
👇
در این ویدیو به چه مواردی اشاره شد:
— چرا تمام روش ها منتشر نمیشه؟
— چه روش هایی در شرایط سخت کار میکنه؟
— آموزش روش مستقیم ساخت فیلترشکن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ملی
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/iaghapour/2657" target="_blank">📅 18:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdHTOpKCY-o80XmEicR4_QCYfllLen16BTQjF1P_OMF5O0ngL-ZgTV0vrNNJof0eRBsTJNstpUYe-iEsRsQF468RKFJd9jxKkxtGxGDXfK8aI-l_huEmeqeKNtGCY4s4YYmI4GlcqaYCVYKPxmj2PkhXqmTXjs0WUPMNpZIeOwa923m5yx0n_eH3oZrCGAYrIzrsfXRJTg4ld4C6X_A24AaoUTfDEk563Ay5Z6QrgpAT2sjrStXhNkC7rQYfz-4RfT6RRZ-vP1DDlXkfkN4rbCLyKEYjYr-Tgw7xB1fQlnyn1OxqR7JLHGVSY4YDR4AUYtkqj-UwYLQhkVu0zSohGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بلوکه شدن ارز دیجیتال در خریدهای خارجی (CoinGate)
دوستان، یکی از کاربران هنگام خرید از سایت
Hostinger
با ترون از طریق درگاه
CoinGate
، متأسفانه به دلیل تحریم‌ها پولش مسدود شده است. طبق اعلام رسمی پشتیبانی این درگاه، به دلیل قوانین بین‌المللی، وجه بلوکه‌شده
به هیچ‌وجه ریفاند (برگشت) داده نمی‌شود!
⚠️
چرا شناسایی می‌شویم؟
درگاه‌های خارجی تراکنش‌ها را رهگیری می‌کنند. اگر IP شما نشت کند یا ارز را مستقیماً از صرافی‌های ایرانی به کیف پول خود (مثل تراست ولت) منتقل کرده باشید، به راحتی به عنوان کاربر ایرانی شناسایی می‌شوید.
✅
راه‌حل و پیشگیری:
—
هرگز
مستقیماً از صرافی ایرانی به درگاه‌های خارجی واریز نکنید.
— همیشه از
کیف پول واسط
استفاده کنید (ارز را از صرافی ایرانی به ولت اول، سپس به ولت دوم بفرستید و در نهایت از ولت دوم خرید کنید).
— هنگام پرداخت، حتماً از IP ثابت و معتبر استفاده کنید تا نشت IP نداشته باشید.
لطفاً این پیام را به اشتراک بگذارید تا سرمایه سایر دوستان به خطر نیفتد.
🙏
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/iaghapour/2656" target="_blank">📅 17:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
دو نکته خیلی مهم برای شما دوستان عزیز
سلام بچه‌ها! امیدوارم حالتون عالی باشه. برای اینکه بتونم تو کانال بهتر راهنماییتون کنم و محتوای باکیفیت‌تری براتون بسازم، نیاز دیدم این دو تا نکته مهم رو باهاتون در میون بذارم:
۱. درباره سوال پرسیدن از ویدیوهای قدیمی
:
همون‌طور که می‌دونید تعداد ویدیوهای کانال زیاده و واقعیت اینه که من مو به مو یادم نمی‌مونه تو ویدیوهای ماه‌های گذشته یا سال‌های قبل، دقیقاً چه مواردی رو پوشش دادم یا چه جزئیاتی رو گفتم. پس اگر درباره یک ویدیوی قدیمی تو کامنت‌ها سوالی براتون پیش میاد، لطفاً
خیلی دقیق و با جزئیات
بپرسید. اگر ممکنه، مشکلتون رو کامل توضیح بدید یا حتی تایم‌لاین (دقیقه و ثانیه) اون بخش از ویدیو رو بنویسید تا سریع متوجه موضوع بشم و بتونم جواب درستی بهتون بدم.
۲. درباره تست روش‌های تانل
:
نکته دوم در مورد آموزش‌های تانلینگ هست. ببینید بچه‌ها، وقتی ما یک روش تانل رو معرفی می‌کنیم، منطقاً امکانش وجود نداره که اون رو روی
تمام
روش‌ها و پروتکل‌های دیگه (مثل وایرگارد، OpenVPN و...) تست کنیم. خیلی وقت‌ها تو کامنت‌ها می‌پرسید که «آیا این تانل روی فلان پروتکل هم جواب میده؟» راستش ما هم اطلاع دقیقی نداریم؛ چون زمان و زیرساخت تست کردن یک روش روی تک‌تک سناریوها وجود نداره. بهترین کار اینه که خودتون اون روش رو روی پروتکل مدنظرتون تست کنید و اتفاقاً نتیجش رو تو کامنت‌ها بنویسید تا بقیه بچه‌ها هم از تجربه‌تون استفاده کنند.
ممنون که مثل همیشه درک می‌کنید و با انرژی خوبتون همراه کانال هستید!
❤️</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2655" target="_blank">📅 21:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رفقای عزیز سلام!
✌️
دارم روی یه ویدیوی خیلی کاربردی کار می‌کنم که سعی می‌کنم فردا یا نهایتاً پس‌فردا به دستتون برسونم. تو این ویدیو قراره به خیلی از سوالاتتون جواب بدم، ابهامات رو برطرف کنم و یه گپ و گفتی درباره شرایط فعلی داشته باشیم.
ضمناً خواستم یه تشکر ویژه بکنم بابت تمام حمایت‌هاتون؛ چه کامنت‌های پرانرژی‌تون تو یوتیوب و چه حضورتون تو شبکه‌های دیگه. مرسی که با تماشای ویدیوها (و صبوری کردن برای تبلیغات!) از کانال خودتون حمایت می‌کنید تا بتونیم با قدرت بیشتری به کارمون ادامه بدیم. دمتون گرم!
❤️</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/iaghapour/2652" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-text">⭕️
کدهای مخفی چت جی‌پی‌تی؛ ۸ ترفندی که پاسخ‌ها را متحول می‌کند!
بیشتر افراد از چت جی‌پی‌تی فقط مثل یک موتور جستجوی ساده استفاده می‌کنند و پاسخ‌های کلیشه‌ای می‌گیرند. اما کاربران حرفه‌ای می‌دانند که با اضافه کردن چند فرمان کوتاه، می‌توان نحوه تفکر و خروجی این هوش مصنوعی را کاملا تغییر داد.
🔹
ساده‌سازی مفاهیم (ELI5):
اگر موضوع علمی یا پیچیده‌ای را متوجه نمی‌شوید، در درخواست خود بنویسید «توضیح بده مثل اینکه ۵ ساله هستم (ELI5)». چت جی‌پی‌تی تمام اصطلاحات تخصصی را حذف و موضوع را به ساده‌ترین شکل بیان می‌کند.
🔸
استخراج چکیده (TL;DR):
اگر حوصله خواندن یک مقاله یا ایمیل طولانی را ندارید، متن را ارسال کنید و در انتها بنویسید «خلاصه کوتاه (TL;DR)» تا در چند جمله لپ مطلب را بگیرید.
🔹
خروجی جدولی (FORMAT: TABLE):
به جای دریافت پاراگراف‌های نامرتب، مثلا هنگام مقایسه دو محصول، عبارت «نمایش به صورت جدول (FORMAT: TABLE)» را اضافه کنید تا اطلاعات کاملا منظم و خوانا تحویل داده شود.
🔸
کشف نقاط ضعف (DEVIL’S_ADVOCATE):
یک ایده کاری دارید؟ با اضافه کردن عبارت «وکیل مدافع شیطان»، هوش مصنوعی تمام دلایل احتمالی شکست ایده و نقاط ضعف آن را بی‌رحمانه به شما گوشزد می‌کند.
🔹
درخواست اطلاعات ناقص (MISSING_INFORMATION):
به جای اینکه هوش مصنوعی با اطلاعات کم شما یک جواب ناقص بسازد، عبارت «ابتدا اطلاعات ناقص را مشخص کن» را بنویسید. با این کار، چت جی‌پی‌تی ابتدا سوالات ضروری را از شما می‌پرسد تا دقیق‌ترین خروجی را بسازد.
🔸
تحلیل گام‌به‌گام (CHAIN_OF_THOUGHT):
با استفاده از دستور «تفکر زنجیره‌ای»، هوش مصنوعی مجبور می‌شود مراحل استدلال و حل مسئله را قدم‌به‌قدم به شما نشان دهد که خطای منطقی پاسخ‌ها را به شدت کم می‌کند.
🔹
شبیه‌ساز مصاحبه شغلی (MOCK_INTERVIEW):
با نوشتن دستور «مصاحبه شبیه‌سازی‌شده برای موقعیت...»، چت جی‌پی‌تی نقش یک مصاحبه‌گر را می‌گیرد، مرحله‌به‌مرحله از شما سوال می‌پرسد و پاسخ‌هایتان را ارزیابی می‌کند.
🔸
ریست کردن حافظه (IGNORE_PREVIOUS):
وقتی مکالمه طولانی می‌شود و هوش مصنوعی گیج می‌زند، با فرمان «بازنشانی دستورهای قبلی» به او بگویید کل پیام‌های قبلی را نادیده بگیرد و با یک نقش جدید شروع به کار کند.
با استفاده از این دستورات ساده، می‌توانید هوش مصنوعی را از یک ربات پاسخ‌گوی ساده، به یک مشاور، تحلیلگر و همکار حرفه‌ای تبدیل کنید.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/iaghapour/2650" target="_blank">📅 22:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgxfHx3gr5_WpfZ09X7ZfxVU6k8AI1BmQ4zr2R-BoVLjwgNo2OV5xkHAqR-N-nXnnyfFfUe-qWIArOEBeRi_ZSfBOFYy19-oDwWoy7T_g__4XPYT_9Gz_ZMZmHVxXEOWqOmWvIEkgFnTjJtO36ktVwFhH52aX-AjfcQ6t9kRRO5tSH8qs3F8CR7QOOjfQqJsGYNbz9t3KB9u_K3MyC_9JBkTN_m-afqjKBLkq8wvjrmBLN169S93myBeXVT4Yxxhct-4s-4EYZrhpsjJ4ZeZdndzGIpleOhSz6VRmIO33PU8aoOQHCUovib_Y_q92Ckf01V4Yr4V284W3sIRT-mN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی GenyConnect؛ جایگزین مدرن v2rayN برای مدیریت پروکسی
نرم‌افزار GenyConnect یک کلاینت تونلینگ و VPN مدرن (با کاربردی شبیه به برنامه محبوب v2rayN) است که با تمرکز بر عملکرد بالا، حریم خصوصی و کنترل دقیق ترافیک طراحی شده است. ویژگی مهم این ابزار، وابسته‌نبودن به یک پروتکل خاص است؛ به این معنی که می‌تواند به عنوان یک بستر یکپارچه برای موتورهای مختلف تونلینگ عمل کند.
🔹
مسیریابی پیشرفته:
امکان تعیین مسیر ترافیک بر اساس لیست سفید، دامنه‌های خاص، و حتی مسیریابی در سطح اپلیکیشن‌ها و پروسه‌های سیستم.
🔸
سبک و شفاف:
این ابزار با کمترین مصرف منابع سخت‌افزاری کار می‌کند و اطلاعات کاملی از وضعیت شبکه، لاگ‌های زنده و آمارهای لحظه‌ای ترافیک را به شما نمایش می‌دهد.
🔹
انعطاف در پلتفرم‌ها:
برخلاف برخی کلاینت‌ها که فقط مختص یک سیستم‌عامل هستند، این برنامه به صورت یکپارچه برای
ویندوز، مک، لینوکس و اندروید
در دسترس است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/iaghapour/2648" target="_blank">📅 21:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW5nNofC81dIMoKyNlEjqlAjAtd152uXjv4UqFitbYArjTViIqV6OJD7iq41HCOu3g3PRYSZVnSRfG6WqMfj3uncjt72M66y3NI9e8f-awdS4YUYD_p8BJAp51HKGcxMm_eVLkswQgB45Gq-mYVeKWzksDkxLf5iliqA0zLC7viM8RWMA-79TXRYOoH6hTRIH8ZNEoJhDTKAPVNc9ToGRVkRJYTGFqHHz_ii_IO8OcsWf7cAULIIN6HVdv73FZeuAcaNTghC9jfA613NyOSUVj0_CNauH4t_SE9rOb0-AYZotiF32O9Z_3GpB21GXAJOgRDRQPnDBcJMfSH07oqTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تون‌کوین به (Gram) تغییر نام می‌دهد!
پاول دورف در کانال رسمی خود خبر بسیار مهمی برای کاربران و سرمایه‌گذاران شبکه TON اعلام کرد. بر اساس این اطلاعیه، ارز دیجیتال بومی این شبکه قرار است با یک ری‌برندینگ بزرگ، نام فعلی خود را کنار گذاشته و به نام اصلی و اولیه‌اش یعنی Gram تغییر کند.
نکات کلیدی که دورف در این پست به آن‌ها اشاره کرده است:
🔹
بازگشت به ایده اولیه:
دورف یادآوری کرده که Gram نام اصلی ارز شبکه در اولین وایت‌پیپر این پروژه بود. او این اتفاق را بازگشت به ریشه‌ها و شروع یک فصل جدید توصیف کرده است.
🔸
زمان‌بندی انتقال:
فرایند این تغییر نام و انتقال، حدود ۳ هفته زمان خواهد برد.
🔹
نام بلاک‌چین تغییر نمی‌کند:
با وجود تغییر نام ارز بومی (از Toncoin به Gram)، نام خود شبکه بلاک‌چین همچنان TON باقی خواهد ماند.
🔸
قدم چهارم از یک نقشه راه:
این ری‌برندینگ تنها یک تغییر اسم ساده نیست، بلکه به گفته دورف، راه را برای اتفاقات مهم بعدی هموار می‌کند و قدم چهارم از یک برنامه ۷ مرحله‌ای برای «عظمت دوباره بخشیدن به TON» است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2647" target="_blank">📅 21:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww_7TJiq1cuPRL0faiTGVR20pe9xdhkh8bgFn4NNGSD8naAvlaTWIsvY7FWF9i8nKmOiVYZsgvS7PInsEi9uB3snG_ZWUuOGVGkBNDsoxAZi2NFvkPYG8MqbJljHTDpIyJ8YCapdQRTCf6MmCE1RGN7HznDfSsVGD_bAhbivQaWeMaPa0QGpQzCWEuAoQ7Bb-DNDCcRuyvZKMUlmmhz5rLi1p6sXAsFeR-J2h7KDVOMZKRQ1nw7Fc9znuwDNAjXTP60cvarvsu-GDhvh8XW8-RSu9H1P2tWw17cpYl5aW253E17mlP3Ez20GnMejRI4hoAvf4_Bio7P_zYbXAmEInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اسکنر IP سفید کلودفلر با نوا رادار
🔹
نوا رادار یک
اسکنر IP دسکتاپ
است که با Wails v3 (بک‌اند گو + فرانت ری‌اکت/تایپ‌اسکریپت) ساخته شده. این برنامه رنج‌های IP کلودفلر را از منابع متعدد اسکن می‌کند، تأیید پروتکل واقعی (TCP + TLS handshake) انجام می‌دهد و IPهای سالم را مرتب‌شده بر اساس سرعت تحویل می‌دهد.
—
اسکن چندمنبعی
— ۹ منبع IP قابل انتخاب
—
تأیید دو مرحله‌ای
— اسکن سریع TCP → تست عمیق TLS
— مرتب‌سازی بر اساس سرعت
— قابلیت انتخاب پورت
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/iaghapour/2646" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IP List -- @iAghapour.zip</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/iaghapour/2644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
آی‌پی ها و فایل html مربوط به ویدیو
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/iaghapour/2644" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZYboPbRboqWdD0x9S-15ZNgFB57vr35wlSUEHTLRYPCTIijKXa_rXJPqlr1RlqUVcc6ul2MrnKtYGqb_ChSdUL5ntt3wMtZfA_28D5pa1l5yQEJAvE2e9b5WNbSE27Z7sJv4kVayfAwQ8NEeMLRRvP6MlcqIM-nd6BaYQL1ECWTOVjvPau279xPmYrVaDbzRmtuBZNq-WPhhgQGmRoeKkX8QDRMU7kPuxDUp2tupI_enSp8cfRKsp7J5rFTsCl3JB8aOUNN4ysPyXGHUsZXgMwQUYeSvYMTyBJ-AIPBpxDSk9fRcZd4idrAmWNe1HWyEWbVdSZOvFb0tlTYVGKwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (تست شده)
🔹
در این ویدیو به صورت قدم‌به‌قدم بهتون آموزش دادم که چطور با استفاده از Cloudflare Workers یک فیلترشکن کاملاً رایگان، و پرسرعت برای خودتون بسازید. این روش کاملاً تست شده و می‌تونید به راحتی روی گوشی و کامپیوتر ازش استفاده کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#پروکسی
#نوا
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/iaghapour/2643" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUj1YsdfOzdZP35hI_BdBj-cYoS065F6aIt-7VgzI68QT4zHwzqHedD-Hfgp3Fp8sEQsCYBO4Dsj_w2CdT-q1MwstwFXYmX4kkd_ZW58pMR0DVS91_vdUJiCLb2lGrvgj5q1-4F-4V7uisYVAHFBt1Odvm5X8lIh2ZaSnSHDlCP-V1tgwWN6Ko_xVRVlzQyij8HVMDlwfqsXTlapPjJjJ8kon4wzPZJMY14VxZzn6anzuB42JJwqZG5hGBrp1ttF6V8LjKRjXnFuPL6mAOHSSs6yabuugpRnAdrQCJ8PYXA3pd19IpLlbvwjm3D91j3Sjnw9V7PGa12t_Lq2Jx10vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ ویندوز ۱۱ منتشر شد؛ پرسرعت‌تر و هوشمندتر!
مایکروسافت به‌تازگی آپدیت جدید ویندوز ۱۱ (نسخه‌های ۲۴H۲ و ۲۵H۲) را با تمرکز بر افزایش سرعت و هوش مصنوعی منتشر کرد.
مهم‌ترین تغییرات این به‌روزرسانی:
🔹
اشتراک‌گذاری صدا:
امکان اتصال هم‌زمان دو هدفون بلوتوثی مجزا به یک سیستم برای تماشای فیلم یا گوش دادن به موسیقی.
🔸
دوربین مشترک:
دسترسی هم‌زمان چند نرم‌افزار به وب‌کم بدون مسدود شدن تصویر.
🔹
افزایش سرعت و جستجو:
ارتقای چشمگیر سرعت منوی استارت و اجرای برنامه‌ها، به همراه امکان پیدا کردن سریع فایل‌ها با جستجوی تنها دو حرف.
🔸
پایش هوش مصنوعی و باتری:
نمایش دقیق میزان مصرف پردازنده عصبی (NPU) در تسک‌منیجر و بهینه‌سازی مصرف انرژی لپ‌تاپ‌ها در حالت استندبای.
این آپدیت با رفع خطاهای ناگهانی و بهبود سیستم امنیتی Windows Hello، تجربه بسیار روان‌تری ارائه می‌دهد و در ژوئن ۲۰۲۶ به‌صورت خودکار برای همه کاربران فعال خواهد شد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/iaghapour/2642" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2640" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaoRPHQ9_ywsyPJKL5l56uL2bSVSiOQxyJa4VO73aoYtx-OjT5iV_ELEHVAeI_UvHU3YPFcBSYOFysAptpHDHKXcGD8m_YI5UpXcn4GkKfHsvoPAiZqMoC901WTpD8-mq39oPeYEi6yaX2ZKiLCAzOoCbYGzIilh7KaonbEGBehf7YoF2mXnrYNMW3pLvNn5EXgn3W5Ft8YeTVAFC-Mp4GcEweA2ubtOM5GiN5mTpLiHTDW90M5fVYfzQM4ymzZj6BLx3udlfZdamBhgAxJ85Bpy0zxRIAuir_PAQQir8S30F8ieTkMjWMjWU3PZvcJJCDh4t90GdtdrFiCcKklVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران در حال برگشتن به تلگرام
😀</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/iaghapour/2639" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💢
وضعیت اینترنت جوری شده که وقتی نت ملی بود فیلترشکن ها راحت تر متصل میشدن!
راستی گوگل پلی و اپ‌استور در دسترس قرار گرفتن و البته ویندوز آپدیت و...</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/iaghapour/2638" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/iaghapour/2637" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
بچه ها میگن انقدر پهنای باند دیتاسنتر ها پایین هستش که اکثر روش های تانل که اجرا میکنن سرعت بدی داره یا دچار قطع و وصلی و اختلال زیاد هستش.
خیلی به روش تانل بستگی نداره بیشتر مشکل پهنای باند ضعیف دیتاسنتر ها مربوط هست.
امیدوارم در روزهای آینده وضعیت بهتر بشه.</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/iaghapour/2636" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">میبینم که رو فیلترشکن ها تخفیف زدن :)
هر گیگ رو 10 و 20 هزار تومن دارن میفروشن :)
پولی که بعضی از افراد به جیب زدن تاجر ها نزدن. طرف داخل سرور ایران سایت فروش فیلترشکن داشت! قعطی نداشت. بالای 10 هزار ممبر داشت. اوایل حتی درگاه ریالی داشت. بعد بعضی ها انتظار دارن ما باور کنیم اینا به جایی وصل نبودن!</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/iaghapour/2634" target="_blank">📅 21:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
چند خبر کوتاه از رسانه ها
🔸
معاون وزیر ارتباطات در پاسخ به زومیت در خصوص زمان بازگشایی اینترنت سیار نیز گفت: «امروز اینترنت همراه نیز وصل خواهد شد.»
با توجه به این اظهارنظر باید منتظر بازگشایی اینترنت همراه تا پایان امروز، سه‌شنبه ۵ خردادماه، در دسترس کاربران قرار بگیرد. هم‌چنین، طبق اعلام‌های قبلی، تا فردا روند بازگشایی اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴ تکمیل خواهد شد.
🔹
نت‌بلاکس بازگشت بخشی از اینترنت ایران را تایید کرد؛ سطح اتصال به ۳۴ درصد رسید
🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/iaghapour/2633" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

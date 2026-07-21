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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 156K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ9s0Ohdz1jEIC1F61UYpsl_265973s48YbwBdQjFM-vQQOovOWaz1BERMOFYn4pXieuhuu1ovU8CBE0PIIfTM8qTrf1PX2R0YUziBa80ZUBOFB42PtQKeFG8avMIoYCVCJSGTuquOqGVhm0tv-VES_ywpZLkZsb688ez6Q-gRW_2y6fBvl7Ju08iQNoQfnJpQhgPslmvVwjAk5MPgLbGQBJPE83f6SrynPFjIHv0fqNGj6kM90cAyLRTpDFZSLuYDZCeDv9RSfAsdbuwhw1cptFWhdVpMCslk-Ae-leSi3cAekLFlXSJzeCeVpgdq5BWy8vPDduTldIo6QE261u1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZltrDHXVt6guSPd7QYKmGg56E2dhqGI6cW8lQ6gyiIxBHLWhhGYOGOIvQYGCGN7Pzj0Zt_o9H1oSJGoCnWeizOk0hI44f6XdHGFn81TDSS3OTy3LV56GHLATf18h7dMDhaU9sUSmi4Q3j7uFH6wq3OUkrQ-lrWFkd18CMG87gqDC5ETT3PRhUutkqUd_Gn5dUpsBeuapAKsr4I1BC6DpupEbmoA4qQSjBOlqO2UwNOVeeiD2doW-ujLJNNs_o-rd-jVUyiG1FPDJnCm66igbgZtEdmKL9Ujg9laTBxotpRDR7fg5dzbYTjdZhhUVrexmIvPQLTX52-7LBdXr1zoBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiPRp7ryaqGWrhpRK7fDLVkh_9r7GDq0kv1tew2kdYDtpo87cLp5rlRjvZcB7jlLx2UBUeEVY0VovNVOButo_sV4xxeMfrY02SQb6ExmTr7lLjqtbnxDIDvzwq7lXf5eAnbUtGr9DuI_inUyRA5fFk3-zIpY4NakORTbIG1twGIGM5lvytl29Go7O-A8Kb7wpDTEvz7HdLea4XPu0kduMfcOUKK-YUqPAy1I6io4H2rEsfRe31UnIxgp1YTUs38sg2P1FgoBLEPLUDAMVSwcdhIBS82P0fwZJOnRubbP1hjNmetjjPZi8zGsFjGfHLZKx8XWlX-lBGG0-2ST9Klp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpojz-MASnh_LSO_MCb9k2ZsW1loBjVAnrps9r0bwdVZO7jbBzsKTdhcGxxYy_TLGJ3E9tjzRQ2JlMHm4Kv6t6OFWlovmnkZ1_Hcs0mIptektMuSQji2_Fhy8j4Xj4KfUYUBRuW_Yy41DYjetV1WtOWfbx_hpbP5roLDmVL8AJQNMq5DG7BIle8nh_Jv2Np3mTH0tt9EzfOHBzs727CjwBYBPIdLiECk_HU7Ga2bbfTfpUyq_JwqENkZ2hfVSdQU7k97rJ28CtdDqApE12o9oIDo_vTI5XKUuik7ZeQCh7UCTpHDR2O7oyrL7AIRU8gynNPwK-lFuuJ1GmLOkY6TwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAcfFOU97TzYGdOJ_uAYDYX9CohQ_iy7nZ9h66WRxNgsj3wGfBS3osvhprjFYoblEL4TE348_Ly7AtFcYx6Zts4LB68jcyXU6fThLwmalAA6iF7vkAF1QZw-1eeMYTV4tMxUM8wUD3j78N7GXsQEoxumx3UNAIJiVroal8tp-pRrxGDboCG-gEpShGm6K2OgdrrHETAWCZFUH1DRt_e0DZQ10vwXlxCEe-9arYKjroNFiKM3juiwuElRkiNqZMHUNfgrzymtH3Q4K4WG-Qf21iKyz6g6ENBqdnSAud-rwIDWng1mQVEzjQIIJBNEAL84NI4QFNfyGpHeKa0Fn-rg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWByc09QF3GAhxnQSSzdHGoQXEjyGZADwO875qIu-m_G4sCNqZAG9Eev2D_QKB4vsP2QvZfCu97m13-vrh7PB6oGXX2bjNbFjFFn2mFhkoxVsqe1XGHYvYaJtjeg_ils7KdmNUCmA_A19UUajgEOBInI8U6a-imWXKOG7iUlayjsjGuUQQ2pZJ2pYOYNOSThILzDILzNqjkgCkveqkH1FmQHyxXYQT_6-0HdQzIXlf7XcQ7yg2nneQLAxgWUGmOXWB1Lb5-wiiXUVLrmmvuLNop1tR4tPCIm1ATQLRbB_jaQyoWTHu_-Cv8dUEoktJt_7E6wXX_5bPXgmSy2XLLlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YjgDb3wGBCKVwVhhOxE2cPZVmBTWnQP5cDdUvgV3BbHRy3cFHagUsIN0ZJneLi4n4prSph8jrU26xdTyrUqNKussMh15h_5EQTgojJCYPI4XJ9Ns1NfwCbR2jiIAo-yAUbwwJWtkv4FsoFsSdLnoudGwZO610BKxdCBREOohCsDvnaruzSUnlLfhw2mm67kQiLcUHA5F_z8c4-WGfOzRHZ1jdkyV_o8Zt3BDyZfV2Tf4PSYhZIneQh-FQthaO4EukH_eT5c-n-eDMRa14pBk_Sw4_E-nVBLlkIPTMYB24bD1x3Vlii2CRxx4lBhpakmB4SQxR1ro2p5rlBLgc195IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oX2CgFrGOYcaxe5F8XuQmD8WctuPa1yY9fSsTluw7NzyWRyy4EbWQUKlB4RmI2TVxdCw9rgHfhwvDxPcAw4EjOJddY5QznYisMlbPfsy7ZKYCIpRqYaORVbNiXYNIbwZjl4MrCA3u0Xk_Wbk8hQDRtvSoGhr_ZBPg22uv4F-JJwT5-119QLdF2rw-Xenzpgf73_lGrdQ6TpXvLsE23iOEDdBt-L7KHGBh9662CjARzl1DYIw1UXiRr7fblfQHUjYhd1u2tOWvuzQZvrCfWRnntfa8bvLqfIm1HmBSoSJS9GxUOhp_lbyrrrO562g2h8NApgu8fUDhJZ-jp54uiHmjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=rMNsPqceT7KTKAY8FOqCiqH5dKPiIV9j8XcjacerJbdbrVRAp84h59o5pLsJw7kQNdxH1vyy6B638EoiXlJf8wgyJkauVZ3jg8zYVdcsX6gZYtcaKrtEHDI7fl6ihNufl8HLbQ2Se1m7hOLqoLhJyrirHFAzRGPqzD-N1Z3pnpfbW1t0nx7ryrXftB20xqLO59qgxjbko_OPuY5gT5jVfRfcI5tP6LLZNi2oKvy_C-yrj9dSM8va5BNktobSbTBB6Tk45LizwD82tZUoHHVTMzyVwHHHF6hM-YDbdTFg1dws1lYrfl24A7CbhO0uEotCcgqqcE5L5lVMRYXii3jbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=rMNsPqceT7KTKAY8FOqCiqH5dKPiIV9j8XcjacerJbdbrVRAp84h59o5pLsJw7kQNdxH1vyy6B638EoiXlJf8wgyJkauVZ3jg8zYVdcsX6gZYtcaKrtEHDI7fl6ihNufl8HLbQ2Se1m7hOLqoLhJyrirHFAzRGPqzD-N1Z3pnpfbW1t0nx7ryrXftB20xqLO59qgxjbko_OPuY5gT5jVfRfcI5tP6LLZNi2oKvy_C-yrj9dSM8va5BNktobSbTBB6Tk45LizwD82tZUoHHVTMzyVwHHHF6hM-YDbdTFg1dws1lYrfl24A7CbhO0uEotCcgqqcE5L5lVMRYXii3jbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGRf1z3-YZgQ3AhWWx_ygbzvmgoquoM36Vw5xr3PgQmhAxHCqj779wgooZF23jwL8K9l9Yt2TxByoD_RWaLOoGPKaHeePbU3aGUHVCYpDoWHqmxmKa7SrWptY2xCZWtONryhetacG0urSS2Yke7HymYcDDi47kPRtUqpSmmtmuO9keQEvkeqsKhF_ZS2cdeIkzRpTzwRMUu4zIhbpKcZBPf2vavB3k4AuTT8zCbVygvQgMVFuLmOKOYxugoQ2s4LxqEsGP5zChFaAsD6onoKBw_3JWhxagU_hUGTKKDalf9ya8_9j-EYQM8KcPH1hjxeZyBDswYfedx48Sz-N0csug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=aq50obxMCSoSiZK2i_V-iZvezqGnadINaqwVOJhGbpWrFAYPnyD9erjH5SCLeaR17OAKquIPsu2KDKwoxDozo65tlzuqaxpBJ3YtMMrmAxz-eysD0MVS9pYNY31bQfNhfslii3l44jD8yMP6nfR-wZmdwgZP4A3p94Q7ukMmflpRoupuf_EDcHmNHcj7R_K_umn83-IoTjZMfF5F7jyyfHdXlwd5M8PVHuPis6krvWTapVSly4majvLPDo4S0JN4Xke5GgoyPMpirFQouoyL0cLNOHsnrX8eObk1R4bheTzqhXU8nsx1D6tZgopwgz65GZuzwh5X3u1ODWE5UUgclw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=aq50obxMCSoSiZK2i_V-iZvezqGnadINaqwVOJhGbpWrFAYPnyD9erjH5SCLeaR17OAKquIPsu2KDKwoxDozo65tlzuqaxpBJ3YtMMrmAxz-eysD0MVS9pYNY31bQfNhfslii3l44jD8yMP6nfR-wZmdwgZP4A3p94Q7ukMmflpRoupuf_EDcHmNHcj7R_K_umn83-IoTjZMfF5F7jyyfHdXlwd5M8PVHuPis6krvWTapVSly4majvLPDo4S0JN4Xke5GgoyPMpirFQouoyL0cLNOHsnrX8eObk1R4bheTzqhXU8nsx1D6tZgopwgz65GZuzwh5X3u1ODWE5UUgclw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=dMZdMG4ggMCL0gw31jTn2uKlAF8cAbH0krqTSR_uKH-oZ82my8814lz8gLFMwUO1-2KuB-mnLBvL0y2YNH53XQlVJxqnT3NeNGVMhWcdud7vA5J40U4yc2dsTe-pKW_YSFqa6m60uLuj6YQbXr4wjrOr7DNWDAHG4B6nD1D-va1-_1mnyw7SkDmHBIAvRs-p4G9t54oGijGiwenNrNbSg3oFcJYDbGbs5206x-Q42HRxuomRfdPl3xiJBweYPwZCVcxqchxyi5qcpE30xXV5RRdnM_2bUI7uNCJnutmazIRPBYWbgzX6FyOz22UKuCmOfEyeRjkZ280bJ-UBZK8TzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=dMZdMG4ggMCL0gw31jTn2uKlAF8cAbH0krqTSR_uKH-oZ82my8814lz8gLFMwUO1-2KuB-mnLBvL0y2YNH53XQlVJxqnT3NeNGVMhWcdud7vA5J40U4yc2dsTe-pKW_YSFqa6m60uLuj6YQbXr4wjrOr7DNWDAHG4B6nD1D-va1-_1mnyw7SkDmHBIAvRs-p4G9t54oGijGiwenNrNbSg3oFcJYDbGbs5206x-Q42HRxuomRfdPl3xiJBweYPwZCVcxqchxyi5qcpE30xXV5RRdnM_2bUI7uNCJnutmazIRPBYWbgzX6FyOz22UKuCmOfEyeRjkZ280bJ-UBZK8TzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlIlZGM0Wop2c3JSRDtqkrObw7VUuCdUJ1Hk7bwysK8_E7e0qcNvFP_mOJlgtvbxGPDPLPGVtXVhv236Cl4BvhQMzCpCl45ZtEamBvNCLRMQUMM6B2whj5YooNwhEjLgrvnNlz5IDed971cPq_9UQjwMgtxAMihxDVGHa94Y6nETVsuWGrtKsmQaiNTCAFSgEAg8bSMjY9AsMx724hfz-LBk4Sl35ozFDi91LimbD4c1hiFo7tZfoSTDEDE66fdfw8AIrsB2wwWI7A-6GYHHAFod8a-tmoIXh95LsRwloUvJI5p-MJcDRC0LXZigcSGeoJPMYv4uNOIPO66PV4QvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRzXfrlMIVcLyVaLeNZZBMgaYQdSxEzP7IY8R_JPMd-DoBE-3IgVxIXEchfho_sHIyUGTkJICdCHHyzGIxYoWM8Bv9SeztD9eA8F2zlQbUplL7XGDwv1h-aPyTULDkAmMCAOpGLH8mh9FxNV6aS-wEnCa8OJsVJDRb-X6x5MuOP6v49BGRCyjLC5WAvVzYDbMJsa80JArwONSf-MwfPE0rwYqQjb0YxK3yoKxAi_VENNEFJEm2SUaHY1Rg6TL3uEXCedwHmpPAvFq111v6Yzo1ex6YDAJ3CCKCn1xyRZhqFM1_T5RU13vNpiYAoaIW10DwTBhUrjHkTr04DgRoi1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO0Rj7_WIQUWvQ4Z7DyNnQktYJMiZNQGOsXdUCCkK5jlgL3PrsoWOKkvwCF9-BBFFUxM3EaTgC40CpwuRNTTpbUh9NXdFUmnOUYWtKMPXJj92Px08liq54v6DAhKhAJu7dUSqptiyu3HdgcRRXca2siLqnGxFTd1lApjEiBgsvS14uk-B_6SZm4UAjWNimdWcaFE10Rg1GcPYmMsCKtY9ArJvyz6EXZ7f4R9-ZvbtgcsFO7sI48jpbSEyZiAHYLsQgCFtNLB5NIdpFHribJiboPSPJ7Nh3fTVHHZoz6nI_Widj0RYzstc0JAo5WwZf67wQKP-9ifFfIVB-lLxR0n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=a79uEI5nWvDNsixtHR8M9zrQ1xaGrsaKya-6kPByw0lSaMqrU-OtcuoLFuwgNyQ3hd4IjWtl6oZYJkDD2rHi_vGPqnzGZAJBzovrk6_jgEia68yFdy2p_yfGDA3bu5VOkIBavBnUr2Ht6OyNca-rgxnrrV-V29SYdnv82wnmjLrieTDC7mmdmSOhMIijTnavXPPw2AVOT9zORH0zJZlBRd9niGS87aNYabmvfaTcxUqLenx0ajqEuoTD7eKmJOsNYRNyEkOl4Gqmi1rO1AYCYimYpXN7jcHLMdjg-axG3S8H71FxI40go_kHbITKzRexnz7hbDNodwtr4SSfAtYRQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=a79uEI5nWvDNsixtHR8M9zrQ1xaGrsaKya-6kPByw0lSaMqrU-OtcuoLFuwgNyQ3hd4IjWtl6oZYJkDD2rHi_vGPqnzGZAJBzovrk6_jgEia68yFdy2p_yfGDA3bu5VOkIBavBnUr2Ht6OyNca-rgxnrrV-V29SYdnv82wnmjLrieTDC7mmdmSOhMIijTnavXPPw2AVOT9zORH0zJZlBRd9niGS87aNYabmvfaTcxUqLenx0ajqEuoTD7eKmJOsNYRNyEkOl4Gqmi1rO1AYCYimYpXN7jcHLMdjg-axG3S8H71FxI40go_kHbITKzRexnz7hbDNodwtr4SSfAtYRQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSuybVvmSm0AYK0c2wOT36a2ZoT9euvzeZNepQHOv4jXVYIqrNcQDhu5dSKBf7Eg56CafXSOQv_I6lh-wFOV2hBTXWoASSRDGZqZPck8Dh-kBFAULsDQpV-buBN6ge0d3CqxR6AqMd3OrLBGiOqTZi5XMdnAjqE9MJIn2v-XN2xB3-hP3HvV3Z6mtOR4euwTUK4hPcBEC1NifEU8NKPaxAqxNQbs8vHY7G3QSFpweh8nkNN0Y8XGDxXSirFN5J3DyUQREwclgCP7If_7UAfkAWzzve3AujtqzJWZxkODmSvD3ABlsf28T9XNjuAllnt-vV4RV3DI12LwBpPxkju23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=eIatgvEjwJERlVprlE6foV8z26Ni12KUekptwFBvUfizSgGhnoYRFU3E9tZoAKxAFyfpQqd-W20lodNH9UnDTfJOlAP1B_UzWcabaHQDZzCN50Zdw6GFxsA2mRWjYat4KWKuF10qqk2gnQePBWYvw1zb78NyTgWVJe9mf9L7Y69smUlEDwoudqtuB9TNq4xOokk7kVWSK2EaDrez1z02cBBPW9g5e7sfhAeR15srGsje9txEeV7jf_DAy6tDh2nXNfl71LnJ_RFZPxROsRGSxJksMN1XEeIyimL53DlhtZZopEKQDP7CKeQcqhxlWXCGYk5bwiJAAi9ned-sqP_LzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=eIatgvEjwJERlVprlE6foV8z26Ni12KUekptwFBvUfizSgGhnoYRFU3E9tZoAKxAFyfpQqd-W20lodNH9UnDTfJOlAP1B_UzWcabaHQDZzCN50Zdw6GFxsA2mRWjYat4KWKuF10qqk2gnQePBWYvw1zb78NyTgWVJe9mf9L7Y69smUlEDwoudqtuB9TNq4xOokk7kVWSK2EaDrez1z02cBBPW9g5e7sfhAeR15srGsje9txEeV7jf_DAy6tDh2nXNfl71LnJ_RFZPxROsRGSxJksMN1XEeIyimL53DlhtZZopEKQDP7CKeQcqhxlWXCGYk5bwiJAAi9ned-sqP_LzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nReEBtmSw9gJAJuT6K2Bm4i35OzIrV3y1R36LYuV4YfudS4jAZu25sltvlNEw_HdmVLQMVUyy6rTZQ9Jwb_p-12LEmCMousg91efd2GXqXYVofKNac_l4pDpHcr3FEP8f5WBUjQHUuIf4K-GbEu8OcfXIBGZw0vLYXJExnHN2s7mumDdLyqUlZQg0y53w8g0Oe3Rl2oXHdShmIkPHphR_QgDxwTurdgkq5Qa0km7oMnlKX8jkcCUEfccuR-PFEIfeKNw7c6zPA8S1ku1LI7A-vkuYrTcIlm3AfiIZWTBQ8XWGgxkn4G2n24HAIWgQseN9awziIrwLvq_TipwZ8Vi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igGOktToMpuPJFzNoRbei-Wi44ci4QH4Zvs2lmFkZ_gCGy7KUhFXF5O3EHxIEy-T8957VRr6BqJvRgjnaSYkEkS1ml09gi5_1gpodCWns5kWhGyUYx1HPvst1bAc9dVxORWd9dRWpaMKipkeenPSARGvJan9ASNU5yHz4nHzSYSo_cukoAra_1k8UEu4Tv9kSC7zzAbw9ybJEJdieNhMFmGcbwDjZZqz-QSwdNH_c0e1LuHPbAtoERlzV6BQ0m-ElwXZql0LI-O0TT42wZZ7kNFIfvHVECp6NdUwi9p4rWDBWJiMP84TizrEtFbqjFxWpOj8sQc7zin0K6a0YraHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPeqJZub1wcNeWh2WwRNSXL_NwUr3q31f7OB0VLHrJqIcibVLE_108grVjXhxNxK9xWgBgR35Xne5v4O90LmXvJnVtKRjEf5M7H0RrPCQScnfVsWxvOv3ZHwcE2ygaTe8LDqGNgGrYE4iIxmIsRCkWdJH5WYrjf__LxK3ZZYeVnmgxPrJw2mKkkOr-Yb6utzZwiM8AfOVoYTT-5FZrMlkzTzg3IYZFv9VQmjJG_wiQobJE-lzJJ5m7Y_cBYZOF_CorDNVNsHx5yplZ0j3vienSNLP63yCxqlwyt80q77xIOcFhTCFL_nxcHzATsbjRlnsAPs8fZsHK5yW-HdAgQx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aq4i4Apz1O8Id-hTnfqo9QvhM4LKu1IaOmmsQT4GZRh5nYg8CFrDFc3XW_po--CYu8J0bAinsi56_cPy2uJWwVhzQieslMhPDoB2kbW3kiU4V-lOgkHcGv8HD1g-Sf8UIKdCgo4_iDUf6bmvHK7HPf0lB1w_Fd8agUxTt-bAUN7Pjt6MMQmT3tJkGs4tMuSZGCLJnfZbiDa3ViKOIkvrzSQqz8EMrPaj4tVRCP9-vkUOkjh5XeEqAk1nm6vkcRSpe2-vdN4_8-MD8ep042yY20aUniWwuy6eqg3y_YZ-xyukw07T96fcCq5pXHHcuFogL5koS7p41a8hNajQ2VptBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAs0Aqs1enF5s0DqJE0oO1z8jj77oukeKO17DKqrK3N8rVJZgNNDrYxU7JIWjAJ935PDUjLiZ146V-7E-aNMK4HvSFirE4WN750I0BULlnrG45BA3C_TKw9l-QXtMedS5NsxMnxs_zAtc-M7LuoT4S8SwyWhVEwvsNwf5z99uhRbYxDTuYasZVEz5P6UjG5zadmhCa72yuVQ_qBh9UqZPw-tDCThBP7MS7PDX7ymJAk2GzI21C3HCX_5_amcToVJVfNqhzC_7l5nKJvm9o6T4qmP0i3dZYC8afKUh4yoc79kkcRsRsuV_L8j8PDPWz4u8kAr5POcAVWy1GAD16CBBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCoFzgvEF9ogNabOXbJ-JB9HrKIO_R4FBM3zybUQPdQdAOJM4VAWJTjcHtZVSFP0GNdw26MjYEJ9b2oIwACtZ8V1NH82XZ0g1w0IHVvdTGbRIL8zBx8Y9DbB3ptgUggkHjqh1cZhFpBs-viPquD_eSJsIo1PhObCiVxtat5SDKfN3AhNw9dHXZmosDi4yaGaqPUoUPSywl2v6f029S1ADnima-WMBPieqVGZX5NWeZCUEzon4NK7CLblh2ecYPNS6A9-fNl1jLrzg7sxXth5h2MReeSEVB-Ol-QkJBHfBwggodt5LIR___Timd1Mutao49pSCKpxHRe5NveKfouyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHNZ0yo_NmCThPbU1QBF8WcI8BI7T-IB8z1tVriYj3sWDL8KSuxkpHk_yP81THzTRgXuy3oaiGKEPgOvI7ZrwIM1LhmJDyFoagOfuc_x_M6Sir7EQB_jaW3Wtc_fyonX4l86QP7KzyA-OgEv7riaPMdNJoXtyb2-z52fG2_se5PkgcbeWZbUpBe0O14HhjYt1AnFbpnx0eAqD7vxvn3Poc5LCAnOmGZ9bRtv_04BBepvNmzts-JqedRjN6036coljajAOLgQOgWUDYspBmT_G75efUgmyyFy4dXCh6nlh4w_TWjyFqqDcwKgkeCTFJYKm0tf5FF19BVmwtNiWkH_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aY7wK3gTNVJ_w-XRnpXYfg10nl3QoAAtVRwpA6_Zb9CE8yxe62_5POlXWop-oE4n2uRHDmixqf66L58nQyVZmOK-qPUuyYa8dT9gEBICc2VvoA26GOs2eZNFgN-9rrbnm8b_QomjG1DKkpYTpzj6-SZbvtG-robgmK8t-Rt_81eE6B1hj9m-kVsumKTHuKLZ5strLuzebPGb8ED7OAkZkCJfwPm-V1sLDZbjNd6LsuLqsbLw3wV9frYVUiklPrdn4M65x49f5zghIiwKGJkGnxuMNgjgcg1_4H3QENFtnsBR8JSTubGz0HNs0EEnkar1XK_VcM6vmeeuLNBNM0R8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aY7wK3gTNVJ_w-XRnpXYfg10nl3QoAAtVRwpA6_Zb9CE8yxe62_5POlXWop-oE4n2uRHDmixqf66L58nQyVZmOK-qPUuyYa8dT9gEBICc2VvoA26GOs2eZNFgN-9rrbnm8b_QomjG1DKkpYTpzj6-SZbvtG-robgmK8t-Rt_81eE6B1hj9m-kVsumKTHuKLZ5strLuzebPGb8ED7OAkZkCJfwPm-V1sLDZbjNd6LsuLqsbLw3wV9frYVUiklPrdn4M65x49f5zghIiwKGJkGnxuMNgjgcg1_4H3QENFtnsBR8JSTubGz0HNs0EEnkar1XK_VcM6vmeeuLNBNM0R8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjvxYXL-r_QSpaPwScSQkUbB-zuFqdEmjmD5PKoS6OCcB7WALunA_UYwEpFNqq0q4nommcB-0vTpHLYgJLvF5QbMk4e2Wova_vfOnlYcpF-pKkKsHvGIp1mkxI2OFAghDXwW_k0fZ589bQKrzhvmMX8u8VNzy2Keqfr86QAGGgRs2ibl3p8MT95W7lYX1HV-k_v5aWA5HwazpC78vWwO2QrSU7mv7siVrxDjw1v-iOItOCWYPV-hL84pmgRDcNFB9coac9RJsePwsidYEMyIJlOXsRr3gniYDvX5Av0-RNG4jx-oZZ7TmqGGiNP5PgcoD_r1syMXgh7tU4_PCkstlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=L3AmFDCcHOgaq9UlZbhh3DBFb_OaHVLUn6GR7UUnGOn2GjXj-HJA5lS8f_itHrSc703zmeLNPGGqKg8gZSiEOi36TveFbGKe9rxBIcoSINdRtnO7eNtxNAYw4-1y346CuYOJcdf6ifST6gG-hFj-Hp6lgGUNUQ6qr8iMOILt2RVpvlkW6k1AAM84shh2V1QU_4LeJ5_SLji0DYCUrTKgucDcM747pEtjEdFymFSwMvLFGd5vm8nsYks5oZsFZ32YHyT-4ZLQxBxENebQusquis3StoMi2u2L9rze2aeI-OaLokXusLAySD_IXK-M0dgRfTfa21OxdYyTzgc2w2tikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=L3AmFDCcHOgaq9UlZbhh3DBFb_OaHVLUn6GR7UUnGOn2GjXj-HJA5lS8f_itHrSc703zmeLNPGGqKg8gZSiEOi36TveFbGKe9rxBIcoSINdRtnO7eNtxNAYw4-1y346CuYOJcdf6ifST6gG-hFj-Hp6lgGUNUQ6qr8iMOILt2RVpvlkW6k1AAM84shh2V1QU_4LeJ5_SLji0DYCUrTKgucDcM747pEtjEdFymFSwMvLFGd5vm8nsYks5oZsFZ32YHyT-4ZLQxBxENebQusquis3StoMi2u2L9rze2aeI-OaLokXusLAySD_IXK-M0dgRfTfa21OxdYyTzgc2w2tikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Psw0CEgDsXcc5KSoDEI1p4_eo5D4LnTnNl3J2xFeJc4jxccDBrAk0G-eh52gqoHyE5I8uTu7DvtfAeOHYY2gRhN2gj56KCbAaN7xN1QQGs7-NtmVA1lv5pEDvS4Rlps_Cx8D_ysNUDGL6y8Bw6Te3uTjYjaGdLSP_HujzuyWnGJEQyn5ztoRjEwyayQCw2aorzzCru9PlyqtoAZ0QJrDycjNG0L6vt4OJwHCnmkfGiUkGLYoyFN7hYWreYCspXDs4m5b7rTRCSUeMbm2KmCLYeCFYjC-0oa6jIQ25JweUN467Qeyj4d6_h282PsR06q1c0skWy2LHa9xwAEesIn11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6-nSTo8QvFrEdM0S4bsCbq_Bf0Mq9wR3lH8zeIbTRjMBj9ELfcsUIwBanoBJQ_b261XxlimcuwUgVBXneNTdoEAKgGdwz9afxiZL55ZAZQmxDKLQ26nvJMNkHSFHma42EXL2Ynz5zrE1Wn-PuIC3AvOWM0pjnc_Fo-uCtATUQxrXcb1LrB-Gz6NLHKZ-Jby3XyehyyYdkW4S8CeizlzeIjOpHoAD_v7OgdPZk49QByxeSbXqWnIEoS9F1IKP2uTPsdr1nmXjqmOUvqCwTX5nsNhD3qXuC3aHmyZJGTANwJt1xXpJSLZBkI6HNK5KzRKE9CiT9R8OcJ-FcChl245XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEOW_aNWDE7ynNTJGH3y-7RR9FjW0ESKMWe0F-r6x3XUehB7Hr0Rt4ibS-cvGRIYb-Kv3__o7cZ_--Mn3DkpS60kiD5MueD316iCdD8k1Wjat30eFaeTy_OJe5A5uYDcBkyYEgk4BXYItNerEMh-VWnmGVv-xfTDpst8MNul0O7Dv1ZS7Jtmgbtm2zGW9RBoSPWYjz1xnj9bDhLQZYVPjyx1eIEL68G8GqKbbIhWY8EILSoLuKtrm-X7jXzouj__y4767ZXfgf7o8VOeWCzmRKVio_cMOO2GHoy1E6KAUFnsBr2pwNkE8rBPfgeMP1wGobKqaMlh69LtIAsz6_w-Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwrUoQzNrkk3b-0bqjprbheJtLZWG8036jENyF3qzwotsAA4-YHg30XZDyQEmhLIYOs-mtUxy762ax_sWUMPi0HKygF_72aAEURVOaNf8xMq7gDVwpmxPc5J2FV900MNcGMWQLYBf0UnM-O1S2qwkk3Ej5UzLUqTIu_x3idka-gylqjCrqbCQRA9dsEI7e0-9pGJP5Z9wuCysOvaVrMWUPIf59FFe_CTOT1bW5BLL5XrLVMILrqIMCsln8zGz2u523yfklbkNw640qo1CeBRgLLQm2Zl2yzg10xMJjKkxTB18PZ-oCFzpUI3I5um2kAK5khJVfL9VfE0r-E7_mQ23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=eGQ7vDPmHSf_IBgOlh7uJ0XqeSfaexkvShNCfi4wgWmefpQDEzBBmnEHN-OEvKX0QfAbrWYU2WZuQ97TXBa2eP40edFa6WfgN32UnAIogNWXHV28q5qv8tn6omCsx2qBkxGkbtjl60Uf265HiEMkt4nSmhPF1qKn9a57EfFOIY2Tb0e6dO8d6WNrno0YF5LX8GZ0CmDfP70YYsQxoDKki3Xj3nTShF7hBzqS6R9J4tpkV3Hs5PWpkee5LKIXyv7I8i3HmFK3XE43giBTU0B00w_7mb8gtJSUgVC3Q_7pCHkd1PDKfwXs813A3LEJ3vMn6L21w0aTunKe_rEfyCUGKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=eGQ7vDPmHSf_IBgOlh7uJ0XqeSfaexkvShNCfi4wgWmefpQDEzBBmnEHN-OEvKX0QfAbrWYU2WZuQ97TXBa2eP40edFa6WfgN32UnAIogNWXHV28q5qv8tn6omCsx2qBkxGkbtjl60Uf265HiEMkt4nSmhPF1qKn9a57EfFOIY2Tb0e6dO8d6WNrno0YF5LX8GZ0CmDfP70YYsQxoDKki3Xj3nTShF7hBzqS6R9J4tpkV3Hs5PWpkee5LKIXyv7I8i3HmFK3XE43giBTU0B00w_7mb8gtJSUgVC3Q_7pCHkd1PDKfwXs813A3LEJ3vMn6L21w0aTunKe_rEfyCUGKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4y5wspkufOju4h93-MpUwm62F2Mvs13rkseE4S_5VfiHZgPa64wvfp8bubA_eWRDIqD-ub6L5srD76SZ7-qwyeemKLHjYuxNp-DT0nTGpQiD6y5hQnfQAKuiU1P3eJPCev0BcAR02_Vva7vu2Fll6OXMesnm-5RNgRZtSwnC-LZF_RdBZN9nui7X8SE-md_rbhv-CpT5McaMeZC9RP_t5fmwBSpZAi8agmUJJ1xNsIxr8iLI28v3KnbKRb9MjFtgrA2E6T7sEx7UIzgyGNMG-Gh_Gvag_YBhwsp4tfxvRxbjZF-nsDjbBqhnc8TUcXIVj2GXCHm9w6JRD0-4UgGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1z1uTUSQE8wUKjfbdz-TYljx9Gn2jtKUW-OHonkpyTWH4Pb3HGXvFGnN3LJGyUyYobXj4uYr7wpEbLlxT7hYEgRn-CyHmAFBAiHuPTjBNJk_aCfqyfiwYy_C4-uL4xWn5nDxsBloFeCeGI2gfpwYg2qfdOrKFUqUC-8iN6wpdmLaTFF8OVHtOSK4P8UU-X-5Gvkv8tblgBLZ1Jt8VgSFoj77UUAdsuX36Y_JAOgoJAFTRBAsHdvuWqWpxu6FOqgabtfKOYJZZM2HWmgK4gXe4YKQVKAtkOoQynnivnD-K1tddzvgEgaeZu-pXod69sljMERva0bXG6NOsFA7zkVxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZM0LfyfSkwnO1orF1onxhIzsux3kMjprj2qvpDE0ZiNMEyrvYmOP2Aw-w2c-J_HhmA33Pr6nvu3NG8dLX9Wz_nLStCMFT_HTOORKM0bAvozxdQOsm0CgnPpLAjS3xf7wvHHwJfoD8wUnoXUKcqUpnXg38_rH1tUjd-TihEsY6--1-kg6sRoH0RLkSfOwtFKYSi7tiS3QgjWW-8QsiBFArj1YFnTwAXDji5X5qHB6czvj9gFpU6fCmdo80MIwxCVzfXU0JqfvoiPuGSkJgJjGMXe0Z6FDnT66IjO1CIa2viv_dUWZy_5tSMnLo0LKkQmJoLYhQNqXL5X34RrbHKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keDKgGtwn9hv-4l6JJl8-aQvRYfI4NOeU84A8NwYNErNbRbb7x3-qdfdcFzqARQJtUMN8bbFXWXy63aZoy9_XAZn8ovYHt-J7_HXU3XnsPxFb0ZUlIj4L8c_YiSjVrZMiK56-K1au3p-CoDIqrVJTuIaFrnfePPZvVwhIvIHEKvNJuvdNp5C59VAYTWYS0A7EobHhVOWY636gDmC8I-T6l2ecV8zbHrvJr9OiozakvGZox2ibuBIw1jZjJDWyMDMetYQ0Y-KGqXpsAY9C1LwrVaBCZxZyTIzW3fw248_XRDq3pPIzKjCsZF8smU3UMvmxfAo0DgKSIeteQvtL_GVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSZQRCwh9RkkEKkQwtNbV9h_wegD4IE7VnwRqwLQII4DtuOv093kpHG5COhAYxhwf-wrK785pZFuW6IcDMg7hC6T2EfN2qltivRyFZ0eraqqESVOerHbHs-iwFFAGHe8hTM3J-tekXFdsVIn68YKbcrRQ6LDBC1lPVofUq1xNx5kAVJk5fl0CJc_EU8a49LBC8KlVrnXdGQXNAYuEr9OyfIDeJ-7bSMZZPQCkZ1xMUhZWSz3zfMRXloxSlf8sMOrzVgXzRO3-BVCeFkJw-iXqhg7S4Gw83xOqEmwfAj8sBXaqZFfq19d43kD740k6t-tR86y4vuvEvTexGFUORKHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=pE0YuzZwpfUObE_lo64Xf1Ojcwzb7luR42qP-QzDo66K3imw7ZTJnnVSDoJVncYnSZOFuHHF08DKH2DMw9p1evEE92mhCSlHX4QEuuZyTS4G_1vxlQ6IltlcvhnwmYxIaFZBKA-6ITZm381266LsvFVyLEZ5b9Ud0l1TUjtIgFmP-3RRM60pZmVUKUdcBUOw_f2-oaQR74yVS3r56m0KYUBnt6oStVZrGBPq3Lx9_MV_zC7zDjnkDRGICTgNgYbhQi7byQ9Sn94bp4mTFx1f3HiRrx0B2pAYY7wyZSdz3vmVQC45rczrC0z-xsXEUHltV4xwbdL-AinNCLSFxKl5J6j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=pE0YuzZwpfUObE_lo64Xf1Ojcwzb7luR42qP-QzDo66K3imw7ZTJnnVSDoJVncYnSZOFuHHF08DKH2DMw9p1evEE92mhCSlHX4QEuuZyTS4G_1vxlQ6IltlcvhnwmYxIaFZBKA-6ITZm381266LsvFVyLEZ5b9Ud0l1TUjtIgFmP-3RRM60pZmVUKUdcBUOw_f2-oaQR74yVS3r56m0KYUBnt6oStVZrGBPq3Lx9_MV_zC7zDjnkDRGICTgNgYbhQi7byQ9Sn94bp4mTFx1f3HiRrx0B2pAYY7wyZSdz3vmVQC45rczrC0z-xsXEUHltV4xwbdL-AinNCLSFxKl5J6j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfQ1myvZZpRBpJ4WTVbKEO0-u-PbfLtYq7cuUAr37j7S8aaC_lR9tnhlmspKgsrVaANgD1eVvdfmzSfOUacYyWbWzOl_aW24_CzIHK72Jq_YsjetWOh99kg7RwO4obkrBVlQUb6crSc_kiVmvQIpVWAT2pkgt-GyNey-CrVKmTTLb4ee_sBjVtg6I7uouwunK2JU68wWqrhKwTMEbYADf9zoWgPTQJopAzpD8OjryZq4Z_odyfxMLQanFMJZZF2Wdpa1S6MHh4oVuFKHBiSOUfvVxJHcMy98RdRNjkIOFJEI5rL6wE8shedDTgT3XgiYOWhlksFV1V0dBT5hXaN5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpkNrdY6CbolHpF8wvq8FhmmxwQdCxqilzgccZmVF1IwfRv2P78ZUH-O1-1Z4D7gY5RwAUKsnWi2jZkhH_hnUYGnGvYzCB6rPnpErVnpcWRKzZJi3loWy2uCq_gqvP0qssBbb4IyjotwEpZAnNOTXwEqI7f1LsNSV8DLukkH1AgtV5HbJsDkVPReomlscRRGm9_KjsGGHNbaygfS8v-j1prnH8oWshFx3sSsF2v7jfrdlIr0vMjKLiUx4m_iSKzI7gNB_g-t8pgmuPxIZ3k1Rz3gi-OpE5O0s6-sK2hJ8WOg_GAuTeug6Raqs8WO0QXo9hPpY3Ot9z-0TDQnoHRPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=MUV0rSkkd9cTZKZLpwDbJFKgvEgSmkyJRW408wjK1WUjK8P-wKkImcfiETt3ycJuxa4ShGVMqQwBXpDDCzStn01F23ZewDwl2BE7dkJyZa1XImrjGz5VUc-3epsK4WYQyuFfZLWYUvJw0V5gJvsCEN9GeL7t6nUaBEJT2_O2yj_nrd-7GB8bvXv7SU9gyBs6Ua8HRj_2FmE8saMW3UDAEb4vq92TaqSbaXiV6XStrXAOCXxSqe_b_UW-nAjQOY1Om-zP2UwI1GxEBRy4B5sPnN6CLNjEI1nMdwUZB0IN-TLEW-SzdZUJ12NS-UnUp_cDymdvHu8fEuu46C5ERMFqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=MUV0rSkkd9cTZKZLpwDbJFKgvEgSmkyJRW408wjK1WUjK8P-wKkImcfiETt3ycJuxa4ShGVMqQwBXpDDCzStn01F23ZewDwl2BE7dkJyZa1XImrjGz5VUc-3epsK4WYQyuFfZLWYUvJw0V5gJvsCEN9GeL7t6nUaBEJT2_O2yj_nrd-7GB8bvXv7SU9gyBs6Ua8HRj_2FmE8saMW3UDAEb4vq92TaqSbaXiV6XStrXAOCXxSqe_b_UW-nAjQOY1Om-zP2UwI1GxEBRy4B5sPnN6CLNjEI1nMdwUZB0IN-TLEW-SzdZUJ12NS-UnUp_cDymdvHu8fEuu46C5ERMFqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=sRAfoYCoBGBkdSls5bLJ2AYL1U_N4OEFfI1mdP0Yoe21-8B1Du1SPTw4ikeQiaz9lkFIQb5za2HCq-kzUC5eBE97P0ezsjem3QeSVoLj0UAFkHxMPNafD4J6DuRr_vMKlTbr4Hi5HxNSlQKmDEg9Jqai296Mu3Gl_XLgjUzNQfdrr50KDxCvVGH5u6MV1Ibns6YRHPhvkB6ZBbyIzGhxgnbKJxzR1JAfpU8hGZUuudVUHiBPq34bC61EofGi8GZhzBMUsvSRSxaLezlmKwl83PZF_Iz3zyMWA56IVA8N_AShz59eItD-kltRTvXO6AHa5yjMSOT2OfimBL0PXDWZzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=sRAfoYCoBGBkdSls5bLJ2AYL1U_N4OEFfI1mdP0Yoe21-8B1Du1SPTw4ikeQiaz9lkFIQb5za2HCq-kzUC5eBE97P0ezsjem3QeSVoLj0UAFkHxMPNafD4J6DuRr_vMKlTbr4Hi5HxNSlQKmDEg9Jqai296Mu3Gl_XLgjUzNQfdrr50KDxCvVGH5u6MV1Ibns6YRHPhvkB6ZBbyIzGhxgnbKJxzR1JAfpU8hGZUuudVUHiBPq34bC61EofGi8GZhzBMUsvSRSxaLezlmKwl83PZF_Iz3zyMWA56IVA8N_AShz59eItD-kltRTvXO6AHa5yjMSOT2OfimBL0PXDWZzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=W7ZLCzGJGr3M7rjYaCO7XXY7kUapsu0L9ZrOFUoM8-FkwQ3-pNJApWUKfHX1Ckdj_mTtDpn6AT7ajtsZ-cgBrw1S9j4HwoaGRHWBtN6Ql0ncny_VTFO1NtBYvgjdW_UcnApD5YkH4tu9e0q0Az8rkk77u-JXthFZtz4UHL7Sq3W-GrGOfF07PfAgC0os_VcuLb2OI1AgwatkfapHmdN5wK9tLHBBFqKo77Me5XkAtsFNbSeyFxQh9rW8jzIkb7dib8BQsBPDpozmP4i3PHY5eHNvu29Y2KsyDNRII3TtHyma5IjPwWZh6uHysmkWFc1vuYaEE2w5tqt_RGaQz0L15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=W7ZLCzGJGr3M7rjYaCO7XXY7kUapsu0L9ZrOFUoM8-FkwQ3-pNJApWUKfHX1Ckdj_mTtDpn6AT7ajtsZ-cgBrw1S9j4HwoaGRHWBtN6Ql0ncny_VTFO1NtBYvgjdW_UcnApD5YkH4tu9e0q0Az8rkk77u-JXthFZtz4UHL7Sq3W-GrGOfF07PfAgC0os_VcuLb2OI1AgwatkfapHmdN5wK9tLHBBFqKo77Me5XkAtsFNbSeyFxQh9rW8jzIkb7dib8BQsBPDpozmP4i3PHY5eHNvu29Y2KsyDNRII3TtHyma5IjPwWZh6uHysmkWFc1vuYaEE2w5tqt_RGaQz0L15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9ZNfwlmPt5E9m7BWyIOPJckkJV5-zogBUrq-ZYiEIOk_xIorGERFkVaKM5QnkqnRsmlN0AXkDIiBLTZwJ0rMj06EERp60DGYMNVckWk8FscigOpRA7rDHP0cNAM_hDioAfLZSvAUk1xaT1c3XEdxVllkARKWuNigCqnxBt3MfW4oob1_yoNC9qRcyZK8AnSU9h6oZoanBSfcSLuMtoxdcTl6hu46FOGd4ME27Ky82hWKTIPOOR3IWqg0DG4pTjD6m4QsEaJvDJDAxnaHOTmFHXbKY6qqZNHOtiUhWHwnuzVZROBAaXVlyBSVIna2xNU0RKpKMemXyg5BaZufJBwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=VrWZRa4wbC32P9jqwOFCcQQPfO-bAOdIgMEtw_ecG0uz9OxJPc7yAruDRyztTRhczmu7hlxVJeX5itKRYc0FyuiVFCcn0GRRcrzQmIaAf-SDrJSGvsbHF3mOElYBUTIxmyCF1fhyVC8Z8-pU70yvG34TDd5hvILCYDbwDL_bWLCnMKjf9gzGa4LUU1DFjfRDj5VxbM_BiPV4nswp34EV865vONpyJovOJmSZZRb0es4htv8u1-RiCMPAzFalNz96Ohs4-GU6qZx809O_JBrngYT8jl8dRKK6hIQkVYsLiHFYt_jXi5EWed6zJd8hxy1YTu1nbZzDzBDdYQO93nnhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=VrWZRa4wbC32P9jqwOFCcQQPfO-bAOdIgMEtw_ecG0uz9OxJPc7yAruDRyztTRhczmu7hlxVJeX5itKRYc0FyuiVFCcn0GRRcrzQmIaAf-SDrJSGvsbHF3mOElYBUTIxmyCF1fhyVC8Z8-pU70yvG34TDd5hvILCYDbwDL_bWLCnMKjf9gzGa4LUU1DFjfRDj5VxbM_BiPV4nswp34EV865vONpyJovOJmSZZRb0es4htv8u1-RiCMPAzFalNz96Ohs4-GU6qZx809O_JBrngYT8jl8dRKK6hIQkVYsLiHFYt_jXi5EWed6zJd8hxy1YTu1nbZzDzBDdYQO93nnhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=MrSTGYStzzojKhc855wX93CV-Umak7aeLzhPisf2o6A_XURRHn8mQhBrye9it9Unq8t9k10gKDdRnjTB2pHBJvUhwPAaOeUhkJ0oX3XCoXFfVHtaXNbQWJpjBbCoccBh541jzvTZAMk_gieBvx4TFbKDKHzRxNGFuQemTT06HfWicfb_eH1buXPRMRwMXrboyiqEIFjvM4HwjOSSV1s1KnzGR0xNWquDje7AvmmYYSDLFVzYFDzQ7pZ8l13Qy0tFS3t4xHBtvi0Qb9SHIn5sy8j5qoAfM1yAnBj8x4U6p2bzPXuTF2dtlvN_Y1vurRboD1dbcOH6erlExdCIY0u88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=MrSTGYStzzojKhc855wX93CV-Umak7aeLzhPisf2o6A_XURRHn8mQhBrye9it9Unq8t9k10gKDdRnjTB2pHBJvUhwPAaOeUhkJ0oX3XCoXFfVHtaXNbQWJpjBbCoccBh541jzvTZAMk_gieBvx4TFbKDKHzRxNGFuQemTT06HfWicfb_eH1buXPRMRwMXrboyiqEIFjvM4HwjOSSV1s1KnzGR0xNWquDje7AvmmYYSDLFVzYFDzQ7pZ8l13Qy0tFS3t4xHBtvi0Qb9SHIn5sy8j5qoAfM1yAnBj8x4U6p2bzPXuTF2dtlvN_Y1vurRboD1dbcOH6erlExdCIY0u88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5ap81GK_d1d-33Tm5MjhoyWijwdvMB2IJfakAHp8HvrxemaNLVQt4fDtqeN9tAOrMS9aYq06_2pddurN8cABAqYpBiO_p_bLStIfqG9R1-H0wPb94QfKS375vEHAaBTCJjZqxuVeJFzWEGV5M15L85fB8okk8CXPWt8N2zfkmr9CWbIxm-Xq3I5Dg0NEttZvdEb2SIEyP8ioEzyYNrtfiM0XFe18SeA3hlElq5To8miY5mzB66tkX_2Ps5axkHNQdD0Jbzxz1GNDxG0e3f2-fnYXFAjZ7o9x0LfMegz4GJTFQGyAdHz84t2ji01YvXIYMxvxWnWoGPBCv7Q0BmiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=GonsMyene4TWGtojwae7W-HBy4sHIYu1k6z9nKCoQhDbN96bY8tLwESpR6-LsrAanN6_FwymVBEmRhlyiRcMc-FF9Q5rALBw9E_12V5IM4-pmg_liqlemWUKmz3qmYVH39W5U-fyzfFCSRCf_Dy3h41Xk6CN-mzoOa3343mrDcoXdCzh19WZIAGZ8pMCT6LYoQpH_2isud1vXeMEAGx3c0FUYA4XGj-4br4TZJD9BC1WmCNcbnZa1Vx0UkN8MCfZZgXi88_1N2acG4RdqdQTINd7FUCIeieWMLmw5KNE66hNfDrzjVM9QRAU2i3RA2Nmh2OTt6aUFtRT-7OIEWU3uDxcnXTS00yiGf0s4lSPRVxcaBetHvYnRMwrhUCypJzahEHtsrzxpDYBk5apUmdNyBAnn4YLq0jGkhwjapZkNGqQdnswuRH0WldXiqzAm5RT2k_y63I_rN5ERdTjEDLKCQBhkNWmF_3ukSXajNyI1sESw9mcCDZehRxby0quuHXfdJdNXj9050Bw36DNCVxHjOM9uhjsS_bAfzd4ir_yFg-2T8Yn0Ns6NjSdeH9zB9feQZZY_527hKa19TxW7P_7K_z7HxAX083OW_GqYrClw36fqeEgdXFzOE0fE0x2gbutTmudSxssK8DwuPTBzmXkuGxz3mYiWgGHZd-vJWghWZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=GonsMyene4TWGtojwae7W-HBy4sHIYu1k6z9nKCoQhDbN96bY8tLwESpR6-LsrAanN6_FwymVBEmRhlyiRcMc-FF9Q5rALBw9E_12V5IM4-pmg_liqlemWUKmz3qmYVH39W5U-fyzfFCSRCf_Dy3h41Xk6CN-mzoOa3343mrDcoXdCzh19WZIAGZ8pMCT6LYoQpH_2isud1vXeMEAGx3c0FUYA4XGj-4br4TZJD9BC1WmCNcbnZa1Vx0UkN8MCfZZgXi88_1N2acG4RdqdQTINd7FUCIeieWMLmw5KNE66hNfDrzjVM9QRAU2i3RA2Nmh2OTt6aUFtRT-7OIEWU3uDxcnXTS00yiGf0s4lSPRVxcaBetHvYnRMwrhUCypJzahEHtsrzxpDYBk5apUmdNyBAnn4YLq0jGkhwjapZkNGqQdnswuRH0WldXiqzAm5RT2k_y63I_rN5ERdTjEDLKCQBhkNWmF_3ukSXajNyI1sESw9mcCDZehRxby0quuHXfdJdNXj9050Bw36DNCVxHjOM9uhjsS_bAfzd4ir_yFg-2T8Yn0Ns6NjSdeH9zB9feQZZY_527hKa19TxW7P_7K_z7HxAX083OW_GqYrClw36fqeEgdXFzOE0fE0x2gbutTmudSxssK8DwuPTBzmXkuGxz3mYiWgGHZd-vJWghWZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_XBohMnaz2GD61tMzMM2S6tbKQsc7DmyLK767EWXJrHl_tysxWxxx6ds-qQugYrX0o9WBFIeGf87okvcLpg4D7Tlfp7u_9hVYb4LtioGFNvXXmwuuhiWxOP8ZxpmpuzMmNAzSNA5GLDp09-uocQ8iPVL2xRSrI3qiqY0QM-bAmLnqJTpmMQfp59exInqdAmZQzOei2DO-p0rOluxCBGHWhaBjsPA4mHpAkoDRHeEKS9_MJVF4g73HxPZuuVFzYK4ETxxMCi2YexVPWiKjuWdGgIYrYDTO5Hp4u1pfq6h8RNQJkOVYtxGUnHxeQ9ujjjelqDHNeyxGjuMN0KBf04WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8LAfa5oGnWh8_TtPIM-Ck5JXzt_U-Gr9MS4HeQDj9FcbUsDDqpsufDOZS9hDTw6c4OHqjIzbj9mIKXAe9V81pHbZsGxpuRMMCV3SuiLtPwR0BFJu3i7wxomPmTkrsEp2q0dUm_9w2rTkzxeWM3p24oW0291JRDDfDtRVhMyl5w2a9ty4YYJCvPRkWHG6qD7v4valSGdNDCnHgH2c4QKVogyxFglvB53SJBPZsS-yYazqmOfTOG5dmZtWeaIhY5GAbhRM84vlsaAeSaX6Zdu6b68kujeXD67xKoXrxba380xvKrhf1AvL2st5RaYISQbtyHzmwL6crgdDtawBp9Tcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=ZfMYnl4sNrZjUSNzwMFvegDglUf8Z8fSL_6vevleUOWRxmYmoMI1b-5X3fPr9YOGCquj0lEjpL5p2ZMXDfa7UqGXDhdW0I_JQAJfsTuC4elYW6LZgemKx79H7cAmgfVLtjSLH5m4-N-TyqltnVsjegh6VYsaw5YES7tIqPtbYJUlwkcRRXKP3-cvgqACgzuikG0H8Gr1_xbLULgsQ-CyKTIEw1V0ZDD2wXxECGj48qyPGrnNNcXKItV7YEc14xbmcYCOb0MAxJ7a-ODmeXs4mUJKXxz3jmB0UfrO3d83E-zCyyZv-M6vR5BSIAMT1C2udZ4kU9pY-6103iKt-AZ0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=ZfMYnl4sNrZjUSNzwMFvegDglUf8Z8fSL_6vevleUOWRxmYmoMI1b-5X3fPr9YOGCquj0lEjpL5p2ZMXDfa7UqGXDhdW0I_JQAJfsTuC4elYW6LZgemKx79H7cAmgfVLtjSLH5m4-N-TyqltnVsjegh6VYsaw5YES7tIqPtbYJUlwkcRRXKP3-cvgqACgzuikG0H8Gr1_xbLULgsQ-CyKTIEw1V0ZDD2wXxECGj48qyPGrnNNcXKItV7YEc14xbmcYCOb0MAxJ7a-ODmeXs4mUJKXxz3jmB0UfrO3d83E-zCyyZv-M6vR5BSIAMT1C2udZ4kU9pY-6103iKt-AZ0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFgUeEM4f2E4JzEAKKyFIdJtM_T4bqcTbGZW1qBcm5nFwJFgVbPcNH4641Jc53iUO5QhIQNDGPGgCcl4maeBvT-gdY2PmGiIO6i4Y6GucLm0OrVxconyPlDw4AAnvCaIjQtYC1LEgHadATeBamyX7jM7OFHoHklWhLYqle9X8bof2RemQ3spGJcfxkxaMChuB-HnOVMs95TM-qbHbyTpb99L3QKVvfcSa2JpUH7aXCFkd41bLEePEc1P-UI5LuWZ9o4W8KfNqBELCuSfEVOLpIBCJm4QUFP6ID0XhBCefWfTawUwA33MQN0112gC3QgJDHr4afmew193t0OcA_kKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=O7x3D0stD19n8N_FnPTTw-4fUXUBQWCr92cvII3Xc4vjT0CqhxoXOg6huf20DA-yrZfBAWnD0Ra1OP2jwBprsPaewwDqJCnd_qqj1xQ5CMgjerqRbnFK5sDtu9GiDt3aJkuuFJurWemxhsz-WVZq_vrTMIF8VcqgQa1aPSwkbHsHowmT9yiYOxlIdU4TD7PtLxiuRIkidXIaYkGw9Aciis9DaBzIhrRaOIQ7qqlttfjAHNzWEf3z8qAD99liQ_iCs4_Fcfdn4ujhFgrfXLWcQyAhrcBAXblrM4Bj-hpr8NgL-a1PIdz8WN1FHFQAbPPKpELOnT2EIH3TM8kfrH7tfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=O7x3D0stD19n8N_FnPTTw-4fUXUBQWCr92cvII3Xc4vjT0CqhxoXOg6huf20DA-yrZfBAWnD0Ra1OP2jwBprsPaewwDqJCnd_qqj1xQ5CMgjerqRbnFK5sDtu9GiDt3aJkuuFJurWemxhsz-WVZq_vrTMIF8VcqgQa1aPSwkbHsHowmT9yiYOxlIdU4TD7PtLxiuRIkidXIaYkGw9Aciis9DaBzIhrRaOIQ7qqlttfjAHNzWEf3z8qAD99liQ_iCs4_Fcfdn4ujhFgrfXLWcQyAhrcBAXblrM4Bj-hpr8NgL-a1PIdz8WN1FHFQAbPPKpELOnT2EIH3TM8kfrH7tfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=HKB_Y4sZxDA9RdMKqwnTalzVlWtKqSqg5hz4m0-bkNGV2skY4Jx2y_XKn_I6Hal7mXdvQcCB7-8YGUgaZcnFMOPObk8G4ECP3RZnkK9Eki9Y27xm-jSxMJ61Mbz9J5sGWcVjYWzIyoEWvQCqdE8cNhcFRgz47AoPdeRVRgs8Qo4l6rBIb7YS_H6AEQSJ_7W0_HyCCOSyxcfiKB1At_wlA-pzLFrp1tgCIcOxco3kXu_giwEcrnzlM0NB62qolBOou4dvh-kpwMhhSKNzpu3w99LFu3YK2Y-nqUNlK51bTUuN_HMgzW9c78YJhTk_WTT6ma3UeL4eTNHNBUqgBcjbKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=HKB_Y4sZxDA9RdMKqwnTalzVlWtKqSqg5hz4m0-bkNGV2skY4Jx2y_XKn_I6Hal7mXdvQcCB7-8YGUgaZcnFMOPObk8G4ECP3RZnkK9Eki9Y27xm-jSxMJ61Mbz9J5sGWcVjYWzIyoEWvQCqdE8cNhcFRgz47AoPdeRVRgs8Qo4l6rBIb7YS_H6AEQSJ_7W0_HyCCOSyxcfiKB1At_wlA-pzLFrp1tgCIcOxco3kXu_giwEcrnzlM0NB62qolBOou4dvh-kpwMhhSKNzpu3w99LFu3YK2Y-nqUNlK51bTUuN_HMgzW9c78YJhTk_WTT6ma3UeL4eTNHNBUqgBcjbKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=klOPpG7DRig9PaPySC4XnP6WUwAIEMUm_pyD9oO68AIzwjE7pgQIvQAluMXELR8BTXfdAZJqdfrZj-nNU-mEZFNH7tEbeQHzRQTtL-QitDEvIp42-5wrpOTu0yJw8WLKpcAg5GpmX8yUO5fnzRNqYFvKKJH4ouJEctPjn2g5ieY5Z6Wi5FIoZ2ncRj4nHaJ2KoGxe0Uf4KwothUy9r8BZ3T_0JmKxACpjoqVlVpVMAXOdbPOPGaBggJPCPk4vNiRTaCsOUSsSpkl5JJe5I6SNepSJ9xTEg5VX-DZ5G1A4u89wQ3ltOn-oyO2H7CJy4I7PQLFxVqwlb8OhNa8J-AB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=klOPpG7DRig9PaPySC4XnP6WUwAIEMUm_pyD9oO68AIzwjE7pgQIvQAluMXELR8BTXfdAZJqdfrZj-nNU-mEZFNH7tEbeQHzRQTtL-QitDEvIp42-5wrpOTu0yJw8WLKpcAg5GpmX8yUO5fnzRNqYFvKKJH4ouJEctPjn2g5ieY5Z6Wi5FIoZ2ncRj4nHaJ2KoGxe0Uf4KwothUy9r8BZ3T_0JmKxACpjoqVlVpVMAXOdbPOPGaBggJPCPk4vNiRTaCsOUSsSpkl5JJe5I6SNepSJ9xTEg5VX-DZ5G1A4u89wQ3ltOn-oyO2H7CJy4I7PQLFxVqwlb8OhNa8J-AB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=KEWVneYoafP2PAXD-rCGgBmryqaxFXMQKnymBaFialyJr57_zrWu9XGwVWQtkXPYO3zpwigEJL-MaqnN94zBv8ZcS2hKyb8HTmvqFDNhMvZEjDG0WhQBTMGUWaRo_8lyPJBOmLkpYUuUi2-KJXNXl-sDBZFuMQu6dehlA0RcAMSMC7FVnLnc9MZNaCywsE_Hu2mPzr1-ewjflZEJ56ucSNMWXWxvnXU3mJ2odyFz8Jwj6YcM_rPplSN9wfy3wgXzYcCaUVJGnWg1CG_ZZzhowfbMMl_ARZ7bU1k0nGjuTxbtsOPlCMUQo4KC2k2T3oarolfnBAk4AjZjR57WmsVU9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=KEWVneYoafP2PAXD-rCGgBmryqaxFXMQKnymBaFialyJr57_zrWu9XGwVWQtkXPYO3zpwigEJL-MaqnN94zBv8ZcS2hKyb8HTmvqFDNhMvZEjDG0WhQBTMGUWaRo_8lyPJBOmLkpYUuUi2-KJXNXl-sDBZFuMQu6dehlA0RcAMSMC7FVnLnc9MZNaCywsE_Hu2mPzr1-ewjflZEJ56ucSNMWXWxvnXU3mJ2odyFz8Jwj6YcM_rPplSN9wfy3wgXzYcCaUVJGnWg1CG_ZZzhowfbMMl_ARZ7bU1k0nGjuTxbtsOPlCMUQo4KC2k2T3oarolfnBAk4AjZjR57WmsVU9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNzYWYGTf9l1T1nFBlDNdPzheaGeu28U-bUj9rlFp-KLleSTwbdA55Ek3eNcyqJVYd4rgTlf2GUCQMlXdvbSOPpFFM2DlyGgMsLiKTGUJDDl4ET8-c5R2OD0RPZB4lM26VCvXLG0IszkugV_PI443aTIGhN4-J9ID-a_qUUYwRmIFfbcXvHxvbDvvTt3JrWd1NUEMGCmhJnNw_AcOsof0TTT5AWwUpT-YI0oVIFGVmEJTGO5DtPOqaVrlP3R5Pw8-FZle-pNRwpwg6-IBA2QFkDfOtQXPy_PefIlXNvRgAiO5zw7kOa1Le70K1Wstbd3TAx05TEQ-qxvTx9vuTHjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=WAlfR2fyGvJFEDuJ1vVfMp6SXzZ8ZLl-5_r-Z-j3wWrZB86LTtNHFfK6eV4V0Un2qvDRNuTN5KS0zGwIbDT2iBmM6KxaSO-mirfHqLndNNN5Koydw0AklkyZB-LXRmHDbNBvNfNs31aK1dObPrJwMZCuuBCIyaf9w30fn1vpziXhZTtQ1pG8BkvuYRaSu_d2EvoQUQDU326NrHHNRyuBN9uJYRPbd67G3fWrmm19tHytPvSxJUXCgPanY6OeW5qhMbsWjdJDpLObIWUkimfvXyLXezRFVzEszgB0aY6BQCZosRebtbQRZOo3oyxFSw9NSMShlmWcl9t1VyNHL8pmrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=WAlfR2fyGvJFEDuJ1vVfMp6SXzZ8ZLl-5_r-Z-j3wWrZB86LTtNHFfK6eV4V0Un2qvDRNuTN5KS0zGwIbDT2iBmM6KxaSO-mirfHqLndNNN5Koydw0AklkyZB-LXRmHDbNBvNfNs31aK1dObPrJwMZCuuBCIyaf9w30fn1vpziXhZTtQ1pG8BkvuYRaSu_d2EvoQUQDU326NrHHNRyuBN9uJYRPbd67G3fWrmm19tHytPvSxJUXCgPanY6OeW5qhMbsWjdJDpLObIWUkimfvXyLXezRFVzEszgB0aY6BQCZosRebtbQRZOo3oyxFSw9NSMShlmWcl9t1VyNHL8pmrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGQrsaFGE4lKQRYowk9oXPTrIU9zTrpj9tUA8NyoH4DPgQA0z0_YzNgdqeWICRizszAdEVrSf6unVs2CRBqhzIz5HhM7-6ZFcKg4R1qN1EE4BwKoll4bj41I1ZRy0jJihnfonremYrVtYde2FK2-hYFpNWhfZzE5Gk0cVoDKD89x1QiUBAlTe-cu_o7wHer4qa9tDNJuO8KTRrICrdv-0jZHvz468ZNddRmfvdy_5W2zy24-qgSYvVphspx2WxknaSlGPyKLMAO9Lc5-wGa2EhQeBnSlVy3_5_vrfmLn1PeLA-EakmjuAJ7e2P4tIlcN_83s4GSHygXXoiHHMV2iFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=sVwWodhBV38_FVkiq_h1MhTiulAYYwe06cOAYx_hAYIRO8E6wJeg0TGf0gGqzQW0bK8_wbEunKjvJCSS_a5tcQkcSxrC7B3MtKzvK7eqfvmx2tRLmFTU6K1mkWUDDVtTWwR9BW6dc0Uyindo_SUhmFPI4gHHAzsf_FMzFzCFky8cChryxy9tWwuOMm0-EHpK7i9oOUodBpzbeo_OmBQ1K3YnhKyn_eEHXSb_wFBQy8gro9pBOP6wf7RTn9We8ynWVGb8C64NlKQoAXEvzca4Ih9GwxuM7kr23WMjNal4A7lzd5QEsPuLwGHPrCBI4S4VtpZKdNCQwvo9q5hDB1NcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=sVwWodhBV38_FVkiq_h1MhTiulAYYwe06cOAYx_hAYIRO8E6wJeg0TGf0gGqzQW0bK8_wbEunKjvJCSS_a5tcQkcSxrC7B3MtKzvK7eqfvmx2tRLmFTU6K1mkWUDDVtTWwR9BW6dc0Uyindo_SUhmFPI4gHHAzsf_FMzFzCFky8cChryxy9tWwuOMm0-EHpK7i9oOUodBpzbeo_OmBQ1K3YnhKyn_eEHXSb_wFBQy8gro9pBOP6wf7RTn9We8ynWVGb8C64NlKQoAXEvzca4Ih9GwxuM7kr23WMjNal4A7lzd5QEsPuLwGHPrCBI4S4VtpZKdNCQwvo9q5hDB1NcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=qUwkUFuyBZ6AmHdB4KAd-OOft1a8Vcg_zmrf5Nbc2jXkOosaqsI0d_HCGpIgXe8l2g0c7ft4rVcxWFNA3qF2-G_SgUEomOrk5Pt8MxlZGHC6kfEj2-fv01Uy92Ve-FY4FYzAs5nhFTX2nABKYGGHLq6B_q-o_TxmzvLoBBRm8MK73YmEdveoheSL1qeFDD8QV1YZGeT-qIPpxVGyMUR07o1Zg2JAEjzKmF7BvknzRTYIJC1RWlciIOu5k0EUvGPHJp06vAVQa8Ha5M5ksWVFQbVCgkS5Z45KPMlVUgsGQXBTMM5RY7jzc5g-Mx8fDIvCvRpSARoRfP-WBuvUubvmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=qUwkUFuyBZ6AmHdB4KAd-OOft1a8Vcg_zmrf5Nbc2jXkOosaqsI0d_HCGpIgXe8l2g0c7ft4rVcxWFNA3qF2-G_SgUEomOrk5Pt8MxlZGHC6kfEj2-fv01Uy92Ve-FY4FYzAs5nhFTX2nABKYGGHLq6B_q-o_TxmzvLoBBRm8MK73YmEdveoheSL1qeFDD8QV1YZGeT-qIPpxVGyMUR07o1Zg2JAEjzKmF7BvknzRTYIJC1RWlciIOu5k0EUvGPHJp06vAVQa8Ha5M5ksWVFQbVCgkS5Z45KPMlVUgsGQXBTMM5RY7jzc5g-Mx8fDIvCvRpSARoRfP-WBuvUubvmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=OYARqdXvt-YPoJM5RyH0F-Lo_TXhpxM8jK7F7kdSB4zqVeOjrj1AQGt1qRzwN8azOiDNeUwJ_Ktq8B7SjcW6egBhZPVEDiC9Er_l24zFQ5L7oZjRQsWjzsFerBkuJBrpkerl-EqH2lXfkMSMIrWUP_A7Ftmf5F-Tmrg8TYXOTCNB3rGi68hwA5GxSG8230FGKnBe4T8Ajnftz22SgAWAAknWmZCr8zSP1ypa4WrAYX-yJ68KSdTjjeqh_bFrk_mONaZbXS-opy9hCNvp0-u5dOBvPP-YoWgVcflpBfSLH8iuYl08bitojanyntKzWBxzzis0LCkfUq-PoPWS5AQ8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=OYARqdXvt-YPoJM5RyH0F-Lo_TXhpxM8jK7F7kdSB4zqVeOjrj1AQGt1qRzwN8azOiDNeUwJ_Ktq8B7SjcW6egBhZPVEDiC9Er_l24zFQ5L7oZjRQsWjzsFerBkuJBrpkerl-EqH2lXfkMSMIrWUP_A7Ftmf5F-Tmrg8TYXOTCNB3rGi68hwA5GxSG8230FGKnBe4T8Ajnftz22SgAWAAknWmZCr8zSP1ypa4WrAYX-yJ68KSdTjjeqh_bFrk_mONaZbXS-opy9hCNvp0-u5dOBvPP-YoWgVcflpBfSLH8iuYl08bitojanyntKzWBxzzis0LCkfUq-PoPWS5AQ8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G74JnUrL8o55tU179Vm7thAJfeA2-axTKdSAbxN1otg1_2HBEn8YbjlqkiJZkOK7biWsbQyUDr-9qLaZCnJ7Ts2iYjMQE_MgvrqVfUTEtZAC6fhJaEp4TSfjdtyuwn_EqiAxLSF8LTSLJoiZxnKauM_LlNErKDqpSR4E76rswFTK11M7gSZj02SGTQK9BdFzDc3gdFc7Thm_rEmwKUp4_KrXV-3BZBF6DwG3legI54VzflumFTrUsJbEStoBQrB7MYawAiZnng2grTQC_MF3QdLH1yf2AuoZElgASWMV7H48MJFfMlb5XB0BncOKfYI1LfcMNFZjqeRIDeQVr6cq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcB47zkhuKyDSHLArya_zLzRLiz8ZldJACfvuqzJVbpzMOU_yrlayLog6ZP1I_caO7p9aEqnLNRrMOqXuFH_cvLPWSq8HDDwRyv52d_tMWWwxiiEjWJ_mTI93X_MmP6gttCpja1lISycmj6F4u9SEXaGxUgpuoRHP1mHgC7-7r6t44Ukz1dI2dkMvs3VK9savHOoXxkZqFqjazJtGFFhFJRw3DByk7daeCttCPzo-Wpq2PE2ng2fPK7Azv-MpkqEhuk8i4EHiRLdZuXO9_8Q6KrSfeMvI7JhRxai-KnUUy4DVko-FGFACM8Td2zXi-E1hIfH3Ui1mNR15lmx1xsxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn1.telesco.pe/file/fCxzT1-3qnhk1rJabGE1KGwe_6CV2peJWRj4XBAQo2VCcnsGFytMQHzlJp--FWLLq1KJnBXwMoHNXCF8R6L75QjsHM7nkyGXebe4wr038vRsY1tjBCr-oNuFvwIhF52ZxxM0rNf7_Pcc9P8hHMm5JyONW7uQN3C0NcMYKs7OoOjtNh-pwJPHXYQeYXKb5YHfOLMqUliKVVnAJJGH_F9rldIEaTmo9UYt1WcOZv8VQEUdw_3nk1NnLO2nfONveNgbVaPBATcTQoPupkK3hP__3dsUlaM-AeqhfK-4ulfmkMFL2n4ha_6huQLGJ6pp0uDxtjgioqNDq_PfTUnk9oPJow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 120K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 02:56:55</div>
<hr>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCIMkhKEWu2kTrgoL0KzV5n4-q05qxfBj4jQLvvDqqWHgwHmkh5cnvtyhTefhi3tdUtqWe5dha0rgtEn0n9MnSklBOE11HLxSW_j-tX9fJyjNlF933_417O-mmk4Z4BqVsWASjxSapzN-Kr8JnEKr8Y8GDG_LT9hRkxSOcwQBkKH9NdY-EB_UHlfqI2eVphQY6q0SKg_LvWWTPu37qYMtlnK5qhzStKd-nWcYyMFtIQBO0CqHK7GasDmxb-FccdWC27m9EmrBYnOMKXLQBE04qIEtQYReDNKH501WAMIv7ZBM_14SRJIvQqHMm61Ph5T5lIDuqWzgv6Z6CICd91rFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eEvIWg_hbLqkWGohtMNTyQlyYntOfPcwbFF7P7nfQ1Kk3cg1ck4UlXe5IbPUym-XSX6nkFcyt_XODAJ5X6iOS2CdJlOIqWRsPIpZRstsGl7FEBHAzi7nUHWF1mytntCGO3C4yFAG60q4VfgmKnxCf_1GogtN7lQdYY6g28wJoDbB-s7F5MmdZWjmG4zcBmFJkAc3Si9vFJxJoFsgPwsJW1v7U7rUEXw995HReIpSNqjomBIN7_O1dm2vWiLFz4lNZxUncwXzmysItyqCM3nX0sqpmXTzTJdZ2YWSaGBs9DYlPELId0AG-dacDWKvXHTue4A8YL2ymHlfxAZE2rD9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUlG-WG6YKCYIn246u36FexESWRXxHRiYDEN7AgRFZSET9PhosotU9IdPdqcEeJP-taK2TFD_VOkcWAzuVDD0fPsHcRyhLxCCFRrcwBjHmBQyd_lRDWYcll2rp4mxCdrGOaufgGw7HbwwvRuHkdUt6vtifJXV-9S8FcLVLWhF5YrpC5Yw3C3Jj2tcoIBKhqXzZoolNyuu_AjWFV2lM64R1SHIeZ92agMMtMSOHKWVAgZ64AgBnW2Py8i2xDeNwSqT93HZJj9zFfQN0pp1BBSkC9Ru5-u7t0oypgsHlfvACh_bVH-1J_8BE1IifTDWc2OPhiF-CJOGqG6GoX3gabVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این اسکرین شات فیک هستش و ساخته‌ی دست یه سری از VPN فروش‌هاست. یه دور بخونید از روش میفهمید یارو خیلی هم عجله داشته
🤣
لذا خواهشمندیم زیرا</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3107" target="_blank">📅 18:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">CDN-IP-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3106" target="_blank">📅 16:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3105">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iXN5pmX8rmmTp3AAt7L6oDiNHXY_2qpmM5lX0Zn_Et2VGTbEVU1bxBasJFMvtPoEsm7Oi87yjSRKV8fLB7IvS5X8Z6_cxg4IJ7flSJ_M1s3wT80UAVxvOJScGBs7_5ZtXjI2Us6aStwrwX_VY9otbc8h32_ZQ5_fADuCtpYKoN97g1dpYr_yPk92U-HqEYruOnXfI17Yx4ckIFxRuPxJssP5eMgfpnrxIczu0NKgAa1OF35vF3iV-rmWNeCWd3CHzzAPHvrEzAFbQyfSf0nehTSL4hKQM9AwV8B11qSWpHk6jyW3dVkYRvP5aG6SibzmCos4hP25D5tPPMTElxi93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان.
مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.
هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3105" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN-IP-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3104" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی آیپی CDN و ... از اول اومدن این متد توی توییتر و کانال‌های تلگرامی گذاشته شده بود رو جمع کردم، دادم AI تکراری‌هاش رو پاک کرد و واستون گذاشتم توی این فایل تکست. یه تست با اسکنر بکنید و بذارید متصل بشه.
صبور باشید
!</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3104" target="_blank">📅 14:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو. بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید): socks://Og==@192.168.1.147:46597#ShirOKhorshid…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3103" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3100">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_arm64-v8a.apk</div>
  <div class="tg-doc-extra">59.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش اتصال با آیپی‌های CDN از طریق نسخه‌ی جدید MahsaNG:
1- وارد نسخه‌ی 16 میشید(نیازی به هیچ کانفیگی نیست)
2- اون بالا روی حرف F میزنید
3- گزینه‌ی Psiphon Only رو روشن می‌کنید
4- روی Psiphon Setting کلیک می‌کنید
5- بخش Protocol رو می‌ذارید روی cdn_fronting
6- بخش Aggressive رو قرار میدید روی ON
7- توی بخش CDN Fronting Settings، آیپی‌هایی که من بالا واستون می‌ذارم برای هر اپراتور رو قرار میدید
8- روی Save Psiphon Setting میزنید
9- برمیگردید به منو اصلی برنامه، روی دکمه‌ی گرد پایین سمت راست(اتصال) میزنید
10- یه نوتیفیکیشن Psiphon tunnel connecting میاد بالا. اون وقتی تبدیل بشه به connected یعنی وصل شده
توضیحات:
1- نسخه arm64 برای اکثر گوشی‌های 2020 به جلوتر مناسبه
2- نسخه arembi برای گوشی‌های قبل 2020 عموما
3- نسخه‌ی universal روی هر گوشی‌ای نصب میشه فقط حجمش بالاتره چون تلفیق تمام نسخه‌هاست اما حجم نهایی نصب شده روی گوشی شما همون دوتا بالاییه
لینک‌های داخلی:
1- نسخه arm64 داخلی:
https://guardts.ir/f/ee1f60ae6d33
2- نسخه arembi داخلی:
https://guardts.ir/f/9d474d75a4fb
3- نسخه universal داخلی:
https://guardts.ir/f/7af85b518302
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3100" target="_blank">📅 12:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompng(Asal)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3099" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
اسکنر سبک آیپی برای شیر و خورشید
-فایل بالا رو با مرورگر باز کنین
-رنج آماده آیپی رو انتخاب کنین(با میتونین دستی رنج‌های آیپی مد نظرتونو وارد کنین در بخش لیست بازه /ip)
-بدون وی پی ان اسکن کنین .
-لیست آیپی‌های سازگار با نتتون در انتهای صفحه در دسترستون قرار میگیره و میتونین وارد شیرو خورشید کنین.
@p1ctok</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3099" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbn4Dry5qVxYsTdI-3FeuIUFOZzt2HqdN6bDsADGK2XOtnfJRrVyi3cB_CsEhuQRrJjeoVExvI1BGbet48JH4Cvx48fFsqpyPAzwIgXkI2B8LDpsJjXa83oLUqYfJEYwvMUxuImpw73AvgZUdp_GiTDlDnCuQvZmAZXH8WcFy6I7gwQY6k66agaJ2eDrw7NGM3OZ7UfcBNSSmUJR9luD-esN1qiyeroT3iko3WjewV46aVS9zumuSzCcRbxTOdgN51KxAFPxOizOaXDiYxWYwE3Ua4xcrF3mrIcyD1uhrmb8kKwpMGR6T3C4-uuix_y8HB6AC3y0cvSwOUkQagyafKRJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbn4Dry5qVxYsTdI-3FeuIUFOZzt2HqdN6bDsADGK2XOtnfJRrVyi3cB_CsEhuQRrJjeoVExvI1BGbet48JH4Cvx48fFsqpyPAzwIgXkI2B8LDpsJjXa83oLUqYfJEYwvMUxuImpw73AvgZUdp_GiTDlDnCuQvZmAZXH8WcFy6I7gwQY6k66agaJ2eDrw7NGM3OZ7UfcBNSSmUJR9luD-esN1qiyeroT3iko3WjewV46aVS9zumuSzCcRbxTOdgN51KxAFPxOizOaXDiYxWYwE3Ua4xcrF3mrIcyD1uhrmb8kKwpMGR6T3C4-uuix_y8HB6AC3y0cvSwOUkQagyafKRJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آموزش کار با اسکنر آیپی برای اتصال از طریق CDN با هسته‌ی سایفون اپ MahsaNG ورژن 16
این آموزش رو فربد عزیز زحمت کشیدن ضبط کردن و برای من فرستادن
فایل‌های مربوطه رو هم در ادامه قرار میدم واستون، و دارم فایلهای MahsaNG نسخه 16 رو واستون روی لینک داخلی هم آپلود میکنم</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3098" target="_blank">📅 12:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
): 184.24.77.42 2.23.168.213 2.23.168.174 2.23.168.7 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 2.23.169.111…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3097" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3096">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
):
184.24.77.42
2.23.168.213
2.23.168.174
2.23.168.7
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
2.23.169.111
2.23.169.105
184.24.77.11
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
23.40.63.69
96.16.122.74
104.109.250.232
92.123.104.7
104.110.191.57
104.83.5.82
92.122.166.168
104.83.5.65
104.121.0.17
104.66.70.133
92.122.166.146
23.73.2.161
92.122.73.138
92.122.166.141
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
104.83.5.216
92.123.104.67
104.83.5.203
96.17.207.151
88.221.168.138
96.17.207.149
104.81.108.10
23.73.2.148
92.122.166.175
172.237.127.6
104.81.104.13
96.17.207.137
92.123.112.7
96.16.122.75
96.16.122.70
92.122.166.182
104.109.128.153
104.96.143.134
23.73.2.141
104.83.5.202
23.67.136.200
23.67.136.202
23.65.119.52
92.122.166.236
92.122.166.234
92.122.166.237
104.110.138.190
173.222.200.5
184.51.252.36
184.51.252.38
104.83.5.208
96.16.122.146
96.17.206.214
92.122.166.197
104.94.100.73
104.83.15.66
88.221.213.81
172.239.57.117
104.117.76.40
184.51.252.4
96.17.207.30
96.16.122.83
96.16.122.150
23.73.207.11
96.16.122.77
96.17.207.155
92.123.189.82
96.16.122.82
96.16.122.66
96.7.218.219
96.16.122.137
184.51.252.157
92.123.189.41
184.86.251.12
96.16.122.154
184.51.252.152
96.17.207.12
23.79.48.162
151.101.0.223
151.101.128.223
151.101.192.223
151.101.64.223
65.109.34.234
142.54.178.211
2.23.168.47
2.23.168.96
2.23.168.144
2.23.169.207
2.23.170.80</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3096" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یکی از
بچه‌های توییتر این
آیپی ها رو یک ساعت پیش منتشر کرده برای شیر و خورشید. همچنان متصل
🔥
184.86.103.210
96.16.248.183
92.122.16.5
96.16.249.60
96.16.249.9
23.12.156.115
23.216.77.16
23.62.61.53
23.39.148.245
23.210.73.133
23.44.201.136
23.205.46.167
184.30.150.142
23.220.161.217
184.28.165.4
23.46.230.133
88.221.168.204
104.96.158.174
184.51.252.4
172.234.199.15
104.85.26.14
172.237.145.27
92.123.103.24
172.234.159.58
185.200.232.43
2.17.100.200
2.19.205.42
2.19.205.50
2.19.252.134
2.20.169.70
2.20.170.91
95.101.111.144
2.16.245.188
2.18.69.150
2.16.106.4
23.58.222.107
184.25.28.31
23.47.124.134
23.50.131.147
23.46.190.18
23.58.222.147
23.56.162.186
23.44.203.68</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3095" target="_blank">📅 02:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دست از سرم بردار فیلترچی</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3094" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3093">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گویا یک سری دوستان با تغییر LTE(4g) توی تنظیمات شبکه گوشی به 3g تونستن راحتتر کانکت بشن به شیر و خورشید.</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3093" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3092" target="_blank">📅 16:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uc44K65A0p6iaoElSdkpL9aywLbqAXm8Sah5kLQmlxA2UVM7wrjUmRgnE08LUuQfCawAlvamUlDUgE4IFa62xQbvTUh6hskLyR2NddtqHtU5YAs7pTOFW5Bk8c2jug7luAM30IMMHUNyolJCrpjd-BpF-NG_9I96rMD3SaIOntYwOSjpPZYjP2GyI5nyXK42PfIMasukHhOsxMjt3y8LLhL5j7hleFNvlwat1LEaTudq4vx1kfu4DFsdO1EpsXL6vJui2SS5tuhCwLUxGKts4JP_XYqPyc1zqru6bYrSSPrjQ-9sJIBLiVJgSFpyREHfSRN_2ZwxDWkdmYTJJznwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره: 184.24.77.42, 184.24.77.32, 184.24.77.5, 184.24.77.7, 184.24.77.16…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3091" target="_blank">📅 13:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3090">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3090" target="_blank">📅 12:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره:
184.24.77.42
,
184.24.77.32
,
184.24.77.5
,
184.24.77.7
,
184.24.77.16
,
184.24.77.36
,
184.24.77.21
,
184.24.77.11
,
185.200.232.49
,
185.200.232.50
,
185.200.232.42
,
185.200.232.41
,
23.48.23.186
,
23.48.23.133
,
23.48.23.195
,
23.48.23.178
,
184.24.77.29
,
2.22.21.152
,
95.101.23.82
,
23.215.0.164
,
23.197.161.35
,
184.28.230.87
,
23.220.128.221
,
96.17.207.142
,
23.50.131.18
,
23.36.162.209
,
23.219.3.212
,
23.223.245.150
,
96.16.122.59
,
23.2.13.138
,
23.2.13.144
,
96.17.207.135
,
23.220.113.51
,
96.17.72.41
,
23.203.185.105
,
2.16.27.71
,
2.16.244.11
,
2.17.147.89
,
2.17.251.98
,
2.18.190.26
,
2.18.190.27
,
2.19.10.30
,
2.19.196.105
,
2.20.255.113
,
2.21.89.66
,
2.21.239.10
,
2.21.239.21
,
2.21.239.23
,
2.21.239.29
,
2.22.6.68
,
2.23.176.166
,</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3089" target="_blank">📅 12:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCBh-TojqdGbhOV3w-4mhrWXhAfggo11M2C3vSh934wnU6GS8EhnDQIbUkQ_OwmVAbA4UN-KFy4v_y0HXfzidQ1ONIT-5G10eYgdqpAirpcDTUR7q2iNeV7aFEFPaofSab6fbODTWgNMulIVcxcIBwU50HxvlMS6QHgfA-em6bKX9Uj_6pbdAUHgu9tNFTpkl2W5Ly28SNVTLIwh4C_Sa0j_CKmTVPGK2b5epe0uRNO1xXqb-Y1d-pJvKlzwCDj44mDaThnuMfa4LwHWANbbQ6we4IKmMZk5XbG-9NGcNDJD7Q8ZBbc_6IKBiHm1EhvfvbrCNqY_PMahjREX_By6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر راس گلر
:
روی ایرانسل تست شدن، مناسب CDN شیروخورشید.
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202
همینجوری paste کنید اوکیه نیازی به کاما(,) نیست</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3088" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrrDEkhPR1lISYXOKwv2SGXZ_xxQnuHLCRnul9NILzskmcoYJpVJu3zeSxS55F24xjXgv18imYBHZq5B_mTMms0njYEPYeWEOB9gMsp0_7ciGhjFHuFTbh-vRzURyhWMRTPfe6u-0-6wzZSlH98ACHG7B2kOT8X22PLrUGnBo_0TmrLv7xMjRpLwPM6WWVUY7gwBDETP6ob-cwIOBR2-PmNbK__dwLot5uPjsj21voNbJwXnp2-NXJpdDA1-kZinTfi6BuT6C2lHKJKiVw3lJSmEmJzHf2xNoFBoGWsrychpcXdKGUc6TkXjFNBc6XCF1l2ghLX9_Q7dd2jLvN_HbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود اپلیکیشن‌های اندروید از گوگل پلی با اینترنت داخلی
از طریق این پروژه، میتونید ربات تلگرامی‌ای رو ران کنید که به راحتی لینک گوگل پلی شما رو تبدیل به لینک داخلی میکنه:
https://github.com/ZethRise/PlayDL
این هم نمونه ربات پیاده‌سازی شده:
https://t.me/APKNitoBot
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3087" target="_blank">📅 10:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3086" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینها رو یکی از بچه‌های توییتر جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم. آیپی برای شیر و خورشیده، بخش sni رو خالی بذارید. خیلیا تونسته بودن وصل بشن باهاشون: 2.16.27.71 2.16.244.11 2.17.147.89 2.17.251.98 2.18.190.26 2.18.190.27 2.19.10.30 2.19.196.105 2.20.255.113…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3085" target="_blank">📅 08:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینها رو
یکی از بچه‌های توییتر
جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم.
آیپی برای شیر و خورشیده،
بخش sni رو خالی بذارید.
خیلیا تونسته بودن وصل بشن باهاشون:
2.16.27.71
2.16.244.11
2.17.147.89
2.17.251.98
2.18.190.26
2.18.190.27
2.19.10.30
2.19.196.105
2.20.255.113
2.21.89.66
2.21.239.10
2.21.239.21
2.21.239.23
2.21.239.29
2.22.6.68
2.22.21.152
2.23.176.166
23.2.13.138
23.2.13.144
185.200.232.50
23.2.13.152
23.2.13.153
23.2.13.186
23.2.13.201
23.2.13.227
23.33.126.163
23.36.162.196
23.36.162.198
23.36.162.202
23.36.162.208
23.36.162.209
23.36.162.215
23.37.197.128
23.37.206.186
23.38.49.97
23.39.249.249
23.40.63.69
23.41.37.129
23.44.10.10
23.58.222.147
23.59.235.208
23.60.69.118
23.65.119.52
23.67.136.200
23.67.136.202
23.72.248.214
23.73.2.141
23.73.2.148
23.73.2.161
23.73.207.11
23.73.207.16
23.79.20.249
23.79.48.162
23.192.46.51
23.192.237.208
23.192.237.209
23.192.237.222
23.197.161.35
23.200.143.71
80.67.82.179
88.221.92.177
88.221.132.162
88.221.168.5
88.221.168.138
88.221.213.81
92.122.73.138
92.122.166.141
92.122.166.146
92.122.166.175
92.122.166.182
92.122.166.197
92.122.166.234
92.122.166.236
92.122.166.237
92.123.102.104
92.123.104.7
92.123.104.67
92.123.112.7
92.123.189.41
92.123.189.82
95.100.69.108
95.100.156.147
95.101.23.25
95.101.23.27
95.101.23.82
95.101.23.168
95.101.23.170
95.101.29.12
95.101.29.30
95.101.29.54
95.101.35.73
95.101.35.83
95.101.181.125
95.101.200.63
96.7.218.219
96.16.122.48
96.16.122.55
96.16.122.59
104.83.5.65
104.83.5.82
104.83.5.201
104.83.5.202
104.83.5.203
104.83.5.208
104.83.5.216
104.83.15.66
104.94.100.73
104.96.143.134
104.103.64.7
104.103.90.156
104.109.128.153
104.109.250.232
104.110.138.190
104.110.191.57
104.111.202.158
104.117.76.26
104.117.76.40
184.24.77.32
184.24.77.36
184.24.77.42
184.25.52.200
184.28.230.87
184.51.252.4
184.51.252.36
184.51.252.38
184.51.252.135
184.51.252.152
184.51.252.157
184.86.251.12
184.86.251.27
185.200.232.41
185.200.232.42
185.200.232.49</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3084" target="_blank">📅 05:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نمیفهمم چرا هر متد جدیدی میاد و هر راه جدیدی باز میشه، یه لگد به گیتهابِ بدبخت می‌زنن
انگار فیلترچی می‌خواد ما رو تنبیه کنه
😂
داره میگه دفعه‌ی بعدی گوگل رو هم فیلتر میکنما، حواستون باشه این سری عصبانیم کردین</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3083" target="_blank">📅 04:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">طرف بله و روبیکا نصب کرده بعد میاد توییت میزنه که اپ شیر و خورشید(که اوپن سورسه همه کدهاش وسط گیت‌هابه) بو داره نصب نکنید امنیتش پایینه🫩
امنیت؟
با من شوخی میکنی؟</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3082" target="_blank">📅 00:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6hiEt_4HbDp_bxYrw_mBj355J2InfMPFlCX1a8lPskoD4Cnyb3zAEc6r8drq3sX-5qozvC0hKu7DxylkaRw--RFZfWpyZmRFQ3WjNKn0DOeYnjBCdLC1QdrAxoFb8QMU0zyLR9eys_dz7QYCjbrlAlH072dmcW1D16w44i5RWGwi3gfY_4a4QA-lNVeeJ5Iyej3u3RI7_tpHgsUTNHIf1Bj5bmykeYUfU-EE9-pqjAc1_fnqokhyuKR1hH_QElf7fDcDMZfcLXh_BUuJOaLpmISAGL0oljNgcOYsK9Y8UahLpxb3iLTtnw9vEYU8wAbFcnELUAguemTyOx1vYxUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چیه درست کردین
😂
😂</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3080" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3079">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبر خوب:
نسخه‌ی اولیه‌ی WhiteDNS برای IOS منتشر شد:
https://testflight.apple.com/join/GfUqXrFz</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3079" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش: https://t.me/MatinSenPaii/3070 کافیه که با کاما(,) پشت هم وارد کنین:  2.22.250.149 23.58.193.140 23.48.23.151 2.19.126.81 23.202.138.125 23.43.237.239 104.112.146.82 23.2.13.136…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3078" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش:
https://t.me/MatinSenPaii/3070
کافیه که با کاما(,) پشت هم وارد کنین:
2.22.250.149
23.58.193.140
23.48.23.151
2.19.126.81
23.202.138.125
23.43.237.239
104.112.146.82
23.2.13.136
72.246.28.37
2.18.63.49
2.16.53.11
2.16.53.50
2.16.19.136
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.8
185.200.232.43
185.200.232.40
185.143.232.122
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3077" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3076" target="_blank">📅 23:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oqMQwOfuKK68Z4Y96QP3TxTKIJtMkU3x4XT1M2bv_6dkpTBLuaUOWaLCFwgTI5677zGv_fvaTcliSV64x2n_Xof4mhlujsQQMR4jJ1pxNgfYKLL81s7SytnRv4HBwsc_g0mkLLJcKRuzCBBNEh5Pj-EhkLUHRIvQUw8J0TyNmFoXeLo_lA6pAIuarUUbU2vNLhBcXkAB5jv7TA_5HyScxhhGv-JzJBRvp3umLwJ8YvHcFbzJBjKfNsehEoswhTXd1E8yRWneBalVMxp53Yc88wTi_n4TPVKTfKQdlkvBAXGII6zfZZ7ks_otzr4xyMw10DzEebZVwJSKyKpLeMQ6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I1QB_dbh0dqVAAQ6pFDimoSmKD2BlLFxa6lGlpU_KPhPLai7P9EiYoxToFzut7jz1LQkBFk93llJtQK2nHgrXYzS_oJs0wmeITysZafhWJNRJjdmOjoZDFJhRuBE3Mqk4oKLy1gKIDWDTbhHAnkUUREYeRXB2Ep_NGVaA7V08KjnFOerTX2f40nNEXsnnyE0yOucE_wcjMvMSTY7WnOsrTpH3U4bo8RdofWGDm7A1NKXzQG9gYKebxFAfkqmjhBbn-qlG-lfbENBqcLQnaw2SZu6brUn6TfT36tyavvvIVNUjTOxgrnz3Uo13-Xqh9d8nthXRTx6LHVLiGMOkpsePw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو.
بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید):
socks://Og==@192.168.1.147:46597#ShirOKhorshid-MatinSenPIi
و توی گوشی آیفون(با Streisand)، مک‌بوک(با V2Box)، و هر دستگاهی که کلاینت V2ray با پشتیبانی از Socks داره می‌تونید وصل بشید.
خلاصه‌اش:
ببینید، گوشی A رو داریم که اندرویدیه
گوشی B رو داریم که آیفونه
حالا دوتاش رو به یه مودم وصل میکنیم
روی گوشی A شیر و خورشید ران میکنیم
میریم توی V2box اون کانفیگی که دادم رو(با آیپی شخصی سایفونتون که توی صفحه اصلی وقتی این گزینه رو فعال میکنین نشون میده) وارد میکنین
و میتونین عملا به شیر و خورشید گوشی اندرویدیه با گوشی B که آیفونه، وصل بشین</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3074" target="_blank">📅 23:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6mNE5cJNGWWg2KeIaHZqFj-Er5aFkZYfJP4fXdcDpWsLEWPIe9lZedWZBK-INgTtcuZbwfEXhXoKU6rBzyFIaF_DSbIMuV4c_VWOtGcSSVu-cb1wEhqsAgKJogsjV-ZPv-ZKk_wT0pEhOKdlf5dXZG1DGWjv9Z_VvuEeNnzIgdhmBxVyGXIns7y3CJliviQWfQw4qzb6MFYjacppN_XULWkHFTbNGL7DlpfpMRDBlM-RH3KYP_5_c0ApGMLEL3g86LnL95WTRywwBtNfRyAUmmPRc-FS-couPL9d_o5eS4ZRdVYQ-vKG-Jpd9Owqpfe2S6HSpD64excANrkqyismA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
‏این دوتا هنوز وایت لیست هستن، چک کنید ببینید میتونید باهاشون وصل بشید یا نه.
sophos . com >
185.200.232.27
,
185.200.232.16
> Akamai
www . mathworks . com >
2.23.169.12
> Akamai
برای mathworks حتما www بذارید.</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3071" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jw1dD7nWQVAElM7mOhcQX377Z6G5oVr0PDsLxxjPhtQlcDnOKYX-AP1Ck2RErrSiZ1yqKj4ieSgCkZnGXjb0lp6cxBM1j0TcXmXeBHAv7hD6nT19NkUhFAdrzzADOYcnPNHt_2vbmaD9GCyOkPepkqsM8vS72HlkDAWyc4vwv1i9NvgLy54d4_EObBg_Npul4BwFE7Pb4McZQNXkTUjConF2opNeKXJh2kDNHCRjFrOu-e36D1N9SA6SF05M5_HEMpmnCOhzsqm3wL73CSQiICrQSpOkqFaC-wlaIrBXHjiKgE8jVhZlYjK2owzCj9wItEHliarXc3j_Wv4nlxvX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر روی ایرانسل با این دوتا روی شیر و خورشید وصله کاملا اوکی:
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎
توی همون قسمت More Options هستش</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3070" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-MatinSenPai.npvt</div>
  <div class="tg-doc-extra">3.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3069" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3069" target="_blank">📅 17:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Umf_UA47U0ht2Y-FBK5LZM3kwhnsAQ82VEtUH-BcdzlEcOdvPTNvpc2oezDVod_C9FDdarhhTJwwpCxxmV4IwXTxqFRW_A62aCYAiIWVhGmPXOZggSa4ojqxHR0xA043vGhtre8PTLMsSDziqlVmR7RKtIJNC92CJoWR210o-jDdKMFvt_7N4ulw49ssJi1IjAGzzRnk3JwuqkGsfb3Lfd-jElFIgBCR9sBs9RZ5XIzR3GLJBtuf97aHv7_j8Q_qMCApKxFSMpugZDjciTc5AHUK8ewrKewsx1pMIr95zWyE3dlERgKvluFz4502qymjZMORcl98Xfa-Z6_8ry6Zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود راحت‌تر پکیج‌های Dart و Flutter
وقتی "
pub.dev
" کند یا ناپایدار می‌شه، PubYar کمک می‌کنه پکیج‌ها سریع‌تر و مطمئن‌تر دانلود بشن.
پاب‌یار فقط یک mirror ساده نیست،
مسیرها و DNSهای مختلف رو بررسی می‌کنه و بهترین راه دانلود رو برای "flutter pub get" انتخاب می‌کنه.
مناسب توسعه‌دهنده‌های Flutter و Dart
PubYar.ir</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3068" target="_blank">📅 15:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گوگل من روی همراه اول یه بیست دقیقه‌ای بسته بود.
نمیدونم دارن چه گندی می‌زنن باز</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3067" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DPGIyDBPhDkIFWSKE03sj8Sl-NGTDOybsAlfI5hI7L2QfzVPbgSc61EnX0JCNhkIG6FHgEb8N4Iv_cJFgg342yB3cGjIzqu-55Pn93ZJif4paYzAfdi5dV5SKM_gXYpQImmge7DhezCNOJIKz3ted25ubepC4UtSzQYindGxMpOZBgnv8GVc57biHvIOYa21eaEeLqZ2mhjTgC1OfkQ3FWRkC29OngxBiRrZ4fUWVMCH76CAeLhPNxyXSmeZ6NzyW1ePV9yBWrryzt35xKkNVHrMffuGFHVYj0opOXPzwEPFzp55jaqRp4ienXOvasCR7CC2byZQuLdIf37MEPsUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qe8zHrKDD-Nn9o6ZjIpd-Ma-L7-Wh032K0u224QsjPR1qtBxkWTacJoLSq3v1GwUqgWpPQ7C0ZVn_zH68VgQSl9MoWmszOv_Hac_748ytGTAGZ_BoyYRiFfW5Jfo01pV5DHWALg_xFdJJ3l3SsUfu42J7RSCYm0HQPFB_WqCHtdZQFSbIxk7kBIie2oGs20DKsd6Vbsqqzfh4UBtbeMPOC6MnseGE1c50haVzmPgVcG3tEJ3vQFXURhluPlGGR176JGqUoWmgUvVTjmK0lMgB2S1tkgxLJVZf3Be-1-BYmtdJyGC4VzgCRQjAVLTD1sD3TyU1O4AoRAUj5iPotuvdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3065" target="_blank">📅 08:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3064">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ورژن جدید White DNS با یه سرعتی ریزالور اسکن می‌کنه که آدم باورش نمیشه</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3064" target="_blank">📅 07:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3063" target="_blank">📅 06:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">masscan.rar</div>
  <div class="tg-doc-extra">1002.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم نسخه gui مس اسکن خیلی کار کردن باهاش راحت تره
قبل شروع اسکن باید winpcap-4.13.exe نصب بشه روی سیستم(سرچ و دانلود کنید از گوگل)</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3062" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3061">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.txt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر بسیار پرسرعت Masscan برای اسکن آیپی‌های Akamai:
یکی از دوستان این رو نوشته و خواست بدون انتشار اسمش منتشر کنم این رو:
متین اسکنر سم و پینگ خیلی کندن
از masscan استفاده کنن چند هزارتا در ثانیه اسکن میکنه، من راحت تو ۵ ۶ دقه ۹۰ تا آیپی پیدا کردم
دراپ ریتش ولی رو نرخای بالا زیاد میشه.
کپی از چتای خودم:
چجوری اسکن کنیم؟‌ اگر masscan داشته باشید خیلی کار راحته صرفا این دستور رو بزنید:
sudo masscan
2.16.0.0/13
-p443 --rate=500 -Ss -Pn
جای اون رنج هر کدوم از رنجای زیر (رنجای آکامای هستن) رو میتونید استفاده کنید:
104.64.0.0/10
23.32.0.0/11
23.192.0.0/11
23.0.0.0/12
172.224.0.0/12
2.16.0.0/13
23.72.0.0/13
172.232.0.0/13
184.24.0.0/13
23.64.0.0/14
ریت هم می‌تونید زیاد کنید
https://github.com/robertdavidgraham/masscan
این خود پروژه
ویندوز هم داره
کل رنجای آکامای هم اتچ کردم با فلگ
-iL
میتونی بدی بهش
همشون رو هم ۵ ۶ ساعت بیشتر طول نمیکشن (خیلی زیادن)</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3061" target="_blank">📅 01:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3056">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-fastly-1.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3056" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چند کانفیگ سایفون‌هلپر متصل.
تمام اینها صرفا با تغییر ip یا sni در کانفیگهای
force-fastly, force-akamai
که در
https://t.me/projectXhttp/354790
قرار داده شده بدست آمده.</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3056" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برای اسکنر آیپی که خیلی‌هاتون پرسیده بودید دایرکت، ساده‌ترین راه اینه توی ترمینال(چه cmd ویندوز چه ترمینال termux) بنویسید
ping
20.20.20.20
(آیپی مورد نظر)
حالا اگر اسکنر هوشمند بخواید، میتونید از پروژه سم استفاده کنید که اصلش برای کلودفلره، اما میتونید کلا لیست آیپی بدید اسکن کنه:
https://github.com/SamNet-dev/cfray</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3055" target="_blank">📅 00:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یکی از بچه‌ها(abol) گفته بودش که:
از وقتی سرتیفیکیتو نصب کردم رو سیستم
دیگه نت سیستم به کل قطع شده
هر چی میگردم راهی برای حذف سرتیفیکیت پیدا نمیکنم
و این شکلی مشکلش رو حل کرد:
ریست شبکه در ویندوز گاهی همه فایل‌ها رو پاکسازی نمی‌کنه. این دستورات رو در حالت ادمین امتحان کن:
توی منوی استارت تایپ کن cmd و روش راست‌کلیک کن و Run as Administrator رو بزن.
این دستورات رو یکی‌یکی وارد کن و بعد از هر کدوم اینتر بزن:
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
در نهایت سیستم رو Restart کن.</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3054" target="_blank">📅 20:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3053" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3052" target="_blank">📅 20:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم. تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3051" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب گویا آی‌پی دیفالتی که پشت جیسون بودش رو زدن. مجددا موش و گربه بازی سر آیپی و sni تمیز.
Pypi رو زدن،
خود
python.org
بذارید باید اوکی بشه. همینطور از آیپی های این پست استفاده کنید:
https://t.me/MatinSenPaii/3040?single</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/MatinSenPaii/3050" target="_blank">📅 18:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم.
تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/MatinSenPaii/3049" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zhn-nSIIECSQxUafYZWtOxU19jaPi9RQODXek9kBXq1ALxTwdRI4Ar7O6PqTnlhYzTiALDmNhyQIzQRrRsDGPoTnHhLSr5FwhS02Qd6AdTG1S8s_x1VKm-4oMQVqjSv_AuXqxPkVlPf9MK1nopdkXBGhaI0u3pXW9lqkZEcrFDlh4kzka1IwUVQ1JEr_JtlCmb9F32DgntWaSJgisX588sTc8owRj6HFyr8yfnlfeYvp6XtLQU3BCwTy4KufmQ1UKObg9Dn9H-9ssCpjbUvYUV1n2Fx1yanPcQ-ZyjgOZr-v7KpLrjyNZJv9bWp7XrxclUNHAYEJQWM4s7Ino5xa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
وقتی رو سایفون ویندوز upstream proxy ست میکنید دیگه اجازه انتخاب لوکیشن نمیده برای دور زدن این محدودیت ریجستری ادیتور رو باز کنید برید به این آدرس
Computer\\HKEY_CURRENT_USER\\Software\\Psiphon3
و EgressRegion رو ادیت کنید و Value data کد هر کشوری که میخواید بهش وصل بشید بذارید</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/MatinSenPaii/3048" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگر به ارور Upstream proxy میخورید، یعنی پورت رو دقیقا اونی که توی ویدئو گفتم ست نکردید. یا توی بخش مناسبی نزدید. باید مو به مو چیزایی که گفتم انجام بشه دوستان</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3047" target="_blank">📅 17:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3046">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">روی ویندوز از این آموزش استفاده کنید:
https://t.me/MatinSenPaii/3035
روی اندروید مستقیم وصل میشید با این اپ:
https://t.me/MatinSenPaii/3038</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/MatinSenPaii/3046" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3045" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsNccet5BP-F4fzEeB-LoG5RAAmOShAhjnu-kentWGzOwc72lGIKA9IxPm5XL5tR7u32zIeAF0oWb8SY2E-BWI22GuxG0J0AWIAVOn2F4MAIL99P2sEnBjBgI0iGZGCDUnhXKKJRNXReuvbPwapDh2b7OZHQaMqj1-DIFMbQFHO16vNBP0ghNcA6EUhifm6xGm20ZI-Fz51v_0QtEm7dADHgntJPkDoZJaYxkSwLYnYgXYQNFazfO0ruSFr1ARQKhagfXq-heLj3TUBbh6ZGUwGy96zcjWqFiLFboIrJIj9Jjup7cMLGkHdAB4JVS4fpAGhpobTiCtiFtkxwd82HNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3044" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3043" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hB_4GK3YMRzuShiIkucAe52Cmg_6uoeiuQwm7toEmgCv9x5b2T6DVhi53NCtAgFozNz747YPfHJ0kOiXhsGyrd4iP1X7pq5QHye6Lflphgc6R_UwWf6lA7_TNH76Ko4MI7AWQhoKDBtvUwqKDdm3LgRnQRPBdCYvPoCcxTKAZYfweERwkwiC9mi__VYHIm19rUcicQb6AkVpTWyF1P4zXt8M9y9v17LkRb0n_wEuL0LKS-aeMHJ6548hhCuWlVpDfWg66xwnh5OpIZY1t7iOGxITccSAvkzZjVEBQfJhFzYqezWyGbyb5mjSc2E7xRLRWbe84oZ0A01m9c7eC1ZWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3042" target="_blank">📅 15:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3041">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3041" target="_blank">📅 15:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PnDs0ZMmwtbr-lDk7rPryvRCPgsaxCbuLBD2W31NZVmEOTyspa-EqNe9cx_HOBTJrzPndnPauvNsANsfVCk0AH5vLMMNE7z4SJF_3a376jqHP0kBMm5AREZCW63RjnTivhsIB57fmCeQdp93Gs-slImSY3nnSi-Xk1eDuegELFj0OBbzPUDmLcvlHaJYDfRtkMjQbdlDZicNFdP9eM7yvmZZ5EYpzx1rOEvDK1bl2EdQbxsWuXSslrcNy8A31W9J3fyz6kFRutQIyTySinAOSFSIUTrIh35Kecj6Swocfja8xzyFu2D5nZ4alL9Zpv0WhVd2__25OEd2dcLtzDOyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MBF9fWZDd4owvCN96uosx69dPqT3YECbgVcqpVKYsjqA51qXdIFtjisWgA4S2LymxLja8IaTEFAHEULecUGrr-PLf7hLqR7I5u6LhQD-WB3E2fhptgRURUVy4_jYmHVBd1RjgVWeJr-J8ASywemnxFz38I65-9KabXc8VsYWNa5zDHTaYcMK1a19IF8hqK-CK2VjACZR0Vtp1RxrmczrCEQEDS2kpxdtG7M0-llXafT1jjjyGTP8Nrj79BGJxSsGKScuWDmMvZZAKdIh-bHa8ORGr_CSjBZ05uV9XizBtLeWPDVxIQ6QxnQYGH9NhCrcDosHhqBNG1Fopp41z5hBIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShirOKhorshid-2026.05.14.apk</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/MatinSenPaii/3039" target="_blank">📅 15:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/MatinSenPaii/3038" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حالا دیدین متد ترکیبی سایفون افسانه نبود و واقعا وصل میشد؟
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3037" target="_blank">📅 15:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان عزیز، خواهش میکنم به DNS بها بدید. معلوم نیست کی مجددا متدهای حال حاضر رو می‌بندن. از نرم‌افزار و آموزش‌های
@WhiteDNS
استفاده کنید و الان که اینترنتتون شاید اوکی تر باشه، نصب و ستاپ کنید</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3036" target="_blank">📅 15:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/MatinSenPaii/3035" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چه حالی میده رایگان وصل بودن
📚
از زمان SNI Spoof اینو تجربه نکردم خدایی</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3034" target="_blank">📅 11:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بی‌زحمت لینک سایت‌های داخلی برای آپلود(هرسایتی که میشناسید اوکیه) واسم بفرستید، تا زمانی که ویدئو حاضر شد واستون همزمان به همراه کلاینت شیر و خورشید و فایل جیسون و ... روی چندین جا آپلود کنم:
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3033" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3032" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قطع و وصلی داره ها، اما هر 5 دقیقه، 10 ثانیه قطعه مثلا
برای گیم شاید عالی نباشه، اما وبگردی، اینستاگرام، تلگرام، توییتر و هوش مصنوعی‌ها همه اوکین</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3031" target="_blank">📅 11:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUwjKc1we-R2uiQYY1gtqSlIZeaHz6Sr9NpkgXEp4dC4Hw_bKXapUP2KWzB0kUr9c157xVgUsNm1BPwAlj_UAlf4m44huG86d_too4q5qKQ5H9F7-PuJafuDaYOjROSOJ8JZmjmd7wui9Fngxjf9HEa7nnhsNHt02IwDg5F_mxWEJMR5PW6fdd66OSQr0QEiXHRGHro9VMKo3Xx8JIlVT4eAg52XjuTr6GwgdiW-1Au36wGPSFZcnndZRY8Uv0BekqhPz1zxDqbqiVWzJ-fc4v58SsnY2teFm8fMq0DjpgwazollCl7eb4hL-rh8lmjdW_Z81-_DIk7vKVGV4nlnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم روی گوشی(تمام باگ‌ها و مشکلاتی که توی گروه‌ها گفته شده بود رو در آوردم و دسته‌بندی کردم و خودم امتحان کردم)
این پست هم با همین متد داره فرستاده میشه
🕶️</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3030" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3029">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwE2xjTYO7hfIg9eAGnS11jxIdO7J5MnNXS3T7IUt04vLhurtHnMtjRbw5jGbpiYg_EL9Ep_jZi_fzeESj54pRGC_kokHX_kGnOtsjAH6HcMVCeS1EVe0jK3xhtTeHvBeoq2SIj1vTr8akjYtnmVqlyAx7I69OlehFQ5HytRQcFpdJacgMV4dhXb3nBsrQNVNfQVoiDAKjADSmh3Tip5QP4cz3OF3d17Cctp0_ODr0HgEZhDhtQf7QLqbtKpftrPp4LfKnnHuiPrjbdctPfZCTL-BgtKhbkVyU6ZVJxyz9ki98-RQ0Gbkyu_f3iYGOkZNvt3wMR4LZ7P-iUHlffZ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای یه روش کاملا رایگان، بدون نیاز به سرور، بدون نیاز به اکانت گوگل، بدون نیاز به شماره حساب خارجی و هیچی، سرعتش عالیه. آموزشش رو می‌ذارم واستون. خیلی ساده‌ست
با تشکر از
@patterniha</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3029" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان عزیز که با اپ میتونن وصل بشن اما چیزی براشون لود نمیشه.</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3028" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISkCQslKqOAwo2MmAdzcpxalR26l4DnfilErag4KUXt7x_H9qhAVnp22M6P9b9sIhbyV5F_L7b32QZzARgm54lpBsDyKeYdPlsDzmed2YDvlFVgEO_mNmd6sAHJm83oO4cYFE9mXu_QBDlNJYBKbecRspLxgCrW3y2rI7iOw_a2htiTXQB_XYlU_sDocGI0rvnerqCeUBMo8Pis-pl2RyKo1nUNdP4z1CgbKQskyTEDZ4XasUckjRTTq7t2eSivsCeHbeYFxLse5bl4iIS5H7ClXAAKqW7HmzJwGCJbGVQbH6A77jiklZCHev_0I4kyb1w8kv4JtMzbHZEEI9L7lPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3027" target="_blank">📅 06:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3022" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3021" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره.
اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم صرفا این محتوا رو دوست داشتن، نه اینکه شخصِ من رو دوست داشته باشن.»
و اینجاست که مغز ما رو به بی‌راهه میکشه.
متأسفانه عموماً از اون لحظه، شخص دیگه حرف‌هاش رو برای بیان نمیگه، بلکه برای حفظ اون حس میگه. و همونجاست که گم میشه و مسیر رو کلا گم میکنه.
به خاطر همین هم هستش خیلی از افرادی که این روزها وایرال میشن، بعدش چیزهایی میگن که ممکنه ازشون بدتون بیاد. توی فرهنگ عامیانه، می‌گن طرف جنبه‌ی شهرت نداشت؛ ولی واقعیت علمیش چیزی بود که خدمتتون گفتم.
اگر وایرال شدید، خواه ناخواه دوپامین کار خودشو میکنه و حس خوبی دریافت می‌کنید اما مدام حواستون به این نکته باشه(همونطور که منِ متین حواسم هست) که این صرفا یک عدده و من تغییری نکردم.
پیروز باشید
✍️
Amir Mokhtari
با کمی تغییر از سمت من</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3020" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2jSTr383eG1pxrOfS0bdGzRVutWKU1SQKdTI53YW0gIftC_8m6FH_e3LffFBM_xgHEuk6wcVV4u9hR23xB12rZ-oaIce8cNWXKlBj-sDjsEuPsNyQN3Q3eYkgxcDuYjExqnMHUUrpNGGEDNevEdQqqUYN8bWSAmMCcEwMK4tjdBTGn14U5LK187V7CFBGzUJH5vFJw7b_dMDgZuExrCyIUDTpQ9GyVMIOWHn_8D1hi8g2PdlgI3RcVHQK5BCCDT-LBfJ-DRXy07l2Yu4i0wVlKpVtkFekMR-C9PyoxRRsLy7xW85QRSiOY4-_83TpvPBCFMu6ROQnY9CIIFgnHjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IRCF | اینترنت آزاد برای همه (Twitter/X)
🍷
اپ متن‌باز و
#رایگان
TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
لینک پروژه:
⚡️
http://github.com/MaxiFan/TunnelX/releases/latest
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3019" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_zb9LFm_m9lK1aS4H4JjCnrrncllUahY3xjOa9Bwb0KTwnp7eBq0kwO03YeFstMm8ZpPQ_9SbAwIbEo6yMaQInq4S77dYYzj00P6WXNScAfcyzF_utXii9gJG-FBuh-yyUbHuRPG8I6n4DrHEzxHYl0JfRUDUZjat2PgPAaqGRivtnOgo8A9S9Wx17yUl7_NgtXxiMndd3EJSQzoZb429M-sgTTKaoNjKy8H3BbDhFv0hkTb0Qmet8kwCJN8JbVClf298xssAcpvpKe3mjQ47qeBnVEtgl659394Kl0NGI95elkR_xgwjQZNAjIrnL4TlPe59Q3twaQXSckLHH2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/3018" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3013" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qMaNk2TUj60Ojy2GOWwU8XsXMUID-IwGrf-DUdRlHt1v8FmFqTp8NiIg1g11bTGqfnVETT_zEX3sOebE_6LpZ6A7hBiV5q7tQJ09NJTLZV8FpZOw6TDRZ9ADXNobJ_T8rwmS9CCpfvKvkNqwxY7mo864nwp2QceukN-sumNu_nlndteXMdVkQXfYGkJctN3945zfPH4pwYmbjK796wwR_bbXkY4EVUXH4LjdyY6NWznQ08m8HsW9Wl_gWldSlxpMtVNvGnPPffJfD2F3C9BtkmbynX7bnRlOFBLQPSbytTdpDur0j5H89bnTWgpNGMCNo0tN7Y8dYIPL9g6T1zWydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cLfKpXg2DXACR5dEOLEhHadkV7YKdFt1dzaAQayC_UMIP4VVAcO9liQa0BMcSKZyKsrT63eQoIs7KgowNiOlY1Idmn1ZdDABRl0soM0TKRx0LbjxQKINewjjaTH01m7xkMy0M-SvbY0Aj-Uk2AvBcN9j9DbViZ65V65b0fD6PBcKu3jgBSDsVOf9tRpManYfDoKsvEetHZ7Vy798gM3b-BqhQ-DLcSjZXkEr5XpYvSIF7X6tF-IfEYB0Rkx3RU6qDUQULty3rz2wCo0uN5JhEHGtFKDZXgDARtOzWJAcXGdnp07-WtsoA6Fnuv122MJSNJVfpvWV5p3N7nsu44mRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی یه آموزش بر پایه‌ی DNS داریم. یک دونه رایگان بدون سرور، یکی با سرور.
به همراه آموزش پیدا کردن ریزالور
با تشکر از بچه‌های تیممون، WhiteDNS
(توی این عکس با سرور رایگان وصلم)</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3011" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من تازه دیدم که یک نفر امروز صبح 500 دلار دونیت کرده به wallet های روی پروفایل توییترم. و هر کس که بوده، واقعا ازش ممنونم
❤️
کمک بسیار بزرگی به ادامه‌ی فعالیت و همینطور دلگرمی هست برای من توی شرایطی که درآمد یوتوب قابل برداشت نیست و شرایط اقتصادی داغونه. اگر…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3010" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پول پارو کردنی در کار نیست. این پول‌هایی که دارن می‌گیرن بیشتر واسه جبران ضرر و damage control هست که بتونن یه مدت بیشتر قطع نگه دارن.</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3007" target="_blank">📅 09:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فیبر نوری مخابرات کلادفلر وایت لیست شده ظاهرا.. امیدوارم بازش کنن ناموسا بریم دنبال زندگیمون</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3006" target="_blank">📅 09:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfarzad</strong></div>
<div class="tg-text">متأسفانه همه راهها رو معنای واقعی کلمه بستن (غیر از mhr که اونم نصف و نیمه و داغونه) وشما به هر نحوی بخوای به نت بیرون دسترسی داشته باشی باید هزینه زیاد بکنی ، یا بری نت پرو گیگی ۴۰ هزار تومنی بخری یا وی پی ان گیگی ۱۵۰ تومنی مثلا یا بری سرور بگیری cdn بخری وdns بخری و .... بازم هزینه گیگی بالا میوفته ته همشونم پولش تو جیب خود دولت و سپاهه همه ی اینا</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3005" target="_blank">📅 09:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آقا من نمیدونم این چه وضعیتی هست که درست شده توی این کشور !
هر چی میاد میگن پاپلیک نشه ! شما متوجه هستین مردم بیشتر از 60 روزه با این قطعی نت مشکل توی زندگی ش پیش اومده ؟!</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3004" target="_blank">📅 08:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رفقا من متد‌های حال حاضر رو میدونم. بله میدونم که CDN آروان چطوریه داستانش
منتها برام معقول نیست آموزش دادنش. نه هزینه‌ای که باید واسه‌ی CDN داد منطقیه و نه پابلیک بودنش. اینم احساسی که بهش دارم مثل Shecan هستش. یه Back-Door توسط خود حکومت که خب دست خودشونه.
مثل گوگل نیست که بهشون فشار بیاد که باز نگهش دارن. اگر اشتباه میکنم من رو متقاعد کنید</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3003" target="_blank">📅 08:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromペコリーヌ</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CWby79bP0-dX5bHeb1-CYcxn8F4rwK0FghvFnFI894nlPYZftmbxZiUKyG4t89WqROWCLGlWtkSh371BnJOtZ9_kgAD4ZR4bsC_PI83sKk2irm2xU2NlZbZWc9MGTW4tKFMSIgOdBwYPtPI961TnS11ZZ48qc_9KRHXlV36GqVJNUsMmxLFRA6bxDmTtd8OoFESiJDlbm11hhKDhWu7f73vho1W56ik-m-EHp0wLjt-wc-6cskdNo4c05sQfcl7pXyVtlCFeNLCQalItdGf7Ld-qeBVELnlSbutV6LZDxeEandv2K4Ng5f8wT5jWmG2FA6BS8qGUidcw9zSWqujC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iCFKXz7VCFtqceS5xllEDVuJoU84zxgEA1FkxrQyfrdVZKHxGEyJJnJriDkVISnt7RsaRcfZ1Uzwxq2Xo3urwL6eneSFYaioyl40IolUarJ3K6XSmH0VPf20C5GdQQWco8lsoL8q2dPggqE4e6wIhsGxXLt3Ke6wBc-SHeQ5u_rh9aRg51B2iLlpv5GRf_nkO_oFMTccd1GzBS6V20WHtR8iUdDDMS4GuIEoZkUZ5Szws7G3ItLGyNveWc1aUffhX5kbtBWAtQuA0d6sH84HHncJslK6-LRS_l9O7jKRMfyh8FzZbjGtTlfvz6SE6koIKNxb4r08ZWi9neBNpb9eJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واسه ۸ گیگ اکانت رو بستن ؟!</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3001" target="_blank">📅 20:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینا رو سرور ایرانی شکن فعال کردن روش vpn زدن و کانفیک میفروشن، طرف در عرض چند روز یک ترا ترافیک رد کرده مشخصه مشکوک و پیگیر میشن</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3000" target="_blank">📅 20:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نقره ای دارم یه ماهه استفاده میکنم راضیم چرت و پرت هست این</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/2999" target="_blank">📅 19:28 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl4n55JUZHA5yZyMgYoEZyzS0tgbrQYIu1J65rk289snxW80_3TxPHJxLVKd3ETPncC4Zl1qADGTDY4nPsFk81dNI3XMaocDA3LPyMO7kAUkFDA4i08YYxgntnObb3XJeHRikk3U3A-FdOwwOnnEXlB3JiKD_hw9cN2Q27JASSKDnyEPrOqf-PhrY-SN0T6yO86nrq7LCODXNC8chjQJ4wLNbT7JOpPugpY-dZk60D18oqOu1b_mVUKDCDD9ZcDPT-_CHJENHoOlIzdIJcTE_zTJIwycJ9xvOYEbFbm2K7a6I7_QK5K2-jQ1RLQ1k34npEQiDn7h6RmjrlQPBvll8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول به "شکن" و امثالهم هم ندید. یادآوری کنم که چند هفته پیش، به مدت دو سه روز chatgpt روش باز شد و ملت کلی اشتراک خریدن و روش کانفیگ ساختن و باز مسدود شد. پول مردم هم رفت سطل آشغال</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/2998" target="_blank">📅 19:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من این تایم 70 روزه رو خودم 5-6 روزشو قطعِ قطع بودم. اما با اینکه توسط چندنفر بهم آشنا و پارتی از زیرساخت معرفی شد(از فعالیت من هم خبر نداشتن و سر آشنایی بود صرفا) باز قبول نکردم همچین چیزی رو و توی تاریکی و قطعیِ کامل در حالی که لپ تاپم بیست-سی ساعت بود داشت dns اسکن میکرد به دی‌ماه فکر می‌کردم. اگر چند روزی دیدید که من نیستم، بدونید قطع بودن رو ترجیح دادم و یا Dns رو هم بستن عزیزان. کسب و کارها یا نابود شدن یا رو به نابودی هست. هر روز کلی پیام دریافت میکنم که من تدوینگر/هانتر/دیزاینر/فری‌لنسر/برنامه‌نویس/... بودم خرج زن و بچه میدم و تمام درآمدم از اینترنت بوده و لطفا یه متد معرفی کن بتونم وصل بشم و من باید با شرمندگی این جواب دردناک رو بدم که هیچ راه معمولی‌ای وجود نداره برای وصل شدن با سرعت قبل.
اما چه کاری میشه کرد! جز نگه داشتن امید و صبر.</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/2997" target="_blank">📅 21:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوخی با همچین موضوعاتی چیز درستی نیست</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/MatinSenPaii/2996" target="_blank">📅 21:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آهنگ (هفتاد روز که من از تو خبر ندارم) ایرانی</div>
  <div class="tg-doc-extra">•(Ali....Amin)•</div>
</div>
<a href="https://t.me/MatinSenPaii/2995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مردم ایران خطاب به اینترنت
01:00
🫩🫩🫩</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/2995" target="_blank">📅 20:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آمریکا هم عجیبه
ما داریم زجر میکشیم از نت اونا هم اسنادشون رو منتشر کردن راجب یوفو و بشقاب پرنده
https://www.war.gov/UFO/</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/2994" target="_blank">📅 20:02 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

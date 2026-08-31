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
<img src="https://cdn1.telesco.pe/file/WRAMje7mM4Ba0yrwZ08wW-AsIzK466KAkiknNJvtPN_IyfvUNfpUqMI0OrITM3LT17VQu8vjzRsRpuWQrYcy36C07_I4nm83UsaHFzUTJZyb4vUKyu9ucVhQvwQ0hkhNuT8hUxm-Px2L8rTrTxgaPtRqTtHvcVTkpZMptbo0686ddR7A4a29y6t0cbZUAm5ubtV4fc0G4GHxYlPqcueSssorvtcx2pqzmGWWOuojsN6Yc7CvyIWdR-jHuTgBwhAl9t_rVzUW96JXfcMx6oSI0DrENBUCawC2DjP_d045oTnpMjq6jwKuOKU-6BjBmzKYSyvRt03gKcMIZ0O0rQhQKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Leh_LtKIPGHKbpufM1vKCwHf10uP7xSOxUsy4uFH1C2zya7IVlsht0rjfg1ovW0XDJ67-8fGnGGqnOeyRkdbNnyTtv3Xc-JuG0e-la59tez4_5nUCvGDhONGcxu1qbIXJXxIjmy80XZtypqfbCKAsE3dqiOBfWomhxSwTrus1fOTJ5QzZfaQxihAbgGN6C0uHlru3g7b-U1cDpgYLAfRCKFYVSz6sOxTFjEqOLZa7C0K8mFlHsO5v16h1kc1xgxAw12HNd2bNmcZtbU6DHE6uiYUnJmWRQ0DlVrCpIA3JYPJdwAKW3Oyy0J1fRQsr0Q9-PYxKcGH4kl2P44iasrxFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXPuZkkP3sXxKtyzajx9abwVGCJZJj_uBI4Ogh2i808Hjv-dIDJelNkXFg9BKRjhJ-ocCbbdnJYjajLqPOjhSFHXxFcZkyCKY3AKZ_NJUXmBu2uZ8EgADTVg8FNFqc2bzzZ0ZWSo8ojmOzivjFdF1q-zhb4y6VvZYOAyAVr4CplUN7vPvI_GdQx2nnvaf0QpbxyGdPev3hFXYAu_muIthMEI5mrHn-NGLzWA2RIGYbAgUHlpqPNJEYkk-JsPTohr9ei7ITrXz02NwMUVU06o61VU-32gKjdxqqzMQnBokR5hAfo_c_0rtACmJLhWBON0IWT3kvU_xN__jZUll6kj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sB8U_jY3f-vfyurl4NAXLzLqH4cZ05K8SzwGH1f7N7xv22BUoZddftGLqRhoMsCBEmlwrDz2ufFdc6HBP0DIAU1kV_GarShimOtMcQIwhfYOqkCNs3lXmQwoXMzaZuCFBfMYcUFbe3Q7xm-dwHjv7lfv3sIb78eDVDKKuj6CtCAx3qcRaZNQins7w1e9wIPOVXnI8O2lDfxYz3HUOAl36xjQ3XN5ztWqxarGyF7RGpljc2MY7GQQD927xB_-GCxUnENZ_AuWOY8HgAdWZmaZbvlWJ6SePxdU6-IqZc0B9Qn9RaejWhJ9S8p-8rW1_yr7aL0laAp4Nz1ujD4DFIEUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AlDmmGvtcYqFCamLpwGP_uAt7s6XyOw9Bh49vM8u6ixmVE0EGqKlPoU4DcAv8m4V5VqYtQxc0ahWnK3vx6p6JyCq99EQKQAlUGV-Bs_oK8Gr0HRWvTNvUYt6yO50CznVodHTe1Dv7N69i1eTf1BXaXhBTC6cXaXZLlNK_tN4iOCuaO8IBmYC35E9LJ1qjRCrFn0oDgDYCIIvn6YgYUVIw5NiEhfRitntrfEomluvm2wCnWJaCREzdX29vxKAvHJwcHn76lEl4WFSz3yHvxx3RjW7ctzCDkDpMCmlqW5eBmH7LT_PXO1Tl1yR5W6GZUc_3CRn9tKD1zrzT2Gd6JhUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQHsccmU1u4TqL-co-3YPpqaqMWgA8tBUUHg-FMyXyp3dghf7LzssktaJVlalE4biXAJNmVaF5JV7-SRq2J95A4OwP00q0nIusvYlUc84VXCU2G4YCoir8wULqLSMiJsPEDugNL-1OVuLxYtGkb8MYiKhpITj4zI_tUNwOHOl7k-V15RunBFzhK0axlZ5Y75yQgCjaFM5UIsAxPqKXD3kZMY4jHU4HfeG6aoqjbjSxUoYkyj5ti1vKerU_Sz_hGFu73d0i3bt5JOU-rGGldiN8Oj-44hyJ6FQEKm-g_upOZBeFBv5o7m08rpOBTOKGLufY4E-U2kPPUL_EjxEx6l5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qoOSQ5q132E-TaaU-bWCjvBSVLTV5ivnYCo6yt2qbGtpQBB_ZfMIytmCJUK1Z8OHIfco-BslQvfcHVJU28kqm-UID1ece_V7qEOIbyC8XrHRiuhhcvfhhdySKnpBn8UflCvPhTz2KVYX4ssZFL3O5S8AP0_ufdnqEbYAnpNbjXzgwt49K3TdJGMfSWHhnz5Z9A_KqpjooQ4khFwcNyACycjtSeGCzJjYlU4OU65nA5vrX-EyZ13kr0Pp47X7AU1s7I4K0EWpoyI8CWHTkqeqAfDWrfM26EOY9QPmCM_R7Han-0nxMXLjoo9B82rj9AJwXoSsrhF8XVHfFwKMU_jvrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKYsK7Doa-YdDX9k1q0yN3AitsIieYzXKPSYvWbIaWUGkmOk-puQIZU3o3uNcki78fc1KieDG5RvRS3ItVGfWy2onKh2DtyF5UzJkmLwb2Lc_Qhz7tUqqG3Yyl65mSxj9Y8Y1OGGHNNxR6HKVJFKl_yQ5vFfFoVilI-KWZc5_IpMLrSUgoWCnCtQwl8ewaxl_0IMy4mosoOrE78T7WCgZfjDMbzDFsShvcDkCeCLsGEACAqCKvNll0AvPsiHi4ePXlCPdigmoVVNflI4CWqrxPDSjXqodJkxZVCUhpkmnRIj0gsYi6LCUr7P0uY9Wxywvu4xzAf1i-TRMcdwCWtM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sNh83_aFiwqXGmrJ_fRX5uYg34VegOHfUk8vsXg8p8rmK63tLBNibSOkLaHH5nqVWms0jY9ym4ndoDy52MNh6oORLG-WZmIY0Kja4y5pXH_P9fwdyz9DPkQe34gx69_ME08d9e28RxsvEfsbVZaA8IE-C-t-a72seqcQRg2FgUl-1R4Aiq-AM19E721V65ULz2-Ck9-cES6nX0PrEWTQpvPGi3GMkWve_ZlgcL99wXzvVzNQffS040As3m2bhgkYpOajW9a2E8JhNd_rZQ8_-0CeqwvCR86ZEKYjRYK4-lC8S8tz6exzrDkwoop-hVZeMx28_fuZmuNuCgANk1Yllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jY9c-PxvQyQrCykxGvJ__Lwh6_o4kMFkKj4isJlb14gSqcaJ6toXgo92EwmYmrsrSFSLOh0rP6bQ_rGvM3uJ3mnxnhp4Kgk4jhhtLCIFpUGVPi_mkIwJTKQjCjL_MtWxsnxY_2_O1Dqjq50ZvP1CV0u7VL9jiZvzXrzJeZZE1hdsGy5nERJ_D_v7Un36ZLwLLjfePtq-E0ISlbm-rzFXDxPD5Oh8DPWBsImdgm4DkmcDiiVYqSM9gM3DHaqMItCv86YGwZJAfbi-7CPyix6a3r1CZGK4sfr99aRQVY2JrLhpcw5nk5HiPEHnmqVt0i5B6UNqe0YeP4SCEW5zmgSG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWCOoC1E7gdKgj78MdFg8X-dgqsTu3bVoZGEikhLZdZ0hl4L7CmDwJq2Uggqo7lGaiT1W6kWcQcvBx8T15QL8qbijLmt3z6W2VHXQxPsW0VCQAYCiSNXjrPvkUNy_vwxoWrl5kuS2t2tesY6bVZ7VSQWfCKhQc-j-AXgtjGbIAgslq_GUtXAtZJw3JqxWRdXgbPEDtspN8gaSvNCs81scfxpeVdtF1MAijfzx09eDrgaMwRdQooAFhBxXOhb3HBhUsk0YFwdiBVJ1Z-FcQTZioMY1KBVMLu5tu4YNcpF08oWCL8jrTYB4v6q3_GpZc4xM9unaRRIhW5fml5866izEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgAqu3GSnrrej7QMKgo7U3I1E07gVtq5QgLdRvx47URf50k0ol26D6Fs7NfIaLXFXWyVer-shbeTwU6RJyWziYDy0c0PdeC4Q7fdHds9b6zUFnxTOkpsKDPHx_QRWwxXZvepIujBen9pwbvmVjDgbMDBpd8MVMm6zMp9wuKYLsw4wzaLGvQZptxWg9nHr0BN-xoKVxcWXuFCIGx8_MdokJYiZFu8oI_g2X9KVGPOGLhyXxGtTCet7q3UkRJ6QQ1yu8ca2Kj4-lvfe5Ff7zuEkSfv3PKubcevivUp3cA78R22w9qPIprrZEEGYQZXPvsRfzvDWtWzZS3RlRXGXkzBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W_fUuN9jHbbjdtcS0lqtiJy9lt4CIT_QvMqTNVZje1vTm0RVs2xaedwbSU7jD6SdOrVy80XFsj2XI5tsevA07unGN3_YoZdBWVH8nvLxolxSjwlI32GFW_ISJFANNb8YLSE0IbrOnA8oO4rpFrn9j49c4RedsxVM2GfEkAdBxe4xDkn10hwT_iCQb3iCKliFb8u8Qgz_PYXboLaJc9MvW5aaWhTpl0h2NVDzxlaXlnBgpnwvJkifh2wfnjMXA_hlTucZlcZhxS3-eJayNqqaaTdskuhqYO51SpEOIrZPm2EExUsxyqLt-1HlRd5EQgC_AzrvnVy4bItJ08ut5exDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isXN2uBFYP0LzQQ4ZqoXILSejfJU97ZaOmc1m1-9NxHxNuq1KDDFKB-MTLnRW4KKC4GQNT75L1Bc_7g75rFceFZenvjhlfeNI8XK9PMdHOucvPauR1zVvqcg6ruyKgM75uAW5gLwVUnCq3Ce3eMPXWUute9F6W71snLuwmnNCHTsrsvGN5g7_w06z2ZDK-vyUbL5goP_upzgJlQPO9neq6frHk1HIHIfVSg0KQwIP7Vop_xXOEkLlteSm94ioaeBWRazl5QbEg0LNdLlho37aIYPdG_7Brzmtj0S-ewhBzZvyLdUW6YYHABWIO1YYcvFQIx91nBpu3UkW5-Uj_4GXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ttlItqqph74Dqsx7M1MMFzrMA30zoeGFLP5Zj2XQyaYz_41-hm0pG_MKbOW8kN9_dZDmffjNDGRVRlATzxcicjigclfj5P6hmduWyUrRfQwNSMglEGNSXRA1fXo64lqNkeY5UBU3Omsv3aE_OWdTvpS6YIcIsNW_z921fXH39SRw2w3vbOfK6CHRMmhjCnaM7NYhzMaGB7Yqf1_DJnc1VJa2uGgzejrpHVVzRLfQ6I_BdW1W8ojkYwcSyVH9BpD6CAV8MGy7jYao1R7FY2l9QaJsOxEXShuskjGsC2B2RcdLq8aGxcQeVeFf5mGJzZ9p1_evZ1fePL-25qwy0zL2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1uShLd-f9mWZRfHcTdc6VAdsPVuZ0SQeUQ6HCimiZfVhFOKUxNao-shhCM1Oq16pt6r70GChFy5UcwZBkDYEVwlyUzmLggTLl8WLJyJKEG3HwAluo3unUELMZCzBqqRrBTN2_oBmqgKu52j1VDmAJ5X0f8WZ81STj5-p3fBGcy8IwZjQmlip_g_Du0B0uJ9qd-4jVZupfSSeI_zOmMmJ3wTwDY_ccQRg7fs9o1UN3zn4c9Kb82XuOogWf3qg-FnmaNiI03wUI39WGAt8VynYXvhkocsZ1PduGdw8A14AM6DJIYBWExubv7Yb8OLCJPBWZsljgNkDjL5w2gXBo7DRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeAMuYZzrTXgRnRBIvBS2GfVJQE14d5YInRLG-3RM5Q7Sd40x_xpUPOrSDZE2rn1Co8wCzrodnoRYHiaNAWBcKEGGGjDOTmopomFqdLIUILuOIWwaPD8Gd8qScsZVxhsj-2IaSmBPXixk4RPC8ueEKw-QtpvShrJzO4m_5XdE4ZPa6SotE0tHYy0q7g2V45n9F8gAizZ_sbckcV2SbVSvEvlMrzll3DWv3oICpfN-aYLE2Zx2JkiT18rxN9Jm7VDJnGcEVNCR5-Pp4uv27eRVUQyd0ACc8eVdT6mPPGGmhiiRQRHlOwTKT3zWDSzmM3NOT__ubLOLanFNW2MEf8prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9-WVPdC70jVEmNkNp7nRvo4EYMppYhEG3DENK623q76Q83OWUrB0AGKW9XkEtpUAaephalAkCXsCQmvDldjGjCiYEOwc4oIEFF8F-7MW_x7Pe1CS1f-ZkIDSR3euqQGazMRvLf1YZlR3hWPjdZZPgz2a3Wwei88dkFUfw8JDn7o_Upf1l3EJFTsnJeMYAuafff9k1TIGcm1CNJd7pkFqvxhcNAusM8eA8rDyRiUQp9O2or8uXYXQN_AkRK1EQmjm6EIVZxjNPZ9ZF14SR6NFjnwQgxS9LTMT0C6PH3CFKuGdRb60YihyKXzYHFWSDkOsOQKn7aAMIDNc20ICSAgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYJKqvST-WbCUkqWy2GWdTB_-xV--UaXmpK_nxkh5MAQ3evj3cHwwln4buLwLJn_pU9CYSSlX9UeJvR1buDJYkYOReSkahGNabHsFyjeHJiFL0cTGx85q7m9mqsRw96ofD3S8iJI3mHdtSxZkpxEz5AWz-JlQBfGspGMLBV8f-EqrckATYAgsOSqgYHghI5pvcRy9oR9q07DGHQzl4NPGsJDjm7VaROi2tg-f04blRMOQz2-6nb_NPBFRjbgPC8oi178NxDB-Ze4VATNDt5A5obrzL9g5hdRE6XdE-eYMRYceHfc4qFbkGw7d8ohDvKemHc_immT9gOQje432mX2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Ed8nXrHmPktNNDPSM_S-cYRxk3bQ7R31zieLDtKeCBy-VK0tdkznpn40nLgww6DQsix5h-rgigMOSyO3IxyaFZaON9OEs6_1hSQwz_JoiUAJ9ZlDIj9R4ee8mZxQpjhVqyPOoGZunUsGOmYagkeJNZJlBKfjmOvGVukk1RHuWvCrsbof5sRN3kBGF-2-IZJeuJc-Xy79ruC4eCghkZeQ4jmA-OTS9sbLWp1zMY1bNW8baAX8tCCTz-qiekAhueiDcRHQxjaUD-asnJUjOEKbucVHYiHL7Mnbdct5WEgF4g6Ja02wxHfvQ0ozEgM9EjvNW-1Isadc0Vxbz0lijZvKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Ed8nXrHmPktNNDPSM_S-cYRxk3bQ7R31zieLDtKeCBy-VK0tdkznpn40nLgww6DQsix5h-rgigMOSyO3IxyaFZaON9OEs6_1hSQwz_JoiUAJ9ZlDIj9R4ee8mZxQpjhVqyPOoGZunUsGOmYagkeJNZJlBKfjmOvGVukk1RHuWvCrsbof5sRN3kBGF-2-IZJeuJc-Xy79ruC4eCghkZeQ4jmA-OTS9sbLWp1zMY1bNW8baAX8tCCTz-qiekAhueiDcRHQxjaUD-asnJUjOEKbucVHYiHL7Mnbdct5WEgF4g6Ja02wxHfvQ0ozEgM9EjvNW-1Isadc0Vxbz0lijZvKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/X7FLVAtUsdcN2kwvOAVhFG094pIly2YycIlYTeKTQIlY71GymnAtDDOzmlQ0U0clOh3E5EykaM8TWHiFJHcxdUjoT9A5OtXh1BGmrscxIpx7GARyfJcOIkxix59-Xc7WguJCPFAeesqBl-lb8gmSyt5hSXKKPRWvm8kweu5XatkOJiA7Dk5iu4KvKu231-JPJRgmLXy8p9h-KNpWt06jjMZOXWVnHt1bi4Wp1cgXbCxZffsPPppxDLOAyDuCJ44ugVjarj16FSOBZ8anXOHUefCCigAu2mWPWN3U07WP6iNWaqEUJtWADVJNJZcusu_UtrADj6NfERDg-zDEFwoguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/svW5hmKziv7HCCpWx34WCah9Lp9QkDYchJ6nsjd4ObL9BBuNmr9-M54auepuro3i3filWC3OY9utzkPSvbno869vLdpqn-JYjUp7n4Kb6Koe9_4-vXAVyhK17JoPfEPpS8r9uFSIidWkEDTeYXbIVFmtuTeeoKxIzYuR1g1J-VgAnYF6bUYp-N02fw-IgKiDDTRS58-Q3r5TMCu8FaraV1z0QpR53YWpGMpzNWq_XyzcRsLFYZR8DBFcFeCzo6j5rMK92wYpX6zPcj5bzdhtmt80xz6Zuz241Tr2diOS1hw3Kl6AjY-625TUpB5Rj4sC2fM9N9m8Z038K11yzVHg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/LR-5G32FL6b4yYoimYShkkgtgXW_edONvGXSAqLI_CQm55XRbQ1j03W4YObre0b5zqho8ufnYqF0ByciPxNhlJTRZfX1ytXnvPisOEZrPVylOrmhaheySxlhtRrZ_ZP8KW9J-0w3QfVSWO0FpqPChsI_kp0PsFTQJPb_LIRBlziE8kbkjJ-CzQWjclwn2tHV7dvjBbRRfpceD3_591XRv-ahCKw2LOl1tRkoyaGtNjjSLg5UWqkPGnsXLTbspP2w8eg3W060RUwVTodd48shjROHWlQV3vUj_Jo_xT8UdNj2ynsbi5VyiH2m12l69Q4h2BQZvbs4AtyF-TmG8AHrwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LP8jHJs7s0DESYgHnW6ZXeLC_PcbuyXnN5T6pJromU-6lKuZYhm7Q6PQnFomciJmR7gM9vISO-yFcC1E8_uajg5jb06378fSJHYAPG51FCYDQRzeYPJ9P8_ovMR3p8Juc-6Hb5vYPWjvSqVJrmJZDr_EPHxFDFYVCe-V8RCg6ykO6Guy-ZHo52iZdrZZA4LwTBpecww3P9McyRZ6Y8EJpJUkWAlJQPPfVpfg4UpTwW5tnWTxdhDmjq3dH2yQoI96WasYhCeKGyY_LklN9-0AtSUKxHBCu0HE9euMNCjvW9dsS0AUcCQN__cza5mzIFZWhQxd8Im0u4POR6tzowpwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nw1NREGhu25THzmh8_hKTG1UWet9Z-mcNCXT3UXpXJStCi8vhwU1_wUXwZ5dGA23qYzHYFSN8XbGs0PmGujU5UjH8NcT7uT7GOZjtaMl2DVJx9LvHdBlOXFEPS-b6Xr48-SAI9EWfhryT5lGeF8WONbDLfQ5Jc_aWKDSanIdiLfojVTrA-r8QwGDm8GI0X21ZL_CP71h9JnAEOlfs39Ay0cwncZYddR-9_sKVjboVRTroHiFPwU0UzfOFJg3Y9NfLWzmIg2pjU8OJ715f7tbcj0si_0-fhLeV-VCekn-J7BDMrvvu5YDeeuysgNhLcnsTZSkh7zVRJ-eHwhm6ahwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hIehlkwguqHLeAo3YcP3xoa0GEmMhn09MLhcilJrtw-Mltv8LrFpkGLimzN7toLBRazeARIAodw4Wh0YCOJ4cY287oYT0u3WNkbMPyNSCs0f4VYtTHy0zelHS6G6jQfGDXBhvkJWeKd4gKbI2oVtTZLYuBsielixLD2oUthhZQflUTDIbJh4fOTj50-ZjQCYJz3yN1s7B8ddm5dLyd_tyXW-PZVixDcT-lRqKAvX0u-xuSWBWZsdDUtobYl7txrJTKR--es5DAKKZ3nWra-SdB1MvmQfDWeedPBWfd_NUDuZoIP6kFgbNDgxwDa-0b6ejfmxvc7To6d_lpqHqGd4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFEydTFQV_nHxalbVnIlZ8xw-rym4ydbpwI3WnkCkxBELgaLC3YfSdKZOc7jaU2DgLDWl-2Y6ktdPVRLFQKqu7D_XDjGy7gsbbX6RDiRE0To3jxLu8Z4R_1wl1x5IazvOiMx1Nm3Ng9t2loexWgpLVCpS2EeE2r1OqOeTi7W5OdaVJ_39LPXZhm_wl7b5-CVoF3TjBxG6U3-7IbmRP48ttFFrTPkv4BNjzDCkkRO3aoKf95IS8GMuJoO0EJx_Ii0V1qwK8f6Wvs0xr9nwRfrIVBGE8mEbBAjCbJ63yEecwQRy1U1c_g6OwXlcmIdmBqIbkp-RJlJXtiFMn0oeB3PBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KCHi0efjKzc-VNUfRPuxmXrrs_iaGJ14uP14AWoErY5f08y2fvc_lVN3cmU2-xmOBJXHKQWtv_r4CJNqeJDaD_B72r2SE5RR2JqU0VtmLjaIzCuZOGIxh11I5Jk0bBCY9r6VPr8a_22MFv0JRzfcCxbTX85Hx1a4DZQQc_S8gSYlHCYiU_sPvW9kFZuDqVGnOEAsCgKnGQo6IUHeglWd8JqAtTAk6HR9aLriWOquo3EVlXGSnEw0vtBzChRljQoDlN1ZfhSO7stavDskrcL7tZWVZewx1zCFz__fgcQQ_FWA0zPm9JSw3uDeLbgdvaiDMzlTiXr9S-HzL6fUUTUo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZTmA1XOQ8CgMpM6snPhcqmQIu0yHl5Gal2ngL9854Kcr8zLReFRSQW95tMwt8xd2PeYs5oqdsc3Hn-WXpE2mL4AmAw6WPWJdyK9PAHlmx8g2Hm0n-w8v7R4EOGV_2mhiz48ICzaepdCS0ZwyNGbjwecUnLng0FL-23qu5YQVuKQKF3jV9p1RkCHtLKQJZ_sJ3dIJyvmsSCtyLC0vsdhApejicm8OGFSpSPsSJepg9ex4VLcucyz9ELgFJj9PYNwhZqF8d7z5MYYtiL_M6ViMWQaimc8mEg2P-l156C0BQH5oy1h1d-GYV8M2F7HG5mkHvoPRx9yTLfNijo_3UQUMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=IrGMUl657l3LsjS9UPWLe8rKsfnz6b9Hmq6O3LCX3RovucIAgehV6yYN4wIUYP2mjmYAOvsL6s1BFu4LD7NjJohuxNJ18lhyPamhQQriLvcfejHOX7k4JmVbY4KinJVLhMHcwVVTsW4c3k7zuPfOLJtpPcNnT2tVfpU8WmLhY18QNbqcKUeDrGlF-BofzXG8NVX_Xf3EBvKVwqI8cZkaw3Wr6_pNL1H2DyzyJjnCWExqJbL1yr8dFYqtt-6pKyA84IkjLPm1EghE5h04MmbE2Jb9RiP5EQ7iZegdOYm-Uu44Z9jyGDlfJG_ZcH9CWAT1s9GpmV8pp3dkojVlo1i2og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=IrGMUl657l3LsjS9UPWLe8rKsfnz6b9Hmq6O3LCX3RovucIAgehV6yYN4wIUYP2mjmYAOvsL6s1BFu4LD7NjJohuxNJ18lhyPamhQQriLvcfejHOX7k4JmVbY4KinJVLhMHcwVVTsW4c3k7zuPfOLJtpPcNnT2tVfpU8WmLhY18QNbqcKUeDrGlF-BofzXG8NVX_Xf3EBvKVwqI8cZkaw3Wr6_pNL1H2DyzyJjnCWExqJbL1yr8dFYqtt-6pKyA84IkjLPm1EghE5h04MmbE2Jb9RiP5EQ7iZegdOYm-Uu44Z9jyGDlfJG_ZcH9CWAT1s9GpmV8pp3dkojVlo1i2og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnIbKMBeAJV0pWgnuSwDzbX70-KhV7c5fscfwRqPoTvvOgcOUlZIKH4s_z92SLBeMUmFmW3auvLuH5xjYmrppbHbNCJCmOWeM386i2hXJEQ5p0T6oXt7PnpVVITFkCOfIUIuj7EuCJwmRlP3vLRfYJbLpau4boUMFNwJouDJ1GzGBn817VhqEWWLb3f0TfT_rtincRfpsRdaO2ZDlLaSUevq6GPdzLfmSXIT7VL37pIc9Lw43eI0LJFIqtdovWq402rwBAbFPHalnny8UmIcESy54zHKyUOl8hqyiJBEcVAMAHGLTXTdFLCJwypv482jhMtlGEc6VS8p6ItkjjZoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kORQWKurMC4H55mymFjvGJR52jKzdoSmLbvpRTyfxzlVcEmmEhzB7y24-HdAfX1pbHubQrwR56IDiDLxZ6hesVwfaEZf83iguJaqLm1znsy-GVgvdQweXtAi_-ukDn9DJoNQQ5jqZW7tWJGHfIh8DcuEeFWHmkTphQ6WaM8OXZDHhZuoTd4KvXmDwkUWEUK-JNrTN_vCAEcqrEFVvUQI-KgutFUeRPOkjD3nf0eNYYM9qDGTY8NoR-Lr2BviD1ZssFyyR1cl-_KcwgjjGS0fcxIjPjqUH7wdW543N92pj8uHc9fVVj_AdLMCDe3zBtCXhsDoqW0ppzSnNbI3iGF_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFSKR22SVBMfv2O4YeFI6Rb4cgWQvzN6fSqSUuj2sOFXD4z7OYW1tCeSXPhLsfJHtakfDdv112S_5S67oHNUQ5ksRyBpwhvOgl5zfdbv7YVR_-DCpauUyJqTYA7o0VV614Z3ZextPUTrTq76qXmWUMOqfhjlZf230s7GbRz-ruIGsYqrQaXpBGX38U3unvAKyw2yJAZiTyOvquAb5hyjFprTCZm7Uqi_mUilLbqs_KmRuPkLcB0H5m6eRH_AZEq0uRdfx_EA8E63HBgrTyEL-gL5d9qaLGHfE_Mp5HgigKIMGuvAWiuuA4ei2COr1STTL3-r4SgHeBP5f1ZVfj3clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYMdP0gBH19I_P3QsW9h-ZPs6XbgSLUQz2eOC_DZFiROX9Z7SzW5-Lia5cBoHGEFzz2l0it2zpK6jDeoMDFv5EtCeymSRi71BFaULWE1BBffxUUlaa_flqFua0RvIMZKlnwRrzP13yAkUTUZfdVhvuv7vAltBrb9xevwvrUjtc2eE2B9811HUu7S2lqOlByIaQkrjJU-H9XEgL3vPwT6HrACZGk9Md1Z8f-PTJcuqSnk3kp2gBN5FWI8GP9b9cipSujdeeQoNLQN1LatbmsgTXXfuMkRYaBL7cESHHZGOiRwLPQORI5SqQOkpAo_VtBgMw1qQQi-QfK8WwjV6aH_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mx_ggQ2Gq9uoy-bGRe74C0UGte2KDQ6yZ_RR8fScBSpDbFltOWIneDO11VuFieLBL0LgsSFDvZ4pJs3UJUNl0eytsDEl48aSR8JE5PuSHcpicorKvqqvJbj3ItynyLdd33aGBIkSV5iozujpMdCt23ztiE6XHe74sNjB3vlTnQTZOYqHMGhFU9PwPC_ygzo9NCn91y85ph-SZtnFMw6-6Ut9FomBsiPInZXHdeRsL-S5fgjI4lybGr_f3RoGctIu_25zkfpPWHDf12Pb2QfwKqkOM5HX6xB_SE_YMYAuJnmFp2v-dyOAj7v31ut5vMF1f28zK3KxNuoZtg5Fe9S-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGrRlSRZEI9MEwaakZHI-F33-2q3oJoTM-wqlocEtovhOU8nGCHV1JL5CUSGaapNsZMtaQhMVo0iHmptpjYRNyXreURmb9rrQLnlAMAqxxx_fwCeqBmr3kecRAzby6ILVgLNkcr3vUVVmr_iJwrYELbDaTNWda_XHybM1JR-E5_PyLoO1inoE-7bcmVbbmulCuZyq2aXo9EygdQWGXA9optqS3gXNqHHbAOpdzcXicUQv2v1MkJdTACEBzL1JhoENO9vfrXzB0MV6ljxjJBiNAaAXLqhlbw9b8QkCuHwQSMgtQMUEw4aTcilVkaYoml0BQbtvWgfHrht-xdsPgGolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vBID1qwt4IIDZhHkICvrYTmDymjk3f5XkBOG1sWnzi9GUmt4GPNbQlNJvIPrLoZB5WMDFSD5dj3WWqNkp2Bdm9JeilKG4JBhIrUR3xYI9kNig0m5DneI4CsUKQvXbqwB6aAy25-1rHB7hP4q5Xry3rnOQhqel7MWXBmJyXgRQHqMCjetYkHbmY65c02mGbMPzOef9EmdMwFPKVLD2JX1spRkfInxHBPfXtB7FxDlHuYB6d6vQOWvzah7ELFNeAU7p44bUc5yIWriN3Gv-YNpLXGFK8RSXjDnJLd_YS-gtj_Hz9_UflBWam2rXVMphY7TF1iPu3NXKnwxjGwX3I05QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pxTukahMiP6HzdZHf_kppK_vP2xGxrfvam3Wghk0VFa34KPtW7dqRDAf4QLNqT932T4Hi5ESfvoGeqo8uiAMD1iyKITkVgw97nsKTI9aGOP2LR6ZUaNLbqKgI6Z_9qNVz1acJaLgP-7XK5wtjqo9fbZiZRPbvmdCPq7EGWtQd84x5YtOpk2uwMAiIQR5tiPcGX65l8aCEDunJdHS7y0Xfb3CSGbUAnQxDQ5_HRhU-P5vl3BP0NwERCBSH764GFJQmsGEZmzM1bHGXkP-lFJJc-4Wi18381503Un3S9Pexlix6C6_9Rgr_2jEoNxIFppUSozggVcODN-QXTaVQQkgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jmp60PgT7FVup8644zyitP5PYeC5Ymf-W8_CCSNv3YUTJNziHGHSeHQWJmdR_1Pe4mO8XMOkPtmuTHCuEykJgTS8PiNQU9OVqp6O3Q0MO0gUkq_TqnoDWGQnIgbxROLoxBzG6gL4CxU55aQgerENKQf4mdQg5qvCEKb2Hvi58LfW0zgWmzHVRVjyuBEu5RJB3UCPm62_Or4n3NapSuhpxvhmA7vFZaXYdaCASkQozMrKzZfM38EiKdEmfTtxKostf2334raSXhqqSgdpvXEOf9PiYIHqNTjB2eFfBQz-6mRmwEZK8OqFVjmp8FvlrMrPqmob8ItNX0IMUPiCbXoXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YKpqVJvFQILHs-rgmjXZ8OT7VYrIILDk6WY2BP7m7rMaluK8frSNr3JNpsAx45GWoo3GJYs-WnM7YsWe6MzxCaoZLlMmDFrtMcF497zdJXhBgZVZUIaeSrneJ9SLdV7oK1_iUJEcYMukv2nQGtm90LFGUer2xfvD83iwO3lLt7KOkzfWNHUbwARPi-BQQl4WQl8VCVd3l2rIYavKzqpGVrv3GSNS9jXeHR7aF14tpxJ4z78gvyTMj8DMJBG-l31DugfnJnU8kdwqZ4U_9pQd3-xi9eq-tNQhqr8iYNMo7ZmV0sqrP2dzCMkAiYl9TX8JxvMn8A--AOQbLluGz4LyQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nmuyr0IAbRfM3lzAyeOwMq0p8SUnEXaD6G5Gr0Ftb27Ju7RBPAcp04uhQzrbKLUkW3oM24d4uUOLCRqFBDm8PSAcsYLAqhVD4KnNq0Ns9wCAHKhsCSqmoOqpn2c_99w_0432ciXx6_qRqLumk3ucitwOXHYa625hpz_zdm7RZrWdKRofbxsiSj6PZ7W2hprFsaAYzWuN0yF4mJdCKBLgOtyKGgHgNG9DiV3oXdEmblJQTHLQXQgT2uGm-F9AqnBr_upRB_CW1_cZzv3qWqZrdICrHN7wqedpjVdYknX8Ek935PqNQblgLI_25_ZKPJknHbcssJvN7c68fdV_2yQzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/De_X2KioeqMNvDEnNkL1nMDtxh-Z2Ect2hVaJ6NKG0YywLNHxDT5NWfLmB0r0gYIgI6No3AjRKeU9kWu1YQHzluBvsWv3ajskvmDebtmTHE34fAoHIDgBi8HdL3et3oLpSm1h2qvue-KiR4v1YwW65uWlKLvGXydqfsIp4FBUx1s-mrW2WhgU3qMs-Zwe32OU4dYniQgtwMGB0GJwhmp4XX1PBKg9iNXlzl0kiE4zFEekj4q_aGfUgWmdyLHZbjkWZtQc83xDi_XUl2pmeHhca4BY9IqCIY422EXzi8VdhI27UzqhepGwSwFneCplj_fXccxlcB8uGAUnA3THEBFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lAIOHTFF7Wm-kESph97I5jQBSGYsKU88LCOVEk4QLQdaRGSZRGJLTtILL5H5GqZ-Xps9ku-iX3vnUlA4re_AOzqRz0RDWCbo_2NXXzcipkJd0iJRZkdsD9KyU52CyML99j5QxfUq4-BKfgcdn0AiXIb6H3joHGm1P4o9da1IIFykQsRgLzL2Zc78hUXB2wXTWiaVufVpa4t5Y4c3VPT8CP8eiUMdk9orxaJWuoCbP8CBLQrANLHXLCsRDxl2kETpNJZIy_85zD6bbVOv6dtaW12Jz9ngbE7agmGqfL9EvXys6ONRw4iZvi9eacD4g4exBrl2FMGApgYAwtBDz6A3Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/myUQZdD0HkUa55IvtPtklvkp3tr20xtwLH0Owz90RmdqaI3uK8Tdg0m350b20EMxWGNcBaiRlmOQyVbQTpMp1fhaHVmxbv1TnB9YIy2DfOdLMKExAenCwxBaHYuquVwGtDzELsnUi9G78smJ7w9vThzkkyhjA-4MI9yoiF5T1iRr43-UBmCnQ6O3Mc9B5dha4Wpa_mtOUIz7IWaGsvR9ZGH_DGsJtKMxkk-5LtmIK7V3SBxAnZjPJo-ieJaqf8PYwZZaQIC1A6UIilwscy7tB7AvJYzO5Ic9etxnjJ1C4A878UhIAb4PuO_xUeOlCelruuZIp-GcsJuCClwT8Mze8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLQVz8cL0eCvH7tfSZESQdr6tqMKSoeYyh6EO_c2ghtBv_w4Yl9KGgpsTEfXxu3PeUKwyYsIVNhyl1N-eHi91gGeskPYQCWnBO5j4Bc4c-V1m0N7ubX4NonjxyPTL7WvnF9MCi27i7f8FT78K3xvFw0h5-paWdEVpgm3d_SPKf4niyZVHF-UNF_4oFxyIvqIK_TvnU6HkGwDGkzm3g2Gk8y6CATDyWOqavI5FBNSL5u0uXWojKDMwlFcE5b9B60YujeEiTUgCZYKq_NbSaLCANvua1SwZ0Q-l2_6PosDomkpmCNsANMuu17T39Z_yR2gnDM0E19zJw63QbYdfKwO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKBKya4sWU1iR1ev6Q6ZZlwGdqvyFMivtCoshLyO8Ags-bYOdZJ280X-3Ia-gRat5z7dxYAM3a0KMt0hEUYA7fPXkYugggeoa_ebKyH2fk3T9YotdxPnnE5astdv__RAl_-KDnybnHloIIkOw9E_d12KWD_gJcf5yxeZE2gCR0hj1tdIN2ALbfgJfv2Zg7SYdTsXdV6azf2fY73lfwUPoSr-Oo5p0r0I8l6lzivbObdCa-a8OvWtIXhvjrPENeWV_Y8XMUvnr4eU7r2mxMQvFP9DkyunPlFAHb9vDL01nAV697_dP7nb6AIkrZGpvAQK90vhOiEs-YUPnp6BUGWiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=nqYThpo8WRne03Nj3pKWo43fo6lEbJffFo3V8uMnlX4ZC1nxI8kiFTJnE8DG4PClnq4w6iBoGMCTGLQQP4ThHXmGUfnMOLm9nQhrgp_vRVwF_kS5t8rsOrrq4SVe9b2xcsqGTg6nq00MUg_s5EYYwsfNstkG3Dzaxn-vb58WzDuHe8fjAjGwrtKvjUdZ6k0kWqPzGW-ptbmVNCpZLxiefpKXgZ9UmcaW0ZzT3AAdTtYe6OBO51l8_jW1NgwUNbo5ZrtymIUf_MMQFlZMB-DqkK6subi4cEchgcADQdhkB5mN74ovOhdaunht1jBzSbAqhRntjrtqQjGd88_GlljLBiHr0gaP1bmFg3_HnvuG81-1iax_tWV6xaK0mJ9XIhY4xHfVN4M1vxRr0HtKvC3h9KBfZ21VgJp6knlwMnPuCxzmDdlnrd-oSilL2QvtKwXkFiyDYauFA5n-9Iwz28De9MyCHLrQNYL0c0z13wk2KLTNguItHBSkszn-7t7h-_OsZ1V070nT8QuDdXq77cko9itdLvDndVyrYYNqCCP5lM68B7U_Cop7nyLVi_NwkJjI1dPJEjCrS7JEOjPzGdebcKhiaVk61D0LOcnxVARy28wj7CD30atM76RL5-_wM6waBdrF6gCEdu5R7rXZdY01FVU-3PnIFu1Gd97jPpF5dMc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=nqYThpo8WRne03Nj3pKWo43fo6lEbJffFo3V8uMnlX4ZC1nxI8kiFTJnE8DG4PClnq4w6iBoGMCTGLQQP4ThHXmGUfnMOLm9nQhrgp_vRVwF_kS5t8rsOrrq4SVe9b2xcsqGTg6nq00MUg_s5EYYwsfNstkG3Dzaxn-vb58WzDuHe8fjAjGwrtKvjUdZ6k0kWqPzGW-ptbmVNCpZLxiefpKXgZ9UmcaW0ZzT3AAdTtYe6OBO51l8_jW1NgwUNbo5ZrtymIUf_MMQFlZMB-DqkK6subi4cEchgcADQdhkB5mN74ovOhdaunht1jBzSbAqhRntjrtqQjGd88_GlljLBiHr0gaP1bmFg3_HnvuG81-1iax_tWV6xaK0mJ9XIhY4xHfVN4M1vxRr0HtKvC3h9KBfZ21VgJp6knlwMnPuCxzmDdlnrd-oSilL2QvtKwXkFiyDYauFA5n-9Iwz28De9MyCHLrQNYL0c0z13wk2KLTNguItHBSkszn-7t7h-_OsZ1V070nT8QuDdXq77cko9itdLvDndVyrYYNqCCP5lM68B7U_Cop7nyLVi_NwkJjI1dPJEjCrS7JEOjPzGdebcKhiaVk61D0LOcnxVARy28wj7CD30atM76RL5-_wM6waBdrF6gCEdu5R7rXZdY01FVU-3PnIFu1Gd97jPpF5dMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYLrmLVP9mjcNgy2_2fjhOof9hcRViYAie7m84wJXYCXV-UcHhhF0DMMRybRE2spIF7Yu1JDMyE0McPiP3JSMXoeoH7rlcGM6VFkHclwYOX_3pLPMbsWB1nNxDLK1n366DDoPRq5ClxovtdFJk4vDAKCePobVSOfDWSetuvCYtDYm4nfIc6MR5HLhXLCxrWzB0dahs7zS2RLRuDfh_yo9Labsjj1L3rfur2St1_e01x0QZGxRt2MOV3f4MSltbk4V2VxYDpF1xO3ntD8wnfmXFdgmpoc40-i_F7a452YiHnoLw0Te_mgCg-hJC2UDxtQ3l-45eCStMKMFqFlqXgiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjZeX62PoNsRlKNQBWNLapt8u2wjuWS6cnphmMSZv66NYY8RjM58-dm7E5d7JV5n3bq-CcVw5kaD1FRvoS2fmGKuxUQSt-1-r4f3UgpO3NDamO9ufRQIGd4BfSNrFOuebGCH3jr9QHLR7S0TSiL5GkKMGvn7E4yiDDlFg0i70Ll7vDAUHKNtadagO-Iph67Bi04ZBlHGZbwIvMkP6CFbo55-Lk1YI2_uVY-7cF5DgOpjqOFK11yhkS6BIve_ZYSrAb2JJFfyM_q2RWLpW_Rf4TJ5l6YH_TbB_giDdki8pkZAmdU332nFpphil29LHfv2klrc3OS451t40yiddq2sNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bwf0aWlt4dnaKMnkS1OOg5yFjTqNyIeYrUJRbjHFmMB6kLzYug64-YS3LwBAZF4WQlPD7nlKD5xEb1tDaXSsPsCdHh2pGhcRurocXJT5OadTJSQte18DcsqJzVj9jClglwSf8umLNi2s5dDYQM9wJSkE6r7EkGUOqbYoC2aLFrBe2qXxdWLJ9gV7rufEa1ROj8q_oBqJlRz_jo-iT606URCNziufZz9LP6oEZwmCfe6d3KsR-MO7ZFFoCCzfxJfkA1X8Qn6HthAAFEMdRns3rKaB2zFNqva8YGGans_DCIE3-NCoYJ4IDwrq2q2bCoc6G0tqk5nDvViERsxnOj4-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/an9BWswQynjcnj9xzK7hql1EItye8nHVfNQtpH1dSP0FcSwOeElbOApIlDHGA3Uz6umVr9yoMcjOmPvWMuNO7lcgi6A1e_LYu_VlMAqT-hbxXEVn8CEKE91mkEXIez9tLs6lO3COyHDXzfEz9niBCJs36rvVanJO9O1dXKOYpLdMGP249NS_pqLQQwc6gDYfWyZZATfMZQfo7DjpGUCiEmIfJRe4GJX9aE-I8i8H2CV-Uf4PAteezpmqjFi4ylU_Snxa9KQWTI89l481RwD10dOepr2dOmb2CS_0oNFnIG0EXlB8zaIe2v0dKNVTLwJjoNMtnqVDCCfbkTB4EPSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iFbjoNaL8OtghBSyipYGaDOsT_axaeg9SlUZ0zOI7qv5-x3jPPyQe6vOc6bbjPZ0f5X6RkfLOOrAb2p9C-ust7S_DcUKbtdI4d_6ocQ9u6tX75pDf_tpBbM0BMLNth7WaFuM0-kcamAm6VJbs_rIXehphzsVzB0z1zKuQq_HOF2YGRBxjx7o-abCcPdNFomat4g0yLQzMjKxmTqJoLp6D11LACNjGfiHmcSUUNUSSkuUo1xbM8Tx5-XEaH-lzy1c1UYEUx8LzQVo2mJ2yApe1H2Nz-uEyqwJ4yJW5E0dFyjRoW8wl0JeUypkPJFfWAbTD_a6KFgCg4zU6FycS54hOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4OxONScY_XMhG0vSWZAQ3Vg7-6JK8sEKchQmSahXnlPE7ETY_tDpvFJx84ULQp4_CqDCPDsujHBjVH084RHOjaywC9arptD09goiOagPxdoekhfB0SHsgB0E5lGs7ohIWS5cN1ITSKRTE3UDkvJRVrZpCXhxrAiwN7BstNGEQuESq9yk6nw7-Nm36QUQ7Msu4U7nuauHsAW3wxznslf8OUxImx_a3oB0MAQFleV3NkdNm2k7z9LvR_LrE4tOBqsN01EWyrJzXxmVY2nxyvDGNHDUQ2_4yZwwjht5JPuTRWadUtBpBgeoyuAkn5tn5COanhMV4uv982PdoMi-bJXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=EA_8k5RuU_sVqUO08bSV2RADxCuTGAZdy9zYd7ATcPhi4kMXkaJTWeC2DmS6FDPLV9mDuyylrhxJI1chlTsbmcyt5QFGjPinAtZOvHx593r4VbsvYHWaezDnUtqVWIcr_Az7uFQiegre0AXYYgrlFvgiXKCFrEE5DG-lZr2i7Cqn-DBkdU1RQWUXsp9H2YFQWw9hR4BmxkQDMN9KUoOB77yk4vyT6gaq-Q4Np3entqOYRq4BAud8h4EXahAdDUWj4-6bNZzwI55gcRMerOGLpKzUlA5S4kc2gnw8yATvUa8jtxLtlW3WrZ99shhJtbRQ82Ao8IKhGClpziyl6al8Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=EA_8k5RuU_sVqUO08bSV2RADxCuTGAZdy9zYd7ATcPhi4kMXkaJTWeC2DmS6FDPLV9mDuyylrhxJI1chlTsbmcyt5QFGjPinAtZOvHx593r4VbsvYHWaezDnUtqVWIcr_Az7uFQiegre0AXYYgrlFvgiXKCFrEE5DG-lZr2i7Cqn-DBkdU1RQWUXsp9H2YFQWw9hR4BmxkQDMN9KUoOB77yk4vyT6gaq-Q4Np3entqOYRq4BAud8h4EXahAdDUWj4-6bNZzwI55gcRMerOGLpKzUlA5S4kc2gnw8yATvUa8jtxLtlW3WrZ99shhJtbRQ82Ao8IKhGClpziyl6al8Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T9QENLgz_os1uxK9qA1UVN3aOa_39X_aqHbeP_FBsexsV4ND6DKE8YrteMzWPzI9U88QGBKc0UXHL6wKrXFmFzAxnL02JEIynSQFPVGv6GPYQjInPm5bGEQbcPRLfEq-D0TVv4R8EAU5lMhchLfnE7DJ__TxGCQzLBl0lMhBH3RP5F4jNtco5O9--uc_tcK_Ch4p9BBso8kf3BI5gDVNx--PCOX-Bv1I_9N7hVXns956MCW2yVnVklDVKX-Kkqx17uZJoe9zAg7J5jbxPgoY2mRYADaGKHbU0EHW7MQG7ZBXdTIrFpYfr7aqS_XuLGi-DQa5vIYBS1qV6dfbGAD-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qoD0_MAccCmc50sFBqrFhW0YyChWvwbMotugLSEDrwfELOa52J-ahKbt3dvHxpBAAygqZEKMYgEJmcWoON-iDHTsOoDwnWskS0J3wBlnAcIIRf17CaT_HL1m7ILorS0a3maXJSABxKXu0YKABF3EWXUC1h00ryxb_kevl1hPnuUhkEv7HhhprYFmksEFQzc0NKKIKZCcI_BCFjOgOsblGioGQ5cV5KYAaBKx1burs6zyESM7HIeFvnZFHI7NEoaQ9bCc21XNJtmMmez-jZKo2qUGVMXYKoMsjefHBAGXnHx7P25jlav-GFjy_cqvjRiUwHfXLHJaE6aV3thzVyry_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/saNwcHpqmHXTWOYl0kzw2r0Z4h2wcQE1JDWAWMhPTcpfA35LvuFAxuyAh1zDIfg8XiNe6M7ZH8pxcn0m-OMm0VSpsDxjUUEIiXSOeWK3sRPbLfZwzBZv3EK9rcQGuaMUUyiVULOm6g1mlYDGcgjv43EvBF3z6gRpWpGYGMqPxo6I56ncRXsg50hvHxGO7bgEfy3DyCE98MOxSf15UgJVsap2gMMxPRKvQ1Geo84daIKAzMsVUEn1eCBeX8f1mXZrB2DvcTfiOMo5IWfv-IMq1OsX8Cuyy-YyNW6idSK_qKO0P9TxM1ZEQ6kVqsEnWTqRAx9hju66bw1cmRVSmrVqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rNGNUGn-Cmyu4knwSBq-YUB5Y0VWEwCoLM7VIQZg4_nEdzedFCnaNu2qXgxmTGv96q3rkU8hx79Wa_Ny-UD6Vi_i9xEY5x_9kNbCsCiIyflTOSED4Z4qfrE0VggNzZGBNkz-g44Pu8BrCotjXkg05PdEuY4fLHtMj3UHLAuSrM8JZ1O7UMDUJTHQydDdk55MtcaXzjLlh8T51ZAI0Kgf2vpMAU0qcBfTyfRPBr7rnyxR4KfNl-S-DotzsCf0VKLeLmfaErsMUloFy_P-WLoYOMOp67lWGx6npWI6EJo_VgC7gtdUFgANtJnzycpkeK0FdEABdsd1TIS-Okm4mAp08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H0zZaSY2wxn2JH8lxn54BqwPf5KFT3nfz8ZbLYSkz1YVjQJI2Px3boXUHJWHt4qRHEcmD0VIImHVfULsrulDqAbUXZRE5V2JK_T_TZ-7HohMiy0ska9657hD1VW3Pq9oCXkBS2_n8MyO9aqBwUZJe5VZi7rXPYT0QwP5Fyr46p9pgNW-bO1USrwrF4BfOH6tQLUYp1dPW5RdYwb12wH-RJUrY_3sW9ytOyk5Z9_WlBU7R4t_i6xdXv4m2nYU5T4eSYjh3d61pp8RM4bM1Rkgc8l_buHMY76t6oIpIHJZbZMZzwqynuwhn6B-mAlxCcUi1UQ4Is8F4EUkzuksUZWGIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RG4VxOgMrkSyJCf_8LT_K0XFVEYmL3rO4-0tpW5C1d02ye3M1ZYM-_ST3BZOOevDR1NpArykFEpffDnfo5odU-2Z4DgL4emkXr-MJLFDQc6Fpcj0uAjwSaGnbfxgBv6TH0_I1TWL10GTBFshpQQeB56Hy7kQ85l86LeIw_lhXweLicH7RrLWYvQpd8tc6I2kEb1OoUUq4uMVrwXDibTo0xWw1Eu6E7VbZRKu24hxlIXsiJ1aAgKqLiKhorNRf-eCGd2E9_MNxTdSJh2FMFrPFBonIfNeDZX7CWLszyXMsRmggIXksPKwbNK8GnqJLNXh6gxO06BUpJFxPOiTo2U3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ExBjaOvvz2qYI1FsYYa5HPEjvV8zRLZw8ZiWKEBYPBNo-YrN-6kxM0IJpKiJZEuaMnVOjFC9LKSxXh7-iauHFW1Y6-ELhKJ39h0I2T7wZQnMgAJx02SBgW9AAftxB6KIefw4MyS9MiZmlV7yJ1Vg9KxnBeA8meY0Yz2LRnVRmqNO8c4Qq8HE_rd_MlPEag5pdV770txecasQCqDXbn1Z2_KKPzTv2kvW8UXHgKnfPuKhd0_lyYxCbutjKod-LHrogG7VGIZ0UVKnDryuNTfgQ4-8DUaQLWWFMaEMnapmHQPOVpjALQLSf2b7DpEuAFTQU__xJNCXdMfM-vaUPE_M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tbslqZorwW3H_OMSN36AYj4A-U5nhK3ZMKWblEjEwOsMAi04vCSWkA1i4OoxVB6_ckDe4taMI0bFyhCcZvxnRJP-apStSUpSTJt2b6bIVupduWjNLhkdBloXpRA9hS9DG7wiELb8Hzv_M4ho9A7oUmsaF7QRD8zw0xtm11G6_pfzGtE5ky6CKlLFbeSUqy9AI-6bFZ4QFgoh0AH9VbI5NewRf-ZnZz49FQ4mDUQNdoCjUcIVl3PGhjUOCOgZWXgsZ5xAI5ZL1yUIZK7vLG5Gx3r0k8bh3qCb18MfJ4ZOqs30ZkDnARqyWYmv15fLQULH_KlKHAilpbuMwbbzEb8wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

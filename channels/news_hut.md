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
<img src="https://cdn4.telesco.pe/file/A30rNUImDgbZtrdOEwN72fCZhlVSAC3wdWgGmZ7NZiExaSq_rHFn25IQnVS_19CDI_IloM-GFhqATBKOJ4REVyLgL_t4aVRnKrO5G0efEKaPCkMs9xPZ8pa9byzR-yC8F0VA0ypehS36FKpfsZlJhQWaBDF1E0yRqN9N1kfKB4ljtxavlSTEXcw5g5uNZtWAYo6xQWlVB_QXt-jCKgWq_WMo7NUvSRxiV6SkRmipEydCq1skjoxRcxiBuUerfGOKYCr1680l0VN6SBnJ4Yeh2ofaa8KuJmn87BObUInvQvZeBBWu-6iug8XnjsyJ8WQtt-sWDTKnkWouc2Loh_5kiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 173K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4kw1hahRGWELz1rkluPnV0AnXReCb9jxWzaQbHd7amqfFuUNj4yrzVbbmsoklFU6RE8D5_T5e_C3Bh35-DU7H8lIa6q2MMjMJZ7oXZAJ84LsNs8LkK9RtaSLWgmeLMdCS1sQDK8KOuA5nBzmveJZbBKEyhBoWUqSxrhwSBmoDio-AenIM18dZCFVvM8sWHMkDjVodxAxAVA0rVzg_cRqHMe_iE14pgFRpRfPEgV10NYvtH8ldEqY0ZNSzmM7GyizSuqMpHPrxvrZhZR9ix0sqyxJUkE9wH4tWgxrfDJ4ja5I9z4FhWbJSN5W-K-AAFR_hLZheJbW8vKMmrWAZxCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=lfN5mQMykvORxZXnkwCOyS0kwPiJQlnoPD29cNi3lpdOdfzE0l12DYZAO9BpDrMgi6CY8OTuEaHXhgg-Q3QYjk0HSrV3Y0kh4X3Rqbbrr2rYrliXlnD1YoAX_U5teztS2rc3BWxN6tNv4qrkcYXzu1yUyIoa9RKfW1zKjpapqGJUwZyDpgxwGGO1HYCY8IcL720XwLak1rP5Gal_KNrDTNeUXwcrXR-4KCzX7DHduAFNdedM1Xh_JKxyQwPi4adS78nO96MPpSJLC8Y8dKEpBR5BswVhX-lOe8loL4-hPVvU4b2hIfpkAP5uYmjUPIhGhj0D-tV89pYITK8NWRgVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=lfN5mQMykvORxZXnkwCOyS0kwPiJQlnoPD29cNi3lpdOdfzE0l12DYZAO9BpDrMgi6CY8OTuEaHXhgg-Q3QYjk0HSrV3Y0kh4X3Rqbbrr2rYrliXlnD1YoAX_U5teztS2rc3BWxN6tNv4qrkcYXzu1yUyIoa9RKfW1zKjpapqGJUwZyDpgxwGGO1HYCY8IcL720XwLak1rP5Gal_KNrDTNeUXwcrXR-4KCzX7DHduAFNdedM1Xh_JKxyQwPi4adS78nO96MPpSJLC8Y8dKEpBR5BswVhX-lOe8loL4-hPVvU4b2hIfpkAP5uYmjUPIhGhj0D-tV89pYITK8NWRgVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp3e9wOs1_E22JcirZOLRkrifznWgYF-_9wRLw7K3FpxtsSAOyof6t8XBJhzKet1YpmKKVMYuNdQC-3uNzXzxw2qrB-eAu36XEujh7j7pcERCanFNJGph80WUWC-gH3Ck1vLs73peNpQiT5dIeDkA0moGc8hGliXxq4RlWa93FaJZIHVSAktGeGhrCWSrAaSmPLmRJXvHqFa3HUY_wGT_n-_aJk_TdFnbyCPrkWFwM4ATDh7uYZDXTnPVhi1JpPYlsTwHCZ9g2vMsAOXrWe6BH1zi4FXQhMpHgRlabVWAA-KEHo-9aCgFSvOMkETTHpkf0_u2suIEn65Z65qi7Ikow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqVvXCNAHlEW8s2gtQGi6hfbOfhuX4bVdDqaQM_da-FF-0_bxlZs_g_gu_QFZOxXjNvv8HYLnnP0j9_N-8opWceZ5XQdsTx9uqMjPQPamEfKtdSDUQTZWwVkwcjIfTfG9V7QLaG7QLWa2Cv9NnArP9Ad6nHg6WLNVzH2Qm9p_rRiEbujTYSrl1XeJvKpv2acEMboJs6wUEvaqponzaPhp8iCrpLHTiGKBQWnl9xgNCuj7LHhSCWgtQrB8ZgyEmI3d3q0-CuTnvKYtqq5Uw-g7CIoXlFtQEe2knE0w2WsmrNuz9JI9ZeFCLolQXYPgJ4iIcZUg13SJlGoaz-lIMpkBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNf8gMM58uwy33PJQdDUwUUWd9UwQp29MiOHnETvu1SUNlcYxWIItD6uq0CDZfIWdE3s5f10ZnmK095J2REX-KuCnGSkOzJreO8RQcoewuC_DmiJG8H-Tv1wMxEfLtD_HnMhhlpV-oEGTnTu1n91HSM2wDx30HL_qK6ipF_Tfi1u7jQfJrl6r2gZ9Q3m87iUmmDhUg-yEIyQiX5x9LkvD6ziJdRQ1BtmIgnqribusBAdhzu96rIOOsQJKzzFz7NxJRJC-xS6jtMlE9ZgLoFpnweZGLHraHTqMUxrIt9GGmaTiHBxXTWJlLpHf7x89XoKUTTKk3CrbalVdR27Q5a_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m81fjI_D88be3YxCJOwOCgWPLo3g5fYjak95RZi2JMHe4i2iTtD7Y9sis2q8fuJkrIatrSLdylFMTDgi8KxV4CZ85yaQuzg82QnfUqQHrUtevcciLTElP2Z9z87RUQp6bMPXi1dxEOnzQZ5abWV6tKjsRmUtMXJl0W3MeYyu73jo31J-EWDw-ENHuk4tcX59npZcy4yIImqtnUuNbky9BOGLx_TAWaMADUftbMGM1-f9GtIYTVCKIBjZp-bGr-DlIJMi8kq9dVePbcNU6w8L-75VQTjmRK2FUnTU25ccmtP41Y4mpsirs_8njT-uJnASpEdktTh8Q-vkPN3y4pEnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHt9I5gaWtQOlfCQidwsxATO1nzhwzvNlBe0nzCiV22aR9APLCilbcaTLKadkQZK9aSKU1LzaGbvhj16Xwtn4NJjjLhESIoElEUEgY2cWLDC4jctDWNye4UHlXTO-zd1jTs5jAT0_Xs6Rofd1dyqgFJq9qkn3PAGAf98jm-4W4OGdoIolen3pMci4EBoDDA1OzOZV2oNgGuQu3CLFshYe9Ov1hBzzeRF12eFWJ-OWlDqh5oDRwdSzSNqWtzTdLDhbWKSfbF7ZKFGjrqAIQcjemVNjEUYN12MTT1q3EK1iHqj9nlxmxMe3CcmdwbtSfsNrcVkOqWgX2j_Zdi-A47B6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXv4mrfMfTQDc59oJit_G4rkeZ1PpwLdJbk5P4lsGq0roblAhp3WSFE0RULEnhDhj6oG7UhxZKcSj9_MplNZMH5J9fstdUOgq-DnQ0kyCwUMmwU8NBIwzxWav5keMuhdclIGP_ewQCoYIi4jEJvaYOeb5NZQS8xLHqwAf-zc7Onv4tAgHp1RA3FX3zMNW2a23uWeHrII0gZmNwySR66emuli7s5bD6veQg6jFcBKXL32Ic7m3hpSyYgNJql7l8YznGXKtviDv4DjUok4E8uaQIva7tfAVlhOrBrmMv_0x-U5xKdj2h0lMqNelFYriH8vD4wIki_bo_-ka3z3L8A8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnnBFoblak4eTOWAx2GcRD2FmPuA7awHBK0uMNK5y3Lcjb1OtYB7nC-cdFJC-EurFEqUJWwJWsIk0ArMS2K69I3735hqvWmyZSB2PQEDOLmS4nQdevoUARh3n_MBciYgDdI-q3l50w4QKJTOjLrQdz6wG8hnEEFtm-T60W-oDDmwvFqDQhXCAYyScBGeDqFdMQxwCC24yl8qssEGmdK9Z_kpUmJlITGvdM4Mzti8aZIZ3VdeSHo84Mq5c_A1OCvp8OWEy38aEbsx-X8nWSQUAA4jZG5Fm8pGW5VZk6fxMEdLhGw-IGPhWhZvZmxuV7byZ4aW6rsQU9YDVRRs-jwQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=kWqwW64a_LJBebhhCOh0AS-VyripCbLoJb9_AHYRD8bs5GoVLk9Vk2JKUJCU2octsRvV50TP2JzOH2Lxn_aNywNB4-wQ_0IBersQ8Kz9QSw5rD7FeBo9PqbnFJ3WqZtvOcZNCypuUHSgYn8YUCjnvMg80qIjVOtfnoQZHa4R_UEqIdZzb3NVnqG3LY9mLu_oi2exXOGJYQxPQg6VRzlwpJ8hcpap8wOV7Q6gu9Kc1jfpaUL9vXlgXReIDSyRxhxsaXQzlaJNkjoFzYMsD1ZdKnE35lJjMUn3DjkQWf9yLHonZQFXpKUVKUi9QTO7BABlg1r2Qau0uWyZJOPIGztkJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=aFup_udgQ2t__XVB_VNQXXFvEjclru8urH7ctWXtE4G7MnltSWC2VjS5Bgx9lrivPJXE8-IIsQ9a7OPbL0UztGX6B9oTN-clKSGua4uNxW0FwGop2yBbhSw8PhzCc2ANMz9hIx-1uhIZGstpWbvo23KiPgXdi-gNOKRYY8aYNC3qjNHZMJTZZ97Vj5DqiFDLrewWnQ0ixe_K4qTZenVpRhp0NXCkTUAWq61RPA-ZjiqP_DUth9rEx6NQXBZyUFutYp0PQYhT_kxBiolchU-LQJaEoLbDEVjXYtfhR7Ww1UHUGMFY5TrKJeC-RPMvM53GGteapap1PCbdcc27lIpumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=Xx4Yv0hUksA2qSM0omHTBuQeFXYsZsLeMJ5IJaYaobIVYv0mSBS2-inR8sTbmAtPPPN5-htNuJf0VxdU1kioGuuyTUavDPkoZceMAKgCK8etuJv78KRdVcHlbYIRelpdAeAX7gYv65KiAFw-bJzmJy385D5YCGZKNjFBOeFX75_6YPdlgQ6BDeAdCPetc3OlDeJ4vCxgO49tmHsmHeEpYaMwYOQ3m2ACEQHfRhrFRGq3qKZQ_WInZ_oxXdCePAAf_pDbIpv_Xi_fo29Aotx9kBdFGPmaAUiPYaMQ0OzudUFh-L_EVwErbnnInwyA5KDyqR0ESfPCTwWBm5j6iiplDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=sz2CxIVdZk-jvvNX0CxgMjs8eJhJ-74JDChC1w4oXnDPlW2tDBYuUWdhhLvOddtdyf8G8MnfmcQo8zG65xEN_IhXdiuV_WG0ppzr4dheGytJrOwZQ1Hd05FubqRVusdIOeIxP6XzsTDtC3NYQdIHE_TnV2VQFQV6XoCI5U28VG4BMKqiOI141ZZTbYAvu7tf18vbAEzvahxhlwuRa5yHQ-WjhK9thwncyEHHzVEGEkrGouTvH-RLjUjNFA_VgGsIgmeoMF5x2TPXNnVsDIedDcwcSZzzfq4qkRGUHyEn4dTEh2aVMDvMQ10-1YHE8zBlhmHWO98XNKvhEZW2ySp5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dhts4byZApzyz9400K9OWEBmh3Fnf100wCl6lAVCcl3juOm5kriy6JMeIt-_C-0MlGghkWevs7DmIDVxmsPSawMPcJLINkk5MLc5fLgb3f-xvdDxPViFtOUHX4k8zoabZuibN4i52MAQITr2M1hzbWlLH8Bo4g6QgeKmcODlUObiTdQeUo2oKziMM4cPQxuIxpJvGYcVYnx2lc67Y1ntmOEHQVsdWHd7ajSYu7PV1Pg8RT8YEM1sY89OI_EBBB4A85LsS_EStk6A9A-ysE9I9-gaKMO0c4abeZ1YWyRK4xTT2TMFRKVRXBYx2lZdR45LOoKxEAp8tGELtQgqFvva4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp7PA4WsdFzgeslThhYSt4x1X9kt_sQx_ETW4ATUHst3OGV20tfPtQOnN01CgwvrEHZ99Kj-Km8CoAYdvZEHWbWDLQTx1hAQUVaIu4xDfdb_uGva9TqxBIOoMysvtHI4TpnL4SdkpZst1zNyLJIghI5XQqJPy139WFWYlVx5zAvuLdEH7A0htl6Ar2eVtuoe-L0m2ECILieGFTnG3XG7rV7WsKbMW8yXHxJ1Xer4K6Dq5aO3psFx_Aj0QKJvUXpWjqwaEDweD1frtW0qfQNngEt9nz7zv9PLcfVgP0bJUHLL3GButfSQkiTXnl6B8SXu8SPIdvXI-mbH4NP9pFuUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=cfBcTKO2xzq9Aq9B5NwXC_FLAZi_zpGukTHHfVhMhHL5nl11IEX-YbyItABA5rv3vhFapIzlRC4TPEAIgJ4u0Evn-ZUBGC6tBd4GaQQY54k92yRv_cgMuv7ZLRRz9Rej5jHVE1ZwX5O_00NbnC_k5T9iqK1UpZVqKwHJIjmc5v_OSEYnMaGTdx_WB8VpLcTKZrU1JeX_xok3J_XTHs5ki9bFTFVUGUBSYqlqEbolKfAXj3CUwfPSzwpJFUxHfrlWwNg58MGKebGfuHaFSJh_gushhpAAIGwWvb0vmAN84Q2UAVGCdK-Qqv811yMfFibAObYpM-OFPoQgISXaqsjHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szc0KHvvpEMER4Yb6nqgoaAo1mQpXZhPruviNxWMaH5PYxFrCo7r_m55mU9JGq-ySjVtnhd7X--HSkSsLGCxO0brQy8bNJBnVa5yxiDauIXB6nv6ECmTerDtj_1bZx4qwUxpJ97dktFzt5-VeuRTY5uTmVi4l1MUfyoPUFIHC08MEhCEk9fSFLyto9nzQwqddQUGcJ_mTRJ38Pu6xKSc6b9c9ZLVmfjT_tv-TGzncDcUgBJfvA120j4FAagvFrP73R6SlDwUgBawF6P3FlE5icsr136Two40XYWdF8Jap44HWFdqUp1okD8_0RxVs46S4NLjzVhuqEzYbf7Q6zKJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUIOEMoN6Jp-DX4XEq_L1xZhP3HJyvfqCOaPBnmsLQ-XYvIR_Oiz1kgIjzqMySP5wHfTlhiMoTL6CTqJecDSBPHhGjPd8cv6Uc0g000XyEdNT5p0U0bvRCmc8JeOpgbOGa_8NE6V5xZgJaw4w34Ut_L9QOuYjRXfZSVUJvz52I2Dlb10N999rAAEEQM5Xa8HDCzGJ4a6XUlemvYKErAd38w4fnZr8FC6adxOOFAGe2svqn5xRFLhs-A13AzMp76SI3KBHydc9BMTyKKdUDdpVJvFlKSv5_5pK9kM0V5m3zod3XfMqTiIkt6xZkzpcNtaclqml-VPb8yKbizHwzTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik0kGdTvQ61mZR-6arIfRayieJv5i3g5V6KlvxmKymoRP3JoqPeHV6S3g06B-6BMazitjjU89lIg3Kb0yExR86_z3OGp0YzAm8C7RYHGOLrFRz2AYPUf-7unqrO6temDNWBpR4FlmLGTiv29rnm3px0ESDXniV8v3kspOcieZLPn_RrB4bvkJwSf_hus7kxGo-66TcGWLJDAngjvR1D-ABGXLW3Nuy6z09fCrEvgjMhtpNUGPboiC3u1iyF1yqSnPJts7UJ7iNdBk6kMMTof1CppMRCMJTA9TpC_H_7SPLHGrSBw_tCV_xokkcP9vU6jWU2YXP2v4bGNQf4GhlCCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=rJjq8OoFzyQO0IzMjhajYUSajixcxzdgqkph-Y2mJfa7tznJSRNuI5y0KpykDV_2suJ9kFYqz9VoPnYLnQQrvd2BFoIaGyXHGAdPc92wVXxEEqLudjmDGTl1vh9ddm3r26pQkTS38AezG5p4ibPTUWuPvBRqe7-RVC6HELZWsrs4Ov76qaKyV5OE7pNtR3t1Gt532hU0XxRts13i6-HTPsYGgzakyP1RvQiXft3hXXxr9tBimyuKSw99kIWL1acDI1gkuNwBNqbgtbzLUviLL-NuqwiVys4gvxp9WZa4cncqXoL6YufhRsQ_GJpB__-RYKSHuFI6ljV9bftFMLjQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=rJjq8OoFzyQO0IzMjhajYUSajixcxzdgqkph-Y2mJfa7tznJSRNuI5y0KpykDV_2suJ9kFYqz9VoPnYLnQQrvd2BFoIaGyXHGAdPc92wVXxEEqLudjmDGTl1vh9ddm3r26pQkTS38AezG5p4ibPTUWuPvBRqe7-RVC6HELZWsrs4Ov76qaKyV5OE7pNtR3t1Gt532hU0XxRts13i6-HTPsYGgzakyP1RvQiXft3hXXxr9tBimyuKSw99kIWL1acDI1gkuNwBNqbgtbzLUviLL-NuqwiVys4gvxp9WZa4cncqXoL6YufhRsQ_GJpB__-RYKSHuFI6ljV9bftFMLjQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdbTWQbQWRmZnT9S61uaRPlTPv_uvchP-giGxKZGf-J0SCtKcQsd4MASyZd9FFmUNpjwklVb_ACo9Le290l0pVoGBVZpJjTjwGD0MFumeR_kZ9qo6c9UJdmRjDH4o-_cXekzKgrFFcZnN9rOkR_FqO_99icrHP6HLfu6EO3WXKJLR6T7LPkdgMJkKLSSjTisZY63kWZzTPhUWBP7OEEas9Fnitm9tEUiKQqbEbRQelQuYAprw-6j1KDOhC8MK7T9U2VfoYKndXCnRIyntJ8Gw8bjCFIGLkGoI0K6RafVDbDPJLv7DkeB_V0T1-gb9AWhLlvIQag7vfFLaEgo28gRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=iVNNoeNOVc3AkPkE_p7DBgNG1jp2cbQVWAQN9IocAoKvYivDd3GPl_MGACGkfGOI6Udr65VmX9HSzRLI_ZqxyaSkje0-s14JEGOa6Xz8CnlrG9CdPB_2VMVUR0leUZrY9WF4US7BAV3aNOa2RriKADgR8I906AgmpB1cawJaDFiLZ7y8-3un-YqO8MBnsmSabnMwDJbCUFKquxE8sNF7rXKgc3s_aFouE5G7bgYmv6__gu0_bpF_K5nowvoaYL168eth3sNxyNkwUT8cq4NI2F0KEzu0m5j_urMjYm2qa2QLxutEdTsxEh7UOkaHOJkL4RIIEt9hZmEGXGtXfhw13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=iVNNoeNOVc3AkPkE_p7DBgNG1jp2cbQVWAQN9IocAoKvYivDd3GPl_MGACGkfGOI6Udr65VmX9HSzRLI_ZqxyaSkje0-s14JEGOa6Xz8CnlrG9CdPB_2VMVUR0leUZrY9WF4US7BAV3aNOa2RriKADgR8I906AgmpB1cawJaDFiLZ7y8-3un-YqO8MBnsmSabnMwDJbCUFKquxE8sNF7rXKgc3s_aFouE5G7bgYmv6__gu0_bpF_K5nowvoaYL168eth3sNxyNkwUT8cq4NI2F0KEzu0m5j_urMjYm2qa2QLxutEdTsxEh7UOkaHOJkL4RIIEt9hZmEGXGtXfhw13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGmIxLlqb5ddqpSKe1hodq1jaSPtj4w25Ph1HRUlEkwW3J4mCvpz7dqenHUDa65GKFFDguQaZoiJZlDI-H6dQHpz4W_7gBLj0ffs4PZbVUmh8_GKe5Jxfki6oY4P8V3WhoEFnzbcQILi94nLb1lt3BEDpStUGeABy-YSYSC4i7p6TK97Kr5O0U3TL-kjkljCl8B8n_HPkTMq4pVcFP4E0CewHc8oHY5TtInvKGDg6Vmntyz-qrqmi9_CiHw8PCin2mbvKVaqlrYTwBmXQFtLc5Yc0yaQlNJmm4qp3kiLCpLM4FNq5Ky75hYiY6GwiwSsU2n2-wIgGaoDrnsQ7U9xsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7HekxbynSL7mN_rkrZMGfWlWNzpwpW-k_G3Xu1BYGVHi7U8deVQEKwZI1F-aihqV9Ig0Az6nrAhn_A6zK5rg6dJfa-1elBQePRav05RmSDcPoT_FkK1ziBMP2XrCRxPirEmSznuCb1Any9ffanwYV77M7KgV01X_337uBi1MXwZdKXbNKAhk0jxWvGBKj5W2ouH3BQCXKnDFAam9KgPebFP08Nhj6OgtsAad82J-GN3Rl_aaGbCU1NjT1VNcgeV0IQ8s3n5jAZ_ivMmYT2Q1K0sC1qdhMm85JSU_WSFD_lVB_e6Wfd6GgG_w_vmtPjf7-fostXUtV8kruE7-gLMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=lyEFDBZDIPUCdmqDX7GJW9--PqeYbCdx99v8MJ5-VvIFreEccgeyid1CSpIdpgFh9EUhp04HMLT1rMv0flO7Ux4kn79lYOTK1_ZvRYJfMkSkjSyJIJQi9AdYnZFrbjKBKzjcapr8J88XgjXKMKj4ajZDutc0ojyCCBRixKBtaHAip_rgy_4a-Wb9oZh_FbA1jMC18_VxJK7jJ01aRCqwwzhg9mab7u7dK9FcYOjmw_-JI2i3BAp2GX75PHdL3wI7oS5rMdPNUHSkXVUgp5xisJBahcM4XUKZLFpH6pkoDP0TRTnOc-clJn8YucG3vcVqbnMfX5ltq40clMDT9vdmUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=lyEFDBZDIPUCdmqDX7GJW9--PqeYbCdx99v8MJ5-VvIFreEccgeyid1CSpIdpgFh9EUhp04HMLT1rMv0flO7Ux4kn79lYOTK1_ZvRYJfMkSkjSyJIJQi9AdYnZFrbjKBKzjcapr8J88XgjXKMKj4ajZDutc0ojyCCBRixKBtaHAip_rgy_4a-Wb9oZh_FbA1jMC18_VxJK7jJ01aRCqwwzhg9mab7u7dK9FcYOjmw_-JI2i3BAp2GX75PHdL3wI7oS5rMdPNUHSkXVUgp5xisJBahcM4XUKZLFpH6pkoDP0TRTnOc-clJn8YucG3vcVqbnMfX5ltq40clMDT9vdmUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=QHTI2W0dQEvEYAnLwEUX5dsMjfCRl8nISuaYq2MFhOGp62bXzVOdnV3UFSInIuD-QWD775foObv-DzbAMUXWzCxFTFPiKV-SXQQh_xRfCQ7Zc1tcCO5f5oBJib6aUgOdG0RCytihqEZQs8cfMU4aM44KAFpsw6DqgQ1KBslDi55coAANY-fwo-Cx7kbB3Owar7vE1zUgycfS6gMDEO7EFEi0OfmI-oewTiIkVKykMru1Id058xGcB1oR8NaPo-Ol5KOAxjZuQZ7MsAq1U77_UlbUIKg3WwWEKM7YR_kEj7XP1zkhZ6n8fnN6YixlESLY5Ewv8XiGs4R6kNZPjxw6QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=QHTI2W0dQEvEYAnLwEUX5dsMjfCRl8nISuaYq2MFhOGp62bXzVOdnV3UFSInIuD-QWD775foObv-DzbAMUXWzCxFTFPiKV-SXQQh_xRfCQ7Zc1tcCO5f5oBJib6aUgOdG0RCytihqEZQs8cfMU4aM44KAFpsw6DqgQ1KBslDi55coAANY-fwo-Cx7kbB3Owar7vE1zUgycfS6gMDEO7EFEi0OfmI-oewTiIkVKykMru1Id058xGcB1oR8NaPo-Ol5KOAxjZuQZ7MsAq1U77_UlbUIKg3WwWEKM7YR_kEj7XP1zkhZ6n8fnN6YixlESLY5Ewv8XiGs4R6kNZPjxw6QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا فکر می‌کنید دستیابی به توافق با ایران همچنان ممکن است؟
🔴
املاکی هزار‌ پدر: بله، فکر می‌کنم توافق ممکن است
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=apxbM5Lov8DlLvKyvt4Ddaj-Ua3QvjtPsmJ0SzR2jCCAFNGvthaMNmNe8i-J7PJlebtTV52RZIGZBdrVKPEpOY_KNGY7pMT_pfA7wYM282hyLSXmm-ZIvhItkQcycbJkgd28MOYJTYIa4vyi-2Pa0PuiXpw-ZrirBNQ3S-ktaFvbSSNejYsKNzGuv2MNaLMh7M5xWnaArNSVVlYso1gt-JnWhr1tezUaP5D51GUgeh5AgqlDD71-o74o2ax_ZLrOq5lgK_1FGefM8cQAakwJZ_kxX9qcf-pJZNiEYpooxaV1zXYyK8ZWwUa9mKqYIYm8TQs1FRLb-rO-wEsR0MQ09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=apxbM5Lov8DlLvKyvt4Ddaj-Ua3QvjtPsmJ0SzR2jCCAFNGvthaMNmNe8i-J7PJlebtTV52RZIGZBdrVKPEpOY_KNGY7pMT_pfA7wYM282hyLSXmm-ZIvhItkQcycbJkgd28MOYJTYIa4vyi-2Pa0PuiXpw-ZrirBNQ3S-ktaFvbSSNejYsKNzGuv2MNaLMh7M5xWnaArNSVVlYso1gt-JnWhr1tezUaP5D51GUgeh5AgqlDD71-o74o2ax_ZLrOq5lgK_1FGefM8cQAakwJZ_kxX9qcf-pJZNiEYpooxaV1zXYyK8ZWwUa9mKqYIYm8TQs1FRLb-rO-wEsR0MQ09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=R3Sk7YY1iwNCATTLLDdweZcJklWZuRnUmnFAjrLwcg7CJUHAWETVHf3sF8Dhb01i895fAfs6jRfuw1HHxTgiZknxuCj18LVFg8gsDQKL0o4N-tcNwwAFGAGGiZV47ZKwGFRi31RhHg_aEdZxPAH4UBanmktuu__ziybVW4V1Q6I9OqGaqJEwIUGkOKUeRepUbU4tKz7QoGJ7MkCxzz_GTVAmFMva6G1x3AfbrZ3kbWvflKLoKBBLDNb0S5iGxXe40W1wBCjSuC5rfXAUn19RVzctNT0tO3syoPN4P0njTLfWAG1-f-EvJ1WvMD3vhsHvyct9TxZsiD2SdFrYZyU7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=R3Sk7YY1iwNCATTLLDdweZcJklWZuRnUmnFAjrLwcg7CJUHAWETVHf3sF8Dhb01i895fAfs6jRfuw1HHxTgiZknxuCj18LVFg8gsDQKL0o4N-tcNwwAFGAGGiZV47ZKwGFRi31RhHg_aEdZxPAH4UBanmktuu__ziybVW4V1Q6I9OqGaqJEwIUGkOKUeRepUbU4tKz7QoGJ7MkCxzz_GTVAmFMva6G1x3AfbrZ3kbWvflKLoKBBLDNb0S5iGxXe40W1wBCjSuC5rfXAUn19RVzctNT0tO3syoPN4P0njTLfWAG1-f-EvJ1WvMD3vhsHvyct9TxZsiD2SdFrYZyU7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: محاصره دریایی فقط مختص ایران است.
🔴
خبرنگار:
آیا می‌خواهید هزینه‌تان جبران شود؟
🔴
ترامپ:
بله. چون ما از بخش بسیار ثروتمندی از جهان محافظت می‌کنیم. قرار است هزینه محافظت ما جبران شود.
🔴
خبرنگار:
توسط چه کسی؟
🔴
ترامپ:
توسط کشورهایی که از آنها محافظت می‌کنیم. عربستان سعودی، امارات متحده عربی، قطر، کویت، بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68055" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68054">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ACn2p7GSIKXEhnn2tvbdrfPmDhY1047_xhZia2lK7r_z8bpsYQW3aIMjJkZ8J5vJuy4s6ZdPHHa2C7fUyXnmgdt_etdDPZmlyUCX2vQwpbQ2YDL_ylKqU19RN4mI-0-IKpDFfE4aVi_eWNXOgbDX_KvqTuHGTAB4jOeXJG034sXxl2t9DB4sNPdSYwhS0UnLkadkC1u4dHSNtsjarUzMG21tONpl2383ikL0pIBIQ0IhNXtJsZ7qxpXIH9MgvA9S4mkG0cL0Sp-3dQb1OpwDn6697Z9qXV926JYhiZp-JcktKR87LuUgAErnz5AqOp-T9Wz_W8RNgGvFEojgpPy0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ACn2p7GSIKXEhnn2tvbdrfPmDhY1047_xhZia2lK7r_z8bpsYQW3aIMjJkZ8J5vJuy4s6ZdPHHa2C7fUyXnmgdt_etdDPZmlyUCX2vQwpbQ2YDL_ylKqU19RN4mI-0-IKpDFfE4aVi_eWNXOgbDX_KvqTuHGTAB4jOeXJG034sXxl2t9DB4sNPdSYwhS0UnLkadkC1u4dHSNtsjarUzMG21tONpl2383ikL0pIBIQ0IhNXtJsZ7qxpXIH9MgvA9S4mkG0cL0Sp-3dQb1OpwDn6697Z9qXV926JYhiZp-JcktKR87LuUgAErnz5AqOp-T9Wz_W8RNgGvFEojgpPy0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آنها را در موقعیتی داریم که هیچ نظامی ندارند. هیچ کاری نمی توانند در مورد آن انجام دهند.
تنها چیزی که آنها دارند اخبار جعلی است زیرا آنها اخبار جعلی را دارند و ترجیح می دهند ما در جنگ شکست بخوریم تا اینکه در جنگ پیروز شویم، که واقعاً به نوعی خیانت است.
ما امشب یک حمله بسیار بزرگ دیگر انجام می دهیم. آنها می خواهند معامله کنند. ما دو روز پیش معامله ای انجام دادیم و آنها می خواهند معامله کنند.
آنها 47 سال است که مذاکره می کنند، اما هیچ کس هرگز آنها را مورد حمله نظامی قرار نداده است. ما خیلی سخت به آنها ضربه می زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=KkbK693wNKsplLRnUZvTg2uKw1Tj5IRV8RAunVCuoRBztbHsGuhKg7SubJ5PR6Q9RidvTKm5jybVvsme0WLWbABm20tG2bolqbjrAWQGJTRSxajcVuyB5QoZoqaH3RJ_l_9Heidwpsszd6S1FTwheObVAtzASpenbCRlbQWrptgmx1EqsjVyu5JK_dFu8la1jrgQHxax-r-v5Ml-49pSjutY3uoNdsha_W9tGN1ZAKjmVJXtm3_Wq8Sff8UyXGeq4DKTsrmeyJeSNzsg3oyTTs8_6M6lVnPNBcuhsdYy-4Uv5x-zzkyosH74S1CpRo0WIUfyZnEgxgyogLHIME5iKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=KkbK693wNKsplLRnUZvTg2uKw1Tj5IRV8RAunVCuoRBztbHsGuhKg7SubJ5PR6Q9RidvTKm5jybVvsme0WLWbABm20tG2bolqbjrAWQGJTRSxajcVuyB5QoZoqaH3RJ_l_9Heidwpsszd6S1FTwheObVAtzASpenbCRlbQWrptgmx1EqsjVyu5JK_dFu8la1jrgQHxax-r-v5Ml-49pSjutY3uoNdsha_W9tGN1ZAKjmVJXtm3_Wq8Sff8UyXGeq4DKTsrmeyJeSNzsg3oyTTs8_6M6lVnPNBcuhsdYy-4Uv5x-zzkyosH74S1CpRo0WIUfyZnEgxgyogLHIME5iKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چهار ماه پیش، این‌ها نیروی نظامی بسیار قدرتمندی داشتند؛ بی‌شک قوی‌ترین نیرو، احتمالاً در کل خاورمیانه. آن‌ها را «قلدر خاورمیانه» می‌نامیدند. اما حالا دیگر نیروی دریایی ندارند. ۱۵۹ فروند از کشتی‌هایشان به زیر آب رفته است. آن‌ها ۲۳۰ فروند هواپیما، یعنی هواپیمای تهاجمی، داشتند؛ که همگی از دست رفته‌اند. آن‌ها سیستم‌های راداری فوق‌العاده‌ای داشتند که همگی از بین رفته‌اند. پدافند هوایی بسیار قدرتمندی داشتند که آن هم از میان رفته است. متأسفانه، رهبری‌شان نیز از بین رفته است. رهبران رده‌اول و رده‌دوم همگی کشته شده‌اند. حتی برخی از رهبران رده‌سومشان ــ که کم‌وبیش با آن‌ها سروکار داریم ــ نیز از میان رفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68052" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68051">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCXFnBzX6V68-FBEaAFw9Amnfucak75sbrSANWB8lvC9c_BDa7TvTu2NRWBawAEYg1kT1RWDREzTVcptHW1Gd19bwrI_t4ee-lOc54S4MGASFMCu6dooI7WYM4RFqm4J9C0Ok_uYSuWmAetz6wHHjNR_HBDT3UAto3U37Z94MxiZJZBy0HxzQG0XZWHpwjQqYLc1eKIqZwBaAVwarX91K7rFT1oldW6QzD7esnSSelYUCovRDKTkgCmg-1zMWwLlTOTKQt0FR9CK3_C3GXS_PJwmjAErJqFeaX3QnBsBOVkEDM7iceciALylqIP1g7II6XAzIn28HtinIu5QBgcS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=a5VzkNOkAmyE_wA6vWJeMAXDzTro2NlgPhlxRSnec9IVh0BQ-YrCfJQ_J2ythE70qhHKdIpthzboTctqD2alGm2J2KlsT2rGIoxRWXjWtiZntkAHoCY1PrlDNFiGdMaIQ2Fx-JllCvGZO_RPf2D1s13B0FS2W0iNF7PdHizOlG1a7MBya0ZCFwehPNEXWduAn2v2mCNgeHEek_xNVJ4fwXny_3ysc93dXENAoCLaennwyj8_xCSx2r66CQm88qRGGjc5A1-EyGw8Dn0GLgl369ApiyVhlRzTxXnaU5XcIk0Ga2AJ_I34N1Im2S9ws2-q3Scxx6YlYSLgyhfD7afvvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=a5VzkNOkAmyE_wA6vWJeMAXDzTro2NlgPhlxRSnec9IVh0BQ-YrCfJQ_J2ythE70qhHKdIpthzboTctqD2alGm2J2KlsT2rGIoxRWXjWtiZntkAHoCY1PrlDNFiGdMaIQ2Fx-JllCvGZO_RPf2D1s13B0FS2W0iNF7PdHizOlG1a7MBya0ZCFwehPNEXWduAn2v2mCNgeHEek_xNVJ4fwXny_3ysc93dXENAoCLaennwyj8_xCSx2r66CQm88qRGGjc5A1-EyGw8Dn0GLgl369ApiyVhlRzTxXnaU5XcIk0Ga2AJ_I34N1Im2S9ws2-q3Scxx6YlYSLgyhfD7afvvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
همان‌طور که می‌دانید، امشب ضربات سنگینی به آن‌ها وارد می‌کنیم.
ما حجم عظیمی از مهمات در اختیار داریم؛ موجودی ما در سطحی است که سال‌ها نظیر آن را نداشته‌ایم. ما ضربات بسیار سختی به آن‌ها می‌زنیم؛
این روند ادامه خواهد یافت و در نهایت خواهیم دید چه میشود.
ما در حال نابود کردن تمام توان تهاجمی آن‌ها و در کنترل گرفتن تنگه‌ها هستیم.
ما دوباره سیاست محاصره را اعمال می‌کنیم. شاید محاصره مؤثرتر از حملات مستقیم باشد، اما به گمانم ترکیبی از این دو روش است که واقعاً کارساز خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=FecOWQ-bB2h1UatLwHq8g6XFc6f3r4eNuqtmC1UMW9rxxJEtD3HGTCraG51CFmKTG_jL2NwzE8QOSzBJNCFwwbXI9LR8bE-jQ96fGZ2v-U4ixlNIvlqCeMikTfpx92WpzNIZjYaMMGHAU6FB75dup4xuUYiRnb8xFoh_8znA0HimfjbpdFrdC7EArozkIlwxcr3h1wv1tt7MxC_e4lZ9oDSM48EUuVypZwNVxyy1kLDwhVRtvGk13vC1wybjw_h-h4KefGKCNh2apkplfobRgncQOXQkQ5R1WEaArmR0Wa-pcWoZYnpKJ_2qTf32t8ddUnE3GnKJc_BysuPkYfgEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=FecOWQ-bB2h1UatLwHq8g6XFc6f3r4eNuqtmC1UMW9rxxJEtD3HGTCraG51CFmKTG_jL2NwzE8QOSzBJNCFwwbXI9LR8bE-jQ96fGZ2v-U4ixlNIvlqCeMikTfpx92WpzNIZjYaMMGHAU6FB75dup4xuUYiRnb8xFoh_8znA0HimfjbpdFrdC7EArozkIlwxcr3h1wv1tt7MxC_e4lZ9oDSM48EUuVypZwNVxyy1kLDwhVRtvGk13vC1wybjw_h-h4KefGKCNh2apkplfobRgncQOXQkQ5R1WEaArmR0Wa-pcWoZYnpKJ_2qTf32t8ddUnE3GnKJc_BysuPkYfgEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ارتش آن‌ها را درهم کوبیده‌ایم. ضربات بسیار سختی به آن‌ها وارد می‌کنیم.
ما همین دیروز یا پریروز توافقی داشتیم. کار تمام شده بود، اما آن‌ها بلافاصله توافق را برهم زدند، چون متوجه شدند نکته‌ای در آن وجود دارد که باب میلشان نیست.
طرز فکر و رفتار آن‌ها متفاوت است و ما چنین چیزی را تحمل نخواهیم کرد. ما فقط به پیش می‌رویم.
ما امشب به آن‌ها حمله می‌کنیم. ما تمام توانمندی‌هایشان را در هر زمینه‌ای که به تنگه هرمز مربوط می‌شود، از بین می‌بریم.
گمان می‌کنم در نهایت، کنترل کامل آنجا را در دست خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LS3uF6jNzwGPFenhu4mKzhvAgLsCtJKBFqU22WmMm2N1br8n7F3giehAg_ryLc4xzTRpDseS8QEBPR7mYrrjpkyvVVjzYNmv6c7sj_6x_UVJooVUpWZMtYD397u2m_QeCNCZ78PaTWuyN6-tUEgIBkNDZTFnU3-DGc7GGYNKzO78RcjFtzqSwfTBfFx0hipri5XRtjNrv1M3WbC0vgwUaG8nDPJDqJWs8J1xyaFuMDm-w_SzVhlX64kS1PXn8KOnYLdTY2yqbTei1j_upTTB7wVLpqw7YIKyPf9Kldttl_9_K0xveUy2n75Ji33HTU5HItGg1gJPCIixphq2-zsmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b5Gh6rgf1v02XJEu72vm6UpgBEO29gfevs3PWwdFPI91Kc10NwCbiRcBKJ0urn8pXEnDG-E8XVK5dX0cdIsjaiUjfLOsA3TVrEl79vCTtGO-udLM0Mp8NEPSTs81USwqpP-2ppxwODbsdZIlNgdBDvvwOyZ-9lTKJ4bwX8lAv2p4ZEV6aAzz8ItojWKGo2NSU5G7h1yx7LCu_uPqJDyE4FbBdX9s3AYXxIkFo0-3Bwwj6BvrjWy6bMq3cXN4bkiJgF9kzb8RmTOCneDpT4OlZreWEAnqKlnLo_yPQBSg8mwlbbOo1DzQO5N-eeKRYAqoyckUKvZoSvfLRLbMaS6G6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqRXfDuBSK819fTrLuYKxtyiFPNvJZm7Gn3BoztXZ1wZfdP2JpIjsBNTCj8MmEh1nnk5jR3nBg8AEf4T1sZH0WXrnpSEwpmzl-FpxaRmkzNqnYxgOo3d32l9MizMQ0ZFu8WIpc94ZgxocaD0MvidAUAJu-gknVzlYkGnIpYqsnVia8lRa5lYoNR_49N9ubZKNFwmS63qxyon0YODWN7ZRb3X1iOqhU8auv5YbE4CxPpPsjiJPCVFdofdExdeNMPJvZNe64RGTR_NbXALHDu3gsrm_RDd7ipS2e-768oZIbJiyvSNniPxjroS9ozObz9NvZhXp7qUtbABFOhetzvC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpEEfecyt5bQ4ov0TsEiGyJI06Zxz-PDMFEvxS0Nod1qZXYLqhEf1xlNQCndY84_mGG-8n747QPKAtjQMFPbJaUbRyc_pnEwhdxRAFTtEM_ViNto0KnST4xLfsT8jirg0MSsGMfSJOL8jmXDvQgI0GH1cyi3kofMuOTZHGHqgk8po-4_Cfjh8PNe-FUyHiOOTwJ9uaww4fJijMHu527cFssovLa8bOwDgfxESoQDjXztH1-E98vk19uwxN0cD6rDovczpadTwd3yudLk6gUl3o2j6NrRXhvPd-j86PCv-cN7dCQ-0CAh7ocqdXfyYah3X_jWHUQW8SdKs-eEMsg87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68043" target="_blank">📅 00:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=lPCeTEgTw0alRiMRwWq7yECsaeis58HcphuWFdySzEj9Pdp7rclKopbTe3i8_tjYoPzl5xTF6tSbzkb1rhS8E_X2UtYtczENhNZ95GbZEdV6zjJdMtvPhk-u6svY8SkjWUSifLG3RRRZvI5aYmzJW1tjkBDWdPM4QJZn_EsRdtS8QwBqavr5qTM2QVi7ia6y8AniWhC4LWEl7KjgbQPQQU14z_CS3K_4_s1ovd-8QKjt7nfiKnwl4jhf3GTRMrXuaRMLHkwbnjIUS3CgOcTSNJi1j5g53wpSp3GMzw9CjeLPx9-7d8uI5Au13Vu3lb0i7zj31mLDNCLRvBmleL9W8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=lPCeTEgTw0alRiMRwWq7yECsaeis58HcphuWFdySzEj9Pdp7rclKopbTe3i8_tjYoPzl5xTF6tSbzkb1rhS8E_X2UtYtczENhNZ95GbZEdV6zjJdMtvPhk-u6svY8SkjWUSifLG3RRRZvI5aYmzJW1tjkBDWdPM4QJZn_EsRdtS8QwBqavr5qTM2QVi7ia6y8AniWhC4LWEl7KjgbQPQQU14z_CS3K_4_s1ovd-8QKjt7nfiKnwl4jhf3GTRMrXuaRMLHkwbnjIUS3CgOcTSNJi1j5g53wpSp3GMzw9CjeLPx9-7d8uI5Au13Vu3lb0i7zj31mLDNCLRvBmleL9W8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
منتسب به سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68042" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
انفجار ها در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68041" target="_blank">📅 00:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
تپه الله اکبر زدن بندرعباس ایستگاه رادیویی
گزارش ممبرای چنل
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68040" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
چندین انفجار در کیش
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68039" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68038" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmKNAXVahrY5lwczo1iQzZdDNG0LQBCq7v2wWiYqtuyA1lqMZ-RZGsaJa49buoTL9jE6zTWkZ8Ssjcu40FSOd9Ea5PWOFOiFgu_o8sPCUt--v0wxL-5slkdSrM64XZbK-TCaLVZ2jvzvgUOmhCXsJT5uxbZ9MyYXTUBhSvxXQIc4AwcBQ4XOMve2GalziJ0LywmCILmvDenxA13tf7Lrfiod58iKANxr6ksDYz7hbxYQC2-V1kVjZrin4hF9UqaGX9XkEyW_0aST6QnEWZh3t0fQveIfvT2eF9w4MRkA7LMN1pgD61H_gSQY7r7hiF4OXz_K5Iqml794UP94n33WNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرقی، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل، سومین شبِ پیاپی حملات علیه ایران را آغاز کرد. این حملات همچنان هزینه‌های سنگینی را بر نیروهای ایرانی تحمیل کرده و توانایی آن‌ها را برای حمله به غیرنظامیان بی‌گناه و کشتی‌های تجاری در تنگه هرمز تضعیف خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68037" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های اولیه از وقوع دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68036" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=tDxeZPq6V0cHhLFVkokZQaKwoJ0C_6dCQSudIWqJlVcsokORXRCLx_Y117usUQxBAztvnVSFm8bx9FvVt-JXhXHldmwgMnme8zKLUnHPFVfxNEtun1cvfA-9wZxwoin2_Pi4FD8MOJ0pP8qLx3Wmmn45ALsCo9kEEA3xeBOFVVfI0SVDnoUQ0buOttJRh47wTncEhYhXbsOOCPKcDCtvzjXT_JjREic0Svh8ZVDL5l-4Ub9XTkZ4eX_1XawJcK2N4gwz3g2drLXxfKTrYXk8UqarXEFVQDcsd05zr2bGoWCLj01lJxHuMN59tL1aclc7z4QLLNYRFig7uhUDC1Gf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=tDxeZPq6V0cHhLFVkokZQaKwoJ0C_6dCQSudIWqJlVcsokORXRCLx_Y117usUQxBAztvnVSFm8bx9FvVt-JXhXHldmwgMnme8zKLUnHPFVfxNEtun1cvfA-9wZxwoin2_Pi4FD8MOJ0pP8qLx3Wmmn45ALsCo9kEEA3xeBOFVVfI0SVDnoUQ0buOttJRh47wTncEhYhXbsOOCPKcDCtvzjXT_JjREic0Svh8ZVDL5l-4Ub9XTkZ4eX_1XawJcK2N4gwz3g2drLXxfKTrYXk8UqarXEFVQDcsd05zr2bGoWCLj01lJxHuMN59tL1aclc7z4QLLNYRFig7uhUDC1Gf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
«کوه پیکَکس رو از بین می‌بریم.
به ایرانی‌ها بگید که داریم میایم.
و هیچ کاری هم از دستشون برنمیاد!»
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68035" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=KcU06UykviXGhovfsxdnEoIRmulLsWs230YkyqS6BFS4rlr-aUnapfC4MgLebVhWdH7tWEXN6L90QsufVRoBWOl2u2UWdW9CgYbBP5VocxsaiGv_DAvczbxCVWM6MfSBYmJbbCl3oQUk_ZHviloDluM0kZqjcMwGoeiM2AZ74H2s_hq3ZB6Jd6mzsoxThFRjcAq9p3vl-9iKY0jtbKH2idTkL1-_7by_vrkK8YPGSluKAvRMpSGOnrhxeeDItMKbbmIPVnLyeyi9yJLQvNP_jJYgzsu-wLXXZJCDbESZkJFLgEJN5gzZr9QHz4lqpRWevOop_z43JuReiBSMSq2ZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=KcU06UykviXGhovfsxdnEoIRmulLsWs230YkyqS6BFS4rlr-aUnapfC4MgLebVhWdH7tWEXN6L90QsufVRoBWOl2u2UWdW9CgYbBP5VocxsaiGv_DAvczbxCVWM6MfSBYmJbbCl3oQUk_ZHviloDluM0kZqjcMwGoeiM2AZ74H2s_hq3ZB6Jd6mzsoxThFRjcAq9p3vl-9iKY0jtbKH2idTkL1-_7by_vrkK8YPGSluKAvRMpSGOnrhxeeDItMKbbmIPVnLyeyi9yJLQvNP_jJYgzsu-wLXXZJCDbESZkJFLgEJN5gzZr9QHz4lqpRWevOop_z43JuReiBSMSq2ZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره صالح محمدی کشتی گیر اعدام شده :
«اون کشتی‌گیر یکی از بهترین کشتی‌گیرهای دنیا بود.
فقط به خاطر اینکه درباره حکومت حرف زده بود، اون و دو تا از دوستاش رو کشتن؛ حتی حرف خیلی تندی هم نزده بود.»
این ادم ها خیلی وحشی ان!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68034" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
خبرنگار:
«آیا تفاهم‌نامه‌ای که تیم مذاکره‌کننده شما از ایران آورد، از همون اول قرار بود شکست بخوره؟»
🔴
ترامپ:
«نه، اون برای آزمایش بود؛ یه تست بود. نمی‌دونستیم نتیجه چی می‌شه.
ببینید، وقتی با یه مشت آدم حقه‌باز طرف هستید، تفاهم‌نامه ارزش زیادی نداره.
البته حتی با آدم‌های قابل اعتماد هم تفاهم‌نامه خیلی ارزش حقوقی خاصی نداره؛ چون فقط یه تفاهم‌نامه‌ست.
من هم گفتم اصلاً چرا باید اول تفاهم‌نامه امضا کنیم؟ توی آمریکا معمولاً اول تفاهم‌نامه امضا می‌کنن و بعد میرن سراغ توافق نهایی.
من گفتم از همون اول برید سراغ خودِ توافق.
ولی در نهایت، اون تفاهم‌نامه یه جور آزمون بود و اونا توی این آزمون موفق نشدن؛ به تعهدشون عمل نکردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68033" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره هدف قرار دادن مقام‌های باقی‌مانده حکومت ایران:
«ما قطعاً اون‌ها رو زیر نظر داریم. آره، اطلاعات زیادی درباره این موضوع دارم، خیلی هم می‌دونم، اما فکر نمی‌کنم الان زمان مناسبی باشه که درباره‌ش حرف بزنم.
باید ببینیم چی پیش میاد. مثلاً امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
اونا هیچ چیزی ندارن؛ تنها کاری که بلدن اینه که لاف بزنن. و فکر می‌کنم کاری که من انجام دادم، کار خیلی درستی بود، چون باعث شد بیشتر باهاشون آشنا بشم...»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68032" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOZUFpzed-RlQp4nUUNySYci2mfYQQJ3yYFBh0Ysc4aXx3qUpTNNO4l3uAwRhkJd1D2OqKwd1gV1bXpzoST4pTZpTMFUHV2XNeie_HigaFLfTKoK8cbS3HYGABeI7hDQOD7fW4KjiVr-wyDpuBAoe3RmevPVBoJiCfZaGs3f-YI489omfKTsxvVqNuubz1HOLpr9mek-rpCxURCwuvACCkOftYR6beST2sDHG7Ly7pgiwkgY5iXIQMOwoHHBhl5ZgZKqguE870b67eY_eaNQkKBcfm89fjBgbheTrTZm3DVyu2tdtVtbuvLwT0bakEQxgrW2-1hptMWWPl-F9RJ7CPg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOZUFpzed-RlQp4nUUNySYci2mfYQQJ3yYFBh0Ysc4aXx3qUpTNNO4l3uAwRhkJd1D2OqKwd1gV1bXpzoST4pTZpTMFUHV2XNeie_HigaFLfTKoK8cbS3HYGABeI7hDQOD7fW4KjiVr-wyDpuBAoe3RmevPVBoJiCfZaGs3f-YI489omfKTsxvVqNuubz1HOLpr9mek-rpCxURCwuvACCkOftYR6beST2sDHG7Ly7pgiwkgY5iXIQMOwoHHBhl5ZgZKqguE870b67eY_eaNQkKBcfm89fjBgbheTrTZm3DVyu2tdtVtbuvLwT0bakEQxgrW2-1hptMWWPl-F9RJ7CPg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
«به نظرم اینا یه کم دیوونه‌ان؛ در واقع فکر می‌کنم همشون همین‌طورن.
اول رژیم اولشون رو از بین بردیم، بعد رژیم دومشون رو زدیم و بعد هم حدود ۲۵ درصد از این رژیم رو نابود کردیم. اینا طرز فکر متفاوتی دارن.
دیروز به یه توافق رسیده بودیم؛ تقریباً همه‌چیز ۱۰۰ درصد نهایی شده بود. اما یه دفعه یه تماس تلفنی گرفتن و همشون از اتاق بیرون رفتن.
این آدم‌ها واقعاً دیوونه‌ان. ما به توافقی رسیده بودیم که همه‌چیز به نفع ما بود، اما اونا دوباره زیرش زدن. از نظر اونا، توافق برای اینه که بعداً نقضش کنن.
اصلاً نمی‌شه بهشون اعتماد کرد و راستش رو بخواید، اگه یه روز به سلاح هسته‌ای دست پیدا کنن، ظرف یک روز ازش استفاده می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68031" target="_blank">📅 00:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
خبرنگار:
«
آیا شما یا ارتش آمریکا، یا حتی ارتش اسرائیل، می‌تونید به فرمانده‌های رده سوم، چهارم و پنجم ایران برسید؟ می‌دونید کجا هستن؟ می‌تونید اون‌ها رو از بین ببرید؟»
🔴
ترامپ:
«آره، می‌دونم. ولی نمی‌خوایم درباره اون صحبت کنیم. البته که زیر نظرشون داریم.
من اطلاعات زیادی درباره این موضوع دارم، اما فکر نمی‌کنم الان زمان مناسبی برای حرف زدن درباره‌ش باشه.
ولی... امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68030" target="_blank">📅 00:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
تاسیسات اتمی  خاصی در منطقه کوهستانی موسوم به " کوه کلنگ " در جنوب نطنز قرار‌ دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68029" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=nIiNUKcLEHlcbNe32aeKfqEAYqcrn_nH0QedsXonIWfAwYluzGWPvIG7wy8YhGvr7Psv27Pmi1QX_l27SjhfEmzWaIsnjgNbw2adyw21qjI16wMXNp-H57cerzETNkqfKwdo3gMgk0EpIeTPggxNNjnQ8UpUpE_UEI69Ou_FpgoGk7ze8GgUXUHFnE1Gaq2pVwdkRroy3S2tSdCL3Hcqkrqpl8kP2UK1gmSYUOjSVz5KfSG8d51Y4U6sQiHFhppJ50hbanCB62X_QqrLYU2OPkDILjE114eMLxtXyHItsOuq7dYrIXOGMzRqF_5__XY7b5atbEmH68X3AbHi-XtDzq-EgGcBtnjDz88Xh9vfVt93OfnC6PSI1BKTX9RKPasXnNVGA9cYJoJ2lp74RubgD9Z1seebbvPx2YGIRreU3X-Qzm78byV_POdvCr8KhdDXkt7OkbYJQtqSGPAQlvpw-otRfGz3wpfBTBvFm1l_JpRckL0a6IUSAK8uYro9-fxdaL2euvyWEbAvmTB4kEPQ_bz2Rf72G9dM4o-psJeJXB4e563boZAHvW-pmqBbBXZ4haBlwmGBvfbU073dLd79_OV26xFLS0zFS2OjALZiDJ10V7AokW63YuEJA0mjHU3Vmi6CqcUjFTXfOGYvz74aDcVHMm9cAoJDc8HEolk7sVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=nIiNUKcLEHlcbNe32aeKfqEAYqcrn_nH0QedsXonIWfAwYluzGWPvIG7wy8YhGvr7Psv27Pmi1QX_l27SjhfEmzWaIsnjgNbw2adyw21qjI16wMXNp-H57cerzETNkqfKwdo3gMgk0EpIeTPggxNNjnQ8UpUpE_UEI69Ou_FpgoGk7ze8GgUXUHFnE1Gaq2pVwdkRroy3S2tSdCL3Hcqkrqpl8kP2UK1gmSYUOjSVz5KfSG8d51Y4U6sQiHFhppJ50hbanCB62X_QqrLYU2OPkDILjE114eMLxtXyHItsOuq7dYrIXOGMzRqF_5__XY7b5atbEmH68X3AbHi-XtDzq-EgGcBtnjDz88Xh9vfVt93OfnC6PSI1BKTX9RKPasXnNVGA9cYJoJ2lp74RubgD9Z1seebbvPx2YGIRreU3X-Qzm78byV_POdvCr8KhdDXkt7OkbYJQtqSGPAQlvpw-otRfGz3wpfBTBvFm1l_JpRckL0a6IUSAK8uYro9-fxdaL2euvyWEbAvmTB4kEPQ_bz2Rf72G9dM4o-psJeJXB4e563boZAHvW-pmqBbBXZ4haBlwmGBvfbU073dLd79_OV26xFLS0zFS2OjALZiDJ10V7AokW63YuEJA0mjHU3Vmi6CqcUjFTXfOGYvz74aDcVHMm9cAoJDc8HEolk7sVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«آیا الان وقتشه که مردم ایران دوباره به خیابون‌ها بیان؟»
🔴
ترامپ:
«نه، اونا نمی‌تونن این کار رو بکنن. چون سلاحی ندارن و فعلا وقت قیام نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68028" target="_blank">📅 00:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=HcnNGoZrEGtbXMbWBCHRjdPrDcS5JRzV-xLhdgWDQlNWtF3omko6g6YkvSj-szaEslGNYw3MD0tymzqUa7Pi6boTL7Do80xngEETWHpvGg3YaisNZoN2us3KutpwMgH-LStlZo5_ZF5OpSYG1-wvud7b6lNeZFGh6RESt25bn9sPWJTyRk5bAiZeLDSCoFYnEwJUcFR8scRNOVhXvPYIsCIB2-juDOr5J9vqsf9hp5AE14CPc_9Nnwzt8z5oZ9KWJsh321arilbOcxkMmHL16X36d55xlfYvgaVSLAAopa5drqZoNkorIbpv0BtvV4ZXSKsD_J5PucbZ3w-nMV5t2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=HcnNGoZrEGtbXMbWBCHRjdPrDcS5JRzV-xLhdgWDQlNWtF3omko6g6YkvSj-szaEslGNYw3MD0tymzqUa7Pi6boTL7Do80xngEETWHpvGg3YaisNZoN2us3KutpwMgH-LStlZo5_ZF5OpSYG1-wvud7b6lNeZFGh6RESt25bn9sPWJTyRk5bAiZeLDSCoFYnEwJUcFR8scRNOVhXvPYIsCIB2-juDOr5J9vqsf9hp5AE14CPc_9Nnwzt8z5oZ9KWJsh321arilbOcxkMmHL16X36d55xlfYvgaVSLAAopa5drqZoNkorIbpv0BtvV4ZXSKsD_J5PucbZ3w-nMV5t2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند تا از حامیان حکومت توی آلمان تجمع کرده بودن که یکی از مخالفان حکومت اینطوری یکیشون رو سورپرایز کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68027" target="_blank">📅 00:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=UHFmg4oYg-5QlU-4m7pPdfMy012Nub5tga11RRtK6REuAO66U6JnrZdmaaGHpPVAi5smaaaOvLngj9qu78WCK5aIqAHL3Io8yvr_7_tDUmwXtXcqsjIrcz01SUFRZNLZ5lDbqHiX5k7kABYACdqBr5eku7YpLUdToemgxKDkvbrXvycOx9dFt-Mk0pQKf8S_nUaknl4I7m13vZ8r_8V1dHmpKyOZ4Uc9qrLXsUX0-jO47N2D8dScpVUpZx-qmjYCKR_0wbYXtM4ODmESxJ7M76CCKtydZWLI_4RTGqUX-vXfE-vc07UFlKUfdpvCObIco13w1cnnHKMkewOW6vCsfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=UHFmg4oYg-5QlU-4m7pPdfMy012Nub5tga11RRtK6REuAO66U6JnrZdmaaGHpPVAi5smaaaOvLngj9qu78WCK5aIqAHL3Io8yvr_7_tDUmwXtXcqsjIrcz01SUFRZNLZ5lDbqHiX5k7kABYACdqBr5eku7YpLUdToemgxKDkvbrXvycOx9dFt-Mk0pQKf8S_nUaknl4I7m13vZ8r_8V1dHmpKyOZ4Uc9qrLXsUX0-jO47N2D8dScpVUpZx-qmjYCKR_0wbYXtM4ODmESxJ7M76CCKtydZWLI_4RTGqUX-vXfE-vc07UFlKUfdpvCObIco13w1cnnHKMkewOW6vCsfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ خطاب به مردم ایران:
«کشور ما می‌خواد به شما کمک کنه و دوست داریم همه‌چیز به‌خوبی حل‌وفصل بشه.
افرادی رو داریم که آماده، مشتاق و توانمند هستن، اما اول باید بدونن شما خودتون چه تصمیمی می‌خواید بگیرید؛
این انتخاب با خود شماست.
ممنونم و خدا نگهدار ایران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68026" target="_blank">📅 00:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکم بالاترو نشونه بگیر املاکیِ پدراشتراکی، بیچاره جنوبیا خسته شدن #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68024" target="_blank">📅 23:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68022">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:   امشب و فردا با قدرت به ایران ضربه خواهیم زد  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68022" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68021">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
یاداشت تفاهم با ایران یک آزمایش بود و آنها به آن پایبند نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68021" target="_blank">📅 23:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68020">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
امشب و فردا با قدرت به ایران ضربه خواهیم زد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68020" target="_blank">📅 23:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68019">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
صحبت های امروز ترامپ با زیرنویس فارسی
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68019" target="_blank">📅 23:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68018">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
تسنیم:
چند کشتی متخلف در تنگه هرمز هدف قرار گرفته شدند
.
منابع محلی از هدف قرار دادن چند کشتی متخلف در تنگه هرمز خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68018" target="_blank">📅 22:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68017">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c2989693.mp4?token=DheInAi7DfYerG_lqhiWNuoJlSnU4WktiwwOXiAHCHnBnkQdoS5XR1-ZOevYUrh-eV239cUcsWdHCckC7km9qmOk3u2cetn-7aUHe7w_x-VidOdk4put6DrvYeQLOAiebQGXW25W2rQDfPvqX_trcEIIL3h_apc0baq9d6AKYt74ADVPcJjJ9u-eD8Z5It4M2pk2Z44mb3n-TrY8F1MWDLR46aasPBZajBLejeXEs_lpFHbIl-i1qJ6G2JZ4h-o9-Hzs8NQqCdgNy3A0PsJwc9R_LpzfqCIxlwFEonUSYn1D6-bCA_YW9etUVzu460i_CkhUkaV3cTI6y6X48KOYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c2989693.mp4?token=DheInAi7DfYerG_lqhiWNuoJlSnU4WktiwwOXiAHCHnBnkQdoS5XR1-ZOevYUrh-eV239cUcsWdHCckC7km9qmOk3u2cetn-7aUHe7w_x-VidOdk4put6DrvYeQLOAiebQGXW25W2rQDfPvqX_trcEIIL3h_apc0baq9d6AKYt74ADVPcJjJ9u-eD8Z5It4M2pk2Z44mb3n-TrY8F1MWDLR46aasPBZajBLejeXEs_lpFHbIl-i1qJ6G2JZ4h-o9-Hzs8NQqCdgNy3A0PsJwc9R_LpzfqCIxlwFEonUSYn1D6-bCA_YW9etUVzu460i_CkhUkaV3cTI6y6X48KOYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارهایی در شهر کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68017" target="_blank">📅 22:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
بیرجند، چابهار و سایت موشکی لار لحظاتی قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68016" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIznybpXXyh7hHM7hyV3UzV9sRknmZ3V6UHE2cePkqPhfxeHz8nxK_8uZE-ClbxaipVvtP1GNHp39o2Y_ncPpTRv2Y3R7AO784HXURwHIzWZXTE9ZbqwXVR9zbQAbR2DHgsFDCW8tKnfC_A1YMgM23oqesH1_FewrUWmagL6aj1EkpfBN92qRehArSckf9df5oq-xa8A_zt8IoqGIswuXsNPXKjGvmpu_ISBF0M0SbHxRPA5TKAv1OQKvgborV1meJDAOva2tr7r7qnTyC8KAFHBmlhwSnhJX99_TqpUIPOt0WuhAs7g808kJHT7RFez-tUpdEhvJgUEgwVG2zsccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:
رئیس جمهور ترامپ پنجشنبه شب، ساعت 9 شب به وقت شرقی، خطاب به ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع متشکرم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68015" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ij7c3sbr6bkCwALzDj491oat8h46VQuV_skSTEWO-T3hxI8PWzXqxI2qmJXHs5ykjCFKtXJxrLNHfniRQeZI1wKt2KZTP02dKDf-I_pGr-j8BwhpOSOawXloBLG5fqgHdn54gApkPV0pN3ii3NibTNmuMZWc6BCsCGf2VDwxOPBIcWe5XuU6sqjfFQTZXJRdwydGHgapC2Q2UhHtp8KfgakhJTsgALOo4KhKqPvT3Nb9l7z8jrpcCrexuQehApLUuqoiG6SsX0d-4AWcF7_M-Xh8N5CFG_AVcJd0txP7ztxwe8MF229Zin_SvOl1atycWU0XzTIBwwhmkAyMeSh1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی، وزیر خارجه جمهوری اسلامی:
رئیس‌جمهور آمریکا کاملاً حق دارد. هر کسی که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تأمین کند، باید بابت این خدمت پاداش دریافت کند. ایران همواره «نگهبان» این تنگه بوده و «برای همیشه» چنین خواهد ماند. البته ۲۰ درصد رقم بسیار بالایی است؛ ما منصفانه عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68014" target="_blank">📅 22:18 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

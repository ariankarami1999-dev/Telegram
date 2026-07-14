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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 01:18:55</div>
<hr>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=CZzOD1RmZM0P5y8eVjGOOE3eJ6egsaZoCs7c9mbtTqYlDLdMkszS5XIoqYXGz9YqMGiQIFIZraz2x5bapjY2KOYUPD5kGafon3kDrBtJfKwHzOYWXxyowBap2z2mW61QqbVkVZeDkg6W9FMKzhbxwk8hps5id7uoDUtUW9fcCkmm6HBVqgDlzduM3pDwvkDtZuTC722dsTI4cWPMTOmSPLa_X5uiqb_Omj50i-6IVg9aoB9YOPFLgfis3UsSYLJrs7HJf3koYwfc1GVwsQ2mCNDDbmZ0JS19qgFD8Dd-mlKwUYzPKiwavRmlPy8LypZEs-Ac8SBC3jwG1sS1hmPaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=CZzOD1RmZM0P5y8eVjGOOE3eJ6egsaZoCs7c9mbtTqYlDLdMkszS5XIoqYXGz9YqMGiQIFIZraz2x5bapjY2KOYUPD5kGafon3kDrBtJfKwHzOYWXxyowBap2z2mW61QqbVkVZeDkg6W9FMKzhbxwk8hps5id7uoDUtUW9fcCkmm6HBVqgDlzduM3pDwvkDtZuTC722dsTI4cWPMTOmSPLa_X5uiqb_Omj50i-6IVg9aoB9YOPFLgfis3UsSYLJrs7HJf3koYwfc1GVwsQ2mCNDDbmZ0JS19qgFD8Dd-mlKwUYzPKiwavRmlPy8LypZEs-Ac8SBC3jwG1sS1hmPaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul5kIS09y3DZgjjhz_MYalp1I-nKrvbwfMD3LELFzKvRJz8AgV_mxxl50UEEm9IuG1-D4sNNQ8xL1vvcTGiLfkDwDCSoA9duxUP49FvIAA98bDQmKEHj_CcN34UmEDU8EWI3AaG4iGqo7m-oXq--124Q1pdC1KSHFCzEUH5a0TuxxX9H-HK2sh5YdM7yKxEby-wStVFu7B4QOI5BUmAbpd4pwOT0FThlFFr4RP18Ry-t2uNNWfkwRO2L_Hr-DVn6WHVMOviY4m8Ju_5i_0ezjJ6HnlQYyvKhSib2WXlHS_e0CSzXbUbVY8fKfNk46Pf72GBXw9oIhHIsvidHH955xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=nJo1jqtMoABSIeVzuFF88Ag2X9gM48qkHbFID2DrR7i-C5lEINAu3wi-aOtyGp09qYVlsVAP2whG9xLRLEuSzT8PV0UahWbvmso6isGrMJreoItyiTtFbHa4QAV6o3yVJr3pACQaz1RprIKjm_t_YrwpBvnLCZOW2vvU7hmXr4oJczsfk1OFb8j1G3KvoJ6YY3g0eKwl3vCY-c1qup-v2FmuDKis7H7MQQALJxxoMwmVwirSO0v2BkDjer-xqabCK9LrQx8IjAcOb8IshJGNuNTcxcBtx6sEtPG-_nrY6Mgi8k4eErfzKgDsGlSUijCDIkctyi4GPPCax3xcgjfPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=nJo1jqtMoABSIeVzuFF88Ag2X9gM48qkHbFID2DrR7i-C5lEINAu3wi-aOtyGp09qYVlsVAP2whG9xLRLEuSzT8PV0UahWbvmso6isGrMJreoItyiTtFbHa4QAV6o3yVJr3pACQaz1RprIKjm_t_YrwpBvnLCZOW2vvU7hmXr4oJczsfk1OFb8j1G3KvoJ6YY3g0eKwl3vCY-c1qup-v2FmuDKis7H7MQQALJxxoMwmVwirSO0v2BkDjer-xqabCK9LrQx8IjAcOb8IshJGNuNTcxcBtx6sEtPG-_nrY6Mgi8k4eErfzKgDsGlSUijCDIkctyi4GPPCax3xcgjfPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4kw1hahRGWELz1rkluPnV0AnXReCb9jxWzaQbHd7amqfFuUNj4yrzVbbmsoklFU6RE8D5_T5e_C3Bh35-DU7H8lIa6q2MMjMJZ7oXZAJ84LsNs8LkK9RtaSLWgmeLMdCS1sQDK8KOuA5nBzmveJZbBKEyhBoWUqSxrhwSBmoDio-AenIM18dZCFVvM8sWHMkDjVodxAxAVA0rVzg_cRqHMe_iE14pgFRpRfPEgV10NYvtH8ldEqY0ZNSzmM7GyizSuqMpHPrxvrZhZR9ix0sqyxJUkE9wH4tWgxrfDJ4ja5I9z4FhWbJSN5W-K-AAFR_hLZheJbW8vKMmrWAZxCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp3e9wOs1_E22JcirZOLRkrifznWgYF-_9wRLw7K3FpxtsSAOyof6t8XBJhzKet1YpmKKVMYuNdQC-3uNzXzxw2qrB-eAu36XEujh7j7pcERCanFNJGph80WUWC-gH3Ck1vLs73peNpQiT5dIeDkA0moGc8hGliXxq4RlWa93FaJZIHVSAktGeGhrCWSrAaSmPLmRJXvHqFa3HUY_wGT_n-_aJk_TdFnbyCPrkWFwM4ATDh7uYZDXTnPVhi1JpPYlsTwHCZ9g2vMsAOXrWe6BH1zi4FXQhMpHgRlabVWAA-KEHo-9aCgFSvOMkETTHpkf0_u2suIEn65Z65qi7Ikow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqVvXCNAHlEW8s2gtQGi6hfbOfhuX4bVdDqaQM_da-FF-0_bxlZs_g_gu_QFZOxXjNvv8HYLnnP0j9_N-8opWceZ5XQdsTx9uqMjPQPamEfKtdSDUQTZWwVkwcjIfTfG9V7QLaG7QLWa2Cv9NnArP9Ad6nHg6WLNVzH2Qm9p_rRiEbujTYSrl1XeJvKpv2acEMboJs6wUEvaqponzaPhp8iCrpLHTiGKBQWnl9xgNCuj7LHhSCWgtQrB8ZgyEmI3d3q0-CuTnvKYtqq5Uw-g7CIoXlFtQEe2knE0w2WsmrNuz9JI9ZeFCLolQXYPgJ4iIcZUg13SJlGoaz-lIMpkBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNf8gMM58uwy33PJQdDUwUUWd9UwQp29MiOHnETvu1SUNlcYxWIItD6uq0CDZfIWdE3s5f10ZnmK095J2REX-KuCnGSkOzJreO8RQcoewuC_DmiJG8H-Tv1wMxEfLtD_HnMhhlpV-oEGTnTu1n91HSM2wDx30HL_qK6ipF_Tfi1u7jQfJrl6r2gZ9Q3m87iUmmDhUg-yEIyQiX5x9LkvD6ziJdRQ1BtmIgnqribusBAdhzu96rIOOsQJKzzFz7NxJRJC-xS6jtMlE9ZgLoFpnweZGLHraHTqMUxrIt9GGmaTiHBxXTWJlLpHf7x89XoKUTTKk3CrbalVdR27Q5a_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m81fjI_D88be3YxCJOwOCgWPLo3g5fYjak95RZi2JMHe4i2iTtD7Y9sis2q8fuJkrIatrSLdylFMTDgi8KxV4CZ85yaQuzg82QnfUqQHrUtevcciLTElP2Z9z87RUQp6bMPXi1dxEOnzQZ5abWV6tKjsRmUtMXJl0W3MeYyu73jo31J-EWDw-ENHuk4tcX59npZcy4yIImqtnUuNbky9BOGLx_TAWaMADUftbMGM1-f9GtIYTVCKIBjZp-bGr-DlIJMi8kq9dVePbcNU6w8L-75VQTjmRK2FUnTU25ccmtP41Y4mpsirs_8njT-uJnASpEdktTh8Q-vkPN3y4pEnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHt9I5gaWtQOlfCQidwsxATO1nzhwzvNlBe0nzCiV22aR9APLCilbcaTLKadkQZK9aSKU1LzaGbvhj16Xwtn4NJjjLhESIoElEUEgY2cWLDC4jctDWNye4UHlXTO-zd1jTs5jAT0_Xs6Rofd1dyqgFJq9qkn3PAGAf98jm-4W4OGdoIolen3pMci4EBoDDA1OzOZV2oNgGuQu3CLFshYe9Ov1hBzzeRF12eFWJ-OWlDqh5oDRwdSzSNqWtzTdLDhbWKSfbF7ZKFGjrqAIQcjemVNjEUYN12MTT1q3EK1iHqj9nlxmxMe3CcmdwbtSfsNrcVkOqWgX2j_Zdi-A47B6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXv4mrfMfTQDc59oJit_G4rkeZ1PpwLdJbk5P4lsGq0roblAhp3WSFE0RULEnhDhj6oG7UhxZKcSj9_MplNZMH5J9fstdUOgq-DnQ0kyCwUMmwU8NBIwzxWav5keMuhdclIGP_ewQCoYIi4jEJvaYOeb5NZQS8xLHqwAf-zc7Onv4tAgHp1RA3FX3zMNW2a23uWeHrII0gZmNwySR66emuli7s5bD6veQg6jFcBKXL32Ic7m3hpSyYgNJql7l8YznGXKtviDv4DjUok4E8uaQIva7tfAVlhOrBrmMv_0x-U5xKdj2h0lMqNelFYriH8vD4wIki_bo_-ka3z3L8A8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dhts4byZApzyz9400K9OWEBmh3Fnf100wCl6lAVCcl3juOm5kriy6JMeIt-_C-0MlGghkWevs7DmIDVxmsPSawMPcJLINkk5MLc5fLgb3f-xvdDxPViFtOUHX4k8zoabZuibN4i52MAQITr2M1hzbWlLH8Bo4g6QgeKmcODlUObiTdQeUo2oKziMM4cPQxuIxpJvGYcVYnx2lc67Y1ntmOEHQVsdWHd7ajSYu7PV1Pg8RT8YEM1sY89OI_EBBB4A85LsS_EStk6A9A-ysE9I9-gaKMO0c4abeZ1YWyRK4xTT2TMFRKVRXBYx2lZdR45LOoKxEAp8tGELtQgqFvva4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX2yz-YkPkpvbXN5RruGpYJ70va-LKi1bv_WmBzfAy-5mzJDcQXrFmIUc4uOa2WROl00_Rs_DpmQKpgby1F0Z1SDFh_bsh6GkT2mqHXYiMbTcySZ7bFvS4En0tDXhmpBnujnjitMoKoejDDiza9b0w6yfXlDIsKOUkcK1RtDamvYzYXVotNwmplybi-XLZln7UtibO_uT86vHBUusmmJO5jDLjHgDTnbC228rZh05oyaS2QkmTs5QqLzojIU8CdhQOTqzFdVz_ryB9YzAzYieevOub5vOfO7Y6im5NMQ8dSFIY8lkJxaOoJzBjDtQkGkF74PAm5GyRX7TjfCXFZ2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2QeTXSxMBxtw3Mv8GTUPuwwbv2z18x6K452k6d3pMcLIhkvTItqN3UDCo5lGtj3FF9J8xBE2474_wFu2bvSUhfEaE4irQPJbG6M4I9m0uEFcID0ppypkFdmRIq8ogxSKweSddTEy31kcEbTsL_iWqjUwQC6lBRCP_jWHs54M2JVOK5nLLv-MsAgbT5_R6kivnvR4KDlsle5q9Y4RsAKJS1pkbm7oJ_P1iX-nNcl-HChYQxPR0DNfW4agyUiJBEolRbh6w6m_cfhw2b9XUTTx95ntnnVvZG6WGAOBt5SoRh_RU6ZlVBS364fB3VB96lh8IOHErxdWSOuqGfyNbWcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=hQebsLSc9qgH6lk_S7ubEzaVHHiLmXh7-A4vPsMdUlRO8czUCQUtK__I_kaxlFwYIopF4U2wY660toQ2zR-cXor6dnmtx2VQ0JDn7-VRl8Y6rEt7ogLo3DYtx4lZiOdr0RDKkot4SY_UgUGrpTybRQxySRZ1Urr-lDA1GKgoSZKD-haCxkkAcw9SpKnq7e1n72ZOMgYnPjTG4YP5I_9rCPkxw6hpmD8NMQhj8wYdG1X-AL6edWZBVJvrhCFYgdemyV2Aa-AJALkcRhELWKAYeMwZ_SCEqtNovC3VIaBOmKoFh2K5TNK2DoBiCaLTCNPcVQS1cZBhq5Ox5BkpOooonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=hQebsLSc9qgH6lk_S7ubEzaVHHiLmXh7-A4vPsMdUlRO8czUCQUtK__I_kaxlFwYIopF4U2wY660toQ2zR-cXor6dnmtx2VQ0JDn7-VRl8Y6rEt7ogLo3DYtx4lZiOdr0RDKkot4SY_UgUGrpTybRQxySRZ1Urr-lDA1GKgoSZKD-haCxkkAcw9SpKnq7e1n72ZOMgYnPjTG4YP5I_9rCPkxw6hpmD8NMQhj8wYdG1X-AL6edWZBVJvrhCFYgdemyV2Aa-AJALkcRhELWKAYeMwZ_SCEqtNovC3VIaBOmKoFh2K5TNK2DoBiCaLTCNPcVQS1cZBhq5Ox5BkpOooonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=in6G5svR5U-Rkx2o_j-yuuEqgm357AdxA5HNrsGxdixQzT_lPHQz6YIMTijhrumiyXnvVNWK0i2YPQV-eFWw85kss3kfg72xnSlhrKd29lyOUoOJ3gRVpwQg8yehXG7PsPbv_Q8heZwm-trndrJogjeOQ4YKS8m8sneqGvVrA0Eb1jnr3FS_95xXQZJBlZBkjqtkY7Tk9yI6HtPAt-i3dF_3IZXi9KdZ8kfRIqziezRtIo_hZBdkdPD4HnMIz0UiVJxfw0RDxic0Y-tuqxmVYEhOOY7nn5BYCOPSqWynNXIw0hc6rbYCska3W4rG5hPrUTTttCzxo46_Kaq7mMrhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=in6G5svR5U-Rkx2o_j-yuuEqgm357AdxA5HNrsGxdixQzT_lPHQz6YIMTijhrumiyXnvVNWK0i2YPQV-eFWw85kss3kfg72xnSlhrKd29lyOUoOJ3gRVpwQg8yehXG7PsPbv_Q8heZwm-trndrJogjeOQ4YKS8m8sneqGvVrA0Eb1jnr3FS_95xXQZJBlZBkjqtkY7Tk9yI6HtPAt-i3dF_3IZXi9KdZ8kfRIqziezRtIo_hZBdkdPD4HnMIz0UiVJxfw0RDxic0Y-tuqxmVYEhOOY7nn5BYCOPSqWynNXIw0hc6rbYCska3W4rG5hPrUTTttCzxo46_Kaq7mMrhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuYDZRSo50ZFFVhhgw9pmjms4sqKJYlBTmVd4PU5ojMUxk_rS6Du-ba20WxQAr-lIiA5MyBYiZLYN4AAGlHHfKclAXKAiAxfa_n13uIzZ1wL4QGSSCWgnwaBhs3b6yItqpaNWjRVZAJ6H4n-KTccH-KJrzKnh06G1csxV0AXzz5-cUWDz8t-BUJMq82OBtIm4Kww3OArPlKZPjoKRJLwWY_lYYA3_eD2hB6YkoUnM0FHz3Mp69H8xHVmNS6d0RDe5utEg-AE2mi4cxh-QSTlatofWQUx8dw-9A8hQ1ceXd4m_b3Cljf5DCh0660kfVA_T8f4rURq_wcIlIL8oOYh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=FbKoSzs9gSId3JP7nPRapnLJ-AiV_mMFBX4PpFRS6yAYzLJAZ58v0HzPXt60DRslvDNTPB-hpkhxccpghcC13892A8UpSp4Pcc6hbO-zQOuzYW3NNj-t8tGWO98f5tN1KYw3bMZLA-Bdfot9Vc4Gcff2gp8mh5OyMP519RhSxHrJYQ-72HVAK1iak1UDPALAUOt-ldXdi6R90aW-cYmntApMpkBNScF7W5Ahs2rTUI0N2AtsWWVFbNndgA0R-BPFZVC-fCKJAnozk3iuv35gx5Op5pE4ER4r-jCchON1G6TK1LW1wV1b9zMoxpj6bmfiiSxQEleVaYN-_P0WBt5xiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=FbKoSzs9gSId3JP7nPRapnLJ-AiV_mMFBX4PpFRS6yAYzLJAZ58v0HzPXt60DRslvDNTPB-hpkhxccpghcC13892A8UpSp4Pcc6hbO-zQOuzYW3NNj-t8tGWO98f5tN1KYw3bMZLA-Bdfot9Vc4Gcff2gp8mh5OyMP519RhSxHrJYQ-72HVAK1iak1UDPALAUOt-ldXdi6R90aW-cYmntApMpkBNScF7W5Ahs2rTUI0N2AtsWWVFbNndgA0R-BPFZVC-fCKJAnozk3iuv35gx5Op5pE4ER4r-jCchON1G6TK1LW1wV1b9zMoxpj6bmfiiSxQEleVaYN-_P0WBt5xiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNAlqo0i_AbI1mlnvs2hmQnFzGgoMOYuPw6Jsp2iwjHce3aP0VzQkhmiiDbLCJda58DPJqnSTjtMnqimS8HUSJEqYcF7wVtz_f0cxaMwnbSoHFvCgoboVLzeU51oGUp2aeSNjmXvR64TG34nlwJM1Vp2vfOGFpwc26v93jF9x4Tgf9l1rXWyqcgkQ-WsnIMRy_kqvgobnKplnTSEgsMpL1QEvTcLAPNGr1R3CyjIYLhjGddLiMVs2ptyZL7d5qO1fyNcUkhqk3kYbq9J7XynO1GnGzINNU-KaR37bfI5IO6_NGmNdhHuJWwNY2NOLs0aTjqftJT4Qqx2E4WoP6V7Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=s3DxswzgySxAEoVxH4e7-dOl2MZap-6YWHYZ23Cwl6xLQlbs-efl3O_ewY8oca5-F253KZwTwGzzQF-vfaWhMkVQerRkCh7bFUudBl-Kep1UmyYPUeuIgDWLyB2X-c58KTxOlkGDJXhp7pRLvh_kCsHF_YKXj0Kc54KShmDjrhC742awRlPxI5D0qOvvjG2TcItpPrp3RRMkmsQVSbiZO7CztV6uyFt6nus92tVvU8kvX4O9uVe2Z_JXN1Z2w08ikVpd4BExJwGBnjqvIE6VD2fL5CtIC0jE_LNi4D76_qzcET9oPmB-62xNN154-m6Me7bew_MF2wSgRahSX-Ks0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=s3DxswzgySxAEoVxH4e7-dOl2MZap-6YWHYZ23Cwl6xLQlbs-efl3O_ewY8oca5-F253KZwTwGzzQF-vfaWhMkVQerRkCh7bFUudBl-Kep1UmyYPUeuIgDWLyB2X-c58KTxOlkGDJXhp7pRLvh_kCsHF_YKXj0Kc54KShmDjrhC742awRlPxI5D0qOvvjG2TcItpPrp3RRMkmsQVSbiZO7CztV6uyFt6nus92tVvU8kvX4O9uVe2Z_JXN1Z2w08ikVpd4BExJwGBnjqvIE6VD2fL5CtIC0jE_LNi4D76_qzcET9oPmB-62xNN154-m6Me7bew_MF2wSgRahSX-Ks0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJRXGZsCKJ09zC3Q1w2YeoLH0TWfDYinuXPqSUxTxri_44oNiQDg5n5fwvsyk7VjrBwYOZrjFHCZ8W4_Gyjd9WtuXUwL10KZf17jVaCy1-Ry7F19Ai3rScFj6pAp_DNnsIfY0MAhfVBLYdH-DnXh4w3v5ZsqS98Dt-_aUxQtzXSbIkRwRWpkG5k5Xn8gtr2PD9NUCXEupRVrxWQEbJQnSkxL7K7voJIfqDkTAkIdG-qIscmhk902CeC7y8KIVfwj4Gi0knAjM_w3I2UeIl6hQoSMEHJd0jNaQdV-SleLXoOGt12bKqfDohOZgiUVtNTaWsgALs0cS3AwdwkpaJ3Dbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9dGfvFo0HUsHl8b2VZB68I64DuhfL6NJLc3oeqqLkkYaA8HH2g-BkHXcvzkcYqcgEwC6oVeGU_cq8gWYL5k_fLbkNVJo9qBWUzOnjChdegl9qDerD7ZrlY_nG6UU8vsjrPn_JoO41EaL3AxFYlZ7EVm_n3F0Q12NweBH0s3I00yXfQf5LuBdgaZueFMCm6R1OZkUXKQi3l-NxN13uuM3PCmjYCrETDAgAgTXpjV5-CS3Y69oNlV6cf-gkN_yZCFyeesPwigwv806EksfcxfKH4sFP_mZQOu-dRNmNlqrrr9Wo74Ve05cJaHihYQrktjEZMX6teAkXnLvCINdE64w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=TEpCMYxOnyaBLSoZsr8NwXG_Uakf0uFVSeqvTrivoc_yvN7a-AMAt2vzOBqpFGt6_xbKWsrnXuiHiBrtsqzYZo3xkP5GINmUGHfVsnk5BdYLqJ7LNsedWwsZUwRZtoNqhulrhegQpCw35Vwl1PHy10htvjSNgDhQnufQhpUN6tAhp9tVgILUn6J0LW80N-GZ1ppDutmhhO6aj20i2IxUF_a_RSAmKmihYJflXIVUD1xqNAE3cUISzZN0fUOymIKrNthlwvMBd5qPwpBZXZ2kIPgcyEUNMOToBP61VU0-ro7MdPEDnCnWrulG447AJ6Oe-4Bd_XiHWIpiSo2sexLn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=TEpCMYxOnyaBLSoZsr8NwXG_Uakf0uFVSeqvTrivoc_yvN7a-AMAt2vzOBqpFGt6_xbKWsrnXuiHiBrtsqzYZo3xkP5GINmUGHfVsnk5BdYLqJ7LNsedWwsZUwRZtoNqhulrhegQpCw35Vwl1PHy10htvjSNgDhQnufQhpUN6tAhp9tVgILUn6J0LW80N-GZ1ppDutmhhO6aj20i2IxUF_a_RSAmKmihYJflXIVUD1xqNAE3cUISzZN0fUOymIKrNthlwvMBd5qPwpBZXZ2kIPgcyEUNMOToBP61VU0-ro7MdPEDnCnWrulG447AJ6Oe-4Bd_XiHWIpiSo2sexLn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DVNiQPmRLG8W7z3eVUUbsR59skG-9IH44_mU010G_f3FjRK6EelKTtt5eg3mHOuztdcp-rmdddRUa8q69D0rA95yvZsiGr978oYaq3BoQIiAU1BtdlAgLZldj9bXJ_C5X8H3kY8rOa-ldW8Fp6vJHegJ9XoDnFOQy6VLY9-qvVJsxB4fBtqWlsoVS87bQnXfw32bXjSaYCO_hG3Moj0jCVuUyj79eAdyRszM8fcJ-NqB8ic1NEC6HyLPL9hDfw1V2W5ukHq3vG_sUrkBj3kInWpSXAvZIAo6XcbhUut1w09vujw3x4tt1qmIkhxSmvvN-CskL4YMHaz9YxFTFxdU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DVNiQPmRLG8W7z3eVUUbsR59skG-9IH44_mU010G_f3FjRK6EelKTtt5eg3mHOuztdcp-rmdddRUa8q69D0rA95yvZsiGr978oYaq3BoQIiAU1BtdlAgLZldj9bXJ_C5X8H3kY8rOa-ldW8Fp6vJHegJ9XoDnFOQy6VLY9-qvVJsxB4fBtqWlsoVS87bQnXfw32bXjSaYCO_hG3Moj0jCVuUyj79eAdyRszM8fcJ-NqB8ic1NEC6HyLPL9hDfw1V2W5ukHq3vG_sUrkBj3kInWpSXAvZIAo6XcbhUut1w09vujw3x4tt1qmIkhxSmvvN-CskL4YMHaz9YxFTFxdU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=HVLqjkEg2TDHVzLfN6fDAYlV-3q7pnZqjkHCiGYeweHFgl7St8i3_vvvXHB1VRjGp8Gd7Iv76UKTLM5ptE2rPJ38rP2DWI4vPqJ6mMKk2Ti8fBUz5xCCrd5dOtgeemSEs8Sd-nowPWZgAIXbYw-6CMrGP4zsTC0Ve9p-QRpknvVFQkXq3dLW5KHtWDQp-3FpTAkukUojSqMKDJlxJcVAsrvBKD8IB1YfPZ22DNAy5r5XFbNWhFEdRuLDeJTjok4Cww4IVD98f8SEMRgpXnI2BSr3wvKVUE7gwZKXENJkfKVDVQa_1gG9uXviR1g4VtQ9PD9IwgCfXiKx_f5SX-kcVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=HVLqjkEg2TDHVzLfN6fDAYlV-3q7pnZqjkHCiGYeweHFgl7St8i3_vvvXHB1VRjGp8Gd7Iv76UKTLM5ptE2rPJ38rP2DWI4vPqJ6mMKk2Ti8fBUz5xCCrd5dOtgeemSEs8Sd-nowPWZgAIXbYw-6CMrGP4zsTC0Ve9p-QRpknvVFQkXq3dLW5KHtWDQp-3FpTAkukUojSqMKDJlxJcVAsrvBKD8IB1YfPZ22DNAy5r5XFbNWhFEdRuLDeJTjok4Cww4IVD98f8SEMRgpXnI2BSr3wvKVUE7gwZKXENJkfKVDVQa_1gG9uXviR1g4VtQ9PD9IwgCfXiKx_f5SX-kcVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=gIf048lWTnjdMk3GiwQI0_vlZ92lh4YM9-6rPuvWuGZnFnHa9WBnYf25uAt9zYE8UPMVBu2ENtbg79Flcklsw3SxvCvE0wP36uLZ0W1Iy65VD7HtBeo8607fX_38jnh_owajCz6c22QieRO9AxT2FkW2fGSo7PLiotk_mwB4x5WhrvJiIfdnQOS3xtbWsqPVdEsAFtAjbv5KcrTZly0DAaeOLin3zuQ0XIny6gAGRcYEH7kIKOz6jt6o0afPIyMTAbORxOdkAP2EDDQ6N_e94kQ67JYJXdFFZ_bkcRD3WE7VqU2oHrFV9o9m7eN7zEfWimEo0Sr7gOGC-epFmCrjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=gIf048lWTnjdMk3GiwQI0_vlZ92lh4YM9-6rPuvWuGZnFnHa9WBnYf25uAt9zYE8UPMVBu2ENtbg79Flcklsw3SxvCvE0wP36uLZ0W1Iy65VD7HtBeo8607fX_38jnh_owajCz6c22QieRO9AxT2FkW2fGSo7PLiotk_mwB4x5WhrvJiIfdnQOS3xtbWsqPVdEsAFtAjbv5KcrTZly0DAaeOLin3zuQ0XIny6gAGRcYEH7kIKOz6jt6o0afPIyMTAbORxOdkAP2EDDQ6N_e94kQ67JYJXdFFZ_bkcRD3WE7VqU2oHrFV9o9m7eN7zEfWimEo0Sr7gOGC-epFmCrjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jnkgRemSzGOR0GZo404kxFwwJCJA32F_lOEtsJ75UoGZ22Q-NUkIJPIGnVNOnyWEjzNXALi-1RZLDZpBrHlyJDDm-OfG-YoZ5mutaaLBdujeiTds4tEOmeyjcHcjK-6gbxYvcIi-eL1bmhsKzHlWbSyOvxAZxiZaHZWm6ln2ZtQgFitbRTqhx-e-d1vqw-1UM_gZhs-Msc2EvbxR06XHZ4miS4URFnfvT5ZaLeSU9ZFUtBeTkH-39MLTcmIMjkAL0elJhlKIWfMVb5P5YHrsols2kabM_bKI83dlmTqJ1Fhr-1RUaff6GmedngaQuprxO2kB0jOPDnOi6y7JKVpO5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=jnkgRemSzGOR0GZo404kxFwwJCJA32F_lOEtsJ75UoGZ22Q-NUkIJPIGnVNOnyWEjzNXALi-1RZLDZpBrHlyJDDm-OfG-YoZ5mutaaLBdujeiTds4tEOmeyjcHcjK-6gbxYvcIi-eL1bmhsKzHlWbSyOvxAZxiZaHZWm6ln2ZtQgFitbRTqhx-e-d1vqw-1UM_gZhs-Msc2EvbxR06XHZ4miS4URFnfvT5ZaLeSU9ZFUtBeTkH-39MLTcmIMjkAL0elJhlKIWfMVb5P5YHrsols2kabM_bKI83dlmTqJ1Fhr-1RUaff6GmedngaQuprxO2kB0jOPDnOi6y7JKVpO5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=vC1wLJNOxhjJuBwGMEgsNv0yavOYTPxNBV5O8XgCi_jWbiGIfmOpWTMqmIkdTtb5dw0VQ5rxqR77CH3rvJL3reKISFY3IN4eG4DtgKHQVUkk1y6RjIGj4VQljf9bPH_Lg9imElBZASUmYbbZMzvDEmlnAG0C9Y7u_2iOBcpocRnzatZWH_o5BgR2MITAs5tGbPRjwLl9ohtL7Nf5LxwaClPcHI3MUdiFgcR0iniinl3yCMhfM7NecFRi8tqIs0d4MxxsIzdLbHI9rA-2aOzqnXFBhtxwi69Oy55EDDF_cOqoxgsXaDig7RvSDv-VycX80LzSDJCMjmbC_w53lhlgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=vC1wLJNOxhjJuBwGMEgsNv0yavOYTPxNBV5O8XgCi_jWbiGIfmOpWTMqmIkdTtb5dw0VQ5rxqR77CH3rvJL3reKISFY3IN4eG4DtgKHQVUkk1y6RjIGj4VQljf9bPH_Lg9imElBZASUmYbbZMzvDEmlnAG0C9Y7u_2iOBcpocRnzatZWH_o5BgR2MITAs5tGbPRjwLl9ohtL7Nf5LxwaClPcHI3MUdiFgcR0iniinl3yCMhfM7NecFRi8tqIs0d4MxxsIzdLbHI9rA-2aOzqnXFBhtxwi69Oy55EDDF_cOqoxgsXaDig7RvSDv-VycX80LzSDJCMjmbC_w53lhlgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ow6uw2m0SIjfxrU48YGOkRseOwt58eS06ThF1RBofcpDl2MasSrO0WWNRisXhU8rmX0HXmuPVm8jMjVXg8xNmHPPAmSIcxAN4TKaOQgO_y_OPsFUK-i8H3xlXOeUXCy7Srj64TnyzSbSHYyOUh7_oBI8nzx964ErmDTvWgavLwGS55W0aPDH41RPZkUrIACsWstb54nK4_r4zIaFn8Sofu_eXJz6h5XIfhK86p1Ge5GelqXVneCc69si7_JPJW8I9WtWB_qwKMCTR5l6fjuznZWLe9PCUwMvOxxsixhiqKpFpIBLIvcdiN6Ov0dRygODV5YoS84PlDA8uFggIHAdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=ow6uw2m0SIjfxrU48YGOkRseOwt58eS06ThF1RBofcpDl2MasSrO0WWNRisXhU8rmX0HXmuPVm8jMjVXg8xNmHPPAmSIcxAN4TKaOQgO_y_OPsFUK-i8H3xlXOeUXCy7Srj64TnyzSbSHYyOUh7_oBI8nzx964ErmDTvWgavLwGS55W0aPDH41RPZkUrIACsWstb54nK4_r4zIaFn8Sofu_eXJz6h5XIfhK86p1Ge5GelqXVneCc69si7_JPJW8I9WtWB_qwKMCTR5l6fjuznZWLe9PCUwMvOxxsixhiqKpFpIBLIvcdiN6Ov0dRygODV5YoS84PlDA8uFggIHAdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Y-wqnUx-Eu-3TEmHfpGz_UWB_7JRdZZRjKc7odYJwtItQXbdbqLjSIOg6bVAVIFIWFIn6oMXjZeFlXAfAetJwJbySDngV76YYzXYdcQlwI0f6JMVSTS_Hzmvjasr34uD_2c_omkfBFIx6O8bZQuat2aGeQLx9xcu4gZvOm91p788METMggzp_nnnVOZy0uM8ixvXlXQQq5oBXUBtrrFAKzj5-TZjwrmyA1xc1-Preup4MurZ_yZrq-otrIGe4k5gRY4aataDj65x-ERlF4jjo8B3F91mdokg_G369MlDqZ4U6LMPYpVWtTljbyXR1uCW5QZMlWY2DUiwpeHVFRSrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=Y-wqnUx-Eu-3TEmHfpGz_UWB_7JRdZZRjKc7odYJwtItQXbdbqLjSIOg6bVAVIFIWFIn6oMXjZeFlXAfAetJwJbySDngV76YYzXYdcQlwI0f6JMVSTS_Hzmvjasr34uD_2c_omkfBFIx6O8bZQuat2aGeQLx9xcu4gZvOm91p788METMggzp_nnnVOZy0uM8ixvXlXQQq5oBXUBtrrFAKzj5-TZjwrmyA1xc1-Preup4MurZ_yZrq-otrIGe4k5gRY4aataDj65x-ERlF4jjo8B3F91mdokg_G369MlDqZ4U6LMPYpVWtTljbyXR1uCW5QZMlWY2DUiwpeHVFRSrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVo-3bSsrEfhmpX2QELUqEKG2F5SN8QC3fdMn_wgQ2VRRzrXcePsfB61SRupeecdaaA9k__O4avDf4AC1-q4ZAek-rsROGhlCee4tGPAi610EzJucYdpwkIjyZyXnTZzh1gfS3AOAJHcmAKjV3rI86HIDZSxsrR-ZxW6PSmUtkyvjyxnrghOulj0ZLOT0CjKA6vaNjbx7NpIK3RZ9yeVKTDKYOsTTuD4-VISvf-XJXJ1EKX4vJOccRYNNRc5dq9L9lma1T2pY7QMSoNPGVAWa0v8U3zkrjhjLm4j6B9U-kohionFh0AYM3gIdVd9-adQkTIURdkE46xXEVidxEjCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=P2zpGDoj_Kt2DduUJbyMfLyrJKVHRQA9A8rUQOn25xj7V4n9iWZ22Y-a1CIhd0pxZinBhpCkn880O8EGaT-p5aAHFPT5PtJp8uePK0NFbaIE_ys6zWKjdoNbdPzGejnqY699r9_wcISs-Kb4W3PsXBfHHVJFo_gXXfgTlwVM-8Kj1LoPcIXIAd17ySwK-FsxNxF8quNgx6NbEU0QbTdrRDdYU37G83RZVCWFlutZYRhV55_iubd2GNvYWgvGYOQyns3rpe_1lSSthgCJlIqkHfmrVvsvnBceteYUOouq9yMvtulyGv0DuUxKfcA54evtBzyv36iQwr9H5Pt-YnCvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=P2zpGDoj_Kt2DduUJbyMfLyrJKVHRQA9A8rUQOn25xj7V4n9iWZ22Y-a1CIhd0pxZinBhpCkn880O8EGaT-p5aAHFPT5PtJp8uePK0NFbaIE_ys6zWKjdoNbdPzGejnqY699r9_wcISs-Kb4W3PsXBfHHVJFo_gXXfgTlwVM-8Kj1LoPcIXIAd17ySwK-FsxNxF8quNgx6NbEU0QbTdrRDdYU37G83RZVCWFlutZYRhV55_iubd2GNvYWgvGYOQyns3rpe_1lSSthgCJlIqkHfmrVvsvnBceteYUOouq9yMvtulyGv0DuUxKfcA54evtBzyv36iQwr9H5Pt-YnCvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=BgcYJ-qnxO49SkPeAgnUKvldamN749OD9oPE_b-bCSrA4OKQJE2fh09gF1J3MkiKmL0Gl_DzC39DtLcIKYbcjMVNE3MGt5G8WFA10G56eraau3ihWhOmtNv-uRq1r7MG2Jffo7GZCIVBA0f-2M0BcVb98uU1pm3eiPLeD1WoG_8TfUrL0dmuZwH1HKvVTjbzZjZoUDBjing_9ykKNrjokW37zojmpOigQDK-Du8s0Je_qhABm1N5Rzvycc6sAa0gxCguKVIybnaZqot467nSlw5ox9hY22ecmHvY7XcTZztZxOgt7NRI2WdhqhyuGOxvklkhjAbGAahz1qXv_47wAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=BgcYJ-qnxO49SkPeAgnUKvldamN749OD9oPE_b-bCSrA4OKQJE2fh09gF1J3MkiKmL0Gl_DzC39DtLcIKYbcjMVNE3MGt5G8WFA10G56eraau3ihWhOmtNv-uRq1r7MG2Jffo7GZCIVBA0f-2M0BcVb98uU1pm3eiPLeD1WoG_8TfUrL0dmuZwH1HKvVTjbzZjZoUDBjing_9ykKNrjokW37zojmpOigQDK-Du8s0Je_qhABm1N5Rzvycc6sAa0gxCguKVIybnaZqot467nSlw5ox9hY22ecmHvY7XcTZztZxOgt7NRI2WdhqhyuGOxvklkhjAbGAahz1qXv_47wAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VzAwJXzeB-HRbK2neEet0RDXririyhcCqf_tprPjDZBn49gpGbQrcZiC-eKKTO_NFFPp5CDObJ3PMJU1v2jbn4_W4WuC6Dh6Tuc_rC98Z82vWkbRGn0q2TliEHjL0LNKbI8MnrLmltjldl9d8tjEi7SMTM8anCtnuF8CKAIVuxlVoq30O_8WO5QeUkrhun5A_gE3_8GFTCmjlnbQa1kDU5ZjjhVcBL3rfepcFJUH5F5kXEtaGbf91P0oAvoYhKAeKy7vX8L7ZGP0_2UnQPLxwyuH94uG5MD7MCtYr1FyOPKoofyF_aLqs6jjzU-zenTA3ushJBHXeCCXyOjjyxwzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qZ0CrqINm6DY61renYf0jupfZTAaFi13riIeKVENdHxnJrcdQr9wWNAx81YGHmcWONo574801ItPm2MEqL_WJhairMjp8Ga_xHuhldgyEoiE-WBERAsF7Oelb6RqnHUBStFpMNGtpW6GiRY8wx6JxFCEuzTxyMATw8Dz7kKgHnCVYaOD8T93IJb43TYuN9nYqflKcz8YAPP2Tq7yiHpkkfpxs9tWhsTqTUpd2CEVVBU7EF3V_k8pB-dPEbDgCLVNtKI208LyR21dxjhKJGn53hjlCoQJxEpBOayQqUdi__0jLqO37sN-HqhEQ4WZQkn6YAXeQ5H96QWpAYWeBwS0Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN6i9_z2CYZQMxULJ9LF4xYAhnFoKqxIQUmSyqhQliQVqexYxaSKTnQTN98MMAnBlVXTDHbedxg1y8B-uW-IOnA-WLsluRMpH4uxVJNWkdVWdMHhtbnFyoRI6dF0BQxWNUDFtceEg3Fo8fF60Gfq10I5LAb74B_QD4ob5WO8GtfFbVeDy7Cq1H6wR67gc2B67t2xonEq3FrYP5IFmTTFSDqQVAUiq2DLkwswaVfa4tSyIg8s9EKL-qK2h_A3ysJblgYFN3XCouryx00QhsacWw-vmd7tXX_62DJLouUxGpEKuvd4OxlEhFxQdYMfzGPiMG8dKr1ewTvAjG22K9mnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68043">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSUk3k5Jmtg4sT4fqcrTJ4_gtLqMbMFuf9_D3tqLOySyFJZE6pqP8KIGlfhXJqwkaHD8qYOAynOciheXEkwhCXUdgTghlrCKUQT1UyzHDrpY15Z3dRG9UxJa_hE18lTTOArx_O6Oatv2D8Tjydvk7wIsr5syl1F6rs0H93JMMXysNU43LhYDTQap0xBGRBPJKY07A051OJFQSgICjintvukVe-AhaCmn-7eUCmlCByWL2NnUtBPVrNYdy3HYj6n9Zi4Vmtj6nzH07sIR9ivwKyLroZaRCu_ZU_VXAkhDHTqmZ5BbXj5UOybi7HnnttwQ_tpOnJUzvZN8-Tuj_4jY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68043" target="_blank">📅 00:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=cKS0WpwcxPli8oksA-CyD67BvlbE0WseOxSohNZB6E0q-jaVbhwr6s-sdDIenDsVVy3zE582mc7p1_gV7q59giqUlAGjXl7N9_vzn0tJ7A_wFkJbfkb07bwiQ16BUNWsjJ6x-xTXzCrDxeiCrcYLlDtAuWeIxX2aKTvyKvhdiWfZnif5FmOc8HcZNyueoH-S9myt2xd1AAH2Cwe1c9cfwkFVeaT0OPE4HCPg_bY5fvr4-mUeMgSnTuxackb1TwjeSrLm3fryQAp8lSB_8oBOo-jC4ulkht66i3b_kenCRv9NuQ5R33VdhnolxIxhlyw1BFdh162VQPAr-Nk3Pesl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=cKS0WpwcxPli8oksA-CyD67BvlbE0WseOxSohNZB6E0q-jaVbhwr6s-sdDIenDsVVy3zE582mc7p1_gV7q59giqUlAGjXl7N9_vzn0tJ7A_wFkJbfkb07bwiQ16BUNWsjJ6x-xTXzCrDxeiCrcYLlDtAuWeIxX2aKTvyKvhdiWfZnif5FmOc8HcZNyueoH-S9myt2xd1AAH2Cwe1c9cfwkFVeaT0OPE4HCPg_bY5fvr4-mUeMgSnTuxackb1TwjeSrLm3fryQAp8lSB_8oBOo-jC4ulkht66i3b_kenCRv9NuQ5R33VdhnolxIxhlyw1BFdh162VQPAr-Nk3Pesl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
منتسب به سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68042" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68041">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
انفجار ها در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68041" target="_blank">📅 00:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68040">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
تپه الله اکبر زدن بندرعباس ایستگاه رادیویی
گزارش ممبرای چنل
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68040" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68039">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
چندین انفجار در کیش
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68039" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68038">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68038" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk32StpwMzov9H18AqZfVMm-2g2fop3deH5H6eK4tFbHcWoXekKACCBy5ynIbHuc7GDCmDVyVVqvs8tL_zFXxKm-ULlMdLAdYboi7fDCIfu95ud1haTXHDjYqNTJMDeleR3jo87ftMPVWA6ZTTGczR6oRJ-KqolP7OWOsPXC5tPNDeUDCHmsA8U0dmTY6OgAmKnhAPer8BxK46CZzfs14j4GQcK3kJpzP2z_1Lqnx7fefMtoC9PiueSJ1ehycnmXGd_jiOYSjHTaMb7-H6NCQXpQxHnHL-In5_Q9lfhZvPkEWBlRnYhOABwGDMMLJhhgO_3pdUvI20y2t6BucqZUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرقی، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل، سومین شبِ پیاپی حملات علیه ایران را آغاز کرد. این حملات همچنان هزینه‌های سنگینی را بر نیروهای ایرانی تحمیل کرده و توانایی آن‌ها را برای حمله به غیرنظامیان بی‌گناه و کشتی‌های تجاری در تنگه هرمز تضعیف خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68037" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های اولیه از وقوع دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68036" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=jl8Mf8A4DFR7uB4gt7dEG28F5LBbXDHwk50YyhvLt4pgtRwLpCVxYF1BRpsayPbP8LTOZqYgkbbEadToJQNsBpLCQVzR79D4J-EpSjP67S-293_JGNDIGdz8WJk9CCKn9KjakD3T2XMBa2-JJkfFUrXkbZkaq56QXj92wVaoGrS_sKZ4HlOaUsZKhAkunZ5SISPYwli_2F7E4E91upsQXWmYKKhSbgKDSIGIBigEvvtKzqpsvfUWvLlCcqHe28ariB_qq_kswvkd2pq6e_ojHaPEmIpCj_hlwd677s1AGNiT6ckfgFFTWH9ruhnE4f6f0hxztIi0y5d_Yfzc0iuDnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=jl8Mf8A4DFR7uB4gt7dEG28F5LBbXDHwk50YyhvLt4pgtRwLpCVxYF1BRpsayPbP8LTOZqYgkbbEadToJQNsBpLCQVzR79D4J-EpSjP67S-293_JGNDIGdz8WJk9CCKn9KjakD3T2XMBa2-JJkfFUrXkbZkaq56QXj92wVaoGrS_sKZ4HlOaUsZKhAkunZ5SISPYwli_2F7E4E91upsQXWmYKKhSbgKDSIGIBigEvvtKzqpsvfUWvLlCcqHe28ariB_qq_kswvkd2pq6e_ojHaPEmIpCj_hlwd677s1AGNiT6ckfgFFTWH9ruhnE4f6f0hxztIi0y5d_Yfzc0iuDnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=jwYbD_0p9_lybWB1BMEUTB0N91R6fL3m6wFN0U0X3JA8rr-2T0Q4RGuE_mVXzDbTAn8RE1V0UpnG8-M4cDXpcf0FyvB-Q9FqMaIUN-lSro8B1Le32eT1ORWbnFmAMpptd7ZUleHhSCkR4h2ka7k3jW3bq0AqgMFOkzO8C2A02MW7JxApedXSe94Fu23-Wo455kWty5b-RW3RjzJ9OtObf6ruShWCjsQgIcIlduuKAqAw34quA3RYjT3ttUCRCNTvk0QJhJGTlVIraRlvldMOMMAuNqkZoLycfwc1uh6tk4XyCXQeRRKGScgVimo7N9t5F4URn1wRjNJyxdoyAN46IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=jwYbD_0p9_lybWB1BMEUTB0N91R6fL3m6wFN0U0X3JA8rr-2T0Q4RGuE_mVXzDbTAn8RE1V0UpnG8-M4cDXpcf0FyvB-Q9FqMaIUN-lSro8B1Le32eT1ORWbnFmAMpptd7ZUleHhSCkR4h2ka7k3jW3bq0AqgMFOkzO8C2A02MW7JxApedXSe94Fu23-Wo455kWty5b-RW3RjzJ9OtObf6ruShWCjsQgIcIlduuKAqAw34quA3RYjT3ttUCRCNTvk0QJhJGTlVIraRlvldMOMMAuNqkZoLycfwc1uh6tk4XyCXQeRRKGScgVimo7N9t5F4URn1wRjNJyxdoyAN46IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOYKACcod7Y9qhhAPwSsob_-bqb1PV82tzpr2qyR99NjpJDei5kdknVeQ0PfITpJ7FMVnVIWBErlls68yTuQMt0gHr-fN7867s8y9Xq6XMW9EvVJETopvJ6S8Non38hAZWm7XoNll9Yoh7tiZBezT7FDvhx5b0rTcSO1s83my7rGgIIU6ttTn7ajzQl87QetsXbRfBB79y6vT5eQY64Mh-bCVS_dxAo0BBt0YfpN9kGOT4Xk8Wf3ATDZnrWuy4F-vtbWd5zEqglH1Q5BhVfiq5fGgoONhxcZOBiY8NZZlnv9_Y1ccd1zjhKf9O3IPYGm_nggY0SMwxBC8kqHrY9615BI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=C8QmxBTNN9voCifJFwgVMgP1TcspvmBoDU0O0DB4oFdLro8E9AW1FPlb7wMAolWtIvgw9bGAAUi7N0u3lap_1jAsqZ94V0JgTMxt_cTLNtN9tXT1Yz-Ti93WgBLYcM7u0KKLiKuiL17brXLfxg_MUuesTHsOA-aGVqeUIfK1fOcDNfMvqR4G3MMa5EeZWfjurZlFEzuvv9ue5cCyMkdiu8HPHD9v2GfmQJ4Cw0SVRev_-x2E6wwS9uimplvfXAUSd427r8t8Mb8HPeHm7RVfnMQZl3fVjTL0TABCg_XWd3z76w6OJdMqw3nNyyMHTBnXARlikVQtIM6PLrV7tJkHOYKACcod7Y9qhhAPwSsob_-bqb1PV82tzpr2qyR99NjpJDei5kdknVeQ0PfITpJ7FMVnVIWBErlls68yTuQMt0gHr-fN7867s8y9Xq6XMW9EvVJETopvJ6S8Non38hAZWm7XoNll9Yoh7tiZBezT7FDvhx5b0rTcSO1s83my7rGgIIU6ttTn7ajzQl87QetsXbRfBB79y6vT5eQY64Mh-bCVS_dxAo0BBt0YfpN9kGOT4Xk8Wf3ATDZnrWuy4F-vtbWd5zEqglH1Q5BhVfiq5fGgoONhxcZOBiY8NZZlnv9_Y1ccd1zjhKf9O3IPYGm_nggY0SMwxBC8kqHrY9615BI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=s6wh7Ujcu6xLlT4tA4gNHXAXvmqdcifC1ph00rnaVB-v4c6UXBGvVhtVAl788BYa7xmKXRyZvIprV77g6xDRxdt-oDF_bPuzYj2ME-bpr3DV0wdm8Q19ylSzKWvPFwvK4VNQvg-sPW50e2llmIRqSabpNs5Y78D37Hh1Ner1rEIqhzlx1qao0b9SeTPsONyErAYi-WghDZUBpDn7-UXpNpDoCvwJsDEyHhA7L5aG3AFTrpKYaf_vN4qkTfv1ZLO55EAyYOFmq_Ams2sKifVBPsCPEbBMGpZhYM_w1RBo4S1EI0otSi29P87r9X7omoEOanC1ngf2_ljDq-00KCISJEkWRLCF5-bZ7c_V0YMMbVv8ACfdUFhm55hx6tpTunOJUftStxEx_HCWTSr9Mpc8CWK6Inhozn1uFlKm-v-w_pny5oJO8RdAe7sYFU_WhmzAhw0Ny6o5-Mb85CtU_MYVYz-WIEI3RJHykDrQMt9Q6vyr9HDpDpNa92sVH5_JB4d0pCNm6ldiH0m_SJ2xHlA15rmL-4rzjtFFxKNgMuBoPATu3Fk43CDpN8eNeMDVwxE5yd-EDPiNu4-vkRRDeiCqxvQ5VAJPeNIx2IMzO-bpdQvaIkSsu_G4z-H8U91LZQv_nTWUkcOwYyyw40EVXIszPE9aM45yyj10yw5gs6FhbL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=s6wh7Ujcu6xLlT4tA4gNHXAXvmqdcifC1ph00rnaVB-v4c6UXBGvVhtVAl788BYa7xmKXRyZvIprV77g6xDRxdt-oDF_bPuzYj2ME-bpr3DV0wdm8Q19ylSzKWvPFwvK4VNQvg-sPW50e2llmIRqSabpNs5Y78D37Hh1Ner1rEIqhzlx1qao0b9SeTPsONyErAYi-WghDZUBpDn7-UXpNpDoCvwJsDEyHhA7L5aG3AFTrpKYaf_vN4qkTfv1ZLO55EAyYOFmq_Ams2sKifVBPsCPEbBMGpZhYM_w1RBo4S1EI0otSi29P87r9X7omoEOanC1ngf2_ljDq-00KCISJEkWRLCF5-bZ7c_V0YMMbVv8ACfdUFhm55hx6tpTunOJUftStxEx_HCWTSr9Mpc8CWK6Inhozn1uFlKm-v-w_pny5oJO8RdAe7sYFU_WhmzAhw0Ny6o5-Mb85CtU_MYVYz-WIEI3RJHykDrQMt9Q6vyr9HDpDpNa92sVH5_JB4d0pCNm6ldiH0m_SJ2xHlA15rmL-4rzjtFFxKNgMuBoPATu3Fk43CDpN8eNeMDVwxE5yd-EDPiNu4-vkRRDeiCqxvQ5VAJPeNIx2IMzO-bpdQvaIkSsu_G4z-H8U91LZQv_nTWUkcOwYyyw40EVXIszPE9aM45yyj10yw5gs6FhbL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«آیا الان وقتشه که مردم ایران دوباره به خیابون‌ها بیان؟»
🔴
ترامپ:
«نه، اونا نمی‌تونن این کار رو بکنن. چون سلاحی ندارن و فعلا وقت قیام نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68028" target="_blank">📅 00:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68027">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=q3U1gEefihUlmSZrCAXBvz922vUwMIqwVjoSvuAmDz4-LL4fjKEzOY7tz1ecrjKFymxnJUNh05YwfJHZqwicM0Nc0WDeXfRQrBdMB0QrA9hjjLyPqegOMqRB1_yfVkCNkSy0jVT5oFI_6DCeCIOmKWj1MaciLU8yA0k__FotZ404Sg0ZeyYElX9u8IVcYK2Kbyh0CFpE5G5y3mtpm6omohWXL_4h0T0IyDOoj4aftRG9vjgXMlN4L4kQ4D7FlZ0Ns-sopIyM-uR93jzN9e-x9dw-tHBE_p0spmmUWvJrENPWH4clvql12gjRT4BuykO14fbENBtrV0i72m9aJiHeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=q3U1gEefihUlmSZrCAXBvz922vUwMIqwVjoSvuAmDz4-LL4fjKEzOY7tz1ecrjKFymxnJUNh05YwfJHZqwicM0Nc0WDeXfRQrBdMB0QrA9hjjLyPqegOMqRB1_yfVkCNkSy0jVT5oFI_6DCeCIOmKWj1MaciLU8yA0k__FotZ404Sg0ZeyYElX9u8IVcYK2Kbyh0CFpE5G5y3mtpm6omohWXL_4h0T0IyDOoj4aftRG9vjgXMlN4L4kQ4D7FlZ0Ns-sopIyM-uR93jzN9e-x9dw-tHBE_p0spmmUWvJrENPWH4clvql12gjRT4BuykO14fbENBtrV0i72m9aJiHeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند تا از حامیان حکومت توی آلمان تجمع کرده بودن که یکی از مخالفان حکومت اینطوری یکیشون رو سورپرایز کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68027" target="_blank">📅 00:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=ZimcLd6M7-xYU3mvcDq0vqaZ9O9dGk8BnlnysPXTqHwZPJYAFR0YfOUq6vG_TLsZncLp-B1JlSathxu3BDnI8VQ8eaaTK54z4GlAOiu_WA8LlVzxwQOoerinvzBV4PbgNu3fV-dxFddXZvn3kNOI9UPkpUCERHPPitxevp7Z6qM8zCfGardASqVMl8-IeHMNpbWBeWjEz_ALv-VisJ3pkkhO_ryC35y5gah4I3U4kBteMr1-UKOiHy6o60YLwlT2zx5e93ZXr2uxmkmylEWwEjpD28drpCXaLUxIhGG8vXtJMuNlweV4JzrVZSwlgZ_fEHMjgTaeeY0jufwE7gGnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=ZimcLd6M7-xYU3mvcDq0vqaZ9O9dGk8BnlnysPXTqHwZPJYAFR0YfOUq6vG_TLsZncLp-B1JlSathxu3BDnI8VQ8eaaTK54z4GlAOiu_WA8LlVzxwQOoerinvzBV4PbgNu3fV-dxFddXZvn3kNOI9UPkpUCERHPPitxevp7Z6qM8zCfGardASqVMl8-IeHMNpbWBeWjEz_ALv-VisJ3pkkhO_ryC35y5gah4I3U4kBteMr1-UKOiHy6o60YLwlT2zx5e93ZXr2uxmkmylEWwEjpD28drpCXaLUxIhGG8vXtJMuNlweV4JzrVZSwlgZ_fEHMjgTaeeY0jufwE7gGnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکم بالاترو نشونه بگیر املاکیِ پدراشتراکی، بیچاره جنوبیا خسته شدن #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68024" target="_blank">📅 23:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:   امشب و فردا با قدرت به ایران ضربه خواهیم زد  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68022" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
یاداشت تفاهم با ایران یک آزمایش بود و آنها به آن پایبند نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68021" target="_blank">📅 23:52 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

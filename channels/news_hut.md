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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 159K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVi4uW7x6J6g69-LaYnhYQa12tUpi6VdUwpQSAm7RIdXzMmQTANKOs_M8C2HMq5WQudL3A6q9_J3PPSyP0HMTc3fTdNRYNZW9YRbQagNR5wRDnLWpelKJ6btkYMKAKvdl3AhCNasXghonyZZwED-zJQtG6Dk6-XDJSIU9RyKa-hJM8hmzHQZKteQSFW3Hp0QRdG3DRD4Q24kW0uma886p49bXbxEJaY-EI2NC7nLDP7N7D6n8icGkpBAyVNlPSruWCt6JHZn8W71zMCWjRTnHBJY9PKwUL5YTt5Vm6Si1s2iDCrXFP7WhIe5nyh9wWNLt9V7N2Xiejpk6G_rPliiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU2mQgwPPpyeadnPaC7b8QjEsJbE4SGsgk0pZCAmweuXdJvWlpoQZ431_lHBc7ei8xTtVnHPtaNo7xF6OvPtkCHPyGGdSG5hm9SebhwDYphxyHp-lV1iKwr97AfBIW7v32EL8gGfPMFBb18JPUb7sD0uqeGX7SKCjHAYqFsxWSWCOa7h-VFWstCDzzlswvLKhm6PSyn5p9t_n3rWbpbvmHd3GEZfaC5N5LVeMd4RHb8OPJUD59uUFNpPjSgiBwElPRTfclFj60RbXKSf8DDarVo8uXH7YyqMLqHaAntbFYswAwHhsX0e5ZZn-s8enOeyccNsDFx1lY3ObPAeRRCSwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGZloMVydgeS1So-w3InX_MysJTwgdgj5ihXKaxRsL-muESgz-cffLjSkX_l4uID85gYwl7FGAe-Y485YbKrRySb9BoR-h2w4QoLOQsZj72PIUXuvSGRetyZphq44OMaDH12d5fDLvkFbhCEXvfVJC-quevNA4g65viNrY4klUl48Dtq_qQ_4LkQEfL082KskGlEPU4tGYCsxMljY0LwthvkPzp-ynQM1RAVQGFiI7infu7k2ATXgxui0SdLccqXjugaBcLGf8XNlDhPchhv120CYIJzgqCZHsO0wvlII-keBeWEiiFA0isffYJdwXe0eeyhJ1kvHfFYkIjwqGlThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deY1RE5tE3R9RUCd_2JlCn2BYFJkoyO8zv2uWCZleWPmY7Fc3Yg7WewL60DmFhGMzplTm7dr_zVjqBXDwmiGaAv2MZNNMX5DjH7afAzrcJBFE5uicbef2mrWJgCagI3HOHpAbxYkwA_uCcerRmSZMLR0T1ZHNE5NuWA5VUb7OZx3Km2kg-Xwa9ozevewGS_ZeYoI7c-chotKps6Xl7g8MfOu2OoztwQ0_TS98fB7uZwIzSYnor_Ji1LRup-aAreOdbmMH95ddBFpxH5lRAs6ry24wgqIC-j8FPPnzV2FMF0XRBTTt_u9nTMPsQFU-1pSLMelLB5_Rc_SyjuK2-QotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=cDFUJmhgb7PP-WlQsMBQkuF_dN5cAkpEeuHCM1jkXVprq3gvzzMHm-SU6B2ETmW-yD9BHi_kM0a4DtSRiLOMmsaY_xaQpZtfQbFiA2VyMpPmsXhU0I7gzA7Z3qH0bWyuXwjWQE-rcD4D_YejMrXQLzzMHPblWApz8TNzZQmu7_IFtk6qdagKeVBEV4pp1pV4GEygndIIdwFe4eTqNtvzCeoOlrhAaUf9Q9Q4Ygq6nc6C7GYByCsR3O_jWwaJ0xNssT_udFPRC4_0sVuMN2RdCYiDtTFhqUHD0MrtgHGfc7i75RWr2sDhg6zbXwHp3dBlJnfJOs6RJ0ZFvbkIwijkDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=cDFUJmhgb7PP-WlQsMBQkuF_dN5cAkpEeuHCM1jkXVprq3gvzzMHm-SU6B2ETmW-yD9BHi_kM0a4DtSRiLOMmsaY_xaQpZtfQbFiA2VyMpPmsXhU0I7gzA7Z3qH0bWyuXwjWQE-rcD4D_YejMrXQLzzMHPblWApz8TNzZQmu7_IFtk6qdagKeVBEV4pp1pV4GEygndIIdwFe4eTqNtvzCeoOlrhAaUf9Q9Q4Ygq6nc6C7GYByCsR3O_jWwaJ0xNssT_udFPRC4_0sVuMN2RdCYiDtTFhqUHD0MrtgHGfc7i75RWr2sDhg6zbXwHp3dBlJnfJOs6RJ0ZFvbkIwijkDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moLAL9oX-HDi9VCCviAIcrc2-4hroaRt-1IcibVueJEOAofvjThjRp2IcmU0fNWXoRW8xJf7VTv8OajN_leZA9kbIn2Db_GmiaSrhI7ZCOhjzvVhoYA3Kcng8bteTDinRQ9elRoed0FtPTX895Xjp0LdiDuLdvA8kwa9F9MoXj79qPUC2wwJJZ5KpYrcfOI5OMsLX5oE-G-6dTBRK3OHK7Xr7p7EHi5g1WgftEkRDFTp9xvhddfhoXgxvJ5RvQBRvWLMbeaBABLV6E0EpaHtksaPdaFUH0HKdf1mVezgEdPXZNwIlXoOD-NnZphAT7OFA-clHmL0dpWVQS3VhCw24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=D1jCk1eKupNpGgOJJy0J4urr9YK9mGGwxxRUXL9UTWBFQTxNdl-HXgNwlibOPYeiRG2uV9dIj4uFDQthWbbgTZIiBEvNReZPzJqVM_UaCZ9by1Qa25GzRdK-KmDL7jT2W_TX6rHeYcMpiZ04kE9EgrOFY8tNFrgBYlepUxO5WcWqfEEwUdgAi4mu_JUTPsT6WEhO8xb5aBW57FiDUK6_xByw1JMF0dkNKT79sxI7Dts8fo1FQZbKzEIpcotGSLYfit5cFkEiHK1WnierfgvBwscA9J6HXeyeSnVFy1rJHnD0OSX570MVq7w98sstfixIx9xJEPecjHIlA8s3ByiC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=D1jCk1eKupNpGgOJJy0J4urr9YK9mGGwxxRUXL9UTWBFQTxNdl-HXgNwlibOPYeiRG2uV9dIj4uFDQthWbbgTZIiBEvNReZPzJqVM_UaCZ9by1Qa25GzRdK-KmDL7jT2W_TX6rHeYcMpiZ04kE9EgrOFY8tNFrgBYlepUxO5WcWqfEEwUdgAi4mu_JUTPsT6WEhO8xb5aBW57FiDUK6_xByw1JMF0dkNKT79sxI7Dts8fo1FQZbKzEIpcotGSLYfit5cFkEiHK1WnierfgvBwscA9J6HXeyeSnVFy1rJHnD0OSX570MVq7w98sstfixIx9xJEPecjHIlA8s3ByiC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1IJIfv4igKs_IkHOGV4Hmle3P9AY0Ck6vNMUiZbKmXETfn03NnEaU3iNL85p-6mG1rCsRTISdKouDhXt5bxW9TxFMH61RAJtAH29vN3c-Ul2mB-4k3RC0BvFGKGkxL6Th9-ZYjL9lqxkhCq9IK7qoGiucM4pQv9t9-Mt1fJpMavMjHwMTbJ4UKuDnsTMImBJVPLJDlu_aWLTgLuJR7HyB-i20Znj5pd-A44G3Qokq4jbjXU8cIq48XJOaqkxDieytXyZrktvSEXZNS7dAiecsmB8uxrBBJh8KV1ThaOyJD7bcYMBX4r2S-28QvjgSMXqU1BnzlEW_1lVVkKxfLI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=j_fFSiqMQMlF888PNzQqva_JMXXBimPzA7uC-kezShHSh3Nth8AGTydrBtQHUy_hobu0V3IECOdXUvXRk21hOaR7pC5dBRoBRFu-HI8MdA5oN-Sm2kxyIpqJUMtMgVvqlEiE6snuCHSlugToi3KzIuD1_U3rjQVbvPDLwEeLsqin2nVfxNUyOk6mGPWIBgpLhRZ1N1Tq-crkEKUgzuBedR68keVEmoHUHxZD6UQDKUVpI50m4uXle3V_ViIumullHwixHX1GshV7cN_k-QhsBtTDLBT9fHChfgkOmUjox_NXSWnM1LJ_gLt10THIIjDFgRWn2u4_R1Gme_Jn0Lw-1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=j_fFSiqMQMlF888PNzQqva_JMXXBimPzA7uC-kezShHSh3Nth8AGTydrBtQHUy_hobu0V3IECOdXUvXRk21hOaR7pC5dBRoBRFu-HI8MdA5oN-Sm2kxyIpqJUMtMgVvqlEiE6snuCHSlugToi3KzIuD1_U3rjQVbvPDLwEeLsqin2nVfxNUyOk6mGPWIBgpLhRZ1N1Tq-crkEKUgzuBedR68keVEmoHUHxZD6UQDKUVpI50m4uXle3V_ViIumullHwixHX1GshV7cN_k-QhsBtTDLBT9fHChfgkOmUjox_NXSWnM1LJ_gLt10THIIjDFgRWn2u4_R1Gme_Jn0Lw-1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=U3fnmbv0ok2wTWK0NQF9ancgXuzOz89knHpcgprrnK_kk-o4cRJL_9Fdv7V63Qm3XzJnfOeuWshCb1o5dVpTzmRTgmRvN1pSb15MjxPRDyfAwd22mR5GXOMoEsretn5wKSoFqe9hmIHsPaEXqQF1_tl0TWyHLQJ4khJTs_Ai07BOLKUDDFhdepEEL6Ct_AK5PhgjOK6nXmvOfrdso4oh5ejDxVTLiYa7oqDe46Gc4srBwOdoAzb17ssyGxvd3TYzeIm9nlumEWT8KWuce2LWgcYKS02vOLSo36zbeyCu7OE7PksUdGfw2HLs7Wkd7tVoczQcNwYquTUvm78QJ67I9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=U3fnmbv0ok2wTWK0NQF9ancgXuzOz89knHpcgprrnK_kk-o4cRJL_9Fdv7V63Qm3XzJnfOeuWshCb1o5dVpTzmRTgmRvN1pSb15MjxPRDyfAwd22mR5GXOMoEsretn5wKSoFqe9hmIHsPaEXqQF1_tl0TWyHLQJ4khJTs_Ai07BOLKUDDFhdepEEL6Ct_AK5PhgjOK6nXmvOfrdso4oh5ejDxVTLiYa7oqDe46Gc4srBwOdoAzb17ssyGxvd3TYzeIm9nlumEWT8KWuce2LWgcYKS02vOLSo36zbeyCu7OE7PksUdGfw2HLs7Wkd7tVoczQcNwYquTUvm78QJ67I9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=r659grr_NBcRFTKmBK3upLQSRedT3wlo89Ywu3Ev96zKrUEOfwpSiQTgwA9b44TBcoK5bYVcBm6wmar1pPbU5fE9BCDfl1dfhmZp7LThqG7rNIWE_dKbzcA-bp7se7AWENChiuFMMpIdVdX9PR9b9PqBBn6KsWKZeHaQWf7TERvTqw8yD1YpjHcp24Wf9A6BA2rTNO2IUcahgNOBnMP-WvjPkHymrgkzjdX_TQ3UpdP8j4CJjnwswrePAY8eSP1-Mtc3MStYWwmLFha54dc0VC7SSxMeQhuu4LmBRbqAtCv1l4gDoKES4DtDU6MHvruEJVFyRGn7kurjeNq0B1vtQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=r659grr_NBcRFTKmBK3upLQSRedT3wlo89Ywu3Ev96zKrUEOfwpSiQTgwA9b44TBcoK5bYVcBm6wmar1pPbU5fE9BCDfl1dfhmZp7LThqG7rNIWE_dKbzcA-bp7se7AWENChiuFMMpIdVdX9PR9b9PqBBn6KsWKZeHaQWf7TERvTqw8yD1YpjHcp24Wf9A6BA2rTNO2IUcahgNOBnMP-WvjPkHymrgkzjdX_TQ3UpdP8j4CJjnwswrePAY8eSP1-Mtc3MStYWwmLFha54dc0VC7SSxMeQhuu4LmBRbqAtCv1l4gDoKES4DtDU6MHvruEJVFyRGn7kurjeNq0B1vtQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDBxc1YV0waSAb3YqO6fC7RnSYBUSRwYiCyFb6g62P6BpybJ8IyEhNWuaM5akUxsI1udpmCuovB2y_vGAN43mR0k8Ay_DhnrhKLQlBi2aEdc82i8cWFFojY1gC74vCOGAI6myRONq1Pn6yfTvsU6adwFsD9Rp-Y1nUk2XjCPx6uxL_PRhmq5axkWO1KxFxYjOnUBahP2GYWceY-gfOySd2dnM7ua8g-N7kuVMZTtfCqp5ukyP-e8KsPh6GGVJjIGAlswm_Y1lHYxJFH3T4az9AjDX5_At_jnLRgFgH9Y5f8sJbwnUqR8nCswJeBLdj7qMDS30p_a-WOXKSiDfyAs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqDKaOPJQr7FAnwUN-gN5J_DYGbEWfGPQcOWWwblzzGZfXw9LwGPOq4J_MjJ4oQXeqHKuxT20b8PHZcSpDrdJTekewJ2SWYUKfTt10ZF54WEvAuOnHp1U7LRwhxAcjgFdxblfKxZSGcXEzb3mQVDcr_-9uXSt6ZBXJ6KoxK1pbx0FV8uXnnptx3ZOHs6SUTICyXHYIqLjy9-V8q9i0HS1uz5Q5hgRvWVL4qyb_zEB5HARZh_7DN1qwvCttxI2sMc8EQ7FuonI9QjKObyTSa3WxovmXQnJv21rkvQao7l4iubibDuO4fbF3ps_JT3JuInjexJ-h_-rwhcd-but_HslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaXC7OmrvgMXsvlKWbRdc1kiVgNRi_W4wfa_Qj7_IKvVs_eZey88BPDtUFGyYjCEdM0VpXnioSAjGOeL43XGnVNyxb7DKM61bi0cAV0Q6GILaFidZEZdMPs08DRh6fnd-bwfjOvgcRbD7uYZ4RPPqmDFK8yNKIVqpmSwPf_WYkjT1umvjWUGL-gUQp864kZZwazkH951lgA_dKPoZb9pnIMrR2qURCULAosOCvCahHwtznXztOEf_DcSw-J4BjT4vMfaJCBQ02FCG-f3SBJ9rsu-5h0HdkW4kGmEqq9BEEReVG5X_0R_HHA_-7fqJzIH6jRbWMUCQXjM9tiHBxivPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPRxR1fxo0Icm57grzU0YKiMLbF4_e_9StNqXMQTCN7SvGkd2asn_Ev_HG7mmWjGjIhBQBwXhk85BVGpoVV2ZYSCTVeACxgSbAHAHdo_MC2oETKyMPZgquExw-XFbVPMQbmvdhUXCYkj4hIiq7_6Mx4pFU2ehfBNfonlf4gtk0pJ3bUJoF0x209ajS5MlN3i2THjpmYrnEIQ40hOa7rlq4j2YMJnZltugrL4cGQcWcYfDpLVqsVVu98x70XB9O1ZjL4b4sAuTK-Ws3la3PUt80Oc14ZiG_F40gxQNhCjhD6UasF7egIDsYtrjczh-z_xAH6GZFe-AKEmZFKDHdvHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDHmdL2Ei3K605d0pRVm-GQCJGuLaxf4eh2mp5dS3i5o-ZNIGNkMKh95BxsFSmBSMAsWV5k1KgBgO5h4zE41rN3GH9OfZSfxIneEiczgUNv-Zu63YNy1znn3fGGinpYWEmVhM0zferaQpuOdrEpzlzA5yxZo2sbBjKmcwGDt7_nf8ZXaX53y-Kzp3PKY7faxzK6PALWKbg9Qi8_B7opONaRPonezCD4KtM8FWkOEEhSILlWt9BiD_rqRz98ofwK8mv_oOUBusF9qXhY1vvQzfkVC_1XbMO5Nr4LuRPb9YeHcgn8-6VxigO828qQXu8ZEolAKBusod-ZooErp99nXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9Dra8Toh7LmsuarwQfjmdMctK085qCZSVaXbh0ngKxzKtiGSLMwK8PCk8XLNZ7_soFBI_Tj-EVGFv5QCoDfTWJdayJrDIOB4t-m1CBL9CX9N_HJ-aoy4WYG8-ekDptpFGgXEcBe81bi9q1DAvH-qxyFINL0uhDjyKLrbnvcH-DSCGDsTnEjg_s8nnuUn8pov5lBxDh9G1JmcxbP7kTKpgEoGQpomDyperqrRR0yoflC7IUTl89msMkogagrGjfIDfcB_WI82H_NNcyFeCFf0W9RJx7F0p0oRWfFFzGh_FesBnBUFYwa2Y11H7xcHC_kmhHOaS58OCG6_rJ_j8WJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ4TkfU-BrkZlSTOxS1kOhzIyW28OMSL2WAn3rhQ92d_EYW8AUiw7YmlnISGBfWboPr3oMslv1gciFJDmrVfNzy7JjL68F4_nUbwCFtVzfHowN85pA0dg8iDAIJD0Uq6FzEQLPCbmdLu1HIxGmbf8tf3KF9i7tws5uZFMmeFzKh3ngo5apEOm-hRk7emI0aeJRN8oOBqEATm82ew097922oxm7r4C2W8YFxzguriUiWqh3g-oPaF76zDFnKU-27BweGQc6H_zpemfLVok1v3MiXs5Yy9V_uCXtcp9jcDWRk3lJLtLqVFb9Zpt0GYNjnx-X_Dou4KS0SDEVaRVYdztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=F5_qHuvTYwTWFtaselq2uyLX0eLySBKfoOhTN-lIFF4llxO5oS_2YiwNT1cew2qT43L06RBpaYW4aDujv9_2Ur08apTtYLapnLpWp5t4YDYhvLBGlFHu7zkT-ZGi6y1Max75DTwwnn_NCcHA4oeow8BvE2EsihQgCV44M9AP2Vd_JcS26k-IPMqbS1GhhMTJ-6CsqrbiLJRm3tK9nRay7jy7FauCxR1qAh0EFDIqQWfo77L6fEvDtqyVQxfLcbR5bX4ERiFoLCFFj1MJnS_6Ls1hwrCRQWyUEQUoh4PVOlqq_OfRmJICT4bT7FDST2E8Ioon__dwrMT29qSx0gJsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=F5_qHuvTYwTWFtaselq2uyLX0eLySBKfoOhTN-lIFF4llxO5oS_2YiwNT1cew2qT43L06RBpaYW4aDujv9_2Ur08apTtYLapnLpWp5t4YDYhvLBGlFHu7zkT-ZGi6y1Max75DTwwnn_NCcHA4oeow8BvE2EsihQgCV44M9AP2Vd_JcS26k-IPMqbS1GhhMTJ-6CsqrbiLJRm3tK9nRay7jy7FauCxR1qAh0EFDIqQWfo77L6fEvDtqyVQxfLcbR5bX4ERiFoLCFFj1MJnS_6Ls1hwrCRQWyUEQUoh4PVOlqq_OfRmJICT4bT7FDST2E8Ioon__dwrMT29qSx0gJsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOb5badZYncXb2Ww-TKJpfTw4gPgy7i9PXEs6zlBd35rKBW0h2N7Ys3BY5wjIX9ubkdZkGzbZklHv06QfsvvnP1OAz2TedF16Ju3Y6VsSZ2rUMUEk9kLs9nNzWDzi0Q6hmv74vYuq0mv6g7EEDWL0Va0bdMAbj8K2utFqDsyzxyHEe7ns021zH4mv-7eJ5O0aTpntt3p_e2TsBQK8m9-90Jhu3ynhQAcxaeBHSgHqrELuT3ULh2ygpyEMz68LHV49Q-4Wc-vGxBl9gB5nIlD4RJgQkifqVnUdQ0FJnlSDVNsji_h2sEkCUtM5a3O5WWomWTogEbDQaCJZ93I7vUSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esWc0ZdpjBhjOcDMTTnxVMfV6eUBRIncutmrcCwA_mLRWyMj32dN9Uy5ruLGzf26a0ZPoc2HTOD9E3j0JayK3E-wsLb_-IgL0POINWOrx6_T5it2OTK43oJVQ_8x9tt9FEiWL4BMcmhXp9dQ16GCcOQBh9rIYrq_5yVftfs_fP2EVIjHpOoEV0wsC1qkFdmc4rtXYIeChl5EgpoMr4iwXSGvPmXwh7LwW2KKkO6IqwsZ3uHlS8Usv8bR5OKiySFvxJz5vRj6vFvgRSArM3PG_UgX7yMev0M9YbjNIpdosWo7gcev5NTEILnIvga-ZNBoKi_LG8eoYzmamLVlZN3miA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu8PiutGI_EWrL9qktMIUsHWvgsUR5iKA83wwmd6MCfrl35YjST_gEUNrupTgq_qiHdxngzhRVyxICpyH23TMswafWdShJzlbC4DlcO5LfJVtVwXummZwIpIOLZE2DOpMBJlj7B0JQ3wVRKviXSw6PUFDtPIpz-krKXqCb1yCInbbKB8A51sPGJk-LYYQoWdXGzU-OPReWjfIH58lEWqDCVHcgRJYZRA0Rh3mepAeLVknObenDIkEGuFuDdY4A1qNnk5V7gZZS85ABNhqp1le96H2OwZGDJgxnIlTX7njwGnsmataCfciWDDv-rdaLtLSi3giWQ53HaRIhZDsD-IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HORjftrGlD7DFrymZEo7gbrqlebWJgYN0yxz6tdNIKgFY51bDXztpUgRtNgkvotoTy3bh5hPGuDfp6YxozGMrdBqptLDwkxi4dnKP_gKmPclC3PmUVOHT0RGkGNJXQJPaNqUb3psM-WcfqUhMvRn7yPyfUINYQTiR2QZ5eDfQ7sDy5v_Fa8_MOFVFCZc9vsoR70DU31IblLp2PORinDd0i3Ckp_yZMNij2Q3TKUgbEmdLhlEvY46iJ5wowMMRa7OMhu670KAlV5ctghYieLrjkU32KxZ0SIv3L33bQHYoSn4xT5cYE9cHwQ_MGuPzN7zvuwXwePW5c_TWfz-s0Acdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOlji2n3SSKvNu3IYu_K8yj0hhNWizLcV_8i28grm8tlB6Sgs7Rn21Mfak9CzcYlqVaskW-DTBUiTMze3LGu-uv4Zc31Co1bNYdbZ63W3LBxZ7br-_JENUEj-1vAQHzyDwKSJRiv6kLnGk1WoV6-GijLgpDMUTCfglGBLYAjT7f6xl_8Bm_lW-ervMFLgGeopgevamgA1lP_b4Tvk7g1gSuev9cNfzXGefa23EBhllkS2mtLYo44BTxek7pneT5wRwdix31ze0vwfZAnRlVjeEgEMV-2bsQGS8IcS2YmME1bjXPsXX768SJxNRDL5i8nAL8Wz7C9mMvHObxeLPiRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nup3XcAVs-cb_FEl4FHfV7rbkTE09WAxZIZFzQXvj2u2Vnd2n9k_dorSzv-W2_y5AWZhn1_DqX7cB3dFbFyk7N4AJ9QGRlIRcufJIyibFuTXDfzriNAGizvdUhjhAi17GPIVwALDM-EZjBGFmEZcTQEMRzawkT71FOpTA7lHhaCekCTbKaZvhF7FiQzpofJ2O3Kgol-LIgZyB3FuK1QKv3t9K4VKtRupX8BC8S_z8odOsb3q64tMJuSqxo4JKT3ZxwM--k5V9vYqeBUqaLJDfOpbzTChCUkhOqxGyZ6c3KjAyAGGf0PBW2WxKcw09lR5jWCGzplzjnOyuMfiqnRbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=Le8AW1Q3XE4xoywuRyheTz7lUYIhpGnKwCprr0kfRtst7O9JtMrv18wLifCZVi5GpSoJV-IpBDdfWGuYGAY7u3YSJUkfI6--Ln4Bo9VnspIdeYAp-bDWiZAXDHwS7k6G1jKuTAXMX1LZ3mP1HFCHjINxsCzj-S-I_zoaPGhArQYS3hsw1BkmPQvE33gx1FBEjYCb6QBBQTuvyPc4m0W90QaG6NsGJwC_OViNmIQ18j-6HFPJpZeDJcVWSaBUQXnR_bj3VJFQs3FbewpWwz7lGXsSyyxYmpQps-VZfpJj8U3GBjcXZKZprUKpUeMd09Of8DAkoHDNG-0HjtikTyjKQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=Le8AW1Q3XE4xoywuRyheTz7lUYIhpGnKwCprr0kfRtst7O9JtMrv18wLifCZVi5GpSoJV-IpBDdfWGuYGAY7u3YSJUkfI6--Ln4Bo9VnspIdeYAp-bDWiZAXDHwS7k6G1jKuTAXMX1LZ3mP1HFCHjINxsCzj-S-I_zoaPGhArQYS3hsw1BkmPQvE33gx1FBEjYCb6QBBQTuvyPc4m0W90QaG6NsGJwC_OViNmIQ18j-6HFPJpZeDJcVWSaBUQXnR_bj3VJFQs3FbewpWwz7lGXsSyyxYmpQps-VZfpJj8U3GBjcXZKZprUKpUeMd09Of8DAkoHDNG-0HjtikTyjKQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=F8FabyUs-BRtwcEfq61sWYkxEY2lwHLZcX0SDDCuhhK6uYLOrRgLtKY-tl_MmsdMqwFsfemaqk0Lr8vgJo867ENeh_ufcBoSUnzpdnvIGqAIqO5pge3ow4oy5FjNJ_9Q6fjW4CkvjzORB3ftzOeLnpR-VlsKQ9X_xyqfTNlGojZz2VoYqagnXA56M7inCWFgJD-3lQUC3eKtJovdfacCqHBCDseiJeFbQa1iG1tvfk3V5jZ5HzDyPVrPV8Voq2k_2JK5wd2-dDNdBZhwM_vqjEsf_tz1riJamD_F_dJqI2xsLs-p-u6-fqLV4wBJO7P789Qwo2r5svzNI3b3Ibl3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=F8FabyUs-BRtwcEfq61sWYkxEY2lwHLZcX0SDDCuhhK6uYLOrRgLtKY-tl_MmsdMqwFsfemaqk0Lr8vgJo867ENeh_ufcBoSUnzpdnvIGqAIqO5pge3ow4oy5FjNJ_9Q6fjW4CkvjzORB3ftzOeLnpR-VlsKQ9X_xyqfTNlGojZz2VoYqagnXA56M7inCWFgJD-3lQUC3eKtJovdfacCqHBCDseiJeFbQa1iG1tvfk3V5jZ5HzDyPVrPV8Voq2k_2JK5wd2-dDNdBZhwM_vqjEsf_tz1riJamD_F_dJqI2xsLs-p-u6-fqLV4wBJO7P789Qwo2r5svzNI3b3Ibl3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZ_9j-QAaFPyhZvK8_aRbuWpkMJ7fRVOZijY28--EvDm0_nbWhxTRTR7VOvlGyQCxFZHiDeaYfHOQRmFq9zAAt8cXh3HfRl8gGn0J5FRpIaJ2Vh0LfOgYEkOT6BOSMly2dfIGDzX0n3NXqsqE7S6WaWARwW2OVAFOeCWxsTMLU-ej7QJgvmWBkQpB1YP0MbKqqxcwoefa4z5Cg0QpIxxe4HAaHQXreyvQZH5e1WCwgQHhcp_Z0SoRsh_iLHHwrHByzr_BAUmo4pKLyGv9UM3pU5ZgoNWczhMe-Dp5VwB1IU9C7VkKBdGMP23RZoPKQAhTFGOWfPjBOJKm4j1x-7cDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDGMZLngdwOT3WXfSbIzYr9Xa7UM-JtBM97f_fRNhBHQ_Ka9NSFtIUbWSrI3zs0olITShizVbXY2Q4SV4rnh0o3HyUsDcOzzzYyB1PYz0j1ntIl_DcJ67vKDRybYXCstbl6o58cpvTxF0c7WXE2lFN6IUKweAVN_epsLmckpwDiwdp8H1TAOQd_dOgF_N10K4RG1_DQ7DcnGbakIP2ypnKYI55GSdzSJFn0JMJEC5Oq6_OwaKWNDoKQQVhBZAZ-VIvktVV0IDbC8yGtT-qvM7IM4iQap-h-7kOMvZFDfo140g-OmUVYMGtA9WtV6IHCQ6VPMz3HMkeOgZrnr-2QHpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=trW0vQ1f4WAUvvu5vpnJZ08Sx9LSWgittYzl09AgBvyn4ApL5CDLYr9Ulfte1MV4I7WtwofMHCV0QkSjwh6u9lwmurbao8AKaZTqiFvGvzoSWS7cbW4jKnrtGMPpcfA6ZVXWZlKyft-AL2kzRqVnIPXiHOUbVUwRXsu_rORSDC0ySr2otdTt9nvMHMCIYVtMtbTFsn6XvYVyUs28BNxiX9BS2auLycKnbpPcsx3JifJHo3k1AXdan07DW149wbneWEJSm7ljtx49gmrHFNhOLuL65NuwCJTt6cl7MU6Bb1C3cpBeOqKAzr7EXdykRsHBjtGAGzTT5iUajGNHnyZVSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=trW0vQ1f4WAUvvu5vpnJZ08Sx9LSWgittYzl09AgBvyn4ApL5CDLYr9Ulfte1MV4I7WtwofMHCV0QkSjwh6u9lwmurbao8AKaZTqiFvGvzoSWS7cbW4jKnrtGMPpcfA6ZVXWZlKyft-AL2kzRqVnIPXiHOUbVUwRXsu_rORSDC0ySr2otdTt9nvMHMCIYVtMtbTFsn6XvYVyUs28BNxiX9BS2auLycKnbpPcsx3JifJHo3k1AXdan07DW149wbneWEJSm7ljtx49gmrHFNhOLuL65NuwCJTt6cl7MU6Bb1C3cpBeOqKAzr7EXdykRsHBjtGAGzTT5iUajGNHnyZVSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=EHmzSxoZ-k9bVavi9KciSsTVyc9Pfz38EZvW1Mkt8-3UhdPY47Vpv-GfkfraryCiRJ9Xel4G37Oa1qlAgvSR3j5ua-CicIBbr5qs8rlum6WhUbJh78d9rjtDWLN1fQ8gWKUmf5m2qqPwXpF5hIMWYLpzm__Haeo95PyounMALRn8eeOc3tr3WwkzDQL6kxMWIkpFYjKf3BC2q1DguZ9tukZOuwXP2kD_tsq2h_-Tl-yPHyVtAJ4U7giz-rPl-vRYLmatql9q6S8C-rHAXRZpnY5JqBhzfzeh8OPaeGZe0LxoeY2bylOtG01KpLnTBLC5f0EkMBDae3hio2_rb9GkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=EHmzSxoZ-k9bVavi9KciSsTVyc9Pfz38EZvW1Mkt8-3UhdPY47Vpv-GfkfraryCiRJ9Xel4G37Oa1qlAgvSR3j5ua-CicIBbr5qs8rlum6WhUbJh78d9rjtDWLN1fQ8gWKUmf5m2qqPwXpF5hIMWYLpzm__Haeo95PyounMALRn8eeOc3tr3WwkzDQL6kxMWIkpFYjKf3BC2q1DguZ9tukZOuwXP2kD_tsq2h_-Tl-yPHyVtAJ4U7giz-rPl-vRYLmatql9q6S8C-rHAXRZpnY5JqBhzfzeh8OPaeGZe0LxoeY2bylOtG01KpLnTBLC5f0EkMBDae3hio2_rb9GkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzM-LVjSxkSjzArod05Au97u6erwIMGQD6t9rQuB11kL0vWMI6JRMurUqxwUxZnvd8loO7zeQbotOcdPS9rHfl3pEacFqNh_GBKi2aMY8dAJSL_W8psxmUL0iL6EF8mIr1C-5ODO273XjBvi8G57hlmDOE8VIDW8UxYG8_7MrHTefMT3GG-45C4lxPbiPYlT-PovjbrgoGDlEV9xlOmCUtNYA2hWkIC6pgTHcz180ZUceYZhMY8d1n0AwD5uRrITuy2Vj5sgw195P4Fn5F4pSmRuNXlTESdvgNegoOaE9jxM3iARD6bTifcUV-vXD4gDH4qRBxV1ZYUNpxk1jW2mHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkj9zgWu-x5gteFenqeqUbMGaVsAZ2BMFcc-TnmjliZIeQAYhUaCBMs2KVHWI5xUYEb_WxXYtY_UUG-61j20WtlGvtEkFPuqcIM88LnMnSApwsAh8m4r7HcOx6TlmFvpcXsCVtEe9OpiXoZw5JW_xBeUcBTtE-GgdTwVxEj9iTbxOOue2Fh0VoKbL3ub5G0RCuwt8QjWqckQVr6bxICGBKVt9w2AqxB2YPa-tQr31FWP6YRNGMUtOhPDcPX2995I94LhHHXHsRbukGHh59XgwI7ZtDiMUKC0hHFO0itxwArttcF1b4p2ryIs0vJVRk2EsKO24CauOc4Hde-1haGUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=IRDBK5ip0ThUbiYeOMe1357Ql5wnARRR6WVhyJDcVs8FUw-qdAPITTOOJB50DVzdSfIfZ8_NLOtP7l8moUZp99bM3pgHi0FpcLkajFt2-d2Yk9rqCC9p8RGwMeXJSGpkNL0ZTkhKAEvoFPKE-xwkYXTVa_rq-bRPpbcJLuBX-r6ZRlG4bFedSYBGTPNc4X35y-OcCdf1eFwU_HuYXqe8KTGLSweLAVmCGkWiAXQq-xOyCGZ-LNmDBmpzKFGztL78hQNEXmBDzWxN6HgJ28N1ZZIyC-9eWPiTMkwcU2ENkjUiPVibiPbmLclZ_gUCGQ52aVokkCKj7A_kE7T5kYok8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=IRDBK5ip0ThUbiYeOMe1357Ql5wnARRR6WVhyJDcVs8FUw-qdAPITTOOJB50DVzdSfIfZ8_NLOtP7l8moUZp99bM3pgHi0FpcLkajFt2-d2Yk9rqCC9p8RGwMeXJSGpkNL0ZTkhKAEvoFPKE-xwkYXTVa_rq-bRPpbcJLuBX-r6ZRlG4bFedSYBGTPNc4X35y-OcCdf1eFwU_HuYXqe8KTGLSweLAVmCGkWiAXQq-xOyCGZ-LNmDBmpzKFGztL78hQNEXmBDzWxN6HgJ28N1ZZIyC-9eWPiTMkwcU2ENkjUiPVibiPbmLclZ_gUCGQ52aVokkCKj7A_kE7T5kYok8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ot4FFqSBcx--N_-dPZ9CxQnesXBDAxuE1rN0MCpkMMhJqoIBlXqWOX5ZusVvhjhcFEkPQYZ-sMGT6jsu4Da93ATi4ippQH-Cm547N2whCFfDPec09Gk8yzJtw5svVuHCPd_tU8J1B2G9o7Ck8DefQ9E6uerKbp_U60WYKMV3vJ48uHlieMLonqVD5vRauLv7B0O6o8p7e33xthpq0uJGImfJ47kAOFsZm9sFr0J1ti_simJLJBM3ZDirb4gsLCIcb5pRqlN5aYu_ME_d7xslvkaXM6WSqDZWZkIi5WueFqaf4OlVmL1vTyMID06wVEh13pYeUXyDdY7uPpqF9AAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=NmHptlzzSgjisnl5kloUSWkTRWasnamS2IBm72XYKJWOb2aezVrpj3c7uVCqpXvVkk--nTbx1p6M-KrlTncLKw4T2peLCcshQKUhXSqP_gFvNTzkrDu_JYZVzu0GY_vyVBCsOZQIoI03GhzVeayUKvooVOxrvNkO8O3T84IogqZgjjdFGVAkHSdpojJb_8Cku6i0L9Ttg6Mc96xBrHMOfmG0ngIhzMIkQ1UezgzoiOjTjhhDKdw_SquyZClQXSzKeWOsGIhm_YPtF6f_BAUtLul8i-Fsy7drren0hp2Czue0z7bmpTeeGqRZeotGDXHsvx9u2bqZojTptw0V_L3kXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=NmHptlzzSgjisnl5kloUSWkTRWasnamS2IBm72XYKJWOb2aezVrpj3c7uVCqpXvVkk--nTbx1p6M-KrlTncLKw4T2peLCcshQKUhXSqP_gFvNTzkrDu_JYZVzu0GY_vyVBCsOZQIoI03GhzVeayUKvooVOxrvNkO8O3T84IogqZgjjdFGVAkHSdpojJb_8Cku6i0L9Ttg6Mc96xBrHMOfmG0ngIhzMIkQ1UezgzoiOjTjhhDKdw_SquyZClQXSzKeWOsGIhm_YPtF6f_BAUtLul8i-Fsy7drren0hp2Czue0z7bmpTeeGqRZeotGDXHsvx9u2bqZojTptw0V_L3kXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=JFOVD8GDvkFytES8gQkiVWhPLfG2i8OMKrCMUbwHuKMgUGcdAUhZ2C7UAs-FzwUcExmmuv_6EjXWdXLumumemtLONJ-KOe7afDiBjwcLOPpPWZLJVJYXWY77Gc50Vb827UBUrtmcPEvznC1btrZKNx7SDDeFLXRqdAO4JC0kMr0CHQEY0f1luTBZXntG1JpiWNBU8AdUkRK9HG1YcrtoksA4YEysS5fv62CFssLoXLZcsq9iIRKQKVOxQsogh2DWvBJmJwW0VTyw6J1mzwKDyI8KFySlkBkCu-hBZkkziDsxiiVXnu9T1RvlemKeGsxcvfDxSaUNg6D-kwl8O0KfDm96XPoERceO9SYryMKimVCf1LIOvtAeR-8m6iaBm0mpuYOHLbWulImIeAZlLBGFLn_mDGI5FGSBQyt3pK42m1oNnLvFAqr345tGbkB_5QJLIn5hB-YAVdrUvqYFvFuyvl_LcXjvdp-u2gnlq1KHbQPFZWixu6aeCrG9Vr5FMObxGAP7Lmnsj_TOyJEdM4EQm_Zcb2kcSBgtVRi_bvFTdrFSF9RF8vJsXkTloXeD5JMHQu_HIJ8odSl5uErucMLoYPG2ib0zvrbq29Jb2hLaFps8sq4eehBV3FX0i--8qN4C32XvH3sXmueBC7hgn811DXY15wvKaxs2vBKe2QDT8u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=JFOVD8GDvkFytES8gQkiVWhPLfG2i8OMKrCMUbwHuKMgUGcdAUhZ2C7UAs-FzwUcExmmuv_6EjXWdXLumumemtLONJ-KOe7afDiBjwcLOPpPWZLJVJYXWY77Gc50Vb827UBUrtmcPEvznC1btrZKNx7SDDeFLXRqdAO4JC0kMr0CHQEY0f1luTBZXntG1JpiWNBU8AdUkRK9HG1YcrtoksA4YEysS5fv62CFssLoXLZcsq9iIRKQKVOxQsogh2DWvBJmJwW0VTyw6J1mzwKDyI8KFySlkBkCu-hBZkkziDsxiiVXnu9T1RvlemKeGsxcvfDxSaUNg6D-kwl8O0KfDm96XPoERceO9SYryMKimVCf1LIOvtAeR-8m6iaBm0mpuYOHLbWulImIeAZlLBGFLn_mDGI5FGSBQyt3pK42m1oNnLvFAqr345tGbkB_5QJLIn5hB-YAVdrUvqYFvFuyvl_LcXjvdp-u2gnlq1KHbQPFZWixu6aeCrG9Vr5FMObxGAP7Lmnsj_TOyJEdM4EQm_Zcb2kcSBgtVRi_bvFTdrFSF9RF8vJsXkTloXeD5JMHQu_HIJ8odSl5uErucMLoYPG2ib0zvrbq29Jb2hLaFps8sq4eehBV3FX0i--8qN4C32XvH3sXmueBC7hgn811DXY15wvKaxs2vBKe2QDT8u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=cgQEbWzaQ1CIlvVibQ_9RhQbK7v2WgvADGXUPNHQYeAS6BKiguVpfMzE1EdvHAgAz513pNhmgDcbSr9q26-cjF4v8iUpqUGQF97ZOH9nRnCc7ZTtTyQZVyUvVnlV6RmCs0RaJERPqp_Fu-9Q-qYCGVoeTMvDM2apbnWRX6WwpzugMszhNOnw0CvAou_Cv_NG8UKcAfTVoDt0jRz-L4owu55aAcho4QKV_G9YEj0jvIQI1CLGxFenoCJLMK1eBqO9PfU_7rhj05NgDx_bU5DuRxSXowg-NYhnX6nIJSt52U4l4aT-VUis4UIVy3k49nmvejEToSsJl--HdznomHfrNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=cgQEbWzaQ1CIlvVibQ_9RhQbK7v2WgvADGXUPNHQYeAS6BKiguVpfMzE1EdvHAgAz513pNhmgDcbSr9q26-cjF4v8iUpqUGQF97ZOH9nRnCc7ZTtTyQZVyUvVnlV6RmCs0RaJERPqp_Fu-9Q-qYCGVoeTMvDM2apbnWRX6WwpzugMszhNOnw0CvAou_Cv_NG8UKcAfTVoDt0jRz-L4owu55aAcho4QKV_G9YEj0jvIQI1CLGxFenoCJLMK1eBqO9PfU_7rhj05NgDx_bU5DuRxSXowg-NYhnX6nIJSt52U4l4aT-VUis4UIVy3k49nmvejEToSsJl--HdznomHfrNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr0sCxuKbsIrGOHUjtXcnbhkyhZchDl9u3s2DmhiHPkQ45B1d2R1oz3e-TbgsWHYWSBtJT90ab4luxaHRb6aLYXd9b-joPDu3-giPu4PHIPEeL5WO8qecnzVgFi-9JF00CN7SO_y5B8ohzZ_IQIvoubR8fvJEEEAEIdITpORVORu7w9z8K09NSpj-UvIZa1YUSUkaDVy33_n5iwziEKJdcvexNZ5qWXgEKDKs4FgRqDGsgcaLZ5_Cwl2fYKnYi4lq-PMpByHvb9rFU0MWJDg3hJBB-jn0fza-30jXuqym5aGsJbe0OuSXn14LBf2o4KK1HWXts4YZ00lY1esKt7_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=TrCSPv4b2WoqrpcgE36MLJIqzHyHJ1zAxT5eoNZeysbHlgmldS2OZicb6vyWKwjZiqB-MSAoj_DfDwQXeDWm0f6J9wzV9BBD-mYUB5kOj0_P5GXFBBam7meSa91gXkx1xl10aK4sV0PEiXGMwR0rpvh5aLpIJfDoivTP_fx5vaXtpspYK_H5b7omLxFM7djD7n0NMLbeW9NegG8suessyooHSYDK4u6QnxBEtz7A6NtuinqM9lej17v7JyQmNXbox6GEjs0mM-HKp6A2d9GikAXHj3HpqzVTdvvNMHg3BTCxCoxcDcvWJdKjlDXNMSTsLbFQemu7k35-Ze11KizszrlY1FZxei7NwSc0gma5Po_ooZnCPdWY1TtTcUxuBojYnmCi2Eg7_amcPCQc8OJUqHao61YbNrvxE4xD2XtwtStdi25UgEdJpBnRdFmsCkDXwF7Bu_he8WDYXfWTvJLTc85hn_JV1SjR-Lj-kRR8rEO0QZKjXgC2y6pFhsnbLjc9CNQSvY4nkDHLXnzSKQ4OkjPYVJkHpXylr8cV8xfZxRutV5_v-k2_lNI1Wq1EKcIfZ3rzJEsUaH4v98okDS9DIhDXJYKGD52Yn1JLXAKmLSQy5ofCJKHOv9QTyz__VNteOCvi8YyNSW_5OcjXpGU_2AuMw1CPzM8rMa-OCuw8F_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=TrCSPv4b2WoqrpcgE36MLJIqzHyHJ1zAxT5eoNZeysbHlgmldS2OZicb6vyWKwjZiqB-MSAoj_DfDwQXeDWm0f6J9wzV9BBD-mYUB5kOj0_P5GXFBBam7meSa91gXkx1xl10aK4sV0PEiXGMwR0rpvh5aLpIJfDoivTP_fx5vaXtpspYK_H5b7omLxFM7djD7n0NMLbeW9NegG8suessyooHSYDK4u6QnxBEtz7A6NtuinqM9lej17v7JyQmNXbox6GEjs0mM-HKp6A2d9GikAXHj3HpqzVTdvvNMHg3BTCxCoxcDcvWJdKjlDXNMSTsLbFQemu7k35-Ze11KizszrlY1FZxei7NwSc0gma5Po_ooZnCPdWY1TtTcUxuBojYnmCi2Eg7_amcPCQc8OJUqHao61YbNrvxE4xD2XtwtStdi25UgEdJpBnRdFmsCkDXwF7Bu_he8WDYXfWTvJLTc85hn_JV1SjR-Lj-kRR8rEO0QZKjXgC2y6pFhsnbLjc9CNQSvY4nkDHLXnzSKQ4OkjPYVJkHpXylr8cV8xfZxRutV5_v-k2_lNI1Wq1EKcIfZ3rzJEsUaH4v98okDS9DIhDXJYKGD52Yn1JLXAKmLSQy5ofCJKHOv9QTyz__VNteOCvi8YyNSW_5OcjXpGU_2AuMw1CPzM8rMa-OCuw8F_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9tyo0ZKQf0CN0jeiVxXG_HJe2C3mfIAxhPhLJUn6pT_aQc_hle0KexelCdP6LIRzPmfsEZUoS1csiuaPZGg1CKucY5l7cnCi1F_BtMKh2Z9axg2K3zqaIldFe7ITa05MjQBIyGat9Xo6lEF_oe9W8GTTrVOJfktjwJ9kbUwmfQi-nERCcMjC7V7eoC_F-WBwJ8fCyMS2-nCpnQGUsdFNHxbbE55xGiAJfa1NMXJV5RcPfZt5_sfZQBPK43mbrl3VIZqgXu09XggIUrCM648--kJQdpxd2_9HAMMS3xwm5a8632qpVQVcil7FcIb1O9vCLj-gEQMrTHyUMNL6Bf9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq_mAHnpzbZruIf8IeH8rtMhfv-n-iVtt3M76nyjq7dc2PeQyh7-mIZCAwMU6uGcoQuMfiUyBb0Vh_l0JPq4Y122Cg87hiu5NcYi0Gjl6k_qp5feZoM2cUiXGroSZ5KTp9FssKduxRcqNK2wiOAVyouJ9_RiSynfmpY_Wue_eR85Nc5Vqaap_GdXrNe60Tn13o763uqS3CKh4_d8gSPUAUEKMK59DL5DN5vTG0XbyDhWqDPJ6n_8sDvc2uKfywJ6N1iXndLp95BNyqVpdNMGJXRKerkzWcNEVwwgNAGM3VyZ5K4Pq9akQQFHj0RFqcFCZ2rHIBU15xiFMrf9LwczHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=NKNAbreJQDaqvFBCTbHJhUsJ07xHhTeVN76RLfKgWRnIQM3Rf97OXyXbYhXra6eW4x2AoVvStP-uUX0GE1-dIFW0S3owIIFOil05vtS65t8WHrrJKiGWzFKn4JOZIbwV7iHC0ceLGGJ8S9WHvsfmG-dVNDyYHWVe2Y17hkurv2Tpk3_E8yExq4hihGg6gxfPYO15N-eW7qXvmNjahf0v7r02cy2wF9rYVTOxfqYHHOBRQN9ErSIRsFo4l-uBKr7GfKYpw7kQCa7eTJxnLqXoWWDSGRUPr0kwNiNGHoapYLx3fiEeUFdUxdk0kvV8R6wQi5x3RAHssSwD00vSWMVn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=NKNAbreJQDaqvFBCTbHJhUsJ07xHhTeVN76RLfKgWRnIQM3Rf97OXyXbYhXra6eW4x2AoVvStP-uUX0GE1-dIFW0S3owIIFOil05vtS65t8WHrrJKiGWzFKn4JOZIbwV7iHC0ceLGGJ8S9WHvsfmG-dVNDyYHWVe2Y17hkurv2Tpk3_E8yExq4hihGg6gxfPYO15N-eW7qXvmNjahf0v7r02cy2wF9rYVTOxfqYHHOBRQN9ErSIRsFo4l-uBKr7GfKYpw7kQCa7eTJxnLqXoWWDSGRUPr0kwNiNGHoapYLx3fiEeUFdUxdk0kvV8R6wQi5x3RAHssSwD00vSWMVn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk6mSnKlcx1llyQ3ecZh0EXE91Y3DA3-qK3Y1y0lCfx67WMe7z1Cxd4D-AsJFU1S9Y6aKDcUQsvtPYdTaz7rNchGFOBiKVOf4411SqVulJ3VDJ6HoK3qRTfnwT72lYEFd5hOgjCtK0biQ510mSJPYgjDPK2O-jba638rUTPvLTniF_JPOdUKly936NzcuN-KWUbzQdbWvnqARyj1X4fsVw609RuF7uVzF3xxcKZTQ1j0HbaraipTkYCWkv2AoT6A44NDWEwpNrFQtyrFwCgfaGmDe71YDlXYvuiLxxcqn54GNscPoxuaP3vF5bLcisFmUDvK0Yc5C2TiC-V3DiDCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=jdWtv-U_BhIICQopResijE3i8f6r61TkukLuuiA01hQrr67yeVjE7G5XAOdZkdx4uhgxqtkvUXFZ0hJFyhRtFQpBD0VIElGPa4naBoTH4e30JxgGScY2o3yHuYwPAd0I8PCcazs92RZKrsyEXg09DOS9gpdupEvOHsn_jWX5B_5XC7FVzrPvElrXQTpN5MNVSNwdNd2uTb60aFJWsacFEHg48KV0fBsBxpv6LR_v8SbroaMEBT1zmr2azRnyEC-SyhFPigoDJSs9cRTtMAVYzyHn_5zg43wSKUA-1e__Gc_6acxsBbcndiEdjDPh9DBXWK9ttn7x1Irdz0GmyoZWRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=jdWtv-U_BhIICQopResijE3i8f6r61TkukLuuiA01hQrr67yeVjE7G5XAOdZkdx4uhgxqtkvUXFZ0hJFyhRtFQpBD0VIElGPa4naBoTH4e30JxgGScY2o3yHuYwPAd0I8PCcazs92RZKrsyEXg09DOS9gpdupEvOHsn_jWX5B_5XC7FVzrPvElrXQTpN5MNVSNwdNd2uTb60aFJWsacFEHg48KV0fBsBxpv6LR_v8SbroaMEBT1zmr2azRnyEC-SyhFPigoDJSs9cRTtMAVYzyHn_5zg43wSKUA-1e__Gc_6acxsBbcndiEdjDPh9DBXWK9ttn7x1Irdz0GmyoZWRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=IapLkrE6-WxA0p0iv3CkvBK5zHcTVMBkmgZ_FX6mdXFOInFFI2U_bO09ML5oxqpOaOKzQ9Ac6RpNChnMqOxpj7gwrRwQIFW-DUe-PuKoMf5X9JqpzUjIDl0RKKQJVG4_azfZRiDhuj6GMlhExWhFozBcunpAtgYLVRDCCmUqBXtPmu-Bxjqgt1ci6kZUvw_mnC4-rLkfUYzNCpJ7ziLR6x5bj_Ok4J-tQGmIV7bi78ped6kZSGf7TeYsABd_DR81p4pmFNVpbbVZlmlNqxiP0Sub3YEMKJ-fbujxqxtkhGcMj7JYNeHvuxFU77-MEudMXPU_WFSobfaBdiMoGGIw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=IapLkrE6-WxA0p0iv3CkvBK5zHcTVMBkmgZ_FX6mdXFOInFFI2U_bO09ML5oxqpOaOKzQ9Ac6RpNChnMqOxpj7gwrRwQIFW-DUe-PuKoMf5X9JqpzUjIDl0RKKQJVG4_azfZRiDhuj6GMlhExWhFozBcunpAtgYLVRDCCmUqBXtPmu-Bxjqgt1ci6kZUvw_mnC4-rLkfUYzNCpJ7ziLR6x5bj_Ok4J-tQGmIV7bi78ped6kZSGf7TeYsABd_DR81p4pmFNVpbbVZlmlNqxiP0Sub3YEMKJ-fbujxqxtkhGcMj7JYNeHvuxFU77-MEudMXPU_WFSobfaBdiMoGGIw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=v4dSqRgobLA-HGNtPOKPKTSMJ84FJPm1Hyfoi_iYUuYu6ll1gAyXDhBqlI7ksxcyns9Z5usQOpTgXPz0dTC4lwx2PvkBb8EuJLAXY94JLIUoxX_FeK49lQA9oZR9K4o0LoOebcJWP7LzRC3_X2WScl5_HfD4cEH7ahKA-ewGHiU_syGKwa83Pu0mwy3lYZ4dnyS6A3uKV4J_EUX2irqi9eoKbQP75VoGhXXGP6jMYsbXpQS-MEghsaCTFSgjF4FM_c21aMHX661GhtPILcT6cBvYo_b6_LW4cN1WKhZzOF76ejwR0qb4rssaQa1hD2Lw0Tofstz0e9rV1KzzPCFsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=v4dSqRgobLA-HGNtPOKPKTSMJ84FJPm1Hyfoi_iYUuYu6ll1gAyXDhBqlI7ksxcyns9Z5usQOpTgXPz0dTC4lwx2PvkBb8EuJLAXY94JLIUoxX_FeK49lQA9oZR9K4o0LoOebcJWP7LzRC3_X2WScl5_HfD4cEH7ahKA-ewGHiU_syGKwa83Pu0mwy3lYZ4dnyS6A3uKV4J_EUX2irqi9eoKbQP75VoGhXXGP6jMYsbXpQS-MEghsaCTFSgjF4FM_c21aMHX661GhtPILcT6cBvYo_b6_LW4cN1WKhZzOF76ejwR0qb4rssaQa1hD2Lw0Tofstz0e9rV1KzzPCFsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=s0STUnolCWRawKiFE3lUsnQBYFjZUVE86ryOZcWh1v0ESHmggIcvbqUAmhh6s1DJVY-wnp31fzjuS0H8WfoUAHNwRY99g0t7SNsbal9LDuAX5KTYD7I3C0xy6eLcS8zNDv29drICOnXo6vkefnJCoreXpHI-K-Lksm-RUwFVrF2hvkinKdFT_Y8Gc2AxnE7X2jKHskVVvtkulpqA-2sp2zgYD8pDn2LHFBPKkQJoqkZxBMk0WoUIfoCADFshHRoMfyfHy4aEe9Udj9AlUBZsfrDc5npekBeUa93vlu1nv1AW-w0yAxRXkRUiAKkcBx2OVeNy0NM2HRWVoLgLsEoEohV3OG-QRwfC-IDqpVTwqGmSRkoh-fxKTZEBbyOwTy_IC9AsLXhQBvBOYzAM8lWrlZXiwh8-dcVw59fRpUqZuCVQDzY3iBh3lWx2xShNh-zRYhLxNX08yRYuXLGiAohxqG6yCoMrsSY0dIrV03d7Uzfz0_BclvAflpr8OLkovl8CwQnVUgC0EdGAHdMyFPBpFQ---eR5fY7nHPPfhQcl-AngrLyzH60pm_EoTlBGsaj6w8NSrufq7pRTtj2XrdtVfV6MhOfMN5pFYA9-MHRjWjB0r83m8_PuMBZjRGSybZzZ9dgxZwwRvTqOHarMjYv8-OK03kcfqnU46h-_5IaHrBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=s0STUnolCWRawKiFE3lUsnQBYFjZUVE86ryOZcWh1v0ESHmggIcvbqUAmhh6s1DJVY-wnp31fzjuS0H8WfoUAHNwRY99g0t7SNsbal9LDuAX5KTYD7I3C0xy6eLcS8zNDv29drICOnXo6vkefnJCoreXpHI-K-Lksm-RUwFVrF2hvkinKdFT_Y8Gc2AxnE7X2jKHskVVvtkulpqA-2sp2zgYD8pDn2LHFBPKkQJoqkZxBMk0WoUIfoCADFshHRoMfyfHy4aEe9Udj9AlUBZsfrDc5npekBeUa93vlu1nv1AW-w0yAxRXkRUiAKkcBx2OVeNy0NM2HRWVoLgLsEoEohV3OG-QRwfC-IDqpVTwqGmSRkoh-fxKTZEBbyOwTy_IC9AsLXhQBvBOYzAM8lWrlZXiwh8-dcVw59fRpUqZuCVQDzY3iBh3lWx2xShNh-zRYhLxNX08yRYuXLGiAohxqG6yCoMrsSY0dIrV03d7Uzfz0_BclvAflpr8OLkovl8CwQnVUgC0EdGAHdMyFPBpFQ---eR5fY7nHPPfhQcl-AngrLyzH60pm_EoTlBGsaj6w8NSrufq7pRTtj2XrdtVfV6MhOfMN5pFYA9-MHRjWjB0r83m8_PuMBZjRGSybZzZ9dgxZwwRvTqOHarMjYv8-OK03kcfqnU46h-_5IaHrBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=F7LrePb1tzowW6uf6oRp-PqsCtTq9Xsi9XQl0dkNZVrBzIOmqjTQEXjZKUi3D0w7OjssVpAHJuTHyR5g9EeKjhjs9VSQYHxVsJvyTZSdt4xxWyOboxIBXpDkQ38LTWFcFXRNczZko75R8X1CTKgyM_GzOvAUTCymAzFBWr-QBIJmY8VaVY4ux5LZ4LwJprHCn4ZEMUz2UPjAdc0oJVPX6xmrg7W6UnpN0ExScjwkekTP_ibI6UFYdhrrKJqWo-lrrL27vjXZYLfBuLeh9zdvAoXO6wFvhivKR2hdNjPqpr2pON7ARW4vcU7U9D-E5Dqgmn1uYkXbcvAeQvcA-cohOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=F7LrePb1tzowW6uf6oRp-PqsCtTq9Xsi9XQl0dkNZVrBzIOmqjTQEXjZKUi3D0w7OjssVpAHJuTHyR5g9EeKjhjs9VSQYHxVsJvyTZSdt4xxWyOboxIBXpDkQ38LTWFcFXRNczZko75R8X1CTKgyM_GzOvAUTCymAzFBWr-QBIJmY8VaVY4ux5LZ4LwJprHCn4ZEMUz2UPjAdc0oJVPX6xmrg7W6UnpN0ExScjwkekTP_ibI6UFYdhrrKJqWo-lrrL27vjXZYLfBuLeh9zdvAoXO6wFvhivKR2hdNjPqpr2pON7ARW4vcU7U9D-E5Dqgmn1uYkXbcvAeQvcA-cohOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8o-_nhe6az7a_UPzsozLLkpLgme8YgddXZZpPIhZ7KPHTmHqU6SUUHUllyhUFPeyUPBFcuFRP59o-Mtx_crLwBw2CW9wYQqUYkMsocojG6T4vhRXb2c2j5edYVz7aOIMLsywtviff0VPZkZBjoHEKkfvr9RtpeBLrf-o3ekE-wIxn-a0pQUzhrn4u3rturqzA6y1FciOjWKoOXfNB6zSGg0pQ724jseKv0oro5tpDH1-AC8xbk9p1VpK4qXtQipoqLlycdBtooO_Zuei-hGwYFJ65X5CHcrWRloByhMLyAaljxxQ-8gEKvZfKToWCQqGVYS6pFg7FL2saCKkt6EEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=sq7Ez7PpSxFLDAGg9PHfKnWmamtX7BVaDRQkRDQzIIL8MMlBimpONgGl7G-GI2WUgxSYtXSUBYSlRq3KJoUWSW8bFOtjx1wAR4X7H9h8TVwiJ3ysVk5YNSA1au5-J9BzwkQtLZeVc0NkGBnX9eBq5PTiMlqX6IuzbKs-7r4ZJoGJz5upDd6jDRuBLczXkT4Jx4nHi_v4NnFl-A89h_vTpCVfJr1X4kqd9dJ01O4RPj6BnO-je8gL4t-M17T1lykhLiEAXcRfOberNWOM4_-ZDbJkqgo2e16piIyxYSXFIwk3tMZEVH7MWR0gkw3Q5_GZ-MNDm-K8t1TTdKXklor1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=sq7Ez7PpSxFLDAGg9PHfKnWmamtX7BVaDRQkRDQzIIL8MMlBimpONgGl7G-GI2WUgxSYtXSUBYSlRq3KJoUWSW8bFOtjx1wAR4X7H9h8TVwiJ3ysVk5YNSA1au5-J9BzwkQtLZeVc0NkGBnX9eBq5PTiMlqX6IuzbKs-7r4ZJoGJz5upDd6jDRuBLczXkT4Jx4nHi_v4NnFl-A89h_vTpCVfJr1X4kqd9dJ01O4RPj6BnO-je8gL4t-M17T1lykhLiEAXcRfOberNWOM4_-ZDbJkqgo2e16piIyxYSXFIwk3tMZEVH7MWR0gkw3Q5_GZ-MNDm-K8t1TTdKXklor1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=uY58cn_DBBrvBCjyUDpA9ZHJ5yMtu4i5OA8gPpjbTaVdlQmRIDuotMxkSZLVv19hO2buiraD02GPwH5FZ6M37q-jkFXYdUm2iNCZl0n63iQLqILMwp3QMALs0I-r3pwkWLeHQgM9ll11xhwzN77Dop6P6K2Y-KwEQurkuy-eafupxUZgKZfA8YFPfzIGVKC673wuuf-3b3FynKe1cHsTnpvKiaY-mB_7i2yHWagsQdGT6ty4dqvY5T9hgDCqNiprYulTCIFnLBFRU8Qz6eO9oDTkTkUgA-SEtHZLq5EWty-RzoPewZpiLfj4m9gasIRYUuYVeZH48JjU4dvFwD7DWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=uY58cn_DBBrvBCjyUDpA9ZHJ5yMtu4i5OA8gPpjbTaVdlQmRIDuotMxkSZLVv19hO2buiraD02GPwH5FZ6M37q-jkFXYdUm2iNCZl0n63iQLqILMwp3QMALs0I-r3pwkWLeHQgM9ll11xhwzN77Dop6P6K2Y-KwEQurkuy-eafupxUZgKZfA8YFPfzIGVKC673wuuf-3b3FynKe1cHsTnpvKiaY-mB_7i2yHWagsQdGT6ty4dqvY5T9hgDCqNiprYulTCIFnLBFRU8Qz6eO9oDTkTkUgA-SEtHZLq5EWty-RzoPewZpiLfj4m9gasIRYUuYVeZH48JjU4dvFwD7DWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

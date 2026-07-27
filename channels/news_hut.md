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
<img src="https://cdn4.telesco.pe/file/QrvxPEjXiB2H_zBMRtR_LJlirnrMhl3U5xR96ve-ivnlP77LXSdtOBsS3DqJTdwQjTSJ6dSehNhGDdtBTLq0v_4hlvw775mlqgSackhzhMQww7rjKhLhRFNF8Kg9-01IxlLWWhcE7r23s3MeQLa3VXZGGTgkoqxpgOEmlX-THh1GSqFA35SPOO6oYSMOEgJfgYcOMRoB_a_SsRTPl7YbUxWCkmRIEaNlJVA1xDZBNrsj01VolEWxDcNsW22fOwI3F4ToC7ioNuJk67YJIQhJ8sGXhthXqMFyOKhsNM8fnipTWz5dLAr7xJ4BHUrf0-Tylk5Wd1sM2Z5VMzNe-2g36w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klTK5t0OXCI6uNkPbjlVPhblzhIy3m1BmUD-Fxmp1i0z7uJdt7iEJGg-RBRxCWlSTkbmQdN1u21mSLiqCZ-o24Nw6-7ImLPh7OgXnI9stdon3uQCaIe9ZTgkdj44vPPnED5P1Dt_jVzOASJ1mCcwLLyATXy9tPKGekxGU3PBes_gl_COVQtrRcLM6mmuXSvLWPpgXXnZsh2Ds9nNON--CoKnCyqLyjnRGbNcABqUTAaos1hNVdbB6VO01bAFMbLw3BMF5WVkLz6g_SSwj8Q3map9S8uyjFsWzM2wOl4JOMFSa5-EUfjexnchBjFdlNqIsGX4d4NQsh9KhqkFqoA0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BupSD1V0Sg2x4ZGsllBrHLS88oGyGMitiK5GQ0d4ESQPgXMOGZS9pNS7juVvvxhTWp5nDkfC-LWvY-puVmyQk1lcMUnZjpAAVehnRrZJKmIkfo4NZU8yvI4WE2-VUXmJ2TITK8Qi3_RwT14sW9bp13syHXZe9cPDrxi02lmkRSQJ1-HCU9hVji_8w-OCrhEdtReeAt3mx5yPDj7CE_8ht4AyEfQ7Els8aOxOhVG7iGWREGvZZX4Il4KSePvLU7U62Ab9TBmPVJuDawei84JTxTTVYTUt8NNRTm817n1ePHsJw4wPzMwFoRYuM7RWBhnw1rM5XwjIoqYqL3vUVecqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4svIsG0l_KaI6or_AEgGqGLx2t8H4LgBntmzDtqupgWeUFSzQH4HuP_RYuQVD_qETEi8QQ-2HcvdmG58iLeoVQJ65WnizFDQT5P8rgwcDcf4nFXyi8AtXouD23m_TUQYD8zmWFAH85cEsuq7tXLuQE0scjhNM_tL5mKCx7MWC5BcSiDuow5N2NWUDihgxnhgx7SHX8zfVoi--SPEHVea2rdoRcSJcJ3G9_RAvFSmWEl9TQUgRs-u_04boUKnbwEghFctVgxAmbhqwblJ1holDtUfccnYCgVY41UfZ5ykkHfdantEnC_eJ_VKdSZeWSUVOYjTF9n7yHCxl6cH9kacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_3E5E6kkFsTF9Fgx77inZMi3CQawzXc_8K7KRPbdfm3tLzd7XpIdo5iQPasGnquVsPRzPjUcJYJL8KNAsoriHINFLU9xD4oISqX7FjotiFXdheuKIeXcGOkMICbbpz6BXeEaCP-egrExJZ4-Ds0PkLhojSMF0CIQj2fx920-abWaDC_XwaFZhW-UBlXaQLdvYkvrMKHa4T6doBCR29m0wGIdtWX37ExjGk6RihxeIwNxnf9mniSj0rftFewXcGKVGuKHNLTNkDFEyfSbAgj6m38HVMefQzqhB95Db597-3stbtjpso79j_VklR5QCrvucmywbodciRJdohPz9Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhNJxy7cNeIWAeEPKA32rQVOaESp1kSWduLeXzNLHoiEDoD5CQqb1VnL-X6_e4c4FnapdIJ7xzW76U4XX0S3g_VR_zqXYqkBfShCClFnNy7VtFhWY6BNvfOt6LNpvuxtQ_DniK-ybAq_Wl0zbPvEqs6sd0gBr1PQE9oWFAHVr15atwLtQPe_7L8DXJEY5fP6xKFUxsOePSEDNjcqa1cTmhhg3NJCdWN2NS9b7fU-9HVBsBIzpRtOc2qYS4baUZ3DrL3kHJSxo3fA5ReZB56W7vVW36n0r4tequjT4mYnKgedfm7L7rNiGA1vLyYewaESXi4lC7e_e_s-Q-HfXxP_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0ZBQZ0T5YPMfVc2fyJp4kbFRQHO_DZAw2Yb3HJLh7Ocn93TEK1oyXkHEr2DfouNaUe8x-um0ibBJgdZFzQlBHt1ocRsyPmWcOjLRTS2YCDA6J3mPwYCHRGaMzjVs-FtdQTqB0EGRKSK99_L46q1G3i5ynMpVGdLbZT3rGvcEqHZmwCf2uwNHWarNZkhhUm8pslgboBK-Vk4VIovXaVi0xCQJikkihm3YIX-WXzkL-OXtcjd6F5Hln12Y3cjmkRuxbF9n4vxjsX6_7GEvnV2J2MnF51eE_s9yxuBbn1MtBiWtA62OD-6zTjrLdpU6Kl6qHfUshoHL4JGvoZu7M0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-mny9qaFlhJ7Jn8ao8wFQ9ifyQzjt7-lnHjOn7WOAG32fb_NzPxwe7t3DGZcep-QV7T2xZve0MKiuSfLo2Vt6s2N9sCbZy6EIIjHmyV5TzWTideKlMU5GaEV1P7N8LIi2Eq2bE1Uu3etq6R0ZaAb7wRyEF5AnX1XLyzKlUw581S3bxNqQzefnmCZr9tn15tZFKncjgdYABOTUx7Co87G19pfQTKwvkwb1vaOSOz_1OC0DwZSIpy4WtlgRKlPBhrWriTpFmBBmCjUiOccizTIFD8XslDKENJvohxUd3Af_QSsuNUu7FEZqTC4oE2AXcV27SUXbA97J0P8uCFKd1NIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p1sCX9o0tHaU37cU8Is6ijgJUtN6Q3PcYmGYIpFUXr0d1E_aqN0P1NE97-xSQ3pnh5txY0Sv5ifuMvm_8pZbX0xs_w1SGpWRCJHt9JxwjRmyD_TZNuboouU0VBQGj8lfbTF7GQ1U7dWdh31n9aBjNmJy1mHXbfNSqr4_buQRiQOllG8i1_HbD8tIBiGJEryIR1Jhrj3Zr8uhmRaEH4etfu01NAcuSmfwM7RtyGqOwdNQ6mV6lPm_Wgg0oqBRwuQn90DmihB4MRijc-R5SevYv1e3UV9IdVTC8Yw_4YHqAtruFrSVPp1Ew35NeeLsP93LXjFXTBMSOWbuQu6WeAtfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqHvF-ytla3tB1HPtPNv0jdyHh5tIPGT6erYd3gSJb_HSrD9R39LPYXDiXK1Yd4sZmbqmwXfrvl8HIhnHn95qgZZe52J10QAqxbr0idYZxlKXNYCD8FQbHGeYzza9aZZDxHxx7YOtUkYCEHns58gc2nIkXreOuwdSEFaMb83hU-uFCjlo30r4Sjk49sBbfgZ4UIgBUW8BUPxU2Fk16mFt_CQalzJPqZGaGyUT4oTvg0u3wGsWdnCIN4Qssr9cjHwqtwzyRou9cB3Ao9i5EPIofgUoheTQLodia_ih8hMhmJ--OzJOPJTmw-WMliAu0C-kD9h0xytVj0gIGMr1xv9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTq7ZhpHRa0xW4U3AZyh6n9KOG6CQUxe96PZlvRbCApPS6TKKZnmOF-zjSxMbKm9jdG3ropQW5OF4OaBcn-KGG5OISC55hWR3lKZNRyAWK-8YZgcWJD3R13JU4EzIcHLfUO1uNe3LKyOFubOz4kwdIpb6bPAx0dpPHma8nEnuc7jHnQYYyRvo4OzQeg1bRLeyakE4X8qCY6_2r07WGcBylL_zPeAl89I7BOTrOTQhnfVHpRDMdsEw7FdCaE6jInGMSM-HQRx8bkoOoX6zp8rOo761bKUbR9bVYhOBbXlGcjIcbGp_6f6hT6sjBwiYHhDukPhm4f-nPXqiEL6FvSdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8bQbJk46hGnzdd_KlTKsLTddDtEQAp74UyTTqgFQB1sDlU1JkhTDmAoRzkAArOEHNy8WUEy17Mi1mM513la_R1wVOAil2IQCgCp6fL-elWRobnFgeijioRIqTuuZC_V_ZDXqI6E4llqMEQdMt_j-CKAKgXuwzpdNjSxyd6lpKWYzdCf1-DQfDHR8yHuPUGxJ17IdpUs_AZ631cwIWW-Q0DBMoh8KJkrcQmRa5shUoOkC4rhkCLQzZcS48-Mg1bT0eeTnlXknDxAS7wZB5Y-yFbe4t-eYaHlZwvS3ol5DaEuC0OHqy0HAOLwqFMH9zSWj4nwpI9Y3b0HeTQhvXTzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORquAA7EzfCozfa1p3isqkWukbUq7He_n8HyfNdT97GwzphNJKC7l6ddn_sXxPqUyYy7vv63k2OTDdVjkrIqYfL-cLKgnjjJn1-T0BK8fwEE-aOJXp_ucjmORQanP66ZgMp-eNT2mkBMI1vwJgbtBjQvtEpxbwB4f_lUCsrJq2tm8y2Tpg4ZShK6dFVbPkrnUimRDVpxRkngNKHa3Z5FWWA-8SW7mCiyo5EncageEIMAu0gIoCDjEKCpwYeaj1Dg-LWq99GnFKnDbnM1ON-kMeSc-8K3rsum2_2Ryka34MVWHDjziuXcbGSLvqzUQGQts2qRJ8SsOriOHJgtQmUAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqOlAIiuW8o_6zzZgpLQaTdSjFL5jWS3fwresLgSnCo93_4gnoeoAZomwPz0G02__UnE7A1l2y8MqosSDqGwOozDkgh8T9NxOu8P0Ll66kqoRbeVwqK42YWVseYLk3BoCoPyN0mU9F4GnslQ4_lthrYWC77sJYqhVaFV4reyGsGRgbWmBmARw4rkVjEQ3uYQt9FsXJTuHav4xK5avZrlqDRTafvXVwQ25hWt05kceGbPFZzkS_8ou98t5Z32Gc0vc9monFtE56V3a9SLgxzcgAW5D5wyQR5Rjq75u2egtHZP15HkxVfF-iUcoW1t0jJIE2wxUnJ1sfuXxl4HSlJwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szbtJ1tjQc3JoTjJ3F2ci02dT-_HvVRGs0mVu0lZHewOVJ0t3iT_l8kVD4td8xX7Hl3uhjRna-eqVQAUobsrzC4Q-6_APyvQ14DXz2dj9VFtOTOXTYQfzo1LqQ_fg1ssf2Ufh_mKYu4jd0_hBU3joGZfrk83fZ306Zo1Wm9fydc6O65Rdu5wABsq3mN26Oyy7kqQ0ra52TCY_mkOinEIB8qQZi_lcwjdN9YEZmCSJ4HqHwzB6vEqHXthCI0V5Vp_IIip6DM_z6u1zwK11wUXF4vrOljyOpfGvjIZIh7mxfV7crgSPa_HM9SpqZyZilDBYS6Fsb_ffoHkedBfVFKWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEfjkWzaccIT_q1H5sf82LOnW7aPrNWcKg-Mp-xmqqeo9qpyP8e9Bv0hRjsNf68NAVIP5acdkAsCOIGZrynotwi-foG35iwJi8fWxj2nCe20sM3eJtXYjVgEj5exqetp1aEpQghZkXWXoEOAH6bXwW6kzwUN2N9rFlbxzkNn6I8S2kUWNcWI97sFm5E1_woNrZWAaguJihln59tkKzx2TBp1ud--w7OhWAXrhat62_kM9ixsrucy9XvMQYRx3LJAGA1Oi4sK967TD5-mM5mFxySrilWu17mdVdffeot1-SgZHDdIRhfC05laWo-vyKptcKC33i0jBQxrTnl3nJQ2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwALPY8INHEb64aZJeuqex2ygVxd0yWCiiuDuegXPwdG3Mm0hZar8GuCk-pvzzhVVDkAWJjZ8KyOz0Ykbk83kc2rdPocL2n6HlBeAsStf6oYxmsHLh9s3d62OHjLWh0biaS6pof8jGp_XXNa3tjK5sYw4Wm3icW_tB2H2xp2I-RZuWWwJuaiM24ANAaTlRNGB7ZsdFcFWeQ_V3s2v7jNluMQBjkTxk1kZl0xOF251yjZTN0Veog83ljBm-rfDz8EFvzoPMmjGrnPiJMm6CAFMjmtFMiXVrxpunb8JqEb-4oiZ5VWV2_6oKocRUkpVFRt2dASJExJpDJwDy8gO39aaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXNXRs14KgYWTl4sld-6g-J7eiZEc8uCnoOs0LfU7G40wUDAvJ3cqjE57727I4IY0dBJe_COnzD4TcUWM1ofB_Ad7gDADfYWMEwd5buwifsDf3ohNTCu2XvgQ-ap1EGJ2Ty386qp1ftErQtHTMUi-n3aOBYGLhWVz-RpXtb3zX0Dp91-Y9bVtGLs8g852NrxKzGu6hDz8AmNKBkxMrFqTPFIT0BHWvWRmNLMtab4HchDXRqPgmWGARv_1VsOWDXrfaBjKQj5iYAlLiulyrKw9CgA7Cr7xsuRzlr2NntgeIBCaGU46ikcVs-mVJ-zwBrLydGAki72o4QkOeM3WgIC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbWVzPSe37HF7cjlr89CADWW_n_BXpqH0-SiAmfUZiMPOAPq790zncnml3Ij2LGSKBbokD0E3EagWI_r6ahQT1lh4rjJOIyadb8UgVWmA5AZoUfG6rr9OaNgAmmZrbKIYazZJpMpO67O9bv-3nA8zytohzTUX5Y-F1Po8lRGONTzW3iJWAJfJl1WdB6wmznQcv7-sAOp1BsVTG-eldnanAXjBFRV0sxwtcudcdaAGkWRLhdC_NXwolX7iIOWob7WVHwQjsWw1J_M9jsp7pSDCAoKUqEtWVSuD4r_BassqzLVEhDtRlJJiRizmFI914ww9ch30hv4SfX6x3JkRoWkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCe4XBlgTmsnWkScQzkhIqqvwsaELc9j-7j_H-ZqZRSKQzcZZ8-FPW3DH2Sw5eqnyTKJ_bjPIZfIcwLEnXD2XxMcH3d6C7ghR4osbHEZhjp4lqYLfoZIE2Dz317ndc3LhCeHO58ppAzrt-nUDBo2GdVZta3FI9szqTMgEHGDI96VCny3FgxvUMQwByhMo_lqEMX0-rZD1Ezw-l90iE0NhrQwVh1-NHUs8YIgHBXzwELkYXQwgo-Q-oQpLCZJisi52isPwF8WuTyxuaw8a2f6i0kJSXYbn6s5Y8bqRWBGt6WWn-VN015wTs670GscDJEGOzcVh5FvXbwa6FV8UiSzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzSI18n95hLS8eeFTvLO9ioMSLoD0L4JlVJ-N0wAhYilt37or7AZQj0u2Rzfy9rfSm9xzn49vJ2cpFaOtFg6qomz-A-gvqmhgznxc0iJb6ECAQucmSToU6qCy__BzbS8H1uZEYSUGT_5PmqLrt7l59iprJBShW-CXHmJWHBADHk9kCfBfkso4BuUOudxTS_-ExGajCoS2lgoU0a5ATIvKp2Ml_Dhy7a6yFW6oYSB5D21zqr4WBTX0hA5pyV7V3qHB7pKyE-JkkXPY6wLzCLOpWS28gphQM62TSUnzMfyW0d2GMZMM4mxvVxLSMdfxZijm35f87wIeDIR1V3aFmpocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQREaawW0phMxZTL6Ajw-fJSCWSmqRZ5reOa85p8hIeb__kKmQvYiGlqcBlmEIVrXCYz47yH7_ILfYswggB71McZ7K2VjKJ8l2nrI1Vhbyf368jg--oH5EiSjRZxd1_V0Kg3JVxYyHgtrhB0ruCqOxDOhKsmu1XSMohSmCjaUwRKZSoERZ6wpY-91pocef0Eoy86FkhQrb36zwBksXaXrEiRqnGPVyCvGPLJ8gWHfkRvlSRgFlSoEj1Jj6kDM7B2ZSEg72sDUhu1v8zEoez2sK0-NLLq1FfM3Mb2keXItZUlTj6gMUMlDXvlbXSE2cKELMR3IIuHor_O3YyMuB6FbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMQqW7DcEkW92ACtpGKotf9ZoiNiFd9GEUEyVdOzfn0GfdFBvmjGSnRZTsRgFvM4KFtkkgUbL3RGo8d4DL-BNGr4P9snDlOqlTCYEokkVPODaUwOTLDlbGdWgZedFaKraRTdpZWNM8rMR00KGgrTznEWl9YKznY7pE7FGH-QLM0gIw0MT3ZEegB8GcV9mI-3kxsANBGFBrpE_1qEpdBsEe-99YgYNI6oTdhgyW6rcNWMTr3mDPYWeoTJYixqWeZswtMmptI6jFndOUBujHbVJ8ArwRFEuCupjna16e9NxTiaNwHRaEuCAzgevH9MABQ6CD2jck5CXxDNss-LPsVn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Wq0e_zqvJJ-CXnGk3h7_kvC4zPPn7oVA23KIByoRFGCuCOGeSuNyEcyQ7FDNeQQWeixfwYZlgyDlmfVyAN_hJ0o_dH_08XS3TlgAzuEmQ23v2zF50E57OMh_Rlb5AWtFeU1cscP0S09hKhS5_gyMh9d7xxH6fTq953AI1Nsy0QGCabs2dJAGZfZJ0GmJdVaIlRu2X14jc5MaiIUGnMlkw2Lv72qkVWV0B3a6Kocm4UljmB0Eck7knhNOdPdy2eBlBUUJm71s4z0_fK11dPqqX2-tlSF2En1NCCkKENsKgfBZVIRLyabSEuIO-Zm7XhlWd5f80E8S8-OZmKzK_aMaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Wq0e_zqvJJ-CXnGk3h7_kvC4zPPn7oVA23KIByoRFGCuCOGeSuNyEcyQ7FDNeQQWeixfwYZlgyDlmfVyAN_hJ0o_dH_08XS3TlgAzuEmQ23v2zF50E57OMh_Rlb5AWtFeU1cscP0S09hKhS5_gyMh9d7xxH6fTq953AI1Nsy0QGCabs2dJAGZfZJ0GmJdVaIlRu2X14jc5MaiIUGnMlkw2Lv72qkVWV0B3a6Kocm4UljmB0Eck7knhNOdPdy2eBlBUUJm71s4z0_fK11dPqqX2-tlSF2En1NCCkKENsKgfBZVIRLyabSEuIO-Zm7XhlWd5f80E8S8-OZmKzK_aMaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5fKswlAoov_C5QR67jS4ZkAPDOI3QjLc1UtmEHICa_G2xBzL7FUwn_c_hhGJRJ6OHBpECTn393khRQGJwjObhjbTfmmjputFpYyr6rXf-cVJxEFxIhCyjO525X0PoNSoeHWywGUuX1Ofg18yPPhDwXZs__XaToOnr4-Ij47lQXxcHRNvEbPSKTWBV0z_hElofYtMJHGl9NiGJ4wY_EcuxU5-Z2TBETjbwuc8nT2Sd3MQkLoN7SSWMTZzYDS4yBYNJq2xrhB5shEuqqOdbVNwvLRl93AOQkLacrU3f_CUmNNGRPrfOjnctFz-WkU9-pCv_DpCnq-sjxQjYCI3KamEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXS3IVnFsK_CHJZgbaadN4zBfcomC-mkOdpu6tUDjn1IjCRtCcWC4PMEam-GrMeV1PJDZNOP4pr-4h-1omK5T0mV924NekUT0Ol3YADklyZ2mI1doWJSvaAgv8OF42Oi9MWwnOD1KVPPvz93L_tYlSX8TIh6bWVzs0FWhESB8QY8cf01Mg_2AocvnBKAKcd_tbvesUJ3euYPfkNji2son3-xVvqyvnTQ8M6TzR1_Xd9jFcpq-qDoH7gabNk9HVT8HhU5U9fRlFGn9TRi98XczZ2jy41ChZ_3elvi9M_De8ZvkstPAMHAH_rBAII8Wu3A9_Q9VC2QZBYeb_i9mxyDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txa6HRzJ3sgiMZEPvYtmNawsNDeWMEeLTkbo5DC4EIfMbQkItDwoAVF2prXVeBlt9t18qocW0LO0Oa_2Uccx8KMgY4Xf3pvMIuT_vxtZ9jLQ6js4kC8SCggJxjlArB-sl_oDdjkwqJ0m80HCSTLVc6SKzNmh-i0TUnQDExTH4sf6X7E8hzonmwZfBRguV1vaxNzCRDOcS2vy0_vS33VDMANh4E3FQI0p_4PdhtXMKSdTXwn3rbWAZoPVdy539jINfMgix4nTaV9B59ZcN8rFbs3zzHUzibK7_h4871luuwWuWbacLz6sNMB5i5JPD4MNkRGxiQw8kkHrC6la0Tu1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-ErvHXZ5NyCHUYe9FXlORjtwxolkGmi7-zHDqXRwlEgcsbF9fw1uzv5u2gyYGKKbsTeT4OsC4LwGXcZVoEQoLBlCfRCBVS-iMpO8LH_oVoGXKsaaV_jato5GsGYXLVCbybZ55G1Y2cLg_42NnjFtlz3bUih-5CrBQJv4NAAJGLKzVs6-2tNQfGSzY3SQu9rkSUuohU8ANg_43rVnNj5UzFxrpd6keOK6a1w0w_6lKy_MtNbuq1qB_eFkjB29mlplCJHi0b2Bjti5x9VZ0For38VLaVwR0BBjKQBmdOYfE7R_Crj4aHKXLeNBKg4xNZkXZ5AEdA3czJMIu-GNISogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=fWhQlepN1jqFrKP-fmS3-jATSptc0fyZlyJ06mGuzEWs-fb7AQJYQMwfszgYj3fzmYGXV2qL-9rc-wERUqVQ3IF3972z_Do2QgHWp0q9eYyfzhZN8P_0vHpo9duwPeIUMOPkAi9jXnTX3lTXqnUoTynjIYCW9IQFc2oZQtiXmL5so8V4Lkjgj9ayK6YIhQWKvGoOrGb40AJYSash5y-mzazLL4uCoA9JGHOMp8BPByvRDhLqb-m7I-KHliNANjdz8Gk0K5tGppp37KPDLrE2xA-uOJelTSwsUakrwTOhUgqZLgkQEBm1VK0ZSQu_140BplVN8FN4Q2fG9XabgEM_UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=fWhQlepN1jqFrKP-fmS3-jATSptc0fyZlyJ06mGuzEWs-fb7AQJYQMwfszgYj3fzmYGXV2qL-9rc-wERUqVQ3IF3972z_Do2QgHWp0q9eYyfzhZN8P_0vHpo9duwPeIUMOPkAi9jXnTX3lTXqnUoTynjIYCW9IQFc2oZQtiXmL5so8V4Lkjgj9ayK6YIhQWKvGoOrGb40AJYSash5y-mzazLL4uCoA9JGHOMp8BPByvRDhLqb-m7I-KHliNANjdz8Gk0K5tGppp37KPDLrE2xA-uOJelTSwsUakrwTOhUgqZLgkQEBm1VK0ZSQu_140BplVN8FN4Q2fG9XabgEM_UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=kh1fUsQZWgdtj29KXdCCehTpV8zlnUQc1aWmh2b_EP-Z5sCCZCKsTATljEpi5c5Bn8mKGrX88D-9aNACaGS9Z3-F64kcl3_e9bmJfM7gCUF3-d1ZI9Q5JUj1NTHxv4RGweC4NEP6iuxf_tIMSZ7N3hwv1HUZHonIgBUN-2TaZcOGSHj8fOCI7jTmZIQn2B3KoG11UZv0qYKdk6B6x3h2oQkPyXyFTKNqSHAFeRI0wMS5J37lOjDmEXegrkK5qsV-9R7AGRn-jm9gOi2ZUSqYmKCkt4JYs6kKarGk_GbVXEyRfUhu1mOGsw3sIhCEkN96GP57zi2bt0A9pfN-vEMzwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=kh1fUsQZWgdtj29KXdCCehTpV8zlnUQc1aWmh2b_EP-Z5sCCZCKsTATljEpi5c5Bn8mKGrX88D-9aNACaGS9Z3-F64kcl3_e9bmJfM7gCUF3-d1ZI9Q5JUj1NTHxv4RGweC4NEP6iuxf_tIMSZ7N3hwv1HUZHonIgBUN-2TaZcOGSHj8fOCI7jTmZIQn2B3KoG11UZv0qYKdk6B6x3h2oQkPyXyFTKNqSHAFeRI0wMS5J37lOjDmEXegrkK5qsV-9R7AGRn-jm9gOi2ZUSqYmKCkt4JYs6kKarGk_GbVXEyRfUhu1mOGsw3sIhCEkN96GP57zi2bt0A9pfN-vEMzwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=IEb6Pb6GJ-u4CQ4yOcv0XNjloMI2mPgGbu6wxqmPp353HN7Cd2XycGbo44Po3rmI2IcGNVUcXOlwHPv6-Zqx3YEZVcHMAvqiGTJvdeNsh6q9wz13W7Jfr57uzx30Ey9lHTgIcNGwVzU5XMdxcf2E2kTw3ca4oxOPgOfvsrnqcKJjbyuHx8ETOSP1VNYt6op2Ilhg-NjQ-_BvcWpypy2isGNZoFQ8tPmqTLynVtB085gyKUHDw1H1m01U6zvjEa_4w4TJxmsVX1IXDwyngJhzogIkSxEESntuWINeyhOdw6Y6WXUr4m_i4w0PMxM8UBLsWQHioKLBBEHM3w0C7rx6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=IEb6Pb6GJ-u4CQ4yOcv0XNjloMI2mPgGbu6wxqmPp353HN7Cd2XycGbo44Po3rmI2IcGNVUcXOlwHPv6-Zqx3YEZVcHMAvqiGTJvdeNsh6q9wz13W7Jfr57uzx30Ey9lHTgIcNGwVzU5XMdxcf2E2kTw3ca4oxOPgOfvsrnqcKJjbyuHx8ETOSP1VNYt6op2Ilhg-NjQ-_BvcWpypy2isGNZoFQ8tPmqTLynVtB085gyKUHDw1H1m01U6zvjEa_4w4TJxmsVX1IXDwyngJhzogIkSxEESntuWINeyhOdw6Y6WXUr4m_i4w0PMxM8UBLsWQHioKLBBEHM3w0C7rx6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_ROOPurBhEo3f_u8hXTObT8Shf-PnOUX9REDFZZGOX8IB89vXI-xvR979jbofdhjh_YuIP2y7ifL2o7HsFhjjpbaK2AYDckzeex16dgoaCHZnKk7REqgakRyuyRLVq9UX6KzFaNPF1lzOstommm4_C8QjcaWuS2Ns2TiDBSKqaLXUHRAyZiWYDNUpJjAYdor_ZUXuWOiWz44DeRC2BTIhCSmA2p5XhaAMGwgxOIlSuBQPr1aIm4_JjbCw5czGeP-vwqyrpqIdoj9AASEcoexieqLcW8UGoIoP0gUusf5n6MDQ9ZrYS-VyfnWapw5oCfHUBKuKL2OIF5SH7eeWj-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=YrnLJAPseMgROXC_KnoxT1vp05WTil86fhA2Sx_Z9JpbTg8rS0lg-YNecKxUkqMZb0udSW-kRFbX8K7sMBqtvlxkWlLhonXweyeDVghVjAQ-lVRlyJvN6ayJjrHLEWlwIyxaEAinsidaLiV-SSNDvXaPw11AHugvu9SG-fGZ0WGohyDLRd_RgY4erlUn0QYIbYPL0JoRNm-u0dzCS9d_gy7rYdCyNXSurLUydPBd3zYqpG9BJUCBVj16VsJV_YoHQlIN7m6gfTwQHGB1UOy26TYgjOYqF5wgdKJQU8qG3-tWoIs5_XsRvcuGTqCxNNV6DH4_pfl2GPO-OdoUgr_f6FRCWgaSECxb013KgfJx4pKq9mlP7aPSZbpfnK_pbezGTAIoTJFt8HfMXS1ib-MsGJvT-uhgUArwxHciF7NNwXygjrLNj94460XmVcpeto8R4awEpbbsRjoiYiN1uZQhhM2a9dPByzYdQWIyswVNhj2mhvWpSBarK57HL010qdm47bJs30EK_YbrrEpKNcslbLbdLgvsoZwMn2hpmZREG8jtpZVDlwVKrm-SG-VrY3yJxak8tJ0SV_n6unLVVu8Ken2vooiqTMssepJnqQEhpWLAizc_ZJqoJTH8_kjGTSVecTb2oknjcmIFdl7Gq1ou1_GQpvhK6bPdLmHLtGza4xE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=YrnLJAPseMgROXC_KnoxT1vp05WTil86fhA2Sx_Z9JpbTg8rS0lg-YNecKxUkqMZb0udSW-kRFbX8K7sMBqtvlxkWlLhonXweyeDVghVjAQ-lVRlyJvN6ayJjrHLEWlwIyxaEAinsidaLiV-SSNDvXaPw11AHugvu9SG-fGZ0WGohyDLRd_RgY4erlUn0QYIbYPL0JoRNm-u0dzCS9d_gy7rYdCyNXSurLUydPBd3zYqpG9BJUCBVj16VsJV_YoHQlIN7m6gfTwQHGB1UOy26TYgjOYqF5wgdKJQU8qG3-tWoIs5_XsRvcuGTqCxNNV6DH4_pfl2GPO-OdoUgr_f6FRCWgaSECxb013KgfJx4pKq9mlP7aPSZbpfnK_pbezGTAIoTJFt8HfMXS1ib-MsGJvT-uhgUArwxHciF7NNwXygjrLNj94460XmVcpeto8R4awEpbbsRjoiYiN1uZQhhM2a9dPByzYdQWIyswVNhj2mhvWpSBarK57HL010qdm47bJs30EK_YbrrEpKNcslbLbdLgvsoZwMn2hpmZREG8jtpZVDlwVKrm-SG-VrY3yJxak8tJ0SV_n6unLVVu8Ken2vooiqTMssepJnqQEhpWLAizc_ZJqoJTH8_kjGTSVecTb2oknjcmIFdl7Gq1ou1_GQpvhK6bPdLmHLtGza4xE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=V86_iBk85noL1WYUTsqobDm7aPwIPa_sHQf7qaxQZ7skbN_YdjHd38yUZR459TZusmRyMgbsGVsBHf5XU6xSZx59oT3o7ud0pqv2IFZON4XC55TNwU2s1ce6MkDf4zz8B3W9ps0U-DxGaX1EINwjkwGjH-uhbyYHz15azcJvpFNcXpvy-sHOTrUlTT3IW4G5hd4fKjE4Dxty7gsVDtucTFjDAlEHJDFwyFyT4Z8oBw6S3f1QrE2Hje9tS9xgi8hZNPwDvvVF9sldIaRJjoKGXL4gD7TfTRHbCZGzHVxBfQnVIJeI8fDDWseVa7O9cxIhAmWvzfZN97roCw16KvJi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=V86_iBk85noL1WYUTsqobDm7aPwIPa_sHQf7qaxQZ7skbN_YdjHd38yUZR459TZusmRyMgbsGVsBHf5XU6xSZx59oT3o7ud0pqv2IFZON4XC55TNwU2s1ce6MkDf4zz8B3W9ps0U-DxGaX1EINwjkwGjH-uhbyYHz15azcJvpFNcXpvy-sHOTrUlTT3IW4G5hd4fKjE4Dxty7gsVDtucTFjDAlEHJDFwyFyT4Z8oBw6S3f1QrE2Hje9tS9xgi8hZNPwDvvVF9sldIaRJjoKGXL4gD7TfTRHbCZGzHVxBfQnVIJeI8fDDWseVa7O9cxIhAmWvzfZN97roCw16KvJi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZN2tuvPFURBJwXtRWTJ6Kq4psWHfNzYaLFb-w2Wj20t6HXRgAfmqAb5sa_tyXyqEHpPfIy5C3Acgj6d19KcGv1DtI3eVZBApNYEHGY0_SJ7jFDc9ZZbs8F1o4Q0QQOHscoEdatQSxRXhMiImpsv1_caVkxDcNOMTtFURB5ZkPit4ATvjDiCsAIFXWPPHXZyaAHixnX6U2L4N-GQhO02WXZ2ia2aObJrGfXuL3r7-Tg8Dp7443VV66cl12PhpAjMr8Rc4jknicmZiwLjuQEbavaw3pFZh2IpTEuRqYQnNLKuyz5cp5Goe5vg_94eb6H0SXad6HM95TNC1fA_PsSWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YskkRxzxjpDWoPyFKOaB2URgc4p3_pFFVr-IFWmNe6QrHdR0JNlx43FEt7O6SnVU1nrFaCz4nRYGslXSFLOcyxHAmDbzBjE-DKlJS5Y5yjf6NlVBk86I6SJnwTO3jkRxf7FeXbocgStMoS9thboOoLGIL5WVOVrWr5h16SbafUG7HSp7xPmQxMgVmK9sU5c6IHTL6emPBhPHa10MKTXnTHyJB3YZvOXyjqWvVGkxlkX1ctNPstHj-V8WCbuTVQjr5MA8rpmvwzRbZN5KWAhXbh36jLwlp-91kSzzjxvj0YE2lSMhFE7SSVwDr37oj2kd-BvnJZe5SL5PSsYJTumz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Ttfcwm5kGtkatVI_iZ5psc30ClaUXeqiN8Dzezi-j95Gv3RB61NoPofKAXuDHI0gVllkdw8-XFtfp1NrR8zW_9H8UoRqihjQl_9VYb2YLVy3a51BWrMU2yLk5CE8tvKCmKVEBH9fCDtLzNfG0ojVFlc46AaVwfAFTSO73sdTC8owN-T3-EKTRmfTcClBZQz35YDbaVmfa77fmxqdt9A17adiE7B4iA_qK3t3e8okZZiRyk3a0qAOm2sD4iPkQ85W5iGlZja7rktB6cGU57C_HLBfm3GvTdwyXjaqvW1l5HOtOKroGI_iq4_7d5Znl3ll3SO8aqKab0-zvnhmDJLR9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Ttfcwm5kGtkatVI_iZ5psc30ClaUXeqiN8Dzezi-j95Gv3RB61NoPofKAXuDHI0gVllkdw8-XFtfp1NrR8zW_9H8UoRqihjQl_9VYb2YLVy3a51BWrMU2yLk5CE8tvKCmKVEBH9fCDtLzNfG0ojVFlc46AaVwfAFTSO73sdTC8owN-T3-EKTRmfTcClBZQz35YDbaVmfa77fmxqdt9A17adiE7B4iA_qK3t3e8okZZiRyk3a0qAOm2sD4iPkQ85W5iGlZja7rktB6cGU57C_HLBfm3GvTdwyXjaqvW1l5HOtOKroGI_iq4_7d5Znl3ll3SO8aqKab0-zvnhmDJLR9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jbQYqF4Q6t8B6UyYi24HRMzu8MCaX49lRdt_aw8RyykqjhuDfxgAbWvty9fvr0TnKOC651ZFGrPBNyQuSqsWR5P8Hd03v9byGCBsusJ3eqIvBDDWUunxM77v6427CF7v-itNmB3-9oTaf8X887w3jre9yowZIEjDm47hjKcQlM3h4cObcYD0WIiFzeuyTqykMBsysL5VGQWFtyXZ7JQl2Z41pELF3gkF6VaQRmQ36gYUi3oIuPUeg1iu1u2YCrkdeIrpjitzVKhnn-wZ6AKe3l2wlziohkpYFJYNsulX3uy-gVTtz2brCQ76fsEbbLg_SmpXuYp8JqL2zn0kUjsHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hKhmUNTZD3tU_WDWKhSa_ckM51UtzYP63z-ku9YXKb_jmZFkEOOtjrIlGETpT8UYvB0o06KKFEFmH9j68MTwOYZfiE8LmQUM7kkAk4yU2zYPtqxlEdb07G1qYP81eZBR-gl83cTySTRKYUC3eVP_0CwEo-pAB5h2wGBc-VDio3Q90c9G6MuchaecjJDd9uBfMk7zekxcBF6OQBHc1wM1lc29aC79TLW1wEuYOMXhXUxotTWlOoQJ3jKwC9cv9gdv6gK3VH5nXc4_nEh8502dV2nuRakxL4DkkHbtyulbvTI7S9kenseL0RIxAqLqRH4Fyid4eFaoWjt7Fvst3OB2sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=jYyPS1DsV6ZuP_Tb_9ldPTADz-3CERp2_fbaRt5GuSuTAxoMv5twybbTQjNLNAXgNFNLSk5xoZuZQJ8-Y3q1eOcopLw-Tk6G2qcLJx5CTBiETISix9Da6RS4A_qipkdp75XpK7acG9JbvSPl72D9upp8a2-vw8i7jiWWo_XJ02JH6gfCZ-2AlQGfgj32-F67WP5jZDTv9KyX-6yS-Irqm-wVf1XJbVYaFGqZWOHVin6u2k1KM2MTLj_PrqwMNkieQ59NWWPcjq7g1ohmMgEfr9d2gBghh1Nk3j5BlALi8tL5wYQcJdGWhGsg3VX6adEnZS4NuFzqqwtOIjrU7mWwVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=jYyPS1DsV6ZuP_Tb_9ldPTADz-3CERp2_fbaRt5GuSuTAxoMv5twybbTQjNLNAXgNFNLSk5xoZuZQJ8-Y3q1eOcopLw-Tk6G2qcLJx5CTBiETISix9Da6RS4A_qipkdp75XpK7acG9JbvSPl72D9upp8a2-vw8i7jiWWo_XJ02JH6gfCZ-2AlQGfgj32-F67WP5jZDTv9KyX-6yS-Irqm-wVf1XJbVYaFGqZWOHVin6u2k1KM2MTLj_PrqwMNkieQ59NWWPcjq7g1ohmMgEfr9d2gBghh1Nk3j5BlALi8tL5wYQcJdGWhGsg3VX6adEnZS4NuFzqqwtOIjrU7mWwVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=iwwRLP9YH0VKCyuLV5ihMenRk3jhVYesgmSpATf1YnETtrIitD-YpP9gU05RR_CFk4meBspxAwp93AA_z6yB02EMWxCvXKbGHZdqlMbbvFNd_o7_iA9FsC6-A_OizYB9rn57yOor6X1y9e_HLWXhuyj6laJOZ45H9kQkzvHRB175F5C--5afsfCIHWNxkntFtS9JwJjDKLMHHk2TKWpynphJ-L1QvZibJl4l6pQJe-m2ZiSKjZ1Un--ih3dnmvRGzk8JHS-i_jV2_DB5Mmkgu2O92fGM0YbAqGqJuZ62Bm8hccezZpAJ0vnZKBvKUjpiGX_Qx_VvvGeJS_3jX8cdrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=iwwRLP9YH0VKCyuLV5ihMenRk3jhVYesgmSpATf1YnETtrIitD-YpP9gU05RR_CFk4meBspxAwp93AA_z6yB02EMWxCvXKbGHZdqlMbbvFNd_o7_iA9FsC6-A_OizYB9rn57yOor6X1y9e_HLWXhuyj6laJOZ45H9kQkzvHRB175F5C--5afsfCIHWNxkntFtS9JwJjDKLMHHk2TKWpynphJ-L1QvZibJl4l6pQJe-m2ZiSKjZ1Un--ih3dnmvRGzk8JHS-i_jV2_DB5Mmkgu2O92fGM0YbAqGqJuZ62Bm8hccezZpAJ0vnZKBvKUjpiGX_Qx_VvvGeJS_3jX8cdrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScyfhQTgqXn3YyMuVHxm6y3U5Z4zeG-nFEq0SdRhCo4i0QxKBHBY6-deYjVurwXd3uzrVnxf-2tZcctOX959fdpiPGqAGLimf4_F4rZ2e6D7vEH35ElWwZuuLVE5RfeRm3XBaLQlWutezltjF5tnD5rNd3WEN_BtiRj-j-sLEbNvaRyL5MMLMjwahSep-Q-JoFE0HHJU_AkTRvhdB8aP_PKVa4Oxm7tcaVYkSByw7dLr0XV4WxBlyOJAR7NVXZphbjUp7tIiZROAeLP9kQ7urckRsCa2Fl2rlaPUNBAKo-bLHGnG9FX4C6rSckGeVPkDlJ8QzerqRYounlXBTpVugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugJqLtbJErgWfs-BRUAZXc6dWcBWWUR0tbYOyQB4U4A3kLdujes_d11j2sQjsVKuGghjQTE5CIFwMFvMvU-kJeeOIvhHslfQ69h7VbJ9HNn4ZPuS8Vkp-fbCQKuLRgMUTEldGEg5I0t7Ix8ydi5HQSmdAJ9aDkIqGwoEiV1_cV3f7L3LW8i7-WU0D05_31GaF5whFiFtBRXxUicTrCBz8012v2tbrxqG0MSedRNh0L8d9CAQO-sCyhvI3u0E0W-spYTZWvRxzLwHSG46wxEXHnZhcORj5ol8OUj6LHiUZ0RlbvMhFJOfsQRZz_6i89ce9KiT-yeakv4CDuWw_ZHkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=WGicrHbLkvSeJNSK0rUbXYsxARJI-uzc6_kEE5YuEsXdVd36mJBlorBAcY7J_4WyfYrNCBsdobT5fTzOXyzFn1czEhGBxWbPRcGa3kQtJS8MMElZfN3NlvFySn1u677VIxwa033S61TY2sdq92oobN3ovYROJKbKxJqULTh8olp8sfQLiabdQ1L2b9fMhcgHxLhMpqyuuahC6EDrraCziwUaYHcXE4BcXanpnVTHx12xSdip_Hol-xL8rovEYJeDr107wx0JyvRaiFG76KRwY5W52VtCSO2K1CgKM0r75bDfq_02LpjxRCdSuiwHjSJCkcP4xiRofcg7tFU3JkJb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=WGicrHbLkvSeJNSK0rUbXYsxARJI-uzc6_kEE5YuEsXdVd36mJBlorBAcY7J_4WyfYrNCBsdobT5fTzOXyzFn1czEhGBxWbPRcGa3kQtJS8MMElZfN3NlvFySn1u677VIxwa033S61TY2sdq92oobN3ovYROJKbKxJqULTh8olp8sfQLiabdQ1L2b9fMhcgHxLhMpqyuuahC6EDrraCziwUaYHcXE4BcXanpnVTHx12xSdip_Hol-xL8rovEYJeDr107wx0JyvRaiFG76KRwY5W52VtCSO2K1CgKM0r75bDfq_02LpjxRCdSuiwHjSJCkcP4xiRofcg7tFU3JkJb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=NHzkjucn7TLE4pEp6RbEsXA7I13_jEBZDEm6h-9o1yQRxHZEc-GeSPT3vc4ui2J9bV5zNuYXFmTbAg-XP1dLEYcQrsUDIapNCkgNPYHALf3d09dmVB81JZ_48tI8wxcJwuVvPuqid5-SXzoQIVQExkCUoeZS5hIfoW3HzMH3V5NCyqHoHfuU_-xwC69f9badGtR4clT8ALPL_Adn6aimaj90nBlu13A9z72RoSyN6B5w0r_0soMF4p1MY3SCYPLdej4w1fonNmJplIKTJjT07-F0IPL7_bcxyXsTNLW4aNpzDC3M7G3YBf2AxpA4IdCBiOU3WxyE_Vu0AFRwCF0SUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=NHzkjucn7TLE4pEp6RbEsXA7I13_jEBZDEm6h-9o1yQRxHZEc-GeSPT3vc4ui2J9bV5zNuYXFmTbAg-XP1dLEYcQrsUDIapNCkgNPYHALf3d09dmVB81JZ_48tI8wxcJwuVvPuqid5-SXzoQIVQExkCUoeZS5hIfoW3HzMH3V5NCyqHoHfuU_-xwC69f9badGtR4clT8ALPL_Adn6aimaj90nBlu13A9z72RoSyN6B5w0r_0soMF4p1MY3SCYPLdej4w1fonNmJplIKTJjT07-F0IPL7_bcxyXsTNLW4aNpzDC3M7G3YBf2AxpA4IdCBiOU3WxyE_Vu0AFRwCF0SUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN0FnZBpufmOVCHv-msJLoErjoIhm-n7VHE6SYP6qlBFpEpwSrV-Lsy8jnQkNpgds65d9o41DXzCWNAyfJAL94eBzRcyC2moaOIf1w31PrETJr1XrHjzvbH9izvlvtUM5pFfkjBNicTDVzhBKL88phbYlEdxmpBFZ4RijdgJf9rCAW5ioYVWV7ZWXA_Zqaypw0PUATeHSQxetxwR1qJAkh2nzyW7TDHuAJIrzA1aSq6DucP7mqqYRzY2-q0pHwQvLbiF7ZP7_I3xGJe9kEgBdi4LYqU5itXB--PXLXfF4-H9ywg-WniGf9ugHG4ajVg3cXMVLAYqfrLUxsboxfHBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=okEMLOzy92S4skxu5cqAIbC7Pg54SHZEMuRiEeNR8PFhbUN4TgqqdelsdTkETuKXyqW4hiRhl4SiM8YgWKZQApLpYhyfZAhvOk0xY25FpOkLNr-d2ckv-1wF6ZyjwmpxrqPXn-TmfI9xjOmPHk2aA1ykUM3XDGEAcIGzFzWrQPVLxJH26q8u8y5FReAUTkhGLunf2OXb3B2ZYE1aziqepDdvVOnGeSc-hZT9TTJWnc4RALA6RJ3m-l0XCBiIB59hKL3yzSLzTyNtVLg1lJ3UraFSOxRgcFbaPWjswaZElW4O-rmBb2d4sZlWTeSRKzgxUnjkpkY7iAr3SEBk5jRvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=okEMLOzy92S4skxu5cqAIbC7Pg54SHZEMuRiEeNR8PFhbUN4TgqqdelsdTkETuKXyqW4hiRhl4SiM8YgWKZQApLpYhyfZAhvOk0xY25FpOkLNr-d2ckv-1wF6ZyjwmpxrqPXn-TmfI9xjOmPHk2aA1ykUM3XDGEAcIGzFzWrQPVLxJH26q8u8y5FReAUTkhGLunf2OXb3B2ZYE1aziqepDdvVOnGeSc-hZT9TTJWnc4RALA6RJ3m-l0XCBiIB59hKL3yzSLzTyNtVLg1lJ3UraFSOxRgcFbaPWjswaZElW4O-rmBb2d4sZlWTeSRKzgxUnjkpkY7iAr3SEBk5jRvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjmH7r2uthmX3DAH5mwyOUg9DMJlibcfqyl5J2hTEA-tvz-OY_9Qz5ekojkaEZGFLlTr8-H4_kXO2KnNAU3DWfIx15MURt63ZcAjW0yD2XXd26cNIZky_GdBH-iVuI2ryDWIEiQ47Qg0zj4zrBK6CqJ_tHNOxK2sgyMztPNJlNENNwr3_aDhzf9doqqk3pEfLTq0MJb7AyD0L4CSPaTbfanaG7I6v0KpyWAReTBHbHGJ7ue0DP3xVGFfjwLiLQsPnTRRMmEHEC_HTUzTde2BAq1QaBODnTIDbuv0VaZiygPww9fl-LXMshE3hY47OwbL8DjlWvCCGilN4wtx2fzqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvUPSXgfyxO-BYCB7St-6hFW--2Mr204f1HQmH4Iz7bfc1ESrHX2frOluIyYaSgQKO_ItoXkyGgDSJBekoA1dt7j6eKEQwByMxuW9HS4rGfkpBgDgkQXSdJ9AwEFpoD-t0DN6GUYtRwG1ndce7uoT4k1rsG--9zewONr-L9B-n6p8JfCW4VWSATYXYeMAOpJwEupigRg4u2331HNLPoiUV8p3l-LfNmk_vuSGZxNgwE7NBuv8pbkNlD-fHQVKou9roHCeD-nHyEiCik98vbgoCej5NaNbnyh2Yl4IyU-_ROH-tEopTKBGGpG4P1XRwilkupIWG8q0yRtTLEEM3qBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak7EfahVjNtHx0-Py7qZpvXm8VZF-tACcYwVDgklKdg2L_zVCE2437qsXmkGVd-KiO19hy6wTXNu1TTUx_CNxC982HFc6ksHEfdSn-l1pWy1-j-vqgP20cH36riEcMqofO7ssIgXTeLKcUqTyz_qOeQPSnIpu_wvA5ZhAHAk2P1_SSwIwfIFGEB4OH3-gKjXX0pZpLhKHrHFV0bcMH_PNc0mwbmODGmB-6l0qLyBKOtB14jwX0J5bfhcHgG1_HOY-cx5D3mkCjgDuSmup-QNKOH4W5ZK8dwLbQSCXcfPEfpNHYQ0ADPxw_GgdZVR7o98t2caZ9cfBfcIr14E-ngNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=UGi8dWSXUVFTQ7M2PDnGZykdQIElSMcK7MHobCSpyW5lzcdW0J_NI7C4f3kg64EirpBWNL1K6c7Dl-AuMt9RoWefldzBzrTH7oY7ttX1I3BBQNpMIm7GhM2VvrGW-zimtDIJIJmqexVbkCvDTlkgm2tt6oStONERIsKVrGo_8LIliS1uK4SjploEupPffSiHYaymLEbbaiW5yxzYdBEQ-2-76rjsWOfivUdbAMXTOwvvhfJG5Wj3pXq4GpRxOJK_lEnvI65quTWYXpb4hcSjg_1iKb_nVAMZ4antxIuwvd3kl_Im7ckWdbM22M9LABoCh27QP2uVurgl5VLdpfZLoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=UGi8dWSXUVFTQ7M2PDnGZykdQIElSMcK7MHobCSpyW5lzcdW0J_NI7C4f3kg64EirpBWNL1K6c7Dl-AuMt9RoWefldzBzrTH7oY7ttX1I3BBQNpMIm7GhM2VvrGW-zimtDIJIJmqexVbkCvDTlkgm2tt6oStONERIsKVrGo_8LIliS1uK4SjploEupPffSiHYaymLEbbaiW5yxzYdBEQ-2-76rjsWOfivUdbAMXTOwvvhfJG5Wj3pXq4GpRxOJK_lEnvI65quTWYXpb4hcSjg_1iKb_nVAMZ4antxIuwvd3kl_Im7ckWdbM22M9LABoCh27QP2uVurgl5VLdpfZLoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJtE7Q3T1yJxSZMlYNtBuVnbbfhDaHH-3RNzWWcrdaWAQwksAvWQAikWDuNPd8N0FImK6lNdaAn6rhrErAzSapR08kMNNPczAnE508zXVtEpR-0AmQFxyMCBYfrH13l9bHgryKpBg4PkRMomBphr3e-edCiMWyjN26BhWpL85VXjtMdfpKv646ZWlkb6smUwmSp5f99e2eCUeDW8Pr5sueAqTqZ0qSoZG9ngxjJKdGVphn6YadTLKeGt6N3UGBo08LpZUaokz-IR7_KzCnRXJXHg_jVEPH2IluzDu05OidBEphKQvLsjwOKjbDR0yT8eDQK8OD3MFs2XOp6G08TaVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=lrjjgl8ZHA4ceJmukpCEkWG_h8tC2M8s2jzUNyDuRkECghT7tHS1t_vvRGIt-9vb9sypDFCaJiBZ87yKl3Eqrn1HRywnLV5cUCUSNdHQUo-TpMNGMPn-ElgoMQejy09aMiCw91Wo21Lamgul0OJ8j9w1Tda9lIwzP2qPiA9nI3Wzp6B81eTdfFO_ZwiZ5KqZigFvKA1dds2z45fYMYd_SLlNlh3cQDmsNDogMHt_xWmqSrZb7R3mqAbhfJ6Cc8L0hwMhr6PEfknS4yWmTUYW9LbM6xgDeZERkbVFLWLG7HNtADqkN3PcPiMRXQlxU5Q2GSOUs6UHvKfgjlYVHF-5iA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=lrjjgl8ZHA4ceJmukpCEkWG_h8tC2M8s2jzUNyDuRkECghT7tHS1t_vvRGIt-9vb9sypDFCaJiBZ87yKl3Eqrn1HRywnLV5cUCUSNdHQUo-TpMNGMPn-ElgoMQejy09aMiCw91Wo21Lamgul0OJ8j9w1Tda9lIwzP2qPiA9nI3Wzp6B81eTdfFO_ZwiZ5KqZigFvKA1dds2z45fYMYd_SLlNlh3cQDmsNDogMHt_xWmqSrZb7R3mqAbhfJ6Cc8L0hwMhr6PEfknS4yWmTUYW9LbM6xgDeZERkbVFLWLG7HNtADqkN3PcPiMRXQlxU5Q2GSOUs6UHvKfgjlYVHF-5iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=TG_DBYvoqDYDk0RS9UM2ulPpcc8vpuB4aru7LZ5rB7giizf4iw-MbtYlZuShMoz6QUq3POaCOHtJWUNfP2MdFoE4Nqs0kNEAOG02MZbGTIEcjsiJnBRe-NZGrGy6wqofalMb0pLKcLV9rz5lDQm6kvFOVAhSLTzprJj9KA0FbrQNAz9Im44XAIOYhCY7SK5msf6J_iIjbXAaZKl1md70w34iASNKoFvmP1OfxQXesnwGmQljUgaxYvpXo0uhQO_GPO69nSqQ_oRJdiglZq8mjxeNZoTJJI2mv1o8cnVlB908Y4COtb6S2esjtx5AZqEx2x0MTThggoSC9AYejQudbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=TG_DBYvoqDYDk0RS9UM2ulPpcc8vpuB4aru7LZ5rB7giizf4iw-MbtYlZuShMoz6QUq3POaCOHtJWUNfP2MdFoE4Nqs0kNEAOG02MZbGTIEcjsiJnBRe-NZGrGy6wqofalMb0pLKcLV9rz5lDQm6kvFOVAhSLTzprJj9KA0FbrQNAz9Im44XAIOYhCY7SK5msf6J_iIjbXAaZKl1md70w34iASNKoFvmP1OfxQXesnwGmQljUgaxYvpXo0uhQO_GPO69nSqQ_oRJdiglZq8mjxeNZoTJJI2mv1o8cnVlB908Y4COtb6S2esjtx5AZqEx2x0MTThggoSC9AYejQudbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk0w_06FDecoMVcRxhkTRREfEUlu_RdE2SWTlJ4MKce8vCBmqoTu6gwr6rnFLVtE8Y6x0MIqemrSe18CiVxBs4Z4XuhKnnwEGJmlUDOC6qF50D-3uATX00o75yTnNOb-wq3V1j9h17XMe-ToqvFjZTQVD1tCa7-c47QsLV_KxJbYAB9AEzzXGrV4v1LfAsn5Iy4cS78wMdHqcyeA-faV15tv8xJtyloWQ5OljPd5VbHrFZ39L75gA4hjZrLHvfktebnlU7X_uQCrSKpW1DvS3uL9b5po75Pgn4c7b2ikj4nPOo3-4sXcCxsFy9k-mgJ3I_xoN72zmMKoTHnKFf0vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=N_V0RUfxpTDpPmZWRNQBocYVp8DToeeM8rP4TF16KStYg_khDshTWS3z_ZKLv609bVca8h1VcbHt-utblmeEnBDk4bUfLWzVqMACBMg30Cyp_gglCW1i8WVUlu27ruPbFNq-V_Aqf6-aBguNWxaWdWoSoVcn7u4Jhsa5M3voTtWSPGWV7alnkE_yV_pMhxcbfGBaenM65RVYsZSwtMgspbJ1fXrqPmlWDKpGiJvX7hi0ScbUdSXcSYSoBd2IizW0pGaVNn6B8Kh3KzyQ6l85ELOg2Bz7uOzSQKyOzPTlIIjIoc7q93WSkNslsEYAsez1KzYKUdFFlWHe8NIxcwanvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=N_V0RUfxpTDpPmZWRNQBocYVp8DToeeM8rP4TF16KStYg_khDshTWS3z_ZKLv609bVca8h1VcbHt-utblmeEnBDk4bUfLWzVqMACBMg30Cyp_gglCW1i8WVUlu27ruPbFNq-V_Aqf6-aBguNWxaWdWoSoVcn7u4Jhsa5M3voTtWSPGWV7alnkE_yV_pMhxcbfGBaenM65RVYsZSwtMgspbJ1fXrqPmlWDKpGiJvX7hi0ScbUdSXcSYSoBd2IizW0pGaVNn6B8Kh3KzyQ6l85ELOg2Bz7uOzSQKyOzPTlIIjIoc7q93WSkNslsEYAsez1KzYKUdFFlWHe8NIxcwanvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=PDTAGO7rqjw4nIGpOi893tTPLwe8whF7VzDAARl015JJDgZTClkhgF-lNWc4U3NdwTF0eJe5V6lMlYIcnlwrz8rmPMiISkhtHbDqf2C_V0k8RBkts-ANr-F3Tcp-i3w3Wr1TL9102YQYciU7QvZ5ckZQY6x2iabJ4Q6LpgMR2spqtG9Ri427P--0mhJM3CLMRZdXK0cHrQd-V_k_PdGLvNtTtvCi25VHL0_h54w0qRNCM7r7086BiekYeXn7gM6p1oGJ_447C0RIlj6RI_a2_5xPNJlnTBp0pD8roj3JEJaVbG4mc39VQHHuq-HQOju5fm6TCuqbG0zXqgHNtDHY0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=PDTAGO7rqjw4nIGpOi893tTPLwe8whF7VzDAARl015JJDgZTClkhgF-lNWc4U3NdwTF0eJe5V6lMlYIcnlwrz8rmPMiISkhtHbDqf2C_V0k8RBkts-ANr-F3Tcp-i3w3Wr1TL9102YQYciU7QvZ5ckZQY6x2iabJ4Q6LpgMR2spqtG9Ri427P--0mhJM3CLMRZdXK0cHrQd-V_k_PdGLvNtTtvCi25VHL0_h54w0qRNCM7r7086BiekYeXn7gM6p1oGJ_447C0RIlj6RI_a2_5xPNJlnTBp0pD8roj3JEJaVbG4mc39VQHHuq-HQOju5fm6TCuqbG0zXqgHNtDHY0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=KWJtdA1SgzL12JmKtLsL5lSazCQ2lpSRkHdM6fWlAgwWJLd62CynvPsmevafHgLzDV61dNX9Q1ax0xJeADePLqhrumW0OY_JslNSMFwAbRJ4eYGn1EVryrf0P6SIlOLh29DySTCvsuwsg0GpSrP42pdQKx_SDfrCOi4pttcu0ZjcPeqgRLMu-bP6cABBuLGSxmH1d_hoVXzPlPFA5FJIOoPUwMSNF9zROM8MbCDhzqa53goLgd-VBdGOutXSaf-S99rywFLPDe3m3ngOSJGq3xd_3MnuUp4035aMNWgamDygKIDnr3gJpw9UFzoegXxpjR2RTfAhNM6Sto-0Aua2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=KWJtdA1SgzL12JmKtLsL5lSazCQ2lpSRkHdM6fWlAgwWJLd62CynvPsmevafHgLzDV61dNX9Q1ax0xJeADePLqhrumW0OY_JslNSMFwAbRJ4eYGn1EVryrf0P6SIlOLh29DySTCvsuwsg0GpSrP42pdQKx_SDfrCOi4pttcu0ZjcPeqgRLMu-bP6cABBuLGSxmH1d_hoVXzPlPFA5FJIOoPUwMSNF9zROM8MbCDhzqa53goLgd-VBdGOutXSaf-S99rywFLPDe3m3ngOSJGq3xd_3MnuUp4035aMNWgamDygKIDnr3gJpw9UFzoegXxpjR2RTfAhNM6Sto-0Aua2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=b_HL1M4sb5XLMkUOQL_bWV-ue5rgWJXeHnJRfLE-X0wblX1tBWzBO0gIOHC0HD67N4O09zQcX8Lv6epteGxBSYdcE96LjeMQsUkgWGziGrL5ZfQqxLEM8xvNm1xlZUyGaHhOflO29MysOA9Df80vXkrRXqLWvVXh-dden2gVn0iYd5zOTGkiqaUmy1oh9pvAZikLB3J8QQ_tVuf2aZ5Ag4iypVswD9EzvNzrT6ER__TFFuLnAhsI8wJUvF0Z-PEsgiKYcyCzd0PXnRtooLIF63-iUBZ2ETPHEjiLqEBXAw0nogk0WKl59TNt4yIudqrMDuauZyZSMRyd7VXi4o7mtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=b_HL1M4sb5XLMkUOQL_bWV-ue5rgWJXeHnJRfLE-X0wblX1tBWzBO0gIOHC0HD67N4O09zQcX8Lv6epteGxBSYdcE96LjeMQsUkgWGziGrL5ZfQqxLEM8xvNm1xlZUyGaHhOflO29MysOA9Df80vXkrRXqLWvVXh-dden2gVn0iYd5zOTGkiqaUmy1oh9pvAZikLB3J8QQ_tVuf2aZ5Ag4iypVswD9EzvNzrT6ER__TFFuLnAhsI8wJUvF0Z-PEsgiKYcyCzd0PXnRtooLIF63-iUBZ2ETPHEjiLqEBXAw0nogk0WKl59TNt4yIudqrMDuauZyZSMRyd7VXi4o7mtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=RRgRamu9cwz5jONpb4WIBANYHfYdwczNtWx6aAFFEjkNlwwPj1qeqdSl2JFsZQmbs8PzreZJaM1gAYpX1Rv2ZBEtwxHCAvomIfi8PMAdEyOw0u8wT9UzMpRpHwHiMLT8sOsY-AFdj-YFMUFhtS9d0jRId_EWxWq68aFJ-0O8ZcabYA89_KgpSUkHCbf7-Kz3P5TcpZMrpXD7g3bATY_dOggGOZGINNT00BS7oTSDnfriE2dVX0tKeqciJdqMtFCJ-iZex7lvtqHL3yLgsSSqR18E5bC2hx8wuAgxuJ6ZaL7lwyDYLRynT6I7ycnYmZ1HcbL6xTKxqWPCP6k5s8uXgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=RRgRamu9cwz5jONpb4WIBANYHfYdwczNtWx6aAFFEjkNlwwPj1qeqdSl2JFsZQmbs8PzreZJaM1gAYpX1Rv2ZBEtwxHCAvomIfi8PMAdEyOw0u8wT9UzMpRpHwHiMLT8sOsY-AFdj-YFMUFhtS9d0jRId_EWxWq68aFJ-0O8ZcabYA89_KgpSUkHCbf7-Kz3P5TcpZMrpXD7g3bATY_dOggGOZGINNT00BS7oTSDnfriE2dVX0tKeqciJdqMtFCJ-iZex7lvtqHL3yLgsSSqR18E5bC2hx8wuAgxuJ6ZaL7lwyDYLRynT6I7ycnYmZ1HcbL6xTKxqWPCP6k5s8uXgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgnJW18qu9wVBlqdfhU0ztexm2bgTHOIwKPa8NbOhYl9MnuVTmNUJPgYGMp17hY6cMneReL_SUqbPZPwQm_0yTmWvqHOQOG0pYO2FogiUSyHm943nQG07-VszBoriuyxdzR4UXCjxVkpIaf9y-UpX_qGL6aN7TKMKw99ncRnc8OYGHChqQoO9vHxciRHCK_kfq3z1Wz5VVPX5SsvVUluK1gdPSIbdddfU9nqJ9f1P3jiRL60Ce3qRvNfTPW72-pkDtKrqicFvF2zHGObGBaEVbZoa_AKKG_yiayeUiyIACcuO9PaVlFaxFDb3C9mdHN9nn3eRYoyeVKodnGdXwsBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=lkZIEuOxiTONpCZmUDDBr8LnOsyUQlSKg6a9NVJCFgjaAFCboG8442-QD6SB8WHpgEkUCEiksRxyky0EeoyroHJRI7HXS0Py6LabHAcTNgkIqAblOWL5Jp_4VP-6i-TgWuE1mFKaeusAkd4-ir_Q4OOEQBNZxJ9Au_uy7OQ4X4L-vtkbAfj9jgtyWjVMBAaU2kCeQqF603Ky23hEFa6poplIyKCzrymaZeOmTj69RXoPyfTz0hUtDSwq6TLhhFZrcF55u7c-eZSwtwD9xl0lOZK0-dTqVjjTaY0BlC6QxyjBX4ZYdq2Tqgu9Hn6wmfYp13rnYAJthXMIELzGxCgMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=lkZIEuOxiTONpCZmUDDBr8LnOsyUQlSKg6a9NVJCFgjaAFCboG8442-QD6SB8WHpgEkUCEiksRxyky0EeoyroHJRI7HXS0Py6LabHAcTNgkIqAblOWL5Jp_4VP-6i-TgWuE1mFKaeusAkd4-ir_Q4OOEQBNZxJ9Au_uy7OQ4X4L-vtkbAfj9jgtyWjVMBAaU2kCeQqF603Ky23hEFa6poplIyKCzrymaZeOmTj69RXoPyfTz0hUtDSwq6TLhhFZrcF55u7c-eZSwtwD9xl0lOZK0-dTqVjjTaY0BlC6QxyjBX4ZYdq2Tqgu9Hn6wmfYp13rnYAJthXMIELzGxCgMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRn7MonPRfxfrNtaNJzFRk_3bBlihrpipC4yzd4cDA86fRR0AR11QX6zyWow8MMgl5p5ejA9kPbI226r9Ficm_YNNqPkaxzyDWH83LbbMIHGB9Vxa2GosWA7ikNvTNc65e9IurCQiMVdlpM13iz1CC2S-c1-yOWoa1wpJmzHyp2wOjeQfey3iF8WldvczcLVv5c17jmY6Jqu7pA8RVvJlKmN5LtkocKBt56GCGPdqhCkUFqHJvkC7qi6Z6c7BdmVPdKA-WtHCd9ERuXbYEXn3DVG15y4VQT6RlJ_SQ35fvacFxdjyMlJvljV_MFGSXynDxhBFcRYcg7rDd9TwQ2Hcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=O_J3q6kUVioRQmbC_f0pN7myEMNgXMhszs-RHLQxlTQCh0hjP5fbQ6pbssjcNs_7HmJUb_iadksJRMkPCLcAC5Zfh_hCMJzcxPMoCu32x2k5OrhY5_Bk5tJ2iEUWpLn4ZwaPiQehZF-FjqgJlyRX6ArnlRrh6neBtuJb7grqM56cfWUVThT-t8wPKbB9M_WddPMIGfkF7e0lTAEWtitv1lIZehJBu9ERgq-fADYwqeTa3IUKqEhiejUav1QhAB5r7-fMt7_K-rd4hEv_YJS3skPkMpXCstiBMtahv_-igbkhvitWT2FRtwsWClqtoIGswz2HSMeCXIg8CM7FoRK0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=O_J3q6kUVioRQmbC_f0pN7myEMNgXMhszs-RHLQxlTQCh0hjP5fbQ6pbssjcNs_7HmJUb_iadksJRMkPCLcAC5Zfh_hCMJzcxPMoCu32x2k5OrhY5_Bk5tJ2iEUWpLn4ZwaPiQehZF-FjqgJlyRX6ArnlRrh6neBtuJb7grqM56cfWUVThT-t8wPKbB9M_WddPMIGfkF7e0lTAEWtitv1lIZehJBu9ERgq-fADYwqeTa3IUKqEhiejUav1QhAB5r7-fMt7_K-rd4hEv_YJS3skPkMpXCstiBMtahv_-igbkhvitWT2FRtwsWClqtoIGswz2HSMeCXIg8CM7FoRK0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=RH858bZPu1s-2OIDQO6BocYPSWMaGL4Kqg3RJiLlNiT1ONhLFCKfCr9kicxchAN55QW1ntUKLdRwa9roxO7JqjryyfeIVQU-z6mt8Gy0_F0bKzysljPLbY6nl-oj1X84ulYhZd4P1hbEHk-f4r6CNRO4ASu4eaP_3TzcBDi-IyQpSa3QJUkrSZzFBvny13Bjq6_2KKThRFhjhIbpk9wzFDCptubI2IcW1lDxkn9PrKTYQOABw6cT9Gtm61tJJM5pV67iV0YcJDITKsOVQ1a0wPC4jcs6Oh314s72VDvSOyEHwaGJlZ5bV3v6Az_d0_p__0S9nDSUKqnabE3CojuLZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=RH858bZPu1s-2OIDQO6BocYPSWMaGL4Kqg3RJiLlNiT1ONhLFCKfCr9kicxchAN55QW1ntUKLdRwa9roxO7JqjryyfeIVQU-z6mt8Gy0_F0bKzysljPLbY6nl-oj1X84ulYhZd4P1hbEHk-f4r6CNRO4ASu4eaP_3TzcBDi-IyQpSa3QJUkrSZzFBvny13Bjq6_2KKThRFhjhIbpk9wzFDCptubI2IcW1lDxkn9PrKTYQOABw6cT9Gtm61tJJM5pV67iV0YcJDITKsOVQ1a0wPC4jcs6Oh314s72VDvSOyEHwaGJlZ5bV3v6Az_d0_p__0S9nDSUKqnabE3CojuLZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=eUCXZr_MHQ8BBR99BVG17mtmo7vh_PkNpsAGFEjz1V0PLLmFPBIbs8GC9rlIfoecdvwC-eHKzQA9fKnr6MXBKVV1NBa4Sby7TsmlYe5yNs16I4IvGCaAnQgsinWWpzZ16BrsNgyMfMsqBHNBA4pwp4w4V9JIzorABAtZ8kIF5eAnDJ-4VY1VF79HkG3sk_Nq0RAvNp0N0Uc7dxPE8ENq2nRz9pwjWMOBbLQOl3cwsKzlJzxqwTrQl7l7aMJe_GW0ErFQt98qJWdvuxF9TexCf5b9g_3YxexwK8lx0cCVKTinc7dX_RTbyxwXC0heq3iNepoW8SBf49lzITZJd1GSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=eUCXZr_MHQ8BBR99BVG17mtmo7vh_PkNpsAGFEjz1V0PLLmFPBIbs8GC9rlIfoecdvwC-eHKzQA9fKnr6MXBKVV1NBa4Sby7TsmlYe5yNs16I4IvGCaAnQgsinWWpzZ16BrsNgyMfMsqBHNBA4pwp4w4V9JIzorABAtZ8kIF5eAnDJ-4VY1VF79HkG3sk_Nq0RAvNp0N0Uc7dxPE8ENq2nRz9pwjWMOBbLQOl3cwsKzlJzxqwTrQl7l7aMJe_GW0ErFQt98qJWdvuxF9TexCf5b9g_3YxexwK8lx0cCVKTinc7dX_RTbyxwXC0heq3iNepoW8SBf49lzITZJd1GSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=l6me_KVMWzCCI4eTVqDD8qMuVAf5MxcG1kq2BsVZeJ9qruwm2vFbgcwd36F0y9XI13LtemKBPL7N6gz6eDLlA3VyBZTVmLtJUTjFPPf49kEQuDPLX-zttBAKFhdvukh6VAPSjQ5ZN3pwwU8N3DUBibkw8AQh_zINE2xbZ4NqyrEexS4ODHr6kWHYGAtkYpv8Lk8U2lAlb8PwgHJytAy-x_ic4xwEqncy7ZGWtYuyr17pRuSmA9kbRS-Pl4JE-UYpQEII0PQVQsjb0UDMLQdHWgRVmQzMdqRLlmvFFG5d4uwrCiXU9l9ycoXjX-whnYhTOUQIZtkqZ9RqsIQvnonL0V_vevTesjcnDYdNivOYoqft4NY1Y2id94S9IfIJBQLeqCLD_iT-lWKkWx_ES3TPHCHiYbC_PPPrs-o5OgBEoI7jwcR7ed-R__mNqU9d4AO0TyR5xHQreaDk2CWbCp5I6uhXYUR5_mGDXBulrceGF-gTXLhjk7E-JOi_x84Ea74lpXtIITX9Xo8pekR8JtUUjOhcWvbdqYW1w_i3ung7FCGkWpRuKmf-_diW1gTxaNPNdnklSu4P76ycGLBtCrpZ6oRD6ZXrcBHc34fnGYtKs46MgKwppADjZaEzNmEaM49sG_Nbi_V8Z6SNmvemkcp5dst_G6ukgy71txNXp1OwvFo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=l6me_KVMWzCCI4eTVqDD8qMuVAf5MxcG1kq2BsVZeJ9qruwm2vFbgcwd36F0y9XI13LtemKBPL7N6gz6eDLlA3VyBZTVmLtJUTjFPPf49kEQuDPLX-zttBAKFhdvukh6VAPSjQ5ZN3pwwU8N3DUBibkw8AQh_zINE2xbZ4NqyrEexS4ODHr6kWHYGAtkYpv8Lk8U2lAlb8PwgHJytAy-x_ic4xwEqncy7ZGWtYuyr17pRuSmA9kbRS-Pl4JE-UYpQEII0PQVQsjb0UDMLQdHWgRVmQzMdqRLlmvFFG5d4uwrCiXU9l9ycoXjX-whnYhTOUQIZtkqZ9RqsIQvnonL0V_vevTesjcnDYdNivOYoqft4NY1Y2id94S9IfIJBQLeqCLD_iT-lWKkWx_ES3TPHCHiYbC_PPPrs-o5OgBEoI7jwcR7ed-R__mNqU9d4AO0TyR5xHQreaDk2CWbCp5I6uhXYUR5_mGDXBulrceGF-gTXLhjk7E-JOi_x84Ea74lpXtIITX9Xo8pekR8JtUUjOhcWvbdqYW1w_i3ung7FCGkWpRuKmf-_diW1gTxaNPNdnklSu4P76ycGLBtCrpZ6oRD6ZXrcBHc34fnGYtKs46MgKwppADjZaEzNmEaM49sG_Nbi_V8Z6SNmvemkcp5dst_G6ukgy71txNXp1OwvFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk-VmL-DJodwN8Zy5hGYcIe9CV1hIMqLiiWLhz0kG9ze8IkVPyjXf3elp7HkPzL4ru_QC2qcMnY1mgzHEK8LE4BtJm4mlz02Cn59SaC8u4Fp6SvkPXPavSrv2h-XcnqWTOgqr_SJon3LDY13DBXsvXHmvE2pDIsrzGcGw3HywBr1uZmJjMJ4GoZqMWFjUSiN8Yxho6zPOu3XwpjJ1Ajs40s3hxsWw19YGsdeG_Ssa6284YWi-kpqAG4wWWAPe8uUwnMWrlkq5PUC6bnRI88i4Y11DxPGQ1f88nxpk4BeiF1AIiD4QZtyMxyZ_Gx8OpHTzLQrIchi29kh0wybIYWvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=J5t6gI8KT6Rf1BGYkuRmqCX6R3B4X9aDIlUIQNzC5gens0aJXzJqsfdcYiqTSRp7L_6ulIAOWinQlyPtP6Dc7H9f0PaKLEkljoyI10tbcLb3dAuQ8rq33_46b6-vEndDFbAghOMWFeNkfBWM0pHgobWY3AKaws5k1BR9je3skHvCf8XyoI8qDKfMzj1MAkwZcN7_-WCGWTaRqFWm1OMz0ZR6ogTNsm4sRmDBB_Cre_2lpPYX0ugDGn78_V8tyMBdpssmuSfjhvBy96OG2D-xrdq5oQUCzAQuIMZWi7uPlmw1Xc3ZnMlOFywC-duAWgpOJT88LtA7_Bf7vzf83GNOeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=J5t6gI8KT6Rf1BGYkuRmqCX6R3B4X9aDIlUIQNzC5gens0aJXzJqsfdcYiqTSRp7L_6ulIAOWinQlyPtP6Dc7H9f0PaKLEkljoyI10tbcLb3dAuQ8rq33_46b6-vEndDFbAghOMWFeNkfBWM0pHgobWY3AKaws5k1BR9je3skHvCf8XyoI8qDKfMzj1MAkwZcN7_-WCGWTaRqFWm1OMz0ZR6ogTNsm4sRmDBB_Cre_2lpPYX0ugDGn78_V8tyMBdpssmuSfjhvBy96OG2D-xrdq5oQUCzAQuIMZWi7uPlmw1Xc3ZnMlOFywC-duAWgpOJT88LtA7_Bf7vzf83GNOeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPkcrHyCEZdUfsyYotfMK9t1dMCKkrPCt61UFWluUzoM4AfXnIyraaZnPPTNXIgb1nKNEDN2lcpp8J6uFPGWE6NPfs1t0ahNrLzLLqIJjBy7KFDz6utnH5iCYz6B6_VvQp2BS6jYRFW3QF2j6Fq0WNJjMFbKeVFAzA9O65OQGlCcUUrK0j_DL4bwG83baVjuDmNTSc1hL01pryBe_EywNQTbbN6skAAqm5eUn328JOkG22p8drMpWjht4Qxy0v6kRn04HKNuDvLrWDXdzbR6JdJSjkam2UmOJce__vyF6oybqNusBfKZXmTOKGAKoV-AR_YBLXJWGzItRGBx7twD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kevH6fi5oyJ29lAH7AKMIG1Gc77hEO4H8YuUCu6jfrAe6s-ZPvL-vewnF6e54el1ECKtdbwFtmV2YqkwZorF8fF3OOqEQfGVE9tbyu5LXsSg016bmpASvjPWC3oCMKn-ackqNd5aChCXid1BiPswpDNwnNgcVmLAcVucPNW-e0IpTAFWPN8C2lgcG5Va_7nqsC4_FzsJr3ATDA3of6xnt2JVsonRrB1dPLViz55T1UTgmSmY3eNI6I4gSly1t4DKd6XIj7z6oB829U6JTvryBeKo99KMpP6Ozk7qvfFPdmnYCkPjFlozz2KbVQPOs_YGrUkfrewDjQOIavoEzW6e5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfweIT1s7uL0Jy193k4LaL8uhYJj5-9gsSbpg-oaHBlaCficSY3IEfpWtVeIrY30uj-ke1i-QWutnNkGcaou_7euoDb4FiMDzPqnG5H2f0zx5ODEDu73sHrOzmIN5CATPzGBLKtl1bISb-G8OmpGw7TMpwMG3zw9PFlppxVdo-Cm5Pc2v2DcTtp2uqsiNMD23mfTByGJF1yiWY_4YqsXP06JrLnxCWq1A5CyDKo_xfIrpuIwy3SSMCvI4dTTrTfwgutwEQK6EB5COiAWctKPN5uUZyRfKImgoluWVcTXHrWRPWzPCRtklnkDpNzX3HdjbE4LZzdOADbIIgvNHnw33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmQKTfHNd2hhf_OKATdr5YdsIXfuT20KCfMTUJSccg0zVatdru5ukPZ6QG_nqX4_xixNiVcSp1-xwv8zwqQVnZaVWu4HhYbiVRP8NmMaBIZ6nAMe5IfYAwaQ3zuL6oeXZjUVmMn5dcurdqC_TUthmNKmIZtW-WRXL8brriYRi3NOqLX4X4BhSZJRhK1uk0L4TVn1OH_uUGRVi_9ya5atM2txwoFKaVt7HqWRGbZrwFRVMxrmGdZdpD42z24vYKZCCI6miL45I8bECy8nmpq-fRfRGTiqoImnB3Wni18CUykoOekWu9f-Pw1x9fwAEwfYq3my9pL48fCKLPedhlkiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNDixkRvy3ZQISsZVlUIfIciYtHScuJBCKKDT_m97T3Z70ieDnMsoYO65JVI4cFkyyFC-3Ej4RmyYOlBcJGZ0EkzTlmC_h-m1NNsb-4LCOWDsjn0pe7MywSxOGbJrRLaaedabZbxVL641knn9KbCp_wGOxJsZnFzKyQ-le6gLNUiu0zFy37lSJbA2okbL_QpNU3eYoVHsLQqRH3l9F6fixj4Cj_dpAjitzUBuAcSXTB3kq-gGuct8a_VQ5yEnzdOp_f0dgsoWBlE81gcpjDuBWHowvUePnglQonaLGf1JZ6JnQa7ZIZW_q-bzd5mxsHbCrl27odf0IVr0rcXnqWH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUZITPI8DxhvxvbyGnRVzAWCBenrBtfYj3OnJOg0q8HVmheZ1PZGCkN19SqD7RKCBxSqRqF_m0VIT2AhxFKIt3FYjTqbu19VuYDtkEgy0-6F9jK3gkh_HfMu8EnW9vFGRJfJxzNqUXtFNqaUkjjW0OIGAKl4SwRBItZRq-UNZ9UUHSBroxSxN8O0fN8SmmDM6AVKJGZ4ITUkRZ3QTti7bpiNK6eyaUE5sNiYxNQq1LTpJdezyQLc2E4St5VNfqQl-YgHwtj1QO58sHql-0TI5SWsPomKaeESHoo5gC4L4uZO6ySUqIVRktgv9a4D-AZw-YCNfOTW428-xaNIHxH1jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=tLN3uABf2diUjCGanbn-DOim5MpL8x6Ku1QuV1JcpxlW_ZHYXW9lH1GJ7zhKqPC80hW3cIG1W1yznUmPsKAiOr6CO06kmz_crXSSIKBwcX8udvL9luPY9uL8lnilGYG9mvgoNsxBMqr9y7ua6HWhNGrKvErEav_5vHIOUvR_kvIf0QtHYstIcSdxEDtHSEiHXCZ20G1JwmF4qYsJV9mVM2JQOtFGjOAubWggSBpoN8b6DRBmRDzPA1N02TY3ma47ejOvPNagA9JqW2HewehALTc9pTEJC6GCsD8nS77lDHiINBp55qrhpAr2vq1gKS6UGjufdaGycclQ1TaID8x4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=tLN3uABf2diUjCGanbn-DOim5MpL8x6Ku1QuV1JcpxlW_ZHYXW9lH1GJ7zhKqPC80hW3cIG1W1yznUmPsKAiOr6CO06kmz_crXSSIKBwcX8udvL9luPY9uL8lnilGYG9mvgoNsxBMqr9y7ua6HWhNGrKvErEav_5vHIOUvR_kvIf0QtHYstIcSdxEDtHSEiHXCZ20G1JwmF4qYsJV9mVM2JQOtFGjOAubWggSBpoN8b6DRBmRDzPA1N02TY3ma47ejOvPNagA9JqW2HewehALTc9pTEJC6GCsD8nS77lDHiINBp55qrhpAr2vq1gKS6UGjufdaGycclQ1TaID8x4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=nHXJ49Qclke6Z07uQszXo51dmXjxE2YQKkukViIP0-ja2FR55V0hIRMZKE41OS945nOFmrGDm31AlVhej6EfD22vaJXTZc-C6Z0LuGKedCuyxgtORwbk_wSmDT7OEKYl5fcbGY3Ov2lamdQz0ac8xET-0ZCwW_VQyQ7YVKFvcYEehc3bdMps8wp47S1cTLuhnPnDh27djA5mq83I7IJzN4AJ25cLyu0Flp7uah2DDIfduc9iK51tApt4rXG-oDVwc0izP_n54jmgcYIcvvFyJMPbYwl4zlLOgNbKnjBPIB8NGyAv2EdFh8_zjHzbnACbsuU6URDB3kdHh7zycdKaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=nHXJ49Qclke6Z07uQszXo51dmXjxE2YQKkukViIP0-ja2FR55V0hIRMZKE41OS945nOFmrGDm31AlVhej6EfD22vaJXTZc-C6Z0LuGKedCuyxgtORwbk_wSmDT7OEKYl5fcbGY3Ov2lamdQz0ac8xET-0ZCwW_VQyQ7YVKFvcYEehc3bdMps8wp47S1cTLuhnPnDh27djA5mq83I7IJzN4AJ25cLyu0Flp7uah2DDIfduc9iK51tApt4rXG-oDVwc0izP_n54jmgcYIcvvFyJMPbYwl4zlLOgNbKnjBPIB8NGyAv2EdFh8_zjHzbnACbsuU6URDB3kdHh7zycdKaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=E-VduQz2rEH4ZCzzabV0QoqxQUYLXdgBOtYwRdCTZK6SP6mPKrtzrUHF1XuDrWc79GOUmcuMwd_7jhSW25lpSp7JVk49Pm6qQu8q9h842DhqFO205ZfDFoze3x6k8B4luMD7Zm1C7euzozwwgiOMYUBUGylTnnASZ6Hopk821QazkXJa37uI0GfUNBvAup-YBKp5moBx2VwSUlGzfkHBBRUaeyyN-M19xMhVIyx9fHyFWfIr5jtFOalorKuWnUYJQKh_Mjy_1Ur4UarGwTdJ9v1mpTJfEDiEfh4to7f38INLgCR-hPEnHpASnpdaTH_ah42ueTWAFKPBvx2zl4mWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=E-VduQz2rEH4ZCzzabV0QoqxQUYLXdgBOtYwRdCTZK6SP6mPKrtzrUHF1XuDrWc79GOUmcuMwd_7jhSW25lpSp7JVk49Pm6qQu8q9h842DhqFO205ZfDFoze3x6k8B4luMD7Zm1C7euzozwwgiOMYUBUGylTnnASZ6Hopk821QazkXJa37uI0GfUNBvAup-YBKp5moBx2VwSUlGzfkHBBRUaeyyN-M19xMhVIyx9fHyFWfIr5jtFOalorKuWnUYJQKh_Mjy_1Ur4UarGwTdJ9v1mpTJfEDiEfh4to7f38INLgCR-hPEnHpASnpdaTH_ah42ueTWAFKPBvx2zl4mWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=U78hfOlY9vmohdGpOxWehkYfj4hSsJEYRoYAnxIN2lcS9KAi2sLHzCV6YdkVil-HpOoblMmbaByEjabET0KWL9Ej8RPYprDoLJr3YOkIDu0jOpYrh6dFaIMgSKhxWNiGQTnNd4X3byPDR6fCLO_tJHZ7lO6sCY6TGSQkbM5iulTxMWzvyAAR18l5LewfQdP0eizYYyYR5swiCiN6_3ImHjZ32IUB2nq-lGyyzBCNev8iJ_rYJ8M9ZIuF0vsEMZMJmMYxIbeE8lTl1UmDZaQVclHfj9lb9EBU_1QDg_O0HwoiLtPVOCmDrGjStG63PTPw51JuJjTX22FRVF5pNBV1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=U78hfOlY9vmohdGpOxWehkYfj4hSsJEYRoYAnxIN2lcS9KAi2sLHzCV6YdkVil-HpOoblMmbaByEjabET0KWL9Ej8RPYprDoLJr3YOkIDu0jOpYrh6dFaIMgSKhxWNiGQTnNd4X3byPDR6fCLO_tJHZ7lO6sCY6TGSQkbM5iulTxMWzvyAAR18l5LewfQdP0eizYYyYR5swiCiN6_3ImHjZ32IUB2nq-lGyyzBCNev8iJ_rYJ8M9ZIuF0vsEMZMJmMYxIbeE8lTl1UmDZaQVclHfj9lb9EBU_1QDg_O0HwoiLtPVOCmDrGjStG63PTPw51JuJjTX22FRVF5pNBV1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=dcTDyIOKdt6hBsaJwKwf6xe6GCVQJ7FzXVxgZMK-0pEiG7JKjFwEptcE1YB0IipYnzOuNygmfNxotGXnH9x1h0j8RpJfkrqizzKb3GlWd9H682_9KEiYNHjKHwa1m54QbRjxgwSYI7F85DA9K3TB4oxLBGFn0DGykRGrjlcMHbRdUDrQnT1GpvDeP0GgPep4DiPMU7S0mv8eX_vZZ6OHsgxb6aSxodnOLxkMG_4N5PxLtyj0tc0aUvE_Tr46Cr-rxj8SsUJykGu8IC4EdQFVPciJ0l7MLITkhESIBdPUzmRSEnjqDv2YovAlVBE4MK8yfGA5cJhjaZI9LcIx88Wn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=dcTDyIOKdt6hBsaJwKwf6xe6GCVQJ7FzXVxgZMK-0pEiG7JKjFwEptcE1YB0IipYnzOuNygmfNxotGXnH9x1h0j8RpJfkrqizzKb3GlWd9H682_9KEiYNHjKHwa1m54QbRjxgwSYI7F85DA9K3TB4oxLBGFn0DGykRGrjlcMHbRdUDrQnT1GpvDeP0GgPep4DiPMU7S0mv8eX_vZZ6OHsgxb6aSxodnOLxkMG_4N5PxLtyj0tc0aUvE_Tr46Cr-rxj8SsUJykGu8IC4EdQFVPciJ0l7MLITkhESIBdPUzmRSEnjqDv2YovAlVBE4MK8yfGA5cJhjaZI9LcIx88Wn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=rOAPmE9_1L1SOQ9_5A8NnlFl_f1J4SKANqoxrzatLbkCSgA1yO0snZWuARSNODxCve47JA83xOfbfW3liiAzzm_ojWVDQ-LeTa-qNkfuueAhdsusjZYBXxkyShn9DaebdSF-U2mHS7UOeo4U_CAI6KhhHpw8GJ1g2tmFBBqZ81ynOtjOMQQkqD4T3A-N92-o_vcbCuOGnpWPNd_PTN8aFg2sbfa4rBdPSE6toDrHX830CPdSC5Il5Qc5uyRrzxxPluB2QinQcMpnGj13ZkHt3GB00XVkCsWWa_h1vY4GsTcqoUOpoZzTEnkH5tCR7q1RKjqIjgcSzkycRwMhV5w4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=rOAPmE9_1L1SOQ9_5A8NnlFl_f1J4SKANqoxrzatLbkCSgA1yO0snZWuARSNODxCve47JA83xOfbfW3liiAzzm_ojWVDQ-LeTa-qNkfuueAhdsusjZYBXxkyShn9DaebdSF-U2mHS7UOeo4U_CAI6KhhHpw8GJ1g2tmFBBqZ81ynOtjOMQQkqD4T3A-N92-o_vcbCuOGnpWPNd_PTN8aFg2sbfa4rBdPSE6toDrHX830CPdSC5Il5Qc5uyRrzxxPluB2QinQcMpnGj13ZkHt3GB00XVkCsWWa_h1vY4GsTcqoUOpoZzTEnkH5tCR7q1RKjqIjgcSzkycRwMhV5w4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Reoiqubt0j2DAJAvsXXvwuucJyc1ynQmzLQ4mnkgvy1pV3JYwTFhJmTk8TnAd6To6qTOl26-rR4iDi_ec2WqA3UScz6hbqLejHHk2dGo3uNw12wKquki_-NQwvXz3FfKPSEnOOIpewUneSisybR-sVPOXTN0j90dJL8fr8E1-1FUYnApCYkzdlQosBVt1XlOiKS58F3kZ0YyfQHlozJtYNGdlRk6KmBOWkUe745SR2QgrisAR2BSDlh-lI8sou1Z1zOmPhSbRkJy35sKW8PUIo132GW2zJDTI4usWqkL_x0xzi81XXyAdxuAC5eXckZNjQzwjS-c-SxOxpY8VKP3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LviscILBDNSJOYXTEi4SNH1gtiUJ-TYJYx5b3cUvYhBaqYaGSU44TsOpeeQVRm1LPMw2MkQZ39EAVQk6LovC5r7uPT3_T4wCYiutsydCFyIBrrkPWknU8h3u_-8l158_kTUtenEAL9dPq8hi104wNaLZxX4oXb5lObUxbRiflj_O8hUi2qoE2yo8n5oJj_prKub1zLTLfRRfvx42ImlN3AHy3bx3xAlUGQmL--8yBFDFWhi9aDoV2hTBiUA0gQsof3HOonNu6o9CXAROYMeOZoeaXEcmdNQjM9A6rQD7otSiA9OLMJVv8dq0-UHRrXHDZ6k6Q2Z5gF2CwIGtnUDnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDW7yy5PQ9bdn_21FwIgqRp3vhI_EngeopvLGms0JQHWhCEppBVuM7GfskzaU8EPbu4mZ_biTgxRYtXUEr44tu4pEwCnn32CaoNkdkZOCwZ4eYBEOUsYmUD6y5vNw61Wy-WAT2-FDddwAFlGtTL6dp2lC2I3LnkwyKstKGYR7-GV3tdA3J348SE9lj-LHVjGYwt8qiRusNoZ37vznJepSZNqUlw82DMAwcH3yAfs3L0__ngauFw50l7CPbHmS0l2qxY9I222uwPf3fqzfqi6xhMt_4cjYKJDBstK78MLkv_CVA8VQE8fNS0TujtGoZ9VUsnULv05Ce41saPnovEloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=lRMEkJOpOG05PkIWoCx5aNodqMs6v0Nxlfqu6bemtmG934PJxRbjzJsaj9kGK7vsrIB0vAuNvmhepacvD6IFRsVvYhNzuoLdrFpHMbcQnnZqqcbhB1JJ6DrMGWptQEnNDD-gEzq6DqPAx02L3-0U1ezolnpu4816zYDkYioaYPieDDHO13NEqqqP0Gyxn6cVfQ9aemR-E1vpaqRjfwUklpI7O9oTODOJw4XGeIRyXIP5-4Pt59K9bYVnUp8PP0o7ANjW9_pqSTLhxfmubvdl4qh88gmtHyJqoQBCyjkMvpsu7AZ8Ec_EBNaqAliWwhrkI0SnCOXbHYHQ-jVdoQAqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=lRMEkJOpOG05PkIWoCx5aNodqMs6v0Nxlfqu6bemtmG934PJxRbjzJsaj9kGK7vsrIB0vAuNvmhepacvD6IFRsVvYhNzuoLdrFpHMbcQnnZqqcbhB1JJ6DrMGWptQEnNDD-gEzq6DqPAx02L3-0U1ezolnpu4816zYDkYioaYPieDDHO13NEqqqP0Gyxn6cVfQ9aemR-E1vpaqRjfwUklpI7O9oTODOJw4XGeIRyXIP5-4Pt59K9bYVnUp8PP0o7ANjW9_pqSTLhxfmubvdl4qh88gmtHyJqoQBCyjkMvpsu7AZ8Ec_EBNaqAliWwhrkI0SnCOXbHYHQ-jVdoQAqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUD_pz9lQlR4lswnIh3r1RPqbwqXU2suyuVoqoQAbGdwWLQvmr6w5nSe5khGOyHSuuKsLPC_j2NjnvrkcD3hGoeEe4ijRY2vGo48XtR3_01xlQzosJZHhKYoBs_Z85d-bccAfbxiNnXIiiLScVDYBGEeh5JROVuclFRu2QLTuEfGjiA_fyaFWtuYwAqLWzKYV4dIaXEV3Il-iBB58hyuuJhsa8Zazn_GrndXzfJXucBl5CzysjmWxL5CSwcjldZ1zxPwKotC-bsF1ggSvpTy_owcaysI5APdv9YQo7c4ExlDyddsRER09HbZzDoxYgy5ROl6jywE3iZafgxXoI06bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

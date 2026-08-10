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
<img src="https://cdn4.telesco.pe/file/DRBtILlBgDCscq5wVankHvtASKsJrPY1lknAwlCWbmAY0ZUtqidKXF-qmGVe9Km7NvN0PeV3G--_TRUmMfH78Peu5tCOoLOblKwGBY992NosEboNfeXrkhvZQ57wRFiQHAzL7NJFJM0yo3I_YJ-fd3O08hlM7jC-WYtdfmdiYJv5g6JBegh3WHh87jn5sjQl7GZCzF_tCZV_sKU3G8skoylWb2o-5fx06dypkiNDdCqA_lt8JqPCqLF_iGNfeAQ2ZQmrXd8wBgpO_-7Kx0iRAe4VX7X56-oGKGrzclwIkzl-eBdH5lXZo_4CTj09HaIqarH63ku82yr2-3RPfnnkLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 23:37:40</div>
<hr>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SBoxxx/19886" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟
ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/19885" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_تا_چه_اندازه_می‌تواند_تنگه_هرمز_را_به_یک_سلاح_ژئوپلیتیکی_تبدیل.pdf</div>
  <div class="tg-doc-extra">538.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکات بسنت در مورد تنگه هرمز:  تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.  آنچه در 2 سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/19884" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuEmC3G8gEYLkyolnyCfwGzS1uZMDDiux9vssIahYa5ulKR553Utq3ofkLWv6Ui7WEk0TSv5kfhu86QP4ujw_cAe2KWWqlaRKkVlBW1pMBcHt6OWQMxSLdZwtw6aMYjAWv5TkHQcd4Wsd43bYbdSl8MhFJKAqdZ8k67NbrCD7k1GKo8xU-Xs9ZnHq0AyICnUqAhkdn-G7fil3YWDR6sYbBoOadmKIEDuzgEkN0FkzAKG6xdqvMyTKaVBEGvW2cOPB3BWeJ91G6EcKWx6hvvUhPB7JQvmXbk6ASt9W6BaHYFQ_Js1U78izloh8-hxjNnEQ07uSkjZs3NvOYiLxhL8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/19883" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/19882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 22</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/19882" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکا پس از سوگند یاد کردن آبلاردو د لا اسپریلا، که با حمایت ترامپ به عنوان رئیس‌جمهور انتخاب شد، متعهد به ارائه یک میلیارد دلار کمک به کلمبیا شده است.  او وعده «جنگ تمام‌عیار» علیه تروریسم مواد مخدر، سرکوب نظامی سخت‌گیرانه‌تر علیه گروه‌های مسلح و روابط امنیتی…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/19881" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
🔹
من متوجه شدم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند (درگیری که به این دلیل آغاز شد که "آنها نباید سلاح هسته‌ای داشته باشند"). با این حال، این موضوع در هیچ یک از…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/19880" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/19879" target="_blank">📅 20:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔖
واشنگتن پست :
پنتاگون به مدیران صنایع دفاعی ۲۱ روز فرصت داد تا طرحی برای تولید سریع تسلیحات ارائه کنند</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19878" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl8iAgQuvyVGREgLqf2Xd_BSJBHnrLExzA5h31G3wOuEGXiQmuo4D3kZA0kF57sdAbejSH514fyqOWmcoyW6bQz2gW205xUs7-rkfsxRezZuCFpWaVNUzmBjOx2Jlo5iDbjI83dVP7CicfvKsXe-1BP_Dgo8ki7MD_py3EPrdfglK8ZqkLOomAA8ZeTxcpyvLIEnFfavWDrkguTf267Ah9arFUV4xnEr-ATth_A--bIQXbCnf70PKYTeDbazB8L-R6GoUMXPFUZo_UZGoA3E1-KBdRgpPDnpkDSc3fwmHQ2qF-mtDunYawjBsebUCndPuBYPu6b1yKrHK5KU_Bxueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
قانون «لیندسی گراهام»؛ تشدید فشار بر روسیه و ایران و آغاز یک جنگ اقتصادی با پیامدهای جهانی
قانون لیندسی گراهام با هدف تشدید فشار اقتصادی بر روسیه و ایران، تحریم‌ها را فراتر از کشورهای هدف برده و خریداران انرژی آنها، به‌ویژه چین و هند، را نیز تحت فشار قرار می‌دهد.
اجرای این سیاست می‌تواند جریان تجارت انرژی، قیمت نفت، تورم، نرخ بهره، دلار و بازارهای جهانی را تحت تأثیر قرار دهد و تحریم‌ها را به ابزاری برای شکل‌گیری یک جنگ اقتصادی گسترده‌تر تبدیل کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19877" target="_blank">📅 16:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVwfHDa8rjw9E77AQ72s5OxY9ME5MBamOh8QPNClCEQLiEHmf8EpZgd2OqN0FTdZ-IuwWJLBEo490XNYM16izwSkxQTNySMWPBowiMr9S13Alj5pqnJhy2u4Wi0mVYydPadLQPGtKh2v6WNt_6_Nh3TAN-I6KalDnsXqZSA7xGdP1-nKVhImGaMhAEAxgjq4HQJBTs1mAN4tzBn9TwTrUsxlW-_sk_jNI7UOaqlRD-R0kV5njKZKfyTnL2XW2KlbOwYaNRX7afp5hz6gyloPrYIZNWWxfDdghC9D4jfcB604CkPwIDiOpIjVhvL5TdihZYmOaDiMl1kd7QE062fvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/19876" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 22</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 22
دوشنبه 10 آگوست 2026</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19875" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">— وزارت کشور عراق:
«هر پهپادی که بدون مجوزهای لازم پرتاب شود، به عنوان عملی تروریستی تلقی خواهد شد».</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19874" target="_blank">📅 13:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19873" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19872" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل:  "عربستان سعودی، ترکیه، پاکستان و احتمالاً مصر در حال تلاش برای تشکیل یک ائتلاف دفاعی برای مقابله با ایران هستند."</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19871" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr1LVsfr_bYJf4XcS5TFrPg9n366TuvlALYC89OYcUVbppju4-f6sUxE5pvVBDxifRy_HKjjGB5EtMjWwXNUWCsHMro9PEp4Eu7SM7keOb3UKkX5tiz3TbK-KNGaVM4Xp42coJRS3b0axSh_QXew2xWnRH6Vw9-znTfV5YpL6pTwoms29B2STHelo704Xg5nUC9IWdTWRZ4jTyWxrG28l_nHoN2LjIhAAM3pvM5Y1o8Z4Rhd48gu7OdvzL8rfKom-X6p2Yk6B1HYts-c5j__eyIW-wummLW1yut-ICqY1zN2zRu7KXdeH6YVRxiWE3nZ2VDIcvChDQI2cOsUj0FnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل جدیدترین و پیشرفته‌ترین زیردریایی خود را از آلمان تحویل گرفت
شرکت آلمانی
ThyssenKrupp Marine Systems (TKMS)
در اواخر ژوئیه ۲۰۲۶ زیردریایی جدید اسرائیل،
INS Drakon
، را در شهر کیل تحویل نیروی دریایی اسرائیل داد. این زیردریایی، ششمین فروند از خانواده
Dolphin
و سومین نمونه از نسل ارتقایافته
Dolphin II
در ناوگان زیرسطحی اسرائیل محسوب می‌شود.
دراگون با طول حدود
۷۳ متر
و جابه‌جایی بیش از
۲ هزار تن
، بزرگ‌ترین زیردریایی ساخته‌شده برای نیروی دریایی اسرائیل تاکنون است. این زیردریایی توسط شرکت آلمانی TKMS ساخته شده و از سامانه پیشران مستقل از هوا (
AIP
) بهره می‌برد؛ قابلیتی که امکان ماندگاری طولانی‌تر در زیر آب و انجام مأموریت‌های پنهانی در فواصل دور را فراهم می‌کند.
ارزش این زیردریایی در منابع مختلف حدود
۵۰۰ میلیون یورو
برآورد شده است. طراحی پیشرفته، برد عملیاتی بالا، سامانه‌های شناسایی مدرن و ظرفیت حمل تسلیحات مختلف، INS Drakon را به یکی از مهم‌ترین عناصر قدرت دریایی اسرائیل تبدیل می‌کند.
ورود این زیردریایی به ناوگان اسرائیل تنها یک ارتقای فنی نیست، بلکه پیامی راهبردی درباره حفظ برتری دریایی این کشور در محیط امنیتی متغیر خاورمیانه و شرق مدیترانه محسوب می‌شود.
در سال‌های اخیر، افزایش حضور نظامی ترکیه در شرق مدیترانه، توسعه نیروی دریایی این کشور، برنامه‌های مربوط به زیردریایی‌های جدید و رقابت بر سر نفوذ منطقه‌ای، اهمیت توان زیرسطحی اسرائیل را افزایش داده است. زیردریایی‌هایی مانند
INS Drakon
به اسرائیل امکان می‌دهند تا یک ظرفیت پنهان، دوربرد و مقاوم برای جمع‌آوری اطلاعات، عملیات دریایی و ایجاد
بازدارندگی در برابر رقبای منطقه‌ای حفظ کند.
اگرچه اسرائیل و ترکیه در مقاطع مختلف روابط امنیتی و نظامی داشته‌اند، اما اختلافات ژئوپلیتیکی دو کشور در موضوعاتی مانند شرق مدیترانه، منابع انرژی دریایی، سوریه و نفوذ منطقه‌ای، باعث شده است که هر دو طرف به تقویت توان نظامی و دریایی خود ادامه دهند.
تحویل
INS Drakon
را می‌توان بخشی از راهبرد بلندمدت اسرائیل برای حفظ برتری کیفی در حوزه دریایی و تضمین آزادی عمل در یکی از حساس‌ترین مناطق ژئوپلیتیکی جهان دانست؛ منطقه‌ای که رقابت قدرت‌های منطقه‌ای در آن به‌طور فزاینده‌ای در حال افزایش است.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19870" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، چیکلی:  اتحادیه مکه یک تحول بسیار خطرناک و نگران‌کننده است.  عربستان سعودی اساساً روی دیوار نشسته بود. آن‌ها قبلاً یک توافق دفاعی با پاکستان داشتند، اما به محض اینکه با ترکیه‌ای‌ها که در تقابل مستقیم با ما هستند و این تقابل می‌تواند…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19869" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19868">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بقائی:
بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19868" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6kZJRRrke2feQpaIuwQUFU_zo8ED2v9BWDMAV5BR3OVy26Wg2zO9wf6f3KhVhB0R1BEsrjnvG5ExYdrXsyANgZp4z222rZzUk8QrlFnZSqEO6hb8a-miFSejrvv_syjRKbyi-eCAqs9hMGhkl-Z5v7I5agTqhfq9sVO2USGyDX2ajpIvbQU0X4SjgjPLFf8orHM0LmfZHSbwG3L1XCUEXuWJA1B5uPUD00TS3bpp_UMkI03LvKSlf4xcvWhapS6x8LK14Z6CGHOKAK8tw1lw_BHkjKfeyMyo-mzjrqWMbG5OAYq4W9sKnRGcauBiF7LgikDws83QWNGN2XmcEkvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19867" target="_blank">📅 11:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elU4cBgrBZfb8KWqYVgHA4GmxALfZrumNeDW5wFVfldvJbjsQgMytcHB-1ERTjgxBH90JAEPZEXCx-TqLCMFUEScPFbKHS-Zdzs6lCjNwhqxU9SAZBsxntXPfzb1nbinin8xPKuc3Rxw5WymPjCpvOFJgOPJdG6na6vcY_5s7GzbPmSI3eQoYZ7pOylnGpeEX4162mUuoJ9g6uwOcZMLBobND-qTwIv-WdkxaZGNegIEYJ96qtfBxG3_RT8XFbm_DXthDpws_3bQzOFc4LcwPZ0YS2MOwzpcR5BvkEH5ShqkeEsLX8CjDMoLwknDnZjujIhN8RSGFNZsjKwZb8zqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بشکه تاپاله
که گازشو لیلاز خورده
آبشو میثاقی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19866" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19865" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">احتمال پیوستن مصر به توافقنامه سه جانبه عربستان، ترکیه و پاکستان   «هاکان فیدان» وزیر خارجه ترکیه مدعی شد که مصر ممکن است به این توافقنامه مشترک به محض حل و فصل برخی مسائل فنی بپیوندد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19864" target="_blank">📅 02:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19863" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!  در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19862" target="_blank">📅 01:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!
در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19861" target="_blank">📅 01:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twSuwfPBDuQSbS0QC6BWxC1QLsKYSM0Rnq6P6re1SX3j-vgLPbZo51rOYtyUXDcVJWRjrZH1vaNJNI0UN2k5rVY_HPu23hWWXTTgG8QAUfXrMKT4A-4ld4S-XbvXsJU3dusAn22Vb3PbPPlrv6CfTZTHujeff7B5ZN9I_iBQERvKA0uaDq1Lvv44T0HOIzOWSdKPBbLnDBD1y-pNp5130jZYQWXPNbVT9arqA5JLKPefBziF4DakUsWYltAhP2jbzd_IxLXCMWkgrUf_bKBfangIdbAuIt1LG5WKwI3fu4MOdfI0Mu_8_rBj7f8jDaEjYf9CJZ1XRs4S_4lkFkwPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب محسن رضایی به عنوان دبیر شورای عالی امنیت ملی با حکم پزشکیان  معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور:   با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد  سیدمهدی طباطبایی نوشت؛   نظر به…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19860" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unF1JNpyKRdUR9pFzbf6e19mrn_cMpTxYF8w9QHbTkt3wy6J9-2yYNHyDIbWEy4Y9QHhFEvcTgmV8dRhRzaJ9qo-SRvO0iShBbkOGOGkehdgNYBrh9aV0QB2bZSC_B6w_UyXYrd59bLI61PT5uJAWquY6dUJJycXOHUGJWLwpDYqOaqbfZxgXGOXWkKS-giBhkG1VSZXN_HgYyI4-sGLl-O-BgFDQ16oeypIwiMY4cTpzoSJBj9YGdskrbAchIKP8Exmo6D3lP9rlI0UIwjNbpfI2SUIdmWTMEm-9d2NsHpzd4nxjbEnjzZPlyPC6h-V3rp-2SC6sPuhCD7CmnunoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره ایران:  ما فقط در حال مذاکره نیمه‌کاره با آن‌ها هستیم. ما صرفاً ایران را با تورم عظیم و واقعیت اینکه پولی ندارند، زیر نظر داریم.  منبع: آکسیوس</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19859" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بزنید شبکه آی فیلم سریال آیینه عبرت
عینا شرایط امروز ماست
سبحان الله!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19858" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شلیک از سیریک به سمت کشتی هایی در هرمز</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19857" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هواپیماهای جنگنده آمریکایی دو فروند هواگردی را که در حال نقض منطقه پرواز ممنوعه بر فراز ملک ترامپ در نیوجرسی بودند، متوقف کردند.  رئیس جمهور ترامپ در سلامت کامل است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19856" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بنا به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.  واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19855" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بنا
به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.
واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.
اسرائیل با برخی از این درخواست‌ها مخالفت کرده است. نتانیاهو گفته است که ارتش دفاعی اسرائیل به مقابله با تهدیدها ادامه خواهد داد و اسرائیل این گزینه را برای حمله به ایران حفظ می‌کند، در صورتی که ایران از سرگیری فعالیت‌های هسته‌ای یا توسعه موشک‌های بالستیک را آغاز کند.
منبع: شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19854" target="_blank">📅 22:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=oBNlLO53yDLLTNzL9NUwNUnMM2IEbCA-PqFPIDtqXR-wtAFOww_0ufXCnRKuSR1DJ_k3TIDRwLXyAx453lqqvaGYdALgxW0BL4F6_x_td0D7Uw8N9RI9CTTnWkyD0YorVyro5SX90FeauQFubuDFJ6LZqmcstB6pkgCzSRPn6i2BIKDyyxRR9eJQXoRuugaolgCiqu8k77SzbSFe_q4J2-MqV9xkFaaMAI9eb3icQXKIrN-T440WrLNbHX3h-xRJF6pJym5Eng1qoKLEIWucBrPQHseYo6kDxg52DYhJDdaPG-5zi-y4oat5ugYCe0p3qDzwa5HuKGUUGpSP64FR5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=oBNlLO53yDLLTNzL9NUwNUnMM2IEbCA-PqFPIDtqXR-wtAFOww_0ufXCnRKuSR1DJ_k3TIDRwLXyAx453lqqvaGYdALgxW0BL4F6_x_td0D7Uw8N9RI9CTTnWkyD0YorVyro5SX90FeauQFubuDFJ6LZqmcstB6pkgCzSRPn6i2BIKDyyxRR9eJQXoRuugaolgCiqu8k77SzbSFe_q4J2-MqV9xkFaaMAI9eb3icQXKIrN-T440WrLNbHX3h-xRJF6pJym5Eng1qoKLEIWucBrPQHseYo6kDxg52DYhJDdaPG-5zi-y4oat5ugYCe0p3qDzwa5HuKGUUGpSP64FR5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19853" target="_blank">📅 21:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19852" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19850" target="_blank">📅 21:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
توقف ۲۲ روزه صادرات نفت ایران از خارک
🔹
ویندوارد: خط صادرات نفت ایران از جزیره خارک، تحت تاثیر محاصره دریایی آمریکا، برای بیست‌ودومین روز متوالی متوقف مانده.
🔹
هر سه پایانه غربی، LPG و شرقی خارک همچنان بدون بارگیری هستند. @khate_energy</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19849" target="_blank">📅 20:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19848">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=Q-IBeAtAEiaIyrXhWQKTJE6MwLzPitHqBlUHGk-dkEqt8l0_0pSBBnSs50GbSHENj9VytbyQWidw4l5ZffgMDpvYMjEnNK3twXhcz7EB7jLmBauKyVJM_XXjHTRSUiscdG3K5GDEjaHZWIUhOHHO-ohRqnpGMurouxk24fkVxgMGYiBPu9IGEpbs3sfedm9ztXu6LxviySWeU3icPJPEM7-v04beONH3AeltZtWOh81KRy4RdU_DIFicSRsNoqNcmlXnkaSumOHcGj-ISBeLTiCr5EKPLRWQR0WERhaSnjqpYDLQZxOE30PfYfjiGapORkk5NpV9cjsfPu2SZPbUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=Q-IBeAtAEiaIyrXhWQKTJE6MwLzPitHqBlUHGk-dkEqt8l0_0pSBBnSs50GbSHENj9VytbyQWidw4l5ZffgMDpvYMjEnNK3twXhcz7EB7jLmBauKyVJM_XXjHTRSUiscdG3K5GDEjaHZWIUhOHHO-ohRqnpGMurouxk24fkVxgMGYiBPu9IGEpbs3sfedm9ztXu6LxviySWeU3icPJPEM7-v04beONH3AeltZtWOh81KRy4RdU_DIFicSRsNoqNcmlXnkaSumOHcGj-ISBeLTiCr5EKPLRWQR0WERhaSnjqpYDLQZxOE30PfYfjiGapORkk5NpV9cjsfPu2SZPbUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز همین که ۲ سانت عسل هم داشته خیلی خوب بوده</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19848" target="_blank">📅 20:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایالات متحده توانسته صادرات نفت ایران را فلج کند – فایننشال تایمز   این روزنامه با استناد به داده‌های ماهواره‌ای گزارش می‌دهد که ایران حدود یک هفته است که در جزیره خارک نفت خام را در نفتکش‌ها بارگیری نکرده است.   این جزیره اصلی‌ترین پایگاه ترانزیت نفت کشور…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19847" target="_blank">📅 19:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19846" target="_blank">📅 18:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پزشکیان:
علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم.
﻿</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19845" target="_blank">📅 18:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19844" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او راهی برای اعلام پیروزی و پایان دادن به درگیری با ایران بدهد، حتی بدون توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
این موضوع گزینه‌های کمتری را برای ترامپ باقی می‌گذارد. به نظر می‌رسد ایران معتقد است واشنگتن برای خروج اشتیاق دارد و از توانایی خود در به هم زدن تنگه هرمز و جریان جهانی نفت به عنوان اهرم فشار استفاده می‌کند.
با قیمت بنزین در ایالات متحده حدود ۴ دلار برای هر گالن و نزدیک شدن به انتخابات نوامبر ، ترامپ انگیزه‌های قوی برای به دست آوردن یک توافق دارد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19843" target="_blank">📅 16:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حمله نفتی آمریکا به گرینلند!
روزنامه انگلیسی گاردین:
یک شرکت نفتی آمریکایی با نام «گرینلند انرجی» با تجهیزات کامل در سواحل شرقی گرینلند پهلو گرفته و قصد دارد با ۶۰ میلیون دلار، دو حلقه حفاری کند.
دولت گرینلند هشدار شدیداللحنی به شرکت نفتی صادر و اعلام کرد که هیچ گونه مجوزی برای این عملیات صادر نشده.
مسئولان این شرکت آمریکایی ادعا می‌کنند که منطقه «جیمسون لند» ممکن است حاوی نفت خامی به ارزش یک تریلیون دلار باشد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19842" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو:  ما می‌دانیم چگونه در برابر بزرگترین دوستانمان، حتی در صورت لزوم، بر موضع خود بایستیم.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19841" target="_blank">📅 14:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو:  اسرائیل سند ۱۵ بندی شورای صلح غزه را رد می‌کند.  ارتش اسرائیل تا زمانی که حماس «به‌طور واقعی» خلع سلاح نشود، هیچ گونه عقب‌نشینی‌ای را انجام نخواهد داد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19840" target="_blank">📅 14:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو:
اسرائیل سند ۱۵ بندی شورای صلح غزه را رد می‌کند.
ارتش اسرائیل تا زمانی که حماس «به‌طور واقعی» خلع سلاح نشود، هیچ گونه عقب‌نشینی‌ای را انجام نخواهد داد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19839" target="_blank">📅 14:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19838" target="_blank">📅 14:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">منابع غیررسمی تاکید دارند محسن رضایی دبیر شورای عالی امنیت ملی ایران شده است</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19837" target="_blank">📅 14:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51206b9fc.mp4?token=pJ90UJ3OjbVNT_5TOfo9sjOtJd8sr2NueTlsUn-9Rw2MlZ9Vk0WPPqv-61V_D58TISGnbUb36ihNm55Onuu5OXAkctRVMrYpkGi7BBAJO38Psi3LMCvpdlVGlXQFuXzfq4kpgJRHKUKXb1p3qqpqtCVdf3JhXqEFi0oONMLJWHYTvg9qqB7L4l7B6gVi9jE0Pkh4J0ahDk5Ej4EtikRY5QSExvb0OJjkxNm-57ajdqIOZLzQUesdq9HR4atY1Zn3POQ1x2nB6lQVv4FRrnRwcCeRXzgo6D_IjiL60ucF77As07i5a5JBNSEwB8b6b-P64cxzhXdp3bBTbbvCBH92rYrp0LXQRyHejtwCTM76sJCKidStRLpqiJJyEXbsfETAVfjbJKYJSvyPm6tAV-S4ukx8bs8HqQ0SObdQUiRBNf6t4GitPcgFkZ5n0cTGSWwRZKJZ8Zz8ZBept3jMn2Nbr0b3T67VpmETwRZpngUz11_XN_Z62Vn1Y_BzFXWeC7fwFWG9bj32huTg7r60DBAg88-XMmVuus-0pasrEE5g_HOd0JPVdUOaYb2DtSB4LYZFR-bGy09JIWZSKVmhKxM9AC_opANFf85S4L0TEpYKHCucNF8201tYEDjx2_wfnhAb_AhL3BKNUFqbuUFAJEGGUcq2qwoE0LT_U4OY8lYkOWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51206b9fc.mp4?token=pJ90UJ3OjbVNT_5TOfo9sjOtJd8sr2NueTlsUn-9Rw2MlZ9Vk0WPPqv-61V_D58TISGnbUb36ihNm55Onuu5OXAkctRVMrYpkGi7BBAJO38Psi3LMCvpdlVGlXQFuXzfq4kpgJRHKUKXb1p3qqpqtCVdf3JhXqEFi0oONMLJWHYTvg9qqB7L4l7B6gVi9jE0Pkh4J0ahDk5Ej4EtikRY5QSExvb0OJjkxNm-57ajdqIOZLzQUesdq9HR4atY1Zn3POQ1x2nB6lQVv4FRrnRwcCeRXzgo6D_IjiL60ucF77As07i5a5JBNSEwB8b6b-P64cxzhXdp3bBTbbvCBH92rYrp0LXQRyHejtwCTM76sJCKidStRLpqiJJyEXbsfETAVfjbJKYJSvyPm6tAV-S4ukx8bs8HqQ0SObdQUiRBNf6t4GitPcgFkZ5n0cTGSWwRZKJZ8Zz8ZBept3jMn2Nbr0b3T67VpmETwRZpngUz11_XN_Z62Vn1Y_BzFXWeC7fwFWG9bj32huTg7r60DBAg88-XMmVuus-0pasrEE5g_HOd0JPVdUOaYb2DtSB4LYZFR-bGy09JIWZSKVmhKxM9AC_opANFf85S4L0TEpYKHCucNF8201tYEDjx2_wfnhAb_AhL3BKNUFqbuUFAJEGGUcq2qwoE0LT_U4OY8lYkOWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز مطالعات سیاسی وزارت خارجه!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19836" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منابع غیررسمی تاکید دارند محسن رضایی دبیر شورای عالی امنیت ملی ایران شده است</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19835" target="_blank">📅 13:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19834" target="_blank">📅 12:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrYI2Cs3dK2TGPtyntDe--GvdGzZMGzHkjrqzzdpZH9fRtXDFPXGsonHP-xNvaH9QhN_nbMFAe2KEsKbPRrmOndDdX_YgZ8bjZ9DrYxjjy2jgLuucECqAT1gGjQRNf7798VRJZnE6k5Mv9AsWw5O3yu3QD7kwQhAqDmweIwc8suURi2izL3YVbzrO6OJT5gVbLi2SxYA6mSwGe1RxC8AHG15SUIn6ETHUSl9Fkk1xtysGmqsCtuaRA4LiDORngxblyuzpbnvBG6-oswO6d4TeLAe0VExAXDXXGqqihugq8HfcpKSEZNzCNFs26zDVDjC74vyFSsKCTu7PyrdbimVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه بوزینه ای که میبینید، متعلق به جناح چپ حزب دموکرات هستند که اخیراً در انتخابات حزبی دموکراتها به پیروزی رسیده اند.  این روند ادامه یابد، دستکم 10 تا 15 درصد از کرسیهای کنگره آمریکا به جناح بوزینگان خواهدرسید و این یعنی دموکراتها برای تصویب هر طرحی نیاز…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19833" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">طبق گزارش‌های لبنانی، ترکیه از سوریه و حزب‌الله خواسته است تا در یک جلسه با یکدیگر دیدار کنند. ترکیه همچنین اعلام کرده است که آماده مشارکت اقتصادی و نظامی در چارچوب یک نیروی است که در لبنان مستقر خواهد شد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19832" target="_blank">📅 11:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به لطف خدا، پالایشگاه آرامکو در عربستان را با پهپاد هدف قرار دادیم!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19831" target="_blank">📅 11:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به لطف خدا، پالایشگاه آرامکو در عربستان را با پهپاد هدف قرار دادیم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19830" target="_blank">📅 11:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19829" target="_blank">📅 11:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a7c5e0be.mp4?token=JgTyqVLJgem9U3q0OUYu8fwbJtC9mTuIgFrcXNEAFX48OXXv1WGWirH8iWxH4UWDb2HE9ya7Viv3ds9XmbJDwxeb5nu3RXP0VAByqHe59_gKHdiNFZO7jYpJB0NOdJ6uzb9_zPiueOGMe8mhJaTaYln_Bvjrz-RSLFI6KopRo4sjRRrEJ3WH_k27NqzLBogrSIKJhefvW40MTS8J7mkA3ckqgUMKrO6hh6-8pRgZE0fAr8YJSAN_0c1Y9AsS1B437LQ5S91ao406RB8kwjU4nj-zDC4kWSkukKvSWKC9sb7fX05ykbwfIjY5KrJVimmkF611cymCI3BgXovYhASa0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a7c5e0be.mp4?token=JgTyqVLJgem9U3q0OUYu8fwbJtC9mTuIgFrcXNEAFX48OXXv1WGWirH8iWxH4UWDb2HE9ya7Viv3ds9XmbJDwxeb5nu3RXP0VAByqHe59_gKHdiNFZO7jYpJB0NOdJ6uzb9_zPiueOGMe8mhJaTaYln_Bvjrz-RSLFI6KopRo4sjRRrEJ3WH_k27NqzLBogrSIKJhefvW40MTS8J7mkA3ckqgUMKrO6hh6-8pRgZE0fAr8YJSAN_0c1Y9AsS1B437LQ5S91ao406RB8kwjU4nj-zDC4kWSkukKvSWKC9sb7fX05ykbwfIjY5KrJVimmkF611cymCI3BgXovYhASa0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ظاهرا اوضاع جو خواب آلو خراب است و بزودی به خواب ابدی خواهدرفت.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19828" target="_blank">📅 02:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ظاهرا اوضاع جو خواب آلو خراب است و بزودی به خواب ابدی خواهدرفت.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19827" target="_blank">📅 02:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19826" target="_blank">📅 02:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpcEtIHt_WzYj6Qd6zIohblAn_h-_7igrfyUlR5v7QQ61rV170s2DR-WUKb_CnyaHn6r8hp6JBeHU7iFm-z8Gr8AJ2lngVCIrwkr-lIQIq4lNzkbs4Np5CfQo7sHWlFw7bDvzT8J5L92BVzhE-Tkk2wlpDELXRF79UCv1fY6WxeTNljK2SqT_6GA_bkyzNdN8x5AVwEojtR58igOFNlMhVepfFk8DX5iNb3PSRnkaukySnD-Yqib3cyfA4Tb5W9Vh0fqX1f6DFw528eSV3oVdehuPahUF9M3M_smbbwcPSOeHVIETXtUzJbWA0p7_Ek-BeW9uRi4HQrZ8hRKlHTG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnzKpuIsb8clPcp2dWjywGGx3CV9bSeB_IkuUlk1rEK0xhvioaOO_1C3II4l2u69anJTfTXdIP0VArWHRFwvxd-7uwxAGXoArrYTgD-ZkZmxG2dbr3FO2O4QmX6WfYdAwbtWIl2g2KOISNFr9f27o3SduFotVnZwJ3XwA0VDvcRlfHsphjJgr3P3iLuQ3CW-iH8BeFICQLz2Ikjg5ZPhozdunXbw3yplvYTQIacXxBPVRZz2h_YBE088FzDLHUuPBJF38a57l1mwPu8JTgP4Cb4Ni0Hx58E16XbKQYml_tUvfch6pHq7sasbLYvtFrlhoCh5xyiMO-8fQDPeS5oAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbyysi9B03jCY1mn8tvuWKKDWOIDQ9PdSUnjDtxZeiPXMTNColxTiKkxEyqsDN_r3tye5cb-gpxsEhqzSQ-8ZfCPxC4LCi9Eh5qx9ykt1hWLP_k7kP-aBzJ61kqbj-fUxaIKozGZSe2TkQOmGf0LvKQTxvARI8V0x7Cxo4dxK3RCoGG2IaA3_CM9VMfX9z_Gks89DltOqNuecdNiO3b5L2PeJkyUNjpWAS0UNyKe8ucz-C5hkOVl8oCXIph9dpptae4USDN3mHoVPuelbc4iurym70pmJSG5Z_DKPPJTDG369kxwjRPeiF3M28DTOefzLKPv3yt0qV-iPhfkj1al7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سه بوزینه ای که میبینید، متعلق به جناح چپ حزب دموکرات هستند که اخیراً در انتخابات حزبی دموکراتها به پیروزی رسیده اند.
این روند ادامه یابد، دستکم 10 تا 15 درصد از کرسیهای کنگره آمریکا به جناح بوزینگان خواهدرسید و این یعنی دموکراتها برای تصویب هر طرحی نیاز به استمالت این جانوران خواهندداشت.
بیخود نیست ترامپ و دیگران — حتی برخی دموکراتهایی که کامل عقل خود را از دست نداده اند — از خطر کمونیسم در آمریکا می گویند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19823" target="_blank">📅 01:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xno4rY38Bh09KnYzmSkjq0gmZeA4Ptt20toUw_IJNXZeaenJpTEJ5O8FiyR8PK8Zc3WUlHA_cmUL4y9ElEsc1a8aiDo02H40a6VUzeBrtwPn5WbH2OsIpzNToOOYbXEd5SXNGwb9EtnbEIjf8BXtb2U9tnUCpFefBDf7EHvAGhhYoj0iiXLq3J0ROWB-imJ2rUczjNR9DwJTk328pzZMFOm6OhVwU_k4ahRwg2DwjgVshz9MoXZ4AyHwJqklZQvIOkcjJyLc4fR7cd3pJAB0xU-IwzuW-JA6dCKQnOz3GXKbiJWlyiMoFqb8FWx3pYkDsGsiQvXp3bamRevXzUN8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول ارشد سابق در پنتاگون و مدیر ارشد در مرکز اسکروفت در مورد ذخایر تسلیحاتی ایالات متحده:  «محاسبات مربوط به مهمات برای ایالات متحده بسیار جدی است،» او گفت. «با هر عملیات هوایی علیه اهداف ایرانی و حملات تلافی‌جویانه بعدی ایران، ایالات متحده توانایی‌های حیاتی…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19822" target="_blank">📅 01:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الی کوهن، وزیر انرژی اسرائیل، درباره ایران:
به نظر من، از دیدگاه ما، بهتر است هیچ توافقی وجود نداشته باشد. ما می‌توانیم به اعمال فشار بر ایران ادامه دهیم.
و من به شما می‌گویم که، با کمک خدا، در دو یا سه سال آینده، رژیم ایران سقوط خواهد کرد.
به یاد داشته باشید که این ماجرا از کجا شروع شد—ما اطمینان حاصل کردیم که تمام بذرهایی را بکاریم که منجر به سقوط این رژیم خواهد شد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19821" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19820">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آتش توپخانه‌ای نیروهای دفاعی اسرائیل علیه ارتفاعات علی‌الطاهر، لبنان.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19820" target="_blank">📅 00:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر خارجه ترکیه، هاکان فیدان، درباره روسیه و اوکراین:  وقتی جنگ فرسایشی در جبهه به فرسایش در پشت خطوط جبهه تبدیل می‌شود، مسئله به این تبدیل می‌شود که آیا به عنوان یک ملت ادامه خواهید داد یا خیر. شما از هر آخرین راه حلی که در اختیار دارید استفاده می‌کنید.…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19819" target="_blank">📅 22:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اول فکر کردم گوشی را وارونه گرفته ام تا اینکه خانه ها را دیدم!  بوی سلاح هسته ای می آید!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19818" target="_blank">📅 22:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_0_1_fQqjsKrWajbhT5YUpDWJYmNFhUxnJr9aZ2Yd3FDmr_c-fHFSC5FGCFHlopwAajwEeP-u5fghwVohE7gNTC41dEDgIo01djOwXUjYCjDYuVh0ZWLa5AOPjipq1sR9Ve4tB_dfdne2zkPJ-yEvf2qbP31X43Pi-wO01SI4Xkmbk62_S45jCTLMM6f-3EewV3Bu71HxCmU0DNPJ4-klNV-FCM3dPdUEnIquidY1IDKd1CR2rxQaHB6c7x-ZpNfc8dKe2apJmQMtc5IXbw3pcfpBlHapFOwFhRb20p8swP3y6vkOvTdfLQ0hQWf1UIkmk9FrGO5Yoj45XUQYDArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19817" target="_blank">📅 22:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سه کله پوک معلوم نیست چی امضا کرده اند که جرات نمیکنند علنی اش کنند.  ترکیه بخواهد در جنگی ضد هند هسته ای شرکت کند، بند ۵ ناتو عملا برایش کار نخواهد کرد و فقط موشک هسته ای خواهدخورد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19816" target="_blank">📅 21:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خواهیم</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19815" target="_blank">📅 21:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال ۱۳ اسرائیل:  اسرائیل در حال آماده‌سازی برای حمله به ایران به تنهایی است   نیروهای دفاعی اسرائیل برنامه‌های خود برای اقدام مستقل را حفظ کرده‌اند در حالی که واشنگتن به سمت خروج دیپلماتیک از جنگ پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19814" target="_blank">📅 21:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در حال آماده‌سازی برای حمله به ایران به تنهایی است
نیروهای دفاعی اسرائیل برنامه‌های خود برای اقدام مستقل را حفظ کرده‌اند در حالی که واشنگتن به سمت خروج دیپلماتیک از جنگ پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19813" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔸
سوپراپلیکیشن "بله" پس از فعالیت کوتاه بین المللی ، از فروشگاه اپل حذف شد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19812" target="_blank">📅 20:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⏳
سوپر اپلیکیشن بله بعنوان اولین لژیونر اپ های داخلی وارد اپ استور شد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19811" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYE1fcMcbe-Jqv5FxaWc7SWkApLY_MoTjUmDvd1FaJaXuz3H8Z1IW53u5l9p2m2FPhdo5JgQzRN_ZYdl9_P_BPLCskIHqtTmfpTH78rCs-N97n6U2ePOmlaBMmCnBXZpMLhx_GnAQr2BET_yp6FjeSAdGHlTFievo6AuvHeOQWygHDO18E3LPjSndq-rZhbHjl0VPmDWnTbMgcQGBqlLILbxQrl0cK8DYOkRw3pucidvi4iWGYV8bHp9olRMFNGmIsd-n06dUovvA_jxksB-JBx8AofZzWVVToImdphQZQpGRsSn3njXu2ZQeYc0yMdX7GA7p9MNN62S5fgW67mF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی یک سایت روسی: ناتوانی آمریکا در هدف قرار دادن زیرساخت‌های حیاتی نظامی ایران  تحلیل جدیدی از فیلم‌های منتشرشده توسط فرماندهی مرکزی آمریکا (CENTCOM) پس از ازسرگیری درگیری‌ها با ایران، که با هدف نمایش شدت بمباران‌ها منتشر شده‌اند، واقعیت دیگری…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19810" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19809" target="_blank">📅 19:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19808" target="_blank">📅 19:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه، در یک تماس تلفنی با همتای بلغاری خود، ولسلاوا پترووا، نسبت به تصمیم صوفیه برای اجازه استفاده از پایگاه هوایی بزمِر توسط هواپیماهای نظامی آمریکا به منظور پشتیبانی از عملیات علیه ایران، هشدار داد.  عراقچی گفت: «هر گروهی که به هر…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19807" target="_blank">📅 19:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19806" target="_blank">📅 18:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19805" target="_blank">📅 18:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkYaNi_mFdqUewN7a1dPW8cvPOxVs4vSKROgUQV7y-0YvMJomjWMqXpcxI4Obt7vebvNyiAhVEpnflYq0IhfJ6ORuyzqJohKzvvaVbvVKumsM0Ltn1Ayd9wjH3oP77qHD0WMUmaTWErK7pIu0Ny_0N3mwx2OQwfPdumH3y_vDK4sK2qpSZu-LQui8TgFKNHd8iCOphvMF13l2u_HyRGbDkhKWeMZJ-Jn-p-oPBCfM30-vwXVUFtoQ2VGYJDA1POwVSsacnFlrbuhCCEMuadNxtKxuhGRtL534_WY-p4G36FIT228Iwu5k77eTrR7yDMsHcotwg63vxjQQroaDzmcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19804" target="_blank">📅 18:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19803" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسرائیل و کلمبیا پس از به قدرت رسیدن رئیس‌جمهور جدید در ۷ اوت، روابط دیپلماتیک و اقتصادی خود را به طور کامل بازسازی خواهند کرد.  دو کشور سفیر تعیین خواهند کرد، الزامات ویزا را لغو می‌کنند و کلمبیا قصد دارد سفارتی در اورشلیم افتتاح کند.  منبع: i24</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19802" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که یک تانکر نفتی متعلق به شرکت ملی نفت ابوظبی (ADNOC) که امروز در حال عبور از تنگه هرمز بود، مورد اصابت موشکی قرار گرفت.
این، چهارمین حمله ایران به یک تانکر اماراتی در این هفته است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19801" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس جمهور صربستان، الکساندر ووچیچ:
ما قصد داریم یک کارخانه تولید پهپاد در اینجا در ماه سپتامبر افتتاح کنیم، اما این کار را با همکاری شرکت‌های اسرائیلی انجام خواهیم داد. ما این کار را با اسرائیلی‌ها انجام می‌دهیم.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19800" target="_blank">📅 15:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19799" target="_blank">📅 14:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19798" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg7mjKWBc_BuJaMSw77j1xTRLQIsmlljfCA2QrV2LjLHIoIkZ74Q3Pl73rdDNicUWFNcZXp4OUMZvcL3dnD5_9a8hqSHwpvu-lFZU1nal2oSWI_yyGWdumJngSQmfTVHqrdxle6bYMhAUEhS5rPzhufUJA7fdPCkjVQnSkdsPdxXtWsxdYI4aWuT9ZC5b-D9rBTGNC626AMWMZFnVFToykbltIjscXWvRwXFDvy96zaAAfPitdgpfVXTak73Rm5xsQiF0nk7-ERkVvcRsxeSCjLSPq4Ccxki0tuG2rA2NCXZtM1PH-Sr8NfYPf6RA_Puq_iePZxK0U6BZ9P7YVFUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟
در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در نگاه نخست می‌تواند یک راهکار جذاب برای دور زدن محدودیت‌های دریایی و کاهش وابستگی ایران به مسیرهای صادراتی سنتی باشد. با این حال، بررسی دقیق ظرفیت‌های فنی، اقتصادی و لجستیکی نشان می‌دهد که راه‌آهن هرگز نمی‌تواند به‌طور کامل جایگزین صادرات نفت دریایی ایران شود؛ اما می‌تواند به‌عنوان یک مسیر پشتیبان، بخشی از درآمدهای نفتی تهران را حفظ کند و اثر تحریم یا محدودیت‌های دریایی را کاهش دهد.
نخستین نکته مهم، تفاوت عظیم میان ظرفیت حمل‌ونقل دریایی و ریلی است. صادرات نفت ایران پیش از تشدید محدودیت‌ها عمدتاً به چین انجام می‌شد و حجم آن در مقاطع مختلف حدود ۱.۴ تا ۱.۸ میلیون بشکه در روز برآورد شده است. انتقال چنین حجمی از طریق راه‌آهن نیازمند زیرساختی بسیار فراتر از ظرفیت فعلی شبکه ریلی منطقه است.
یک نفتکش بزرگ VLCC می‌تواند بیش از 2 میلیون بشکه نفت را در یک سفر جابه‌جا کند، در حالی که یک قطار نفتی معمولی بسته به ساختار واگن‌ها حدود ۲۰ تا ۷۰ هزار بشکه نفت حمل می‌کند که اگر سقف این محدوده یعنی 70 هزار بشکه را هم درنظر بگیریم، در روز به حدود 25 قطار نیاز است تا معادل یک روز معمولی صادرات نفت به چین حمل کند. بنابراین برای جایگزینی صادرات دریایی ایران، باید روزانه ده‌ها قطار نفتی در مسیرهای طولانی بین ایران، آسیای مرکزی و چین حرکت کنند؛ موضوعی که با ظرفیت فعلی خطوط ریلی، پایانه‌ها، گمرک‌ها و مرزهای زمینی منطقه عملاً امکان‌پذیر نیست.
در مورد مسیر افغانستان نیز باید میان «امکان راهبردی» و «واقعیت عملیاتی» تفاوت قائل شد. ایران هم‌اکنون دارای اتصال ریلی به افغانستان از طریق خط آهن خواف–هرات است، اما مسیر کامل ایران به چین از خاک افغانستان هنوز یک کریدور تجاری با ظرفیت بالا محسوب نمی‌شود. بخش‌هایی از طرح‌های اتصال افغانستان به آسیای مرکزی و چین همچنان در مرحله توسعه قرار دارند. بنابراین افغانستان در آینده می‌تواند به یک پل زمینی مهم تبدیل شود، اما در شرایط فعلی توان انتقال میلیون‌ها بشکه نفت ایران را ندارد.
مسیر واقع‌بینانه‌تر در کوتاه‌مدت، استفاده از شبکه ریلی ایران به سمت ترکمنستان، قزاقستان و سپس چین است. این مسیر از نظر زیرساختی نسبت به مسیر افغانستان آماده‌تر است، اما همچنان با محدودیت‌های جدی مواجه است. یکی از مشکلات اصلی، تفاوت میان محل تولید نفت ایران و محل مصرف در چین است. بسیاری از خریداران اصلی نفت ایران در چین، به‌خصوص پالایشگاه‌های کوچک موسوم به «تی‌پات‌ها» در استان شاندونگ، در مناطق ساحلی قرار دارند؛ در حالی که مسیرهای ریلی زمینی بیشتر به مناطق داخلی چین دسترسی دارند. بنابراین حتی رسیدن نفت ایران به خاک چین لزوماً به معنای حل مشکل انتقال آن به پالایشگاه‌های مصرف‌کننده نیست.
با وجود این محدودیت‌ها، نباید نقش اقتصادی صادرات ریلی را دست‌کم گرفت. هدف ایران احتمالاً جایگزینی کامل صادرات دریایی نیست، بلکه ایجاد یک «حداقل جریان صادراتی» برای جلوگیری از قطع کامل درآمدهای نفتی است. حتی انتقال ۱۰۰ هزار بشکه نفت در روز با قیمت ۶۰ تا ۷۰ دلار، می‌تواند سالانه بیش از دو میلیارد دلار درآمد ناخالص ایجاد کند. اگر این رقم به ۲۰۰ یا ۳۰۰ هزار بشکه در روز برسد، اهمیت اقتصادی آن برای کشوری تحت تحریم بسیار بیشتر خواهد شد.
البته هزینه انتقال ریلی بسیار بالاتر از حمل دریایی است. نفت باید از مناطق تولیدی جنوب غرب ایران به پایانه‌های ریلی منتقل شود، سپس از چند مرز عبور کند و در مسیر با هزینه‌های گمرکی، تغییر استانداردهای ریلی، بیمه و ریسک تحریم مواجه شود. به همین دلیل، نفت صادراتی از مسیر زمینی احتمالاً با تخفیف بیشتری نسبت به نفت دریایی فروخته خواهد شد.
از همین رو، راهبرد منطقی‌تر برای ایران شاید انتقال مستقیم نفت خام نباشد، بلکه تبدیل نفت خام به محصولات با ارزش افزوده بالاتر مانند فرآورده‌های نفتی، سوخت‌ها و محصولات پتروشیمی و سپس انتقال آنها از طریق راه‌آهن باشد. حمل محصولات با ارزش‌تر، از نظر اقتصادی بسیار توجیه‌پذیرتر از انتقال میلیون‌ها بشکه نفت خام با قطار است.
در نهایت، اهمیت اصلی این پروژه بیشتر ژئوپلیتیکی است تا صرفاً اقتصادی. هدف ایران احتمالاً ساخت یک شبکه جایگزین برای جلوگیری از تبدیل شدن تحریم دریایی به یک ابزار خفه‌کننده کامل است. اگر تهران بتواند حتی بخشی از صادرات خود را از مسیرهای زمینی حفظ کند، اثرگذاری فشارهای دریایی کاهش خواهد یافت. در این شرایط، تحریم یا محاصره دریایی دیگر به معنای توقف کامل صادرات نفت ایران نخواهد بود، بلکه تنها هزینه و دشواری صادرات را افزایش می‌دهد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19797" target="_blank">📅 12:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy_BQLPSpaJMFhUT41qn2FxkTfbfl-8UDkKiRQJDjziAtGwyi_JZM_SYvchBx_KDFHlazlU8qKx7Vf2scedXF5_PSBUlS3igESGBpquGBz9UIbVgPUziyWGas2mLQVLo5-77Nm8xLXT51Wz_Kme5tpsY40OKsdrgTNZnPZ2zaQJyqFwbh0MH44LSxHPcUTXdvMBVZdeo749vO4GWcXNb2BvQlWLdayzicasrqEG6i2iI68buzruwovyjh4UM8NK97rFp5Ky3pefRkjFC6Sgh0B1ILbU9SNKBqlmaIWFgEkERIrRgbruXwUSbO6H0XGWEmjNJkbLnfSZZAZ1v0ipfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد که البته بخشی از آن به دلیل تقویم اقتصادی (گزارش NFP) است.  انتظار یک افت اصلاحی در طلا می رود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19796" target="_blank">📅 12:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوال خبرنگار:   مانند مه ۲۰۲۵، زمانی که وضعیت جنگی بین هند و پاکستان وجود داشت، آیا ترکیه و عربستان سعودی فقط حمایت کلامی ارائه می‌دادند اگر چنین چیزی دوباره اتفاق می‌افتاد، یا با سلاح از پاکستان حمایت می‌کردند؟  وزیر دفاع پاکستانی عساف: هر چه این توافق‌نامه…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19795" target="_blank">📅 12:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سوال خبرنگار:
مانند مه ۲۰۲۵، زمانی که وضعیت جنگی بین هند و پاکستان وجود داشت، آیا ترکیه و عربستان سعودی فقط حمایت کلامی ارائه می‌دادند اگر چنین چیزی دوباره اتفاق می‌افتاد، یا با سلاح از پاکستان حمایت می‌کردند؟
وزیر دفاع پاکستانی عساف: هر چه این توافق‌نامه شامل می‌شود، قطعاً به حوزه عمومی خواهد رسید. همان‌طور که قبلاً گفتم، قطعاً به عرصه عمومی آورده خواهند شد.
اما این توافق‌نامه تنها امروز امضا شده است و فکر نمی‌کنم مناسب باشد که در حال حاضر جزئیات آن را بحث کنم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19794" target="_blank">📅 11:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3roq_sthOh-iVqq2lxl9BMiNDZ9fUV5948kPi-Zvbf7zTvSySgrjkNi1Ww_6GDjMWl5Ako64Dx6wHhDXzbTTPwzO8_5-wvmVnrJsH1RUNMs9Ua42TGtygTVJV6xiWreWJHaTIAkLkAMV2UJ1LQKLrG4ME9OK5cQxEyXgMm1b42UhtpKAkQNQ-nvPYKvncaKfLmnUrCH3s_7kt_ZwmtFgsYC_HFk4W-IuSj1bXimnsirR0pfBnvqUOhMpa6cFLB8C94o0WsvvgYPd8tUTJRn-NLSIBfl77JLpLBr7vlIzrR6dYeZLCoxYZUN3AWj1J5kLk_UY8Cxf6SgbE78VxrkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده توانسته صادرات نفت ایران را فلج کند – فایننشال تایمز
این روزنامه با استناد به داده‌های ماهواره‌ای گزارش می‌دهد که ایران حدود یک هفته است که در جزیره خارک نفت خام را در نفتکش‌ها بارگیری نکرده است.
این جزیره اصلی‌ترین پایگاه ترانزیت نفت کشور است. اسکله‌های بارگیری خالی هستند و ترافیک نفتکش‌ها متوقف شده است که نشان‌دهنده طولانی‌ترین دوره بی‌فعالی در مجتمع ترانزیت جزیره خارک از آغاز جنگ است</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19793" target="_blank">📅 07:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقام آمریکایی گفت که توافق مربوط به بازگشایی تنگه هرمز نهایی شده و در مقابل محاصره دریایی ایران نیز برداشته می شود</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19792" target="_blank">📅 01:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پزشکیان:
من نه تنها از شهادت نمی‌ترسم، بلکه آن برای من یک پیروزی بزرگ است.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19791" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">402.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19790" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 21</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19790" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه های اسراییلی:
محسن رضایی جزو اهداف ترور است.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/19789" target="_blank">📅 20:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19788" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انصافاً ببینید کشورهای منطقه (خصوصاً عراق و کویت که راهی جز هرمز برای صادرات نفت ندارند) برای گریز از اخلال ایران در هرمز چه می کنند.  خط لوله کرکوک—جیحان که الان هم فعال است.  خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SBoxxx/19787" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZC_pvHvjfVz8LC13o0yaT6AOT4TMzyaARjFts8kI2R68Uk9V5MGNxY9MaAvtU8seB8TbgmPAxOSW7ZldCvGKpE3R7dz1tsfD7V9qub8zdZyBUYnPHE1jNe_UR4n61o2LqXyc1wl6BYNEUHkFqVzi6MWJgeP9aDvIpp2oMiNmc2BiFZ5lpWoh9uYjsMDfo8sJytxebS7p2VLzptaMZPGUAi8ZZ52xtn2d4_NFbJMdGu5Hc_LbVFsKFm49jJywyUdVhcktb41KWxjGi78ahHP3UiEXjJRG6zF7oe-tZUR0bp7HrqTe6L8WjhYDy6ALF8zpywG4A4wYZWfdzE7P5setg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
با شاخص های سهام در سقف و نفت کنترل شده، همه چیز برای ماجراجویی دوباره ترامپ آماده است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19786" target="_blank">📅 19:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESbunN4rEIsqjt5D8F_Gg9emxmm00Hcp1egO3jVGcM-cqeBUHqRdlJri0PEcE8cVCM7sxqnF7bjb6rEI0SUu8Z8yTCUhuxZHjwYRGsD8FvMSkVP05O7hOy2V05kK8WAJ4cC3ibDHU-hL1SyCkQW4hmJYRacg9-ktajJ6pq9DgHYguLJSwyZJ5a7GlKcEUAGFDHS0NJZekCXQKtk6X_Jb9ipCKsAo3scBnZE44nVeL5D6CTebSjWUWDOSCZe9AqPh6GPv0zQVuPTgDoBc1hsXDyEuTtW4i_80cJbD8g_BV1ULU1FnEeYyvJUq7ZC9iNP4ktJ_vBRZLBWbFNfpjo8xLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD — H4  میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19785" target="_blank">📅 19:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ریاست جمهوری ترکیه:   هرگونه حمله مسلحانه به هر یک از کشورها، از جمله ترکیه، عربستان سعودی و پاکستان، حمله به همه آنها تلقی می‌شود</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19784" target="_blank">📅 18:41 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

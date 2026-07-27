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
<img src="https://cdn4.telesco.pe/file/JOmetdvvms-AVIYvqX3at_T2XsYzElmSE0JdLPbTXCb2Fvg6Ct3sIBmdbPj77MxotygSyc2Fz6PzSYjlP3mtUpKBT7Dxpj70OWaaaePdFnCvwa-1OIMelC3qWkA4cwTG5Tfm-RS3uR9gXTV-GqK43dvVpPlYzBL2EQKPOxOm607E_B0fvLGDmiZXWIzHToH4JeOg6m-OX1ncpzpJA-HRSK68R8zCtlwPiBygS-DLpnmCWJ9yA2MHgTUNF7EWRJfeJ_OTV3pQXe2gl1gebXKzU5zvBYpVqPY1VOrsOv7aDX8NPzGVw5XPgFnpcZpgo5drlluJBAaD0iDmgDiJnCsV5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 185 · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDWbboUD_6_V4ksSxc52wywxtRXp5QwHM_38T3Dktm5FGhi23rf0DK_VkHvnwrtv0TfaFjKE_yy_LZEFlJnIEil-Xdyb-W2kMG8G9CK_VZk4kz5mEpOghMIb22A18CSykI1A80HXgR5idpMa4GMtYOMqOpqOCEUwowYv714dOIoTWRk3TriuVzHBjrVB6ciIagyBXYaCRD4YMrPnosYtQiK2wQRxP80eVnJ5IMxM3kzjSq8ONnFyb7FQZ_Mzs59mNvvIAfRZGsEr6rQS4-SX22ePTvRagZhh5MUf3U7FeSZ4JqxgiJOnQLCHZGl4l7Syg5OvQxeNJGKRn3D-o2h_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 13</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 13
دوشنبه 27 جولای 2026</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZTnbhEcGP_cSO0MuMRV-dkU4PipBNgxob72o4ckIk7byftOrfXPUhUE0uSacDms9A-MZqseDG_-WHuu5CKHz4JSMIusvbuIXT9ZvVhiC_-tqwzvzanlapuZJVABFzYtzGkjurxIgJoPvmojOtYlMmFXzDEB_uDDWP9ENb4Gisk7nhAXKSqSj3CJxa58uKYGzd4dWt6XeExWD20dM_DojM1KoWrxypCG5Kqs6FOQ3JmmyOIlXWMXtzPRCWIPFtBNG4HfJE1c8VWocDRmkq1ef_PWIlJHYfgwGvRZ_jaGnuRbyXK3Tblh4Hf3iaz4zB1TLsD4uX3GGLCoejiQm-6nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYc027kXIrcqluaXzSW9CGj96kGj3VV2S0pRjwEXSNYA7ToZo7cOdqYvvr6uBTPakrhOljqEWKbgVhrirR-pWX5GLqpibPTGE12zO7sUO8CvqS3TwHZFEk2fjw96mA4BNPHfxT3-eQNNd6o6K9exhrPJhAU8miZmBo1FYVmlMu3yBiYRRnsF2XbYOgC3Ix9FAA9CZyg0jmbrPSPfr2yUlgdZLZX_y3pm1v2swc4xrfpWEsb1USw4h3RJVUKIqFppOycE47tgv0J6Zsj7G3aHj0JmiwJpN9XwLGM4UBpWAyV5qtI57MQxHf1rVeZAu0OHRy8Ygg2hxs1tr5siypbfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcJnWB7sXV6-7C-vKOql5Ql2c0zTbzEsSXykmVDT_MOPjLxVeZO1Drzj3Q_mGBkJvUA2EIAUwGk4figEpTYRoegyEXC6O63ek-dJTQ0WbiSF1PsNtjXNZmpaMO2pF12o2siBUaPNC6j6GQConZV9062XiAX0mZxL0_3wOuGwFN1AkxlquUJT1l4lxMok_0TKckqHjyTFv4u9LhsvOWEclUf9W2nhTCIjKsRFtmrpS0S9M73ip_uC8UrdzeA7_hJ0yOHNDxzxmI6IN29oRR2fCl20czSAKOYaqV_HYvg19cnQq_f0uPQQLuvOwRp7OtvFSIRTcvUGK5efEGvlj9zpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها و اخلال در مسیر جایگزین صادرات نفت عربستان
با ادامه تنش‌ها در تنگه هرمز و دریای سرخ، عربستان سعودی برای صادرات نفت خود بیش از گذشته به مسیر دریای سرخ و کانال سوئز وابسته شده است. ریاض از زمان آغاز جنگ با ایران، با استفاده از خط لوله شرق–غرب، بخش عمده نفت خود را به پایانه‌های دریای سرخ منتقل کرده و صادرات از این مسیر را از حدود
۷۰۰ هزار بشکه
به
۴.۹ میلیون بشکه در روز
افزایش داده است؛ رقمی معادل نزدیک به
۵ درصد عرضه جهانی نفت
. از این مقدار، حدود
۳.۵ میلیون بشکه در روز
از تنگه باب‌المندب، عمدتاً به مقصد آسیا، عبور می‌کند.
اما حملات اخیر حوثی‌ها به کشتی‌های سعودی، این مسیر جایگزین را نیز با خطر مواجه کرده است. در نتیجه، بخشی از نفت عربستان ناچار است از
کانال سوئز
یا حتی با دور زدن
دماغه امید نیک
در جنوب آفریقا به بازارهای آسیایی برسد؛ مسیری که
۲۰ تا ۳۰ روز
به زمان حمل‌ونقل می‌افزاید و هزینه‌های حمل و بیمه را به‌طور قابل توجهی افزایش می‌دهد.
در سه هفته نخست ژوئیه، حجم عبور نفت از کانال سوئز به بالاترین سطح خود در
دو سال و نیم گذشته
رسید و انتقال نفت از طریق خط لوله
سومد
مصر نیز نسبت به ماه قبل
۵۰ درصد
افزایش یافت. با این حال، محدودیت عمق کانال سوئز باعث می‌شود نفتکش‌های غول‌پیکر نتوانند با بار کامل از آن عبور کنند و ناچار به تخلیه بخشی از محموله و انتقال آن از طریق خط لوله سومد یا استفاده از نفتکش‌های کوچک‌تر شوند.
در همین حال، ایران پیش‌تر هشدار داده بود که در صورت تشدید اقدامات آمریکا، ممکن است
باب‌المندب و دریای سرخ
را نیز هدف قرار دهد. به همین دلیل، تحلیلگران هشدار می‌دهند که با محدودتر شدن مسیرهای صادرات نفت، توان بازار جهانی برای مقابله با هرگونه شوک جدید عرضه کاهش یافته است. در شرایطی که قیمت نفت برنت به حدود
۹۷ دلار
رسیده و برای مدتی از
۱۰۰ دلار
نیز عبور کرده بود،
گلدمن ساکس
احتمال افزایش قیمت تا
۱۲۰ دلار
را مطرح کرده است.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOKO06ErVovvT5XgGH-KpRVwK9gc1Nh5tbqux9TRABn0JREPUjJMA8Je8zEHf0FJFW5wCtQmZJneB7saEk-TLuMHeGZV3zsK9PkNRCGY0yQhrdAJbo53CSF6wR9znzXyS7VWMzjDvllk-25kIgyHAw07M1WBBSy0565hG8R1S9vwwpPfKhUx1bj_re9w3jW41fNaIuCaGjsyWPYnJNyDNgR8EUY7qF7OWH3JxsSKS_uPE9-JboCBXC0XHm4vyvkiw3u4u1t8L3moNQkPWaO-gzI4Xmpg4Rl77j3R1mSX2oJBGWTO9yoju-bVv-dXzDlkKahGDeQW59gu69KTBjlHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym0wcbg-DKGw1SvZAfVxBfjOTKKwMQ_JsKJh2FuOgPOxIUZXtg3lm5xTKYmYb0WLcTpIf6tvcWiG3tvoSmqUxUBqaO9HOeM46LsbDQF5kBpF40vlZ7q8FGePZhjMu9MEk0tO54m32XYzaa-KXGez3iJ636Pt-MNSiUkaT7UtW5Gfy1Oh6_OozNPx2WiFmPsPM3MtAEJwwnuYzv3G8p8Y6DWI8cWodWZgIRJ6ZWuFU8f2ubvBb005mwlplmfTh1nOMTAAKW0Pvo8cOoztMQ3O1qnDFFE0RAMXrme9FCr_nJELm_0rcMNf5ByFmpgrcVqnM3CJ0dlJoI-4DGtA9AGECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G195cS3jk3EZFEUPip3FZUJbLoGGTDndpkNHbi3mmUFwUprbWR9wVVdmYAg9_A5eUX1HdSfvYwYsGq9VgkwGClYLlFw9Y4R6TJ4wPoUIzo0S5-Vyf85vWK_eAUpyftIZqglhq8y48csqBT1yBlstsL3KY1Fz-IHXbsxoEPoBklge8Uz1RGNqMNFKF3JBCbUoNfEdLUVA3Ng7CG4oKafSj7OQIvN4Eq-qP4sl-8ijvJmafmx-RvxSR0VOidYnsRVkRp1T5Y-5y2pp9lfG1laNkkGLp8Yh5MBrc-7pk2ZR0usld8zf0Sd_uFIqhUyTnBTxXz8ZrPSuIOzs3KSjOfMoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVUCr1HfVWCXIc0Y2rZIgT7ZAxWupD8yxWpp1idi_gE6bR9q4xxPhBYDAN3lx2wOQu5Lg-D8Zb0VJ5vn1OapI5afJF1g-xI7Bf6gC3g9GnF8jxqOW9rBafJuJ0tUOdwjlZoUjkmS0MRpoIvFBbJpo5TwXnEkg-Pw_tJ33momZUoJAez6hhwu6RKLNbEen6KZFM65ylKyWUvxNmts-8vGV8Fg2ddL3ksWjhauPmq3UVgyTYZGtZppovDlrZdQerpUHKOg2x1oYuEdhzps2PTeiONRn0srLhcXJT_Uuq0-6ZHEbbD7W8cKx5oa_YwKkMvtK26SYw_qZZkujSNP83M1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1GWbVC0-WZgpD6Dg_edUAD5AhFPZfl3_JNUPIplsz4uZpDgsX6a-wYlPvWrHxXUuzVCyheK7YErZe2JC2kbUDGS_EA9AnrLkEhX5eLCvc3rAsB-HPoWDGeUJhP1PehsqvORFlUk7Yy1gee1k9IEC_3wIwLK0zv2KpCF56Fpqxxdje2cqu25SUIc7Z1grBvVWGkDxXJpqEXQmb-R1pp90ZO7EOlg4ZefRBm49M96yjEIZeWHJFUJJtvZjdtbWEJ8h-i_KbR5PfXKk9palzR-Wm4p8dfGKSnrGyAFZ8I6SAUhvpOLKSq1AkGQQ8NsB5EgKodj0cntwOul5vZW5EMpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8oplIa4YAhBkm0Sdn9T45dpmgrJy9f_CEUkO6c480Szx9dy3wpwf2PF99FwGPPzKCAopL80aHtlRP6SxuikYLSuPkPb3kKuUt-9Qjhq6sZhcqiVgjyyLqgC50Hg6JVH3KFmw6bDbQVoE4LaO3jkPcis6MAiwiYyqmUYQkVAgLGoNpGi-qAy-rrQfcaHoSwaL4Iehgmr9fIkP-TFZBkLZihZK4_sD6xcuqmevKu3TDLYF25zdWtbJiUMV2wpfIt0rr2CvkcPbcLY3uvqrMV9x9neUKloGuPndqex0HfPifJYUhqSYx7Ys7TtwFOUn-MpCVNNJVVtwjHoe_Z4meBTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh_8beU6fGqQn-pfHhqomX6hVl8tzckWzQWg2F0VsNaBYJL8k_CTFQZQ9lsHgDvLYYBkUXJLG4hOdKGo4vhjJJJgIJMRYkSSiQTlw2ge2xyct3HzfgCTdHr8icfNAsiCAD6fArA0VSpHbMGUSiaaVC-EHkaemitxn6hxVJYLZLb9-h6_3w_DEsmLc1Esgb39pTW6uSxFLvLTefAS5b71Lknnh1_PJnxus800Kuc8o3ZuVsyFY42CFvvoo_R3LZ9i-iI-8ZA0aD8TGBKelEt1iXB_fQUdGPeX8o2cdY1aJqrzmNDaS6NFqUkFOH9riXK9-Pp1jD2hCqZhn-eTkCOq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmNK9QzMwGsdvwyWEeKhOKXXxbs6ehQUt48SXs10KOmq_xzHu-WdhBUhWtGV1u7GpHyLBFtAigbfaixJ4_JCyHLhGjD9HVuCLjqJKD1_hWDRTqdk3vNxOhRZ0_vbLogsAUhqYC1qqp9f1v3UJKahk8ErR3q89qAyjhhdDpSxLGK0i_cI82ZmDCq4IcPhHnrHztbBM6o3EPsh601M8xJO9tJu7JBbNn2Cmey5PesriUb39G0PCTNzGRSOBt-nCvoWrcEiy8LQeK6VeLhKuQhV6FBAhstUOzwo6f0M2aLVFmK0YO6DFdloEYNZhrssYb8RWcJxieo3bZRk1Bbo8TP3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnrxII-XP1fHv4UeBrfl0BQGQQP2Dly3JVohWxFMmWexojnFsiuP9envquRLsFJMHyEZSZBFPl-zQCgJIbpwbPTXS_q-W08SvvYTjARTV4vxugIPtTwDHd4YiZmucu0VqrEGcMFMYv1XHZE6pnWGaRpzcsK8RZoZvi6LKDgu-3-FtyjGJgyceLPDQhAYHpYMeCUMvsrWvvO8IgSllZJdXCjlBWqc6L_Xjoh3zoaICTpxYNCkyOp1cfjR02YkaY6Jlf2VYAbSNCjr2TqqUMF7DjooSOGgRCPN-A7oi-iggekMbXRV5nPzuyFBtEd6grn2wNZ2c0STBVqnax6v8EmYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bckkFVuK4UvOcOmKL6_X3xhIDXiNZ4fEKW5bPOLw5et8xWpTKi6vBhD6kcfyVapXkxC4zr2y1Fk-ZaCIyat3wfMpxg3-dVWCzcaDbKUKzdJ-QhzCvX5HWSrTNV0YgrNtB-4P-K2kyF2trKDBD026-EtS-oIgK88PzXR1jyOwUpZY52N0lL_iDW5c4l0Q2AMGSDUW54X4rPQux7_nUwIZBwAdyozn0a3EEom9iMGLhlCPzOoPUizLKGbQXrHsAijk_O1izD8OXkKyYBDHKdw7xwwYBVnUeEIywQxJMYzjY7IooWJyCpd5-mG2B37xdzgXs2eLrgxdgxs0mzu-4og-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYBDoDivt1TwBOvryqkgYNi-2r8175nqe5A9N12Cb49oFBPvV8mk9OxfwqMwDe6odQ8jQKQ87kretYKUGvgKl63TugRSi8ZAlDgMAiMAghK1EJMMCXm8IlOD9zPgvNpxeuW3C0Bp56Mfn-MDf1XStbJE8iAPqiZv5-ish-Wt_20UiiW5N6rgOR2xHecKJoST27NV0BI9hTpEGpaAK0ZHIqcnifDYNGsj2TjBNkcHKkSivjC1taQ5j_8h2oTCrtVbmTud-b9HfxVHZDhfjeDNKwWaDa-xrncu_c6gi_Nx3Tj5_JWuw-ZtYuPkK82Z5kPbiuyghkiq6Imvn_eXYlHp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxiKLlof0q-xUvUVzFa6SEnvZdpJ2Z_GZm2lBtoNW7MLc_OO3T3_3LmuA0X-lgpUPisO1Ewmhrbpb1OImU9yJ4Yq6KkxYwnEs3xYFx0VtxdqxwsR8tyEbEjl_Qk72QEZABj50ymKsFrLzp2MEpPsry-pOVIJIl7-Xq5TPhOHZfwZVINaBuHR_Ibh9r8DkJsHE7rUICt5pVTD1B5NvkjddlqCeziZGiK35pyIuOwMLSZ8KUWiyiLTCn0wwAwCON6BYVDw8cS-U951BTpt4Du6nhDjwh7THKu81UFJDi6Oh2OCu6hHlCSKET8R3WsdRqQnQDiGe4A_fnriMTBidQL4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgw4ASrcZgzYxyXmA7UOaVMyjvOLZGwoHHDPIddPzi2nUnhRLVaGVpkznY99amMgPTJrcq_fV6mRazXSNsujJpEgujdHKOu00smwGoJsaU2GtrF4Y6cp01MrMEejgEakBckjqyDj6X8rLY4E4rMhbgX3y3mx4qe7zkKJTYBJZs9uPJHDmlA2-sPW-udyKYcKhXQxUo7nRy5oERGF6CN1h3ClvSz-8YvrIZYHXyp3S30C9JP9WAdrWvjpBbSYlfBCQn8bPQ09F_pcVzA1E5zeuEE_Yt110B17GaNqvQOynd2A3VqAw4jE7-AJUGwFRv1ZKLTJt3g-2RNV178g8GMieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=f9wuju8xxyZN5iNRlfBzbbwJAV9UMIktHWY5eF2s-B2_2G06_eby2KbmLFFUwAgJxztMd46bF4k04xvLWzcCo_rALk84k6MB_VXx_txXrN71GljLg6TeCKqTgC2QZ7wWbNQ8IDfECbcCmH_djvor8T49tpLstLvs9C-Hcb7KDt9Aa51BavgvKXFjHfs68yNK4VTCh_W2uwwne5Gv9KYSnjkwSt8uj1mqbyzrqeFU5uXr94y9MzFo94W0HpBaTJ54nxBOqcc7pE48f1k2c1igvYY7FMtSD3jPCmRaUWMSbp-eFf_E6c38xkuhH59-oDTiz7uF0UTM-gIBuRfpDDB4d16HTvl-9ZrWpvgxcNxB3IRD3JtpyLFkQpRvnfhXgpVDW9eRPnX_JsUENoY0Fao_vPFJwK7ESg5WmD8ARqGblqyf8d07HXCGp3dbW2vAQhuZjzmmkigdW68aQyVFOvpi3gK-EhHd-TkiNDKVyhoUQcpz8pOiQfRVI-OLiQSCDDXHOH36r8KJlbKQUg8Y4sH8hHw6_M9Ij5S-Zq96srEQdP3PwJC26Yn28qQSB_J2QGA49bxLyjmJMumrNYlnUep8BgztkTWkeny8J5EiYJ8K4AQcoILq46-W5EOk3QoFtCQ7FC_WZCETJs48OYIf_N5X_iwNEMfbBBlVSjNr2JAozVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=f9wuju8xxyZN5iNRlfBzbbwJAV9UMIktHWY5eF2s-B2_2G06_eby2KbmLFFUwAgJxztMd46bF4k04xvLWzcCo_rALk84k6MB_VXx_txXrN71GljLg6TeCKqTgC2QZ7wWbNQ8IDfECbcCmH_djvor8T49tpLstLvs9C-Hcb7KDt9Aa51BavgvKXFjHfs68yNK4VTCh_W2uwwne5Gv9KYSnjkwSt8uj1mqbyzrqeFU5uXr94y9MzFo94W0HpBaTJ54nxBOqcc7pE48f1k2c1igvYY7FMtSD3jPCmRaUWMSbp-eFf_E6c38xkuhH59-oDTiz7uF0UTM-gIBuRfpDDB4d16HTvl-9ZrWpvgxcNxB3IRD3JtpyLFkQpRvnfhXgpVDW9eRPnX_JsUENoY0Fao_vPFJwK7ESg5WmD8ARqGblqyf8d07HXCGp3dbW2vAQhuZjzmmkigdW68aQyVFOvpi3gK-EhHd-TkiNDKVyhoUQcpz8pOiQfRVI-OLiQSCDDXHOH36r8KJlbKQUg8Y4sH8hHw6_M9Ij5S-Zq96srEQdP3PwJC26Yn28qQSB_J2QGA49bxLyjmJMumrNYlnUep8BgztkTWkeny8J5EiYJ8K4AQcoILq46-W5EOk3QoFtCQ7FC_WZCETJs48OYIf_N5X_iwNEMfbBBlVSjNr2JAozVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQGcs_67DiVEjR0UJQrFMmywlr2mmsd0gFlBne1GxcBoIZ0XLyffaTwMOCgpQqHDkJ1ZUXZ62qH23z2DE_xC-d6jfdbdswt20qxshusz0_hnhcU1G5JWqxioe9GcEq2f8IMzDO4urS5_BW8NdDoHv8KISUSnMUl40xPPcDBx2Dc6v6CAdLkd7dz9bNngl4f-GyvapMP59itzKp8EcbKdubMXdcPrhGL4Oveg1WDE3ZBlz_mZYJ9keAq44j89bU91x7VWNnxxvsqRjf8KueNnHNnqtDJRaVDOg4cRudiuIAWQL0sNAjRWESAjHqmoBx6njLC6-MCXE9fnCUnFNlfoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=ScWqIlHlMVetMlo5eRqk2ZZsLU8cQrstjmHZDNNpTQhCGJLttGzR0v9A3ivjvgwAOLSCWQ2W2oAJ1QdhLgtkMLOFH_sook0h8dDiw5FMj_v75ssXoROSgKfHUKvrxRMJD0g9Jr6R4WN8L74kbRi5coyAfQlIgjn85eR4dVGh7nFfPPwUfcEPmy7LOmoo6DDvmP1X728hLoWncFlZ0DlVsRJuA9S_cYdJzwX_XM4R9XZZ6WSkD9CtJVBZUBdaqMpE1sX9iLTwcc-xRfp_KnGjG-0LZmG7UnczzART-SPosyNvN-5Ug8qBODz8jTDCh_3kC83bnw7YAkACNgtZ06Gtlan41oJ8hHnnPxo0fj5Ylmy72BBUzJ2bQu59OVgnuCVESs6WVXPUT3O5k-nBF9IkO_83j43LvJ5LcY-JSqGPx1DAiRwQ_zOZ5IfDlRJC9EhOexlGi0Fn8wgjuwhXN5wCitUsouN167QwxCrmTfB9B7Ki1ZjVMWjjDVjVgNfnm1wGDVXyOwIiHLglrJgVnlUBXHnY7LabOJubFoBm-Nz6dcxjIKoWsAtspFFW3tpvP-h6ODdXBTeZ61DfGUXuh9hMG2ttii7N9rS8qeeel6VseJ29MYFFH2G6sp2naELdCDf2R8iv6DcYg0TdqsKAAAgxp6PFcp9-2FhTa5CVO9lbeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=ScWqIlHlMVetMlo5eRqk2ZZsLU8cQrstjmHZDNNpTQhCGJLttGzR0v9A3ivjvgwAOLSCWQ2W2oAJ1QdhLgtkMLOFH_sook0h8dDiw5FMj_v75ssXoROSgKfHUKvrxRMJD0g9Jr6R4WN8L74kbRi5coyAfQlIgjn85eR4dVGh7nFfPPwUfcEPmy7LOmoo6DDvmP1X728hLoWncFlZ0DlVsRJuA9S_cYdJzwX_XM4R9XZZ6WSkD9CtJVBZUBdaqMpE1sX9iLTwcc-xRfp_KnGjG-0LZmG7UnczzART-SPosyNvN-5Ug8qBODz8jTDCh_3kC83bnw7YAkACNgtZ06Gtlan41oJ8hHnnPxo0fj5Ylmy72BBUzJ2bQu59OVgnuCVESs6WVXPUT3O5k-nBF9IkO_83j43LvJ5LcY-JSqGPx1DAiRwQ_zOZ5IfDlRJC9EhOexlGi0Fn8wgjuwhXN5wCitUsouN167QwxCrmTfB9B7Ki1ZjVMWjjDVjVgNfnm1wGDVXyOwIiHLglrJgVnlUBXHnY7LabOJubFoBm-Nz6dcxjIKoWsAtspFFW3tpvP-h6ODdXBTeZ61DfGUXuh9hMG2ttii7N9rS8qeeel6VseJ29MYFFH2G6sp2naELdCDf2R8iv6DcYg0TdqsKAAAgxp6PFcp9-2FhTa5CVO9lbeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqgHe5uEZXYq4LeaR3OoJFiETvqLda2C2YU5cH5MFZgIzqI-7L5SQLHuvQRoC7cxGAbMF2BvG0AThgKzFkUEX5sajaXmMHBfTI8KW3O_YvUkKr5vWl1uyuNcxKj50VtAW1EEjLsDtIMsJkkU50k5JYMe-HzNFlaaFMVYgAql_rGXeMjoOSXqBNY2wn6bf85WtGP5C3tVbjXso_o4iRbjI-Rm_6zzwkx5egsI4hrsE0IjIwU9xCdduUCekHaRMtwNbIKFuaSouO2ZSZHZKqguLasZuCz09OQNwhNIMgYc0QFFlAFnL9ORGA94iaRyBMMVurRotTuRRIl3FB8fFhx2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=u9-78zDhatb4bfp0sm72Cl6HPXTCvmLl-nk-Dx2uBHSu7TufNtgvgwP8jAOPJQcyjVkPvlgkCnZQyQxptvMF0c0Syqm61wXT9KXp9uj-VH3UGWqji7gKZY9b8ZHKXJ18rxRUK1d72Q66JV3Fzw3FW0jqusntojTDpbixwK_S9M3TcMmv5brZm7_VtYXte-aizdt1o2ovr6GuArPaYMtVD6NMQdef9NRVwJJbrIvhq9I7tBsotgUcLAH_mTu8WadhHOHgMRBLmHcP8XymizdwD-KAJxMyFq6_I8D6KCt82tyOI6OLrm2HlfzxRipKa9MsObvn92gBj5H1ynzF3r9tcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=u9-78zDhatb4bfp0sm72Cl6HPXTCvmLl-nk-Dx2uBHSu7TufNtgvgwP8jAOPJQcyjVkPvlgkCnZQyQxptvMF0c0Syqm61wXT9KXp9uj-VH3UGWqji7gKZY9b8ZHKXJ18rxRUK1d72Q66JV3Fzw3FW0jqusntojTDpbixwK_S9M3TcMmv5brZm7_VtYXte-aizdt1o2ovr6GuArPaYMtVD6NMQdef9NRVwJJbrIvhq9I7tBsotgUcLAH_mTu8WadhHOHgMRBLmHcP8XymizdwD-KAJxMyFq6_I8D6KCt82tyOI6OLrm2HlfzxRipKa9MsObvn92gBj5H1ynzF3r9tcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9B3UU_2lRsv9V2DpHfYU7dxSjMIzsjX1U_9bu8vBN5Lqqq77rhWSb5feg6OtA8Ved2c3KMoQhGn9zGB1kz-uKx10GDmh-OO5H7LapwwaEGzcJUbj3dzl9inTfC5zg3ONSDYj9FWarqjCJBbuITcbzrcK6mh6luHjMmA7Ls-eGjGm_H8tRw8DNm7mINmPIkGQcmt7hnDEW1H9FOaGArCxNHUU1ZeD-9ssWUGwkp38GNpremygwOlyw8xlNrgTM7IXwejzu1Q_N2Oa2cTHRbMqGE494GLiJ-N1oU99R4f_UTKsSn--tf92vY-yqihA6stLWwrQJq04B2lrcHywBBHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdDIQWtHHpSk1kYSUFQ8ZFY_U_Rl9CH5NLzGH8J2TsPjvxj6lTbI0ngcHKkKShwNhfVqAylNvHbWFpMwTaeKPlIvA0wO9RqlLoT4l61OSOaxscBuAJtRVFWRn6bMx6Ap7V7em9jrot8RTlSJoF7ydcKk-oIhjojXpwuHTokYjEXpU9Mb73q18OEt8vm_q7FlrK_dVRDhh_NnOL1rPYDOdl7MIeVwWck1ZPG3OlPDE6K-0tdOHs0HwmQyooZRWAfSoYCfuLwb0BxJJ6Et-2LxHpY53njzDFtGwWKhQmvjJK082zNtNDJ1BTx_v-4PrQXS6lneEFI_rV8JG_n3sXtHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXvM4eUopaC32RsVRlrrg5URKNqhu9Cz1JqSftz2uWI-3Q__RcJ9nGIjpZMUP5oRwgwug1GMkoUY8B8KJKo9bmG9srdmhbFs7kgGeZa5WZq7nEue1XszX0I4IYK8q_oRLHbQIHc2yK8Sl1kkp_anXhKhg_rYsQkcRzCwnZsoyKmWDZdl5rOkdyE2UBTDBkjraLu0GQsJqDv0YafZ2pFhi_LqiFJlWeUEhELYO_hURCHkEYqcNyi7AQ-zXAhrvYNIa_iFOuXpUGmvZBBhd2WyRNVHI8IcmQsK6uaYNRgGfuAuqfIiqQjLB6ESpEgfvvT_YSMFd9vnH_rL6Eqmgwxf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GphNpWvlWURWSnF0gb347DfVEWqCchl9eCfW5JnBVJRYfFtpuCNeBo7wuUle8zI1blR1MG2LsSCB7nHqsw6PyfL_6i0zl7wsvBh2c0PXyFZrwwWzcu9_sFnsAnjF_pMxcXGzgpj-wBgLqwORM2DBwPJHVe4MdJEI55FJFrS54zVOi3hgZseb-ioTCeCUV33jx1hQ3L1LHZIepckd5c-aOB2iUwcM104tRNn47L8nWhCnIbsht_ZWt6LPzUKywzX_h1bFOiu0MElaCKoKR0sNS-o6IFhQcWWbymchCby2Gj7KZ9GvWp6d4zfG6WRpOCzaVjxIQUhLO2mM6OD4u4fzXwL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GphNpWvlWURWSnF0gb347DfVEWqCchl9eCfW5JnBVJRYfFtpuCNeBo7wuUle8zI1blR1MG2LsSCB7nHqsw6PyfL_6i0zl7wsvBh2c0PXyFZrwwWzcu9_sFnsAnjF_pMxcXGzgpj-wBgLqwORM2DBwPJHVe4MdJEI55FJFrS54zVOi3hgZseb-ioTCeCUV33jx1hQ3L1LHZIepckd5c-aOB2iUwcM104tRNn47L8nWhCnIbsht_ZWt6LPzUKywzX_h1bFOiu0MElaCKoKR0sNS-o6IFhQcWWbymchCby2Gj7KZ9GvWp6d4zfG6WRpOCzaVjxIQUhLO2mM6OD4u4fzXwL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neoCt3gmThd667ec03PZeAoTHfi-ifdmMMrfU4YLEbN382ZtO6vDcqejdWUkFs-TPaahvZikXIR6LE8HlhBEnmS2r-1T7QGcLLOGGcWrV4xbGPj8Ty2HsxTnS1VQo95muWvf5SPzDBUGpI3CPibZg-1VgiVgC01nl4Qq2WO5ro1fC5innh0uC-sA0RnTi1N1vQO4A1TWYq_V0LWEiAjMjJ7yk6JtGU0__IprcVHT6UeW__M-01nyY8GVYBJ6MXle4IBmWrZ10d8KLco7KHyXHwx82PQbAZ4DXjGg1QIKKrdO9H6DtCLZACgUB_VHv1AWgGYjsrQsqQ-7Uj29dnilfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LspwVernV0h4sckvtUgE0wlrLxzwtMloHkvMxit7IlxVbvKW9o9CPz2d1rFGgUSts-bz07wDc5URZ7dBQMzCNPndAHVZlHwx0X8SPrGOL9YWHp2HKshqiiQYlxDSYU8OzXtzfFVOtbZ_EzvpYy5ZumwElda1QnF3gvS51ao-pFHj_RUsaFyNnWBq-NplRuicDJ87PCVlUbAP2AXr_Ikr710jj-B2NKrAdEVZc0Xhc9C4offgvjozdfT5BSUca0CediX7Y-Pu0SVAxliEoIzGMN5Yo0ryRtHTEHo-RRH0g3JlVpeXIugNuD8al4b9tAWe0YzsHgm4XbPVec-MqMj-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tukwd_tuYcFUJupaSVJa7XRFQ7Nz0C8BQFSXRa-j2AOv5cGJn-3TZ0JuHSOWKfGG2R-bOu551sCia58TSlqF9KKF_YKAR_iVR0EEOB4iXRfUeHPffCgmAyEgcMGuBY-OzJw7SsyLWCYTeETK1M9_FnZk91524zcs7GlDyLyauMIvC9diTGjlamXtjmN-k5LRPL0_6aW2V1ACPv4SK8_UY0ZlRnB1PHqtruZd24vi77vp6GJhUdqS_SG2neqVN8W2KKIe5zJ9LFDJdXDONKgksD4jYKwiQy4Q2aJg0kZ9odIpaN2jG9aVBWJUzCIOPz9M1Q6iudUHsR05ITSzobBkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzoz1XxNcw0JjjZf6zRyF5m6dax5vMdLMRChHsefzr2jjrtaOr4zdfm3nhpuPzD4rXqYJaE-GWD0GQGp-Jhw2Y6Oyco9bC5wBrgin1YBhiCUqQS9Y8qJzyneH54Y-naFUCtTDL_LumFbtzt6b9qUC5RYSy5DWift9U2Aac0FFf_CJ31eGGKnV3aVR3kZe-eTsLRO9i1dj6-a5r7W1Awm9uYlIGquil4n2dj53_H489ZHpQiMjJbEtx5uQifHzHu25UEbWhMLQozepn_jPmdpC65EMfjrr3JrslXYSAQt3punq4WdliM1BHbdJu4EqDZEgfoZF2_wu6lC5trFjJWnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAxyMcvlDDp62DpN6rvUxaJadNntQGefrKir02iekzyTgRtglqcqLwsMBYuF-Cd3XiPucTJEgHN7uKwjYsUlBCOchU4TJ-1iUeMYlTncfoa2Z46c1r0ibzynlaLGSNgx9O3Esv6q8WurSdjEQNKs-lkfbeJalqP65odfNUbJO5Z6JK5DU0K2HjKiqqAq2bsEVVMvuxK1-zI_baOV4kt3UE2LAUlHEejmHZ3cT2MgEA1WW5C8IuHSU9J8VTSq2fxg1NLeWGtQqtUzVkuZTqTJei7UT8KQUTjkR56Hgsr1GnNSmLEKKLTttd6wLoZepM7LqR_qRYS4pJv9YkA3IqKOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=M1LNofNdlmP4kutK2hKcBrTt7ZkGjDjPYm5qdaHF1Zi3ThwXKO1tmazawX7UH98MpmBjCg7T4Fm4GvgoKD-uBGB9XGoWCFX0tGqOHvCjSck3K4-m1eIaSmlpzsQ60fq3W2cUBBMtQBEZDpicjnrEWAeFD5ntFeJsXOQj_Lr65VEK2E6fMiuq1UuA86_xaDlC4R4vwGkRqruW1N9aIw3moQevpPqOBpcMSIzkejzTBl8QxZZ6l41dJlRxGS9sWBozLUAFz7AtP80FS0P-9POUnngCdseaM5MG_dA54ctDr1Kyy0siwv9gAJ-56LdRd1AHEx7PPXRrkXI9ILALGWFn5zgaBbrTwtinho-ifpzzNE8uHF6K4eER42AHBSAbk1k163TNG5LS3AO6QJABQf1oH1ysce5z4BtRv_b6O9HHmS-RaqDxqX6cUYdjm-9GXiCseVh15GkMPsFRiPRRKCWn4Dy2_iXJ4xLeMDaUkueR5gKySXPJeU44GQJQmiQMkHjL1Rll1Qe79YZ4mS2DxdLyPe0cW54wuhS49dUB7gEbrTmcOfaLbedv616ObJenMStQqzyJ1U2J4RemOIxH1twpQ6-rmdR18vRkvjwSbfTcsQGafaO_BxPnHBn6dk2oPBFSf_UNfRE9UlkChX94Qv-vqDGMyPPiApVajj18hskTKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=M1LNofNdlmP4kutK2hKcBrTt7ZkGjDjPYm5qdaHF1Zi3ThwXKO1tmazawX7UH98MpmBjCg7T4Fm4GvgoKD-uBGB9XGoWCFX0tGqOHvCjSck3K4-m1eIaSmlpzsQ60fq3W2cUBBMtQBEZDpicjnrEWAeFD5ntFeJsXOQj_Lr65VEK2E6fMiuq1UuA86_xaDlC4R4vwGkRqruW1N9aIw3moQevpPqOBpcMSIzkejzTBl8QxZZ6l41dJlRxGS9sWBozLUAFz7AtP80FS0P-9POUnngCdseaM5MG_dA54ctDr1Kyy0siwv9gAJ-56LdRd1AHEx7PPXRrkXI9ILALGWFn5zgaBbrTwtinho-ifpzzNE8uHF6K4eER42AHBSAbk1k163TNG5LS3AO6QJABQf1oH1ysce5z4BtRv_b6O9HHmS-RaqDxqX6cUYdjm-9GXiCseVh15GkMPsFRiPRRKCWn4Dy2_iXJ4xLeMDaUkueR5gKySXPJeU44GQJQmiQMkHjL1Rll1Qe79YZ4mS2DxdLyPe0cW54wuhS49dUB7gEbrTmcOfaLbedv616ObJenMStQqzyJ1U2J4RemOIxH1twpQ6-rmdR18vRkvjwSbfTcsQGafaO_BxPnHBn6dk2oPBFSf_UNfRE9UlkChX94Qv-vqDGMyPPiApVajj18hskTKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3B5Q-N_wvGj6S7q2BRZh8Rt9BUp1NhlTrOR02d-9qmWzLFVIjG98qlygCT40oiAU0OYBMtRPuQE1hFKBut80KYCAt6jy6g_K-Mg3_NxT9V9OnvKJHHYWjFUklAf6zTaUCxxUn3qz1eELYMp1fSeM3mK5dhafvs9rMnCPJl12Tj1sToPGmddWvLGTKjwMNyvDI4974d9rh7_8n3gtlxRrbsXCXSet5bbUFQNKZrkUAQnzTuXpFaqceZbefgx4DQutvM2UFNd7E1btiOlP1eFKlfN0T31Fa29h9q5xjLqcwXhLiINAgd1Cu_XJFDKO-RnEyIfI3AposHhKDihJz_uBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1xQftsGJ5XOGBI5GngHoOenidfq0eUOK9QY89hD1m2sJF3quOcAcDuvhcmEkauztNXTH2oz7mwBvfAOUCkwit7FXKGqQFpAYEkT0u6IkDd_i4GJpPClqxDdKkQRLaie5mkqEjoLOPClqPR8_fJO5HseG8MP99EWR0WyVh5jnSpfOTTZa8R0gMg1SU_cge4AVBjM-ZsENr9p04p_i8DIGpuphB21NqV64hvX-X12YQvc5DXpPleU_l-2_qKCYzeY0WJq84nX5bU4_6VauH80V3YgLc8KgDqZzdQQZ3ttZEUP8zFouERJ-cdi-wG0iJuNoVsREcrcqVeWZQxAABTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

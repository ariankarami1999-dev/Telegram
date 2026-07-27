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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6eT2TRdRog1O09sbpIQsD6zDFiY5F1CjVEOC_XC_5CNFj5mZASKkT3RkwrkCH_feBaShnkGlE1X38DQjIUFZE4MEnYmiCEmn79G6ndMTNh9P5Da9qdYllQTHZQdvs7UNWqC6zM4CyFb8lJk-3BbtbUsugTBtSOyoJu6gSEXCYVtPBfE3A7jkNMr3Urtr1nVZkvoebXULBRgdkbe2v2HRIxlUaOsXeCxsCV6Pd2PsRjcqSKRUPi7t1S9BBnOeaaqBU5x5DLdTNNYH3gKUbN6mPeZuIY5_wzglKbXYfydOq7y7BKT8aLWkfvxngrMWjlzZwJWKNi52Px_zdCDvyS1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLSitPygeGoxr_AuXNpCCVIK6MhjTZPiwDLbskpcivLZ0Opr8OW2O_D0_FJsSJ7pN39OS7-_8o9UtnVxoB8-7K-2FX6viJ3L8qwMdZabIS7g-t81tqxHE_-l0hhDTswYSOj-xDZ7k2yzxrwkSAA-w7G-YYtw2ZZqCGPUQGFFrKBGQoU9CRRSbHD6jOJyULUNoIUdu0mZ-qH_zKc2euPJSi0G3LdAwQU3iZsmAQ_KmnIDHFzJ1nzE7TQKNd0F9HUEbfEUlcVsPAmmUCnnG0yImhd9-zAKextann9Ho1UA2FcHmAdXiVLsyZH8Qd6KXET9wf0S1Ul_KegBthkFhO6lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R82mskY8wJdk60za3piXD4Mi834o7zIzaq14QtK7F-gufUJJuBfe8suaBnlNNzJzsLxMtBd-LwU929z11mjUfimjuadKa9haWIA2XXWxO_ZIKVm44m-JGWdUKrmOHTI9NmZ_Hpf-4My92_Fr-DigjK7beeGrSKsWUSeff0cEkOVi_7-FOLI5zo_ftqsBSKHTvNCY_AkY4EZQP_apmVTmZEohuQHPxEaJEVeEMLpyvPvf0FdMJ2hy5ttonwaGYqPh5c-TTRiiI1s7Z21WTwz1iCetg3CdnFFYz9H-b0W-3ji_0tIgMgdMnCVueSv6eyH9kf38rSff6ThhqFCEVKN0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmjt9P0zyfloGGBuJ16PhW8BH0JLWS82_T5nEHaTj2n_ubANHY3AuaE85oLfGpFc0ZBqKqn-rWm6JJRbKGSV76Shts2F0BW-_4idvPu6N5cWZswu8ZPBz9pUSKCx6SLRQTjyNnNS90mqftKnzzSGMkOClWqYMkiuVbMEXCVxI0s0fGKHqDee5kujJ6FAK_FSJD2wiLVNJz-F56qbkrhyZBIcw4A37UDEqaoEreBj5cgXszbOeBGRn9AyvHstziY4RcD_Pt0L53ziQKL5KcSFYCM39EpxoBvfnHfrLPqXmjVKa8pFPb8yd7v1FXNJMWUm7eDl2OAkIYoi1fyM2LNLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9MRBlAxdm74NEl5GaUuZSPWCPEOqhTPlFE5LjPThfUpbURxaeGyGfK0iKzJ2gqbXbuuwtSxzlyeyLpETC5ZVpTqUfCmhTufEJ4rixlo6hZMYW8mqQ3hWFrjaZ4UMgM1enx3JqU1PXla9FNX20FqY1AkCKSs0tbApX4A6xKu5--tGnWjoyaVG2sRfoR4FtlhlRSPVcRsjkq9adch9dzVSsyZcA17nEKnVJNS3PNXwHHNVH2Z_xtck7aMLiOgGrApKDJ4OuBr5_sbGw89CzzZF6yt-11D3U59FgX4vD4ahGGKc1713sdo8imyS2N4lmRETAVmD8NKY6ds-grBbG-eAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZpQQrP051S-KFfTfSqMUtE_hL30UuP_aW8lqMDfn4vmYnSDMYYKs7XWooRtAsU_CmfTlKWU_PBvoPIDSDHqm6WE6mae-XSNAkRbQQAgDCfH55RTj74DF6UA7LJ_y-wz6mg5z97wkJxycYaB1Z8uFekuqHLvIBf-G48vcBKKUTpOofcLFAUH9QrsiDl9TMSObgzdq3agY077B5yqHfHSkbgc5usP4xa_RHQOfHXKY1iXWWB_KRlowl6Ciz2sNkRQwNkPC0tKab_hx2ao_20SrpMEcrKTP3AiRgLOOlBsCpxhyQ5-vC998-bnR-qMD2GJhqU8AaGr4j-zU16Vg0SoDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz1df7hhp4f7PVLwPdvQoXj9MLEiDOQKsqOtUMZQcdcb18YsRQ5wG6y2M9Kvd8TYYCfdh_gsGMjF9Ab_9lxZlOsBuqcJ4F5mLOqpVz4H5i-9xjFN_YJ58zpn_YsIixKGPJ3HF3HW2DSwiS_TUj9EO510mUyobyrWlAqR9otxuHOFgTRlukSo4PTzAdI6xu-ws1jjxWF-ssINpoRgtDaWUQFqlrkExFm2Ndn4I8GIn-AMyidkNylTRcTmbiPkgQds0-Vq1nP6I0TrMjDbhKcZby3mg080Gj8LCeT4pHcaU-o6OvqhTl5uP_hd4HnrlsGqvvUsWRGSnK0DoUH_SHE8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7fpdajI8QhyT1g0_EvorMx_Jn_3np6Rvb1601DfP13LLBySbtwSsgmQlz0co2StcN6cM-NWGOsrkPYiliaCkuT1jsu6BsQsplqAJcu86xHwtzbJoDKun-uki0-QmdQr9204bkIrYK6zlt8-LmO-dPDRUSBPRulRZ_AhGh7v0qjJhlNuvJJ88R4pjqsTt5ugGy-xouNcfr-10ir1wYKI7aCemsgnNFQzf047AbhF7it49YH2w4FVPr6CSqoJ7gA2R1__quhCU5klU_N3Oe0bS1zpLcJ2uhZg2Nrbog47-_PGZ37xrn-wto_TZS-BujhZ40sbiouHarcSpYv9eQXmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR4b5lj_5-ZPkzkIo0iX1F5uJMlOAnq96XfBkgEohSch7LUqnUaGm1gS5uBhm87iosMFqjEG5eUaaivwVRsW0zKOW69aFgzZC1UOHTW63rks527sFvmksXDZfwl0Hc8iRTmqAE4z9V4ddDUsKVL4lnI4jC0chV8JMRLzaXPJ3PdJfZP08SSUeVDPUoOo5964t_qfvzf6-9yHMTZ8q4ec7kFZgRFw9ivYoURRwlCzYOZrGnVwP7ZTFVPatRaJNlPDWYL0NpZ6FHBK0wDHhnRIknYb80Cw1xBomiepgcAOv1g0sTWoyGh63Z_Mmydso-WARxAls2glht19dBgP9IlYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkJ4-vTcXbM4SRrgnq7VoGHMCFdyB0Bp8wTz1r3dSJ4W9HqniI5E1MZG7RNDZUkI0HtMVdefQNEunwkLNCSSaA1-Z4cHK5QKaBgZNjd7vd1sqwpLUsgmkbKfIuOiRr480iKg0UPBSZYsVrSpKZDKj_W2jy4vhaXJaFmnZxPh8hjC2T0LCiJZq1vCU2Z2sCP94vn0bpKJxsr__IAdp8epyOjEcYeZxPMQS9IEs5HfDBWOO4CaHN3BAwN66NkEWnRLeA_X4PWdVBFL-6X_j396uqsdsyhkMd0OE-WQBRrvcvmj4ptuM4ysc-LxeTfipTcPD9LVLqRlC5L1RnkhPiS_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCdgPHhGNtwBHwcZsYy4n1yDcuMk7bcUsX-O-f-Tuji_sUiuO7mf0tkaz5qyxaPFNEEt9t3ab5q6svrFJNPY-S8FwaNHw5CNgxj5F5HFIKg2HePlQYoqh7RCeSaNL-TgdIcrhoN4oUXhE7IwVcdr9QDpZa1stFqp2sL1QNMCi_e0n957AQdN6alG_uaS_VrUPN25H_5cF9KWE4DkqypxmfDvlYOwgj_87uwbtpTRLcWw7DYmm21A3kGu31hrXrnEAKAnc0Nm7sKMyQeR9JJ-w08Bu3JaXM04crFnWMntsrC56j1mGRglDOy7VBBjuQqVGKFah-Ejok_Jx89S_tCZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAPTqI1z7mvKdRzmpW6GNUpHhPQsmQve_jmnsND3ziwbbYQbNnerueDJiBIQKQpuAXOycpt5TDybpIQpveFORfszSEKXaGe0ZAlVMlkYhhlTVGj6oQ_m8xTobMdNyJVVpZrn3QTugQDVO-Mv3KpyO_4R7--cWBbGKkKjT_AMvwbzE0qlt_1Ps3kqsNoHvJFSB1Ida0L9C0trOzMaloI_lUN_g9yKt64_1bmd7WTTbt30V4qnd1mHkpTUrXbndl_Uz4D_I1c3TiWSkBcWFh79xujaB_CNmfkjDiBynuw4Jj0k3CvLLZ-ZEGSHg56nLKqA3PoZBAFvgzYqs-3HqBEHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtqF5hwqGFb-gLcvQb_ydyEX4Ba0R9u33C92WdKJ7S34stbLLLk4Z5SCazInRSHa7y6YSwFqe_vp3gbTLBDhPjMLsqZpviPU3qnHFdpe9_sKiYbI71b0Vks6ve9nCGVPZ_clAysXennWiAEyqSE87QB2ZuS4SfwXTOU_7bX831dm41_Dv88sMhYoR64OVBkCgeEGz8yP-dJDmlIbAa5gqOGR54b3dSj4qG2VA2f9nIgstWZRBmfbSPdHUDpTrssOfKUH1u0MfDKB11kNzEi8jyv9fbdKY3I2t1eNnx3VUIFNGcOt7M1l3ErHzisNcUTCNpAzUGbI2SOvvb8apGOzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMV-pftKhYOWpfGm2xq6JrQHqzTrnKZ31Q-O63RUUXkhGE1ZdqAo2bh8SK0Wyz3vBi_43KBt0m2WATcgMAVSGz9MghC6DraSaiAzukWNxXdem5DgfXcumeidFPJlUlasekv_uAx-s9qMNIOp3wzokuxNBxyElIZbJwe3fXivd9hHzfArgx1IKZZo-h2Z1xh1ezZ9KPyFSdeafCkDVJGquo1v5MSM4fqkx4g-GNEPR9uqXZGZBUDCh-5hi6YAg8Iis1OWMPnMwU7VaRMbHot2jhlSclau4rjez3mTY0zhBWZhdIG_JUzKri-VhejEYhkg6s3dZ63GgAWz1wnF-_Pbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkLvpZoCUj1MOsTXPhJxY70qluH7YQgx1OKht0G-0qk4j26Y6_SGwm6FGXRjZCM5QABi4oIhM8KO4R8jUo0xpZVQgM3UgHQBDx3lCCYhLz6OIJiwmg65VloNV2o2kffNoOR8v1vqf-cpcBP7KZr52ixBHYPdS6XNSN-C83q2eT_TqxJu4lSmtWMIhlPckh69ckfKWg3aogt1M4C0uY7YaHIMrrw_Dvq_tIM8Y5Hv6SCauvtdDELeCgkbvhNlMgRMKSzGnFmUprZ5BRO3jvobluZS3eOli_jHWdtFTth_-mK7m-_fmfBY6HjnNRpEqrA-6AFojK1tomVR7lCMPqsYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz29OJBL4mD_ZKr5nnMUFD_2kiddYaM4W5mS1oo03vM500NPQBP-bqXfRvtKjBPmrw-b-W42ZKqAw_c2D0_hJNGwVZwBCLrfTUQBRAc-NegRPbjneJTIRNma0auUhmkhNSV1S7IHnlEdyuTjCW5Cd7em0ZUzu_Yh7mn_M_TUUwpFaEW2H9bVY69dJBlbfnbX6OSnarsdSsH1F1fR0Vh3Ck0JYjU1pZIBHjd8pMs1VnDnKcdGUYYNeNH9VY8xRQb_JRXg00QJpzIoFJMJJu0y-QOJXyrygeEfcknqzDjbpeDVHqlbQ46uvSwbzL5zLiT_DB1X6kIoC33hmIjwcpUlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIiVSnyc4yRltw0ce7bcyJBgY7daiA7OMtXziDbA4dSLPRAm05mRCOIk6gp3zhHMe9-3y4YqUy8V1lfUKVEt7cINNC8DUkEeYkAe9AZ2poZOawql5YBJSzNOx3MjHtfXMOzS4Cf94XAWcqGpq3k_1MmJBIUdw2cpD2SM8-A9Db0HXUBO39mJiI9MOgjTMLsmHhQ9DnuJRc_5tiPUWSZjLHq2hnN1KIt-ohfANkbwH1qwrGjiTAZCHNY15ygwYjdsW5JcSJGAdkyXZUgFDa-gQErBK-P_dil74KRnxXazzZMv3gPS-QVWjuiRsDMJ_4lATUS9R-x2KHZdpj8kgUOVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0PoEb_OQXmq7gA8anVCKK1rJNvg4vMazzHO8HDUMgVHuT2ihy38UVvoPUChu_zI67SwDC1xGPFzrrvPHDMlij_iMhPux4C36Zl6eLzuJ9IFyCbSxvZAYW2OgKqLNYOO_PjeaGwOFocrx_iRu0RhrUSDRJQ0Yz1h50gBv-gxJHIYWazXgSuaJozj1q05SPiJd1orqj8_xfxv9ulX7sHmywkKSIu4cAViddWPDQtmQdjAbqsmbdR1KoXl9j8o-pQW0N_L9CbPBG-jMspQPEqWBDScIdsuJS5hX1LU2mOFwcrmvu74yoiWE9Cze0xHwE2n4IdtI_yOjSbKK_ELiWPRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMCXG5SrtWUpOZDwGhTzhoOiuz84awnGRwHLFxmMkpIqi9vZCasz3IESO2nWwQFDKMknB315l9_rqTGXOkpodfIjWB4QJXVb6Sp8w3yZ2uhWaIf9uk9sK4RAx3zZTi-H5P7jBMFVMwbNH5OT2HH7FTQQr7NIIPztvzIcMglSb_PjDKd4dPXSOeP2s7Py5HKwuog9rHNzOAxAEEavF-VcxuYHBLv1RSUg0aOqvCFl2aATg_fg6GQFMyT9mc5sk2OrCRabaUkBy3KheCZHprrMF1ii5XDp1pDvi3VjVklDjCsdwOqaQ6Cf-mmeZfF2z7kuSBp0PZOBrlwfSMC8hokeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=Bhr4OQBLNTrwFnMRM-HmZ7ZM_Ic8b_g3N3ThSJyRgeIYs2Ye_pRJfgQC29zvOb8R0gooEdi3j3txLIk_znYQu9mFXP-1w3Bd1Ygx7MCDvwx9EE00O11aGfe3W4RseO21zvh3g5dER6eDGYOeXl2gBqJ61PeHhGeYJpcZSHQt55GitMBHzDVFdvKwsjL1flttIkAlCGTPrE-C1-r4uZ1nsgnSvCBenfkgsmwEbnNtVNPD3ilVppWDyqgjhAxtFOVado3ZvqALz-2tYO5Tuu45k72kt0TTkD0qEs6zbC8uxflkpI6IaxJOO2lT8KKTmCA3lQj08NbZAdPQr1H8h9Z66UO7PlHhh86DvrdFebuHAJl6tQ2GRqm56h-6yt5XtGC2Aar9Bpah3ThE8sgvmXMxuIvpmG4WgZgXGGLmUJaImhdNKfMsugZHRcrGdCKFyLtnQLDE3OIeI3Nx_Y0RKPZTl7iUzFSIbEZI7VgxEccmkZL_AnRdbnsHg6CbTe2chNQihgr5lTXVKAA9z526uwPIfzrBfzPkYp15erfwCNGucJ5MNuLm2-O6lUcBCtJZK3kFwhrEIx0HWxol3rQS2UBbo4kb-z4mzOmlx0_cp5itxwL8vX2WqdqYMn8Ps-edZdILZst89lCdm1U62rxYHcHPbbp795lqG_IGOTqy3Hg0Bag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=Bhr4OQBLNTrwFnMRM-HmZ7ZM_Ic8b_g3N3ThSJyRgeIYs2Ye_pRJfgQC29zvOb8R0gooEdi3j3txLIk_znYQu9mFXP-1w3Bd1Ygx7MCDvwx9EE00O11aGfe3W4RseO21zvh3g5dER6eDGYOeXl2gBqJ61PeHhGeYJpcZSHQt55GitMBHzDVFdvKwsjL1flttIkAlCGTPrE-C1-r4uZ1nsgnSvCBenfkgsmwEbnNtVNPD3ilVppWDyqgjhAxtFOVado3ZvqALz-2tYO5Tuu45k72kt0TTkD0qEs6zbC8uxflkpI6IaxJOO2lT8KKTmCA3lQj08NbZAdPQr1H8h9Z66UO7PlHhh86DvrdFebuHAJl6tQ2GRqm56h-6yt5XtGC2Aar9Bpah3ThE8sgvmXMxuIvpmG4WgZgXGGLmUJaImhdNKfMsugZHRcrGdCKFyLtnQLDE3OIeI3Nx_Y0RKPZTl7iUzFSIbEZI7VgxEccmkZL_AnRdbnsHg6CbTe2chNQihgr5lTXVKAA9z526uwPIfzrBfzPkYp15erfwCNGucJ5MNuLm2-O6lUcBCtJZK3kFwhrEIx0HWxol3rQS2UBbo4kb-z4mzOmlx0_cp5itxwL8vX2WqdqYMn8Ps-edZdILZst89lCdm1U62rxYHcHPbbp795lqG_IGOTqy3Hg0Bag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVo_I4Q7C1kSZouPYkK8y4uelycB5aBSHBTj6jmNQ4mKnBzvbOeYIRI7BVQCPwCMOEDIngp-R2mZAaTPm2bWYLyGRFEttcjzZ5Z9QzGkx3hbHrcJrCXHaP6Kz5spMm0VZww8XU9BZUsyYxYkVx81RSzZfeRWlgeMY0AFLlEEJmcCwevMDDmVe_DWVPdl3QNJIsbNCQGVnZhg8_T_12615tM9HBCt3rf5DubLyXWXn2GIMPLLe53wMOMPMd2K6XVVYWaDDggb4D-GcyKfhEt1nW3htIsYAlG0rzG0g7IYI4k6TJ3UtMBXfLxGdVRS2OzCufDdiRZP15WHfr1072t7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=pqpf1SxT2P3Pu86iZI0xqcK67aCGTRbcRl8L4wPnYwqi9ZNSf6tpAQu_v4wcwV9Js6J6XvTbyiHu2RTKYoaHQI6fv9epn18ycXw_3STHF5XDDv-i-gnbgdLwwNT8h5KATWcKBKs9iuWnictNA5Uq_sbX2hbqi16fB4ocs99FvziXYf_k6M16Yz9WnaOzPneeI5sU3l1Cr7UPSUJCq27G13W9p2LPtkTroeXvTE8Rpci8HFgDg5RQ8FOjFgoHCKNDXeD9bui-8QzqU8eRSTQYOtBwtGMpTwrv7dQ7vvQgsGM2CAY0I4GlGATG8fWnLTfJ6vTrmsoeh5GqFaFY9S1xaCXwVcGD9UE8mKY43j7cTxgjSG8-vVOn9hqE3ond9aozLYbTaKNYQlhmr_lcJmgSEIruqErfHb6VkCyCLpjpnUUQXnhcOysSTZERjJ97kEE3u0w2_-7c2L3pvmLDtO7LR8oplGjAXAQQID-WGi8AFCvoMn1f9ToS9l7tdnN8oNYPmaAkhY2GdK67HW0SuIKs_LPLm0iORMiHuVo_TDqkCK5C5h54Aw9e10LGaZcKWtSuECyyp_d8ZXtFeiVsEKCTq_TCzo_MfDlqag4cmwfCfaUsq9DavXN0MgHjUid0X5DOrkM_mIQUW8SVegBykCPAveWLFSwaDqxmfZOM7FILiwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=pqpf1SxT2P3Pu86iZI0xqcK67aCGTRbcRl8L4wPnYwqi9ZNSf6tpAQu_v4wcwV9Js6J6XvTbyiHu2RTKYoaHQI6fv9epn18ycXw_3STHF5XDDv-i-gnbgdLwwNT8h5KATWcKBKs9iuWnictNA5Uq_sbX2hbqi16fB4ocs99FvziXYf_k6M16Yz9WnaOzPneeI5sU3l1Cr7UPSUJCq27G13W9p2LPtkTroeXvTE8Rpci8HFgDg5RQ8FOjFgoHCKNDXeD9bui-8QzqU8eRSTQYOtBwtGMpTwrv7dQ7vvQgsGM2CAY0I4GlGATG8fWnLTfJ6vTrmsoeh5GqFaFY9S1xaCXwVcGD9UE8mKY43j7cTxgjSG8-vVOn9hqE3ond9aozLYbTaKNYQlhmr_lcJmgSEIruqErfHb6VkCyCLpjpnUUQXnhcOysSTZERjJ97kEE3u0w2_-7c2L3pvmLDtO7LR8oplGjAXAQQID-WGi8AFCvoMn1f9ToS9l7tdnN8oNYPmaAkhY2GdK67HW0SuIKs_LPLm0iORMiHuVo_TDqkCK5C5h54Aw9e10LGaZcKWtSuECyyp_d8ZXtFeiVsEKCTq_TCzo_MfDlqag4cmwfCfaUsq9DavXN0MgHjUid0X5DOrkM_mIQUW8SVegBykCPAveWLFSwaDqxmfZOM7FILiwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQXWlBYLMuFALGwVhTEIcvLRko5R79ExRihYFIt8mHLJNnqhguNXfR_s3903MWjiC4zrXI_F1Q0VSDjkm4trj7dbUFBIvAr-CfW9nqs4LjCsR6KllL-YfAtro5Pv717b7OYHL1XNjHqps6nDu306wszb6JFvPOgtrB2mqQDJl9RRg3uvs5DQkc0zpfHwos6qSj3-dm-FtLhkoC3jVE5VDwwmIpJP4Jq_3rFMdbTJjhZxd_fm4HNCfs51EefTbcxvNkNdy8AKQmZGkVgbZKh7jmQZife4bYMrVnW8iuLzAyQUY8dHp2rh0xjXsEbTcsNYfKVGnwPOGYzaDv7GIdSuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=s6n6i_EIneJqwFoS9NpYKSEZiRqrXQsMc6Su4uD0FE7307eyxaMFjjh94kPfAW2UxVFruX70abT8-ZxZbDI_9uYH3zgMDzlhrUvYfJ3gBZnh6E8-EFwkbCo2yPEFtjP90ZQB2i3LyTH4jEg8GraZgql20vMj7jaNKMU8gs4B5VXvGSBsNU7e02P7CRmREW2CDAi9gckiLKd1yDu-EzxjQ6R_3V5sb2LLJsRKhxWMnIxF41Eu3aohz4n9tlUgjfANNn80HdoyJPKdoRX4Ad6jqIf8NlkYt0LT-ITcYFs1aNxrsG7wC580b5zTtOyqjBTavZEsQW3c3-7me-UATXIW7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=s6n6i_EIneJqwFoS9NpYKSEZiRqrXQsMc6Su4uD0FE7307eyxaMFjjh94kPfAW2UxVFruX70abT8-ZxZbDI_9uYH3zgMDzlhrUvYfJ3gBZnh6E8-EFwkbCo2yPEFtjP90ZQB2i3LyTH4jEg8GraZgql20vMj7jaNKMU8gs4B5VXvGSBsNU7e02P7CRmREW2CDAi9gckiLKd1yDu-EzxjQ6R_3V5sb2LLJsRKhxWMnIxF41Eu3aohz4n9tlUgjfANNn80HdoyJPKdoRX4Ad6jqIf8NlkYt0LT-ITcYFs1aNxrsG7wC580b5zTtOyqjBTavZEsQW3c3-7me-UATXIW7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFy3ECTgb_keb6l9dAcVZvRkxuUo79aIcoor7OFJ47w0IWC5_qCPbxwOTfpGJWZzvWhcHp96Wmol3_QdKXGj6UF1rs-plpOQ3TlIvUCZ9hWnymOjGKW726aEf4_lpiY27DavkmAJEDLIkn8eB6M-6aSMOujUNXdqjWnT6wbZdDiSAfIUYSMP4BuYfXR8UF3vGyj3cA3vfLL5Ims5IMBe7H0gsn08cY3bEmRz0Rl3w03KNsc7gQU2m837S4AAxfBK4AwKdk2Umcm4gKfBdSIqErz5M3qVdHOfesQ0_OZeWt8Xaih-sa97CUe7rZLUZ1r6085jExpBnCXwbAjyp7_kAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOmcm3XA5_2fBQNHe-fxrRm8QjI1CL8T5gLf5o-4cSYpTPQaAGMW92G8cGjFqclIRS_2wEr25_VZnQLxoB5a3k-be_c_5cYumOJNzkxgmq9c53XwNhmI2wm7pA9Q-X2dkMEMwUha-_8xy_iQPfPY7D7E9maFAma6Q8tVKwjOPVq8wV1ucE3L5j5llSo_UC-4xi133AFXGmXM0esKv248GQNwE9O64NGA26PQ8fra3pfEY4tCs6_vZJ5tXTCEv_JYR8vjJzkb-vNhccCM9heGQ8k6WtzronjV8JZ_IM2yqidBbyMJUp6ABZjY6cMDCut7IauEf6omDaLwn0ied8oC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4g2dit3mJ6FEygsM25p28iODmQOe0EMNfKE0XwcfAKyjYBfd1xC6r8FwkNyBEF_aRF54F6gyXp63Kl8mgvcyxGBdz93tQs8MzBAUxHXXUSXM_LJU-YpRzKu8bVsPgkRfymG--MF1xevK5KO_7vZ6HzTGqYPEicj0z2t74NWabnZ04WcFztDqZOWL9Z94dR74OpqD1FRob-IbwolXyIn19GzuS3JekLNKVhrRgWjAOAlXwYFG0B48MsZX9QIhQzUeJW2dwaJkXkBw1uvfeoDk9wAkxjsEdo5YIO_A-58UluW0lA0xPaFYNmxtaXwabd7yO0v3O86LagSfP-sDrvK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpqSenLkwujeCS3C6NnIhmWhMcWYmBcFwouZMzy49ntVdDwVsAXOZmH85spCwEvbnHdmSXduslOj6ppETCbQPPHAwVvln9vDKtEXl0mSIGA8El0YgrqO1Z17ajczMlXYXsAJ57oVKntbVSoUad8NWbJlkleEB2F6JBSWD21c6S8kKs63VQsGoYZiZYlUcsd2EKd88TSgXT9ZBm1RdB1aj_3iiRDfMiEck6l4R198WY6Dh8vwHOX4cAOon0x6315CfA2fewQlpYZZoVJdPO8XQWuq9Dg1rBmSRbd7irgs3bA57A5wdphjqtmgwIee-SaNkb7TGuQbT8WxOKYhDQxK5jtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpqSenLkwujeCS3C6NnIhmWhMcWYmBcFwouZMzy49ntVdDwVsAXOZmH85spCwEvbnHdmSXduslOj6ppETCbQPPHAwVvln9vDKtEXl0mSIGA8El0YgrqO1Z17ajczMlXYXsAJ57oVKntbVSoUad8NWbJlkleEB2F6JBSWD21c6S8kKs63VQsGoYZiZYlUcsd2EKd88TSgXT9ZBm1RdB1aj_3iiRDfMiEck6l4R198WY6Dh8vwHOX4cAOon0x6315CfA2fewQlpYZZoVJdPO8XQWuq9Dg1rBmSRbd7irgs3bA57A5wdphjqtmgwIee-SaNkb7TGuQbT8WxOKYhDQxK5jtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpKLEkELEiXf40PEtmmKdgXScWrwWp4WYc4jd_98BNsGmQTv819FZ6Et4Ud5Ug6Eu011j8TnfmLMFtat_wAZemYhdZeV0mbm9YVxY01L660ixUtngAmMOEVRldMybwOniSGoLBHJQWdAYiC76BxTK6ZICRURgW1jRrH8PCrzQWX8jyZVejIaPhj_wr40afeKKVz0N3egpX10Y4FQMCJpyxNmm4-VEP-nOAnG5RobtPXVmy5vAxP5miXdBVrDJorjbsh43525c4BBBQBVr-PS2xLOZ1QPS7O1H-F2d00B-Q85DnDv-lJSb7-Wwk9i6VzOIk3DUjmBpqGK6P7Ek-acwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_6FJEZaeA0bTuOUctqQp-jf_JdTpZxkImzZ7BCq4cHNmr3KwwB8EK21bhEINqnDulWVs7ghFLwqtfKkXDRrjU-C7R5eRe8CfOIeXTQJqdHQ5Gi_sAM2pfDFoyFExyOHA8YU5Meqjcl3njbjCR17s3juSseQvR8ULUpzhAFDdhw7clCxtsFQZzdNCyrBWz17YEjwS2oiDHAf_dIS0ENhuV6DyreXQU76mfu2D4D9jVfWDghhPtOjO9TonrEWIusS3vq1lisFayVh3I9U2Ae0rzVeH5giTsM1C0R_FOjzsXSlcMlF0bNjTKWjfkRUtPTKUa7llmSR48cpWUMs_SJkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXvLycWC9WzetbgExxY12YzBjTaaVxxJAtSfbwcqCDZsp67o4i_HxeaitVI9xaQeW0OH1PbrilBmSe_vcsqjDZkF13krBNZ8EPku_CvuH6vqhxLxosKVs77RCzo_qY6TglCj8rU7ox48nDsV2abod3TXZF7kZNmC5cLrAC62XCTY2QqhaXDLRERpu3vbLom-hgEuV6HmBUhzJ0C_XHTvUn-t5vkPYpJOkKHn8oLO6QAMse44GB6fQOmsmRDhWStgHyi-ed9Mn5xsv6wgRhiTrVfIzkM8GDQnfn-HDLR78YnXhWoKLaLrzJY_fylOHPJiyUnbILGnWwza741VKnNsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5KNlttwuPHHqX29UiE8PaPj4LcsJC6it8q9MnmZKldLjCRnwOPOBO4cVixpZXkj2ktLeoUX1LwRUpr8HjgmqKQbXcagK7GmohRczpjG5ved6h7zsHelBFUD-4h0hhb7GTU59UHPgysCDmqxipe-jjExiqBV93tS6j0k-LALeUDUnI97dSEtDP3OZPOT14fY5LuF0AA8K43HM5J-KEEiYhzS7vmEZWhR9H8mlRmEFPmUjBFf6UGvFhfxquLUjkOhe_fuojkV7j5U-ssfBzS9GZfQ0U2R7Mma7atT8LAuzdakj99PuTHRA3W--472bqJAOawdgv-sDGKm1MkXr7WVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s46VCQrGJDpSryh1C0E-u3ltSKDUQ8G8Q3aemmVXpFwREq3ZX_-hlZfxkVc8CXZV8ATekr4ReCoOV8JQ1Yrzz_2YF5aWWtW1oX6veT9lxrztnyjsFeppm_BoWgf7jRN9baVyf2wzYkfo63DQ5O-7kjUyW5WpT6XaydcqwI7k256h4qDBDw9pBZHIq--o-jCkD3x3mLOGu8YP6zpqC_KZPqTHKlWhBsb-2F1WdTetcxi_YkUfYs69JNC2Ime6YJR__igk0lUe9tq9qGIMpMJoy0pB30uQPjDMJbeKJd_MR3HQkM2w7wc2_RvUJxuf9Owqi3KBnb-YsUAy_8hvL-7aGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=rekm7Gq4XxglEQBo6iUFwqqAa7ANqeStRtZgFPo2c42Pyt63ZzpXswtEu4QG7wtIlNlOfhx7akAtZTwL1_pmFbd6z_ZuEKd7bUjY5EY3h73-R_IxCjlHUCeezHgenRK4A2ShM8s9VbKzldEXiBNot7EP2f7MyvQz83w4ZewjxquzNIDlo04ygYGHM1oSUdNxI0-mgT958yJz0Gbc9WIDcIFpRxxCLYU0Q727WBQoz846klY0FYUdc8q-2UQWa7FcUatGrNrWudJPPIC4NKM--VFSuD4VBHYiCdETTeSn64lCVvTF1dNgcoremGrgVr3NqhAnqtwX4l72YZuFV7GQ2JmTmLAbPP4MCqKmDco6U5eqa-i-75-dTabGyH5FRaueUYCG5vLajQy435u_AnBABDLlITPqaH-ZCp8w9o9-MK_dwFMa5emMyLTa2-YDHSSBmQ3jFJIHcSSacpf9xWve83i71WRiRIQl7k17DG_RQJP17GNpdrRF1Lj8PLpUVmMGpFCE0VLW161ad17YiaJ0KXfyD7JhSlkSMmQOgJZ8D3eRkSHg7mLrmxhiD8AXFEZ6XalqImVAerk4bkzZHz2HHO2f8FmKCTLHe1UgbKth7Pe-46SwRTIJpFiLng4MRvjSQ2tpPMSifPpwRZQcxQ9S6GeTm1WZy-m9bci8PMoxcyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=rekm7Gq4XxglEQBo6iUFwqqAa7ANqeStRtZgFPo2c42Pyt63ZzpXswtEu4QG7wtIlNlOfhx7akAtZTwL1_pmFbd6z_ZuEKd7bUjY5EY3h73-R_IxCjlHUCeezHgenRK4A2ShM8s9VbKzldEXiBNot7EP2f7MyvQz83w4ZewjxquzNIDlo04ygYGHM1oSUdNxI0-mgT958yJz0Gbc9WIDcIFpRxxCLYU0Q727WBQoz846klY0FYUdc8q-2UQWa7FcUatGrNrWudJPPIC4NKM--VFSuD4VBHYiCdETTeSn64lCVvTF1dNgcoremGrgVr3NqhAnqtwX4l72YZuFV7GQ2JmTmLAbPP4MCqKmDco6U5eqa-i-75-dTabGyH5FRaueUYCG5vLajQy435u_AnBABDLlITPqaH-ZCp8w9o9-MK_dwFMa5emMyLTa2-YDHSSBmQ3jFJIHcSSacpf9xWve83i71WRiRIQl7k17DG_RQJP17GNpdrRF1Lj8PLpUVmMGpFCE0VLW161ad17YiaJ0KXfyD7JhSlkSMmQOgJZ8D3eRkSHg7mLrmxhiD8AXFEZ6XalqImVAerk4bkzZHz2HHO2f8FmKCTLHe1UgbKth7Pe-46SwRTIJpFiLng4MRvjSQ2tpPMSifPpwRZQcxQ9S6GeTm1WZy-m9bci8PMoxcyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

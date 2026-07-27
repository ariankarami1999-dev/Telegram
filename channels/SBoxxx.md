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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6eT2TRdRog1O09sbpIQsD6zDFiY5F1CjVEOC_XC_5CNFj5mZASKkT3RkwrkCH_feBaShnkGlE1X38DQjIUFZE4MEnYmiCEmn79G6ndMTNh9P5Da9qdYllQTHZQdvs7UNWqC6zM4CyFb8lJk-3BbtbUsugTBtSOyoJu6gSEXCYVtPBfE3A7jkNMr3Urtr1nVZkvoebXULBRgdkbe2v2HRIxlUaOsXeCxsCV6Pd2PsRjcqSKRUPi7t1S9BBnOeaaqBU5x5DLdTNNYH3gKUbN6mPeZuIY5_wzglKbXYfydOq7y7BKT8aLWkfvxngrMWjlzZwJWKNi52Px_zdCDvyS1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 368 · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLSitPygeGoxr_AuXNpCCVIK6MhjTZPiwDLbskpcivLZ0Opr8OW2O_D0_FJsSJ7pN39OS7-_8o9UtnVxoB8-7K-2FX6viJ3L8qwMdZabIS7g-t81tqxHE_-l0hhDTswYSOj-xDZ7k2yzxrwkSAA-w7G-YYtw2ZZqCGPUQGFFrKBGQoU9CRRSbHD6jOJyULUNoIUdu0mZ-qH_zKc2euPJSi0G3LdAwQU3iZsmAQ_KmnIDHFzJ1nzE7TQKNd0F9HUEbfEUlcVsPAmmUCnnG0yImhd9-zAKextann9Ho1UA2FcHmAdXiVLsyZH8Qd6KXET9wf0S1Ul_KegBthkFhO6lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R82mskY8wJdk60za3piXD4Mi834o7zIzaq14QtK7F-gufUJJuBfe8suaBnlNNzJzsLxMtBd-LwU929z11mjUfimjuadKa9haWIA2XXWxO_ZIKVm44m-JGWdUKrmOHTI9NmZ_Hpf-4My92_Fr-DigjK7beeGrSKsWUSeff0cEkOVi_7-FOLI5zo_ftqsBSKHTvNCY_AkY4EZQP_apmVTmZEohuQHPxEaJEVeEMLpyvPvf0FdMJ2hy5ttonwaGYqPh5c-TTRiiI1s7Z21WTwz1iCetg3CdnFFYz9H-b0W-3ji_0tIgMgdMnCVueSv6eyH9kf38rSff6ThhqFCEVKN0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZTnbhEcGP_cSO0MuMRV-dkU4PipBNgxob72o4ckIk7byftOrfXPUhUE0uSacDms9A-MZqseDG_-WHuu5CKHz4JSMIusvbuIXT9ZvVhiC_-tqwzvzanlapuZJVABFzYtzGkjurxIgJoPvmojOtYlMmFXzDEB_uDDWP9ENb4Gisk7nhAXKSqSj3CJxa58uKYGzd4dWt6XeExWD20dM_DojM1KoWrxypCG5Kqs6FOQ3JmmyOIlXWMXtzPRCWIPFtBNG4HfJE1c8VWocDRmkq1ef_PWIlJHYfgwGvRZ_jaGnuRbyXK3Tblh4Hf3iaz4zB1TLsD4uX3GGLCoejiQm-6nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYc027kXIrcqluaXzSW9CGj96kGj3VV2S0pRjwEXSNYA7ToZo7cOdqYvvr6uBTPakrhOljqEWKbgVhrirR-pWX5GLqpibPTGE12zO7sUO8CvqS3TwHZFEk2fjw96mA4BNPHfxT3-eQNNd6o6K9exhrPJhAU8miZmBo1FYVmlMu3yBiYRRnsF2XbYOgC3Ix9FAA9CZyg0jmbrPSPfr2yUlgdZLZX_y3pm1v2swc4xrfpWEsb1USw4h3RJVUKIqFppOycE47tgv0J6Zsj7G3aHj0JmiwJpN9XwLGM4UBpWAyV5qtI57MQxHf1rVeZAu0OHRy8Ygg2hxs1tr5siypbfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxXv_Vae39O-AanssltLwXZlNHkHAzTMCjnpWsAxEZpamPH0R_jzq-okrDSL33POkg5dp59VibwfMcs0VH0HaAdxjBt--c9nrMRiO_2EDs4WwoIdm36AXGuqgcQ2IVFf4sbihUw3Lo60vB_BegNXhxF1Rpj-Oyg5lx-A8--GYuJO_Z4ObF_4tuqgLnZcz4ieS_RL1qSN3f6a8H0T_lcggysIYFdcAkvj0UoVbZ4r44AuPlKrbCchDTalKkJTV545x10A0KmBT16zRzS7yG11XQ7tAB13vHsXx_SfTsItteFn-RBq8REIcXFibRuvyzXYvJsADMm8CEBma57SO2N9Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtXDVKpAXl0jyLqjsgM8d3p1KzyKV1byuAEExVIKCUWMXxt6iUJQ6HsSA8s747UT4RYX2rA9hSHZawD6qZzdqGkRbErJJLJAWpO5M0d1yIDqIzA27kKYt-fPtmYpa6SiGnhhK3hZAqmU2LHWznmhtxwtl0QePtDuHpp3O_5JQ6CSQiVa6CmeCzHtARQt8hCzhdfa5WDKhDATumZx6UTSD37DbhR3zDlXrRmcPnhWjpmxrgdu0TMaH89gM-7Vswnsob6C8ZM51sRLldg1uBZ2bgQKKzl9EoWe6VDzNTtSygokh_oAoFfeSfcpDbSp2MqQx9vRILq0oal4X6smd8atkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKBz7F2tCPr1Wex7ojg4mSKV0vgeoeBU22rnMtPC3gbLS709rjlkC3aAFu-MyxYVMfj54f3ssmGVDggrhnYNcqX2STEs2sOOfePLgHJl_2x410kErECHguTykhj5JFMVJjeb05HpXc-YvL7T-1GuOUnPLmEE18HoydzXYko6Tt54uPB1L0gOSnNrmRP_8MNJFsw2_vhiS8l2RtyAcevJ5IVG0Ziuv61RvRZJAtFwct0yEt8_uQ7AUAAIf4sm0KNh5-F9fMN3ULZhoPhvScpT64aHHUgp7cO3PiHA6b8y5ciCU5P2V_rgPn_bVQvLgmd-WmMrxUmGcrps1ijOxehnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVSKelBgcbYb_MbVa5VpzanHUm8H9gHiwyDmntVW6Jbt77RdgxhGsdqIiMTXYJrH6Y57ZwWVSGojr7UXKBR8wgdQi4699ZLmCzWP3jIuOK3gTkBODH6Sg_H9dx-Pt9jNBLlx90YEE8mD2fO9DGXqhSiUhPE9SMQoPkslr8k2fseNcSMF3hCe02bW3epSwhRNw_a6p2g-IJBOm5BbtCVPDbKR6Dz-HuLrEVcSsmiXSgcx20PevoqZjYpMBp1trx9sn6aFja0hBu0N1eowCcVx1lvfSCWIdg4TM8OhrypiQWefT2JUuOTDj-__0PoXPhawz8pnYOA_2acU9q_pDv_x_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1Unp4DXNaP-zWlZcIdLFUp_pC-Z8a88iEMSo9vSloN3y7O7Rj5_S7ACvLfTNgHKQS363uDfGSPMOBC3K8iVpGg7eSju2x3hysJNVVh0MebikjBwFKSCZYIG7CpYo1G6ZgCqCxLPQ9kNRgwmlfeb-FM5Ng1Ijd3XKtzG5yheYfNLxlCyonLk0ox8VAkgjm2p7yXErWE4rKrEqaW6CwDlZ7_8zkveQ4tQjYwdunva6cR9qKiFsrvv_J9MT6lQI7OyJeZuKIMLPdJKCpIbzgnskAYSnKXf7JLkBEDlH_RKhhuDv4Le8oJhZjWQ010kkUgzRQPAFvI0IaxLmu2wGOTNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSwlLq97DNlLh1_oLuQR-IX4v7v5Ds-fa-A-ldIYVZPyQ0OXNta15CVxaQYE3ABVIRF971AbRmxX1O8QJSHqAQ6Eu4PRfVoVlsBi2I2ci9A3nnkq7OPWaxAuF87nqaX44mk6p_rtbnA6OfK4ZUuYRwcJzuS0CW20iZhj_gmTtqAZmuVr4tAdsWIvdoQPmuK4EDQS-pEVbe3qboxvQg92W6tzqFiLd2HjRHXm6x04-Y_a8mUt_kX-CYYVCgzOdIgnA9GIOcxnAlfeBXK0LknvawvjtIRsQSmSJk0hQ4vUTICQynkqgPgiaTn3quYraTbADyXZnhONK7Ktbg3kwdeKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPg7LDT0jFeLzpopx6_DQMUEyLX5HxC1fMMX3BAwL67aFUkiR_uEjgWP4rles5WbMduSkIFslX8fecrdwOKBhul6CNbHNlweVVgTABwssI55JdAjG1YGxpkwXtspgCMn63Z-r5tVwF8WuZDI8pvY18jO_EsoMC2AE7EUHLG0W0MmvOdwl9xJsa7XrRg82qUeeARF6UGrBNYDFsg3yK-O-O7fMgtzp3T1ZNzV9JM0SN8B5oeav8E3CGoFBOYdWDt_j1ylofH7VbbXywaVq_8tTuDgrunrjyDtf2MEra1YBoNJRaWf81xM7goGVssGUPYWIpRtO_z3PVzEF8osuswYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtaE8tMoy2OD-w0PM_zdY5oIiyl-9TIwzoGAbZMOZ26QMIEHXov97LE6K5WgmaKP93E3ZAu1qoYqCPHiG4II9wP0LpLOUsSqywU_i2JQE6Q37-8MUNtaxm1epoa6xauInQ4NXNQ2Q4mYBudihYhA3rsdvvxmfnEAnXD1nwxrOQsMIdDPjn3HUcPZHHk5mbxZut8VLuaqB3wKwaeVkYkKBpYuMI9ksI5qZEE9UKHsumfyaGdZ35nUROMPxmAVs2h7DumMCKjIenoB8bP4SP8CsFUKh8EjNfjkto6L4f5rmsPIcH9pQLJa8W4nBBSNAhWcrkSZle-w18t11F-QWNyFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-k1K-t1D4wJx5qJ5uIyv8awkwSa4ZlF5wvbApQk2wXpKr5BsSyP7VNH7rJhmQQHMZ81p8B4rjFtyBLGGiCQARmfmNl8kbIjvmHygqWmYP1h7-ykFsvch76Mytl530fGsmoihkRKM-oyQ8lBBpngGaMRXkuzKtYRdgTpvxOZEFX457aOaIFp-SlWMWifvCklU6FYXSqZzSIVP3chSJXTRuP64IMy-oeOXBEoxWDh3yqknrIEDWslm8eZnAsMTXcFuA2mRH1qPcvmBgunbmUD9jNLWQDeUGlLIsIq5aPaefF4tzTCOfD8Qq2l1t5kLZyq1EIeOrgnT6YhhZYxHi9oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHABZz0chAIBgi2PumEFE54hOdYFFZqhRLbC0Cg0mcpKDnmh_05MewaK4pudWztnUporL4VK5hT8DFgXhfnIxwudpLIzdWfQkrYYU2qn5aRJLBIY5Hf_ftv19QiVwtoHbZAAe0w0rMODauOlpTU3KjgZrzNRn9Adlh5r0hHb9Rk5wxxBD4d2Gl4HZ1kLXvWj33sPebYFArGRliBPWCXn4uhE5CeZd066TisFeOI17Yl8kURWOGTAx7q_pWbcRV_pNosjGK5iG7WZDcoZzPD7oUgZNZpx1SeTK0XSAJ9nP0rD6HcTu2zZUz1URI5KZY-R_Sa_pSdv75Avb7Re6ZWJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaBaexwtvvwnB9krfglaw1vnfPw3dJCcRY2_pnntNm9LcnihmJRp8X4LoMPmPYO7Emyvbxv3aHaYp5UqTM5NFWO5jnRhZN5yrPti8o5rA5M_9JjiiH7UVuVMUtOLGJzPtSdtavryaP0UaS0WWLuY50Y5JPmv8rAXBDyDOXbf64N5OA7qtyEIPuZ-FAqmRy4KpsVWuGnaM2cu8f70m0K3ESbNwOsXlNTU2pALStLGqQUjIrjFnqNpCis-a1Mec3Tc-sK10V5PnwpcnPrAyKKY7C9PuyvzRibqdU2lZogyUwaAs2Bcn_FEK6BKMI1ZLRNprw5zdDY2am3oCgsm1InTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULGbyeYAm41adV15r-jULp03qLoFuX9AkukWS0uJ-ablMLUbX5mJk2whmjZaN2YcX7tniaEkJaHhwXAYWACRuzALATbCpgIsFfEiENbH_TmunOmLJlBVUn7zlH39crFbTYudFxyliAkMWR1XrzQPcUAwaASn1AnUWfZ3I1XK4Yl0GKiwiChRFrmYfuba48jQhDw_lW41Ieg_kQ0vQv67zyeJZAxlhpEzdwKp3gi7QsxiKV15de_eJKK_epVl06fdU457qVlEkG1JVgyXH60uF0NrI3JslMoVK9KnpkScaIIWu4XyJZcIAJMAE2wyasYaIBAsaf2VpRNFGHFsNg-sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYB9caMs8idR71U9KyiuRa3IBqH3-vQhuIStxm9SAC5wBc_a0t-BDGBo6LSwg5Qto0O_-z6PPq-MQaHkHWfDeC3ejm5i3lziL4iJKAjXV6p3dzp8Vpkww8kM8uIlVoKL4tYZflSfh7ZcCEMN0jAhSsghYWX2RMSxG6OxRfW1kCBf_IE767_qElCVJzXI6ABOz6TXaD-FM527SUBNuumVbZgjI55dhTwtw2fBvQR236bDtBFvJV3BkRGlm46U5tX9jdZHTDP7HRrx1XV4KSQlBLKHWp9DEiyM1a7jL_iAgJoeAgUy3Tonss2-rUAOtBu0IcgXX_rCjc520ubnikK85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Fn7bzsfxBcBzDoQYsEwdgbnFuqW1FQQqT1uDq8-dM2BZ6R7x15NOVA3UMBJm6vV-KmVrKsdc2sqpwS4Zt-Qd04Crn6MiHGWbgUpJ322kQfKxoJtBKBo-0rDhq6UCvvxwrQVw4FEpXMiUcjnBr9J2NaR9u0afCBZp5RaLhiapDCqDa7oXhqDCKBegT2xY-SRGTkPFhzqzyBSHN575HMHr_qRb0DYHw2jiWEbcs2n2ryCAaX2APAPaT5YMc8_CyF_FMlLrY74Q-eUmyZYL54ppNL7zBn8JRrxR757erfvBvEl4dfQnUOSC0-yPrT3sWaaEpab_TmczpCbeGu0aM3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=qP_YsPtN4FNFUbd6mkg6YvUHOqNVry_H-GM4lx8yUo0J11RjJ8YsqWQwCqFibl8cfc8s21KqkyLINVPyCxNIzMSmntvYy68tDsz4VmupFah5H4FFR9BVpbJF4lXOGSd376fBHh-vX7fbM3rO5G2kMF0VhYu4RQu49zfCEgLPf3Mi9VnMZlwwhEAusEkKDf9NYYUZIWebPGhPtfNRJl0zwfndciOdGyF2VsA4WUW7QfqhYx_FFn5NxVl9EkG4iIgBjZto5MfPfsGYFqLjDUwQI7r4PG2lBTLzB72nkEmH0pGvWJT3DX_tHS59hNaYk17C9unKe2EPc1EsV4fxCIPJc6LZ3HklKMMmWwpYFCjgXL2hl9pyMIp8q3davg-zMQfY4_pDkwe0lbiMX3idV-FdTGCRoAR1NP53VJoMxq3OshuZYXhSxjuEcqTFDz7BaP7xUqzbdH0W0o5iyjsPyPGEAY3ZItdpyWhrAIQaEi07ebN42Nj5dCuQBCkTBa0B-GA8i58nAbuN8JLla34QEyJEJAUogYKhBeRI-UFnCpbdAiE_OZK3P7u0vhZxlUxtBrPqiKWyG63m-0J4aUR8cSr4QVi1dFC050JtymlnUsCvhZNRaunbouedu6Hh9he0Y8UwbeNeAS67SUT_1PkEwH1QOHpV6kRlBCwTKC0WXerqroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=qP_YsPtN4FNFUbd6mkg6YvUHOqNVry_H-GM4lx8yUo0J11RjJ8YsqWQwCqFibl8cfc8s21KqkyLINVPyCxNIzMSmntvYy68tDsz4VmupFah5H4FFR9BVpbJF4lXOGSd376fBHh-vX7fbM3rO5G2kMF0VhYu4RQu49zfCEgLPf3Mi9VnMZlwwhEAusEkKDf9NYYUZIWebPGhPtfNRJl0zwfndciOdGyF2VsA4WUW7QfqhYx_FFn5NxVl9EkG4iIgBjZto5MfPfsGYFqLjDUwQI7r4PG2lBTLzB72nkEmH0pGvWJT3DX_tHS59hNaYk17C9unKe2EPc1EsV4fxCIPJc6LZ3HklKMMmWwpYFCjgXL2hl9pyMIp8q3davg-zMQfY4_pDkwe0lbiMX3idV-FdTGCRoAR1NP53VJoMxq3OshuZYXhSxjuEcqTFDz7BaP7xUqzbdH0W0o5iyjsPyPGEAY3ZItdpyWhrAIQaEi07ebN42Nj5dCuQBCkTBa0B-GA8i58nAbuN8JLla34QEyJEJAUogYKhBeRI-UFnCpbdAiE_OZK3P7u0vhZxlUxtBrPqiKWyG63m-0J4aUR8cSr4QVi1dFC050JtymlnUsCvhZNRaunbouedu6Hh9he0Y8UwbeNeAS67SUT_1PkEwH1QOHpV6kRlBCwTKC0WXerqroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJfaeWbgrlS3ssC8hp9k-WhLFcJ1J5UkCby1MIuqC8pUK05laz1fJLijbFM26N0djDx67TqSEt6Sj-KY_xM-36OFpphxQFjm4t3hwjAYsJbojmKAnmY3X7f7Sruj9KzAes3kyGkE2E1kk5Tdww_Gm9cWffI3IC9J50S3kOrfvg2fprlfeo1A8m_Gjg-PPrgDIcPflT7_pXE0RKVykz_RpDQ--1k3CaanhIm-3Jd0cOQgsHozUUwdWGu0cbYxjchDMfzhjweFvgjnSrenciXTn0LZljE6XnnVSw8oqUrJkRfbdCIEFut7Sat3nglY-Qzv1KvQdErfOiaBTrsohytOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=a0J6kmPtzBqqglo0ahAExV5kA_ldYQMa0DAH6T_RSnBjHUdYTS4EEQIAtwEu1h72gWp2AyPUg3EJF5Qk4f3m88Q20rG4h2z3P51W4Lr-QIQc5nMif_qIKz2P5oGavzEkaolFgGtvE6SaLVOB_QPkkcr5XkhqI3F8AB5dLZc3rh3L0j62QeZS6nNHX3ajTTdI7PxF-neZO2M47bC8pOtorwyeWOmhFjeyrA0VMA3MohM7XQlnmPtbXKNyga5ci8JbpzaYMbfwL_tqB4icZdP8afqfJyHzaDZOlQbUsKjJmtSHk1AAQK6s0hi7Xg2I8mWGEq-ryjvd9_yGa26gaQT5OFVvchu1D73kx6r2JAl9hCi-ZTkWdM6rFY7RCrk2KG0Cgshow77JIEpF3nDC_NvXQhkuuON6SZjtBAx53uQB2OetozpWrSybWPMntW4Wg_1eqe4AdeChobJ1EijP8D4NuRF3b0Vsob1MwBwYxYVjjWaAuBGfAS6Af7X01UmJKiPw05yYOwQthUdtTR2IZ7J8N71r6GNVY7dwDuAeqnHnRMSnkFSui2cdebnpKVKwTr0gudQGqib5lx0BWO-hv_lbZhzvS3IhH9n-vcyQIfhvVmLggIl86ft2-IhSBuafF5_2M3LI3lt0q5913Dn7jRF8ZcZoPSZsoL2gBwxjefM-5ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=a0J6kmPtzBqqglo0ahAExV5kA_ldYQMa0DAH6T_RSnBjHUdYTS4EEQIAtwEu1h72gWp2AyPUg3EJF5Qk4f3m88Q20rG4h2z3P51W4Lr-QIQc5nMif_qIKz2P5oGavzEkaolFgGtvE6SaLVOB_QPkkcr5XkhqI3F8AB5dLZc3rh3L0j62QeZS6nNHX3ajTTdI7PxF-neZO2M47bC8pOtorwyeWOmhFjeyrA0VMA3MohM7XQlnmPtbXKNyga5ci8JbpzaYMbfwL_tqB4icZdP8afqfJyHzaDZOlQbUsKjJmtSHk1AAQK6s0hi7Xg2I8mWGEq-ryjvd9_yGa26gaQT5OFVvchu1D73kx6r2JAl9hCi-ZTkWdM6rFY7RCrk2KG0Cgshow77JIEpF3nDC_NvXQhkuuON6SZjtBAx53uQB2OetozpWrSybWPMntW4Wg_1eqe4AdeChobJ1EijP8D4NuRF3b0Vsob1MwBwYxYVjjWaAuBGfAS6Af7X01UmJKiPw05yYOwQthUdtTR2IZ7J8N71r6GNVY7dwDuAeqnHnRMSnkFSui2cdebnpKVKwTr0gudQGqib5lx0BWO-hv_lbZhzvS3IhH9n-vcyQIfhvVmLggIl86ft2-IhSBuafF5_2M3LI3lt0q5913Dn7jRF8ZcZoPSZsoL2gBwxjefM-5ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiNVzad7vhaB3Ga40-jFVda7aT7yCX-0EcRY1X6gm1KNfTeXahdXsyTjpe9vUuD8FOw3gVf71sN4zG51FqKf8B1tLKRDCi5oCsJTDsAXQZgJuGynadHXlOcL_mLbhPKjrAOj9a4eMXQ24XvwfAlMRr541d-l9DHRP4-YRbjwt0Qw5Xo78NVPLcuiq8VSwC8f2_7xFT3vTpPpch2U7uty4iz1lTbBvZkiaCQ_7zE1OLUBiy14D_A0SGXNhsOgJKRDJsl_TjAGTtz6meN63wJXpXhlo0vfGR4PUu9L4zzFSH0ZZ4M9gugVjYvUUes9s9DbKuS4YvU61O3IpiZHKQF1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=qSxSwx7BqS31iWgXkZUcM67GrmWiMSQPXLHLx5Zp2x0Qci8-VsdkYeoOB6mGpQZKDlBuM7HzJJdGWPl6ZiqQ4cPbDNlcHc8G8wP5yXXYAJZCu4ASX4OTg6I7pORG-wo5ss416z06q0dKC6_UDwV6oua2yWn9wTXODr4JFcgb8Wos2qSO9-ukKeWnzggIIHaY0ugh02B5aYKmAbqNGMTlBDsv7qcH2vEbYJ_3ZDYclaijuWJKswuhrA9P2eDsq2xEYCokp7q5zoMIGQ2FEBzSx5n4c70Us0u-03RqR3AC5Qff0AniMopIi7ac0PI4Kh1UEfZtUuelAUWbwUP-lht5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=qSxSwx7BqS31iWgXkZUcM67GrmWiMSQPXLHLx5Zp2x0Qci8-VsdkYeoOB6mGpQZKDlBuM7HzJJdGWPl6ZiqQ4cPbDNlcHc8G8wP5yXXYAJZCu4ASX4OTg6I7pORG-wo5ss416z06q0dKC6_UDwV6oua2yWn9wTXODr4JFcgb8Wos2qSO9-ukKeWnzggIIHaY0ugh02B5aYKmAbqNGMTlBDsv7qcH2vEbYJ_3ZDYclaijuWJKswuhrA9P2eDsq2xEYCokp7q5zoMIGQ2FEBzSx5n4c70Us0u-03RqR3AC5Qff0AniMopIi7ac0PI4Kh1UEfZtUuelAUWbwUP-lht5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXOZVlnn9z9zlMGaBFhRPfrWWHTyBNgzJoC0T9mv5a9tLSA-2jiYs8jf_VSpTEzQwEhl2jqO-60r0-rJTzmyfyZpGCDydjL1G498TK74soPBbWiUvU5RhewTeG6bqDYBOZPhOLj0ezFcAzvno4gPv5SFPGeyMpJWaiuJo1BdwwRNcpl1hvenYUANs04Hzoq3gH3XCEqerryDzBVjHumenaNcZn2LNHrYcsCNnwt4hoURAHpTQ3n6piGnkyUo6Td2z9wx9YQMYLvnO3iAsGC3HbhIZ0Aj0SvFsuL_3OmzitDVXt0BVIPlDl1q4aDL8NbxyT2pUDR1GeoTYluGryQxoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_gBdMYZOKoxc5r_AapIQSmhYX-vJtbHT6y-_dy-0iAr56zW7EDiFLYcvo7ZxFawEAjtRvT41nOnABexadcOpTMO38dHECf0vpeGCj_iHkarVtj4OIHaJSO1wt9lgpxqZKq5zOZlmZpj_QxVg6AcOwsXCn3vZggKulzmwj7UYBpajQgy6nnmzeqq9up-k40ee54d_sq18LvWss5DkHDkUMsek0JcXwT2lelLNWGz1RkxBQOmkeYPR_Es8Hd9-kFVlA4nJ3jP47U0g7-vHuUgX1uYdYQ5I6GAqjrwk2KQhS-dS7l7rC75mXEDLWu7E4yKhcl6f5yHKOk3kHhL0Raijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBzcHAkv7l_mbmy3iXHeg6-2CCXJAKPQYRufKGA459Wzo8oouH3mFaL5geL7Lf9xK1U6FfRcE0Hi4lzuTXhxYmaPbajrZDkKGpZ8n8g4laK7Z1uvSkUsxWYrBWVUHXbG-64DskdAfCYpMvZhInDbWek_gla3UBa79358UZPkE-MDCELSfPyJy9SgwfIfJOVMNdSNefYcq76RkTPId19ydB4No1Pv2iwzgqWKcGZ4uRVSMMeA2aRFE3yuUntB4eAI8kDqc1oJC-a_Y-lOAWjOjhVrFDy7EeH3SsKihZkjyvGNCqFskpiv3tuCrJbocGgWTrD1bMDk1x7SafcMrHLruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54Gprjl7MQAsHL8U1k8fx6Zph1QH9onhht9EUbnp0WZ9e0-RU8m1tEZP0U1_eZ0LX5fwnZ39FRiP2R25OT15USWaIehelU3q5hZ1lFUcO4vePG-E4UO-eiYqYqOssix0oJYvJ-JXnMGGFDO5XSHvfrEyPyQUkBJoHu1qk0zX1Ll2QTrPJv6A7MuVpKYY1mXqS5eh4xxVkBhln1fqpXR57Mhd5BBV9h-PiSI2pfh6YgpiACTcklWiUFSF79BD_JxqGzJlSwXNxZeizZr8yWnLvIUXA4Df2jo8EQdvAYCf9Zsr1vQP5qsUcJ_yKx-udqgxoQKSThRF58NLS9AHl88FJ_VeCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54Gprjl7MQAsHL8U1k8fx6Zph1QH9onhht9EUbnp0WZ9e0-RU8m1tEZP0U1_eZ0LX5fwnZ39FRiP2R25OT15USWaIehelU3q5hZ1lFUcO4vePG-E4UO-eiYqYqOssix0oJYvJ-JXnMGGFDO5XSHvfrEyPyQUkBJoHu1qk0zX1Ll2QTrPJv6A7MuVpKYY1mXqS5eh4xxVkBhln1fqpXR57Mhd5BBV9h-PiSI2pfh6YgpiACTcklWiUFSF79BD_JxqGzJlSwXNxZeizZr8yWnLvIUXA4Df2jo8EQdvAYCf9Zsr1vQP5qsUcJ_yKx-udqgxoQKSThRF58NLS9AHl88FJ_VeCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlvZpcmG6d_GVJ5up9R2e5stZo0GyUbQIKKlFJUv8lvgdRM4yQw6k8RGisWfrdkxvkUuTBcDaKrszLD7zSjk1jG6jWi830o2zddvsAGLH_mM3VHtTfJCcLcprW2URAUYT_ZIIm-LO3VM6-cf0EkrQQpw3NNzn-jXyV1n5JxaTdr5E150WSrVZbzXqx2897JpXyF7gc9mRU086GUEkxkhSeCF4WuZmkA4ilk7A3I_MCLzzkQuvwxYYhdc6AZhuBGpnLNjFYgmRNoy9dEOp6ZjK6tK-nmyGWwBloZOBt_aia7CtU_qa8FC7K--4rlc40TSiF_BKZp7749zSSeYfQDIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyGC-R_Z1rHqFcZjf42yKZnTk5OseoTrzdEzLGkXZf2khxvAHi24t8PFAbd14PNbbV3foziPthz5LsX6F9SZHC5JjWkz3bIjykGtam7soMjp-1P2O9DU6LoC5gcTEIfxegAyiehuxmPMp8QdnaVfAG7OWz0sRhOnuYtLPutoB3OPGtzcVdIon7JF8weJXYLCjdLCfsaKdQDblxaG5vHqwRLBnHY0pNVV4z5PExg22T9Hr8OsPRl8U88ItVgxNDxKCZw1ix1ncdzh_r8QGm5J38lyWLCeZ8mkPnPvSzTCDG42cee1vDVguO2qUklSqpS8rs-2Ww7u746JVgHSVzCePQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ8E53wWXS82npBNCgpLFmZibpKOw3iO-7iM0JbHprAXxhWlEedafPHruW9GpVcb5huxhPG2DILRXBREiAzFhUdB_n_QpF0cXGCwmZI4n81lVcXh63n9jCbZmBxknC9Rr7jGgHCyU0HpTak_yjgkD3FfRvFO31Fo6x8lqYvLRcRf4qRcUMEIKwx7phQeqmXVr_tLosf01qjwQ8gpgVq1SlTzUoVYBw6LpyIdxvwaVYZklz_B_HJa4L_sOv-ioPdN479IRVBHpNHuIJ9nUQVQkdg1GIdpW4FUl2BuKCQQR_GlRJFympmkXf3-z1RrsGx5EHmR8E8SDeOsqVJ0XTbINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7r9GmviS9gXqyS37gKIl6kgKAktHtrKrBqwSdNyI99pKY7BUTIdZFcvDBgWlb2eimwVsRTXxMq7rz9iKvVUrzFo-unNAIbL45A5-WdW5weJv_QOxKXTzcawRC0gF9ifLaPHv727NGga4NFXQYkJ3ulQ1oqUdcbEYKrDtejvpW8SgK60Ibg0QmVV0p-dKj-xEwh6cjOrOk0YDENlLDAu3BDI7iAEw5ms0kC0gixh9qbD3Uy_4-DdZDaAvUz02zyba1Qh25tPe07kgPcogoleBZQyo7ricv1fUQa5x2KE54lQOm1HhRkvojRJICpmLQ6-URiysAQePj8SaIPj0nZw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRn9sY0vtIqL63lopIlNjzLNWvs--_Vbhk5IJ---Wi5rd7SAOoybkRWcHCfZkFSUs40Ywg4l1mg-iuXzgLNEp6cf-WQQyRhchrLpcLcWKuBPIHhXKrwgXdyjw-gN6PvDjc4z2roCdNEiySa8DqONLx9zyKrKEbF-WC0Xd7jKz3qDmZCzRrBA49tm9R37eaqDYo5KYKQ7Qcc9j7zasaprKAfJ861k2lZ2qlZmnO6TTB-eDvOPY4l9d4VBHhm2CBUpDqRwDP3vVqI8GT8RkAPH6Xm06aACj9Fu8dPVJoG0gFmlGJFgvAPYJqFV9mVZhNc-OtvfTNHXs4_Yhcaz176h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=eXWq_onA5_kgleT1JMa92i3qM_y33w81WHdBFmS4ZyEOF1C4IK0xfS75f6Sh-5ppa6pUGS6YmDuHxMAVaq0xyjio6ZLAP-W-k0PSdz43qEYhGQmOu_YK9NtOJrq415eOBcADuQPgtHcEnp8FBGTkV-AmOydeFWvA7a9F_-8nShJakXmNcDn2nPB-4C3MC_QRmzqO6jctWHIkIEYUAjZ5SLtwa8lsH-d19rm61u4cz8hTv1LpwbTKvKhGiK2mOb6UMbJmyuY1Vnineb0gEul8XieRM_egl07xyVk5yQpIeBYVoDjYR08g6jddbBGfUNc9Oyh-oBTN0PGTFcXG05SSTi8F1fvdq5QCeHO-GVzD6Y1qhvY_jWq4GLNsbAz_ejmtXGitHOBMOz560UcJFxvN5QHoY5vYJ1U4Tnu1uZ7B8EPWYSX9_2RYyfKZn5X8ab8Fumv13kH23ga2NfLB9cq2WLXjGL8f5YpHGCcPVeXhpe2QtNdwo3akL35_F86dvkUF2xiELOM5L6N7TLE0xAj1UKU78ZLPRGYUiWF2eEO_oMMlw_MRY5_PJB4Zu0ZZlcd2sUTnoWsMtNjdpWcsy7mghI2orTPzwC9kWFwmEG8h5NzT4x-EUyJcT3hzsWZ6VFmSaOqXtFotm-vUqXGb5Mcd6jW9E2EC00Ab0dR8YFFAyp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=eXWq_onA5_kgleT1JMa92i3qM_y33w81WHdBFmS4ZyEOF1C4IK0xfS75f6Sh-5ppa6pUGS6YmDuHxMAVaq0xyjio6ZLAP-W-k0PSdz43qEYhGQmOu_YK9NtOJrq415eOBcADuQPgtHcEnp8FBGTkV-AmOydeFWvA7a9F_-8nShJakXmNcDn2nPB-4C3MC_QRmzqO6jctWHIkIEYUAjZ5SLtwa8lsH-d19rm61u4cz8hTv1LpwbTKvKhGiK2mOb6UMbJmyuY1Vnineb0gEul8XieRM_egl07xyVk5yQpIeBYVoDjYR08g6jddbBGfUNc9Oyh-oBTN0PGTFcXG05SSTi8F1fvdq5QCeHO-GVzD6Y1qhvY_jWq4GLNsbAz_ejmtXGitHOBMOz560UcJFxvN5QHoY5vYJ1U4Tnu1uZ7B8EPWYSX9_2RYyfKZn5X8ab8Fumv13kH23ga2NfLB9cq2WLXjGL8f5YpHGCcPVeXhpe2QtNdwo3akL35_F86dvkUF2xiELOM5L6N7TLE0xAj1UKU78ZLPRGYUiWF2eEO_oMMlw_MRY5_PJB4Zu0ZZlcd2sUTnoWsMtNjdpWcsy7mghI2orTPzwC9kWFwmEG8h5NzT4x-EUyJcT3hzsWZ6VFmSaOqXtFotm-vUqXGb5Mcd6jW9E2EC00Ab0dR8YFFAyp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
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

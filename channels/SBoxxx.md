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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZTnbhEcGP_cSO0MuMRV-dkU4PipBNgxob72o4ckIk7byftOrfXPUhUE0uSacDms9A-MZqseDG_-WHuu5CKHz4JSMIusvbuIXT9ZvVhiC_-tqwzvzanlapuZJVABFzYtzGkjurxIgJoPvmojOtYlMmFXzDEB_uDDWP9ENb4Gisk7nhAXKSqSj3CJxa58uKYGzd4dWt6XeExWD20dM_DojM1KoWrxypCG5Kqs6FOQ3JmmyOIlXWMXtzPRCWIPFtBNG4HfJE1c8VWocDRmkq1ef_PWIlJHYfgwGvRZ_jaGnuRbyXK3Tblh4Hf3iaz4zB1TLsD4uX3GGLCoejiQm-6nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYc027kXIrcqluaXzSW9CGj96kGj3VV2S0pRjwEXSNYA7ToZo7cOdqYvvr6uBTPakrhOljqEWKbgVhrirR-pWX5GLqpibPTGE12zO7sUO8CvqS3TwHZFEk2fjw96mA4BNPHfxT3-eQNNd6o6K9exhrPJhAU8miZmBo1FYVmlMu3yBiYRRnsF2XbYOgC3Ix9FAA9CZyg0jmbrPSPfr2yUlgdZLZX_y3pm1v2swc4xrfpWEsb1USw4h3RJVUKIqFppOycE47tgv0J6Zsj7G3aHj0JmiwJpN9XwLGM4UBpWAyV5qtI57MQxHf1rVeZAu0OHRy8Ygg2hxs1tr5siypbfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOKO06ErVovvT5XgGH-KpRVwK9gc1Nh5tbqux9TRABn0JREPUjJMA8Je8zEHf0FJFW5wCtQmZJneB7saEk-TLuMHeGZV3zsK9PkNRCGY0yQhrdAJbo53CSF6wR9znzXyS7VWMzjDvllk-25kIgyHAw07M1WBBSy0565hG8R1S9vwwpPfKhUx1bj_re9w3jW41fNaIuCaGjsyWPYnJNyDNgR8EUY7qF7OWH3JxsSKS_uPE9-JboCBXC0XHm4vyvkiw3u4u1t8L3moNQkPWaO-gzI4Xmpg4Rl77j3R1mSX2oJBGWTO9yoju-bVv-dXzDlkKahGDeQW59gu69KTBjlHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRJJ2t1MvF94yFyxNO2vT4Pmlnqu4ab0_jd6DqemvZWpcnlrhqoVIActtCDMflgF_7DT6zmdPXeyLphpaDTkJkZKSbKzMQzvJcleDPtzV14wcO9263cqL_e_CdE66TuNb9lotI9QPfAKMCDOUta6aKtyYT0bE_Er5_RLNXiksX3pySFeSqChNaS7hrN05QPTRxqo1xjyLH_szrXsd5ThiVqPUZnBiC3CWuN2LlEOSwQPFNb9jBQI_SmxOss-sOh7fqGs2-Azgy-Frp5Nty8gmPCCWCMudrn110RuO1BDjFRU-3BUGnU3CeyuveR5MyJqFkrJ6Ot-TqSuTHGRa69eTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDS87z58SkZuGsDNIgJxggtklZO3HnDKiU2GZAH6r9Yeg7kN3miO7bpeQB8ofQP57K44cMkSIozCzyn6SbKalkAUrESM9bcgll6FTxN6KZgsc-WA4zM1jPa_xLZaC47b9Dm-3FcUXsa3YnwRy_Bd5zw2jzXyFht6aNQRrgXvakKGGGI5K7vNVqDJjJq31DFLFm-2LE0UqSYmU8We5f69jDIXXXS_MTsteOIR-l4_Qh5OnO3gB5lw21nnryP6FKnyZ2HcB2pAHudpaP8jkhK5W3fMOva-xh9L50vMp876s74rH0GwuWbbGtz4Z_Aiom8WcmtZ_WhKfvcIaKjWvu882g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8tQodypWQABXAdc6dNfbHD29RuYPgcn38GPpwcWY6F7koCDQh-ojecgB6lUe8DeZzbnruolujJj51QrmnbX8ayKXsiyoZeirNnM7FdjsWoUc6TC-PJ7jMFLz04S64PgWK8VKgHEYGuUVv2XaIEK9wA6fDvJLTWDwokXwVNXYnVBaZcqSNcrhRXY1b5yskn6PT45smWDrIQyG70LdKzWbMx4DLOJIJm_VId4UFSATTsMsb9qwjzliHkr-9hUlTkG7B8PNo1eB1NN8TTvcbCi2DP8zqNNeRMjfCdLMel3Y3iacUkOsBKm0DjTabqeQTwhL3a5lt1MITDXd4LxJCiANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtKGWflHs8XYfQ7LjQqxo1xPJwhrbLeIBlbDk4PRMAUPwPPwojraXhJ6Jor5ZTZ4Z2jVY7sAtt-H5g9dbKdkXYoeLCXRikBBNEYD3k_LcXZPzLXnI34FE0AoJhVKFZ9y4n0r1qivRpK8SZ9rGiwDk9CVjrhI7p7ioxIgSE7fXkSBnJ55rMWsGLaPiz5t-iVGbNb_EOqgnvcTlVQPnBSyFPS6dfWzxQVNKFW0SUQbwG2A4lfzW9Oi5E2fliErFeQPfTc7tBs4_htozDH6bFQ8aoClL2D0ucAghLVA1jKjPxkP-2WbgthODhUgIJKwsLq9KSl8WZ_PNXB2wrGK711JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6tPPME9o4nRi69yZceF12OT7jUFlXNnB_dc5MkzFzTtWqrM3EQ4C9nE0YqIx5QEs2MBoWTxD_JWbOApgdijCAA1xk1BiPJxDSCGwHee5Sfrfz-gdYu5l_TTpKuPgxL04ffM24VLGNvJAYbFnZnVVF0ZZbOzDbPsYxnn-PE5yA6cfv-h2DnRIiQwNAZzYMj7HmI8LmrFfvleSdF6f5a2FCt0CTdJ3FH_jdqg6ahvhOFc7-RK65pF00ZfKv0XE93OwdGye3BdiYTVTaPLJJG3Q8y5ZrBm1srh_6hNQlFFen8DGAilBNgixjUGSHvdg13Smy6ltMbiDvn3G9NCL0rehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8jz-Pq8JaGWXepU2EygW1PiUQva8LOTNEN2eAWittT4-Dwvp6cBwEkthBBkzRE1emOAUk6BIiGt7fyLmfkpdqsiCv3O975obIHN1-qv65yRikd3DUHNc2rpdE9F69Kp9namLhJvI5mh0QJKSLAii9G79WLvG9Rd3bUpNzcHs_HSm-pRwp0iu7o_yPtq4q5b3zch6yAJPvRYYmhSOnYivLQq3Zk7RHMKM7vfGPy33RBS_UIz_8GoqcshuiYdRA8Nw_VULxE-KArIXWGadO6mJ697kI10PilGjzNfJ07uCtJoDAEEOxoEJ88ti6MnkhD5v5-vxNOikWMlq-spbysxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3OZlWN3xyISGQpx5UCDxqaJM4bqbS3hMXKYBcmwZZGi7WFCm0r2SYgXdlmOeeBOu33PiBS-DfUj-cEA1cxJFHWzoK3997WAb_jQCK9z66zZkrd8LVLDMZRAj6XK5kS-9tNNiGIgakllxLh5xl6x7d-yu2Tlen9zwW6ykxHLa1kefq1ioQvsztlcmQh98qQIqzSvo6Qk0UtA_hqqmaYNLG66fMh41siQM83CJTtRBOFeFxxxq9AS0WBs09Eq5DJEgFCnG5fy-z15EQx9l9a8VB99dZhChTQLvrZxVAn6JiwEN-h7W7toelQMH-9gpK3zZbWI-kepkWB41XKkuFPPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpc0qFIo8ZU94OYyYIvbYyv1gi-nTb7rZyLgilCqjAapaN7GhH2Zkyy2LR95zvVzq1CqKfG7IKo_n7oZ7cfAkgImuNheejnYi3ZxJxSxAGdT6pw2w3e2376KHwNShkb1inw4T-NgSJxg4o_2kkhTr1HHyE_vucxW4SWm8IxzCv0-GRe0n6hY4bUbY5ytSnK0eUUxzH7w9GMKR2nS9zyqonvkyPiTQMeNGCQ7RujbqBgIfL0zNvMEWYgyPXUOE3j43aHlB4kGlX2DQmUVsrV9-v8myuWNEFmjq3-rPuEKWtneE5ks0H93Wjmj9spVe-EpNxYwYG-WqjL0eIAO0XBnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2eUdUA_GjpX2SsfvbO_xJ9WAWpP3kbJI7C3VlaCv3BDInb6Eky6lysYPxPrfftPx-pn5IXZbe9WEpCo_hAFShxNAls3nGBOQbTfqfr5LTIGlxgKhp6FuFE36DbyzlltuW-EC4002aBdHlhw8grgXrJZMwbJ23amtGSK8vPvJFPf8ZOSTd2edY99MpSLI-a_XFYTffTbInUyBMN_yUgZuGx3vvQ2yyEhRmsiIrtVJaFwIhrtgaGkQC_QVN1SxYN_sBWDHarnwlSDxew8FPFLnV2XkObUxWdUx1r6h7f7h2OOMcnGXv_7o7naDceA7r8nzjFhtZk2w_eAyRqnm4eIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUEUYsUtD0FTfKHmvmRcGDxntXoDEFRUf4FkfL0b3xWiJI4afM06K0LfH4dVsfqkMGEQyPVGG7hTaPzPPUOGi2cSpsj40B0XBuRIUfSiZwLbF6zLknNHU5Gm-Zh1ZLv0Mfq_G8zxqaHJYsfpTb5uZtfdGpD2X7jjPmR5R0G0thhs0ebQLaPbUxheLJYbYN2rw3797wLLsJLZTdJ6Rv7i-88YIee-mLoMQDNv5IYsZaoz2EOoZcAYDW7jhykAY8Bf7n7icM9QPPGD5ElclzmZYd2MT2PUrGcM7vowLT8tChVt44RaktBec07efPbDi3OiuXsdS9NJl_GtFyMH6nq9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8wIW5c01OPcbGGJCxLDoJZiSYe1zhhJIquzSHt3SfBM_ZZQ4n1J8aT0XqtXppn8Gxj-EEQTy0XY4JQmRjQaw5VmUKmbu-py4GchAwUuKR4je-fZRsKX2e6aA1Ho7AjOH5hzjjGZtEJAxqYbaMu1IDL_-g_eLFdwp2x4b01VNLZ-KcVtZlDxsxJ8EXhIA59vD-ugx4Dw1PWySgEfgP72GF6lfh52qUL_amWRibWGDv8O6i8gaLZmuWzbJPi9Boc5GW67w_4O5NVIP2lX8sElenGb5DNLp0s6x40K27OqS9OvAJnoKxnNpuxFHfsPmzxmSqGa9omLwwCAliXfBA6DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8kp8imTgv55r9VLB2ZcdHbXmqmjup46rOyAwgOfR36L6-Dm-4SPWAtTWGKDQuZcQ3RbKFTTqoGwkmdKmiJnYxk9ZuZgfCtqjoNHXYBvxXXS0lV09aU8oSQcFaWBMCN7T769UNetLFTNhNR8teXADQyPr3hcgNANivHM9iI7bp9RaTuaGp9316v_S5_X94TOPntyHBDZIu-mc7a2H98lDtz_C0PCGJUEXwue6rHDZ46weLuP8AcR_jG8xpp4Q0Fbotf3sOyvNyK5PuIBUH0iZApP5YBOmjcR9AA-Au_HPmGni61eorFkJLXbLrapo2xBkaubGV9fzv4ENayQHj-3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=KXC7nrX4QM9UugtuhgZvvIupz1RKHa-7qopW8Xupzp1Dmffo-DPEWZEQ0F88yeMqlUPbNN5Kv-Ey47HteeLU2ehVmTWy28yF-fAMIx2aVMZMr-iN4ALSlpoRxcj3awwubSBmHhuQSdDv_P0a5kELF3UW76rddHoFpdwUc9nZPRO3IpMJpK34OklcXoTBMgzfjl2Xoj1liR5bqidWgw1ThV4TS5IW5D1xKrBwzxhYURGH_8-N2BeJ7YL-8kbbCOjg55LWmiINCB_HaAocp4plQRDnIDVpF-cmPBaPuq6IorDaF-aTqpAg2woAAOu9bm0se8QMgsK3uGaNY-Zdhc3oAL0G84IIkjj45lHTJGMY7HY__VgAtyjwqOX0D28InMOGYf5SRg8QM1DReS6-l1xD05NTi6eWQfR5AnKrsE5IRPvFlwS4Eaz_yghHmoPEQ_Npa6royNp1PxKBuq25xqvSfTEW-rStEAZ88HWafbV8Ij8Q-NAyivWigOCOpgy-WV2UHHNz39P6CCzcISZaObGOzTHejKuWw8J0VLh21IE6K0_YHJgPfnSBE5dmLQZb7GkZlpepE4Gf1lqHg_U5uF_RzsQTvsaQddLBsoo8UNi2unFwTaIZsqtcZe8G1aTR72naOe6pSfYVzBTfKFLirOHCS0Pw4HuvKw4WhwaXgE7Emh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=KXC7nrX4QM9UugtuhgZvvIupz1RKHa-7qopW8Xupzp1Dmffo-DPEWZEQ0F88yeMqlUPbNN5Kv-Ey47HteeLU2ehVmTWy28yF-fAMIx2aVMZMr-iN4ALSlpoRxcj3awwubSBmHhuQSdDv_P0a5kELF3UW76rddHoFpdwUc9nZPRO3IpMJpK34OklcXoTBMgzfjl2Xoj1liR5bqidWgw1ThV4TS5IW5D1xKrBwzxhYURGH_8-N2BeJ7YL-8kbbCOjg55LWmiINCB_HaAocp4plQRDnIDVpF-cmPBaPuq6IorDaF-aTqpAg2woAAOu9bm0se8QMgsK3uGaNY-Zdhc3oAL0G84IIkjj45lHTJGMY7HY__VgAtyjwqOX0D28InMOGYf5SRg8QM1DReS6-l1xD05NTi6eWQfR5AnKrsE5IRPvFlwS4Eaz_yghHmoPEQ_Npa6royNp1PxKBuq25xqvSfTEW-rStEAZ88HWafbV8Ij8Q-NAyivWigOCOpgy-WV2UHHNz39P6CCzcISZaObGOzTHejKuWw8J0VLh21IE6K0_YHJgPfnSBE5dmLQZb7GkZlpepE4Gf1lqHg_U5uF_RzsQTvsaQddLBsoo8UNi2unFwTaIZsqtcZe8G1aTR72naOe6pSfYVzBTfKFLirOHCS0Pw4HuvKw4WhwaXgE7Emh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwsXWDBIyPe-FSGOOx9IFHImGhbSI3MWnIxYDiGCNDzUVo7kRqVodPYqy9gzTn0fZAH56PM7NgDhZ0r2JmaG3oSnECVTKF-pyAXTmqgbBw_x9npBOZAO_-BdMfBf6wKw0u5_c-6LN_gC8zLUJQPnU36qfKZWYBYxSbI0gFVLBOhLM2dG5MvWzH-sTTMVCezKh2k2Bjys3u7UKTE5juSxo7_hF-YbQsPXt3Ntqh2565VtjSpSQ764E0zP64EU0A1YbOCqTV41606dH5zQqxECmhK7yUZPhJ8vsiEUZvnXvc8q_FnpjbBQ8bD-WwHq_dPBPMH19qutkD1Muj40wR5i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=TIN4sXfUYlwuQ-4KX4_m2vmNQ1ZE8CkL-jTY9MVve6uEVqr5vYoXySxDmiO4V0sbdb8WlaK8UJrZelSR406Z6SvujeOmsHRPqsLKmTeRul8loalItG3h6TdHWAqEmxw9mOIfiPoCn6EoCAtZvjDQeLviGahlcSb5wlz2TEKX5MnpOjd7VGJ8nCfWLDF-ImpaMXE2kKwMiQjFD7Bh-p3BxSbr5RGBlp_7cUzWc3AXwf59dz6YGb6dEK6y0s9-0Oa-aAglUCnlKncjnwMWxIZ22P6s5bn-mjdXCnvTtRngXje1rNdeKUDA3artTteHAo7RnmvwzbXL_D0b_XQzkBnuVaktb2TxkEwFtQu8C9Xwp84D3rSNk-yQNmPeEmbrxlMj0Bmy2pCBEGC4-OagolLx2q0wWqA9NN88R2UCe0fduTv-tnEnVRI2kziv10PbJEoWNtXTtSjJO4MeEWLs4yVtlKBmYHf3FwE7LKyI7UNBKUVlI0Pxd8eFYyMIPOY9ijLWEA2epCfn_J-QSJ1nZH8SxipzZYfvcKzCcDWucPJiuBc1Ob86FD-mCtMYsfkjL51QPHjdaNJYJVyJxP6HvU1cL7HoI6cua4Wqv6uLsR0i8oWBmoUkkmIapfaoMqNFVhVauAk46E___evfFENlBm7QJsHAIdZ3PqlX69-kkX3kOkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=TIN4sXfUYlwuQ-4KX4_m2vmNQ1ZE8CkL-jTY9MVve6uEVqr5vYoXySxDmiO4V0sbdb8WlaK8UJrZelSR406Z6SvujeOmsHRPqsLKmTeRul8loalItG3h6TdHWAqEmxw9mOIfiPoCn6EoCAtZvjDQeLviGahlcSb5wlz2TEKX5MnpOjd7VGJ8nCfWLDF-ImpaMXE2kKwMiQjFD7Bh-p3BxSbr5RGBlp_7cUzWc3AXwf59dz6YGb6dEK6y0s9-0Oa-aAglUCnlKncjnwMWxIZ22P6s5bn-mjdXCnvTtRngXje1rNdeKUDA3artTteHAo7RnmvwzbXL_D0b_XQzkBnuVaktb2TxkEwFtQu8C9Xwp84D3rSNk-yQNmPeEmbrxlMj0Bmy2pCBEGC4-OagolLx2q0wWqA9NN88R2UCe0fduTv-tnEnVRI2kziv10PbJEoWNtXTtSjJO4MeEWLs4yVtlKBmYHf3FwE7LKyI7UNBKUVlI0Pxd8eFYyMIPOY9ijLWEA2epCfn_J-QSJ1nZH8SxipzZYfvcKzCcDWucPJiuBc1Ob86FD-mCtMYsfkjL51QPHjdaNJYJVyJxP6HvU1cL7HoI6cua4Wqv6uLsR0i8oWBmoUkkmIapfaoMqNFVhVauAk46E___evfFENlBm7QJsHAIdZ3PqlX69-kkX3kOkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggrkkh28OZBRAwXNmpU3iEN66mY9j-MH-QNfYpIxFUU5KCtO6sV8G0x4gmvG0sPjD3SbDQ3tjbtkhTLyuKNZI5HLQNuAg8GRXUDlCLR75J8-rJkmjVynmncT8pOh8K-5i9yBCc9LrYimR7_8QJGBk2Darw0-spd0HomoQ2u_HStzWV_jO2e1aTrHc1STMXWbKcX0IP-tDK07dYQMl87qaccQB4L80fEvKexQtWcy6eUXyDXuaxVZpdi1ZCQOjA_cbF77TmLIA3IaAYM9XHlGQRLES71uOMcgcZaoO8n1rATjoOarbc754bkUJ7jOpSueySlNxXfDgUc06Zv69NPBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=s3GrYSjZREiw1sHVWq_ao2cwbNQO9DnfvpJQb_551qpD9DwjUe5sqDP_Oo2xl8lpLbAPGxZEkQ6fPQ1OBsxr-z2hSRQdGL4_K_39T3KtXg4u0qWlMxNKrb9KVm0SZeJX_4kqNQL9-nNtfRZHZYeRFNhwc0b7YjrYe_4PVYKgJSC4RLL9S1VsfFaV85OwMVEcxfvETocvlMzJetmP2N68s1GKdPmbBvs08Ihh8B_wQ9BgeqZcVceCBymIiaRMdFzoekYfbbwEfn6FLUdSPjgV3F7iP9wQvJHtdcf3YqswNiPYnkf6Z-himBJsHLuD6it7XBfcFd8XPeWkA6wwwX0dmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=s3GrYSjZREiw1sHVWq_ao2cwbNQO9DnfvpJQb_551qpD9DwjUe5sqDP_Oo2xl8lpLbAPGxZEkQ6fPQ1OBsxr-z2hSRQdGL4_K_39T3KtXg4u0qWlMxNKrb9KVm0SZeJX_4kqNQL9-nNtfRZHZYeRFNhwc0b7YjrYe_4PVYKgJSC4RLL9S1VsfFaV85OwMVEcxfvETocvlMzJetmP2N68s1GKdPmbBvs08Ihh8B_wQ9BgeqZcVceCBymIiaRMdFzoekYfbbwEfn6FLUdSPjgV3F7iP9wQvJHtdcf3YqswNiPYnkf6Z-himBJsHLuD6it7XBfcFd8XPeWkA6wwwX0dmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFkkknnQgFQBEIjEXw2ao4WrpWFZT8QknyfMAHAL7IJl4gbQ_1B_sDS-MvRbL-ToU3waQA06K1UWb9yy_nlQYhDvIJwutmSj7J3EkRPnIoCN4_PNSuk_gNlbc_883TVjE2UmnC8L5LwU3DG30yEAC6ka8ESY_SKlOS3R79Rc9VKjnIyBMK0pBmLvKEy3fO-3fnpP8U0KJ6rIRoIoJDRX_G1JxFIcGWcM-aQQms8ZZNYP5_M4uX763X0oCFzWdo5EViEAHUcuL6ndSYj5jEBMHgRJYg6NzJXTuqaQRhyQlVx69ENNxc_sxubVtLx-NND10Ap6SfzkizVabFsrwGzjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXz2BO3bb-AD-iBaDhU4EbGSXM0dPC6D9IdQ4BtmvJR_trrAOl4Yl4zZ-eOlp97LTUs6p0Asbv5tyTBasYPS8Jje0wAZQdorzIwk7V1rFFmfQc7mOvH2hN--f3giWE0ebUHYq9V3Ja4hvQxNo-JJgnM9QrL25KF7LFCun36LL9PMJbadL0ncwBqTSH9MYj3Q9z-OW0pJXNGUBFoChjZFD45k_5iGLqrfu0XOpGjCyoXj82_9q8Y_JAS4digbwAWImqZc0YqLmL9z12poqp5hY57rMeWspurh2clEIo0er41XT-L4c3aQzzL_GHe1geoeO4E0HnXAJH_cOSPABmTt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH26kSybRXyy5pvQaSVDd0Ta537dtYEYFJSzNAbYPdWBPJNTiqiCNmd28Aqw4kcgmXX5F4uunDYu9O3ynSd99GR2fHLGGk4HUFeAkc9714Fbq9HSm6zzvD87RZFxxiPFnpp-3cZJuOPQzq1CYIggNA2iRRTAiwySkQ9YUkhJdWbGWz2L-duLJLpsraJgrZRD4GTOFvcymzh_eC2hRjIBlJFE7uPOvpVlhOJX77isjZXPWqp8hGCfr309su0aeVPuvxfmZmRSZjf-thWrBPaVmJQfMh0KlP30newxeoGnr-hURQWe-A0UbIVwoqAbunYbGFLamBdIc4VggWgp5mgRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpgL8-3B-UV0lzDuZ-CvU6Lmg1lrTOkpPePCRd8wmngwaYgoqOKQ_s3J4k0Uift3zDtA-T95psXHCMnvi53nxvchrAmJt-THgPjf4VVbh7OQJcg74RS83BVeBYUag42MF-3UqNoeDeS39fyjFwxjs3Z8gbcgvrSBBTxMu2Cyx1EjpwjJLkOAKNVRh-0DQK07kORrj1WyylUDqOaXl8TBUu3CXM4IduAghcabROwtZ6mQdhqpEczwG-n3P7ZJkXPffioiPMkI3EIp8P73vtsbaUVjcbVndUtT214-l0J4dEGhqCdhEld-QI2kRgXPPAcwmYrQ3vR5NpBr5iWFMZaMJFUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpgL8-3B-UV0lzDuZ-CvU6Lmg1lrTOkpPePCRd8wmngwaYgoqOKQ_s3J4k0Uift3zDtA-T95psXHCMnvi53nxvchrAmJt-THgPjf4VVbh7OQJcg74RS83BVeBYUag42MF-3UqNoeDeS39fyjFwxjs3Z8gbcgvrSBBTxMu2Cyx1EjpwjJLkOAKNVRh-0DQK07kORrj1WyylUDqOaXl8TBUu3CXM4IduAghcabROwtZ6mQdhqpEczwG-n3P7ZJkXPffioiPMkI3EIp8P73vtsbaUVjcbVndUtT214-l0J4dEGhqCdhEld-QI2kRgXPPAcwmYrQ3vR5NpBr5iWFMZaMJFUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpn_FQSL4LfPewonDFuwbtJqxAI-a1toMdBahyYq09_XqZVywuWjQYpAkLI5xRTRGdrrXNTr_iYcYCVej819rc41cacuAcFlyXor38vgGWFAZxGSAtFFqiJbm18Yk76TQOH0aXsxtB6acIkOB5fHUXUmuZZ07E0kYV7OZD9-y9P8qbF0x_jZP2eNNNPP9zdOzgVkUrfL-7GA8yCr7dYpXi6WFZKAifNCMwEp3Q5XT5xdP7P78w0zXe8id38giXLjHtexU4YXKV9QBBV9qALYZuvkeTRGbTCn15FQ9UwgEKBBLUjjSyPaJkujp8OZFizGmtfdhkzJq0b41Sq1_3TpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9PcmM2I2ZkRRdx_mAzOyD9jvv2hdF-DrQeic0roCkb1_t7_wkg2rXqNGxb1RdIeDwppdaHl44s1KbFTDrHr0POy8etcbnsFOiLVmi8sLnnsjBjs4ceYhF-aoTiSWZodXEDKTPEfXUADagbcgukAovmydh3pav2E40SxlO06JyhLhBthP04WsabZR9Hm_99fKWBxlufE6KsqmNXd_SU9Xnq1j1pns9i6PLSvSgvQUiWMJVY2RrZyg-0d0pHOIv7F9u-7ajU5K6bpXBB6-Y4UUnr1aVr9_7M-1F9-OveW7qqNH28d0iLlM_Wi33h_n6SgCnGlQcSsdLFkDBHwZ_rpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC-2OUkCtjF6FzFS5T3Mlu5-TJSuOsiL60y8OXEfzwwxlpP9HjAmedgkyakF2Dq6Nqalrq7i9cNqwYjnDYeuHybz-TZ49tYgSqobP41WeL3lJhw2r7NFvYBUZQZvjTP4HjCyXnKi5zOKmKElVQaQ6KZTwiitKh4c4AeqeYdxU3JJ-Psp0pK4aMcjC4uMno3V_EwblbcvW0dOS7gvYksO3cZcvh1ER_k8hjuwidY7WUBYXBdxj9mKLRUWB3VHUDb5V2wxmGAxyPl4LFSavs9v-hVJAuH50eAJUlxOQOvD5Ce7hbDdODloFGG5d57hIpk6FFm_bPiF5dokpass_9Zq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMRN6oFo-lfoIYZ0MKptm8dKfXJyjmrfytjPo-X9NAfZ69YLzjapbG96jdPtFw-s5KIPiaVqBymY-PcM87CDFaspN3z7QOvQ4tBTk-Kjg7avBRBB7MgRbD_4xlIwREFYQN8hfTWXCJMyNrwM_XJ44cWOvbinJDbYpfaRoYk5bCCAl3-smFpUzGThAR2ThefPW1opqDLOsn6_LLkHPFel6ZrDnsOW4v16Ymldq_vEcpaLyYouqiq92Gyz6prL15_bn-foETNJbrMHNLDogjzBuhUZeJXyym-IXHKzq0igbtWA7iwLZG3U3iFKQq4PI_skNlJLnH-pe-GOYQWCQGSOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMOtDyOmaDNCWuGi7n6NmQZDo9AgS92gZyEBReplXhc1DQLMZcZiJAValUns67FvC6b_vekoHySmrl__zia-RWNT025JheCDN4AW0vbrL6k2aA8AcCtTZRgN4ae7VZcJvwNT8zWme5-Pl9ApRM242AzkXE9mHrntDXetAZNfw86DE9bhMNoLyM22zYfABkVXpc1Zv_S5rgtPR0J6eebq7h6G15jWHnwpNV48g_kubhWaxDipxA9Jnnlrk3O0NzrlQu0nN9PSR_HrQX5uzHNYLHPTZleYFnVS-_ubDVZoRXwGHIj_AOi-4PuEPpvQkKg1zl3xZ6BWWld4Xx6Jayk-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=XCjztJ0d-dnK_KmCiPWa0o0mJrqQRGM0QCzKNIH_xb7F6115SKIIr0y79iC78V59yu8dtpT98YXDaBjqEiR1gRwUzHwvqstsPz734os6XGUAfdMuxYBh8KTDSj-CHPvldfu41LsiXaT-o4tQOtuKOZxfMwWlcGnkQ1svX72nXAS80uQmul7QeTuFXqzw8yww2nN6cnlfHIX8DAcA0IW1h53HPt-TnHFgITFAp5XPm_Ib3r_LE--dvP9micbV7ffiLq4U_Cm8M-kOwJ0abCIPNuOYj5tHa07lq3qqNaBqkxi_5UDUlRgBUxhqRnTMvGg4_50qTidAJaOQdFqb-wYBKySrM5EtM0NIDpYRxOsIib4N6OJKLh1Ufd5Bc6Ss_WyJW079nEMc-ldNrdFtGwuMi4F_bm0BOcM5ONzm32du26i2CQmfuXqNVuu0WQNDYhGuH6A4wjTwzcPFT7LPF-sZz3VoE1xyJGGKKzBEq_IcS58P-GOgf1AxZdU0TcjbbjiRDnO1Mw2BzDnpD3aduobigAnWG1wyISEF-F-XIv_-TU0kr8rgt0CCzlkC_XXuR9RH0VbTpm8fhdzWw4lIyUr-lPXJuI8QyzSCcFQnDAzE4GB6O5bPi38n9ygBjcY7aElz5NFes0IJaxrv5kYFyj8o3k1CUlJj0Zc6Vj7FNuzl-zI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=XCjztJ0d-dnK_KmCiPWa0o0mJrqQRGM0QCzKNIH_xb7F6115SKIIr0y79iC78V59yu8dtpT98YXDaBjqEiR1gRwUzHwvqstsPz734os6XGUAfdMuxYBh8KTDSj-CHPvldfu41LsiXaT-o4tQOtuKOZxfMwWlcGnkQ1svX72nXAS80uQmul7QeTuFXqzw8yww2nN6cnlfHIX8DAcA0IW1h53HPt-TnHFgITFAp5XPm_Ib3r_LE--dvP9micbV7ffiLq4U_Cm8M-kOwJ0abCIPNuOYj5tHa07lq3qqNaBqkxi_5UDUlRgBUxhqRnTMvGg4_50qTidAJaOQdFqb-wYBKySrM5EtM0NIDpYRxOsIib4N6OJKLh1Ufd5Bc6Ss_WyJW079nEMc-ldNrdFtGwuMi4F_bm0BOcM5ONzm32du26i2CQmfuXqNVuu0WQNDYhGuH6A4wjTwzcPFT7LPF-sZz3VoE1xyJGGKKzBEq_IcS58P-GOgf1AxZdU0TcjbbjiRDnO1Mw2BzDnpD3aduobigAnWG1wyISEF-F-XIv_-TU0kr8rgt0CCzlkC_XXuR9RH0VbTpm8fhdzWw4lIyUr-lPXJuI8QyzSCcFQnDAzE4GB6O5bPi38n9ygBjcY7aElz5NFes0IJaxrv5kYFyj8o3k1CUlJj0Zc6Vj7FNuzl-zI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfeNmidArGZW8u5w-Pyi7YXWZcscU5ihRmKp6lAaLzmmJ7A8a9-t7-hbGiIPIkDxKW-belryD_N1OAHeQxkYJChHzWSWAGJy8rYBmbDVXx-ggVBxvUa8xpun7dkiBrH7B9IZL30xkvv9h4Ai_p0jPbGUNtZtfHBUQMRWfPH9dL_aDfcITy10HyYdbZYojNl8vz3cq6hlu6eqUax2GOifsgnAjZ0u8odezuyVw3tAiCyrrJnRXqCEOhiuQCoF3AwC3_cYL08q6-oEZKZUaLgZ7m8bdDm2XMLSS1dFOkxc8Pahdnlr7isIVcL4BffYgq2bIVC-uSH2EX9A7gi5MVKewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKRSlWZbrytxhdCy-wZi1TCu5PcuBmKEU0ih4R5qA8klTXqI6WKVXGQOAUC_h-5MquTnSD5r1-Gm4RzEKN3ijw5o4dE7LNhIrV1O_uKG9w4EawOL52bYM_CQAyhc5NuTfYzp-NHGLKcxAcYn0_LCoFisDCdmuqtbiTJhz3qhrXrvGWJUhSGu84dIXEOr7vgZLnf-LYZhuBncPhbRlvXs1xLZXtuVTeenUngxUTDKoQ8yGjhpMnsnvLIDhTlA8cuyF0itBDIONzXVIyKX6M0Wj81-9HAYZH19LxZD6j7MYvUKUhTUiwj1zo3o9Q6GCQ5NM-pdY9sV4zT4vczr6DLPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCBJce1ESqb2tQklTpqLZ3oUe23hKDSLgeXqKfjl9AJJ0yFye2vJGEBYCDUPhWvOcOo9w0xGcXmkVeUa77T-jQY2AQq4auFo-IoB2Sosu2LaBTd9PPRociKDMUJhvXHo7_E3nG2n6jkJrDP5sEHbq3qJoxmrNSzqqGHBMZAi0cn5f6MaEk4O5ixrqrviWAQSDP4-6ocFu6Vd92kyAoQkNr0wlRUnSjKNnVR72vE7_aNtRABDWj7ymjEp6RD37glB5f6wu-MIo8HybTedhKGeMqWf-8RsCv8mgGPEBvB-sbMBUAY6TR3ITzbCLR4UQMg-EwxUdn4JEuE9loJB_-vQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

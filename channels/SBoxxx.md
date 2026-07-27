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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 23 · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYc027kXIrcqluaXzSW9CGj96kGj3VV2S0pRjwEXSNYA7ToZo7cOdqYvvr6uBTPakrhOljqEWKbgVhrirR-pWX5GLqpibPTGE12zO7sUO8CvqS3TwHZFEk2fjw96mA4BNPHfxT3-eQNNd6o6K9exhrPJhAU8miZmBo1FYVmlMu3yBiYRRnsF2XbYOgC3Ix9FAA9CZyg0jmbrPSPfr2yUlgdZLZX_y3pm1v2swc4xrfpWEsb1USw4h3RJVUKIqFppOycE47tgv0J6Zsj7G3aHj0JmiwJpN9XwLGM4UBpWAyV5qtI57MQxHf1rVeZAu0OHRy8Ygg2hxs1tr5siypbfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOKO06ErVovvT5XgGH-KpRVwK9gc1Nh5tbqux9TRABn0JREPUjJMA8Je8zEHf0FJFW5wCtQmZJneB7saEk-TLuMHeGZV3zsK9PkNRCGY0yQhrdAJbo53CSF6wR9znzXyS7VWMzjDvllk-25kIgyHAw07M1WBBSy0565hG8R1S9vwwpPfKhUx1bj_re9w3jW41fNaIuCaGjsyWPYnJNyDNgR8EUY7qF7OWH3JxsSKS_uPE9-JboCBXC0XHm4vyvkiw3u4u1t8L3moNQkPWaO-gzI4Xmpg4Rl77j3R1mSX2oJBGWTO9yoju-bVv-dXzDlkKahGDeQW59gu69KTBjlHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRJJ2t1MvF94yFyxNO2vT4Pmlnqu4ab0_jd6DqemvZWpcnlrhqoVIActtCDMflgF_7DT6zmdPXeyLphpaDTkJkZKSbKzMQzvJcleDPtzV14wcO9263cqL_e_CdE66TuNb9lotI9QPfAKMCDOUta6aKtyYT0bE_Er5_RLNXiksX3pySFeSqChNaS7hrN05QPTRxqo1xjyLH_szrXsd5ThiVqPUZnBiC3CWuN2LlEOSwQPFNb9jBQI_SmxOss-sOh7fqGs2-Azgy-Frp5Nty8gmPCCWCMudrn110RuO1BDjFRU-3BUGnU3CeyuveR5MyJqFkrJ6Ot-TqSuTHGRa69eTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDS87z58SkZuGsDNIgJxggtklZO3HnDKiU2GZAH6r9Yeg7kN3miO7bpeQB8ofQP57K44cMkSIozCzyn6SbKalkAUrESM9bcgll6FTxN6KZgsc-WA4zM1jPa_xLZaC47b9Dm-3FcUXsa3YnwRy_Bd5zw2jzXyFht6aNQRrgXvakKGGGI5K7vNVqDJjJq31DFLFm-2LE0UqSYmU8We5f69jDIXXXS_MTsteOIR-l4_Qh5OnO3gB5lw21nnryP6FKnyZ2HcB2pAHudpaP8jkhK5W3fMOva-xh9L50vMp876s74rH0GwuWbbGtz4Z_Aiom8WcmtZ_WhKfvcIaKjWvu882g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8tQodypWQABXAdc6dNfbHD29RuYPgcn38GPpwcWY6F7koCDQh-ojecgB6lUe8DeZzbnruolujJj51QrmnbX8ayKXsiyoZeirNnM7FdjsWoUc6TC-PJ7jMFLz04S64PgWK8VKgHEYGuUVv2XaIEK9wA6fDvJLTWDwokXwVNXYnVBaZcqSNcrhRXY1b5yskn6PT45smWDrIQyG70LdKzWbMx4DLOJIJm_VId4UFSATTsMsb9qwjzliHkr-9hUlTkG7B8PNo1eB1NN8TTvcbCi2DP8zqNNeRMjfCdLMel3Y3iacUkOsBKm0DjTabqeQTwhL3a5lt1MITDXd4LxJCiANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtKGWflHs8XYfQ7LjQqxo1xPJwhrbLeIBlbDk4PRMAUPwPPwojraXhJ6Jor5ZTZ4Z2jVY7sAtt-H5g9dbKdkXYoeLCXRikBBNEYD3k_LcXZPzLXnI34FE0AoJhVKFZ9y4n0r1qivRpK8SZ9rGiwDk9CVjrhI7p7ioxIgSE7fXkSBnJ55rMWsGLaPiz5t-iVGbNb_EOqgnvcTlVQPnBSyFPS6dfWzxQVNKFW0SUQbwG2A4lfzW9Oi5E2fliErFeQPfTc7tBs4_htozDH6bFQ8aoClL2D0ucAghLVA1jKjPxkP-2WbgthODhUgIJKwsLq9KSl8WZ_PNXB2wrGK711JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcEIqfJHMWF4_CXphnCKHtVRA887a_FuF6yakKZdfHFVRylNE6S6yISirDU3g9hsYMVcygWWxSLRsBOZ1s5TKiQYk4IJXkzQ-Hvbxh-iwD6RE3Yj6eRZISCEkJoT8ZcfjtgEJJ2VIGAKCoZVRjWVvJEC4HoejPjR-V-NmNbR9bzCidswXUJ1D2ZZSypZoIxzgisa7eb-t0ZcZQ98wViC-2kRiwO-QhhiJRr8Qelu5FcwjxMhVZZMkBYZAEb8k8ujUny6iNTaqsSRzjAAlPjCBFZK389iDl0_iifb_ng9Jthyc6AsPrBei3kSEgDHlxTEo0mtPUKYrqLqZGVMz_qH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5WydgEBwS2qpSFoxLzv_-Z07-GempMLezbLU5oRbzv4KMyyca2tHVmFWAP9yf1RGAsJxHmaDndZVkFS2UcVhgfvSDOenfny1nEe8DI1Prn3dlVH7qSEqUM4f0CPdlppsMkKAriaOQohA3XZhiZGXOfFCdRWpS4J21Ycejkok-DHNtREJCHLREH_tm0_uMHMxgohrKfzlS_jNp08iaSJkbCdMQmUL6GWFBfurqnmj0dCyGPN29I-mF4ZDzhnrfRVchSiK7ZTJSslh3vzCIG0yl7TRhrulY34DjfzCk6T9OahIpfdLIZrJn8Fmvvg8PbLkZPevDZXqdYoGXT8F4eFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNIKKv0L5J_OdUMbpbNLoGb6RDf2IKi6h4xERsXPNLJVdwglPfYMd7faILLOCiIjDSvF33ryU4Gwwa679dOTUdwI9Ei5FXZtVYJkFG7UYEtM2zkyNHGTzX_hZ1LHVxK8oVcIzEHJrqbruwWIMtqtv3f5jvjDR6WYwNUH5K_ImriYpr9YTs9G8MYw6aF3kmIelXs2agQamld-lsxON7xcCN8h2qaWeruYLtbJTmakh_I4gKp7BNAyTnQbX8kEuOJt6wATt0k0iBVCLr1AzeU9Bkca2aI7mGN02DqewtcpSpszg6DA8fnDRNRR1gfh6T-i94GIe_uYxjLljXhvvraPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_mctXGMubfa_Qyn2BixZadUIKEBFUX7uSoEAwdT8rYtR5h6DfqBhSY4YsRtySFv16TOqyARvZiZ5n_ggLPe4O6IJ7_Q_l1pFn5qYctGN1HQFQIiKWytJd2xaFPE3AxIBqgIbZtgQBe6_-e-CFeFaj_00rLJlTa7VeCubAwpbGEaTZDBU-i2XTGtCIfE7hAYDjYXll4UoX8Q8coW3y9JdnxtmVHkdNtqvNK_9nx3PKd-Q-dfCDLzMemlIrd_d51MnkyVUZS3bocfEDQwYlWg7lnTy-7v1E_gMQ09HO1IMHpDUYwANpjbmbt64g4DKZVh6gjTL_k2pMDOUVS2k2OJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOTB7IrhiZWeQIiQKKDHuFjY_8wet4GJ5RZOK5NDIgBIE21VcGjJvSuWE_R05U6e698Wp7DqnrdYikFs6xEjbdJvLxQAZ0c8MfWGC0ffKXZBvC3sMNHj51K0eiHlqbM1XR9UP8J_m3yocVWbulxWqRPXXKBFB3tX07RQFG8BzznbhF4xgnKr7Ys1VC3kX1FNn6iqwf9s-YpHKviSHZbwf_n_iJLacKvUcsrR5-z52iuZi1aTDUmj-RImP_25PmX6HJM1nkh16VG0TOCw6j5IE7AAOxe4QMUDVD78d5VhkSYyJF2gHngzwhXqm2WEw1q3fXunl7_P9Rc1BvonRyyoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrDu1x5HXpn_WoUARDG6EI005I1tZg_SxTUOQgsm98VHZdaPffZCkvUUKI0ytf-wDBRdV6gD28PgAnr3HJ47CbLd893MbSR_wDp1czzHB1q2MMa8nZM1UbSqk-L5DUoq0kZyTI1RExK9snaGRrNnbZYhuSTOrAQSfXg9Zh95h1fZcoqjZ6JivMqkPbNskEZywYmMXHO0HXKlPsyJXUjL1C5anMUGlUm-kHazbTPqtT64vOFXnK7KNpvOA42gvRV3687UST-6Cmf943Q8HHrlfakVAbcjDyJfSll7tY9hIx-fcr45IEM93yxdqrahu3DfKWQtEr_2jLM6bg-0R1u1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZxWlSt5FOtfSNT_oRcWk_nmWpmx8BNsJtAQ-FqEZWl_ygQVwC3BJ5fkD8C5tCGIipgJBx8sC0I_YS5sNv4kDP_3Lyg_H3ZG0f3udTGGmw2JG0Ce6h7AORE-PIRnalqIoFeoHql_LtH6DI3Yn5yZiT7SYpJYxizTiOf8GO0yaUfO0xlacQz4kzpiNN6A4hjtC1zCnDIdJxrrJNLVz80rmn7iMP4Agdz5Po-iV4UnIPxjjcI6k-S7xjwvn5VQRteCZDITY8KrlRM7xbvMDmEnTC5XSae1cEKyPoEYNu09i5y2xIBdiiWTA5d_2_bCUBl8RARVRJvj2FuQnEgIMrXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYL-zDQQztYzLLl-mTvB6xXltIT8B3xzc7sg8BoEdxSlQS40i-nc5TJ0vAzrw-5YF1P0XPZbVNr7mI3byaKLYIbbwcR84AX1GzP7qeVqnP_nMpGWpcLkmXY15LK-aieuhdybsOTj-Mrac1Se43XrK_S_qnmGIZBlZANBR7Wh2cPdtJyWRv5yw8llUa_Z94oY4LSyvIinujgl7bwDJDFwSXjmcVqRzvmL4EZrzLtWNlJtMkFEAOc53ecqpOpp8s2j1-unUo3c0alCpZh4292B4mZ6Ln1bxuBn75uVGxg5IgksqaG_Ys6JxJVvjF-nqSmHk_WTYVZqDjZvmdML23-Zcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=OldpqxDmkibwvNJyBNH3p6ULU5fpU2yMgOh1i268Cc-3Tgd-Bw4YXi8oa_cp5kAtkE5yK3-Q5SXMzVTRTbCA_YLR8KZ3tZZdY0bZAfb_sOeqYNxyYBC5IedLGiIF6LOJDO4LlnBldOUavQduv_X6E3VN7E7OapvxkVtZbX1_jzb1GJH2KGXljXL6iN5uTP_VRbMvaL6cbHVgVo1A3wMwosioz__dB9mL2IbioEusUUoXsEA1pwtUc0xBN7kwUFkRp6ty54d_sJrDNxGBGMsY0KzT90P7lDsOelY5hfdp9SC5yQ35Ti0doikxs_zC7bUAhe2fnwW6jBfqoFhib5j7GBIDbAfjZIoQDgboU6XRXu1oN25PwW3jFrqmq_yLZmsMX4-R5uyTKgxjz4ZjtZv_N1Y8kR0m5Bnst2mn2DEG_qbdwOCVnP6waf1a53NgRVzXH_hW5uUyNoVkqRFVtKm5HwRIpfupKFVT3uuUzKMQfG58hmoLbl8dOL3YIDzAs_uc2S6deT5kQE6YMKyr6Qq0v21IwokdOOHvAR-Iz6J5jO68KJuP5wrx0zAkDHvHnxrXHPKqbFcPmyVvg185KGHZhwNn_oDV2aD030Xgxj7saBsUUvplCxzQr1IbqWdwC_pO4gsHV1dOZa34ZEimAmwjUfInW9Xz9fdVv894QF9-9PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=OldpqxDmkibwvNJyBNH3p6ULU5fpU2yMgOh1i268Cc-3Tgd-Bw4YXi8oa_cp5kAtkE5yK3-Q5SXMzVTRTbCA_YLR8KZ3tZZdY0bZAfb_sOeqYNxyYBC5IedLGiIF6LOJDO4LlnBldOUavQduv_X6E3VN7E7OapvxkVtZbX1_jzb1GJH2KGXljXL6iN5uTP_VRbMvaL6cbHVgVo1A3wMwosioz__dB9mL2IbioEusUUoXsEA1pwtUc0xBN7kwUFkRp6ty54d_sJrDNxGBGMsY0KzT90P7lDsOelY5hfdp9SC5yQ35Ti0doikxs_zC7bUAhe2fnwW6jBfqoFhib5j7GBIDbAfjZIoQDgboU6XRXu1oN25PwW3jFrqmq_yLZmsMX4-R5uyTKgxjz4ZjtZv_N1Y8kR0m5Bnst2mn2DEG_qbdwOCVnP6waf1a53NgRVzXH_hW5uUyNoVkqRFVtKm5HwRIpfupKFVT3uuUzKMQfG58hmoLbl8dOL3YIDzAs_uc2S6deT5kQE6YMKyr6Qq0v21IwokdOOHvAR-Iz6J5jO68KJuP5wrx0zAkDHvHnxrXHPKqbFcPmyVvg185KGHZhwNn_oDV2aD030Xgxj7saBsUUvplCxzQr1IbqWdwC_pO4gsHV1dOZa34ZEimAmwjUfInW9Xz9fdVv894QF9-9PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbnRWO9838bLFSFFgUG7O5Xt3TBlXMxjVQ9tKA--Wpr_D9BR2ni04udxFq3ttEiJdbIDJFpYQbBu7KZDiHjhlIQomSp2lgwVbqQgx-47AssUXHuiif2SNikCBlx1ANlS_4VZyfhzj-MzMlgkWwDfBH5yR56_E7woe6QV1jYs4L-DaM-L69XxCNoNI9tY-c1MtnCpSTv9z6rI9hoy3sfeEmDcou5EaX0DCIO6cwIC8qSI9OU9rxg8IEPqgRE5cD6d3ux68g4GczmXO7uXZzXaUXZb_jX0YHvW9VOV8ep8mHASg2vczeTrhLt4mW1UwNtNBUFWZPlK-I4s2JWC10uoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=GmHtvdmfL239uTdVupAuKzeYWUqiWdhyiW6MggNMzThwxFY6OHBigPdFPN4QfDpL9abSGl3LXt-BdmmS87N8evw9_X_zMOSh1Mppo7YTO1NivvT-UmIjWC1JzGSaoQOnrYS4Qihe5vjjvVFEnX5oNfe6xfXcjbSYecWcfwSAQ6IlxQO83JP-jgdd6vqVnV2ITj19PnhDW_-tQhBkPQT9VVPw_i1Q5hOQ6iwRa0_cVED8W3qaiyUX3baR-KOPwpCKQwgQny2iTvWDN-W5_-4LSSFjEcCoBsYw44Z4egGYf9ADv88TjmffrJEzuf57cEyRHX4Gz_Hv2J7LCGW7stcYsHiZLvGBBAH0Cqv6_bpkYNlQGCdvkscZNSwGlnAIaiml12w3JT9aaEd1nTk7c3MQOU-tMNv7QQqL6Oy7AVaXKYPCFCJ0u9hzc9CJ5K_jX1ZHQG-v7UoMXgw1q-DJnpMT8EBtXvaxnxwcP_p8YRlOC2sYvgBt6QzFXXQyxHKaIIeW95tyNyUVhAvEnzbD7u4JPC6ExsJ1USyitY1sz_AUgBYNMvce9YjfahYR16TFdBNqsefbJknkAkPhfVmLeHLlrIFrvWkWrJ_2UmAHWt6N-uFI4ql3UPIOvK7P3h87BYTwl6aofs3E6Es78DkzuB_nJeLaEY8PXzNqutNfaANcBT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=GmHtvdmfL239uTdVupAuKzeYWUqiWdhyiW6MggNMzThwxFY6OHBigPdFPN4QfDpL9abSGl3LXt-BdmmS87N8evw9_X_zMOSh1Mppo7YTO1NivvT-UmIjWC1JzGSaoQOnrYS4Qihe5vjjvVFEnX5oNfe6xfXcjbSYecWcfwSAQ6IlxQO83JP-jgdd6vqVnV2ITj19PnhDW_-tQhBkPQT9VVPw_i1Q5hOQ6iwRa0_cVED8W3qaiyUX3baR-KOPwpCKQwgQny2iTvWDN-W5_-4LSSFjEcCoBsYw44Z4egGYf9ADv88TjmffrJEzuf57cEyRHX4Gz_Hv2J7LCGW7stcYsHiZLvGBBAH0Cqv6_bpkYNlQGCdvkscZNSwGlnAIaiml12w3JT9aaEd1nTk7c3MQOU-tMNv7QQqL6Oy7AVaXKYPCFCJ0u9hzc9CJ5K_jX1ZHQG-v7UoMXgw1q-DJnpMT8EBtXvaxnxwcP_p8YRlOC2sYvgBt6QzFXXQyxHKaIIeW95tyNyUVhAvEnzbD7u4JPC6ExsJ1USyitY1sz_AUgBYNMvce9YjfahYR16TFdBNqsefbJknkAkPhfVmLeHLlrIFrvWkWrJ_2UmAHWt6N-uFI4ql3UPIOvK7P3h87BYTwl6aofs3E6Es78DkzuB_nJeLaEY8PXzNqutNfaANcBT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct1R-TEbdrSM1KHupHN_VbdlaoDiwDpEkyJsSx92XoKNaxwlQml57-q4VrDMWfUBIANWaVM6rXceWttBfv7AXLirKHSQ5fY-7kL80UXpxmbOdB-o4uFqg73hKCzapoVpyFOHoswnECUgEjKN7ADWasqSxEp2YheQHvL3jYA8latzvDPS2oCzfJ-8y9Dqi2EsF_XivRnp3fyZnaTfvJh9BbmT_CpwvPmuecYe6tAVB3jm0meS4q3nIOWKgV1kDd3hmliY1MUpUjl8G3BeMhOillgjtIqgNATLbfcxgEmTV6M7hKMVP3gfFtDTL1NKzwZDAEkOJ_spJL9fN5iGQgYeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=Kt9pm5q32pZ9mdYPSAas7FjJXz9gZLRASKdG2YYpz-HZlIBYhs71Qrrn4PeOPzLVXsNUJeTZ9HEauxwrrYSQWziM5KsR0VU1IZ79hi3nSnFn7vXN8-NQUchKlqjCR8UMHscFcx3pyb17V3dPojh5yc76UF8VLTNXmyYemMrN0d2VQQhu7VKugqNWOu0kk72dH5hjcRbXYSf1TyiPSemAE9qseadKzvhaNm4Chc5pLhyM6COkMPE2OXLQ3al2G3GgCn8J_nv0ipXrQuHttp23fu7ESPsP0k_2Zyx83N9K0yCmFWbneOHZNjIbZxIYQ3lUwqKPBSG38XrHS6sob0sreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=Kt9pm5q32pZ9mdYPSAas7FjJXz9gZLRASKdG2YYpz-HZlIBYhs71Qrrn4PeOPzLVXsNUJeTZ9HEauxwrrYSQWziM5KsR0VU1IZ79hi3nSnFn7vXN8-NQUchKlqjCR8UMHscFcx3pyb17V3dPojh5yc76UF8VLTNXmyYemMrN0d2VQQhu7VKugqNWOu0kk72dH5hjcRbXYSf1TyiPSemAE9qseadKzvhaNm4Chc5pLhyM6COkMPE2OXLQ3al2G3GgCn8J_nv0ipXrQuHttp23fu7ESPsP0k_2Zyx83N9K0yCmFWbneOHZNjIbZxIYQ3lUwqKPBSG38XrHS6sob0sreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkrOj4NWByjID9v193J22OgET-JG_fcVkfOOb8lBiMvijxrAlMLVK_bpEdreXNk2HCIGJN8wW4eMZr-MkdPqDEvJNAPgXqUH2oQAfzHIOtATTL0fnuvityNvTq3qJREOvP2pK6VW0uWEbTVCPsYRFuWROpMIrBY2HmRVx97Eeav3ZuRKqgfMmaYmd5Kz6cupQEALYpg0-fM69fYRR17ybi7SBHa8LL1wj7YQ69S3BSfY08ghCea_bm79oYlmVc7pwPEUy2x1wllwV3mdpYStbbCQ_qTCIaaZDXQFkJ5YwI3av5fh2Lxz2Jdv-4Ev8TlfidMluFl2YY2CeV08TxWXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bth1khrkf-x8y6HuLaVT3QFG_bd65XWw0idu7aV2y4Jj9sKs8E0KLaXEtQmUVbdS_3vcVtTzOGiOPEWsEhg4aGAYLt1brETGuFNGgBCf4EX0F4NQ6VCObvdWkRpaLtdDRSb-9KYdJv3qCnP7hvGx17412swlT-WIXwgRUbPdaU1jQqs3UEKQNBhrsq48CCmln2-QayLkogL4znQXFqpVlVGXLOPlEjPIKENRrxPErKEhY6U8d4ioszcuVV1_kaP0nOBgojzgsIYZdnHyoV-u9csf05YP_pI4FOdHoBDAEF0CC0OS0vutRZ7k_NlliaO3uoLjiBfhzTKlom6tlOekHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi61XqXvABB-2_pIOup45s9tSHwNBZxeJOhl9O-ccMEbOomHd-JYc3Kc17VJkseILNfJrAleVrDG3cVepvuSVgEOAWD0IXW2I1cYsdcWd9pwdyGPCZ2S1zNNZ4K93t007qBOnbxDwER-6he9Cv9Ar66hz8AEmqSjdoyHa1tkxgTM4mE1eZ0vHa6_z9IJ7bgzzPZNlSlSo-MB7nhdkKzyxc4jtu-Q3doX1TnFZXqBayJqTk83lylhhaudFYTQGuX0AW8IsRh4rQYXpiA1qWEvHsFqdF1OZyaMxNj6YTZ85RaF01_EtuE1fB6AxiXFnC9x75OyWgcG0-U1GCJV_0Ddfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54Gpp1YjzZFHSQXeXxfeEgHCVFv-pA5FRUqMXxWpCwEILl22vD_SWX6Sr3mdnSr9BwMOQNo8mP6-QMzR5weqAuq_CDkYIhzGWLYKaFHFOFIoji7pts95XewDxghu0Sz1chzx7IN8bTxtMGvB9QcHS-O-6FVb6ncFZ4VcCSd301wb-S-Xd4yp9we_vTgbbXRcTMbGTGKQrxQZYSCJkD5BD6NGRDS4y5cIj4YGtJWgWa11RYB0cpZBXxcz3bTIUfZJDlZmf2FkXkjmEJKetHYK7PmZEjR_tt1f-VCC44ISpGuwN7B3BdCJoiMJnQVR-zYlogkkycTpUTwdZbnsiKTVvvClss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54Gpp1YjzZFHSQXeXxfeEgHCVFv-pA5FRUqMXxWpCwEILl22vD_SWX6Sr3mdnSr9BwMOQNo8mP6-QMzR5weqAuq_CDkYIhzGWLYKaFHFOFIoji7pts95XewDxghu0Sz1chzx7IN8bTxtMGvB9QcHS-O-6FVb6ncFZ4VcCSd301wb-S-Xd4yp9we_vTgbbXRcTMbGTGKQrxQZYSCJkD5BD6NGRDS4y5cIj4YGtJWgWa11RYB0cpZBXxcz3bTIUfZJDlZmf2FkXkjmEJKetHYK7PmZEjR_tt1f-VCC44ISpGuwN7B3BdCJoiMJnQVR-zYlogkkycTpUTwdZbnsiKTVvvClss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1ivgaItAjnRj81B62xkb7YOtUm_VVKnQiRoRwv6tCBY333NBpQdMPYrTozXXJapR29nPvM2LzHYi32hCgV3DD2Xp9zAzuR7B0A55zgUUaHaiHktjvfttwPJkiDvi_fYeWCKajpBVvRnWMWvtvbM-8mXRWdqafWQqZfzRqwCR8VxbUfKKD_ql7Dnm-nbMt7mIISu7nY7B9xyKO7_CZ8VQnf-cDyXko6bWE1ZcjI03c5d_Y-VWTWiKMzg04Sznt3nNtBuBlrFKrCakAIawGYcq0bxji6_eYPwem6cPuBffhrS-MjZN910ijoJisLbR5lUflsgT1Tkm8Q3mzKpQlO8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP5YBrDIYYEKxfPg__8Y1atfhsSwWUypIrIHx4xQknKATFg5JwNX5Qa4OvpiJsx381-T3-gp7aPLnqXbZjH2drbt_1-3_2Z0Cc5nNDZiLpB7VD1IKp8JKm9O-BEn6bP8TCZ3NpB-d2ROjQKUtBU7xTqbnlAjMSSixXKeuVqyBgWqcA8IYTUTs9z981yO0l6QOyo9ooNGEuLHXKnj-YCQk8Ro8hAorpcuyXitFOui4mVx8GMhZ-CJ6dR_v8P66dZnDDLuPvnvLrRE1SK2NJY2JJYhiBejVvjDRc7NJhIMtDh4caPXy-18ws_OX2kn-lI7vblef7tNKZXbgIKQhbpiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ngxu5IyczMmywPR6hhoyP0uFqVSKc8kcBSJzrMC6CpEVIV5No8HMnB88QTVWKOlr_Q5ujMNzDzV81IWXaWzolIS-aTbTwQgQVcsdvf4hwsoTVB2gCcwjiUKwEU8nt9iCbh0Qae42Uo7td_NoCDX9aKkOonMunH8vq6VnKzDA6N_Wfh3suQe_LRurulJQ3hqwGsAryPDm9GF-snOQgu99up3hhiLr9B7HvFiPprBUnUx6AxXS9VglumxTIm3CyzYVnLmRYWGE5J7hLhjaOCn29tJyi1DOjSXsQE28D8x-fCW38TnN-hNSXfqXfCZEuoQuZuMLx2NlJMoOIXWNiGu99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL0nEDaw8krsvZPBsLCkadkAhdMInuelVKxXJVJ_HAwh3TZcqAGmiKbWAy1J7PD9wMbVkj4HAWuqGdy1nstPkQl-SjfBneNrKBb7CyRHMMFNd-cXL_rk7-8wMumnkpYC0EY6MCJbO_NGOaQ6cPRnR-AfkO1qRim4n4YS1hHDJf068jXyiuW_ebljacb-SK_UJhkUAzPvrq217mWqClFlLeDznuSF_MfpoSw_XT00G3EleK3ubO10chIAtz7BlxguAgW73bF_UYgpc32JFoGUoPC9IgZHvKKXOLe1LZMOjI14nxMPxlJ7CeCLnKKw4f6pcDPLpgL5GthVm5Y05qbviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy2gf723pvABzPwqPGAJnhIZfFIlLADf-fFm0PeRfL35cluY-OWAbaAmoIiaEhtcPLpoERx77jBPTiTFNN5BWEU2kzkZBddQ1CDn1qkMefVVsS0qdlWfXml-NDJB3AwGTpqtV00iCQLGbmnGV1pUETgNRHx9yjVK63_40PgBqpHIISrdPI4wUJoIJdOA4fcNTQOirWky7Xv9DdAXbS7tbxEfXq95tKO-63jTwof9LG6uFAXdJl5R22sMVXIzKnGVJlPoVo45R6eBImECWxlCh6ffcb1xnErCoAOsAsdexAmoyaej4ZfnMvhmmpQ2_fI_Ccz3YBOP9dXL9K15hyxjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=REPl_L9xZxkACKe7QUHmcjRQQuJaTaFZEkmCFiIloMKtHLIr_MpGzeeQkhdH3qH0Mg2-C0ve8dFFWSL0reJZb9x0WwnYU2HWdawBnTQicxgRq2zscmnizkhowzzMc4Ygw9_zkyaH7Ld8edIuT8HD3DV5OdvkK8Nml6h3zDrd8ykxqsMVIFhHI5fWFAUVJusSlEPs5VR3461Hh_PV27GRwVDc9wd1PLpCwWqgrrW0eduWXjDK4Aqmhge2ZiDE61KjjBvn26uPnYtnZSvSPQwl3O4zSJyInN-3Bj7kjlV1u4160ouK8BTUwQ-zbnyS__3Qqg--kjI19DaLTN-5lsuIzWZIU_13aFqqj2-dj74sOvqX8gP7k-HL6rYIZA0aamuS_u7X8kjy6Ys8z0uYVM0qiwNUDxI2dTOk4LRluSlbWtzY2vEGDQwOudzPrbgl59A3pJbGduvRKvjkXje_Cfw2U6HF1yCGmkKXWx4invGaN_FZoBOXvmWE2a6J5cExhB5NFiDNWGCt-PR-K-WFMqfjOy6Gj0Ci-MJoNQE9Yr27sLB69T8UxgIKrm6D6Bd1VYz9F8s0dOc5JbbclOx3E4BsKpleSJFJy2TiMTDrcnP3WqGZE_bJYDliDtf1bXlffkWG3Ebyln4tq5Xbmvj2U_cVSbYA6yPPXTWraRsjflWK1xI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=REPl_L9xZxkACKe7QUHmcjRQQuJaTaFZEkmCFiIloMKtHLIr_MpGzeeQkhdH3qH0Mg2-C0ve8dFFWSL0reJZb9x0WwnYU2HWdawBnTQicxgRq2zscmnizkhowzzMc4Ygw9_zkyaH7Ld8edIuT8HD3DV5OdvkK8Nml6h3zDrd8ykxqsMVIFhHI5fWFAUVJusSlEPs5VR3461Hh_PV27GRwVDc9wd1PLpCwWqgrrW0eduWXjDK4Aqmhge2ZiDE61KjjBvn26uPnYtnZSvSPQwl3O4zSJyInN-3Bj7kjlV1u4160ouK8BTUwQ-zbnyS__3Qqg--kjI19DaLTN-5lsuIzWZIU_13aFqqj2-dj74sOvqX8gP7k-HL6rYIZA0aamuS_u7X8kjy6Ys8z0uYVM0qiwNUDxI2dTOk4LRluSlbWtzY2vEGDQwOudzPrbgl59A3pJbGduvRKvjkXje_Cfw2U6HF1yCGmkKXWx4invGaN_FZoBOXvmWE2a6J5cExhB5NFiDNWGCt-PR-K-WFMqfjOy6Gj0Ci-MJoNQE9Yr27sLB69T8UxgIKrm6D6Bd1VYz9F8s0dOc5JbbclOx3E4BsKpleSJFJy2TiMTDrcnP3WqGZE_bJYDliDtf1bXlffkWG3Ebyln4tq5Xbmvj2U_cVSbYA6yPPXTWraRsjflWK1xI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOxMNBcEQsv71LHQZyDASxVRF_DoAmVOeadZXAit_380gOgMZ1I9n7vdgLn_N79Y3by1hFxzBA7YX5L85pegG0iXh6YM73ktvFQfug5SIPgHcgapLEgD-nBHkoBw7eO9EXXe1m18dVdxMGotDeZ_IoKPCvPEpNEE460WBjV1rm2cmZsQJQMuZHw0PcTbzFgWl3Sx340D36JGP-FTruMs3k0kkMzDtPLH4SJhBvfqz68R05LvXfJ7j3ERQX-gQCInFmQGz2Bte1VsVedkdfbKwFKgBJNHFVHpjsgL2_GngKnZ0x70JIwoEu0oMT3ZGjBz7IDoyZ6PPH1CuYvJ9bx4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uptJHkiT-uHXgFUVOkNlQLFjO5pvxyhdbTkj0qbb6lhuOP0IOI85KXVtpLnfdh6gdOfkQcXSQ4H5zYAD1v4OOHFbh-F_JwlAK9E8lMd43E_uzdtsrotwI0SwisC23wkivDy0C67p96xLExji-0w4IqEQfLIxI6MmidnhFESRv-VmhbMU6R3RfDt1rbMpB0LbKNSolX0S74rI18UliUG4atdpmT6jeE3qYZ92_gyPnrh26jnCiI6YkaRMVogfIf8zZaor6DyzvWtE0CeF9dm0sUPIG_FUXn3xsVqkmoSPpPSCqKHTAtaectVP1UTFeuaQWRnSTObRJaPXl1s_KzQp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFSH-_H1k_0Yrqj0etdx_GaX6FaVWyHbL4N0Qt5adLnwpcpnlYbqsSP3PXWVN5Rwu-tYveEcVa7s52AvboRsdyyZbCNxZ0G8Ml7AVKFX_G8yH1vPAFLYrB9S2oUQWVozb2_ySlA9-ho8gADROvCWLnb0sqXjirP9faW8JoxDyyEcy6dOOFlLlb2Zh_sEJ51cvUxxwA6xu0mT5J3MMS9dvUBW0Yg9M_uTgZX2zsRVUR7PjgC50JRbpkagvfUura3R3VzfDeQAjZw8P0rGNrTjHcPy-brgquXZqYw846-Mz0O4V6W_iX2oB6EDHiUTzn5DQTPVkuAEX4jqS91JxNbBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان  مدیرکل مدیریت بحران استانداری اصفهان:  از ساعت ۹:۳۰ صبح امروز عملیات کنترل‌شده معدوم‌سازی مهمات عمل‌نکرده متعلق به جنگ رمضان توسط تیم‌های فنی و تخصصی ذی‌ربط آغاز شده است.  محدوده اجرای این انهدام کنترل‌شده، مناطق…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19223" target="_blank">📅 10:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19222" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع اسراییلی:   بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.  تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19221" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر این خبر درست باشد و اهداف نظامی ایران توسط کویت و بحرین که ضعیفترین ارتشهای عربی منطقه هستند هدف قرار گرفته باشند، یعنی اینکه عربهای جنوب خلیج فارس با راحتی بیشتری می‌توانند تاسیسات زیربنایی و غیرنظامی ایران را نابود کنند و اگر تا کنون چنین نکرده اند ناشی…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19220" target="_blank">📅 10:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">استانداری گیلان اعلام کرد   صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19219" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند  به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19218" target="_blank">📅 09:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19217" target="_blank">📅 09:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19216" target="_blank">📅 09:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19215" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

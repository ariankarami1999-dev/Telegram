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
<img src="https://cdn4.telesco.pe/file/mswG9WrXWmyTnlM6inCcPUKERp5ISVy92UpEIGokcO7d9ep0KC2Bv11jJR6yxU_ahekZsIwnuek-wTbXb7JdQ2pG9eSluC8jf6ruPfLvJuKTcb_bjPfjE5FTkaUgj-M18QKmfglEOfbMEzcj_9pNuq7MhCOVj4uDfd2VMmcXhOTxHslKBmsmWGKFhDQ-XriC864glkL8FNu-5bnMVJneGSY7Rrz8evabqStrRSaKLfGzlgxpj26BxFxDjyHEVqcY_ZPgqguK6lUhi-IE57oXsgvkq1-vC7h9p8a66zfna5byc7f6sf0_pMGkyEhqYTVq5p2eju-m3f9dy1Z64W4-Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-663839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
آخرین بازی دانش آموزان مدرسه شجره طیبه میناب؛ روز حادثه (۹ اسفند ۱۴۰۴)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/663839" target="_blank">📅 12:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا پاسخ داد  روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله قاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔹
به دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان،…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/663838" target="_blank">📅 12:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663837">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P26xGBWf7PBEhJQGLY9KTa_m1-Vm0vzAD0TM6FYBr6vrKR72yw66IuefuGvXYcgdScs2xdylVDQJ1xDgHSkIN395Ig8e_IbHsPJFK3PnFZL6VxSzi7MU0T4VKA0y-eYpQUQIdCfO0Vbw4aOsTfKSGY3lCMoPIaf6pSI2h4zAFlzm-zOfxFj4iU92TlqCCKYoCbtp-le7u-nP4LC50ljrNbEnvCcoRY2A9kjDvPGGIxGHwzG8JEN_3xQMpWcKxwQrJ4qeVKfjAZ4OWJi5a2C6TahJD-3SbO_KYp6X7R9XqfkzcjHpiL7njRAIOeWHDfy5tPGTn6PTKbuPZffgAf0NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاد هیکی درباره بازی امروز: انگار همان داستان جنگ است؛ هرچه دشمن بیشتر به روش‌های ناپسند متوسل می‌شود، ایران سربلندتر و استوارتر می‌ایستد
فعال حقوق بشر ایرلندی:
🔹
دومین گل مردود واقعا افتضاح بود و به‌ هیچ‌ وجه قابل قبول نیست. با تیم ایران طوری رفتار می‌شود که انگار مجرم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/663837" target="_blank">📅 12:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XARTQ-INzjIqMW-d_Y61IVgVj682ILCd7Ry-yNcxTwrQSRb6fskcSfHI6xos_BKSrrkzk9Aer2GbyliD81vGxG68w9Dpn4bFMvHbHo3bsd_eIPk-vcU88tMCcqotdxROng-aDa2ZiHLblqYGKZ-BZoiLf9oKgNch6ZqEbcy-JHU9Brvv0lmbhI1SQ5vG8XeMh5OhXmqiD5zr1agtazkj5RdvN_zKRD48ksDoXvuWg9mluH9hHKwa0ljIi1kbjSPpjqTyF935aNEF36tUYAmoyRM8VSmintcXWK0NOrWragxlxuXwpIe9CxRI876gESMrMjKn1_atHGgHVG-Sl1JuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMxk-Gfm2jyUu-e0zcsANddOwA_BxHXZZEQq4vSvnLWACUNfMCngVPgHT-HAW-0cnzo-GSSvJe0iEm05Qh9E1hahChTH8SqbtXSBEaLhvFSheVb7rkzgtQ4vqb0sfjO0yapMYgtDn6s58r-b9AOMXooGBFbLFBlrdEPUVhO5WyXgqPaVxRAOPn8q0fajYHDPegKPMWkK4jgsCvEkzEu3GH4hkTKT_9VHoXUJUpzizmMFuSKlShOYT-SOeyAqkcT87X-ZsCfDIhSyqB-6RpPNZyLb8jySorTIC4i_g9FowziLqQDcd0Lm9SzM8QTW9P9EdneOav4mLRN9AyDb52YWfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گل دوم تیم ملی چگونه آفساید شد؟
🔹
دروازه‌بان مصر از دروازه خارج شده و‌ جلوتر از شجاع خلیل‌زاده قرار دارد که در چنین شرایطی، مدافع آخر، به عنوان دروازه‌بان در نظر گرفته می‌شود.
🔹
خلیل‌زاده در زمان ضربه چند سانتی‌متر از دیگر مدافع مصر جلوتر است و همین باعث شد گل او آفساید اعلام شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/663835" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgSa_Qqmx3al7PL36vKXkqYpxMLhtKuFM0YcSdyqwhe2PiWfKTNCvshjV_kpJNuYl_10-9i0fG4Htk4BqXB2a6eijt-EU2mPwh7inrt196-Q_xRtY_L2gxRIrYPOar8azwb5lfuEB3P--jr3pInqy7PhrRlA3r3boK1f69d6Djoh-5O335JUUsTUGfGJGOObaTCnByp8HhUAMgsrsqSRTZiDluDM8RgjHNTTQzrKBw5zMij9DhFAMot9fY3FePg3amQgZIGm0bpcPivo2z2LEv1INtnR2UiYYka5DxdhuIwTp3fbF2k71T_uHzqk1cqVA54JT3JwzURRpNtj0lOkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور در کمتر از ۶۰ ثانیه فریب می‌خوریم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/663834" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd53596d48.mp4?token=aupJlPMlNuLgRJRsH767sVwrb4p3nY7eAJGY-PJ4rni1RSKhWRZ3PoNu61aT3nTYY5gTHrbaUdERaS7uKfAXvMOVw64iwLoUkJlZZiatTzmViUlXSrN3CxQqz8oaYEJ6TNoRgsa5J49VzSBuurNclnCXRfrWk6iuD36-1dBARIptgEjV5j7QHFT0aK5CSOdcU6LENxxwMxwxuGP6a_fCkpuq9oGUkdB1F9Mpfp21ndJt57DE9YmKp71NBKYUFhtLg0ZlsvuxWN0r2nOrp4axIEdy6aAnGvn4OiR10wIEDgSfMtQaeVAlAOUdM8pz80FcQoYhxYZ9ZdbereQZWcu7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd53596d48.mp4?token=aupJlPMlNuLgRJRsH767sVwrb4p3nY7eAJGY-PJ4rni1RSKhWRZ3PoNu61aT3nTYY5gTHrbaUdERaS7uKfAXvMOVw64iwLoUkJlZZiatTzmViUlXSrN3CxQqz8oaYEJ6TNoRgsa5J49VzSBuurNclnCXRfrWk6iuD36-1dBARIptgEjV5j7QHFT0aK5CSOdcU6LENxxwMxwxuGP6a_fCkpuq9oGUkdB1F9Mpfp21ndJt57DE9YmKp71NBKYUFhtLg0ZlsvuxWN0r2nOrp4axIEdy6aAnGvn4OiR10wIEDgSfMtQaeVAlAOUdM8pz80FcQoYhxYZ9ZdbereQZWcu7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
روشنایی زیباترین بافته ماست که از خانه‌ای به خانه‌ای دیگر جاریست
⭐️
در مدار این همدلی، فرصت درخشش برای همه فراهم می‌شود؛ از اروند تا خزر این جاده نور پیوسته باقی می‌ماند.
🤝
تار و پود این عظمت به دست ماست، برای تداوم تپش زندگی، ۲۵ درجه قرار همدلی ماست
✅️
همیار ما باشید
ba25.ir
#پویش_۲۵درجه_قرار_همدلی
#هفته_مدیریت_مصرف_برق
|
#شرکت_توانیر
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/663833" target="_blank">📅 12:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/663832" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb908d1e4.mp4?token=bOmlk21x12UDdXeEHfnEkEvu63VEk_YmPDLViZRiBf8G3WraFIiezixmvrpMLlMIUStpSf0LkgRfreMHkcVVzy7HEN_E-T8iz42s-u3ySVi3-byDKCtGCXpgN7-dKWcq7cdqANsW3uW8g6XoTlS2OgMDkR-V_YgxJnsuOjTi0vKBoGXjOGqZ84_YXtlfv8vRBVcLD2ckMY5QNAidEsUvFHXHEMcpeAe00doeQxGG-Yqa0jDNIAsiS1RJTsA6U0k_3rlm-z6MNyla8nobLcneP4OwfvgL9fYXPBBMCFD2uXwnVKP9wz-DFH_azoCcR337E0M0iUgCoembLUn84kdYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb908d1e4.mp4?token=bOmlk21x12UDdXeEHfnEkEvu63VEk_YmPDLViZRiBf8G3WraFIiezixmvrpMLlMIUStpSf0LkgRfreMHkcVVzy7HEN_E-T8iz42s-u3ySVi3-byDKCtGCXpgN7-dKWcq7cdqANsW3uW8g6XoTlS2OgMDkR-V_YgxJnsuOjTi0vKBoGXjOGqZ84_YXtlfv8vRBVcLD2ckMY5QNAidEsUvFHXHEMcpeAe00doeQxGG-Yqa0jDNIAsiS1RJTsA6U0k_3rlm-z6MNyla8nobLcneP4OwfvgL9fYXPBBMCFD2uXwnVKP9wz-DFH_azoCcR337E0M0iUgCoembLUn84kdYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر خوب برای دانشجویان، هوش مصنوعی به دنیای خودکارها رسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/663831" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرگزاری رویترز: کمپ مخالفان کرد ضد ایران در شرق اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/663830" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a430385722.mp4?token=o0cuf-8uG5Pjc10mlL7RX3PKoX_K7VXJjuIbBXuR0I6djPE5JgvlhBC_UDV4KLsB2tLfnDZB4ZdFUA9_us2MGEGy6bBVuKDGlx2defnJXTi4kSSk3B32N16Ve4ARQj4usBkdPLBRBX6AsoThx-l2sFXcQLOju08Zztx7CygVO_WT7LXxd-bD6r_EAPffwaoSl5OYP7j3pFnxFnzhw4LDoKKeIHws1hmUnTvHS4PDeWCvZZXs0KPuMbKOCEwi9cSmm_vpQHEqLQHMrspYXwySggZBpish6Q4UnV2qGb1rxPRjuG58QffxzYs6ksPdxHgCvO3zjvLlxxch-18OQQdAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a430385722.mp4?token=o0cuf-8uG5Pjc10mlL7RX3PKoX_K7VXJjuIbBXuR0I6djPE5JgvlhBC_UDV4KLsB2tLfnDZB4ZdFUA9_us2MGEGy6bBVuKDGlx2defnJXTi4kSSk3B32N16Ve4ARQj4usBkdPLBRBX6AsoThx-l2sFXcQLOju08Zztx7CygVO_WT7LXxd-bD6r_EAPffwaoSl5OYP7j3pFnxFnzhw4LDoKKeIHws1hmUnTvHS4PDeWCvZZXs0KPuMbKOCEwi9cSmm_vpQHEqLQHMrspYXwySggZBpish6Q4UnV2qGb1rxPRjuG58QffxzYs6ksPdxHgCvO3zjvLlxxch-18OQQdAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویرسازی لحظه گل آفساید ایران در لحظات پایانی برای علیرضا باباجانی‌پور هوادار روشن‌دل تیم ملی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663829" target="_blank">📅 12:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حکم بدوی اخراج دانشجوی دانشگاه امیرکبیر به‌دلیل اهانت به پرچم ایران صادر شد
🔹
در پی بررسی پرونده دانشجویان متخلف در تجمعات غیرقانونی دانشگاه امیرکبیر، کمیتهٔ انضباطی این دانشگاه در حکمی بدوی حکم اخراج یکی از دانشجویان را به‌دلیل اهانت به پرچم جمهوری اسلامی ایران از دانشگاه صادر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/663828" target="_blank">📅 12:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ7jYOiIsRWyeuYy-uRtGcTNPyuaMPK82IHQiabpkLFgKpS9Fpq1lSNtOrbvX4iJYzXYJPfOzB0imzwmPwVpWLYaFu1cksjJRv8bowDMv_btwJBlTNnO2GE_v-_X1DPXXi8prYVgVL6b4uA3Gk8OKJhDEYL-Il3VnQ4ifWC58Hs_8TCI3GEYnc0JRVJ5kQwCQeke-wAoNv5MWQaqKBNiz7Vru_qrhA5Gn4J858XUScbTV6A3BZ0xJKvf82bAeI5WCUb-tpg7l4F8taQQVrANQz1TdVK_raUcSZ9ZvjuduCKIZqdkx1bMf1N0h-n-Bp1q1fX45ZWnkZqLKHV1SwlWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیشرت جالب هوادار ایرانی
🔹
این هوادار ایرانی در آمریکا با تیشرتی که پیام«طرف درست تاریخ رو انتخاب کن» و هشتگ ۱۶۸ روی آن نقش بسته بود، سوژه شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/663827" target="_blank">📅 11:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGVCMxxDcxw7bsQ5qiF98_kXxT36QD5XAr50_xDnbJA0WiC33-1vJ2UtuuvIHXsLGxz2eSiJlRFKX21iN7GBVo6xZGXe4lvDx4BJo07TX3A3O7BN1tOCkYvXt3ektJIy-XN2rBS5MONt6ZpWsIpzEf1s57FPAKKlAzFlnkPELnIdTdJm4jpXT_WwHZmTNoBaQsilQPNR11gFO074bKthn8URuyF-8hk4Net0D6X0F6P0aiymG21qIKWheOymlgFLtqDPpXNxFiM4IcYqQyowiVdQn3QKHdXyDUuQdPVBfvVAYaPIGXsJgKHBqOuVdKdLEYy7YsmFvtQDWgemBhpqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلید صعود ایران در دستان این مرد است | آیا کی‌روش دوباره قهرمان ایران می‌شود؟
🔹
فوتبال دنیای غریبی است، حالا با توجه به نتایج به دست آمده و رده بندی تیم‌های سوم یکی از کلیدهای صعود تیم ملی فوتبال ایران برای اولین بار به مرحله حذفی در دستان مردی است که سالها سرمربی تیم ملی فوتبال ایران بود؛ کارلوس کی‌روش.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3225973</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663826" target="_blank">📅 11:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سفر آیفون از ۲۰۰۷ تا ۲۰۲۶؛ داستان انقلابی که هنوز ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/663825" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ee4ddf11.mp4?token=FgjcqB4DyDBXEZYyiVimIPZG8XnQieorUP5-7Xtd7hxfY9hQQw9MB95y2tPzmWh7iNeHjfksENdPHQmPUFSya1Enyd2hmBWXJGa9H6Zg_A2iIBZzSmymEfUszhUAKtayryOZO1q1Vt2SoAmYBSZ4fnrLhqR079sHkvlwQBMtGNZMMfJMSRybop3PlVwnfn4trHR5GGelEUG7z0AY3Ayl0dWPvq9TOiI3IvTMtq9lqphvGnxn6MKa5C1i7muU12KZxNb7AtesvbTOO-UixvPteDWM_E6pT_ySRnv_OrTw1cIvFBv5Lt7qIb6oi_gztjppcP1-f6jTXHlLkK_VR48lZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ee4ddf11.mp4?token=FgjcqB4DyDBXEZYyiVimIPZG8XnQieorUP5-7Xtd7hxfY9hQQw9MB95y2tPzmWh7iNeHjfksENdPHQmPUFSya1Enyd2hmBWXJGa9H6Zg_A2iIBZzSmymEfUszhUAKtayryOZO1q1Vt2SoAmYBSZ4fnrLhqR079sHkvlwQBMtGNZMMfJMSRybop3PlVwnfn4trHR5GGelEUG7z0AY3Ayl0dWPvq9TOiI3IvTMtq9lqphvGnxn6MKa5C1i7muU12KZxNb7AtesvbTOO-UixvPteDWM_E6pT_ySRnv_OrTw1cIvFBv5Lt7qIb6oi_gztjppcP1-f6jTXHlLkK_VR48lZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی که مادر شهید ماکان نصیری برای بازیکنان تیم ملی ارسال کرد
🔹
ماکان من برای مدرسه از خانه رفت اما هیچ وقت برنگشت.
🔹
دعا می‌کنم شما با عزت و سربلندی برای ایران بازی کنید و موفق باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/663824" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c42893670.mp4?token=umqv8CvjVIA_TvhIve9pXNN0KGiDapzBrqvRGWKUNUGW5jW7_6ux3-kEKE-0fpAtM-BpPJZKG9rf0oMK6RclH1tmitR6Hv4kTtploLXGMyOcCAGghglRZZ_hZGP1QLpzbSK0r_CvNHggS-C1cFevSSrtj_1i6S5kZuLzrs24XW6j6aFMsf-ZNM3BATzFP_1Ryjg4uFACy-_M2CezHdss63tM1iNwBLwd5MWWNB4L8XlINJK-c4HU975KDU1MCGqYjIaxPAOVrXgVeHTmrVDIsmm60-lM79d3Spm8rtm34kSfCe4D8MEG7Jk9LPLGyegXpJk1ZkfmZpK_yrxjRIDiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c42893670.mp4?token=umqv8CvjVIA_TvhIve9pXNN0KGiDapzBrqvRGWKUNUGW5jW7_6ux3-kEKE-0fpAtM-BpPJZKG9rf0oMK6RclH1tmitR6Hv4kTtploLXGMyOcCAGghglRZZ_hZGP1QLpzbSK0r_CvNHggS-C1cFevSSrtj_1i6S5kZuLzrs24XW6j6aFMsf-ZNM3BATzFP_1Ryjg4uFACy-_M2CezHdss63tM1iNwBLwd5MWWNB4L8XlINJK-c4HU975KDU1MCGqYjIaxPAOVrXgVeHTmrVDIsmm60-lM79d3Spm8rtm34kSfCe4D8MEG7Jk9LPLGyegXpJk1ZkfmZpK_yrxjRIDiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جورج فلویدِ جدید؟ مرگ زندانی سیاه‌پوست در زندان کانتیکت
🔹
تصاویر تازه منتشر شده نشان می‌دهد «جی‌الِن جونز» در جریان مهار خشن مأموران زندان کانتیکت جان باخته است؛ حادثه‌ای که بسیاری آن را با مرگ جورج فلوید مقایسه می‌کنند که جریانی عظیم را با عنوان جان سیاهان مهم است در جهان برانگیخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/663823" target="_blank">📅 11:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
صحن علنی مجلس، هفته پس از تشییع پیکر مطهر رهبر شهید انقلاب برگزار می‌شود
گودرزی، سخنگوی هیأت رئیسه مجلس:
🔹
در جلسه صبح امروز هیأت رئیسه مجلس با حضور رئیس و سایر اعضا مقرر شد هفته پس از تشییع پیکر مطهر رهبر شهید انقلاب، مجلس شورای اسلامی ان‌شاءالله رسماً تشکیل جلسه بدهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663822" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663821">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIrv0XLV7VAZNw1UqZ7ou5qKT8Nn4ulKdkOzBX29VJdxdXaS9P0QlWz3tsH_LB2Gx_2YH1tmwBzo51EXMpBMZC1zSv2UlAt0btzFb0BtRApwP1yggJakQX94rXGIHxWVMWxYbVvyC_k8BkdWlEnT-HCtcG5tyEE8L1aoNTK3m4vmhFFJi-op5oZ2VwCYrEGlTt8Q4t6AhHqpa3oplMnRYjn4DXeKksBUupCIzP0FjzjKXuC87jmTrjzulVb7vCSEEFJqdq6QyQv0Q96cA5oCM5U7dJo-awPhe_8knBdScxlIuxIvpoa-QvaKIX9TdOpuJBKTLWm0or2MgPw02gQ0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست جدید شجاع خلیل زاده: «شاید خیر باشد و تو ندانی به حکمتش دل بسپار...»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663821" target="_blank">📅 11:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
صادقی، معاون قوه قضائیه: در حقوق عمومی و از نظر شرعی، منعی وجود ندارد که زنان موتورسواری کنند
🔹
دغدغه خدشه‌دار شدن حجاب هم صرفاً به موتورسواری مربوط نمی‌شود و در هر جایی ممکن‌است که رخ دهد. اگر مجلس قانون گواهینامه موتور را برای بانوان تصویب کند، قوه قضائیه هم موافق‌ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663820" target="_blank">📅 11:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_bXCXeXXUqfuQ1ozVmvr7kHB-DrRs1J3KcJBcLc_xh_wBWfZzxVg5iP0SCfhhkJDuw-aLkpmYnLJS8y44IA4ZbqC46oB8vfOMhRyXikaYqR_29SiNIVFerZNxrXjUyaat-bWYl0hSZ00uR0joJqiCgYx41fRacNBzK4RpGTiAoPOuASmTIJIgRoyMSiF28twdLoQTu8WSPORLPHVN8a4Qk2nnXlTQWolWOGTaKG4bsOFYSkyMDbZ5QUBeUFty8HxdJu43JXLVSMPSaCzYCRGPKiHvCcbc-PqZRX-_Oze4qA0W2H34VjJ2WUJfmnnLn4ON-SOmrZNTibfU5OHDjqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف بولتون ترامپ را شاکی کرد؛ او بسیار احمق، نامتعادل و دیوانه است
ترامپ:
🔹
جان بولتون، نماینده سابق بسیار احمق، نامتعادل و بی‌مهارت ایالات متحده آمریکا، به تازگی به گناهکاری اعتراف کرده است!
🔹
اودیوانه‌ای است که فقط می‌خواست دردسر و جنگ به راه بیندازد و باید با او برخورد شود.
🔹
بولتون اقرار کرده بود که از اسناد محرمانه نگهداری غیرقانونی می‌کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/663819" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
۸ کشته بر اثر عملیات ارتش پاکستان علیه افراد مسلح در بلوچستان
🔹
بر اساس بیانیه این ارتش، عملیات نخست در خاران و در پی شناسایی یک گروه مسلح انجام شد که طی آن سه فرد مسلح از پا درآمدند.
🔹
عملیات دوم نیز در مستونگ و با هدف مقابله با یک حمله انتحاری احتمالی انجام شد که در جریان آن پنج فرد مسلح، از جمله یک مهاجم انتحاری، کشته شدند.
🔹
در این بیانیه همچنین از کشف سلاح، مهمات و مواد انفجاری خبر داده شده و تأکید شده است عملیات پاک‌سازی در مناطق یادشده ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/663818" target="_blank">📅 11:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEOxww9zQxg7uTxOmnc54qVU81NGCd91ktGLsyiCMZ5oER-4uHeUI1w1jIpgEVO60GyNfKl52QXDyVtMqwuqbjpPfGiAYGQD8OPSOQhLlvj1jDjpP5qVTxUXhM_IhNXvn7PZHUdz3t3K4x8w0IOheombYYMrDq1bmzhoZNmfbSE91Iz2EIDdt4mXPD-TLMFsTIFT6NHmaYqTQKzlWtxv_x3iNaiTN5rjAW5M3B26lqpKKJuyQu2GS-2FXBnL-JjsmdbOJs0sMICJHX5b4E1SjVwww6xuEIuBbtWdCa9TrE8GziVDZMlQjgSo5EwY9ygGxJnoRULYLPJ4cHaWLTg4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تیم ایران از رختکن سیاتل به دنیای فوتبال برای اجرای FAIR PLAY
🔹
از ایران آمده‌ایم… از سرزمینی که هزاران سال، شرافت را بالاتر از پیروزی دانسته است. برای ما، فوتبال فقط رقابت برای نتیجه نیست؛ آزمونی است برای شخصیت.
🔹
شاید بتوان با هر راهی امتیاز گرفت، اما احترام را نه. شاید بتوان از یک گروه صعود کرد، اما از قضاوت تاریخ، تنها با جوانمردی می‌توان سربلند عبور کرد.Fair Play یک بند از قوانین فوتبال نیست؛ روح فوتبال است.
🔹
سپاس، سیاتل… برای مهمان‌نوازی‌ات و سپاس از همه ایرانیان… که قلب، صدا و تمام وجودشان را برای ایران به میدان آوردند.
ایران، همیشه سربلند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663817" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxvqVigDgv9XFRDvV_2Cf5_2lp-dLN1LBK6AKoMcvB6r-oXggqpNJsh0plzGXSoYh6MbKoiB8RVk_micFz19apyPe5UBGJ1eZrI2ndYZIYhHbER3hTWMsoP0s9Rs6lwLXBnPnGNyo6wfnDYodCbPDNlsUX2GB4R3lOln5k-128EqJuSvxKJPBKlN0WeiV2uyP7BvXIlNUtNyQtNpyADRCIdw3CHDjAJKhIpmsptnrpuIvm-tyI_0Dv5FLsW3oEy7FcDdkKKXEx5z8mdZdRrRExbaTceNb7--W_yTIwjNONRK0QcqTNAy9GHrDtrKRx-oF5e7SXbzJLwfw1FqOU8OrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: بعد از حمله دیشب، هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/663816" target="_blank">📅 11:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فراجا: آخرین فرصت بهره‌مندی از معافیت سه فرزندی و بیشتر تا پایان شهریور
🔹
آبونمان ماهانه تلفن ثابت ۴۵ درصد افزایش یافت
🔹
تمام خدمات حمل‌ونقل عمومی تهران در مراسم تشییع رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/663815" target="_blank">📅 11:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtqn1oUTjX2wIt6a7LbM-Yzcdd49YOq5xKxspuYThq3Q5u0QwDzeoThAVfjr9rqPL6X9AimnonXRX_NlF78doFRcVTIWA8sqnE7DNakZrY3ToedY1Nui4isg0uonik-LZ7nlvaA1XQCxbxuZzXbM8EMEntSkGtwqYxY6nJmH7WzZNE09HwqfrLDrhOdkx4NViE6_GR1PR82EjQSZf5IMx1OKlaDOeag0HLZVq5CJ9-WNn0xzo4FrdyUGxGYON8WItZqE_5pJBssOt3UyXkUdxiuIqzNKMCEJD5cP8wvxLDKUcY13dQFEU-3UFcdbOH_OH9GJe0B6KMcWf0v0nW5sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از قاب تلویزیون تا جام جهانی ۲۰۲۶؛ نبردی که واقعی شد
🔹
سال‌ها پیش، در انیمیشن «فوتبالیست‌ها»، تقابل ژاپن و برزیل فقط یک کارتون بود؛ جایی که سوباسا و یارانش مقابل غول‌های فوتبال جهان می‌ایستادند و میلیون‌ها نفر با هیجان آن را تماشا می‌کردند. حالا در جام جهانی ۲۰۲۶، این رؤیا روی چمن واقعی جان می‌گیرد؛ نوستالژی و واقعیت، در یک مسابقه به هم می‌رسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663812" target="_blank">📅 11:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeUBfSi1Xd4Bx3pcJm0MboJUzWBR6nQkBJ6igRmRW6vH6dbsddXEKTUEXA5-NR-711WZBT73PcwyGIZ9TPaPp_1Hi_b1WadjfdvZ0IgpHmkAbDGjPVnsZjB6KolbajkV-oB2fhhnrG_SkhOuDUdAJK4xOVw3xMD3TWyh4sBM8LxbYAletHMxC7uTTK7yzNKUJhjzBIP5bAkz6TueFVoP_EFtXyegoK-rR_pW7mDBNBuYHzG4L1q93acBf5AGIFEmwFWplO4BUqRlKK0ScLAhhCNEsbqTd_nLynwvZS1InXoyTrGp_5pP_txDnm3810VM2sGzYgC0PMf8Z0DUv76DZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن رکورد دار رکود در ۱۴۰۴ شد
🔹
تازه‌ترین آمارهای بانک مرکزی از رشد اقتصادی بخش‌های مختلف اقتصاد در سال ۱۴۰۴ نشان می‌دهد بخش ساختمان با ثبت رشد منفی ۱۵.۸ درصدی، بیشترین افت تولید را در میان تمامی فعالیت‌های اقتصادی به خود اختصاص داده و رکورددار رکود در اقتصاد کشور شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663811" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64b94b7bd.mp4?token=KSphOchZSHg9sk2PneQUfZmaspUZv-wbRV8HBiKStFoasFHZ9VqF0PglUGUX50rc9e1ZFRb70pzL2KMeUG9CH9hfMDwt2Ksen0bZCZ1eVCUo4vLWvGHjmRkZBxPvvSzepqxQN_kTg5Fltvgu42S8Qu1RXiCNkHbQ_dwouTwdFtdcAS91t-wYhqwrvSXFDMrMPEE1QlVivHYWs-PhhgLTuDrb4u3Y3-tCDM7H97vf0Krz7sqpdlr8Fa38bOfYqn7vkiUkOPN1UqzmzCkrV10td8Oyp0oJ4FNw1gSYCGj6h8vetMUoAhZSwz3JOnmWI68qeKWXYrAaihxoU1--60X31g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64b94b7bd.mp4?token=KSphOchZSHg9sk2PneQUfZmaspUZv-wbRV8HBiKStFoasFHZ9VqF0PglUGUX50rc9e1ZFRb70pzL2KMeUG9CH9hfMDwt2Ksen0bZCZ1eVCUo4vLWvGHjmRkZBxPvvSzepqxQN_kTg5Fltvgu42S8Qu1RXiCNkHbQ_dwouTwdFtdcAS91t-wYhqwrvSXFDMrMPEE1QlVivHYWs-PhhgLTuDrb4u3Y3-tCDM7H97vf0Krz7sqpdlr8Fa38bOfYqn7vkiUkOPN1UqzmzCkrV10td8Oyp0oJ4FNw1gSYCGj6h8vetMUoAhZSwz3JOnmWI68qeKWXYrAaihxoU1--60X31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من شاهد نسل‌کشی فلسطینی‌ها بودم
🔹
هوادار تیم اسکاتلند در حاشیه بازی این کشور با برزیل در آمریکا خطاب به کسانی که پرچم رژیم صهیونیستی را در دست داشتند شعار داد: فلسطین را آزاد کنید. من در غزه پرستار بودم. من داوطلبانه در غزه کار کردم. من دیده‌ام چه اتفاقی می‌افتد. نسل‌کشی در جریان است. فلسطین را آزاد کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663810" target="_blank">📅 10:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0434cfe9.mp4?token=U-8NR3jumzBZ5yHnq37H98_nNqGylMLglS0zffJIETerry8Vh9UJXKYwfCJr4ueYmXg-HrOX9CkR_fr-4eJThktPaL3DEUxwwdSMCKAy7P3qNoZF5LdWOTQwjFk8CK2lhpQWC3HDtJNfSb8XY7lptQddPKfBUYf-Dho2hgZJ2MDvuT8_Aa0DzBfTvsyO-UXSFliCGZfKvHeR-8wg5ZkKkej3kJOrt2Ygujsj_PJiM4RhV2OqChzJy8aJIzTpzasW9f4C_3iDb0YXcu_e2H8IRpeZ5R05eZ7zTVYVLs3N7m8CzhoIrhf7KBdmQorgC7Z6sFykjtYdDEvCg7PkTpWAXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0434cfe9.mp4?token=U-8NR3jumzBZ5yHnq37H98_nNqGylMLglS0zffJIETerry8Vh9UJXKYwfCJr4ueYmXg-HrOX9CkR_fr-4eJThktPaL3DEUxwwdSMCKAy7P3qNoZF5LdWOTQwjFk8CK2lhpQWC3HDtJNfSb8XY7lptQddPKfBUYf-Dho2hgZJ2MDvuT8_Aa0DzBfTvsyO-UXSFliCGZfKvHeR-8wg5ZkKkej3kJOrt2Ygujsj_PJiM4RhV2OqChzJy8aJIzTpzasW9f4C_3iDb0YXcu_e2H8IRpeZ5R05eZ7zTVYVLs3N7m8CzhoIrhf7KBdmQorgC7Z6sFykjtYdDEvCg7PkTpWAXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663809" target="_blank">📅 10:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl20oCTfjyekFLUv8DHSkRt8qIxqjJ4n8n_gSRR6wcsD730HnxplnQA8FNxlBeqMHiMUfF_b3_aESV5tGGbyapTnv6wB9FKg7AAP-JOXNkHJ8zcEGcn9y3cpfxmF9J3WrPg2nVUD9caarACEYj3JuyxGm7pL9KaHEMizO_UqGFJnj7utpvnLEE8gcpLDTlTPxiE1ClBHeQO1afEHqM4Wog16l2uA2w0ef-RasVrjumHMbjtj-TVXEWVPcWXkj6n4MfDLi1EIyyBTVPa3z4SHwcih_lL0r7Yt1uo7SqYB4jSe0BLq0tOp4rEQIQ8htRg7FmLZj_Zyf33xdVym5CD7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریباً از هر ده نفر در جهان، یک نفر هنوز در فقر شدید زندگی می‌کند
🔹
آمار کل جمعیت تحت فقر مطلق در جهان روندی نزولی داشته و در سال ۲۰۲۴ به حدود ۸۴۷ میلیون نفر رسیده است.
🔹
منطقه آفریقای زیرصحرا با ۵۸۲ میلیون نفر، نزدیک به ۶۸ درصد از کل فقرای دنیا در سال ۲۰۲۴ را به خود اختصاص داده است.
🔹
مناطق جنوب و شرق آسیا و اقیانوسیه، نسبت به سال‌های ۱۹۹۰ و ۲۰۰۰ کاهش چشمگیر و موفقی را در کاهش جمعیت فقیر خود ثبت کرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663808" target="_blank">📅 10:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_5ayUZ59tGbiiVbMV06EpdqJ1tt77lX6BcNTV0CHnyY0AodnAz71LZJn5J_MYECzP-DL54PyD3KMZfyKTt962zQGMoKiKkL-Xx3bt0ZaXmEarbHfLdq2j37-9G3BvUDhxsB62Bb3bVTFrc1ft2atmPzaLOTnKF0okoSGnMosBpDujNIHjMC1em7SyBy9JpohUcSaiA8H0X30i6AWVUrGGhIjEmp0cFJGZzoWdX-PfrQOa-saArXLgLQ_OOBRwrqrBidvnAwKyk4hDRTtSUYqSwZVK7tvg4u4I_NBVsQWmSj2lVcZKLGzLvnPi5LRd6AWaoJEXO11c1EuLiP6I-uuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۵ علامت را نادیده نگیر؛ شاید فقط چند دقیقه برای نجات جانت فرصت داشته باشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663807" target="_blank">📅 10:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHzLjdH6bVzUxY8zMoVorhvWLLZ-pjw4411m7d8ibAul4OWTuaF6qfp5pLHGL4MJiCu7ywM7GKob-Aw0Js4Rx66g4nY8jTjLYsvxNV_-rbxLEmDgboefzAgyptftz8TLUjbBNQP5ep0IKjyvENMjo59tnTiIjqG9bXJJRRYDWas3Ox_beMlpgCoUVM4qE8WrA3NoJnrH6P_lhfrUjtd5CJO4sy2xUUqTq7iLjw-mvvFeBMTuAsSeZqo21ZeQOkV9k4Mdd-mWcsxweEGkKcv4Fi3FfzQkAJGuy9waJTw1MnmX6jc-x62M6XhiMxFSW46DFSMJfBcwsvTvU-EIGG8VUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره نقض آشکار یادداشت تفاهم خاتمه جنگ توسط آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663805" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a464775ad3.mp4?token=LjZ4uqLd7TcHzuTlk7IMCgXL2LuUCHMfeWRf-4t8L_-dt9QbubkxE0A2MyW9ZURSNJIU6YKvY6zbCXvnNwBywcGnZZjYHR7XOH9aRyTFjapyFofUy-iGkNVWvzEtANBlvA-MNdzzaEO5EwT0WwDUu-R1Uxp8PevVUFPZdaEuvXbBwCWZDuQ5qxEULkbbmzbp3feISvbNbrXYX0ilgYvA01nmMc3ZG0R-RIkyF6Yldf7gD1hHlocQizK3eGIiTv2IhCYefkVT2lIE8QG0YCpc2Tsg3HzAZXNhhsyNQc2Y6a-8tEEymze-TVZerII1emzQIv9Uv6nwt4mJMoadqAji1ZmOZq_PDGB-9xvjTICi1uWOhrY07-3sEurmFUu3GEZ8LyZH6ByikpkMmq5QtH4BFeJ9E-feY-hX7Y3acs39_10gnh6mvtUNVTg3jfBW0vMmGkdQWdfZ_sLeuE_PA9noeqduEdVqqr61UF6VK3ybx5-EWmZYWoV8aE7R4BaHMitaTgLxhSSGJtsJAgX7w4cNy-EKEWYWAWzKaAfSrB6g0Hd2jBdCF8DJQ4quLzplN_AVJLYlPI9iXUx_4AcTLssiJG9-yr5QwZUVGe7UctISXwvrhee0YSIZkB4P_6Ayj3od6_6jTdUHfEhNuxH6Jv8NVZl-3Tb1dFX72v4bXS07xMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a464775ad3.mp4?token=LjZ4uqLd7TcHzuTlk7IMCgXL2LuUCHMfeWRf-4t8L_-dt9QbubkxE0A2MyW9ZURSNJIU6YKvY6zbCXvnNwBywcGnZZjYHR7XOH9aRyTFjapyFofUy-iGkNVWvzEtANBlvA-MNdzzaEO5EwT0WwDUu-R1Uxp8PevVUFPZdaEuvXbBwCWZDuQ5qxEULkbbmzbp3feISvbNbrXYX0ilgYvA01nmMc3ZG0R-RIkyF6Yldf7gD1hHlocQizK3eGIiTv2IhCYefkVT2lIE8QG0YCpc2Tsg3HzAZXNhhsyNQc2Y6a-8tEEymze-TVZerII1emzQIv9Uv6nwt4mJMoadqAji1ZmOZq_PDGB-9xvjTICi1uWOhrY07-3sEurmFUu3GEZ8LyZH6ByikpkMmq5QtH4BFeJ9E-feY-hX7Y3acs39_10gnh6mvtUNVTg3jfBW0vMmGkdQWdfZ_sLeuE_PA9noeqduEdVqqr61UF6VK3ybx5-EWmZYWoV8aE7R4BaHMitaTgLxhSSGJtsJAgX7w4cNy-EKEWYWAWzKaAfSrB6g0Hd2jBdCF8DJQ4quLzplN_AVJLYlPI9iXUx_4AcTLssiJG9-yr5QwZUVGe7UctISXwvrhee0YSIZkB4P_6Ayj3od6_6jTdUHfEhNuxH6Jv8NVZl-3Tb1dFX72v4bXS07xMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت هفتم مستند احیاء و حقیقت | این‌جا زمزم ۳ ایران است
🔹
بزرگ‌ترین مگامدول تولید آهن اسفنجی خاورمیانه
✔️
جایی که روز افتتاحش، یک جمله بیش از هر چیز شنیده می‌شد: ما توانستیم!
✔️
اما امروز، وقتی ردِ تخریب بر پیکر این دستاورد بزرگ ملی نشسته است، یک سؤال پیش…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663804" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZE-NvQpfkvVma1KDCTipVdP1fgvApUXTHZUku6N1UPYl6n9XXEuedEljpa65dWAzNhQsedyij8YmcyHxGL-q2aZyYWg6HXYh71ukHNLvSLBsrBexNda-XlafEux-SO-EvCPjRDjEFNADQT58m6-9W5tenbMDgRqFX-kYIh_IDFg6y0DfRkViacKFusirsfFuapPu_bfZjkEXU7k1bj9EKC74ZbOKsCp4UzagJ6_Gcc6sQJ93lMxRWGIdGItYHU-7DewmYKALJ3H4E1xoD8jLUHSRPHxdubp58Zm4trOo9O16y7qHx9_-oVrtTd_TtB2HkAYCsTAtEglPVpBjkXzilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOHTFR0xsj5ICseczTLdtsBToPqcAy1b7CV8DtLs9v7W8DZ4Bzo9RnxdKsiFvRG8V7UUiT9HY3F9Z30neacpdj6e3SKs-I59Xy6oSsb_YPXb_1RJqOIKyyFVJaR63yjlfmAmm8MlRL-LgnzEGaWuJErR8re2iPQbXtVpgVXS8koRneyg1WxW5SB4TG9dasl4HfnNHviCC9TMIDLNPyPH7TM9HGPZoYtAI0J3h_MMXQtu5ZI2U4GWEei8TbRi-pR612c6GjrZZVo69Nlqk1Q3YhJEb5SpPlUm4RlRFRgWyhud-vrajXsXQJb1Il69zq1Gtw4ITPh9KNJ1ErAex4b30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nk_T5GStV6TQ1foc-D9jeG4J_ZibDi56qorkXg45iz-1jSxKXO2hYCcKLx3tjQlWm7IaMFFpC-APNvZ7THRtZNzH0ZH5IBkZQuDU9bsoJpojHVppSMrCNWdcV4Sur-IRbvdm0ST8CUJiqOnZA-ySkmbuZFh7bLOgviuKHsN3VMyYfE2_eozV8v6B7OnzS5eMWKEXamw3ohfER0UM4tGF7QQF3GecwW1OYicpjPTMbwS7ANqA9-DZDomJcZds6mJvZYTfyAUxOYQpmfrtgMDCLWNn1gpqS5o-KO7A8VRUvSd9VEpvD1rPqoHfLbrVggyIjYfMQt6zMfzrEkR_PfTUJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر قبل و بعد از حجم تخریب زلزله مرگبار ونزوئلا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663801" target="_blank">📅 10:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون ستاد مبارزه با موادمخدر: رصد ماهواره‌ای کشت غیرقانونی مخدر از سال آینده انجام می‌شود
🔹
رسانه‌های اسرائیل: ارتش اشغالگر نیروهای خود را در جنوب لبنان کاهش می‌دهد
🔹
لیبرمن: توافق لبنان و اسرائیل هرگز مانع درگیری جدید نخواهد شد
🔹
وزیر جهاد کشاورزی: تامین امنیت غذایی کشور با قدرت و بدون هیچگونه مشکلی در جریان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/663800" target="_blank">📅 10:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شایعه سود بانکی ۴۰ درصدی تکذیب شد
🔹
پیگیری‌ها از بانک مرکزی حاکیست، هیچ تصمیمی برای تغییر نرخ سود بانکی گرفته نشده و این موضوع فعلاً تنها در مرحله مطالعاتی در بانک مرکزی قرار دارد؛ بنابراین گزارش‌های منتشرشده فاقد هرگونه پایه و اساس است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663799" target="_blank">📅 10:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYASwrIP4N8-fUtlM21-WOVJ-KSQBjIiZvmn2nFVPmvg2_gc34HU2aqEjmwuYYcCBAz9nszaafzgZ4z5YoJd2eA8jmZUVXk3RydI7WOvINXttoB_A8R_gBm1CknaOUDgDBBEeVCViuP0UGL5FllWf_lPWQFYBoWB3EZ10-8Iiy9YmWK7Nw0YDUkvfv7X_dpbF7y2TD9NPceADaV36cXDWxAXGc1ZOheuWDH-29g_ww_7-4TGXFm9BYPKOjJ7zZQ3L04t994omtbKEpPdHXd1mdt42g81YK9qhfxOiyrpRF0NPGYSDa1iAYqfcK3xxnuypxGm1Vqi_NoWzSiqcqOraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشک‌های رامین رضاییان و حسرت از نتیجه بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663798" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مقامات امارات مدعی صدور هشدار در شهر دوبی امارات در پی احتمال حمله موشکی شدند و در ادامه توجیه کردند نقص فنی در سامانه‌های هشدار اولیه منجر به ارسال پیام‌های نادرست شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/663797" target="_blank">📅 10:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxR4fgQNxBJlucAt2yxbLHDzOTAtPvkHAr9a5OXMpVVeXjMe46mgPyXAHLCIZM-vf92iGTiD1t7lzdJIckB7OZj-A6w3ZS-q1n1yQzuT_o2pC00qchTcPGPg92hGStnkFbCcvs0KAVgmD31ysaBTUlDKTh5xVAmVkNWwAAMBFGTm_shqveysdiBJEylAZ3edVetRdLu02jYPAEX1Ze8KrJnk-QDj7Sp548jEkHZqD0XuyB0sY6JczYGf9i1KELKsMrNaSZlIVvVrfWZAQFhzYOfBoSLWITqzqcvPdnziuJvwwxa2XdvvNQUjr6XwefOGlW1O-FbKx7-uFp5PkEhreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرکز آمار:‌ تورم نقطه به نقطه خرداد ماه به ۸۸.۶ درصد رسید
🔹
تورم مناطق روستایی در خرداد ماه نیز به ۱۰۸ درصد رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/663796" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9103364e.mp4?token=SWAfg168zeCD0d5YDCPDKqar344LaVPN0H5ixB1NUP7EyqvVzWdvKRYOwKnLpeYksz-7Wk8pNGtx2Hd5lCf2UMxmAiB3OGBsdPzcV1mCarnIJIeJqZdh7W3TddinmvO6_n3gMWejqieBRfKd1ZzEty64kZJFuwwtrtbtOXHVcQ84XpSGmGcm0N2pVzOTGpS5Kq6JV0iFJ3YC8gmx-yWJRxxYoHTGA5eFU3GZ4nNcz95EcgrukMBnkOkHXrg4C8mcf5d9sJvuMcpUjU8VY3AUq6xlPpVw2XIjSkVLCSpgp98GilP2R13IAr1xJ3Hb6B8SpqViVeYqdm6rRg5IlhVigw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9103364e.mp4?token=SWAfg168zeCD0d5YDCPDKqar344LaVPN0H5ixB1NUP7EyqvVzWdvKRYOwKnLpeYksz-7Wk8pNGtx2Hd5lCf2UMxmAiB3OGBsdPzcV1mCarnIJIeJqZdh7W3TddinmvO6_n3gMWejqieBRfKd1ZzEty64kZJFuwwtrtbtOXHVcQ84XpSGmGcm0N2pVzOTGpS5Kq6JV0iFJ3YC8gmx-yWJRxxYoHTGA5eFU3GZ4nNcz95EcgrukMBnkOkHXrg4C8mcf5d9sJvuMcpUjU8VY3AUq6xlPpVw2XIjSkVLCSpgp98GilP2R13IAr1xJ3Hb6B8SpqViVeYqdm6rRg5IlhVigw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق جالب بازی الجزایر و اردن؛ شو نوری با موبایل‌ها
🔹
در بازی الجزایر و اردن، هواداران با اسکن یک QR کد روی نمایشگر ورزشگاه، بدون نصب اپلیکیشن، فلش و صفحه گوشی‌هایشان را با یک سیستم مرکزی هماهنگ کردند و یک نمایش نوری جذاب روی سکوها شکل گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/663795" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poglgd8uaUUsqktJdzhPJwoX_CanJ-N9JkbzzA2wHQHfmlmVmbsZk9g8vH3uwVUj2hgNAQPbqTZvvlEd9fWpIOSYvKId6vY2E7PJ_Cwf-nFBKOBW6NOr4PIaNlDEiP0RNEk7J1Co2wMLn1GNoH4HfzYtVG8kjdbwpIbBGfBsG5eMwgVI7FO2nSQpjFVm-qkdg2GTuC9eUodGofjnSzo9s5Bz4bCDYV1c6FMkbYqs3ZsZjNTJQDnLZH1gCMSu45wIPHuv1e0gpTypvrXFokrprlMkhX3PqwXN0zLg1ONLVx7JAeTCEX3hepZMybXyKBEKx7AIaex1k5QSKYlNl3ugmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی‌ها خونه‌ موندن و دیدن سریال‌های تکراری رو‌ به مهمونی ترجیح می‌دن‌؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/663794" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
جی‌دی‌ونس معاون ترامپ ساعتی پس از تجاوز ارتش تروریستی آمریکا به ایران و نقض آتش‌بس و تفاهم نامه مدعی شد: اگر ایران درباره نحوه اجرای یادداشت تفاهم اختلاف نظر دارد، می‌تواند تماس بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663793" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lanIxM79pQxIazgOG1kj1u9JP49hb1OVxjIuqguXUiXBP5e8aQsr_W49yJIf2VVv_MtKi3f3sBhMTSyej-mRN5wKJU9SlZOdXz_UtZml2xikP4LQskU8pK6dNMG5U2Nr-ZOzEkaJuX6-PdkOXkODw69MQiTOLW9xmjHZPW6PaREPMaA2iCK4ZQeMuIFuiFNdW0i4zksBd1Uc_oriIht-sJCD_7oib98GnywR9zY8C_5XfLc-n2MdmGvaSaW9PskNvXCOKVJaU4neUj8MxG0u71tFz_ZEI3xrX5DmBdKLLCLv_K0oXpZXz7lj1M0mjM4BTlkYm0aNEx6T7mFqTOIwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
🟥
🟥
🟥
🟥
🟥
🟥
⭕️
شعبه مجازی کافی نت مرکزی افتتاح شد
🟥
یک راه حل ساده برای کارهای شما
✅
فقط یه پیام از خانه یا محل کار، بقیش رو بسپار به ما
✅
⭕️
انجام کلیه امور به صورت غیرحضوری
⭕️
✅
انجام کلیه امور نقل و انتقال خودرو (تعویض پلاک)
✅
درخواست صدور کارت سوخت
✅
وام ازدواج و فرزندآوری
✅
وام ودیعه و کد رهگیری مسکن
✅
انجام کلیه امور مالیاتی
✅
پاسپورت زیارتی
⭕️
ابلاغیه شما رایگان دریافت میشود
🆓
👨‍💻
کافی‌نت مرکزی؛ جایی که کارهای اینترنتی شما در کمترین زمان انجام می‌شود .
🟠
🟠
🟠
🟠
👇
👇
👇
ارسال پیام آسان در تمامی پیام رسان ها
📱
@Cafinet_markazii
📱
تماس:
09388780700
📶
09216800950
📶
🌟
«یک بار مراجعه، یک عمر اعتماد»
🌟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/663792" target="_blank">📅 10:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcPS1yfMPhPxQnBOOksG7xqbZW9XyfHjy6jgCPeFAjYJfBNtL7ANMefiQtK6Szg7FsTsPOTQI8lhfUBIlnF40_C320eoi9OnqGmMAkmm86k5O1ChEtXe-k7jcDoZxpbSccXv3ocJ0vLdCo9qOygZnRIhmLk-X26hb1JEnIgadXIQW8ISmasBTv5NTRoXchCy-npnwe1YnX32grSVRAVZxXN3SD3ELK3goNpdPh-V_Ap70PCmrdw247ecSvLLTZbvta-EbrQCsrq0ZWFHIGbiAXVWDcaa_H8Lp6TFQtspyozs-B4vBVHNuhqmb2f8AvKJ6R_MtHWqv9yamZDbHGy4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا گل ایران توسط وار رد شد؟ + عکس
🔹
از همان دقیقه رد شدن گل ایران به دلیل آفساید، کاربران بسیاری این تصمیم را نادرست خواندند و معتقدند که گل وقت‌های تلف شده ایران درست بوده است. اما واقعا گل ایران سوخته و داوری به اشتباه آن را مردود کرده است؟
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3225956</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/663791" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfaf70cd.mp4?token=ORSaDUxJNbfVgKhxHGaw3gcsPHvN-8JO9YiQ3BXJbuRcuVqfj6oKVHAjeZ6Q8FYiI7kVMzwwymtAkd0HJZl0BBXkn79grchdbfLikTnymzORx_6G7FvZLRO0UbY2i3JRfOIwJ0-W89-94ILUEAEYZGIA2eM_fL3UkfSKOf-5YZtkCDP6AJl9Hg3f3gbBoE3AvQRhjFNuBvHZ_WQfSPq1XU7STwMfDDpLHOz3spv0pZlKe2QSg8WZxDiqQesaZP_IjWa08TV1sx1AiDXEJ3GMmbmw8s7KraG888nTZTX3nnUm9lYjkab61IKhtF9ASMuJS9wsH87xyB5tusyu1z0lhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfaf70cd.mp4?token=ORSaDUxJNbfVgKhxHGaw3gcsPHvN-8JO9YiQ3BXJbuRcuVqfj6oKVHAjeZ6Q8FYiI7kVMzwwymtAkd0HJZl0BBXkn79grchdbfLikTnymzORx_6G7FvZLRO0UbY2i3JRfOIwJ0-W89-94ILUEAEYZGIA2eM_fL3UkfSKOf-5YZtkCDP6AJl9Hg3f3gbBoE3AvQRhjFNuBvHZ_WQfSPq1XU7STwMfDDpLHOz3spv0pZlKe2QSg8WZxDiqQesaZP_IjWa08TV1sx1AiDXEJ3GMmbmw8s7KraG888nTZTX3nnUm9lYjkab61IKhtF9ASMuJS9wsH87xyB5tusyu1z0lhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/663790" target="_blank">📅 09:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به اروگوئه توسط بائنا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/663789" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سرلشکر عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا: نیروهای مسلح برای تقویت امنیت پایدار کاملا آماده هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/663788" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW1090oJEs26AQ7b8V2-Vb6PDX7FZNa4CC-dQm_yM80D9Jhr44n6ggjVrsV98ax5IlRTgwM4RBccfTG9R2514SwVGl_KTcMuKr_0ltmQJ33u6Ph1h7WHHJJvbS2nkeR4sTDGId_1DPRUDwK1kAFWZ5mA9yGKPk0mefxWm0lBi4kvxG68ze-NTIqHHETtjk-MTeW6vLg4XBcFtpv-VTEz8TYk15llEQL3R8ZlckRflxyHIyrf0uowRspN3TmJlCkNaDbJOrGIq2iDwWRHaCL-1lL_rQCw-sl_adr1f2P_1NGNNRr3h0Re16QkdVVjz8Sf31UdhXiOa5el1b41eqcBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در صورت قطعی شدن صعود ایران به عنوان تیم سوم، ملی‌پوشان ایران در مرحله یک سی‌ودوم، جمعه ساعت ۶:۳۰ صبح به مصاف سوئیس خواهند رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/663787" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج جرم از تاج خورشیدی/ ویدیوی منتشرشده توسط ناسا خروج جرم از تاج خورشیدی را به نمایش می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/663786" target="_blank">📅 09:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyPU4P6oMUJN_nFGh3bfJ5a4ozt1IOLCA0DEQ_rUDIBKGGugBlBL-Ky604Vgf7R-WK5nVB9wD8ESaGhXt4fwMzx_1VF5it1_4IzOYGE1FmXQ6WWzhWDezLgLHBuR_wM30DfqgrNGd74yNchTPPWl-ETBISio3-stLMWWInlmSpF47QP4hEaF-eORuMrQ-eo8lc7e-maOzYf1kWDGnyhK67CRhUQNgj6olBOi8oaLLpwB0h9zvlqBDqmy25nkeiG4emuqnuE3tFPbuhYhMmTWa6yY99g46PoYIcodd5jXO9c9KRIpA9IdjRj8Bqo06W3P7FRENZmttwNgyNw7zOOfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس ۹۲ درصدی ایران برای صعود/ برآورد سایت اتلتیک از احتمال صعود ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/663785" target="_blank">📅 09:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نخست وزیر پاکستان: اوضاع منطقه اهمیت امنیت دریایی را برای اقتصاد جهانی ثابت کرده است
شهباز شریف:
🔹
وضعیت منطقه‌ای اهمیت امنیت دریایی را برای اقتصاد جهانی و زنجیره‌های تأمین نشان داده است. / انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663784" target="_blank">📅 09:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663778">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7tIvhiIJCBvdlqE7oDA5NH0ayBkSt31LBoncD7dIyPdq0bEnfSnWWcAk15b1uL-W8xFDHUwwFGGOVZECFSS0uJMNSmL9_Lyizs3_MdHhwLKYfIN2u-QXJhJea18C7ANvbDGdUsnkPUpe7lWtOk72L28BHUYyEw0xONUFexMKY09K_8GlGZnwvzwBhrTHOAZsBEexVPom1XkBxM6eKbqG_QiGSEU9jtF57GLx7kN-M3ggkj-7m3nJ8NvPb9gqJVpySDMXTGlUWSvkiSWhg7in6akQvtvZVIsW6T1XloY0XOTBbFgJwcdzR4I1aPJ0QBmRxXeRbgRfFHFC82LjHMtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVh1_jhohFA1wOtqCVphjV4qlcKxppOJDyyAfkuS1sl3qI3f4rGulEsiZiuOdhjB1OtsO5REf3x1QqpfGo3JgWDCT2mAZ7gEe33Rtsnp8w5ITq9i_qh5uJnk_nwOaWAOdGxC210QgKQZsT81lIV_w5eMcyTqliPTawixDx44wbtolF9X9g923HsorfXIZmat8dPHmQ5KpRJV9daEb2gCEngABIzM4eKyqgZP3Ll0-Hsro1TjaKcA7yGf4YDdudG3ZO7QvOw9-jXsg4kQDGXaAwFXJ8aDFe7uCPzlLWmbq4gcnNrVBAS-vUXo5_y56iPxgXqD2PFnB0Vts4MLDY8QtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A10G0uVKzib0Q7fDODKYshmOAgcogMYXE6Olt8DxU6zrL5eselKsu7R7jAcPIkernNbk_vsKh1id2R65j_i1v5un-ZElK0H2jBQrNX3qwAn7e1bDh1SysAyg__wKdt2OWrjyjcQoKjPjWPNnTzIqwJchaaM2Ff7Q0Vtg9amB__kVg0Ph6Vs9mrZSIGhKtxGKWUKNzMjEA2kE-TqHPkS58oOICFJ6tq0LqYMQl8_7vaU2tB7j7yG8QHwOzSZyLffd15dJhTGGDdbHIW3GlM2ha73IyhUY8ayIYaOCssBdTmlGJJVYZMDqnDMFeASdyKC79he2nhf4crJs7yhV8zZWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp5WDAo6AzpsbqSvbCQsBD4lSaunu9SR9UsXhbDsfCPVAQnQMoP37JBB-aYuo5o8YCGvmkV-1LloqOdP7tC3LCAPO5oD4kLjzwLa_DYZvtf0C5DH6lSjTIKVoaJXUieK2mnjiwmdfshHQXDqkkiS6hNKrj2xJHzHOHAOKxt12yyptI6irDdRnMZKd8ZRjCPEEmUBxp0oIMcapXgeZxUq7hVgAtHxyjoU166Tz-1tbX7PMPKvb3wYGyfI41_5lOOUbF4QrJFYci7NdNgHO3E_RFSLg4E_warcNn5qPOnjNa24WLE6qJQF6LJ_NAgz9LkwfOtj-oZrAwTfGtAkInXLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfIy8GwGq-In3DosbnjdJr0vN15eoxCdrLy7brTQmK-4XzdWG46GS32CtF-TlWj_Dg14Fj4yE7ajO8qZ4EXBd58jDMZSb8ZSqJWS6Yy-QxezXGjZTpEMA8EfgVbirYq_kJ3YaDFBlGMh2pOLYuwvVH1lMApCYRrGVe-JNHbMg_jnfNhFM6_OnCHm1WlccJgJR3HV3LbvUoyf8zDEO7qcfY5Oa-1W24KeKb2L-30hHNT_UEezy2K7wlp2Z3VrGlT1CmGy0y4FQRbFf3EWbxmWw25YExRkDbVa6wzz3Vne7cANTHnAoHhFy1dCwj4FvHBpLfJJlR4uWcB6BmsItup-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlze_yR-56jeRbFvEb0t7EMragVF0ajZOVWgFRj0MVUfak3Fph38dOl3mCpx1UC6obiWDL9V4mjLChc0HlnBiJjQTTQKjpG0JQHQo05MfAK6l3tpYLQVJIQ3RLN5_uEArEFZoqAVOgoZFq2oumaQa746sa0aA88cUqf4ShT9tWQNZQTFQxQ3xltgDO9DR41dHoFsukUSkLp3tBDDgqDZutzKP_-zzkwJ5A4LseU104rX5a6R38aRU5t4db95Jd_LUe8gB_tc5nMtS1CdT_-H8tq6cEjy1cKc6jafVnTu12DVn-jJOPBpiRTcT-MG8KFEQKbms5JPMr9HsOX-WdfLfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط یک فنجان می‌تونه عنوان «نوشیدنی ویژه کافه» رو بگیره... انتخاب تو کدومه؟
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663778" target="_blank">📅 09:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUJBR1HToaQVpL0cydA-1Xz4iY44HYrA5uXKeAVh7Vrb2x7Sa56NFH18uzLEfRYL0cOWTFGIC2UYHJaIwivCMLSKb-2EieHiKF1cO_Mj3DTuyoW92cWWqhmFBXXnFVs65fr7PpIb22Nam0yjiXvJudH5q2WEzbMkJjmHfCZmcz8dbt5msByUb_dTT9zTfs9jkr0pskV-OvMt4yWan3OFlfyK2bMnQjQMlcSJKKUasBytdhoQp2oiXO1BEqz5W8LuUTNp7KFrXbDzYr8tVHG6hvNORLfMAAeiuEUHXSinZDl9WmzxzxpYERsmWCGns9u3c0weV7q8rAy78ot4oBY1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663777" target="_blank">📅 09:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663776">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین سیکس‌پک؛ قابل اجرا در منزل و باشگاه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663776" target="_blank">📅 09:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663775">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYMEd1D0f_UkS3WKAMznkkK2827Wtk5ev7UcBu5XK7h_0YLYR0w8nx4hQgYSnkoF9JR6KqYBn0tj6U-yZHSvTnMQRHTf4ph8Bgcm_LlMsRjDZ2CG01rEQPnQJEczSgD-yM7_O5VCqZaH5Jt9bjrYAgMTCbT80RZqfml7NctRtiug5_-xCv5WBTfQ8dxWbCc3xcQ5XFt4jCC3EYwN8O5Qb7iIigyQikRDXL2y3RyBUMvZWpNsV8kfCQO5kLtth81XwE5KiIfK86HFOL-TFS_bcHZqEhcYBstnKIxwRggzbSHGa4dHdBQS9oybw7SruYAzqKSANWnVX65nLMIT_iqIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
🥛
معرفی اصطلاحات مختلف
|
#واژه_کاوی
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663775" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663774">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد تماشاچیان هنگام خروج از ورزشگاه: فلسطین را آزاد کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/663774" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In-z9_XCTE2sw3yQntpBIUqHLxwqhquU3Epk9DucNUCFGA6L9LsY_yU1RieV3FMA48Wk_90d5WIP3p7rlKbkFWMonVBDkJrNljxmgvxL4vhSUChHLwW9Kc3MV00NsI-9imXgdbGcPB_7r6OOYD7ZZKk8Zk0PZT3sfTCR-_upXCxtOtnBCIxRPcWSAZzSISigRxRF5MlPuFOWVB7V0n7LS4LanGfuI3Csb9bu_Lyc5vQbNtDLXCpaEWbrKZDFrtozJtB3zlAJL76HaFGMOOow7LE4WzVh4X3O9kYmQbffGC8bi4djSBUipv-IYrgY8LkaFrjs8fgeYbSTiofQXCbbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《 اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
تجربه‌ای از دل سال‌ها همراهی
🏕
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
👇
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/663771" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663770">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/663770" target="_blank">📅 09:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663769">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdTgMouohv5cw9N1yoGiOexaP4-Y9KFwFhdCxdOVY_oXvw5sxd5MVOkQf-aEaUhu8_UMi3sY5zaKyQBeHxe_vCWBGeVjkgAWeJK7GQnazSX4smGMhAAUAK4S6t4WLqcc65ppIfRtgB3NPScJ2yEfo6-C69HLY9WKQMTxNfkLKpCfPrKEoQMYiCF8ynSiNws4JHOvkKFsm3MC9k3fJwtZ7cq1QxOnFymQ3Bxz75JcxCw92xmuCvhp8H8DKx18KUomjVZ6FHMZeLCyOFwPn7qELBQ_HycLDhOze4bvQVYkDSKA-tEZLHB9GA63wfo1Jiwy5KuD3cIf4z1ocHXArTi3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی حسن، مجری معروف بریتانیایی-آمریکایی به بمباران ایران توسط آمریکا و میزبانی در جام جهانی
🔹
آیا تا به حال جام جهانی ای برگزار شده که تیمی در کشور میزبان بازی کند، درست در همان روزی که کشور میزبان، کشور آن تیم را بمباران می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/663769" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663768">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663768" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663767">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtP4OMFdnjPnBOoycUzYHBPR01NqhAliQx-whnG87lZvs0xyQfLliGH557qB3T6fSELZpM4cUllvzSfB9iiBpS4KB_u8tvu22Dnazk_JEigfqebhpmnPWkomEruIGZ8o2-bb7LJF3VHBHm5RPa4Ults7Mdq2vpaJPhbUWmS-CNAEbv3-_dIkoTbp6jGIOEsT-3vNI9q8h3egPZmAFuZ07yWfSLwyyeDwYCv0t1OarMpei7VOtVd70DySDVl9fPPCo7SUdIeZpOQasPXvC9655TGYt6myI3X94bpUpsX_LfRcnLYStdff65hUOyUj3LBG5LyZ4liimN9-LpYBXxGSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی: خلاصه بازی واسه کسایی که ندیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/663767" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663766">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعه‌نویی: همه لذت بردیم؛ حالا نمی‌دونم خدا هم با ما سر ناسازگاری داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663766" target="_blank">📅 08:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663765">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ-9CJAyGua6P7IJpaeglr7c63Qyt_wguGly0sQyeBksQAkW_FVeU8Z_irkkc0Zv5cmVw8PQ6o8xK-gQJhy7xhZcZpfdltIzy6sls6xRYtEtxcqc-vUk-QcNdpvXaf0VN_PY4geVGD-iWhmpnQErrLGT9VueHkPfg2fBtianq6JUPWEedFWJOflZyleAhqM1POwO1SFxsKDWmK5ETP2aUinMv1k-_35TtHgGjiQ8D9BdF7H-1s-I8mMkSX1xbY3miIUwdyEbgeHGWZ_j3p1vLeMiGivP-CJTp4dscG7K-tHhUUXE2INFmkxl2jUOUzk9zp4XuJGYIlGc8vkjd32JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون پس از تساوی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663765" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663764">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NrM3e34sFzLeaiK11ky7WIcw9MMmreUfyNTZFSbXZzD199LM4nu24a9wKhG5ANM8hFCwlZ3T4qmn_2SBZ_GRgbLWt8lVx0DvmBJneeVwtrc4JkLR2Ej8xg6XpHaZtPbDw6yFe6CEwoAxcVW6s71hMLM38HywF48-ZOFq29e6AtmEqNZ7mFiwVl3aq3b_-U5ly8ctVl39qKtZ3KLT_An9VE4BdWfi2Tor3SIPbKkGa67m2E0Th8QA0o4KQHIgoXBT_lqVY8D_p8rv9Kj-tqJQ5BGXF6U2k2d4ek_R1czuKJMUyltpv299X2ze1N1W1ObTuEF7hce3BHtBMfxfUMa4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی ۲۰۲۶ تا به اینجای مسابقات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663764" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663763">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq_hpj6FxZYsAp-BTxwlETN-9iQKC8_nBBbJTySORaRXnC1tgGzbfmXIjIcRxL51JNMy0r3jK_JTUS7xmYfzpRxucG3LFzq5LZztN3VpsB6kXPelcRMxYVSvKhgD3VzMzUqHP2pVhTOHsB_NsFI-MomXNuEEUiO3QE0T4xTYEz-3FxB2UfSnNswmWmhne-OAs5SbKCLTAtdrccXblZdAslUVnBKgGqYKFg5ljxedkRb6cwWnMN2IT-UPtUpS-6teW7tK0mccXW0XwbEh-z0bFc5mu2GsXoldE6dQduBQx3t4EmpDac8m5GodhVtcWo6n7s2TNxpAlSI6VFke6tAuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663763" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663762">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwmv9inYih1t8Vefjc2bxPK70dM6Ii9tqBRX6FfdLEW3FrUzJk8OYL3WiWW6-l38HchFqYpPIrKTN1X2adpg8Q_SQMMMIArmpdJfnpGsBcoru9G_nMxUbqtgbuHAo9gtEgZAxCj9V0YWdyJHfTgbOCzB0-bn6PDvc1mC0bPlQ-fDw3s-IcyuUl4uyt-y-hUJUx4aBdp-8mgi7r1oFXeqG30TjEYF6JTM1A8DKVScmUSWtstXtbSQ5haaC4oCKPgEhWTorY08VTHaOWmJC8LgblCEw0cx-cafxi8jgg-7Y08G8p8_hGUPbq7R0P20bCYemeLmxekT1EH75Vg29fp5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول نهایی گروه G جام‌جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/663762" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/663761" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رامین رضاییان و حسرت از نتیجه بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663760" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/663759" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/663758" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران ۱_۱ مصر</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/663757" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایان بازی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/663756" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بازم توپ به تیرک دروازه مصر خورد</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/663755" target="_blank">📅 08:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گل رد شد</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663754" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شجاع خلیل زاده در دقیقه ۳+۹۰ گل دوم رو برای ایران زد</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/663753" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⬛️
⬛️
⬛️
گلللللل دوم برای ایران</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663752" target="_blank">📅 08:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر طارمی با بدشانسی به تیر دروازه خورد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/663751" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">علیرضا جهانبخش به جای محمد محبی وارد زمین شد</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663750" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663749" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توپ به تیرک دروازه مصر خورد</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/663748" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663747">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY54s8g5ZzN9aU5LSp6Dyj4UxpuSkUTT8LFyTslxVpUX9nQn9qu9vyhkkGaMadmsoVRjZ5QwNNThT_VeuuBE3cKIRGWOI0JW21fV0KbXA9NAdqmadp5WIsqF6jkdSyaZr_32icjQyO194kZLtZQ92LByNoLp9THGy5p_RrnpM_GGf2sblpPSMRv18fzy8BiLLwYhihgMk6muE0arOBeOghYlXbieu5QgpDKSi-LQXVO-GYJAczcimyh2uhAwHP8AZdJprClopId91TgCI9uqYYmcoIbpQB2ihNqya36bm1VHqiDoz2tF-2q8tNbMR_EzPobklaK9xtK7jRQlEEG0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ملاقات مهدوی‌کیا و اینفانتینو در حاشیه بازی ایران - مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/663747" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663746">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کمتر از ۵ دقیقه تا پایان ۹۰ دقیقه</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/663746" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663745">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گل دوم برای بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663745" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663744">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
مصاحبه مجازی دکتری ۱۴۰۵ دانشگاه آزاد از امروز (۶ تیر) شروع شد.
🔹
زلزله‌ای به قدرت ۵.۴ ریشتر پاکستان را لرزاند.
🔹
نماینده لبنان: اسرائیل به دنبال به راه انداختن جنگ داخلی در لبنان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/663744" target="_blank">📅 08:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663743">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a0272b0.mp4?token=kcEADhTkhHeclFHtg8bNb7waouJNlNW2fJVpAmEi_xbF218KR-Z6Ojxqn3ANbF6c-hDpnj-Se4SCjh9V3QquAc4oSwcsZqZsL00FJjK4b6iW7PpOLc8Pr0725pZBh5c1bc94TrO5H76EJurTsryF3tBRbHKLsHQuuCzTOgoPEygUpvGM0pylVvhtWY2REsmmjU1UUTlEIv1RSe1M5xMGlAJZMd5FVxVrN5J_Z6wVvxQzuGrk6F7jRziZG5UobaytimC25NGVhYp900SSk9_zE6aHpMAbAJCmcYBYjFXA7QQZ42LiwypvguTCTsEHjlbi8KJZU4VGiwH1HBPEC6eLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a0272b0.mp4?token=kcEADhTkhHeclFHtg8bNb7waouJNlNW2fJVpAmEi_xbF218KR-Z6Ojxqn3ANbF6c-hDpnj-Se4SCjh9V3QquAc4oSwcsZqZsL00FJjK4b6iW7PpOLc8Pr0725pZBh5c1bc94TrO5H76EJurTsryF3tBRbHKLsHQuuCzTOgoPEygUpvGM0pylVvhtWY2REsmmjU1UUTlEIv1RSe1M5xMGlAJZMd5FVxVrN5J_Z6wVvxQzuGrk6F7jRziZG5UobaytimC25NGVhYp900SSk9_zE6aHpMAbAJCmcYBYjFXA7QQZ42LiwypvguTCTsEHjlbi8KJZU4VGiwH1HBPEC6eLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مسئول امدادرسانی سازمان ملل به خبرگزاری فرانسه: بیش از ۵۰ هزار نفر پس از زلزله ونزوئلا مفقود شده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/663743" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
در حمله افراد مسلح به ایست بازرسی سبدلو در بانه تعداد شهدا به ۳ نفر رسید و ۵ نفر دیگر مجروح شدند  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/663742" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جدول آنلاین با ۳-۰ شدن بلژیک در برابر نیوزیلند
تیم - امتیاز
بلژیک - ۵
مصر - ۵
ایران - ۳
نیوزیلند - ۱
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/663741" target="_blank">📅 08:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqdY5WNBrDJ0i8RR5_2QESFiCtjA3vhpUlHS_SEU6hqUivvEWjrArQXEjCCNlAYOAY2HCoK0XV0WcHseFW1usqtfr_zgtyhgpqzPd-Aj15BvJiDnOySM28BWLRrsLD9wfmB0fpSURKjK3DuqUegbDajTzEuxU1WZ8n_sqoKTsArfxG-L8j-QnHJunnPAh91ACWovQcyYAOex0uklquQLEp-DXg_zkpZm1u-Q7ZAfOcayOIxhA1wx5deUDSE6S7OQjeGYwZitQW2CyFr28zcmJWw57JeeLm3lyYE8CQvvmzcPsS2utEvzanJlzzqiwE9Sb5rJwsT7lPHOvXDT8O3aOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهار پنالتی مهدی طارمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663740" target="_blank">📅 07:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
حمله ضدانقلاب به ایست‌وبازرسی بانه با ۲ شهید و ۵ مجروح
🔹
بر اساس پیگیری‌ها، هر دو شهید از نیروهای انتظامی بوده‌اند. همچنین در میان مجروحان نیز ۵ نفر از نیروهای انتظامی، یک نفر از نیروهای سپاه پاسداران و دو نفر از افراد غیرنظامی حضور دارند./ تسنیم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/663739" target="_blank">📅 07:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محمد صلاح تعویض شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663737" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f873145d.mp4?token=Dwn274XRjxulaKo1xKriOawd9uJks5Hs3i8mWXCY1NWdytdZoeYBARH8s2T8e2hOpc5rHFs_Rd_GqSMO8J08k_TsxRLlw4nuq6ssEJQVi2l5xn3B-GwQfxU4cOXRZtzi7aQQpBi6TgsXTiS6Rl3joZfYmnyM2f7uSSHschAHmif2dlGmqfrcRxkbxD3Wf8GwGxw4ruikHDj1jKQkXd9_kY_xZ73hdqrxKq8vGY49oxv-n36wkbKrmQHInXkYJnMLWDW8QSe6WB9DAMdF9TNy4teYeY-I7ilW0HvLNZj2WpV1hIFCHCMTV4McnFnBoedm5AxJSxn2aupiDBXkApT_yBwWShSQgqJhzyhs1K-WascIbzgR5obieLAJtLHUA9zjduilf51fB9aosDtn86bZ6ts6cZXf6cP2w7mSXLOH26dcxexzT3852x6mB8OTxKxDrlu8ct4ZWVDYJ-uHmFyqgwCUMo2L5JKF60gTJNUqybKZEEfQA8QLdDNQmkNHtTFzEKPXAC1Kkqmeed7MmnZ4bW88ojccXu3-w9TVWROa5GoZ30rU6zRYFYMXqyHaYmNmdN3hdzk8trYffSB8jbpQyvfn-DCgHLAnElYXWTABZfQmuEUdamlbw_qgbNCy2fWfTXSorKU_4IcFggHJT4lPgKvUtoqvUka0VJW12yEa_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f873145d.mp4?token=Dwn274XRjxulaKo1xKriOawd9uJks5Hs3i8mWXCY1NWdytdZoeYBARH8s2T8e2hOpc5rHFs_Rd_GqSMO8J08k_TsxRLlw4nuq6ssEJQVi2l5xn3B-GwQfxU4cOXRZtzi7aQQpBi6TgsXTiS6Rl3joZfYmnyM2f7uSSHschAHmif2dlGmqfrcRxkbxD3Wf8GwGxw4ruikHDj1jKQkXd9_kY_xZ73hdqrxKq8vGY49oxv-n36wkbKrmQHInXkYJnMLWDW8QSe6WB9DAMdF9TNy4teYeY-I7ilW0HvLNZj2WpV1hIFCHCMTV4McnFnBoedm5AxJSxn2aupiDBXkApT_yBwWShSQgqJhzyhs1K-WascIbzgR5obieLAJtLHUA9zjduilf51fB9aosDtn86bZ6ts6cZXf6cP2w7mSXLOH26dcxexzT3852x6mB8OTxKxDrlu8ct4ZWVDYJ-uHmFyqgwCUMo2L5JKF60gTJNUqybKZEEfQA8QLdDNQmkNHtTFzEKPXAC1Kkqmeed7MmnZ4bW88ojccXu3-w9TVWROa5GoZ30rU6zRYFYMXqyHaYmNmdN3hdzk8trYffSB8jbpQyvfn-DCgHLAnElYXWTABZfQmuEUdamlbw_qgbNCy2fWfTXSorKU_4IcFggHJT4lPgKvUtoqvUka0VJW12yEa_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
درگیری فیزیکی شدید در پارلمان گرجستان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/663736" target="_blank">📅 07:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d573238b97.mp4?token=hHW782rcJmvUCZe6mntDO4pT_bvuN70bqR_FxW8Jgn-T8d2rkJdh6FFi86WsP5sFOefLSZoU2VyhTCiz-JHOWXreOdNAW1D7z74SWbj8JUkb9l3JvzB95T58_RSW2f3yyV83M1tQ2N3WpuIqrSlG0m2IXSCNAbfr06_fNc3yhFZReLwNCFsJQ2sAzryQM3k2YQmoLqUVaMvVJ0cFUGsPYwv49W2tuxCUecyMmA_SgiPjrJZqoLMvhB0Ccwwg5OimiSQG-eq0qQU62_W1Fyerlg8iHy72fRgu9aeV8VF76tByrF78dwx5O9xBl8LTiSZ1P2Eu8UM0WY2jXOhu5Qs_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d573238b97.mp4?token=hHW782rcJmvUCZe6mntDO4pT_bvuN70bqR_FxW8Jgn-T8d2rkJdh6FFi86WsP5sFOefLSZoU2VyhTCiz-JHOWXreOdNAW1D7z74SWbj8JUkb9l3JvzB95T58_RSW2f3yyV83M1tQ2N3WpuIqrSlG0m2IXSCNAbfr06_fNc3yhFZReLwNCFsJQ2sAzryQM3k2YQmoLqUVaMvVJ0cFUGsPYwv49W2tuxCUecyMmA_SgiPjrJZqoLMvhB0Ccwwg5OimiSQG-eq0qQU62_W1Fyerlg8iHy72fRgu9aeV8VF76tByrF78dwx5O9xBl8LTiSZ1P2Eu8UM0WY2jXOhu5Qs_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون؛ تحریریه خبرفوری در حال تماشای بازی ایران و مصر
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663735" target="_blank">📅 07:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بلژیک در بازی همزمان دروازه نیوزیلند رو باز کرد</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663734" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSH6d2JfxT9y8pt723X1ZhXCQehyKbutrlgilsZb4mG01Ko1jPzKwApRVYy0Y9Hk6-MsDXPKhnrDFhNTPNeRrl3GYtTSSu9zZdqI0i1ksOlcyDB8C8ycK4WE-EOKrZOUsGh0JSloq38U_iXeBxZEwRml82FTNm0-IyEaiPjTbA6Hvd4eoApYnI9VusmlMOUsDyWnK43VM6Bft-wyFIqumFaFLXx9R6WisMPv8r827bMThclwj3O2sS1ORURIW4zZn60byTohTQP_ea0-rKJZTpZqros7s0CWKGCFuH1_ZYKko-mEyZMDEG8FJxX_YqN-jJzfAwU77ZIZbJ5Wiq8G3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدول بهترین تیم‌های سوم گروهی تا این لحظه
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663733" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663732">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhFJJBwtEe5c6esvy_s9lGTJwNOueF8Z59GT4yfy6xBMF-uyr5NaYxtmeK9Obbn3ScOjIuVW23sSzBMpdk8FRtxCqnhw14m3UdOJNAbOdjHJrUe31w58GXod3QoNXRdu03rk3K_g5DC_bJ6_EIVFvcQ3XNIzl1irXzkL2cW0xameOz-KYBCdp7Z1QkxYShx7_u8hWWFKW87eWuSMEWrSSAtmRm3mb5VAugwk1KYyuGpLGHWRmVyt00limtqskFrqgYMaLEHp2olm5iOw5BT98tJ9ynA5mxVw36bnOuynp7AiP587QsW__4mao4PRHQOtLlUnp-c2ChEjOEjgex8YVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمرات بازیکنان ایران در پایان نیمه اول</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663732" target="_blank">📅 07:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bunIR_gFQnKdRRJi0FtnXCAUOSq60n7D3E-shIdTSG18A-PVtXfBfRu3qs5hABX9OhKsG73tADc65EePwVdcI5qV0DGqC40TYrShL6oq2K_NN9N3atiG8vusoNU9bBf2pVKjufpRYzkyacFf7iS3_a-nU55_JCfRRbdNVjmt5-ZJcGDgpm_EQNWxDTdJhggCwCW3hlmgpGSLLo7TnejwvYkFD4FAdt1Jsqo4SgOedFtkrSge4QfDWbL3nwd-U4JBYgD3wNQ5sV4S34TF14Y-JY76mfpnWimVIVAbCL6Tv2tFlixRN7Wa_8PMrS1pCSA87wW6exF-6ReivOX7Fc_iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYyXQZBw3jl8r-hihQvS-HJgPXAjAJh0HM6We7wkpiHj2a6x9IdVzucyp_5O-5Gmaty3LAoeBH8d5nJvZ-FSgGjvHrS1fA-7iosc3lB6-GYOV8STuBPhGX5aW11IXctN-uYe6te2mdXhPWq1ZVfH1OLM_Dy6U0ql2iguKA37t89YlHfLMwR1NKRJgx1jAHhinMoRcuZvUZ8802a4bRq5vG6pJCEKEC5Ze0pd8Z9RYUP12dZEBXIh_n22wMaUv22-TwBb1gehhz-huLNG4nQLtVCLVEDTnkJecDIziSh-SKbl8KBBCcG8o3goBVwX8KC4l6MkIa7pekrdEzesntNu9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شوخی کاربران فضای مجازی: گفتم این سرمربی مصرو یه جا دیدما @AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/663730" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شوخی کاربران فضای مجازی  لیلی و مجنون ۱ یوسف و زلیخا ۱  تنگه هرمز ۱ رود نیل ۱</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/663729" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2v-JZJerZiQLVcBPRPwSvgUUUgGQDx8vvZt69NBql49cJlGMS75lSZ0dVafTdQDgfD2_OH0NFo84dUExBcfvq7yxqaq0kO3K7X5lDtFvpewNsh2G8Fq1vWsjPGQ247qa7gQDzk94zDAVSQhFznepDlbkGax8cPP8Ym5GegPTwVz2QbvIMFkhT6s-Vl_bwL8bU3CMRV-5cTTz_UjMOw2F3Sva6dLML2CYTmBj5YWRYMyJoeTPswA45zo_dLSOOtYrwj7pPeb1_gkJuyJno35GMNl3fE3IP_ndTjcIOduzEV0iNI9o22_cKqXrIgG2f-ZMSqeNDy5SGbI6NKY32hQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_DBiovfiYhIBjb0_BDXCG5lA6SLC68_qp33NKFAIpNOUU-4e1koQzR_d-J5didnf26MtwvIpl99eBZR8hY3nIm8IA6vjQEQ4nK0mcZ1h8HzD50-Ktboiti3RU8-kuDQDqnZIKgoCvzdLZ2zavgvpvJkyi1RJDrXg2jho-AePLbg08A5--P_xR_YvZAQzLfpZiyf8HDWv2kP1BI8aPQ5XuJR9PWQIIu5CWp62EeCjGzgCOMjUkmUTr0UClgan0Ub3yXfQ1jsWtzMlEZVK5BoQXaDqKWkhG_o4Nq4g5rKJZcqCYkV0qFJvdsUM7q31JqR8Wf4SZiDvMvDu_ziQNUvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مربی مصر شبیه کاهن‌های معبد در سریال یوسف پیامبر هست @AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663727" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS3CZSlq7mmrfpb16Z2Dj469Ziq7iyOJ2WQ4AmQYkTHdHneVz-l9nSaHUxv9K3QSkVPwPNoAfmqClzY0tdm6QRrYZ0GrqHX2eoAftYUL-xN4Atsh04YQYh-70pqf7oiQHuWU8ImqQPczSawc5BymWb8pdYavaGcbRS_CsH-g5qiO7dKClUZ8nLdNB4-oxY8eKnAjyi9lLei3PFn-PRka0_tIkNTIThIYe60k5fZt-_0a11qe59j1etMHMimsATN-rwpiISvCwMwW8a9lUDGnI7a9NbpGpPbY2V5Z9cdkv4Z6sCiTLoK5ybWC92LhXxuD7ewmi1DdXScHs4x2Us-lVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی کاربران فضای مجازی: الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم داداش؟
😁
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/663726" target="_blank">📅 07:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تنگه هرمز ۱  کانال سوئز ۱</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663725" target="_blank">📅 07:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvnjYyK4TNi18ErMhMbzwMNdoVBnnRG4J10PB8em-ea7fNZqRAzV9lbJKmpL0b090L0VKmsifx5q_qZJniriJKJXzSXuatC9pRO-TOeXdl8NXnp9SEyl1itgDo3ir2gnjNAPYJaSyF4mnrJwbg9Yb_EJLsxq3bqdBubwEQnXGf4aB3RLf39zr2JyvM5QW0hk6v4bJNYwdjCmLR-rgFMy6CaehbHyP1SKxaz9MCIPq_7K8D0zPN6KskL8RZjazWHuLb5N4A09cTFzoN4t0nvZM4WCQI5F4MwaAYy5n7WKvILieyr2fdAdeqfLYFTLeSJhc5ds9kLiDtTQhMMYI21E8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی مصر شبیه کاهن‌های معبد در سریال یوسف پیامبر هست
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/663724" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

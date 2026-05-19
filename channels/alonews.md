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
<img src="https://cdn4.telesco.pe/file/I3wwY59EwyQschm8mCui56P2nXu8-o_BY7UETGxAtT3-qcCE0nYJMErFeXddiGjAMjgZ6zgQip1ZTHWUO480Oi414uVaMk3CVRzv81D2ZmUO3PVkVBAeuaOBfKxhZa7tFaHfUrGlDneDrvpqfqp9ibhkDB2uE3SXaIn64hEhNMvXOjzNB2n4aM1YsUtwmTKhkNehbUiSJDUzmCRHJ6Uj0FggQup31Fx2g8hm_bY6SNxEroqegudLAMwxElQgya5ZsfxAfDMAr9d0qehmmlUmC5VGt-Gh0EkOc4sUPoTS7QL4W2hxTJ63fh80HXT5zyOgdCWLm9l0sEMGXflqXvu9DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 22:24:34</div>
<hr>

<div class="tg-post" id="msg-121170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsKhsFc2vAqjyW2BmSj_VxG44fmg_xrU1rl5Txu_EV3WyU0fzTY7ZrqMXL26eV74iaypHHRu9uz0ZUQlHuyzMqOJxSCj-cCt6Qog35eptyr4d8mgTgZ5QR7hpXZJUc-ck_AFggx01BHLfsfIk5G1cmVKXjSyU5yE1ssyCv62tFQ1ZtIv0wJtpPGp53XzlWW9tStljB5AWH9d0kGQtVd5c429fqCwIolaZC3s2L7Vm0VDqaSGLWLac1KgfQg-e3RE_Xk_jGwr54XKJXrRQ5gimUTFfVbkfgpWOnEpiEFkvDrUDlzeS89qu32UxZH3NKewSnpAloOMHS-wP8RB2-y0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فیفا
: ورود پرچم شیر و خورشید و هر پرچمی جز پرچم رسمی کشورها وارد ورزشگاه بشه باهاش برخورد میکنیم و ممنوعه.
@AloSport</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/alonews/121170" target="_blank">📅 22:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRRvop2LGShnUQv7710NRFCkqx1c9wFNkqAoORrBAg4bUfThqHQDr4Ir7fWXwk7sIcey6DtkhvnzD43LsWVV-VhVw4r8T5liXwR2APWcG4KB4rJM9vDtbNMprDRXut6hupDI0zyMJBCs5CcplFkpHRFOZOo1104GQVlXC2TFsenXB1iggRnWXZ_zEyBdKH78-LtMSlMqUiBgvl4vapEGeLdaFv77mTCyKIoDSxzdXx92vx_MoxHs8TvsL2xPL7wPeTLFspESZcW4AB6F9wT-OiLeTHKXgHTTWTxiSW7DXdnp8TFsM6ZB2ufuV85sMZp3Y9PEpgMcWDwYb6zCcrAP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش wsj ، ایالات متحده یک نفتکش تحریم شده مرتبط با ایران را در اقیانوس هند در طول شب توقیف کرد.
🔴
این کشتی احتمالا در ماه فوریه با بیش از یک میلیون بشکه نفت خام در جزیره خارگ ایران بارگیری شده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/alonews/121169" target="_blank">📅 22:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37b0750de.mp4?token=ogqqPdI-rpOCmfbn2Quw0qKF6PfjorUt_IwOnSC5B31doRoMxnHNwJ6_DzxxRzqPHX40HfYcsHXpeo2GV-kOg_6b4RV0W6zUdBKelB_qrxitaMIp5tb4ZKqGhmfAdXnk1ABhhuWSCAS4GL7orsUzdbLOUSSTNCLPsvkLrLQeVyd-YCtSgq6bCaGH4CEEUrubCA1zA2jUe3b7Ju-3g_VxyDkK31KSnAUNM4O05WFk2emP6Krp3MH3u6IfcO3diZK4S5O9tTpruKFZXe0QGeu9va8OocE7CSUQHHXDzC6tQ9wks7u23a_NIQbs39gceCHeCwXUM0wKWuBqgK3ipp88jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37b0750de.mp4?token=ogqqPdI-rpOCmfbn2Quw0qKF6PfjorUt_IwOnSC5B31doRoMxnHNwJ6_DzxxRzqPHX40HfYcsHXpeo2GV-kOg_6b4RV0W6zUdBKelB_qrxitaMIp5tb4ZKqGhmfAdXnk1ABhhuWSCAS4GL7orsUzdbLOUSSTNCLPsvkLrLQeVyd-YCtSgq6bCaGH4CEEUrubCA1zA2jUe3b7Ju-3g_VxyDkK31KSnAUNM4O05WFk2emP6Krp3MH3u6IfcO3diZK4S5O9tTpruKFZXe0QGeu9va8OocE7CSUQHHXDzC6tQ9wks7u23a_NIQbs39gceCHeCwXUM0wKWuBqgK3ipp88jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : این جنگ ابدی نیست، ما کارها رو انجام می‌دیم و به خونه برمیگردیم
- این همون چیزیه که ترامپ وعده داده بود و همون چیزیه که او به اون عمل میکنه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/alonews/121168" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اکسیوس: به گفته دو مقام آمریکایی، دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه دوشنبه جلسه‌ای با تیم شورای امنیت ملی خود درباره ایران برگزار کرد که شامل ارائه گزارشی درباره گزینه‌های نظامی بود.
🔴
این جلسه چندین ساعت پس از آن برگزار شد که ترامپ اعلام کرد حملاتی…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/alonews/121167" target="_blank">📅 21:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121166">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اکسیوس:
به گفته دو مقام آمریکایی، دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه دوشنبه جلسه‌ای با تیم شورای امنیت ملی خود درباره ایران برگزار کرد که شامل ارائه گزارشی درباره گزینه‌های نظامی بود.
🔴
این جلسه چندین ساعت پس از آن برگزار شد که ترامپ اعلام کرد حملاتی را که مدعی بود برای سه‌شنبه برنامه‌ریزی شده بود، به حالت تعلیق درآورده است.
🔴
مقامات آمریکایی می‌گویند ترامپ پیش از اعلام توقف حمله، در واقع تصمیمی برای حمله به ایران نگرفته بود. روز سه‌شنبه، او گفت که «یک ساعت با دستور حمله فاصله داشته است».
🔴
برخی از مقامات انتظار داشتند ترامپ در جلسه‌ای با تیم امنیت ملی خود که انتظار می‌رفت سه‌شنبه برگزار شود، درباره حملات تصمیم بگیرد، اما این جلسه در نهایت شامگاه دوشنبه برگزار شد.
🔴
به گفته مقامات آمریکایی و منابع منطقه‌ای، تصمیم او برای خودداری از حمله، تا حدی به دلیل نگرانی‌هایی بود که چندین رهبر کشورهای عرب حاشیه خلیج فارس درباره تلافی‌جویی ایران علیه تأسیسات و زیرساخت‌های نفتی خود مطرح کردند.
🔴
مقامات آمریکایی گفتند که رهبران خلیج فارس از ترامپ خواستند فرصت دیگری به دیپلماسی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/alonews/121166" target="_blank">📅 21:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc00d765df.mp4?token=pNg205Bnp-OvnUNR39dBl1-t_WGj5ntgve-1w8dxy3qNTYVIO6UfBlKphARMxrmu2VEyK46qLSUCQn5zlFU4Z83rCYCYj15vRnTZK4Vw2-mB7daESXo7XI8fw3OC5MdpFDByYLc30PUbMcKrwuvSRG7k_nyjPbDCE04QMSn5qW5fXZ8C1_HqztpIiJh1XgmFfJRuNmxvqwUOQPgKCaFVhh-lsBUdIyxJDYGxOWyEWqxQJJbZD13On2KgRGXVdf3t_6Y3WoisBo5bBiHFVwYFdDnziwRyPznJkJXv9fR8EjaOA9u3-zmwAR8LThPPmN4hJlJikMkXLxNUcpkhE0OELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc00d765df.mp4?token=pNg205Bnp-OvnUNR39dBl1-t_WGj5ntgve-1w8dxy3qNTYVIO6UfBlKphARMxrmu2VEyK46qLSUCQn5zlFU4Z83rCYCYj15vRnTZK4Vw2-mB7daESXo7XI8fw3OC5MdpFDByYLc30PUbMcKrwuvSRG7k_nyjPbDCE04QMSn5qW5fXZ8C1_HqztpIiJh1XgmFfJRuNmxvqwUOQPgKCaFVhh-lsBUdIyxJDYGxOWyEWqxQJJbZD13On2KgRGXVdf3t_6Y3WoisBo5bBiHFVwYFdDnziwRyPznJkJXv9fR8EjaOA9u3-zmwAR8LThPPmN4hJlJikMkXLxNUcpkhE0OELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : هر وقت حمله پهپادی یا موشکی به هر جایی بخوره، مخصوصاً به مناطق غیرنظامی
- اصلاً چیزی نیست که خوشمون بیاد ببینیم
- ولی خب تو آتش‌بس‌ها این چیزا بعضی وقتا پیش میاد و همیشه همه‌چی کامل و بی‌نقص نیست؛ تو غزه هم دیدیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/alonews/121165" target="_blank">📅 21:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ونس: «چرا به اسلام‌آباد، پاکستان رفتم؟ چرا احتمالاً ۲۲ ساعت در هواپیما برای رفتن سپری کردم، ۲۴ ساعت برای برگشتن، و ۲۱ ساعت در آنجا با ایرانی‌ها مذاکره کردم؟ به این دلیل بود که ما می‌خواستیم نشانه‌ای از حسن‌نیت نشان دهیم. رئیس‌جمهور حاضر است توافق کند، تا زمانی که ایرانی‌ها حاضر باشند دوباره در آن مسئله اصلی یعنی هرگز نداشتن سلاح هسته‌ای، به سمت ما بیایند.
🔴
بنابراین، ما در وضعیت بسیار خوبی هستیم، اما یک گزینه B هم وجود دارد، و آن گزینه B این است که بتوانیم کارزار نظامی را از سر بگیریم تا پرونده را ادامه دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/121163" target="_blank">📅 21:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرمانده سنتکام:
بررسی بمباران مدرسه میناب پیچیده‌ست، چون این مدرسه در محل یک پایگاه فعال موشک‌های کروز در ایران قرار داشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121162" target="_blank">📅 21:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ادعای جی‌دی ونس درباره ایران: تحویل ذخایر اورانیوم غنی‌شده ایران به روسیه، در حال حاضر برنامه ما نیست. هیچ‌وقت برنامه ما نبوده است.
🔴
نمی‌دانم این گزارش‌ها از کجا می‌آید.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121161" target="_blank">📅 21:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ادعای جی‌دی ونس درباره ایران:
تحویل ذخایر اورانیوم غنی‌شده ایران به روسیه، در حال حاضر برنامه ما نیست. هیچ‌وقت برنامه ما نبوده است.
🔴
نمی‌دانم این گزارش‌ها از کجا می‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121160" target="_blank">📅 21:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fc576811f.mp4?token=bArF6hjnYLoprh_KR1dblCKgMuaARm0yT8y-eQB2xioLlalPBhkSw9rM8SHXJR46-35vgG62RYoNMYX3MltPH9EMBOO8ioHrUZ4pBhGNVX4CtPhP7f1xGFwaY0VUVToOPSLXs9euEntDi_xATQP402j0LDEdruV-qqAtl8t5xqijdBfXK20m5SJr00iP-A5UE1glyBIaNvdn8Iv6eCMvfKnQMxtJydxrY2gOHBgAEsIo5lG8NjGU3eFA72gE6X7oaMjQ9vfzOIKJmS8uBTr4qpE3iVVCp0tbI0m4MM7L1XoABTirQQme_zvKhOgAIvHfMhQpalVHSxJuuX_2Ef_A7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fc576811f.mp4?token=bArF6hjnYLoprh_KR1dblCKgMuaARm0yT8y-eQB2xioLlalPBhkSw9rM8SHXJR46-35vgG62RYoNMYX3MltPH9EMBOO8ioHrUZ4pBhGNVX4CtPhP7f1xGFwaY0VUVToOPSLXs9euEntDi_xATQP402j0LDEdruV-qqAtl8t5xqijdBfXK20m5SJr00iP-A5UE1glyBIaNvdn8Iv6eCMvfKnQMxtJydxrY2gOHBgAEsIo5lG8NjGU3eFA72gE6X7oaMjQ9vfzOIKJmS8uBTr4qpE3iVVCp0tbI0m4MM7L1XoABTirQQme_zvKhOgAIvHfMhQpalVHSxJuuX_2Ef_A7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : تو مذاکره با ایران پیشرفت زیادی داشتیم
- اما هر زمان که بخوایم میتونیم کمپین نظامی رو مجدد شروع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121159" target="_blank">📅 21:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69ee05e41.mp4?token=ddcARIC6nbkwrVTXb2dITTUMkbqkl2i90BoqYHH1F2TB9XX-eVxXfps8fjXJ-GHjVDdqy3ySkusfkwKFXnrZOmpB-yzqxLoRmguM39ir9UbXiHhzUUp5eLIOyyZ_QKT-yks8sHgOlEmt7achVP2mXn5uVKPOOomUKMrCyjJ4nNENgVU55ZKqL0NnyyVxeP9jyQ2WGO6pD0WkcrQEQo_OHw7ckRB5ysTSnWGS9fZbjH0QsPk4jEJ-4mjh1asGPt0QlY4iBD__GSQ21Jyji6qKUollEYloDr9zc_UAUFU43Cb58rtsEtcUgK0k9aliDcmflx3-tB4QXVeEjJghY5yczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69ee05e41.mp4?token=ddcARIC6nbkwrVTXb2dITTUMkbqkl2i90BoqYHH1F2TB9XX-eVxXfps8fjXJ-GHjVDdqy3ySkusfkwKFXnrZOmpB-yzqxLoRmguM39ir9UbXiHhzUUp5eLIOyyZ_QKT-yks8sHgOlEmt7achVP2mXn5uVKPOOomUKMrCyjJ4nNENgVU55ZKqL0NnyyVxeP9jyQ2WGO6pD0WkcrQEQo_OHw7ckRB5ysTSnWGS9fZbjH0QsPk4jEJ-4mjh1asGPt0QlY4iBD__GSQ21Jyji6qKUollEYloDr9zc_UAUFU43Cb58rtsEtcUgK0k9aliDcmflx3-tB4QXVeEjJghY5yczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما شخصاً فکر می‌کنید ایران به توافق می‌رسه؟
جی‌دی ونس :
- از کجا می‌تونم با قطعیت بدونم؟ فکر می‌کنم ایران‌ها می‌خوان به توافق برسن.
- خودشون هم می‌دونن که سلاح هسته‌ای خط قرمز آمریکاست. ولی تا وقتی توافق رو امضا نکنیم، هیچ چیز قطعی نیست.
- پیش‌نویس‌های زیادی هم داشته‌ایم، اما تا وقتی رسماً توافق نهایی امضا نشه، نمی‌تونم با اطمینان بگم به نتیجه می‌رسیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/121158" target="_blank">📅 21:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3761ff7f.mp4?token=P4ikidbeokiLAnWX0on7uNpPo80Zo_TDpCqPzyIhC27-sSUehaMs5NdqZ-C3-pZSdH1JRm_SZ4Pdpws-PaSgqujAtrZgS1J1Au5UAuk1huFsUOsD36LfEOY4liVlf-eXfmTiUu-a01fTnFRCgyw8C7OvZEdTpg-_D8BwHpLDrWWnwYrLA533UHGm92QGTGlQ25tw0z_PqgzfDJBJh-vtOnlXkqiDbOahkwCu1LWoX2J8-ZNoWLrAouK0lzuNqeY38yAQE0XdbDjzZNd85iA7AhODWgRrav2DY71viHigGEPzI-wqlITbO1NszmSIxx5_YPVmwifAff0DDWHdIKQehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3761ff7f.mp4?token=P4ikidbeokiLAnWX0on7uNpPo80Zo_TDpCqPzyIhC27-sSUehaMs5NdqZ-C3-pZSdH1JRm_SZ4Pdpws-PaSgqujAtrZgS1J1Au5UAuk1huFsUOsD36LfEOY4liVlf-eXfmTiUu-a01fTnFRCgyw8C7OvZEdTpg-_D8BwHpLDrWWnwYrLA533UHGm92QGTGlQ25tw0z_PqgzfDJBJh-vtOnlXkqiDbOahkwCu1LWoX2J8-ZNoWLrAouK0lzuNqeY38yAQE0XdbDjzZNd85iA7AhODWgRrav2DY71viHigGEPzI-wqlITbO1NszmSIxx5_YPVmwifAff0DDWHdIKQehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد ایران:
گاهی کاملا مشخص نیست که موضع مذاکره تیم ایران چیست.
🔴
گاهی اوقات سخت است که دقیقا بفهمیم ایرانی ها می خواهند از مذاکرات چه کاری انجام دهند.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/121157" target="_blank">📅 21:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a328cbc57.mp4?token=MSVsM5IcZK59epGqqyT2dGxlgPCRSBn145fgNG7RwDY5BRgx9NJ_4npUhxlpO6mqKMlnn3ZWC8qDYOwV9KNKePsqphgUA9eGS7IVAAEqldyyPr9bZEXFf8Yq0NT-vowYgPF3bqQy_znS9jpOmQOu9MX8cScxsEjVlXsTNMwdQdktebze0wSMYQNp3_2IX0h4toAq6pCdY2hMGNCmQDuXQsXPUcraUoSjG4hhypn5S56WuJVdy340oMxskH5FK2pu1b_1fSZOv9QnN7lXf93y37wOLyqzN1AnZYguPjmTZFbqJVxp5HpX5ojKlHY0PBojmFz71gP02L0Z0wncrGN0s4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a328cbc57.mp4?token=MSVsM5IcZK59epGqqyT2dGxlgPCRSBn145fgNG7RwDY5BRgx9NJ_4npUhxlpO6mqKMlnn3ZWC8qDYOwV9KNKePsqphgUA9eGS7IVAAEqldyyPr9bZEXFf8Yq0NT-vowYgPF3bqQy_znS9jpOmQOu9MX8cScxsEjVlXsTNMwdQdktebze0wSMYQNp3_2IX0h4toAq6pCdY2hMGNCmQDuXQsXPUcraUoSjG4hhypn5S56WuJVdy340oMxskH5FK2pu1b_1fSZOv9QnN7lXf93y37wOLyqzN1AnZYguPjmTZFbqJVxp5HpX5ojKlHY0PBojmFz71gP02L0Z0wncrGN0s4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد ایران:
ایران یک کشور بسیار پیچیده است. این کشوری است که من وانمود نمی کنم که می فهمم...
🔴
این یک تمدن بزرگ و افتخارآمیز است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/121156" target="_blank">📅 21:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121155">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f39267e3d.mp4?token=mPB-y2pFAZ55IfvYzfq1Ju4nF_wBiArgs_ExxaY-2FS9GJATIqbcHyM4gjc_ITrZGmp5Sj9yDy4c_PwuytQVTieBslEovSZUD6-NX9FEMp99zBpN0PJZPQlLWSocmBiNH04x8T3O1dx9lHA923DeHp8pI49bzqHA5igKNfGX7UWEDHOMzUHreH5olULLD8i26uFg5qqO5ZoOsunsgVfk50G0eaOREtk2hh_PF1h3pAJWUAH2FucSA0NcfSuWXM8dSF3A9giSx0W7qfvZVUSSSZYvdM1rVqrcsQTMgvxmny_tm5quJ4E_TWWOJwR1Coy8pz2K-Kl_zhhkdzOH4Ai3OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f39267e3d.mp4?token=mPB-y2pFAZ55IfvYzfq1Ju4nF_wBiArgs_ExxaY-2FS9GJATIqbcHyM4gjc_ITrZGmp5Sj9yDy4c_PwuytQVTieBslEovSZUD6-NX9FEMp99zBpN0PJZPQlLWSocmBiNH04x8T3O1dx9lHA923DeHp8pI49bzqHA5igKNfGX7UWEDHOMzUHreH5olULLD8i26uFg5qqO5ZoOsunsgVfk50G0eaOREtk2hh_PF1h3pAJWUAH2FucSA0NcfSuWXM8dSF3A9giSx0W7qfvZVUSSSZYvdM1rVqrcsQTMgvxmny_tm5quJ4E_TWWOJwR1Coy8pz2K-Kl_zhhkdzOH4Ai3OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
«فکر می‌کنم ما در اینجا یک فرصت داریم تا رابطه‌ای که به مدت ۴۷ سال بین ایران و ایالات متحده وجود داشته است، از نو تعریف کنیم.
🔴
این همان چیزی است که رئیس‌جمهور از ما خواسته است، و ما به کار روی آن ادامه خواهیم داد، اما برای یک رابطه دو طرفه، دو طرف لازم هستند (رقص تانگو دو نفر می‌خواهد). ما هیچ توافقی را که به ایرانی‌ها اجازه دهد سلاح هسته‌ای داشته باشند، نخواهیم پذیرفت.
🔴
بنابراین، همانطور که رئیس‌جمهور همین الان به من گفت، ما در حالت آماده‌باش هستیم. ما نمی‌خواهیم وارد آن مسیر شویم، اما رئیس‌جمهور اراده و توانایی آن را دارد که در صورت لزوم وارد آن مسیر شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121155" target="_blank">📅 21:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121154">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
شبکه کان اسرائیل:
ایران ممکنه حملات پیش دستانه کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121154" target="_blank">📅 21:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989f37ccbf.mp4?token=ZTM8eAhq4rIoXi1jJ4xuDLJCRfBYR2JEgPTHV7bSD4ajAnbVEjZk2GyXWVEuVaGRtJS7Q77gjxtJILChOs9BeSKQ3nLEUiOXsQd38UhSvqFqJMPQMHtB1qLaXYzChzn_d3khKrte7M86wVbsbEmCiTz2ja0AwS1s-1IJ3WNB4ybXzbH5SNmZA67NrhV7uoTtesaiAypZ6WeNGrJ-w8cwa-hRBdKJrx23uWrlUS3OvJ7HtaFh49UzNNS2E_dW6_Gp0-tjt-7kbHwlnvf8vgZoAHHhZnuoYyqTHQQhGHRB8UEYAEsVdGvEYt51n2piIIo3WRDWsMstauyrAoSqL69cew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989f37ccbf.mp4?token=ZTM8eAhq4rIoXi1jJ4xuDLJCRfBYR2JEgPTHV7bSD4ajAnbVEjZk2GyXWVEuVaGRtJS7Q77gjxtJILChOs9BeSKQ3nLEUiOXsQd38UhSvqFqJMPQMHtB1qLaXYzChzn_d3khKrte7M86wVbsbEmCiTz2ja0AwS1s-1IJ3WNB4ybXzbH5SNmZA67NrhV7uoTtesaiAypZ6WeNGrJ-w8cwa-hRBdKJrx23uWrlUS3OvJ7HtaFh49UzNNS2E_dW6_Gp0-tjt-7kbHwlnvf8vgZoAHHhZnuoYyqTHQQhGHRB8UEYAEsVdGvEYt51n2piIIo3WRDWsMstauyrAoSqL69cew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس شبکه ۱۴ اسرائیل : تقربیاً حوثی‌ها شش ماهه که از ایرانی‌ها پولی دریافت نکردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121153" target="_blank">📅 21:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSs_M0I4sZFoYs3MGsXFT8pla67eC1lvmE0cj1li_IPLYQF6E06erxd7cfwc5rGuaDUYcaUH5lM_fwXUkjU76XWZFMHFn-mFruRYfLVfK_mHG6IW0HXgwyocxoie-BXv_6OdNqqxmr0o3Ny3gltskq2Gkre24VdMMQWX3FEBST8S4-r13OGD-U3mkDzErEd7DR5kffa-x8lup50LOzU339A3KOqy7blVgvBhFQQuVtMfoivddbtT40LwgBzwULwQYEOG-EGMng5hzFna3bdDRrVqYPHyPv0LfGE6CpYQKZOMvx_dohA_jh96A4pqapekgku1ou4_fXfNPnPaEHfBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین :
@v2safeBot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121152" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMGzJMqSFYw7u-UGmLNy5i1PntG_x6OjE_NWlQXHi6TS_b5l31a14IMZ8ah8Pk_ZvqdgMcs_EjafffDju6_V1EHCCJj4D-hnBgLCNFYopEB95Tnwu9AAMlypIEXXVt1QBmGE1-73fvi9yuFREcNZJrnIVjBJ8bzbo0Po8FNU5_gmRaZb_uz7pszDm_dVCoxp7PExldrtleZmy_j4RlLVoc2ljTtmgUcXmKVVIeLt_H-UayZQTGfGH9UAfl8UuMZO-Kwp-hdAtd4LXzE3N-aeltsrLbF7u6KVi70-oeqxpnkYVSQjV1f81UeUrq3Uo2VYQokXJqpxwDIlGNSfyeXfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kd_fHvhGVSsu9-8L9SwokWiLc5_h_ggtUUxsq2QEvSxOkRU1uOeUXwqGXdvS9KqAq34roTz8zBMa0oyUvmhQTPBxZHudSoT0WNmDZH2-2QQuVpUk9p-SNYgSQPXZySMmoLB9LGvpX7IwdddKJT9KSDs57uM6UaqjPXIZHU7A5bZquemiEYMoAo91x6RPBv-35vFLUogidZ4OXx78BDHMZogB3VB5Tn9Njz50xwX4YbR5XYZJQ0pNK8fAp1BU90-UQpxHVB2Pe4ayq_nNvpM7VEaC5AorTEjhfZr-9YI2U-g3mpEctHHkFr1gNlZFWGeeynouw9Mur2K1T-p1hpudlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یاشار سلطانی، روزنامه‌نگار:
درحالی که هرشب تو تجمعات حکومتی شعار "بی‌حجاب هم خواهر ماست" میدن و خانم‌ها با پوشش آزاد میگردن، دیشب هتل تاریخی|سنتی عامری‌ها تو کاشان رو به دلیل "حجاب" پلمپ کردن و 90 نفر پرسنل اونجا هم بیکار شدن.
🔴
حالتون از این همه تناقض و دورویی به هم نمیخوره؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121150" target="_blank">📅 20:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو باز هم به دلایل امنیتی درخواست کرده است که فردا در دادگاهش برگزار نشود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121149" target="_blank">📅 20:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnpuvrw1GjwVMtsZT16BUv-HYXQBxFBd4PL0Lzuj1OXjWTTy5wwt5exsdM6ePOtL-7juErMagdOjG6J1U-Ayblaxpgr_9_n29fiBz5JjndlG4mf_mVgzbil6weQhLlAekVleXau5jtAuxEb7AjUbQPqqq4g5N1doOleSubkEbGx6IDAGP-hkVd4HWpM6DZH4c9YybUMXWeaGrafsXOuyvZD1BGUOfvJfnRPqi4GUQ7obWxigwFsvWVWDzpzutukHgBrsNPb-zP3lqFLdi4-QgBVudXLcVKiMYJH90wpLNsi3gzncGZxsmIDZbYD_RHuycPxHELoefWMNYDhHOJ7PfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده سنتکام، دریادار کوپر :
- ایران از وقتی آتش‌بس شروع شده، ده‌ها نفر رو اعدام کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121148" target="_blank">📅 20:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: یک افسر ارتش اسرائیل در جنوب لبنان کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121147" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زاکانی: تا زمان رسیدگی و نتیجه نهایی طرح رایگان بودن وسایل نقلیه، خدمات به منوال قبل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121146" target="_blank">📅 20:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اسرائیل هیوم: نتانیاهو به دلایل امنیتی درخواست کرده است که فردا در دادگاهش برگزار نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121145" target="_blank">📅 20:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: ارزیابی‌های اسرائیل نشان می‌دهد که ترامپ تصمیم حمله به ایران را گرفته است و اجرای آن فقط مربوط به مسئله زمان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121144" target="_blank">📅 20:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرمانده سنتکام : چند تا ناوشکن آمریکایی اخیراً از تنگه هرمز عبور کردن
🔴
ایران از هر نظر خیلی ضعیف‌تر از قبل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121143" target="_blank">📅 20:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رابرت مالی رئیس هیات مذاکره کننده آمریکا در دوره بایدن: مدتهاست که زمان آن فرا رسیده که کاری را انجام دهیم که برای بسیاری از ما غیرممکن به نظر می‌رسد، و آن این است که به حرف‌های ترامپ اصلاً هیچ توجهی نکنیم.
🔴
این بدان معنا نیست که او حمله نخواهد کرد؛ به این معنا نیست که حتماً حمله خواهد کرد.
🔴
معنایش این است که حرفی که او یک روز می‌زند، هیچ نسبتی با واقعیت ندارد و هیچ نسبتی با حرفی که روز بعد خواهد زد، ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121142" target="_blank">📅 19:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO7fVBlwUIRfOVf0BbchVZNC8-7Zm-__ddjneTJc-ohh_kEMF95S6skjXxqqye0U5kutW2UG75xVF385Lmzm2u_oHgjKSrYbLZmvYfZIIsq81MAPlKqOPW03zDJX9_KezL2jp5s7uA61Efc1I-1JSunmLmAg19ZGBCzAQ92fJCuHrVudPsT2PTThGZyHpBtgEPM4CwJG99zW2ox19L5Z7EE6BDW2GHuHK8ACLKsoRcyHYWvGtzhOr0P-2261l3jYkjkhD9g8yV9wgaGD2Zez84h_BvSPW2ExJCvLd6HnsmF8O9Nl1tgrm6sQyrg1sWRzoHBzjsOvSMVn195GI89JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب‌آبادی
:
برای ما تسلیم شدن معنایی ندارد؛ یا پیروز می شویم یا شهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121141" target="_blank">📅 19:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آتلانتیک: دو هواپیمای سوخت‌رسان KC-135 آمریکایی در تاریخ ۱۲ مارس بر فراز عراق با هم برخورد کردند و شش نفر کشته شدند.
🔴
پنتاگون اعلام کرد هیچ آتش خصمانه‌ای در کار نبوده است.
🔴
اما گزارش‌های اولیه اطلاعاتی، آتش پدافند هوایی شبه‌نظامیان تحت حمایت ایران را در آن منطقه در آن زمان شناسایی کردند که نشان می‌دهد خلبانان ممکن است اقدام به گریز کرده باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121140" target="_blank">📅 19:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صداوسیما: ایران می‌تواند اینترنت امارات و قطر را قطع کند/ایران می‌تواند شرکت‌هایی مانند اینستاگرام را با اهرم فشار اینترنت تنگه هرمز پاسخگو کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/121139" target="_blank">📅 19:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0VFX0_jLdD1sfpOebP4svKhMMvw1BV9C_31aGrvfdb9MH-Qv8yKd8OYyqLQ2TF0zErgYbvBUsQpJ2q-MTOsDUBTdZhHO7gs19iKk4fVehoUexMQysxPyUt6-zYVATl7KZE6_yZRdjVhjRMQQmuu2IQShNnYWZGjL2rPPZl_6qvocTOshZcqphNYWYMX1EWZCGywmUWrpNHgyMhh7U0ycG8ZJtg5FadapceT5-9gWbFwfWdLnCVnrtHHRrtnYM_pLrdsDLuOwZ5r3hh68d44mI5p7xdJXDCGgY4iDSo0aCj_Q4WKizONvxBpT3CklPD-JsngtgeRFlXmGYXrVaf92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۱۰.۴۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121138" target="_blank">📅 19:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ارتش پاکستان اعلام کرد ۲۲ تروریست را در عملیاتی در شمال غربی پاکستان کشته است.
🔴
این عملیات در وزیرستان شمالی صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121137" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بلومبرگ: به گفته یک مقام ارشد در ناتو، این سازمان در حال بررسی امکان کمک به عبور کشتی‌ها از تنگه مسدود شده هرمز است، در صورتی که این آبراه تا اوایل ژوئیه(اواسط تیر) بازگشایی نشود.
🔴
یک دیپلمات از یکی از کشورهای عضو ناتو گفت که این ایده از حمایت چندین عضو پیمان آتلانتیک شمالی برخوردار است، اما هنوز حمایت اتفاق آرای لازم را ندارد.
🔴
رهبران کشورهای عضو ناتو در تاریخ ۷-۸ ژوئیه در آنکارا دیدار خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121136" target="_blank">📅 18:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: متحدان اروپایی باید با بستن شعب بانکی و توقیف دارایی‌های ایران، اجرای تحریم‌ها علیه این کشور را تقویت کنند.
🔴
متحدان آسیایی ما باید ناوگان سایه ایران را زیر نظر داشته باشند تا از حمل نفت توسط نفتکش‌هایی که مشمول تحریم نیستند، جلوگیری شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121135" target="_blank">📅 18:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ادعای نشنال اینترست: ناوگان قایق‌های تندروی ایران تهدید بسیار جدی محسوب می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121134" target="_blank">📅 18:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: پوتین به چین رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121133" target="_blank">📅 18:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cd783799.mp4?token=l0bGW1nc0dkV1pW9vTPSCgVt-jFgJ90tfpikEOcAiYlpHBvt3-nc4GRtZtbNOXXY4ys-WucCwqqAX6Hb-p83zRa0r5IqgDXdadIjz388_m12KFYJc8dsUz8BOwxVJ_7rEmtlJboaMOeeuJuxegBFS8lFpffL4CuBMTnhwUL7FOD_tgh839Amcek3Q-_7pIW_0Pr_kDJGWwNQSB5RzpcG4ahkKLhXfF6DdpmAMupGbDslX5hThnbKNL-hurOQ15Er5iu-7LOmxHEitt2bH4qixgBCSIvhrtSgCDN8V70RD4Y5icREoRq2sb8yoCHF2U_xSyj0beDO51CTNQMD0kCNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cd783799.mp4?token=l0bGW1nc0dkV1pW9vTPSCgVt-jFgJ90tfpikEOcAiYlpHBvt3-nc4GRtZtbNOXXY4ys-WucCwqqAX6Hb-p83zRa0r5IqgDXdadIjz388_m12KFYJc8dsUz8BOwxVJ_7rEmtlJboaMOeeuJuxegBFS8lFpffL4CuBMTnhwUL7FOD_tgh839Amcek3Q-_7pIW_0Pr_kDJGWwNQSB5RzpcG4ahkKLhXfF6DdpmAMupGbDslX5hThnbKNL-hurOQ15Er5iu-7LOmxHEitt2bH4qixgBCSIvhrtSgCDN8V70RD4Y5icREoRq2sb8yoCHF2U_xSyj0beDO51CTNQMD0kCNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا رئیس‌جمهور شی گفت که پوتین از حمله به اوکراین پشیمان خواهد شد؟
🔴
ترامپ: نه. او هرگز چنین چیزی نگفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121132" target="_blank">📅 18:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcbe32ed97.mp4?token=bWHYsA33XOqm9vYmF0MD8rDe10jhXZBSmgGUDKQJ8vpvQlQJgFVhODZZ8d_J_xfEFpno7WB7BkHIMGdERKDqUQGhXav4jn_2eBaqGVD2Ozqrseki9AQPAAJtqMi_WVz4AN2hDRbTOaPxvdF87m1RgG2ksz0Q2LZHtSKYIf27BrwmXuKUJcpVLb8Cwaq2rWbZeHXT-rdFJNlgCHK-p26CdO5G2se1k9ZXBj6BqEJejsUOJRI-cBBlMJXZYt1p32nz5ObstNXEzF8Y2-RZApPM9-HbfwFZO9xtU5aVf0Bluc1yO5RANfL6kPO1IcruyBmTUix1MqKLUgq9guq1jEB-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcbe32ed97.mp4?token=bWHYsA33XOqm9vYmF0MD8rDe10jhXZBSmgGUDKQJ8vpvQlQJgFVhODZZ8d_J_xfEFpno7WB7BkHIMGdERKDqUQGhXav4jn_2eBaqGVD2Ozqrseki9AQPAAJtqMi_WVz4AN2hDRbTOaPxvdF87m1RgG2ksz0Q2LZHtSKYIf27BrwmXuKUJcpVLb8Cwaq2rWbZeHXT-rdFJNlgCHK-p26CdO5G2se1k9ZXBj6BqEJejsUOJRI-cBBlMJXZYt1p32nz5ObstNXEzF8Y2-RZApPM9-HbfwFZO9xtU5aVf0Bluc1yO5RANfL6kPO1IcruyBmTUix1MqKLUgq9guq1jEB-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر امروز می‌رفتم(حمله می کردم)، بازسازی آن‌ها ۲۵ سال طول می‌کشید.
🔴
اما ما در حال ترک نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121131" target="_blank">📅 18:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ درباره ایران: تنگه هرمز مال ایران نیست. تنگه در آب‌های بین‌المللی است، این به آنها مربوط نیست که چنین کاری کنند! آنها درس خود را آموخته‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121130" target="_blank">📅 18:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ درباره ایران: «رئیس‌جمهور چین به من قول داده است که هیچ سلاحی به ایران ارسال نمی‌کند. این یک قول زیباست.
🔴
حرف او را قبول دارم. از این بابت قدردانی می‌کنم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121129" target="_blank">📅 18:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e7462ece.mp4?token=hmFSeuyeO_S3eqPdAWMY0Cmv1avvYs9WyV50OBWeGheWttUP_C2onB0ySZ9Xatpf6R__fR7BzNrdRNzVz-9cxTbOftEYGGUWPDLsVg90LOJgFCmuZxTT6HzMYPF26pBNTdnO9fvGq9k2kMpCUHwicgprVfZwZvJEn2SS0CcckPhNewG98NWUlyOS4HLPW4FkV54tnxMJJ_4Sv8jN4rR42LOhAewd4IDClVarcPGE1vLbo82Oh7V9u9oCjUDRUAfKHgYnypYg20o-FSlb3TjZi014qBPTqBu8kU5oremqC8_2bmNRcEWNlAj9pBC5noIglF_Mhqg-nFCyLtbDn-OWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e7462ece.mp4?token=hmFSeuyeO_S3eqPdAWMY0Cmv1avvYs9WyV50OBWeGheWttUP_C2onB0ySZ9Xatpf6R__fR7BzNrdRNzVz-9cxTbOftEYGGUWPDLsVg90LOJgFCmuZxTT6HzMYPF26pBNTdnO9fvGq9k2kMpCUHwicgprVfZwZvJEn2SS0CcckPhNewG98NWUlyOS4HLPW4FkV54tnxMJJ_4Sv8jN4rR42LOhAewd4IDClVarcPGE1vLbo82Oh7V9u9oCjUDRUAfKHgYnypYg20o-FSlb3TjZi014qBPTqBu8kU5oremqC8_2bmNRcEWNlAj9pBC5noIglF_Mhqg-nFCyLtbDn-OWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: توماس ماسی یک نماینده کنگره وحشتناک است. او از روز اول یک نماینده وحشتناک بوده است. برخورد با او واقعاً وحشتناک است.
🔴
فکر نمی‌کنم او جمهوری‌خواه باشد. فکر می‌کنم در واقع یک «دموکرات احمق» است. او لیبرتارین نیست.
🔴
او همیشه علیه ما رأی می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121128" target="_blank">📅 18:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: چه اقدام نظامی علیه ایران با حمایت مردمی روبرو شود و چه نشود، من اجازه نخواهم داد دنیا جلوی چشمانم منفجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121127" target="_blank">📅 18:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=ZgEUwJC0N5BesdN_5OoRqvUlSLsczVdMTUR05wj9iyAKuDFtChmgXrbdWxsTs7r-bRwB-Q4uVz8dY4PZHBSyz0q9qUxdWZ9XKp1J1rOVM72NWeoCRefUP3QvLhL2XcLaswAOB7RxbIbpLnx9JveQLeYlB6pTCSiYOKE9KddueBqSOUda1H3gjdIVsgSucGjkeLPdS4DIwl3BWUdVbRkf0NU_Czv4VkwossP6Qcij6xt4lmsM_eLJlSdIJnWd_S5MtjTEmceRrgDSoUVNWYhXbUQy1OUQX8HNSPj7Tf1v_gywNAF3bsujbm0g4CF9KZlc-ulcymqQw4UTYHmzHB7qMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=ZgEUwJC0N5BesdN_5OoRqvUlSLsczVdMTUR05wj9iyAKuDFtChmgXrbdWxsTs7r-bRwB-Q4uVz8dY4PZHBSyz0q9qUxdWZ9XKp1J1rOVM72NWeoCRefUP3QvLhL2XcLaswAOB7RxbIbpLnx9JveQLeYlB6pTCSiYOKE9KddueBqSOUda1H3gjdIVsgSucGjkeLPdS4DIwl3BWUdVbRkf0NU_Czv4VkwossP6Qcij6xt4lmsM_eLJlSdIJnWd_S5MtjTEmceRrgDSoUVNWYhXbUQy1OUQX8HNSPj7Tf1v_gywNAF3bsujbm0g4CF9KZlc-ulcymqQw4UTYHmzHB7qMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران چند روز فرصت دارد تا به میز مذاکره بیاید؟
🔴
ترامپ: دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک دوره زمانی محدود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121126" target="_blank">📅 18:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ درباره ایران: پس آنها (کشورهای خلیج) تماس گرفتند؛ شنیده بودند که من تصمیم به حمله گرفته‌ام.
🔴
گفتند، «آقا، می‌توانید چند روز دیگر به ما فرصت دهید چون فکر می‌کنیم آنها منطقی رفتار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121125" target="_blank">📅 18:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ درباره ایران: «فکر می‌کنم گرفتن غبار هسته‌ای (ذخایر اورانیوم) مهم است، شاید از نظر روانی بیشتر از هر چیز دیگری مهم باشد.»
🔴
«همه به من می‌گویند این جنگ نامحبوب است، اما من فکر می‌کنم بسیار محبوب است.
🔴
وقت کافی ندارم که جنگ را برای مردم توضیح دهم. من خیلی مشغول آن هستم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121124" target="_blank">📅 18:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: ما باید کشوری امن داشته باشیم و باید اطمینان حاصل کنیم که ایران به سلاح هسته‌ای دست پیدا نمی‌کند.
🔴
ایران نباید به سلاح هسته‌ای دست یابد.
🔴
دموکرات‌ها تلاش می‌کنند مانع مذاکره من با ایران شوند
🔴
ایران می‌خواهد خاورمیانه را نابود کند و این اتفاق نخواهد افتاد.
🔴
رهبرانی هستند که در دو روز گذشته با من تماس گرفته‌اند و گفته‌اند که پیشرفت قابل توجهی در مورد ایران حاصل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121123" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121122">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
هم اکنون ترامپ در مورد ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آن‌ها بزنیم. هنوز مطمئن نیستم.
🔴
خیلی زود خواهید فهمید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121122" target="_blank">📅 18:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121121">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=T2NPQRQSdHGhv_VI6uCoIUre5OIxAOZxmavbfywTy9eivpCNaOHQs0UMWzJuk7am9JOkY-WUoaC4dxNuFzeSTqwy-ouIChTy3DeQWZsvqqs_hbmpSH05SrLGX7fazxiyRUwgZ1ioEzQtd12VXTl5ktHWXPvDAkkTnq6JpcDpL18__uhiKYpJjJ-ByYJNlLMiEqqpeKVkaJ5a24LsSiQIWjwQ5iNRgSJ4VqwhH3stIVNX9TYrs-yBl9HwV8NoApeS4SXcoh0UsdkMvZxMZVuV_NAtDz_WM7IWMWW3b7s8RkmLTDhE6EewEcjNoYjd8knjJb1WAF23Qhp_SNpFtJS2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d31e39e6b.mp4?token=T2NPQRQSdHGhv_VI6uCoIUre5OIxAOZxmavbfywTy9eivpCNaOHQs0UMWzJuk7am9JOkY-WUoaC4dxNuFzeSTqwy-ouIChTy3DeQWZsvqqs_hbmpSH05SrLGX7fazxiyRUwgZ1ioEzQtd12VXTl5ktHWXPvDAkkTnq6JpcDpL18__uhiKYpJjJ-ByYJNlLMiEqqpeKVkaJ5a24LsSiQIWjwQ5iNRgSJ4VqwhH3stIVNX9TYrs-yBl9HwV8NoApeS4SXcoh0UsdkMvZxMZVuV_NAtDz_WM7IWMWW3b7s8RkmLTDhE6EewEcjNoYjd8knjJb1WAF23Qhp_SNpFtJS2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🔴
ترامپ: یک ساعت فاصله داشتم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121121" target="_blank">📅 18:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری /  ترامپ درباره زمان حمله به ایران: «۲-۳ روز دیگر، شاید جمعه یا شنبه، اوایل هفته آینده. یک دوره زمانی محدود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121120" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت دفاع امارات ادعا کرد که سامانه‌های پدافند هوایی در ۴۸ ساعت گذشته، ۶ فروند پهپاد را رهگیری کرده‌اند.
🔴
تحقیقات روشن کردند که حمله پهپادی ۲۷ اردیبهشت (۱۷ مه) به نیروگاه هسته‌ای برکه از عراق انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121119" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56750e37ce.mp4?token=qA50KJHIRkcoH9HTJqs4M45uaMxUL9KxhvIoHhAK55REjJZIrgRvoiHRdNkyX2H8kTM9HgROC6LFydmRQsJvpoNImOfGTMVHi31cawita8u64NxU7w2prWKc2zcpthQnzU2rl9v3MzHkrJVTGt_ghUtS63mDL4RX98mlhhXISerSkjUFiOblToiRfqm1NV-OnXbD8zMqaQB9JJeRb9j02LKlHIpIndDS68r5PqEaoJQGiLWCY9cP-N19ugDCyaZwFzFun_F1dp5WXkhvOzyFLYHbRU4wLBuQU0BzFVpex83H5Kez0EqrY-lpFyL_i2QK93G3aAd6tVisaa32tKnYjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56750e37ce.mp4?token=qA50KJHIRkcoH9HTJqs4M45uaMxUL9KxhvIoHhAK55REjJZIrgRvoiHRdNkyX2H8kTM9HgROC6LFydmRQsJvpoNImOfGTMVHi31cawita8u64NxU7w2prWKc2zcpthQnzU2rl9v3MzHkrJVTGt_ghUtS63mDL4RX98mlhhXISerSkjUFiOblToiRfqm1NV-OnXbD8zMqaQB9JJeRb9j02LKlHIpIndDS68r5PqEaoJQGiLWCY9cP-N19ugDCyaZwFzFun_F1dp5WXkhvOzyFLYHbRU4wLBuQU0BzFVpex83H5Kez0EqrY-lpFyL_i2QK93G3aAd6tVisaa32tKnYjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سالن رقص کاخ سفید:
تمام این هزینه‌ها را خودم پرداخت کرده‌ام. این یک هدیه است.
🔴
این هدیه‌ای به ایالات متحده آمریکا است
🔴
این بیش از یک هدیه است؛ این قرار است یکی از زیباترین ساختمان‌هایی باشد که تاکنون در کشور یا در واشنگتن دی‌سی ساخته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121118" target="_blank">📅 18:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b9680b69.mp4?token=MEdwlrfIdMtmMajGvbfU9Dg7V1E7rska3Vr32_N8-rzZej5hUBQtqNFHKDxPslZKv0WRAbQ5OgBQMZwYQY_i8kA02c1sH5gBQbqiyLh7NMU9M5cJ1EUp5jHITCIKJiO3TAaI2S9osH6o_wDm7AxuIxaHGC4M4UYgtg_DciEhKKKhciX5TEWP24YGYIVOjMU-K73JYCvsu06nSzlOvqzthLAvZo1AXOvxW2_fYHYhlOJb52KGcjMpazpCGkmRl6ha8YwxSdrZKb89gO6fuWSlLRGsoi6N21l7cq7OO-_YMN6xMWGQFAzt-tAwFwlUSfBt_GRTMJ9n8CCTfCNx8vBTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b9680b69.mp4?token=MEdwlrfIdMtmMajGvbfU9Dg7V1E7rska3Vr32_N8-rzZej5hUBQtqNFHKDxPslZKv0WRAbQ5OgBQMZwYQY_i8kA02c1sH5gBQbqiyLh7NMU9M5cJ1EUp5jHITCIKJiO3TAaI2S9osH6o_wDm7AxuIxaHGC4M4UYgtg_DciEhKKKhciX5TEWP24YGYIVOjMU-K73JYCvsu06nSzlOvqzthLAvZo1AXOvxW2_fYHYhlOJb52KGcjMpazpCGkmRl6ha8YwxSdrZKb89gO6fuWSlLRGsoi6N21l7cq7OO-_YMN6xMWGQFAzt-tAwFwlUSfBt_GRTMJ9n8CCTfCNx8vBTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارشد ناتو، الکسوس گرینکوویچ: در مجموع ۵۰۰۰ نیروی نظامی آمریکا از اروپا خارج خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121117" target="_blank">📅 17:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت دفاع امارات متحده عربی مدعی شد نتایج تحقیقات فنی مربوط به حمله به نیروگاه هسته‌ای براکه در تاریخ ۱۷ مه ۲۰۲۶ تأیید کرد که هر سه پهپاد مهاجم از خاک عراق پرواز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121116" target="_blank">📅 17:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ادعای امارات: طی ۴۸ ساعت گذشته با ۶ پهپاد که قصد داشتند مناطق مسکونی و حیاتی را هدف قرار دهند، مقابله کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121115" target="_blank">📅 17:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاون وزیر خارجه ایران : ایران آماده‌ست با هر جور تجاوز نظامی روبرو بشه، ما یا پیروز می‌شویم یا شهید می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121114" target="_blank">📅 17:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121113">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ7K0a9VFfmmt6OCXARSg1mAMYirz55EmlF-PMF_cuVUsWupvuNgwNMwVwPVkmhzp9BdtD9tl7jWh3LzVViSm-u8lJK8P56x5IPxVwhgM00F4AlSgdv6fFaY3TSC8UDfRPRbah_ic1Is94GDVdG5tUXTxStdSWyLlX85oN4uA-HS8wW5efxLK-rkHNkM-_JA9838i0YqqXl1dAm3lqCk0FgbmarkjMXdjoyFnNfqCSkUtHMOsAOiCu8RmF3k0IPU1I7RRggK2FqHYmBkQDxPu1-vMJ0eGgrvQGnSK3fLV4Yx6fN_KVLB-jyxsz6s10fFza04XZm37Z0-L192LG2FBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نرخ دلار امروز، ۱۷۸,۵۴۸ هزارتومن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121113" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/ef61b8367d.mp4?token=YfkpZZqCxOEoSPUHkRwo37nD7Xx35t30Tvk3yDI3SdJ0y76ZZZUm-lqRvm2ZZYjFXkj0nDQQuzCyAeo5Qv5Tgd7dkPJsD2l4C7XmkWt4gDmMGG1F2ZwmSgFTXvFXhWQ5nQ5CZTRF2bEIiwzkrRFarjfN_cyszr3URgEmWKVIWB9s0CKu3o56PkADtwJEKEzX2xHH4Uxa4SuaQU1lLu_NFpDiREyaLgbIxmpo0dD9caQONLYoextsUTZW-eX4WRbMN3Fpp9w56o5iKFeo9hgfm1lykAobh-70x1qa5CoGv3El9EcoO_o67NjDKQzyFqINoQdc_FvOz1ZNFQpM3Gq1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/ef61b8367d.mp4?token=YfkpZZqCxOEoSPUHkRwo37nD7Xx35t30Tvk3yDI3SdJ0y76ZZZUm-lqRvm2ZZYjFXkj0nDQQuzCyAeo5Qv5Tgd7dkPJsD2l4C7XmkWt4gDmMGG1F2ZwmSgFTXvFXhWQ5nQ5CZTRF2bEIiwzkrRFarjfN_cyszr3URgEmWKVIWB9s0CKu3o56PkADtwJEKEzX2xHH4Uxa4SuaQU1lLu_NFpDiREyaLgbIxmpo0dD9caQONLYoextsUTZW-eX4WRbMN3Fpp9w56o5iKFeo9hgfm1lykAobh-70x1qa5CoGv3El9EcoO_o67NjDKQzyFqINoQdc_FvOz1ZNFQpM3Gq1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار یک وسیله نقلیه حامل بمب دست‌ساز در نزدیکی ساختمان وزارت دفاع بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121110" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت بهداشت لبنان از آغاز حمله اسرائیل در دوم مارس، 3042 کشته و 9301 زخمی گزارش می دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121109" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سفیر چین در تهران: حمایت پکن از ایران، آشکار و بی‌چون و چرا است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121108" target="_blank">📅 17:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دراپ‌سایت: براساس داده‌های ردیابی کشتی‌ها از Lloyds List Intelligence، ترافیک عبوری از تنگه هرمز در هفته ۱۱ تا ۱۷ مه به ۵۴ فروند کشتی افزایش یافت که بیش از دو برابر ۲۳ فروند هفته قبل است
🔴
این افزایش شامل ۱۰ فروند کشتی متعلق به چین است‌. رسانه‌های دولتی ایران اعلام کرده بودند که تهران به کشتی‌های چینی اجازه عبور می‌دهد
🔴
همچنین یک کشتی حامل ال.ان.جی متعلق به ادنوک (ADNOC) که از طریق عبور مخفیانه (با خاموش بودن فرستنده ردیاب خود) وارد خلیج فارس شد. دو کشتی حامل ال‌پی‌جی نیز خلیج فارس را به مقصد هند ترک کردند.
🔴
این بهبود نسبی همچنان بسیار کمتر از میزان تردد قبل از جنگ است. پیش از آنکه آمریکا و اسرائیل در اواخر فوریه به ایران حمله کنند، ماهانه حدود ۳۰۰۰ فروند کشتی از تنگه عبور می‌کردند - یعنی حدود ۱۰۰ تا ۱۴۰ فروند در روز - که حامل ۱۵ میلیون بشکه نفت خام و فرآورده‌های نفتی در روز بودند، یعنی تقریباً یک‌پنجم تجارت جهانی نفت. در کل ماه آوریل، فقط ۱۹۱ عبور ثبت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121107" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3607fd785c.mp4?token=Cc6vq12nW3Q8dl2cRLPs66XEg1cMb86DJ1s9RTdlxjQuM3yNrE350KPBZWDLfUePExMCNqPl_xCLBNyfVvZ5DQyp3V8rgqQw1bHF1faHcqsY_9n1mP5zRa78LGASHK42FRWw_encblxittZaCYePwH34OSCno8jd2zv9-Uk3SaI85mh-pbo_rgidapDWr_YfjLWDuUsyU-wuE_Qj6bCaexR117gcsGM3_WoxEuWn1SZQtuRbVcbUmIf8IqJhw-XSNaj50yolOf_iZSvSewWaCvh9nCykyxnFx48_fCfgPLjqvDIcqaIm_j0doAz_FDIj5cgOD7EbAz2SM77Y5PyY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3607fd785c.mp4?token=Cc6vq12nW3Q8dl2cRLPs66XEg1cMb86DJ1s9RTdlxjQuM3yNrE350KPBZWDLfUePExMCNqPl_xCLBNyfVvZ5DQyp3V8rgqQw1bHF1faHcqsY_9n1mP5zRa78LGASHK42FRWw_encblxittZaCYePwH34OSCno8jd2zv9-Uk3SaI85mh-pbo_rgidapDWr_YfjLWDuUsyU-wuE_Qj6bCaexR117gcsGM3_WoxEuWn1SZQtuRbVcbUmIf8IqJhw-XSNaj50yolOf_iZSvSewWaCvh9nCykyxnFx48_fCfgPLjqvDIcqaIm_j0doAz_FDIj5cgOD7EbAz2SM77Y5PyY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله همچنان داره تانک‌های مرکاوای اسرائیل رو تو جنوب لبنان میزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121106" target="_blank">📅 17:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عراق: قاطعانه استفاده از خاک خود برای حمله علیه همسایگان را رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121105" target="_blank">📅 17:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
زنگ خطر آژانس بین‌المللی انرژی درباره بحران بزرگ سوخت به صدا درآمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121104" target="_blank">📅 17:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a498aecac.mp4?token=shu3CLpWaepxAem5JdRt5ZkepZeZOrpPB26OyZI_KHon7Y8Y1KrN1zbeAiy2-RQ8afBILI1_9v3p1N3MLDTFaOzB6e5B_sn_6kotbr_kxxWJ8TnzkpUc4Ab4iAW15Y8_FKqCOQqtOsuHQmtFsAz-UFkzhIvc4ooZF4y72IRe3PSVrvgRpX_AAtwEEvtLHs-08BqCbWZnSs3UM9pdprmYp3qXo3t58pONsWV1adkcEPtcgtIMU1KqkyNhQX_pKZT8Xe4Qmloq3gTIGG9Czx4IX9_tQ6Yp7eostiE75bcMGrnPkU21GrWa32lnbadiCg_53fUpyL9xwCktD2ZNDBIERU9LZt3rIS_Nh3ngKN2715hev-ZVojnf5iYVVPyIrQp0TNKB4r5eUbHtAL4MD9zi3Ai8WKeiUOgJj0U7Y_Y0UdZN5Nt9Ysc2LoCnyLd-AqjuHAQKedzrHw_l9st7aET5GCOX_rJ7pwJXH0SedSgFPN_tfy9aOFrkzeIbaYZCCGErBE5gd5m9jrFmaDuGUvniIR68QrcHoc3u1EyoJVAyuzknCw1XAoJidcdtxSi0oQbOKID2K4B7U0Hl7eIthtZ0YfxlAy6pequJp0f4uvQY9u9zfA_Q90F1EQHV1lGWVChZx-fq2KZ-sfqSWWEzgYPV6e0JAfdsNar7xT89csXXWrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a498aecac.mp4?token=shu3CLpWaepxAem5JdRt5ZkepZeZOrpPB26OyZI_KHon7Y8Y1KrN1zbeAiy2-RQ8afBILI1_9v3p1N3MLDTFaOzB6e5B_sn_6kotbr_kxxWJ8TnzkpUc4Ab4iAW15Y8_FKqCOQqtOsuHQmtFsAz-UFkzhIvc4ooZF4y72IRe3PSVrvgRpX_AAtwEEvtLHs-08BqCbWZnSs3UM9pdprmYp3qXo3t58pONsWV1adkcEPtcgtIMU1KqkyNhQX_pKZT8Xe4Qmloq3gTIGG9Czx4IX9_tQ6Yp7eostiE75bcMGrnPkU21GrWa32lnbadiCg_53fUpyL9xwCktD2ZNDBIERU9LZt3rIS_Nh3ngKN2715hev-ZVojnf5iYVVPyIrQp0TNKB4r5eUbHtAL4MD9zi3Ai8WKeiUOgJj0U7Y_Y0UdZN5Nt9Ysc2LoCnyLd-AqjuHAQKedzrHw_l9st7aET5GCOX_rJ7pwJXH0SedSgFPN_tfy9aOFrkzeIbaYZCCGErBE5gd5m9jrFmaDuGUvniIR68QrcHoc3u1EyoJVAyuzknCw1XAoJidcdtxSi0oQbOKID2K4B7U0Hl7eIthtZ0YfxlAy6pequJp0f4uvQY9u9zfA_Q90F1EQHV1lGWVChZx-fq2KZ-sfqSWWEzgYPV6e0JAfdsNar7xT89csXXWrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چی میشه که 57ی ها این سخنرانی ها رو شنیدن ولی گول ملاها و رجوی ها رو خوردن؟
🔴
دیگه چه توقعی از بچه‌هاشون و همفکراشون دارید؟
🔴
معلومه درکی از پیشرفت ایران ندارن و نمیفهمن سیستان و بلوچستان یا خوزستان و آبادان چقدر میتونند پیشرفت کنن.
🤔
ایران گلستان رو تو همه موارد چه اجتماعی چه اقتصادی و... به جهنم تبدیل کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121103" target="_blank">📅 17:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : دنبال سرکوب جهانی شبکه‌های بانکداری مخفی ایرانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121102" target="_blank">📅 16:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
الجزیره: تعویق نشست شورای امنیت ملی در کاخ سفید
🔴
یک مقام آمریکایی به الجزیره گفت که نشست شورای امنیت ملی در کاخ سفید امروز، پس از آن‌که ترامپ حمله به ایران را به عقب انداخت، به تعویق افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121101" target="_blank">📅 16:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سفیر چین در تهران: حمایت پکن از ایران، آشکار و بی‌چون و چرا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121100" target="_blank">📅 16:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t06ImnqxwNUObOTvhT02pudxY7YV1i_mR8wejWL-z6nNTsOI-RAxwTutDpzs2BB7rjlmjliEEf5Y49JKgfxYxNTwQ3PvATDio5NFFdXqnWx-WUNoNDRt36_dMw8GmpWvt38Tbm1KW4-1tlX2vgqNnkan-hT3ecKeLbPV9iJTnU1tUK-q7DqnjHQVACy2nXa_CkgC25k6WUrhPWdSgPqVZG5TZ6bEQyd9JUH_SDg3wKxITwY02nvaUqAgAY8ZdwQBJd0NIvRKA4IQZL-7x-7Zp45L85Z0_IyoRl-bAzPY7rSlAAjDCc1RDgPZmzkiS9QI2tCVrkAdrysHoUx3Wfpkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین گزارش فایننشال تایمز درباره دیدار شی و ترامپ را «کاملاً» رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121099" target="_blank">📅 16:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وضعیت هوای تهران قرمز (ناسالم برای همه) شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121098" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a474872a0.mp4?token=Vn_PlHfw-DqZj_xwX4Oc31NZbRb_A0qkGxq8eXpDIdFtul4XDxjK-dX3d3-OglMooB8AC-5TQfqQh5NUpCRnlYk92e7XyuZj-TvA4aBD1QoozsDAwjSkETro_YftmqwU7k54t8v7PjEn7RgfATGiVTWw8PWEtPiI0NBoDqPRplBOf3qvFU9ZbBI-JvVF6Jc8ro-gcXNKp2kve3L-ffQ63SRNfjQ8GFMAsuWHCULlbuJBiYCtZ0QFiIaMtX5CvuNhQLSQWKpgkcA4jXk1W6lYSFCazLDOn7gjzueJih2oTl5enWNCzVVT0Y4OO5TUrbyOCP3UPI8BOc2PAqL5RyVOeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a474872a0.mp4?token=Vn_PlHfw-DqZj_xwX4Oc31NZbRb_A0qkGxq8eXpDIdFtul4XDxjK-dX3d3-OglMooB8AC-5TQfqQh5NUpCRnlYk92e7XyuZj-TvA4aBD1QoozsDAwjSkETro_YftmqwU7k54t8v7PjEn7RgfATGiVTWw8PWEtPiI0NBoDqPRplBOf3qvFU9ZbBI-JvVF6Jc8ro-gcXNKp2kve3L-ffQ63SRNfjQ8GFMAsuWHCULlbuJBiYCtZ0QFiIaMtX5CvuNhQLSQWKpgkcA4jXk1W6lYSFCazLDOn7gjzueJih2oTl5enWNCzVVT0Y4OO5TUrbyOCP3UPI8BOc2PAqL5RyVOeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلگرام به خطر افتاد
‼️
🔴
بابک زنجانی رسما فعالیت شبکه اجتماعی خودش به اسم «مای دات» رو استارت زد تا این سوپر اپلیکیشن با تلگرام رقابت کنه.
🤔
از جیب ملت به نفع حاکمیت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121097" target="_blank">📅 16:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک‌تایمز: اظهارات ترامپ درباره تعویق جنگ ممکن است فریب باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121096" target="_blank">📅 16:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjCh3jM5HAS7GbxGjLKkZKCf4JcmBYot8HcKMCDKBa0YtLlZU4cdnT3aDzM2utyeTbm_eURRuql6mZqxpegzCrtov3KB1nWsACeQ09fsGgNd2SfJqycq8L6b4fo1aPiSBJ0IxdrvKg2HMkO1xLGBKeGyOk1bbgGYRjbOdPATJHP_uRRYPA5Tp20NuIbRapgqs2bsxAPl5qy2rohy0lr3tqzBAdjQgDoruHP4AllfxBkSVUFInD4cRsak4kqDXNHG6rY_mlGy8YIL5dir3yR58EBvpfTX0pguEvp2iloqe5fV2Ztiky2-iNI7CKcW52GDFVx6aXkd1MRV_ecatyrnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با حضور کریس رونالدو
🏆
🇵🇹
لیست تیم ملی فوتبال پرتغال برای جام جهانی ۲۰۲۶
@AloSport</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121094" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4iIwOvgS1IoTw5Etz76ey-KNT1UkooOUz36onHHv0lHa6BZDDNPO0ZlgVmCzDIuwUXiU78dHqOcuow1UMQBoZE4PZsWiHAv5dDBbdMSatnrTgnyevxbJtdNwaXWwMfI7tToMWl-L6i0yx3dGpr7i5xlFLUWGssNx-_pzyOh7FViQPxXB58yeLkqlCpgWgj-3azQggW6ldvHDp6w83q-JBpy_Z2_lO5SGCqcPt1UDGvwr1PQeo6WBu9-FBwJWW2smO_ugNJ2DSX2p49eTGLuzrs-PuapJpd0gKlMTajx6IXQd1_jR5fcfYczGFTQlAzjlrzPitKigHHgeGDFBnRI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: نیروهای سنتکام ۸۸ کشتی تجاری را تغییر مسیر داده و ۴ کشتی را غیرفعال کرده‌اند تا اطمینان حاصل شود که کاملاً مطابق قوانین عمل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121093" target="_blank">📅 16:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👑
مرگ بر سه فاسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121092" target="_blank">📅 16:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpzgLOigXXXEfFIYtezUNq090y-nLQx0tQzFE-NNyk5oma9mpfDn_Rte_934VUe7nj23tgz2CKRf5_3TmUQBjB9OIbLLjsy6-xuaIGZk_jQVvhMqLjbYTNHgINUkXLdWVA9VzQ83ErvGgITFfErYM-g1_t5oSxIN7H2iK8FgearFyFHrTQaCxGLgDDbbgraULZJIUDNZQwtnmgyk1Fej46_ElWLzi_FdhUv6ctqpcbPAH4uYcPPh2R1wKQuCwIi3kRUA9i1g7vf26P6te09dRY3zpjudITQh4jsmD-tJzVaRncpSijNo5KVlzjBKLsMDotiv-I5xeTtOv7MoMx8d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: آمریکا هفته گذشته حدود ۹.۹میلیون بشکه نفت از ذخایر استراتژیک نفت(SPR) خود را به بازار تزریق کرد
🔴
این یک رکورد بی‌سابقه در جریان روزانه‌ی بیش از ۱.۴ میلیون بشکه در روز است.
🔴
دومین هفته‌ی متوالی است که نرخ تخلیه ذخایر استراتژیک رکورد می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121091" target="_blank">📅 16:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
خوش چشم؛ کارشناس صداوسیما: موشکی که کنار دیمونا زدیم از جنس خاص بود و زمین رو سوراخ کرد و اسرائیلی هارو رو توی یک پناهگاه خاص کشت/ اگر دوباره جنگ بشه فقط از اون جنس موشک می‌زنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121090" target="_blank">📅 16:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس مرکز ملی فضای مجازی: در ایام جنگ روزانه ۱۰۰ حملۀ سایبری به کشور می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121089" target="_blank">📅 16:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a8ea39e7.mp4?token=j6_FE1NkeRhzB5l6AaYPAwtfpTrr7nRMKdgZoZFfcvBJ0JVklR4onIpc1A0pp4pXnMK1yryC25hKNAZcmrg2FJIAx-pG_E6rngMx0Y6KKZv37k39S6eJjsaNt7_FK9xMaev8KCJ060_O58qPsps3tHtfKE4TY-QnWEb26TRotRjAM8lL3VnCFG90GuJVu9hAqmcsCNh-MT5reADu1p4Z1oVZoAqIEbqPWlAJ6LmhjfZwpToBPBnp2zKKTVb2f3DpbjwMyx1U3KcGveL9vlW704S2CcSASasYoJTmxKoA_TBqrDb1Wslsy8tEmfMX1U3d_PWn9HfUiMjtUz3GF5G8XWuEJGQxuicIg8UCgVpEpxSOFyC5pSJzCz57xQq70O0gt4z05TwHX2-7kHB0j8IuEh3XcPIlXN-H8ofbg1Z8HVOPp7p30zSuGLPmNCHGQsRN4Seo442U7s1aejfu48YtT9HMlef0bXBzZQUsgMlisQmMIjzEsKGv-DYgCFw9yb6ZgVeN0-UBhrdRIC9oEM01XbJKO6WIC6NpMMqhm3XSGsvNO7ILLh8aFyuRgOjowNsZ2IK3zGX1O4EVUrAhKJ01ruv1I_uDukYAYAJVtgijNq9MEEzhyjhVgYu1yYyZ85M7VJpi7zu3EjckUKFgsRgJCx2VXUxo6QuLueg_00LAwVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a8ea39e7.mp4?token=j6_FE1NkeRhzB5l6AaYPAwtfpTrr7nRMKdgZoZFfcvBJ0JVklR4onIpc1A0pp4pXnMK1yryC25hKNAZcmrg2FJIAx-pG_E6rngMx0Y6KKZv37k39S6eJjsaNt7_FK9xMaev8KCJ060_O58qPsps3tHtfKE4TY-QnWEb26TRotRjAM8lL3VnCFG90GuJVu9hAqmcsCNh-MT5reADu1p4Z1oVZoAqIEbqPWlAJ6LmhjfZwpToBPBnp2zKKTVb2f3DpbjwMyx1U3KcGveL9vlW704S2CcSASasYoJTmxKoA_TBqrDb1Wslsy8tEmfMX1U3d_PWn9HfUiMjtUz3GF5G8XWuEJGQxuicIg8UCgVpEpxSOFyC5pSJzCz57xQq70O0gt4z05TwHX2-7kHB0j8IuEh3XcPIlXN-H8ofbg1Z8HVOPp7p30zSuGLPmNCHGQsRN4Seo442U7s1aejfu48YtT9HMlef0bXBzZQUsgMlisQmMIjzEsKGv-DYgCFw9yb6ZgVeN0-UBhrdRIC9oEM01XbJKO6WIC6NpMMqhm3XSGsvNO7ILLh8aFyuRgOjowNsZ2IK3zGX1O4EVUrAhKJ01ruv1I_uDukYAYAJVtgijNq9MEEzhyjhVgYu1yYyZ85M7VJpi7zu3EjckUKFgsRgJCx2VXUxo6QuLueg_00LAwVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر فرهنگ اسرائیل، میکی زوهار:
کمپین هنوز تمام نشده است. ما هنوز در میانه آن هستیم.
🔴
دو روز پیش با نتانیاهو ملاقات کردم و از او پرسیدم: «چرا هنوز به پیروزی نرسیده‌ایم؟» به او گفتم که این چیزی است که شهروندان اسرائیلی می‌گویند.
🔴
و پاسخ او این بود: «ما به آن دست خواهیم یافت.»
🔴
ما تهدید هسته‌ای ایران را از بین خواهیم برد. ما حزب‌الله را شکست خواهیم داد و حماس را نیز شکست خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121088" target="_blank">📅 16:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رئیس روس اتم: قادریم برنامه بازگرداندن کارکنان نیروگاه بوشهر را اجرایی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121087" target="_blank">📅 16:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2718f30e4a.mp4?token=k1NDQuVvP3CerBxvMNM4zelNX2anFI4IpQkmY41B-av8W2IU8VIlkqRge5fPJLcjI4NviUr2wL9CybrVICgD_d4aE_aeNe4IMOtx1B-pb3_8s3knQTuboKnF1NQVlEH5ap3-fAr-wSjfuHj1o2x3XCQCg4QEaxYQnrpHSGuNPOrkwbPZpUxEyTGyjIyn8hSaghMuy2pB5J0l3jeYuWDedVgjnbxNDb4nA05Fve7nN66P1e7kTHAB4PdQeh2nIGM1Y7NeTImc9nQXD547BXuUDAdmLSE22iEyTnlgQCsUu_ZJsRpppSFg0A9rWLPHcER4Qj6giw6CziU9tBWyAalcfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2718f30e4a.mp4?token=k1NDQuVvP3CerBxvMNM4zelNX2anFI4IpQkmY41B-av8W2IU8VIlkqRge5fPJLcjI4NviUr2wL9CybrVICgD_d4aE_aeNe4IMOtx1B-pb3_8s3knQTuboKnF1NQVlEH5ap3-fAr-wSjfuHj1o2x3XCQCg4QEaxYQnrpHSGuNPOrkwbPZpUxEyTGyjIyn8hSaghMuy2pB5J0l3jeYuWDedVgjnbxNDb4nA05Fve7nN66P1e7kTHAB4PdQeh2nIGM1Y7NeTImc9nQXD547BXuUDAdmLSE22iEyTnlgQCsUu_ZJsRpppSFg0A9rWLPHcER4Qj6giw6CziU9tBWyAalcfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر فرهنگ اسرائیل میکی زوهار:
مسیحا چیز خوبی است.
🔴
این چیزی است که همه ما می‌خواهیم هر چه زودتر بیاید. حتی رئیس ستاد، فکر می‌کنم، می‌خواهد مسیحا بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121086" target="_blank">📅 16:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48fee383d5.mp4?token=lOPYWNjxQGEdw5WE9MMT-B42ZLy2eGIHAWyvKvRNm6iFeKaQP4HL7QNYsgBD5WlzIqRV77B-_7Yeo9GMATmsDpMTgoWfsjgn-2YE1uXkOPN5pqxzJ6EeoODFNER-BmEQRPlKA-Jw_hjNg0xtrcEx2gCvB2EsA9-vw4kgnKVLAWYVoW3svn2-LOlSf9xa5r7X6Jrbdy2kkG7aibbe62pkX6RS4s8JpqAm9pkQ14Z00J8ZB4WQ8hjvKxCBwO3PAbia0-_Mr2ddLJ68lAFEScdcYmzf9K9syaDNoAx2fpJY1mJES3KjvGCiwTN8y7i5jROH9a-lnr_hSd5aMlfJvpMs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48fee383d5.mp4?token=lOPYWNjxQGEdw5WE9MMT-B42ZLy2eGIHAWyvKvRNm6iFeKaQP4HL7QNYsgBD5WlzIqRV77B-_7Yeo9GMATmsDpMTgoWfsjgn-2YE1uXkOPN5pqxzJ6EeoODFNER-BmEQRPlKA-Jw_hjNg0xtrcEx2gCvB2EsA9-vw4kgnKVLAWYVoW3svn2-LOlSf9xa5r7X6Jrbdy2kkG7aibbe62pkX6RS4s8JpqAm9pkQ14Z00J8ZB4WQ8hjvKxCBwO3PAbia0-_Mr2ddLJ68lAFEScdcYmzf9K9syaDNoAx2fpJY1mJES3KjvGCiwTN8y7i5jROH9a-lnr_hSd5aMlfJvpMs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای کماندو دریایی ارتش اسرائیل به تصرف کشتی‌های ناوگان جهانی صمود که به سمت غزه در آب‌های بین‌المللی حرکت می‌کنند، ادامه می‌دهند.
🔴
کمتر از ۱۰ کشتی از ناوگان در مسیر غزه باقی مانده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121085" target="_blank">📅 15:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بریتانیا هشدار داد : اگه تنگه هرمز بسته بمونه، دنیا خیلی سریع داره میره سمت یه بحران جهانی غذا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121084" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
هم اکنون زلزله در استان لرستان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121083" target="_blank">📅 15:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYPL1geXNk3GKbALs_bW081s1cNHfHe-TSf6kMcgCl4uMTQnGxyP-4kfsBqYUP_gNGNymytKG34aa4vviwr8UkaC1KQHhoMTA1oz5vtrMcu0FIdbzT0Mfw1cpHsjHiLnOasGdRRUSNzJCwAT6pg_NAUVJuyvcWDKJGvQJ6wGXNIn824wkLOvJ2tcNVSeOrHSUGQRBC_Z0wSAbW4DzPXMUBOWIP1lhgVsKhKCbc31aofo7MnIb-xW_Qf19NBhxtA1oovH2oHbSwc-CsyxMEeKIBzpCLs8XWIkrzi12fSRpS-JC9tdlyUQcF5zmLktZUZlPkeX9BRLbZD99E7ZoQtFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
"بریتیش ایرویز" پروازها به اسرائیل رو تا ۱ آگوست به حالت تعلیق درآورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121082" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ادعای یک منبعِ اسرائیلی : یه هواپیمای مرتبط با موساد به ابوظبی، "امارات" رفته
🔴
درباره‌ هماهنگی برای اقدام مشترک در صورت حمله احتمالی به ایران صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121081" target="_blank">📅 15:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ گفت که پس از درخواست رهبران کشورهای حاشیه خلیج فارس برای زمان بیشتر جهت مذاکره، حمله برنامه‌ریزی‌شدهٔ آمریکا به ایران را متوقف کرده است.
🔴
با این حال، چندین مقام عرب خلیج فارس بعداً گفتند که از وجود هرگونه طرح حملهٔ قریب‌الوقوع آمریکا بی‌اطلاع بوده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121080" target="_blank">📅 15:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZoF8WVP7Kd-rlLSuiTtTRhs-GWNGEZa_gOQBO1TOuvmO150MEr0zGnVot22jaCGlEv4EmQRgagTk416e2qTgBq_RYclmkdn3Oq61NTiWGwKwufUwrwnXc1JQdNPGxaORwDp39mC3g5dOVNLXV7n_ovhYjqSPZgpPpRpCKalJvHIAt5c52Hrrul54iP838-B4rVzRWIs2JBuJGVjMuN4QDAKt2VBMoEGbQNuzBRuiwRptewp4uln8Bomm4IJ8mWw-ONF5k4Bhn--njtMU9mLnQlzphnJFACe-QHwcWlQ3HCxkREzHqbJ-rcyc8I1JG-BLnTYNcbz6EC0hUNqFMw0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده جمهوری‌خواه توماس ماسی:
من انتظار این را نداشتم، اما انتخابات من به نقطه عطفی برای کل کشور ما تبدیل شده است.
🔴
امروز ما تاریخ‌سازی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121079" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
هم اکنون زلزله در استان لرستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121078" target="_blank">📅 15:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376babfab.mp4?token=aOSx1jsJNym5vRol4s4pDYSlXrE7vcq6h9a4INIZw5qRQY3L9SW52TCKDzth6bw6A2Sf91YFt9jRl_glVhWNH_zy8TphQ7FMUq7c7yS_ksQCqHMoMZM6ksMD8T78qpoOoA0hWv6KXfej9wrF29hsPyCvh8b1NkiTLMfPUNLR4CuoU9EPw_b6fGN69xx99cDcj7scUJRGbWFFLff4TfTbiAgsQoQKQRLLiWojmNyp4qquZSSXHl2cPOTjkKjtr_ImumKB9ODm3Q4m9tSqvkeTN6fYNHHEWc_i57XtJ080oWBgKi-MPUDMaFKibhJM1_QDVOLwmAEAv6YpH_Hy7IB_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376babfab.mp4?token=aOSx1jsJNym5vRol4s4pDYSlXrE7vcq6h9a4INIZw5qRQY3L9SW52TCKDzth6bw6A2Sf91YFt9jRl_glVhWNH_zy8TphQ7FMUq7c7yS_ksQCqHMoMZM6ksMD8T78qpoOoA0hWv6KXfej9wrF29hsPyCvh8b1NkiTLMfPUNLR4CuoU9EPw_b6fGN69xx99cDcj7scUJRGbWFFLff4TfTbiAgsQoQKQRLLiWojmNyp4qquZSSXHl2cPOTjkKjtr_ImumKB9ODm3Q4m9tSqvkeTN6fYNHHEWc_i57XtJ080oWBgKi-MPUDMaFKibhJM1_QDVOLwmAEAv6YpH_Hy7IB_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع نظامی گزارش داد که یک خودروی بمب‌گذاری شده در نزدیکی مرکز مدیریت تسلیحات سوریه (وابسته به وزارت دفاع) در پایتخت منفجر شده است.
🔴
همچنین منابع محلی از شنیده شدن صدای تیراندازی خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121077" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وال استریت ژورنال : چندین مقام از کشورهای خلیج فارس که ترامپ هنگام گفتن اینکه تصمیم گرفته حمله‌ای که برای امروز علیه ایران برنامه‌ریزی شده بود را به تعویق بیندازد، به آنها اشاره کرد، گفتند که از برنامه‌های حمله فوری علیه ایران که رئیس‌جمهور ترامپ ادعا می‌کند، مطلع نبوده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121076" target="_blank">📅 15:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c489e1b78.mp4?token=uhM0S7tdbUwE96b4m0n5KauzwOwJ-ttm8NunzfWh32AIxXbVbniYBmGPazPUlic6KPS_RHlo4lZCW4ysBHLDW7Xwxmo_o1YtUIxkObc4rIux9aSstvtav8t9Zng67wwMBRWQo2wLuFtuZNWKOh1YfDWq1pAlM3kxmB9mqEUkhZ8Irn5ndQX1sV6WXMKyMcMPjxijiK9h1Hc6vmmBv36j9M_AKrf06TMpMkW1y6dbr-yInsH2rqEQX8O7Uw1WIE3KX2VQj9ytv5ZuwowZPSk-_vcEEzHyPOSsMgTFBSPj5qdeaH8Rv7HYLA1irHWf6sgnvFj09nGNmpK_3X17cygqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c489e1b78.mp4?token=uhM0S7tdbUwE96b4m0n5KauzwOwJ-ttm8NunzfWh32AIxXbVbniYBmGPazPUlic6KPS_RHlo4lZCW4ysBHLDW7Xwxmo_o1YtUIxkObc4rIux9aSstvtav8t9Zng67wwMBRWQo2wLuFtuZNWKOh1YfDWq1pAlM3kxmB9mqEUkhZ8Irn5ndQX1sV6WXMKyMcMPjxijiK9h1Hc6vmmBv36j9M_AKrf06TMpMkW1y6dbr-yInsH2rqEQX8O7Uw1WIE3KX2VQj9ytv5ZuwowZPSk-_vcEEzHyPOSsMgTFBSPj5qdeaH8Rv7HYLA1irHWf6sgnvFj09nGNmpK_3X17cygqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل بیش از ۲۵ هدف وابسته به حزب‌الله رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121075" target="_blank">📅 15:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نیویورک پست به نقل از منابع پاکستانی:
ما همچنان معتقدیم که مذاکرات غیرمستقیم جاری میان واشنگتن و تهران پیشرفت خواهد کرد.
🔴
نسبت به امکان دستیابی به توافقی دوستانه میان ایالات متحده و ایران خوش‌بین هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121074" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
صدای انفجار در قشم مربوط به خنثی‌سازی مهمات عمل‌نکرده اسرائیل و آمریکا بود
🔴
معاون سیاسی استاندار هرمزگان: صدای انفجارهای شنیده شده ظهر امروز در جزیره قشم، ناشی از عملیات خنثی‌سازی مهمات عمل‌نکرده متعلق به اسرائیل و آمریکا بوده است؛ ممکن است طی ساعات آینده نیز  عملیات انهدام مهمات عمل نکرده ادامه داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121073" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌تایمز: مقامات نظامی آمریکا می‌گویند که ایران تاکنون تاب‌آوری فوق‌العاده‌ای از خود نشان داده و هم‌چنان توانایی واردکردن آسیب‌های جدی به منطقه و اقتصاد جهانی را دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121072" target="_blank">📅 15:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qjad4gR7QIKG4frIkbQziWnvXUaDnoPX4In3ecC-Pv6ZaEKpayOuxw4LH8QCh-AXdz7yWakbFLnIIxGmKB9-xP1daoOwAujgbLE4tG0cUDO6Q8HgOESPHtmoQENpLhNvcv1IqU6lGsRr5OMXvGa18On2e1Mebhk37P3DOGEqcGezoRgdjbdV9sQcbEZALv3RRlaeN9SE2pARqqsKrWFH7tUp2hjj1lHifz9FveYWuaAlaLIgxDhuSBuFybapDCqutKUp-Li7e63F_YWmZWIPckepcLuykP2ELK5xvdtINKX_Aou9xex97Z9PUknk6OVwRdly8XV6JrSU34tKmJq31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-KyJWuhtxlMLb3OgyGMrye1OUlEkRS-uWloXIlok8TFowQJRlP7RXjc1EFC5kmLVLQVUithBTQNKPu5zPAYeFU85otrCtUJyF6OaSGjjwI1CXlzZppDn7xKl_tps-RPfOFEL0VEDstKLYBbS9Xc6UoTSKGUjT8BDi852hUwth68rxoBWlrRCCyss2IXS9bFjapAQWM9qGCP8LS43RmRCeOWawYPLXUrUNNEPlQRSQetjFdKbXFg6SZyLhwi21g0IgTaBFUtPM-dxRuaBHSgGT_xqUgkitb9ZhX5G12YxV6JnNZIg2JSApKHkm0pN3vsr8936434lP2TRC3BVzSEsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز هتل تاریخی عامری‌های کاشان به علت بی حجابی پلمپ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121070" target="_blank">📅 15:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
آی ۲۴ اسرائیل:
انور قرقاش، مشاور رئیس‌ امارات طی اظهارنظری بدون نام بردن از عربستان سعودی و قطر به دلیل تماس‌های مستمرشان با ایران، این احتمال را پیش می‌کشد که ابوظبی برای درخواست از ترامپ جهت خودداری حمله علیه ایران، تحت فشار قرار گرفته است.
🔴
قرقاش گفت: «آشفتگی نقش‌ها در جریان این تجاوز(!) ایران حیرت‌آور است و کشورهای پیرامون منطقهٔ عرب خلیج فارس را در بر می‌گیرد. نقش قربانی با نقش میانجی و بالعکس در هم آمیخته است، در حالی که دوست به جای اینکه متحدی استوار و حامی باشد، به میانجی تبدیل شده است.
🔴
«در خطرناک‌ترین مرحله از تاریخ معاصر خلیج فارس، در میان این تجاوز(!)، موضع خاکستری از بی‌عملی کامل هم خطرناک‌تر است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121069" target="_blank">📅 15:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: عبور اخیر دو نفتکش حامل گاز مایع قطری از تنگه هرمز به معنای بازگشت دریانوردی به حالت عادی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121068" target="_blank">📅 15:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فرماندار اسلامشهر: عملیات خنثی‌سازی مهمات عمل‌نکرده، چهارشنبه ۳۰ اردیبهشت از ساعت ۷ تا ۱۰ صبح انجام می‌شود؛ مردم در صورت شنیدن صدای انفجار نگران نباشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121067" target="_blank">📅 15:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVMyx7FeI-0HpCsqT7ZvR4gGF_pHbxLYD5nCeRu32mYHEtqhvt5Wapcg-BvWv_4yEPBMkv9J0UItuP06Y0Yel39q5o7IjjwjfPJ0s2bSOjT_5plhzzHsciO-cH-dW4ccpZjoKcse2xKidRmYi0haXXViHezucJKpI4-heJpiCRDft7gc0lLb1mcYnNEzDgn0uTpXjvR21VcA0cKWuf9DOUY9H7DDJFCDize5sg9RtO8dqeXTRaoMpCVjSTYae4kzybtzJXbZR68g-GiRXWWiyg9yj4yM2efB4PdRI2nq5ltzSCS4Ut_LFbZwh5KXFjveL0Th1xJZ7bnkfM-NJ7Q8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری سردار آزمون و آرزوی موفقیت برای بازیکنای تیم ملی
@AloSport</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121066" target="_blank">📅 15:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Zj7zeDb0aIwtg6J-aMblHsJ4GvVGGHdUFh1XIa7Lg6R5G4_5P9KW9GCp27s7dRy_66FzSnlg32Ri4ln3a_rwMU85VVFXEs7trJJWzY-B4BIgqRQO3BfwzabEA8BAFUblycvm5lD1t0TvYc4QSPyoDaPIYKJXMlb4Uk7ms6ISKRe55gZnu6fWgnT_zXtmASZyeaM5tv7rVXLrjUTl7QIqSPVUZ8aHXhf0sQ4ChuIjI6BVl9M-kILh7-9NzD_jq9VN4aDurMlEUV2oEBg9bO5Kf2qeJWDCk5MPSW8lyN3RiF6GL7XqbsKRDNaBd-qaPhE_NP6JLBjYx8arx78M2a1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عفو بین‌الملل:
تعداد اعدام‌ها تو جهان تو سال 2025 به بالاترین سطح ثبت‌شده تو 44 سال گذشته رسیده و
اعدام‌های انجام شده به‌دست جمهوری اسلامی
، اصلی‌ترین عامل این افزایش بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121065" target="_blank">📅 15:00 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

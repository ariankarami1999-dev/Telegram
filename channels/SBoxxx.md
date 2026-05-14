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
<img src="https://cdn4.telesco.pe/file/ScVS9WaouBEUhiDAPfuN02G5rGo9T3ri4kFLrr1c82s8fFVS0whiGW9Y9gbZlA889u7UtAU10dXEm3ybrwfWFAkGfz_ogzoFAHjqLCCjai50oqS0TwAF5LnDVdthKleNslaQJgwSaqQuv-b0aLw1aLBfKIaM33KtrDBacp1IZQu1W-Cx8d7k5DXSP8DwN_d9KXBOAdiTRjBVDfqeuWF3IV_wUnfSH3sz2RkJRVunr-2pO4Ha1ltZgKYPfkRfKT29BM1h9z84d2MoM8ad9eyLgYsGPKNWS3igOajHcyF5cJjZzSYd015BwCDKlIoQFJZQZ-ujoWi4egLeQSFh4m-nVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.84K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 03:29:18</div>
<hr>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🖋️
بستن تنگه هرمز به سود کیست؟!  برخی به اصطلاح نوابغ دنیای سیاست مدعی اند که در صورت هر گونه حمله نظامی به ایران، ما بایستی تنگه هرمز را مین گذاری کرده و مسدود کنیم.   در صورت مسدود شدن تنگه هرمز، جریان صادرات روزانه ۲۰ میلیون بشکه نفت و مقادیر معتنابهی LNG…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SBoxxx/16260" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOXz5NPxVPDt4LH1kC1hXM82nuqfcxpW2ZX6pbFjk9AjxuYWSF__ODX93LQSskKW7lwOr5D2JygPNkKDGP677DdU6jkfc8AfgszehC63uArUQuSx7Zxi0qUMgeWcisPYHR8w9G7kc0-L-VGsuR5oKvsmQdiLQ-ygnDcO3qhygx6yPWZ3dWGscBNaNL7KkSEm1py_dYX55iSOjhH0evqxhCy8yDTacmOuy_zOj6xG4pSYoie6bQSoWuTKRVMHZ3y8Gd7zSW6gqvtgl6lAN0zBvqUmOOmZkQ-iQj9yiA5JMaa87uvXMtFMRGBHfDX_BWTVNFO4mzF5PtYufvfU_s_BZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پولتیکو:  چین ایران را برای رسیدن
به یک توافق تحت فشار قرار داده است
نشریه پولیتیکو در گزارشی به نقل از یک مقام ارشد دولت ترامپ اعلام کرد انتظار می‌رود دونالد ترامپ در جریان دیدار با همتای چینی خود، پکن را در خصوص مسائل مربوط به ایران تحت فشار قرار دهد.
طبق متن این گزارش، یک مقام ارشد دولت ترامپ در این باره گفت: «انتظار دارم که رئیس‌جمهوری در طول دیدارشان، در رابطه با موضوع ایران بر شی فشار وارد کند.»
به گزارش پولیتیکو، ترامپ از رهبر چین می‌خواهد تا از نفوذ خود بر تهران استفاده کند؛ چرا که چین تامین‌کننده تجهیزات نظامی برای تهران و خریدار عمده نفت ایران بوده است. هدف از این فشار، وادار کردن حکومت ایران به پایان دادن به انسداد تنگه هرمز عنوان شده است.
همچنین یک مقام ارشد دیگر در کاخ سفید به طور جداگانه مدعی شده است که: «چین پیش از این نیز ایران را برای رسیدن به یک توافق تحت فشار قرار داده است.»
بیشتر بخوانید:
https://l.euronews.com/q0ZO</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/16259" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMztSZ1Y-e7jn8-8x4yRl92OttL-8C23lgVEgrxsrO3XxPzlDvfrt3-IzkzFREWeC8QTgKmbEcOlAXlqg92DAVpHYLu1g91QrQG29kA_qYadP2Wp0-NGsPwjchaxitGdIzPsLGcdlF4saRqbgnRVHZ-hlhWLWbtckJ1ToeNXW9GcmzsB3MjswA0UVFC5OP0NcOs2Sb2AMfgKr-YmZGzBPFU95bQT3h5NETV-aSOAPJ5_vMi0ESopVIBvICSX6fXADk_6yVA9_5Br9L-ZHgKXVTUWaYjg3Cd4QwSP_n4YsTE-2cp5EqydDyEif6Ukj7-2VkvhFzeDaQu5PKNfR1Srlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗯
جی دی ونس ؛ معاون ترامپ
:
وقتی ترامپ در سفر هست و من اینجام ، حس اون بچه‌ی فیلم Home Alone رو دارم ، میام کاخ سفید، همه‌جا ساکته و خالیه، بعدش یادم میاد چه خبر هست</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/16258" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIGXADWRTmIl_cj-XwwASbxPvXlZD_RwmXReelYk7WpVV0b3y7ZHZBCeih-he6kdWotSwlIfpncMulkc0z-l1FEhDgyhO7EaBBhTxV5rabdO9BZMhFAsjHWmqq27rtycdJi4k5cdZ4z9sdP52ey9lXUumBJgTNmpk7UgUp6x9SK_jHEjF_Wu1cz93Y2cy-jYnXROC-nn_IAT0q8eS1sd9fFbzPdEEM2a1vIIYW-0UJWVU7zbpjiN-FVeEUshG0J7WaW-AOgjYVHLrTVUBSW65BdkBkR7GDAw6fD6U2bpNTdBt4HpdcqQZoT_bSgeVW7CO5HYu1FvXxZeHrpZHsDaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند تحول اقتصادهای گروه ۲۰ در ۱۰ سال گذشته!
تنها کشوری که شاهد کوچک شدن اقتصادش بوده ژاپن است.</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/16257" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: عربستان سعودی و کویت در جریان جنگ با ایران، به اهداف شبه‌نظامیان وابسته به ایران در عراق حمله کرده بودند!
حملات عربستان توسط جنگنده‌های نیروی هوایی سلطنتی عربستان سعودی علیه پایگاه‌های شبه‌نظامی که برای حملات پهپادی و موشکی علیه کشورهای خلیج فارس استفاده می‌شدند، انجام شد.
منابع عراقی همچنین اعلام کردند که حداقل در دو نوبت حملات موشکی از خاک کویت به سمت عراق انجام شده است، اگرچه خبرگزاری رویترز نتوانست تعیین کند که آیا این موشک‌ها توسط نیروهای مسلح کویت یا ارتش ایالات متحده شلیک شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SBoxxx/16256" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل تایید کرد که در جریان جنگ با ایران، نتانیاهو به صورت محرمانه به امارات متحده عربی سفر کرد و با رئیس اماراتی محمد بن زاید دیدار کرد.
این سفر مخفیانه منجر به یک پیشرفت تاریخی در روابط اسرائیل-امارات شد.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/16255" target="_blank">📅 20:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/16254" target="_blank">📅 19:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns_CIn8icoiT1KFyTl4Ttm_uHBlyjjKMMX5nmbrSsiKXYZhWRieSrkBldupEeuyYYyx3ZH0gZBF7n5VJ5bYg-tyVpxiBJe6njwU7-WkUpNX_kHHj9_nnHpfSMYVy6jgKECKm5g-vGTS3yi33YdYPclxZ-Rp0K84yGsS8G6UrDU3tDanq3hu-NQSiV5_xKGKmFa6e1HbilXzdwV7IOlDwAWzMd_J6c4xMWNuTeG64QWKXkpRRJi1KpDQrtU1STMf4BhsjGXUtRFWQua-SEomKuV3MupA61dHQQXW3QocnU8_oUvyRz_OUFM8dw40nMStdtZpPCIoul7veQi0UQ5PEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله پهپاد جدید پنهان‌کار خود را رونمایی کرد.  این پهپاد جدید که احتمالاً توسط چین تأمین شده، قادر به فرار از رادار و حرکت در میان ساختمان‌هاست، ۵ کیلوگرم مواد منفجره حمل می‌کند و طبق ادعای حزب‌الله، بردی در حد ده‌ها کیلومتر دارد.  ‌شبکه های رسانه‌ای حزب…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/16253" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/16252" target="_blank">📅 19:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsuO7Nrnd2gaPdLQD7tInWhyq5vazcEJg1Tp34CA1y--JRYuHS7SlxIp5R1xNUWMrFKRJedsy7yL90Z58Sut6CVfWD1MY1zhb0PhgFZKX3PjEN6yUslLR-HcZtz3lFZLS_A5SCIQIgSUlCw0GFYpVBFcnU-hnyy-DLsOPRfF_eV37igEg4WGjEaFjYZ4duqXZqTnyUDQf2XMP4e4qsN3-ktTSGJ44DVfRGJPD6wrsAMgfP7rs2OvzH3z1HLNfU-9sSO0wRT01fYvKP1tJ5Atz6EGGKvPWMT2rw0g9PJD-Z7batgk_fX2bdTRJqgFqq2e-Wkk929_icHayuUAd4dxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16251" target="_blank">📅 19:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585750fa88.mp4?token=Vnv3usvk_m0onMeEf7eVnA5fRxn3h67Ztw3x9BxQCn1rcq-MR_zHu7j7jof_4ZEXfvMjAFAyzKML8bsmMx37KfXSTony-pa06XJgYgMiz4dj71KA-OfBKOJzbdMaiQ_P33OYYqoy6s_YpexxOsMyBAzQ2B-hVSFJ5sBNOxjuoxwtmStMKbs5tWeSYCvcbZnQ1lo6g1O_SRMO3LJmZ1dfFLsON-POBnJaIWZ2qsPx-fC7QrD2tNc7v3ojiJIG4cid0GBoCCZpLaUqI8qk_CENm_hmIOzHXuHVVN67hQZYp3vnYiT5vdK1kWiY4pwKnLxyDT0Gy5FXKLZb6bpzF67dtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585750fa88.mp4?token=Vnv3usvk_m0onMeEf7eVnA5fRxn3h67Ztw3x9BxQCn1rcq-MR_zHu7j7jof_4ZEXfvMjAFAyzKML8bsmMx37KfXSTony-pa06XJgYgMiz4dj71KA-OfBKOJzbdMaiQ_P33OYYqoy6s_YpexxOsMyBAzQ2B-hVSFJ5sBNOxjuoxwtmStMKbs5tWeSYCvcbZnQ1lo6g1O_SRMO3LJmZ1dfFLsON-POBnJaIWZ2qsPx-fC7QrD2tNc7v3ojiJIG4cid0GBoCCZpLaUqI8qk_CENm_hmIOzHXuHVVN67hQZYp3vnYiT5vdK1kWiY4pwKnLxyDT0Gy5FXKLZb6bpzF67dtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SBoxxx/16250" target="_blank">📅 19:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx3BlFQzDQaM00dkZJ1LVAmm8la8nCNPJ2FzaJt0tzGHLlje2louIqtonMP2oFGo8AYE2wj1mxyv7GpvT65kpNeUSQOFc-LkVLgbOa2O0GSlky-xb2sWMbACz381w2h3KM3JZ4n__RBkI07o_asQPvn2KZQ_32IAq2h-vERuyaBFgaRouX3qzaY15yfywpmTsw_Jlb_NhqATbBdUa59Mj1HWCUwLSOT88_tlNYRR7g1542VLQnqyGzbx983N_hc-gu-nAuPbgfcd9EKmzjlFoyO-_xu7jjUn_G1YfnTU94BMUNlCH9SZ9NUTYKnPCG8ERM5qSZcaaOuWe00y9pT5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SBoxxx/16249" target="_blank">📅 19:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16248" target="_blank">📅 19:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/16247" target="_blank">📅 17:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🟠
کارشناس امنیت اطلاعات
:
هیچ منطقی ندارد که منِ شهروند عادی که دشمن هیچ نیازی به اطلاعات و احاطه به من را ندارد ،  به اینترنت بین الملل دسترسی نداشته باشم ، اما مسئولی که حتی می‌تواند در لیست ترور دشمن باشد آزادانه به اینترنت دسترسی داشته باشد
دشمن آمریکایی-صهیونی تکنولوژی هایی دارد که حتی بدون اتصال فیزیکی و نرم افزاری می‌تواند حملات سایبری خود را به خوبی انجام دهد و این بسیار ساده لوحانه است که تصور کنیم با ایجاد یک شبکه اینترنت داخلی ، امنیت را به فضای سایبری کشور هدیه داده ایم
در همین ایام ، شرکت های زیرساختی که دسترسی شان به اینترنت بین الملل قطع بوده ، هدف حملات متعدد سایبری قرار گرفته اند
✈️
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16246" target="_blank">📅 14:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16245" target="_blank">📅 14:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار جنگ ایران و آمریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Us6W_aotNnFuFxm8Ky__eAl1x_NduR-8k8rOr7I01hGkATePRMpfTUrqbhIdTXhOuievevtsQpmjJNG1g5aSa8cKJRCf8zqK5IosDV9Ot37J2_A_EPa_Fw6MxTaXmWCLhIvgDG3UU56qmUWJ3QH6WqMei82ww3e-2hUSPSA2V6B1bj6N3ASY531a-Fzkza3mMJn-75mR6qp0sVE5OY1qL9SlO4bsUE_uvzIrVv34ZvN40xZUGJxbSYl2lwBZnaYRV7X_AdXGU5aNo4PANSX6bkidDDDFYCZTIkZRkCz655IxzFJ1BjKbZ512K6-lJUJZJ4_h5l-w3yAqyKgxXHEThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16244" target="_blank">📅 14:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16243" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxe8oqOXffepo0-Qe1my5UqPPidwpsUlSa0CO8yp9RTPSCWmPxOvtwtpy3GVrjFxAYMWzGTZLbSD8l5RSRgOaox2WYuQvD0hYqMZz2zdrW9Q723jaPzqSeQUFeO2WYnpIjgh6OvyQIuXfEnlYTcxRNel_81cxZtlenqdEMReeuNZeOJ0pjB7Cf0lQLg1iQU3kthM5xaR41KzJ2XZcXRf8xlhd4Y3a8Mt4aFTML--0jQYrTHgafKTyLyCRPi_aHVQV9T7cl7POaC-08GS0OlGGUIQi6R3gQXUCE8qA3AkXe0AQRNRMdpQtZkYtI7KBagtHXCf0m2mECJDup9EfSZLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک انرژی جنگ ایران و فشار تورمی بر آمریکایی‌ها
افزایش قیمت انرژی ناشی از جنگ ایران باعث شده تورم آمریکا دوباره اوج بگیرد و برای نخستین بار در سه سال اخیر، رشد دستمزدها از تورم عقب بماند.
افزایش هزینه سوخت، غذا و خدمات فشار بیشتری به بودجه خانوارهای آمریکایی وارد کرده و نگرانی‌ها درباره ادامه موج تورمی را تشدید کرده است.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16242" target="_blank">📅 12:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFDRMk8mN6Cnn3XpXkEqUQ0T4vf0cjx7s9c-7r0gzmGNWZrUQQrgnU3Upf9DfuQm5zIKI288bpdgWF_V1ShQc731m8qW83sfO-MexFFcQjrde5DpZDmRk1aPiLbXVaMbfN2CnzqRJ9uuIN970nvuEmBXeR7JZG4y9VynQDK5IO3Ygtp16P6ckeufgBjn1S0yOVXNREZZKDT9i4KG_C5qeU92yB5CHw10UT7mc2VCXzEzdHmV3OasrJiULAq3kalN9_qfb7pqtv-8i2vrab_IT9tIEWmSF3e7ko4_CizHnsI9jStsF8xmt6r_qo4qvB3fj0fn1jGxg0MeLhLXvyYW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنگ ما با اسرائیل بیشترین آسیب را عربها دیدند!
سبحان الله!</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16241" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ می‌گوید ایلان ماسک، جنسن هوانگ مدیرعامل انویدیا، تیم کوک اپل و سایر مدیران ارشد شرکت‌های آمریکایی در هواپیمای ایرفورس وان به مقصد چین در حال پرواز هستند.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16240" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLnrGga0wKaOSnonN38IjPP4ABQ_2pr68c9AehaW7VoqYVI3RPcQRfBf_gk_3FWUkb-TAJlMgu8VgEdqSgiUAqamf_6bH0ZA_X_uubKOxRa7FrMTFeFMG76aAUOSYIm4Ag-V6vCDYA9-PN7yJZ-MUtKCZFM9q33NbR9d4U_wf1OQhxKvCVA5XnyNAneNzL77lqMn0Dhuri47mTxDbum2tkBWFt-BhidhMDtEZE710-D6RDHJguhAw3oMaibMJk5_Vy4tYltDfSQdLk38XjixcOX6W_4EMUpmPQITFtwOZplbcCxd4BihaUrAytPKyO5BvnYZbXS2N6IJo0n7IQBxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD -- H4  مسیر بعدی مدنظر پس از رسیدن به سقف کانال.  تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16239" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihkObq0E4QljsztysGSG7XIDI0aFxE5WV5X5rLp0UqGqe_6NFSp9J-8mp1w3TXCgbHvJsZ3wo-jtLHcazO_tuQER3UvYtYOobeWTklbOGgCQqnQ0VVB59cEdqCz5YcD3-hAyG0IpHtmtgBwfyr620FEoRNhwLFdfIUOx_rry-AClpyA2meNCItRMHL3cLuFYElEUdfhiVHfRoS1bkGLFw_3YPcV5pW5XYMeGaKqzNFGFGQK2RpxDtDuQWBheM_QG62ur-AW21GzJptB9GfOPbux3hBiCNIVZ8ztjJl5t_w9kUErfwFAHR0AOA9gp8JLK5BwdruBerDJiKIwIdm89Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
مسیر بعدی مدنظر پس از رسیدن به سقف کانال.
تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/16238" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ترامپ می‌گوید ایلان ماسک، جنسن هوانگ مدیرعامل انویدیا، تیم کوک اپل و سایر مدیران ارشد شرکت‌های آمریکایی در هواپیمای ایرفورس وان به مقصد چین در حال پرواز هستند.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16237" target="_blank">📅 09:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQDLAM7Vt9ZvaJNJSFRNzwB3Y4t_QfaGTcbAA5tttjbfdSj7lr2nzquQqhOBim8nKYj2TeGflSblaRIzDyGYSXj1OkdUYBQvb6MS1YDlGvUYTuP4rTgXnF6va9o4LUvcKUVcny6TrjPUMdcVC_BXpqVTYdH-A2DioIlmz3A9ePxRWNJKFK9iC5ppCDgyIoiilqUgl0ud6TX4Xql6aiqI0wIJCCBTDAJjvzRU1otheUvR0sPFXBdQ_t-5vgPSzqaKZGU9VlASOtmkoOA4DCunwELYzZvecJVfGkaJXtp0H7uxzchwIbvCNd8u2KKyrPY0C5IuXb4Cyrxmo0md5xKZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی منابع خبر از طرح حزب الله برای تصرف بیروت می‌دهند.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16236" target="_blank">📅 07:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لازم به ذکر است که این دو مستراح بزرگ تا ۱۹۷۱ با هم متحد بودند که سپس بنگالی ها با کمک هندی ها از فاکستان جدا شدند.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16235" target="_blank">📅 06:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیویورک تایمز:  برآورد فعلی این است که حدود ۱۰٪ از پایگاه‌های موشکی ایران به طور دائمی توسط حملات آمریکا از کار افتاده‌اند.  ۹۰٪ باقی‌مانده پایگاه‌ها و سایت‌های پرتاب موشک در سراسر کشور «یا کاملاً یا تا حدی عملیاتی» باقی مانده‌اند و احتمالاً برای از کار انداختن…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16234" target="_blank">📅 06:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پست جدید ترامپ !  استخر کاخ سفید را گفته تمیز کرده اند و این را برای رنده کردن دموکرات‌ها سوژه کرده است.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16233" target="_blank">📅 06:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیویورک تایمز:
برآورد فعلی این است که حدود ۱۰٪ از پایگاه‌های موشکی ایران به طور دائمی توسط حملات آمریکا از کار افتاده‌اند.
۹۰٪ باقی‌مانده پایگاه‌ها و سایت‌های پرتاب موشک در سراسر کشور
«یا کاملاً یا تا حدی عملیاتی»
باقی مانده‌اند و احتمالاً برای از کار انداختن تنها با حملات هوایی بیش از حد مستحکم هستند.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16232" target="_blank">📅 01:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16231" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چرا معادله روسیه—اوکراین برای چین—تایوان برقرار نیست؟</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16230" target="_blank">📅 01:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16229" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should exist. These are American cowards that are rooting against our Country. Iran had 159 ships in their Navy — Every single ship is now resting at the bottom of the sea. They have no Navy, their Air Force is gone, all Technology is gone, their “leaders” are no longer with us, and the Country is an Economic Disaster. Only Losers, Ingrates, and Fools are able to make a case against America! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16228" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXAoMA1LC1inTbY9skiTvP2jJ_nAVBGbM-ZVNR-wTkbLuyiPPJzh6bz2dx0rGavC-xk3tzaxMCmYILZ0eXUcMWJLMaVGCh8yx-2fzQwmXb-8F_qSo1IL8vS0_3py0892lT3pcusKMK__2_ZCR81EnFEBDhIypx226AQCmSN94QWVQg665SzRwdtZiyLEwYEPDkQE_H2JTm80uca_FES4V-C7iA43xc_U-hg-5aaeqAeKayq25Id2QcC73ZQelWVljQa3S1s282CxCa_lEDA1cO_Q9fMO6W9f2Gvsfj58SqXHDNfVSBbDXiIQvZKUorApWUFHBFfc-ec68l59T9kMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA
— D
#سهام_خارجی
این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.
نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته ای هم یکی از اینهاست.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16227" target="_blank">📅 00:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16226" target="_blank">📅 00:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
  <div class="tg-doc-extra">347 KB</div>
</div>
<a href="https://t.me/SBoxxx/16225" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشت تحلیلی Foreign Policy درباره احتمال فرسایشی شدن جنگ ایران</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16225" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwTwz3HyKvjPmzUA9AAgCyl3eVkLf0PyxhNK9jYVO3NF_XeJlpquXJssnAHLEsS1eyuDBPPUV4ROwStn_G-mJ3l_VKYZISNhGA687sSZKA5qa9HKmNoYQntjq7DAX312BiflrccPc_xGjzbeUsSkM8o-7HvDIFJcFVZAh39EzXd8KaRTOzMDLW2wwEQ3ixJuD6lijo4Ckv3Inw-PK1xUgIKl_Qic_3nY9GtNVNg5DG0AlcWpgTLhuE6orFBhJRLbnU-bJKv0jJXC6K0snraP4x2SlclG6iQYZarbrFdQqkxbTC-Cthjo5HvyVuHctb2qK8m9ldN5WWlMg2bcUkl3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای نخستین بار از سال 2023، رشد واقعی دستمزدها در آمریکا به دلیل جهش تورم ناشی از رشد بهای انرژی، منفی شد.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16223" target="_blank">📅 00:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16222" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zdjbosj_fViTvxDIzCgRkNBd5AKvi7rFscjtcMvftzjS0iElBsGxEmuhqBBkmun-0vzUno8emkMB2u-HjTUisdlJwvnBAc9iIHUZvuls9fEoEmSd7re3TRkqyhdG5wN6EvFhTyiHVtzVPcrEw9obL6Dn_yLGAaDZLB_kx3cS3KFX3BhOzAOBl_4vJZfDNWQCZpfSt_Mtiu6j_3VKaENUWsCDNheQHa_4NToYXnhMJVkKQ80t-otwUZYpAgZySPmsRpwfIwx72giryqJ89wJaQM1lUygR7lXrDsx2v_Z7FbFAdPSgGwDyJ4m4HBBz0DdeMcJYUaqJXetxuX1YnRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16221" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منبعی به خبرگزاری فارس گفت که ایران وارد دور دوم مذاکرات با ایالات متحده نخواهد شد مگر اینکه چندین شرط برآورده شود، از جمله پایان جنگ‌های منطقه‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های مسدود شده ایران، جبران خسارات جنگ و به رسمیت شناختن کنترل ایران بر تنگه هرمز.
بر اساس گفته‌های این منبع، تهران این مطالبات را اقدامات حداقلی برای اعتمادسازی می‌داند که پیش از آغاز هرگونه مذاکره جدید باید انجام شوند.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16220" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as8zrt37KBrvGlnndb4FstczS5dwMg-5tGbbXuhGiUMfDTbxskvPi-JvOQzKrQ6JfGHR_7JaC9k6M93Xn8S9b9bv777u2vBWilkci-IszcONUYppjgcaSpDoZqB3BGaMMNqwddfd-Ii7BZrW_QJKYe9l-FKapHMxvTP1MfdNFrg7Z8Z0DrdBSoZreuIqSsqXBpL9dj-gZVVmAjBGoTer_-rzubMO4wUZ33N1QXy2MixSjhqvPJQ2vxLMgmyjCFCFbdsVqUXD5foWvzciRxuAuOGLTtZ44HPRcQxiX3nMCoqC4o9hyF-zRYaWpbV00zYWmrmdzWrOr3TEnb9cyON8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توزیع ملی شاخص فلاکت
📊
بالاترین  مربوط به ایلام و پایین ترین  مربوط به خراسان جنوبي</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16219" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inkFxhbG4-6zaT0drR_TA1s7PJaoIDajPj62LwWYSgdry7TyFKEGsHG9OPPQJtG6ve9SOkv9ExuMdPI107tuK8TY2bS5PEG3sQ3aadNJ6dLjRXBdYaVpxbxCWNrP4GSr2pt5zo78gENCQLIwzYd4JlgkvtM70M421Pec3Udgj6ntpGobfpv8CvEtpMC5pCA4JpdrUY_dC6UbOwvUtG9-wjgaygx_EMpbnATNZq3Hzr3GdkC7ni8DyyOnTR_hiNW2X1hnYZScRAWwQoZWI7gxdo6HachoU9tOEhmbeWZh2CT4wDfo6b9ev9cVKzbOY_Se2K1ZDbu9kuprbq8Yto4TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند قصد دارد یک بندر استراتژیک در یونان را به دست آورد.  بندر الکساندروپولی در نزدیکی مرز ترکیه  یکی از پربازدیدترین بنادر مدیترانه است.  شرکت هندی که در مذاکرات با یونان درگیر است به احتمال زیاد گروه آدانی است.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16218" target="_blank">📅 21:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو از تشکیل اتحاد جدیدی علیه «محور شیعه بنیادگرا و محور سنی بنیادگرا» خبر داد.  این اتحاد شامل هند، یونان، قبرس، کشورهای آفریقایی، کشورهای عربی و کشورهای آسیایی خواهد بود.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16217" target="_blank">📅 21:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzlQAjVK5qpxsgyVHoHLSOaA98P6YUZXmDhvDmZ9T3_8_-lTt48B_E-EUanGrmDWksWPfOxMNj-ZtB59SxlXd11flzZBH9ETjvvzPZVdLCUc1GkxRg4F7qFpmOCnrT-2LKIaELQ6A6gsssiaU3e9Rf_hpvmWUGEmM53sXC-dWsXl7yq5KxYPC0f6QCtDBcm42BgZwHySJxpxqOUlYpEqizKWb6tR-YC4xg9aTD8pSRNL1iO2wK8PtHId2VxOl2Er71GfI9pbK_WQJ9Iu6LhmrbKw8dRSmUMnMvRAUJIRic2qd8rcmM1dAxd1Me2PIpGILtNSbkbTGOobmVfa7s9Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16216" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16215" target="_blank">📅 19:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erkrc1-dagOkK3vCNWkni3A51HXQe_bBX0eYep6yApz9jrWV_k4cLYOQYOMuoyJK7y0hNGlwVLsF-vAXcp8ATycIBdZPGE7e7HNd66mS2O6-MOxJsJwNcUAoAg2Q4XwkClYvs8esF-dYF9u82XMp5fdEvyzgi9ImZZuT14C6e1QnU_SZgDPVpwPQkn67tjUCk61WIdH_oRMlSYMJ6rx4lARWFHUcRkoUxUxvpWDu4m2_OEcEPSGuP_K5lKuAFQ4aOzikFET0CG7wSTGinsaKywlII_lN_8WhMw6mJgoAU6t_zH2sDixxzQVGSnPIKz4Uul889GsVFdrPUUNxF7ES_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16214" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8OEXqjPmw1m073xO1CeJSxH-z0PXKpnlFJC5SUjnCOWWV9p4l7S4QDE-LNXFWXNSwaItBmcgZAbaoEc82_uW0M8igNqd5Yav6sohnZMcWp3p52jLPGeMCmYXGbSQGiE0I8GfEUszqgRWMNyxlJ2uZzvqMhMfYhCTF-BOiDIYAQRKLjSjMf676_UaBV8Y4gqnhdt8MAE-p1Uu9bKSl54_r5VfYofZICtnXbzWfJYTXT94wC7IJGwdM2YTs8FX-IAllUNpyJHn-J9hwoEXpjOuiOqyfDgkghreSVhnAe1TXdexhsLI3IZR9KMAtkjWDEvcg4JaUv1UFEsj_NsN2W8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !
استخر کاخ سفید را گفته تمیز کرده اند و این را برای رنده کردن دموکرات‌ها سوژه کرده است.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16212" target="_blank">📅 19:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ درباره ایران:
ما صد در صد به گرد و غبار هسته‌ای دست خواهیم یافت و کل ماجرا را خواهیم گرفت.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16211" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.  شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16210" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.
شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان منتشر کرده است.
به گفته نیل اولپاک، رئیس DEIK، پیام این است که عضویت کامل ترکیه در اتحادیه اروپا به "استقلال استراتژیک اروپا" و همچنین امنیت جهانی کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16209" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew1m6LlLYQnb4s-xQXmxsQDS8Ezh_TSdWD_kZTQ1n3vsmCRZd5mP0dGhE6Fz75Gz-0XDMV6Uk_RT-FChoE9v58TjB4e45BrXhO9S3o2IeBhjJ3LiSg9yKoF-GZWnEWZL969xd9wN5lgsAZv0qeJ9BflVmbag6FF4Ci9qqPAoWyQ--SiOu-L6i_f3jj9KxXJsNj0ZZdsR_qUC3nZEoYryqCvY5cPUkGy_8Y_ZEL5LdzKXJgg9tmWIIxoiHi6FsycBvB9-ABS87XYMj8wIM99vFS7t3-YfUxfAk-g0jpV6h1VclHm1ZZzk0hQOjmO6guaQ7QJaZJqu2loo8ChwbanpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#US500CASH
-- H1
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16208" target="_blank">📅 18:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
وزیر خزانه داری ایالات متحده آمریکا
:
تنگه هرمز خودش باز خواهد شد</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16207" target="_blank">📅 16:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فرمانده عملیات استان کربلا:   نیرویی که در ماه مارس در صحرای نجف بود، اسرائیلی بوده و بیش از ۴۸ ساعت نماند.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16206" target="_blank">📅 15:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16205" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxVkCggpd6z04YPdymHsP_enRxil3gIHaTh18EJLI7_oBhWhCN70X3Sh04Hl3gSaPNTEraWRgBCbuMib3DWE73jWpy9xMoFpq2UkJ365k0vylDWNJMQZhmu1MOptfMqVDF_hMfOmY1l0w3tSBdcYSFTzq2l2lCXj4In1SrjDoH15_YyNX77kulXzF6xtVvPnUw5OeLlSPl5D83-tmciVME2AV4pucx0_IPpLHF2WWeFrKMYEOvOZC8SUovecnp4ePVo5xB7bIQwU22GVxSWm3TeytPijMMaSkWhFAHTug6VV7AcQYesES3IOfiDgb8T1OZaydoLuGepg7ik0B7rvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از یک شرکت کننده در رزمایش ضد هلی برن «قائد شهید» سپاه محمد رسول اللّه تهران
به نظر می رسد احتمال عملیات زمینی یا هلی برن آمریکایی ها از دید سپاه پاسداران افزایش یافته است.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16204" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0dnkZNxX-FPbmnw0OYfw4sonM01ZuFEPIx8WuobnoYf9nOxJD7rEHOhDBk9ejOgVpeJDPd5YD2bBVchF9_-GNI03YSx8NOyMkcqZp98TFEJT6zDO7eUxeJa3OdvDz7G6Fw7WlRlcfhQTPdMGHa8CANj7RETg4bCSXJaXUC01CVfuXU3PRnaNMzhPl4XNtIyNe89XYjmXrVPMex_4LsbHroh1B3Olfq6kL-w7Hs5XnR9WVsnMnlNn_SS13ZtLFBYl2UAi3VN-KNZzboW27SipH6hhSGrRiy3wtUOoOPAJlv7XR_bKPqg9z5woOYw4fuvv--GhB-i4SnSlCh966-8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان وابستگی کشورهای مختلف به واردات نفت + گاز طبیعی مایع صادراتی از تنگه هرمز
کشورهای شرق و جنوب شرق آسیا بیشترین آسیب پذیری را دارند و آمریکا (گوشه سمت چپ پایین) کمترین وابستگی را.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16203" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_yDGja4tVSpNBaxz6kqQOz_aKUI_bwQxhc5oLjLjNnxVJpqSNqtUOjL0HGwr73mrp1Z8BefbBxMHzMfMlkX9CucXtNH2uNUxoamWoWTB32m-mU1_NwCfm4u8miERzDaRCr3P0LvjMAzwdWCy5uVVM_w3ySMCdtKXTmZ15Ti90M9peMv-om98axFdCAJLHKvBjZcU8BqcjHB76aeCFcdDgUavSM5_IiXxlOUjZdPr79j1h5D7Im955ZKggxsLaFhTAUNtnU1Zkjj8WrdLVTXRF_5qxD2LGKlunfFjdfdYYwtDwfYu8TQU3LTM8aZ0_-irnGyqkWv4oczY26ZHZBtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H1
در محدوده مدنظر یک اصلاح 4.5 درصدی داشتیم. اکنون طبق مسیر ترسیمی رشد بسیار عالی داشته و در حال نزدیک شدن به سقف کانال است. از اینجا احتیاط و نزدیک کردن تریل استاپ توصیه می شود.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16202" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJOUbgvqAhYlBZFhN7akuf3J6xEzbOj9NJq0ukSYQY5l7j2AMzUE3XXMY9sMGNRILKhdGvJ_CuxJfe660UU4XPRzk_ks0SVSWAZyIyG1dgIAQta51eyDfNquwihSPsAoIec6LgToSbGK4IHCKLeyJsEidZ3siZvlqhJnoYIwkMW3VzRGdp2-xnWtroJNZeQRPKNsbdCdVm-WoHDR01kotfC5JMzt7QT2HY5Epnftdyuxugr3YVMhOi8vfyujK1dQow796KSifNaLWsilPJiEaRdXe5rwQ7rj2prCxlm--i-XxPbc9SinhYeaNVGTj9dQXUW65zLO1N_viWWppSiNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16201" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtDOXioox6ox-eZ2C0YVOafbBUXGJD7ZyDoFq_e8rcB-WgtCnUmmpCskEMu2HkuwgcQKfDs76QgT2Z0C8PY7LwwVY-IOfENn0NJxa65w_QPvIps6z-kFGoMm7KPG-nG63uaC5PWS17eX58ZPtao-kkS0q0paQOupU3BVVh_ah2-OkpoqmBEZIhNCSe1OJWf3Tnx9f8uvD7WIRTSRwYhHIdGYlLdMUTiVGZHyqlFx3E-p7s09Z0elw4TShbY8SYujA1go-H7gAjOGwXHZxdxEi-AA5n3NMzSxZnA1JygCn_jFnIKpjmGg7Gz-dN8I4zu_KMFSLH4291tfiV1Np88HCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و فشار شدید روی ذخایر ارزی و طلای ترکیه !  طبق داده های معتبر، در یک بازه بسیار کوتاه—حدود دو هفته در دوره تشدید جنگ —بانک مرکزی ترکیه حدود ۲۰ تا ۲۲ تن طلا را به‌طور مستقیم فروخته و علاوه بر آن سوآپ‌هایی معادل ۳۰ تا ۴۰ تن طلا انجام داده است.   در…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16200" target="_blank">📅 13:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">CBS News:
پس از اعلام آتش‌بس میان تهران و واشنگتن در اوایل آوریل، ایران چندین فروند هواپیما به پایگاه هوایی "نورخان" پاکستان اعزام کرد.
این پایگاه نظامی از نظر استراتژیک حائز اهمیت است. منابع به سی‌بی‌اس نیوز گفته‌اند که پاکستان با اجازه پارک هواپیماهای نظامی ایران در خاک خود، احتمالاً آن‌ها را از حملات هوایی آمریکا مصون نگه داشته است.
محموله ارسالی شامل یک فروند هواپیمای شناسایی و جمع‌آوری اطلاعات آر سی-۱۳۰ نیروی هوایی ایران بود</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16199" target="_blank">📅 13:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#ITA — D  اینکه سرانجام ترامپ برای 3 روز هم که شده میان روسیه و اوکراین آتش بس برقرار می کند و سفری به چین دارد که اینقدر دستکم از دید خودش امیدبخش است شاید همان گمانه زنی را تقویت کند که بزودی یک صلح بزرگ — یا دستکم وقفه ای اساسی در روند جنگ ها — در جهان…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16198" target="_blank">📅 13:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر آمریکا دوباره به ما حمله کند، با ۲ بار قبلی می‌شود ۳ بار !</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16197" target="_blank">📅 13:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
در صورتی که آمریکا دوباره به ما حمله کند، غنی سازی ۹۰٪ را استارت می‌زنیم!</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16196" target="_blank">📅 13:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/16195" target="_blank">📅 07:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcb0zCrs2xX6-DRPk0x9ajs_2oPeyIXQxUWbZB7_xXhCqh3VIVW9xawTIeGn15C1RY9Rou6NLAQIgCafbYtfeTSsrN7bIIDVyOqm82eJpaNWFfpTWTM2HUSGzBWTgESrC080WA6dEjHn3trrj1ldvSp23j20F655n4VGdbed080wlAuntJsFP5ON_BJJS5OASyDIbbfyQoNS1owCpGAc5VFTAATXexov423IKdS7xeCU9fkY9NC8k4gsW6oxu5td6Hihv535duTFqQ4ft_G2G3YtP26PImD5h2IacXFVC1X1xBpGu2WwCFm_qKe1KBdWCGVi3QrOZu2M1Bp7iic8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی مایر از شبکه نیوزنیشن با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال اقدام نظامی علیه ایران پیش از سفرش به چین گفت‌وگو کرد.
ترامپ از اظهارنظر در این باره خودداری کرد و گفت: «واضح است که در این مورد با شما صحبت نخواهم کرد.»
این در حالی است که گزارش‌های اکسیوس حاکی از آن است که دولت آمریکا در حال بررسی یک کارزار حملات محدود علیه ۲۵ درصد از اهداف شناسایی‌شده ایران است که تاکنون هدف قرار نگرفته‌اند، تا تصمیم‌گیرندگان ایرانی را به مذاکره بر سر برنامه هسته‌ای خود وادار کند</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16194" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/16193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16193" target="_blank">📅 03:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSduco6JFXYli5EN_2ed9vBsfYGP4yUHPpa48Nmsvo1S_BgsFpYDN4uegujx4WzJecppQYyI5z8S6VSqzjHu6qBqgYW1OE2QncEm0Cy_JxDur1AWPQY3ni52OYDW3l4jv65xn4xha4uj2iq7zx0IbUsZKHQzX4g7b_l0bkEZGmNAUhBB-kCSzuf73rs1wFVt3iFoxihpvJqr_HIPIWTr-MFO19r5V-RoJ-CxHnmkz1Z75tpKGM9Qz2lpLx9gDCrRp3eNSDg6rciW8_usS-zuWRQTVpJ8WbDgRU1DPiz1TRR-O-ZyyMqLYzyZ5rPvw4Y4Rby8O1NTLOFztl0JDHGnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی سی استار ۳ همچنان در نزدیکی بندر جاسک در حال سوختن است.
این شناور اواخر هفته گذشته در اثر حمله هوایی نیروی دریایی آمریکا در بندر آسیب شدیدی به بخش عقب آن وارد شد</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16192" target="_blank">📅 02:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwuGieDWdZjU2vyQDoYKtnzuHVloTGeYX9CpWOXIt03imvpgMhWEAbLbZbg28Jos4Z3PMRF-ujmedgf_JL48d1MGt1Pm1WxonOVfGfHSeVrE5Oe8tyItPbeau4WJKrZASF__6Gs4tbBWWc7FVBH6u819--L78m5IHEgBKrwnxvWbWbH2wIa6e3gzVOruGaKNJ0VMDOku88uN_Rwla8ic1cXr-Q-Tu38449TEIlXuyUOVabHQI63efeeYWaFOycs1O-z2PMehAkm2pnUHX-kSql6jVTsgFEmo515MK6dsT2T2kxv4LFYad9qYZ9T6_hkibutaIpEKPe74juuTN7xIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Rheinmetall — D  ببینید چه شد!  بیش از 23% ریزش پس از شکسته شدن خط روند.  به نظر می رسد واقعاً دستکم یک آتش بس موقت هم که شده داشته باشیم.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16191" target="_blank">📅 02:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvVl2vjJPI6Nd7echXADsDzV51q80PNcU9BPJDGmC_rekkl-utjWyiravAyZxR18_kanRZ62NsVPpZeoQNS8N965KrmVl2yEEV-1-NlxZjRWE7XhOi542xms50J5QKo-8IY-kLgRPEnPRll1jSYP_gEXbgTM-84Y9ZxQ7MvtK5WV0HlFaG1gKWqSQXWM8bFOKf0M9soYAdLrxIrtHEEmyieH0YW8-CzxaLSC0L0YUw7g5_krXduGygMgZUwW8nEnTo8ysIqBPn_zEiq0pSKzmS6TrHAJZId3e_C2wdjybgz4tLquAKz9VocoM071jPGBoDAuVN0hZnx70dkeXolbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ITA — W  به نظر می رسد این صندوق که شبیه ساز صنایع دفاعی آمریکا است در آستانه یک سقف اساسی قرار گرفته که به معنی کاهش تنشهای نظامی در آینده نزدیک است.  در صورت شکسته شدن کانال اخیر می توان با قطعیت گفت که فعلاً جنگ بزرگی در جهان نخواهیم داشت.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16190" target="_blank">📅 01:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObMYzdSMoRuVM2nCU698vZG-_QD5Ss3pthu1ywlG0BpOXjMevYQjI-Kzqieg3pfXvqc_n03r8Dg_ypzCGTmQHsbPWfUuu96Dn7R8dAQ1DLZh4up_9xJk2I5_VAcaz65BfsyH9GkKSEtFyn5qMwlkbuLGQUBZjZdJGJXek97A_gzeHX7K-t8HQTW8xx44TORBDYPpgVBYdbAi4ib9-FnAl-rhOzv3NhZFSS1ysEYeNR0kIht6aqWOpF0KteGqHtJVFl8Bli6A4k9T8GZeBEfAvT2gU-70yqxtiyjBMECrthMfq8dfgiCbOgGUDLopiojs7gQz4RxOituAaPVCVeWIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16189" target="_blank">📅 01:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JTqVndtdWs0abhFW1iS0zGXEyPEDp4OGPg-hsUclWWx1UjQcK5J5IKY9Qx65kbIzsy5UKkFvkPOScOOAZSij25cIC56chq5Q7ioQesHJjjrAMh2wzIem7NWR49RfkagkWJqHGZHG_a1gaBw6-RDSSQSx4Xdq_Gp9JRp4HxhTPr_6DJX6qyu8x-RCMVAa6JVscDOagplPiBNiyV5Yvnngi9J3vAT1Vzzzy25d-HxqJ5KXBo7BKzsXOcnEM_r39QVQDoJLb_4e5SOUveDoQ1oTqOgXxkarD1-oQLEg7sC5zt-yrRlwxw2vsn1pgrFgjBcKLPqzA19-lWYecWFNJTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16188" target="_blank">📅 01:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uB-jMmTl19e5lEC2anCrqyJPDlRn6o6hz7rFcuqAbj7XvkQaPr-9913AF5cQbjsFUKxgIYSrNTjrEHkP0iVbU1MiXVgTUJcJbLeXCMK9-PDWNP6D9Lwhzt2KRQ8RqCo84hwamNQ4GSDlLwHfq2auw6IRoK8DWkCv4jOoWvTLn2Pvu0BMudwuUkf6x-jrYKnmBxueGT3bVhiswnPL3EBe4mDvXAgHaPzy0wfO1-2_ivD41l7_34FzK_xZE2Fy6p4ZQehpclGJJVHOQeLZmw3Y-Qv8rbeh808SAYZpBmDDvEK1PUsgPIxLphXXl6BKVfOEMfAiiU1dqqSPK6FqROWIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نهال</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16187" target="_blank">📅 01:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگار: آیا فکر می‌کنید آمریکا باید همچنان به تایوان سلاح بفروشد؟  ترامپ: من این بحث را با رئیس‌جمهور شی خواهم داشت. رئیس‌جمهور شی دوست دارد ما این کار را نکنیم و من این بحث را خواهم داشت.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16186" target="_blank">📅 01:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtdymTadXUdl1uozXe2qu8dKZ7CpDVeGzAt4nJ4dqd9psVLupZnrUrL25VF9LHy_Gw5lI_7ANXtvQMqI0SuHmDXqdKMK4ajaJ_aQ24B02DRc_FqxHbFyE7ZsyhcibYlPVdpnrO40GtRAeFR-yW627jF6HHGRREl_OaqrRcRKkv1ont65ggzlbdF5L_qSiihs8tXg2ae4g9nfInnBDJ6AEEkUQioL5uafZlLqZwVxMYwLXXWTNskZ4b6xjWDhT1C1sciuPwcw4VtkpPZJ0zKljLdgyHBjI4DyqCWT_mLZ-9NDIehy-l0FMbig-I7t2T89Glx8AAKN4P8zWUpf2VoMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دونالد ترامپ
:
من همون حسی رو دارم که ۵۰ سال پیش داشتم شاید به خاطر غذاییه که میخورم شاید فست فود برا آدم خوبه و غذاهای دیگه بده
آدمهایی رو میشناسم که خیلی مراقب غذا و وزنشون بودن میرفتن رستوران کرفس میخوردن و آخرش تو سن جوونی مردن</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16185" target="_blank">📅 22:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">قانون‌گذاران مجلس نمایندگان ایالات متحده در حال معرفی لایحه‌ای برای ممنوعیت خودروهای چینی در ایالات متحده هستند!</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16184" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">طراح قانون حجاب اجباری:  موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.  هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16183" target="_blank">📅 21:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طراح قانون حجاب اجباری:
موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.
هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16182" target="_blank">📅 21:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: با رئیس جمهور چین درباره تایوان و ایران صحبت خواهم کرد</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16181" target="_blank">📅 20:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRIhRZ-S7WL9ETFqKSapNno6kto_AJKQIulWhDLh_ZMbPqZlw_REkWwDLYLwpKC8FaZ4ze871JytNfkzOAadWJYYLLhJC5SMEWCJMUv7qUsQ-au00OQ3-lydqWIZGK2zGs7xC3z_vNDhfoEBFbuSe452zLmb8ICR6t5ED1e9GvbJCV7aqKT6-g6yMZ_tZ0Ecz5t54uXJ_lr-A1CqgMQRoohNfw30ciwia_f5OLDz54scuyLeWx1alX46ihD3JQD2LwThIgAvzDXhHu-qFBDFBore74hpCSvSkgK7VlQSzFVah1c1WpauwXMXjpDfnnlTISlGyLVg3KyqzQ9UM1yn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16180" target="_blank">📅 20:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16179" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تسنيم از نزدیک به تیم مذاکره‌کننده ایران: ادعاهای مبنی بر پیشنهاد ایران برای تعلیق غنی‌سازی اورانیوم به مدت ۱۵ سال دروغ و جنگ روانی است</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16178" target="_blank">📅 20:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq0_6mKaC1Tj9_Hv5WLoipoIsIrFPFIRjJuVQZPjOvmWFxhITkAntDUSxtBKt83mJeeB3tnACzNhhOPq96hfpSgwLTvKW3SCsmgNlur6nudE9LKClpYfs81IqoXtNWkdnEcSZXJCbpXM-pcEVWoQy7gDpKQrb0mBJCMs0u8etLZVL5C6GJzO73c30Wms1FXbtl9ReCvPE8Yx6EC5VXnTmpE-MPYozVBfMIsOX5NSxDYxWZgOnhutRLVelApBOIZBlVuipQlHaOPslQvGY_giKQG8-qQfSVjLLwiFWyqO26uTkkFrKsxeiwKW2McVibrO5scWBJzTgfOJ0UeXJFM-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازارها از دست ترامپ دیوانه شده اند</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16177" target="_blank">📅 19:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ به صورت ضمنی چین را هم تهدید کرد که به خرید نفت از ایران ادامه ندهد!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16176" target="_blank">📅 19:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ما هم باید مسخره مان را دربیاوریم.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16175" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پدرسگ مسخره اش را درآورده</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16174" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">متاسفانه ترامپ به ما توهین کرد و ما را به دو دسته میانه رو و دیوانه تقسیم کرد.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16173" target="_blank">📅 19:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ:
ما ۴ روز برای سندی از ایران منتظر ماندیم که تنظیم آن بیش از ۱۰ دقیقه زمان نمی‌برد!</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16172" target="_blank">📅 19:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ای گریدم به کله زردت</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16171" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:  آتش‌بس با ایران بسیار ضعیف است.  آتش‌بس با ایران در بخش مراقبت‌های ویژه (ICU) است</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16170" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امروز کله زرد روی Long نفت است.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16169" target="_blank">📅 19:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16168" target="_blank">📅 19:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1ZJZ-kKwlOsZ-C15PAqw4iitReP7lNevoyQix9K36KV_Vhv3m8aQ_DihsiL8bVK78bgz44QJrlAzGtcedRwDNJgdahZPX637XeU2yyqFBWHy5MAWLRxcUciybLemxjjGC3-rE7htVhoxpVFg6MvDXiM_sLCkBhcWy7eINOVCUFn1CvfqMj8QZH0_OA6aYkThJ7azFk8Ndvzhi0p2MmnRFWeIKh61mxRRuyRUC-1UshYpc5-wfB-PaLJbSSSwNeZbN7gqxzb0IpfyHiD4NjYyQHXRXX9CfZtPgdHYlkrWldtMIs_18jW_WnTxujEQrCcPYB--_AdYSGm5f5aqCbjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16167" target="_blank">📅 18:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16166" target="_blank">📅 18:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وعده ترامپ برای اطمینان از وجود ذخایر طلا!  در 19 فوریه 2025، رئیس جمهور دونالد ترامپ در حالی که در ایر فورس وان بود، اعلام کرد که قصد دارد از فورت ناکس بازدید کند تا وجود ذخایر طلای ذخیره شده در آنجا را تأیید کند.   این مواضع منعکس کننده بحث ها و نگرانی های…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16165" target="_blank">📅 18:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16164" target="_blank">📅 18:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مشاور ارشد کاخ سفید هسّت: در مذاکرات با ایران عجله‌ای نیست چون اقتصاد آن‌ها در آستانه فروپاشی است</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16163" target="_blank">📅 18:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به فاکس: ما تا رسیدن به توافق با ایران تعامل خواهیم کرد</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16162" target="_blank">📅 18:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل اکنون از مانکن‌های واقع‌نمای فریبنده با کلاه ایمنی، جلیقه تاکتیکی، ماسک و یونیفرم نظامی استفاده می‌کند تا پهپادهای اف‌پی‌وی حزب‌الله را فریب داده و مهمات خود را روی اهداف جعلی هدر دهند</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16161" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6utastvtL5nyg1OWwhOoyczKmPOD9CRT219Ysht-tOF8gdI08LtupiJixccgcyTqOchhIriSxITMkDuYvB92zqgxaDo4CcbrBK6RvEDqMumV34yVYYQkEXgbk38ikvrCzpgvAf0ujoYGo6AgxQbhCRAq-VSUSWLfEAtpf34appeZToXvaS6Kf3YH_XV-btcWbD6_tTKKlzVZfuArqtuYtcFvtBqIFXZ7bh-PWSi2Wvk8v04KI0U8FazBKPo86DT_OG8GzjveXAtUuEUWfNWfBqHtULwsRHG-jspxDA8BwtMJNSDyUz0QXAHSluDsaguHxSmFrRY5YYwl8R8hjfvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزایش تلفات اسرائیلی ها در اثر حملات پرشمار حزب الله با ریزپهپادهای FPV، یک شرکت دفاعی اسرائیل به نام Smart Shooter سلاحی را معرفی کرده که طبق ادعایش می توان آن را به سادگی ضد این پهپادها به کار برد و خطا هم ندارد.  شیر آهویا، معاون محصول در اسمارت شوتر،…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16160" target="_blank">📅 14:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebk9RJv4oYvu_kAZmBQW1Y5YQWUcsiIuJYAk_GPF9wfKfdJt9dY-1Ko3Hcb-0_Iw9QYl9PhYvV5P2ueAGW0LuioGcOKWtu5KYqcI9rp76mHIZz5u-7YKRG74os97ZY4jkPyaEywY5Vyj8mynY_4TH7HBEdwCLPVpWG9qW98nLkrmgvBwjuwwj-s1S64ON28TcfbyuOquntDIPE2Hk5T6MlAm_PyI1bSr_8P6PePscG8HoohIZ0yXZRwJml_wbhzc73cAB3ztCpNlIPOgXYeZ0QrL3WOcv9PxlaOiH767AOnF-dmgp6-wltfLuo3CXlChoRzOqJY9gkYUsCZ7TyR94g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا دقیقاً در همین مورد یک یادداشت تحلیلی در سایت کار می شود.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16159" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

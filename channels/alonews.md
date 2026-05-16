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
<img src="https://cdn4.telesco.pe/file/O2aWxPgh7A7l5-Le1oZrswqIGfq0EJpX4L_19Un-TS8jEGgbrnB4db_N1hAkJKdc12JlO8ziGQNnhLvBF3tQwDD6fRFEENQgy9I5m3TLC-iNZ_5PbL8neuZ3FRoiIQ4VyHjMaEW1uWPF3OPYgiyonr-5AOFSYeuZNLEyHKKc4025N_fiZsu5wq_HWvexJ76vX7GCST9YzmnMpgvZ0ylkbaFU7f_B_pZrzSD5f4XiNwDM4nOsL6HnyxJzWPDJu1DF81sLLWmpjovfbJraWiQCCZNUHUAKtgwYSwOrQsDnNFZiDX8jaZwd5e-aC8V1zx-srMfs8AQdkR48GfT57TubXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 953K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 03:12:48</div>
<hr>

<div class="tg-post" id="msg-120502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHb4jP5MQQ_U-WTJVX3qrf2AtB9NaHLDjKeEejIrkzVKa8_FXSrDGP7iOtRN7udpeC1CDYf2OotiZ425yKkLcFtW2cpqGb5RLciTndTdOK1nXNhWRakyNiy6I4iwiCd7JFQ31IwpPXfMvOltcVo8Ljh499TBVxt7-rRbZQDli3tgPcz95Ac8MoJHIvRUPwNa5v7HP-V9XEpWiY4nWBagHIMaCYCPhRPumiwWNQq-JXi0ovPgSaJwOFi8TbZd_W7p94oiAkkRact_5dAIsOdbrLlYMmXyOqFlk5YWVOM6PqqcWfA_d4odFn_ZLGEKj1mGPcQq2BMpdabDe-71jX6-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/alonews/120502" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlGweNkOJmVkxVNYZaNO_RsMWGiYG8asEb-5yPXlxbAvBFIIBaIborbaZ2N0iEMW9MDbcq0r1lFRgzaoMT76wr6fnG3HAXshijao7oXTGYXWrhGgLdK-BV5CSxWQxFYXeZWqTP4vfuJn747s5GGDwpICTh-tk5uLAxFXBEWE0fuJoNJx3dhHQReIYW19sY1A499PGyrBTu9iYTSurNTd7TkoYGO9cZEDPYDr3vYz1vjiicdcndauWAlXGayyHTOxfmcJSRwllkPEaoIoN2Y21kugnSjcKyT7H6rbBgJf-NXh_-KPhvcI-v8J8vKz5_K8cxovduqoJn8561xti030_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده روسیه :
کارشناسا میگن آمریکا و اسرائیل ممکنه به‌زودی دوباره به ایران حمله کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/120500" target="_blank">📅 01:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از حضور غرور انگیز بیرانوند در دایرکت یک مدل معروف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/120499" target="_blank">📅 01:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmBb-DIA_YiE-_xIuvdga8SeBlzYqtcz4qTE6w3rJiuabo8vRp6e2NsawdRhHrAau4pCnbreYmxstG8Jbd4-PCwdI4SHO90gYXRjLtjoO8roSCr5yxTETod52Ecg2Hsj-pqO44ZCTzxiuQgIbbM8LqVF6Mt2QAwwUjPHkwIa3ZIXWF7DQXpQ3pN793KMNlpNq8mg-cKIID8rXOvBnoEaUbQ5l6qMHwq-i-ev69vw1WOsnHE5wMYoIVcX5XqeubSVDUlsIx6rBNeo3nMmLmoLCTn55YlA41t2Gi7zT1oMWlgO4DDbRES5jtJkr8WLbOVJGsHInxRzPfmQIZIP4mCx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیرانوند : با صدای بلند و رسا کف آمریکا سرود جمهوری اسلامی ایران رو می‌خونم. مخالفا هم نمی‌تونن کاری بکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120498" target="_blank">📅 01:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj0vDORE6vCYn7d8RLQ4ZkJcMS7qVfSSH372FY75Wvxgmoyj9jRg5lIRQESAyRMAgXunXRWUGQrnPO0YPjaFmEy0NEMjiCde1oYGSuU4TMyoaOerk3uyduNwFIaNsQEON5vg0cEagKkmQ2ofq9FZVk51BvT1sdD94h8LEN521eEUEGgg74FjBpcmduSA-RovkxDIKhPhKqWieiBPk6-OYioTcPqNsiwqNvk5O57fOBY9TeSq7MUG_UCsptX0ZROSOgtFonbAaLwLrHl5QJ4KyepxJdORJ3ASuaS1AdZ5wAr6CU8SJz3EGFLMHwlu7uLDHzXRkC61tC15bfUAj4vBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: تو آمریکا 9میلیون آمریکایی پرچم ایران رو دستشون گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120497" target="_blank">📅 01:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شبکه GB News ادعا می‌کند که نخست‌وزیر کیر در حال آماده‌سازی جدول زمانی استعفا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/120496" target="_blank">📅 01:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان مناطق اطراف صورت گرفته است.
🔴
کاربران فضای‌مجازی گفته‌اند که سوال‌های بی‌پاسخ زیادی دربارۀ این حادثه وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120495" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muPamYvHylvpxwzcsDCYF7ne_-VAfQ94A5Pak4RbHrtCP-dgf7_7WvHQathiKKmEiAWIjD1GPc86SDQoseqEPsb8K8lA63til7hXGM0SuQX2bh--0UK6xgl8PPJP-qUWhIMqij1vDysCgRmKDWw-fKLTV4dDR-m6DACRlyz3zKe9k7mhDdaakZrEJwTUEP7ZH3aUcwyM1DxySpEh42HzzhWTimNxuSjWfuWgr86yn7qg6n45Qj8MEjPO3CKpwW9rsA_6Q7Bo-pRcF_Opt9LviIXKY9vjORLs9t_dAfVgAydWHIIm-uZInebUL5SGfxkdyUi5Qw1CP4mBpGurvtEtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
🔴
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120494" target="_blank">📅 00:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fHbdUxkOTZCbge2O7n4Te3n7HeNvuSX-EW7ZizvIAJ5txDN_1hJoOaGU4ZFOKoLoWsgf3Gt6k2TnnxfqsLnHIdoc6bFBwQ7LNTGsX6k8BeuOKdnYbnHWzY0CrE6PhMj3r95QHxuzOOKU_EsesE1txKFrwpj7M0iF64fsZa2_6m5V_vG2QYw0YQPxtWrD5uetXmrjLvPgyLVe7k7UsFF0cr7az4DmbJOue5BRwhAET_Kvr3Dd3-QFY3ryid_jptHhfwGmrj8DDDunvh-03CSAp8G8IM2WFOdwU9UrtCoBxOykz3fAUuKpSQ9hEoHcqQh-FZ7_In6PAf6MVNRl2g3New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE6XUqcspKVQfkffdCV2INot2dzZgwnOUXdb2VdAbV_e4RMaor8LegDub2DI_Fc7Rordx26uDs-S3YyuIXAcjTFpR4AtMLoQAd9wwFKmC8Wwg2aKNtq8d1Gy6sQPwImK__Lq4XnvLk8fetIiRGFiY9zyDiT_QWaH01XPp_DvTptUWLdr_Q4XqO3UyGCbl2e6PpZVDHkCif8sT1nNkssGu_Jb6_qhrb2z02j-8aJH9xe1-5MPxveTYnEM61wCTlz0F0BzqcIIKU6bFkRL8Ta5FdDId-U7fx-vkpYg1oNl9rp6CPTWl6uzNNHwbvIAbgRLYnuQzda4UhhD_bMd2cTXRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی از جمله Channel 12 گزارش داده‌اند انفجار بزرگی که در منطقه بیت شِمش دیده و شنیده شد، مربوط به فعالیت شرکت دولتی دفاعی Tomer بوده است.
🔴
این شرکت سامانه‌های پیشران موشکی تولید می‌کند؛ از جمله موتور و سیستم‌های مربوط به موشک‌های رهگیر Arrow 2 و Arrow 3 که برای مقابله با موشک‌های بالستیک استفاده می‌شوند.
اما هنوز مشخص نیست چرا این انفجار ساعت ۱۱ شب شنبه انجام شده؛ مخصوصاً بعد از گزارش‌هایی که آخر هفته درباره آماده‌سازی برای حمله احتمالی به ایران منتشر شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120492" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کان نیوز: حادثه بیت شمس اسرائیل یک انفجار کنترل‌شده داخل یک کارخانه غیرنظامی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120490" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120489">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: این ۱۴ بند شامل خروج نظامی آمریکا از مجاورت ایران، پایان محاصره دریایی، لغو محدودیتهای فروش نفت ظرف ۳۰ روز پس از هر توافق اولیه و یک ترتیبات حاکمیتی جدید برای تنگه هرمز است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120489" target="_blank">📅 00:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120488" target="_blank">📅 00:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج:
در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که در ابتدا توسط دولت آمریکا ارائه شده بود، به اضافه سه ماده‌ای که ایران به آن افزوده است.
🔴
این پیشنهاد که تا حدودی به دلیل تشدید محاصره دریایی آمریکا علیه ایران – و ظاهراً با ناراحتی ترامپ – به تأخیر افتاد، حاصل دستورات صریح به مذاکره کنندگان بود.
🔴
به گفته یک منبع مطلع، پاسخ واشنگتن که از طریق میانجیگران ارسال شده، کل این چارچوب را رد کرده است. گفته می‌شود که آمریکا بار دیگر بر مواضع از پیش تعیین شده خود در مورد پرونده هسته‌ای تأکید کرده و از پذیرش این پیش‌شرط‌ها به عنوان پیش‌نیاز هرگونه مذاکره خودداری نموده است.
🔴
با این حال، یک منبع سیاسی دیگر که از جزییات امور مطلع است، چنین توصیفی از وقایع را رد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120487" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120485" target="_blank">📅 00:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdtwhL7C28eWBMKyeIA8HvGsAa51UeFzGMzeQvFEMzDQp2cRhBzz0Cj1I2THNUZTZmPKDYJPqyHp7hjnw3S2xAYghKcVl-9mH4UsZ4pDsdTWQAOgkU0fL4T9uNC11ToDeDo9RUlHLfJXAWEXZW6WZ_vQKSit9a9hEMpyGFJ02EoWziBBX7qqPGlJissh0dL0Ga0VmmR-OVsgi8IVC_sMtYNsChZU3gPheIr3KCbQmlLAKuim5z5Lfw4iK7GCCM4ORHKGSbgGorkpw6jQX0_blds8WDuaK-H3Rig87llpYOyIzp-S6Hv7veX5aK6QTbx1n_tZRaFtv3TCmwI4xbCVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ عکسی از خودش و شی جین‌پینگ را در Truth Social منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120484" target="_blank">📅 00:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120483">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120483" target="_blank">📅 23:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfDCMoYh72YCU934UcBGgcRsmYJ430H_DTathnhzTFHCmW0h65HTVt7YfzS1Z5RxUMhMzHfJCShkkSL8zDbkBaKCrme4tLAuaEhTy9rXjsBUpntjCX9LCcpyikXVRfam3rGleKXObe8sRogyTnaXjeaufFLVQ0YcL_h6iZ0vK8FGYp7ThXXPOkG2MXOXrZabqqYEMadQ5PuecSD4FnqPbbPBX6XFwoEt7tBtRnpKTVLv3Se415-OtgxJQ8Dp79AdM6xFeFFAepeSLgHx5rItwLE3UAxdi-E7_grN-7SXkO4TcKqt7N5IYujsCUklUlAlPWSVJbXeTRaryYMPMHEqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
این آرامش قبل طوفان بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120482" target="_blank">📅 23:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPuWCNQ0znGpfJIOBH3eZTh4rZOT7f_vsDvtmAxSPulFVXPppgqcTqI8nGyk-BkRDR_bIOasZjnnbWGEo3_Hm-sgdSAVdGRCgK_zi44fiI7F80At6p6jYz0ChjLlJgBW7kPacqKJUlH48Qp41UsNmIyPoDxMHQbUKS-eYLMiIJAvcViCjOVxjOdQ0_MDQ3xkaoghpGmIea0C94Thb7EK0vI1lOep1znHpUX2xxaF4PUK0lzSXLD2-xb6JtcBl4upLnDOUrQJj5-TKivQZ7YSC1u_YplreBIOGmkJjuMJl7Z_J51fH8HRBlxaMUNC0MAXlx6HcZCeN4DNNGz4XCOBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید پیامی تهدیدآمیز از ترامپ با عنوان «شوخی نداریم» همراه با تصویری از حضور او در اتاق جنگ منتشر کرد.
🔴
در پیام کاخ سفید آمده است: «اگر به آمریکایی‌ها آسیب بزنید، یا برای آسیب‌زدن به آمریکایی‌ها توطئه و طرح‌ریزی کنید، ما شما را خواهیم یافت.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120481" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYKAXp-aM-NvadLiC0-2um3NId7NpgN0Qvr6bfN52dA4W6l4JeF-7aqjYJo9-AM3lZ1IDNKLy4a5qTBbjregK7lF-kOuLSjqiOfW7SUwH48sKAYok89i4q1LKD0S4jc2R9Ui1uD_EicrX_Nx8jmf3jbTB2TvU6mG6wrIeDEkMGNp58q72d8DcU8gsQQVJzVDIBloqh4SCFgEaxE0PXudjp7oikhiNtB3BcoIyUdAB4v_y8Jhg7_UKInvl1xQ4Dtl5zbkk21T8pF9MiJwEznJyCClzsCcwNWhCUVRsywuN9f9ZD1OaEqVa9lTDdWz_RMR-3xiuq5wFSnLRhG6Nx8Hyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1374، کل پاساژ علاءالدین: 500 میلیون
سال 1405، آیفون 17 پرومکس: 500 میلیون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120480" target="_blank">📅 23:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120479" target="_blank">📅 23:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
العربیه به نقل از پاکستان: حضور وزیر کشور پاکستان در ایران یک روز دیگر ادامه خواهد یافت تا در مورد چشم‌انداز ازسرگیری مذاکرات گفت‌وگو شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120478" target="_blank">📅 23:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
العربیه به نقل از پاکستان: حضور وزیر کشور پاکستان در ایران یک روز دیگر ادامه خواهد یافت تا در مورد چشم‌انداز ازسرگیری مذاکرات گفت‌وگو شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120477" target="_blank">📅 23:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سی ان ان: ترامپ بدون پیشرفت در موضوع ایران از چین بازگشت و نسبت به مذاکرات متوقف شده بی‌صبرتر می‌شود،هم اکنون ترامپ در حال بررسی گزینه های نظامی بر علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120476" target="_blank">📅 23:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120475" target="_blank">📅 23:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXOgL8hG9x5FZLA6DN77WAxL2C8hVE-tz_g9JGG0XveiYbXfc36G7cgTv8FVYGmFmw8J7KgHRCw9tzIZUK6IUjucg2yqsbvabny8yfZxbWeu0eT_XJUgfC9JVn_MfZaDuHDA3lJGE_B_NACILVgFvFRxSE0HLUJrHgUxlgBadnvyXSnXShRCH6q5hds-Qg4uQcxUhmOFHIE78t8eU7qTVS3w5V9TzQRZIAfeZc8UQ2E7cPLHIx0IMIf47NDmpgbASn3iVBOMka5IXx1X8MrO8tHXcm95PZrogEAbbifyrmMVgUuvJ4x6kpI4NFTxdI756Y1Dmdy_mnOw0ezCA356hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120474" target="_blank">📅 23:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4581f1ff1a.mp4?token=e217og9J_i2Wgs3P0tWMcf76wdQGnGLZd8edQulX9AvmX_TH7KqOQT92YHyG8wfv_6OMJm9UO-9UM3dSY2VhjtW-aLlRUuNzc6-BatQdmZVOtYtHFZjCEwFMUPi7AFtjva9BUujTVgR6j0zXz9t6aUtygTjiidsx7oLNlYg7f-U0OBkaQv8X3rNG10xx91dq8SbCNC5VmTWMfX5GMOkWsT9c9iBRsWZMVFVWHGkXULlCSuQ8fpoDWHDvFYBfCMZ4tXxqWZWP60jcVh1uKE5ePXScmsFQRA-kAsK6oIp-qmiYJvm-8ZRKm4gFfnlj5NMpspB0m5LK2RFZCawM44e7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4581f1ff1a.mp4?token=e217og9J_i2Wgs3P0tWMcf76wdQGnGLZd8edQulX9AvmX_TH7KqOQT92YHyG8wfv_6OMJm9UO-9UM3dSY2VhjtW-aLlRUuNzc6-BatQdmZVOtYtHFZjCEwFMUPi7AFtjva9BUujTVgR6j0zXz9t6aUtygTjiidsx7oLNlYg7f-U0OBkaQv8X3rNG10xx91dq8SbCNC5VmTWMfX5GMOkWsT9c9iBRsWZMVFVWHGkXULlCSuQ8fpoDWHDvFYBfCMZ4tXxqWZWP60jcVh1uKE5ePXScmsFQRA-kAsK6oIp-qmiYJvm-8ZRKm4gFfnlj5NMpspB0m5LK2RFZCawM44e7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران در گذشته بارها تنگه هرمز را بسته است!
🔴
ترامپ : ایران سال‌هاست که با استفاده از تنگه هرمز، جهان را تحت فشار گذاشته است.
🔴
ایران از انسداد تنگه هرمز بارها و بارها بهره برداری کرده! (بارها تنگه را بسته است)
🔴
آنها در گذشته تنگه را بسته‌اند. از آن به عنوان یک سلاح استفاده کردند!
🔴
اما الان نمی‌توانند از آن به عنوان سلاح علیه من استفاده ‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120473" target="_blank">📅 23:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یه پهپاد حزب‌الله مستقیم به خودروی ارتش اسرائیل خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/120472" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/120471" target="_blank">📅 23:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک ساب اختصاصی
━━━━━━━━━━━━━━━
📦
۵ گیگ ➜  650,000 تومان
✅
📦
۱۰ گیگ ➜  990,000 تومان
✅
📦
۵۰ گیگ ➜  4,500,000 تومان
✅
━━━━━━━━━━━━━━
🛒
خرید فوری از ربات
👇
@Flashnetofferbot
کانالشون:
@flashnnet
⚡️
FLASH NET | همیشه آنلاین، همیشه پایدار
⚡️</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120470" target="_blank">📅 23:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb22a2603.mp4?token=XhQ_X4qZ9acyNrHt5pIxqdiDs0Q9bL2u2Bwoe3QZVNUIPFfsnlRjI023GDFyiX8H5M-PrCqNY1N0HTcsewbUBkwnxal_q-TlBfO5Usu4XBLBKL_6J5fQwGwj2oh7ta64N70HKQP1-hL9piHeNNyk5IfvnNnsHTODq6IYgji2_DjSA8Jd7ZkzXLhw1_zRtXWb65OBQe4ap_IA77Id6IoKQQPf5ZAjFKcBmERyXKlJKUqjBWFYCIOMX_Na-HTAJb2obhJjwJ9zUy2T3q665PMRkiPjHDrDLuFcKzsAaw1qtvkOVDvoCCwbKnFwC1nHkQn-fKWcgBjTaKJeZMpu7QKqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb22a2603.mp4?token=XhQ_X4qZ9acyNrHt5pIxqdiDs0Q9bL2u2Bwoe3QZVNUIPFfsnlRjI023GDFyiX8H5M-PrCqNY1N0HTcsewbUBkwnxal_q-TlBfO5Usu4XBLBKL_6J5fQwGwj2oh7ta64N70HKQP1-hL9piHeNNyk5IfvnNnsHTODq6IYgji2_DjSA8Jd7ZkzXLhw1_zRtXWb65OBQe4ap_IA77Id6IoKQQPf5ZAjFKcBmERyXKlJKUqjBWFYCIOMX_Na-HTAJb2obhJjwJ9zUy2T3q665PMRkiPjHDrDLuFcKzsAaw1qtvkOVDvoCCwbKnFwC1nHkQn-fKWcgBjTaKJeZMpu7QKqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسول جلیلی، عضو شورای عالی فضای مجازی،چهره نزدیک به جلیلی: اینستاگرام مثل اف۳۵، اف۲۲ و ای۱۰ آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/120469" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIXiAzAMrzj6id_NwPa3EZ0k3L0wmCfZtJJs78p5f8lpTCKuU3mo3wNQmbUC0Qm-xjDDpjFziCnVrOybtMQ43agHck7HLPm1JArZ-sJcnICL-1S2vf92cEzxU6-XNZayGR_vlHYpy0SusdKFmil9RDIFYxR7dRC32JbGhN5821evZEKb4KD4oCqDBUBOWXo9j-302wzbbulJdav5Y9ahDbLOvGEOmFJhIM-tiivw1qPXcyU-5lO56rnGxgxZ--mw0nqDBGkZS6zx12Mn_QDx-88D2bDbPPaXUtHjws_q0B_3DKVPsBNlp5u84ZCGfaMFSMfdC4SCSaVWxNas6mIfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: جهان در آستانهٔ نظمی نوین قرار دارد.
🔴
چنان‌که رئیس‌جمهور شی گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
🔴
آینده از آنِ جنوب جهانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120468" target="_blank">📅 22:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9y1FxQ0tgw4_Ls6AhWxe3tFYyfmJHnKHLxR-B3YFftdL63p0I_iTxNlumcqYQfDb6aj9jmLg9N82FEbAy4RLgLVf6nikr-rVdVyfBoyVYNT0Q36twsOh4fG5Z8zQeMNdJ06ipjw9BQiWK37svlHj65zkiP2M_qNrSIm_BNV2hcg_3ZGP4sewUBztcflUIIjg0kYOTXVU52HvfPAfobH9II6XAgyxAJL2wvDxgFLnvQbdx1IckjQAHiysc4j9_w6tBdsu-1Zz9N9K5YvT6b-gRt_a3qAQm_ESuDoPm3c9qjJ2pd6WnooNUAZF_jxm_m-pv7M7rEV7NCu_g99PPiXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت بیمه ایرانی تنگه هرمز راه‌اندازی شد
🔴
سایت «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگه هرمز را شروع کرد.
🔴
بر این اساس، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج فارس، تنگه هرمز و آبراه‌های اطراف آن عبور می‌کنند، ارائه می‌شود و پرداخت‌ها با بیت‌کوین، تسویه خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120467" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کوثری، عضو‌ کمیسیون امنیت ملی مجلس: دشمن باید بداند، ما در خشکی و دریا امکاناتی داریم که هنوز به کار‌گرفته نشده و در صورت نیاز استفاده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120466" target="_blank">📅 22:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUa9SIAKgoneyP7x1Mgv0_GKnR3SWLH2CHc6Hp3rV_2yPIuIYLsDUeavch2Sbi2MeRNPfHMEXM1PE5knl0jk52F_pqZwISNQSGfC5Ohscjt90b7ca9j_EcwxsPwntp23fIQwBiwKoqGpkHpHPv6Kf5SyaQGRvjhnt7gbN_21QUIyCjUBJ5YBwF_73oTIt0K44hZ4G_LSPL447wMiQyVo5lpxuJa18l1vpCCOVF5uzACM6O6BtTGa6jSyU-xZrKUOqEupLMf1CKA4f1Vj3V1gXERMjDv2NzE86uhR_lxgaarVHVF8VxyiIDMwwJFjphXRVYgmhETPmtgxHVLhzZdDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورل، مقام ارشد سابق اتحادیه اروپا:
ناتوانی اتحادیه اروپا در دستیابی به مواضع مشترک در مورد مسائل ژئوپلیتیکی، جایگاه جهانی آن را تضعیف کرده است.
🔴
اتحادیه اروپا در شکل فعلی خود قادر به پاسخگویی به واقعیت‌های ژئوپلیتیکی پرشتاب امروزی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120465" target="_blank">📅 22:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از سخنگوی کاخ سفید: رئیس جمهور فقط توافقی را می‌پذیرد که از امنیت ملی ما محافظت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120464" target="_blank">📅 22:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رهبر حماس: ما هیچوقت تسلیم دشمن نمیشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120463" target="_blank">📅 22:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سفارت پاکستان در ایران: گفت‌وگوهای سطح بالا بین تهران و اسلام‌آباد درباره «تلاش‌های میانجی‌گرانه» در جریان است.
🔴
وزیر کشور پاکستان به تهران در چارچوب تلاش‌ها برای «تسهیل گفت‌وگو» صورت می‌گیرد
🔴
وزیر کشور ایران از تلاش‌های ژنرال عاصم منیر برای «حل مناقشه موجود» تمجید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120462" target="_blank">📅 22:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💢
فوری/گزارش‌ها از پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120461" target="_blank">📅 22:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyc3HqnHKKqAfA2b_sXo217rMpawwlZ413N92K-OMy5ZGyPWPTsWkTVO6kn7o7MvLaCHr8K8tLYjNcnPBwmi5Skncz1-UHwjSEcVt34zGAlMsL2oiHClx-8jq4yeqkduQOtqSJ92axmVavOCeuniuQW_kExK_-ZjoFpNIbWfCHzFVl2q33l3jCgTOWDTdxo51bx-Kx7G3yBVcLqD6Gm20f7UnSELwcfqrP0aAl2soRAwwyA6Bxgl6fJs8eAUpQgdAz5Cjxa9PnoNZO8YrH2kkuFVyJcvTofrKpvloQ1w0s9u8EvGeQ1L1nG4sNqjPy6Jz8d3zt9iLVV66eoZQVl72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک افسر اسرائیلی از گردان جولان در جنوب لبنان پس از انفجار یک خودروی بمب‌گذاری شده کشته شد و به گفته ارتش اسرائیل و رسانه‌های اسرائیلی، تعداد کل کشته‌های ارتش اسرائیل در لبنان از آغاز جنگ به ۲۰ نفر رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120460" target="_blank">📅 22:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران و آمریکا بر سر یک موضوع توافق دارند: فعلا درباره سرنوشت ذخایر اورانیوم گفتگو نشود
🔴
در حالی که بن‌بست دیپلماتیک بین تهران و واشنگتن ادامه دارد، یک نقطه اشتراک وجود دارد: هر دو طرف می‌گویند که در حال حاضر درباره سرنوشت ذخایر اورانیوم غنی‌شده ایران بحث نمی‌کنند.
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، روز جمعه دوباره در هواپیمای ایرفورس وان ادعا کرد که ایران گفته بود مواد شکافت‌پذیر را به واشنگتن تحویل خواهد داد و سپس از این کار سرباز زده است، ادعایی که تهران آن را رد کرده است. اما ترامپ ادعا کرد ایران معتقد است که به‌تنهایی نمی‌تواند این مواد را به صورت فیزیکی جابه‌جا کند، بنابراین این موضوع فعلاً از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120459" target="_blank">📅 21:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نتانیاهو : اگه آمریکا دوباره بخواد عملیات نظامی علیه ایران رو شروع کنه، اسرائیل آماده‌ست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120458" target="_blank">📅 21:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=TIIA0OwCdLQx7cf1CKHf01OI4qgx0P251JunFpq4RG6stAKL6sxpxWst8reExzgavX7u_rztAk6TJLnPRsINiKMl55-eJcBZX2mSgfEA2h1qVukNX6vBCPRj8FXBTxT2yz1b4zqsp4fDpoKb9KNWo5uXJtO8HHw-hx0u3epboUTDpoiqmNVPPhy4FK1x6NTJh_dBcBXZ1z4pvEwpnHct4kU8t1W2fUoIIbOV-SU7BvED9MW0XOSe7vhIIQKcjzdGPdZxZ-hVsg5lwoo_MAgSsoDfI38uKSF0jhM5VCr-469xXLLc1cv_UzGXbjOVffSfg6bpJ_NpfJk39PBDy_P7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=TIIA0OwCdLQx7cf1CKHf01OI4qgx0P251JunFpq4RG6stAKL6sxpxWst8reExzgavX7u_rztAk6TJLnPRsINiKMl55-eJcBZX2mSgfEA2h1qVukNX6vBCPRj8FXBTxT2yz1b4zqsp4fDpoKb9KNWo5uXJtO8HHw-hx0u3epboUTDpoiqmNVPPhy4FK1x6NTJh_dBcBXZ1z4pvEwpnHct4kU8t1W2fUoIIbOV-SU7BvED9MW0XOSe7vhIIQKcjzdGPdZxZ-hVsg5lwoo_MAgSsoDfI38uKSF0jhM5VCr-469xXLLc1cv_UzGXbjOVffSfg6bpJ_NpfJk39PBDy_P7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ درباره ایران در Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120457" target="_blank">📅 21:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3O4ZbyzroxOo4kAZ2GkVhfHs2mSGSMDHsTt7dsGl19HOf4_Syaqb0yVWo_5007pm_l2gHy-1ZC4y-pWzy2dEysBUjTX6UQdG27aq0SyQkKC_PxDsUii87rANb4Hs7ptIyWTFZWnXGI4n0qNCc7CzFXXv6AcES-_iCG8zigN_asd8UtFYZ4yTzs0inY1L7ogoLl-1bjDO_JppoMNPWOkQL1b-O4NBuSjqo1Ry6jzWOpboH1TNAo9QzXvU6BI_eajfx21fk_ZKx4U9-hqdVDycAn2oDNMXnzYlh2zdF8IxQCiJSqMMzyAKsuSkU5sZIsyBS0t7X6-GeTNDrBZEJeGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از شهر بنت جبیل، قبل و بعد از حمله اسرائیل به این شهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120456" target="_blank">📅 21:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
الجزیره: بیش از یک میلیون لبنانی توسط اسرائیل از خانه‌هایشان رانده شده‌اند
🔴
بیش از یک میلیون نفر در لبنان بر اثر حملات اسرائیل آواره شده‌اند، از جمله پناهندگان فلسطینی که دهه‌ها فقدان و آوارگی را تجربه می‌کنند.
🔴
بسیاری از خانواده‌ها همچنان بی‌خانمان هستند، زیرا محله‌های حومه جنوبی بیروت با ویرانی گسترده و ناامنی مداوم مواجه هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120455" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c07hbxi9_Nf612psYP-dDVmv3bZy8Lpn4b9HojdSx6PZBpYE96QO7iE7W-ozB3JORopmna02_o9guuRLKWqlc3Thy96O4p1cz7bTtHGJrsTsNXlhcYUdWBdq83DToEBQ9Da98muy1d_xlzGtQvyWmET4pkX2h9dfaGjSGrg-0O_KMUMFGMsYXK2PlVx1r5feMaOqu9Q0Nz1o1-hr15H_S4dOM6n7mEdwFojCKxIKTT6IDXswpOriUH8mIQ3rvcmh6lfA8Uz-MkJddx7_oAEizjoPMxueQG8WS59aitpO8wjSlVY7NbBQjoH_73n38aFHrC2qLSwVZ1QBJYLBZGUO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، بایدن رو مسخره کرده : چه تفاوت بزرگی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120454" target="_blank">📅 21:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcpD4kiQU55_MkUBfYw6vPkpXLi2iSwdA69DSt5OUm3h5zIP3oH7adp7ivw5Ht-Kk8F0Oo-DT55WQ7I474gQu0FRED16WY3THgCCtBr091jcMRjvrbUIhLn6W_agN1a_sQNbJ4p8L4LgGLV_nfo9QBwPfwFpL1z0_pipmEV_VYeZvLsgIiYc49eLwSRwKKneTD34PWB3A5yy8Eea_2Czhe1awrWrqUJXgenO1vpcwRtVmjCJ0Zyji8YCwFVC7XOBFPFslEqXXiG5tkvWp4-EJ3mpsmOgPQ0geliEKABE2CpZt-4eEC6126jOIJUq5ymFi6OnvYVCATOV8BGvGaYg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابک جهانبخش، خواننده: به تازگی از همسرم جدا شدم، من اونو از ۰ به ۱۰۰ رسوندم اما اون با ۲ تا بچه ولم کرد رفت. زنم فقط به چشم عابر بانک بهم نگاه میکرد و از من به عنوان پله موفقیت خودش استفاده کرد.
نظرتون؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120453" target="_blank">📅 21:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : تو اسرائیل یه سری برآوردا هست که میگن احتمال داره جنگ با ایران به‌زودی دوباره شروع بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120452" target="_blank">📅 21:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqce6qwBRY2TGMKHoepQhhNGNuyPQIssSlfMUx4vl4Q7mRZ2dm3dZdQ8u_qq-43k2NWtK3zC7CNmxobnfBxXXe4XpikoweVWk3DLuYdNYjvSwgASIGWpvdOv_ubriq-pn5OYsJi-yfqXIWn2W6rQ4LE0mDiFMNCITAT3gDhhyWy2IbLzTcPulj_90eJSG-jKVUHKt0-tLdXqPrW-JEgJog74S7shdXOXl6uPW5l4N2vUDKsF6ZYKzXJ2it8lIldsTtvq6vufd42GBtZT9oTOBs4qdEIXT00WQadcZSEIF0oUUitXuLrWYvv63S4BOGW73f0jh6Jl8ecFHl1D0VjYJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120451" target="_blank">📅 21:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwKvL-bOzwffxdvn61_F0i5h-fhofcnUvAcawFC7ymyM9HpqcF956AFolzXnXkizsGCJi1vFcLoMOssgyMQAMsvy7b4pZUTegTjGM0wRlFFRH_sRMUJy6gXuRRK3TyCRh2DdCYNRIx6rqykLlr-QxLgyTwPpfP08zsniy8wvrOf6YNAb4Kc0HqV5WnrH_e0l5YBdA3bkzQChEOyrZU7YIbne0QCCU3G_8DwvUEBnL2e-CpbhENmxIljfGJNsqiMVNmcIRdoan3TyCNsVlvHXbUgvYGjYOUhIz23xrTDDV2adFC3pmeV8A5ndtMDgeLEJSe-IB2uTbWFmAauAZbaEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YowlcsejIwUWVLMxVlnFFdRKNvvgZbDmYo74PLMdSbZaHFt2oy1jAnoWkx2DmCW5gEtIb37N2UJQTGFxW5S7ySvOnlmaeBDefCpPNMJbyKXTPpczlVy4QUo7FpSrDxb0b-gfQyF_K2EFA1mBqWBlvhnn8A2EZzBtqJCcQNEJMDIWqP8ujcLLAAdlyKQHVeFgwHKp3tq5eMjGHTPExZfxLKVXuZRpnX90zx3pLpi61nNu7KuqFuNNMuzrhwS-fQQ3qOlRDe72Gvbb4Hxras_x-3SdETCnhO26ig8nOybCFZ_W-jjouLLBCsQdNJsrWTp3HxB7kyJGNWdqzYOY0qZtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZqRvJGcJc2ZWz4MlvLyOsKAHUkC7atCiKKLRiGUl76ln3ssNc2Chr4LS0pApWSxflOM32oekdFdbCM-_5FxX4sKl8iUshwVsqyPGUBMjr_2lH3pRpL96_-GOAjInP-wL_gdlga7r0HPnMFhIHlA0LnEmnz_7jWPVwZmHoCr-KvOOXqhTFT1ERDFxHwYa2puCN-pozEI13dzSUkPP7cmwyueRqd8s9OrSj5baj7BdI85wFu3Md53b3fUhE5Mg8qMRRlA4wfOU3Q1WBKrsPatAv9dJjBClbY1Hujx8Tw3F7Pmqac8wfZHYwq9bxzmaj9W3avJKR8cf1TRhlC8H0zCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUbzNYZ8-xO-zdGlVvQEi-HNf5lkXVv9HBi-vEF8JB54u6hLL8vUb4dNt0gpslxDdtP1apDrjL3aI0GPRYvDdsr6Q80rxQBc8Zc1Khb0Y8CAVj3tXNFJlNguMV1J3SIPHHlbX7JVOIr2V2tZmWhHtiUKzrpFEl7t2dviFMy6nCMTB7kbQmwcHnSGXu7l4eEg5eQPeuInrrn750LMAXce5rSuCqXUoEevHfVjVT_gl8guND35062DEiruw27T3tREeiZTWMGNGE31X0GW2etlyvGCMWigo-XP8DvAmkGBYLfKwaV2B9Dzs2Euz3VfrIycDTsrvycGZRNLg9XVAv4wZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به تازگی خودرویی را در غرب شهر غزه هدف قرار داد که منجر به کشته شدن حداقل ۳ فلسطینی و زخمی شدن چندین نفر دیگر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120447" target="_blank">📅 20:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRE5uqT9QskIE9pDh_k1Vt92-oNfhc3hGbqlWwtQ7-twc-V67zliu_B_iFUfD7pCi12D7bzxnbAin3Xk6hdeq1d2ZfzP7T78Q0yFMGTtBAd0OS8qyFl2PUb9QSKzgyt5Zc5nDAW5PI3BRuC5yWBwTfDZMG-G_oAEyRJmXiaEMMeuMZaHdJTWhSUITVuu_o-KgCuUK4XSbUIz6ear_wq6ff27iMu9a3SpHl_1smpmOBSfLa_Ekb7zKWs2pX9JeV2I62Ep4G9_SFvj5wL1NdM14Yx5TWBYuWxQPUEJiFG2tIFwXHWNOM542gEcoMD4rOuFZ9YLdKWGdHudjSV4VWl5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت مرغ
🔴
اردیبهشت ۴۰۴ کیلویی ۸۵ هزار
🔴
اردیبهشت ۴۰۵ کیلویی ۳۸۰ هزار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120446" target="_blank">📅 20:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff57b4508.mp4?token=EZCuZRwczKwLKKA-RncHbThczJ7_MscyEPJZ-qerO6d6Pv3LiRvM7SU9Bm5xQh3Im1fjCTjAb1J1hD73Oj_Y2xk1UokVeukAeWVyfLN-MMX65pxvAQGaxx3mU6I3HXTGDcPAsjhCApoR-m3iOKhKBCnhdvRARFTFvpPWOyLSWiWaeZhzHMI9EHQeOxIaPfCHQ0tfVgC25dLCPWDJqCht4tl47mvmR2fD2pt7FkUeP0CzsSyyaYAmJ_qo0AylC7CCx_ILwf4bFMTZwgNbnaLYQHWbRA78_Dg27qKtxdWXznz5DLYhVhAUwVS_y5IhwoIkBR0U_0aZlfzJz1zAFmMlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff57b4508.mp4?token=EZCuZRwczKwLKKA-RncHbThczJ7_MscyEPJZ-qerO6d6Pv3LiRvM7SU9Bm5xQh3Im1fjCTjAb1J1hD73Oj_Y2xk1UokVeukAeWVyfLN-MMX65pxvAQGaxx3mU6I3HXTGDcPAsjhCApoR-m3iOKhKBCnhdvRARFTFvpPWOyLSWiWaeZhzHMI9EHQeOxIaPfCHQ0tfVgC25dLCPWDJqCht4tl47mvmR2fD2pt7FkUeP0CzsSyyaYAmJ_qo0AylC7CCx_ILwf4bFMTZwgNbnaLYQHWbRA78_Dg27qKtxdWXznz5DLYhVhAUwVS_y5IhwoIkBR0U_0aZlfzJz1zAFmMlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا به کشتیِ که داشت مواد جابجا میکرد با تیر هشدار داد و توقیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/120445" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
زمین‌لرزه ای به بزرگی ۴.۵ ریشتر دقایقی پیش گلوگاه در استان مازندران را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120444" target="_blank">📅 20:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا در گفت‌وگوی تلفنی با شبکه فرانسوی «بی‌اف‌ام‌تی‌وی» آینده مذاکرات با ایران را نامشخص توصیف کرد.
🔴
او هشدار داد که در صورت شکست مذاکرات، ایران با پیامدهای سنگینی روبه‌رو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120443" target="_blank">📅 20:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار سی‌ان‌ان، کیتلان کالینز، می‌گوید: «ترامپ ظاهراً نمی‌خوابد.
🔴
«یک منبع یک بار به من گفت هیچوقت کسی دوست ندارد در یک سفر طولانی مثلاً به آسیا در هواپیمای رئیس جمهور باشد… ترامپ همیشه بیدار است و حرف می‌زند، و اگر کارکنانش خواب باشند، می‌فرستد بیدارشان کنند چون می‌خواهد با آنها صحبت کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120442" target="_blank">📅 20:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020cf5e837.mp4?token=SMmQQfReX0P4VekASyWNoKJwuDCopor35MKoFUOXPs2wMp9z5lGMflXdzy9Mgt9sUIcFeYgrKCIhrPhN5YjonItFYIRtpcXmWpybGD9eiOvxH0kiXRTdPH9WY_KfDJSwXsoNk1uiPDTO6dcXzy8LJmtwZlZdGQlGBEnbZO4NAm-_8kWS9nzYmfuBi1Ox2m_fGM6gKTkzSn1iW3pGJxqQ9W_k2M1-DRO1iB5_HdHZwUKglrh2JM2_qeoyKNtQoICZTvtEZUCbT9-k0R1548jSrZHIWDuRgSdjtB02be8jqKt5ytYbege9tBQu8pQErl0l_BgzwvaQqcOJnHi5udyqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020cf5e837.mp4?token=SMmQQfReX0P4VekASyWNoKJwuDCopor35MKoFUOXPs2wMp9z5lGMflXdzy9Mgt9sUIcFeYgrKCIhrPhN5YjonItFYIRtpcXmWpybGD9eiOvxH0kiXRTdPH9WY_KfDJSwXsoNk1uiPDTO6dcXzy8LJmtwZlZdGQlGBEnbZO4NAm-_8kWS9nzYmfuBi1Ox2m_fGM6gKTkzSn1iW3pGJxqQ9W_k2M1-DRO1iB5_HdHZwUKglrh2JM2_qeoyKNtQoICZTvtEZUCbT9-k0R1548jSrZHIWDuRgSdjtB02be8jqKt5ytYbege9tBQu8pQErl0l_BgzwvaQqcOJnHi5udyqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرده است که در طول آخر هفته حملاتی به حدود ۱۰۰ هدف حزب‌الله در جنوب لبنان انجام داده است.
🔴
این اهداف شامل موقعیت‌های نظارتی، محل‌های ذخیره سلاح و سایر زیرساخت‌هایی بود که ادعا می‌شود توسط حزب‌الله استفاده می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120441" target="_blank">📅 20:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e055879407.mp4?token=GNLjYmdoysjOWO77SaAf0fX0QINtbWq6Yl_kFgqzPBtMUezmfCLEJKegj4CfDDZWV5YJyYOhITkQWls0JvCWrDZKU2dvAhJjOvlm1KQol0fOGEJ8pT1xb9IuYbPR3MwS42DiBxUmx283x58qrq10T7AeqadrtA6vY-b3DGK5m3T-LnB00VpcU8aLA4Wq6-CDZ7ZSHnVzMMxrSL94OA9KUmkQjSpJKMh6O9wkZVsqFY9dHHmprBw2sPh4ALN2pazbFfCn6_IuJG4OIfnEqflZscQtCJqEcaTVGn1dwezWNmt8FzNT4D9PXw5WkpK-3AQCFlZT4y5qLSHQIM_Z4zMjwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e055879407.mp4?token=GNLjYmdoysjOWO77SaAf0fX0QINtbWq6Yl_kFgqzPBtMUezmfCLEJKegj4CfDDZWV5YJyYOhITkQWls0JvCWrDZKU2dvAhJjOvlm1KQol0fOGEJ8pT1xb9IuYbPR3MwS42DiBxUmx283x58qrq10T7AeqadrtA6vY-b3DGK5m3T-LnB00VpcU8aLA4Wq6-CDZ7ZSHnVzMMxrSL94OA9KUmkQjSpJKMh6O9wkZVsqFY9dHHmprBw2sPh4ALN2pazbFfCn6_IuJG4OIfnEqflZscQtCJqEcaTVGn1dwezWNmt8FzNT4D9PXw5WkpK-3AQCFlZT4y5qLSHQIM_Z4zMjwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز بمب افکن B-52 تو پایگاه هوایی فِرفورد تمرین‌‌های خودشو انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120440" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
معاریو: ترامپ در آستانه چراغ سبز به اسرائیل برای ازسرگیری حملات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120439" target="_blank">📅 20:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کاخ سفید : همه گزینه ها در مورد ایران تو اختیار ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/120438" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان، به نقل از منابع آگاه:
در دولت ترامپ نظرات متفاوتی در مورد چگونگی برخورد با ایران وجود دارد.
🔴
دولت ترامپ و مقامات پنتاگون بر حملات هدفمند اصرار دارند، در حالی که دیگران از دیپلماسی حمایت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120437" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جنوب لبنان دقایقی قبل ، پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120436" target="_blank">📅 19:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRY-MA60g_DNNgVhriLOhBP9PiXDremonAsrHlfOwxkEbJp6hSP92mI21CEaSOEQCJ8ZbQz3LZX3j9vjYQVSPp3AW01gX50ZohIJTy-ZUkzbuxY3laTxx4WX6SQYcis54OpzhhF4NbMxY5T9xdM9c617RzKwCwKh2hgu6v1uTEFJK7SHPc74Mj1GkJm1zk2snk-np_045IhXj3C6ANVOS272gdcwyoK6MoHnvFVnai07xJ6kmLwuVLJSMSSG-k-0SEzH2YklApnQ-Qezq88S9KR4G8IClPTDzEQgg-SfNqkX5hWN23v2C7T5eh1gNE0R7I3h2kssQX1Yt730dX0dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، موضع چین در قبال قطعنامه ضدایرانی بحرین و آمریکا در ارتباط با تنگه هرمز را تایید کرد و گفت «روسیه هم همین دیدگاه را دارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120435" target="_blank">📅 19:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هیمتی رئیس بانک مرکزی: با قدرت، شتاب تورم را کنترل خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120434" target="_blank">📅 19:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1bb05efa.mp4?token=J-S8XyFfE7mqnlI52zG-Wfa5JCj-Htv4iaDRVUUEVf-5qunv11TK9I3vzLhjFX2WBCFKB6hc474X9uixFPJFJKR3_L4IdvO2l6eNLwxrNZPgVhtew4Pl_yjw-0OjamY1KImDdSxYxNum0tF8bWP8idIt7DHHKWAKTMUWveVBSIOkschBlJ5DkrDRrbRWrzplHC4SsVCE014hfsLDOsOLkaK8LXNHrZJKjGbBknv3ctwqy5mi8cSfaW6whoss5WxJR1O6ldMWlo24PofyRW_g-jbf8NdfeY2lwfhTvR0SxdKA62qZm5EUrYXbVZiMM_5YRZPqcOwCJMNrSafzux5wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1bb05efa.mp4?token=J-S8XyFfE7mqnlI52zG-Wfa5JCj-Htv4iaDRVUUEVf-5qunv11TK9I3vzLhjFX2WBCFKB6hc474X9uixFPJFJKR3_L4IdvO2l6eNLwxrNZPgVhtew4Pl_yjw-0OjamY1KImDdSxYxNum0tF8bWP8idIt7DHHKWAKTMUWveVBSIOkschBlJ5DkrDRrbRWrzplHC4SsVCE014hfsLDOsOLkaK8LXNHrZJKjGbBknv3ctwqy5mi8cSfaW6whoss5WxJR1O6ldMWlo24PofyRW_g-jbf8NdfeY2lwfhTvR0SxdKA62qZm5EUrYXbVZiMM_5YRZPqcOwCJMNrSafzux5wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز ایران یه نفتکش حامل ۴۵۰ هزار بشکه نفت رو به دلیل نقض قوانین جدید تو تنگه هرمز توقیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120433" target="_blank">📅 19:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کامران یوسف خبرنگار رسانه پاکستانی اکسپرس نیوز: سفر اعلام‌نشده وزیر کشور پاکستان به تهران، بخشی از تلاش آخر برای حصول توافق بین ایران و آمریکا است.
🔴
نقوی از معتمدان نزدیک فیلد مارشال (فرمانده ارتش پاکستان) است و یک ماه پیش نیز او را در سفر سه‌روزه‌اش به ایران همراهی کرده بود.
🔴
با توجه به اینکه ترامپ پس از سفر پکن به واشنگتن بازگشته و در حال اندیشیدن به گام بعدی است، سفر وزیر کشور پاکستان حیاتی تلقی می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/120432" target="_blank">📅 19:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120431" target="_blank">📅 19:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJFjnRshuoHqMVWIYa6Yd5I-HHVv1TGp7KSbfmdfbkesNjaJzuzZc_EU9QnipgW7sgMENn26r39YaEP4wsbnWotcPkpLb7G91-7kDr72mx_AQjFh8dMun_gAkB0Tg4aCLG3cyMsP8rRIgJ6k04N8M15uMGOI0dZYIEFPqiAK2rdnLsFj0ePTJUUsypRTLhieedLzuMTVhETFOig7npuAbjHC7Q5tvPQOVcDWvv-PjH2-doOkxjIEqNeBAcAXxFMWUAb2V_MAsoIJYX0gVQMoWp1Izo007DLmYHL1ZInhd0DH1Y_apxSLGmwMLTmpqSZW0NwMSN_asueXzXvW75tZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف : مقامای ارشد دولت ترامپ از امارات خواستن تو جنگ علیه ایران بیشتر وارد عمل بشه..
🔴
حتی صحبت از حمله به جزایر ایرانی تو خلیج فارس هم شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/120430" target="_blank">📅 19:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
حماس: جنبش حماس یک دور انتخابات برای انتخاب رئیس خود برگزار کرده اما نتیجه در دور اول مشخص نشده؛ دور دوم بعداً برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120429" target="_blank">📅 19:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر بهداشت مستعفی در بریتانیا عزم خود را برای نامزدی جهت جانشینی استارمر اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/120428" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
به گزارش آناتولی، دونالد ترامپ، رئیس جمهور دولت آمریکا  در گفتگو با رسانه‌های فرانسوی درباره مذاکرات با ایران مدعی شد: آن‌ها علاقه‌مند به دستیابی به توافق هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120427" target="_blank">📅 19:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اولیانوف دیپلمات ارشد روس اعلام کرد که مسکو نیز همانند چین، پیش‌نویس قطعنامه آمریکا و اعراب درمورد تنگه هرمز را مناسب نمی داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120426" target="_blank">📅 19:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گسیل ترابری نظامی آمریکا به منطقه طی ساعات اخیر افزایشی بوده اما نکته مهم خاموش کردن سامانه و عدم ذکر مقصد در پروازهای اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120425" target="_blank">📅 18:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
العربیه: طبق گفته منابع آگاه پاکستانی، در بحث تنگه هرمز، پیشرفت‌هایی حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/120424" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مدیر روس‌اتم: عملیات بتن‌ریزی و آرماتوربندی ساختمان‌های واحد دوم نیروگاه هسته‌ای بوشهر در ایران از سر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/120423" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/120422" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a616414a5.mp4?token=FqFSF8OAXDXxpFP2wqRIl75bNIbbAemXZvMX-K590cR8h1APhlpipPiDduPUYTBPNsUMKaB6xJhRI4dhbNIthDBG-bs0g1kwcgiZpnCshBS-mNnDlXUmRbyx1DiUqFS8p2CW25Yfm7Tf1pOpcl9x2I-_C0zXLm_z3A6xZyqwqOwN4ATNMyofaOBzG6fgyH-j6SEfboGf5Zhn7Dt_8LGQHkuS9lpJLAyRfy9zwdWFkeHJuWMSd0NZzZ2HPS_Zmfhi-oR4csdKfNF5NDdiEa2XuB9I5O3MqSIMfyNCMwsyb1jE8Kb7agAuJrf57lLReuPVfAZRxEHeeJuUhrZvkqW6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a616414a5.mp4?token=FqFSF8OAXDXxpFP2wqRIl75bNIbbAemXZvMX-K590cR8h1APhlpipPiDduPUYTBPNsUMKaB6xJhRI4dhbNIthDBG-bs0g1kwcgiZpnCshBS-mNnDlXUmRbyx1DiUqFS8p2CW25Yfm7Tf1pOpcl9x2I-_C0zXLm_z3A6xZyqwqOwN4ATNMyofaOBzG6fgyH-j6SEfboGf5Zhn7Dt_8LGQHkuS9lpJLAyRfy9zwdWFkeHJuWMSd0NZzZ2HPS_Zmfhi-oR4csdKfNF5NDdiEa2XuB9I5O3MqSIMfyNCMwsyb1jE8Kb7agAuJrf57lLReuPVfAZRxEHeeJuUhrZvkqW6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب و طوفانی توچال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/120421" target="_blank">📅 18:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssdvGskLDJuddeCXMKkYnvfcwX87Ib2cRf2b7E6l6qNObC2f43Opx-xfChtYjRzuI8X5eWliiSTTeZqBaOtoDByQFfFkMbU4S5yvmMzjtoWCiUJjEtoFiwK28AuvlMg8MQazvrohhYFlGXV6pykQK1uLv5-n8b7q6J1xUbegitfGUGawqo0RmnEFXQDmXekhDDlgg_SWcFzRaNfllSPeJzQNiDJRckIKxxZKnm0Xxd8Eb5IxzhirVzqYhciQFCl3P0HkClCH-hrnpdU9JqnStpwGft5u4TwgEUpv3aqkB3UJZOK7dU9-oK4rC90YxEuAipA-BkI23moCOBXe1fs-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری صداوسیمای جمهوری اسلامی، روز شنبه ۲۶ اردیبهشت در گزارشی اختصاصی اعلام کرد که «چند کشور اروپایی» به‌دنبال انجام امور اداری و دریافت «تاییدیه» از تهران هستند تا بتوانند شناورهایشان را از تنگه هرمز عبور دهند.
🔴
این خبرگزاری با اشاره به گزارش‌ها از عبور موفق نفتکش‌هایی از چین، ژاپن و پاکستان از مسیر تعیین شده از سوی جمهوری اسلامی، تاکید کرد که این عبورها با «اجازه نیروی دریایی ایران» انجام شده است. صداوسیما نام این «کشورهای اروپایی» را اعلام نکرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120420" target="_blank">📅 18:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امتحانات خرداد دانش‌آموزان پایه‌های هفتم تا دهم اصفهان غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/120419" target="_blank">📅 18:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaYHiQNCqefEctnXIVmrjcDqtKU4pcIO3L70b8QhO3-lIRC_5Zuyn2FtZdHOGsQMS9CyAa85uU5c2Xgws31b2Y8fI5fjZ7luCTtskuLkFS0EIZrFNv-EsvOEfs7WlQrSqrih3vRRVvv2kzkXl8GqFTtVyE44cH4h5kKqGoo89tPet0XlbB80LfTCO0iwRJWEHex-1Iakl-F7q_NKt9Zjr7Fq5b6KQ2WjUht0l8w5YH4_WknpU4k_nxq8PWMqlkkGYOz-xyB9nxPYHi0aPQQZjZTVoNoabmyUH_3Kgfd08NaowWBfxex_sNeshkuA0m4WEPA2kUts0zmQBMrMLfrKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کویت تصویر تسلیم شدن چهار پاسدار را منتشر کرد!
🔴
کویت با صدور بیانیه‌ای جمهوری اسلامی را به حمله به جزیره «بوبیان» با قایق‌های ماهیگیری  متهم کرد و اعلام کرد نیروهای سپاه پاسداران قصد خرابکاری داشتند؛ یک نظامی  کویتی در درگیری زخمی و ۴ تن از عناصر وابسته به سپاه دستگیر شدند.
🔴
چهار پاسدار احتمالا نیروی قدس با دیدن اولین اسلحه دست طرف مقابل تسلیم شدند !
🔴
دو سرهنگ، یک سرگرد و یک ستوان‌یکم.
🤔
عملیات آغاز نشده لو رفت و تسلیم شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120418" target="_blank">📅 18:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هم اکنون گزارش رسانه های عربی از تحرکات بزرگ نظامی در سراسر خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120417" target="_blank">📅 18:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: به گفته دو منبع آگاه، در داخل کاخ سفید هیچ تلاشی برای متقاعد کردن ترامپ به خویشتنداری بیشتر در پیام‌هایش درباره ایران صورت نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120416" target="_blank">📅 18:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UavQQgsYzKXAbQDGHe1Qf2c2oGNbIyN4eI46PjHjK2I-OrKfaJx06JeAEwkETAafl2fVcCZexBFFzRLgDtM3a1iCciy_LDOOsr8y84-xDrDDZzFZt4TpFNQ1yI4nv5rpW5uNzN225qzvOxUrmkODSzIexJTGhVzDNF_malYnmeEDgH7GG_VL60PSc7TlvQ7tzuvlRT6tLUCfXG2ptBIPrcXR5gHT0A9zZf3UpMxW03buYkpJ81Y4bynrH-s3pUvnlYHUcbsvuPIFWeSmo9ACa8fAgq3GdRiXeF9Jnmr-u_SIqt2gRZCrpmYFmrhTpihhfv0BS0U85XB9Kv2fhPahcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9GtgCsZ4VGIM9LKQFTdwm_EyorZs2RhNjen8l0bzaezEVOtzlSCzznBQFjVzqBks09HbwWjOjNw2quX4VkKIDb23jPA_dndqPBvcZRMyWPtWzOETE-CIjhljv2G1ZWy2f5JxIykzwxbD1Vw9qBEzFpNw62_AzRj9gpdj40AhRZ119L34Dy2x7Yl8mYoHv3IENASNUBdM7AVJ-0cQ1XkQBJdTXN25vLi7jxRiPGxVYNXDpQkxAETNIuXGUgVP5MWoeD0V_XNc-9MLHUFnUYWj4c1aIidfGOU4k_vfbAZwh4wbhx9UTUmBKqjqsxuJdCyaICFUOGq7bp2V5zH5nWM2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ی‌ نیروی هوایی اسرائیل به المنصوری، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120414" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حماس تأیید کرد که عزالدین الحداد، فرماندهی از تیپ‌های عزالدین القسام، در حمله هوایی هدفمند اسرائیل شب گذشته در شهر غزه کشته شد.
🔴
گروه ادعا می‌کند علاوه بر همسر و دختر الحداد، چندین غیرنظامی دیگر نیز در این حمله کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120413" target="_blank">📅 18:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b8f05fcb.mp4?token=K9dEJie0QzA3lKTdC1v3nEqEMcrIecHl9Mi4iD1g5hTU73JYMR3j84xUO3sdVxsyKn9nAtkL8-JQrXrsfk1xCbXlkfYD6MxXsDw2Gq-YHGE8Cm5tImcMY8XUzynDk4obKudpv6EpQgneg9lZ8fs-mklpRPLVlwRRtAtr4XGmCVnEAkqICMLlNsh_5NUY4r5gO350R4ankFf3vD17n9Sbfwv1W4EjY-o1Pq_WVs506XJnaHwZTFs467W_oDP53jniQGV3B0X2DKy5WzMCRB6ZP1MIp-P_QpQsAeJgfUXmXhQLJcAEa477IW99nq3cB3SwLs1ySCtGqq6o0ICe4Hcu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b8f05fcb.mp4?token=K9dEJie0QzA3lKTdC1v3nEqEMcrIecHl9Mi4iD1g5hTU73JYMR3j84xUO3sdVxsyKn9nAtkL8-JQrXrsfk1xCbXlkfYD6MxXsDw2Gq-YHGE8Cm5tImcMY8XUzynDk4obKudpv6EpQgneg9lZ8fs-mklpRPLVlwRRtAtr4XGmCVnEAkqICMLlNsh_5NUY4r5gO350R4ankFf3vD17n9Sbfwv1W4EjY-o1Pq_WVs506XJnaHwZTFs467W_oDP53jniQGV3B0X2DKy5WzMCRB6ZP1MIp-P_QpQsAeJgfUXmXhQLJcAEa477IW99nq3cB3SwLs1ySCtGqq6o0ICe4Hcu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ، پیت هگستث، دریانوردان گروه ضربت ناو هواپیمابر USS Gerald R. Ford را پس از بازگشت به پایگاه نیروی دریایی نورفولک از یک ماموریت تاریخی ۱۱ ماهه، خوش‌آمد گفت.
🔴
ویدیوی اول از USS Gerald R. Ford (CVN-78) است و ویدیوی دوم هگستث را در حال خطاب قرار دادن نیروها در USS Bainbridge (DDG-96) نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120411" target="_blank">📅 18:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کرملین : پوتین با رئیس امارات متحده عربی درباره ایران گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120408" target="_blank">📅 18:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj6iYgAMu25TD2LDZWqum0IOAXaJLXFg_tc-hzL-VPNZpMW7pyJBU5QT9j84zRK3X80APtrBawtBEO1GAtLmRV-vNo1VeDii_miAWbred2iTNWRF-oFeOQZHnbjXGiE76V8nLBPzfQrHMzM2eOtpZ_j9999ZKgMAU4l0MSuwdpy65_xmGA0fHTDPpBrjJDUTX2ED1lk2yLRry5MTCla9f8EF4t37SgSFrmvpX6L35EyUuCXJFWZeG-WbJz6HmdMDFaHtDZZhfzngizPDuJGwkRIz1pzrZvwht7sNpM4JwHSUodkHTOvswns7sNCBjLdFhxmgmvh4CGfndP5Naz-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
بازی نداریم! ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120407" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ویدیویی از ورود وزیر کشور پاکستان به ایران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/120406" target="_blank">📅 18:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120404">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDvq0GgTXB8kgnS6qrtH9SNlGOaZc3b0OQJW5F0v4vr7E2a8DIorZUOpHrxbA0XX3Dry7ZR59dCHZxa4UEl7rfs2RFHXHxzIO69RyKei7xVkKF3hRJQhdsX00H0vTe9evakwvqp4cgg6j_x2Tdeo2LI9qXhYenvghU-C3bvPD4nNkkXIobqbvyxIhQFH2kCS_ocr7sz4f3Rm_btTtFKmQT16UF9Ak8KPo8fBIlgq8T23RBrw3x8Aax6eNjImMsM5OEOqxwhU9pXAsqYMbczxqO0O5aJ3RbDJk_7FF4SjmOJje9ulWzxcQWPFErT3UtqjP7Il3T940mbqOjTGklovPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e829d87678.mp4?token=XXynBzPnBKuCXcBrXgvrG-5zCDf3Ham9G9KXtb6H_H107m5mM7BKQ1ReSRFNUVz9DoBYeyHEWOsURgbYm12Z3b5aSAMIg1Ka-nur_JYmWWQ5UcIs8lelQ39UKY255-r6ofyyKTjFBiPVAmTr_fYFdFd-9Mq6N6sSssKfFyiiCJ1yA8uikSAqDJKhfAlw1FnbRCIHsvG1i4FvWb1r1Dr0URehEvWhx4FGMCkUwLhkiD_dGpDLfrRMKSP_nz5oLhlvqQ27WgGf0R4J-l1cW7odq5AbvRqs0gf1oUKAqH68IexuCZ3P9RZqjL0sdphdWw5IgadbcJsTryk-pZW1TfefDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e829d87678.mp4?token=XXynBzPnBKuCXcBrXgvrG-5zCDf3Ham9G9KXtb6H_H107m5mM7BKQ1ReSRFNUVz9DoBYeyHEWOsURgbYm12Z3b5aSAMIg1Ka-nur_JYmWWQ5UcIs8lelQ39UKY255-r6ofyyKTjFBiPVAmTr_fYFdFd-9Mq6N6sSssKfFyiiCJ1yA8uikSAqDJKhfAlw1FnbRCIHsvG1i4FvWb1r1Dr0URehEvWhx4FGMCkUwLhkiD_dGpDLfrRMKSP_nz5oLhlvqQ27WgGf0R4J-l1cW7odq5AbvRqs0gf1oUKAqH68IexuCZ3P9RZqjL0sdphdWw5IgadbcJsTryk-pZW1TfefDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند.
🔴
شش نفر از این افراد توسط پلیس دستگیر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120404" target="_blank">📅 17:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120403">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgNQ90du7wv7TIUtMMAyYbi0yTABNNBmqyCvtoGUZK5jUHUIGeLrSAgpRkYpPIbN-EtIB_bxGp6dmQv6w0AeiMf9Af7qadsI3yp8PyusrKBKz7wQ1dPwHQ4vkch7m6R87jmGy81jbqui10HACY8gsv_E9lgEotfYu0rnoB_Un5UvJQ7oUEX_orx3ZjdPcUnpDFpft1ufC3EQ1gq7L6HUbB1ge3yeLvGMpU4PWIxBz3vy8Hsp06dozI04LUu-GlKMjwCqeCNpJvXL7nI3Sk_EBXTF_d35wuMBawHiYYUzxY5fkxbAygGQI5VIdS3XGiqMcePdh5R8to_WRN7cS4VqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دورف، مالک تلگرام: دبی دوباره شلوغ و پر ترافیک شده
- از همین الان دلم برای آتش‌بازی‌های ایرانی تنگ شده، حداقل شهر رو از آدمای زودباور خالی می‌کردن
- پدافند اماراتم زیر اون حجم آتیش خیلی خوب کار کرد
- با مالیات صفر درصد، امنیتی بهتر از اروپاییایی داریم که نصف درآمدشونو مالیات میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120403" target="_blank">📅 17:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120402">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d65uil_jDNmDBm8nVsyUg9I3S6ClnyfI8q42yVvgnZMl_MyJhjW9E_OQuSmWxv2v6JhRsl_jFUI1UDSfhqr0anRfBaXl_7CuyTKFGuYwooH8lDzwljpmSwCnwyCIdDvMtec69b5IAp5xWOp7v5fHrQY-wAvZz0gOmt3Pj99uUG88n96Hsdbh9ZxG_m1E2zlpjBYzEYc3EGU6IoNb8mhPxRSPY_5QWky4EdDZFc6A-QkXbA7JHZA8rnfglmKdw9wpGywa5DTsM5wHwUD2O7YK1b8AFXhluRZs2l4PI8YVqNAWj9-GM0UR9p1p70j8UfsnLZEk_jBMF9q-FcoUjFT_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب موسی
😁
فروش کانفیگ وی توری
🔐
گیگی 195.000 تومان
☄️
گیگی 220.000 تومان
☄️
🔥
سرعت موشکی
💎
( پنل مشاهده حجم در ربات )
لوکیشن ترکیه
برای خرید ربات رو استارت کنید
BOT
📎
@WinstonMarket_bot
PV
✉️
@mosadeveloper
CH
📣
https://t.me/winstonservice</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120402" target="_blank">📅 17:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72181fb229.mp4?token=UYbmPPHW7muiPVlsIbw5NB66hcTyiRbH9Nf2pYKLuJZKQQenz83YIixoNPEI6QSTM5KInvz0nMeQvmPcUe7GZyXpTiVIYYA7jwIAWNWdEH56CRH4lk1xFy2RqRXk9qeqeDlF9ca3dwN3hVmOVRv-r952W4_VXs_sqxx59q6_AJDLavC6YSEuFIMi2wbZJuh2nM64UzuoG0Q0SF9Daymc3mwkVPNJU8v_Qd8TmoRe4lLEmVSmh9YuWuQTHcucVbxcGn1M4z5cRxKv-bdf7_Yz0BUcgMCxhBzPZvH5U5NBalpABTNQT8Eu0EtpaOw6iMbilMRwFyMiKWzXBPYJZEurHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72181fb229.mp4?token=UYbmPPHW7muiPVlsIbw5NB66hcTyiRbH9Nf2pYKLuJZKQQenz83YIixoNPEI6QSTM5KInvz0nMeQvmPcUe7GZyXpTiVIYYA7jwIAWNWdEH56CRH4lk1xFy2RqRXk9qeqeDlF9ca3dwN3hVmOVRv-r952W4_VXs_sqxx59q6_AJDLavC6YSEuFIMi2wbZJuh2nM64UzuoG0Q0SF9Daymc3mwkVPNJU8v_Qd8TmoRe4lLEmVSmh9YuWuQTHcucVbxcGn1M4z5cRxKv-bdf7_Yz0BUcgMCxhBzPZvH5U5NBalpABTNQT8Eu0EtpaOw6iMbilMRwFyMiKWzXBPYJZEurHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120400" target="_blank">📅 17:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر نفت عراق: ۱۰ میلیون بشکه نفط در ماه گذشته از تنگه هرمز صادر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120399" target="_blank">📅 17:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ویدیویی از ورود وزیر کشور پاکستان به ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120398" target="_blank">📅 17:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
هم اکنون بمباران در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120397" target="_blank">📅 17:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfJcM-StishnlLusKaRqSrbkIzd91Sim8jIpY0sIpiqTZxKsdx6WBtKhbXttG44_1TDtCyhSbu4ZTOMhGGwhVt7wI1OAPMkkvVYu0OKZXYvJX88IQ7r2i9fuZ3ytrP6EpLfkSqyHFfzeva6Di608Otzd3pSrgnAbKZhRULEpXUETSWKtB-0uc_Pa1jb26kM4aO7_vt3cNGIbDzRlS6AvvObQUGS-5EuNJJ-xrFgkTdFVdY5VtToRiZDPEzK1YLKG7NZWX6KC_bURt1BpGwPWqntv7M7Jj3qjDCLPEpKb9Kj4-dxZir9vpsgqlgvKMpFnYH_rfKvyS21Z8YXqVGcQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدرنالین خالص
🔥
💥
سلتیک در آخرین بازی فصل مقابل هارت به برتری ۳بر۱ رسید و قهرمان اسکاتلند شد
🚫
هارت رقیب مستقیم سلتیک بود و با یک تساوی هم میتونست قهرمان بشه اما با گل دقیقه ۸۹ مائدا قافیه رو باخت
@AloSport</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120396" target="_blank">📅 17:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc03da9d9.mp4?token=vV3IPTD-ngCIxMsptpKyj3LNFHrgw4tBnspmE1HcmR8mAudWZnAIswdST63spHRBEcSis1p89XppyEHTK82vj8BKHjGCrEd2yNJ49vRw_8y1mCY3C39d5kFTkeTUIniiv0fnpKPGwKrKD2q35OsdAOURcZs8N6v-sm2PsuUGNVwoxhYW6kEgYarMnds2Lja4fhzRk-VlhVjBdvc3EsqC05-7tt0p0Mb_u9MnmQHJq1vJQ-lIw4feNAlXvIHiq8jWyJLe97oRCkhfMIwN1vLeNxgiGh8wiBn4HgKHDQun3zGx7Pjkfzbc2wI7Wr_6-LQdPzcnNbKwhM_PIls2ldWFNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc03da9d9.mp4?token=vV3IPTD-ngCIxMsptpKyj3LNFHrgw4tBnspmE1HcmR8mAudWZnAIswdST63spHRBEcSis1p89XppyEHTK82vj8BKHjGCrEd2yNJ49vRw_8y1mCY3C39d5kFTkeTUIniiv0fnpKPGwKrKD2q35OsdAOURcZs8N6v-sm2PsuUGNVwoxhYW6kEgYarMnds2Lja4fhzRk-VlhVjBdvc3EsqC05-7tt0p0Mb_u9MnmQHJq1vJQ-lIw4feNAlXvIHiq8jWyJLe97oRCkhfMIwN1vLeNxgiGh8wiBn4HgKHDQun3zGx7Pjkfzbc2wI7Wr_6-LQdPzcnNbKwhM_PIls2ldWFNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
به گواهی تاریخی هاشمی رفسنجانی، خون کودکان میناب و تمام قربانیان جنگ ایران و آمریکا به گردن علی خامنه‌ای است.
🔴
هاشمی رفسنجانی: «نظرم آن بود که باید مسائل با آمریکا را حل کنیم. با آقای خامنه‌ای یکی دو ساعت بحث کردیم، ولی به نتیجه نرسیدیم.
🔴
من گفتم: ما حرف دیگری به شما نمی‌توانیم بزنیم، فقط مساله‌ی ما هست و خدا؛ بالاخره روز قیامت از ما می‌پرسند این همه ضرری که این طرف (به مردم ایران) هست، اگر این‌ها را شما به عهده می‌گیرید من دیگر حرفی ندارم.»
🔴
علی خامنه‌ای گفت: «بله جواب خدا با من».
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120395" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBYHGYi2AF1O-CxtVPaW7E9pdbaUx1Uae-XbVix15s7jpAgtEKcv0dlNdeizvKf6dA8Ifngky2vb6xuJ6iL5P3yDvL8OaRTZotdZFS9XA3bDnHy3A3nY-IaAU9uSRVTNdkcKObxeD0sDUZUZRcaQYckH4lYbQsk3Wu0q_2rGGMWObJItVOsbKpmBrgHlPEd4v0s64-AH-wCHPuNQj_Wor5YlWHjLTcJ9MY7DfqADTXfiNhuj4ci0HMrlv71BbQ-mJdk1tQOTyE4xtBAIcE0BkEymuGwChLmfUqi4O05doT1pSIdNsClFxRNCVFUBPpO8is2xmEWiwQok9GhbFxulZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZp77g-BCL29K2aIznR0ySz2wqOhCJBAq6KBLaQVlCHqMeyC17z8kGXuzo0mxKmQ74hwxHC9T6RtINQzDFxa3m6sf2Cqj-7I_mDoMAc0g6YKkbU5TGCpfnf7u2Z8wHbxqcw68zefUDB25tjg-QaIHGRB1v50i7bxrsTD9g4qPmbHQC-ILMu9n7Lm7njwJubxV2K1yYgYCu9-jZR-QDjkxjcAq4l3Eb83AN4ohCcfbGxthc-OqilCG2Mmtr_HXWrJoTIrswopXEUkdw3PZVDgbiZU4F1lD8OSKpp2vvqR5PL8fXczfvHu1j9r2rioC5pGgNfe9Xxywf59KomFNy6OEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ی‌ نیروی هوایی اسرائیل به المنصوری، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120393" target="_blank">📅 17:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120392">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تا امروز، ۷۸ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین محاصره رعایت می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120392" target="_blank">📅 17:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120391">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4aa4bf95d.mp4?token=NYsWY2XtRkxcZV6WJiXDHZpUE5rSWClFbc2JS9zsZZpwb292UGF-LjYGAjrmxHMN0dZENv-Es2k5ehr8mq6fKvlFK31NlrQH_vt4fWNEhw08Ba56b6qqe2-EsSg2F2XL_n5O_Z4GP_uQrdEGWsjOBGmtNynwrKN1hMcdHCo4EtkI9kcLmv6L8-XLTy5prihLoiZ18VioS07Rir56A4enSBMlM-1m2_MF7Cu3zYPqGsmeX_PTae6BaFyDM6Ir5x7nVXHkibW8N5vG5xU-fM33_RMetL1ctcUNRcG6r6mjfgcA0e8TAn3b4loZaBcHcbrTX943N-KmfRSYHBkJzxFrIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4aa4bf95d.mp4?token=NYsWY2XtRkxcZV6WJiXDHZpUE5rSWClFbc2JS9zsZZpwb292UGF-LjYGAjrmxHMN0dZENv-Es2k5ehr8mq6fKvlFK31NlrQH_vt4fWNEhw08Ba56b6qqe2-EsSg2F2XL_n5O_Z4GP_uQrdEGWsjOBGmtNynwrKN1hMcdHCo4EtkI9kcLmv6L8-XLTy5prihLoiZ18VioS07Rir56A4enSBMlM-1m2_MF7Cu3zYPqGsmeX_PTae6BaFyDM6Ir5x7nVXHkibW8N5vG5xU-fM33_RMetL1ctcUNRcG6r6mjfgcA0e8TAn3b4loZaBcHcbrTX943N-KmfRSYHBkJzxFrIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: ما از حق حاکمیت خود در تنگه هرمز گذشته بودیم و اجازه دادیم از تنگه‌ای که متعلق به ایران است تجهیزات نظامی که قرار بود علیه ما استفاده کنند، عبور دهند؛ دیگر این کار را نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/120391" target="_blank">📅 17:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4552dff5.mp4?token=NgCjgjoqx8zkGmzCkHe9R_duzT1gFqGkjtn32hFyil4-YMou9pM3Zx2wXOhWjxvitc4tNAAz5u5ExqVZ9PROVaPzMs6l0W-UdhftbdnwR5uldUjUJDfeiveVqN6xefKGHJecfHTmaT2gkZBIniLu5eVbSX_MHTJJtyZP9dcnzaV5N6TZ9u64nkwsCsPnNDtzF2tfCLhxIF4Pd951aSmGeIqVlFFR8QVvcSs-_qn26XrqQ5Ygqn8bTxHBoixwreZsJ5VCj5-NKykFuTiv9ifMSm89x04RETQJ5xnkLnhW1y_Q5pgGsyOnY3rtmDUr9BF77rRsfmIA7g2vrj8LETGHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4552dff5.mp4?token=NgCjgjoqx8zkGmzCkHe9R_duzT1gFqGkjtn32hFyil4-YMou9pM3Zx2wXOhWjxvitc4tNAAz5u5ExqVZ9PROVaPzMs6l0W-UdhftbdnwR5uldUjUJDfeiveVqN6xefKGHJecfHTmaT2gkZBIniLu5eVbSX_MHTJJtyZP9dcnzaV5N6TZ9u64nkwsCsPnNDtzF2tfCLhxIF4Pd951aSmGeIqVlFFR8QVvcSs-_qn26XrqQ5Ygqn8bTxHBoixwreZsJ5VCj5-NKykFuTiv9ifMSm89x04RETQJ5xnkLnhW1y_Q5pgGsyOnY3rtmDUr9BF77rRsfmIA7g2vrj8LETGHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دفتر ریاست جمهوری تایوان:
جمهوری چین یک کشور دموکراتیک مستقل و دارای حاکمیت است.
پکن هیچ حقی برای ادعا نسبت به تایوان ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/120390" target="_blank">📅 16:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسانه‌های رسمی ایران: کشورهای اروپایی در حال گفتگو با تهران درباره تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120389" target="_blank">📅 16:50 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/MQV8QfIv5h66PivvoKpqYQjDY6GLVOW-7vzZtw1jJbhNO-vRydOzyBWbcvoc5hgYMg6La90Ma7JEEraJIP-Cr8dZPxojHIhNoECT_drB5RyR8JtB_g9o8iQkUJN4QYZmyMsECSX-MyRxz6mpPJMRa7M15JV7yTbGpuWMmHmloH4EQfJJT3-qfI6fhrBSeXtgik14VILTlOb5csdoNw9mxqHBAR7-RrtgXSVPEulO-YacPsBvNa4Vj73a7p4LpmQ-AxFpkqXdq_Zm0WtRNrtYsB_nxNhx4EpjfjXqV56snKNg4L2y_H1i6KgmaI3bjWE9FBpwPz_JK-ozEs3QGyplXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYTO4BDIEoxM3kll3W3r8pSqF0YZE--zZ9hrw-uvvbh-57N0b2MAP40JcDGpywRAfZ40p1Dna6yHw6NzJhJdtedbSi_0iG9KEohtM4bQln0dkmM0peQIm7UVfwqnLllAhBVDguV0msi1Mq6RHY0lLfE0ncgbwa_rduOlHxL61Tedk5MD_-kE2CsosrpkL6d-XOBrk0njDjkfDiQ2ogIBH5lGGntMOVJ5jWVx-_0m63p2QgZqrLZBlPG3mwnPBp5-BUVdSH9LpNav-aPMtzsvBEL6E5BOz1NciJNbb6qLj3h5LNMhIuu1kBQBL73QB547MYRWvCFsZrdY--bzDEwEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6RZlm2qBFzNSgTHhsUmZTYiB2wvber-TaAhx4AyJ8IcVJ4No6L63_nv7toUT1yNqYf1qSgEhFMyXzojvNiITr4CkeGrp4Tfe4WGIopSuLRisE86fBrt_LPg7HtJCwCSeY0SxHG5Tgrci8Lq_4Imy2r03kt-UUP4OLBOFZH2n35eDFWiSK_19SByys4ufG9PmzSHLKJeZeIJdOs_uzeyTiSbjxnq9QeaieUIJHZ2WvYPYd2y8Sq5zu0x7z2CH5F-ICJSBJd6W07Gsvf6eJcs9KfDyQdaCpUDcGgi4U5uTL0dv68ynu1KMFBvB1Me3eLvK4Nr21OlEzSLdo59EMcjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caz3IggL-8AsuVYMuVw_b8pCCAmrXNBetS-KsckbojWV1_I8ncgpVORRcXVQwOV4byEEMeZcMRe2YpJtQrUjLHrA3ILbEdW_Uee1pJgish5kEwiF4btL_2pduYKVSiuN12QdiHKO9qNtr-DTBzHm52WqVNwZfmB3XvuDARSZpqUgqnFw1gXKqdbHqCWe5ym3Kjq_mMGDl658Kb7w4dDwRt8zxLusgM6UK8ZH35N2qZSC3O4ZY2B0PEIXca545-AJ9nDxjRGmjKK5W8wTluUezpyxbH1jTNbm3ALw_YVb_VLKOVdRdOocaVIs2mod30MRx6OlEiDWeOXlzmy5tzJ10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ba28W7k0Kd55kaieyu5p2ORP6U1pqpC5emORRFs3SoCAB6lIBG96B5TUEtIPTAD65oYAt7NoSFyvLxBaJHECiNB2xeeNyVKnkuHmrrQa7EMG3qJa3ihUKbQL8-jQKrzvFEAE0p675nnhmIgIPS1uTtOobHfjdeZMKS2MWBANY3RYBFiK_3qYgMIlDDybdOjHmE0CsPUD5VUNoJdsxo1ojWwwiDsGjPBsXqFqaIymNHA0Tthvyo2WiJKwte8sl6i1KbMftq9k3AcHhCX4tczuO-1IQF1Hgxd0eSSHZKpRcKSjdXQS46DcWs1aGMMffKBQvgxBz-BDBCbno20jjk9nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 600 · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdJhQ6FtIfvB8AcRc1Tgr0rtMjW6pQtkgpI6xzuIjwnaZMi5fGEv_CeX2LESmElaXFXPHf1VS3joxX5G4yFvmzxembh8QPL_wEyRx9KK6o3yV4E0NAYZONoE-8S5rc749OpRCZPpku4rlbOSZs1jbMQaLKTRVJ79ao1pNu99_SO70zcSMWSeCX5ESYQL5g0vDsWMKCHYgIXMAbFuZcHZES8w4Y3GbHwUkKVVVPGAoZT2-FGG6tn6KpUYrZWGZBjF59xCb1-eepcQMSug2OKq4LnxvA1uNUTgMc-97a4p55e2qNZ2him5hiHAYnSsmkSXijtj-7h7K0f8wwYtvRsYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkUk6-0nsQVFKk2sC_XiWh0j__Lv_LyY1rWwbjc3A3WDeobnXC0hJilVLWoZISmSHSJRakPk2SiHyfOEmrPvk8hSyo7imufbCt94FdiOl4lgdIOVk8abqZz1hJC3P97bPtmRHYHuD1RzC0D-Fr0gzEAvDMz745PcYTSmfPVT0F6Xhs-jhdhu76rAmLPGq_RFq-BKw6SUDMro-yBV7_BRx_LZZEEnOMBaA503Ke56uxysjKZ40bHZx4EZtAlgQTah0f4VumWmUdiTZcK_vd3-suIaa387UKbrou5sPvEXedXC5avXoCsTEnLy2MkiSpeDg2PcRLHrNV-DGwig9KKA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCRMEPCe97cu-6kPC2yAY4YqnTShPfR5ltIPTXibfkmXF5-xsKcp1gQMk_qv9r7_bGaMVddlTcsU0SBViEAiECA51pAL45QBwHB1wkM3mYz9v9HyyN--e0gN4p46z0mUp2vB4_1SGMglfk2oUHCqWx3HvMYAtj86-nHWH8pMhmY1S98GvdwEpZv-kVDzgebBAGKsYvU9j9XMEFXLYP1ol7UxbWe_0eU8by-rH_d4F99UW6wmQFxzmdvPjk566OnD4RM_rBkra59jtB8WwEd46uPf-0bJ5tUVMKyBcFx1xhc4drqP70UH2O8iFJ-NkC4ARqSsvYt_KIGkEV6_Rn0c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdPy3O8C63Fgy7IczySvGLxPfMp8G4DyExkFCQe3CY9Mp4wtR8l3_JjC3T48fU-FuxOjevfjiPA6XG9s38w98YJG0qdgb2Pfs-Md-OzDqABHYktcldJ2UcEIj_5RXQZMOw2KgtwrpgX8L0EL1Q5Oky1iQ1Zhj6DYV4UU-IeaA9wZs29tVnr-XMGJ_ve5_xlKdqexJqh66h9C8yn-YHX--O23A5MaDnrxBFb4myLlQDEUV_AWHqjdCLFjTBiSgV7m4HEC9gDVfYDuELMEnfIL6o90k60YXaf4HnjrLdfdHBDcA7WYQeBNhUMJWkWF4Srbu2Nd59ZpthkPDysO7fBwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0liE6J2wFVU8Qa4sL2WvvwBKkhq7kcSIfSfmAgTdpCLdvMWOGVKkmju5_OUm_GH0ttVzdfr_TsrKhDBA64fquK5KujdhMqz8LVLz5l9hD0tSvpRvVtzRYsfsLn9LfIGcgevWAx2a-nPGwP-uxEZfht23vCgVa-odvlDR_mYneX59XKtU4eJQRwYXbiy6OoJpbKiE0CO79-SMPed42-fdxLGj1qtS7Yh9s1T4oPHeCshgwauqnWCh4_KJLMmIltMYecEhfPSp3FD1Tu4sUh_vliYK2gtaNgD5_RqE1dF7-Vr0TSkGhq4TPwHS_9FnEG9N9VhhvvwgOTPR01DE71drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxgVswh3Kmeex-hTaEYnb4bFwQPMUhrONvMN66x6UQ9upZxwgwnA0FTUKq6HiCelSJ-Uc0oBzLe5LuvD9K9jNPwM6XJVT4tbDh4owzJt7P0kD8h2VNcd5Q1Uwo9KOkTWyxpHt8Y9jHLULcb2BLiL78q3e_56otL42erZdL4LwP1iIuRiJnxjm8Dg8INYPYXJHabsa8o0PWLgtfO3PpWOjbXSetn2qRdzNBIJ9QA4Mf5WrkhmjleNjwi5gt_1eTxrGNQ2bKiOl1fxzOX2z-0opZJ0StMXRachyvm0Dq2rkIodyX6RoMkJij3_ZsHWp0e5GzersDBSTf4a2o5z6B6fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fuoEdYQp0DVqDBMqe3vsQRovPjLdpQFO11QXh9FQcRfN_9mWDq9IVMRZrjEdoMmlekAzPPgbwh17Ap4G-D2mksNyOQaTWniaFnKfUs1EWRyr60BorlisHXTnJwUvcnzMU4iVJthrZDaAevH577Gps8AKBm_pVJjdkTzlKlGqieAys3jgouP7EaT6nsir-MwE1gdRFq_0ULFt-vh7hn05ngE6V15xG4kXmujxAoXe-u7XR3908C5zgWpHG67cKH0DQ4pA8gjZhr0wsjbGqxDYIWHUemeiu0rUtex1Wbe63OmtW91iSGPvq1nOUPRrP4St_3nbgEJcgsQ21QIrmv680g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=hQ98wNWekNxAdZB8wzo3Mnja7JETLkL4amAZi3uE6wIl09zRaA6zYvG2yo5_VqGzzS5IsERCyZtuEbMEPqG1S4nkBgGzKcXRDXb9f_ku4uOWHoUJuIjiNF5_AjJq5WIlZ_OpokBSjQmmRMDIefYhCjfmQewrEweV5vAfqsmsq1mmwphDDQp3YuBEjoDFOQ0GPlit55K0iSt4VKH_hlM2qGAy1XqPaTKPIWnd4fei9Xs4iDR8BuIo14niPZFV6hSOO5wCztCDSjIGdINlNOfbnGErJcBzgvRJAmpzglnf5Z3czvBG9JEIVXBVR5B2uK44KP40wB59oVGDL1QXlji7-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=hQ98wNWekNxAdZB8wzo3Mnja7JETLkL4amAZi3uE6wIl09zRaA6zYvG2yo5_VqGzzS5IsERCyZtuEbMEPqG1S4nkBgGzKcXRDXb9f_ku4uOWHoUJuIjiNF5_AjJq5WIlZ_OpokBSjQmmRMDIefYhCjfmQewrEweV5vAfqsmsq1mmwphDDQp3YuBEjoDFOQ0GPlit55K0iSt4VKH_hlM2qGAy1XqPaTKPIWnd4fei9Xs4iDR8BuIo14niPZFV6hSOO5wCztCDSjIGdINlNOfbnGErJcBzgvRJAmpzglnf5Z3czvBG9JEIVXBVR5B2uK44KP40wB59oVGDL1QXlji7-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieCqFDQDCeZ-1dgrP7C22t12JvrTkfZca0ZunW06lCSPNgxKQJaGxEe4XhkBNW_ibh3D4D_U-EfLjuwFMdSbh1R0wDOqfTdG1u1P1gCorPpAeX7sb89s63kqnbMsvSsh0Pfi71p5FXCcXSgshct8XXSo68oPEJXvpAh5mnn0zOVNlwNDe4EKGR10qitToJkYcXQdbc41moM_crECUT09SvlaNVzp9DnwN4RYcxMHHAjiAfjc7obIrkZDyT5nP8_cj9zyTfsR3jOnm2ITAyjVUzqi8Aya2iNP-ESEOY2tez_XrcGgGDE4s5n3yj0PePyBQ7QO6I4qKqX9UkTK_d2BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=jzUzgtYAZ2qkAQxMspq4RZlNwpU17CnwOEFczjh5Evz16wy9m2rMoVJKRZ7-aPO_QsSqwF3ydZL6LAr2uFNjljpAEXTw8gYRS1WE1RUVre6QF_OQ3tX1SRbij8mNtQrlX6VUsgxExepCwTaM_kjM_jZ18El2-eg9vuLGfavZl_rIXO7oPFkNOb5LBhZFb9kQN9Tri4GrbbgxEfseuzvftJKx8sWZ76Scaypyrck9OOoHTXsaSdHRECUp3pyiy-Low23l6jTpg1M1rvvLtyfqn3kQ9GaozRm_gRKpxVKVT0tHyTnNMG8ZRPR5HWcK96s3cS6czhMxgM7kWAYttsUryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=jzUzgtYAZ2qkAQxMspq4RZlNwpU17CnwOEFczjh5Evz16wy9m2rMoVJKRZ7-aPO_QsSqwF3ydZL6LAr2uFNjljpAEXTw8gYRS1WE1RUVre6QF_OQ3tX1SRbij8mNtQrlX6VUsgxExepCwTaM_kjM_jZ18El2-eg9vuLGfavZl_rIXO7oPFkNOb5LBhZFb9kQN9Tri4GrbbgxEfseuzvftJKx8sWZ76Scaypyrck9OOoHTXsaSdHRECUp3pyiy-Low23l6jTpg1M1rvvLtyfqn3kQ9GaozRm_gRKpxVKVT0tHyTnNMG8ZRPR5HWcK96s3cS6czhMxgM7kWAYttsUryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKsJNDhQZ5el2Bnv34B7B5xYrpNlkzqR5ZoLgQVEuvurSkC32d9Yg-JyElzkjeDXLCYXjR6bxLO2WFfOtxBpQAHrbh_YZLKkQM0PSZshh2mA4ZuHnxyy8OH9J5fYtR3Ge2FY6qKDxhUR_lXsfuh53Zs1Q-ypSzOTDopuSWLNwQIM5-exHNp6xK1nf3fVPHMTNukKdrVEZHmjtPR407mzUEg5RCveH9kqC5kKDRxsskx0qcakW5CIeVzF615JHkd0HyZIHepYgy6_uTppEXVDZmXxBUtsq0EfSgSxf89B19O4w-pV7aQeZw0Toj1klzDfCjl19-R8ttPBSQSYQwTkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqhZJkZ84plUJROz7NkQ26vZs4VLpGX0Yb3fIuNtH-7-mccxp_vWEX0zBO9IZjLuF6zMJp2ZKhJaZp47rz0hE7yhb2kOJsS4UHvf8OFpi0A-6Z5YQAluqLbqVrv9f2rhyruyOvGMwcEGaX8dww1hQXng7o1scyyQHCrk7u5v1ya3jg1Wnmm6gMsUTmnmUGUw0rBTGvVJLWhl8LfNQLQe8CaRgSPhCAAASZov02EPcFSvyTtDUZCKpqHpVfg_iHaJMwi2Jb7WtaaInFzNC83e8njuwWrJLOCevZRov7_OyDePrSl0f2xRXbKsR4GqJ5xnnQp3CArkwd0T1jnP9rCjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b2TSyixxHrfzK6M2ffLCCBq8v-8Krt2UzLUAa-7RG7qPR7fv-L0rbzBI_3oOUCssICRqr3qMS1FjUtACbuES4OLOA78UpKONMEv0M5-FY5GYwrkN6MzF-5dBx7YmaqeKkgE5wHBYSZpP-TLv-vljNWGL06kF4XwrHAHxNREiDAEt5fQ0KdihD9NMkBxE69E-tM8aKTNFQrpvfxGqqKY4_V5VDcuer9lXlnWwoRDzwBa7tDIXcAQm5LjNNBftUNBuT--seN7CLSGFveoYAG5_vwm10uvvzIX3AziLlgJW21JhtkhQuvn5dh3FTe_Uv3gnNZJKbT4gb9SKD1GoSwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVBM_fNt3NnpPvHNWZ5_Bd4E4TayMbqKmOIGyb7KzOYh7I2DxvLQKb2mhLhoCA9uzSh1G_1wySnkfNYDEk5lgTI7lnKFNtrg_h4q2l0pHqKjhx4TGT7ufibB-svsuwu9MP9BCGbegZYppnT_9sXs3CImuIQt99leCKOgKhhoEUjW04Fs6KrvBCQaZ3pTf4eE8T0t8SHTAd2BkkUJbfSoKmigotN1yBQ5Yotir3-lJYnU1mNkk8r-vP2yWhYAASjA8atf23J9sPW-uKgAJoOgK2or7WS7RXIyL2HA3kgZDF41Ph5KSqZZI2KrlNIjT1PLu-U7sXXBAQFTDl8RjYdvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWwCtTz_BVjwwC1yXvHsGkBkYb5HJE0wS1fDmQLK2yW2MVXGzDIxamLQ2oFHBhoPHIeCiV8IFswGLjtwsqDZPt5G-Fs3x9u_GC0HGWIJxhoJh5SUciKK0xBQ8975dafUykNlGAIO5iQ_la6gDIwQ-Vs_YnQlLNnjHCBdfpVJPCftu8fZRDkHSOyY_vR-avC4X7KekpE6SC8DtEXpbbpVGRDVoszrzEp3JMvNkJkPNBV5x5RkjKs0lU3LYLYQIX7Lwl8MeLsOd2rKZmOE1GGzF2NhxAM6rX5kd7N9Hbxu307JDrUEeH83r1VPSMer6GL8Cp2T7yR8wv15CCIYP4VVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KooP7ZRSP9blYe_PPixZIWN0e4h7BXtO0F2AsG81st71Dcgd1-DqAMCgnsVOVpa1QmA3NUQW-viuNQ_lcEmJ_7NzTRGAZOALOjcP05fgf3nuSTYdlHh_phn6zZMocu2nR0g-BLnAoy2KpbyuRsPCsQTcZ6K9Wz0j0SwZ8luSMw3xZeP1gE5mBc8S5MzyXjSkGL8GfpqZPYBdfyT09ELcf_uF2Iyk_afglWj-q_BNQOBApMZjNukCJLmWEWQGQuOsNEzO1VBOKQm6iuGAcuuf6u8f3pnAQAxIF-O80GlMJ5rZWLDvNDtXo6m54kTGKafE_U2BQa6rk9ScUhcN2j3t-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW1URCpm63_TSCVRGQKPQb5-VQCdfbA6oLZK6kWPwIYoyQ3Rz-ulM0j50pA1B-Yt_kVPiFM_XdXWdda3DMIxGMBY8N-sGYqtY3jvW4UMlhNCbG1Om-VAw98GjhuCvy41JsFUJpdX2Zj-8mWhV3AOPvXzCW69chcfrjuDO4RA9V1Axmr5wFBrIK0isfWwJ_hCqQ5F_caVL7d5IKS3U4zi--hofUrfeMcJnXc21lscfM9bfXVfnh7mF1KA8Zyq9VIo9Sd_xxHtGww3pylvck8N9lKf69VUeXxqlH5IRLfxlG0s2wedcqfYkqYbnTSayiWkjs3mxZyUVEiOROZE3yqnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqJaImk9qUNAczQ4AjRugEgqbgL_5wH9FAtdzNsiclDbawmqvNtSiyhM18aH4-4zkB8R_yuWSbWCxZAaOiPwJf04zkb7xCk1j9oX9947MxjCBDWIAxgAoObKaVpTOKlgFCQxbSdA0qshrtNrdED4xD3fct2k6IFb5iPua2QJnJzaMPrV2HYTuPR3H7rmMhqU2G9DS-XAZtmM_DphXbcQaUaNLrZ0a9c1DyFCE4PDgK8YCJZvZ0AeLzUNWRx-XwH20RgWn64K-Wa-nAEYPEfu8LyL4SS3EjNJqmNSGJbxODt2STVpSvLPbFDczEDjAipokgCqwbVd2v5-cn3Wx3qwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=KKn1G1wAAQN0SY43_OK1SgsDLLGspzpcFajFMNMtYkq2LdjRuT2lEnvRnxi5b7y2JVgg-IP5-SNCP3JNEtp-xWF-84wHyXmHGH20Vd_R5npaQsl-NFbGqGcm5A8scXN0brt9E2I6qCEf9ZBRn3LMsbAxnyyQ6Fl3IvnhvrL47GiY2byWRLDXMUPAS6GqlOTs1pV_rDf7RUi8hXmWOdzPKBrjtJgdmyAdRe6jP0NqMf1LiE_gJh6XGAwgJohlHNvcBw5deJV5r6k9p3gZ8dPzop_Zb5jpY9blTkigISnvH-uarzuBArSLkSpuPdxlnbcf5Qf9CMTsnv3fVEc04emifVW0lmU0AxZ7SGgllyo3F-l2gXUq_ctvuGtUfG5E02-2GRxTnJQnWuUP9spKKFfueCdoNK_lkI1IbXmUpqPW3h9sUzFRgu0hoDW3SgXQD5nkdPklBTAsZf3Se7T4WV2F-xUCsDMkJnmVx8iJy7mk11UKSax57Njcb0791s9x-e_emLHfLUhhI5COMg5Cl4f9Lkzp57h5HD1f0T8KG5tjbvT2v7Za7ez65JtXfvhT7-CpW36TUQeWeLVGbO0vI-xtJy4EfVQC7yHKvMxRGXUkP5CI31WLjn7GsM2aG1T1firhMP_REuN95Qj3zd-pzVWYXhjQ6wz0h5oRdWrUrHlYVEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=KKn1G1wAAQN0SY43_OK1SgsDLLGspzpcFajFMNMtYkq2LdjRuT2lEnvRnxi5b7y2JVgg-IP5-SNCP3JNEtp-xWF-84wHyXmHGH20Vd_R5npaQsl-NFbGqGcm5A8scXN0brt9E2I6qCEf9ZBRn3LMsbAxnyyQ6Fl3IvnhvrL47GiY2byWRLDXMUPAS6GqlOTs1pV_rDf7RUi8hXmWOdzPKBrjtJgdmyAdRe6jP0NqMf1LiE_gJh6XGAwgJohlHNvcBw5deJV5r6k9p3gZ8dPzop_Zb5jpY9blTkigISnvH-uarzuBArSLkSpuPdxlnbcf5Qf9CMTsnv3fVEc04emifVW0lmU0AxZ7SGgllyo3F-l2gXUq_ctvuGtUfG5E02-2GRxTnJQnWuUP9spKKFfueCdoNK_lkI1IbXmUpqPW3h9sUzFRgu0hoDW3SgXQD5nkdPklBTAsZf3Se7T4WV2F-xUCsDMkJnmVx8iJy7mk11UKSax57Njcb0791s9x-e_emLHfLUhhI5COMg5Cl4f9Lkzp57h5HD1f0T8KG5tjbvT2v7Za7ez65JtXfvhT7-CpW36TUQeWeLVGbO0vI-xtJy4EfVQC7yHKvMxRGXUkP5CI31WLjn7GsM2aG1T1firhMP_REuN95Qj3zd-pzVWYXhjQ6wz0h5oRdWrUrHlYVEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmwiptUFhoBdE96jTg_V7sySi-JDGmQEgbXG7EtjRpZG6ryQajfD5BkcTIoeNyJFURza8yGsyel-JAsNGumnSY0bf1PESZ6IloK6uCholbUF1-a4_3d1qzHs9tTA7sMhhnh-Mut7wPdQ80WVi6SswhSwuNyRPSUYaUWox5ExmW39b1nEaphUAn4stFNjE4pvFKDQV3Ig0MXpXBFmHrARIRJqQwIzi0pLYqECZHh88_PgJK19l5Lx_qqxHBcn9kYaF4QMuPBmhlwUxPQ4-RA-hiA2H39V7WbHluxN5aBX12pPzCMrGCD7d7_J9GWEa3Nk2sdcXtz4wPVVjk7y5Cmoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBgM08qAIUo0tIb7_H-U0QOIF8THRe6s54UDXFNKLYtqQjwMIiuZe8n7SPPFoZrbuym95N4Wt04TMujDcEK7BsRLixY97A21tbi3r-7Ph4Cjz964JNYfK1b5p6A-SvrkN7rq2Vep4KDEK5kO1f0pCzoFnRreXSRdLwuVE8-RWOIGUJ52CaM7Wjsjz6Cgo7FfPeb_J-1chLfyWnq7QfBuAYZtlf2D763pyiZJwP1iZ1a1AIlfmrg2OegF_J9WZbzxcbk2HDJa1DC2a2p79Z0kslqKvX2XOSN0sETkTEuV4AUU58yT1Gsgt11mWpW3KgydJowGh9UIKnVwKNTAI6B7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbzU0BdzWhLfNgiKGNrB-GLC225p-YLcDeVp6FVwcyhswWFR9r1Ise6aZEFSj-c32LleubP1KsSnRTj2vXcT2KSK85gi91K7p11sRN1jtVtqSihbdfLaQUvhbtAVwMprRpQWckX9l2eRTqGm0NU8S69mLHRtVf8UgPe-RyR9-Nsb9Qlby5K5YHhN_GMGFzE2G__72YmEHhpeTov7dMRtqYEefSzFTN5mLnszPorYcV9Zio-HHtm8IJEKzEZ6dYwaVclsQMGrvErFIXncopgpIkSe0QrMEwUkNI7-gTCw7z7CH_2w8_isgOoJ2-_xrw_GJqk5pGdhoMU3m4aDVTR_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLqKI5DHETxYRP9xBTx5fK94XjN_X8ancEtPgnuRH97gWzkduXurPqdwcrV9pGZsdEYkRuCu66EpPUroii1LQSXG6c4o4VgT6wR_6me87dA8T1nuY_XoybdCKpoDi5HlMwclvZULuVtyueTeAaXYotEKdeqgv59bTwk-o-7fMopI4bu0SHvqZL4tdYYwNrrZU88KzpIdYEWnfFRDNkh7Xbp1_bT1n9Qriudiv2CALldl_D2_u6oSXR05lN9XkUtCeIzj4oxrrScr-ZJSK86j8auuzqFC2Qc3eUEflNflfS6B2UbfuolSU7R2Xdsa-S3LLjF2B5go1d3Hnv1fdnk2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Qx-n0ji2aQ3Mq7XYuUqHl8TcSG310kJBnerTO1bFKYqetZJwZHID16fXLfgyKYRMKGutju3KF0NyRRxv-ExWJkwyqbl8T-4tiZ7HCtlrjISEHa_HLfwOq7GDqcFbVEYhuCbmrr2bXwO9obwNZW195XjbIQNZJ8GOcIy6pB9GwVV4Rp3ugCPnsnXjJ7k4c_qjErYIdDF5ewLjL38_b4OX1n0v5SMNGW4Nq7k6WYwntbE-vNu5b1dT0vrtCEU_KzqLNXfaOzOLC_wg0v-1TmHnoK0J7YgRhQEyvBaa7sKzZNmu0d7FALxrYn1xoPNOYL9z9XSgQE-qxZNe5QMyyz7-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Qx-n0ji2aQ3Mq7XYuUqHl8TcSG310kJBnerTO1bFKYqetZJwZHID16fXLfgyKYRMKGutju3KF0NyRRxv-ExWJkwyqbl8T-4tiZ7HCtlrjISEHa_HLfwOq7GDqcFbVEYhuCbmrr2bXwO9obwNZW195XjbIQNZJ8GOcIy6pB9GwVV4Rp3ugCPnsnXjJ7k4c_qjErYIdDF5ewLjL38_b4OX1n0v5SMNGW4Nq7k6WYwntbE-vNu5b1dT0vrtCEU_KzqLNXfaOzOLC_wg0v-1TmHnoK0J7YgRhQEyvBaa7sKzZNmu0d7FALxrYn1xoPNOYL9z9XSgQE-qxZNe5QMyyz7-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=QcQbNpOVbM4CgJI6m8X_79MgBXDeaMW5TyWLiyjwr8jHee6EhMfZ5pI0juPLmZqaGy6eWOxSJOIH07R6rqJ1v2chhJdeidGrwTLL55cOFCNGGHGFHNH0B3Ei1fRYYFmk22gZItc1ZpeA5q6OUIhh_erZ6YTKbtX9TlOolKbjqZMD8eIhOw1PAev5K2pB8Mw_Ft0ewhG-Kgh92VVJaOyqe_vKkRrLA1gvmvXYOMJHHjH684BH-aplggqlRvZMIgyssDErJ5Uxy6yDdUwwO4t4NWgjMr-od1j6eoEByPnBytzQzla3fy2mviwqQ-8K2N-wMJV6cVLQ-oHrVPuK1rmBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=QcQbNpOVbM4CgJI6m8X_79MgBXDeaMW5TyWLiyjwr8jHee6EhMfZ5pI0juPLmZqaGy6eWOxSJOIH07R6rqJ1v2chhJdeidGrwTLL55cOFCNGGHGFHNH0B3Ei1fRYYFmk22gZItc1ZpeA5q6OUIhh_erZ6YTKbtX9TlOolKbjqZMD8eIhOw1PAev5K2pB8Mw_Ft0ewhG-Kgh92VVJaOyqe_vKkRrLA1gvmvXYOMJHHjH684BH-aplggqlRvZMIgyssDErJ5Uxy6yDdUwwO4t4NWgjMr-od1j6eoEByPnBytzQzla3fy2mviwqQ-8K2N-wMJV6cVLQ-oHrVPuK1rmBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo_DE0Jn5fvAVSaBHbW7y-WRqAbtIMpW0ff4hglt5AH_XLuzA9QBoYACn_vXXr7kXv_hRliYJMOBV0RvzL9HhvbJUekUDMcvAaUd9RvUbz1j0bnsJsRgOGP-oYJtMIeZ1LLa_Z5PJSqzqyFX3CTT5t7KZS6UDWznQl9MlwIMPcn6aW9mWxhKrf8yUgJLjo1U418tfQga2ObSIZ8yecj3nUDLdVXKy5J-mMxYNDmy14-Qwqt5MRjsLyFVMuK91xZVswFfC7oB7nnDr0b3KzvqMlB0IJGtW9dO4HezoqFz8gg-d4lmD4aoqHXRVsMPlQq3eX9tGMOnhXvbUTO8G-AFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGmDbPPAASsg9DAdA1nDhi7fSra1ucz9S3TpkrMqrWJlwwaKTOFc92AQ3wyUxRdXVLHs7qCn6ihF8CBnwkO_n6XFg2XyfGvhPA5CQ1duvj2nPhCTDnebhS8ZDLaF9yhcNU9TqPPoYSeXpBdeyaaL1iRnfpiB_MG1QZ3XiBXKJwC_-GOnWxWMovAC16pLL6nyrSpXja9O-LFgIC3jET9PNRdVG_qp7fcs68PTRQ3vtWndWBkSvP3osM9CnIQwb75PuWIjSltvYQAUDhSpEWrlx_3IYmBRoj-kCPIzVgFsScpAbWR8z_h4Z_qjAbjGIajLBmNXapC6rlXJDt3_Ipb7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7xd63hM1wnSCSnNvzTxSB_-eQIO4voPOI3rzJYVXN07yIQCMR_F_LOVAKSPdyoJudr6pfEjUgSGKUdLgzLVMc-zyDrECgQ5zidDciHZv3IkFkBkLg8PSjjvk0yDt2md5gqnoNQkfOOod9FzhZQIRQYcE0JBhnUiL95Kop1a3lykCnrup3yCDpwFRNrrZm_KLXZsME_W1nnL4-QQXdFYBfAR_kQWCnaiCZWJbYqkvAkgy8ItrSADslM5LojlzRHmEoglKGZZ0N0TKatsoAP4YE__D0HeaUPWYcMg4c11dApHgEtwGAy2aqOCCVhdzCk7YTofNIwb4zQiXDUYeLp5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqV1g98amELgHIPlrhha6jWpGJSs3Q475IRxdkJVWvHh0tTF2GxyL7Dsq0wlR9pXBSIIGbYM9SPIWvS0hROWbEItOq10Sjh75gUn24aSE_tuk-8F6vv90w0D5l1TJt9vk4DDfWkBE5U3MPywa98LxPWVM5AWCYpUgZaNrfAKmX7hf4QUksHa6_x9yBBZpipUfq3mOKeReytzA7p85FWn25FFPnPCNjvbs8jSbeCSKHbZKiqVkwZlz_I7L9VuaQXSthYhhey_oX4UeOAGEKLtGkUyrv55s-GTUk8AgdPIiNB2xLkmHesb2_1aKu0vqf9KeD6IbPRB37it28Q5VJUHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQaPJ7OKLxcSlrSHamqmUo5aQh8fpxB1lGwSegqE7Q74mbe_ss3k3ttSDM6-GEL6sUqwON4AuhIg_R0tI4uPCHRIL9N3Tm4NYG6iK1lV2xbTUHWB4Y7qZaUx4qdTHz9Qe8YQIIS82O3B7cgtqJ_GmrnSAhLZBlTWGEQsGE226xaFrwd_c0O0NztZ6Xc55z7K5S_Azcjua_H5jrEnSdM5Jn-6rXUIHRlXnXJ9otfbSKJ8DbkmNMGVsZ0U4pPpM1jL6FaJ6-qCORSGk0Av9XANweFBrp3rdbptDRzypuBQMD33wSnfZoxowBltjp_20Ci5JFi-DZQ2Qm5WqVapDBDsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2KO60WOMPbWP3c3cPq2oO13gYyIhh1avVhKem8DQ3FuSk-0BRI1Sn6BGq6uWabk2q7Q0it2MNDDgE7MuY_vhjNOnkyX5SP9q-vEhErb_EsVgJUHTuuxLTXz3jkCeHSXVy3bh94lhYICS6bK7GOzoaden-HBsE8h_tiC6dFAsH0QGs7gBctoe0jS6a0FUXzz7tTACVEZwkWf6Z3FaxmwX3XUxgTWsGJq2XXzwNUVD7Hico5I-_Rn-n5_-3srwIO56Iubc2MEXkvdmJgO0KIEcDxV6WrwQlNk5Kp7Uevi8sIZUyQJWTZKA7LQ-fbR6PBoHh6Z5ehcU7MZHVl6BSjX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNMLvfVxBTVf5cPbpOsm2mHwGFNDLTx6ciXRbBIxMLGY-JGNbfTTTV36Wd6L9uQZ1lMyEl78uAWmrRBcea1qgIBajLG9ZWiGswlV52L2kLJtvB0OpDCeJeCgB9dPcynxAg2WAZxquJ-AIruNHuU4vZnOJVNxXl90VlySwTJd1o6_C9MXNrPflOdUmpsQ-Ps_1RrToI3TkQ24ZZyvMy_6oUtyuktZybMkSiRHjPeNsrZ53Ciqhkx7olrjafEfwA517ida5C6c5xUfkQ2B2Ua1n28D44CRmya8sC_DNYciffhFi4LYNmCA30XMJSYk-u4U4voftaoVmGlK5p8gZ5iZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=RTqSGzNtre5SYzI0YwfR8R99yICy26EG_ep88Psv3uzxXiRzPgQ4eK2SuEjZafvP4VpogDgDvj7S6fFFQaiJRH478AtQ6PjtAjJjFDrfvpOSjgwUcZ3pU7kdTHBketc2GWPUWSk_vx5f75eEFj-nmT_9K8Moxi5-Ah8cHrAnCFkW-ML_DDXwaQmZMlKEfcOSGxsKg9TPmNgO_oziApYtkaQ2lZEWdq7spmpJcWZ32lLzjrus0RgZd6LSyNxOTnQG0vZvsERERY01heG1pvXOZ7U9jIgYlC4vYOtaBEC1CnRW0J31hkU8JekcQd8eqWnzGHETENC7l2PxQaA8DTQePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=RTqSGzNtre5SYzI0YwfR8R99yICy26EG_ep88Psv3uzxXiRzPgQ4eK2SuEjZafvP4VpogDgDvj7S6fFFQaiJRH478AtQ6PjtAjJjFDrfvpOSjgwUcZ3pU7kdTHBketc2GWPUWSk_vx5f75eEFj-nmT_9K8Moxi5-Ah8cHrAnCFkW-ML_DDXwaQmZMlKEfcOSGxsKg9TPmNgO_oziApYtkaQ2lZEWdq7spmpJcWZ32lLzjrus0RgZd6LSyNxOTnQG0vZvsERERY01heG1pvXOZ7U9jIgYlC4vYOtaBEC1CnRW0J31hkU8JekcQd8eqWnzGHETENC7l2PxQaA8DTQePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObwdoX5I9VW0lKjHXC0ray83ZHHtpqGvgxyYuIOBL3upoNWGvf5z6u8eU1lHTg48V-AqILiIyd-V3PqmujMSih4DyDUwm1DtbO9yy3cKMtV5RU9OIZKfqyHWglp2G9G3V4Nlq7-Cs1Dd7VmCHonNXkkUolzlV2KlY2kKFx7x_aF5KIFTX9y3_FGK_oK3Lz1YkVmNLAIIdWj6p4E3OvI8mCVtMv2WXjcknoY_zbygszyiTfM6PhkeWM_rPHxk9ZdZJLFuVwlSlLredSoWI59Oow7GhOdsVQZipsf9xpq55Yi4OYSRDmr0h7B1PtOWJf_NFPV5VnZfql9JxLFJipmf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsLB-EjFjh56iHQrKwMiqB10Ae3UbgkWCZedbNkGA0rFcfJVVRVk_ulHARoH1tAeGj4pbdPCbStNQHRdMfaV6FL9jIusRaz4h5K6PgrMgtMhI5ZyjizY2N7uyi0zmF9YsJfHN2vOq8EO7GQoEmEqjAaSfyJYzerMm1wt56Kye6rv7ELkNklIpw9IPsgj8iySas1XK3heYcfDoXH67yvNY1u6raN707fGSC42QLAJdz37JH6aDD2bjlsjj3jCggNtVn_4x6ey1OP5oa1fR3qS4SibKVffhR9Z_4piuPu6P3xtiSsW66FZnU2KIoOApTiVikUzJ1l8Qwl5DhiwLpP0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgJe4xNDssNm_91PlJT8vt8DlqgPCbJO-TnoFQIYgSiqS-GNk-14vxlFzeACwhWBwUVIoazNxnjDOy5zZ4BTiN2uCzsud-9VMYLMkWXFrv5x20xoMPgrhkHVUQbg355YGpJYYmPXETXxxh0IQqWBOiKhrTCUY6iL7gGtOGhxZUsVkgW3hPYZDKOthsHM_t49Nci3-SFm-YnqR8h2v0lw5RXm4IX6APt7bi1QbVFtOefHViCvAPCTUDfVKG3S41PSUrz84ho_IKwbwqlvPdWn4hnvAFNPlsVlPzWtJkM9rJE8L9tDVAxX_VpwdtOUhrPiTTKWploNOGbQBP0ZSfZ0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAyO005-u-GjvFJiNo9_24P_49teSF4xQGag4XYwxm763bpLW8Qh9OBmXjJOI1vhg8fL0yflYfSS7Famma3mb-KNutoNGZkdb3kVAWxZd2PHj81qgoYvWMH_ghJ_kD5ovRRwey5jhGrLniVlHqwamUWZqNLvGMyPW43NZaQw9XvVNv3RWh_y-3Atp-usF2Tl4LhPUT711vtlaxgJKxcFBYMbs43f61_xsZXXQZ7UehqeAMkKfluKqWJKeiNib0MdZyAyoyImddB8EJyXGZe6ZD32USPe3Il6ORFg4i1-XufAnNec3MtXSDX9QaSjzrVbLlq96NLbdMmRs0BPKtubzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inxZYtAFcOmYFF7-Oz3iATdemifeBFYR8xD6Bf1mTpRM8OgyULqiSyb29whs7Ts_wCYzTWKlyuXogwflQMk8mJOZp0X1z68p8QGdlPCFYNlS3PTjMlzxpqUaar437lvmWt6DURMo6XiMfC80gS7vUi9eHA9BBAg2k00dfv3LFN0c2GTTzLKUSjWFo-AB9OvX-t-EcQ6CLe0-RZBXTULFqXhbzBssiu0C6GrH2j5nEcSBF3547qoRkfICSc3pg_JSm4r-DauybPlcVukGmN4LNuhrNOQMDC0ggFknbXqmDsjudXcZlbwcCMv7uTTHzK-iQrLpgG-ffIi84jNpozkFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noOrJuxqwNfCvHva9YszuUhN7oKUsrhYVp2AhMihZ2ygmYiVI12-AR9s-tOrVfMy-PpAb-k-w3Ske8CjbuJPAtU6OfAH04xwMrD6yvySMAwy2S_QRRdSI29yGbIyUb-_oHNgGMrDE5Wg-4d0u4tfpxvs1B_8zBw9LOw9CuAHGiTDcfgJeW1czagpAMBthCL-Er2ubtW-QlHHITqWy5BxFo68HSzPONKns8gGW2nQnCLA01YbGwfYqU_RB6EyTrrNWFXG_VOMZOUqnHZdQ35Fe8i7q9oewfXtEqim7jyck9CFC3i3ZWOzIR1YR7GbLuaWQToyTEIE0jxsOUDDxstgCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KunQKFuCQZw8Cuyf_baJJ6oOJcGtS7VdwZmhQeSMuxtRPq8btSwkFNBaq-XK2LhHfR-NRflIVc1PDbq9O2C8KSsivxAf8TrPMWVH9auVxhJy9vxxu9vA_SijAy8gx6F4-KgaEtwR1Wb_cB09DxbsFx4yFp_cpcphph8bkiKZ-LtC3CPaOZr4z5g4JD5jyEeuU8b5H4B5xc3wqyNK_4xDoKDbI1MMZXz6WmcQg1Zjk4hU8RTYCDFJsdw_cnuVlGrl-hTUi1vRGaJSXvbfqWO-KA68hSkFXZyj_2n1MByqTgKoYUgTUuqoaqI52F9GnKUHWPbmnow1UxCkYJZS0Q62og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=WGfcPo-6_3S5iYV7oxYCyddoXucZ9d2rSO9sBI2tJGE8Ngx24Dt0n53hloYtq6NUsxZoBBOuvLL-TcwbRDN1aDe1uZp0OorANlwXqHIOEmmU35nns0f2JtLd3eALbY0iYadkHryxQmnig-1u11bfDsiotqlcWh4QnvBT2WFhnAb5H2IjaGxjvtW-1apS8Ch-nh6Fn0qK8U0JN7pBNWCan-WxwJbToGgxHLJ9WWMrxLmEuyXXz1Fxh1qzFEtJw512V3T8tXPQca5_lxm9rL4iQrxQpZP7xhqmxjuGwpIvPAUO3srtnLotCp8j3crXzAhJhARv44PwV4LkCrgXh9NWBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=WGfcPo-6_3S5iYV7oxYCyddoXucZ9d2rSO9sBI2tJGE8Ngx24Dt0n53hloYtq6NUsxZoBBOuvLL-TcwbRDN1aDe1uZp0OorANlwXqHIOEmmU35nns0f2JtLd3eALbY0iYadkHryxQmnig-1u11bfDsiotqlcWh4QnvBT2WFhnAb5H2IjaGxjvtW-1apS8Ch-nh6Fn0qK8U0JN7pBNWCan-WxwJbToGgxHLJ9WWMrxLmEuyXXz1Fxh1qzFEtJw512V3T8tXPQca5_lxm9rL4iQrxQpZP7xhqmxjuGwpIvPAUO3srtnLotCp8j3crXzAhJhARv44PwV4LkCrgXh9NWBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXQTC6GDNPQldG0PLmX1OhLvtO4eLWTKSYYKJt2XnWPDN0EJ9z9WJ4u2YDnepIMI_bSDr2b1n4ZlREIdUXvPTvkW277oVoZLKQXrxBtuipEo0FGu7VQEHcFqybrG8930IHBql4f8QsIzQ_-7gJX7yMNK2IL0xQnBBV1yL4iL2SJBRSUY3iHfilEeqH3lgphRAcjtawa2i6A5ApXld_K35z4JjGowCtThat4Ekl65of5HJNnuvks2qG9cRastziez-53OxVPRkv0rFxBLyucPQsdJqgvfYI0airyZ5MreUMdVYZ8Yvx3g04v9R67IrxOqQhN57yaPgubOwZK86XPSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBK8D4-dfBFP7YbZGzzZtGuUas8INmUJ8IDfdgGIJAExOFR99xtlzgcmfBBwv3NBuXpr0BithFV8NhBWZglPPR40QIMchHYU60UgTGqIEuxaXQZuYoY0TAKVWpPShpRI7-AQtI4mlMZGyKzVVTeUDMe00QCkUTxYdQMQLtK_CZeRZGlyPnaVzrm-rZlBKSn2AoLd91yTFSHclGL7p5F_aFsqy9ps1AWVw1-A0MDCfD_rYNNpxWnKqNsPXfRKBIq2yk-vMRtyX3Nv47_EuIIOm6KTzShuefQRjQ_j8QdlEb_6M5L4Z3YgCY2gTjWypVMnd_UIvoPF2Z1oy1UZLB7Y1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8GJKKhdRbtQPTdl5c0X42JNe4AvR3uHlJJjN_8nvq4pnF4vcPwo9qk3fWt9z4leASPKjuTQ8RmE-_dFwJEXGP9xEy11KKBM4rk_c2H6UQDguP6_wpUJdu29ZqfUzcidsHE3FRh5PqMpdlcSjubOp7dKO4iy0QaJnB2dp37XZtsYiavQ9W_zcCovgAd0AgmoaRn5Gxaz5SseY31fBdEPnkrhkkg7Kx5pYKhsZUIp2fxoBKQpEC4Ac9xYqULIF8z72nfjPRETaBiZv1cHv6g0MhzJweiQglSyLIFsO8ZDlN3RK4rim4TrlLOTVMJAcOEIp7L9GKnkmB-vRv1VH0RPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_cy258_htRc7Ut_Ah0KBM0q0Zrb5w8hEEk2RPjjs4yEJmM03cYOrciryDEp9EVmZ0r-ii6x3zH8nUQF2g7FtRqe1SCqFbL4JVDez96P7LU_W8HpVrhPAjpTJuqTChfHtV_tG-b3Eug8W2dQhifN2-wePdDCjBcgOst-AuuGu7-OZVMVtN1lrrpkSS79_y5JlE7n5UMag2acvdtjS186lsT0ZkOX6u-7M_vWWYgUCHvVovevbet284DiZusNDoIGDUYHGYjmR_KsDTxbfCwZ6385c2B4nBEHbjlPXtwn-knCpQM_sUK1BUiKLNHZFj08b2yaeaeiozyJAbhnfz_fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbKq5RlUqrF6mguX_ETmxKUPF32Xd1u76bbWpazrQk4ZCY1IT160Q3jp978IYA3R5MoVKhsGMYsPT9RArRLkQ0pa1q_tnudBEpZb1_OYcStY3wPh9mzcl0wgt1lmqLG90kDkuruOlA-JqL8q2Sc6aOg69ZtHFq8wN98GKh6fIfIeX8hZDy_a-5oZFxHvCtLP1Aarlltuv3bVfCCcOCIDwFnbJ8vyl6OcAuEUGDEctKgEH1No_kBu4eRo28q-S9JYTwzCwquUXBPdQvvzhI7p6fjNqikE-fqZU-yRhxrMqeXELZxnjOqvy77c9_Dk9l0xIOTBCMQcgOcuPINpfPeECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvYeOVq3aropbmB-whV-8YMzdS_QaLXzMoefoyqOQSZXNEB2ZnYmJrsyiON63qi7itFd-igI7m5e3qYCA8JaGP8rq1oT5t6D5l-GqxzNVN6szgw_PRUnwLrJfnxsBS7loY6O_wFaFHKXDyb9vELdOOIxrUrj7oK7MD0FdSKAOlj5UEffRqBATszjaGpXYG5kLKb8LPlvFdrJ352OeadtjAkycGUIf1JufzS0q2X92H9h7JBD9-ZGLbPydjb3-KwWujaL_YBMjpPzcej06Sc2TdII_oLcWMGoq62P7vpSIZ_wggeGJ8dn1bNl95jwOxgOVzrXpXxSI_zmkhyuwfcQ9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=UznsW3xoocWBmoJmA4vo3aDG-mF7pMlXvnG_yYq4LCRP05YH2Fhi_QCDKhWHQiAN7kP_K9PD6Z33sS6quxhW1dmojfyiys2EF61l_8rxjBWHU4hQWEhVcCXYvsz5bNTVckF_dJAPYlOHsyW2ME09uPxt5spnzREoMEUr1hNRtlJwCL45EVM_YLd-y0SZF6WKYBkOtlzRA-rw5cvkLVofIjmhqPKj-eyFpdwV0knKLex2DXuVsER0nRZpy1X8IEoSgmAoFiPvKYcJhgTnpoo7epEeR6WsZW9rS6j5_NXU1-wz0n6dlP_HDX__ttRM7qKqovKnNjwlk3rLJJh54bz3n03b5BwIeYTn-Rlirvf5GwLlLtjVnO-9e_E2A65Pw5MRj9vK_fTHsugXYW3CrHCB3EypaJZYr0s3PyOTEtOKkgrAI9IiPnpUdKm2L6jVTrG7i6Xd6OiYrzD1ew3Pf4CHD3GzOe4m-xDiC1VYHw23enu_IoNAHFJ5jD8EWySGzQ-PJ-9dGwiOFMuIEP_Jd634ObcPlv6RHL1cUOAPlHSmKj5qeboRqfwRzPpr6zbDyMM0pWQv74AWduuXHK5uFzH7tb8xuQuksYRZXxNWkJjoFxD2yvPr6jC2lX3vl4f2-ZlSZI6qarOxTdFpKrIZdqG0TReSMue6myTMq8nKXJXRNbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=UznsW3xoocWBmoJmA4vo3aDG-mF7pMlXvnG_yYq4LCRP05YH2Fhi_QCDKhWHQiAN7kP_K9PD6Z33sS6quxhW1dmojfyiys2EF61l_8rxjBWHU4hQWEhVcCXYvsz5bNTVckF_dJAPYlOHsyW2ME09uPxt5spnzREoMEUr1hNRtlJwCL45EVM_YLd-y0SZF6WKYBkOtlzRA-rw5cvkLVofIjmhqPKj-eyFpdwV0knKLex2DXuVsER0nRZpy1X8IEoSgmAoFiPvKYcJhgTnpoo7epEeR6WsZW9rS6j5_NXU1-wz0n6dlP_HDX__ttRM7qKqovKnNjwlk3rLJJh54bz3n03b5BwIeYTn-Rlirvf5GwLlLtjVnO-9e_E2A65Pw5MRj9vK_fTHsugXYW3CrHCB3EypaJZYr0s3PyOTEtOKkgrAI9IiPnpUdKm2L6jVTrG7i6Xd6OiYrzD1ew3Pf4CHD3GzOe4m-xDiC1VYHw23enu_IoNAHFJ5jD8EWySGzQ-PJ-9dGwiOFMuIEP_Jd634ObcPlv6RHL1cUOAPlHSmKj5qeboRqfwRzPpr6zbDyMM0pWQv74AWduuXHK5uFzH7tb8xuQuksYRZXxNWkJjoFxD2yvPr6jC2lX3vl4f2-ZlSZI6qarOxTdFpKrIZdqG0TReSMue6myTMq8nKXJXRNbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=R5_tvjD60xxaFY3Fkml2rqvQncUQ1INmHfGEXX2CyCFW9Suq_sdM07Ujmbl9NJqqlmqNdQn3RVKdHjEgS0vJi5kutizPFJW3sPBTg0sAn2kWZb0pkjx2zmwmMQ0_WATajj5IfADC3sPyECSrioCVLFEoLzZl_kxHTrkU3uD1JQgKuqmzStSp4inBCac2JzO3q22fmbyMx4dzaDtFtZNy_dRZtKILNZr8c3uYhaGKsf7OmNhMgBdgVKgWATU0kaf1zZA40TlywoAsPHneSWcp7cW6jKKQ_-b2jfzNMOA_ek2kukQqK9lui0JMfjzi-jS-ft-B9MS6MSUELBGOWt9MNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=R5_tvjD60xxaFY3Fkml2rqvQncUQ1INmHfGEXX2CyCFW9Suq_sdM07Ujmbl9NJqqlmqNdQn3RVKdHjEgS0vJi5kutizPFJW3sPBTg0sAn2kWZb0pkjx2zmwmMQ0_WATajj5IfADC3sPyECSrioCVLFEoLzZl_kxHTrkU3uD1JQgKuqmzStSp4inBCac2JzO3q22fmbyMx4dzaDtFtZNy_dRZtKILNZr8c3uYhaGKsf7OmNhMgBdgVKgWATU0kaf1zZA40TlywoAsPHneSWcp7cW6jKKQ_-b2jfzNMOA_ek2kukQqK9lui0JMfjzi-jS-ft-B9MS6MSUELBGOWt9MNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHkXPX_O55Ml4gQEhvkf8-Z-lEEhTtdvKtyS8UebQnzbECVDUI-Gl_5bAldQ-rj0YcFTc0VP6Onady-nD4u0cVWTCWKjapmIJuI8DwFPIByAOfVHETRWH5o7l91yuxUMDILorNb-Wy5k_QP9L5uFO5dlniUMMNz9h8IP0jG6Bvz6EpowTZ-oVma3zrcnBtpmf8dCCiLYafi2UcVLnaTRBAdRM3lnODgVKnJutVldD2ILPyl0K1FYrC0i8GxY-RHBg0RgXP-0lGaQWWXyJKLwjBb2qZtbuBdMcNE7t0exA2DrE4WP7sKRW-e47cM45sM-gmRGSGRbQhEZOCCzmr3CmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=H6uqE4Csm_AkyamtNHQ5hbLrItWA44bJavf5t-UkOktdQ0HilRj-CEMip-69HvfSFF6VbGhYqP1OEJ5MUfGOftg3c9CMPDVaZ6UzR9W0jZ6eyUrNDDC7fuZAKYfFLe07gDxH1m0OUWzght1P-nGX8wXnAEC2aNjorcJj7DjPuOFBDp7GJ78CZR1_1Xy_S_RjIZdCC2-BX2WYrHfXkYkILujvxEFBTKit6evxqYT9IFWG3PUc4ZXjHrSfeoUsUcQK61VXd1eaKcW943iesDoto4XdCY5QgxKZ_IDIzKqc27lyA_o5-dCXG2jw8b8TNwlNEiQtgKIm3QHs_BYoDiXqnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=H6uqE4Csm_AkyamtNHQ5hbLrItWA44bJavf5t-UkOktdQ0HilRj-CEMip-69HvfSFF6VbGhYqP1OEJ5MUfGOftg3c9CMPDVaZ6UzR9W0jZ6eyUrNDDC7fuZAKYfFLe07gDxH1m0OUWzght1P-nGX8wXnAEC2aNjorcJj7DjPuOFBDp7GJ78CZR1_1Xy_S_RjIZdCC2-BX2WYrHfXkYkILujvxEFBTKit6evxqYT9IFWG3PUc4ZXjHrSfeoUsUcQK61VXd1eaKcW943iesDoto4XdCY5QgxKZ_IDIzKqc27lyA_o5-dCXG2jw8b8TNwlNEiQtgKIm3QHs_BYoDiXqnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=UFuRGUL1jKeX1FSzfW_KCjOMOg4t06tucpfEq4zlsajRsNdAbjIx86NqcxikOXShL0tr3JOVielCHAbr0bZuVh6G4hDY-RmjQ9bYQt5Yft8CqgzuqSZvc4ylsrZ5EaijrO2Ywu6_PaCdhIWnGRY11_SRl4YphNjSJI4LHdEIlUX_G5NaQMMtEuDyOJNDGmLk7ZwZVmd_vaeHVXeO7xzLcS2Ao51tXc-6J5stpV7XdCag35uPHP7XOCdesArphNxMCiek7BKHlhxWaZK7D4yx44lx-wVgT9dZrsGhY-HF-Fnu-zR-3Fxf68DIip0LNJ7UADtAgtHosq60QYUVyUDyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=UFuRGUL1jKeX1FSzfW_KCjOMOg4t06tucpfEq4zlsajRsNdAbjIx86NqcxikOXShL0tr3JOVielCHAbr0bZuVh6G4hDY-RmjQ9bYQt5Yft8CqgzuqSZvc4ylsrZ5EaijrO2Ywu6_PaCdhIWnGRY11_SRl4YphNjSJI4LHdEIlUX_G5NaQMMtEuDyOJNDGmLk7ZwZVmd_vaeHVXeO7xzLcS2Ao51tXc-6J5stpV7XdCag35uPHP7XOCdesArphNxMCiek7BKHlhxWaZK7D4yx44lx-wVgT9dZrsGhY-HF-Fnu-zR-3Fxf68DIip0LNJ7UADtAgtHosq60QYUVyUDyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4POYCcYbEnXfPB0lwMkyMKafYF7TeiZs_NfwawzmAKONfNFfReqV91BXXo2LG4DVsz6lCa0149ywta52LfO_4hsTAr5YbgXoDeEHaman0LEy2kEamM88BjK0ZUyEZU3o6Sx3Hmusw-kSkiWLdn3CqR6q8aaThZLpySln5gWi5exXxK_738v4MkkrNLL_osCKQ5m3fH2vT8vlmJMpYUpBsAdFV9V-Uj4haYjov75UoBrV_11uj6ia_5GkTPbnTj2RlZ6jrPqy1XDcmL4qF33apG0bZLa-v3cTngYlhz-cHu9nFvkcY8ai8-xMsiJRZboe4N_103wha_J1_GXWL_giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNV0ed4NdyaOriLWc91PuGQ9ZHmXWzlN8BIEc_V27SSG2wUXndcdblMOWie-bzTTtH8jAb7SEk35GJ5UELIUVgJGgyERubhp_xxnNkg1RqrfmZtbNa1NSbdNubk5z83-Fto5DSEPddUUDSpikLnbI5VAmpNaYAvBy6eyLpGSGIP9GpMgsMEeM68hIDTlzuB4QejsZx22GQxljToL6ff1VKgutqwnizbZcXgiXRZv4XkU5gfEVoyzA_p89SHAAy3_M52z603WfXy0q6GM9k3BKVLnSgpge5MmMNakP_zPFQJgCrKB8KkwvNen8AHIxYQUo-vIstxu_VVZ50iK340ZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlSCCE4-ybCJp5t_i1esz1V0kyF0bpq51BkLhVHDaJF16pKiHh-iN2XGBXNuWLorTd2Ndd1FA9pfHMAokgeCWNMStChC4bEjfRiyts93I5CdxcJXo2GGTTskX3wLQUGHcKceb0rO370UtRlzEgYWbn75ttpUx31XnI2X2FxMd-PIHP_1aoP8Xrx70FexomKQ_RQJrP2VJzaqHTnOoR9sg6SXOcnwXzZHWh0opbHeoKpg0o1JMiRDCAfPNsf-fdenwc2M7sZWIVSnrVKnn1YSXxRm-YHfGNB42ix_lpF5wfEURP6ScDVh-2GJ6e52u1b7VWlHw1FWpOWhA127cCkfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=oyOL3ghKqUg9Pb7JqODiVafKdOLgG8MsXXxvosU0Ae2libvhGGZ-Axt3mgW4R-mbmO5tkDUVtRKj2tgX_J1WC8Z0mihgaxDP3YS5-IJB2Ncmee863Ks7bdlW-4wis8yN_itBY9m1wiNguI4rKrrBk_V08eBo1VL5O8-WbAmoKh2LcFdJs6fCdvXojChaQi02-RarBbEm_VPViIgR_Mj7dbJUDpOOW2gBBh5G7yJnVfvpB5v5pGJaZKHmEMup54AfFFVqVPKx_evEI1NtQWcRt-lN7EOY9Lsk0oCsliTw0GwWPequVoLELAF8hFDd4tvvsD0G5LM5eHsaIB0W6Cc8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=oyOL3ghKqUg9Pb7JqODiVafKdOLgG8MsXXxvosU0Ae2libvhGGZ-Axt3mgW4R-mbmO5tkDUVtRKj2tgX_J1WC8Z0mihgaxDP3YS5-IJB2Ncmee863Ks7bdlW-4wis8yN_itBY9m1wiNguI4rKrrBk_V08eBo1VL5O8-WbAmoKh2LcFdJs6fCdvXojChaQi02-RarBbEm_VPViIgR_Mj7dbJUDpOOW2gBBh5G7yJnVfvpB5v5pGJaZKHmEMup54AfFFVqVPKx_evEI1NtQWcRt-lN7EOY9Lsk0oCsliTw0GwWPequVoLELAF8hFDd4tvvsD0G5LM5eHsaIB0W6Cc8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=AWG2L_y84H07IHT5MS6Cwvdd4X09REhbB7XxIX9qo4T_VFmUpixEdUfVcMRjEbpHcG96HWm77lu1RadR7Swm8iJSDqFpUvEI-jDSsjPOP4yTF6qq0xRwxJ7Koe0gYt4pUefHYjWTA8rybNvSvImwG4hR8LO-5vLCsHvIqutSqtnACUvZOHUEOT9hpH0PmnxpnJIGTIwGsqi7u3c2pqCDc_N-Yl1p-0UL3nxMc_cPXjmtXAOVMN_N-0dnzMYuhcbw0k1mJYOD1tZWD299Eu4BiUuzzD5EFE0R0K23Db-ZjefOixKcu9K4RYE0HoKBAvFHilSOMWTgRtZWNGrQzmdqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=AWG2L_y84H07IHT5MS6Cwvdd4X09REhbB7XxIX9qo4T_VFmUpixEdUfVcMRjEbpHcG96HWm77lu1RadR7Swm8iJSDqFpUvEI-jDSsjPOP4yTF6qq0xRwxJ7Koe0gYt4pUefHYjWTA8rybNvSvImwG4hR8LO-5vLCsHvIqutSqtnACUvZOHUEOT9hpH0PmnxpnJIGTIwGsqi7u3c2pqCDc_N-Yl1p-0UL3nxMc_cPXjmtXAOVMN_N-0dnzMYuhcbw0k1mJYOD1tZWD299Eu4BiUuzzD5EFE0R0K23Db-ZjefOixKcu9K4RYE0HoKBAvFHilSOMWTgRtZWNGrQzmdqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBUElmosMPxS-hShl5o7WozlNkTQKqYzCSaVoaGJkm9KMVEjx0MRa0GIuVgELaZngu3h-MWPxTv4iCCdA_8abTIbBRqCVlGrk4iVXlt2Xm_Z5U9oZODFG0iLW8Gc7EHqUaFBUvdUaQgiT4w-EUeawXTjvTmu7nFVIwGvpCLWDWCKfvYk0APKH2giWQ6G8ojMd1nxQpFgNVwM2OzGpaP3TWUAnpQYh7N-Arz64ni6L2HCnUB0PFJP9X8K7xfRMEB4tgqOMvjuPNzDqD8__BrP-GBW8FNdEjmE91HNJ3RVqFlNSRttuD_bz22J5wnO_79n89RwwPlSAZIf5A8YKPCBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/k-P3zXKSBrz3fvYUYiwk41sscodIkxh6enp20PhOCODZZ0QQ87Qu2ASJT_jYET1Gc9jMBsxjSfoe1U-pnRcgVLwWaYTM_bGxMKya3HGuP1lNjq2PNbL-JnQ6xtIx-rLWSGqUrUj64QgRiHOkWrxV8Kbsg1c3Tr4VgJleQzxzava8NWTvW09Pr_ageMvT3x6jKwSyTuLnZYnT5uOto4_4YjGk1hvsjRev4NGhI1ghySPpOq3ch-BZsqWsRIDdxjP6djzFu0SlLE8dsQ51MxtZmC8YuK1j8epWYt2-n1Px-rTmeb073q7uKhSChb5t05jLDCqnvNeJHvsEE8_gr-4UPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILwcAEZHPZEziBBCY6HIBlZ4054LnAZDGMVroliZ5ltLl-tf2zMK1d7Qk7T3CHZJPmtjkzjDz7BoOtMzPRwEHP_TBoNMpyMHUyARg87EFc8YaGM_uZ-_8sIkoFAwwIqTJwlAcMFFDnzkAKpyScMB22wDG-DSQdH1cvI2yk9KoSPTXnHNoTo19VV9o5j8a9xWzSgZWFARqXtY9GBfNWdPdAvyL3R_cBKQv1UsUIIDRABMsM3zsvq_kSL0DPdu5f-F2q_EtkXetpSrimCRzLMVcu0bmr1A7vhS7gsDqDd3lxTHNsnl8O9GK4-o_RxpFJMHbqRmQMM70f2oF0dDdTo6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 80 · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LY_YRI3QFt1vRNXs-U11LVtirv_L1zps99_JnRVyZJeEiz5PhwkEvwunUt4_ewMcc1WozXTcLk5Iw1ZaqVJr6bMiEd8Dnu66GAtZV03D8ZxdArvlW2b26jHQf-i8YTWT90fBUHs4yYf6qjxHHQiCkDz9RapTSk-rcWCjnHAzK57BgpQ1oZxKv_rfz-uNbEjR0nBeJyfIXkv1HEzfLJElwFlL4Y1GgO_hPlrOGMEbw_E7chNlCXBPKzJSkW6YnXfOPswInPNg8owc9cMJ1IxB_dYWqd2fYcGqCFff5lSMGrz9L4ry2vRE0XBzuq3NXmxMDBdsIrBgLJ_wqHQgKqXjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsgW4-aQ79e6_3fIrL6dRaaWSRES_mVJhcYLPHyHclDnQQXx6VJYf8Z3jRKZlFgmeAg36_-7Ah7gZdS16guOSd0RS6dHKBf9i7Z99Uod0hBYDRVyRcL5rJ18Wj4vsf-IhxHBei1iYv5DtXSBegEvJ7y34aAwHo2Urr--Osa_tY6s5EagAJLK69jU99eeTlgO5uW4SFpzUvdkd0L38D7Tdkfa8WZffaGZLmhqV0agunR5Zy9tgQNZVr9_Qqv53_egTorQxeb_9lRYyH9-QgGh-XzXjRmQbpZYu2IS4buxxSRJu0IoBVOemfHbbPaJ0UxszDlbhAFzv0RGgjCUJyLOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBmpqXnzzM7iuJnMxrf3R9R_L0VDVhVdXoM5W9JK8oxjCKTx4ByIqpDAbrwJS8XwnkFEOVnLFtQqgOFQLeH_FPqgliSIa7DVNAQoBSr8pGRxeyGd3WyzQxEv6RyZONEauC1ks0Ax-ciu4BCjtvSfWHR_IaFOL8qyPEMMma991PxQjBLdSWoh-kRaowFsfBazaPG6xZfKZpIt4sfxwnsCispqnOJofk7y6jrT9G53IIzSUkVCNOTUnlrRZa4P2TrDOtrcV44FOO-gsNvoNfOk3S1BPt7qW48f_wbJI633Gcj2CvkobBp777x4XvyWStM5qSH7rodFJGgKJqa6bfEenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJrE-O5WiVHF5wYfY08j7Y5AW51QUE0OmkAa3T2sZ9hX-vZXh1u-T41k_IshFDWnlvwTlSnKYq4al79LRl3DQQA0-ACz43HUD-73QsTQ0rdSb_X2DHHmZWHxhjrJ7isGOzW-Sm2wRAPtcEAwkYw0445N0FKBrViAyT7xSZfx0hqNm3WwdQfuPK1hDVcKUUH_1r4sD-I7u6wg9SwCwe1ef73bNnkLTbHxayPYteb0xqB7sZJhuq84rKJqWzMYLrPM8bE2PIKjBBuxo-JvUDBeHQwB4PEgrnMIff6s27YYH1UVyAFZ6uqIcSV_LgZ9YSTKlRWD27rOvSGq1llWoTa_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao27NdUXi1Tp-e-q8xXPxZ5vSZ4cHtTay_TxLDvEn_AZ5Fg5kvjGsK22E4VgaB2qefRq0DJ7ifXf-HLw3VFWkiW4SZRxUCulE4sODHm6vDmVuPx0GL2g3styB2A-48GRB5ugz4PX1mlKYnLnnmg1cy76_rAOi-f49tOhv5s7kXQj7FKFkXuACazwm7HRn2GZSOOF3ANXZramMq4gFSePTwC5mLxr1JeGlbQTH-IIGqyENN3ouqkk7hdOV7sObvSGEw_ZYXxl2YxGUgfiv7Jp92_H7XpBHsSuNUWMiBJtRlvw3wjM0l_K_UcDHe8YId75GsqBQTv6qYQTBZeGgVWuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAz3x6KvITayRPAOwwzEZdS5RKZ9muKNRP4za7PNYid9ZpEUwKoAq0VZNNru-oxBCmpM4RKiBHJyWFazqQqmdIm09sWx0bQSTUqXPgnfaEh7I5NNsOgfYwHnYQUZ7I-X8MvKXQt-pYexzbVVsajNNw4AzJtr38FL2qZuK-Befw03ERP0o6Zhb_nerO8PY5rCt2y3xbC9ceb4cQeOHRlGSF93w460iB86ybhWeLFvb1pnn2IMyhADnX_WDty3XnhBfsGVOKGI3dQHGfxBT6RF8vPvp_UgQ2-_fTPXLNNh65K43sL0ft99RFN_66yKGW_Vo2Kjwh3LXZdBw5K9wATRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZvFpkxLHs8g4rNTIFEGd9TwoEvyf2cdXjyE7THBpzTHqlPYaH70hPRuv8ti1LNCejCOW3-__g1YsjrSWluzc_RLJtXUNB2zLQG9arkLryMNxEV3AUTbbi99Qr_Ru6X-CaEX2FOTqA7Scob7TGsNnRz3VZj5apy7CLJau_ZMJf-V9VG9mPOfqP1Yeg23w5nVDy_KepN1g-KocKZg4nYVjFEZyERqwMBqAh8BcmcjpCytEagb4S5GO4TCkRTV7_rMHBwJgwfspB-ZeP2VKJXYtKIUGK-pm1GScv3LCaf-RmimI2d0mcSKQILS4l7wI4CW9GLDd6lwgI3YIX6NT_i6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG5c1XD2II0_yFkxH1hJwJnoV2dqWKZ-5n292Zu-aYOIkNOj61KvnCJ2hawV18xVP-BkRaQNv9Qlmt33y2A5MNktrrrMIj2xEo3mTINTPy9foMj4loQr2iuvi5Dl7IJ0kOFMTAQnHpfMcqQbR3iaadMxLh6jhKA9mcth3a9D9ZPIVqqjqFRDjQebdcoZMS2UMU8WGjnWchlJHJI__fy10RSdNhSt2K8t8JsJ4PiwLHqycvOA8lDbJpk0756QTgHBzSR_sjGHXccC8ep-bLhH1hXcoB0UOAjtDn6nWx-siJDWE7AE_BhyXFtgbdSF2t7fFynOmmzUD7eF0PPg6FjAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtLG1zr1fYzN-AVUwFg2G7FahNAOB6_OyFjo2D3KtE_A21NBqfy7TsXAVyG3ybsUzfDMsco0ljK3N8drKz06YDuMW76EOqk5mgyxpAPhw_g4Z3RIivDKNFkYMcoH9C_4Rhn53bs9GYB0IkR5O6qaA5ReEQQgKgrPyYGAURwcuXb-AVS1KwXG1ZvUip21cq-ZyP_kDT7omPAFp3odYyjSuOzwa7ssc8LMnsqHiGl4QRR6nE34wtVIUpR-wYiYRNwtmr-MI39NvD4Qs0pjHFy9dBWrNWoYrVC5ErGPhcEd1oMO27T9zigriFH3d3dYGGFonS-LcC5BdoFclHOJzCWtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbZUMgDm1CKkBiK9cVv9t-dtHfWi5hIoR1_BFyOcke5CXQ5bvGoFEl01H9qvyTTH47AonYZx9r0RBxaZgtrO-iLI4L14kEC4M9Xe0YnurTIxs4uJ_nf4dtBDoSPHRuiR8MT5i524ETr-lVwRstSmPMP34H5MOeuZTNNoNCP9r-U2_WczMYLU4NsjiqZFEeoVg0PmDG0kDuT1TRTo55DznEB73DWypFvxLTdXLlwjj1bt2F6K0esDA7bgWMnQWGEY-ocI1U6L0JMTkKc3Nx1wnf7f1hBOs52Ps39eeGotqFWR5dyJxrFhpcLB9qOI3odG_EK9QCJc1_RTQBtTV7UsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIhGPrb7_MvDEVXOkCsX2zKh5BVYpm4EJJRzXJigygFVqVTMRslskK3ql5I_vF9Qfi_85CMsSz7PlhYceAI-wbBLZAkeXOyeVe_z6iZkG9GCKzTYMw4pyY7unUvnMRdWH7MmYKNuOlB77m1IRqsC0Epb8ttYbxIAJNTSJ69wsSBYMsyfQjvjR967WNO2cVFDO1D1lUVJ4q8w1LyoBPj8s_b_nIU6eKn0175cXIjRhiZ_DdNnFQypT8Ax32roPrXVKal0gWOiEV8wKe29zsbu_xN3Sr9YwyBkwmBCKJriT4ziq37l8Ofeqfp_qYkQIfyGn62JUaJXIQzeBYNs8ZITIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQ_6HEIm6C4OKmjgOfT_OQPA_EB_yKCvzjhjYtyuI9WiWcmhJgBqOfN81avNtKXb9VwDZIpVW4ea_wSS_07RqkKbteqQmMN14jGWaPjSvXx0SWB72DlXuz2XA4TaXyzQP9kzD--vBA7rOOOdtqQ0Sm2eVh3qhcR9mboH4vg0yL-w2WyRFDLdeV2R1Dojp-D176D1mGxPVuORzxHbHMCyKrNYdDB539Yn1vvAcN1zn3smHRB51UBmXEfMLzgED6qCnnJpQSAdSS9QhD1cQrUbidgJ66OqMF9NBpkFALnECpUorINsmo1RkiAujiojkbvi8Z2MQ2t6VH0JxyrlZYzLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLR4ZywMfCAK3I5mcghhRkBxYBUxdUR3z4OJnZNRckbZoo3GScIjSUELod4Pz6WGVIkcweb1mXJ9bXgti2zxXRAx1FQodMOq3Nuf5zj18sUJKA_WOy9wleYv9JOgF4Zbcmn9saPASsvs-CTgSZWqRvNbNwcrI_zgnN5g0bm3pa-riqepo5_CNRB4IoOaxlsOopWDhGyVAh0uW3ymx9RY2t3DHh_WCzU0YC0K25WNiynlY8H3-LhXm2vSEd8tIJEdkGFeRb8GxH5htX6QeBu2QX_92UUCTWQ8HyTnmNCaGt_GMLBRB-fRigK7zd8uyLMwehJYR6jDalErd_iTChT00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOenQAQoW_2noTHw-btmCAPrf0QjYKs1LObeiKd1UXe9Ql9EOfhCgfDj_k5aH0U2zpbVdXJt4ir35AOVL4vgVfOI0AYQuT_QLBlm0mwazcdPAUrzEi_x_pGDW20I5EkcwvK04j9EKsZuwWFgIoKcxmHKPHzm-0oEv0XpEnSfPwE8LPmPpNGSVMNbgUwuhla5LPpfeieTOwqVGffmlS8VODu0q9LdMxQqnwt_BhvHK_chmlnqzk4B3IsYhRNULf0vUfIHp90U2ben08fpDONR5_6r8MH97e3z-DODiKRsi7ZzGHrP0pySZD_wk16cPcrHdrCgaYRIeQ9MoBKCTZHbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhAth7THZBX-VRCMavxB5tA2wJu2CCntuiRyOUPh4T1SK_4puPdt6NqYzPQAFVkiaKiLc7hmcbSyxJMgOEdld_owR1aFVu3LaP3696sdqIXaCece0noyM9j1bYRLP9cjV0gNXTAm5OXLZArPJk0EMkblmftcN8Shk4UaCSgo3zIQpRcuL2lhu2QzQn4GpnAMkJKhQNmeqzWu0FIQ3YIUwoKafpnoAmHRuyQPDejFBUD7L124g0bLf56w5TvqlLrHFEzrXAqtK4-ZUuoltfZ80999TchaNPCmcWY6mtzXbXc2YcsNXNKK-pHNKk3Dap6oSxRvGYCjR_4LGRbdcBRbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH9bqEZcZ5oeRLN-wQdOY-NYa72zS8WtPNzM5JdBtLIVkxdvk3ydV0DXrTjFy7yJ5RJO1U7rvjgenwA0-FRTJB9fDxOwbTuV9Om5E15zgIGtr0BMYBgRGdLSVoLcLncbj4cnKjGwTx_fr0suSYp2eNLbv274YwYD_Epdi0ahFe7cZWM_Mh5iMzooTJ8a_AI7eGNixlnpXM20rGdR0MUX0mmpoxBd95f9JimSWp1_GlLjAsXWUqnY-Lltx9RBV15J_KayT-fC80P5o2AU7gHWUC0v30q9OodKDwrhZXTVytIzND3HbsfjLGdVqlB48GhPxJ4vsK5kafGypgPQYMMWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxeSI8_Mo8bY7VOTuqIUexFiPvGH4i-77smwOrMejqd4zeb_75MGSXDvK092nEQRT5xTTP-OQCz0HaWZMZuFU3pSMHX8fdkPDyceh3lMclNSMvaXUN_x_mhxkm-je10xwARutaa4WEgXmU8qQZ31rCDarJR-mu9x9Ts_c0mzpP6Vcrjz9WIG8qtn17zEwIdx8IO9_We6n28Vi6Vvo5HNK-lSkULmL8cbiU8fdIfPDdZbDt0mYVOdbK68J8tXM2nEVGxRGbdI01w9WLCp9jvvv5XwFfomKsRDNvh2b1qxlB_EL9skw3JIMidsS-ktbtj4DrKe4CnCDEcUY-HoHi937g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL-elL0duLEwxtLnJxRrJ8-q3OJNs3uzmsVnvbNbpKLX2o_98L8YkNFk3-1qRCLYFMf2WRTWEuAxNnoAnku2ByVPRZWtMjaqMyulsHyL52MRSO6Nb5NF_muMbO1GySjdnAoWSr-EjA7vLxi4u27odOIbx612GoGProR_XbyOMK4j9wWxi5u532lcu4AhDbM9Z2MXRlNeAqEkYuz827o10pJr0iaAOeOw4SSzsGqnmxcUDiiLc_SHl8646UQT4Eepqshc-2m8eNqGGkmr59gN7My5geSTTd8E7PE4EaBQIiShkOxFnTS_sNF2xgexeXKQOZp219i-AmUqlzU4mvii7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvHHzB4fKte3jE7G6SFjoJkFNnsaMbwAfM5zKO4xBTVGofQPLCaki3ytrATUmbPZDp_uISTduJeqNPVB5V8ix2Ni_MslWC6j21EopcCY0aAcg_fUq4mKdB0wpIRY8OzF__qFgbrrVn8sHvh0eyZ9JjFf7rj6MDyUxYMrEd_CFE4E0dNj_05Vzq_tcHVzkElfy9_MsQlghnRuo5W6OFj_RR8VHDXwms5JdOdCx-Sp3cQQbLZ4NI64xC_13a9d9kpEnMLco7cq7u3et-P3gI1u7PGS4oEeT-ZAEWNIERuUw5pp2BprFjxd7ZfQpuHZTBNUB1w38WsfZTKifLFZeFPcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghDSVRKSlKe_7uuz8xlDTc3mrbR0cf0_kPs9wyYcX-qEcwE7Yu3duRIHn8euIPxXwWICPM2G5b1eY1S93nFY0y2c8tFo7ewz_U3XYbFTWOtOHGygoL_94PQchQkmVgxJL_FiXJaEHNuEdAJYXRtf0R5QOZsdQ2wMCZmjCuUbiMHt7yEa--STg_mFGAgqvXZhI6kG5o2P23voMQnirII-doiJc3EhtiWvK8xgu2XvCdp1-4unjdzsD93n_8hO2la2ZkvCX3mDcUKA5dGdSmJ10UBCXf-QlnzBHhIa1RC6U-ebHeBWWBoANXITffrlVWk2hpBmSJYSU66pngwmoOYBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDN3rgUBE5Cd3zW9RTXjlOyjs5WcUjppMajl_wZHPsYXQKT0ljHXQsl-MZelFZjstfp_PKjOw8tSmC8xI_QFT3uozqps4_THx3tNARpEUE6xwYH0tth0xmoS9cMRwXuCryaJYnS10YeGC2b7o05l44dZI7GCeDhFYYXkZizYguCrO0DfTAzxRzw4mxVQquKeljAbwgp3KOSwHeEikeOPlMs4mVfLkOiUUyjAGFNUCZYvvHIgoQYyKCkkBKQ_8o4SoPZATiFPe5HQSZH6el55wtBKpZeb781Co3dT2kEu7a28rBlaNYDbMs74LGUpFLrXdEX5sUplK7DuKELUd9rPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp6OtN8tHk9yu1k6S3vhKdZ_tgPEPUOsOCiYKnlr06ikDGj6pGqVcc8mm4QG3jOnUQ6RAU-L4GcfjnoVzjBf014LVwaeSiBxpL-FCmpoVG2K8V8L21-ww9zxJKytl9tCOqAvGPsXAWbjJtfd7XeV5ByapeogKR_f0EDy4SgH3FimUWNfY_GqWt2k_QZ4WpZsZOTERvFK4eGS-WIQiRveiHIrIM74qw6oZ-y5cAqKFuFZqcwOHawoGoYdU57K6L_3B6qnckGj9dORLcR4erln_KCwQ394riPtBfRMJIs04dy6k3GA83ei6ALgAyUSdUiDgFCTNs2OGecQTfLRgx28eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDvbf5RafpUq5mKwa_ODrGRH8RuX4ErGbEAIJkXDHxeFMcm_T4SpmgxKGCNCeAMYdMBpXI5v3Gef-v_eoPM7MiYT581EvrGTajXS45dZ3KHsHYxIjEBlzZ1xxZy5d1bek00pWYXCURbidTCLs_221nhvBSGy954lInHmeNigC13Xchn3vdOA5hgZOVmwgU4HVPWmDSp26mp5Lsei5sLf-24DTKPXlA7Kug5d9HxhrLbQn_BEMxFBbgQWf4gqDNawaTDOsgyfiMDxciBo68c94iwejwbh1MdmN1jEQrqNA1m8Xz7JYRzV1Dse0T5HoCk0xGg2J7poQvmXwvjNj_a94g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcGKmgZbqFkevFQhqOOIA5ujkMOz5y0GCOiOvyx-REzmslgIioLERjMzSxvCqjQwW72I1Ilv0wSQV8DupK5otOWGcF48cjM_7OeovtKdOlzNw3thccIW2OQCBFAizw3BzuT2IV2xrZxL3612tNcMm0rwye5hzbOjgJNJU87oax4f_7wkQiDjuVXc2-jEhAMgjLCLm0zPlI6DP-giAunXHs7mfc38R-JuG0UZRlfF9Lpg59xw3HR-wLhZu7H8nJWoQCUA-A8v0k-OnTDRQlelVXSZL5GT4R_5ia_z1t4lzsVWTGZDdAFDaLOp-VEwT8Fuvttu2fwzOMxxLXYQVkRnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVV0w6IBTbpLijDjwijv8L3JAWOo-qLMCI35-c2x9ipgCmZigdRSSMUgdvNSFMwpjz0suIqfbTP1k20fqvjIDMXc4PHdHPHUTP73nyINjRghg8kKl3aN1q-MR97iOei7hdWsN2FYbchqE_lWYM2Cor-7vH6D9TR-m8wg-sLn_3ztxo9-9rLswV9-xMB9TgjXnFAzXp5G-biUNJ164lJ5aIBuYeOa5mtjOzin8-JJpFbzNjMk9G_0-6X2oURtof39aN6yb5TTj9qdVRWtMtiFSaZHb0ShwRPO6YSi2zjudiQynj7RunzngNvKPNGcL5lNXUFHPr_V3eI1XA58weayOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrdEYUq1ENj56oAOy0VbSY4zAyIQiSUy9wS_x-O-AGg1JaRPKSBjq799v8x1u3snhsxA_eAjimc9P-_ecWvO7fbEMsP2IeSPztgQOkTZWNgVFGyoSTwJw99_TGYrrlMwoPX1CgDnRBi0a73a-dRyFQbf7MnmIM8i4KJs25qHo_O79sp-4jcqjbY_M0q7JBs8cB1Pm6WCN4vd706z3FkBhaoFeGv1NrEpMbaYSfOMHDVNLfUvLd89bztUANVwbwngQbCee79hZ7tsPr3ofJF3yuoz_Gt87pJufp77GHBDCG4bp5MkrRT064ryiobHxJNvVCWmMJgHfMOhq32Yw5M2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frmB7NOmNibyODeXJlOiJJaJ1VZPmlBETG6IUAYXqw-Xnxyp7Ms6zlj8EtBm8DtcCXPNUTN9QEpC_S9giSuCJZleEZfM4JwSJUAqs0_9dZ6oicUF7ztiVX37NUzx1cqHqB4OSY--4DF1pWPLOCjvWAfHTnjcRKhEGJe9Jv3esqFe-gxV-UQyFcEaDPcaFA1t7MadSA1ypU8oh8bKiHu0UvmePIAM24PefffIZzLYbEpPk948WZATPcx5eO6nzTY4dl_o3mS6lSNo4K--ltzqGrwO2Dack90837PdXSz_Td3TIvKU1YwtaOFMwRT2hR0odxks_52kzi9TVaerFOiRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8FC8tAHoVXUhoiqRdbm9kz_bJ7E6R2LQQyWR2E_lxdqC_Fx-0QVj8WQN9IzUQHFRx8Clg3b6dUBh-JUg_cBuYxFczmprdo5W3ewIDk6ODcvnQq0tE4lwzimii40wOgGnvE96DkKz6ECXgjQlYWavfQmdK0yCRrqismrXTNpMvi7hOh-aITO8CnW-RlJqaqWvhhNqJ5yQ9s4bYVXjaTPGQzC2yjWz-DNP7ZCTdlTCpAcCrdhqXawg683NuxdIy69uEIxGViI21ASGRd2gqgAmwY-mq78opc7JdGVWK9C-eCY3VOenMrZOri_3l_Kt0D39pgxpoV0-GS6AR53Awo5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7DJVIfQsxMK9sybjseHhjrWZbjebNH8JNWeDBzJJd5vw4UeEyUDuCqhqSKqY5d6zFb79_j70F_upFKzocYjbUK_Tkj98sKkaTEAArV9858I2kXg631x8QzgUb1XAf6outET1utY46sSVPoRv9Tw8xn6xXKEosf9gNRGnw0TRZcQV90Tnam1dvd7fUuXgj2Pf96jiSveepkLOptvAlw6XqRedRNS4CF0hMKnGdqKh5eOghuB7mN2d8P-japn_6ysuGrSzETA5l54xaoaUckdu-Lj1q94jK1vAkVSErEGHsvva9FN8z95hMQCvNxnRA2ln5zlI1sH6p-VhNYFr61uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkBiqqwoQEMffJnEd95m_2rCXCCh_fcMge2TMysIgVSZA1em4ZrgCORsyU1TFnOZzbj6a2cqii7z-pNjIifcGeTBIh7hwEfbJXFPdqZRyXCMSgTL8xjehJhLBwnhSPi6hEGY4sxF4Y894IVOTd1ibFAlF3I9cO9Ylhw_y6Hu8eqQkv3hkHGmXjqWAPC6sFZjNAfXyVUpvA40I6FpxS4OdHAFHM54yZM9Nj0ICTp7DvqrnNQfn-qgKFpXI_vxCVqN25W0cQr6M-tEWH32Gk8w-P-l5AfLEfp7ysjlqq5oizviPBAVn5NiRFdTfIrPabSjqqAjJbCwjrcQasg5V5ULOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1w_Qu_4KkSWvxM4Gg0CTCrhZZ8Y8bBQP3JoYmWQjZlMpzQC3kinFvZowpap-8U5rpDPztX7i8xyjhQmIAMuMpN8I-eWJdHeX19AwSgeenGJsw_dquU5BCC_It7XlIFyMFspec27m6B51OS-iwrpWPLbX1nY8C_GpQVl-g609SnCfc48Rnyb5pjPgTvXd-vYRPWlqGq8SWX20CsQfpHNHeB9mp0ZR_ey1KLWGAGnXllVIftME9lvuMuQ5FUOod8GyEjlJwcofKBjponMtB5S9ZgurOxUlAsamYhOHntqcc3jxs7G1psksqnKdkTRppzDyvVMQ2jCWYS1Iq1-R6cpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAH7rBdxXK82QYv5AkcbQgwi5pliMcxNuCZYFGIRVVd_ytmUXGVkcQJ0XOlH8XRBn103ca0yWqM4pOVvNKQ3-BOu6zaZipnNZJWxPsTOpsmpQGhodaBRkIweeSdpi1dKzw9pUiEY769MimAU50C2T8TME8ANvNQ1ChCJe4HWL9k7OH4YK8iCvAc9TIGU1ZkR9hpslqT3apymWVyeaM8CtrOBci2XHLGHYyhXOlOcrLTE8MIA1cGad2bTDTcLTxqbKP5s_ggXZrTkXSfe2FrGo1txVEkSKE0DY6GtKOc3CCT2VO3dqjj3-GR1-ld2Ls0R-jnRqkNjri4wRkrT6gpaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITC98LYPUGcv6jX32cct0NFj4FDmYVQ269HQoCqGLspoRUmoDsWyyP2HFPmH5l07JfkvU7HSaKry0EwlZohTba-SC71FMtR1iB-aBow-qPAjdQlokg6qEmMB1dN3Ztnu5DUi3jYvg4dpwnE2gxFfr4a-NVWXqyImUU-dUBd0SKI2E48jdhEHg1FQl7S7Imzyp46trR1Aes3DIfdg0z5Ej_bVdrbscbsoamyaTh1RVuKts89q9svMfbUdMIRvJzTas_JRb1M9Ys-OP-N4z9jL8EGtFBuhWN7jQI_FCaYUBpSN31tBj_gK-wK2kac7V6D8LPVuD1k9M5Zwsgnj1Q3ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKfOMaLmfB6b8lenyqJsu9-Yg1X6OFklj41EHgPXKXV9-h_YBKQUs1RuKG4r-yEeG79TY7ZjXfL811NJ2Yd-cbarhgoRg-GwU4o2DHRMHCbzKC47AX9eI07-4aJVoB9ecEJ_4X6OHikvQvKxLXycqNa-TP2KWJilK4UliWGDCybJxSB-lSngu4Fo0QBjSvbS99Y2NYQROC0atlF7ZbF8V1dYh3OLWq-a8tNX6V6GGkzb6z3aG6s7f_cmvxbQvZKFb09i6iNQnLncDngfChEbhobV1PMfTVdYD0XWlClmmMFTbOLhODD8Lmi36C2RoU1Tg68Oazsdr4jXigys1fFOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1CvdpD4hLgSbPSp6IQ_g0wAmWP80aia5VmWPBCP8As_VwYRBfs7Nm1LIQmsoIm-ZFs2QKs7lOypcZmqQ4ybbsV9oUlw58Mw-lIngWQ6srQRltR-93V7qzwWuFHrpAKTVifmP_YjhaUyqhontmBOQQ66qg71dlzjFMhYVlvMxJR7w6KORaAHz-oxs-RtSLJWyGoKPTa7tvI0LUbhnzwYMqtTKOMqY_VkhyZTXjegB6G3oxmrrR3cN0hvpKFVsmxdq0QySA379bWFCwENfIpUCuIIDkYV2_0EkgCVg4v4RpRcKIlEEUaJvOFlsMJL5gBkdPFqfdysE_V02yitEd9NgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCeahswchBFH0Ejyfvxv9Op9t4mUCt5MPSFnz7uWXFqtiYa2JdsbKlrBdNSl3NpkFYlijiI3RiO8AF5ua6g_uzLHc72KZ3Gh4RXoxSGX8BgPd3h5-HJTgcYjKfYhFOyD5-Lijv6QaC4kWtYyrnOi2zCOfuMoJrhRI2HbWeyEilGXIXxwPc0gK6CN5qlUxZudQDu4vFYliLWuvUItK7Y1zIaSN4wCGfKCCKN4Jj3rmSkiB9HuWTjFWsrxbNpDnck3Mpb5fuX_8hzYaakLMQoOnBbSiBP9cFrxzrDhGYDXP0xS1hojcY3N17amMlFP_WIm3r5M1MB6M34llOdYsqp_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-1t-_xx0TUsq6TPYnL1Ge9kISIyTibmheXLqoHuT-BiAUCpMB-DFZK589kuqAnd_NcisW0s8O1iWvM0muVkoOoeogBVikyJT_qGQ2R5tFBcIXTI1KPRTy1MDeFm91Esc3AVZeWvuN5dPM577HBpoKnRkiGvSRWFxyAEZZ6_mwySATvuHBAQHzlCLo7uAED8Bv-EeBv65OZdEnB3UNlJLwZiw-hjIGFWiY_54j_c9ksuWFwvyZr7uuKAyZpnRY4zA0alzaFPHHbkLz_pQ4wFdl1eF-GOqokPkH8p7b0P-6sNTuf6cAkG3yG2iN4CLoelAhzBfY_6wdasQKZ-WoqPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW1tcfAlUC0xrTZ52C2zhA1yimM8bm0DRw7-0HaQbF5jhwWUSky87WEzIo4-Gx4RWYlmuzKbuOhueGReML8XZNpJtoBcEEueSAz_JrInzhPyTEeThs5YtXzE5Da__q1UWmO9e3xzzuAAiqWl14Vi4YwEy-GGVxHSeS-olwihQSr7xU0utwn_MMS6IN1BSOkNb36wYr94DHl2ciiAjvKwcjuqKcHVCVm_yfNi050fQBA1MImT0xwN20rkLXUd4tXQogahf-p7-JFXoSbfrJPKi7RAmBWSLTs8JMPaM5zfEpZBFBe8aItdEdHsZLJQu12QQOCdIPVmSihmFbbc3JUuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsTOsomo5i-JGKF_XVMe0k2ORulGPm3qedmjBNUTx7JubgqjweGGENRNw-e96jkfQBxMhhP-PgSTPsPgm_mAM2aNGv0lQrUy6TmjWzAnq9aCrDqU8fLxO2vrrabX-R258qwdLWjPdq5tQ1O_H40M0TolVTFEa5bi8OlSxb4j8TKjNOhh-7nGkDmBoB1tMpqNfuBVDgDQonTvNlSQMGZ3ZOR4MUyfwpyWoAUHWB3Te0qPTiBkjM8H4Ske9P-0FNzotf2YUB22JjUqAb6_MupEj2YR-I8S2784d4FYfxmZCRFDrbZJn89QIAM8LAy_BMqLyc7oXdhYnpV-QrXSWjcgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjQjf52F-X9ouhuwhJO-UvZstVxMC2PBX9qeuLBLM2mQZACgqcbFk1hbU6I1pS6BwMk4bdyQAihp2FNoraNAj80YL_MOEksrrP--UI9u4CcKUN9TQ23-_oj3FAzrCOnsPzJamIH3ToW7Rf_CSt5XjumvPq6_MgAU-LXE6aYdamaJzU-v0ZRypoZCaDrOeHDR0nDWKxRsZXjzmnEJ1LodGli-dNrx3Q7G8TSgAvt09mj1hpcaPWupnSws-qAKTqmv4MZMRK21GWsJak0Jm1sAY4YGdrmAOvEaUgdtFtHBcU7yl1VDyQCGtOpsPhVV2l7ZfNHJuOmkIjaCykqImrsSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T89Er64S9wtSMXRaax4M8TlvPqZGSF6tiVRDnUkzQhdiZoqy5DY3baW-OlNabPPp4i4W20gkygbajU6evfmr7UsLYnoZg3k-qvX7-joSLmeO-TcnvW58ra1D8HlJcBrRNhLX0hsL1jL4mKU7CLMEr2FKFdRVnrrb5SSlKYairl43DDPdVmm50sAV9kuWKMFp_idr1L1bJXdx0pUDV2hBBzt98IMf756y7kiHTnQNlfDjyL7B9Cy0DlwC9MsU6J-5XX8ku6OhqMt6uiCgfdCAnb_VTvP_XUVdypGIEYetEz-keU9qxPasCaPlVRSE7aG6BnZiPI2sCImrwqMIJSdx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uz-LxXu9y604SxIx4S8zi3_gcV4a2-N-MyPgxEsp-gtSQ0-XhksFayUiRZiFbQ0lxStQY-9LgNvqM8dsre5CAkcbheZgGMv7htcttP-0bVrNoaSbf1OzFnDQW75bAiZc-UNMvaCAs1sNjjU6VfgZssiXvgipkAAWXtx65y-UBBiy5YorxuLy0mmBFM02I6lg93fuzCq_lKtjMjJZPrj4p4qFIc4g60nPbanuhXsFpSqGxse75wcs2-Tn20ePMJlyBvaWS8W9VGGdjV6AEPCVk8xzZf5N7NWiJlEU9sU1kl4HzLHu4KrrTBE8L-ehiQgYgdCUbLPJCQto0GQxJTIe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUGeQM8R0P1FQaJOCeQ96bNZWhW8wP10vYcmkB_jIRE_J-mmua4Tup8EsM4lF5o5wXrwYS9liHSWheLOJpwVWPblvHivu0jnQF8UQiEX2wPAqImbCGxRnqJ1IQuSoxfjsROr7cbDoshQYfjmyURyTEzwnM2Sq6N03D4Z00Kr6qc_iHQBPv4WQsX1eCgPYnbq6NzqxQv5ZFqOiXhvcMUuvopGQMhBUqEgJ1DXv8ybj16hl8pnDu0VHHfvzeMM1cvTbWJnmVOdAzt6m9hUgFmgV2ySBRThn970-mJvTYYkbPI6rgT6pXFoDhu74EhgzQbTLnA6J29rHEycecrKsEW05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1YRWPi-VJmGQk7BSMpTKUqyrYAEdK4s8S_67G2RYsss6Ikf8XYt3KIIsLNhQzduuYSNjxS0VzDrkb1VyiW8WaP2U4Texa3CUTAPI2koN49FWKqZHNqSG2PAY0R3BFG4dysbzHEpKvfKkOS1JyzHgSfs0LAoEYmD6a71QqNMx_ZWhM3GJ_9OE3ArvAfc8u5Tk9ZSw0cab3X-DqzUkqPKuM4z1rTFaNI4in0KJ0Lq6j17hbwq4DpzYOGV_mEay27V79OR1NATY_7bVidk6jdbMruQatxlzpeEP_Ik5S_K0FKuOQCuNb1pFhsg16yD-sbQBQ2VkfjADqtunt7kQWBdTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQMSn4jSNTgjh8TRsDU2vaJn7j8go2cCwG3c_sKZAE1a7yTl8V1Y_vswpiu70XNOlf3K0hi9oQL9LDeV3PAh9YcxFCSvvQKojIDh9MBF1UiDhautAkEOM2oBAEo0YLPA1E1Tfz51DhKl-MyqMGz0pZ9IpKFZZoV9s6MrXz6PVNwjnwWzzN1RMgmadjzMSWxSSnl6ah-fat1B5PZqs4QzWWbcBylwWWrFZGfFkNhNvdzDjGShDNIJqBHML8EUMagomUbo6Arz-M0NSm5yqnZvbqUnE1nFsBtuwhrL4WVimCCbn4gyFfrirzy3Dp7A2fsprCns865MdrjysuO8mM_eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avzKm3DjLxtPY_z3DLTCY5L7x84OOgW-htulaP-B0xSz5KlVis7INa_GNuzwymuoHsXusuVVxvAa-f3XAbYFawWVv3iWC_EF75M8_kMa2AYLUXHQQAhHGDmtycUjm14nluwdgMPM8bECbN2hWTkkCEmn4Y6YlRs281WfFJ0-9qSe0U9YvY6nKQTCI-A6PU_Yi_WxTWAoXVzIIUjSwLMPcUk2D6xgIOD6nDbCZo-5RIZK4hZjT98kEk1Fa5nf2NzIyLiBfATuKZSBFclvVSvtcfeYwn3u6Ity28sjB_a7JAzMWanYFMHYh33tqOTYbQks8fZ6YnM1AHZ_ihwJ6ufLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jkc2H0kiovXp2W8m5UhzNlqFBoiZ-BUnqpOeJRQ0bv5UxVX85wEjlQiFaoQr2qoU-IadSNjKuhiIN0o7uzDxteOU2zAVoetRuouzNvc8zLfFh6mj85TqTPrz1nOl2Y59MM1r_pdNXy1yiHzmM2moFwo4nocOEAY6K2NRXxAMqB_l69A45RS-QhUlzqZlRRl21rcmd7wYB8evJEfW1pz3Xn7mFoE_-JTTpLhlaMgUJ9nF-fZnwd6hrkaWl8X36bLboNwTTCrzNNT8dlEcjLAIYwkPHFll3TARcprffPd2BVq_L9bMrWniA3WVFzMdqj7CImC5puQ1yChrVRhih0dObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYP6WHJbVbaAbw_BP8YKi365lnbpaAWQrJMFnHTQAYYNZ4gPTfOyIUxVvY1NLrVL2U7h75zHEwdY8NjaxkwYriPMUByLjbKz5fOe6IYhNLo3o6W7_i85fGMflHtRldqzeZM3hhxphybRIP8ZVnkt-LZZuKqiRuq9ufOCebGfSpiXiXoHC81yIxrY6I-ghef-cngS122yDN2vQFY0PtwrEnrCMu018r1aqrIVVBTjQw-BMlljg9c2xNDf0WeQ1JeTL0SpX8-YmzBUv5Yp8j-E3giYbjauSjdu1ju9i5pH3pMOUr4LUHIZW1KwEIt2GMs3ojqkBARdi975xEbHA5kqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLZpvoKn7eyRx2akgRb4O-EYXFQgoV-hlIvmXpswRWNpUCBdxMALb4pmQScuaRHPrOrWAw5X2taGbb-ZWrb02zhDxQtv1jqQVbrdSXibTqtuUEj-yOO3wZVtUx90nip52ZfqKYviNaYvCB1n055yoUCll9eW7-MWzLoqklMsz3I5EHuAt9oBvOQ5s3yVRvphSw3-1Qolt2mwc0ZT28eO8e6I7b8CeAvXZ2FjapFvxM312T-i5-WVg6iXY67-in2_zdJg-41e04ET6UWfo4v8WBOnKm6vRxm8XRw3lG3WKDWTrEGpSOpEVljjGHV1qrPR6c8SzUsZN37sEmZLvfhVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZeh4ivvfMLd1TMe8P9gZRvJPi-oRM77j-xd098-DjDoUmaWJGojNk_I2LV6fwiOuj-BxSULO9FOvsEOCoEvnMOI5e0ZwqqU3k9Y-yHwK68rXoC9_YSCczswGhMS_WWeYJV1hv9WBPbl0NURJh_1RxZ71J1bQMDsu6MZY4CWplElluRxkEpNvhrnMEy4Gt7dPPTlNM4dPMqhBs3rGFMyM1D_1WjT8yb8Izufc11UTv5GYAGddSZhfvg1QRggN4L0nRa7JG-XtXp9wYeKPXTAgM8XHdOQDfVIaQjFKMPrj-htRuBgh0CE0DcWsm9h_Tp6PPMgIsijWZWzfDa8S0G-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=APFFNs2wq4UJvWKPe58H6Uas-rOyN10RgqVZ8QY9-xStpogZOHumxIm4QQZmOoNoCCSSTOBgUu5hZYr-QJwoODWe2iH1GGD22cN45_sVcsIhh2hb1Yu-AT40cvjI9B_nOIYtICgdDTWQ8KecUhyWYYtBI58Bl0X8OS-xQedTQfJVBNIj-tx1dMnvYS0yTs0vP2qQlSfAq8oi5CYmKIvPU1C9I5myIdFleUoDgdS6ZQEiPy1uxFM0xZ3asL6fh0zK9eKSOULowKDS0Sf2dKLjkYbTK3y7TVNk7E8DFt1s1ufq51mJgzZCM8MsNfYc0Cuv-hcCW-7dpar3fFZy-LMGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=APFFNs2wq4UJvWKPe58H6Uas-rOyN10RgqVZ8QY9-xStpogZOHumxIm4QQZmOoNoCCSSTOBgUu5hZYr-QJwoODWe2iH1GGD22cN45_sVcsIhh2hb1Yu-AT40cvjI9B_nOIYtICgdDTWQ8KecUhyWYYtBI58Bl0X8OS-xQedTQfJVBNIj-tx1dMnvYS0yTs0vP2qQlSfAq8oi5CYmKIvPU1C9I5myIdFleUoDgdS6ZQEiPy1uxFM0xZ3asL6fh0zK9eKSOULowKDS0Sf2dKLjkYbTK3y7TVNk7E8DFt1s1ufq51mJgzZCM8MsNfYc0Cuv-hcCW-7dpar3fFZy-LMGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gugUinQm4hp7KEz6_ShgBnqsqxt_wySnaM6NrPmgOn7_kUsDUfjfF6HejIvzQ_BUaVgXU4rW75J8WC_Mg79Sd3SAyU51ObkOzbpL3khkzZ8z_BaPKSqiiIe7IKMcxfdgtnALbBuCBvqPFoZHOVBRsFuDC9SEFOqD8hJpF2UTarmwvkTcokMH7EnswsozT-RcEMfpyh6oYd-HQ2Webg1eO70fCo3Tt1yYUfa0EG3r-CcovFWsj8w6ZF7PIHUexbvaKuIyTrhinEj77A4ksq9I_Uuii0SvZx1MHO7bFmTcJF4J4W0I2du_i4tMclt_QcGNxEgowGqkRsZM6ieu79xwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI0PjmNU2K1l-29AeALr63AyGWglZxYCxXMoQd0Nhv44hMo44huCS-8VxCRa2Wc-W4rFJiJfWDFXTwE_eUS4lLqGM21qlnm1gNPK8uQPka9RA11bIiymnl9QR86xZVrEFNXGT2IDNnC9PlbdiGopkZa8_hcC0sZ3ASqN7HVxm35PVVcJDRz9HLCwe2RP1gvlpWpoIbhaW49IHC_KlXIUK4hqzAKY9Xl-wQQZu4jGXhnubYgECss3eARzvBMbPVWdVMH-KYtDPkWJDGS-i3zB36rNaA_KsulfykFGGCKgmqWrvsf1V8scKP-yo4lSYU9pFWMkyDLsOpSU_XFdRTZD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlLWosVrj7_wovPsdxucWEdSJG4PNnZx1lCvv6T4IRwmgXG9yopkWXyG1e82zXWOFoNkpspqAVWzviMhgHCLiucchUi58ifCecSW1hB6bB3ToWmy4E2leqZb3Lb4zU03gadzOkvBZ2LJCMFgfNQSjbN80WulSHisJViPXNJ1TQS5hfYDl-Hs93shpShRx8fbU2RHSkV3qVgNRANF5Dq6AezEGql3tcnCOZlsi5tvtE1wZBJKTFlfyQH0cfQ88z2N_LmXEYelI4J41vkkAalOwgFHy00yKZU7MJ6qGksqdXuNLkBOan3J7XEfLnZ4RewL2tDOl5rBSZ8YJq6Rvoq29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgBQUXYSaZ7WgRo5YyEoz8FNr0fv9fTawC9316w5-j4rmUwa3sN5UNqcU58wZxp80xjkPzgYJ9CFVucjV_TR6ZD_UlpTvD2vDdxiOtvOywmuHgXULaYCgtJ7_214ByX_B_ZpydlxkqVJHYgo9Xfs3OQ3w2LAHxlbBz9BTrz977XOO6_AlDlqqi5jp2Y2q46xtu1kbz7yg4wwsmGZ-DWliPFafHQsi_cvpmgjF1rtijs-81zY-aQ7pAfMqIsBs-2taru5_YL5y2pd6Me1Yny8ABZIv0nU_nhkJjmYLyeCIifhG9q6i108NBTs-92BBmWyCziEMYf_y4ccp8r5LhmF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7zsOHvBBmzo67iaaGIQLU1VCPooJQ8wxA83Ra24N29nBpTWq_-P5w9FLuROqgsKJhlGaOosTEtQWctvNA6L0cy9uGLaTwRqeikyKoHNObEScv48Jp1OkrBoZiWeDOqnzdbiR11DYDBUCVLYiM6ZaK_Ds533BfWQ508lYgLJE1dUb7GDMqpNYQL83KyumiWJ1oCVFeJGBhVLiWLxtKvUf9o8p8ynrjQ_RhxI94j9uZR4Tx_XeXUztdedhhOS4R3P5EFQY9CmqX5YVTpLBl_dblhiun3xfEQcm4q4bbMsYToCE0OHhpw7S0ACWmPrJLQkC9UOomTpE8xS0rIHJxhEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUjPxzIWf_nfXx2e4pdBXCt_ZKttN3NvS8ttcP45snFlu2IaMcA4l2pH1Ib8K-zO1g-8B0Ez8hDvdbeYRM8QmpLpXqrYdV1XwFH-iXK3WE3k5T0OAW2-embR_mlk_PPoAR_JDPkI5F3eZW4uUT7LO7qzJcwDnOPAeBA0O17917DwBN0Dt9tTHoc857row5KewGP_qz83HQIU6RtTsf1DD64560t4yxviu8jDxTwpYiehlLxNFUCjpayHb67T-nMq9YN1x4zcVbUtpt6Ehi0opDB56sd2n4hXS23yvopQApdNIVj1xEOhh3sYI3GXX-2E2z-cSMtY4Q6rBsrJgPiiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJxCPl9LF8y5nfYP7jJvcI_aWqSYxmO1MuQf2dhpMF6i6m4MJN1eAg2o_6m9TgKCLpGcoR9NuJbSBB4TEqZCMbEkXOa3MTn8LbgDRJjGa31exlfbtF23z1y2FZai0uktwzpujFiq7Uo1ZngSVoGrWcBVZJQEavNkDQPLwS6TQTkLdVUVNgQoDyKEETpM8pFaEra_st5BjhpJV7OqSkd0O7IboeDKJ1LOLNNu2X8Ag-rgVMOIA5iU2QnMnvDpfo6R4khDtiP_8UVPF_8OT5B2zw4TNtCKX9ZBszlUJ7XwOxTQMfG2B14kVu-sPpeoyNf7-ibsBXvpIcwBrPpjFUXUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ2gc4dWp3-m65aTVRZ0765H8J90_rEKMDhO246oubRgpAA_TlVOegjjJBTrsw3qFZVo3Fq8GxhFcmljwCbw-bjK4_V_DhqBu0_FmBCQ2O77JaMxKCIRYHnYb5OES8_YCKikmps1-Q2ZS9Rf5uGWnprE1EPl2X0JpexLmveb4iAG3dpzLeOTwiqN4iNcRs7XgeBDCBMCkqE3zyuxvS_wDwXBYkpExIq5HNQGrD8W32nHXJvlq8dwyLD_tLCEPk5X8Lvygi8T6Pakl_8RP45sF_B9eV2APXvAOmN2HQtro0ME3r6UaSvQfV_hx8JwPUnPbWi_ul47wk3eSScj0xpogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChJ3FwnP39DgCgP4Ghw_Ml-LIhdc7YYni1Sw0UW81iaAcasADyDE1oijGAm4dfkowSrDZGJd47vjEG5Y7JmXWLu2vjMTqqybI-QOtU_TmvA1rF1QUZNsgoP2fxK_UaWdAK9T6vcWXG-ZOL1xBV78HhifgCVqq9ovi63aHDwpcWfCZLYsXA9LAkMPWgFkdGUmSCtcgDkLmFVeTDdOpbRvJo86uHpBhg9jS63-Ti8z_GPT4W4caQX0dvvT9OCq1G7pxsxVc6TBaPPAGUcKaRLETrt_OOPQEMX_d8y6lq8Lt2LCSUYj1nzsiC9DEVWy-gFsLG0MMccZgJWndoaS7jvKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ4x2uEHmWQWwb604ifWHDDTp7PjRlOk3vjY12h4EDVFiOUPRbXmToBHge3MFIITS-DMXPz5lNVck2GnHCfaqrghRhCyRUAAEmsdhNaxe6Nh_rkh6N3VO4u05A0loA90TcHoLbS9gBSvCcVyL61YDbiQtx5X5B8nVbwMdF6Ly9GHLexttAn7oXG49aO_LAX7gLXK1h5tWNMjCQadt_2RzPVzx1nn50YbpGZ_gcXSm7TvYAKxGDu6lFmWTM7Xj44ilVTUTKKOZOpxAGCI8x3AgXvFl0mnieozll5bzzwoEX0KCGhA-_5fq_g7O-VYtbC3HZru9wk_nJ4OJuoq9eUSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmtb4E0Kx4pxIQINhr-z0x5A1U_xHBn23SjbUPPJtKG2qnvNP962D-QU4znny_FL-hGLkkXVtqWaMqrYgfka-jtrVM7uRYGb_Tz20D9ytTOzbxgvOr8KHlCMbOJPRBgeYUGzorHh3gC2Y-KkYbb6sQsHa8oxv-Jsdy3_kbKpZUtwA-KnB4Q28MFXOStyxTvqqpcyGfbAdaHNHcNBjsUbChLHtb5-w8ptotofvugxfnDHoxnjZwWrZqSHs7J5-dRCLrvaFANUl_pToNmWYMAnpsGzXKDKVkrgrfZPDD5vcqNpWbg6KndcUE_tniNbG4x8d1glA4xg62TJbrDg_L179g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3TAtfpinrv034X7CX2piztkwWmHEy68iQAXAcrQ57kO-0W6rnaqGz21xDB2J_f0gXzfs5AL0C3U-JawrrjwD6bXJXZrFv3Z4T5Dw9SVbSQJwLQws8UTypOvwjuA5X4Srmfn6C2lAs6F3w4nWlHxNvxGRls8Js7e0ZcTNMhfjPyzLfOQK0iOI8jUBR1_eUKhCzHrHu1brbUk5eYSidzgAuRtZ3erYJ4WKELFoZcMYMtsUcSpM6-t6_kAbZiBN3rUZunnDUE8-9c1-U_raI7RiiL046xX9LlpWBdLqBlvzGBFsGNKZe1w_MqZMOSODI7h4JKoa_a2jjdGvJ5lwzFzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeIKPQDJL2Vffdz_aKM9IyldIz-EbwlUeDu9xymiLBoU8mpmOToz5BspPObyURUAfcTWkmxABE1nTvC9_UBAda78zzXmyahaRS7NZaBpr-pDyUKqRNsV69bpdKwKDESQ-zj1bfzuGpIL_m8mp9bfiNKLNQWRBDVtfoMn7v7UIMdDnaW2kJPHtNiCdgO5Rq_OEkLXFWA0pO8VUvU9t_KZcI6ObijM-2yb7X4OQRxU65DvrL6U2FuJgYAQ1Ugw1p4oTNdw5Tm5JQib1AmZB5uvo0-2XUgM4GuwO77NvK7YOCuxR_9INg2bYQWdxXM_ZJ8kgP51UUxVJb7U9S188HhRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X76IH2a-JLv1RIKWBFxWiNW7vgPJfnVAOHWi2ryBJSgRACkaTUtes7GGBnxP9ivE5SssF0SLoeoUyJbm0scpLVrkL5jbBHrUl8xAJABMIK4fBsV6qLckN38Vk3_fsU8k0sU0ZqoSQp256u8_8qLYg4nnFT0o4-g-LMIYunJi3FZCydFGXSKv2vsKXUCb0iw7-jVKQZSUKtjkvy5WXjrVuix2ScGLDj5eAcohTe93p4ajFhpWYDMge7AECjEZbieRG9ekXD64RnqFBp3Sbm7bFoMA0ubsjjtS_K5niLW6DN_MclsfB0zc3U1SUUx4QBBNtmBBkmmKGS89nKxzJBKn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Beb0we1NleNrjGzbSqiQe_WNuS_RVOIuTwSzQQ9-871it3yC8eG_iIabQHrrQyPFSCCSXEIalOhjL2RGqZGtOD3MNhjRxIRa4r9Y8DDkGEaNpUTOIsvXTgioFTTAFpT9b8VSq_s68XDlxxVc2psm6tdNNQx-QiQN8frvKUm_YFw4DuCntadUHwMMN-dz5T5bC7N66JYT3U3StJeExVXBEumNZe1UscmH5jr-UtX33YEmFSXpcZFFBujPth7TkH8EwMPBqgyHEPk6POPXa7l0XIBgnr_3NLZhcrEM9DpJZT2Ya6OI6WBcinTOcL1hORFU4j4JRTqfOjwChHoPe8OSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdtC0kfB54fm1FBq_4lKiOGEkKJoxgTjDeC6x-06xaveKXvWG9XduY80eCbqNHDZHUImB0FTcJXODDKwOLRc0UEQAyCuYm6Pzb6N7a-_zuyzt5JE_89uDe7YslVu4yIgjFptEBR39ZquWbW0TzXrUAFQYjHUqNnD-hek9342rDTtSy5hU4TUH2Sb8ecRCitY9ZHPHO7DpK5bllbXcRRz2LCP4HZ8tjseB8DZIUucQb2tDM6QRfd8CJBKSqZUG3t9r2OvTfnz2gIo3vCzAvcGtSXX3iU5qH9HZ3Q5dYH5wvVHAQCcLH21jdhnBtV15rOBa3IOIVTaUylLPN2tDHhWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLRvTGylvEb7PmIMtNkr6MKyiA6aPyP_0MteW4nxft3z9q6uDVVi3y9_zoVUXra_G07L03Gln9jamKEQj4bd_mpPBElxDb8BkGc3miahTsrpfRbz7QnSfsfkP38jBtVicV--iDr39mhEiKG1PkMGQF5VT6d1icFoU-85Mv-vHLuIi75Eq77IMLScKsCKHcxJYXUo2kHT8_-MtdQTNdyoOgzf28jKGTayWKR9SSmGu0wmpadKAC5Z6FarGz7x6FXxd8JtoSR7y16UMEf0yH6fJbPpXEtWvcfD5AmvkJw3hQtAL81KDIRtpV7EcHSorVdXZjqo_8nL4SAIDR6vH5OLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsgj2SbG4EaTBZQzLMHdNSBNXdObtEHN6jR4b0-II7foaJOsTGRm0YoAJVhazLV8zSOYoQTNrgbbDbMny4C1qfVpVPE3hndgc1KpvOUqBQ4M9Od7h360r-diIEZdy4cEClTykdv_8vfoiqNniJFf6vA_0Di_GYFFpxYfjxnN_GFoVWgFb7QLnsd2QQtLlJiy-lFKJFHR31veBc1XeCGoO51NEULtWlndg-MOHa_UAJgndbhw1goSZUCNyjSZFoZIHGKfMW0xcs98bGQaad-5GJuv30Xfrj388Wsnnzzvt_UyjvDDpvifHLs1eZz9ojTJYvLETbO2igQy8IHKe0Jmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTVCAim_BpO-lKQT6mx1Ou4ZJr8pUtpnN-MiJoIWQ5Yd9yfaXMcQHHQTdyjO4aoEIQkuLrM741D5c7juxnUd_YrlsCNW68e-cG9TOBDR0uAKtqrKIaD5LEVBsJvPtCFru_VMZAWsvPd4cW3YEMoZU21Fi5jCVr884D6GY1Tdg64M7GV4rdzBu3f7cTXJc1TkjTGKR5J6kSkMmD_zTXKJd05WLXSb1s0HWhGUGDUTwY8AOWg1u0gjpnpTM7hZ5FurZgKE_Sqsa4--vnbxqlg6jzI2t2_L8NG6gOdFWRUc4GxietVhbMr96Vyifyt1YJRXfbdw2mtUBi9eY2tOOm8BnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIzY_25zS0_4TuCPOIbAJgEpY_XsZmuzTbHKyJFXve3lkSHXTHMQUfJNk7k42vjWsdAwUyWaRzEvo8Pkoltwf3QPHqiFstXuBzuXfzLg8DZLGgwCxZ2pB-pypyr-EjAeXp_2r64QBnQopoZI9EtpFs3CtX6DXJdkO-VrWNd9kT4XFFdmTl7NFr7Tf0GM6EqTp-e3M7Tz4T42Ci5tR4QsKzRxeTKMBjaJBIIP7BlkRYaUvJfiJQxYm89SasT9fdw2Nlffw8FLdbo-Dc6mive0ZdP4HmTtJXwn604mHcys12uA2hc3yHFnU-FA30lCe6iS7ki17HocWaiK2IKJqHZEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga_jMMxvZAmu24s_YpZle_wfi_EHoVJZC4Ud4BXRz7vcMH85T4IU2cqBrkiypAZreRr9VqhttKr0TRfhBz2-EjdXw-OYmYXoVqK5WgUU88DLnySwR6trZn4mQ0W6A8Cd8BajvJKtFVj2daI0py6XzQCOgqaKhrtncQP97V2sCplPk9APhNnn6haTnkl9rESqdj7srV7iFicq1_hCthMhhdriaf0V2ymFJgNVGfe2XGgDhC1NoYA-yPHYW5Pcal2TURdrxX0aAkPje0EsLj2jwDwZnxqgY0Kr1WghsZXW70QzpFSf3002WNEvUz2qKxUF43w83BrxKH2phRpNnPEiBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=FCAyE55mhke-LrZuxtpEvPf3pakB94F05FRFULFU74zPilEYNzbF93Lgc1qfXhiAYVjNxEUbKcU8OedgMSPxEkNGQL9NP-MJb4kAij8OEONy_-3pdc98xjNqgIXe3XWhF_TmZPpvR9iB2w-CLM5otqGfzU1vLjg55AA5j26LOoQmFbQF38kcxPeKA1QjPZ0M_ydxyThkwhzImuyS-SGJmO8Pfn00BZhi0UiujmF0WP7xxyq5Zo5hBkQ2SPjo-7fL7r2R2GPHkaCrw58Fjqo6WYbl37joLm6lRUwmyfHZrnWzNCTLoUmzim7B3mBtq0H90U-sh6YxXJbEKtl8K3y3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=FCAyE55mhke-LrZuxtpEvPf3pakB94F05FRFULFU74zPilEYNzbF93Lgc1qfXhiAYVjNxEUbKcU8OedgMSPxEkNGQL9NP-MJb4kAij8OEONy_-3pdc98xjNqgIXe3XWhF_TmZPpvR9iB2w-CLM5otqGfzU1vLjg55AA5j26LOoQmFbQF38kcxPeKA1QjPZ0M_ydxyThkwhzImuyS-SGJmO8Pfn00BZhi0UiujmF0WP7xxyq5Zo5hBkQ2SPjo-7fL7r2R2GPHkaCrw58Fjqo6WYbl37joLm6lRUwmyfHZrnWzNCTLoUmzim7B3mBtq0H90U-sh6YxXJbEKtl8K3y3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkua1WijFbmoD_QoA5rdVKUSKyUE2d-kd4BcRuQP1xo8uHxLVXZkr1AUdFT9jywozazDWhC4rrW123mnmdgAhvnQW2m7WwN_Ktcgepppmy2H12VubMr8F6c-uHY3dZeu2KsaDscle4Tj9sKKejXZAcRTOSHQJOc2I3DEXctXVW3f5bufIU_xGqb96uksLI-ET77rFQ8ezoOhMZy1IeNj3zqopPHvVLzZCRSgvNfC5-AFVJ7Wmob7b2piM0e7xisuNk_X8A-3TyRa70J7YpoZAhO1jvr1nY1LdAOCYxzxrAiNIMcV-iqB6NnynuCFX8TuPaFWfo-eIIjRdCcbWc0RVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlMPXDht2DTbKBN1K4lPUwpK0H1aubiXSfIEM6euzfT2o54ICF7SUpyYQ03nIb-ZunSKVHGp7E7WGpjo9AxzYvSax12NwbpX2cPMCOOis3f6i8f6kPt6HxU38LQChLtPFY3LC6n6JL9KO1ts5W7HI5oLfkafe5ofB12SaKvq2h3vV73gQRoZjPWHf9K0jECJzqehVk33uAThySdzP9_iHA_WAxoP7-WFlAc4HqGlvjv55qMlR6lHj2435sdwJEW0Av9LMkjue_p6PuemUllOFdGuRpXuqc-CB6PNofSokah6o12KCUY_PE1f7JXU9bmGxf7JOlQQLaChhhA1ua6fiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIjYfkDpfwRePY17c3BOXGZFVbY3BwcoirKOAhdUbySE-EY791ZZNMqhjZ1A6j_sKuztPJ6nIWywmxXF0OueVhdCFgE_Ft0NNMsKIIpG1rrU3FQSkPV0Dsw2T8h3e_7lFDDF_hBLx96qKvfCtjRd-ilcJABXn90YUS7bL1CdPwpVFUF6zxYX5EM2DAOyST_-WuRWN7uh0MJQaGzBw1gY_yf6JUxlg7eneejlvl3CAJjK8EMne-8aGznyiuvm8JSTGOGo0g-xQ1CyNEISU5YmFL9jIEPOdgQub_57EvUQI0a8O6D0HJEePJV9IxIIWfx8g99gXqHafAY1bXopX0Xy1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=LCOGg1ZWLpq9IjjIgEjwwln0sY3J-GsocVsUXyI-zBVh_ga3jXX6vgeI9I704GC9KsBbRbp0nWrNFWQ-r-EY3ia3CGgTZ9H9sEweCgV0sv4XHy6lKapwjfatnNDShkWyC0fvDIEuzj1zLswZLBFACTR7IV-4YLkvYr1cI-NJyyimVCOE8LsNfPrNRrk2di_RzSIgHDRIjwMWy0ck-tewwIjaaVGuQYZA92OzAa5wxWSjYE5vFZPp2CWz-ubrcCHFET_TdzFwAoADKZWnU1_RpvicD9HTMzlViJN8GuFop2T9OpwClrxCuzipoc3aiSxtiZ7vwWTbP-8PgQVx_ORp5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=LCOGg1ZWLpq9IjjIgEjwwln0sY3J-GsocVsUXyI-zBVh_ga3jXX6vgeI9I704GC9KsBbRbp0nWrNFWQ-r-EY3ia3CGgTZ9H9sEweCgV0sv4XHy6lKapwjfatnNDShkWyC0fvDIEuzj1zLswZLBFACTR7IV-4YLkvYr1cI-NJyyimVCOE8LsNfPrNRrk2di_RzSIgHDRIjwMWy0ck-tewwIjaaVGuQYZA92OzAa5wxWSjYE5vFZPp2CWz-ubrcCHFET_TdzFwAoADKZWnU1_RpvicD9HTMzlViJN8GuFop2T9OpwClrxCuzipoc3aiSxtiZ7vwWTbP-8PgQVx_ORp5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlPWCuCJpBCe1UxGaJlN3r3DT2hTAlxx04Iu6uOMXKJGrhEhnf7-2AqYO9HhSqjcM-d1tVibCOTTXx4QUuXIJKy4Hx-9w_StR29XDhv4EUnj32X91rNGpQYYO0NvmF6kc8Pe9NLBcES48gA3G_DdLC7ovmLmKXfYK6kDKkDx5XN-PXEMUfES3twwjdw4qDFA6pSeEAosiaWtYRzIXLqO5XOFPtS8tJ3mJ5v0AJnopCMmmxY8xnwrYRPqZr2SiSXpB_FHG3BqcUeUkqxrF6UHqERxvbi4QnYUsRFRlM7kAlCEFEeT1L-ZbNMAD6KFJTIuRkiRek9pD0lbluhM-IBYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXK5S82VZUa3pv5Wwin0uMho1-AQB62WcDWcqKXqI4OMqbZKL8GwGf4z0RUDbtJWvKTQ5cfEqqN7XivQJEx2ky7N4ViMWluh5sAzcGQnTKquMZ81oooe6jRKs3opJwylsOI1JYj1jLdRsFRoyv56QGI8nekG7A0gy_K6zD1EqHB0f9apIcAVc6dmjTOqogZff6xa95GznsPCR2QlVmjNrCqWkZziWjuoMgGhnNlPjhCwBle9SzPDucU9vQ-mdy710zyzVQBLu1nghO-M9OI6j_UcFu4CnBKl27dS_lgRCIZQRlYO_N6MNjTGUCO9l_dT7pZNWD_MDyghfWxrMytSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ber-X-_IeuF_lCBicGxEeiguz-1NSAL7Bpz8JDu3IC5ve5O3UytK3DO2m3IoPTNjayswGL7hbmMPj0ILyJji6ZLO8dGLCHq6SplJS3oNasppnliTY65pJNl6-33bMw8Fn3W_jwTjUNs8SAdtolLmuJ3CLz4r8lWjCuauPCwyZ7qlDhYIzu99j6nQufyOzkpg77LR7N3IqXBL7bkWP9ly33M0QKd-RK2QpvS-tJbkhPqY_K2SGxS_QcUxbWW-u0ICnEvc6aG5Wx-1RAE8At2IavOnHIZRsfXUASNhKN95dIrSquV5FYFGlaE1mxRs3FCjg7yr6lTjlgF5Jx1kvlHDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgyUBEuIV7yvqbU6E3iT2-TgwmW8g8IZ-XjR7DZexCdJB95vE0X_dduo4Ao4Wj6CwSWVjRnHXCIxv4_ZKQjwhPJv9ge4ifkGTMQJQI4Zpuvnm5Y5UrFn9wlHbwgpYX_yOlNov_Iu1Bwa4nayos79BdZsMP4pZUv9ehAXnXTevwCj8s9mLtnSwkmdNUd0NPNo2bycQ-S5K0DuG2AtyhuXoAm-rS_vUzaFs9F0ZuwMWYCC_N_n2CO_4Hlpc6EWGAqiwsoLOh-W88KAqG1vTRf9LVrKmj2Ntj80AXtAIMFlwRboPqp2_0u0GKgFXs2R8VJrLcNRrmBcXDFlrUdnq8EOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urMmkFDAWzmSRZeulkiEmcXiUKAm3RNwb6TUDp_RbiUQyTWIKNUMo1MQ4MNWmbGTItI07zh6A3asFMOmeAJWWN8Hhre2qSOs-f17MU1vlC_itGme1PmXObrEHAcAXYq7qGW2qlw0GlUf3PTfjcS6qHt5_FmY8mJFRhF4BIhXSxFhOoWACSzFr06H8k08Q-KUgLANko1_jlJArgpldOhu2rzYhC4yB7UYSQ3rNbjwc1VUPV8GVXqnJeW86nznmDCS2lEjQ_eKJnasCBJ14x_h2zSJ3NPN53sRyoCcC1FBft00iUye1Z3cAsQjLXurEdFr13U9hnhvDCu5c0ebiGUo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFM038falhKeoD1ygaEKhx1B-g0wsRhEKoliSaB99eO9g2Q5bbzkkNe_o1P99kp1H4mPSe2p-hBkzQhJZ7GWsQw2ePWt5Ntd2kg8Le2-N_nDqLk5i9ffbLH9s14GXarcami0G-5Fqz8u-Z3AnauRHc-dsFuEu1vpzho9MC2wxCFxGKQSir8EhK9pF074oO5tS8iHDaUphX1orXunkf-pmjYrXU-8UcCyrOVaiCuZ2jbVVGb5j5hzp6lqmHbJblqL19hN24Doaha006TJqNl6K2s6ooVG_Sk2hy4GqMtqwaegSKaP0h0kUBDBI2Yan8YDx7RJ5XJwZSSm2YsBTt95yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHawKvITpp_dobTMoKtLmjJUnNWSfIVLdURVKhv2tsw5Ix8B5h1KtDB2p4NZXviFGTYoUvxsKJP_H2wX82-d6qRYkTXlNYegJ09j6esllaSf6QE1g87TcAPVRrLkkCGmj5Wbvc5qfLfanPq9yZc430lDEl__OfQ1Hr_WiXI218i20MwNTPav8aU9YwN1JKhEA92EOLYkhOI9A3tfvpWgZA9Ph5vA24W_q0qP69ZtMEZx-EjlIBBoSiJ0OnSg49pN5f_09mkm6DPIVdn0FFEUMnh0d9L3K5qjBDTSEp4WjIlLfXhEuF7r8grya-gNwOaOfQVIZAzEdPm5jWCJ7MYDhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Z99kFgXMVtZGqHhMObeRSfPSDISXAaEBAAs9oH26xjZENu2GCGkFZ3GlmvNQQ-0d2_VqElQp10BgQOYwIxXlJOthaZaSJ7E53axRnBsi9REK0FARTfz0VlqT9mpBEuXghdaMy0yhCMvOZgyiPs9iPwBC_6Jwq5DXl0qRANOkk4EAYh00UrnkJudiX858j2vVDE-uRXBnEpGmQ0gW1K08prjfu5SU2yKWCJyiagAzxvNNfFsIV5BXDen87FwcIr4YJ0HuKb7pG9QPyJNj9mVcMa3d8gBf-BZ2FpYwPrcl1tPOzsuuf6451uJuMZSnagBh0YfmS7EvcuWiPNvcMxiCRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Z99kFgXMVtZGqHhMObeRSfPSDISXAaEBAAs9oH26xjZENu2GCGkFZ3GlmvNQQ-0d2_VqElQp10BgQOYwIxXlJOthaZaSJ7E53axRnBsi9REK0FARTfz0VlqT9mpBEuXghdaMy0yhCMvOZgyiPs9iPwBC_6Jwq5DXl0qRANOkk4EAYh00UrnkJudiX858j2vVDE-uRXBnEpGmQ0gW1K08prjfu5SU2yKWCJyiagAzxvNNfFsIV5BXDen87FwcIr4YJ0HuKb7pG9QPyJNj9mVcMa3d8gBf-BZ2FpYwPrcl1tPOzsuuf6451uJuMZSnagBh0YfmS7EvcuWiPNvcMxiCRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

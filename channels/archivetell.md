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
<img src="https://cdn4.telesco.pe/file/UREB0kWH3yzcXfghDx41sjivdc5Sei60ZbrcDqnuAG1cXy_9tS5GbyKQUNXTcdQWnpscA2bnGDDB5kyZg_OYW5_KjcI5j8YMCQmXK6cVFC9xiGRO1HYeL_xOPiJ3_VPvaadXMrO6VGIbG6YeMiEpf_ZAKEh4aJiKQWMcvkYilEOYsDJ_TUMHI0XpfOpadh9545SRo4iy05gkTx8ZnBqViPPvzpV3Hv2Y5Mgt7Fskzp9dhdMmfAzIaS8Maw0NzGEQtoH_suy618pMZQ58dK76jf8aW9ofe2tO10ftjS2VitbfwutkK4-eb2O9rcaQXXzokufL482SZoOgkPb1EftxGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 03:51:05</div>
<hr>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiPNw9ZDyxyZQFh3gcDAzfuSG3ilahEFtpFBlduFap9UQtzs2Wf4UjL9YApw-ZBVRZD2_jp1-4LsFB6eZg9VDDrz8SoT7B3DM5tlHoKAayh7j5Oft7qc-iq0zmMSLI_Ye2AOWvnJ-lz8kHdRwnegqvbSOmY83kmp8wGkZ6CFwsHcStetD-BjKnVMHYQ4UMQYculFaiINDxt_DCtin6MvljXh2FHyzqmXBuNv8a6_MZ3PZQn3genfeQyE_ejevDjB-tL90uTErghjIsNHWCIfRvxc6crsGbC78n8ktr2UFRoT_PQ207U_RQnJ443r1cpY2gO4FE-dPtjG2XxZWq9Y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔗
📥
دانلودیار؛ ربات تلگرامی دانلود از اینستاگرام و یوتیوب
فقط لینک پست، ریلز، Shorts یا ویدیوی یوتیوب رو بفرست و دانلودش کن
✅
🔹
دانلود پست و ریلز اینستاگرام
🔹
دانلود پست‌های چنداسلایدی
🔹
دانلود ویدیو و Shorts یوتیوب
🔹
انتخاب کیفیت دانلود
🔹
ساده، سریع و بدون دردسر
همین الان امتحانش کن
👇
@DownloadYaarBot</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlUixlPTecccISB6YiKK-aBcc1rGGAUeNgsi1zpVRIOTV6Ulb7CabEshNk0dnTK4DBWUq5DmCOF2ayshYqRneb2hR7pEjfqxELuj0pVveZ44ZKylAKaJkPA_uBX4nKTWfRzKZnBkmPO_xpgAJAAijoLoukYLluDgVRb31J9q0MG9EjcO5Q2EM2sgNqejLladkyHWvCh3ySw5HdAqTcKlMZqZYj24mHJmn8c1wwhY6q_50QjTQfgAiL9xF41ylq_8FwuaMIPDNa69m2IVJp7t73TOpRrfR9rDwaOkjeMSlaie5sMC4j8thKKmi29NUFyNuIFcQNet1ThuOwck9gzsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivJpf7zj5w-Zy5c9b_aFKPfw8jwOD8b48CpvkABR4ABZ8SpBXTM5c7kWOHRkvd5XnexUweP7eIQD4-74JupGmdz3dbbP1q-vHfOmKIYHOG95G79IC3Oj--Dar-1q6pzh0jR2tB9ro5PYmJH-6K_uwC7PQeo64b-rTOhf20ckQWLv4ftKP83IuoMBGXF42V55-UX4ywOtIuulf9kwBzKHBtWCY6qOK6bQOifETzOcGsKdx6XIlBDA6VjpNmXWhNUbgLnHI9WNJikZrcICnMl2QQB7ba96lAYHCIHv8zH52AnUJ3_yjvlIaYuJSu8M0dLF0aOPgKxe0RP5vc66aj0LKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuFpV3Nh56Zb9NsiPWYAMfTo8Hctsh5j9fumWTwCT-lDU9pmvVgS7yDekPhWNqZKAwbyb35FEczxhvCRhggp6uwKaOUF_e8E9CJPHGdHXnBKnaCg1OPJJyae78xzI1IB4pMu0YOZy23wTxGRu9OcmOc6Zj3ftXOSrpVwHPvgeBc9yzcgduwC76EcNJhFZ0IGnaIt9pNhSwC3WRWhnd_Wpe_WBp54MAAiNCy6h93FjZS610lMtAFOvgJ64a_LPGuGJrt6UrSeBvbM_fabI9RhjY1bwZw0NpNiQOFS8aJiK_1gQaf-vJ9dmMruP6MY59EIJgPirZvwkSzgXsU5rN7i4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e59uHivCjbs-67TQOEufjJJEoHqOpuIGJ_33-BHB5rYUItLHAf_tCrTfdgqYf6VMQVI0cYQTqbyWxegxnjm1eSt3XTeHJVSYhbLASbqopmvAPKSS7yu-NTNPf0Jk8Fsl_BTjO8YCw0PGZE9Hlhv5g7zYkvVsH8k2ElHuQbFVxKKE6lGy6AKWmu7tcNE_Duix-GCnvYB7ks5CTcadbtu7Y2GyDbGZ5-gZSaOWSMvT7mCASfAfIaoc9Q6HpodpkhtSB3oXhYwA7wXZ70DqrfR7TGuE66z-McYjQxEqlNPtnZGj1DRUylZVayi6AggdUF8GhLX-AjpV82JWJgvwD-mokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgIU3ZsgKNnzcZlgPU0e8-lLoeTyf4kxrXh8dGDscjOyRKeur8MSjekRAM4k58sUoXp7WDJYfgVFYDgL6QX1tTU24ARZyhJqfFoNpgXxuKWqHBEsb1TCuIbLrIS-doKpf-vnwo9pZbNCO0gAWqYu6NgdO54X34LXzw-d2YQo5zLUcTHX4obDbPknOqODSxCKC-oiAOYiAfY6okMHdDlGRFhWDAkYeIbHYnVtrJ7Ovm696NVjPnVLV0PC-VV9wYNTUWO7TjnNjx1GCMoSjmkKVypwj6GkGBAqelVuY1Q2F6IYFLZECitmGfxM-3jGHfyRAgAhCR9AZUshG_dWb23imw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnUh2-l0kd5xFU4DyR_kGelZGW9mGdy7FL5G4h8BFmCmHbrgvkXuJhMvxEPp00a8NR0XjDviboV4EbD8s8yqSZXS0Fjt9bqPj6KE8CNtseIw1UoEwHT06WU-0lxpUo_hd_oWORMYjziqwbGFEF3T04QdT_mwjs-cqRJZiOepoQWOs44bxGIaDPtU_wquAs_uTwAUYhz1RqpAWJsMujMzkiYYrUbm3HRYVqeD8roUKaSuj7F4Hc1D80v1USsVcX-2EWteFGvuSn6YQ8Y_ZfPRByBDyuHBZYr3dHaN5FfHjseQQ5Crppqi3cpoGlBg5uxYTaClSpuSVAOEjOXp2KYCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnmHayInO3wLZfbCqYzxK2iVsOUIu7rNH73414q4xhEGmxXy7TAqUxvqZZvAptUIzw-fP9UA9-99_XTaENeRVGca_veS3jHVCRBticrbMp_bHmaOTNX6xzrqBmFh0C3rHQZxwN1rLLz3I-wGa8Euf1ZCU1gJkMHXgL6Qtm9AI50m9c_mK_3SaJ_QctKXkzG7aJMcJrTLdG8acoDInxe94BN8r_RqW9Gf-X00FPtZmNrAI1xZVIkj5n7wY_H2DoW4_kZERpIvBvSr1xvIteuLGSGvnKzm0PMTufpwWJ7DnaIZtPAfi0p5pDTDMWZO2vmbEnK91BHAzx5BCzlQENNqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-pK_vQbdKXZEesCqcl5OSC5xksF0EMIOTt1oCflhhKNO0OkNdGkxlLmkcIFjpY3HAvpmHLkcy47NIOKrHzRYPwFPdjwCUcQ6AP40GPthjPybSvwxZj4kmu_9KNQaYX1YtsJ7vxRW4I0D2AZrV7PU2TJvg7-qkHH4TsuluEeQWoTHbTjoE0G9LN6AwPdtUvZ29lmpr8b0tQrorgw34u2jRhR_XBKvsQmyP3pj3M43tC393XBrIcqFbwyCOzu8x3QB2eqQBpFKFmoooku65xrcT3iFTJHaIF7Dko_ZslR1yLQ0mMYGz_wEoaKfFrBcAH9YbDl-ifMIPJZvIJCcXjMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJz7CLTr6dDFwELqVdwxzzowfxlXiHZc-6FTnrrLLpL6R7xYdkhO3yl5xfJ28gnj4ORgUUmo10MTjVADQNR3M03JCoAHxMAZSAawiIwx1SYaK0UANiRD0z8TyeRNBAleJxHXFeGJ5TcJAAMSjWJk-hZE195OJIp0idNFidh3fO5zxui4IjtbmQOFe-mA1SAhxPoaAzZ-BFSibb5fTE03r9VMg8WR_Qb5tVYJXIUxR6851QyY14FyoWdmM0B9dI-0snqXqpgG-Ef5WfXCvXo7Ue4aAEU7n_SSVlbQHdTxAJug9aHjpT_Qcy3_oUKdROKAbQiN0eO3hJQlQpc9UIg3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw_O_mtXbwJQ9Lu69FxU3kMebHh-k3StC1Fx2kVDtSZv7TysR3rWTyPGLsyZ-Ata56jQrPGSn7QM0ypPV8cpVkaHpIdDR85gY8IW_fHLQWskuRGxzZR5aPzyNqRMh4_OwJXsNhf0sRxSkibmkQOAMFkYPSQJQJ2ugOsbc2c6e1jgQjLGXqN6LW-l_zEji7bhEAg2gPaHIKToDgfw8eb-Ajr88n1WPEPxvxkJcdIeI1G_nPUBjpauyLT5LcHWS7BY4LnIdAUoAhztcqm_Ln6Z8H7v7cjLUOfw3dihJWZdGWBxc5mvqNYHUHT5ehQfxWLr3jaPnxJ7bRg306iK4KXQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flvAeiLud2qBxH__tfsAMI4h4pI6B1WeoJLyHmRqs2l0gsiXQXxIqSsMPJvo1hikyWP8dFqTwwV2b37r0pQkS8BcOAACVceeEE1yQdDoY_oLcu97PxdXaIashLOwHN-GUEyMMi7AMudhHe1GJQ5XtV8mI_lYhJdkIi7UD26SSbaH2NTJU-HelsdFCca_cSbKDAXDS1TXrHOU78SKKhFSukoUjam2CKdL9tvIsQKsDBwCQix-4r-JH62zQNsFzX0wcKNtj0_oU1rGHArp7E_E_sByMmU8F4Oc2CyZAXHkcg4Mc7E9zrx9ytEvOtQzhyFPCYccqacCyv6oIt1BVEJU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iebh8NIdxc4K0CyqXS2a8s5VSiRVNmaJE1YcknOI_JjK1MgGz4qgMJDLQj6frxI_kJ6p0HthcVVCAC7B5a2l7lAG6FeeIHxrW7Gn94fXcSt_Sh_NMSmez3rahnhOx8TiDc9tVJ9sVAW1MwjGLZr7SS_ZfS1jw4REwWpHoxlNwXIs1xZkGm6BneP2mpmtHVRo5zvHtCjMHo6ALk94hbP83VL-faJoopMp1UHlYbT_gAXvTBnhizS9mnMMRbxH5jyGNArIf5xI4fHPeQstxeWOSw3b1_Fp0ASYv6xZfM35TsYvY_tsgF8oCsvWfR_mBLp-0COkhvjjNOQL31fny45o7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8xbrDai3qNBtduJVxYnHios_-pauOpdFstyEOxh_RYLykJiBI2u7tbU-CPBNAoV6LzB8qB91bT37cAWYcJBPQ_32VyAnzVzKZhGSPXXWKlf9Q2Hki_XPE25ybzD_2czQ-tb-jxSwwyPw_DUTuzsvVoLmrBNPkh08eoYBlS0NmxhaPBvOi5IgFwvKRtIQDs_xXbWFiJygCyrqaK1kk8fJRIhmfxI5iCu0gKEJMMNSfgQGHDryRpIF8yDKT6uwBNc7G9tnFbg4i9XKHHaQJ117M-G7MMBevFFPaLlH0yUEO-syrKudVx1_r8XEXNM2VTN3xyTy96GT6v1SWrj7x1vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=M_BT_2NgqYaN1LnETUE0WsOOxv2Sez-Uxy0J6hqBnKyfOFIPJZaXRpor_fpYLC5b0_ZzWW-EGnhm_abICZJkFHh-Tu2DJFYqSUSBhaiD89cMIQ8Rqpieb-9aTlTSUQJN82CB6zRGCy1Zl0P7R5mkyFA_AMZON6UKNEZ54CKOPNbk8ZUr1IhcnES_85oGsV_GHP9dZZa6aA_hQ7ThzQt6Qt0hmMJMaz6zcuT4FoXOqmVZ11UgmSICKoQEwhViysutIB1gAyoS8l9umw4MSiSfy_U4OZCi5vZeYQdYz3pCDBPp4lGgsx-HdUDEVXLTS-Y4gOGDCJVA6tHp8hwO8g4vLiWv0AtrSPMVnRnX-uYLM9fTHJArED9s5RzMSKjqL0FjOUp98PzzIIsNQC-H1SYo5Mnrgwb-DziBXih6CEc_YlfCqG9Rcy9jCDtovOBxlEQA9ahcF-0btE6k74IUkfMAZpUO782C7Dx5ZJy3uKkfjEbpqG03uBksVwhwdzeL60J6xsMAVche_rgOeuX2cvIrYjU1ZwBIpZtNNgF_OmkJG5mrTZs_zSuKqLSkX4_BS1ugG5Ax3N0Ghmks2MyScLpgxQFAK6J6tFseua2cTc6gz_kxCWOBpjmFqUdYMRowlFAQESjS6YJpcjCV7z81-kO7Bp--Pgw7vEqDi9zji0RXzmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=M_BT_2NgqYaN1LnETUE0WsOOxv2Sez-Uxy0J6hqBnKyfOFIPJZaXRpor_fpYLC5b0_ZzWW-EGnhm_abICZJkFHh-Tu2DJFYqSUSBhaiD89cMIQ8Rqpieb-9aTlTSUQJN82CB6zRGCy1Zl0P7R5mkyFA_AMZON6UKNEZ54CKOPNbk8ZUr1IhcnES_85oGsV_GHP9dZZa6aA_hQ7ThzQt6Qt0hmMJMaz6zcuT4FoXOqmVZ11UgmSICKoQEwhViysutIB1gAyoS8l9umw4MSiSfy_U4OZCi5vZeYQdYz3pCDBPp4lGgsx-HdUDEVXLTS-Y4gOGDCJVA6tHp8hwO8g4vLiWv0AtrSPMVnRnX-uYLM9fTHJArED9s5RzMSKjqL0FjOUp98PzzIIsNQC-H1SYo5Mnrgwb-DziBXih6CEc_YlfCqG9Rcy9jCDtovOBxlEQA9ahcF-0btE6k74IUkfMAZpUO782C7Dx5ZJy3uKkfjEbpqG03uBksVwhwdzeL60J6xsMAVche_rgOeuX2cvIrYjU1ZwBIpZtNNgF_OmkJG5mrTZs_zSuKqLSkX4_BS1ugG5Ax3N0Ghmks2MyScLpgxQFAK6J6tFseua2cTc6gz_kxCWOBpjmFqUdYMRowlFAQESjS6YJpcjCV7z81-kO7Bp--Pgw7vEqDi9zji0RXzmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrdjhY1gk4xQaO_OhyFOqomqFsuR8kt1noe-blQhOVmwxb8yyeHEBd-zMthl6NlYdeu2hDg-Ar5PjxANMqhOqvQTvCulrlcC1A7UoaocYTmg8B_Y4CfijEvwJ0knZypliJKm2UUz2IBKrO20wNq4E4vi9frrV0f3CHsuYFUzVab-TI97tp7RpV-5Z39YKF32h-XhlfhGeoX6tghTBhZtFIeb0jAsgv9W2aFEolr3N6upSQ2q0EwsJjh-vNtUroSRsjWKI9iGjXx4pNFVRUemqUmFnGK9_NPfVV7tcX2GOiUHaNAIHDRtJERlVd0cQg_UQoBj58EkRiYdJKe5RvziPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glZ5QOzDUOykl8mtEEfohL25fcFXyVFUgzSby0wMW25Flh7vbfA4JTmebw6IpW_s6PqUP1C61sjeQvW8h2Sv5JavMZ4P_jzTYJcFSxdAURa5k5-PCxHBea-cAwckD_zqMdcJP85ekF1wpQWmsqQ8FVikYxnFk5K2DjsAWO65sKRARXylevM3kTnY5RR6x-WxXs4VfH_LruDpr8erbWJZCOeGduUPZSN9n52NnZwmoMSd-auDewJY3VdZ7GjEtMmkQtHoxrMwlYXPtSPqQ_wCCTbL7u0EcxeaoPkx07EXYwfXZgR55oW9gEBmsZNJIhVNWJlIPt-fbDMm-I7ZceExQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTGbQUN4VzBBQS55KDeBd0KN3HTZlzz7tFJzA5fMgsAizJIO_TiJibBiVU5E6gmyarznLF0AlYBdaE-PnSK1PgLh9Q_rtwv45ZDyXzPtgdzbZBCUUI0PKG07-Pqw0D9tIqGu-xYbX8v7y-Bv2uT8lf9HVqPDybajzd0dx41py66reY-M2Kq4GM6RI_ibu7_9IgjopJhwgqiDpmNVXyZp7h-kC-chAzAYqBBKa0h-zE9ZvXNva039JuzHe-5AD8AbxLrTTf5CH4_RBJMY5PC-cOd5h3ivYrxQJPzs2iNlA88qAqorNnTxpdRe6oV13rM2bL1EfQtzKrjCmBdOVkt0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwxeek7ZB5TY8f58tnKcbnk_MV0i2z7VrolJYrT0AVBLtJfsWF4TXc-XSlDmCrdeV-agZhpcvtA1w8ET3ExeCj397_4kzr20QBBTnf1B08Hzm9tZNi8w6DhMG-kf7mdWKnIeXmwfBqUMmbe5VhZPXN83waP_3284lZnHGXp4rjOb2CES6P4Muh1YEFIR_EvwjN228NeJdqVD3JNcmgV9slkjR9W5ZgSC46J3tudzaMpz3xSlUu232a0zE7aEdwBtpNY6UeKLu_jfk2RXGNGWx_tPzonBEx357NQ5rKz3rPUtWrEE1ubdPAAFwfcTmO2iZcxylteXteWZ2p2YKkxOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhQ95NUxT0LuWK_bVih6xluSqls6s2ZMTr7sPKeOuEiGqfbIvnQONZaOrhMR5OdLCVKIakOSmXJvkaKhEQxYO5JbyfiO0UIkUiiM5ePiVEgMzcHZvXgy4H7WhcSpk1oqI08JogmPCgRDqHzvW8rV6jjxAL9ODyOStOcgKL_ibyUZ_wP8TxnmS3RGT1ezBpvMDu5Yo6zsD5aOcKzwmLsc6m0_6AScjlCwxXJd2gvcK8Y9NUHkOU3mpMtLMYcD2JFgjYGIJsC7mim0oZOnFmRbB0yn6-ErT9YOUlvLbYn_ajt8_UY7wiN9-rYdkYJosyRlnHLs9wqYpx8EeuT2R7bAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msreV4BTq5U4JQfqXTWITU9hC-I26uHYnn7D0DFjw-Rfy9HfuWeTUkkw4jesomSNz17TLhPPLjQa11AVMQjTgTdtknFKTUylt7eAPg97NJ3tEERyoK09O_cCWr9VOh-j16K1eRf2d5cOcha6uVrR1eGymd127m7Uc6_AJAqf9JzlPemmlJFoSrKeid77CLUmuw9uM2MhLSFV497pH6HNduvPq23Lp6buC2KdK176G4KMTEkzyHhmVLpEqOdwCeZsR15azL0tJXi_Y2VCVqK2l6cJnyErhgPCsz-IeEk0p2sqc_L3du3-rEwoy8Zq_aUGULhbqnszCyLFYIKaU-4PdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_GB-ENGaYwcD0yJIIOZUXgzW6yNqb_XFi_4y1NsZIxJz1AGLvfHxRX3uZ3F-xBSmBOX3rIgIxDGgsKrI8-7Ihgu-i342OeFgwOFKOlElZG_5cX8kFoyS8TQYpi05e7VuYCLqxikY6SKEUDpGfyYl-LFdY_d412Sd3dSYCGe2W6aU_Lz1ssdleo40SMIqIKblZlAt9naMCM4u_OhN_wqWclEsvGFnaWS7Lz9WudT0M7-Rhgg2Ak4fvJmrEO7kBQrtaicK9gxk8uFZVbxjrtpUXIoxCclnhp8ORXHtIIWgE9b6MORp_uZA71waEJUTQbbFx68TXdYZ13pYp9v84CODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrCjY754m55ezRqgREpib_Pp122-ZvAcg8jI65s-kkRWekL00LdJioeajSP2cwR44vaadd-qEXrXD24jJiotjIs54bw-SVxgadQzqL1KFoETo38jJ4lC-VzUkhbUNV-ibHswvddoeCfDecFtJfay2kA3AKwcM5t7rc6tZBKhRshsiysF5SjQFbaWqR3UyxgvTVy6_SDi-w4SwjpWjh6cvZ6B06iVaQWzReZDISX19KpHK7Jq5FfaB0nD0IMjI7f--qDP3vjG94ZghRbuicl5QIzpMP0CmDlHkuxADZNH2JcHR142e2Pikkwl2oXOXS37w7tU78J1kpeTku9iE5Fw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFO-fBj6TIoEU3z5G4CARqceQacI3Tm9iUhyc9506rmTUqUBmwUyyB7tGaSLIwnc8pIpKta1v348L_tth9paM9I1-3fMiymiVGQTzSkXRqa5h5Fh2Qni5qefEAZUqAPJmlIlvpS_--mMrbSqeYsxIWhZ8a_MCfle9QOkQixpIgyHh7M0ey23i7f_zTg5CD6inr_6I-pCxKA_JOV579WHblSk0zfSMSiBiyPnLEXCnKD-Ij8SN255ORUJ0ulGM0oBfhztwFoJngAeuZxGlxL2sKPfGA1GEQwp3S_7RR5R7GDgwHDXK27P2_fSEluS6PPAj2v_2zgdpHOQFVC_4qzFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxwjADny4qhXq1yXmigfah8rnsvCSYlZHbD7Um5ctF5hbYpYfANbmIT-5YIkmEwunvIfZ81hyHp9q_G3ThcIRbqR0p0JGaQknckiHK_9pj7uSfmYSEYNLwTRTUB3L4E8Bn-Uc2pJ0_X2o62eTN4t7EyTH21EZAlzD9SkDGFd2EeMnj2j_IR6OwEfsmb00kh6CGG9sy09Wmx1voaMgthHhyU3yCFQMu9gX0gm5harRUkgOdYkhBlSoUPghm3WzuM9YlSvX4cA0LsULi6KapbEjgUwpwHJt6YgAJjmt1v8INlc-TBsxtTmeOZd222U6n5iX7uOhszqfnq-2Y1rEqSjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=j22R7KbXSOdB_-f-x96dLGwtk82BHre_92TiHTBquE_gAZXS75Qdv2cAHncjZyZ5wKA_rocj2HS3fICCentnWDaJxtVdy0yfFQWQLN51x-ZqtVdvQ43pv0QxH5sTaVrAop2sDFZr3QZxM3RUIbtKJ7n_ebkp6vB75DfGWpj30S3JaqVzyOAedelpQ8KfsdCwIiNa1f4Zp38KhlGuNKEWTI9IwjQNrTr-AZKXGyxSq0tUy1KEFgK5HMc6OwDbqgaSrag5hcDl6HIG0aeK9WSoekleOwUndTSy8O6fYlr_Rr-83kK9afv6OmkJAEV36Vc8H8Woyhp2XiRCL4kSUas-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=j22R7KbXSOdB_-f-x96dLGwtk82BHre_92TiHTBquE_gAZXS75Qdv2cAHncjZyZ5wKA_rocj2HS3fICCentnWDaJxtVdy0yfFQWQLN51x-ZqtVdvQ43pv0QxH5sTaVrAop2sDFZr3QZxM3RUIbtKJ7n_ebkp6vB75DfGWpj30S3JaqVzyOAedelpQ8KfsdCwIiNa1f4Zp38KhlGuNKEWTI9IwjQNrTr-AZKXGyxSq0tUy1KEFgK5HMc6OwDbqgaSrag5hcDl6HIG0aeK9WSoekleOwUndTSy8O6fYlr_Rr-83kK9afv6OmkJAEV36Vc8H8Woyhp2XiRCL4kSUas-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=HaeVi34Nw9pVuWvVWJTe35oCK8wxyq9oI_z18rWtZCGOsMrYHTOx8z1VXHoF73j273iYuvlwks0IGG76wZ_3DBwvZYU8IBgsjtLP7u-27efcVMHI9_k5E8d2Of2NCoz5-Hw2b09N0-F1KK_mnNuuvkBFl3kbyp5vyPD0Sf89SGbW1QFao5ws5G4a7l2ndG3nrKwBez2A35fqAraqZ8-E10BVKz0vPGAArBqHTK-TPiAvjjCci3aL440Vm58CEazv8WFCSHrw4SyZkcqL_qj99b8yxcsYcQzCtbpYaC-wPxjH2RbtFYDxmhefKjUFIbbJUU-woQzhMYRCd7uFZUgmBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=HaeVi34Nw9pVuWvVWJTe35oCK8wxyq9oI_z18rWtZCGOsMrYHTOx8z1VXHoF73j273iYuvlwks0IGG76wZ_3DBwvZYU8IBgsjtLP7u-27efcVMHI9_k5E8d2Of2NCoz5-Hw2b09N0-F1KK_mnNuuvkBFl3kbyp5vyPD0Sf89SGbW1QFao5ws5G4a7l2ndG3nrKwBez2A35fqAraqZ8-E10BVKz0vPGAArBqHTK-TPiAvjjCci3aL440Vm58CEazv8WFCSHrw4SyZkcqL_qj99b8yxcsYcQzCtbpYaC-wPxjH2RbtFYDxmhefKjUFIbbJUU-woQzhMYRCd7uFZUgmBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-Z36HDfXEDHqHYPcAmGO2KaxLjR3vYRrU8Yaw9mpIwoIBFmdYkK9MNjSCBaPRArPGQFuvdNfpcZpEjvVWQBf7dHHg2Tk4E630ZbKdXgRJj88qglLSnJhxPCX-S1QJ8smAhLVsIVRVCdRstTA-dI11G1kLgKunQmASWudI3iQBRvzi2vk8pdnK0EkH6swpPxV7gopT54zvFJaZEY4PjIpzdWrDA9djD68R7NV-uWcYGHldSW19X80uqXzhrtnQBLBX9DW-pRjXRytgy7-sH8jqA6MyKW445UbjzfpJsxR3z77wiomGHPuNCbr1PXLKvp8eFjmQ_m4tScjti89_WKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2GUz9Hvc-3EmhxVHG7fWO8g1-yI9-3OkyJoeHsSqzKTZ4h5S29PcAItjdj7fDuTLaL7Zm1tsKxNZyW0hd_3N6BwLN0oLNkPf9j8x4sX5cb-3EJRidBoZdvCThPppwKF895_aqtBCzsMttx3-8cpjOTBlr8-4_-xSx2zOwoqdO2bnvNZMWdQSqfVYPHlmWdDix8g3whieeG0FhzZ6guvX42_md3USXO4MysTp-9ABu3i-z4YgGYw6kGZ9c9gyfGa9QZXqHET3seAPmISBSnEOmarV18rCvN7b8Jm6bK3UTmt6H5xPvdHhbeupeZUa4eg5DJgGyU_TRSIE2U-vZAAC3Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2GUz9Hvc-3EmhxVHG7fWO8g1-yI9-3OkyJoeHsSqzKTZ4h5S29PcAItjdj7fDuTLaL7Zm1tsKxNZyW0hd_3N6BwLN0oLNkPf9j8x4sX5cb-3EJRidBoZdvCThPppwKF895_aqtBCzsMttx3-8cpjOTBlr8-4_-xSx2zOwoqdO2bnvNZMWdQSqfVYPHlmWdDix8g3whieeG0FhzZ6guvX42_md3USXO4MysTp-9ABu3i-z4YgGYw6kGZ9c9gyfGa9QZXqHET3seAPmISBSnEOmarV18rCvN7b8Jm6bK3UTmt6H5xPvdHhbeupeZUa4eg5DJgGyU_TRSIE2U-vZAAC3Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td07LVOYOpAwyIvKBG4OaQ8n2a10gCfdQ3bkPoOuPaBFWgsBO-87a-zXuMx8cfQMqYI3zNAChantVPPbn2KYttbpmkXbwt4QYbMtCHmykz9DKuf4Pi34PhTMq9TXyaT5bgUsOcldk74fWKbHePOjM2GhrqzexQz0UM72DowmnUBWmyVpolglxwa9d39-aKwbxXLQBObnvyGqP49x_1C_tjxIgXh4Xfm9SXzP0oqCY-S_cPkWvNu7m7B6YlrLlHD6V7tokJjQ_SnaYSe0UW5se_-NEyditsztA-kdOM3wHAtIiI8eP91PrtEWp0MDjYILgsTneJSX2vs0-NTAu4O2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K16jah0S0sFfubAYjzp7KHm3zUjZ02PrkUnGdy_cyoHmjakh56soFTfQXqD9ntULyDInIDMS_2soie2Pq4nSWX2H7N5wW3q21o5HJOo07zUOqDqUYW23oMmxinKQ51gHp6TZqDSw6JdIiyFxm0rlMZ3MgaptFXkI-EJCm26ASZkMFmQBvkQNV8m0Ah3tY4tHODI7kMNSPArHzYtr061BRJFreOfe5-vqc1gnRn_a6ueb2-ah2qQoUCyXxu_nr9v6sBBk43X1QL-Ay85LFTMDQu_b01Mun9S2DjYB-QlztGubZQjY_0kpk-EzV3H2t-ADrSromQ3RmWGmuDGVv-um_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO3x-oRcsqvmVP5fAS2gtmzljKwWNOjLBX-zhpuB4FQWdhJDOmwJROIN7zviRh5BGgSDFw4BoCgzw2ctoeAOCH-NTOiDTYTVbDwft7Q3qCockSgNXcqA4s9jdKAG9d5KVvEPoU8krMoVJoYisGDGPlfJtkwRxLxMmB3gDOR3a80c3BU5FZdBOheYW1wQJONKAfZuA8Y7Q9jPNNjFsOBTPfXy7YXbVp0zoNUwQz0KIGYk5abXloYwPodBK3UHLHhGrFGE5mWHw5gYvYcECrTYfa5WM1cJ6eIEYrjYFPqsbAJLmFaPN8HDdzJrZv5gQmFzUcKs2CBH5zLVxBxeu6QHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8OvpepVgZgMrjx4XbP6eMzqFVo5USx8f95hUCqpWEN1i5XS8q2dv2a7uEqousNomMN8e6Ws9J0c_Yozpqr_SdDDNfXMjZ7Nu1fGYm0x_fDs4md-t1plsBD0TUahJngQszUNzQvVt5Fy3Hc0YPITlP5JYQPkO4sizE-joDF6FEFAjH2_iRTKTkp5nFDRKzSAKccTbVGKbq-OXAA9ThnFWGffNKy_bed6qGzxMz4z-IfGnKi3MC7X2h0eMhHn2YLc3kqKIxf8WIs7viXmdfuorTwJPBGUtEWp-L9kN4dX3c8kJKi0da3wNKY2u-m1mycbnPP__U-Zb7QAPa_UpHTxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf7WjNNzgusCxoCdSFq1l8cEeisuaf2UYx7Z3MieFoVhKsepqRmT1RvlCbu70uM_VYr3JW-ryqkq9iDRNQVwTsa5EAOac4L_SCLUb3RpOH4Iyk0wIaewf7ONAC-T4a5XcVPmyZ8Ei7SnyCg4r2so3tbu6R4aUFIaXH86p7LY9KKKzmpUlnF95CS3vyqVVo_oucPjULbKaWKfnKFk4ErYCussKlzS_7we-C1J9zf5jzToaFQ70N-e0xtkbhI5gnKInpErOsfJslkpgbr-Q1QcSgEB_6Ua2aqFPFb0LTPIJAtYgGhWJhf3GmDOyQk3WgPwNKHjg-lLW8QutRe3KX0ZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNCDFkZGd6ctir-l7N0FDt1q8svIUAe6qnBJ3qiQgyyk_fjCFwlUWwPVpkoLNrzDDvvo-yzO07LbWML6dlTKICQKD1lPr42d7nYQWckxbgwB7f0zlNLnbS3AiamRa1bRq7nNw5xhIxiF_ejKWa8auEyLsYGNZFZMXtwm_YE5Va_jmkO6IQvnECGk0VI1O0pSeMglWASt7SPpX6JbpHD5kRuVQ02EihDy2TnV_9Wn71gY-gAFJ0-xNeCK0N9zb51OuNBsAeFPbasjOOHiuXkX04JO7rtvV3_o1URmmBlV-N3ud-yRLiW4d3wl12szuefARptebs2FpLVdQhQk26qXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS_QVlxgPjMCRaudiGl8-0hmFE2AfsqTTylTyfVpzv2hFOUNy6AWgyKGDiSwfGKUHTgCg3urHFkhVciVATCJNx4OJknEFqSQP4cjefWkVIk4GU47IXmBUiz5-NpORQgYIOOUUh2izWXy2oo4Rngs0kA38yr76C1lCT6bLCubhE7oJjLoii6V-AQQX1EVX0jo9mjFriBP2fnBcHNUydtj6dkvkXxAGNeQ-Y2guCvhsnfSsWl-9pFyk2bpYIxQTxcwneQrSifygn7gpaULv5NoJxCZQkvJ01Ct2WV-KK41di7_hqp3LuGhiKZjUy8lZ4E_LA3u-57boQUWFroVKfOmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB6sHSV_ZUTp_1InPbSboRuugvDUmar_H3rFL3_nQWScNggxwusDPMsDeortkFzz0gtx_kCNeGN9t-OR0vBoLzWCcV6noP4zK6SrKst3h2v0jM8uzibSXYsojI23mEc8pd9ADuE6-oZrh8PZdpMe6OYAyC9yMDxPpjCMvw88pndI-BTmRAtu41YV9rLlXtNUQyE918GzEIBSYHc6kVecfKNlDT8_LI3VFX29u0vg-KcCIUsqxPf6dgc-A7dH-m45pnRTyqdohWn9kyJ-nTd-Hx66AsH9UAjcSCr9cTX8Y3nFZwd0HKK2B35b5XmgBaJxaCGlxZ0FhA1zB5IM-GRDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbcm5dDe32AGJ2xuxCF_7IYG1GgCxrM3CkCAauni_g1nfad0ps2LShyaOwdG9DMXjCzrPsqIXdNw3_OPi35YdjYuIONn_CBHk1sKAvPSL-cv_5_E62X_2lW9vZ_ulK5nHWonDqtD3op3fuM_tVbeWHiQeZ4X5fZQVQbBsrGPiMsdU4OjhvKMgLQtZlV0_NU1gIPPxACZhewRsFjzDlF2paNf6r32vDBESP5sh34Wexb0FtBnKNiwA1EERF1wBtHul5J2y2k-UIi8uj4G8AZpYVuKxSDVYiqsZQD2aK0N3WMdfA02cgw_SLG8V5fJT-Hivu_59uRYCuxbyfFRBZKQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhSb4sUTm_q7BLiso4CAtT_n2KXNAalTcYx8xBfiP1iftXdR8vPJ480mPYzxEXYj6UAIXOWBpOlH46lFCB67eP8f7ipeqeXAIgQqb4PIPXkNo1LDBIDbj5D0dRJUvCi2l4Fh1ukJ9uSb3eK9nYQf0jtEvoDAk9U3oDmd754awYixZxsHuqX_pWwI9wP_LF1mNI63l7r8VvYuhu8tNwSxDJ6tL8lb_ukeGtu_vup4N0nwZlU_376sADFtzx33BehifwDRHR_cCik_CDOXW0ivuWedrPCjAUKvRabati2EnJZK_op_GFrBuYVuyikc6YDLPFyx2jQFv7W-J9u2qAGZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVnnHJnahnpgfOWikPRvJbJN3gOKqBKOSG2rGmqqBoZKqhbq4bLSy6GbEeS5GLKKydbZcHg4E5YnB35tVzYouotxyyLREXteYkiKxWJBqTft0G7iDn5feA-9Asky6hitxpzZcBDaJMwVhXogBEpl5FJnAjp1pxYAKkBJ3Wh4o7IP4psGbbjvfJOQocWCrKm9Wi2V1c21NEwgR82EnxKo5yn579Rxgr4cxjkNJ0p1SElKu4NxwOkV5Qdl7h6W5lMG8-7AAX7veDMPG7ai1DQyM7_k49JijcMY9n5FvL86AB-QRH5z1DmVzuA3qpOkBLm9sgUzwDMma_MrmaQAqwblRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsOdQriv-WkwUMMMVxqhMFpNMb8LTq8UqcTPG-hTex8B5tk0GFgMiA-TCozcta7h056Z6B8mjfY_fOHf7p4FemOpvHJXycIwP-FiaxHIoFI0hEOurkVk_a_hB9ctRKYApk1-OlsizdBen9eKAdFsSrO_gtisazhIM6D2ARjj6aS2isimxqXEo7D6EgStzL0EkbGzEy2Nxd5SQ6NQA02xBQl8CdNkHoUlyNM1ZaFWyCGudj2X18eoYIt2yi2pI_TdlyQ99PfyNURdqOtJXcO1BhyZCxoBl_TrW7CwRHr7eQDOcG4-DHPYvnUoi-nCIgWGNpi8qY5a2PEDl__6p3Behg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKEJ1nMj9qs2VAK-JEbIdJzvXWPRBZLh-dv1S-WJUKeM4l3X1saHYC34n8PBa7CZFmt9p1MVlt-Z0wCM5KdvOp6JX1ZIOZRrJeEksofCc8cvB9VN6LAM_-Mvp0MlMqG9OVpo6r_8NYdTsbUUfX3v5UhPXtN4OI1xpypQOLfHawy63DC8UDxrkTs79C4fzDwqh54lh7rvnSO0NXISW76DKVAWSs8huMNXoqCmbBUNno_30QgvJAMUBYFxxKvoKcasaOFuwGC3wPLlGjM_t9kr0sF5Fes5EdZSBK_NVYjCXzKBD_7rjmx_gI7NyLG82SR2T8OtZf_R30saqqDozLDBMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fc8JPu44tL_7yi6luK12n8uqSC3U6SpvO-gEzJkc_Xks2yjEKqIg4X5v9rIEgZCj2eZ-Nok6bUreB8zcxrvBJlC4v_YebN7OuHYYWUUnRrQVSNMWUIj9Zwa1ij4kjkMFrOBRb4W_b5bqWBALQ1uhx7B1kr6w7iJxE2IyBukVeB5x7dt3XNXZCoFG2dN7sCgyMZS9RiGxtA2-OrK4DTJBZKj-q5Z0IIbT1rzj5oWOU8pumtntWWlBqTY1ebg-VekMhQi32HckBAVWFs_Z2O2xf1YZ5nQe-XAhMG7zomzNHrtkG0dXBK_LpEwYKUITF3lqnoO6WotMZnacK3nyaA42jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hgi77rhpFait4iwUmKCPPXk1xcm03vhhJmqLSpeA-Z6vs-Xob4HPyVeup_XU4akE-WSAMOfqmtViWEW-wL3wl9_N-CwbA_H4rAFlyk91UcFDU-LxNQvAUNjJIzO1rqJcDw-hosT4FUY9D9cVrJuzw5dO6G6neGyBd6MpuNZu_iSwuXA4dbONrsDvkURvCqWGz0G7nma5cphfpLIcNpsI_R8b-3ctbldQgF1Xka5M4PX97ag-MT4U5LEu39phK3MbCphlcmup_9ITdTRe4T3fL_d9LwNxBwn4n9Ti5dV1bVtDu6osfykRut_XqtdGyZJXoXhOY_-PpWGsIIlTljrIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtXeVjy61BYNgl5ysaAAvG2HkTk9XwDsSk-U8t6zI1Nk62ZglucnN63hmZaZdjEs2NJawj1I6nC4wANUmL3SiiSY2IKl0B3872qLMWm53benYTiCpWomU3S4oIaPjVN8tc_C75UOsLM804x39rH5PNirnk1fr7JAtXwbUyscUQIc1qfvGzurw8CbJYnvaQCN05y_E5-YkJIOaRx2ZuvKu2LrqXiHmYEVsIRbQ_eJWas9EAPMvsMLg4zQ1UzeCljRmKqGTfOhPd6uGlGgbyEi778Sa_9zFyJStLFO6HXE8az19EY9NKhQNOTl6xNKg-Kri4nrU9H8SyNhCSFERuN4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7qFrDAJQuJ4nu9rOG0ss2oujKNUYikV3-YD9upiAWiPW1dvrCwAqm4x60XbI1WBJKSaPCp5wytp-Ep1DAPXMAr4lsFl4UbfKoYUEwZfPyYWtZchynQr9kvIIP_iOwJhAMct_wjKnANzYfADyp2Dcx8or42HWozf-gD8yZ9HLEMEeJVSmJ5Iz1PXAeeYQXKZ3lp69Xrei5DwnPAExHISSHWcEGpo4b4V1c7mcyJHBl-OXr9F7pnZ50e8vWVcJUXmBRtpfhszbhSeJ7XrVi3eCLyPtDh-nV-4a-WDYadQ76IOVmt1otX4Ol_n17nnfrnDZKUMetlodKV9Nia1R6kt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBMCE1uH1V60ks5s3tO6wJ5_DGfxL9ieA0DyWJv4Yd7wtV_HZRRT53uKWEVUD3TAGm_kKyknqD1TR0n-AwG7Uvyj-RRBnz4RaqWlGVfx1oMc29Dz852HnfiIe3dxuswEnMV4IpNSmT3W4vs5o8uBAzBFWlIjqttTHwy1egz3gIcBU12XqQHzyNvBxpGsh9XSNIsh2NsfQgPZE6pZW0XSHzh5DlxQBQf9ZIrQ7pl2_MlhIgECk-FrrOfpLX7jHsZkrzjefBSvgbbeboE7ytw8SLpKztE5d59hNhZlsWxeVMgRSGdWoBNYs7yUvi-dxCCeQqQqeTcUG0YZ0GHrlRyHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJrweZsvlxPuFRglOzkX4fyEkt-5lf4RYQfMkK8BHNt6uJppjHqrBpH1gSaY-W9vYn3-3yawUIf2qltX2CZMAdWUrdSBFMHGTETflCxIb6wu4JbS96WEHDOLVDnw7oOo4EPnRdLMkskeq2-m4gVDo-5-e1V1iv3N0zYHPHK_0WNao4j6SX5WmZW-S8LuPw-ee8gbhEd-bbECENqppG4GVLrTTEmFVxzzeeCO-6VZLera0QEu2eAP-hs3XfpNQP3jwvJsNnX-Pf1dUl2xsv0AIt4Q4OGi97C-St6YrHv02N1ZuUrAtHFyYvgjxMcm3dmEv8O4QKa6cqafCO2HiLQiQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNBnR2bDkChiW-F6JdwxaqraQShyr7Mo22hSEioPNtcNgVEp4MQ60YgZW8jqTPvPlB5KY9Q9oTHRAOPMYsZzZ4uty2tcW7qeX_kOfDKXZY1aiyPkynIroIiexcCboG2A5iDjvYX0fzyVN_rSTjzm-DqbWbFEXq6sqOmd2pJi4Hp2KXIIdDOS6VMVjm3OSRs05iKMkIp67iLscem4HOKQ6KAKwY3BWIhsKDXD-oeEOB6eAwC3kBcoDL9p8131OmVbCvf7ZSB-YMBot1r_2rOiqOcXz0yvDh2BBBUXjvInLKGy0FNNqM3LOq6UQg0HrIEQ8fTFyE0TMORa07pTBu1eqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULFXizsc1pmWVrxvqezqaLKnWPk-zBOd-WomdOOH0K_6MXrh-MV7QLL3GpB0I5WjPUHFK8hNH0JSmAiHp9rjELOjM5qrx2LrGVtpHQZWZV6Eiie3NGURekCQ8IAC-_-pIOI5MtqNdzIYxckVwBx6KwuTzieLvYzbR21KwE-eh7V0EikfrO3vFmUlfCkzFHpF496mXmNUwNw_hRR6ECOGV64P70L8p_T5SrSMB4Wf3whAtdQxRH8zJ2otzACpxocXY3h1ix22uoADyvrkejDyo62NcUmBrlejKDWCjfSKfERXtyIAvn8lDbfqoI8scBfQ3h8ruqjZ-2rUOPknFlnGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALMyATOrrC58QCAw7UjRVrTV6ouVSIED4lHiTZ5jj1uRHAf9o1G8C8CV1h3SHePGen-r78HGaHWt9oaz6lLOxd8Irru780ttzxjwbpOcWdxSnJGCb4mJbSTqtsnCa1R4wtToqszJR54AY3k5hy3HL3TKnHsMuNnWBVKXE1GZfzSvv6qegv4mnHjR5CHmWpCygzayX1l-5j77D4xOGulKxTcG0AL95VEtrfZGPu6wtTCfAWvSxYahbYtDL4N9tzVwFl7QuXPau44WJw4m47WpDl9kMciqAKLApufHx9GF8R7WkGe94vR8w3APociD-N7OL6KrZIXw_6hghGxB3IEilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeRMnpnSimDSARotoEx7nNkexE7T4nThCoiY9xdMlZ5QBD9vIFOV0geh20cU_MzzcOVuiFx5cer5MJoCdQQmB4UVJRNO9DbZW3mSymr-3seUAbC2nNzXfRthnZ0cuH4KciMed-JOGPtaPw7Va81JziWHf8TmNaVs_YLPQrbuiPOOa1702SHmxZdnqP574LZ-RuTVIbRx_1CwaV87J6pYfsUelq2wplvX2vP36Dmvi_RFlNjfKcTKYjHY3zT0Zz-gBaJWi5IdxNwPMXGV4MhjfFwyNhTZN0L7GEAmchbPuv39IDnT972MJX4BAhNfT3GUZ-fi0v5AOwjpjdI--6dd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYxRleYyfsEjLujHGsfPn_XF0BR8qfveBpUYJaICla4vcmhdxJtDcCvQ3wt36RO5DTebVYApKaUL7Afyrk5SX4sG2lWpJsAxzEdNfUcpj4A5v52B_W8xSbRt4cdg4voC866vhTPCfLZgOQCYoHqVprTbilEvYaXXx0rcKnrmvhTWUFLdngv9XH3X8IkT6Vz_vhWqifxNf9w3_crgjKl1dPclTRQZIn-NXv0rsP08RqwhC2u7UN9YItiV5n-D5m8Dvc-BBxkxn2-YCBwXARt_ZjWkaVy4R2gTMhcMzHG4Q4sRzZrI-g--XcvNZ81uYaOBg_CDDJKYCT_ExXqDjyUcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOY_R2QvTmlqPHLTH9K6movvImubuEXmOdR38DJFr4OrV1j1o52irnq_HLxYyYdm7ZK8e-tlF4Dt5RjTxdqqHwM8XDvtPIIrG7lVji0L-fLGWmaHRXmk08BAS8e30gxMQK3TTEAK-DJTmWqkeQpRCCYQgdxy6ZXn8DQ5THYraM4ihpXPI6qj0U3PYSxCt1_9oJYg182SWhVr-X1BY8JmNk64tdFfKPo6xBywU7iD623UifBzEKnA0czRXDKG4z4smPfCMmMkmQcZh549_7EezcAJvaFaFFuXEw2vBoMHSJ6-SpbtUT4pm0u3uHqPIMq7qA-2MmiEZELeIcSA1THY4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmDELLolmhcLfHL5RJkWI0XjtqdeLs4hh5NfzTW-vgSGYsQcQWVNvysBe_lmdpMxIX3M2ItXMTnASm2FAvHKdlFZMwy2C9sLsYBWvOx590vGmWZ5-J71RsGSj5jraWjQz2KKF1zxhSAGFkg6ffSS27_qkenBW9JpkEvuL2q432wOHdFYzbPW5VfJXSmnLV1vyz9gjZjIWQIuO3LjJX15Fh5rNjVSGt_X5LfUvZvDs_fCDLAcYjdTtB9xy_X3fBb4hMwBKa03rTCzZud0YsTWucHJeeaMDiacP5DiZ-FiUcMQbfRYJ8YAYtjwsIW0W3jRZWNPI0QeKdLHzU4htS8YOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTaMP910sLiyjE5cUHDtg0VUkjI_hQe9-sZZiWQMNf-ktwiSl1Y7iBsa0cNblhfwedmNurQdJ7jNcGmuDS4NOk58Qd2oY_axJ5c0V2A0xvaJkZier8pfFnxL0PsQ8NphtKeEp3jJid3LeAkQT5EQe1FYJZGJPGWnvqd82Zpxa7fXyq7M5dB6TKtxa7lS92V3T3_pBpsjPNNGrXI3qsGh-j58diKSoo3GLtrbhC-x5jgMVNaKqeGj0RsAhCkItTshTLc6n4jrxR5_L7DznXkZ0FSASyoeUcoLqJseO51YqrF1gOFFGKt_k13nCvJZK4nhFHFIk23R7mAD4_zzHc8bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk_LE0dQe7rkLEr6LiAoNpKlesf_oxdYRJd3w_Q-VERNm8qv-TRqVM6Z_j0iX2MUIM7qLPHtGOy8Jt7lsjBj_7t-Qti3NxiquSOElX4-I8Q1Z9zKIRhkGPyku26vPVq_T69d7dUIg9St0chBw3Y9_MQteGr8zzzxqM1WnUItpErPJb2VrtJ40lpWqmv1Ih5byVDY3OtzZQ_tB6HReU307gS1KiaMh2MIVk7El6svQphG1-QsM6FzAUYlyo0xC1didkzs8McSmYbQwkwLeLNpDUL6H9_H9CewC4Guwyn5q-UC7F264kiTVxJ6HV5BhmvK_AsY6rvXHBLLt1KkQEkH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3_8haysU3CqsyAiVcOKiBV2sVh-ZOKW0jDanVKfnv-O9CS29NyxUaD_CD4FXHflrp_WoBSH17JhjDb5rIo4oBp7Etv5YPN6rhdkQmKi33adjDdUj5ykFx34kqwk4SGTjaKjIC8eCErARUgAEQt3q_6RB-Y6V_XYD8LF2VpnZia2bri-HXnViNKpNv9C62TSP8kjqVoAv4X8qhteLgMNeYSPVf_VsHStqtmkjtJWt6QuM46yXOopGDN2CcZoqHQUt3xBMpz4NcD8czJpSbA5AMNpauNYuWsmK2-AvKdvFhk6fJhwj03BuBtUQwdVibA8PgXmjz68jyoK-8Ebuuk50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvYDlGH5-HPf7cjmW0sq44rmLyDwnSIcdJjVhucFKkeeUq6ccVYhN9qgBf6I57qvaAXJ4rM5R_xBJwcuCfRBoxsdunvi1jy8Ed70o5ZmiPNW1hNIbDIsVLidRfuqX35zYdLldmd1Es-_iP7qmxWMpFAXw5dGZzIVWS-fuTcxmef03sE95UX_ip_sGC3F5xE73F0Zk-ffRCiyrey2AgiAde7rDigAswyHHZS3ccu0H-grOfDQH1yOZ5a-ejEAoOxvsv1_I8cvh--eB7nu4Um6658YA6arXtZam2gtDwcHKyM2_Gah6FTaW_MIS_hRC_6ZZHhKgephghpeIMlkW3uFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqb-pzEiKVT-2wWfBzEKAMr4ySfclv9Gvb0IYslXj6VH4FPSRHsj4mDi6QU5d6Jm4HkiGwQIvafR19d46U6zpVEBL7BPgid4pMiLadcY4LBLze2xpYebW4EITxNOmiVZkHPHw4T8qF4x1NksZCCaH85lcp4Atd64wOv5QoknGP2_cYehliVB4Ca4s65J5es7VJRH3gIGuLY4y7mOlmIcJkH1BFNtzYb9lQpE75c0mogZ6Xo4SHYBDSYqfPq9JUOM5tE-Q_pgC1y7xN0s8XH3Be3RkKCeiAcdK40kpE5dytk79zq9Y9OmyHwJeRx05o2aZLUbQnTYi2zlYp7V1y1oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تغییر ظاهر لینک سابسکریپشن 3x-ui (پنل ثنایی)
🎨
✨
پروژه
MiTemplateSub-XUI
یه کالکشن عالی از قالب‌های مدرن برای صفحه اشتراک کاربرهاست:
🔹
تنوع بالا:
بیش از ۳۰ تم مختلف (سایبرپانک، مینیمال، شیشه‌ای و...).
🔹
پشتیبانی از فارسی:
کاملاً راست‌چین (RTL) همراه با دارک/لایت مود.
🔹
جذاب و پویا:
نمایش انیمیشنی مصرف ترافیک و چیپ‌های پروتکل.
🔹
مدیریت راحت:
تغییر و نصب سریع تم‌ها فقط با یک دستور (از طریق اسکریپت اختصاصی).
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8BQLIHc7O91ur9uFprYS63m3wBDFlUmEOkTIShZtXMQj-NLo5krPVxa3_ouy0c8ynx4CMENRDkich3aTUtsUeTjHTvOzuwu7sQufcySLV2CrPgvr8uSuQfgW6zPQfUjfQvuyJ79EHc6hEO9MW1tNj_bW90Tr01a8o_Ue-Ks6Uh6bOt-_gQDcYLn-04x0gMxmQJN9XG3SbQyVALcIC15aKRLWiYxgsCwxQwfFywsUBCocmWjickAZRgzCzlFW4BYqXSuoYQFGTvaiSGt5P8Ye-wQQNykagnZVxrfK3GnUX1UOwYNm1m-9Jc-pRP7UcrQ46zzkhjiqixYhHHV69pXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ابزار ‌Onlook⁩: انقلابی در طراحی و کدنویسی!
🤯
‏اگر طراح یا توسعه‌دهنده هستید، ‌Onlook⁩ دقیقاً همان چیزی است که به آن نیاز دارید. این ابزار مثل یک دستیار هوشمند، فاصله بین «طرح» و «کد» را از بین می‌برد.
🛠️
‌‏
✨
قابلیت‌های مهم:
‏
🔹
ساخت خودکار:
تولید پروتوتایپ‌های حرفه‌ای همراه با کد تمیز.
‏
🔹
تعامل دوطرفه:
امکان اکسپورت به ادیتورهای کد یا محیط ‌Figma⁩.
‏
🔹
سرعت بالا:
صرفه‌جویی چشمگیر در زمانِ طراحی و فرآیندِ درکِ کد.
‏
🔹
رایگان:
دسترسی به تمام قابلیت‌ها بدون هزینه.
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONMELyJykCw_xEuyZPjvCUk2RBt76O8G992C0M3-FgO667siMArE4pTaQ8MTP8-KnhFuS73q-Gp2b5oMRhx17TgJY4pzxSKT3bupicbi2enmOyA-UjBLx2a5LRzEjRH5rlDIsGaSH_TcknBdP4RIcYAIXqGYSj_Lx1U26t9U9CrUTAQ5f9Kg3QfrNDl8gAf7FvTH3P9HCxZblACaEUURLl8srdSG-v0QGr9Do93KoJ2lypYz5qNjHEoKPE4GDrw1l6X8Yo84vLjGpUUIE2G-hcqfki3J-r1PZMPMAMHbIx6yEBkOuoA2teYibhTKpY-MXp1B4P8rhTrzjo66Q-ebBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
گنجینه‌ای از هوش مصنوعی در دستان شما!
🚀
‏اگر به دنبال پروژه‌های آماده و کاربردی هوش مصنوعی هستید، این لیستِ طلایی شامل بیش از ۵۰۰ پروژه متن‌باز در گیت‌هاب، دقیقاً همان چیزی است که نیاز دارید. از چت‌بات‌های تخصصی تا ابزارهای پیشرفته‌ی ترید خودکار؛ همه چیز در دسترس شماست.
✨
‏ویژگی‌های این مجموعه:
‏
🔹
دسترسی کامل به سورس‌کد تمامی پروژه‌ها
‏
🔹
تنوع بی‌نظیر در حوزه‌های مختلف (از بیزنس تا مالی)
‏
🔹
مناسب برای یادگیری، توسعه و شخصی‌سازی
‏
🔹
پروژه‌های تست‌شده و آماده‌ی اجرا
🔗
‏
همین حالا از این مخزنِ ارزشمند استفاده کنید و سطح پروژه‌های خود را ارتقا دهید
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ0PELREuvQSW_HTOZOADeG2FfTk4ZhVqmXA35flXOjLOyE5eQcoRWjEysezRLKHMYueYXrNvorby1YshzuQCrfhRsrcSRn8FBsft_nhu3mMtxBz49w20zUsdorLsHYH7CLkpJBCVqyfRkMMweco6M4eTHuINxSMDljOxSNmRLUbuUC8KfZqsHSij0bGyioVdYsRZkMPg490X6SYkALuCHHqmpvR_mnXSDHDUA4RhjTzOq3xtZy6oclKmYSQzF5aOBtEYMI4epgU8LClJ7c7XQsZM2uuX0iHuMdJx8SbmmL_uKSnIaId-fq1S7-qm6Bvv7DUuThFI7V7ybvCRgjkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi4SmAU57c8h93VoC-lQRNKNxkLz1V-c1_gS5sPAJlLteKxmbgykRTdbwJcuiaXFoblDaKooDvPkc2LMB08Hm8XhOcHfu2vlZx6LFzmLZJ6VXrp3TS-hCpwBFd1BEMd3H3VXspKao5T3ia3FdxA6xWOqYwZsoVQfwX75wwduywmCZQ-KhTSjUOvkuarUwHjRgOJI3-_mXrKoHuiF6lZT6hjJGKlq3-cveuqQCtd4skTt0ttNoHc8bVBvhsriRP9Znscj6T5lSQcCw8x7GW4Yl6Z8R4WKUsQnvLKIWUtfkw_RDqawUl1h_aUcPVlf90jBW_JATZ9gxADTTwqbjZXWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWRFz20_ty4zuuXP0ye4_-qsmvYGVhGDPk0zUlMmCHJdtZZEei_a1jUpu7Yl3MBA4eFiSYmYxvV_XjJMBCFXu9uOmvJUDmf_szByhiPLSUuRyyVsJ6VFzjqKZMsyOJoJfavEaYn9wtIwndRRvZu7n5Zi08iaU0uteL_3YgwNCMsOH-RyVyjLxJlKTacWxATy5PlkL1Uc_3Pply14k-ZCZLJahb135zkcWWeZifvihhqwNDzTLGjZUCBHEkB77P-AlMcz4DJQnW6uR4U8dVexNCcsyFMSEmwgoGs3a-OHV3bBUVQDrWjXA6KeHE9MbZw4rAfYcKJQyUWOT03p9IFzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌APK Converter⁩؛ پلی میانِ وب و اندروید!
📱
🌐
‏این ابزارِ آنلاین، پروژه‌های وب، فایل‌های ‌HTML⁩ یا بسته‌های ‌ZIP⁩ شما را مستقیماً به فایل‌های نصبی ‌APK⁩ یا ‌AAB⁩ تبدیل می‌کند.
🛠️
‏
✅
ویژگی‌های کلیدی:
‏
⚙️
تنظیماتِ اختصاصیِ اپلیکیشن و آیکون
‏
🔑
مدیریتِ حرفه‌ایِ امضای دیجیتال (‌Signing)⁩
‏
📋
نظارت بر لاگ‌های ساخت و مدیریتِ تسک‌ها
🔗
https://gentsergame.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRH2otzdBdvSwkjeCB50KXMrUU9DoUpl9ju6fGdsT8qHalMNXbvR9IARcwdPvEPrAkloEmh-OihBte1Qg86Y411hjMGWxUACdgqpvIw5Xr-2vYdNXYXC2AMpZkw3cxDPBHOd3avSxV6XRiXHpX41qh0p7oM9ztfhqbp34kc03xdfyR06EOn4GxORfksDZhY5PIrWGp7xXRRU8Sg1_dSuBh1kmOyY9rbMxgx4_woFXQxfVQ5TJH-UrWExZ0IHhiJrH5eEjUz94gqH0XdIvWAyseLBchNja9jYfpxsMejEkQ8ElLC7EViigyM9ZJfRA5pRco8skXlwNFMDmAxskmG-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
انقلاب در کدنویسی با ‌JCode⁩: سریع‌تر، هوشمندتر و قدرتمندتر از همیشه!
💻
‏اگر فکر می‌کردید ‌Claude Code⁩ سریع است، ‌JCode⁩ با سرعتی ۲۴۵ برابر بیشتر، استانداردهای جدیدی را تعریف کرده است. این ابزار نه فقط یک دستیار، بلکه یک «تیمِ کامل» در سیستم شماست!
🐝
✨
‏ویژگی‌های کلیدی ‌JCode⁩:
‏
🔹
سرعتِ خیره‌کننده: ۲۴۵ برابر سریع‌تر از رقبا با بهینه‌سازی فوق‌العاده.
‏
🔹
مصرفِ ناچیز: هر سشن تنها ۲۸ مگابایت از رم شما را اشغال می‌کند.
‏
🔹
معماریِ کندویی: ایجنت‌ها با هم همکاری می‌کنند، وظایف را تقسیم کرده و کد یکدیگر را بازبینی می‌کنند.
‏
🔹
حافظهٔ هوشمند: با حافظه سراسری، هیچ خط کدی در سشن‌های مختلف فراموش نمی‌شود.
‏
🔹
سازگاریِ کامل: پشتیبانی از تمامی ‌API⁩های بزرگ (‌OpenAI⁩, ‌Claude⁩, ‌Gemini⁩, ‌GitHub⁩ و...) و مدل‌های محلی (‌Ollama)⁩.
‏
🔹
خود-اصلاح‌گر: قابلیتِ عیب‌یابی، بازنویسی و رساندنِ کد به کمال.
‏
🔹
تجسمِ پروژه: تولیدِ نمودارهای درختی برای درکِ عمیقِ ساختارِ پروژه.
‏
🔹
مهاجرتِ آسان: امکانِ وارد کردنِ سشن‌ها از ‌Cursor⁩، ‌Claude Code⁩ و غیره.
‏
🔗
دسترسی به ابزار
‏
📂
مشاهده سورس‌کد
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCS0YORrjmSiY1XlVGRMm031HcxIaVhjm1vKxo6-HbypIBIrmKgh0Ty4JrpSCv1bT6Kk-MVTDvWSQCV2mhjmqbYzY2DbWyNbWsEl8JQObvM4LrwW8--0fflBMruNkBqnPMIUAYEmRtjc9A5sRE2as6EmHGxcpXB1lo_dbRcnLSSM-QdNFOeRrXJR8l9s8J6CPb4Ps-n82IDkDWBQZm0j6tS8rEm_ACHQtIqTHGQ4e9u-LKZZR1FGWKGd7yR98Mo7PnPYtWqBBqEf69AMij2-wuuoovWj708qwv9vsT6JCftxJ_vQkdFComJa2MyVLP2MgWvdTauFW_a-7PagjAPpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
70 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Opus 5 | Opus 4.8 | Sonnet 5
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts-L0IKq_dkFV6c9oYuFgaNjoKONzWzQFzLp8eH8orHv1IdP1VIUtua1roRk5DQJtUJ2ZPNAWqEJDZcdE9pAf586As-7sypZ8MZb0kJo8Sv1XdJTT5Y28xoDQzUQ0GZ9VLeF5k8A8yMLcnqceadQ9OjBOqFJWvW30EVP7hnChrAdhUoqwhuI1wX4mb6Tiw5nDpjAGWfd1HsGoDN4Tt2nGBg2vHTvXR4fktRyvTccjfFSd9O27aIPgd5armmGFSjXvj5h47zpdNV72npB1FhGuRkY8SI5NIMjdc8I_AL9V8MmCaqgVm6ikSFUBK5huyLKE49AgohwGisrXFTc3fLxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام جدید و عجیب علیه پاول دورف؛ حبس ابد به خاطر ربات دوست‌یابی!
⚖️
🚨
یه خبر عجیب تو رسانه‌ها و کانال‌های روسی داره دست‌به‌دست می‌شه! ادعا شده کمیته تحقیقات روسیه (СК) پاول دورف رو به خاطر عدم حذف ربات معروف «Daivinik / Leo» (یک ربات دوست‌یابی تلگرامی با بیش از ۱۳ میلیون کاربر) متهم کرده و شایعه شده ممکنه سر همین ماجرا با مجازات سنگین یا حتی حبس ابد روبه‌رو بشه!
🤯
✨
ماجرا از چه قراره؟
طبق ادعای بازپرس‌های روس، سرویس‌های اطلاعاتی اوکراین با ساختن اکانت‌ها و پروفایل‌های فیکِ دخترانه تو این ربات، در حال فریب دادن و جذب نوجوانان و جوانان برای انجام فعالیت‌های تروریستی و خرابکارانه هستن.
اتهام اصلی دورف اینه که چرا با وجود این مسائل و هشدارها، این ربات رو از روی سرورهای تلگرام مسدود و حذف نکرده است.
با این وضعیت و اتهامات امنیتی به این سنگینی، به نظر می‌رسه فشارها روی تلگرام دوباره بالا گرفته و فعلاً نباید منتظر کوتاه اومدن دولت‌ها در برابر پاول دورف باشیم.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dockerfile</div>
  <div class="tg-doc-extra">35 B</div>
</div>
<a href="https://t.me/ArchiveTell/7299" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!)  با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز: فایل Dockerfile ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱:…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!
)
با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز:
فایل
Dockerfile
ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱: آپلود فایل تو گیت‌هاب
۱. وارد سایت
GitHub
بشید و یک مخزن (Repository) جدید بسازید.
۲. اسم مخزن رو
railway-3xui
بذارید و تیک
Add a README file
رو حتماً بزنید و دکمه
Create repository
رو بزنید.
۳. تو صفحه مخزن، دکمه
Add file
➔
Upload files
رو بزنید.
۴. فایل
Dockerfile
(همین فایلی که پست کردم) رو بکشید و آپلود کنید و در نهایت دکمه
Commit changes
رو بزنید.
🔹
مرحله ۲: نصب روی Railway
۱. وارد
Railway.app
بشید (با اکانت گیت‌هاب لاگین کنید).
۲. روی
New Project
➔
Deploy from GitHub repo
کلیک کنید و مخزن
railway-3xui
رو انتخاب کنید.
🔹
مرحله ۳: حفظ اطلاعات پنل (Volume)
(اگه این مرحله رو نرید، با ری‌استارت سرور، اطلاعات اکانت‌ها پاک میشه)
۱. تو صفحه اصلی پروژه تو ریلوی، دکمه‌های
Ctrl + K
(تو گوشی روی آیکون همبرگر) رو بزنید.
۲. عبارت
Create Volume
رو سرچ و انتخاب کنید و به سرویس متصلش کنید.
۳. در کادر
Mount Path
دقیقاً این عبارت رو وارد کنید:
/etc/x-ui/
🔹
مرحله ۴: تنظیم پورت و شبکه
الف) آدرس ورود به پنل:
۱. روی سرویستون کلیک کنید ➔ برید تب
Variables
➔ دکمه
New Variable
رو بزنید.
۲. کادر بالا
PORT
و کادر پایین
2053
رو بنویسید و Add کنید.
۳. برید تب
Settings
➔ بخش
Public Networking
➔ روی
Generate Domain
بزنید. (این آدرس پنل شماست).
ب) مسیر ترافیک فیلترشکن:
۱. تو همون تب
Settings
بیاید پایین‌تر به بخش
TCP Proxies
.
۲. روی
Add TCP Proxy
بزنید و پورت
8080
رو بدید.
۳. یک آدرس TCP (مثل archivetell
.proxy.rlwy.net
) و یک پورت ۵ رقمی (مثل
14841
) بهتون میده؛
یادداشتشون کنید.
🔹
مرحله ۵: ساخت کانفیگ تو پنل 3x-ui
۱. لینک آدرس پنل (مرحله ۴ الف) رو تو مرورگر باز کنید.
۲. با نام‌کاربری
admin
و رمز
admin
وارد بشید.
(بعداً از Panel Settings رمزش رو عوض کنید)
.
۳. برید بخش
Inbounds
➔ دکمه
Add Inbound
رو بزنید و این مقادیر رو ست کنید:
@ArchiveTell
Protocol:
vless
|
Port:
8080
Network:
xhttp
|
Path:
/assets
|
xPaddingBytes:
5-70
Security:
reality
|
Target :
www.samsung.com:443
|
SNI:
www.samsung.com
دکمه
Get New Keys
رو بزنید تا کلیدها ساخته بشن و در نهایت
Add
کنید.
🔹
مرحله ۶: اصلاح و آماده‌سازی لینک نهایی
۱. تو پنل روی
QR Code
کانفیگ کلیک کرده و لینک
vless://
رو کپی کنید.
۲. لینک رو تو نوت‌پد گوشی یا سیستم کپی کنید و این دو قسمت رو جایگزین کنید:
آدرس بعد از
@
➔ آدرس TCP ریلوی (مثلاًarchivetell
.proxy.rlwy.net
)
پورت
:8080
➔ پورت ۵ رقمی ریلوی (مثلاً
:14841
)
تمومه! لینک اصلاح‌شده رو تو نرم‌افزارهای V2Ray بزارین و متصل بشید.
🚀
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

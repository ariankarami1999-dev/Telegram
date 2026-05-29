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
<img src="https://cdn4.telesco.pe/file/hQhajDmEeCBbEXLyUHM3soVJujc3Cz53kC_00iEpsN7MCQ5TcLsBfhMnBYHOaTf_dFCC19baWL6__XCy8_DI656WBrfyN5A_5AVMXUkCPAxKsMVivrG-FuQATBKsoQYi-cXRKymO28m76YNKNMWT1mEVR2ra65FNvIT_IFVfZCyXakWWmSK0f8L0quXkBVzoko0FV5dgq7gnlnBmcXKu6Qj1z3glTd7NiLZ67sjM7NbCL7d0T17CSqgou6GPn4TwA8WxRPFLiKvwajUnE_8Qgt0fSzowrkv6R49ksAGJ80IbkBsC_fFU0DsMvvxo8Q-JMwSnZgU9UvNtUMnbT_UF_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 122K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90371" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqSEs813_zqYzfDky4bWUnAN6y5eiC03tFnVvY3tCur6_U9hOeXg3N4oetielmDtNmnmqCs34NFNo0DNLYHvIXyP8iZzQ1IX-wf0Gm15ifcZ_00aGn7GwULZdxYq86YgXt5MdG9Vh8qXvlwL5X5yIMR6L2QXOizB-Rg7tN8PBQb9foUUrmPuSCXhUzq17XGalQwFECJgadmo5fc2fzntfQmPKYeyD89DxhcdyN3TdMFcRrLfBrEM5gEgcFWlBuTjtidemZC5HM_uODaCo8HaKLbhyaczLo6as-1_tXf3qaJKcBuCWVnDlsc_6nvVPgEkic2SZP9iRJ7ai9ltmp8OCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90370" target="_blank">📅 00:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVMXtTY6lEVI2R_q8X-I1TsS-qxqRxhdj-7eVjDyWm-s-ptErOtljDg9ZDJzgUaq4GTULa8Xr9HmLewk3o5GZ7e0j2vnp7GsVIOqjZiO_Y1sN3jGB6Mx57mJZGcoQtMlzD2DQ61kQPu0wjUJyEiAtSUVdWuQlvDgHCIwAL0a_irUuyUN60RSmOOc9oAKIPKMLra3Wy3aYfSjuEhGaFY8gaJ7RS6QhGi0Asvc9qpPfMtHd-tn-iuNSj34xphliathKAUv0svt-6Dyrf28dHnibLYJLYYhdmFUMFwR7dSwOEllPBXB69VG3_Y9EK7U20o2qpPrthAMkQIxudPwbN6CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=jv4kn0OZaYE8d24TYndKXDKZUgyVdUisin9zIFM8TS9bFc24gsdC7BYc0wmXqzF-vTUgJWA607y9mauA1LBkR6K_eWj9gOM5yrJPwiGA4-pFqZIAIOBd0muYTVDif0O4nqoVH_pzie7zbslIl77hS0Z_KVIkAFiQymXYDspypROD5wa3g_YsLBvd_KsdeMDYWTHQw6hQQ1SPRSBgJFaZ-tqvFk1WCWmF77kkFmcAt_KMslph25JBgplWwsi_1a_81fzZWiozOJzCqQPFc4HNRM3znyBZQNTMBWD4whC_yo2iGTJXl59GsCvuoEZVajfwsnLgnpvhG2LUbqnrDzKvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=v5vffCFIQooZMh8-tMFg7A3gpWhEs5wAHTcGTtjcLK4bKcLwFBNyXpcl7aXpnRxil3mw0Vpi9kBEZL-buzV_5Pga_fLn_qE50lHMVTqmHaAjY_9-422V8x7DEoyw9EyYq7fiFpU9Ox0FLazdvyfOfdqHbM7J3yGrtg-gZWRjb-h5OqC6l0AHnoPpApLVwHcWNeQBfBnalePWi7KvtYarE4J3VzeBOzLSHeIQGznhTzkZG2dzgKJEie-IMqyWgvip2gr4oXe-YMHUFtZC4ZrEuriwVM-NOsyRaoUINZ0tE8XHmfmJ1dzSiLkedjgOzDaeN6_wT3KbjLHd1-QXwoQD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoB1vtRtMWnhbIZ862nJYviPu2aTM261AJ0HKQ0Qfqis5XQb_QZ2aVxq33sdHH1PVgSobyf9bNU62JEkGEWcwF1JmmtAHRDU8bkfV97QtjiR6hGedi7SL06VZBz6jA2nEtLuvcrSlAssBj5nf6dMoq1oqrOb8aAeo8-djhkSBsQS5NOu_xjXZvRHNFJKNBrSIgL7JvLIvtRUQxNc_0IEznZzpb65NBMb252i5hTUG_DVjmQCW_xR725baEIgpQQ_OLj6tTF5CF_hvNplzLocIS-c_N4dsjLGNts4lPto4iGqlIvBQMQbiGmOY8STxfmxw3tp_dd80Q6LM1BrgXj6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvyf7TFofw8HugI6-UfgEbNvDlR5mPbr3TDAioti4nONZiF4bgmn1bo6uQzyIUSBvO44YcXVpzLU3wxOI5dvMozSdXXnxXFJbhLjIy1dkcz2XnP3llJTVILlXz9nTHTkRA9p41dTf9pZTA2unIuZX6qVHb-y_eE8NfcnnoRqOVGTBgzl8hwHoUul9QKwy5Fk2S1LBAvI9_X3UvNA340QQdxuxz_KxZHA-U3_Qhby0PSLG4FB-CKQ5JvkxXhWUBOGH0Zf8WRYQrBpPkS8NWK5r1Mcao6u2ROUf841eIXDLUkwGps64mg_O8eBAUAf77B3nrpwCMatdxcCcQ67n0ekvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90364" target="_blank">📅 21:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL9_rRLY35J7bWeadPLvXvrEiKi4ackWMIAWM5TV9K9XGBl78_NZrbphFFQUQPLM5LvjBKIS1bhG5JWyCbwxBpMKeDYTV7Noyg4keX3qHcCjcevLnyrCZzYo3s00GqiV2yrZMwu4CBdlTw0Rh7BEZWgOJk0-t9nklmokRACDsjpscF2tZcYdQ70lXp0xm1evTa2zgtgG4EA7X5InlSoQhBtJA5oN0IPPsdTOVqGL1bCkKVjMRkW7TRwnIk628ymMaIu26nWV3FiBnBdQu_XvT0pJyO67CEhO8txXZGtfa4orGhanWHv3mwe7471XUJ9uqfBdZuCEywCvkkqzb_5q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbJPBEPUKYp29UxCFicUMeRTfJAtw-y7w5_MJ5IKBxfovzG2xSk5UALTOCuk3sLyQUzBi8aphUNMIQrGmQ3Y4gyNhUYeSpDCCRRbGCdg6zd6GjT8VXo1MhrmRB7VMQEw1OvTJ1FEa9huOiua4ZihXijTWsDZ5lgQ7bUidyE33kmwFBdZmadPxkfLkChxFyDn6NFVrrceSUvG00BRhsymsVu6MDJ_Dk5XlL9WW7DMEku1ncHBmhTQYnY_LtrYm-Qsi-aKR-CFEUYCOc-autNmOlu9nviMlJf94A4ZvRokk-wBgu_ouKRXZz3CEnUAHkL2NG7mv0cT5EWjtspgwdUiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhS9LxPYEV4fevASSSwxC03QEpbrzeMsKociWH40OrWs41o6wqsgAdffUTyguFJqZFz0GIoIPK5-Aj16RNJHTgbjwGW6lP6bTBj1ClKXIl8HNVdbu_ug7DbBDuSBr0uu1EGBejm3Oze7cF6iKWZrmvyAo_VZ9Q-DC4e77iQBMfd8YI1ZTjs5iK4nYIwVxuvlg06xBZLevNbxu0c6ZptU2id0VBzx4iBSY178wPJwMO8qTjmYRqu5TPU4u4Qja9Xfo3PBbmYh9N-b4_TKMgvbFL8JeY1PMYIxF7omkD_UJkvXiyCfuNIHZzWV-SX6vxZ8Uf1j4BcQ0ko55Y5GjHepzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B334AJ8VyIjwh7kKYB7jNZ_faX3LICaqPPla2ceN6zFgFDAW9wjE0u1JaKCbchvH3THsHo9EHyLbXK5gfUEcv7oKuLITevqYxsgac7bAmE-5xbTsvf3w0KbHNAUQRdWR1zYAJp4F1EiS_iV4Hs6V-r6nVdHhU-DB6NyVw90LO3NDP9JSMv8tY3Kr8MyOVmeHi3lfnOwAMt5GHbv7NUIW71L_TBg9lpWVzhsLdr27p8VspiMi7eJIYeetoQdcjLxphxEmvGPJm28S5w3jEIVqJV-WMLnNDNv_yDxhFUYb-MtQCpQOua2ZdTciMNQPYPksmKbTOo-Jd0t6Um91nL5YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC71Z5LCuR0_Qg9Z5v_v9CsTK8sRUIK-_mmlS7u7lXM5QnY2TIMoVWegiCXaXvQPixz07l8MaRP5GAzSuZ561LNHbAPzfFyfKqVieKupzBbnHlbpl3bPzPWIj4uuulDje-QgwvkU1hO8HwCAYK-uSiInj27qY77dUNbbR32r9BUUU3EOC0iShczrgAvSXuurCltxNtXCY0UIA01XC_20f-_1WSEic-o1Qy1zxU59a1OTWdfebpJ9skYT_Iof2WASIgXzco45Kk116lfnj5lGcHxPbCMIFr1T9-37L6xlsjdcaq5BsHANpLRdtDLrVFgbc4o6rnRfSkhMBPWZcK0IJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOMWH6m-fWBTSaa6B6sMj0XBYZ-wQDFtONyIz3eGjyZvTaj03aV1_Juzv66EYZjPTIe7oNyOCsZZMPwNItfyTFGaAqGSvezfghvXXy-0aJI58TacXnNSTX-9JmSHdwejWcb3uzDV9bozFqnmcfaSub12r6ywZy9zXfq4GBZQhYEvN79MYgbLgW1SvNd8TLBSR3x4pEJy7wKq5Kh2TAyA-4HPf0eo5R90X6jmRTxe-H9Ijh7h4eu_qKaUX_VGVgdrshO1ofTNBgDGKYzvmPsa2NzTGQa5OsCzzx4iuhdLRizIsrDJvaBDPxkTTRXno6FTDRavGCl7G7up7kOIgy_sJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBNC18CMZG-ZyfR91EBpG4e3HUFw0tBIAicOl8kZjYMMRwo-J8QiCRXHEGlBb9yIaLdjbBgAIaJEKJh0jXEsoMMp1I9zZI_4PO7NxpPU7isPpNvY5qstey3kz_BA0VYrgUQtQ-YdRvx6hn2NjtGCDgzRI81TQZb_wq-oXNjsw0tmbxgUq9ypfinn9ivqQYa0vpChdC8lYBTVQLQIuPJcTygSPzrii-Nq5ucCe2Zy7-K-8c_nGso0SXmrWyVlw_G1JXtQVmZ9I7G7-R-ReBp5ABPyUeLZCQsQW81I-kf6hVUp29S7vnsY3_CS1qUblPn9roopUUUi9A3I31TirazBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abw7k5_0fNfeXl1mySAdkaBWAW_bzxx6F1rTK_2RHZt8b3WioATKjrZ0cxOR1-g5h4a_kAl0EOTN8ITpQ8pThZN05t5mx9UL5wCw-T_tihb2fokNW13Hpezo4km-LfKn78KvF0o3KRJ3vpio7-iqfjlg5Yl_F5obGcvPU4NEaEJZUT3s22oJuH78L8ldrEJk_gcvx3KOM4eBrTcgR1WXXWHhCh0gIu_9AyYvMfybxHGc4UF51_HvSMEEAAE66_654r_HEmwRJeoKXgavMhhQbrL59wZ6F4SILvVUaP6U6LhLMewCWF3qnWqNtwCxJSffA9-na4aL8qEyLZrQMUM20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoOzrntmgG5Gllm1wYErK3o7Rw04l5KN1EOI7si4gllSc8Z1e6pC-7i1bVCHFafqsaKsPWn9gXZoWfDKX_1mI-7EWsfLWFcP2anmMgoYzK6tuYlBWHBwonYCCEdKu4Zf04UQ9WNk7HhEhmFjgpxNfsmdhS9NFCo9dYs4hfH30BsBiV0cQfJpphkpOhTXHBnSB1t8m5EwbUMkj-IoiyqO7HaY6pJ9cKEGON7rQq7t6Wh7Ngw4orvociPUNrgINIVdfle9hgxj_J1y8zZaJ2y5namvq7CPLgudVoYpd2_s_JjE6ytfjoQldpxjd741iu9TGyDI-VuGNN23rJ_18hKgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2FF1v2sQdK4dq_N4Hd02LOaclRUowr9HiZDK0XVi5WzRDwOU5zAFeKCgvUCu_21S9wKZjZN4h_6F10OOQBbPObKijrzJA4MTnV3bXhpr7-mYY_EyWCWkPXr9ay5B8Gax-9ihPwH25WbsHjJtnli0I_hsYw8i4_j2sDQuTXtrIlwk95QVqLYdQVyazrTFkhJLX-7y9kDcgTT0BycT7LN0HvxiFXVzN5BJCynnLLUzwEAek5jSJqx3Wp3NDxA78em-HPpVwgtdBFCy5q-qJQ5Lhgeb7zuHDYuUjyiBa8tGpGcbY7uhAg-6mH-X_Y1t6iPa5xSYdmZIvzNGjbh1FICAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae9wSRQ3C4p61SmL8RvjG7SaAhrUFVv2XX5py6qHjxtEuyLW30NgNSyQY1srxAx52NITMLlz_l2vIRF1YlonEGLPejtP2eLkVLWnyeG3UEj3vih-MoIzPzihkTIEof7C5SfTr9CQd7HBAobYwVvGNYiX9YQB-9lcX-77dEHMnbJZQewUHfPPZJCEt_Etjc1Qwms2U6OzQUgDKt7I93IZw5rVH6rHLAAiIRL3yaG7eSBVSbD9Eosl_idDAAMb2M0IMtKDvn-EJzyqcN_tlI8-exCF4YqpsMKf9iY26UHh9Q6e3no_ZCvL1y3VxeqKuzgA4dvKWwsfC7pDtjAgnxdiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUXcb-o6MalQJpnNpufQCo3-jP81_s6IWPMPwG_9J_DuYGooLkIRCGZjQNDVD_XV0zm9Z7zoquwfYHxmmId5iqw6rmW8G8ncTGULcgxHSI1YuJDs0lEEJI1v-8KSML9knEj3PRpykSEQpjVzDlK8plCb6RT6jTx7hI84zBm4Aj6KMj8MOHqwTK_P1-zkCOKo4wFkC-nlU0Tt_tYLw4lgQfDU27PBcvoF_h-sRPlNCbCYK466drou7As7qC1bIOPkWH8QmpdPsMF0brIp0h7DXYX0HyDwOGTqsVc2G9OiPJ4rTiBiXd8uFfT43zMCz0PfIX5J-gwk9U-NOTSN8RHPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5SH_2ycOLMiEDQGtv8ehB1IG17boO9YwiCkbR8vuLMvOQoB4BiJfEhfjE6O7hAx9KNKGqr4cEV_S3DVgzNxGn05oCfpulC8nTYQnpUZ2o6jymo4yUs3vrnw39vZXX57ml-KuD8tgwIOYRLHtn16x-S-DO-ml9q1k5B7P0SMJWuBFJXm6vZXroidQmMbDRJ8cfM37_g9BBsNAsR-4MNki2ENIUNEuHSubQIIJcWtLNvCJfh1_gDRIBprCISl_yMDYF11zHEyXRfVp29hpzkDwQLtsLUCAxypURPeDRC2t6geyuA_TJEwFtWyZ8PbbcdBBA3lOBW3HVbz2M93fob7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVPWnnB2ho_J8wH5wyx0KYp1AU2WB6i7gVozrQLph2kvjLFm20DD1tizhyHTCjt5R6o2URI5o5--5pD0spjUcavoFt03A7vQowlHtzOK9C0Z-Pbg9ZJLDQM2-LbmscPjeTl1GVFnrSAzM6lYDTWHxVEu0V2mlLFCLpR8ggLYe-VfqPACN3zsg7nzLKUrVOiPJnN0oKSLTlAWhKEjIt-lhe2Ni8MxtVbN-bCL3EubqU9lG5ZVd2kzuwE4sVkiOdcjTzzUam_prKAMifk3k2ygE_NpvbKgk72GNUs2kxR-wxeh4sTecrG5RMfIhIzqy9Ym3NCsffAX1252AsuLr3Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOyHWDlVHlvhh0Uov-uneb5f3A9rnUJ34DFWK_bdx69gBN6oY0Ovwm2Mx0RDYeRZ9HeF5frqafNMCxAf2XA-a8onW_ZLlJiNn28LM97766K00qhkVM_3l4g6fW1RBrnysv14N2cs8OoO0WL46KBf2HVPBAcKLpZf4ASMTbchsEzyWG5LyddMugkmxlCQm1WriV6eGqah_dEwDCLoVmGqYVbjvlG8qVGHEnR-183wn8sRLODvlB7pPMqkj3uCStxZ8h0yJ9wqY8s8jn6V3kTedPRnVtCVEuj9GcEYOAiPuaISFUXDDxyGD6Nzz_hbKs8SVUZHGPEGCf5Ago7ClYbXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFyxN4Y3aGoJYAG0ITXVGRjItb97GXNAURJpOX52zI6qXXWiPO-jRQzrKref1IS4HtQ-q4Eyzv8NBF6ABSKbEaxQi-ALHsz8XwtVZfPuDvlVtrDlrD14ODyXzOTHXcLrB5smw6fwFZsjDxLUPXpAhFTpMx_yeS7VWnRxyDGUGnjQIqMBVMYWr582TRiYmu6A_Q_hj-14sWZLsTwouaCp_68p2FJxesIlP7GCG0E8lJ_SlvVkH4B5qZkboO8segrllMtEz6YxVeK1N7ffzdUIe406ZLiKsI4u53YX0PhWuSv-tUp7Bevp9qVrCIvxMD21QF5wsT40ze8LFgyrmkAJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkq23cUzjqdR9w6Eir9XLOiCsfZeHQnjFZPmC4KlxqyUIP9Ig8x_ET63QuEVtau4x1P61tFhjIaXbKEmAyQyiG8zqEA9NgY69Uxobvk7jwhP5jMhp0kA6pdg-wH9piugNtKOo1kd3za3Q66l49YfwHukCRMnJWhaQWOihY-f1hppQ7Mg84kNSZTh1uhLVTkXEAR8Y33_xf6i5MN5kOXMYFGYWH5GBMnRuFGKmBAdtp--nQgWdR9w0d0xP9AVjQ89q7kWrVE9cjw9GQgsDni87C5QnKkcm8ZJ5XOacHUhMfP2_zFDBA9JLwrpqRwWV27SpAcp8cmXI4X_KEvrU4nO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqrSVKr5CWjynmOFt7cgyKTaPYREaS9XI57grwShCWyeRKiC6cYUQCL8o3P_slgw-n4c5-yCiS1ONi7EPRGFHrQ3fQAgflS-XFDGhm-r0SgLG7qfgrw1eyzkFx9S3XdUYB5uhkzuQbOzqTOcOoKzy8wj0fJdM6MBhntC7D7bVPRyLAeTx76EG_rFf2aTYMgof8aN5wOWWJNfmtIjgmnsI1QOBj5Z-gt2mZIFsX2NvvVBKOrIzOXEyw2XMxE6lW5NAKZGrtNhJ46uUUL3LkvEhH4vxPYzrSyn0y9AQQjMExhsWFX2XzZIL-oUJ2DyK5YWyX12b6DUC6Yu9IWQ2MEm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdDXXFMpB3twd6F9qcISJUgV2YOkIIh90sy9CyG9vehkL0n4GKYU0VwLCZBuR_EKjEOX9S_1xSgXEDRRudUxfXNuII6WzxQN7tWNSbVaulXf9grVf-05CmJFHCpZCOG5KPx6ajCkr5B6-1hCEkqgVcOfjpPEVz5YuXlR1AGMWEppWQZrvl1FHi76CpQszRnTsLWEaMqUhuMgYBSP9kqvVOlJrj60Kfvnm8A2pBNyfHWnF_n3JWyyc_NvxKl_WJA_AnsvFVFYzMcpA-8CNY9s-Kah26AWqYz89I0UsMZx363YaE5ut2BW5rkOgvt58nWdAqI3pDoM2Hgxz100rflP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJhSaAb7ziiEHhfw2_YdMHkHG1bFR56vECrch6UGYrKX2oNeAjmy3MhHVU1_pwPjcjSS583NO3APUpHnWR3D6R5vE3lIDbHKDOt4G468iGkvHvqQZ5cwrLOa9-R5yUZY7a49iqacY76UOP-s7GwNHbItlLdDNT0isZcqN6s61joFemtBWKsdlV0eyM1dEE3Wibq3ExfdDdOUtxKkwnxioomPOlpncU_-wYCGuJhtP0Lp4ns_Vg6502UN19HdwFlcBDKs6AEYe4d_W9TPnb24Q8hJsmKyK-ePbC3U_1kafOWmCJ70nvercz_cUKACV9YGUkI_gPPDIsPixkm3s1AVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxaaxEk3p82le40iFMOx9ISLAUyMl5khaYWR5icNZ2adCSOCJDFNwMYF1CF89BDK-eN54cEDNDxc12atVzwuf7eHNxAR2th3ZIM4YEIMHVhSF49sp-op_nDeOOK4XfgfFqgj8DdILMiUM2LamwYsekRYBuyC-AomjAQJr32Ilo6RkL20D1TKszXCPV-kmDJB9nGVRMRoy5g4H9R6eWXoFUI2jcPgxt43XuYh5YRdkV-xl9RgPo5ku-94XWPQbqcYF3tulxN4tso4YeEdgdr9pKLV7Myev9P_dJidd1dcKPxdZhf3hipGAUesA6Lc4JPK7yhrAudleYWwZUQkajMqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnM7zZpL-vXBHwMB8jHMbKgKJUtm7fS-s9S5tCYys95-Q9SAXisnaO-b12mcsxMtJDdTM-f-wzBjBw0NX88s7tIbYPlmbYM0XiVw9elRtyE3APKXLuS0KG3aaQUqNVduWLRujzQ6b5O9Ajj8VxOrfq3DV3rwZ4ljLv34rcSqriy0zlt94AxW4jUwcnZHEb7L7h0G72Sq52RluD5K0Nb1bJXoT_7ZOT_hPg4c5lurowLO4yMplnJlb_mls3MX7tYLZM-s0e7Cxuk1HsH1nXkIp9MZ7cSbzKkljwB1hWg-autxDlN98-3qG3rSc6cBUdRWHe5n4kcC3J20eZXqubRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txN6JiZEyrhxUdR3jplFCLHxGpwDWsqkWyB4xJrVO1o9RjgFpgDR8KVjJhf_C9WA7jxgyzoh9_cS-j0tFo-jJD21XYyw-ivZa1YsY8FeWwWsvOizWjKo3QyytYt_eyf94tARuFDP0Kc9ENK037VamdXuZKMGJ7xNhSpSIQg0QY02CsRmFg7eY5GMvcsJ4y5ZAWdq4_wTsla3_1A0oPEqwAlykibmAhaqjlMGYOEykocuqyXeew6oqzgKGQesOz47bMhwhewlukIbvLylqaE969RvgAA7bCVZdW6H_xlc1QOqST7AsvWse3LAxoi-WWZcaEtgeeRymYW-z3dUrk-KnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njm0193h0GBAWTL_w-wMhf8VeXspC7k4EqIxWnAiSlsju-h5mK_0ti8jAy5zFOnR_2ezGbAV0drrit16X-qXc6TrVpUeAKlZmx5hEcke2d0k3xESTm4-BY6VkogffYvxxpMCThQNL6IooYSNZGQNPlya0xmDg_dF28_cr102aqaVzpZYq5MUx7L5PEXHTVd6fxBhS7lHJTmXfSStcVv5aV4GkUMRLvJHyTU7UhQz3POOc6qTghf74BNeWZnejbR5Bu8gLHK4WxPCyuzKD1Jq3FORJDVhLO8jV2B0iHJp1iMMt980TBGdL74VSKmvEhjGcAPw6SiQ1txL3euUapdeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90320" target="_blank">📅 10:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVJCVbLBYpTYneC7vx2vYNOJBqAYtWPTcPjH9v8s4g_adgEVKFVuqQuZr0t2-gjLaGJao7zsB_B5BLPCS-7Fl6vmZXEm0gXEGG4BpKeI2yr95qe5jxueTYEC3Ym7kkJIYiMvUTFaRladNWf7_tOJN0AU_fmV39Lqx8kywPDx1cn3JOZ1fqcasUoppkpr2dlkLkMMtmSZZxLUh6sT8KgAj32s1zOVZgGyafSA1kTSgi-tHM-v2dpTIjOYzZ5AoyuhZbnKqJe1Yf02VR1vpp1viaxo5AdaYC2rV1DiYJT8fnmweoj-7FJafqPbbwRASdyBb0i9uyurEvFJ4tTUFUW8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=qg4OR7h2557fWKWNl8TXg-6i2vn9Ao465ZD97g9DCpu82X_fMO62D9iGI1ojEKUiDtpiVg8uyGlnmbYTuNK7cQ9JCbSniAC0gvH4wyJubbv-FdesdsUoxWKXKRHKPJADFZXSRR7fR8s0RyJFij0NJThbYf_VEq2WV-VuZSLkv0RBoqocGzw1_K5N1M30rNGrR4q9YzhEjqKPyA0Myy3rdBx90nQAzCCOctw0-xvmn2xGwoSVDRMK70u9zIkI1jyR0pROVcW2ZndmAkFHqHlUidThM3-BWdmRQHnEsMj4mLXCtBH5x97Ati0FYJ8i1rAvLtmvPPP7g7Jlek-WkNdqE4v16gJHuDQQVPG3CJtgiC757qppjo3uaHqPx8CCIbPZ9SlBqP4cygJBkDZ8zzgxnao3A4VGcsg-5dfpwiP8J5WbswXUpFhQ2x6zxrLrsJTNP8kwf6H0JeppvLskEZnDsiI4_tKrwFTtcMct9mS5cS5gRmg7_AT96EMt7YflTTjtyHQZhlIXFMQ2TvYa25zLbhuw375jhH6KPunAczrZPuOxOeWlSTMBXFhdrpbzsnl0qAFzs5Z1Xk1mE1IR1o0R-sPzZAGIbSew5e2QMPUMACUB2nGMS_Q1bxthOGOJF34yXQ-dyTwu5j1LXuh3t2uZSyOx-95SMB9EnqEB_VKa_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=qg4OR7h2557fWKWNl8TXg-6i2vn9Ao465ZD97g9DCpu82X_fMO62D9iGI1ojEKUiDtpiVg8uyGlnmbYTuNK7cQ9JCbSniAC0gvH4wyJubbv-FdesdsUoxWKXKRHKPJADFZXSRR7fR8s0RyJFij0NJThbYf_VEq2WV-VuZSLkv0RBoqocGzw1_K5N1M30rNGrR4q9YzhEjqKPyA0Myy3rdBx90nQAzCCOctw0-xvmn2xGwoSVDRMK70u9zIkI1jyR0pROVcW2ZndmAkFHqHlUidThM3-BWdmRQHnEsMj4mLXCtBH5x97Ati0FYJ8i1rAvLtmvPPP7g7Jlek-WkNdqE4v16gJHuDQQVPG3CJtgiC757qppjo3uaHqPx8CCIbPZ9SlBqP4cygJBkDZ8zzgxnao3A4VGcsg-5dfpwiP8J5WbswXUpFhQ2x6zxrLrsJTNP8kwf6H0JeppvLskEZnDsiI4_tKrwFTtcMct9mS5cS5gRmg7_AT96EMt7YflTTjtyHQZhlIXFMQ2TvYa25zLbhuw375jhH6KPunAczrZPuOxOeWlSTMBXFhdrpbzsnl0qAFzs5Z1Xk1mE1IR1o0R-sPzZAGIbSew5e2QMPUMACUB2nGMS_Q1bxthOGOJF34yXQ-dyTwu5j1LXuh3t2uZSyOx-95SMB9EnqEB_VKa_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPhbW6QN-Gx70VU9sJJ5Xqjo3dUPcv2dDGXiHZpLJ9UwPL_Busu3R-e3kojRdktlELgl2uhakdRVutcChVKUZ6DnEG3tU0OW2qBN_jys1c9-K9-WUlnLHZRHBYQhoRjS3Kae1G9xaU7aBzs_2aaPp69jeJYh0u0dyqHCsjhgdrPpOe12jatZ7fYlL5b-IORHzNH_m_qvESD3zEy6LzOGNViLCPaETiiGozLDJOYfuZ4sim6HmQhsFNXhfeGe-stzP94V9pUyvEvKDI1XZNEedmU5dLz8zfHFxeOg8ALemQQ1J6-FX30sAD41N82wda13xbgs9qdG5LJ2np108Ti4BTHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPhbW6QN-Gx70VU9sJJ5Xqjo3dUPcv2dDGXiHZpLJ9UwPL_Busu3R-e3kojRdktlELgl2uhakdRVutcChVKUZ6DnEG3tU0OW2qBN_jys1c9-K9-WUlnLHZRHBYQhoRjS3Kae1G9xaU7aBzs_2aaPp69jeJYh0u0dyqHCsjhgdrPpOe12jatZ7fYlL5b-IORHzNH_m_qvESD3zEy6LzOGNViLCPaETiiGozLDJOYfuZ4sim6HmQhsFNXhfeGe-stzP94V9pUyvEvKDI1XZNEedmU5dLz8zfHFxeOg8ALemQQ1J6-FX30sAD41N82wda13xbgs9qdG5LJ2np108Ti4BTHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjufPDBxKwGUD63XwyUWUFlJFga7mXsdg6AHmvV44BrW6rnlozEA60YzbmDrib2Zupv_dn7072KyFeqiXJ18a9Brys5hmY6e0s-YBOdltyuyy3Dmqh_xOqCrmeye_whvXENrbcnvA9o11XFagyhepECK-PO9NfoyVKiSBSuO5WnmDdb4rxiChHlE-hfX3j41Zrt2c35SzuYTlE8Xf1q0SLc43iZuZeD3FZTKZuQd22eEx3MfXFqmvn2FgAO3grLVE1Mg9eNz-pbmtv-rk8U7-P6paX87oOlO8vyDY0zt5apBjB9cIXDbusMkoQkrPV9G0l4YhkZb59u9Z46z-mB4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cryH-QhCE8sUDmatgdMxpe2Q4oLSwDw52IoSESIxpnFqIszdNBQkei3peZg466yY0gEjwrgG7McpqZqNssbqXljaVMOJ3iFHfDiJMLZ8zXAuwGcZBNjFMvtAjjXS_7BHfpuoxH3QS0m3PPfs622oEI8WsdJuK9bQuL99XTBon4qrv6mcWFmA1dHRmp-CXNhGl2G5i6vyh02gjzo7Fp_x1OzLZBQPzlYnd1PZXUyP3zfcMhg1TMWKDYYYOAwJj_2WQaoSVD4k8jN3lz9HIdWVaDtw_MrQx0w8-63Q6i3WDg67xRekbiCyuy7O7tvv6bbUyjqTUcZsnQAHHVgcYuYiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM4L3G9lkbDzEnAe_sQB-ZyJYJifTu1l2yP8OKcVx1-MWwjwaoLBfTHKK7VgFyCBlzhuR008gAxaMm14OZ808OJ_Y_IYT9CnasCg-cdMju3vKPooXsrJB3aBSadruXfFfulQeLFBiU4g1BFIXJn_Saq4AvH3sdgtCnIsWfFolUl_VmmuBAmt8UX8VIuDMzc6mzHKV7KGhexoQq3CbuolFphzqVDmYDTF8sZ-YynUbhtSYep96Tedr3ZJo838HRfbIm4vnd0_aytNSDt9hF70ShUskoBTRkuhq3vFfIXO6NtcvV21YmedFQpQgx17nD0CnPXxKI1yyTZ2FvkMbGPB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awy-YlGun332zDlrOdiVd_jCv2kOb5HeY9LXm65XgA4w318K1hNSMRmmv1VvJPVjcLlvEXtVjNBZFJFYShPXSB2RZqmtqyFbsBN2p1RxPJFSYA_HdHXizeOBCy9MXcEvZBXHp6WQPBLu9nJbJ2-9y0ifg2glYPOHHgTmHDIFJUkIKa1DmPUUZkn6AX9-1cJp5ri1oBfLSPyEyQsq-aE4pXM828JNyQRReR3J_wZDsL5QolfOMDkh6-mjLrsLON56UX7cyw1oOL_owPpX-yTEY_QGb9m5Hf58ITGXO2iR19EujZG8XnZ4Ct6DhR1e316GhSFJCS8wd2BYZfzfFIJZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfaCe4cy7EZVWFOqbUZSh6MphKS6aWHeD7tQb7Dfz9oFXNbkknjR117Do2PJy8GklTvs60u5Qqbhrh2JNkmrCmUJer96tcV_3lapPDs_zTSyxyNgG4IUhs3CLr6B2sVL_uSvXA-m_qBA251Q78s6eyT3qy0BFIeBq9EWT5sHNpGJO9u87kXlyNf4DQJmLWnTeOCsA1HoihgDrnBE6IubwZJatpFvTeYjDAQQWhjFZBpD8zxCYi4xw-CLBFOPYkm00jN2Z_j9dwIZMBoOr2nkLx-q2v26wec1scxJt0A9am2fDJzXfp3HxQIv0cndggs5OYMJfutEKvJ48LAiz0v5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=gfazDEe83wZs2IVMe_tGzIR6_y5y8aoxwEyEePcw_EaFaOd2OxhLSbGjIsYsxilY7sGFFEnFDChPVTpb_7grVFjIh8AaBe5UeJfNJOGLxgD1K493bjxyLpP5d8H1x83NgAahvsVbdzb4ZOluPg2X5XZTMjcAuvXz_VfSDNz_jElSyd4vCdhdcpqIy_kNWswx_aVEXc1vhsGMESNH379TubeUP5sumcnvDSmP6-6-SYkHfjnqTOnc49E3rSPryPZQU_dJwGLZFqBOYiil6MgvSt8IyWZaHK5x8kFJ7DDPIZsVIM8xsyr2ao6hiqAgQQnbqthXhfmZX0ebXBtlcrGhVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=gfazDEe83wZs2IVMe_tGzIR6_y5y8aoxwEyEePcw_EaFaOd2OxhLSbGjIsYsxilY7sGFFEnFDChPVTpb_7grVFjIh8AaBe5UeJfNJOGLxgD1K493bjxyLpP5d8H1x83NgAahvsVbdzb4ZOluPg2X5XZTMjcAuvXz_VfSDNz_jElSyd4vCdhdcpqIy_kNWswx_aVEXc1vhsGMESNH379TubeUP5sumcnvDSmP6-6-SYkHfjnqTOnc49E3rSPryPZQU_dJwGLZFqBOYiil6MgvSt8IyWZaHK5x8kFJ7DDPIZsVIM8xsyr2ao6hiqAgQQnbqthXhfmZX0ebXBtlcrGhVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phSzj9t7Mex-IjwDU55slHzAqbdv__pwcfzCpfdjceZRG6gOvpVVAGCrOtBnSZX5bq6FAi6nQkC_JyR2PVgcfC0Q4Lm5enN_wr192Z3qmY9K2Dq8i-gLp9zqUXebZ0Ev6cDGHC6tBhmFNVzLm9VB8F4Qxc7-l6UrZ5D_6brkqK60TASXr5n8hDemyHjNX3qlYqW8RMYPbjv0u0cRJNgsLfJqmx4cyWsuD2sxjwNyWwvZwe1njPy_ToUW0N_FN9UXIFLGlvix6MfCfFtjvzICbFci0P9BMYuNeQ08WOSp8-Id3Wdi60BLTYi8CWvpUIltfxTA-vbTa9vpNb-AWHGkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=MhnmlKlLWUvIf1O72Xj5EJH289WfkuW9TtTByzLVuy4zp-BoEasc2vS7BBPlh7u4BSqEqcPdRIjAxrW8nNLqHLLEFy-9EMJdr3hLPpgAlftRhXvADLDRKRc_HWoiYFDhL24YoWyHJrUpEYuWY21NSPASZNh9OYsFZ28PyKTBjyyyUs3kQK-MxDWcojNH9EtClNpdJFNS3hZpCqe3Zt2IJZAfEDUdQNXE9u9Ywwf6lHPOd6AlkbeVuRfvGG0qVs_FHGngX3XMkxmzuffDJvCLf3PLFIb2lp99tcxQQaCR2zn6r_vltW6xWYAxP4tN_XD-yEi7c26ieVvsKOHvLMZMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=MhnmlKlLWUvIf1O72Xj5EJH289WfkuW9TtTByzLVuy4zp-BoEasc2vS7BBPlh7u4BSqEqcPdRIjAxrW8nNLqHLLEFy-9EMJdr3hLPpgAlftRhXvADLDRKRc_HWoiYFDhL24YoWyHJrUpEYuWY21NSPASZNh9OYsFZ28PyKTBjyyyUs3kQK-MxDWcojNH9EtClNpdJFNS3hZpCqe3Zt2IJZAfEDUdQNXE9u9Ywwf6lHPOd6AlkbeVuRfvGG0qVs_FHGngX3XMkxmzuffDJvCLf3PLFIb2lp99tcxQQaCR2zn6r_vltW6xWYAxP4tN_XD-yEi7c26ieVvsKOHvLMZMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=EiSFRDM-ygqWF84TyL3aP9QeAx6R3zOKl_VpsJ4dQ-3NKEKxchAiNf_VptrKizpLSA9TxnTdj40XD6-6cyRvic0dU8s9fIVbXvpp915a1JCBUCyfhRkoxNanf988OgDE9tJQyZ0ct5J6hRAwJlOvdnOVhNr4AdHHfxunTA_yRmJ2GgDKqNKXViYfFkIVBJIlE5OHOmMjzPCtlZMBvR0NjGTGepayvyb6glPs1Rx5vf0rWNEHt4dRqhGq7wWmolRWREs7GOqCLERfUMIK_758YtePv8NNDgJlNaSUIhFCrJPiZa0B7aykBT3y8pLzYO4wolr0XY1n9-VkD4tUS8vdrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=EiSFRDM-ygqWF84TyL3aP9QeAx6R3zOKl_VpsJ4dQ-3NKEKxchAiNf_VptrKizpLSA9TxnTdj40XD6-6cyRvic0dU8s9fIVbXvpp915a1JCBUCyfhRkoxNanf988OgDE9tJQyZ0ct5J6hRAwJlOvdnOVhNr4AdHHfxunTA_yRmJ2GgDKqNKXViYfFkIVBJIlE5OHOmMjzPCtlZMBvR0NjGTGepayvyb6glPs1Rx5vf0rWNEHt4dRqhGq7wWmolRWREs7GOqCLERfUMIK_758YtePv8NNDgJlNaSUIhFCrJPiZa0B7aykBT3y8pLzYO4wolr0XY1n9-VkD4tUS8vdrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=OnrPUIZ1GHTfg0_X9wWRyVxTeZ81LXVhQfF9Lw8INaXP4s88zt12c8PH0a2Cip-_UkylKohD8fAgYouGAuFTIXMMIl7slWMJR3K55f6YBTCr_hWL2WvkICazMAFjCQ0sF0f3f-xUn65CzfA7mzwTK7FZBZP2lgq46n8Fh_MztirSdvlu6WIJ9Vf6KZ-sH32ksQm-Tl_ePZOVUvfwvfE6-uDnN2wuGNWY4rNXC8Na0JGD9gnn75hDAY6riFlUsrpjeBpUnTO39eHeYL8oWaMl4-ZlgBcl2dMxl0JpAHmwhTr0Eaa7P-B4jMmtbg-avUbBptBNMYhgFsIOy7-0j-6PJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=OnrPUIZ1GHTfg0_X9wWRyVxTeZ81LXVhQfF9Lw8INaXP4s88zt12c8PH0a2Cip-_UkylKohD8fAgYouGAuFTIXMMIl7slWMJR3K55f6YBTCr_hWL2WvkICazMAFjCQ0sF0f3f-xUn65CzfA7mzwTK7FZBZP2lgq46n8Fh_MztirSdvlu6WIJ9Vf6KZ-sH32ksQm-Tl_ePZOVUvfwvfE6-uDnN2wuGNWY4rNXC8Na0JGD9gnn75hDAY6riFlUsrpjeBpUnTO39eHeYL8oWaMl4-ZlgBcl2dMxl0JpAHmwhTr0Eaa7P-B4jMmtbg-avUbBptBNMYhgFsIOy7-0j-6PJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4o8T6ZJ8CxDmgMQcgs8tv8_xMluHB75gpCxIZPDdKkLRWwigyQjpGFgkGf-LbxumZTBPBTYeQwvKUJE4SKW1Jta56NsecSUSvu03am2WCfEQcVeLagSDLufp-OrT9hiCU1nT6gW6X490JyPBEnDMr5HvZbUHyfH7FwWbO5NEt8WE75kOYcg4MA_rq0bqMfN8EpLkrn7NeXh6QE_MJPa-3hO0CrxSKGuYF4PifQY2M1-D8xtWXrHffIHUMVgG6yn2ge1tDs7f8_dU4hjlMiDq5R9H0ehBlMeDj97W-XAkYbEFpqY5DwJI62uJUiZMtgMw2EbyqGkS3_lvNGwsVdMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=OUiPrUN5dEapgR2aTx9sCSMqrP2Fii5eKEIBOUNcvWDARVFmU2jo2qUu8TL2W09IgESB_jfgqjqMgarkE2RSMEy3Mgy-a6uVTCIbBgmq7vjHgVPHthlqN42BwymHat_dY4ReqYHpn9UQDJf-OwPgBTjsznVP4EPXhIX3RYoZWp7SLWjACIXGoraN__2pF9tB1UFdBHCBHYrfCdefGhpzWn5O_nGh9TkouSC5pWtwa2a1zXqS_OEWpk3jffqgQSHp-aRN4VCbJDoFzrfwniAEhCWrIHjXyRXQ-RtgbJeSooIdkSzXIC-iXgOuxLZOqUKbnoPpWdPOG8s1N2Zbe6zu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=OUiPrUN5dEapgR2aTx9sCSMqrP2Fii5eKEIBOUNcvWDARVFmU2jo2qUu8TL2W09IgESB_jfgqjqMgarkE2RSMEy3Mgy-a6uVTCIbBgmq7vjHgVPHthlqN42BwymHat_dY4ReqYHpn9UQDJf-OwPgBTjsznVP4EPXhIX3RYoZWp7SLWjACIXGoraN__2pF9tB1UFdBHCBHYrfCdefGhpzWn5O_nGh9TkouSC5pWtwa2a1zXqS_OEWpk3jffqgQSHp-aRN4VCbJDoFzrfwniAEhCWrIHjXyRXQ-RtgbJeSooIdkSzXIC-iXgOuxLZOqUKbnoPpWdPOG8s1N2Zbe6zu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILc28AzNZHln3B-LL6QCmslU7QNxbDhOrYmKEyL5u31snGa2aKb6-uYLXHCwIulBINmDRnlCftkVUj0YSjaetOIdgnm8RD7_zDqr55cl0ZZgPmhMbczpAH1rPZ7z3WEJ2_5n1uBw5ycibbNOrh-ybsGhH7GW6E0dRq1LACHnbFH_ADK213HeB_-t5yPa1ZTDXIxNflpmBtNshZhpm1JyjOJXgU7RYyqInfpt52om7ut_hghNjgL6qjnA66FUZ-J64mPt_77Mrjg-iLOraG-RGIiRUtHp18JLjh6KTyltz578SqmmYhNAxciCGbo4-oOod0kp4wgk2oVLK-gcx9rtLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3qbrxMEcCKxNtKvuqAK2hYWR36xtSbo0Uirth4acnN7MNRfIplc4CQ7KdEWYTUOdZi6CIyA5qaSqfARFLBORUKUdTCeuI6zKhQ8tpdEA_XrZNlTUfunaMikk2PbSvrbRcXGxsFSUn5eGaEp0ACTe74uJXj6Cfzn3OWSMuH80oXBVuJdAHdNmrUg_WhehrkqcFwrLmKnYoUjEnaRZ-nUGVlqqLbM-zEThTdshk2W6U2JLNSKIbyO83mbVSIkq7tOrpMW81ylJum6h8dq83Lxhy0vVDZ2gLm2RIRLdqMDURt3fQgww-JAsGiisDj5GiatWhAPkzvUng6vSSJ3QpyXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pZPm5coajxUbyvzcEd8yL60m7vhSHXV3VOAq0L5vtKv9tKDqOaQwrrR_maVMxVITuR7z3BBHnQzibVTWgo1-VnCV8D2HqISYQFxaVN8PqltaCUDfK0jTmt51BOh_wtjzlPB0XbMw79d8TC1iC3zxQCrMnFFaooBu3YSLXiH4Ptr9lZQjZqETw0fRJ1gVEnB40IzKcNBiaFYNpZNK0bS-gdxzHUlwZPCL6Gbou8qjlmJnAxOtspapWYa-fC4udHt0I_MzLVdPaXfyMaDiEccNwVlMkeYPJvo6Fe7gl6HE0Xh0EAse1wV3rS_oCXNCqWZKE_ClcWVz6JXBMi2KDhpetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pZPm5coajxUbyvzcEd8yL60m7vhSHXV3VOAq0L5vtKv9tKDqOaQwrrR_maVMxVITuR7z3BBHnQzibVTWgo1-VnCV8D2HqISYQFxaVN8PqltaCUDfK0jTmt51BOh_wtjzlPB0XbMw79d8TC1iC3zxQCrMnFFaooBu3YSLXiH4Ptr9lZQjZqETw0fRJ1gVEnB40IzKcNBiaFYNpZNK0bS-gdxzHUlwZPCL6Gbou8qjlmJnAxOtspapWYa-fC4udHt0I_MzLVdPaXfyMaDiEccNwVlMkeYPJvo6Fe7gl6HE0Xh0EAse1wV3rS_oCXNCqWZKE_ClcWVz6JXBMi2KDhpetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=hSDrJkRDhPJ85cWxB2deQwFwvmo4XeNACmeaYogbC3mBbbue9mu0AOWa2btGO5FsLklIKgsW2xDtUUN5eQzGoxEpG6c6dUK4i4Y3CwINl8faE4oeQab-MLgM_bBEhTXCeDPpXSY_Q9_1AXIeA9P26INAYYfDAei2HLaLMyqQTrSTExqyj89Qjb1Qq81IgsXlYsOgNfqxrG7W8ZeINi-cZALqMkdHDo9qKQueCnsSm8pEhFG2SKHqIb3AOL4fjv3I4VTgkjnrk4ZLLamrs4mNEnQiJmBhjHqiyQT6Umf9RtZ5bDOsWf6KUKtmIVaKAakaaJk8DjRbX9I_HbJTLQ9isw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=hSDrJkRDhPJ85cWxB2deQwFwvmo4XeNACmeaYogbC3mBbbue9mu0AOWa2btGO5FsLklIKgsW2xDtUUN5eQzGoxEpG6c6dUK4i4Y3CwINl8faE4oeQab-MLgM_bBEhTXCeDPpXSY_Q9_1AXIeA9P26INAYYfDAei2HLaLMyqQTrSTExqyj89Qjb1Qq81IgsXlYsOgNfqxrG7W8ZeINi-cZALqMkdHDo9qKQueCnsSm8pEhFG2SKHqIb3AOL4fjv3I4VTgkjnrk4ZLLamrs4mNEnQiJmBhjHqiyQT6Umf9RtZ5bDOsWf6KUKtmIVaKAakaaJk8DjRbX9I_HbJTLQ9isw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=mhD9avwYjZx9iYiROHmrPENaZWQmn80gAQN1iw9XWr6EwrOrbU2ldEvgqzDdoXlGJ9b8zPZ0Ud6EAzyDsz18ZwQ34HqF-GME_zmtKbzky6G5K13EG-MhdaWIa4vrbQcF-lrNllfop5tumNOq9Y99wO9K2fpb9jNdEzdEPGJp3eNs5fC5YMaqi1U8xCsUXn0VKQl5pgUiyamd7dOBa-75TJyoTKFsJAAimBp7IydxqAQFgTLQ9ISubP4TrzDqjyi6t6SPFCaJePtXIdRqTEunjAtzkRhU1uwsVhenW3hcwChE6emmpmEnzYuyfAjaS7spERsZAgk2H9S_8yMqGDoLlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=mhD9avwYjZx9iYiROHmrPENaZWQmn80gAQN1iw9XWr6EwrOrbU2ldEvgqzDdoXlGJ9b8zPZ0Ud6EAzyDsz18ZwQ34HqF-GME_zmtKbzky6G5K13EG-MhdaWIa4vrbQcF-lrNllfop5tumNOq9Y99wO9K2fpb9jNdEzdEPGJp3eNs5fC5YMaqi1U8xCsUXn0VKQl5pgUiyamd7dOBa-75TJyoTKFsJAAimBp7IydxqAQFgTLQ9ISubP4TrzDqjyi6t6SPFCaJePtXIdRqTEunjAtzkRhU1uwsVhenW3hcwChE6emmpmEnzYuyfAjaS7spERsZAgk2H9S_8yMqGDoLlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL5Y9UsvXSiSG_0tZRhov8_pqn7mQI8_oTjU6q_oKY07S5fF6IgGDtiHLIoWDIuduY77brWqRwOSUSepOg8MzwkCBmJ2oPOQhnuKTbA5vf2oDkVJG8VgRVJ_BpxB0-GHXs0YJPrFqZP5sz1gR4xxE1BmJPbNV5ecWVz-XPragIFsdaLELClK2X27K-Zx0lN8B8HUjoRWiTMkYI_bzODADrpJkLJhuMGLJaZEeo3uLNQXSI07jUD13_sObvpHGXOiDahuZsaB0xqoVksVh8nhSREojkz4qLAglh8xFg9tZBYTn4if67Uko-CBdXftyOgIa9EBMqvtGGLwFvGRDPhE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=kwnczwO4_SPlb5vMcb6BClMdIK_ge02KtmXzcDGvTWV9ju8P3GooALr-rKCeKIpWiphgxIlfaWxZCnvXPKktwbyB9fag-itVqUKxAH9ZnmLcuyiAeTqibyYyEs0-PH2C1G1eRuOmhbmW428Jf6CHNEKOyeoossDbrNtjhN0ahAHe-ZVaZypsFjS2yspr2f4UFn2MAsxPovkXjcuE2tVzeQTzJrfi_zGBCD0Xqx8MNEMwG38huTxpVk4DQ7hnSlCxoLIG0IdU5rvp7qVv7OJoJ5eW6jr5T-pn7uhtTALFjw31LbXYeMnHCeFi2jR38Qhb-_eKnbvb0fW93IfX7GfpLD2BT8gC-cBLmyYGpmdg_BEq3ickHR7ZlQkuBPtdTQ1UgDOgs_62QTVUJSFPX5wZa7L4hTjHIY8N7CsAhGmNGB8J6_hd7_M31tMh_W099dt5BgpCIGiI3XMihOSZQnWy6Prid4QxX27ZIRU65EcVFq5m_2UFKp37grHTLBlLNHgTZPfOWuQyM3iCXliciaxkWHYqEARKDjjioGP5OXjMlCewBD23wVdri5cClkBL7ys5sSwxgjHflSn2tzGmI55Cy3p0OjYIr_hf4SQ5azGfS9_yQASEcTR-UTiRvDgxoRbWJ_MERpcALciOzNO-1gfpOUU-BdNumC3iJPy1Ini0zco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=kwnczwO4_SPlb5vMcb6BClMdIK_ge02KtmXzcDGvTWV9ju8P3GooALr-rKCeKIpWiphgxIlfaWxZCnvXPKktwbyB9fag-itVqUKxAH9ZnmLcuyiAeTqibyYyEs0-PH2C1G1eRuOmhbmW428Jf6CHNEKOyeoossDbrNtjhN0ahAHe-ZVaZypsFjS2yspr2f4UFn2MAsxPovkXjcuE2tVzeQTzJrfi_zGBCD0Xqx8MNEMwG38huTxpVk4DQ7hnSlCxoLIG0IdU5rvp7qVv7OJoJ5eW6jr5T-pn7uhtTALFjw31LbXYeMnHCeFi2jR38Qhb-_eKnbvb0fW93IfX7GfpLD2BT8gC-cBLmyYGpmdg_BEq3ickHR7ZlQkuBPtdTQ1UgDOgs_62QTVUJSFPX5wZa7L4hTjHIY8N7CsAhGmNGB8J6_hd7_M31tMh_W099dt5BgpCIGiI3XMihOSZQnWy6Prid4QxX27ZIRU65EcVFq5m_2UFKp37grHTLBlLNHgTZPfOWuQyM3iCXliciaxkWHYqEARKDjjioGP5OXjMlCewBD23wVdri5cClkBL7ys5sSwxgjHflSn2tzGmI55Cy3p0OjYIr_hf4SQ5azGfS9_yQASEcTR-UTiRvDgxoRbWJ_MERpcALciOzNO-1gfpOUU-BdNumC3iJPy1Ini0zco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV-cJmCgVb_xtCbGqC6ADQohxu2jUGzmd-d4KPZVmWUS9U_IGRMtlw_itinJKw1NOrnjM5xKUtwZ2dlb6CGfOn1dw0FXq5iIgnyi1lB8_n3E6TrS8_U4OqdQre5hZO3iLfAw-R8awOzMIiaY39D1tATCoRm0qnsMZikw7LIXI2GkBPq_g-YITKHaqEAXe8tva_Fm5XZgM15HBD_DdveEzFMXAFwFbzoYQlAoVV4TW26nC4UiJh4OoZhf9_TsUIbgl6kc2ufXkc7IypJZh7UzXxy3hMHcyD6ynAL8_UvCHUn4LBTNM7SxZ740r3LV_kyGKGdapTzhMpcOdJpDIuD_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSrJFKUAqvt57yG_IJNqbLELef-Ie5fvzl64FxIjLGizPal-usaPLPUT4UrNRM-LhyBoAkLPybK418RsJmhNk5XQ9LtuAdvckPoAem0SciQllfTNPkOEcdSRtJyxFOzZScLeqeswn7zoraxKBlMro1xe7fZ76ln1MXW4kDofO9L-nVgSZXRFY6GhvGk8e_Z5VjSyr_Hp-UzHhuFfphwo_0g0NYEJ_9XGZfS22pdBqP4li6kuKOjlmzTD3PnpBHbvfWk9nmcRe2dpVi4-Hr-MaGa0HYkb6VYHHRV1Yr4ISSgE8feJNyoUD-ZXEEUtilC1paCSCgyOEPZtXraynVAsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsJ6ME1ec-PfV_ub8nQ4CSU8H4t1r0Ec5XC2O1KM38NLFCqZCr2yTLIFy-v4LX6SXy5kAg4p5RJqnb2R4v4sQzLcmj0KU5oHEFYYZmFG3wqN_pdeX9awvGVhOwZN3cjBdOX5tI6aH6Ja_TcgrVIs0pBVzeZNzAn00gavsVdL14n-lbrOR68fPIs5Z_siBTvNFoVLTMJFw0IJmAI7KeGW78H7IedJvhOyzqoMZlvMzBlCDhVhWtsDSC5AwgTLaAu3127Py3gCpcHGiM8R-MbPCKPoW4pmYlHMuNenjGAIXhlx_irJecbIneQdKW5dwN7DfTUxk75jfYp-B55cq0bOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1H7gf7sclWcjI_lVbktFJyHotoQCmWb5Q08n0fLnUr7OyWEP-DB8-hb4dmts_PeCFLWIGB7m_xXzqhNqoIo8Gzr6-IFPXc6Gc6YWXnHQ0a79QQl994-hHvGttr22fuWxKmbv5e5FbI4TVrgHpPyhwbocIkZ_wPrAkmxUBS3iVfp-MlxcsrsrR_4cO1HNEIfQ6rQ4xBF746QXAwRhH8-Yr_HzYkMWCodd52VTGmyWPmxnrPGyWLRIc9G0lPiZVjINaz8m3i0KRKh9uXaf9e2xVyX-m7R95kkqPiFaVUHHrVcheBeBEfbF-oFnFoVWy7Imi6MrLZfw1fD9blN5W8hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFHzSxs7xHbNJEn7H77GIpfpVC9MKFCMjydqeHUcY8mh_hbG3yZdKprlgIDllc3-wcHjkJFF4YIE_Ea2eFx3GAZiFGJ3poyluLLf4tFbUZ8EvOaMJebzKWIguAoDFHNcYV5Nih_KR3MYh7fALF5qNWUGkocgmSgJp_o6YrEuz4tmJmupZIRDY6k3RKBmd1issKYQJLAHEpBOWvYuOtkJAdV-MqYIKsUF5EtZJkvDUflEEP2ZrQb70CDv_BOjfC8DjasGPOm-Fj4SlmX4xqLN3gH4gxAlj0w4C8P8W-GnYEn_wnCS7BUo5rGkLLP6J9WBru0AShdMqZDpeimO--xqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX8wjKbVcphBfzmcIxrmfprSMHhWVKdVCNLQHJMotbVK0YEtnZRSTwMJXwga_2k-_qQxOnRKSc159J7j7MFgvvMKUnilGoZA-KGAvxZ_QVWAdlN48tp8zLVzNbSWrOAEh0J_IypnMZRBxI9YR-dEozSn1vNdEDqYtjW1mUuYb76HK2d_49IWPBAoBUwFdKm4os8xPbWWWgBHd9lK6pjkGkUuYeYz7A_aRtUWth-DwvpvOnMmW1d_IgWxHyQHFM4e0eFXnF5H1togsarPSH41Z5TQos_wcM652gP4meFBdRLcuZF5kP1wlWNsyje177RVYyHBCzlIWdmQmqfnr6lsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=E9QO0_BA26XU80iJAGYECfViGiM8_8-2aq8MFe8XMOCOaTCM07uG-gHuxyM2CjwNCAI2SodWK-du6wBhqLIU65K2NlYQw6SJn6RqesML0L0YuJdyHTeUO0l2NLD2UxQFX513aJDetBQGJZjBKqV-FvziPjZqslYXF16fhO_cYRV3TvEb7nTC_lmr5K8u8ynC5bNhcOb7Bobt0t9X1uvtSQjy2aphhJ7MY7Cu4WQSTM3485MVNG7nRSibKq6o7fZTrhKDI3GEubCi1WJxAc9b8hjN3xtcU9YIYcLC1cyTN9XER1ZzNiYQQe1FpEJryeDYWxbZIXHPKMHTLuGM_t0wHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=E9QO0_BA26XU80iJAGYECfViGiM8_8-2aq8MFe8XMOCOaTCM07uG-gHuxyM2CjwNCAI2SodWK-du6wBhqLIU65K2NlYQw6SJn6RqesML0L0YuJdyHTeUO0l2NLD2UxQFX513aJDetBQGJZjBKqV-FvziPjZqslYXF16fhO_cYRV3TvEb7nTC_lmr5K8u8ynC5bNhcOb7Bobt0t9X1uvtSQjy2aphhJ7MY7Cu4WQSTM3485MVNG7nRSibKq6o7fZTrhKDI3GEubCi1WJxAc9b8hjN3xtcU9YIYcLC1cyTN9XER1ZzNiYQQe1FpEJryeDYWxbZIXHPKMHTLuGM_t0wHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=BeXxeTI6M1S-NLsLJMwO_GD8IwD9Q1t_MWycqjW28zyhFO6dAuGTdRhkcOWMYobCyXk01z4IKCxUWT8qNOykeQcOD6hKMovHiePV5LaXP35-rTwEmMczIekwRshTpvMkqWShut4qhSgdjyzygpKVOLuFsUZGUsqYGbu3V4mSgii4MvOu2jpwgkKkkmn0lY-YQD-DeWM0WyhIcd80OkF5ZKbYpe-SM11LOAzR2cUAHRA-HfNpNUS8WFjkelIDP0yqf6mLLQqhJeD4YWBiRsTAsHxNQV8jhQifiX4JLsiVzG7R7riGsr740Ehgxkisc2ukHrTJ3mYMGR5XDIjZNo99uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=BeXxeTI6M1S-NLsLJMwO_GD8IwD9Q1t_MWycqjW28zyhFO6dAuGTdRhkcOWMYobCyXk01z4IKCxUWT8qNOykeQcOD6hKMovHiePV5LaXP35-rTwEmMczIekwRshTpvMkqWShut4qhSgdjyzygpKVOLuFsUZGUsqYGbu3V4mSgii4MvOu2jpwgkKkkmn0lY-YQD-DeWM0WyhIcd80OkF5ZKbYpe-SM11LOAzR2cUAHRA-HfNpNUS8WFjkelIDP0yqf6mLLQqhJeD4YWBiRsTAsHxNQV8jhQifiX4JLsiVzG7R7riGsr740Ehgxkisc2ukHrTJ3mYMGR5XDIjZNo99uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5yUBfAeuRcS0M55tdaA2B1VaNpflWlwyyG10pIM-3Q8lRDGwu9cpETCHDMHbRCyL6MHKKLdEVKEEet4Dlhs4SHTbjM_GSHimscAVG_vAQ_PsNmwOV8GyZNzU3zDM0Jj0hRL8X_y3AxlCscjti-CmHJqWpDqQyak4KRK5HTrp9UFZDY7m5JPMEhhbiZZ6dFsDLodMhKlF-eQiOkhQGfBf7fcKy1mDYAdHSCn46UMhcpltEtfEO7NA4Z2XP_gXwmDtE8LXs0olq8m4zyXGCuWuqacYRja_n3kIlbSD3f3OIXFfLW8WgJAxvJFVn852vTAGmc5REnxslBQmkeHbhp_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fydjDyIyOMwWKL-M2J2wgC_S_a3CPhkegrMLVX9KP1IcZaF7TV0o9GD42DxqPRa4Sl4q1y5vZmTtkfpOz-zeNHiGjpyx9FWaK-R2hvn_tF_Wrpv3VTDlaEtv-xQACCAnDjmV6m1WPh7EU_ubl8Ml7ueWnM5eqqqdRzU_WvpbKsqCvIu5LaVxXf03U1ItRm2s3DK3Alc03LiMrrFooPE2VmOHu25qLJbwbrT3S6o8GIdCgmSR7-CcZWeKMWIcfIIMzesIVezOxiv1pQG8GCYHaSCh4v5hJpnEUpXQDUkYXSsZm2DJ8fpD46PHlYW0YeiKA1T20v0N8LXAHYSMCJ8YnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzbr-DfFeRLTeIdoW4rUkTXR3HEDpjt3HDH00T4h-y0tyeRfD18iC6vvp555PfbAR3xZmQv0RnufNLS3JzxoenjCXx7YXkK3GZ92cI5njiv8X88mE_XzdCDZmIw3jdY3AC8GQ-a189LyLgglXomWQ3eB04DO57QVHZP7NuvXAJxyHBiULOkm7a0xGMfkQruzrKI3O65OVZjoQ9zkexjB1nq3q42slxWX9LcbYQIJdjyNPr-dmF_hz6gALPfvQqxwikzgFHPBLEk4lNwgsAniw5T-A4oX4-SZUaYKtO64FXE2xLS8pmI7qhqtNjdP6qKB-mkdhDd4v3bho0WiHbjvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAE1C7q8XdhGhSPHXuBImr4SOWZl1kxWObg6b2Sxv2vFnf9HYZJgPTDI7Sh92qbeYRHVYcVqi9QDjEC6nptGisJecM0EYkt72Fp4FGBdXpJLpzQve6IsbqqiaZdwrggRMFyfdjeMB7CxdNRCmBO8oZ7ZAvG93wxrkh4Eorevl-8MZWAabbc59Bk608cL0DpTl7EnV3xSSsejZ6CYlkmD5QSkwCG95d6StlZNa_oWYLj3lIe2JHlp9qvvXqhImX534MrgFst2c9GD85JQ79QF0z-6dxbn3BFivdVOjbv3nJinqVciqiJVnMG-Oi9U2TQ1XdzcSCXJjzMpCY5g9MtK_GMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAE1C7q8XdhGhSPHXuBImr4SOWZl1kxWObg6b2Sxv2vFnf9HYZJgPTDI7Sh92qbeYRHVYcVqi9QDjEC6nptGisJecM0EYkt72Fp4FGBdXpJLpzQve6IsbqqiaZdwrggRMFyfdjeMB7CxdNRCmBO8oZ7ZAvG93wxrkh4Eorevl-8MZWAabbc59Bk608cL0DpTl7EnV3xSSsejZ6CYlkmD5QSkwCG95d6StlZNa_oWYLj3lIe2JHlp9qvvXqhImX534MrgFst2c9GD85JQ79QF0z-6dxbn3BFivdVOjbv3nJinqVciqiJVnMG-Oi9U2TQ1XdzcSCXJjzMpCY5g9MtK_GMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWygDxsfwix1KS2_9w8azZ_YD05xDnf9N4hn1ennNa-guMxG8r72J3VpF5AYTwMbcy4D4LJ0xaCFiQuHW6jS2Xz3327BEDK0F0ImZK0_KNOL3ADDzh6TNuQ_mRbQhnMQiJujrHClzOlYJ4CFNAEFtMT3bD6DejZf_4O_-k5Bs5F8t5wwe3TLMSU1MCD_wjUi63Ng_NPTqvVhc-acka24FsLfvtRjKed1tmrvNmu7jZ_NjDtVuDV5uPqT_4nt0xkADQYPJqspq3UfUZrcZnz6P_DBV9LJMqJjHHHiH4bQfqnewly7KpnU0rq9U2b4CG2Ukw9F7Epa9DUh_Sn38FRcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=NNTqENdPs25gTKIXBJHSksPNPuXQV8miCucqT7lMP39LJ-URA9a5F2hmmnNwHfYe_-DQS9yGwsgRm6NYc8JGv72aKDsgs4SbGbgDXZQ6TVo0_s-T6XYMBvNvnJdx4LAyYZbqySXmdTjNOgvIL73Uf-mlVKWxDQErdJjYckzCsKEfovU5fyYtpkCgWCx3fMFbOXZUcbSWRaDgFW8cBm_vts2_gfvNIdfLLekk3qwKAyFHm3D-9mQQXyqCuqlya_FTi2x9J7YON9OKeJQbsXzz_VMZGV21R1GxLE0VZF5dvGmXFtdnU0Gkb27Kc1L_9mW0stp83ga-gSmYv2Qd37ukLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=NNTqENdPs25gTKIXBJHSksPNPuXQV8miCucqT7lMP39LJ-URA9a5F2hmmnNwHfYe_-DQS9yGwsgRm6NYc8JGv72aKDsgs4SbGbgDXZQ6TVo0_s-T6XYMBvNvnJdx4LAyYZbqySXmdTjNOgvIL73Uf-mlVKWxDQErdJjYckzCsKEfovU5fyYtpkCgWCx3fMFbOXZUcbSWRaDgFW8cBm_vts2_gfvNIdfLLekk3qwKAyFHm3D-9mQQXyqCuqlya_FTi2x9J7YON9OKeJQbsXzz_VMZGV21R1GxLE0VZF5dvGmXFtdnU0Gkb27Kc1L_9mW0stp83ga-gSmYv2Qd37ukLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=mUCSii_bldexpoQLUIs5xC7fHdUE1mODN6pRG-WaDtrIKm6YRGEJtGOmZb4rhgtLhMgjpnDwDIpDxB5IrWsA6fNuzBYJszcbQ6rSyStbY21QLxBmuOqh9fbBmn1ltGl7ALqK7zxGvTt4dQmKV3hxRNDoDVFuhcIxaPjYSJQbhT_PvQPy3sA14cef6ED9476JyWGU8iwkO8X5Y1f16CcV4-18lA9G-7nV4XvDZ8H6Fs7xUtwTTholponuRDxmC6qhxyY2q0VU_Bs902Ov_rR6M6l5c7K10lowaq0PAwZlA8dLdoJLgaBM4hdgCbbrKQcxJ1-r6vXxYCO0nsD7podt3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=mUCSii_bldexpoQLUIs5xC7fHdUE1mODN6pRG-WaDtrIKm6YRGEJtGOmZb4rhgtLhMgjpnDwDIpDxB5IrWsA6fNuzBYJszcbQ6rSyStbY21QLxBmuOqh9fbBmn1ltGl7ALqK7zxGvTt4dQmKV3hxRNDoDVFuhcIxaPjYSJQbhT_PvQPy3sA14cef6ED9476JyWGU8iwkO8X5Y1f16CcV4-18lA9G-7nV4XvDZ8H6Fs7xUtwTTholponuRDxmC6qhxyY2q0VU_Bs902Ov_rR6M6l5c7K10lowaq0PAwZlA8dLdoJLgaBM4hdgCbbrKQcxJ1-r6vXxYCO0nsD7podt3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6-0Q2tzuqFrMijkySiwunso3c4sBpwp3vxxDuy84MHUCOvIBE9i2Abv3Iq5L5nrheSjoTNFSitTPdbFBiOiDT5SbUlMTCwlHK-7NoXwv-EVwFxVv3sU6l9DewYhd3lgiZqRs1x7v5JFqHhZpNWAeYKWzAQWOV0nSUY8IBqTdjLBjJtKmTapO8NI0K1pngiqOfCqnjTkpb9PUhama38kxy4ExX4EXfZKsT4lzS8fqj0tjuol8NgJj7sb797G37-OnhQxKDb__hVdQvsOPNZGX6vG5IDNYDTMtRW_W785BtcibVCYj9_lLHl3EupqYw6F4NzvPmezsFS-4tr1T4iYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=oNa2x2NP8EnYkNf7fQUYRYSJ0t4fzi4klmLDW9oA8Ta3BDd4ewCmmccjAhu-JXmUGlnPJbgRNb21dETNlBpAdyRuvhR94ZI-X4FTLFI5XLEBIV7iF45YOeP4z9St6eaRrSctPdkdMmWeXqI_cs4L4dyy3zFHIpSeiXOXagIholOV7oLAXoxnmeuWJT0RFw6FqVpvB9Wul6YgyOHAs-tG_ka2Mg2272R8M0JtZMXyjD4AXw2M0MdmOzh3I-xDsgQG8QeiaHj1Y7eZTkePDGRzX-laLrOtiHmOHQtdE-CKz-B_6tznVQqgFO3iA1N4EbkhEFZH71zL6cJ5f_LH3sgt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=oNa2x2NP8EnYkNf7fQUYRYSJ0t4fzi4klmLDW9oA8Ta3BDd4ewCmmccjAhu-JXmUGlnPJbgRNb21dETNlBpAdyRuvhR94ZI-X4FTLFI5XLEBIV7iF45YOeP4z9St6eaRrSctPdkdMmWeXqI_cs4L4dyy3zFHIpSeiXOXagIholOV7oLAXoxnmeuWJT0RFw6FqVpvB9Wul6YgyOHAs-tG_ka2Mg2272R8M0JtZMXyjD4AXw2M0MdmOzh3I-xDsgQG8QeiaHj1Y7eZTkePDGRzX-laLrOtiHmOHQtdE-CKz-B_6tznVQqgFO3iA1N4EbkhEFZH71zL6cJ5f_LH3sgt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUEBCCpb9UDnwWXH5NpyML7eHhf4QhFY2nvH08-wmT-zkrH9Sctbiw4VxbKhp_qXudenLqfco6Ju8cvz1nh9PGfVpzBgWIuyyZU2OQLWh10YHGlJQbK6URANehL2C8_IzlDIzVohWWLdwxz3JRrw0rOJMQBlNIMCl994IQWfcXJYxG5_j1N5eBFf-g0cap5NVPEdK7t74bGbd1lruplzPGU4CKQkklMX65Zf-LdIcjCKBtG_G5bZLyhL5F-LMeqx6SnXi2H-Uo7oEilDwh_7oFHQDiLooh9XvBYA_mNmNKepqGB8VCgnosIgaN970TuRvvzMZ_6Ym2C5tJkc70C8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdtaBpsnFKkPx2oyymRDlQXqCuTLb0ergPaSfNh913j9FEcKuBFvQOxau4PsMegCcYXZBup5zhubbxEX1EC_Zk52AspcyCvPdNaldttcd7pTgtfpzrKa91OVeMjaZFdpcbegZSSBWuZ7hcLGpk3y7d4eCZJpCJjvg8oUeAOHYbRxfDuAwGCBkSyYKB3KaGN0NO-LPYAlzZSoVQLaNtyHNlCPltbJiU1W1sdqdyAFZRUWvo7xBkeW1lvtQ75V4oy8aRlmbZWurKuPg32yQ61qXCpVPnDc___yZRoTOxUYrSt0WsH_pnFU7VM2dMl94YSIBaKRhjjuAsS0IUlVb0KtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzsYI1pRyTjBPi4tPTJXvhN55Iagabn5yz8gSDHO7mgu_8jQeMQkWsidd2moImPWxnsxneHWJdoNgkfjqvL7kocBz5hJW7wZDtLweHThaijEy-J1DIpQ602otJm0iXsDMPiXIyA_WzaJzl6fP4oVpXIv6sQ_5fxV8a1KCRqgQC-iZtgKLhbhOpBmK7OEQQZzHzLWETt9BGa4e-1nFWKbIKD1TJ02gKANmKs7eduyltf-8J-hTki4nJxshFQMnmC8Kk8titXJNsX1wBnI1W_09lD7saClFPefE7MQ0MrVnsrB-kx5kbP-mflLztTrZwerEfimtBpTyxTqO_vPyO3FhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=rAfzr_cAlJQFcfj-X0uN-ihMtNIDMHQ92LmzvdaYkvnAr0oj249E-hko3R7zWDdf2slPhvRL6hE0pGdLk3uYF0erS582uqUntw-hPUqye-ldEn8f5V0vezR1ljqcK8bnnJhp6QU4ggBkF3XRPKYPrVuD_4WRl4_bYzOP-t3sRhv2D-rrfhRGPXpOBJgZYJqA8YCJLmfcFjAw4faYTchiCr3FbrChHEKPwitjwixWH8Cn4VWO9KHQoGT9tf94Mv1S17He_cJE1D2vKdH6R4dJpNL9GESyBoLsGksetDCNmn5OwTG-lT_cIbdnlNISAem6akKvlK6MbrEeZ6pNxCzEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=rAfzr_cAlJQFcfj-X0uN-ihMtNIDMHQ92LmzvdaYkvnAr0oj249E-hko3R7zWDdf2slPhvRL6hE0pGdLk3uYF0erS582uqUntw-hPUqye-ldEn8f5V0vezR1ljqcK8bnnJhp6QU4ggBkF3XRPKYPrVuD_4WRl4_bYzOP-t3sRhv2D-rrfhRGPXpOBJgZYJqA8YCJLmfcFjAw4faYTchiCr3FbrChHEKPwitjwixWH8Cn4VWO9KHQoGT9tf94Mv1S17He_cJE1D2vKdH6R4dJpNL9GESyBoLsGksetDCNmn5OwTG-lT_cIbdnlNISAem6akKvlK6MbrEeZ6pNxCzEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=DwPNRPqaYoDBrakYx6uhXsUpYfWIUKb4bTKlj4HK0e2wQ6725MBhSXtN7yoP9J8NPN36nuYhu43d1tfoeUy6L72Trg3t6IEAj3lEOuVd409CwzGivSYotmtjm5prkU-RwDPzjb6u5rP2qmjfP-yORXc3u8wzrRt39uth7Yd2KRpXT1oRc7LRTc4df3xWPyuTRE_naTrnv0xqsYfdqpNBfGMISMTQzabW55SPWdKbJ-HTH542vFtv5LEIZk0aM2zibp8Nd6vVJfjiCeJE3egAMoWZiNPxq5xPTs7PyA46M2t6xqpolaEykT3InyIwMdLAkVOywqDRm3pKqciZ-T4D0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=DwPNRPqaYoDBrakYx6uhXsUpYfWIUKb4bTKlj4HK0e2wQ6725MBhSXtN7yoP9J8NPN36nuYhu43d1tfoeUy6L72Trg3t6IEAj3lEOuVd409CwzGivSYotmtjm5prkU-RwDPzjb6u5rP2qmjfP-yORXc3u8wzrRt39uth7Yd2KRpXT1oRc7LRTc4df3xWPyuTRE_naTrnv0xqsYfdqpNBfGMISMTQzabW55SPWdKbJ-HTH542vFtv5LEIZk0aM2zibp8Nd6vVJfjiCeJE3egAMoWZiNPxq5xPTs7PyA46M2t6xqpolaEykT3InyIwMdLAkVOywqDRm3pKqciZ-T4D0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=OZ40nuMpy6_8ah3JEH2Y1biM6xfhmAIhhxg2grdN4_Gke5VV62dvRqoPw5yOoiGG9jduBENpLPFU5nOqG5-42dAocPhvSLaF3e9_g--8GMEF9VFOy6_AS7kGVa1OddiPXs4MsHa-boSZu0gqhpUMAf4X4QOiT82JHk7VAZx6u0W5ovHw5dViof2mz5Lz_JRRSZEQRKJ3pNaMr3klR_PWSLd_W9LdmBaiC2pt2mhILWLVhB66le1SSI7C4kX3d68B27MtgLQLw_Mdzom1BlTD-NAGFTsFpKepiaYGi-mK4Hvr2BndEbkYCXItU6oadDf420FipsrCcL_0UAr__dqpBwPVO1MDh066pMpxqToLPS-VoHrS-xy_X1qIy0LyXqUrmTujg1fPHpvOZbbOykJMsLFNNFU-aa36_tDB8q0Z7S-cHhk3sVuT0DI9I9VwL81fI7ZQD1gyGiEI4m3TEVHAmCE1sWkp0PdD32JZUtXpO9XQmvqRegcjiQ93DGh3SwtvdKVIfqPlJdbLMjmeVTVrBqeekycSTRWUHkbX93A9_vncaoDL0aLusymvuSXIQCOWQrEOuz-Y4ci_L5l3wZtgNwF068bTpWde8GUNoZ-1E5v6i5vYypTNuovpCtzZqVI3zFGgdw0cKmY-fhpaebWdUk_XyniTscvXFRVrmnFFTRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=OZ40nuMpy6_8ah3JEH2Y1biM6xfhmAIhhxg2grdN4_Gke5VV62dvRqoPw5yOoiGG9jduBENpLPFU5nOqG5-42dAocPhvSLaF3e9_g--8GMEF9VFOy6_AS7kGVa1OddiPXs4MsHa-boSZu0gqhpUMAf4X4QOiT82JHk7VAZx6u0W5ovHw5dViof2mz5Lz_JRRSZEQRKJ3pNaMr3klR_PWSLd_W9LdmBaiC2pt2mhILWLVhB66le1SSI7C4kX3d68B27MtgLQLw_Mdzom1BlTD-NAGFTsFpKepiaYGi-mK4Hvr2BndEbkYCXItU6oadDf420FipsrCcL_0UAr__dqpBwPVO1MDh066pMpxqToLPS-VoHrS-xy_X1qIy0LyXqUrmTujg1fPHpvOZbbOykJMsLFNNFU-aa36_tDB8q0Z7S-cHhk3sVuT0DI9I9VwL81fI7ZQD1gyGiEI4m3TEVHAmCE1sWkp0PdD32JZUtXpO9XQmvqRegcjiQ93DGh3SwtvdKVIfqPlJdbLMjmeVTVrBqeekycSTRWUHkbX93A9_vncaoDL0aLusymvuSXIQCOWQrEOuz-Y4ci_L5l3wZtgNwF068bTpWde8GUNoZ-1E5v6i5vYypTNuovpCtzZqVI3zFGgdw0cKmY-fhpaebWdUk_XyniTscvXFRVrmnFFTRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu7zADpz4IJe3MT1hsAj31xb_FMRhVRoCaezhBGSfrBJG-tgjjBgccXjnSBici0z2i73ygZ7PuhU_iAM6FXHFY7KA_S52CQS6ZQh1kN3fP7A2r0T_r4ePseO_h1ihTqMh_XzkVpgpkaPNysD06zATwUDOE6dsFjfZh7UhYkTRXfS2MGIEOUh7w_Cd-9wd0YsCSyXYb6M1zPE2Z0MeKESvCtZNBJ4GlguZPGoZrp1rHarx4db2Za2uq0TIJdx2YcL87WQuybiVfRE4hkDdeEaLqr9ZhsvFpP9bOvhlYqEe5eDtLOg6J3_wKdZySJvjyd-4J_zjF-V-Nv34Pa3xL_RFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

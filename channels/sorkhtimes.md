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
<img src="https://cdn4.telesco.pe/file/V24zRRy_nu3pBRd49U4QZH8Oz-Vp9wCah1PzJn1pJUW2xG7BlbFSicpN9LKGXaT7UpNSIIPJL-UChM1gNaAzfMDcjziCQxoMPa5QBNhkL6LBZ9Uc0fb227m3BW2ZEi4Tt_T6cOl3TEEaRGnfOuMGrbxkOojZfT6bLMOurlDX18pAMBDyoiJ5rpEQ_36IK16fquxBj47qIpkq2Ajue39rVDqZTpj0FUhYqlnwbwv__RLTbzP0FTgp0NiC87CQhUznbIyzU-KMI7B0bA7YC2E31yJPyd3blRCJVWLhTKfVvrT2vQNRja-IT1cK6UZQZG8XVxxHDYjiT2tmCWq2stuQzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fABzdIMJbvcdqX9dJO2YbkzDRaRgvJXQ9degmTtgHH9CojmnuxFGAgSiujxdc9Cwe66IStcBhrDCQ9_Bz5LIYihxVoPPzdrEaGXY8lrgzkTK9eQQxSAp3mHK4-CrvLUf_2GjgqU1MSOBrYWb-8uUFq1POK8nz5Yjc2TCXaT8SZCZqx3Wq0YO-1btg_9qXt054EDMmRaGOQX5S0344OUDn9uZ_e97cUMTSVd7Bncxd6asX2tyhbczdlpg9XqFBol2QDVWV3rvGYZb7WFusVQkI8IblNy5mmk45vwN-NWN0b3ymbLHfaIdojzTRehE2fUrTwgO9l8ZgHAdunRad03VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid -
⚪️
Rayo Vallecano
⏰
Tonight 22:30
🏟
Estadio Bernabèu
🟠
رئال با برتری کیفیت فردی و مالکیت توپ، از همان ابتدا برای کنترل بازی جلو می‌آید.
رایو وایکانو احتمالاً با دفاع فشرده و ضدحملات سریع، سعی می‌کند ریتم رئال را برهم بزند.
کلید بازی برای رئال، باز کردن لایه‌های دفاعی رایو و استفاده از فضاهای کناری خواهد بود.
با توجه به اختلاف کیفیت دو تیم، کفه ترازو به سود رئال مادرید است و شانس بردش بالاتر به نظر می‌رسد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 388 · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZX1C2d9oQfeN9MnxR63jKpm-10uN-4aZu52aZLIzA0fyl_6Z71ge7bSujNoyjUAcFbUDHaLQy7kfD_Qx0jMhzjzfcJtMH60MMpSWqkQO2GZYqQIr9LizVgB_XtsuFi5YQUNiiKnrigmyOT_V9v4BgXKdTmFEdT79bD2tw2rfifHAFbTtLVHuUOIGUQaUr7c7_ViAo3z-3Xa_RwxUlhnAJeDu_yGPHIACvAeCABpM3XfjhhWpVU6z18Thq4sDtBehR8IeAj4SonsLD4RUfw8a12wzYtUJf4lAKF9Fjp8CkOL7eSvQuF2I1O3sY4vgGbxKq4IBAoRRb8S1wSbjnDwKP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZX1C2d9oQfeN9MnxR63jKpm-10uN-4aZu52aZLIzA0fyl_6Z71ge7bSujNoyjUAcFbUDHaLQy7kfD_Qx0jMhzjzfcJtMH60MMpSWqkQO2GZYqQIr9LizVgB_XtsuFi5YQUNiiKnrigmyOT_V9v4BgXKdTmFEdT79bD2tw2rfifHAFbTtLVHuUOIGUQaUr7c7_ViAo3z-3Xa_RwxUlhnAJeDu_yGPHIACvAeCABpM3XfjhhWpVU6z18Thq4sDtBehR8IeAj4SonsLD4RUfw8a12wzYtUJf4lAKF9Fjp8CkOL7eSvQuF2I1O3sY4vgGbxKq4IBAoRRb8S1wSbjnDwKP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
با توجه به لغو بازی با خیبر، پرسپولیس فردا در دیداری دوستانه به مصاف تیم شهید قندی یزد خواهد رفت.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/139944" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/139943" target="_blank">📅 17:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/139942" target="_blank">📅 17:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/139941" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARPHUc4uGDsZ6TGocWB7jkYiwkIvSKbbHngW1g458Xmo8OjigLWFkiLyknMAu7_E14Jbf3TBCv9GudWOuC32GXi9kY2X6p9s3P-52kHtNud-nRHwgCATOp46O9DGpIQJpqfqeHHXw27DJuRQxGey7MziB8sYhLW05d2QMUl3DrdgcVi64Vq6yCpJOrD0Qz2fjIV9rUNQSY-sAVpuIxYUiMtykM4FoRtwkXzWgq63zUACkH0X5H0YQSMvxxOYfXz_T1eSL6QAX_KWdg8ImWjDytVDYV4B42kSz8gNddeS664WT4LsJ7bsn8w4EyG132erE7PWGM7tpwGss42g-M07Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میلان در آزمون لاتزیو؛ جدالی نزدیک و تماشایی
⚽️
میلان با تکیه بر کیفیت هجومی و امتیاز میزبانی، دست بالاتری روی کاغذ دارد. لاتزیو اما با ساختار دفاعی و ضدحملاتش می‌تواند بازی را برای روسونری سخت کند. انتظار دیداری نزدیک می‌رود؛ جایی که جزئیات می‌تواند سرنوشت بازی را تعیین کند.
[
آث‌میلان
🔴
🆚
⚪️
لاتزیو
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/139940" target="_blank">📅 16:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139939" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/139938" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls3FzT4Mffp_nxafyTud28gICNGCM-APN2S-_to_2vn4fVxXHNxhPnx3Ktkl9A_7sLZJbqxWPOKBBm4Vx9FDrJyUH0MIlUCDAASafkGH64M90qKhNGfGpxLr5oDkStgDNBw_p_CjpmXZL6TFfP05I8aesjIIpAbwgSk1oSNop0cyy5pxBqdd7U4ejwgj5zoSfwcCGRa3LyZroOIaDWaV6RS3hCIDGhv1Bhf8l94C_VBcM0SMl_WKnMWiTCK1wOvnjLw_G5HAFMROV3vmv07WoUKfbQubZyzGse3fVsfmAj--6M3E0h9QqSUQMQRjrEdYJYfwW8Dpy_CviMLIfWkyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده است.
📊
۶ بازی | ۱۳۰ دقیقه
⚽️
۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139937" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
باشگاه آلومینیوم اراک هم از بازی کردن آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139936" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139935" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139934" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJaxKAVvfCGEW4_RB03l9pPrpiiLwCpabP83xDPa_A609yuuTI7Fi8mq8StqWFc5gkcrLIuYC9JBU7OnILwsU-aAtj8j8A_gNkh2CUwqWxbSuBCfAODjdP6d66FQG6FUf49UFfwI4Yq3DLPVgKOXz9yCQRrX6M0HErnWpjtLHVv9kIFqD75mwIAZYjYhrniB6Azus7J6tpRMO_FvL-U8ZdnYvYuEqtKkfQ9L-T-nlU-Xqo-9U_tk0r6UUGyF4iqjzEu77jqWtektsLDyaJPitmdzD3ceRLSZ91g-F04Wa_l6dYN4N8C9oyueXsCvEpNb0XeM1A_BeXD_ObLIADUrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139933" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6OHF94IeJLcbNksq5aD50dK_0B0FXPIEBH9hyUjkl65_U-cR891cGnAHsytjH7KCk7MQANGf63ZVq9650vq12Qn7hgVNugvmEO5WqIJd0BHxfIUxpGxNRl932wO_Qliley3fZIc7Ao3ZJaSH5eZyCh0XTxKnsKGMAJI2-UUzTUhkPsclR9g4s6CWEfqTIboL089yHbm4xV1EISiRAIvmud9JKoNOrnHaIHYmKJ5HUqE4-KSnZd7Kki3wnPfLXmNFLkuLsBjeOW___rQUoG5rMC_Uy_wW41RMW9s9n-e6qlVJaNzwr0s9x35rBu_DjK8lRbxfbZtdlrkOhUB7aQhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسپانسر دو باشگاه لیگ برتری نساجی (وارش) و تراکتور (آتا) توسط وزارت خزانه داری آمریکا تحریم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139932" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139931" target="_blank">📅 11:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
حمایت از خداداد عزیزی به رغم فحاشی های زشت و حمله بی اساس به فدراسیون فوتبال درباره var
✔️
✔️
سخنگوی فدراسیون فوتبال: قطعا و حتما امید عالیشاه هم زمانی که خداداد به استرالیا گل زد از آن گل خوشحال شده. هم عالیشاه و هم خداداد عزیزی برای این فوتبال عزیز هستند!…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139930" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
پروازهای ایران–بصره تعلیق شد؛ سفر استقلال در هاله‌ای از ابهام
❌
❌
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139929" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
پزشک‌باشگاه استقلال: یاسر آسانی هیچ مشکلی برای همراهی استقلال در بازی برابر السد قطر نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139928" target="_blank">📅 09:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pny4ERFvk2VTeCZB5OJQUlfI7VQhjgJt-vHQgwIxu8id9d97oxuit6URmkiB25pAgXyDQGnXJUD7ZokDDJaK2tQZMp1L-3xLURsA-8zCBzI3JHVViyxR8HbPsNGMRje_qUfMnI0XyDtn6Zx5RoPBIbfnpnVKy6AorbQJg8x5tPnGbA4jnJGLrW2y3JCM13cvAmKimeBpQxwbmhLTb6e-BJ4DcBo0wuTXqq7W9qF9OiF6i1VH4DYM20B3Gq1cEVqDuXp6_ENuYlwd8RBZR8JkOU9N7dPSDEJWAlscETVpNORA19wB3cMUfkd3pLl2OYCNmIY844XHaTayu847089x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139927" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyzkiBI3LRQ3k8GqRzyBb4Eqs5EBe0lRQ2cLNpGE7jZx1Zl-av4kbtqOWrcIyVml5VwG9rwW-pdL9UP-_jGRhboVcz1pySa24qVWB3hzKtvfwtyx33ttQ1JUMk8UoJ3ICPoqx0J1S7lANnXNK3yWFrKFE_U6y6YjTWDTT6C5fI6Py7cXP2cSP6DETh5VAeCGWX0TIrNbc9KfifQPQq0uBaIoMTGH7KRoKu9In5vClrDDouVs2ydlyURb53Q22izpIJnXyq9BkwxICJSrb8bIVs_BVmBR1h_V_8R0ZVIptFtS12q3689HaBzg52ocpFhDiZ0KzRL_eD-OarQBcPINgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139926" target="_blank">📅 09:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-lP8SZHZVZ6QU11Vm8sfGpxj5HYmW7KqVq6jCyZOBVR047aA1OAOnulqoSC4602FTyQKN7ujxeJc7tkBmuHVu8Ht5rkK3w_GN13Qq0Q_Gk3wf7WVrm7C14VgcPCTqZO41vLufXSZstgdXWYk9eWgWg2iCqZZVqeKnUIEKMorAkrS3oO8bV6PQcoEATRSiZrM8xuACzbpPZIjLNaxphQEzr3rAXowlETXuwz39gza0isjewQYWvg_YIUVqAiCsdCisB9PV1g6PFz7kLTafOnXpp1IpNkt2Ktkx6hZ_j7uTkWrFkJuX94sTmddHz2fNMwQqpZ9ej1w8K650NgTQGbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
شلتون و تیافو؛ نبرد قدرت و جسارت برای صعود در نیویورک
[
فرانسیس تیافو
🆚
بن شلتون
]
⏰
بامداد شنبه ساعت ۰۲:۳۰
🎾
شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند ریتم مسابقه را در دست بگیرد. تیافو اما در رالی‌ها و تغییر سرعت، توانایی بالایی برای به‌هم‌زدن برنامه حریف دارد. اگر شلتون روی سرویس اول و ضربات فورهندش مسلط باشد، شانس برتری‌اش بیشتر می‌شود. با این حال، تجربه و تنوع تیافو می‌تواند این نبرد را به یک بازی نزدیک و جذاب تبدیل کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139925" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139924" target="_blank">📅 00:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
تارتار قصد داره که به اورونوف تایم بیشتری بازی بده تا اعتماد به نفس رفته این بازیکن برگرده و این بازیکن رو دوباره احیا کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139923" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎦
تحلیل مدعیان اصلی قهرمانی در لیگ از نگاه وحید هاشمیان؛ شانس اول قهرمانی به نظرم پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139922" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
براساس گزارش منابع خبری، مسعود پزشکیان با درخواست زنوزی بدنبال حل مشکل سربازی علیرضا بیرانوند تا پایان جام ملت‌های آسیا است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139921" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139920">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=DZE4M9xaRhL6IJGVzOBkipizsY5OtGxW2Bvoo1ETuxvsYeWl7ookK2Me_u2de2KBDGyE9k7qWvL0pfX0ndInxcSc7LaKNEsujaEeJlj6mI_SGPiC1gWbeXSD7k9BrVCYZk6UiGGSUVZIxTAQULp8CTYZGB9NFg4oFurvHvQkexZ1IlisKMKmfFJisBMT0DkENOWAYjlK97ZOg1NKz0GRDzjcUljT9cZnoTUBgS-38KlDwkjxR3S6X-3novtxP9NS3xW8rIrI12ECz2J3xQA4el2SrsbAjVRcnPrMKEicHjmZUtBF7jJMc_xWrYL5KyN3vIOVm9E_rU8V5zZp9qTY3rnlwt15QX-BEuCtdVNu2sWpNMeoShxyuUkb5HxaGjseL-GtKZVwxayarI8kSdDYulDdr7w8nBrpThSI4_lu2uv515LErkfEZKSZAsMtwD9qe5Lsx_f1qaNPGFjTTxI7YOQ6erQdwJK_DlkFopXisMEJ4Kthg4uQqxymHfTPH6OafXKuA8EemtSzwlRuVbFXgYFu9OxBzgG67jzfsFuSJdSSm597lD2cFNQRpb8iKlJjSB1xTUJ3RdoE6ppifcMc9LKV3zd1N-bJMRxj3ZbuCj4wB7AvVvncOTP_-8NfW6CGZ65jGRFBDdyufHEmbdl14RDP8bprgfFikx32uy2QCKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=DZE4M9xaRhL6IJGVzOBkipizsY5OtGxW2Bvoo1ETuxvsYeWl7ookK2Me_u2de2KBDGyE9k7qWvL0pfX0ndInxcSc7LaKNEsujaEeJlj6mI_SGPiC1gWbeXSD7k9BrVCYZk6UiGGSUVZIxTAQULp8CTYZGB9NFg4oFurvHvQkexZ1IlisKMKmfFJisBMT0DkENOWAYjlK97ZOg1NKz0GRDzjcUljT9cZnoTUBgS-38KlDwkjxR3S6X-3novtxP9NS3xW8rIrI12ECz2J3xQA4el2SrsbAjVRcnPrMKEicHjmZUtBF7jJMc_xWrYL5KyN3vIOVm9E_rU8V5zZp9qTY3rnlwt15QX-BEuCtdVNu2sWpNMeoShxyuUkb5HxaGjseL-GtKZVwxayarI8kSdDYulDdr7w8nBrpThSI4_lu2uv515LErkfEZKSZAsMtwD9qe5Lsx_f1qaNPGFjTTxI7YOQ6erQdwJK_DlkFopXisMEJ4Kthg4uQqxymHfTPH6OafXKuA8EemtSzwlRuVbFXgYFu9OxBzgG67jzfsFuSJdSSm597lD2cFNQRpb8iKlJjSB1xTUJ3RdoE6ppifcMc9LKV3zd1N-bJMRxj3ZbuCj4wB7AvVvncOTP_-8NfW6CGZ65jGRFBDdyufHEmbdl14RDP8bprgfFikx32uy2QCKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139920" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=IlPv9dRWAt1UmVObQ_XNSDPGtL2j7AFHDWiDcSou8bv9yfb6g-wgcEwABW-OqieBkp62DV8K-KRk1alVLDekx4DoqmS30N3K1ialWyC4LOLOzDIPCn9el8oTkartnAb0Q6OZHb8-TNoGrIaEn_OfDjHI0fe1vyfUn9eBPDrgi4W8rJRGyyumF_2Tbtboo_OFAflI9hyPN85R3h_u2XIaaq4LoUCQzWgfxJ8zpgyxefcd2cakDfOjKcP9AlbYcSSza7qdwsV5fpC7Wabb7pMMmjPqlYJIdviqW0j6f929GQGE1dz6GXI38t98rZNWOZOmpzCcFDL0TNIh9wp3X9ZYymAohGxGHYN8SGDCDCgJrhDueknbxZAp7O7VHfdGHcON5UiFQJkFZBdsg9U6ZEWlr8PP-7QToo81lBILxbk6Hj3zEiUve_VynAhwPaSBC6F1LlEKKaLDiap-s5Cny-2zfJftkF8Fy2u8jWErNzlNkntMfYoryZxy8HeKsZicj01wbUWS1yQQRi81zq4kIa59ZrPc7v13JnCHDl1EYEssJsqB137ZZurK4pycbBdisjGduxR3eGEC9h8rzvq7NuzVhe4LJ_6YDy0kC8s0VeaLrqof8cUdQyZg4VoevUctwiUj_8yabLboDEYaj7gvEAuJExLNfodbqbcBXKq6bWmwOm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=IlPv9dRWAt1UmVObQ_XNSDPGtL2j7AFHDWiDcSou8bv9yfb6g-wgcEwABW-OqieBkp62DV8K-KRk1alVLDekx4DoqmS30N3K1ialWyC4LOLOzDIPCn9el8oTkartnAb0Q6OZHb8-TNoGrIaEn_OfDjHI0fe1vyfUn9eBPDrgi4W8rJRGyyumF_2Tbtboo_OFAflI9hyPN85R3h_u2XIaaq4LoUCQzWgfxJ8zpgyxefcd2cakDfOjKcP9AlbYcSSza7qdwsV5fpC7Wabb7pMMmjPqlYJIdviqW0j6f929GQGE1dz6GXI38t98rZNWOZOmpzCcFDL0TNIh9wp3X9ZYymAohGxGHYN8SGDCDCgJrhDueknbxZAp7O7VHfdGHcON5UiFQJkFZBdsg9U6ZEWlr8PP-7QToo81lBILxbk6Hj3zEiUve_VynAhwPaSBC6F1LlEKKaLDiap-s5Cny-2zfJftkF8Fy2u8jWErNzlNkntMfYoryZxy8HeKsZicj01wbUWS1yQQRi81zq4kIa59ZrPc7v13JnCHDl1EYEssJsqB137ZZurK4pycbBdisjGduxR3eGEC9h8rzvq7NuzVhe4LJ_6YDy0kC8s0VeaLrqof8cUdQyZg4VoevUctwiUj_8yabLboDEYaj7gvEAuJExLNfodbqbcBXKq6bWmwOm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
❤️
🎙
انتقادهای تند وحید هاشمیان از مدیریت پرسپولیس: وقتی سرمربی دارید چرا به او احترام نمی‌گذارید و رسما اعلام می کنید که دنبال سرمربی دیگری هستید؟ همین می شود که بازیکن هم به سرمربی احترام نمی‌گذارد
🔴
همین جریان و اتفاق را هم برای اوسمار ایجاد کردند و این رفتار اصلا حرفه ای نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139918" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=fqSgNPmeJXf8PPVj-kQSVjGy6dNKCLA9uJDUn5YcAB9BXb2GYyPZqJA3yzXIjY_YmC2VVQvQBDgrE55htw5fUx3Kt_rzMyRS9_0tsmZr-ItbDZXiuYozYXxnzBqI6StAKldFO52ecPPu0Y1Fzz1D0Z5rarFsiAokvu975eVviFHh_r8WfeR9YcpiJoExPfunKfpZxD02pFTTj5Dgu5yAYTyUmS2Fa9tuwJDJhp5dS8dJwZCzgtUtbNBmbEVwWazMbc2mFqTqejPmd4qiHNDFC3kQ089NrG42vpMFA6n5mC5ijyRTwyAz61eQdIPOrGg7gDGFsaRPvGjaWxv34yLa-WMuDTiswDHeNuAgTOPTX27PfWCTprUbqEYr8HVaGB1g5OP7IhoNZ7Bae7z2XXGQyPbaaViy6URph0f6okoLXWZKJLfC2JnbR1ifufgKark0pFH1qUoNR2YMmtzCzhiYOcU3YDYmoQYToXbqpnXTKbkEXrJb5YAvQI-JNGMHTZ1eNrCDnjSLU_hFXko-I-Am2ciPlGAYAjh9_7l9EqbyOonrLhCwV3aDscQ-D35yDFGz8-hH5WJsJODQnSGng_oWA_4t7biJG3H1s6toWjo8RU9vDy2FqaxJUaHpg6k4MODo4fwoHX6hLgKYfGmOeH4JueZGCOB5NhKkZynYWUj16Lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=fqSgNPmeJXf8PPVj-kQSVjGy6dNKCLA9uJDUn5YcAB9BXb2GYyPZqJA3yzXIjY_YmC2VVQvQBDgrE55htw5fUx3Kt_rzMyRS9_0tsmZr-ItbDZXiuYozYXxnzBqI6StAKldFO52ecPPu0Y1Fzz1D0Z5rarFsiAokvu975eVviFHh_r8WfeR9YcpiJoExPfunKfpZxD02pFTTj5Dgu5yAYTyUmS2Fa9tuwJDJhp5dS8dJwZCzgtUtbNBmbEVwWazMbc2mFqTqejPmd4qiHNDFC3kQ089NrG42vpMFA6n5mC5ijyRTwyAz61eQdIPOrGg7gDGFsaRPvGjaWxv34yLa-WMuDTiswDHeNuAgTOPTX27PfWCTprUbqEYr8HVaGB1g5OP7IhoNZ7Bae7z2XXGQyPbaaViy6URph0f6okoLXWZKJLfC2JnbR1ifufgKark0pFH1qUoNR2YMmtzCzhiYOcU3YDYmoQYToXbqpnXTKbkEXrJb5YAvQI-JNGMHTZ1eNrCDnjSLU_hFXko-I-Am2ciPlGAYAjh9_7l9EqbyOonrLhCwV3aDscQ-D35yDFGz8-hH5WJsJODQnSGng_oWA_4t7biJG3H1s6toWjo8RU9vDy2FqaxJUaHpg6k4MODo4fwoHX6hLgKYfGmOeH4JueZGCOB5NhKkZynYWUj16Lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
❌
گلایه وحید هاشمیان از احمدی و مدیریت اسپانسر اصلی پرسپولیس؛ صحبتهای او حرفه ای نبود
🔻
احمدی گفت که هاشمیان نبود دورسون و امیری را رد می کرد و این حرف در رسانه حرفه ای نبود و میتوانست شخصا با خودم صحبت کند/ صحبتهای او فرار از مسئولیت بود و در شان یک مدیر نبود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139917" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139916" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
روشنک :
✔️
✔️
باشگاه‌هایی مثل سپاهان، آلومینیوم و.. به ما اعلام کردند که اگر هفته هفتم را برگزار کنیم نمی‌توانند بازیکن در اختیار تیم امید قرار دهند.
✔️
✔️
فقط پرسپولیس درخواستی برای لغو بازی‌اش در هفته هشتم نداشت.
✔️
✔️
نمی دانم سازمان لیگ چه گناهی مرتکب…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139915" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j80qXwjKEWBqfa1LpAJs5PTHkAdW5HdfsGuaONKZPRiO_t59LEnExsxNL32PzA_08n0LUai3H3nFkQPTl9S0uGqEfPC6O7o995hXNKSe6-JNH7rhbZY3P1VL1PpxGooXUzz-dPoNiQBU9Bs91J2RrnFTaLZjlp_zy6LI1mZiKtu4dwmRF6-06pwmphWeHIhaB7F-bgbV6Kw0iE5UY4DuC5Q0d46F2VJMqK1b_VIUe7494RFaZPpwombag5YYZ3Dr8PAZrB_oAehqyMru3RWUAwnjqLYbOO6VRnJpbm6D7g0t33H4Es42ZvEZ8s14cX1sxo9glMLGkAMbzxGlTqXmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با وجود لغو دیدار برابر خیبر خرم‌آباد، پرسپولیس امروز هم طبق برنامه تمرین کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139914" target="_blank">📅 22:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=uWDmg2R-PkKQYAdlTaUFIb8OV6uaKKj--dB_SivC4bcpXAZvrPlkeqPfdnwQwcjwbiO0OHSITVxyqvxQbGEFx7JWjpl2zNV4L0PRE6UhWB_J-JWT_pRPzybpndmXNb70nH-ZeJYjSvOSCsUzKQrrK6stCCyPT1j-ez8Yf75NvpYm2BIe_lakfAv_vXfmqUKVr6fPUfxZYRHPqgoOYwqfm5H_tTJCjMPVE1EHlQsl0jW509GjKgYLWHiIBRZ7WQ3FTaEklgwghsvoxG4j0YYIM5TRfjyXG-mmKk8NvcOdD6vAE7JplaLe1RwXbw85fhgigXawk8G5t6S92P-SGjrPqDJ86CGYECM_Na72GeDz40nqV6oGURCdpsl_Obz356xfNBZNKCVtfVzJdc0M_7_gYlEjNV_I9ds8zBTSdZqwySvH_xek3t2Zem2lr1NKANu4ovNQncIGVzYZQVsMAXYIsepU_Sco2WmorCMaeyCco6_K2NUWDgJzIWDRxE3OEXgQiFSYxjmi_8zMFAp-VCqJSmyX5FvVxGJ9dLcJm8I2kYocDPXNKxMPwuFO2Oqd3o1T_gCxFfc4eKKuNGHvfN-4CBtQ166scAkyg1vNZfBUwfdSWxqP525iyi08pLiWOK1D8-rvno25PfjL8rFpvLqP67JJM7C5xLThogT6kcswvw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=uWDmg2R-PkKQYAdlTaUFIb8OV6uaKKj--dB_SivC4bcpXAZvrPlkeqPfdnwQwcjwbiO0OHSITVxyqvxQbGEFx7JWjpl2zNV4L0PRE6UhWB_J-JWT_pRPzybpndmXNb70nH-ZeJYjSvOSCsUzKQrrK6stCCyPT1j-ez8Yf75NvpYm2BIe_lakfAv_vXfmqUKVr6fPUfxZYRHPqgoOYwqfm5H_tTJCjMPVE1EHlQsl0jW509GjKgYLWHiIBRZ7WQ3FTaEklgwghsvoxG4j0YYIM5TRfjyXG-mmKk8NvcOdD6vAE7JplaLe1RwXbw85fhgigXawk8G5t6S92P-SGjrPqDJ86CGYECM_Na72GeDz40nqV6oGURCdpsl_Obz356xfNBZNKCVtfVzJdc0M_7_gYlEjNV_I9ds8zBTSdZqwySvH_xek3t2Zem2lr1NKANu4ovNQncIGVzYZQVsMAXYIsepU_Sco2WmorCMaeyCco6_K2NUWDgJzIWDRxE3OEXgQiFSYxjmi_8zMFAp-VCqJSmyX5FvVxGJ9dLcJm8I2kYocDPXNKxMPwuFO2Oqd3o1T_gCxFfc4eKKuNGHvfN-4CBtQ166scAkyg1vNZfBUwfdSWxqP525iyi08pLiWOK1D8-rvno25PfjL8rFpvLqP67JJM7C5xLThogT6kcswvw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
به مناسبت خداحافظی گولسیانی، یادی کنیم از گلش به مس تو دقایق پایانی که باعث قهرمانی پرسپولیس شد و باسن خیلی از کیسه کشارو سوزوند
❤️
🔥
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139913" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139912" target="_blank">📅 20:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤩
🤩
🤩
🤩
🤩
🤩
💬
گولسیانی:
⭐️
من تو تیمهای زیادی بازی کردم ولی یه تیم هست که وقتی یه بار داخلش بازی کنی و بدرخشی، دیگه از قلبت بیرون نمیره. نمیدونم چرا ولی وقتی یه بار تو پرسپولیس بدرخشی دیگه پرسپولیس میشه عضوی از خونوادت. من رو نخواستن ولی من تا ابد عاشق پرسپولیس…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139911" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia0LlXfhA88Y2x7z6BZmXDHHdGqQDQFET2J50bCNSniutHO7h7mEPD6_nGdrIyxkdarsqgnd8NX5rTBxQZeGP_d_hxT4B9K65K5WW8VNWLughILGNJPx9XeWijWl6uJn_ci4x4emVKPAPSlIs7TWXKTDhMHvqZCTu85pQTwiVLf1a-XON7UKtGl-lYi7bOiIsJwEy-eveud0IrFrFZ5InuffwcfUuJYmYoEe9pRJXRVCa4xLJuDpdib9oMNxL9GCR8eErIpa1Bnmr2DaY7hQtlMfrCZt2QI4b0HqisRLB8bPkJ8UO3mIjCiUANz-ftCW2DeMabJqiDHuAQXH39iIjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽
سالاری از پست مشاوره مدیرعامل پرسپولیس استعفا داد.
🔻
محمد رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال که چندی قبل به عنوان مشاور پیمان حدادی مدیرعامل پرسپولیس انتخاب شده بود از این سمت استعفا کرده است.
🔻
سالاری به توصیه مهدی تاج رئیس فدراسیون فوتبال برای توسعه رده های پایه و کمک به فوتبال از تاریخ اول شهریور در پیامی به حدادی اعلام کرده که دیگر به عنوان مشاور او فعالیت نخواهد کرد و از این سمت استعفا داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139910" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139909">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
فراز کمالوند سرمربی خیبر: سازمان لیگ تصمیم بسیار درستی گرفته است که بازی‌ ما با پرسپولیس را لغو کرده است/ من نمی دانم سر و صدای دوستان برای چیست؟
☹️
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139909" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
فراز کمالوند سرمربی خیبر در گفتگو با ورزش سه:
🗣
باشگاه پرسپولیس ابوذر صفرزاده را از ما خواسته و ما گفتیم در شرایطی این بازیکن را می‌دهیم که حسین ابرقویی را بگیریم. همچنان هم در حال مذاکره هستیم و به نتیجه نرسیده‌ایم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139908" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCRk2aQysMq_DcJRz8YzRhHEMwbA4z9R9Wa14MWZx8VPEgef-QTlpDVX2byBjbxaRID9qppbscOq2kOKWAMd6oIYj-ZwGGXd60s25qKDXyJPfDyhfBQawt_vsJS0M2G_ApmjRRjbU-p4b3raddu82BEHvHNlCus-h6FKG2JpQTsW9FNJu-CsxP72qb4nxCvg04Id4msLEYpJorva9RoKARsyLLgJffpsFxhzX2io2s3c0ZmmebgcSiXP9FOw9fDUJmHg_1R0skjWzNfKk0n49h77A9XXe6GSqutmEoUWx3FquiE40xfh3OGtcB5M8FgnreRPz4l5fmndtUuayhM-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبردی نزدیک و تاکتیکی؛ والنسیا با تکیه بر امتیاز میزبانی به‌دنبال فشار بیشتر است و سویا امیدوار به استفاده از فضاهای دفاعی حریف و ضربه در ضدحملات؛ دیداری که می‌تواند تا دقایق پایانی کاملاً پایاپای دنبال شود.
[
سویا
🔴
🆚
⚪️
والنسیا
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139907" target="_blank">📅 19:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXzxZTKZDfn7TzuIt6ZcWW2tFMwBaJuo7iWWKsCM13G9pBUH7dpxcGwPL-yEaO3QOXTWAKe8Rfb2fGi9Ha47_dfGWe6-F8dbdy5nGV8bWr2gMJXTJ2rODIDaN08adb5XAt-PqxJc_YOrf0YWCQp3_v1a6XOha8v6MBtk3wcBAzX7Vl5JFy-n_Lqe6LrN_fpLLCJv_-GdlCvyMpmTSp9iSVF_wySf7l2mAyku5fhqXcbfgmnoE_tbbWRWeqBlzk2JXfMUhEuPIQZceUS9IOvkyzyHQDZ5aUC8HxbpCWc3GBjGwEBqvtctA3_AyN0xLhHuTzLVmMeYY98O2migGXVCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM8a6fkL9TS-hwy4DAxrbshPmtdHO_ehsmYNqhDT-UiX7Jg9-NTYzhiBd54Tw8xluOS7bVZr5ysM0ajQe8-XbfLPiJvNZKdAzs3g5nGXMdk9I5W-CKKec5HrM0AqvQ_XJXPwEAZjcMoI6e-Hk2rp9iuIa_PRjQaHQ8ZBrCWvb4EItETz-N62axGE2OTK4KuFYTfGJBFMEvRj9aBWYE-sTP2bIUZlM_2dQ5ZU02Ed4EcPmejxH4TXXi9EjfN64qPJMF24tzOLEorGx1t7Vjwcs39z3nWIlhJirRmvWfRBlWFHuM_H7e7Dvl5w3AAQT3SnKzZemoudw3ovl5R96y-bCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139900" target="_blank">📅 16:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139899" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
🧤
علیرضا بیرانوند نتوانست کلین شیت های خود را ادامه دهد تا رکورد هشت کلین‌شیت متوالی پیام نیازمند در لیگ نوزدهم، دست‌نخورده باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139898" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
فووووووووووووری
✔️
اسماعیل کارتال سرمربی فنرباغچه پس از مساوی مقابل رم در هفته لیگ قهرمانان اروپا از سمت خود استعفا داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139897" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139896" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139895" target="_blank">📅 15:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaV3AhB4j2ohhR5Bi9l3Yj4w1DAEDAEwI-XSRshcHdUKnoqOR2ttFAYJMgPCqN3xcfB2yV7ltstSo7TOJGPjmxC5_Fnd5k6L3nLtS3HQMzqYi5Tfc5qe9nHpykUyFk7XDo9jHMILAHQ1SlKHNPnKJEXOxvbqHGX7UGTgMwOesjIhAbGzgBcovOoqsUuwHN0C9K4DhuZXMUyoXtJ3BxLH2V_t_SMB10UHTng75H0y9y3ZBd_rj5BTVe8joEyffHdoH42nFfQv9kijllfyXj43Bk-0Fkq7jko0qGi27iIRZ-OCb139dXoNLmGDVi_6dl5w0TdPsTb0NpklByq2eMDxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139894" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEwyCE9a-q-glXNFqVZiTim8xCnNXlGRzl89D71GIMEgje6edxV4WZequuNw2dXW-AG5cd5R4w2WY6WAjow-lx9O7m1J8ilU_w0ztykx2mi8U4E3qW80ARE6CT_lJ_09UW4dv-D4i5w50pJVaKMRE05I8Li5U-WldIZbiRymxSaRe530mDRwSux5tgFyT6YFJihbCfBHfKBH-qeBdI5qt4kaoYV0HFGuy_Ji0C4NBlrCH7aPiLoOoBps4gmDFC40mawzClVjSIfrbo34xmps_QpRDw4MYG8zUv6CvrEIhS2Zdn7ApaOWejlvrGryrBSTRSFXAe3-EOrn4wGiG_qH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان نیز پیشنهاداتی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139893" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139892" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⬇
علوی سخنگوی فدراسیون فوتبال: پرسپولیس دوست داشت بازی‌اش لغو نشود؟ باید بگویم از آن طرف خیبر درخواست داشت که بازی‌‌اش لغو شود
✔️
✔️
خیبر فقط یک ملی‌پوش داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139891" target="_blank">📅 11:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8g_fQGyXiLLgHl7VSyekWZblLdMW4XFVRwzRWE7CZeR7UTytTXA1FzU9TNQRqFbL0A84W9zf3IwJYiJ7TCjGjpTWBEPUSkC62JY7k53I-3Z6fg-wEpKu03X7tfQCn1hI1jLFWyPKcyCifnJYPU_nBpA91hWoQhpSwoA_2cQYjqRNVUF8udt6gtynruw1N5k4vp5YJozOUcpjY2pLrceuutILpqxFAX2uPhx0DH1zsuRmnEjHxzh5oROqN4iXKoiWmKdZBSM1IeU4mR0GQQ1HQoSHVvnNHrYd_-kLrQk7h8mschzgZFFskVWpFDOhRjNilS7zJGYd4x21XalkjfUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
از دیروز و با آغاز دور جدید تمرینات پویا اسمی مدافع وسط 17 ساله که همراه تیم ملی جوانان در ویتنام حضور داشت در تمرینات پرسپولیس حاضر شد و اکنون پرسپولیس سه مدافع آماده برای جانشینی محمدمهدی زارع در بازی با خیبر ( در صورت برگزاری ) در اختیار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139890" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139889" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
آسانی مصدوم شده یا از ترس شکایت جلوی السد نمی‌خوایید بازی کنه؟ ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139888" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139887" target="_blank">📅 11:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
۵۷۲ دقیقه مقاومت بیرانوند برابر رقبا
✔️
✔️
علیرضا بیرانوند از آغاز فصل در ۵ بازی، ۵ کلین‌شیت پیاپی را توانسته است به‌ثبت برساند؛ اتفاق ویژه آن‌که بیرو در آخرین بازی فصل گذشته تراکتور در لیگ‌برتر مقابل گل‌گهر هم توانست دروازه‌اش را بسته نگه دارد تا ۶ کلین‌شیت…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139886" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
رضا جباری مربی پرسپولیس :
✔️
من با علیپور صحبت کردم و قول گرفتم که بتواند امسال آقای گلی لیگ برتر را به دست بیاورد و این مقام را تقدیم به خانواده‌اش و هواداران پرسپولیس کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139885" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139884" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=tL2bzKHCpKbj_lT64bD-R67ItyJDCWM9YHGapiJVa3itDtkg_9iaJdRjgBZ-hHvDw2hbT9OqGlK-raFxEl8s4x_1mJbwCFc4ruX_4syQXKjUX524kF7jV7qbCMPOLzo3EVryeM2YZ9IbjXIHcIIoPoRaXtqDOVOZU4_QccRCX39XGGieyofqq1p3-D7IjSRCAPIrmIO5rZSbdT-pV6cKQBtiUAvgEDDneSzqcyaIqahNEw4ndA3QZmc-OP2Xvy9h3oPvK1UGsw2fvSNuvVK7buURhep0IiCXLGMX65LiS_LGS4931_8zUZ07casYoxQxDzp5HgWRP0SCBYyVN6RaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=tL2bzKHCpKbj_lT64bD-R67ItyJDCWM9YHGapiJVa3itDtkg_9iaJdRjgBZ-hHvDw2hbT9OqGlK-raFxEl8s4x_1mJbwCFc4ruX_4syQXKjUX524kF7jV7qbCMPOLzo3EVryeM2YZ9IbjXIHcIIoPoRaXtqDOVOZU4_QccRCX39XGGieyofqq1p3-D7IjSRCAPIrmIO5rZSbdT-pV6cKQBtiUAvgEDDneSzqcyaIqahNEw4ndA3QZmc-OP2Xvy9h3oPvK1UGsw2fvSNuvVK7buURhep0IiCXLGMX65LiS_LGS4931_8zUZ07casYoxQxDzp5HgWRP0SCBYyVN6RaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حردانی: آقا سهراب جواب تماس هامو نمی‌ده
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139883" target="_blank">📅 10:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139882" target="_blank">📅 10:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139881" target="_blank">📅 09:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a73w28_mKADkBIOmCHaj1EUb25RVTVk1T0KYuYWIu4q-73-3GFrvs5MB_UlaYTZ4tEmzWxSHPadZ2hrYz-ma3LNtPDSXsIw2XXMoODsI5UDjuE_N5EVtn88W-Q9ByBZX8_DNBj_lhAcJWm-aJ-lHpJnbo9gDhDtR_yqS8Q_7ETTx58ro8bIgkA0_PG-XhqoFERvdq7Tcqr4H4N2KqM71ycRi5rBGf-72DNMD1WzAcXZ-GcKYJraV_Jh68rVYjykR1a2sIEjpo2ugP8thbkLX7XebKPzrCf3vwLHM1YfFJfD-2fxIBPX9ZqrYtdzVWo1Mo8UPp7V3Agm9v4C9q9WeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سابالانکا مقابل پگولا؛ قدرت سابالانکا برابر بازی حساب‌شده پگولا. ریباکینا در تقابل با گاف؛ نبرد سرویس‌های سنگین با سرعت و دفاع. دوئل‌هایی نزدیک که تمرکز در امتیازهای حساس تعیین‌کننده است.
🎾
Sabalenka -
🎾
Pegula
🎾
Coco Gauff -
🎾
Rybakina
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139880" target="_blank">📅 01:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139879" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=LwTisgNAN8lMLZfhAZZiRCQg2n28XTHkKuQOaCDe_B55KEjmuIvQN0hMfu-WMnW1O5HMR5WaaLjsZC3rF6J2pxylLNIi2jGipvvpcJCwLi_3pPXweDHOzqn5VIfqKyBQjvOLlP1qnluGC84yS0hWRuYiisrux0InlsvMeut07cIszRUwrnvlitXM34xumyp_O9TjaGqTUsVtluyVreT_a5MPxrcvGN6WSAEkME8R0Nt-tI995s8rIOQItfTz8Hk1uQCM7QpdttmGRfDFtW6KQ7zvWiY9h04kI6_Kmrqeuuo3DtVux9TRdgny78He5VIuO6EpiChoGQDE3_lVAwTg0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=LwTisgNAN8lMLZfhAZZiRCQg2n28XTHkKuQOaCDe_B55KEjmuIvQN0hMfu-WMnW1O5HMR5WaaLjsZC3rF6J2pxylLNIi2jGipvvpcJCwLi_3pPXweDHOzqn5VIfqKyBQjvOLlP1qnluGC84yS0hWRuYiisrux0InlsvMeut07cIszRUwrnvlitXM34xumyp_O9TjaGqTUsVtluyVreT_a5MPxrcvGN6WSAEkME8R0Nt-tI995s8rIOQItfTz8Hk1uQCM7QpdttmGRfDFtW6KQ7zvWiY9h04kI6_Kmrqeuuo3DtVux9TRdgny78He5VIuO6EpiChoGQDE3_lVAwTg0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
دقیقه 95 بازی استقلال و پیکان، یاسر آسانی به یکباره بعد از سوت پایان بازی مصدوم شد تا شایعاتی مبنی بر مصدومیت تعمدی برای عدم بازی در لیگ نخبگان به اوج خود برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139878" target="_blank">📅 00:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139877" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra6-pCczp3Jjy2Tr5BJz1dtTTbFVIUUrM8oPe2UITnwFMXrERWwHgtFzap3rvEFNltVsb8Gzt4XvgWsUcbHFmkqpbx18t2VatgfeC050UzwzeR9fsKeHDcPDs0hqVneNJv6tW53ZutP3SkjUCXmFbVYJpghus1UA2BlQCRk___rih4dTGMWI4qyO1bIZ7rexUlFs-TBz1cIVQJzFuJGX4gPS2HNKyncjszQzyu6y63b898MkDtHJ-gdybOLcH3fkIqeIL7kewio3G38sXfDKf9Ey9hNUHq-rmlCj2xBTD8ZdqXlkYQNbcxvDgUb_gxhY7fcKWL9vFgJ6mLbJUOF0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
جدول لیگ بعد از بازیهای امروز
پرسپولیس با برد خیبر می‌تونست به صدر بره ولی آقایان رنگی تصمیم گرفتن خودسر بازیها رو به تعویق بندازن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139876" target="_blank">📅 00:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🗣
🗣
ورزش سه: یاسر آسانی به علت مصدومیت دیدار برابر السد قطر رو از دست داد
‼️
السد قبلا اعلام کرده بود آسانی بازی کنه می‌ره شکایت می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139875" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139874" target="_blank">📅 23:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
#منهای_پرسپولیس
✔️
✔️
استقلال ۴ روز دیگه با السد بازی داره و السد تو پنج بازی اخیرش دو بار حریفش رو شیش تایی کرده به بار چهارتایی و یه بار سه تایی فقط خدا به دادت برسه استقلال :)
✔️
✔️
شما فقط مراقب باش دوباره خاطرات العین و الوصل رو تکرار نکنی قهرمانی…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139873" target="_blank">📅 23:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139872" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI68_LXjFUlVKsMEJu6LRzHzhwHFPNds4AAZtjqgFpXyrwqO8LGPt7XXiIfGBl_SNE5drzifWgBgfgxvDf9Q3VaDLsTuk5e6_WDpPJ1UDKjhHhe225BRio52sCd2XTUBhsDOWLnZkqOlZQLXbcwVSduqUi0Q-SPOoY9vjmpIMy-CyVqmli5-Iceotz-4i3Csd1sQzRHnCV7wvMReFiPTsLV1EM23bMdHNzUJA7uE6yzc8uxSyoT9DLg4cm31OCKSPNAiemdIZX-Gho52VBHWhSkiofhTDpBSS9FHFUbVVXX4oly-ybBsiKmte0f_w-QiN0xbs9w2uKLxymsUnf12FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پس میگفتید که استقلال خوزستان ضعیف بود که ما چهارتا زدیم؟
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139871" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139870" target="_blank">📅 23:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
خداداد طلبکار هم شد
❌
❌
بعد از فحاشی ناموسی و اظهارات بی شرمانه به امید عالیشاه، سرپرست تراکتور:
❌
❌
دارم میرم مشهد به یک زمین چمن سر بزنم؛ فردا از باشگاه گل‌گهر کسی ویس منو ضبط کرد در جریان باشید/ پسر بده فوتبال ایران هستم؛ شما خوبید  «سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139869" target="_blank">📅 23:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
بازگشا :
❌
سازمان لیگ بهمون گفت بازی بخاطر یک ملی پوش خیبر لغو شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139868" target="_blank">📅 23:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139867" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp648j9z0qsxNSZeva9ViDM55CAG3VURCBF9Y6Gt_Tz2nBDE7nUmQfh2qqReCU4ULlACzrLLxvAJFfg6zqsopF7ou4KSTO3dbDwU_ac_AN5iQD2kbmpCUVyycN7E1hird756TWHYtkysNlIraWwHxJiIhEC5lYpSnq6DiX7xj2F72E-GYHMv3owxWs99hpHyS0QWFlOeePvBLSuRW75EUTAxSozq8GarK_z58VD48NVnY0-SuNPZus4U_8II1vdGv3FuJDsKisEB-lEVulMMlxqccw6SPUWzffFA0OsNXBqzgl4At019SggDQOTghOBQJB-3HhwDabnnNWdn7SJOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139866" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: تصمیم لغو بازی از طرف خود سازمان لیگ گرفته شد و برای ما عجیب است که چرا دیدار تیمی که فقط یک بازیکن در اردوی امید دارد، لغو شده است.
✔️
✔️
تمرینات و برنامه‌ریزی پرسپولیس همچنان بر اساس برگزاری بازی با خیبر ادامه دارد.  «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139865" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
⚪️
⚪️
⚪️
⚪️
❌
⚪️
⚪️
⚪️
⚪️
⚪️
⚪️
لعنت به بی برقی ...برق نداشتیم شرمنده نبودم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139864" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWe-W-mdnOJqX7sV9FgE9SXmAi89usVTCEpii1pk5M0zpH8eZNGrCur7WVm7D7cGsoxu9HfXr57fdOWK-K3NDnueK4rqGmqHX6rzN7iENcg89dIt79fZqFusYNfYYURHXW7vUhvr0SZHpGwWU_cRNlT4yiufyVRhE75X-iZj-F8nPYLr7wI0x8DbCw4NWN-LNEaZVdxFWIDYvKWYNiNIfjIDSAoS-THxkCN3NY3mi6XPajIaANb904huNMUdTYs32VQ6NwqcjYkPEt02bHC1boF3WhsYRNAmr96cXGKUtpr-0QErdXf2_ERVGgbSKjrmcXrIxhqIwbjTMYc0hXfM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Bayern -
🟡
Bodo Glimt
⏰
Tonight 22:30
🏟
Allianz Arena
🔵
بایرن در برابر بودوگلیمت؛ بایرن برای جبران لغزش‌های اخیر به دنبال یک نمایش مقتدرانه است، بودوگلیمت اما با فوتبال جسورانه می‌تواند دقایقی دردسرساز شود. با این حال، اگر بایرن از همان ابتدا ریتم همیشگی‌اش را تحمیل کند، مقاومت نروژی‌ها خیلی سخت دوام می‌آورد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139863" target="_blank">📅 21:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139862" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139861" target="_blank">📅 20:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
تارتار:سازمان لیگ بیجا کرده بازی مارو لغو کرده...ما هیچ درخواستی برای تعویق بازی نداریم و میخوایم بازی کنیم...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139860" target="_blank">📅 18:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139859" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139858" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139857" target="_blank">📅 17:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139856" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139855">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139855" target="_blank">📅 16:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139854">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139854" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139853" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139852" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
با اعلام سازمان لیگ، ۴ دیدار از هفته هفتم لیگ لغو و زمان جدید برگزاری آنها متعاقباً اعلام خواهد شد.
✔️
ذوب‌آهن - سپاهان
✔️
خیبر - پرسپولیس
✔️
ملوان - فولاد
✔️
فجر سپاسی - آلومینیوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔔
🔔
فووووووووری
🚨
مهدی تارتار با لغو بازی با خیبر مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIG8DZ9-SCNO_djPpzZBXqlKkmyUYyjPaAM-ImYFp2YsSJMDkynyNEBxyxqdEcvrNordtJeGdHkPWTuZ5-m-CyfSgkSbx58XLfjJhsV_FJAfgm7ZiS-q4_S-e3zj5nkLR13DLmnCaaxDRFB6WsHfjqy-NF983VDXJmG0Zf3zvbb8-KBooGiHA6vhz0yjDb_5rbSw21CkRa-kJ20fIzGWaSE7RG5JbQnn4xQOBkIUpFax6cBlomCThb80qQSJdCYGemImx52sb17zuI7FWN8PdZGhvk0iwOGy2bxm7GXXvlLDMfJfhMT7f6G2ULlODoDc4l6b5GWfCzs6XKXSW_yYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مونیخ؛ بایرن آماده‌ی شکار بودوگلیمیت!
⚽️
بایرن با مالکیت و فشار هجومی بالا، شانس اول این دیدار است؛ اما بودوگلیمیت نشان داده مقابل تیم‌های بزرگ با جسارت بازی می‌کند.
انتظار می‌رود بایرن از همان ابتدا برای گل زودهنگام فشار بیاورد و برتری کیفی‌اش را به نتیجه تبدیل کند.
[
بایرن‌مونیخ
⚽️
🆚
🇳🇴
بودوگلمیت
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

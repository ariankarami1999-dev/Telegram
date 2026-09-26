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
<img src="https://cdn5.telesco.pe/file/uzU0bHE8WD7WLD1RwrUy61HU63NqUuMbybJyaDwe2uMEWy-sY8kJBkNF3wDbNPJlmbjmKYpOMIvSmmjzHwwX0XH6FeII2MwZbr2YgW50TzttE7SKep-pC0Jz8wZPiSDdsvKlAigj6kbmPw09Z42NN9wYTb4jp9es8F7EDBbDmt9bIhbhpJlTArGKpskuqhxmyZXgBU_TZoxZnY-zgtLYoDbEpkqKelZ7Ext0yE9wDoa8PIyTdodov5BmagSUrsTuAMRHNNxbyVoGt5BzLcTSzb1N3s7KqLPTN-aHqUt1N31ZFaMw1fpHCQYhqrcBrk3l0zW_nwIzjdYsq3y_fTt9sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 399K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 02:32:07</div>
<hr>

<div class="tg-post" id="msg-107351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/Futball180TV/107351" target="_blank">📅 01:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIR9rDfmWiQ0B5D7XZOBxHhVMfZtEUfJNPVnzwZTshWBbQSVjjOExn9_F-QFnOCOGIfc24OfDYqfh7ZTpx3XqaUWukJ8UdRce9GXTgmErF_PK8Mw2MyT-CHAdYOPSA5NaA6kbH6k_ZeBpRfrIVpbRMmB9kjO80mt5mrPqlo50LF0rTfp_rjQ6fBth5fXlx_6DAyXpIbSInTWPEaS79XSCYQbc9iYDbIwAjQhSYhWWEYaTjLhmqCULLY6mBeOq4x5OuWvRELpAKcuyFop2rJkcvpV3HoxcDMSMcC7FYvFwjO4nfk9_8vpZgS7XbIxhZHC_ogZMiSiCkIN_-CnwMOQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/Futball180TV/107350" target="_blank">📅 01:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1xZdSTQ3vcDjbgDz4IzxISuVmuRP_2EXw-mBFZBZ9SOKOBGOB8ODHGADmA0ZnH_RuZ11DugO9ffsG_0Acju_s9ousQIc1_6JIfgYMqvFELiSu152aMrUwstfwOFUJ9QtcIh2_3dM3vH0K4pjAmVzSeyDzkFelzRc-olxWrh6pe1a6I3buO1ArW0ZNCvhztDzjSPVpSqSfXzjNBL3NzNrFgVyVe7SKeR4SVUkXBnGK3PHrHffc7JkuIblAn4nZQyKsAsnDDfRarna6oCfZOWpqbI3c_R0rZobj6HnE-TCn66OJa55PYKXncp_nCaUQEfSYLT1rfMsBPzUZp6gMsTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جیمیل بسازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/107349" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q929dFC8TvUw28mfwYdb6qAntmtyaMKfnOQbyi7Mrn0kyGI6RmSYf9xSH_5J7alfwH-oZI-fgN43I8UcDBmZtKOcKjip26NpLu0n7i5otaJMD__JfZlYwCZYJrEssSgIsip01jgexJf89bIlDSJkoMxfE6WlOojpQ72qeRuXDg9hH2r9t1tUnTf-cbCK_k3bsNAoQOzIcuRlVGhXPwE9pTX4YC1ZtO9hRD79Bx5MKWJZ3pe4198oqoBJYGtecSdXDlESw4KnW8MiVYAaz1Vrk0mblz2JghF9dRi9sVilt0q32CTtO8_fAPwZd_6eCPj1S6f5MZ28l4ETK3b2FLxz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇪🇸
فابیان رویز تا به امروز هیچ بازی‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
🔻
51 بازی؛ 36 برد‏؛ 15 تساوی؛ 0 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/107348" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/107347" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIWdD2AykCSdNiO0pwY1AMOVhJYoxqNHSIp2onPifZNN8VBEWyNp80oN5x2tAGsy9oo59K2YIj9xFe8rUr-QT_bZ0FJTnIJlBJEfMHs27DxCRwJRGtDSUItLQ6SfRhZKmN4vSMDxLM1GrX22iymoc2AVwvk3lXZqKIpuwPTm7_yC83L4DKt9_TSRzMOiIN_67k__OldZbWtqmRsEuvsBrRMnElg7P85ASWNQo5AiopSXuUW9TJJ2aBCAXMr59kFrZUPQeu9vcQGPJuxvMa5c_LyAwZ0QCFtUfg5EATQI-1m0zEDG5gIKvJP3glxIipx7Jmh7RU5I9OQlOxxP78I5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
طولانی‌ترین روند عدم شکست در تاریخ تیم‌های ملی:
‏42 مسابقه —
🇲🇦
مراکش [2023 و 2026]
‏39 مسابقه —
🇪🇸
اسپانیا [2024 و ادامه دارد]
😳
🔥
‏37 مسابقه —
🇮🇹
ایتالیا [2018 و 2021]
‏36 مسابقه —
🇦🇷
آرژانتین [2019 و 2022]
‏35 مسابقه —
🇩🇿
الجزایر [2018 و 2021]
‏35 مسابقه —
🇪🇸
اسپانیا [2007 و 2009].
‏35 مسابقه —
🇧🇷
برزیل [1993 و 1996].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/107346" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7pLV58Iscxqc4yMYOM5NUIXiY0dIEoXsDPdnlg_lEAmFKC1BQ9RM9YgA8PiOuwMxH0qmpqJxKYWENd3hSIUac7vLYWF1uEERRfCid5iKaATtc_q9FkSySsLWTCadgWmLvI9fJTbSZBjb0GYjhpgLVXO-aX8Dz7CmhUwHe5rX0SYVcHkg8YgJmAKEUDnNOoYG7EbqQP04MxOEA17kFRstkJrct5AZ88O5T6UeRLAcHvQtJOjOrVkfWaLJ0HMPhk3kX_FNyWmHFmcIDcDCjqhqC_fL5KBBZ2CClknHBpiR6AIYbG9UKkn4ECqbHudT_12hc4HUVMikYehJGgMweD-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇭🇷
کرواسی در شب درخشش لوکا مودریچ ۴۱ ساله مقابل جمهوری چک به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/107345" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHxzLENkfwDH3FwIwt70CLGBLkeH0hslqNQLvgXcSdlIZygDC35D80jZu4-G2hu6aCLDOvpBLSLRz9ijppR0wurJBy0Tbn3pqw-j6iiKTivSWtWGsrWuYSwZHOOyEdk3HzdHZBTMQGFPfQLvfowkmQ1zTCOHA4LyCJQ-hAhw9PNcotSodSrx0jwiwx-2DRu2CBKAU8BXUvj1r0jhM6BtgqGqgB12XQb74N-xvO8vu5nXyQBAk1vSF8nzH889CMZUQkuZfYnBOnUHGu6ZB67ZUlmW_UkM3eCAZpmuFIDH2ZKcYuMOO28bcy2NM4eRfE9NIU1Rg7_M_L3Cb1PlJASrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ‌ملت‌های اروپا؛ قهرمان جهان در لندن انگلیس را از پا در آورد؛ یامال بازهم ارزش خودش را در زمین نشان داد!
🇪🇸
اسپانیا
3️⃣
-
2️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/107344" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=ha63Y4ZMQhdXa6rx5BAvEv3vQSXWO6zbskT6-dEnYm4nTyGCs6W2dNvkU-4S7VKi7WZeHGfXzM3pIn1AntqfMWMkwdeOVCk9H_-zakD96Ml9zjncHT9-xkipwCGvF6Z2GT7glJwqUTOMuIySSQu6w2VJ4kr8Pg45UYPa8C4H8GjHzhU4TKbLYDMbQkNnadTMX5Ig8Kz3dWech5dRF4raUPvBoYJMmpSkNPDEgxgKp89dcF_2Xr5WTrig2eNpLiBz7XEkFxFwB3gGKx4oG3co6qKCAInajv_71mySTq_l7zmDrXRf7eK7ZXptujaBi92Z3CCM4QTraPfFFxZTD2ks8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=ha63Y4ZMQhdXa6rx5BAvEv3vQSXWO6zbskT6-dEnYm4nTyGCs6W2dNvkU-4S7VKi7WZeHGfXzM3pIn1AntqfMWMkwdeOVCk9H_-zakD96Ml9zjncHT9-xkipwCGvF6Z2GT7glJwqUTOMuIySSQu6w2VJ4kr8Pg45UYPa8C4H8GjHzhU4TKbLYDMbQkNnadTMX5Ig8Kz3dWech5dRF4raUPvBoYJMmpSkNPDEgxgKp89dcF_2Xr5WTrig2eNpLiBz7XEkFxFwB3gGKx4oG3co6qKCAInajv_71mySTq_l7zmDrXRf7eK7ZXptujaBi92Z3CCM4QTraPfFFxZTD2ks8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم اسپانیا به انگلیس توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/Futball180TV/107343" target="_blank">📅 23:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/107342" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گلگلگلگلگلگ سوم اسپانیا</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/107341" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=APdzDacQIyZh_xWhvp7HvXpvnZFL9pz6Elsxw9YltBKJmhlilrw42tmgfSC_pcToxkicqWKm-nyvBdiKE3va_oJfvnxKEajdy3VG0TNvqEYZ0BCcpq5HV4M9i3J_a4hZdstkq1IqMMtPYDaU0IACPl8C878m8yUIEYvSIjgIWetFkeWRm1MoH6CqSKpUTKY5Vu97JvPBLddYxtzPr-qgm5MDg-rd8jpOwqqBBhw0aG5zJ50uFcu40CI7zSO-GRu7iQVkh-FgvlqGBK-xPYAVBugdeEj8PVjTId7giTE9rZGfEXFFosuNnUlwGDLRcZDb1bAWFQLSncFBLbuApcYmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=APdzDacQIyZh_xWhvp7HvXpvnZFL9pz6Elsxw9YltBKJmhlilrw42tmgfSC_pcToxkicqWKm-nyvBdiKE3va_oJfvnxKEajdy3VG0TNvqEYZ0BCcpq5HV4M9i3J_a4hZdstkq1IqMMtPYDaU0IACPl8C878m8yUIEYvSIjgIWetFkeWRm1MoH6CqSKpUTKY5Vu97JvPBLddYxtzPr-qgm5MDg-rd8jpOwqqBBhw0aG5zJ50uFcu40CI7zSO-GRu7iQVkh-FgvlqGBK-xPYAVBugdeEj8PVjTId7giTE9rZGfEXFFosuNnUlwGDLRcZDb1bAWFQLSncFBLbuApcYmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی اسپانیا توسط الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/107340" target="_blank">📅 23:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=YfJEg4jM0VHylAtLucXHToDEukNrU-L0mdZkROPKie9TsOxcSVpoSAxgL4bzQK2hOitTm0kCOm06XEAkWIDG2xlBrydo6bxCGvZdSLfvSowOPX2c47ar_4lyvBrudgHNVPDIhbQgHtkkQOH_v5jOvXs-5nc973jbmFKcyExUcMEM8gFU1vRTBKkZQUkRG2N0_konT1QzhOOlbDfyahfupUImrznj0zl__UNY_zvHrVws3JLDN5RpG4TAwjeK67wd50NdTae0P05xn_BGnVIpvw3Xu5ywSxN3imlZY_JdUllzOv9ieu7UNcy3Ab2FzE6dA0EpOUbd5c3JTRoSRu137w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=YfJEg4jM0VHylAtLucXHToDEukNrU-L0mdZkROPKie9TsOxcSVpoSAxgL4bzQK2hOitTm0kCOm06XEAkWIDG2xlBrydo6bxCGvZdSLfvSowOPX2c47ar_4lyvBrudgHNVPDIhbQgHtkkQOH_v5jOvXs-5nc973jbmFKcyExUcMEM8gFU1vRTBKkZQUkRG2N0_konT1QzhOOlbDfyahfupUImrznj0zl__UNY_zvHrVws3JLDN5RpG4TAwjeK67wd50NdTae0P05xn_BGnVIpvw3Xu5ywSxN3imlZY_JdUllzOv9ieu7UNcy3Ab2FzE6dA0EpOUbd5c3JTRoSRu137w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به اسپانیا با گل بخودی کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/107339" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=saa9cjiee52UmFajFpQAjHXtirwqtbTPgxxd4KaCs1sGOIcjjU1m63-sosuQ7v9RMGuWoBqsYAyCA9mYas2UipHJDcQ9lDO-4dOZFYcKNNqxq9AFVUA1V1lT1HQbEe41uyAL44veDCHPEAvdMpWJhJTRjJNyySk5_4N6Y1dLylWolfunJ04ukgrOMLLzd-cT1iJ5jhkYwDN5jn1CI669XgVCdbyezPqPIrt8QT3Ki9xrxqEIVYGo06YwGRXHP7GNEyyvZpE_kx7qJoe5kfby085tBld_3y_z1HLtj6UWprrCBG-hp7stc8B_z2d18Uq2Bws09Sxr_OIwFIUmn6voig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=saa9cjiee52UmFajFpQAjHXtirwqtbTPgxxd4KaCs1sGOIcjjU1m63-sosuQ7v9RMGuWoBqsYAyCA9mYas2UipHJDcQ9lDO-4dOZFYcKNNqxq9AFVUA1V1lT1HQbEe41uyAL44veDCHPEAvdMpWJhJTRjJNyySk5_4N6Y1dLylWolfunJ04ukgrOMLLzd-cT1iJ5jhkYwDN5jn1CI669XgVCdbyezPqPIrt8QT3Ki9xrxqEIVYGo06YwGRXHP7GNEyyvZpE_kx7qJoe5kfby085tBld_3y_z1HLtj6UWprrCBG-hp7stc8B_z2d18Uq2Bws09Sxr_OIwFIUmn6voig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به اسپانیا توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/107338" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=LQmiKNiLjQDTpOeKW21ADsZCljmtP-j32XHhI7l3n6DHFrj6Du1VNjx4MxSxNtzZW0CDj4DVAIxzQulwoT98Rd99IAQV-vjlbMVw0_9lgtHiaK4ffasmZq_8u9ZvEXnMZMVhqFGAB_RSckJ2657myA5tK6PLksY6Tg7F5I5BSb7GrFwKuxzVgs4aLDnmJTapUYPJlZND7o_veB5CKfoSaTOPHudPQKfh5Pk_LupetEx5FW4Lm9keh5zIlnJlLMyq0tEDYhqUseAhFysghhCRRm4ZNHHC4fYkopnvxO1HJ0XN2RUEnop0FSIsR_8dyB9lAdB-o8YbMOxEU9RQFJokKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لامین‌یامال زددددددد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107334" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107333" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtcNZAI963K7MzrPiPpLdT3qG26a6hTqhujuR4jEHQebgpPGXQuDjw7ZHs7fkMFrizmlHBWmiTZu7CNJ1-rlKyrrSkngp7kbwTR4XPMCaOyc21Spn1UkHkDHt0JafQXfMprk88GLqJjIrx3jTHu1UTT4NCt1hf8f_RI6zuXUq0JB4hlw_2pdqmMeJcnQNAp0oAlak1EqvlAvUjNN-tTxuquEtRFJqWbkZPzC0H0402d82wLynhlsYFZCiHlscXA6a3xzqkJrYUsDphlTPB_cbhVKMzZd66ENlIc0cgO2HGhyPBo-IKgZmZM7h4c2D_FgyYXtPa7pBK7dV5TaBLKduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107332" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇮🇷
تاجرنیا مدیرعامل استقلال: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا میگویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107331" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka0cDNi82DDVPfPiKGyUIOsrg-9DAbvXmEWwPXuF--rn6h26mw44kb8z2AUI9nBved4G3Av2mqys22dmZLo92HsjeKjHoGQhM0Mx5UBR5S__mGbVgzmXyG87a0z8q60oVozZ6dqc2Qr7P_OiGa0Zc0HL8BO7lFht013RJfyUyW6UBcvlbRvwdkPmiV-10_LYwlOp8DnG5XKj_bOSQYYxSPPf92CRXyKE4aaxG8OrftPL6-dMToTSqKKXNqeVPspw8rGBNv0SunShjZFJcEeygKEs-sA8GDHgc7-NpwIENuP9Mb3cv2il4sHle-4S0LU3sVd9LRk01z3f_SEiDHxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107330" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwIxbrehJEtu5r4ydtTEPZLqSaOYGQLlaMz9-50iMQJ0btbcF9715q466Iv8lOkOwqkI3WS1l-VczskTVEZL5foNENNIZdWIIHBWZUPjfykko0t7jUSSzjR4jAYiAz3sP9o6Lc3NhJaM-nGtvQbgv0qDGgudRltSYUGQJCdSdfbcJSdRDNmVGodRGXFtIX398Jd59c1pmQA3xMNdCH2pzHTbaJJI6BnAHwfVkgmhA25ewIFC9SEyZ12t70VeEBzQvTG9t2rCgJPzgUN8kxl7zQVGfzPRKh9_LoaoUR_OHr8pVXRfntn1-mwKcwX-uIqYjwVAvkwZv0sG_GTRlv4FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آمار تقابل‌های بین انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107329" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7WHRDf36BDZhmJgbxph6oBHysEIx-Ep8j0Nm9WcKROhJqbZununRezyHQyBEAvZbk4InnFyi-m9P7feJPGGwTH8jtHh5xiB7LsRx9RtzXeJ-baFzcYVU6BNhwXsDMu4sgZdb40kpK12k7qRdmjG1mv1J8pQmqOx3-RwXWFuW5NnP9PJnWfA-3E6sMD4_SHAlKlKQR7S1VPk5HYkoE1tm8o10y6v7pQ-GWzZSzqye3tU1FxmCoHmjnvVS-X4_BVz0oJ9tzfx21MGpzDSuogPegV5rC2D4fS6Ds4fbGj_eyuAuIqhrVPJyTPTQnoILAlSMT4gNpPULKKPCl3NjhaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107328" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=hjWiDxzHJu-UtYwVuWLape1m8UvihnuQjP3qNTkThOERh8btWQY0b7eSDc3qUoDDiUeoRh73moxNIHVj3TIqrsi9jGKvFWhCwIYYwXS05caOxbQjnDHWfU3ZR08vWry57cqOqi19931v2CgJw8EVDqrR-s5Da-VviB84DPSgJoeExznMD-GNriOFrA4i5DGWnpKbesoD_fmW6VpFu85sqvt3JyEDFciHm3s66zDT1YldMo4RvFtqgj-t14rWj8vzfVwxRYj-dS1qV4dGFXHLu7Geww_Ca4c3zQ1O9rr_661LYTw8GIB5Z7NrMOF7_BueaXkvzwFJsSfDlNJST16FRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
توصیه عادل به بچه های کنکوری
😮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107326" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDBpM9jX9xOhB8CZPd1vsgk6bsS5-UkPeWcydlsm67bdPZez5xYP06z0-ED0yLhv6DIRcX9GhPUbyu5sYQGlfLcXBCZGaPtE7uRtxEoRTpHVuTvjotkP53lKuDKdMMCETcUOHsdoxiQWD43ceiHV1i61g5-1x1BybTQDascMmNazUNX-ABJoW13Cjz31IyHN1NM3tDfIwAVfXPOeMh1Z7Dq9wRHOdaJEJZDS5kIrDA0PVVUfw4sR-i-3u-Zfi0ODnovWp0l1r37IZMhe_X17MK7TF85sYfcYpZr6qZ9_SgEq4fF8fulcLoeWtNo2evDFvw2X8Nn6yhKGQX4JKnQ-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107325" target="_blank">📅 20:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUSqJduvM2oaAPDiJ2wQ9z-k6u0hrZm3MdqGSDV24d9TpK9p_s6aNlmP573Zmn8Cgkf4zI3x-RH2d7zZq0HGk8PkFixLUIMRCTZfZH4KxZ2F3ASiPk6U_utBzTX0SeLKgyUoODJ1CPhjh4gsaSyVY9qM6srSaH1buquO-39G4nmY8M9fuVdqfLWXd_ZEtIOjsZh_HWvWyiRpg2u4Mb-yuZH5yhj57uPFiJ8zEhNjTFf_Cni2O3yR9xgLzgO-BZ3coFcWE39W-b30jYhA4dAptTDCwor0mEQC8TEVOmubrnpUSJ-IDPb12kLN1HNfdrqcGeO93B7OGQDXEr8vAEvMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO2sTbwt_sv-qrcjTNEkJHkgdFkHt1HJUW-IirgGXlVQnq698vFeWunMIOMjgFYOpWmwnZVcW_58DlGRoreC2vkZzXVvgcWYI7A56XLxkofhSjL19enT1evfkX1OVT4T4ajV4myKG58KcP3YDYXwI9tOfD73GRwgb_899kJJoHXRi8LVJxSp4tbY0IuOWI2Qt-pGIVJsmqY5uq27NYkIZvOJPxCgPTh6ZOlNNIcMv-KOcpxU9_xGvWG7s3-wrcUSNhv6i63vXoBl_emeZ_Nc1FdBCvaBVEzsY72cICGuSfRlbGbXX9lmqVwfajv98DALFEuV7Sh4w0S4UOrbmkFAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq8cB_xZ9TbuJAbE3_QJIEW4l-0TvJiFYOsl7VqxTh-F8_KTNSfTamanBHnNy2MpBSOqo9CkzZltwANPI6YLn6wlupEnVbC1rkyWqAnmw1IOmlmvWaE7orCsJQyp3s_NaB1LwFSzy0ELT6RW_AzE83MwoSDZozTa4G5nbA3zfnmdtxShLtKkp-qZlAd2zJNLcIMPz-50AzaAXYtsSjynU3K3kSykmJgPI30-JWmfdoCDHfY7RVS1x5ozsR34y9kXv87U6FJgImS6YdBRXL8qYTmloVrnqwS3mZDcfB4EcAVuF76Cu5YwWwB1lX1JR0p_GpeVvZIz91fCr5_rv2kXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcb-6f020xGg4yUh9XrMI816nO_WIbt_PXG0WEFv9TEVvfPXIXKGTGYVnacaMiGy0eje50qrOJSgHNs2Jx5PkvQ1FLXNVx_Lr6VZzxhDiZaDxuBKQxRBGLhgZG5v3W20amzjU6tH00BGSvqUgm_v84o-go5VL1E3ylUo3A-kYUGt-N5NCUnXUyIPVxgucnMriYefVJw7bsZEQZMcXjy3GnlzmKJbz6tQdvAD2Ub2626fIbUZ3sZY7FvmqrJ011VJkJ5nmOpU8G2JJsxQfRrsdR92wRiNeiezIioWTYyEny-3ccr7i1oyg4wIIdJJANejCOKuAdggVUbkBpY_XTC03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107315" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107315" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKSBBY_7KsrtjNizvFOseIR1DI7bgX7PO2zL_V2D8EYr_CruZk_trA7Ohur-GlTOaMt9N7IOVzSGMdx8MaBkjiXzSy3UqJfCjvRFeTv8s0zRDOHfS8QsPB06ZDCYOza_PCn0Z9NnOw85GUpahKhbljNeafyGCghPzpez818on_VBAnVO7AW6ogZtG2m6V_Um6bsQcsnon6RWCS-Xu1Wl3NScjTp7ApKPmcZOUvIkiz1kB47n41zdySsaKRvcVUfL3mdj-ichzFipZE5yOjxn0CVYolqcPA0IZVZyGbuZ5gN4EIlHDXVQcEThbPr3MIfR0b4NP_XjsKzRV4lPLKCzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107314" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRBj8tc_HF7cfrDI3zeyf3J1CzCH3I9XfgrZS0fTZE0baq7tWcPrce21ryXuwVfyImv5CpRDI2Hcw6_DBIz-SktiRvftsAzgjxzboVvKDFwhKxz8uA6H2hVK5D58lQcSXdcfCOyT2SjdU_zTlfh0uuWDQPrUoHiY-M8XcAxyZjmOsYStejB-XhA1FBkSPMucp_WzAVNf4u6dDtpbrB7TVBPPek0XG3fKltrK-O0ycldg7HWg_-zBCdz4iAylzvJtH0H4CXhO2uvqgi-icCXZI-o8c0lFZ2dBcFgjCRSi_DIjauOMoIjkPgRS08RExFaC2lv4sD7_JruxN421LeQxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRrlcVHzgjKtxCpDHLN6Legf5JXrdD3Yt9eyIm1QtBvo6ivC5mgfkEB0jNe83q9Pe_5yglTisGfkHlX_3Rf3j5ArkyjpDEuxKT0UylBEy2ebmIZKfwVDFdbWOhK3vTQE_jYJElNpbSDGujwGJqAJBsAj8iN_0L9cvX-HHG2-uOwUtq8eV6wuInY_z2fqJqZyb5LS-Tu0llurv5vGPNFS04wKtDRn3HbJ7NXHqEtf1hplS8CzgJ1Bdbxw9ztkDYT8uVI-f034l9ZPcBEgoeZKnCcxFHYmwZjsERE0qVcxOnl5shN7jIGyyJ-dZzdraiWCeoc1g-lUzjh-EvYTs4nRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=P7TSUD6Osa_i_kwe2Zb1e1RsjDBZ_tPS4L1tFGiI3WdaWdzogk9DrcDoy55aZQze8pfFqeZIxPFoxDfvzHTw37TTyP-avayhb8vpbSOWWn7MLW3II3hqet4K8fDnLCpgPY24u605-HIn04Ce8mGW0iZSVZ7QNFApSTiDynGS0dx8M___m4U_FwyzzM2dhUKj7kdFKnCJyuo65adT9PXuZxWNscktCKRSSwsieVJ807Zzn1n-4xa3z9hVxkTfGCL5lg3Q0dVEHZng9a0OsUdCX7PflkG6ttRq3_HVFP2GS_elegErF2T-X93dXSd1OszIZ-BBg-Ya5bye_N5gXtBSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=P7TSUD6Osa_i_kwe2Zb1e1RsjDBZ_tPS4L1tFGiI3WdaWdzogk9DrcDoy55aZQze8pfFqeZIxPFoxDfvzHTw37TTyP-avayhb8vpbSOWWn7MLW3II3hqet4K8fDnLCpgPY24u605-HIn04Ce8mGW0iZSVZ7QNFApSTiDynGS0dx8M___m4U_FwyzzM2dhUKj7kdFKnCJyuo65adT9PXuZxWNscktCKRSSwsieVJ807Zzn1n-4xa3z9hVxkTfGCL5lg3Q0dVEHZng9a0OsUdCX7PflkG6ttRq3_HVFP2GS_elegErF2T-X93dXSd1OszIZ-BBg-Ya5bye_N5gXtBSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK9CEEEHuraNgX2N3zyTEnBhZg0Grh8prpg6A160_oGp7swY6ocQjXEZ0uUeCv-AiGvrgRUDdP4s6oWAQMGR1WtShZEmswh4kXSPVZkDtgq2uCfDpdGxUV6dscEU-fk-vp-CEhSX9eLgKRsSJl7ORzfzSfGulK-3MwQrJRkeuXFP3e7VQcX2yK2AenJxAgAC_x1X6C_UJ5sMCUmWKltbQk4cUAoZmcNtqPYPphzLV63lq3M82w9ZUIrCNxlDj9revXysU0ZOO1RSwOj3tmHOSXH4TFUCvlsX5NuWbl44pIPtTCuKt1VQGU9VlI8VTalwmM1-m4B9zEFEqbI1om8RtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0woe22zJH8J78Fh-mt01wktPL9201vXDU_69hHXHMEP_JYuesMEszkWnb2qfCtuEaTNkdW7IlMsqXATeaMZZxUpyo7pVXrC5at0l9wkNyffJfJNZtQKQeGhwLNqmvVR_3EE7jxRTCeZaIdXOCilwsl-6y830eIpANGtjYqPTiIdAm26VGEHw2A92a0Ahy9-IM84y7JQO1BZi3EDCs6-w5ciMbjKvEtQk6uiDpcNfMGyBu4wiyi7gjiciVM4Zp0IEQxIQ3iI04NDDOZM4-B-k0TV8r8f8Y-oMQGYTQY8JWv872NZnUcOmRvaDV9bpy-ne3Xvl90WcpC5HEnIwYQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgzraEbxAm0ZzKO5viLq09yOr1BXx5eAz7rPk976DqxmYQiP_gH2bZcaP0dkMofjGfRdzPS6oo5xBbzuw6EFjn0-tkjRBk9SGt5IH8tL_Im_sH7MBZiXEDWRmZTsLkY_nQasmrXYAFs5o006IFeWSeViAxnrwII0dpUMreQ4OaJcg5TM0XrT3PlJLve2HSOfwlpKz4E7L9afrhN9JJl25QjMC0Rj2qBTRB94JLup9CsgxSC-wE8nl0D_wed5305TwxyzyKkq6Do9vZLbMIldd6tZwMuTAKYc4aeDxnBrfquKLWSJIUgYZlI6gZ3WQN1dRK7NJzmU57JJfxjVIe9Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJBUz01LVO8Q9kuFB7U74LKgO21HhQC5oynMOUgojdUnypOy8cK8EiDj1aJfUuxWs9FFPujRZOrnvOe0YTwt_vt6cU1B-t8oyuTgm2oSj4anSE3gMIRP91kktSImKb8BtVQELesLpNE1yxFKAzJl3j_Gj1QlhpK3B0qdHgC9R5xpEA-w50kboEqbqMD9CcbqUgO6L3isvd-fPcAHWYfEE3OQjXz-x0KFjneUxQfA_daINn8g3pUVIUITBuzjA13fo6FUAFTJ6_EdB_UTXvuU_Nb2JMIO8rD-mSBxcJU7ICTn38w_Ai2KdMDx3uudjdtMU474ERVB9CnQjqL_2svXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107294" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZo_hgBxoD2_quLX9o2zRGMHRLOFUertLAxyHeIVpomnqcxNulgse4HgbavfzzcoDplCsbKnQn1-mIAKsEznRvmZvVw4obzHPM0vjuA3QBdeoA6kh0-fkHjliLdlmsCYzXv4KJY7hyRS4T8azoTYKA1qE96uKftkYphWcV2skkRzY9wmuGyOp8FSuIT--ruzSDt7m-x_mINm4DovJLLhaCXTiHBl8pJIYDYH2pHFNJ4fAAUAGTlTmwOjISiLd67_X5oUjk1rmMh1t9BO8TfHLlRCgqlcoZZ3GtLVeWiINorHOYLTE6JtiCbP9HGMyZKhConba5tmJunHEUCL0oZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107293" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=CFeVzyXWRDBAQOpej6r7yIzYsGBdxL32BDadHegRgLdcrv-GQ19N_ZuLgJqkvdVgSpoBPzp6jPRPDa4vi59QIFJaczSDUcQs_jbmpRSX11Szswco_O7CC9IfW0qAIb5qJcuBlauHJ5-6X8GcG0csJx9dFMjUp0y1p1JAHWgtjQhtUTM2aYxryr1QkBAIMFQefZbWTNs-f5SVZLAi3WWultK3ZB1Q4kdc_C3VcTA16nX3kGb5OOOdNCgQfGAPE4BAqUaH6NTNHGmeZ3iXvudCzJZC-rAKTEgcBK7Qs7i-5jUbAesUxGgFQlIhoVIcQQ9inBohf0UqDQGyITfkbLwvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=CFeVzyXWRDBAQOpej6r7yIzYsGBdxL32BDadHegRgLdcrv-GQ19N_ZuLgJqkvdVgSpoBPzp6jPRPDa4vi59QIFJaczSDUcQs_jbmpRSX11Szswco_O7CC9IfW0qAIb5qJcuBlauHJ5-6X8GcG0csJx9dFMjUp0y1p1JAHWgtjQhtUTM2aYxryr1QkBAIMFQefZbWTNs-f5SVZLAi3WWultK3ZB1Q4kdc_C3VcTA16nX3kGb5OOOdNCgQfGAPE4BAqUaH6NTNHGmeZ3iXvudCzJZC-rAKTEgcBK7Qs7i-5jUbAesUxGgFQlIhoVIcQQ9inBohf0UqDQGyITfkbLwvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=dA_NL1aNx5eOWHwhX5sLWErna_vQqjwDepw4yzB2eqC0zg8hd8iBbN3YIYrCKHVmV7QqFX0VZMKdwl0v4N3uWdywCjdEchFkTKNDJymY3Rw4rZw5J4Iz44c7u8DArUqTH4FD2k-wdkxpIREHZPsy8zUTWdzk2K8R54BcWURVYTBmhyhZmbbrS4W149E9E1l_8pzx5x1JQYPnRWFW6AtFpCM7Y1vgpP0Mvm1AlD_gkyaZzaUbzyetGd7FM5YP4xQUp-ABGht-1Y_Ip9OZKtUVczjvEItmr8xV9hDfm0l9in9frtj0pRfGOK1_21oncdn3zB3q7zl7VE7CFE5jzAbXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=dA_NL1aNx5eOWHwhX5sLWErna_vQqjwDepw4yzB2eqC0zg8hd8iBbN3YIYrCKHVmV7QqFX0VZMKdwl0v4N3uWdywCjdEchFkTKNDJymY3Rw4rZw5J4Iz44c7u8DArUqTH4FD2k-wdkxpIREHZPsy8zUTWdzk2K8R54BcWURVYTBmhyhZmbbrS4W149E9E1l_8pzx5x1JQYPnRWFW6AtFpCM7Y1vgpP0Mvm1AlD_gkyaZzaUbzyetGd7FM5YP4xQUp-ABGht-1Y_Ip9OZKtUVczjvEItmr8xV9hDfm0l9in9frtj0pRfGOK1_21oncdn3zB3q7zl7VE7CFE5jzAbXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=txuTvRouw8QlX7UDqahhToRlAI5DCg_HQToKUYCuA4J6MEMo15DLxKPnUH397V5PjOXfTukeIkVxJyP6MbwINCWe55n3LKuYkBEUSUwoYo5c7Wd8ifTQpp3W6x3ErfGzy-nFPP23FfSHeCHIOQiDtcVL0ADUlsCZAiuxqu5LJ9AhHEmSbgR62aLAuzDeVUv-qVdO0xudkuQ1sxdgtNDdW62FFNeGV8mPM_PphdWbV9Y69Y2WGZVbN51wta5Jg9xBzBnpcoMiaVmewfBhYdXkxjWm-WkdB8k03X_sft3GduL0KUhqemWtOYzSKxFxRCYs7iwuIqfezSFDl9X6coHBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=txuTvRouw8QlX7UDqahhToRlAI5DCg_HQToKUYCuA4J6MEMo15DLxKPnUH397V5PjOXfTukeIkVxJyP6MbwINCWe55n3LKuYkBEUSUwoYo5c7Wd8ifTQpp3W6x3ErfGzy-nFPP23FfSHeCHIOQiDtcVL0ADUlsCZAiuxqu5LJ9AhHEmSbgR62aLAuzDeVUv-qVdO0xudkuQ1sxdgtNDdW62FFNeGV8mPM_PphdWbV9Y69Y2WGZVbN51wta5Jg9xBzBnpcoMiaVmewfBhYdXkxjWm-WkdB8k03X_sft3GduL0KUhqemWtOYzSKxFxRCYs7iwuIqfezSFDl9X6coHBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=Qshv6I2HhMCAoE3sXQ6yczjm0g7pm5hMRbbTRe3f1Hhty3XxZgR-_sJcwihm7mo8qGlJ1b5NsPeHnC54t8-NmwhfkUI_aU3fVr5AbEaVnM3263gHHAfe7HSv7o5ZOuFoau1MQL0trCfGS7DrXUdpf1AGWEtKOLKI4PlIu0p4zmjx9WF2C9clwk-OQ19xSvkTWPLeQ7v1NAln1XPuayCIClGHIpktzU9FufDxcDAQK-S5nHP9S2M09j8Fm4t_wEVKqfV4YVfyHyBI_pM2iM-_p-_digbi5oeGReooUIdaXVL4k852d1QVJB5ZPlCrzW7VTHFgQAvm6c-SQHWEY6qACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=Qshv6I2HhMCAoE3sXQ6yczjm0g7pm5hMRbbTRe3f1Hhty3XxZgR-_sJcwihm7mo8qGlJ1b5NsPeHnC54t8-NmwhfkUI_aU3fVr5AbEaVnM3263gHHAfe7HSv7o5ZOuFoau1MQL0trCfGS7DrXUdpf1AGWEtKOLKI4PlIu0p4zmjx9WF2C9clwk-OQ19xSvkTWPLeQ7v1NAln1XPuayCIClGHIpktzU9FufDxcDAQK-S5nHP9S2M09j8Fm4t_wEVKqfV4YVfyHyBI_pM2iM-_p-_digbi5oeGReooUIdaXVL4k852d1QVJB5ZPlCrzW7VTHFgQAvm6c-SQHWEY6qACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=FXDqsXh_340Z3uLYHhZ-QK02N73zpOVzyURWU842BSwdbh5GLcfgafZv0JDiCd-b0ZjbWUD4flv-_XLBKk1VsSo4aalfpk51WmGHjK23mARUQ5BmvDh2tx1dNVmTFsYdlMbGDEXHas7B5RNwJpeJ3OqYPo9it-YoAtpGm9FE0keOapwS4t1Vvv5KMTrMHsJtwScZclPMrf1btP3IvQ3G-m1xtRoRDqdN-9p3gHJvowuKpYXbQ4gSwwGMKE62WyFtDPIqtxd-NrR1gQZtSq6Pjm5IeG1-cGsKV5ZGLhH33-l8AF6PdBYWgLu1qFE_XhtGT6XUZOtVD0VTEEcfUj6S0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=FXDqsXh_340Z3uLYHhZ-QK02N73zpOVzyURWU842BSwdbh5GLcfgafZv0JDiCd-b0ZjbWUD4flv-_XLBKk1VsSo4aalfpk51WmGHjK23mARUQ5BmvDh2tx1dNVmTFsYdlMbGDEXHas7B5RNwJpeJ3OqYPo9it-YoAtpGm9FE0keOapwS4t1Vvv5KMTrMHsJtwScZclPMrf1btP3IvQ3G-m1xtRoRDqdN-9p3gHJvowuKpYXbQ4gSwwGMKE62WyFtDPIqtxd-NrR1gQZtSq6Pjm5IeG1-cGsKV5ZGLhH33-l8AF6PdBYWgLu1qFE_XhtGT6XUZOtVD0VTEEcfUj6S0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=IPTNEOLdS-PeYzLSHakvuCgTDf0GequIsgZU5mtiQZVnfS27gMVd_GkSVuIl2gfjJJxt7WxoPabM-VWBQ6tzgGiZY7fjlyxYmiNsk9ThQs2N79YutW7-vjTF4HcOySKzB6CHQn4lr4v-FgVYPRX2Rqvgafov1Kg7T3OW4COVewH6dMmgjuk1kw8Mb1_D1PVzbqjh0YP1LnKSBMqk7gnjUIiixKXv9nMnFbFDhFwnCcohf7Cs8C6pBzzIX8Q22II2uD_EqLbsgbebeVlh4HVWbGh8PCXxWAMPYUYPnXCcEfYXWm1hZK7fj-aT4DfNR5YABg8NWApINdQYkPMB5xcS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=IPTNEOLdS-PeYzLSHakvuCgTDf0GequIsgZU5mtiQZVnfS27gMVd_GkSVuIl2gfjJJxt7WxoPabM-VWBQ6tzgGiZY7fjlyxYmiNsk9ThQs2N79YutW7-vjTF4HcOySKzB6CHQn4lr4v-FgVYPRX2Rqvgafov1Kg7T3OW4COVewH6dMmgjuk1kw8Mb1_D1PVzbqjh0YP1LnKSBMqk7gnjUIiixKXv9nMnFbFDhFwnCcohf7Cs8C6pBzzIX8Q22II2uD_EqLbsgbebeVlh4HVWbGh8PCXxWAMPYUYPnXCcEfYXWm1hZK7fj-aT4DfNR5YABg8NWApINdQYkPMB5xcS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=VGXzOz-BUdGtNdNam9VDmNtxbRcbhjK7mwrKqZxa6X9vNJu_SM_KrK90GEC-MOuwTMnoR3Dv7_8jCDigJDZ4HRd5Hu0BtuWDDQcDyxlr8sPB97bKjwdkixSh13Lr4RVO1-wAdNC327pW3aLYS7yzc--j_pI4gq1pBRhf3zqTomMqiD-RCQVM_vE5jlO8OizvfywReWueVr8UdAy6PDgR8VAoEpeTkX82zQjAhzRVE9kc4cHu1lJxY1dFwDtKeH4q5Tb9HcyuGIqSfqGjtIbuMzOoPlo_jzJdqolpKjaJbGuoR2iCZM06eXf5lVDi-vJi31ZN0KM8zL7jVwYBtNqkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=VGXzOz-BUdGtNdNam9VDmNtxbRcbhjK7mwrKqZxa6X9vNJu_SM_KrK90GEC-MOuwTMnoR3Dv7_8jCDigJDZ4HRd5Hu0BtuWDDQcDyxlr8sPB97bKjwdkixSh13Lr4RVO1-wAdNC327pW3aLYS7yzc--j_pI4gq1pBRhf3zqTomMqiD-RCQVM_vE5jlO8OizvfywReWueVr8UdAy6PDgR8VAoEpeTkX82zQjAhzRVE9kc4cHu1lJxY1dFwDtKeH4q5Tb9HcyuGIqSfqGjtIbuMzOoPlo_jzJdqolpKjaJbGuoR2iCZM06eXf5lVDi-vJi31ZN0KM8zL7jVwYBtNqkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=ElE5Io-uUXmiFbiC-EWQcjyLz0CkkTzmL8cPhDfCYcQuGLkfb4acutyecWO7MUWQn6LFSSwgKVq_DmNIeq1mD50c_mkRXgulDfO8GDvfft-28Rn2skfD97O8KULWsXqpFbrMekBX8NMrJuhndsOfyRL7oFFhgEWdoNK2Td_i18hV1D6IGeQoaLPGjl_vk_eIrjOtWNMHMjXbD0GBLExS4JIdEBa8dvNOds_nOP1X-ayd1z-XsvaTQpHXNdNrkhIcYjujnks7SViMMATzBOJj7i80oQ5CTK3k2laKfAlnJFCjCR58wBQ1HvAXh16hFVWEE8lp18sOL4kD35iDxqGNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=ElE5Io-uUXmiFbiC-EWQcjyLz0CkkTzmL8cPhDfCYcQuGLkfb4acutyecWO7MUWQn6LFSSwgKVq_DmNIeq1mD50c_mkRXgulDfO8GDvfft-28Rn2skfD97O8KULWsXqpFbrMekBX8NMrJuhndsOfyRL7oFFhgEWdoNK2Td_i18hV1D6IGeQoaLPGjl_vk_eIrjOtWNMHMjXbD0GBLExS4JIdEBa8dvNOds_nOP1X-ayd1z-XsvaTQpHXNdNrkhIcYjujnks7SViMMATzBOJj7i80oQ5CTK3k2laKfAlnJFCjCR58wBQ1HvAXh16hFVWEE8lp18sOL4kD35iDxqGNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIFvHK2XOLz8fMnwETd8Eo2U0XVHp3dKdDh6F1s9nj0zbHyhN9PEkwdO7f-_998NCYJ_DSQd739HzuLnSmwrdoxk3J36Qfy7sHTX5FuzPrGPikYaTwl-9obgc5S0Mmre2hGKGQcqCNR6Prsn3wJ2beb8ZgppWSQlwyQJ3xg_cgP6ouwCKzLtEruJXEy5JtwFPTbKx7fiFKuGF72WvycH5MjMm2orcvG6prJ0jHtgFdt0Q7BDkKIAWw2Gu3GqrkLPA2dG9eKvAOrGTQAmcCkMuhFxfvuQ60GvK0oCPNjOhKcZYVPDm2SZWUe6hdOniPxFGQciVgUr2SjPSK1FTADJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCtRCeT_1FVvc66Ew90yVQH05fC4XtF-pnLCFisUUaF2OdVt-RFCZxfgkCq4Uty6MG6BFu4c5AZkzo5nyhqX0G5tZyFGFnlvPad_MW74khWAbHu13ljfl9rA5c4PKnIYS-gzkTAlANeifWXn0vp80X0shC9Vlej-NhWVrZFpX5EV5xpLH8KMBghwsgKWjKuoIA5LmB60hUQyjEFgp2IwMtAxO8BeMvilIwra1b_pU7yOEE1Q6Fl3VaMs1H9y54sqKhFpSkNA4krPCgu9PnendLIWyiHZo1wo43cVLUNYCHG336Skdn20eVDVJOjGyfWSigKv5f27cO4FovRoP22lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=vYjMVWR6GhLdTZsnnvIGdM51-MJodDDVzdumtDWnNK2eLgwZ0d_r8UyNKo3FkY227R1kQ_gYXbuaWwjJUa5id-hZRNF43Qt_gGHnqkDOiMnwQ52jqi_P9-rLoIabenmhv4wNcU6GPUzN1D7vUTadvhM3oXPgLVAWF6sh0YDTNteDb5nwSxaH07eX1ZtTh9VZO0i2PGiW3EknUGCH9JEsgqomJmb_K3ALbC-IqHXDtR4eOwtUOBROx4cAFjogZ3tPPxMViK2-h7PbpKAe0MRTfEqdDJvJDq0W6YspIwAU_ue0oSOVmcpzVsIaaESUuPm6FHSfQoIYOcO4ItgB-BdrhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=vYjMVWR6GhLdTZsnnvIGdM51-MJodDDVzdumtDWnNK2eLgwZ0d_r8UyNKo3FkY227R1kQ_gYXbuaWwjJUa5id-hZRNF43Qt_gGHnqkDOiMnwQ52jqi_P9-rLoIabenmhv4wNcU6GPUzN1D7vUTadvhM3oXPgLVAWF6sh0YDTNteDb5nwSxaH07eX1ZtTh9VZO0i2PGiW3EknUGCH9JEsgqomJmb_K3ALbC-IqHXDtR4eOwtUOBROx4cAFjogZ3tPPxMViK2-h7PbpKAe0MRTfEqdDJvJDq0W6YspIwAU_ue0oSOVmcpzVsIaaESUuPm6FHSfQoIYOcO4ItgB-BdrhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCGFBxOWZiPbaqn8rqpHWVrJtGjTNSRgAl7D6UhEFWE46VVtb1S8DQJmrPPJO63Cb9lqontt7TcK8OSVcxbBeXUTPvaFlCXAR0NIGFWI_Nq_0gMR1Effmc-2fLh_xVuEaxP1Ja6IjldYf9iGhRXVX_xqF87vqajRSIkZyk1tKmFHK0SYDZoLenb6Cw8KbGWxa6gO2D36m_9F-RoBdO5jrnoiYpns3m0KLvDdaBoepDElssWKYRM-vrYUj3yaVzSG3vnauGjiejODlwOOeslWWMsQDQChjyk8DDo0jcROnRS7lwcJS1CjLNqmb5rggPFuXZHBWh_Ntm122Go2GYZHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYdcYEu2uLh_hUzybADzWBqXgsUnBqITgVR7Wqu3cDTxWP_0km5ZTfc2f3WkXf2EDAZlhDhC9Dq6OXnGMrfMlxzuzDiFMMOoZpkB4qiiCC14LAUkl7n2sW63x8EJ5uqVLkkLF0z05rJ4GkVO3nfcpCNEfHOVZW6taZ36l9Ocg9BqeSdLgC908AlI7jnp2CP9Cy3MYktklQClt38_Y0WXF4m_ZG5Q9D5RY2Iy74FjdWRj2jcSP1ldABfzS6GyPRRbd79nm4IzQMy-C5Ptg3mXvTvK4TVZQ6nE-xLzxe-capa-hBeYECX_1dxLJS0ahPcrWHjR42aDrhyKUtaH0M09UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpJze7kNIW01LW8BdL6QG4rAruXPKMkUX4fpgGRODMrNBdqXCFtQSlZ61KfKsJtNJVUH1BMlSuMsh5gu7K3xBgvgB8SfFsOiSE-5bDaC6btul4_ScxdcwneW7jxTunL72F81Z29MRO6f3N081oGDp3WpoPd68mQxpcACWDDwXqYOdIi7u2wrFKfDbDaStw0uyBcd1UJJcZzdLqTNHtWH2tu0bPGiCS99bQQ7Ke3AHVWfVv_slbfTPVtZg3Z1rNt2RB0TebBAlOyTYl9ZVuUFiiGmenJ6Bo1XcuMtx15iXnCbh8u7RSa-fKGXIJCWh4bXBH4lo1yVR92P124y2NbcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS4REd-_4u0AEMJjUvYR2YNKippa2K9-xDqgDwJWTt99X2VyYcg1OIIlaosbOddb7Yi256QZklysFjegyJKVYbob9OH2LRdyw7_NnbUwy_qgsFA_EH1h0Do8LtACTj9Jf1rRZQ2ofNf3M0WAWo_J7RfGruAKsCYFj-zk9Eq2drRrMOP7-rtYWWT31npBhlV5ITlNgZVIhDa3lnphxUQsRxDz-lepErpWRZeskd5KNJ1pRY8i9oVBObiwrCLpdoGrZQKGANHkwXdyvXar8tg72QTZORnY9sNu6mwArkond-WQzwmhAvyNV-VZ1wc3AnxfLBRqzxla4JeHeLvb_q4zQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107275" target="_blank">📅 01:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7yiToF426yMka_1oKj3IBAyoAYyqNuhpZ_yH4wMLb2FpAtjQUS3RsX-uWRIuXzNa9-LFDr-FyvItGfWy8CKaqBCHgE-_Uv7dMOqUAqvowcqPi_LZ-LgyiOx_4EmTa-Ig44505SJNfxFzXnXhn8mZLnEAXfQW0yelP3Rn2DdGLkVM20PMP61AEdxFPzxaBblN6-tCgzNf3T75xgpNQgMN0zbpNj9DKnk1wdr1bFjS77h4dS6P5sslAWiq26OqJhm3Wy4cUoE5u6Z6MrHqiRTubvhLlfsEjGCIYmd6GFSdUDrZtrbGE0DWmOuLBLENs6XwTvZrr-tVSBwOPdOurAdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• امباپه به 107 بازی ملی رسید و رکوردی را که قبلاً باتریک ویرا ثبت کرده بود، شکست.
• او هشتمین بازیکنی در تاریخ تیم ملی فرانسه است که بیشترین تعداد بازی را در این تیم داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107274" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0s9TTXZQBPIx-kpe3dZRuIks8oc9nF2oCn7aMbFoyYHIpEyfSR_TZDcQ5yumAMKMO167pcnw4n3Lk5SC33FvZBNhRBP9-Q1wDAq5xQJGzKseiliVRAlgcuDo88Ft9Lyrzl6FIx7pakTOoCVKMtpIieON7eOt9_AHE7TtgaEfF0lKuMVYvTQpGOPgWnWauhEImKSyLlJDr59I25kGMHvKj63Pi9eHducOQELIm-WkiIdHruChPbcjmyPTIWsQ6slREfr7buFsZL3d3VE8y1Vb7lvDl2fJfHDwfYLNfOQHg3kYgM18tsJ4E2BHtZeX2B1Dhye3LrEBfS9tUHai-RT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107273" target="_blank">📅 00:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js5YLb8t5ehHApwuLAwAJUCAhO3C0aKTqtiVMSZPyRHdHLbeZ61KK6zAphMv3giDdJP9wogGO2mJDR_uoyqcGByK3utBgdtg7G2f1R2xwXwbQNLoqmULOhc6muGuPNUiam_ZDRWeC7kNhLWDJDghXxd1iVXtIdxThF3tZ12hK7BNWxM-OCYiqgqW6DONCzBUcrUFplqa3_aNN5Y9nFOyUpygXHbP-3Lyw9nTDICg93ci80VXt6YET1UFUYDnIy1hjk_jfGzd1Gl3u998fFV-00dGe-uTL1TCGCRLVT3_8OETQUKveMt8IcalA18l-eSVSGoQ2MhjlVXKPki_mknCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107272" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=sEYI6Htfnq8-ycBr35JYJs9TPbvS76Tg63Z3vGuYbd_SJVqGGwaEnfO3OmpnK8gK6czZrLO4VEwivnilKbq7dWk_E7MTJBpCTnHpXKkpeU9V_msjiig-WGyvkFqSMQDy5rF8gs_125En9nWNY6sxblBEXqSZkjIgvuyAtA2DEtGktLrluaOAMErR1g6t5s7F0aTXT_fNiAqSyS8RafDQfOyy0-gamiCuPhgQnBTpgNtn_BGkRRxsWBmArSPQqm_IDhxLaNlJAcYY-hbn39pV35e9uRSjwgqhZsc2Gqne6yZltCq-0T6N_SlkMVzypQNwNxoflAG4dtd3E28tLTmrliOWI8MePGP4XFGzLZNu6wKB56lq2t4NDdqp7lL6b84JKpT-Fn6Y-AMFttSVehfk1z3Zj3EuJ6tcAG1VGOvke3mpDF5btt9B95lM4cTvGwWfYQFv1LI0JVvylByGEFL26s2L0MEHf22zvJDEubW60OqWzskMinPPMeoWKZKZL281Y_BsicrZDP8AgAMjI-xXvLSGlzyJqN-nHOK5-oV9gOqv1EUtCKYFxQ1wc7I9brFlVLf42zpCzTzlSqCE1y0cg3j6khc9jF1fLRKRLEvdBAbbxm0qh8baHW81-DilpghwCO3rk698eEvMV6mn1tkb2zl6zhvIwruLat1ZMRCWb3k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=sEYI6Htfnq8-ycBr35JYJs9TPbvS76Tg63Z3vGuYbd_SJVqGGwaEnfO3OmpnK8gK6czZrLO4VEwivnilKbq7dWk_E7MTJBpCTnHpXKkpeU9V_msjiig-WGyvkFqSMQDy5rF8gs_125En9nWNY6sxblBEXqSZkjIgvuyAtA2DEtGktLrluaOAMErR1g6t5s7F0aTXT_fNiAqSyS8RafDQfOyy0-gamiCuPhgQnBTpgNtn_BGkRRxsWBmArSPQqm_IDhxLaNlJAcYY-hbn39pV35e9uRSjwgqhZsc2Gqne6yZltCq-0T6N_SlkMVzypQNwNxoflAG4dtd3E28tLTmrliOWI8MePGP4XFGzLZNu6wKB56lq2t4NDdqp7lL6b84JKpT-Fn6Y-AMFttSVehfk1z3Zj3EuJ6tcAG1VGOvke3mpDF5btt9B95lM4cTvGwWfYQFv1LI0JVvylByGEFL26s2L0MEHf22zvJDEubW60OqWzskMinPPMeoWKZKZL281Y_BsicrZDP8AgAMjI-xXvLSGlzyJqN-nHOK5-oV9gOqv1EUtCKYFxQ1wc7I9brFlVLf42zpCzTzlSqCE1y0cg3j6khc9jF1fLRKRLEvdBAbbxm0qh8baHW81-DilpghwCO3rk698eEvMV6mn1tkb2zl6zhvIwruLat1ZMRCWb3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107271" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yRaUapT8TSDCRT11BoSmwysIwRInSdCFVOdELYuxHy_yki1ZVT__IKWrDMbk-S7tv8scRH5Y-wBKjaC6lb81oduLzJnY0emkZzDAkY34-uQ0ZFXDhtDf_yyPeQkaF-l2TUkLAbT-OhlqD1SlvCMwvycmUkQZUvFXxDdjcgJQNU50jXqic9qOlroJj_oc5sGQh_KpnATLikA1ssXgByJJqKg8llAQg83I43ijDyJeFcfw_Z8l3mm8qdpBlc0I0i-FuwASiA9ZvdLxwMl5TEN3eKYtL-C5wQHKHpwP9zgUZreJHdDBWofz-L0EC8ztPNVB9R8A7RoUIgI-RYm5EkIZ2b4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yRaUapT8TSDCRT11BoSmwysIwRInSdCFVOdELYuxHy_yki1ZVT__IKWrDMbk-S7tv8scRH5Y-wBKjaC6lb81oduLzJnY0emkZzDAkY34-uQ0ZFXDhtDf_yyPeQkaF-l2TUkLAbT-OhlqD1SlvCMwvycmUkQZUvFXxDdjcgJQNU50jXqic9qOlroJj_oc5sGQh_KpnATLikA1ssXgByJJqKg8llAQg83I43ijDyJeFcfw_Z8l3mm8qdpBlc0I0i-FuwASiA9ZvdLxwMl5TEN3eKYtL-C5wQHKHpwP9zgUZreJHdDBWofz-L0EC8ztPNVB9R8A7RoUIgI-RYm5EkIZ2b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107270" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107269" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=l67nW2Dg01Xd_M0NGocByNlCeG4ZKIiDL0hRNcCCdKCQr_4zJ12Pol5vuCZ0L9pwjetL9bDFq1xK0GewLk1htZzZzE6HMTuqVd3yM0ge0J884DwqpmyAWO8UexEukqCvk-FxUNAMD8TGDQLLEHwBnalon9HBvLRkX9Zo5PY7GWPCH9tds_sMGtAzy30AYak9ab2i112pQEalkgO7GL-d4bngk5XKSFkFAJTo5Wy_1lcoOP1zNBQsmq1CGWOar3XYBNIR2g8FcJYEVqLJw5SwgFym18DZbyM8_M22R3RNNh2MtBwRAF76x5yuAri6TnenbA7dFQQKl1Lbo6qYFiRpdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=l67nW2Dg01Xd_M0NGocByNlCeG4ZKIiDL0hRNcCCdKCQr_4zJ12Pol5vuCZ0L9pwjetL9bDFq1xK0GewLk1htZzZzE6HMTuqVd3yM0ge0J884DwqpmyAWO8UexEukqCvk-FxUNAMD8TGDQLLEHwBnalon9HBvLRkX9Zo5PY7GWPCH9tds_sMGtAzy30AYak9ab2i112pQEalkgO7GL-d4bngk5XKSFkFAJTo5Wy_1lcoOP1zNBQsmq1CGWOar3XYBNIR2g8FcJYEVqLJw5SwgFym18DZbyM8_M22R3RNNh2MtBwRAF76x5yuAri6TnenbA7dFQQKl1Lbo6qYFiRpdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک به ایتالیا توسط میکا گودتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107268" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایتالیا یکی از بلژیک خورد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107267" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFIVmOQHKuelhywZVEy9s1ngVYAv9IErCrydy8uqgkFBurvaAUXlxk-ytByrV-7s9P5W9HgGNWXpvXT7IYmGvGIK6zLedec7hVGK0-9z4TJrzvVax0MgTz1rOuyZ7SugjIprT8XX1ACn2e-8huJCWmacDFgczyCNKgI4G1A5gAL9mTPhSvUczZ0_G62ikHli8mGYD8mzaSl-mwJvuIX8TDxEMAT_HKQeOZvSurVc_8KjacmBKGW6zeznPGL4VTh65Te8_5qozwXWlkYOvCP5Xa-63j45acFF-buCKd1Y2rm7OqqWzLSyVbvjvyOVwOrG6IKMDQXeSz2uLJC9L0QJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107266" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLskBXiM5WE6KKZVchtLc1QBkbGg5yk-to_U_eQQP-VxUOCaWEkPh2o1KOTWYT-dmRYIhY_NGZ3GeY5nOt9V8XUrupL2pFepFHbTE0RQBX6c2fVzzsTmShmh8OUOJhjm1oZmmcCTHSyLttzCAHX6FNIzXCsS0dA67KGP3GFpIu2KnjsqMFGBp3DjFPjauMJ17yxq9A4Fi3zOxzyRQmA7wfHDu6uLGw4gZH5-kpiYIOSkvgdmXBbalfRFpFoMSh1mr9LJAuQkWIzdzsm6JoOmbxTv6cFA7CjfZP4dQHxG7wtQvTKdBYbBOAhfNGfEq5JUzOFHW1075em--wXvSdVF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایتالیا و بلژیک | لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107265" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31INZlyRQvdB1IDaxlSrJ2PtMuFYEc1Rg7_nVtLXyIE4g8PUt6ZIg3vQE0j7kBt1tYKO03K-znIO8ms9HSnT3dsTYsehKjPTFxTV7DPs2sUJ-AX0U-qHzPhR-U6vZ30GXejpCANibL5RYH0Fd5NzETEA4NkHjslE7A-jfGtvstPzQ1FXcsfF2ps-sP_Hd5zHYPo5GNFp1X2OzLK0Zh47LT10d-Btr69A5mugnE8osyxL1nn6QG9CHdRntDwtnwlpIR_g0soLVO7D35PYM032gGJkowlBLE4TQ_7zMirbH4_KpbbL7jsEUp9ugn9XTd5a5y9CeRCYOyTVUBQOQUDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه و ترکیه؛ لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107264" target="_blank">📅 21:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=ix__5zRCV4jfPG1OzhewGSHimjSM6EFw2HmbtODAr3O5LrfDpYKViUKGA10TF0mxdZnDI-3CwHPoAQoBbwg6JrTyBgoPS1l2Jtg-XNqVdUNyotQSqkifTSxCXtYJ4cno-QcTS3_bF9hQC4fm8EFJK3KsPh4yGjkjVmTF3S3Ozymj0zr0YvmnFuqZY4YJkO3GJ4uEL7IpxZl3E-pv6d4SyxipVu8SN-okCgJ02lMB1TCw-EPw2BUs3N_bZzhOa0EGvMQ75fXigTcjxtst7i7fGdFkyoOmy43p6tgFMCFkuvtRktXp0PWBWdHqXhOoUgHo5lA0OxGRIZA0pIkhNKC8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=ix__5zRCV4jfPG1OzhewGSHimjSM6EFw2HmbtODAr3O5LrfDpYKViUKGA10TF0mxdZnDI-3CwHPoAQoBbwg6JrTyBgoPS1l2Jtg-XNqVdUNyotQSqkifTSxCXtYJ4cno-QcTS3_bF9hQC4fm8EFJK3KsPh4yGjkjVmTF3S3Ozymj0zr0YvmnFuqZY4YJkO3GJ4uEL7IpxZl3E-pv6d4SyxipVu8SN-okCgJ02lMB1TCw-EPw2BUs3N_bZzhOa0EGvMQ75fXigTcjxtst7i7fGdFkyoOmy43p6tgFMCFkuvtRktXp0PWBWdHqXhOoUgHo5lA0OxGRIZA0pIkhNKC8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mTze_i9l2NERqAgOWT2LSFf_zYQQY9ZoeNtLlDLCUg-IP5yuo2dp6yjNslEjTg-1zNbXH3UnX4C_etjL15lLdTQzoPtNKSqIrbYnEdAJRzTlE_1pcPHEbC9f9I7vDN7Rwvi1rR0d5q4Nz1XvkobFGw1LwEmpQETlqX_4OZrjrb2ibFddLpT3OMLqSpbb5t_0OK_aCu16_8RvRh9JAWL-VUAXdwvNFt7JA1kN87utVvsSMywUH7zOLLAARD1nd1Ic2hBDm-qMg-x3oH6G5E2ZyLHp60GzlYLpFkvqP46nAFsgeVgF5M8-MI_7QxXimP1n9TiHvjTuyw4mzX9Yb0RE0o8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mTze_i9l2NERqAgOWT2LSFf_zYQQY9ZoeNtLlDLCUg-IP5yuo2dp6yjNslEjTg-1zNbXH3UnX4C_etjL15lLdTQzoPtNKSqIrbYnEdAJRzTlE_1pcPHEbC9f9I7vDN7Rwvi1rR0d5q4Nz1XvkobFGw1LwEmpQETlqX_4OZrjrb2ibFddLpT3OMLqSpbb5t_0OK_aCu16_8RvRh9JAWL-VUAXdwvNFt7JA1kN87utVvsSMywUH7zOLLAARD1nd1Ic2hBDm-qMg-x3oH6G5E2ZyLHp60GzlYLpFkvqP46nAFsgeVgF5M8-MI_7QxXimP1n9TiHvjTuyw4mzX9Yb0RE0o8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=IRvzNzgfUSv-9qEdV9rCVMXKA_xANc6ENeW94kOsJpAuFRTkaeOs43NhoQGdtgsGDYygeki8JRWG-FnYu9OT-AjCXsp_fqO3dJhZU3mNA43eXDDv0HgeLVFqwT_uHplvuKz_IXiC6G6JxYihBPozWVs7JSMpBAoVY21NFCGNRTXzvDMqivDT6I-z4KWqPMAEyojq9T7SuEOJ7F6ZmE8fhXoM5iJgjDej_TT-FFvYVcX2y2JUovDEu4B5VfQBysw3rdTaI_AuBbMYInmG1Qp4V3v9ijtHvDcfdDwJSNatZPp1-oPjMKIHzZnA41zJpnZaO5DLi_1wJg8zuM95tl7ggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=IRvzNzgfUSv-9qEdV9rCVMXKA_xANc6ENeW94kOsJpAuFRTkaeOs43NhoQGdtgsGDYygeki8JRWG-FnYu9OT-AjCXsp_fqO3dJhZU3mNA43eXDDv0HgeLVFqwT_uHplvuKz_IXiC6G6JxYihBPozWVs7JSMpBAoVY21NFCGNRTXzvDMqivDT6I-z4KWqPMAEyojq9T7SuEOJ7F6ZmE8fhXoM5iJgjDej_TT-FFvYVcX2y2JUovDEu4B5VfQBysw3rdTaI_AuBbMYInmG1Qp4V3v9ijtHvDcfdDwJSNatZPp1-oPjMKIHzZnA41zJpnZaO5DLi_1wJg8zuM95tl7ggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=IvoMgC1sS7k5g5avBE2K4Rfs04nOgWvSqLRN3M9BI8ZUKqIkH_frsP6VeJ_Z9s3Sf8eJgM74dTCU_oQZFeA77qbK5rUwdoFPFuzbXff7dMBaIzeduh2-DtFyZJ1J-7Xq2SGkk4t-b-JV4_L-r5H7D7MbwHkGSiWtna29k2_qNKlIHxAHHhinYncX099afH7jU1msMukBquLwWBaL-_YX77xPVrD5Vfjlvkja_DALMkggkdJSRantL0NhXaFPmH-CTbn_o5IM_wHQwQV1lN-JQsu7oqTl9CFGPwzn833T1B0it_UyF1DgQidIuL2g-kxgbAJsExfu1qo_OEA58I1yww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=IvoMgC1sS7k5g5avBE2K4Rfs04nOgWvSqLRN3M9BI8ZUKqIkH_frsP6VeJ_Z9s3Sf8eJgM74dTCU_oQZFeA77qbK5rUwdoFPFuzbXff7dMBaIzeduh2-DtFyZJ1J-7Xq2SGkk4t-b-JV4_L-r5H7D7MbwHkGSiWtna29k2_qNKlIHxAHHhinYncX099afH7jU1msMukBquLwWBaL-_YX77xPVrD5Vfjlvkja_DALMkggkdJSRantL0NhXaFPmH-CTbn_o5IM_wHQwQV1lN-JQsu7oqTl9CFGPwzn833T1B0it_UyF1DgQidIuL2g-kxgbAJsExfu1qo_OEA58I1yww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=YQp8hnAkJggQBiZnKcEZtgiynAB2vTEBfP05g4hpdaIG-KrAjo36xuQtJkGDFdyCGEHaiNLcoVmoPgBB6-c4kEFbRAtBELX2X-nn0_G6SN2NgbP3ezmy5qqeVL2fPfiUfG-wBnvwXxPOYK9os-nTuN3wPrQQDXAkCCINjT9hj4lPIFk6GwZEAd6ykFyjif0JhDxPAQgT_R_ieQIyhF5FSpLwNRYVeAMu4HbhVazq3mPQSvi9WM2vM5LQzqyJFzT2Z2fISEnu7YBmjlZQCgvY9bKuiWbV1SDUEA1sFA-LNc4LsQuGOw1y5yPt1YR5dZAxxlf-nGZ2BUMtsSZfD4hi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=YQp8hnAkJggQBiZnKcEZtgiynAB2vTEBfP05g4hpdaIG-KrAjo36xuQtJkGDFdyCGEHaiNLcoVmoPgBB6-c4kEFbRAtBELX2X-nn0_G6SN2NgbP3ezmy5qqeVL2fPfiUfG-wBnvwXxPOYK9os-nTuN3wPrQQDXAkCCINjT9hj4lPIFk6GwZEAd6ykFyjif0JhDxPAQgT_R_ieQIyhF5FSpLwNRYVeAMu4HbhVazq3mPQSvi9WM2vM5LQzqyJFzT2Z2fISEnu7YBmjlZQCgvY9bKuiWbV1SDUEA1sFA-LNc4LsQuGOw1y5yPt1YR5dZAxxlf-nGZ2BUMtsSZfD4hi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU9mwfd59JsO86zLfN3GOGv_EHynyudIHkCEvCaMTc4cC6zZJ7-u7x0045PpxZ4PNCVUYrQOV6bapKJu-oCRfE-UXt-nAzFINsLnkPRlekXGs_VUx8LF425ZyKZeIlQgV9cgludPSYQpTJNlrtTlUpb-pYEcluWd2erLrWxNIsQSvgHSjELPsd4IaWB7pDnx_Ic08SWlpl3kcmeDX8JA2H7ykWVxCgZGw96l2QsW9mmFir4cRAT-3JQPK2iWotE6BEvcpUeLxDAOlR0ZnyrAYVkCNMpwkTkbIuFuTec-TY7ymsBB0-ryZGZV3NHTWaJCW7jWmZ_jivBKR1n8CJm9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=Q_IVO6n1PpLVQUJqiWlQ2lMMFVAcvKCXUPWU_NTb7gRPp9RmF7_Lw8-upZQceIB24OdDOLK28GBJVz16gtPz56na8P_vg9JLU8GZG--_BV5tnRZaZbdYd1LWUxxhGlcewwVfbcvzW0JrNmsF3_5PIIBifjp30ewQLPdrPv1vGYcMP0Ea7kWldzY9akGC0zaLsPMcNpcJ-nAswIE9KoyyZ7noHXLkdkdaNSzKu_F9OETslE0NTKmsMGXsvP5m2qdQ8XGGH2Ze8p5mNB5jpDXNd740AG9yMCmZZ-ZgACyIyMG3TcMlnPdNsbRwfQBySBQJacgNRbilDBf3ogK-LJVcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=Q_IVO6n1PpLVQUJqiWlQ2lMMFVAcvKCXUPWU_NTb7gRPp9RmF7_Lw8-upZQceIB24OdDOLK28GBJVz16gtPz56na8P_vg9JLU8GZG--_BV5tnRZaZbdYd1LWUxxhGlcewwVfbcvzW0JrNmsF3_5PIIBifjp30ewQLPdrPv1vGYcMP0Ea7kWldzY9akGC0zaLsPMcNpcJ-nAswIE9KoyyZ7noHXLkdkdaNSzKu_F9OETslE0NTKmsMGXsvP5m2qdQ8XGGH2Ze8p5mNB5jpDXNd740AG9yMCmZZ-ZgACyIyMG3TcMlnPdNsbRwfQBySBQJacgNRbilDBf3ogK-LJVcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUWKwNrGjzy01Y9WfqnTtW4g6Lvuz88h3BUw3yOfOCJrHmXdZZN-3pYHQ8nWNPgRiJX3M0txEVLocVDJtoeU-SiJqTgfu6eQSlvJR7xo_h_QiQlPNGdTq8pE7GR0ihtsRAQi6xXh0kIt3n-ra-wvrGuEIrpGz4XOFqR4rQW4T-Vi-nNxmFjjBqOWw8qtg3zBHfPkbScJXjEyFc-x02y38KrUEUWHDCbkXv0zkMXLlaPpeyD33UXV1RFfK3zxrob35OJsb0ZzhXF8YOD3Mu1t_77W_3PP4TZfBDSH5I_JunqQ4_zDBQDYIWprTsHrifavcTVq1PqIyzdL9Lvh--fZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfHOsZd96uWllecVvBeKnpmGoWLZVZVwGKP5iizEi4GW24XBUqzGrbiXEjM9zeARND0dmI0wHcu-R26Wjy_31hwe2uRsVEPvVi63MVEFYkC3Tvl582CoeOv3VNgK93P7XHG46kim2YUDvT1hPrkia42asO_k5NCI3TG5earduRyROrd-1M9wr7hS2NJy3W_OPh8NVRGM2OdBwhYL1x-N5SOl9wnOani1lLGyD3ksmdbQMjpEB16Gg82W7dnch9s-xqpA7OfZhQ9PSWY_X0NimVdVF5BFXhe-iFOuz0M_I9KTtm6Yzebnm-25pHwZc-iPvl_TE4X5jOzsI-OaNK8YOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

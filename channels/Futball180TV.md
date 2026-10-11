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
<img src="https://cdn5.telesco.pe/file/pDL0E12lylfR7sm5ETUI21Ip7F8QQKI51pFHdy_ibHNW578jEdUeyJM-eKHGqnJZUo3yn__hSIR1lXA9BMTVBnZAOGR_Y2Sx-3waRg3SMzm9bysaC0QiBq3u8uO5RqpUmW-NJVc1nOTmFm35fnojqYuueAHE7laFLbuhguPkZxpYKjeDfWAb8XebhC3XyFc2wNOtt8IKqtIIfumhZXnOquL8bxW1Ys687WkKEKbA-G4jaQQrC9rXQPyYddnKIqQEfIhrTpBkik3vRS-cCDplYxPkwmvKscbkzkQrNlwY4rFEvI41h8TN4_EnwxyeFG7kDKI_TdEHLFAtIcA3l4jtfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 385K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-108374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/Futball180TV/108374" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjRcbMdyqJfub4MHPGk6V7YO2rmcK8uHEFRZmeJ8IgK2mv_fzjL8sZOPG-IqsGP8XgDhhXGS-me4DjKf9JoOLd1Di7WoCABlaegYY1HxV7M1exWjj2JqE_pUG0yKeNDapgrxPURnOA_-EQt_-i3KOAbGe1tdOdfGRlmRBgrmw61FuKNKwebnpeTyGIIGbLbZjKgq6KKoSCp_yElUNehfq5ohi2GjcLfzpjX8SONTzxuNBx-S2HNV5El5CY-mOlxASHaBoWEHjHyVhKLmdS8qh3jIsy9g4Npetb3PvV20jZ5uB9Z-C6YSgYJ8SnsUU6LzZ5mvotC48jFmZnzfroO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/Futball180TV/108373" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/Futball180TV/108372" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108371">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Anfm-1TNnVIDxp686e6gWqFWHZZB-s2GJNqqIF3--WxDPr79O1EXuwEvzy0wPuRVXZwVKrbEah0Y0XzfVOyTAkt4x8lP2FoEcFEXw-woZwxfqamoBfKs9rzLkK3Xlb851zuO_jAaIl5HUEsrnuFQqw0NPGjmdXMM1iGEWH5O73R3YsheE2Yry8VWC5JrqnHKFnOMOBh1O6wrziXms8ubsk82RTyzTWRI6dhYK8fpbNYOEwmHbdpRsSIpiE1pRbtm-cDH1hEd7FI1fAEul0okQicdOgB-g0oxkqgS6t7KeSh-zydW0fFrB9ZC5j5ApSi59j-iYrZjyAHfz4XWHurvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇮🇷
📱
استوری یاسر آسانی خطاب به حبیب فرعباسی: داداش رقیبت برات پیدا شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/Futball180TV/108371" target="_blank">📅 01:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-ocOfQ66c07G13d9RyE_w4OWlVA5qbW6LIA50Oi1yOpvalE5GxmXSYoG2lYwji5oI0FJHjXoQc-4b4l0a8RS_GNQfBkIbkYWYBxq8DMMv9m1JpNiZYZskuWHtVSOi9wXXVKUfSBIszgqvR-PXpMQydje47WHPrK2J_10zrgtkxdyzGgyXIQURven17emLB7i4QBMzBYSoHHqm_uUWnqnJc_1TUAtvSpXjwmI2VgcI_y1koZRJXxF6XCHVac8OtBEcBu2h8JFCKVnbJuwYOeR53gepfzIsrll_BsI3i4Ih-z1FkLbFjFIgtzlmJKSESV-nOchqxBGtYbDlB3SIAa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
حجت‌کریمی مدیرعامل تراکتور
: زنوزی با وقت و پولی که برای بیرانوند گذاشت میتونست ۱۰ تا کارخونه جدید بزنه ولی یه آدم بیشعور فکر میکنه همه‌چیز پوله و اینجوری تیم رو به حاشیه میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/108370" target="_blank">📅 00:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjQpMty_Pqg9M3jg-8Kk4pbYcGME62VE2aIzR9V9J2A-MD9Tk9ijPxQ9K_sl8XOnLXYTqwYI7Yq0shhTURuPi8aBu1RzHDl58rbdyk6t7Soga3_fINZc2TAn7-fpwQqwRnSGYD2f2s4WTDBRSvYlfsJgSdk2miFNDECC2ryeIDWNZcDPZdIrOpXsl9RTzNbDfOgajrIAWiWVDbHh8yuLUB4j1EXcnL-X-EkP1tdlP8r1O3SrVdgKDV0hxxa0X6hiUKfEnt_b6ckaLok5Fnx4R5cAkJuH6RtustKRhGEhFA7RgsiyfnbpbQYw6Dqlbm3YvtWmkUO-paIgoSx6nMOFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری از یاسر‌آسانی در تمرین امشب استقلال پیش از بازی با الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/Futball180TV/108369" target="_blank">📅 00:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
⚠️
لحظه اصابت موشک حوثی‌های یمن به ترمینال شماره ۳ فرودگاه ملک خالد ریاض که روز گذشته موجب کشته شدن ۱۳ نفر و زخمی شدن بیش از ۳۰۰ نفر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/108368" target="_blank">📅 00:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108367" target="_blank">📅 23:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108366" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNpbtvCYktoSY9EZUxP3aIxXObBczPlGT14-IZlftZupYBAW_jPSdqH36txfoimnfq3VTdhlWzUMBMF8JN_R0UtM0p-iVzrsR1wlNR5B2GS49vA2YaMd0efZw6zoagV1hg1K014Q02e2CI-WzlBkkCdvLeXQT2ZW076WxUi9Z3Xd8zF_2FtzlaE9TJEv3FYvCNwApKNIsFFvaUzbyBuGBWUL4xcEZdq12G9T-HkDSSPpLyiV97CMSL-wJzgWXXcv5lnXEDPBr9hbjJuIiLLbnrDbLbe3fmVGsKa7PnRWDFz6-mxhydVMy67lXDt5k1cEky5FGfoJwhhIkA9Eaaqp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108365" target="_blank">📅 22:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goliqZEgSZqPb3SYZtHaSuoQpeiOj6H2Dz_jLF0-oAE0JO3QNUzkOdacQpkc9Gp4qtQ90vx6gTbYhzHyM69WO_vmZ515QOAn1KbqRgC09QpxgPTYru0lMsqYm2nzyhBKDIZ-abzGb4VPjp4ieDhyI4ILVQa81cCDRrL9_-czc7XTBp1GxQIWv86OyzJIjyisazHKm44T8Rgk2pGJVf4QhPjfTQSRWKs3nX5ZfJEwUBtZpqdu73QxtTtB6G49GtHpmxPF7tZaJc6qd_FrPZ145t_A2en8ronMYhC5ogAQtP1dCJANEmLVg56aTtXN0cYLBADFlNsIgpZxqzKjV60DhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇪🇸
🇹🇷
ترکیب بارسا اخرین بار جلو گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108364" target="_blank">📅 22:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqdayfDZRD4eFx6KR-ienHeAej0FnyYblC6dwLiBeNxjmexoBSkwAB0AdoPZHj9fh1zziqYfQrYw-QXXvkeYct0C-Oi71ApiQ7e7Ntp-Y15joIqPO-cyMkQ9ReeTtED8BSYjXHngHbr7Su9mSxNvOum-XZnPnkLzkj8nRfIXhy8wS1kxnLY7gBo7CUCWUax0FmJOOY8udmCM7YBrwdOzeWdHwR32o_qdI9lVjx9v3gvmFFLSQ90Ga6C6nrXt5mWxX5pVL6wZjaUPPJyFay9WeOoN3tIwc5E0gp1A7IxW7WobVU8ftlDScjihXGTn1v-vU4epYog9zAPlUrRjxlgTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
جدول لالیگا بعد برد امشب بتیس و سقوط رئال‌مادرید به جایگاه چهارم جدول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108363" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=J8WNcD9Riqt6Qv5FDdmsjzP53PaSZLd5fo9ZzuRvNGL10yzs3X1eDUsUVu49lFQ1g9o7442SuBbboGuVMpVp8wEnVj-rZ4AZeJFFKKUtdp8pPeQSjdczTtAK3y3lN0LC9D13rgibI9NAyYH6cM0uCxSY_4Yt1Q21Q4mWM5hojNKoeLLC37WUIH0wVTRH5r9qOthKWSkBEx7nwRmZDsrY5twD0lo0maiLY9OiEf61JUjnZLJgJ33G6orbRJPEQRvJj_GCRWZHXlZGxyj-d65LbPaUtqWOlKq3nbl-seTwTj2YbOmXGrSZNDQhIkC9BhidY_v0Pt7n-ycjKgv1of_iPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=J8WNcD9Riqt6Qv5FDdmsjzP53PaSZLd5fo9ZzuRvNGL10yzs3X1eDUsUVu49lFQ1g9o7442SuBbboGuVMpVp8wEnVj-rZ4AZeJFFKKUtdp8pPeQSjdczTtAK3y3lN0LC9D13rgibI9NAyYH6cM0uCxSY_4Yt1Q21Q4mWM5hojNKoeLLC37WUIH0wVTRH5r9qOthKWSkBEx7nwRmZDsrY5twD0lo0maiLY9OiEf61JUjnZLJgJ33G6orbRJPEQRvJj_GCRWZHXlZGxyj-d65LbPaUtqWOlKq3nbl-seTwTj2YbOmXGrSZNDQhIkC9BhidY_v0Pt7n-ycjKgv1of_iPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
یک پیجی تو اینستا هست کلا یارو با یک بیلبیلک میزنه به مانیتور و نسبت به دروازه‌خالی خراب کردن بازیکنا عکس العمل نشون میده..یک کلامم حرف نمیزنه..انقدرم بامزه انجام میده که میترکی‌ از خنده..خیلی هنرمنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108362" target="_blank">📅 21:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJZZkm0wy2aiEKTj44heyXqmh0t9_zy30OZal7wiBHBnHAu-9GKkPcbnD7J3D2wElNdrQ27LgGP8dIXf2Jx-XQkC44s5Q0tD7BjFEFq3VTbg0xzoPHNBn_O1qc8mGtTFQDuEmFlwJlnTnUy9vNIJwSniliHRmed9tgzqeO1Im1bVrRlA6VzW6ok8sEf8-ztz8TkD9d9JJxnkuqIhxBeRUykv2dOKtbrf_1CkUASOZC6M0s-PO6JW6BU-k9mvYzET-p_piIY49WWPnN3Y4qcJ4o47B_eUHQqfaFGTOg-sKNMrhKq2PzgZS4_AmQNJ5B_Ssd7kEdv1JkydkTpYw-8Z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108361" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108360" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دوم منچسترسیتی به لیورپول توسط دوکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108359" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108358">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به لیورپول توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108358" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108357">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
دیشب بیچاره شزنی سرش محکم به سقف نیمکت بارسا خورد که همه از خنده پاره شدن. فقط واکنش لاپورتا رو ببینید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108357" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108356">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد ربیعی: سرمربی تیم ملی امید نمیشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108356" target="_blank">📅 19:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108355">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رختکن شیاطین‌سرخ بعد بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108355" target="_blank">📅 19:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108354">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بارسا با 9 برد از 9 بازی به دیدار مقابل گالاتاسرای رسید.
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108354" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
ترویج گل‌زدن در صداوسیما و مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108353" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3e_Msi5Bm40-HPxfabZu-mL3_20qvLvMwxEugcMwm1h7lnt3jSQC_cKeQBVOfDAXCNITvKWbrchw__4Ho2pj6gS3YNtrNLmAVO-Yvy9pYCoy2KX02yRDQCvBMa4gcSxd9YB47Lxf2yVb-2niF4NoUNOyxlBg9qDleUTYu9HUd3YdYW-Lloz7YTyzBylNurQEcjz1SpIGrRKa9tJNIevprAxSeLKOoBZDByCyxnk7qubik2y7RNWQPmtovyXmu_oMrSdIRFJrvPi1UY1q3yhrujnLTW58bjuzPcnmdBetgQLFDJ2pQDcAzorBTok1f-QM0vOMyYAtLP7lGIVSkpPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلارنس‌سیدورف از شاهکارهای مدیریتی تاجرنیا که به مدت چند ماه بدون هیچ کاری چند میلیون یورو از استقلال دریافت کرد و از ایران رفت، سرمربی کورنتیانس برزیل شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108352" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlwnbDRXonE5ZX09_Nqx0f6ON9I4aa6hkpqitkfU6XRJQw9_uW3LkRC3YwUf1G2-UcZ2USeNixFG2tS2lPFoUwDblKEhOBN7CMZuwYs7G1znJ5myhsXD4FIXg7h9S4BkwKWhxQrYEkW8rng9RmYJnQfDkfzs8SsRpZ5MQS_f6pKDSv1Sr4x78BEFAov64M3T7g9p5CYF2A0bhW7bcxnrwMp7Q6ZcN5A9xPDiKVblVSgfxrR2KL__7euhpLVuzyX5R_8X7Oh_2MYDmwcz_P2rt0J_R1heKnsaV4cTkOSu2tXpfl8nXvWgi_Zd18PqaefMksZl2-e5QUw0YTVzqyiczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXXqeraMtM9uUrNWdk2cyKgGLnsYnpYCzez4aQr1u8W3SFfcU9R-ZLawbrlxD8zFM2slMQXRbBtRzJRpsHvyYW-Ve7GWuQTl6ME_U0udwiHIlH8-tSwZOMDOXZ1cWZKv2vZIO0EzTZ8xXVeNLC1mfYcm6FmJbrtN5bpJXYInGkeGuuSsmtEqAaZ5KlIsM2xloDctKBX2Dj8NqmZVZXR-5N3b_kpkjbuVaHVve-6tSCUejwSXstnSSPqpTAVNxofGHeFbxeXaALalP-dRMP624Y4Lqjbmixse4qHY8TvuLuyxsZC1-zAvgF4lkYBoHQmlAQfAGQ9Qn0jnngHiT63j2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچسترسیتی و لیورپول
⌛
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108350" target="_blank">📅 18:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR05krKe9fnZg14jAeY9ZVr3AjNI1Ni3hoB7uD8Gtld4C-mCAkH6EzXkDb8Uc2etYp3QyDRqRA-GJ_aAAbVfevULmetKwIBMDUiOdY1f1eRT1xtiM1Ne8EB2TanwgPWBRBAd9Qo6krVILcr2l1wOGpGDHxiEhzg-s2gXOiRqbmEwoylqpMRJc6XRYmQb_N0hkqDTQnxTRtzlNHAJfE8zxOMBcIWoD20TPu5UUz1-L6OXq6oPWDJzivgX_1zC8fdftoaLi2j8vCvnT8bdE75RM2bM1jZ4xAtmP9_lSZDnOpmmDlPtPs-nf_sk73ab9JFCrXVL17iLnBIPxLDZ1fR2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیر سفر گل‌گهر از سیرجان تا بحرین را مشاهده می‌کنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108349" target="_blank">📅 17:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب خیلی جدی ادای آخوندارو درآورد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108348" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108347" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108347" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbruxj_aqXRY21nP26LabQJpDIzPemaKsEd-srEga6s8m2t4Tqe-TXGKSo78lP6hoeroENn2XgTKgk2TeN4ch8VIKNDmB8lg7TNzG-3T0nkBV1y1gTkM1TNR5jYntJNpJT37JEKNMLxFzCM2tF4S6-SHLdXYxBsgRV8yUH6Z8neU_VwC6YTPcUxnv4MkwxrQVQ15HmJu6JMnMliwWbncdInZWT5UAOGRhWwO9ujlxEKrMTNY0gRjj0r3RKOYetQ8OlRdxKSDeTxV_bRwug2cjlCbO-8RxTA3ug-bWdWclQNOngmPvLxfPYnJOGpUOTgEv_AOyP5DSN8MBMp1rwKxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108346" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس سمی عروسی گرفتن مسعود شصتچی در قسمت جدید مرد سه‌هزارچهره
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108345" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842c49b387.mp4?token=OPe4zHifpkRCeEIog3meHoyi_QoZDdn3CB_bu7GQa-W1dGgh7_jFLQhWY3uKNdCNWATleIG5L8vk5WghcP3ouz2GPXadFM6nVzbFD8YjtuFUapg6bgQhZIXkv9fhOTsxzMsRQG1zn5MLF4WpT0PxLPZVsGPmxgU0qiJTqgVr8g-_pFJ-brNjmOwg19HSp4IwAUUqNwk8PwOQ9a4IQdMI7BpbpDi0aY6slwpImgLclDQm6_EvwqxSqMhZekO362Ski9MkYFs8eaZjHmXlGJyep4101DY2lnWI_qOXnNAv_W9YbNwKxhcgJSJwLy5cXOmeXFf7kc4o76WZ8_cQzjkEyzkCEi49LvBlO1-wEHgP4lbJxFlZu353QLAP9ZGizRG3b8stNojlLZbF5fzdGYU1-09x7lBoZXRbgQUsLeneDXzsKDTo9uWZU598wCqHoVurPATGkjPnVpUYzYLINL5DRIPrBeUa3LIYu2pQ9lzm6gzfl_taMs_RbxVvqS22ossMLUU_zqtCbX6Vng_z4vNh8qb2keW0IlcZCZZyYKQT3JO7Kk2_Ma11zsBG0olWRW7AZRMn_4GfryRo9u4nLwTT-sf8_CPbirRn4uvcl3NIHdLOhhX-j7TVJ5qcS5xAFDkzT5tFlQckM3g2GNulZbZ-cszThpi2X6UTI4IsLDPcIcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842c49b387.mp4?token=OPe4zHifpkRCeEIog3meHoyi_QoZDdn3CB_bu7GQa-W1dGgh7_jFLQhWY3uKNdCNWATleIG5L8vk5WghcP3ouz2GPXadFM6nVzbFD8YjtuFUapg6bgQhZIXkv9fhOTsxzMsRQG1zn5MLF4WpT0PxLPZVsGPmxgU0qiJTqgVr8g-_pFJ-brNjmOwg19HSp4IwAUUqNwk8PwOQ9a4IQdMI7BpbpDi0aY6slwpImgLclDQm6_EvwqxSqMhZekO362Ski9MkYFs8eaZjHmXlGJyep4101DY2lnWI_qOXnNAv_W9YbNwKxhcgJSJwLy5cXOmeXFf7kc4o76WZ8_cQzjkEyzkCEi49LvBlO1-wEHgP4lbJxFlZu353QLAP9ZGizRG3b8stNojlLZbF5fzdGYU1-09x7lBoZXRbgQUsLeneDXzsKDTo9uWZU598wCqHoVurPATGkjPnVpUYzYLINL5DRIPrBeUa3LIYu2pQ9lzm6gzfl_taMs_RbxVvqS22ossMLUU_zqtCbX6Vng_z4vNh8qb2keW0IlcZCZZyYKQT3JO7Kk2_Ma11zsBG0olWRW7AZRMn_4GfryRo9u4nLwTT-sf8_CPbirRn4uvcl3NIHdLOhhX-j7TVJ5qcS5xAFDkzT5tFlQckM3g2GNulZbZ-cszThpi2X6UTI4IsLDPcIcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
رونالدو این‌روزها کلا اعصاب و حوصله نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108344" target="_blank">📅 16:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgEgZc9n8X7VkLFgy73x-JlbwYGE6JbKtQLSFrBxR3xH4WO-0Ct87XBDEeTr21fN4dy9-MJfx8mgWvnk8ENgFGK65TbnYBE29jrXaMfC6Usrh7MuhBFcT0WRTlea-4C1Sgvxcoo0E7ZUGbfKyTN_OQGwcCPr_S2ldiyEDSTqQIVJ5Eb2tDWTRLwEDzzf8cJsvOnWMwjDeuDC5G8-NdikL_SMZnjfyQeIRvqUChYGFTVpi5ZBLimA2MdfQ_o_OriCH3RWPY91j7L1zDBErZpwq0eXi6S5-umbvGDluSGShz803taUuwqCNQRMuSzMOsBLhywUQeJdKF5or9DqcvjIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
با اصرار یاسر‌آسانی، پزشکان استقلال تا ساعاتی‌دیگر تست پزشکی از این بازیکن خواهد گرفت و در صورت بهبود نسبی امکان حضور کوتاه مدت مقابل الغرافه وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108343" target="_blank">📅 15:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkhgCnF8dnpnyOc6lDgrvEtNy4Kpcj0q6acG0SdHPQgSmdpV-J0rtafZaMWNXBy2slX7cRzyR50cQcMnH2EWPRs4Vo2gfvEvaSika2DGxBDdGetq2mmr9Q_a5phPOfFiz9QXJi-hmhgKLURonxejKcRCzxqAY6HFEcYYZBMRKUiThQ0TDK5-fkc1rzZ2iNLR70N2VSzU7M_7k3BoaGyz0CHrpua41QFXU-kymENRNTRjY4uKY4oKUpra6zXH9RY4SfZjpYJYVVWseZJi4UO6eWljMZYtqVehOLty78bYsHb6dBnJLxXePNVkMWP6yCnQxbBQKh7EI6zs4VtfAHYyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108342" target="_blank">📅 15:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT2VNlNg-pK1c34UjdRZ44dtifmKKy2hKnccHE2a7EtBwPLkdXJs6OizjEo5UBOcwFAzRfQ1n3zZML9rnnLSZCUQjnMYUpQR7ophxj_yNFCrj_LaTA_UBQ8P02-JAR1-DN_xBYI6jrhtwz-Cb2Ba2s3Bfzu5jYEtQWEnF6ye8PZZwjmVcvTHQivLisMVpTD1TGmF3p6Ift2PsUjZKq7MzkgKHW6duuQHL-v4GR06CerSYF4gOec-c5CObystHmqqF970M57KfgiPahm4fmNLv0Upv8l4xJlGmAvDxbF6RED6bktDqHCbqYQ1V9Udtvm_W6aZjlkaoHyiEFnG9_kbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آمار تقابل‌های رو در رو لیورپول و منچستر سیتی در طول تاریخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
110 برد لیورپول
🤝
58 مساوی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108341" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش مهدی توتونچی به مصاحبه علیرضا بیرانوند پس از بازی با استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108340" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه‌سنگین ابوطالب‌حسینی به ژوله
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108339" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
واکنش گلزار به ساخت کلیپ‌های هوش مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108338" target="_blank">📅 13:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbt-7Qyswj2KuE_Ht8w7X9pXVecBL4RX4UPM2MzK4H-usJODevYJaUTOuZI03GiAPFp8TNepQI26LBeybe3IYB4HJ2MQNlc1s-UqWYPbkOlHg7Aeys_klwnhcrEOjkQQzmfnR65bd1EzmVZfR_g0C_sWo-zLYSWtgjUXGunZ8NF_8m_TOFGBSTKLC3oItjzRYHqE2LX0TjiELdspGWn4msqFwPnz7FWd8V5JwSRbFo7rZr66FppH6rODyz70HwQ-GxVsjY_ko_icWKzMS92_cJFhJcBkG3jMv-8CYboSsc8eV5aj-t3GDvWSupnB3vX93ye58nRQOm1hso6HmSdrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر باشگاه استقلال ایران برای بازی الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108337" target="_blank">📅 13:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تذکر تند رضا گلزار به قیاسی درباره ایرج طهماسب؛ گلزار با تاکید بر جایگاه طهماسب به‌عنوان یکی از چهره‌های باسابقه و پیشکسوت سینما، از نحوه صحبت قیاسی درباره او انتقاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108336" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینی داشت به فوتبال برمیگشت که ناگهان ...
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108335" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOrOvD1JIWfdr9zNglo-3XWNYmYglQ3qG1kpj8QbtqcirdfN2PwYknguNIWY2HnYv_CmP8_ArKgPqnq3dMFjk1SSozhrfYUnPX9vHvCn4D6vQbvARTTyzPxRXfsk335y6FX4Uz5O3QUmnayWS9CIFTmb6Y0CqTDL2U0c-sReEoVLmKtpl7ZoMfYpYfgkXuOMJMirMV-RmzZhhCSgIARtBnJB8_Kxfg03ZvZtebYhCZ8E4S-NqePvyjljMxkHzvC83Qq8P08kQPW63MkBkb2f_5t2Di_GJsfqmEo5_PnN5P3AZh72p1YIHSi8zA6VI5aDHeTJSk-LXB4ZizM7E6ZRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108334" target="_blank">📅 12:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108333">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پشت پرده دستگیری مهدی طارمی و سروش رفیعی در جاده شمال؛ رویانیان ۱۲ شب به داد فوتبالیست های معروف رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108333" target="_blank">📅 12:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108332">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108332" target="_blank">📅 12:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای کروس کجایی؟ رئال مادرید بعد از رفتنت دیگه پادشاهی نکرد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108331" target="_blank">📅 11:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ختم چالش رو اعلام میکنم
🦦
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108330" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جادوی دیشب اسطوره لیونل‌مسی در اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108329" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل یک فوتبال
❤️
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108328" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108327" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZQoOL3CNIgUHF-U0fp44rDoVZoZney9NatzdKfM5zP7xcO7ZpgV2fJH84TvywVlznyvWXbFCGXaBEI8SIHv1a5-hwBTUecWsI23VT1FTY7BSOeWOKXGaRdhpxlo_WWSYx41WMKAQYtZtQgCFBzvElksUAvvjWQm7V_5g4VCANyZ3yua9GO3J2mKEPk8Gg35Alaxr3EMdWjzKh1ghlngPMKAe2mQVYWMYaVCaSStq5hTfN-90SP00E1sJOn3vj5-HcEwnICLx-Sb9LHwDJWvLfTWwVXUNiSPEjKUC3imua3rEa-ONV81EC-TgDge8H3pk6u4vtzjbo5AR_9Jts0uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108326" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108325">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxII3TBqq_yfTM_wK6QgMC6R4rwCYkcbohnQSPqTu7bDQTvnCgMYnq_wcqlY6NuSAzD-4uXmbI-jhAIDTWwUAkGBKVQBLduYIz0b2g-Bdp_IB0c2pdllIl63I_zjZnDkC8RlvlPZEsfJICeKdnsyz8CMbHLM4WGkOWm0CqhnGc4Uy9YY3pNFW2p9ogYdKPtfxRWObaM-TA9zBZhkBxvuCFtAW0-bi8cbO5GC1ga7l5t4jN9XisGym_1ImCtLSrdQHl2AtsUpF6bt4x9iPKBqatpiL3xak8494KAn6F1a-55yfUKmid-asHssOSbi5DLSBVf4MUga0Bf7iSP9mbNHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108325" target="_blank">📅 10:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نادر قاضی پور، نماینده پیشین مجلس: تراکتور پرطرفدارترین تیم جهان هست. از رئال و بارسا هم پرطرفدار هستیم. کل مردم ترکیه و ترکمنستان و آلمان طرفدار تراکتور هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108324" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108323">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
بیژن بزغاله 2008 روزی 4تا رونالدو و مسی به عنوان صبحانه می‌خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108323" target="_blank">📅 10:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108322">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108322" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108321">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
🎙
رسول باختر، کارشناس حقوقی فوتبال ایران در گفت و گو با فارس درباره یاسر‌آسانی:
🗣️
درباره بحث مندیت از آنجایی که این موضوع به منزله فسخ نیست اصلا نمی‌توان به آن پرداخت. شاید باشگاه پرسپولیس بخواهد از این سند به عنوان قرینه‌ای برای اثبات فسخ قرارداد استفاده کند که در این صورت باز هم فارغ از اینکه فسخ صورت گرفته یا نگرفته باشد، باز هم تفاوتی در ماهیت ماجرا ندارد. چرا که آسانی بازیکن جدید استقلال محسوب نمی‌شود و به همین دلیل از نظر من بازی کردن او غیرقانونی نیست.
🗣️
اگر بخواهیم طبق نظر فدراسیون فوتبال پیش برویم که مشکلی وجود ندارد. در زاویه مقابل ماجرا هم حتی اگر قرارداد را فسخ شده در نظر بگیریم که بدترین حالت ممکن است، باز یاسر آسانی بازیکن جدید استقلال نیست و قاعدتا نباید مشکلی برای بازی کردن او وجود داشته باشد‌.
🗣️
کارت بازی بازیکنان توسط سازمان لیگ و فدراسیون صادر شده و نبود پروانه کار این نفرات در نهایت نمی‌تواند باعث تغییر نتیجه یک مسابقه یا اعلام غیرقانونی بودن حضور آنها در زمین شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108321" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108320">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=HcvVAym5Ps6Cb-zg3Yg5Iu3bpH4bYzsncvWyXtnv3ldPQKYfUNualblxuKpga4uKl3UVBdaoevGol64OT46CfHLw6V3QwTXx6-PfneOkU0kn4BvLOP6m4FtoUQx28l4dK2UCHr1yNttrPBeAcy0BGaJGpFgsKD7rNg2orsvIUvAOOPDaZiIi3AHgpFGeFnUbwPmLdigaG5KO6KH8DRnW0TslR_RoCVUMi9pM_uhd8TyQzm_ts_xQjNEejE3YmH1oBL3d2wRQhWPgtY0U63WjneIFUfbGX1y2WKFwcuCAfuGmyijkCwtm4pR3obc7sKSZQ37oIDAtYtA0rG3a5lqTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=HcvVAym5Ps6Cb-zg3Yg5Iu3bpH4bYzsncvWyXtnv3ldPQKYfUNualblxuKpga4uKl3UVBdaoevGol64OT46CfHLw6V3QwTXx6-PfneOkU0kn4BvLOP6m4FtoUQx28l4dK2UCHr1yNttrPBeAcy0BGaJGpFgsKD7rNg2orsvIUvAOOPDaZiIi3AHgpFGeFnUbwPmLdigaG5KO6KH8DRnW0TslR_RoCVUMi9pM_uhd8TyQzm_ts_xQjNEejE3YmH1oBL3d2wRQhWPgtY0U63WjneIFUfbGX1y2WKFwcuCAfuGmyijkCwtm4pR3obc7sKSZQ37oIDAtYtA0rG3a5lqTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
پاسخ زیبای سیمئونه به سوال درباره مقایسه مسی و مارادونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108320" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108319">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=lsCGR1iqW3DSCYJWknOy8FicwpPabR_b1Cr3LzLQomACgf-q1w_LKXEN3-d7iyAV10C9PM9_76njLJO5ynyKKRG-CRuj7CCM9zXL9rxlc0CbwzeADgHmUBOCfQYYeKAk8nscOmamfVJ-xNrfUzv_SNDIYpAO31ZRW8dl_UCLA5Lm-2W12WKlTtCsUPwE6u_xui1IJb0XF9d33lJrc0_e6lqbG_EDMXDUkoikz-Tpe_m3aJBGtR8-7kK5XEKd19jNBOpppE5rsMCDt6D9ciiJj6tboFq2SI-faXo_SimXNkH6asthte3zSueqtuaaPJ1XfSgQNJqEwZr4FUWoGBo9nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=lsCGR1iqW3DSCYJWknOy8FicwpPabR_b1Cr3LzLQomACgf-q1w_LKXEN3-d7iyAV10C9PM9_76njLJO5ynyKKRG-CRuj7CCM9zXL9rxlc0CbwzeADgHmUBOCfQYYeKAk8nscOmamfVJ-xNrfUzv_SNDIYpAO31ZRW8dl_UCLA5Lm-2W12WKlTtCsUPwE6u_xui1IJb0XF9d33lJrc0_e6lqbG_EDMXDUkoikz-Tpe_m3aJBGtR8-7kK5XEKd19jNBOpppE5rsMCDt6D9ciiJj6tboFq2SI-faXo_SimXNkH6asthte3zSueqtuaaPJ1XfSgQNJqEwZr4FUWoGBo9nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
گلشیفته فراهانی توی جدیدترین فیلمش از جان سینا اسطوره کشتی کج و قهرمان دوران بچگی خیلی‌هامون لب‌ گرفته و حسابی خبرساز شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108319" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108318">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=tosHj9Det3PMESK6nP7HPdl0wO-OuGQG4eGuW0wRhMFtUCPiIZgfnmW0qYCYfbXtCdoEWGw4ZcpI5vHUxliUYotjUn-ZvEb35EbGm9iQG8iTOonu7xH4v6Gi98ppbYVkIFRqAxEVlcujAeWhT8NEqYB6NpAS34Jk16mwhtW5Vxe0yK7jOJfTzsT4C4Op8Lj1V0--JiCYYrbM4_RA5UOncX45Dbui2b8esy6j_P2so_vvroTQJmJ5xVFdwdq7uVPMapinUlmbi-AKiJ66Cl2kw4kgL_4hh5scnMjkhjopQxZwLDa6cRTiWp3-sAqAiWq0mFgGij8CkfmPQcTXdgD76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=tosHj9Det3PMESK6nP7HPdl0wO-OuGQG4eGuW0wRhMFtUCPiIZgfnmW0qYCYfbXtCdoEWGw4ZcpI5vHUxliUYotjUn-ZvEb35EbGm9iQG8iTOonu7xH4v6Gi98ppbYVkIFRqAxEVlcujAeWhT8NEqYB6NpAS34Jk16mwhtW5Vxe0yK7jOJfTzsT4C4Op8Lj1V0--JiCYYrbM4_RA5UOncX45Dbui2b8esy6j_P2so_vvroTQJmJ5xVFdwdq7uVPMapinUlmbi-AKiJ66Cl2kw4kgL_4hh5scnMjkhjopQxZwLDa6cRTiWp3-sAqAiWq0mFgGij8CkfmPQcTXdgD76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت هوادارای بارسا در این روزها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108318" target="_blank">📅 08:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1G2jFigGbK3YKS6vkh6wbAcz8tm2Ot_dFwSkhoo9vgO5cQkeYnO2RyJwH2NMD9SHy9i9GDARTTbjaxaTDCmWNwWE5DOq0lDI--8V3oclHE6PjC8zxHgGHm3akrsxF4ZGbIyvpbfkD8wGg6ItW4yFSFaE3iDl4zu5o10BD_MFcQHYq7KgUBMI7lyseWNC3ztENe0sC21dTAr53tOU40B8TXE-DTP0IwTTkGifW-d0s-91ZoqFovvCE4dIMfuryucd9CVo8NCbWAtSjGJwEZyqe0IQx03Vth5HStqia8upz8U5WL67V8SoamD5RMcva-VV8L7r-TK7AIaDvOr9ld-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6LJ0Z8-a-8Y35HxTC0pg16AgOvRqsEYu0ncI989sz3CwUrkUZ7Ca_kP9hdfzft71mBxMAmvPZAof-6xgsAZg4EoH6Qfq_cxx10zT1uKQXbhW6ItiU_v17fQfnEDxTg0u_nf73fMPKvJ7TjAuxvEq40w8_PCzIh0EsgHbNm1pBSx3TvDzTiiHVmrY7ur-d0zrm5pX4di_sH7at_ultdos6-hSPbCVZ5T10Ia1Gjfcc9XBVIoOhYD3QUnEAs0NMqIqixtBxbu6u97Mtvs5rArRoi4RqMwqop0R5RqOn8nnHMMHypttE62MCPcKoQ86LzoXzO28h4kaz6VzWMjp6vuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFqlfo1Zm9g26UMRGpUyPIUtgYbd0vrDxw8Rc9W8bAlimrxbKApJhZBFSdkDPd0jnTN4olwxIapW9AR_ChqA8Y_0f7LTpPgrG6xEuOzUQKLaJ0SBwKZn2YTxZYB7PKWHGWYMoVB7qpS0LuUvDXYB6rmzBzXoFu9fKXPQGvWFON4F6BV3zIYOMNmHsExEmGbgBCnwBaZwHNQCeHh4srV2HFU0bOTAkRarfIMh8bMpcwFQD5IDtCnHbWm_GD5dq0IXF-JzMmGwfTaDDhLJCaOKcNMmAGpuPEYBSuGU3W0rz4KK5MNpnOQcL31z-NTDXay0TNMCVf16YAtur8If0BrPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
وینیسیوس بدلیل حرکت غیر ورزشی حداقل ۲ جلسه از میادین محرومه و الکلاسیکو رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2fF7qzg3wr90iXD0VSNUIXqj2T8Ej-a4vLbB5hICcp9GLzuqcnFSbRFWVl3SuGaXXbN8PLAcWEZSHVRx0sjjohUvapy-DVGTUj8ggSJfO-fHcPL6Km0DSTc8Wd64MgN-c03xzGjP2-c_k-xdfRAg_G3NMIjY6UMCMNItmuAnpCNNtXI97AfI1SbJzj9SjMxMsfd54l04anaZl3nLhPsM36-eZEfz-W1gU1PwdgPqFuYEBA7COZw_wSP9lLs3e0_FZJKK6kt8K0Zk7Z_iH1gEgtKhpfnxiK9QIgs_x7D0YtNoAO69kFfiV3llVMSGcmUgGK00MCR1O1EhBjd53itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxA0d0Lb-XJYjCgFpHc1ZeHTIdWz4e-rrJicr8A7Bsa-nPJAqbEPYuNTDTlYOAJILeLcB2iEUpG_B-n-JFSIuMdShpi8pQZSdOIK7XNKKQH69diPhJUj1DroivfQi0IOZ6J1UcxuF_-Hdp3he7yGxyeYkOe41m8uq-tVhsPCWRD7ixxYdyliHjPQaGS1m4N0uHYSKlNuoajh0aa5MBlZZvHaBL6b9YWLUtLDsiZ16AWvTXV5uKy2SN6d7OO-JQy-p9VCv9qOiIL1OVlJoGNUHfUAb6sHIgjnT3ZGbACEbNFLPxb0yKL6BMmJixrCzqxU09Nt_G1I3kib6vZPgreeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYyLrKrh8jIeNqjdpNAWQx3DWPYA5MsDbA-534QOanDS4W9wsxe41WLTBqYEL1Xiq6BsjGFa72X4Jnsn0nIQ8ioHzCwIgsNDiSu_ttOLquZWArptyPRbaw5yzi0r_PKxOo-Ddi5YKmH1M6WvxMhavo6xuTmdAFbyD1zor_2lN5T8LEOKsd3NqNQyyb0WYfFQtDonxt2HN6gH-xEjeUTizZyRLGqn8oBh7YzO8xkev2iPLex7xRuHDIm9O5fUmgQhWHwejJ5S4TuuDnWYrh59y7SiymoAxDmnqUjiPGHHSarcIzhr1Yct5bH--9SEToLbRTZKLMwN-zTBGsbUZqIoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjuGW7jFVtTN4inok_bxaNgaBZ3EWZmj6-yErxMT0l8Q5AlFW985zg1IkIEwz2EA1knmzZ0bTDoKr6206u8U8FqdmXs46-GE7XCNx63BIYZqpMNdROX_Mt0wMWwRRL9oAxWklucpfBC7GL9WAPGA_oTWDrLleyQSMxzrxtUVIAaYNPYgAAAhh4V_O2J0WgtJ9phcFizt-Ptm2_e_8vHPUveSvBmzAgjmpSUtzhI6mg-vxIAQ3ydzkL2jqpG0NbgP9xsegFYE_7XScrQYQzQWJXLx7jgOlpqPRxWdAXPAINZmIWNNnh-uFbBeIqm1W9KNfAASCTmeqhzY3HJJhO3KbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=VA4Yxd5cWXWAyK5-DLLOHoqAlopBHFl7_rOO5qEwIAHV0watipPbi0gVmLSCI3CKZCcUHBJYPVQ5asNAYMXhUeMwt2FmxBnoTpbQLxIHm_lrnN2zPvdWiEJruJe7ldU2SsHs_7_mvTuFx1YzDWRm78t14QZLYkEzlo6VPDsEYBb8PVA79sbaPdlGdAzB37X0-YKmCnkUvVSaSoEXFbVIY_kcr1KPrf5vCbKukOSwbFW7UhKQx0VG7DofCypilr1x5MNo2wBvwwH2GFWhmQYokwF6vm9yNOUoAHlpQwwc8JguallL8VAPr8PhjTEv1G3czQ1Xz3O4Q_2i7lt75oIZOnRsiLJFEFb_8DxNRB8aPJfYC75cvobJRpzMpE9ox9Ob2VcK4mseQihvOfzMyobzbmWE71sbVtHIXkAjmJUJnadH_HsXK4kqUr5FGeTt7nVp0a4XV_9L7lMAO9cX6BImHwnOyj8BlT7JYRfFgaPqLe7An8HOAS0cAI27-s9MyyTKqJsvvwx79Rh_wO-0lSGUMBBTkCZJJYEPv8uz-5CUSzwrM616qLV0Oug5Xh-SbaOqAP_Zz__dOT0Q9tZk4-VlyoRPhNWl6zFd88Fmt7uiYYosgl4OSbdMqCr-73jeWUn61lAVJcXgrBN-S2kFgZne7vyZgmawrbQssW28XFhkEsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=VA4Yxd5cWXWAyK5-DLLOHoqAlopBHFl7_rOO5qEwIAHV0watipPbi0gVmLSCI3CKZCcUHBJYPVQ5asNAYMXhUeMwt2FmxBnoTpbQLxIHm_lrnN2zPvdWiEJruJe7ldU2SsHs_7_mvTuFx1YzDWRm78t14QZLYkEzlo6VPDsEYBb8PVA79sbaPdlGdAzB37X0-YKmCnkUvVSaSoEXFbVIY_kcr1KPrf5vCbKukOSwbFW7UhKQx0VG7DofCypilr1x5MNo2wBvwwH2GFWhmQYokwF6vm9yNOUoAHlpQwwc8JguallL8VAPr8PhjTEv1G3czQ1Xz3O4Q_2i7lt75oIZOnRsiLJFEFb_8DxNRB8aPJfYC75cvobJRpzMpE9ox9Ob2VcK4mseQihvOfzMyobzbmWE71sbVtHIXkAjmJUJnadH_HsXK4kqUr5FGeTt7nVp0a4XV_9L7lMAO9cX6BImHwnOyj8BlT7JYRfFgaPqLe7An8HOAS0cAI27-s9MyyTKqJsvvwx79Rh_wO-0lSGUMBBTkCZJJYEPv8uz-5CUSzwrM616qLV0Oug5Xh-SbaOqAP_Zz__dOT0Q9tZk4-VlyoRPhNWl6zFd88Fmt7uiYYosgl4OSbdMqCr-73jeWUn61lAVJcXgrBN-S2kFgZne7vyZgmawrbQssW28XFhkEsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmAUv48gup4OpiLyX85h503cqLsMFqX5LB2n0ICWurj7d3O-TxLAkIwnFUDzgZWaF2ym0xxOZCAwtpntiwDlzwDWclssVdKkBv1WHfzkVZS8SdLGcQ_pG8dyKcDjs_pfUjlorBzu4QVIXOTjxB8Dkv1GT_jaZnrYNG3qBo-38rhgpIVv58vfeyOxdGRxDCldFcScC3vPfaifCCZRnBc6XpLjAaJ4iza6JkFCE1RCfJyjECkWYki1EzaN-UH5Es9iYZmcvOCWs-kcD5q5fZ-89MaKgH3wRFLHUulCTqns7UXpiGyIcPDOUK63LBkjnTs6iAlM-BAFBSQv5q8BdHbg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUsFLYYfjQlI4c38JRhco7HSxNIpX1JRwn6h6VDKctYKsolsegYNkVXzIjWvLZSBn-BcHKRARTArV1YjkTGWrwtC05PY150TePUiHIiOqmgUIZ6UGt91oImuXg02YUcyMHRYWW-jehzvVL77lak7ufZkC2q1x8w43Ungyt3kPfxNpqowlHPafjgdDtYn1sMHFXS3b4d5vkhMr9HId_i2dyTUEhmZFvx5S4d6R-DhQFNdWwiy9lQUfiGbbPVEzkmD5ibvK2UZn5VhD2Lu1i1HTN20XFDuews31R0zrzjAnYGELTR-Cqt_DFWkgOmbyTsfHUnG76GyQUhCCtbqQdwVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس اخراج شد
😐
😐
😐
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=QHdfCvueXsFGc6yC45NLrGXH8jGbLJGIrBvgrZdZu0kvGbwuvJpoFdPISlqXwsLEyHKaZL_l25g2Qye4aVIkOU90vIvyf5fN4uj7c-Q6SJHK9s-bmWJpQIBocKhEou46C6N9MrUjd3rjm-9URIIOk9UUi0My0gxUTdp7CQeapp3SIyv4VmzeTEN4t0TC_GL0uE4BJAjLB7SQuK8u-VJMytiiWA-BXt9FKmrCKGGmNoRW8_uLuY2DHcKcE5wIVtoAsRAkya5KstS9Pq19yC5UseFIj7aRmWZvgVYH7e38Ex-yI9hSL-byiYkEz_hPDHWMwF4JkpyGagzPRj1JwAcYE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=QHdfCvueXsFGc6yC45NLrGXH8jGbLJGIrBvgrZdZu0kvGbwuvJpoFdPISlqXwsLEyHKaZL_l25g2Qye4aVIkOU90vIvyf5fN4uj7c-Q6SJHK9s-bmWJpQIBocKhEou46C6N9MrUjd3rjm-9URIIOk9UUi0My0gxUTdp7CQeapp3SIyv4VmzeTEN4t0TC_GL0uE4BJAjLB7SQuK8u-VJMytiiWA-BXt9FKmrCKGGmNoRW8_uLuY2DHcKcE5wIVtoAsRAkya5KstS9Pq19yC5UseFIj7aRmWZvgVYH7e38Ex-yI9hSL-byiYkEz_hPDHWMwF4JkpyGagzPRj1JwAcYE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
گل‌اول رئال‌مادرید به ویارئال توسط دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8eRBc5wuYCRuP4r-8B06KtCIzNetFg0bycF6O-dcteObyTmg4pVgwMGzDBD8uHRMmklUdJeyvLfcKYheIrgmgxt85xLlNlZvl2w0f04q2KHyTRyo8TZk1sLGfbkiCNc3jUI-Tz-OZ1QsYgWOwfLVxvLiqfTDwACV2sqh8o-C7dO34noNry0HlcfyoUjgUdLbnRFkH1VeEzGCPUyzSBCLxWfKaSenpNu6iaQA16nWXfYl4oclkLRUoWq5OU6XL1h_GPIGfXzbGRm5VEn31vKvaZgKYQrOWyelLL2-a8tzoMQ0w2jH3SIGQ2N1ZQJGMELBPp73R3aDw7cFQBHZrGqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هشتم لالیگا؛ برتری قاطع و آسان در خانه؛ بدون حضور رافینیا هم برنده شدند
🇪🇸
بارسلونا
3️⃣
-
0️⃣
ختافه
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIYnCjgfJ8TH5-3KG3yVPHOnkFqWxzFMcz9sL92Ltftr2bFpgp_CxQ6Tcyo-aJeK4a1GYx9ojBVETeaZ3DbjZi7Ptr5nIc497xuv_IofbhtB-MR8Ec5TjE9O0SF7G-BTqKDdcvMNzCMt_-02X5sL45BacCKlW8uRIu6bP1RdkavmAeFbsNdXwVqYdlJzlBlBMa775jArWy7oHCjSoxDeyKlLXUlsYKMOMVYX_6UyhFZczA_XoOeHsVlwPUhbexemt9xX5jN_TAnkp946B1Ch8u19P5Y_Eve_XCHIqcNM9tzSmI2TYEO92SjTLStydEH2kqOlU_06oqNo2poKPrFdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=QJx-dVWPwgBSQGTLAtJAzG_UqfyGoS8ztqWdIapuqXifZwAGcif4laEIMkVtXNoN2MnipZMVO6bLM9SkTgDQC9tLn9Iel4bkvXykev3mbsVDK1B3wq6WYgKndJZH_v-luHxmrUToZu1CtWkczmIQxTS4yNI431YUbPoH_cAg35HzDMGEMzAoWUMYIeoxUUXlYcvGdnYOMRsMckAyhQkHz9h7Tqen3UOFy2p29_PwHULTWzGCAN7SoIQHStbZCJUEVH4m3a__eccceFyrf-pOv2Lxkzb1t7fvqkP8n-TaU-fFVSeoKuGeRQipaeXMFyWcpP7FgOZkji_YlEGayfnq1ZqsdhrVKS99Z4gnpXz4DWuSoUMJTeXCC9327-UVLUhhAn_8NQsJ1-6SXs3N2f9hNEFp7laQZZ77_JKpuKkXl8wL3N3UEdg3JDfURtbi9DnPqpVXafB-hQESoAvsqfZ2VZvPLHLXOgNTOWDrYm5ZNDQLCrfcImKo0YXHj6th8KCFVYNwFrFSatPu8UHVXLlV1XLl-F6fVvNsT9WPTIkET1EiiQJ1xH0YbEULdsPKtCjdrS2QXFRrw-q9oNPgif3Nrh_jbd-Rjn8Djn7_G3VMUnHIFw6pPAGkWzxBBdueHnqgil-8Xs-b5bo-06X_bCbg2nQWA9eF6IHgM1MCasaLgnE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=QJx-dVWPwgBSQGTLAtJAzG_UqfyGoS8ztqWdIapuqXifZwAGcif4laEIMkVtXNoN2MnipZMVO6bLM9SkTgDQC9tLn9Iel4bkvXykev3mbsVDK1B3wq6WYgKndJZH_v-luHxmrUToZu1CtWkczmIQxTS4yNI431YUbPoH_cAg35HzDMGEMzAoWUMYIeoxUUXlYcvGdnYOMRsMckAyhQkHz9h7Tqen3UOFy2p29_PwHULTWzGCAN7SoIQHStbZCJUEVH4m3a__eccceFyrf-pOv2Lxkzb1t7fvqkP8n-TaU-fFVSeoKuGeRQipaeXMFyWcpP7FgOZkji_YlEGayfnq1ZqsdhrVKS99Z4gnpXz4DWuSoUMJTeXCC9327-UVLUhhAn_8NQsJ1-6SXs3N2f9hNEFp7laQZZ77_JKpuKkXl8wL3N3UEdg3JDfURtbi9DnPqpVXafB-hQESoAvsqfZ2VZvPLHLXOgNTOWDrYm5ZNDQLCrfcImKo0YXHj6th8KCFVYNwFrFSatPu8UHVXLlV1XLl-F6fVvNsT9WPTIkET1EiiQJ1xH0YbEULdsPKtCjdrS2QXFRrw-q9oNPgif3Nrh_jbd-Rjn8Djn7_G3VMUnHIFw6pPAGkWzxBBdueHnqgil-8Xs-b5bo-06X_bCbg2nQWA9eF6IHgM1MCasaLgnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به ختافه توسط کونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6WbaJh2iw3P0UBwFAauEowat7UUorxiKKU6ViUUjhsButnRr-iaqHMN9vadlK5hC-aelRvAqkT6DHyQuh-BXjJfLdxwJNGqI1ZmaxU6vxcyz6nA6-YVkuI25sg29RAI7o2YHnpuRMvvZF9NZ2Rphzxf8nWKfS607YEIJS87atTfVJasIrf9a3hnxYYM6BMuiZnb65pWXBJKpihLV13KgQ4ourOTbQc8NKDtXvqkS7wAitr0PWhewJOAMAA-GRKT1yfhnsR9Q-L9MnURu2o0PBkxwnmLhjtVABoLlSV_JmIx0lyBmP_4jsIJtJ3EEKRK835_ia5qtnSQpioiWl81Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSuI1G9RmZT1yDpfG7FTco44kRwwSCSkqoBJop35sE3zl9MODPUirG8Nl6zey3cJHn1pYCAGaQxm0l62XEbHy8vSoidwdfV7v0Kwb8UN9Kp01lXOk_6Gl0RYLn4XKYz0vWDN2HYOu5Hm6aRpcvb69iCmk1g75j4VlzgAqTxINUVzfrKB8vmFskpk58CZ1X5jt02NLVt3or0cKp7w79mb18sprLjK35E-GSfd3uDDdK_8rj2XwQ8yarjC9yf12HvI74ij9tGOQPi2CxL-XPLbR3-mJ7tDZRQMyHQURlBdtt7pL5sPK90iO4ykZOCvkgTbfnrixAv5WzbWaGf8iEyS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHnknYCLS2rzPIX-N8H_VhWVoX4bOvQN9ovtNwXms3k27G4cn8BBk7biP7_CODja259XSUDENUYochA-847EZAaiuSDPMi_UTFmkJnZyoMcaO165Oa6qIzOBNJkZpM3W8z1AZtROu19llZs-wFWI4Uec1Zh6UG7_MwI-Kv5L3ON-vCu1PBhowoy4Ws_DuyGC0pw08U-dJaZFoeZzb-Ofu3SZtpL6MbxDoYnGs-4rWV31U0nUEVkf7UjYrovCT4Pz9PF2bKQDhJ-dcAqwaTdpNeHreM7WciGdkWESu0uOMTTlg7o4mACs1yBiYgaOKD7p90FXvGNSb7GHUbU29V9ENMw4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHnknYCLS2rzPIX-N8H_VhWVoX4bOvQN9ovtNwXms3k27G4cn8BBk7biP7_CODja259XSUDENUYochA-847EZAaiuSDPMi_UTFmkJnZyoMcaO165Oa6qIzOBNJkZpM3W8z1AZtROu19llZs-wFWI4Uec1Zh6UG7_MwI-Kv5L3ON-vCu1PBhowoy4Ws_DuyGC0pw08U-dJaZFoeZzb-Ofu3SZtpL6MbxDoYnGs-4rWV31U0nUEVkf7UjYrovCT4Pz9PF2bKQDhJ-dcAqwaTdpNeHreM7WciGdkWESu0uOMTTlg7o4mACs1yBiYgaOKD7p90FXvGNSb7GHUbU29V9ENMw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=fUPJM5EuJIqEGJJcbJ3wv8t7e_ZVwGJzfzGqjWko21dEkLRPMXy-9PqQXtoOQRieB3kqu1xMu2n6ZsowI7PRvnBoD4bA0neCibiUg3E2Fh17AlJVjLoP8mrcZO3HR4E1OZ7ytdAVeYReatX1AkqDzUsm021D62gKu7FOBGuLUJNLgwpAQHgEZjBK4MsyB53aqmUM_Fj9_P9mmYErGNY7k6KPnyhabW45WqKRR7K6xCL8tEhwX15qgbDKwf2xHhuJb6iYwhbHSJkggwsWtn2aJG1z0cn_o4eCmd4c1ZHnAAY-jonohiUEwHdcAqzYqt_A9-3M9Swt4vaZjKlj8ij56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=fUPJM5EuJIqEGJJcbJ3wv8t7e_ZVwGJzfzGqjWko21dEkLRPMXy-9PqQXtoOQRieB3kqu1xMu2n6ZsowI7PRvnBoD4bA0neCibiUg3E2Fh17AlJVjLoP8mrcZO3HR4E1OZ7ytdAVeYReatX1AkqDzUsm021D62gKu7FOBGuLUJNLgwpAQHgEZjBK4MsyB53aqmUM_Fj9_P9mmYErGNY7k6KPnyhabW45WqKRR7K6xCL8tEhwX15qgbDKwf2xHhuJb6iYwhbHSJkggwsWtn2aJG1z0cn_o4eCmd4c1ZHnAAY-jonohiUEwHdcAqzYqt_A9-3M9Swt4vaZjKlj8ij56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=cbKHy_TVEuYfBlKe50JUduu_NzT6OnR0xrmrf7WvcLKq3XbO5a20Swr_pwdYrafkWXyMzHgMkS0_otJVJkydnksqmvHkBMeANQJbHLnF78196576XkZ6gq5Ch-IJ-K5RxL3isAWfc16JC0yIYz71uLZgDzU_OS8qPLsCRUFd-I3XCXbclUDp6Oan2lntZFoVtqbGVU9y9kwmyJ1v-t53sQvnuGqDtLNxIK7bJUjBhScWbyLmfgHNMVHNRzJvS3BU79Iz_p2sQJ2WQrJU5VybGpbceMqVT3EvbWIwrGu1n1vtM8WFRL69nuAYDg3AKmeRP8_t1vOsEiVi7DEP1Nw8VYaQTP6IzNfswofAzXGnd24NP_mSL31MD0aycNmctjtrETDbEpduruPMgkU8FSWCWomnvQ-Kitl7yxfCdgJkZda6gM2G-m5bsvfT3V5ttrAZbTlAoUChEx-_p08A3s3YcKg5aQqwCE_6pbstcggXNif9WbhEBhQeDEzkZ2WOdbq6acWVKnwYrI-3ludNi4HNLO_iBxpRPrQ6DwD2JudgluPVte79YY6OXeReZF174lbhSttoTHq4JxDGIQypYt9uLveT5As7Txs9hTtPKCSp3VrzQodI8ECacspjY073T_9aEYJO20RgZHypcDMdLorcakIdM4iGe9p9Kjq2zQQPX-E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=cbKHy_TVEuYfBlKe50JUduu_NzT6OnR0xrmrf7WvcLKq3XbO5a20Swr_pwdYrafkWXyMzHgMkS0_otJVJkydnksqmvHkBMeANQJbHLnF78196576XkZ6gq5Ch-IJ-K5RxL3isAWfc16JC0yIYz71uLZgDzU_OS8qPLsCRUFd-I3XCXbclUDp6Oan2lntZFoVtqbGVU9y9kwmyJ1v-t53sQvnuGqDtLNxIK7bJUjBhScWbyLmfgHNMVHNRzJvS3BU79Iz_p2sQJ2WQrJU5VybGpbceMqVT3EvbWIwrGu1n1vtM8WFRL69nuAYDg3AKmeRP8_t1vOsEiVi7DEP1Nw8VYaQTP6IzNfswofAzXGnd24NP_mSL31MD0aycNmctjtrETDbEpduruPMgkU8FSWCWomnvQ-Kitl7yxfCdgJkZda6gM2G-m5bsvfT3V5ttrAZbTlAoUChEx-_p08A3s3YcKg5aQqwCE_6pbstcggXNif9WbhEBhQeDEzkZ2WOdbq6acWVKnwYrI-3ludNi4HNLO_iBxpRPrQ6DwD2JudgluPVte79YY6OXeReZF174lbhSttoTHq4JxDGIQypYt9uLveT5As7Txs9hTtPKCSp3VrzQodI8ECacspjY073T_9aEYJO20RgZHypcDMdLorcakIdM4iGe9p9Kjq2zQQPX-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/326220841f.mp4?token=UymVYpWxfVkrhNX5GZN8eiI67erOXJfFrTNizrvhNStgjIbeyOfXLWlgr0zND-Rxsr6Pt-PRZb-W5tuVk7LGrG5JPQGAgMScCJuMCQxukhkZkkFYwFRlWTjhwD5KyxWNKHIA-m53ZM-yOVwGcjmtV2JsZXCeonJPX9lC0MymqLlF8yoW3vDLRfKGvX17LsuriTeYniyfg0aRD7SsBHjfkJ0sP_ubyOgsx2HBko4_eui1PQvY27b1IWoMlvMxp2GEWGcWBC2hklhGdS9yxtEgddR2N6-0OVX0ayWxBmFRuP-kQCJEdtQxF1pT7QN7QbAqudrDT_aeYSO2mi73NR0NbHoM6uMwysz5gHdaOTRWcpCCAF_gVhX2im8H3lhzYXMPcDkt8_1mOXVarWf159tMtZlFGjcsxdwp0GIC45_R59LPjmNOcRE8g1do9TVhsNkVfMGd1eX5Jx4yENEpgk6gvomXvAsOaWYqjJPCjMWBR-vjyksG3H_tCCS6-0btfa0KxzpWjNNUhZ6mrFKD_muihsS2f7rXEE6m3aQ1zqnRnIV-fjHn7zjwYA5hg3fRVU03o-VBjexUfsdkr6hCgPbXjpQKNh1lexPhlR8o1oFxezM0tK0CngoD98eI4F6npa_k35FizsoxzNDPTUVj-5G_DwPOZFu-UM-CnafJ_KRBlDs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/326220841f.mp4?token=UymVYpWxfVkrhNX5GZN8eiI67erOXJfFrTNizrvhNStgjIbeyOfXLWlgr0zND-Rxsr6Pt-PRZb-W5tuVk7LGrG5JPQGAgMScCJuMCQxukhkZkkFYwFRlWTjhwD5KyxWNKHIA-m53ZM-yOVwGcjmtV2JsZXCeonJPX9lC0MymqLlF8yoW3vDLRfKGvX17LsuriTeYniyfg0aRD7SsBHjfkJ0sP_ubyOgsx2HBko4_eui1PQvY27b1IWoMlvMxp2GEWGcWBC2hklhGdS9yxtEgddR2N6-0OVX0ayWxBmFRuP-kQCJEdtQxF1pT7QN7QbAqudrDT_aeYSO2mi73NR0NbHoM6uMwysz5gHdaOTRWcpCCAF_gVhX2im8H3lhzYXMPcDkt8_1mOXVarWf159tMtZlFGjcsxdwp0GIC45_R59LPjmNOcRE8g1do9TVhsNkVfMGd1eX5Jx4yENEpgk6gvomXvAsOaWYqjJPCjMWBR-vjyksG3H_tCCS6-0btfa0KxzpWjNNUhZ6mrFKD_muihsS2f7rXEE6m3aQ1zqnRnIV-fjHn7zjwYA5hg3fRVU03o-VBjexUfsdkr6hCgPbXjpQKNh1lexPhlR8o1oFxezM0tK0CngoD98eI4F6npa_k35FizsoxzNDPTUVj-5G_DwPOZFu-UM-CnafJ_KRBlDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
اتلتیکومادرید با این گل دقایق پایانی کوتی رومرو مقابل آلاوس دو بر یک برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=u3sM7UotfmMIUlesLN1Mf_saCROONBxo6Mo64xhF5RH3pDxRgFAfZ8hO1cOVNMCHnQwm7q6vrl55drKA5F-VZRhiM3Seeo8jcIp9jJxhyN3H47-ArvbCIB0gm-Qy4MU0iuKKb5B3-O7a-YxAeb15zVBbe3duqJUkpK-b8Wbpy_19KKpAaYA0dpTapOiFjJ3B83wGosCBHv68qvDBH9M-XPDi2VgFMBNOreZuQ_x1kP_5scxxvgvXGy9k4ZH6EwP0uZ8K9gbQH_LvcFainwPjcFqteUMpVlDQbquPCSequul82ErmqoVUpw9uXZGT69Sq_PJsECGHGpFGhl-1ZMt97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=u3sM7UotfmMIUlesLN1Mf_saCROONBxo6Mo64xhF5RH3pDxRgFAfZ8hO1cOVNMCHnQwm7q6vrl55drKA5F-VZRhiM3Seeo8jcIp9jJxhyN3H47-ArvbCIB0gm-Qy4MU0iuKKb5B3-O7a-YxAeb15zVBbe3duqJUkpK-b8Wbpy_19KKpAaYA0dpTapOiFjJ3B83wGosCBHv68qvDBH9M-XPDi2VgFMBNOreZuQ_x1kP_5scxxvgvXGy9k4ZH6EwP0uZ8K9gbQH_LvcFainwPjcFqteUMpVlDQbquPCSequul82ErmqoVUpw9uXZGT69Sq_PJsECGHGpFGhl-1ZMt97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل دیدنی و کاشته هندرسون بازیکن چلسی مقابل بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=a0VXRKmf1-4PGkwWYf_sL5WIUjf8TrgwiHC8kxLkufTyN9HQjL8LaWkfmwU7ehKKiXgWmOFO2-gwuDc84xygG2gfrv3A9rNz0ZAgkix_8dY5vFX_YCTLf88VNz-9JgnhtceBcyOUA0rusjIa8ts6DwSwNrfxRv03CxJhY37GUPZF-_OpK2d-BLA-C7dvtx9NQH1xXLxjYbyGHlKNwLQLp_7wBL6vSwzRDzc6l6nxyAhVLWxBZueMcuTKc6auPInUEVqf1BgOOBzGFFTnx1IYHSHQQOVT1-dBWMkSbecRjs_fSuUhoz97jm0Mla6ugy8Z-XEcIhb42XqRsKEwWbQIEYcH_5-BJY1mcq2NtfFyKFzkXMtZ3NlToupvf_9yd1sR-QQ8rbPWTbI0fibDdCHgKgLWAOLToM3RkABge-isTY-AMw_lyfmY9UKijBNEiZk3PqWZ6pvtMLTtxQ4YGiNdCmxOA5TpOAH1u017suio9FE4ctxXG-Yli3YoPAhosdaG0Yhv9-3lCAD9RJ6dxtYSEZvTrZxoCHRZ6tTDBRFYkxKOJEyif9n44i8U7o2W_rztnAWql27khNeHCEoTGK42ueQiMoR-OT2txxPP0w9d1hazsAAMIxX8Fou5y_aA_23nAK5wOP_iGbMXVCM2bz_yQGvcoal833D-Gtkh--yHVTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=a0VXRKmf1-4PGkwWYf_sL5WIUjf8TrgwiHC8kxLkufTyN9HQjL8LaWkfmwU7ehKKiXgWmOFO2-gwuDc84xygG2gfrv3A9rNz0ZAgkix_8dY5vFX_YCTLf88VNz-9JgnhtceBcyOUA0rusjIa8ts6DwSwNrfxRv03CxJhY37GUPZF-_OpK2d-BLA-C7dvtx9NQH1xXLxjYbyGHlKNwLQLp_7wBL6vSwzRDzc6l6nxyAhVLWxBZueMcuTKc6auPInUEVqf1BgOOBzGFFTnx1IYHSHQQOVT1-dBWMkSbecRjs_fSuUhoz97jm0Mla6ugy8Z-XEcIhb42XqRsKEwWbQIEYcH_5-BJY1mcq2NtfFyKFzkXMtZ3NlToupvf_9yd1sR-QQ8rbPWTbI0fibDdCHgKgLWAOLToM3RkABge-isTY-AMw_lyfmY9UKijBNEiZk3PqWZ6pvtMLTtxQ4YGiNdCmxOA5TpOAH1u017suio9FE4ctxXG-Yli3YoPAhosdaG0Yhv9-3lCAD9RJ6dxtYSEZvTrZxoCHRZ6tTDBRFYkxKOJEyif9n44i8U7o2W_rztnAWql27khNeHCEoTGK42ueQiMoR-OT2txxPP0w9d1hazsAAMIxX8Fou5y_aA_23nAK5wOP_iGbMXVCM2bz_yQGvcoal833D-Gtkh--yHVTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل های دیدار آگزبورگ دو - دو بایرن مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGeaU_bk7EqkYoOW_OI8bLuHMLjLUminRwQ6Z8PK4AVDuBj_W05I6o9QwLIQ-j-cwABlWgIPQ_uCnWYg3yEETu0VwD94MapFK1l4wylXRJjr25xeUNk0SdIhXkIbVt2UWiihQ4zCFwiL3n_NLAbZ0kpe5HtG_xDbmkigfsTpebvihy_htNQkvjH5xfPu-qCqllUdmVHAM_dvJ10kwVjdVn6j-_yklGSIqVGQoVpS4DN2H_zeE8fBcFIvyqf-EwKMpKvl3S3kk-qzEW8bZm7VM-JeT5f7zPYu9EQ22bnEW_WAkzO2fXe-XirOqfYzsAIei5ybFgqE20hwETEizsvP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8xSSeas_ncq_-DttHmGAuAmPavS-l4sN5yJCg074BtNzckogEKMjlhJCQNgF8TI_bYDcTonMU4u83BKmmSfaJTUaNBoo0MIrZ2BL4v3nok5cgXPUtXpLiS3pvqDfIWFtUuG_NILu7jw5dyBser54i6DO1BbDcHoji4cPqoNPuKDA-Nfyv7mLZVNln-kUGplD5RO7HGTa1U8jkotjDN60kol_tFHOOuLN_C8zi0f9sFBDIZlIRO6Gn63vt-LWDk1yV6aL-CL5qExOvvc_fZ7i9mVrCIqvUi-22-87xDujk9xhnCmkxGqFSDaBMAPDUXyaot2Dm9bc0rEjVhkFLFLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdFrR367vxohj9eqaBrVw0AhGL-LC6KS7ZfUrXztTwMHiCjt2n5FVuzdt3gQ2N1lzsErlS8koeIr1rVu7Yw4cizVwME5ZmEWHM0bqq35jtDpZVaQBgSvHNOKygjtN91hQhOzEakbFPO5GYwWN_bPkAGmMr3yhvN2Rq-NjQuFUu-6yA6WjGaxAtvxnEZwHNG-KUQx3XuVSSaSORLWaCyVTEc1C3l-tbvtT4WkJ8hYV46CB5w1FiSoWT9E4KzOt0RzNlbqgMKAIjOYFyEr1iaOIMZpcF5WDQEvgllpj1_i564hGSKt7quWCDBp0JoqKV3ViDpvScBXDORCX_-ZnfsGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXtz8s9zs0ML-Oj7gsVl1FhpWvvihD3KWPw6rUdmBax5Wp0rDOAnG7FPL8iCH8yVdP41gNLokf93Q8NgX5TQ2kIJsr3MokEK1t5uCXkT0RLMtWgZapltqlCJcUU-4I0N7tQLYQxEVx2XaalpZnKucTD0o39urxEh6OfTUTP9NvQOb5HhyNn4ltEyY7JalrMHi6okm-B-Ow5jXm4jqRbT6y0PbsY5uKXW5VEuI0m6xNZIQ2ZRVdnvEpJjTASXlIWwIL-jQVdQoLS_Dd1tMkuNuDlavih9GF7gprZbo68ZKx8BmEi2gJsSb0QUvnjrcSppe-LWSZ3s64tyjLyEpIEx3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و منچستریونایتد؛
⏰
ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-126131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgOY-AFRMNDwx_qAGG9VOmxhnOe6L52nkvodTTaokls3x-Hc6LkSBcrDiso-ZQ9H_wHza3g91G1YdGYjdJpXIGw5-juTVIwrQfDGzgz7ey0Gbxsu5TgdG-eCNrLjZzwKiKBOa79k_CDGMDPnmACVBW3FDQmd0eGZmH852SKfydeRa7EJurF_tpjSPqSJxE-MvPnnXbjfu6DAOztp5L3XDfF1vWlntXIq7jjBW4QI2r1m5M4XAvw_fWMl-otlWSuCx_ZGHyyoYCKqJ-qjRo6ShEDPbpbgQ2KaUStUyHXliipyvSmAFjVRJQnHHMyT2Qxr4Q-gxOZBmTGIoL3JifadLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از بقایای موشک‌های شلیک شده به سمت اسرائیل در محله‌ای در شرق اورشلیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/126131" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فووووری / تنگه باب المندب توسط یمن بسته شد،یمن تردد شناورهای اسرائیل در دریای سرخ را ممنوع اعلام کرد
🔴
سخنگوی نیروهای مسلح یمن:‌ از این لحظه تردد کشتی‌های اسرائیلی در دریای سرخ ممنوع است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/126130" target="_blank">📅 09:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کانال ۱۲ عبری: رئیس ستاد کل ارتش اسرائیل از دیشب، سه بار با فرمانده سنتکام صحبت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/126129" target="_blank">📅 09:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126128">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ارتش اسرائیل فراخوان گسترده در نیروهای ذخیره خود صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/126128" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93a8aefd4.mp4?token=kPfUCtkQgIvTXvyUt7pi7ysxoK2r_G0yqHL2rBVgTxyGHsgt8DQMZ2AjHjAy0fmzO4v7Mdqz1rk3MywQTsy8ajgMHFzNnQ85AbvXx_IT8XDWheymYx8NUpZqdsIkEfqI-H88Y30w1W23lTI7Cko2dspTqyArN0mTw9MuMzrygs0Q3wOTW4gFHeIxzi5xOqW5Y2hNmc1-zpqPoppV1udw6MLR0N-1jA4_NBKwdodWh-aF20RSd2GbQhc_S4ji7hStG1BDX_nvBKvKmHOokI391meBwpY6GivBPsw7IBCZUgm1qtCao32cqefr2vitvr7QEZCxCWVoGuN3rpEBbdd18Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93a8aefd4.mp4?token=kPfUCtkQgIvTXvyUt7pi7ysxoK2r_G0yqHL2rBVgTxyGHsgt8DQMZ2AjHjAy0fmzO4v7Mdqz1rk3MywQTsy8ajgMHFzNnQ85AbvXx_IT8XDWheymYx8NUpZqdsIkEfqI-H88Y30w1W23lTI7Cko2dspTqyArN0mTw9MuMzrygs0Q3wOTW4gFHeIxzi5xOqW5Y2hNmc1-zpqPoppV1udw6MLR0N-1jA4_NBKwdodWh-aF20RSd2GbQhc_S4ji7hStG1BDX_nvBKvKmHOokI391meBwpY6GivBPsw7IBCZUgm1qtCao32cqefr2vitvr7QEZCxCWVoGuN3rpEBbdd18Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مقام سابق پنتاگون: حملات به بیروت با چراغ سبز واشنگتن بود
🔴
برنت سدلر در مصاحبه با فاکس‌نیوز تأیید کرد که واشنگتن به اسرائیل چراغ سبز نشان داده است تا ترورهای هدفمندی را در بیروت بدون عبور از هیچ خط قرمزی آغاز کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/126127" target="_blank">📅 09:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: نیروی هوایی اسرائیل در حال حاضر در حال حمله به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/126126" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126125">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فووووری / تنگه باب المندب توسط یمن بسته شد،یمن تردد شناورهای اسرائیل در دریای سرخ را ممنوع اعلام کرد
🔴
سخنگوی نیروهای مسلح یمن:‌ از این لحظه تردد کشتی‌های اسرائیلی در دریای سرخ ممنوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/126125" target="_blank">📅 09:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126124">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7d28035.mp4?token=ly4yWC4BMKE-H9WzFgV_k0ltkcwVYlD2WRfy9jFrHPpc6MGO3cmBBljsAdi8ZZDV6Go0zJPXjl1HfLOl7OGKDnn9pIxupz02_3gAB1IfHvTq0reNES6b9yAJ6C2a6UvNqxI-Ob6trjsG5uh8sgXq7Zm764BRcuvtQmvqcM18QtRCobj2xfa--J-WoLCeevJBjwQ1xGZkKYyiqHES7_Svs_KupMsmeQgSq-U8PxSQ0_pCaNrSLhFcBtEhrYmVVXonmsXn-QLDcUyflDqS6v4r-ys5aLgaJ3aMF2C85We6laHmZCloHNYeLrMvKm4JkzlaLz8mcj9wXqSekK76sNfTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7d28035.mp4?token=ly4yWC4BMKE-H9WzFgV_k0ltkcwVYlD2WRfy9jFrHPpc6MGO3cmBBljsAdi8ZZDV6Go0zJPXjl1HfLOl7OGKDnn9pIxupz02_3gAB1IfHvTq0reNES6b9yAJ6C2a6UvNqxI-Ob6trjsG5uh8sgXq7Zm764BRcuvtQmvqcM18QtRCobj2xfa--J-WoLCeevJBjwQ1xGZkKYyiqHES7_Svs_KupMsmeQgSq-U8PxSQ0_pCaNrSLhFcBtEhrYmVVXonmsXn-QLDcUyflDqS6v4r-ys5aLgaJ3aMF2C85We6laHmZCloHNYeLrMvKm4JkzlaLz8mcj9wXqSekK76sNfTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس‌نیوز: ارتش اسرائیل اعلام کرده که نیروی هوایی این کشور در حال حمله به اهداف نظامی متعلق به ایران در غرب و مرکز ایران است. این حملات ساعاتی پس از آن انجام می‌شود که ایران دست‌کم چهار موج موشکی به سمت اسرائیل پرتاب کرد
🔴
گزارش شده که ترامپ از نخست‌وزیر اسرائیل خواسته بود به حملات علیه ایران پاسخ ندهد، هرچند دیگر به نظر نمی‌رسد که این خواسته عملی شده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/126124" target="_blank">📅 09:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126123">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تمام پرواز های فرودگاه مهرآباد تهران تا اطلاع ثانوی لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/126123" target="_blank">📅 09:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126122">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
حمله به پتروشیمی کارون مصدومی نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126122" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126121">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmFWcxiYIUOoqtlvESdnLtuZt8FSDjiE9gtytmSwjF_q7YWXaRHg9DPQks8gxv63s9nCPp1V_7Qe6OkuJjkBzXJEDQTCQHgDEwr7uFZKatlcly0FDB0xZk0ovoEByvORTXEp1nHiI2flDZoyV3dXUUw-b-pu1jtSWDrnjsbJ4kUOre6P06lAqnRc3D56lem9Yciokj0deOuAHkRmRpTz1AMWBC2jJa1Z48k5GtwK_T6j-uWysHodXS8yORnntVL_CCd6E_-0_IQG8TfpwsfjJ4qGffsI3BoihlylXTTEROZFdJD2AqQsFonYAWkGVWmAg7zDubP59qe5pFxGa3XdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده توسط اسرائیل از نقاطی که در آنها حمله گزارش شده است.
🔴
شامل تبریز، ارومیه، کردستان، کرمانشاه، کرج، تهران، اصفهان، شیراز و جزیره خارک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126121" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126120">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE4JIaYN6WIiuPOmD3v6-IXZiYeXTac56iEzR8NnKROOjPVkc2sfwnb3FOT4c1GSFshq6ILEJG5X_L3I927oJLgd9NVAG3hdJtH82KkPxn5x6A7PVtHGHXrKQ8U60qjcks-jGOL4lYdH-02pH5ouKyaBXNOXW8qYxhrDGDc1QFzvxMDCLSuTTUx9KEQev936kGWTH9t9FMBoUK9K1wY-nn9Kzy-GL54qVH7lectUiMgY18bf7B-j2_krbjGClwRTs3yH7VfRzV_CRtgfq9Sve8ZKQFCwx683VAGoswQ6hESUZ7lyzfR8hholZNlAenMvbtpV-7WhNFWqxHqaVsL-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۷۰ هزار واحدی شاخص بورس تهران در آغاز معاملات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126120" target="_blank">📅 09:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126119">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از منابع نظامی : پیش‌بینی می‌شود تبادل ضربات با ایران برای چند روز ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126119" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126118">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سفیر ایران در روسیه: «تنگه هرمز باز خواهد شد، اما تحت شرایط جدیدی که توسط ایران و عمان تعیین می‌شود، از جمله هزینه ترانزیت.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126118" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126117">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b485173d.mp4?token=ROjqreQhXtjwZX7IW6FKlCOHk68gSLaGn4WJ64tpRMAsjB2PtAiqD2T1CIfAxJqwUgA4fIjbXCK9hqPBjJsqKl3I8lIm8TeRbebDw1qCgBY3KPz4Wa6ISBhLWkzi3FLpnAgv75p4qO0SiIktPqaZY3DoqFUKtYxmZysSqnC1VxfZ5cWRyHjqCSaUkvW5wB3fegazRvxcC-0kPrCrvB5jtA6UiBhXDxak4ykN2r9R6PJOVVZDliCMJ0hElhvDz4aMvzk-k3J4jxiwHNNzJKbwR6nSo3i-nH6C5VlP7nTXRzDxun7Jfu_8qZIYMDv92h4ECSUUzGB_Y6yefQrEX3rWrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b485173d.mp4?token=ROjqreQhXtjwZX7IW6FKlCOHk68gSLaGn4WJ64tpRMAsjB2PtAiqD2T1CIfAxJqwUgA4fIjbXCK9hqPBjJsqKl3I8lIm8TeRbebDw1qCgBY3KPz4Wa6ISBhLWkzi3FLpnAgv75p4qO0SiIktPqaZY3DoqFUKtYxmZysSqnC1VxfZ5cWRyHjqCSaUkvW5wB3fegazRvxcC-0kPrCrvB5jtA6UiBhXDxak4ykN2r9R6PJOVVZDliCMJ0hElhvDz4aMvzk-k3J4jxiwHNNzJKbwR6nSo3i-nH6C5VlP7nTXRzDxun7Jfu_8qZIYMDv92h4ECSUUzGB_Y6yefQrEX3rWrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌های بیشتری از پرتاب‌های انجام‌شده از ایران مدتی پیش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126117" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126116">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTMPEFblr4qIukLLTMbzEihC1ZlqbP_-_n2aKduEPAZ4J_2bh4CSppDqNuCsJiJ3nlhYFeKmoaigC4M7DH-aqq7ZQXqkbWQ8oTukWXbLl-AV8OwEQCnusGu_r5m2vkr60oeCy5lcp0sAxVgyjtnXTwehBwa_Vp3OCU79iTTaBFdEWklm_6ED4PCDLd2keA7ZryE66Jb-gueLEaxvaAA_8hI4uPrq6LCx2tDFUXDOWrycZjTVkHA1904b1ahcoBwzZ6LnZJAFdGu3-iEAtJPAyirvWqRRNSH95L9y97hf6Mg_lZN1LRkGV-b8N6lobRdLqb0f61iFJtet3gCc2L4Mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد هواپیماهای آمریکایی در پایگاه هوایی شاهزاده سلطان عربستان سعودی از قبل کاهش یافته بود. هماهنگی آشکاری بین ترامپ و اسرائیل وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126116" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126115">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر تماس تلفنی از وزیر خارجه ایران، عباس عراقچی، دریافت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126115" target="_blank">📅 09:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126114">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تمامی فعالیت‌ها و تجمعات لغو شده و مراکز آموزشی در سراسر اسرائیل تعطیل خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126114" target="_blank">📅 09:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126113">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
صدای انفجار و فعالیت پدافند هوایی تو کرمانشاه گزارش شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126113" target="_blank">📅 09:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126112">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کانال ۱۲ اسراییل: طبق اعلام ارتش اسرائیل، یک ساعت پس از حملات هوایی اسرائیل به ایران، یک موشک بالستیک از یمن به سمت مرکز اسرائیل شلیک شد
🔴
این نخستین حمله‌ای است که از یمن پس از آتش‌بس که از هشتم آوریل اجرایی شده، انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126112" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126111">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
منابع عبری: بیمارستان‌های شمال شروع به انتقال بخش‌های اورژانس به پناهگاه‌های زیرزمینی محافظت‌شده کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126111" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126110">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
العربیه: وزیر کشور پاکستان بامداد تهران را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126110" target="_blank">📅 08:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126109">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
معاریو : اسرائیل حملِه‌های جدیدی تو ایران رو شروع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126109" target="_blank">📅 08:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126108">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573cd32c93.mp4?token=IGTVHtboFilHhF5TNOXR_F1Z5U1qFM-WTfdOzu9lUTTvolzwyTnfTKj48PwvZCIXi8O6x76SEH0AYZEdirp2ExSac_aoHjn7BZCCWvbaXTbBf4KRIfLK12xjfOgHp69AxBQLfHC98mPqGeL0R4X9q1t8uxRU3e8XmpOk4yhDpz1drWKs4HdXCGJaiCAidgvKipRBn8jdTru7RRO1C6TAlS2uY6n4GASLQM_UTtw4YUWf6-rGSFwXVqH_gfKDFp7IbrmqZiC_wm5CXobxG2bDAPNCz1uQNbtLbnNSD48YeoNyM9VFGiMpCl6mY1NUdU4kBlnBh9uGCg1ktogcAI-m5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573cd32c93.mp4?token=IGTVHtboFilHhF5TNOXR_F1Z5U1qFM-WTfdOzu9lUTTvolzwyTnfTKj48PwvZCIXi8O6x76SEH0AYZEdirp2ExSac_aoHjn7BZCCWvbaXTbBf4KRIfLK12xjfOgHp69AxBQLfHC98mPqGeL0R4X9q1t8uxRU3e8XmpOk4yhDpz1drWKs4HdXCGJaiCAidgvKipRBn8jdTru7RRO1C6TAlS2uY6n4GASLQM_UTtw4YUWf6-rGSFwXVqH_gfKDFp7IbrmqZiC_wm5CXobxG2bDAPNCz1uQNbtLbnNSD48YeoNyM9VFGiMpCl6mY1NUdU4kBlnBh9uGCg1ktogcAI-m5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آثار اصابت در خانه یک شهروند اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126108" target="_blank">📅 08:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: نیروی هوایی اسرائیل ۲۰ هدف در ایران را بمباران کرد
🔴
ما به چندین هدف در مجتمع پتروشیمی ماهشهر، جنوب غربی ایران، حمله هوایی انجام دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126107" target="_blank">📅 08:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مهر: هیچ‌ منطقه ای در کرمانشاه هدف قرار نکرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126106" target="_blank">📅 08:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126104">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGJX4Gw3G2I0MrWs1XpdB027jhnx2Z9e8Ywwg2Lgb0KmFgszQxt-CLXo18aIkgrx-wnXpKNcLGtTNGqQjg0HBbe13bF1f7P_FtN6mf30iwfPA0pVO40Di-eamy6TJvgRKHuGbG6iB4o-z7YrHFN4YdFOdocRAWme1AUfvqSW__mCud5M2AAeL0czNjtS4YS8Ir6oH6fS8HoaYAbPtyMRsZ5f-EnVsDrtAX4ETfrvCpZFd_XphGz8Dj1XZSFn3DGr83n9EJ-S1qTe9LeGdB5haHtbdCSqhkcvtjOcxZcaZWSFh07AHNNFBWb_c87mYft1lUo1cMcPuI-eos4ldt2sBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXoJ212ZG7YkpYkRH4xdbXoaWr6dq3z76v9Rq0G9VCZ40ECiY1pk7vR7CWWLmiz3i96doqlSNj2N7KOkrp3pLr3u_qzcae9VA4WELwLF_tLSyCwdghpbjOj711wvluHXjEe61rxEaoEGlExKx5GZt5XYpT0nHgKziPtPQS5JhjFHpPwbc3IWTl4s4-Kdm2kF6itLipD7vBU2_wcZtXjA1KyU0P9Gxqhvm_3lI-LBYt6r6ty-dvKTewS8lFrjTc9iwxvYPMrgn_Dd55DmJcrHBUEwkee3-oFSbPCzvK5p9mi23fMSfyMvA0mV1gbeEH5Vz7fQR9i0Q1n1FwixSEMIzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
به گزارش اخبار کانال ۱۴، یک مقام ارشد اسرائیلی تأیید کرد که نیروی هوایی اسرائیل به یک تأسیسات پتروشیمی در ماهشهر در جنوب ایران حمله کرده است.
🔴
این حمله گزارش شده بخشی از تلاش‌های دفاعی مداوم اسرائیل علیه جمهوری اسلامی است که همچنان با موشک، پهپاد، گروه‌های تروریستی نیابتی و برنامه هسته‌ای در حال پیشرفت خود، غیرنظامیان را هدف قرار می‌دهد.
🔴
ارتش اسرائیل تأیید کرد که نیروی هوایی اسرائیل، با هدایت اطلاعات نظامی، به چندین هدف در مجتمع پتروشیمی ماهشهر در جنوب غربی ایران حمله کرده است.
🔴
با ادامه‌ی عملیات دفاعی اسرائیل علیه زیرساخت‌های نظامی، اقتصادی، هسته‌ای جمهوری اسلامی، انتظار می‌رود جزئیات بیشتری منتشر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126104" target="_blank">📅 08:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کارکنان روزکار منطقه ویژه پتروشیمی تخلیه می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126103" target="_blank">📅 08:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I86Kf6TJFZYlH6RUWYa3JUtqxLW8mPeSEwD2bUXI7wYtjHFk_J8NTHqGx4sk6OI8f--j3e-MoBwRVNipT24h063F_rsVLgWCNR0wiY8XxkIAtogwOtiK-rvY_jub7O2M37H038CrgWhyYRzWVW3Smy90Lu-HycuKOy2hn76s_Uh6aM35XKUpZ9bKl9EcJiyDwP1I09x8Ly33sGSZ7_ZFp1oNORFGqIcioJrVAS-GdYyR_jzZS6OWU42y7yRIKF6V8ekJSVd0XYesjqdPl5ggPKqCM-G_9Hk4o7kwRZBfv-IS7P-fWEsy2NWUy1T900bzQDtTpz0aCPTA9ddKos37rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور مورفی: این جنگ برای آمریکا تحقیرآمیز بود؛ ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126102" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126101">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل اعلام کرد که فرودگاه مهرآباد تهران هم مورد حمله قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126101" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda9836535.mp4?token=YuWl5DIegxlilGVYBa8m6W0K339uFhmPk9bXg9j6K32H2UaS-RvUo22O5SpzxLCGhbLwDBFFItKbry1R4sWHgIsoh-euxuddS-SO51wwVGvcBNhptOJhzn4cGxl_aU4_25FKcmOXS5Yl5wUkQuiKTnHSqjYzSqewU1LPGiNHhIs5_gf4qDLpWrrR0hxoGelntqYwU1lYiY4iPtDeCif5Zat-g5Y18L2Jxjk77kClU6cUg7t3ImbInnzoT7NUUP9udkY9kxXlmlWSBi0eKYmC9vniNJItgjSOSkf0zVlOzzqN4pAdPJIPcrM5M5VJr-qbFBUDzU-6wvNIZsyfVy6tfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda9836535.mp4?token=YuWl5DIegxlilGVYBa8m6W0K339uFhmPk9bXg9j6K32H2UaS-RvUo22O5SpzxLCGhbLwDBFFItKbry1R4sWHgIsoh-euxuddS-SO51wwVGvcBNhptOJhzn4cGxl_aU4_25FKcmOXS5Yl5wUkQuiKTnHSqjYzSqewU1LPGiNHhIs5_gf4qDLpWrrR0hxoGelntqYwU1lYiY4iPtDeCif5Zat-g5Y18L2Jxjk77kClU6cUg7t3ImbInnzoT7NUUP9udkY9kxXlmlWSBi0eKYmC9vniNJItgjSOSkf0zVlOzzqN4pAdPJIPcrM5M5VJr-qbFBUDzU-6wvNIZsyfVy6tfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر شلیک موشک‌های بالستیک از سوی ایران به سمت اسرائیل که کمی پیش انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126097" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d6ac5443.mp4?token=XijcnhyMAI0PJQ4Q5KOft6e088YUzkSdjazoMGF72T--yVtifR6To0Oh8i99hZi-g1RZBrR8uWGLrqaWTaddb4itlIUn1fqN93XjeKUkVHJFuZV5UnShimTku1rlPEg4g7VE1-gZHEF4ScijmVvCUQC3NlSfLZn1Pik2GsWugTR3t4TiNc9VE4Wn2PM_WKqYBAyy1wS5WmNCNsuuve99-TYVpAG0csFIuXgUdmf5lYmKsf_fVRjDsb0u-xXamoYvswwGb38lulJE0Off_h9GswKGJ68rKC0ajpscuoXnPquwMeaIPk0zL0M4DEKzY2JY9dFXWGsH2J1wBM3RWVqn0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d6ac5443.mp4?token=XijcnhyMAI0PJQ4Q5KOft6e088YUzkSdjazoMGF72T--yVtifR6To0Oh8i99hZi-g1RZBrR8uWGLrqaWTaddb4itlIUn1fqN93XjeKUkVHJFuZV5UnShimTku1rlPEg4g7VE1-gZHEF4ScijmVvCUQC3NlSfLZn1Pik2GsWugTR3t4TiNc9VE4Wn2PM_WKqYBAyy1wS5WmNCNsuuve99-TYVpAG0csFIuXgUdmf5lYmKsf_fVRjDsb0u-xXamoYvswwGb38lulJE0Off_h9GswKGJ68rKC0ajpscuoXnPquwMeaIPk0zL0M4DEKzY2JY9dFXWGsH2J1wBM3RWVqn0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت موشک ایرانی به شهرک ایتمار
در
اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126096" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نیروی هوایی اسرائیل ۲۰ تا هدف تو ایران رو زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126095" target="_blank">📅 08:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a84d1026a.mp4?token=DOCy2QuR1UMIPaoQ7gbsYfw_SGavHrRbtq7CvfPIw2RCjKBzWolAum8ACeZVCyRuPEGmePIB7ikHc-b6xQDKTmXZPoVWrMiGcVzyzrAAm_wmUCIjO-h99hdYhtsVhdGhpspgq49neQl9MoQfLwhuDPujHqoRJ9UAOA4e3K9VTbu--kD1xdCYJnvWlLbPhRypejP6b16aRxixeFBq6N4LGqKU253b1zpEs0eWkIIu_qNc6mKSCpYQwVriU3OTFGiDgp446IXS4IW5SveLkE140-PXIPIlmztfkZegd6SuHndQxu2SBT-VvAWbXzv0EPtkpHJcfSNaTkA_NwGWIHGdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a84d1026a.mp4?token=DOCy2QuR1UMIPaoQ7gbsYfw_SGavHrRbtq7CvfPIw2RCjKBzWolAum8ACeZVCyRuPEGmePIB7ikHc-b6xQDKTmXZPoVWrMiGcVzyzrAAm_wmUCIjO-h99hdYhtsVhdGhpspgq49neQl9MoQfLwhuDPujHqoRJ9UAOA4e3K9VTbu--kD1xdCYJnvWlLbPhRypejP6b16aRxixeFBq6N4LGqKU253b1zpEs0eWkIIu_qNc6mKSCpYQwVriU3OTFGiDgp446IXS4IW5SveLkE140-PXIPIlmztfkZegd6SuHndQxu2SBT-VvAWbXzv0EPtkpHJcfSNaTkA_NwGWIHGdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به پتروشیمی خوزستان!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126094" target="_blank">📅 08:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کانال ۱۲ عبری: قیمت نفت در ساعات اخیر ۴٪ افزایش یافته و اکنون حدود ۹۷ دلار برای هر بشکه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126093" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
همزمان با حملات ایران به اسرائیل، ۲ انفجار در منطقه پایگاه هوایی شاهزاده سلطان عربستان گزارش شده است.
🔴
یک مقام نظامی مطلع به صدا و سیمای گفت که نیروهای ایرانی هیچ موشکی به سمت پایگاه هوایی شاهزاده سلطان در عربستان سعودی شلیک نکرده‌اند.
🔴
احتمالاً حمله توسط حوثی‌ها (انصارالله) انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126092" target="_blank">📅 08:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
برخی منابع از هدف قرار گرفتن پتروشیمی کارون در منطقه ویژه اقتصادی پتروشیمی بندرماهشهر خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126091" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsfyWseRvFFTpoZDhwANUWCgyupwmURyoucNLfK0v1d7XJD-AjMVlxw2_5_8WugvDHaMMe4bg1jqpf5iCojxSbUlOuzX9URHZgecphw-UXF4OwXCwOUF1RDrOFimhd7dkMh7cV2YpeHc5-PkIfEoFuG_gydm4dhNMqUoOMskvfmMOXCOe9vLLyDzyLf2Vmhp4TLJ0Ljiw_GsheGPdNBcZnFPcg70TGAbtbO5pUmAtPVN4SVFZsCLa3VRaTwbsyLX9o9a_ap_da6YP6izv3Krzw9Li5k5riQ8bfDR0xhyQoeaYkDo8oMrIHzw8dQg-KzjiFyrNlVLnpSqjMdzP1fZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126090" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKnVxYfocUQaisgTaWoFlER5O_jjXzMS5V5DK1pEYkmaSPz4yoFdrDZfZfoPee15BGwb3300UGv_CaWLbWabk96V3Gox7Cm9sTmfK-4iyQQTeGFh0IDYREj72PJ6IN4MkYqA9Y8tnn-Y6vuM5gwJetyfMAXKhVzXq5UD1W6BMIxy0iGphKJFiYslI9HUx5d7IVO_BJjWQNFmIdPA0nS8PYj6QspitAc3D3gcc-yuoFMtx3p9daHBNqyM6sG6f7LrGUZDv79Gnj2FH-J-peDiFPUINHl63lgcgq9Gr8VeU-Q5YTsgvAo4Q-cBplpd4pkmkJBGjzkTUsVzp11iJjLhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
موشک شلیک شده به اسرائیل
🤔
100هزار دلار سوخت شد که بخوره وسط بیابان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126089" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD7PAx-ilUqHA2XxKuzkESgGZx4rFvXcw3YQQ3JzNpBPTt4pWtjzMq4XRxCkXIEvRYNFFDg9K2QxF8i8_PZ8W95G3i-6XA9nvDDCSUu8N7a3Pm3who7SlY7uevwaBqga59o5N7MWSKmYk5FEAJMqQebPmwKK1W-zCwsaSFo-cENY5VEE6CJ_Gdtv_8xg66lE6CcnQgI2BfcZEi2WrSRH2wb7KVrRTkuQS2bAXZjWfPSgNi1obkexOxsVs8Aa44sYdq2WBcotjHpndtWXXVyU8nPWkDERPq1NP-unFx9042bKWeD4BMdiDwJsiwIKkikBxwzXWmovhSR-9kWlUEfhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی میل
:
یک فوتبالیست ملی‌پوش  تلاش کرده دختر 14 ساله‌ای رو به بهانه‌ی «بغل/نوازش پشت بوته‌ها از اطراف خانوادش دور کنه که پدر دختره فهمیده
😐
ماجرا از این قراره که پدر و مادر دختره درحالی که گرم سلام و احوال پرسی بودن با بازیکنان ملی پوش ؛ بعد از ناهار که پدر و مادر دختره میرن بستنی بخورن و دخترشون تنها میزارن کنار استخر ، یهو تلفن مادر دختره زنگ میخوره و دختره با گریه میگه سریع بیاید کنار استخر
وقتی میرن کنار استخر میفهمن یک فوتبالیست از کنار صندلی های افتابگیر بهش نزدیک شده و دختره با هیجان از فوتبالیسته میخواد باهاش عکس بگیره بعدش یکم با فوتبالیسته حرف میزنه و اون فوتبالیسته میگه بیا نوازشت کنم که دختره میگه نه ولی فوتبالیسته میگه بیا بریم پشت بوته ها که کسی نتونه مارو ببینه
😂
😐
پدر دختره به محض اینکه این موضوع متوجه میشه به مدیرهتل شکایت میکنه و با چندتا از مربی و کارکنان اونجا صحبت میکنه و کادرفنی میگه بازیکن میفرستیم بیاد عذرخواهی کنه و از هتل اخراج میشه
🔴
کافیه لوگو مجید ببینید که روی کیت ورزشیه و خب این فوتبالیسته مربوط میشه به تیم جمهوری اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/126088" target="_blank">📅 07:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyMBBHrkZwxL0mdcTb-tixhnWh4Rw2XILMJTLA56J56EPoqO6CxroquIsuemNYbYb11Rd2JZQUSZPndMGUvfs4aPbyKSuMrcB7b3ItxTp9iUbs-raG5hSdkD1dkOnsg8h36tbLkPsQz_WRRRfaPOMbZGdYsrDfeyKHKx-UgO86YvuHD_B3zuIqXdTxLUeBw9bdKzlIJMtlpzQ2SlINCQQUfBWjK0cPp2KqaR38luEsmlMieua4KAJn3Y5Ps_puMrFRSGoZe5fUzyN52W1UOGcb7O2X-dFm7v_fw-n6QgekmZIroMHZB5c4Kdrw1y2QAM4q3RvDHP4uj5Fkn6WXDBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
🐸
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/126087" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ادعای یک مقام آمریکایی به کانال ۱۲:
نتانیاهو «به نحوی» با به تأخیر انداختن پاسخ به حمله ایران موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/126086" target="_blank">📅 02:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dguil-xNUkB1eTxx7QhO1gJp909CcFiPxlLaVAfMpqjHt7sLzb770wrIBcvY4YhHyTfFUdbjq3w9iA0-n9Wq4Ssn8YomvQ5RhxwraGZ3g_LL4EEgkCDtL8g3camvtmuIhrBXj_Cxo-8jQPBN89u0j0PvIpzZbJP4M9guS--04P_O-86U1lTwxtMzNxxUHOXZY1_31UkDZskH0j_G4dsuM6ErdQAEjApQmeFi8rYKxb3smy4wjxI-HaFEhuzZnNAe8vD9pwoOV8kFA1PeA1wcLbDBJ68aUe-pcm2k14oeuSfIFWpWGYadlEYWL8cjXNhYeIQh0b58mny6KbnxTY_K9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تسنیم :
ایران امشب تو حملهِ به اسرائیل از موشک‌های "خیبرشکن" استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/alonews/126085" target="_blank">📅 02:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126083">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjymmoaZF93nI4cwTvUa_Uh5cCoW59arg9tGyXhLWSkkO0hyvufaqAktvHjwmS5Ozzo5yHAcr_tXJ4-caYxm_KmhD4bXWIiWhwIyB_5Fd36WDQ2aixNcVu96NxyPH5mlrPkct7YHw5Bpr0vF_1AM-KE05-zqRY-pleQ6k-dVAe1prt3M17U4TlEwUwo9j9f0r9oo0jxwLihmnzR3H-q7dWIVqtM2I7tXdhU8oFdPnwKIQRJuDKBgj6BqouYjonoTSAF1rIpJwfCJ9hnxsDG0XsE28fq6w7VmuSAUtoiBSkVUjDu-2JbeMPT1g-kCCjdBXTpdhAaZVFWdFSA3fLXEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5a7a839ab.mp4?token=dRl22uPpnNApLutETiAKxs0sfwmvBqWlBpmKf_CPSveJwb7n0YErKXzLqaexzAWpgv2yvMa1Rktog7CRy6_VOMAalWE3iHMUTid6xXEIWsMDORdjD8fMZnEPIBNnocTAOAgCvi9DRY2013sCf1fH-rJCXEeRT9edaYWu67GWl87QKYpsOQ5mfJd2gO04yvk6gyX2zkRklK_2hq17MUr5NbOHAAHHgSKvkZ_SOLNbp54V1VLz3TtWo1pL-mEL2xlytfcXdlId4hvc4XmNbxZAwtlSo9MD1uD-DaMz-4ui0r5MVEdMaSCMs8PDDafg3--SolmJ_IgwewaNXx3G3RFk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5a7a839ab.mp4?token=dRl22uPpnNApLutETiAKxs0sfwmvBqWlBpmKf_CPSveJwb7n0YErKXzLqaexzAWpgv2yvMa1Rktog7CRy6_VOMAalWE3iHMUTid6xXEIWsMDORdjD8fMZnEPIBNnocTAOAgCvi9DRY2013sCf1fH-rJCXEeRT9edaYWu67GWl87QKYpsOQ5mfJd2gO04yvk6gyX2zkRklK_2hq17MUr5NbOHAAHHgSKvkZ_SOLNbp54V1VLz3TtWo1pL-mEL2xlytfcXdlId4hvc4XmNbxZAwtlSo9MD1uD-DaMz-4ui0r5MVEdMaSCMs8PDDafg3--SolmJ_IgwewaNXx3G3RFk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/126083" target="_blank">📅 02:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szAH46000VhelVHYGrG9iFIT2vSWjMzejGMmmdsZVIpzL9hc6rE-tEf7h8huXivFQEAn0_lt7YmqL4kyuA1S97VT9lC4sl2AZiUhPAjB-dh0EItTx_V266kbs2Hk3ueRbmWhIGQItoZldXprw717ObioRPI9SoaQsFU6hPesPPshfm3_nUDEluji3_yg2dZOUjoxTuB5EosW8R3JxwVwnghYlCZ4c6v7xcDQdj9RHfnHQoIUKTuhIWg282ZfbDQtpTTLk9Sk37XGxL9yw8-NktDKFJo3pkn1p4qfNjDso5vK_Tvrt5b_pmF8I3E8UDpsBcl4linDMEKeYiVGuL3fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: هر چه زودتر اینترنت رو قطع کنین تا دشمن نتونه به ما ضربه بزنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/126080" target="_blank">📅 02:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: محاصره ممکن است قوی تر از هر حمله ای باشد که به ایران آغاز شده است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/126079" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال کان اسرائیل: در اسرائیل در حال بررسی تصمیم به عدم پاسخ‌دهی امشب، بلکه پس از چند روز هستیم، و این قطعاً به دلیل مخالفت ترامپ با حمله است. در حال حاضر تصمیم نهایی گرفته نشده و بحث‌ها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/126078" target="_blank">📅 01:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از ترامپ: فکر می کنم توافق با ایران در حال انجام است و خواهیم دید چه اتفاقی می افتد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/126077" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: ایران اگر بازهم اسرائیل را بزند ما اقدامی نخواهیم کرد زیرا دنبال توافقیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/126076" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: اگه توافق از نظرم خودش شکست بخوره احتمالاً گزینه انجام یک حمله کماندویی به ایران رو هم در نظر می‌گیرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/126075" target="_blank">📅 01:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: من تصمیم‌گیرنده هستم. من همه تصمیم‌ها را می‌گیرم. نتانیاهو تصمیم‌گیرنده نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/126074" target="_blank">📅 01:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ : نتانیاهو هیچ انتخابی نداره بجز قبول توافق با ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/126073" target="_blank">📅 01:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8PrZbvctbrVtxLKJz06BuprCPqcrcyMaZzdXy6K2M4eRg_a71v8NMSe2W7TeH9PHGs-BHtP4Grrqu8p6q2EJmKxaL8qpKHmiw0Y67KS_wf_pjB58LAmyXi9XvWA0nIuml9XTJvnNkZy3ABSnN_DVz11eGAtwBnlkX7NiXDjZJgKDvkwVmlAS6T9TqPNfVm9s4CLlTCCI-5SPHjBte43S83SNrhWSOnrCZ-z9GWARudAGh-Yh64W1uQ8F9NZHzdXy9UJ9gpcayQbIHHjz2yKUljM8ye0V7wGZxaIg0mL2gSOv81RjaOh4vqDzxpoUWYGEQAD5Jdj3CQdGR4aSzVx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی پیش؛ آمریکا هشدار داد به اسرائیل نرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/126072" target="_blank">📅 01:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قیمت نفت برنت پس از باز شدن بازار های جهانی با صعود سه دلاری به 96دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/126071" target="_blank">📅 01:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbg76q9YYHFgY8r6k7tO3O83EsfqCMhDeJ-udsWvt7-tQbWVW_94gh2AHp-W7VdVEaAXwaLTrFyN3MqMG7MY2hSG5BO4R331i0MyLMKzt7xiBUy3N8EK0zYG8kYHahYFbigVjxFALEH7Ob8zbh0d4pera7JPgcuwFmHjVMwJyvVfvd-VxQcSKkmbX04Ofi8SxYNvIhLsOfG-JccuPYuBcMUxkuVJusZf975oNrKOtZKbt89pzBPpiCI-_sTIjXk73lNwd5yIhn1XmjQ3o6J5H6975qNxZfEoWbVPkb9iCIq0yXZkCiLcs0HvNw1SCpEz2FTz9rgVf3AT_l6c2xaFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان از تهران رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126070" target="_blank">📅 01:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
جروزالم پست، به نقل از منابع: اسرائیل به ایران پاسخ خواهد داد و هنوز در حال بررسی زمان و مقیاس این پاسخ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/126069" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مراد ویسی: احتمال پاسخ اسرائیل بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/126068" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منبع پاکستانی به العربیه: پاکستان برای حفظ آتش‌بس و جلوگیری از تشدید تنش، تماس‌های خود را شدت بخشیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/126067" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
منابع العربیه: عراقچی به پاکستان اطلاع داد که لبنان بخش جدایی‌ناپذیری از پرونده مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/126066" target="_blank">📅 01:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amrftNo62Rb7Bru3MHoPxYVlkyNJxpgxCq2Zq_VwaSkg-YTwklEvm_4qmBCYQY-R8eths6_uoOB0CXotgMRZ25FUsLAQP_tBORJWcG2x6SsgQpZcLsLy4pvQV4O3cydHuAiizwipPQME4DExVq-fb87qMW3eUdSz3Y-EHm-5JyRz5yk9spumt8Ac-wAj9y97uYTJmeCLTsMYuQBOWAsg7uN2L3pThZWmJI2uv4vDr1qW1aHTPJglCTlEtmcVrXgUae1StdMu4jokp6jZ0ZeQOg9cR9k7xh9HHTV7gj8OYnLJYCNEj9ODWnQb1BikS_9ViVC4lKXn0tVuaI9mjV132A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: شلیک‌ها از آن جایی انجام شد که ترامپ می‌گفت نابودشان کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/126065" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec0f487e0.mp4?token=VYOlSRi201ARD3xwqtHXdSCZaPufv4r3LnSBqmcR9S84V6-ZrNcSVd6qwSMhRGUDZNjG5ucFGejyCZMprSGWmcs54r7OnDRRDytymLnjSDM0HfB7fPeREgp_tPJCUmMRgu39XK0dhWTMRlQ_ty8yBYSc_6jXebkA-pnCnw4w7xspvcG56qC0710NDxma-dczTqb2dWovGO_QKPmEYHQ9Nwjn-SpAXh_cLJ9tRwaE7V0Nz-7ZDweASFbp9VjSpY2mefvJGH52UNXMZ7kcK9PYW7ZuTvoVjTcdhEePSBN4n5y2-Py1SdBDLwz_VRn-mKjvw4SOQcUZQ1-P5FRMaFeTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec0f487e0.mp4?token=VYOlSRi201ARD3xwqtHXdSCZaPufv4r3LnSBqmcR9S84V6-ZrNcSVd6qwSMhRGUDZNjG5ucFGejyCZMprSGWmcs54r7OnDRRDytymLnjSDM0HfB7fPeREgp_tPJCUmMRgu39XK0dhWTMRlQ_ty8yBYSc_6jXebkA-pnCnw4w7xspvcG56qC0710NDxma-dczTqb2dWovGO_QKPmEYHQ9Nwjn-SpAXh_cLJ9tRwaE7V0Nz-7ZDweASFbp9VjSpY2mefvJGH52UNXMZ7kcK9PYW7ZuTvoVjTcdhEePSBN4n5y2-Py1SdBDLwz_VRn-mKjvw4SOQcUZQ1-P5FRMaFeTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جابجایی هواپیماها از فرودگاه مهرآباد ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/126064" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54201f2699.mp4?token=p1OuKV5t_CuSOrOuZ70blAP4nkPzhnVHKRF3KwXH-jhxEBhUhnkB35cUZhlw8NXOjtxXNKSbZU3v3RBM0VuugizY46e1f8lHvltn3Jto-CE2jlr19jnYEhinxdiSdvseyysW_vLLkLcPGM_JOqtrKNXBrzjc6yH_nH2O1LAY72GWdAlabiKe0RN9MAmL_7lmqJhHr2cw9rsdrErDepXZbrOYI1X0cXBk32OVI7PMeQhnI5ijgtiPdnKWG9X0FQAB_yNp7_1yVJc2aNVbpkAEkMGESuRwa12bS2Llc1MBBG-U-lmm6vKzy5ZreWPnMieThAmqQ87enSJsoUZCtQEvXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54201f2699.mp4?token=p1OuKV5t_CuSOrOuZ70blAP4nkPzhnVHKRF3KwXH-jhxEBhUhnkB35cUZhlw8NXOjtxXNKSbZU3v3RBM0VuugizY46e1f8lHvltn3Jto-CE2jlr19jnYEhinxdiSdvseyysW_vLLkLcPGM_JOqtrKNXBrzjc6yH_nH2O1LAY72GWdAlabiKe0RN9MAmL_7lmqJhHr2cw9rsdrErDepXZbrOYI1X0cXBk32OVI7PMeQhnI5ijgtiPdnKWG9X0FQAB_yNp7_1yVJc2aNVbpkAEkMGESuRwa12bS2Llc1MBBG-U-lmm6vKzy5ZreWPnMieThAmqQ87enSJsoUZCtQEvXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه شلیک موشک‌های ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/126063" target="_blank">📅 01:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مقام اسرائیلی به اسرائیل هیوم:
ما به این حمله پاسخ خواهیم داد، حتی اگر در بازه زمانی فوری رخ ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/126062" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVdsOW0FLNqvYTZhmlX_kXUd1cG8rsu8cOLh8LHaMMAgZv8_GOEuEhI1E2cknCkFs7-1Rleq0u-DyhmvCmyEMX_ewOrchywJAViJBd-pmugqyzPNb1yrqIw_lS_aoGAyeIDSBpVrnnLjfbp34QVQBJdmsfncbSIMnE4esyTe43QI03dnKFDbcwdApvGn68urUAy30e2n2g0MBajTSedX-XaOnYWBNFSy52dnPIachU-3ul2Z4cNK1M-YzmhntuEuY2efmxiGniGhI971GXm1lu6nIJ86cig5HX2RYo7lb_SIItEMHwChPaNnuiJsLMye02nx0OCgl4YBtIaxkmKNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل کمک‌های بشردوستانه به غزه را تا اطلاع ثانوی متوقف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/126061" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA_MWGWtHPTtyTOocWy1EBhMeQz1svx5oi6WISMUTv75N7rXUAlMNQ4Ym2SCTpv5C9p6LItmQZ4wrso4AYllVtPCfX7qk35_ej0ssZsjx_uIpzFVVPvDa_7n7v8PqQzseYa2xjcL9tV4Mwdvz1ISncYrL5FrlmFMzUWnnCS24TsRQxA1UxaYpdQK_S8VdPWTvNg-LoqhC7dz29kL02YCY6TkaoUpbhG2qbfHuVrUzQ3_CPYWfAM6mHukpJubHsUNKXoDRGFsQBad2GQ4sowrsbOfc2g3ZUYcPiTxxvMePVRvkmnNEGJLS-xa_AWScxBRr9XggvqTVyu_ApWQ3KxliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو وارد یه جلسه امنیتی گسترده با وزیر جنگ، فرماندهان ارتش و موساد شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/126060" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126059" target="_blank">📅 01:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💢
فووووووووری/جنگنده‌های اسرائیلی پرواز کردن و فعلا معلوم نیست به مقصد کجا
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/126057" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کانال 11 عبری: ایران از طریق واسطه‌ها پیامی به اسرائیل فرستاده است که تهران حملات خود به اسرائیل را به پایان رسانده و حملات بیشتری انجام نخواهد داد مگر اینکه اسرائیل حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/126056" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKEKZ2GJEQQ9Lo1CFnxWe7TTItRYeQgm7n3aAbwAVKoSVtM4BpdjuCnN_jGxe4x7wc-LUfFQeGt7YW-oMBbvCHLbEGqsCkM-naks4M_uiOjsH8zhKj9_b4e1Tb-BvE3fXbY6Uz7WmFcs1uJ6FtYe9aT3xsAqZq2LmZRbwqWJyEsVGpv-_T7aBrFdnJunAeLmcQasBBhFg_IkjsvUms_6aFJId1P4iJTS4vp1TSnzYGNqBQ1djO1vm8Plb5emanD4sGFDZ3MsdodwWliHgxHQIUnavtKdB3jjtjAPOYGV4vsvz8huE3RJu32yoxnZJ_ZBDEdnrNJAxlEkRnIXXpe13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا: درگیری ایران و اسرائیل بخشی از بازآرایی نظم جهانی است. ایران برای حفظ بازدارندگی اقدام کرده و اسرائیل نیز احتمالاً پاسخی کنترل‌شده خواهد داد تا هم اعتبار بازدارندگی خود را حفظ کند و هم از گسترش بحران جلوگیری شود. آمریکا نیز به‌دنبال مدیریت تنش و جلوگیری از جنگی فراگیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/126055" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126054">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ایران به سمت گروه های کرد مخالف ایرانی در سلیمانیه عراق پهپاد شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/126054" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187389113b.mp4?token=d6UA1-q4dbmRFrKrNIYlscxAdThYVHG-NIW-3zUVnwFKNTrflQDpXRuz08fHWQcCNnNyR6BVt0sc4ibGKc1Oklk0q3Kz6ORcAnH99J_75r_1xEyIaxeGq_8J4XCyDz-22TAwetqVqCkH1XPzICVvJepcqyV3dO6YQ7750gMTy6gMCELhoiKcv7QVOonTv7QUAc2iiTviO-pDmeK6rhE9Jbt3eTlrkFVWpn4L0depZ3PtCBxxtjQx3U2UgovUyjDewRQN3lZc16uuEkLsDWP1DQtwVyMOspG_n7NXS-botza27i3DhBuuyBvnsYVDy2oapecMyVutYgz6cFvl5lbPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187389113b.mp4?token=d6UA1-q4dbmRFrKrNIYlscxAdThYVHG-NIW-3zUVnwFKNTrflQDpXRuz08fHWQcCNnNyR6BVt0sc4ibGKc1Oklk0q3Kz6ORcAnH99J_75r_1xEyIaxeGq_8J4XCyDz-22TAwetqVqCkH1XPzICVvJepcqyV3dO6YQ7750gMTy6gMCELhoiKcv7QVOonTv7QUAc2iiTviO-pDmeK6rhE9Jbt3eTlrkFVWpn4L0depZ3PtCBxxtjQx3U2UgovUyjDewRQN3lZc16uuEkLsDWP1DQtwVyMOspG_n7NXS-botza27i3DhBuuyBvnsYVDy2oapecMyVutYgz6cFvl5lbPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوتی عجیب در شبکه خبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/126053" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرنگار شبکه ۱۴ اسرائیل:‌ احتمال پاسخ قدرتمند آمریکا و اسرائیل ضعیف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/126052" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا تا الان برای اجرای حمله علیه ایران موافقت نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/126051" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mt7lUCZGpsL3wHPj2wSocVdm-x-NA0ns-y8xZwF9d7uU-AxHUEEnXSzVyknNaCAudwNN2X-RwtXFiBzYiy2JuiorHI8Et7v5qRY6KnyJg5h5f1cqiLLu2SYYpHEPZPpKNIA11wdAabzfip_cpV0VOpzGgcchawo4LhqhmGVy3-WbMKHV5peWyhsg4oAaOonOSSwMSi7dsk8kq1NLsNB6WB0AEwWF6EVX-LXmxmlcJ1u-I4gGe0DScWPpFksMqmF6MKPN6Qn7a7nUaNYiICxTy8MNuXdSx5J5tUXM7HvgOKCzxqHchZYqnpXV-4HJpZTOuoEnh7Hrm7-u2eerESowdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/126050" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
جنگ اینبار بخاطر تروریستهای حزب الله شروع شد و قراره زندگی مردم ایران رو تحت شعاع قرار بده.
🤔
ایران برای جمهوری اسلامی و عرزشی های حرام زاده وطن نیست، بلکه یک مقر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126049" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شبکه کان اسرائیل: رئیس ستاد کل ارتش اسرائیل، ایال زامیر، در ۲۴ ساعت گذشته دو گفت‌وگو با فرمانده سنتکام (فرماندهی مرکزی ایالات متحده)، دریاسالار برد کوپر، انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126048" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/یدیعوت آحارونوت: بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/126047" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ به آکسیوس: من نمی‌خواهم این توافق به دلیل تشدید تنش‌های فعلی بین ایران و اسرائیل از بین برود، زیرا این یک توافق خوب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/126046" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
والا به نقل از یک مقام ارشد اسرائیلی: پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/126045" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFI-Bmj2vXMUJ7933kwrvtVpp7a1ABt19ee9eO7tO-T3Y1VOQw4s-9jqCOGiRJF8YCUiS8UJQbTVEpiUFSxEYmK3NaKR4WCG-ATt0oEtYW9B_HUVOmq9N7KDZCv6dTVO8C2v4RVJTdPB-qgwauzw0sMJ4YE46YJQFeV2_2p9oJXE_wpsXlODjEDcz7v4CVceEdEFNBxjdkhaCyP0HkZYbn272XO77By4_V-VXnxBLsCcgzWbtCUv8T-MnDzQTE6ObkbioByB0r3gvZM-6vgEg3Zi8qXrQpFAS9y6bmPNdl7Z6-7ghBBH60iQWfLCL8AQ5BGsnnP_mtr_K8Px5uPS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خو اومد زد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/126044" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس: ما بخشی از این عملیات نیستیم.
🔴
اما هنوز مشخص نیست که آیا دونالد ترامپ به ارتش آمریکا دستور خواهد داد که در صورت حمله احتمالی اسرائیل به ایران، هیچ کمکی به اسرائیل نکند یا نه؛ به‌ویژه در زمینه‌هایی مانند سوخت‌رسانی هوایی و سایر هماهنگی‌های نظامی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/126043" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X14d2-dgvjTOIFljC-BmWKnX8fRveBN6KbGlCIUOmXUanRwdg752udEfiwf-cSB1JtCT4i-07GO0c9AQZlOfo3qaUlZ2oVAdOfU-Ih_L1-hUGeEL7f49f_CpgvI9BFPBp4ndZCp2DqpACks6dku7gi_7-wahcYtRGFg6Tp_zI3ROhKtiM9KOmz-wcoiaa_e7nGvtbg-LzN7TNQXavHssKtLnbC87sKHIxOUVCRm8Z2po6W3iVjp2e6hBS8nn12sEKSMkaMgMu8U4mXh8ZHGitXkhUl2QEiWVCy4Qmzfi-zJnjEzptZ2N8NfBbNZdeZjc4SJfnM6uhO6VZtW9XZTrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وای نت: آمریکا به اسرائیل گفته بهتره چند روز صبر کنه ببینن آیا امکان توافق هست یا نه
🔴
اگه نه، طبق «طرح اقدام مشترک» جلو می‌رن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/126042" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
خبرگزاری ایرنا:
پروازهای فرودگاه امام خمینی تهران فعلاً تا اطلاع بعدی متوقف شده و هیچ پروازی انجام نمی‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/126041" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSrO1PTtjfCLo6eMMvm_H6q9qNk0etgy9ZbYtU6Bgzm44lU2CNkEjAaOjV0o8c-gxKQb9Cm44FKa33YVc7iS7cl9Bxgot_kupaR56yCPMyVPIH9rFovGuP7TyyD5lfiRbTF3eFrgze4sGLsvZoOwhCwKYpPJ-ke4eJI2y6rqbVqwd5LHZUsBYhLVXzaJSkaSON6Z1N8gYjGPW0RKpW8bUspFPKKCkRtnmsmw404ACOVNPL3AdmAOc7pZvD_x1Vj21JhlgCevHN-fhkHwbv4mATcQj8NKBAaqPGUYC7zMQgi1Rx9r1NYXsXZJjMDI4d5rDsH6mTNH6ac8cKvLZKZ3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
اسرائیل و آمریکا جرات حمله رو ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/126040" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
جمهوری اسلامی و عرزشی های حرام زاده علنا نشان می‌دهند که ‎لبنان برایشان از جان مردم ‎ایران و کشور ایران مهم‌تر است.
🤔
اینا با چه زبانی بگن که ایرانی نیستن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126039" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل:
پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126038" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8cJ4KUiKLYDFX-f8TTkdhIo84NbWrnXUE0mgzhCM5fiUWAG94KaCjQsJIPQHt39W-tGBpCFy6ujiCvzq5XDhlqK8h1cSzW_MusX_tapeKe4QJAKNvpCzAvv1mLo_Ggk7XN9XcKlkcnXCuUhYg56suFBCfh3hCwsWqB5RLAaTB969Bfqxr3bPg4tBaJGo7wFvDIZsx5Ah1eh_VhePEWVPiy0u5sW8L5x66glCjoGcFW9Z8CpsEzK22zyiPRDaRUIP11l4aE_fxZCyWHWGMrG0Q6_iUCNbqCeoox4Ch8KGRNz7R5HSNdwUpfAQcDu9OFYuV4aBXPVrCHQAoRpmxsCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایالات متحده در اورشلیم به همه کارمندان دولت ایالات متحده و خانواده‌هایشان دستور داده است که در محل خود پناه بگیرند و آماده باشند تا در صورت اعلام وضعیت قرمز، تا اطلاع ثانوی، به پناهگاه‌های محافظت‌شده منتقل شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/126037" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCcRg938ZbWb2sIGvzVYGNBZAOXSPGLpUYXUTk5jdocrvkN8PQy_jCfLnMnN0zflQVTIhdkNUFmWO1LLLaxyKK6QBSr_JIihShv-IMStJtpG1QMUEyn-V2nXR12P4GD3H_UgrZ6p3Eafg5BjTr2LtbSliozkzvpTC2MkaOLsZmmUflkHN7xF6p3io7zMbO_zKZDAmAi7RweFAIoSgmefm8RuretozI-BkvfXsNesOhu9hRFXV2kTjczKvvj3PLUE29-MPTZewhRqG9XEKx3xStkmID8-uG86TqmcxlgTYCygaI7XnKSsAjerjH5ZIh_ILUfIib63MmZwlHiuL_4zLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: باید حملات رو ادامه بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/126036" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvPmSoCpTFxjeGhrzVMe-OGUnw5_MwNjl6rYF1QsA7CmBWtSR9MoArbCpUWBzaWybAivpNiOEj3Eib3NR0g9CcdGYk-3I8iyS1PwbN8WRwi2gXCBKszIcsDHBijrlvtmnXNfub2_4AhvoBpiKlIZzzR2yN9nUGREuqIAln_aG0dg0kCBqZc7VZFbNaEmNC0lhl5DzKSnM8N7Oe-T8ICJxWylTw9wDR7mq81WSBLiFeRoVRvvQF06R-KkIIYoFUynZGT68Temv1meG9e-eIGRFKAIvePLOjz61SnLedcFOqV38A3zm6DzWgocKq4fEerRE-cRPia-TxUF0w7W6s-HcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمام هواپیماهای غیرنظامی تو تهران برای پیش‌بینی حملات اسرائیل جابه‌جا شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/126035" target="_blank">📅 00:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آمیکای اشتاین خبرنگار آی ۲۴:
«در طول یک ساعت آینده، یک بحث گسترده با حضور بنیامین نتانیاهو، وزیر جنگ، و فرماندهی عالی امنیتی درباره ایران آغاز خواهد شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/126034" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126033">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/126033" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=ptdRZVR1b7tJHOUq0YA5iGFkveRtlxz0UikOLqPWVNEe-bk5w-kQW28xv7MTM-Pah7E4-mxaeddu_G_6RODK2sG860_gPLJdv3LLXgzi7OZYrCPmqQmZq4NY2dVfKoCHjwXvt2EQTJCT4bFxDOCaa1D-FLNCsNgXkK_AGgwNEov_zHPD1jn-oXIOq0ysLX7Eb_x7Zkwo2bO1K_EWIkIjvuf_Ktg6JZLUWgVQl7cRKJwrGvAVL0LnishjwINW8RGWqybDbVk_5r09qaU2AERKs6DJw275eZHoKV56AkBUDok45vhfmiwi9dY6ku_1psB8ZHqVP8tDvik1XXS983hEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=ptdRZVR1b7tJHOUq0YA5iGFkveRtlxz0UikOLqPWVNEe-bk5w-kQW28xv7MTM-Pah7E4-mxaeddu_G_6RODK2sG860_gPLJdv3LLXgzi7OZYrCPmqQmZq4NY2dVfKoCHjwXvt2EQTJCT4bFxDOCaa1D-FLNCsNgXkK_AGgwNEov_zHPD1jn-oXIOq0ysLX7Eb_x7Zkwo2bO1K_EWIkIjvuf_Ktg6JZLUWgVQl7cRKJwrGvAVL0LnishjwINW8RGWqybDbVk_5r09qaU2AERKs6DJw275eZHoKV56AkBUDok45vhfmiwi9dY6ku_1psB8ZHqVP8tDvik1XXS983hEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/126032" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
اسرائیل بازم به لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126031" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm3WuikJX6iYGEj5rKPIwOLirk6ipdX9XnAmk1kHd70AIplqmBEBxnVnhLdJiY334Th_X_AfVGiYEwIcxG8wLFBfXrgDfbyH2yLzTeBlEE2d4qNMUbtQvUtdrm23vJvAbUCOxVwBEcS8dngoKGtJktJ_YFvvP7ese2JWKEMHZy19K5_YlinLFrM05sH4hMSSVcVdV95LkNJYoTmSpeDjzWAmPEG-d8JP4jN2KstqNAbcTgmYu627G7QPrO2Fn_n7L-pjKJkzBkWmFwuQDHNxTuusTQYsewITQjvgazU8Vxd03BkaqCK32Kj8RbqyGHPznDGXUUEpQchMS4THI3-vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران اطلاعیه NOTAM صادر کرده است که بخش غربی فضای هوایی تهران را تا ۸ ژوئن به روی تمام ترافیک هوایی غیرنظامی می‌بندد.
🔴
تنها هواپیماهای نظامی، دولتی، تخلیه پزشکی و جست‌وجو و نجات مجاز به فعالیت در این منطقه محدود شده هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/126030" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
چپ و راست داره از فرودگاه مهرآباد تهران هواپیما بلند میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/126029" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
هم اکنون قیصر در میدان انقلاب: پیک‌ها همه بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126028" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: ایران نشانه‌هایی از پیشرفت را در راستای تصویب یادداشت تفاهم نشان داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126027" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر خارجه عربستان سعودی به صورت تلفنی با همتای قطری خود تحولات اوضاع و پیامدهای آن بر منطقه را بررسی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/126026" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
طبق گزارش i24 نیوز، نخست‌وزیر اسرائیل نتانیاهو، وزیر دفاع کاتز و رهبری امنیتی اسرائیل قرار است در ساعت آینده جلسه اضطراری درباره ایران برگزار کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/126025" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbac3626bc.mp4?token=JSHlMQX3zJABoY8ygkee_hG2Ol-YLYnNmD9OUKdlCLaLaEUa9Rz4SWoVR8O-znQ8qHWHXsv6wF_A7ZnYUfiDOOVgSavAVjYJxBwnBKKs4uzdY1KFWZTqVIqvaxcqrdhsIE9D1dTdmUsU6j90Xn8ouK2mis5a9qjJ94D-u8JVI-IysrcotqwoylhC-Ui7widwshC_FUCJRjs1j2GPH-Wfn9cbl686WBtEAglpT0Tn-8SKiwDbZ_pVynbVzZ_DIVYCUXylFe5GCYZ69poybjulSuxd8u9uYXPmmquUyblj2trNlTZBFODpB5Likc18BnTwJ8ntx9V2RNZv8J3YxRi-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbac3626bc.mp4?token=JSHlMQX3zJABoY8ygkee_hG2Ol-YLYnNmD9OUKdlCLaLaEUa9Rz4SWoVR8O-znQ8qHWHXsv6wF_A7ZnYUfiDOOVgSavAVjYJxBwnBKKs4uzdY1KFWZTqVIqvaxcqrdhsIE9D1dTdmUsU6j90Xn8ouK2mis5a9qjJ94D-u8JVI-IysrcotqwoylhC-Ui7widwshC_FUCJRjs1j2GPH-Wfn9cbl686WBtEAglpT0Tn-8SKiwDbZ_pVynbVzZ_DIVYCUXylFe5GCYZ69poybjulSuxd8u9uYXPmmquUyblj2trNlTZBFODpB5Likc18BnTwJ8ntx9V2RNZv8J3YxRi-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد ناشناس، احتمالاً یک پهپاد نظارتی آمریکایی یا اسرائیلی، در استان کربلا در مرکز عراق سرنگون شد.
🔴
این اتفاق تقریباً همزمان با حمله موشکی بالستیک ایران رخ داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/126024" target="_blank">📅 00:26 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

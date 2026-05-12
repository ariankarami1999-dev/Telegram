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
<img src="https://cdn4.telesco.pe/file/olWm-ck3wRbulvIh7SA02gYlvhjtUxmPQ-KMzCTqfXE1kgbcXBFHF1zT850SL8f1C-TXE6I-74q-eACx9b5qTwIbK30lDVQU5O6qhzaIB19O_azOUacvR52BcJRSItd-V8mnLyBvmntcN-4i3lNkeAQv-cyE7fQ7varSozXMZSnWCkzagUH0tLoMLf0zRiMx6NrthbCCBE6pCZr5nfmNTYbiVa1u49g76Z3pXb1v5m97RvLy6ZfkL-Sm1qKuqymDtAVznaeSqS3JxAKFsaKmjJbBwIn7pk3FtDpuHZzATr5hvj0aTO4UvLLCAO2q5a-mJWhcIYsy7GFCJFwRJuN1Tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 13:52:58</div>
<hr>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1156AIzSqSAxI4zbC8HBcfvV3lXN6-BX98oho3jv1OxDoLeGq4A0kOI3s60FqQ6xrzG7-ilOZl7-_lgBI3QF6wu-sQXDv-NtPo0A2JkBLtmSgVe7go2E09DU5YPrqX-ZwkLWSjqQk5O1c5f9-OXnl5SuW1ZIrT9nwLeKvEoP2Qt7mjwgwu0QAoPCnTA0S6RFa1ip69BSconDtHrPLyTFk5IX8rNurxE8I9p9nTnU4GVq2V-ThDGc8hyNSvKHREFW1FBT6TCFxUmslZo1ce2NZFO-n8kldi08Ff405spKIjuDNOoNW6rdtktdHtZa61v-T-PPMkzmHyu8mPyEWzXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H1
در محدوده مدنظر یک اصلاح 4.5 درصدی داشتیم. اکنون طبق مسیر ترسیمی رشد بسیار عالی داشته و در حال نزدیک شدن به سقف کانال است. از اینجا احتیاط و نزدیک کردن تریل استاپ توصیه می شود.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 372 · <a href="https://t.me/SBoxxx/16202" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-gBv0odQDAJy2G-98ThKSjJ_GyfuoHO5CiuflZC9cIc6HrqAh-pm5lbdzVJYE15KQzagpy2eZSJsuuuEQREpmTLdyaqXozVVXQRgKTkEjL9Gr0bTET8gmju-GPzFEdwpMLZkX68RtKIxcWJoDQxrQH7LKkVl1zlc60twx6sgiP_7deoXPZ76WMlDn251Hv9_ubt9qT4FbynO6nTY1r89whrhIHZsLehdcVcb7aaAjVOcYh89z0FciR16sBopKFuQYx9VfV-9zlbHM8aL_wUsE5IpYROeZgdP28STdygg9GI3hunZjSZS5LmTrZMoGX4925oTnEqa3TZNfoicG5TLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 383 · <a href="https://t.me/SBoxxx/16201" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY0UO1RcD3sMKn3L-oKnJbilHn9_6KFhfPLa2G7VOqUS0TLbtosizOp2klTnKlKLS2y7yL53Zkg4p4H5Bvu2pBEldrPiD8vd1SRoL3bx2oEcCkZFu-jXaD5mk3tnfF2WT7sIbLogExDPjqzOlLnIZpNuW4HxN5f1SaFv7OYH1Rn8V2V30hgmPLMmSdYibJk0e1dkpj850hsw3PfCptTzK4W5VHtRfLFoz8-WzybvWNZMA37kNpVKAIB_U5p3td44FnePFb_igYUrFPWKSbiIbn3tASkxgP2v8JAUaIb1-iuQ3xY9aXB3qd9moTLjBzO2YBq_fheVaIq5Hd8a76CmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و فشار شدید روی ذخایر ارزی و طلای ترکیه !  طبق داده های معتبر، در یک بازه بسیار کوتاه—حدود دو هفته در دوره تشدید جنگ —بانک مرکزی ترکیه حدود ۲۰ تا ۲۲ تن طلا را به‌طور مستقیم فروخته و علاوه بر آن سوآپ‌هایی معادل ۳۰ تا ۴۰ تن طلا انجام داده است.   در…</div>
<div class="tg-footer">👁️ 663 · <a href="https://t.me/SBoxxx/16200" target="_blank">📅 13:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">CBS News:
پس از اعلام آتش‌بس میان تهران و واشنگتن در اوایل آوریل، ایران چندین فروند هواپیما به پایگاه هوایی "نورخان" پاکستان اعزام کرد.
این پایگاه نظامی از نظر استراتژیک حائز اهمیت است. منابع به سی‌بی‌اس نیوز گفته‌اند که پاکستان با اجازه پارک هواپیماهای نظامی ایران در خاک خود، احتمالاً آن‌ها را از حملات هوایی آمریکا مصون نگه داشته است.
محموله ارسالی شامل یک فروند هواپیمای شناسایی و جمع‌آوری اطلاعات آر سی-۱۳۰ نیروی هوایی ایران بود</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/SBoxxx/16199" target="_blank">📅 13:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#ITA — D  اینکه سرانجام ترامپ برای 3 روز هم که شده میان روسیه و اوکراین آتش بس برقرار می کند و سفری به چین دارد که اینقدر دستکم از دید خودش امیدبخش است شاید همان گمانه زنی را تقویت کند که بزودی یک صلح بزرگ — یا دستکم وقفه ای اساسی در روند جنگ ها — در جهان…</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/SBoxxx/16198" target="_blank">📅 13:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگر آمریکا دوباره به ما حمله کند، با ۲ بار قبلی می‌شود ۳ بار !</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SBoxxx/16197" target="_blank">📅 13:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
در صورتی که آمریکا دوباره به ما حمله کند، غنی سازی ۹۰٪ را استارت می‌زنیم!</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/SBoxxx/16196" target="_blank">📅 13:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/16195" target="_blank">📅 07:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCJJ1NxQ2_xvzWZyyWlkymakS64Dx73YdYgOiRxaiqa5Ux7VW9twTUQySXwlfnw3KiqQkqifLcqUHicnqtR429Uj8SGgSyu54Dta1hU5YCKWSGUpc8tNafDvQlCZ48X1_1tz7i7-_nfdH7NBV2j7LFkvI57UY6fzy2pflDBQtpQH8LQzrg-t-YwYDXgf74QUfR0AV62ftPRgN-POf9GoIKFN8rtExUK1W1j0Z-6xcs8YVBsyw7VENzw9W4MrwYk7uszuvNuu_5BneSAHyNRD6M-b4mom2AIbXtrvmTznDvhNO0HnNCh45XsYXQ4Y5XTU-PquDL2lQBgOeG7cGMUz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی مایر از شبکه نیوزنیشن با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال اقدام نظامی علیه ایران پیش از سفرش به چین گفت‌وگو کرد.
ترامپ از اظهارنظر در این باره خودداری کرد و گفت: «واضح است که در این مورد با شما صحبت نخواهم کرد.»
این در حالی است که گزارش‌های اکسیوس حاکی از آن است که دولت آمریکا در حال بررسی یک کارزار حملات محدود علیه ۲۵ درصد از اهداف شناسایی‌شده ایران است که تاکنون هدف قرار نگرفته‌اند، تا تصمیم‌گیرندگان ایرانی را به مذاکره بر سر برنامه هسته‌ای خود وادار کند</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/16194" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/16193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SBoxxx/16193" target="_blank">📅 03:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCjeL5PO3bZz7zio8OJZ-CWFBB7HEE5UAT_o9JhHFFfrN85CLNApsGn2pHF75M9onKmIUfyRKe7c2O8gvw3bQHQC7753ja6xmv64NIqlI4rpAKevhhJh9veOzyICbHttBb6WHYeapZhWQfKaUr22xsBNcOftQ3PMmf0Fr2-AuiY1fNjdEx7quhRLryy8hMnxgwEs9ft6ZarjMjV2D0QCFgEHHgHYImYHOzRRmo36D3RZ1jaA9xFZz473JO1nYi0YKFjRW4WmX4g6RpYzIC0CuBAUZHlJXFU2EhYtUwa7UZnhgzwZrY_XlagfKU9SgsnXfhogk_Pa2dcFYNBgzUBj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی سی استار ۳ همچنان در نزدیکی بندر جاسک در حال سوختن است.
این شناور اواخر هفته گذشته در اثر حمله هوایی نیروی دریایی آمریکا در بندر آسیب شدیدی به بخش عقب آن وارد شد</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16192" target="_blank">📅 02:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViQsp6UfJhYD2lh78qUvEwPseSzu5nVYECquoNiz1V4dhOdIPjssXRhRT3CVErq4Ist9ZtmiqP8HkEZsFNxHEqpmfbjbI-B8PFB0AoYnGpXb3NN16_U0_YgVPaLdcBehm4xR-PJbfOR1JZoJfiPr32vDmQzgBlEPwreDhh4M1O7kkzb29Kex6u-u4dJL6DAEgTr6KRaMivJX1HLAuyxTLvDPlWHJJ2039I13xznc3OORO4Dw772z5kH1JFzu2Q3Qi9PYOkYm5p-kxXPU9U8hnT595GXFVH5jVRaj3Pl5YgA_2i5iKjYYONKe5L4CX09PYC6uOu-7cYFgNEKJwhwIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Rheinmetall — D  ببینید چه شد!  بیش از 23% ریزش پس از شکسته شدن خط روند.  به نظر می رسد واقعاً دستکم یک آتش بس موقت هم که شده داشته باشیم.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/16191" target="_blank">📅 02:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3OiWZYb76WGG0NBT9ec733Q93Zyq4VvXTcwlh0Qq9ncMz1wgMbTZr0vs7yMMGfqu8tEifNLNXP-pLq4oUW73EqqBDirgtyveY9IETxCGjzMYob2aebc9DbCMA5-urdP77YT6ozY7zq_kvDmxXr1lc44ht5LwOtVgKXM8jvKsYpL8MB7KLj5TNqP_85BusH0PlhYAORDuvSfgwX7TfVrwVpHAsCX6-yvFfa5DjlYtUzaJRDCH9cJs--jCy7gIsgOan9jM0zRh06l8fjFFFDba2yCnd1l0q1XXELx4KXqRUQVfh1otGGQkhm591GTuSaub7vDIUEtYExiKAMay9eh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ITA — W  به نظر می رسد این صندوق که شبیه ساز صنایع دفاعی آمریکا است در آستانه یک سقف اساسی قرار گرفته که به معنی کاهش تنشهای نظامی در آینده نزدیک است.  در صورت شکسته شدن کانال اخیر می توان با قطعیت گفت که فعلاً جنگ بزرگی در جهان نخواهیم داشت.</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SBoxxx/16190" target="_blank">📅 01:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGJDdsfP4kaGDRyZFgx7PsqREiLaOmxF3sJrY88Jjoz0_1y_Jc15CIcbM5dv3hfkRcnt4ubpTDh0gtFLbxAzR6ltsJSQbiw12mQatxAlnGeAbf_xCiYblFE_oCXlAK3C0xZ-E9f6her_-1c5J21DI0EU58owPSTyY1QRHcCDWYAMoH0QYyGqbr9PUDSepmFArbrXTR3QOrOJueJCPg47X8n1IpY1LnYE9Vi63VrHm7Xc7S8DWU34UsDQ1bAzzpFiexa0QBLlL1uXAw7WKqDtwZzIYYLcvZ_XWZPZVObsxmXBRq2TpAKV187lZSQFVUlT_52Dk3zvncnvNGm--i9Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/16189" target="_blank">📅 01:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csjWUz2n-OZ_GWR19WoNBYZfjw-QGqrgVX_hKSUum9Q7a96gW4nDvI6SA4MfColJb9bTqw--jXeCIMm0dTnq5SXBZgnbrhsyuSJduasdlvHUyUS0Mm8bl5F5XrNT65m2mvd1AfipVnf-M0MeQLn4mbmUAJSIZ__jv_Xohf4NOfRFGaBgc14yGUZ-E6om17fAOqfkB0juOoTaL-KqB0kHE823IiGZHl2-4hIMo13IOb5DngQoWigt6HE5XSdilVleM6rn9q27fp9HPd0qvS-yd-s73KQB29HakutSv6h9YQE2zREmd4gACf722ZEstvQH-3w6xMLIGVrbUzv7slW12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SBoxxx/16188" target="_blank">📅 01:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16187">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvgw3AfW2bNpm5ygsVqsyJ8ZmeR_5zgc8UlbO0eqZUsK1U53JVEjlJ-MaouJIsDPrBfIOGo1g6mTeuDUCRpMuuVE49DkJTJozqWtzK6VLtG-zF0I4SGiAegLTHDY60APmyOPspaKRYUYGu3MhRvPz8aWRhHHuEvE52gX9hkTi3FCvmiRnrsFwsZ7Mna4Znt7ZYiD-KDnoDezdJG9DlR4VUPEi-rfoxmiaaPBo5MbxPRyl4Pn1SixwYkx4D86iYPUQtc4MByyaZsnSV3QCfBmHyGBUg3QBySJwwQhrg3LZzEBDHGVuGpScChCFcW0-fm5C7QMmtVMw6Ezg3y4N0tRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نهال</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/16187" target="_blank">📅 01:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار: آیا فکر می‌کنید آمریکا باید همچنان به تایوان سلاح بفروشد؟  ترامپ: من این بحث را با رئیس‌جمهور شی خواهم داشت. رئیس‌جمهور شی دوست دارد ما این کار را نکنیم و من این بحث را خواهم داشت.</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/16186" target="_blank">📅 01:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXz4HRm1tXmMu0UltePyFgHwdsS09HPaAzMRQOfQVdCD0TTkgdsHuZvzXahv9oW9y5B3vjBvqJirWbtYI9G2he9CkbYS795CIbQPJvBuqQIZHIljKULDRnJHsUmx9IYIV_hxAqjXxHYLY02ffa-NFIdOwmaFbYI7ZifxfJ-DcsEVoaIdOPjC2RE5thibGeMt4RsyIMEekcA1QbACPcFgKXD91kigM5rvsCJOLXWSMFOV_77VAboH-SCeHMwnMnhPXv83_JaLYSb1UehBYRUqVdYRJ86aSiwLSbvVR8E128pPthMJxSE9y-ycDl9sDwVQpKX3bp0GGKOeRese4ASsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دونالد ترامپ
:
من همون حسی رو دارم که ۵۰ سال پیش داشتم شاید به خاطر غذاییه که میخورم شاید فست فود برا آدم خوبه و غذاهای دیگه بده
آدمهایی رو میشناسم که خیلی مراقب غذا و وزنشون بودن میرفتن رستوران کرفس میخوردن و آخرش تو سن جوونی مردن</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16185" target="_blank">📅 22:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">قانون‌گذاران مجلس نمایندگان ایالات متحده در حال معرفی لایحه‌ای برای ممنوعیت خودروهای چینی در ایالات متحده هستند!</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16184" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طراح قانون حجاب اجباری:  موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.  هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16183" target="_blank">📅 21:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">طراح قانون حجاب اجباری:
موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.
هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16182" target="_blank">📅 21:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: با رئیس جمهور چین درباره تایوان و ایران صحبت خواهم کرد</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16181" target="_blank">📅 20:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InNVQLYbPTsSi1G0MIVtIXiBuvih1cdx70O0na9r0Bqs54OfhW0p0T9LZkyQ8arh8PaLgTg0IiiJPJOGUjUO1AlRVp9NPTpZICEdSpFXIZ0VvFcrMRTBwuvNwaKCMcNbEZVxYwH2Ms3pyMVGwWJ3v5lzU1y9skFt7GYT3PNmDYy2mCdwSbO06ypQmuXauxeHsbeNbOhNfKnRbGUnXs65Jh5FUUO6GYXdzv1BKRkew6f7P0Nm-EXZYtHuIY_TMAvXrlgRNzfIgJEFbsHdM0rs1L_NQGeud90bEMMbs-sbyYlSQq5gMu_p3FZTKFUXczS42RNhhEvxaIBD949SOxySNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16180" target="_blank">📅 20:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16179" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنيم از نزدیک به تیم مذاکره‌کننده ایران: ادعاهای مبنی بر پیشنهاد ایران برای تعلیق غنی‌سازی اورانیوم به مدت ۱۵ سال دروغ و جنگ روانی است</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16178" target="_blank">📅 20:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqDE1L_GJNMeZ8qjmjiGalwMpERzdicH-RshAHzP-FKAsEwP_1XFLx3NNIvsuXfNijVxhgJkWAvSwAZ8Np9oQv9CK5EzD9LVYjOYCcvqpexp9UAcoEBgQ3TVIPd5l5OglkL_65B8242IklZxyBiuWQg0wVGtFe9v6k1sqDlE5i12oGseHPa1lJp-barbx5bFxQsfk9XMRLOjTAGGiwkAGQdKPynneDt2_u69Wv2e1yLOfDYFdDyXnxf-MIB7qPlDHrcJEjlecqSo_LAtuu38PYEXnVlNIbUo5eNNIl6ZLaA82lcDjNbU5wyqZ3c5qox0ejL4rGJSsga4NwtMDZ9qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازارها از دست ترامپ دیوانه شده اند</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16177" target="_blank">📅 19:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ به صورت ضمنی چین را هم تهدید کرد که به خرید نفت از ایران ادامه ندهد!</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16176" target="_blank">📅 19:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ما هم باید مسخره مان را دربیاوریم.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16175" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پدرسگ مسخره اش را درآورده</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16174" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه ترامپ به ما توهین کرد و ما را به دو دسته میانه رو و دیوانه تقسیم کرد.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16173" target="_blank">📅 19:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ:
ما ۴ روز برای سندی از ایران منتظر ماندیم که تنظیم آن بیش از ۱۰ دقیقه زمان نمی‌برد!</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16172" target="_blank">📅 19:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ای گریدم به کله زردت</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16171" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:  آتش‌بس با ایران بسیار ضعیف است.  آتش‌بس با ایران در بخش مراقبت‌های ویژه (ICU) است</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/16170" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امروز کله زرد روی Long نفت است.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16169" target="_blank">📅 19:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16168" target="_blank">📅 19:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-zy-7i120J8Ra9XNlXVxwJoS6Nzax0-I6BLj9dF_hpoOYiRQ5A4L4hlxihrHF4MHxMino14GFLLxS_Ms275zg_h0fly9dhm8N5Pss1piDszXl3d3o__qk29TR1jDwtc09OwqYSQpcdQNFTvXHZDkfvBLNeDqiuMCvBIlVbfCukL0U5vXWwy3tGpBPIwN8j40qlBc1jPoqrJaYJFgIWaAopjLt0WBQE68Jrr4egpYR1UVjABls13Nufm0_geY0IrecnBJeIPzNHiPVZh3raLPfMuNLTZTVY1hOHoijM-to8xtst9t_gPS8VvE0u8a-qSspKNxGsQk_7vF91Fy08fYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16167" target="_blank">📅 18:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16166" target="_blank">📅 18:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وعده ترامپ برای اطمینان از وجود ذخایر طلا!  در 19 فوریه 2025، رئیس جمهور دونالد ترامپ در حالی که در ایر فورس وان بود، اعلام کرد که قصد دارد از فورت ناکس بازدید کند تا وجود ذخایر طلای ذخیره شده در آنجا را تأیید کند.   این مواضع منعکس کننده بحث ها و نگرانی های…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16165" target="_blank">📅 18:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16164" target="_blank">📅 18:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مشاور ارشد کاخ سفید هسّت: در مذاکرات با ایران عجله‌ای نیست چون اقتصاد آن‌ها در آستانه فروپاشی است</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16163" target="_blank">📅 18:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به فاکس: ما تا رسیدن به توافق با ایران تعامل خواهیم کرد</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16162" target="_blank">📅 18:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل اکنون از مانکن‌های واقع‌نمای فریبنده با کلاه ایمنی، جلیقه تاکتیکی، ماسک و یونیفرم نظامی استفاده می‌کند تا پهپادهای اف‌پی‌وی حزب‌الله را فریب داده و مهمات خود را روی اهداف جعلی هدر دهند</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16161" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptMDFtzR7KQr9YchwI0hS8GP_aOFGzJuCSzARXF0BGvlH5MzisZf7NhLEmNLL8Rv8f9JwXydZBT8raLfDhSBTkIwpxXoyztsdJRX1DHnf7yycGc2CZvrezWsHdTIstgR21V8dH7NtbY_FMgNURlzCr6uhm3_MnRwIi67UewGXI6ypRKb1YXhThKtKsOXSlVEX4JCJoyfs6zyB6IO4b-WM0rP9waEwkUNmbldvvrAI9TffG0z1ahKO4SqUD3cvwLpaSxiso8jpitUfE5DawY3S6IMGIPfdEoXZBlEIMqOxVrwDLDBuZZiybVHdaeP8ltCav__vaezOYc-k2wUyQO1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزایش تلفات اسرائیلی ها در اثر حملات پرشمار حزب الله با ریزپهپادهای FPV، یک شرکت دفاعی اسرائیل به نام Smart Shooter سلاحی را معرفی کرده که طبق ادعایش می توان آن را به سادگی ضد این پهپادها به کار برد و خطا هم ندارد.  شیر آهویا، معاون محصول در اسمارت شوتر،…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16160" target="_blank">📅 14:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VqSXU5XMDpzgaxo06fLS71SO1iV2r1RGXyh0VXCEjzqKy9PqUDT_EiySg81zv03XGCxyBdIpcTZ8CLeQNPF7llLU3j7WKPP-3t4G3hA5J5BpNMnpGnWScuGp6vY-ldHRLntUE4PJKrzQKmdhvet1RqDJalPEhM8K25b9xkLpapuSpcTkUih4gcxmknVajkci1mv_nPM3rCVrI5ojiHCuDIpVy-Uu1xrOGa7NNo6iFplJ_GU3Zrb41Jb_ASIQ7otWwOVdaKgya6eWQ_zPdAEKAhNuP8eNoNRFRqfjR_QstV-AFiav7oBUSIOG5cyNh-RBAh3oH5-82PBLDQS3-qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا دقیقاً در همین مورد یک یادداشت تحلیلی در سایت کار می شود.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16159" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پس از رد پیشنهاد ایران  رد آخرین پیشنهاد ایران از سوی ترامپ ورود به چه مرحله‌ای است؟ آیا به معنای پایان دیپلماسی و آغاز جنگی دیگر است؟ همانطور که پوتین گفته است، هیچکدام از طرف‌ها علاقه‌ای به آغاز درگیری نظامی ندارند، با این حال، به نظرم سطح تنش مقداری بالا…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16158" target="_blank">📅 11:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نمیدانم این احمق چه اصراری دارد که هر هفته یکی دو بار به همه یادآوری کند که دستکم ۲ تخته کم دارد ولی خب.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16157" target="_blank">📅 11:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بقایی سخنگوی وزارت خارجه:
تهران تنها به دنبال تأمین حقوق خود است و پیشنهادات سخاوتمندانه و مسئولانه‌ای به آمریکا داده است</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16156" target="_blank">📅 11:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رتبه بندی ۱۵ قدرت نظامی برتر جهان از دید من:  ۱- آمریکا ۲- چین ۳- روسیه ۴- کره جنوبی ۵- فرانسه ۶- بریتانیا ۷- هند ۸- ژاپن ۹- ترکیه ۱۰- اسراییل ۱۱- پاکستان ۱۲- لهستان  ۱۳- ایران ۱۴- آلمان ۱۵- مصر</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16155" target="_blank">📅 10:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqOF6elLBfohEUTIr3eshbv0iDS8gxBJd4FjI-SYXg85_NFXfBCX5W-KnsTkkMIeHnGrAGs73RzurUku9mdYVKa7_cUqWgmpyigSBIqD7MALyJ6Nxe4E4hiFIoGLqKkC92slNnVSGnuAQIx-jytfnKysoKdohPxDwZdMHrY0DMZTkkXQ6rn2Bn8vTq7xSePLShBaR8mr1u3AOvjoSrGmml-NrRTmrUg0V5rDZJwTV7L70p1Fd0wq870TM_77aKRXKPyFua5EhIdx2Y9HIL8CMN96ZZ3an5cjmmx6nZYrAcEZPVne4UcGalCZf5FYpEklRdsFBUNyTOELSc2RxHnmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره جنوبی:  «ما به شدت حمله به یک کشتی باری کره‌ای را محکوم می‌کنیم و قصد داریم پس از شناسایی مهاجم، به او پاسخ دهیم».</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16154" target="_blank">📅 10:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.
در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16153" target="_blank">📅 10:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16152" target="_blank">📅 10:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سفارت ایران در سئول:   ادعای حمله به کشتی کره جنوبی در تنگه هرمز کذب است</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16151" target="_blank">📅 10:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1f-v1jcd_vTH811EAD8krPDtCohILVnJEUNqCNC01kN8GAPpoGslgVopHxbnb23vAGuOllKlCGCGaq6ZGA3Zpsb-6SE-EOzHYa52O0KNqHTNoIfMdPLVxpjO_id760NQqu3GNTEl22YvjovzYno97ablCTs5zbCGrr77HDqftihDuV2vrwuqPRn-F6BTrr06CHuj9mVx8JHkTcWxJaJ0mQHClG6ZggFnFn2e2UOibxc3qUKNAz_coyhGtMysJoxTpRAbIjfyRY8Uk2jaCpKt6Y9kG9Xp30HbiUK-RgXmQQ-JbNy1PHgiUsJMZKA2whhuvtZ12tvR2dWF1dGVlo2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16150" target="_blank">📅 10:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu-szVHb5EKms35pQCzpXNNdArDs4ny929JbB0VHzPWd6e7F9ihicerWTgr5Cg0qzhsuCgliwba8rlo1FObaWY6Dh-X5L_KUQjxCU5oBRmTiMz68lSTlY9cgLLYvZMNZnOpIh_P4cdPKEYWV42YyE2AXkhOoG5pDxI-JkIvPaLRz8eAYX9lv9kFUTzRfOPBLuZSB3b0CeP-5zBcViqwObLiCM7IclZ776acykEFSazJPGx7AT2VOddsRLKqegSczkqNgIxjkTWAomW7_eLN79EXghYtYgZblpHwz0wr-0fI39PD86jx-GWZSaVMnFUWPL1ojfVbBQkdcSf5yBQfHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT
— D
به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/16149" target="_blank">📅 09:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده بهارستان اصفهان  روابط عمومی سپاه حضرت صاحب‌ الزمان(عج) استان اصفهان:
🔹️
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده بهارستان و اطراف آن وجود دارد.
🔹️
این انفجارها امروز دوشنبه ۲۱ اردیبهشت از ساعت…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/16148" target="_blank">📅 09:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده بهارستان اصفهان
روابط عمومی سپاه حضرت صاحب‌ الزمان(عج) استان اصفهان:
🔹️
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده بهارستان و اطراف آن وجود دارد.
🔹️
این انفجارها امروز دوشنبه ۲۱ اردیبهشت از ساعت ۹ الی ۱۳ انجام می‌شود و جای هیچ نگرانی برای مردم عزیز نخواهد بود.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16147" target="_blank">📅 09:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از همه کریدورها که حذف شدیم، یک تنگه هرمز برای بااهمیت ماندن در معادلات بین الملل برایمان مانده بود که این هم تا 5 سال دیگر اساساً فاقد اهمیت خواهدشد.  عصر اقتصاد دانش بنیان و هوش مصنوعی و ربات ها، آوردگاه گردنه گیران و تنگه بندان نیست.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16146" target="_blank">📅 09:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16145">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بزرگ‌ترین شرکت نفتی جهان،  آرامکو، گزارش داد که در سه‌ماهه اول سال ۲۰۲۶ با وجود جنگ ایران، سود بیشتری کسب کرده است.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16145" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNGPmXnDB19p1xUChFDuk0rxQw9a4NJs_GyU9RM9J70B9fcWZsVU1z4CfZuPtGBzmBR_RVYu06mj2Hjc1HduO6pkemJOppbS2LuFF0L0F7GFU0vX7I86T7_IGLP8zPpAIfJiUjXV_Vd7Zp5JXEbuwdHXZHI5wRre982DUtwzF9Otxr5YwTzeIjbPkPt534seAqo6O1QhwNOS-XEFgfO-SCAHL51A280cBj2iXY9Ni3zuW6HmVsbuP7fmx-qGatzxY6a_AkDZIBMYil3omcGsRW6WjR317rPkbNAMxc1FOn40YafYotkCSycdUzQriORBMUyKXa6urAorgwb5L0e0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه بندی ۱۵ قدرت نظامی برتر جهان از دید من:  ۱- آمریکا ۲- چین ۳- روسیه ۴- کره جنوبی ۵- فرانسه ۶- بریتانیا ۷- هند ۸- ژاپن ۹- ترکیه ۱۰- اسراییل ۱۱- پاکستان ۱۲- لهستان  ۱۳- ایران ۱۴- آلمان ۱۵- مصر</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16144" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">متفکر آزاد، عضو هیئت رئیسه مجلس:
تنگه هرمز برای ایرانی ناموسی شده است و به هیچ وجه آن را از دست نمی‌دهد.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16143" target="_blank">📅 09:01 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=Ol1HcwiZML73muY88n1uiyCasgXABDlWo_dMwUuVerVidexR8uXthZFJqZLDKgbBwER9zF9qXGkdl34RNZW78a9NrQagwOtyeDQARb2I4lW2KoVaKg1f42m64daK2KXaNAP2fIceGrEeQY964rKK2_Z7JXnCcJFQO-XKkaGJJSSHF0M3pv6f2h8cQv_Lt6SnO_FkD8JiLH6cZQDPfFnlEXFWYJqjheD0-1nfTnbrHNnEaN6EjWcWvo0twc6xvGTfEd5GOk5FKpLHuxdA8_tkxcNX7SATl_iBRWKjS_lsSeYcjyj7IKGIsCHjf2G9xiDUs7JFm3ggI9-5Y2TnQqmubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=Ol1HcwiZML73muY88n1uiyCasgXABDlWo_dMwUuVerVidexR8uXthZFJqZLDKgbBwER9zF9qXGkdl34RNZW78a9NrQagwOtyeDQARb2I4lW2KoVaKg1f42m64daK2KXaNAP2fIceGrEeQY964rKK2_Z7JXnCcJFQO-XKkaGJJSSHF0M3pv6f2h8cQv_Lt6SnO_FkD8JiLH6cZQDPfFnlEXFWYJqjheD0-1nfTnbrHNnEaN6EjWcWvo0twc6xvGTfEd5GOk5FKpLHuxdA8_tkxcNX7SATl_iBRWKjS_lsSeYcjyj7IKGIsCHjf2G9xiDUs7JFm3ggI9-5Y2TnQqmubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: در ایران، خیابان‌ها را به نام من نامگذاری می‌کنند. می‌دانید؟ خب، البته بعد از رئیس‌جمهور ترامپ هم، چون او رهبری مبارزه را بر عهده دارد.  اما آن‌ها این را دارند؛ من فارسی صحبت نمی‌کنم، اما مرا «بیبی جون» صدا می‌کنند: بیبی عزیز.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16142" target="_blank">📅 03:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بنیامین نتانیاهو:
در ایران، خیابان‌ها را به نام من نامگذاری می‌کنند. می‌دانید؟ خب، البته بعد از رئیس‌جمهور ترامپ هم، چون او رهبری مبارزه را بر عهده دارد.
اما آن‌ها این را دارند؛ من فارسی صحبت نمی‌کنم، اما مرا «بیبی جون» صدا می‌کنند: بیبی عزیز.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16141" target="_blank">📅 03:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در پی رد پیشنهادهای ایران از سوی ترامپ، طلا با گپ منفی و نفت با گپ مثبت بازگشایی شدند.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/16140" target="_blank">📅 01:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esnx9toIjrUEzaofUn-u1UiKH3Xc2sfoPtiQNN7Z3ZPt_1KHxlFjL0Qv1CJ6MzR-RN49ElOmMKyWw-SvA98BM4B5wuucIenYOypQJeTFPBU5DxYtr8WMW-_E7cuLw0T1acctVIUAYTDdsXets4_GQtaGxFKHZHdsQjWZ6x5kpi_rOARk07KNGtQ73jZujDweGedRcvN2xHYdAt9I7rAaFPuJxgZblsfti7v-sF-xSda4Ak4cy_XlkOBOmZZiEg_mRXTHj8uHgheIFvhjALATkBoyKcedEMK5zKdqxzh0YkiSzVw_M13FD0AX7Hw1S_zBupJaMU6ZANC9mWnhU5QL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه چیزی پشت تلاش ترکیه برای دستیابی به موشک بالستیک قاره‌پیما (ICBM) قرار دارد؟
در یک تحول شگفت‌انگیز این هفته، ترکیه مدل یک موشک بالستیک قاره‌پیما (ICBM) ناشناخته قبلی به نام
ییلدریم‌خان
را رونمایی کرد. صنایع دفاعی ترکیه در سال‌های اخیر طیف بسیار گسترده‌ای از سلاح‌ها از جمله موشک‌ها و پهپادها تولید کرده‌اند، اما برنامه ظاهری برای عملیاتی کردن سلاحی در این کلاس، موضوع جدیدی است.
مدل تمام‌اندازه ییلدریم‌خان برای اولین بار این هفته در نمایشگاه بین‌المللی دفاع و هوافضای SAHA ۲۰۲۶ در استانبول به نمایش درآمد و توجه زیادی را به خود جلب کرد. این برنامه توسط وزیر دفاع ترکیه، یاشار گولر، ارائه شد و گفته می‌شود حدود یک دهه در حال توسعه بوده است.
ییلدریم‌خان یک موشک بالستیک دوربرد
غیرتاکتیکی
با کلاهک متعارف است که خود مفهومی نسبتاً جدید محسوب می‌شود (هرچند قبلاً در مورد چین، اسرائیل و روسیه بحث شده است).
این موشک قرار است برد ۶۰۰۰ کیلومتری (۳۷۲۸ مایلی) داشته باشد که آن را دقیقاً در دسته ICBM قرار می‌دهد. موشک‌های این کلاس برد بیش از ۵۵۰۰ کیلومتر دارند.
ییلدریم‌خان با ۴ موتور موشکی تغذیه می‌شود و فقط از یک مرحله استفاده می‌کند که این هم غیرمعمول است. این ممکن است نشانه محدودیت‌های فناوری ترکیه باشد، زیرا این کشور قبلاً موشکی با این برد نساخته است.
وزارت دفاع ترکیه اعلام کرده که این موشک قادر به حمل کلاهک بسیار سنگین ۳۰۰۰ کیلوگرمی (حدود ۶۶۰۰ پوند) است. این موشک سوخت مایع خواهد داشت و از ترکیب تترااکسید نیتروژن و هیدرازین استفاده می‌کند. این یعنی موشک باید پیش از پرتاب سوخت‌گیری شود. در نتیجه زمان واکنش آن نسبت به موشک‌های سوخت جامد کمتر خواهد بود و آسیب‌پذیری بیشتری در برابر حملات پیش‌دستانه خواهد داشت.
در این مرحله جزئیات زمانی برای ورود به خدمت مشخص نیست، هرچند رسانه‌های ترکی ادعا می‌کنند تولید سوخت و توسعه کلاهک‌ها قبلاً آغاز شده است.
نکته قابل توجه اینکه در میان کشورهای ناتو در اروپا،
فقط ترکیه
هم‌اکنون موشک بالستیک زمین‌پرتاب متعارف با برد بیش از ۳۰۰ کیلومتر (موشک کوتاه‌برد تایفون/بورا-۲) دارد. در گذشته رجب طیب اردوغان، رئیس‌جمهور ترکیه، خواستار موشک‌هایی با برد بیش از ۲۰۰۰ کیلومتر شده بود که این امر نگرانی از تهدیدهای رو به رشد منطقه‌ای را نشان می‌دهد.
ترکیه همچنین روی موشک بالستیک میان‌برد
چنک
با برد ۲۰۰۰ کیلومتری کار می‌کند. تایفون بلوک ۴ (با برد تقریبی ۱۰۰۰ کیلومتر) هم اخیراً آزمایش شده است.
این موشک‌ها اکثر رقبای احتمالی ترکیه را در برد قرار می‌دهند، اما تهدیدهایی مانند یونان یا شبه‌نظامیان کرد در عراق نیازی به ICBM ندارند.
ترکیه امکانات محدودی برای آزمایش موشکی با برد ۶۰۰۰ کیلومتر دارد و ممکن است برای حل این مشکل به پایگاه فضایی مشترک با سومالی متکی شود.
موشک‌های بزرگ‌تر مانند چنک و ییلدریم‌خان امکان حمل چندین کلاهک، فریبنده‌ها و ابزارهای مقابله علیه پدافند موشکی را فراهم می‌کنند.
ترکیه در ۲۵ سال گذشته صنعت موشکی خود را به شدت گسترش داده و بسیاری از محصولاتش را صادر کرده است (چون مشمول محدودیت‌های ITAR آمریکا نیست). اما عضویت در رژیم کنترل فناوری موشکی (MTCR) صادرات ییلدریم‌خان را محدود می‌کند.
احتمالاً هدف اصلی، تقویت بازدارندگی متعارف دوربرد ترکیه است؛ به طوری که بتواند اهدافی تا پکن را تهدید کند. کلاهک سنگین آن قابلیت تخریب پناهگاه‌ها و اهداف گسترده را دارد.
فعلا هیچ نشانه‌ای از تلاش برای ساخت کلاهک هسته‌ای وجود ندارد، اما این ICBM می‌تواند سکوی پرتابی برای چنین قابلیتی در آینده باشد (مانند مورد کره جنوبی).
ییلدریم‌خان آخرین محصول تلاش گسترده تحقیق و توسعه ترکیه برای تقویت بازدارندگی ضربه عمیق متعارف خود است و نشان‌دهنده جاه‌طلبی‌های رو به رشد این کشور در حوزه هوافضا و موشکی است.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16139" target="_blank">📅 01:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکایی با اف-۵ !  این مقاله NBC News توضیح می‌دهد که در جریان حملات ایران به پایگاه‌های آمریکا در منطقه، زیرساخت‌ها، ساختمان‌ها و تجهیزات نظامی به شکل قابل‌توجهی آسیب دیده‌اند. برخلاف روایت‌های اولیه که این حملات را «محدود» یا «کنترل‌شده»…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16138" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ:   من تازه پاسخ نمایندگان به اصطلاح ایران را خواندم. از آن خوشم نمی‌آید — کاملاً غیرقابل قبول!   بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16137" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBnNUu8VGiM-Xztuy_WAfzgNr1X7Ek_FCraNj5K4V8B4gqJU38u0kZmcOuZKwoZCYwl3ycrVdOrssOBSmk8qezE2qgD9McpE5aOUJWqqhccJQYZOXI8lW2aTfbrJz861pn37zHDfsWN00rwbDSxRVG7IFogbW6vU7p4StSrPGCZn_cCSoinK0mBczn0EE-SV4w5_HnagnkEEkQUvBCAuAL2yZvwkOP4p670jNTDs_aNCX4S-WM5uQEZe2RvnKfDdcKf6UrUk5OuUMuJG0Qf-YPBNzVswAq6yg5n394WvMf-r7Z30Pv0Lscx54weQAbdCdUG-jXe0Hp4cnvnqjArr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طفلی شهباز بوگندو</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16136" target="_blank">📅 00:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16135">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMv0OLdlblbs9hrf31_79Wh2LMpAhNOzxFAh8UOFfHIa9Eh5rdM1bIke3Re1iudnRx4VtUEu4BUefhs7vVyoWf4al85salzN7Kt--Oyu_EeUK-OlChxygtQv4sCFTQLEVCSJYPVIHSWT8C3bHMLEtcn59zaFXrmsVxDlcyA98cc3tm_eOquwBbSCyelGL0pSoLWcBWphhdakfBLeSzlDV8kgjDnLRnYQnkjtAnfIiCZTI8Xyk7eTIo9-o-40SajkxOwdWey3eeOsm9IusjDBEWEFJkM-Q5GHjt16U0-eVae_XfbijwKwhCu4nU3yVjGvsnxcUj65mRD78rJqp1qQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16135" target="_blank">📅 00:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16134">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:
من تازه پاسخ نمایندگان به اصطلاح ایران را خواندم. از آن خوشم نمی‌آید — کاملاً غیرقابل قبول!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16134" target="_blank">📅 00:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کاخ سفید: آنها دیگر هرگز نخواهندخندید!</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16133" target="_blank">📅 23:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2b9O-itDHD10G4bIC3WNy_8xN13V4hiA0CJUujYL48zsDbfUsOnzCTQ_8qRZiLp9ZLuQHk_QODcUTWnaZ-MLA9vk1lgGQy6Qz1RZSb6CvpFsWW9iPH0njncyxk9eItSP25ylQxF2QA_Zsxn6Y9V5pYLybEQ8SivikbYyB-qrT-JveAm6Zl4W7OqoE67ttnUGcwzcRKAbpHmmvadhrI3VKHD6FCQD11PPGEfknjNWEfHnWMVBx53SKER52FHjrZ1Orex0vYngHLc2pBwm6yxRq7UHaoRmVsOAf-SCyvygWqlhicci8uLfLp4vyi_Z5Z6GIFZlnAOKOUXVmIunUFBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: آنها دیگر هرگز نخواهندخندید!</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16132" target="_blank">📅 23:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiORlv_96bZXRVigN7noGgDJM5vlZba0KkYYPufz2gMIz8HDogHIegty_lsuH-H8hdJMbCWsODWNRGMewcV_8Kn_wgJg-KgdVQWNqGnlX5FfDhnqIB4THJxzJ6Ag689OPwELGiDg61Ny0tS2bwnfdkofbJgcqpZwuljbxziEkLlawlvPldwFH5Zzh2f_MJq2-rqKPFtXNW1Qf7D_FWEk7UjWPEpsy5JcS4qtdHHxyoYWxI4Hm4FVOfLjnMhCdD_pkbFnUVEUOh191LzmA46gjxpY9qEmFudcksKhE3gF4NT94vBdCExMAQWaOjvb2q0Xk11BlzR7Qkk4rhJO4SEFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL
— W</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16131" target="_blank">📅 22:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tELugAd9HgnW47_OM6BkXixN3smqXW1dvP8KKqBtgjWOhYjcjXGRowPwSQhqJHAy2bv9tOwtSRIo2t86Ejo9Ri5KD_J0idTk5m8-CrT2EeTDy05CxO-qQlnOpN5B5qMWGL6j4y-6z7qF8l89eiv4-kmFj5L_df4XAYltiN6p-U8zps2GMXpimHHLZB7FQVbJL3wgAg7SOTIqIV7-5jnJPwuCvMPycR4EkIpquKArZfhSVdSojPLWEzVNJ4APIDeM1WNj_QNIxzGTkY3KIl6z8jR-7SZ8vh-9znVj6ZHi-L8VckCxf6xJEB5GYm82o2g5nObBURBSxVpznnFm1bfxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL — W  یادآوری....</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16130" target="_blank">📅 21:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16129">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR0kIABr1k7eKfZmgxYgNyWbFicJPTsuKCp9XiJh2wq0KdmPzyptmKvwkNKHEZ_hFNDH3j92sbKNxVr5LrFocCQOfCxMjPAyodhNp4DwVqNCBgo5PyKuY-5rc0shwWv8BXoGVcQ2MHKy6zrIpmOh4M4x9QSq5AUnmJZmArghVGBlrWq3T5A9q7XSInwwHWaOzmZmfvURWFmKHK-izshUDlURhZGdIOVKKnHDnWgx7Wy3ql7ZK2_ovbaL72bVfLkmxAVuVudRUqRsKfIc0Q0szTBPkMQNtcqaX6_mIJDhiPdEhGk0zC-CAXGY4Otn9TK9LGjI0Nplbg4RqAK0Kj8P3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Total — W  با کوین وارش، کوره پولسوزی عظیمی در حال تدارک است.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16129" target="_blank">📅 21:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دقت کنید که بارها اینجا گفته ایم ترامپ یک «رالی مدیریت شده» (Managed Rally) در بهای جهانی نفت می خواهد و نه یک رالی پارابولیک دیوانه وار.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16128" target="_blank">📅 21:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmE_NvLtnjNcYcTlxxxg-1sKMy3XVz-ZjNQkjivq2r_3Z-gVtRUM6GG_Van529aYCkqv_QQ-kgtNld90fUkaTiQfNIz6GuLIqhelec_pHHC2067fI8sJdRm8OcUYOQcbsP2ItobhISJLRYoXbbeUWHG1vMKc8gEt8KBGdd9z3HRWqkE0d145jRRTNlKKIQYEOczpRScx6sw3ZYpYtP_ZK1XqBW2s89jGQcqeR-VhJYKT7fSqb56ZedxzTlXt0Kcgt03XXUmylyC54AkZimj1Vh59H_SbX-vbd3t3GFEjfbFoXqc28l4X0mvykHX-McOqLKu8Nu5hr5I-Myj4JPFgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ثروت شخصی ترامپ به سطح 6.5 میلیارد دلار!</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16127" target="_blank">📅 21:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚙️
طاهری ؛ عضو کمیسیون صنایع و معادن مجلس
:
اگر ۴۰۰۰ میلیارد تومان هزینه کنیم ، می‌توانیم کیفیت ایتا را در حد واتساپ ارتقا دهیم</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16126" target="_blank">📅 20:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:
ما به ۷۰ درصد از اهداف در ایران ضربه زدیم و می‌توانیم به مدت دو هفته دیگر ادامه دهیم.
حتی اگر حمله نکنیم، بازسازی توانایی‌های آن‌ها سال‌ها طول خواهد کشید.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16125" target="_blank">📅 20:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو: جنگ تمام نشده است
هنوز مواد هسته‌ای و اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی‌ هستند که باید برچیده شوند. هنوز گروه‌های نیابتی وجود دارند که ایران از آنها حمایت می‌کند.
همچنین موشک‌های بالستیکی وجود دارند که علیرغم نابودی بخش زیادیشان، آنها همچنان خواهان تولیدشان هستند.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16124" target="_blank">📅 18:55 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔸
نیویورک تایمز :
به دستور رئیس امارات ، اخراج گسترده کارگران پاکستانی ، در پاسخ به میانجیگری پاکستان میان تهران و واشنگتن کلید خورده است</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16123" target="_blank">📅 16:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16122" target="_blank">📅 15:29 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نخستین جلسه وبیناری مجلس شورای اسلامی پس از جنگ</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16121" target="_blank">📅 15:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE_Vlp7vJjAFn9hS8XCeqSmkG7YVq75xJj6ZmZrorFNrieHSEy5fYk9VdS58mGPgsqGrEUmVTfjRMeyYda_G10uYR9F8W0mKmN1eQ930z0ZpalWHPw9A_aq6pZRWPaJ94Y87tIQGCu45O19Urf9gcZ9c5SSYqVUAa82FdaJDLDLe5auNfWRnv6lbAjujqVqkA_2Ei23HafwkcmguOPSh9sdbVsJpcyBZ3a6CBuNfr-PjFlNFIt_WxP2VJT7-mtjxkn9IBbTkTyrxzFUMIvJnh7llcp2si8ru_jYAcXZxtDL9zFyztEBkGfJ9ntk72WKImHLIVtkPOjRO7HUG4ATzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین جلسه وبیناری مجلس شورای اسلامی پس از جنگ</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16120" target="_blank">📅 15:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16119">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e1803338.mp4?token=cFDzGUHcrA9KiN0jwecjpHYoEk9Edkz0iayE9R76vw1VZJH1bBOqHKGwPQiOE88d09A0V230V0VOwThsPLtEWzA9khXWNtZdBqVuh55z-W8JwzAviFuacZqBEh8EjiSd5nLrURZf_6eUAj70KWowuKtnMqLLSpjidCFrzX8JdlYXftf28Q3Vwj8TavcyQ-qbJLOFzfHHeLWq9hlzXuNvERl3Yn7W6bzRQDY6Gf8rS8-Tz5e42Qg6h1cJLwRHSpuCaBuKmWCLW8mLaBFIE8pQzf7dn6ru_A-P3S6VrZ3s7d3hP0UPSVBScn-hOAucQq7lhM39csVVl3D9g0b2JCYU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e1803338.mp4?token=cFDzGUHcrA9KiN0jwecjpHYoEk9Edkz0iayE9R76vw1VZJH1bBOqHKGwPQiOE88d09A0V230V0VOwThsPLtEWzA9khXWNtZdBqVuh55z-W8JwzAviFuacZqBEh8EjiSd5nLrURZf_6eUAj70KWowuKtnMqLLSpjidCFrzX8JdlYXftf28Q3Vwj8TavcyQ-qbJLOFzfHHeLWq9hlzXuNvERl3Yn7W6bzRQDY6Gf8rS8-Tz5e42Qg6h1cJLwRHSpuCaBuKmWCLW8mLaBFIE8pQzf7dn6ru_A-P3S6VrZ3s7d3hP0UPSVBScn-hOAucQq7lhM39csVVl3D9g0b2JCYU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16119" target="_blank">📅 15:13 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foF--P3YqWvH2ra7bPQNIetltH9B_QrpDSFWe1sCs2w3clNIt3sZK3FMZEbyqBeI3duGDG_SNA0meunHqaWkwsOdPeiZlMcBXTSNy9K_7m6AlnmHny6kLD7qNBFqE97LLy_Fqzg2kjZVjQPNfqCOLQzyT1Vkh_xQRo8jjz7R9AmEpQGaJ6wS3iNY16_YLRVLmcNn8shCfFhPQ50Ud7Fi_bR5qQ3jtuJjTyvRHPiBPDZj5Eve6SiLvVVHzzaBgZAUXFmLB0wlHvtdEqTR2GKlCESfDPnlM7TcCKq4tLJAn9kKjvp22Nxia25ux3pk2vfL3MgPTpCDl6m5E0-hir98VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه اش بازی های ترامپ است تا دستش باز بماند برای دستکاری بازارها</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16118" target="_blank">📅 15:13 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فوری/ امارات: با دو پهپاد هدف قرار گرفتیم!</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16117" target="_blank">📅 14:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروهای مسلح کویت بامداد یکشنبه «تعدادی پهپاد متخاصم» را در حریم هوایی این کشور شناسایی و «طبق رویه‌های مصوب با آنها برخورد کردند»</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16116" target="_blank">📅 13:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بزرگ‌ترین شرکت نفتی جهان،  آرامکو، گزارش داد که در سه‌ماهه اول سال ۲۰۲۶ با وجود جنگ ایران، سود بیشتری کسب کرده است.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16115" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کشتی باربری در نزدیکی سواحل قطر توسط «پرتابه‌ای ناشناس» مورد اصابت قرار گرفت
خبرگزاری تسنیم گزارش داد که این کشتی «پرچم آمریکا را داشت و متعلق به این دولت تروریستی است»</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16114" target="_blank">📅 11:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16113" target="_blank">📅 11:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🛩️
دقایقی قبل یک جنگنده متعلق به ارتش ایالات متحده آمریکا با مخابره کد 7700 بر فراز دریای عمان اعلام وضیعت اضطراری کرد</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16112" target="_blank">📅 11:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرمانده نیروی دریایی ایران: «زیردریایی‌های ما کشتی‌های دشمن را رصد می‌کنند»</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16111" target="_blank">📅 11:29 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔖
بازگشت مسترکارت و ویزا کارت به سوریه پس از ۱۵ سال</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16110" target="_blank">📅 11:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIbcsNQN7CpIK8aHWKrGr8AG21Wum-hg0AQCjILZF1KD3_HWV4_t5tKHrNB5S6tZN5DB8-Oykp22_SLQSdQdypE7VnUC9B2c-hFR6QYPegpqufWSZwkHUqQetvygI_sqk95QtfCPpcV4UKuUK1XsqaF2NS8eRnuznx4W32WzTRDRWa-zUc73dSNc1riDsmJQNkmNezUL-NiNF_hmHL1fJLwYO-MAX_1QsO2mxzHVY4oTvvUb-y3Rnih0Sg0HU5lj5MhOkB8tIuTGJnsrPTxCdUt_a30rXq6RvulUKgzt8C7T3ptgOGDotCdLeXpA2zY5bZwWPILRy0etuRkE-OcrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تشدید نگرانی گلدمن ساکس از کمبود عرضه نفت
کاهش سریع ذخایر جهانی نفت و محصولات پالایش‌شده باعث افزایش نگرانی‌ها درباره احتمال کمبود عرضه در بازارهای انرژی شده است.
گلدمن ساکس هشدار داده تمرکز ذخایر در چین و آمریکا و محدودیت‌های صادراتی، ریسک کمبود سوخت در اروپا و آسیا را افزایش داده است.
🔗
ادامه یادداشت را از اینجا بخوایند!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16109" target="_blank">📅 11:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI4xCXMqwA8-68upX94s667ur89Al3jQP57mhBczEGXyn3BqnaL1bbIMJ5kCa6me35SGO2Qjq5WhnFgoqVn4QL-OsKmdNoP-lMGzdZNkhX-6QH1RpooPOem20GOTEKtJv4VjXwxd42wob5K_voRjEzAcvb_FPdUhY81WFm8BimLomYXtKRRmV62hLZZWv9_K9aDQy10KsD-Os749yFc1FcJnhMIvCoC-NUsR8zUu5dci1LVsMxfyww6RynOpCAIiLawJ6ppCP_9eWvJjnPrNs2q97H9PdiAVtgBnQk0QAzFAMD0EqKUHJbT44Nv7cdMBSpKXU-LckbDMMPSfeIGTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!
تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.
به گفته افراد آگاه، اسرائیل این تأسیسات را که محل استقرار نیروهای ویژه بود و به عنوان یک قطب لجستیکی برای نیروی هوایی اسرائیل عمل می‌کرد، درست قبل از شروع جنگ با اطلاع ایالات متحده ساخت.
تیم‌های جستجو و نجات در آنجا مستقر شدند تا در صورت سقوط خلبانان اسرائیلی، به کمک آنها بشتابند. هیچ تیمی در آنجا مستقر نشده است. یکی از این افراد گفت، هنگامی که یک جنگنده جت F-15 آمریکایی در نزدیکی اصفهان، ایران، سرنگون شد، اسرائیلی‌ها پیشنهاد کمک دادند، اما نیروهای آمریکایی خودشان دو خلبان را نجات دادند. اسرائیل برای کمک به حفاظت از عملیات، حملات هوایی انجام داد.
پایگاه اسرائیلی تقریباً در اوایل ماه مارس کشف شد. رسانه‌های دولتی عراق اعلام کردند که یک چوپان محلی از فعالیت‌های نظامی غیرمعمول در منطقه، از جمله پروازهای بالگرد، خبر داده بود و ارتش عراق نیروهایی را برای تحقیق اعزام کرده بود. یکی از افراد آگاه به این موضوع گفت که اسرائیل با حملات هوایی آنها را در تنگنا قرار داد. ارتش اسرائیل از اظهار نظر خودداری کرد. دولت عراق در آن زمان این حمله را که منجر به کشته شدن یک سرباز عراقی شد، محکوم کرد.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16108" target="_blank">📅 09:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هم به مسدود کردن کامل تنگه افتخار می‌کنند هم از تنگه بسته میخواهند روزی ۱۴۰ میلیون دلار درآمد داشته باشند!</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16107" target="_blank">📅 08:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آیا میدانستید پیش از جنگ اخیر، ایران با داشتن دستکم 42 سوپرتانکر غول پیکر (VLCC) جزو 5 کشور برتر دارنده بزرگترین ناوگان نفتکش دنیا بود؟</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16106" target="_blank">📅 06:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تحلیل‌های ژنتیکی جمعیت نشان داد که لی کی‌یونگ دارای آمیختگی ژنتیکی تقریباً متوازن بوده است:
۵۳.۴ درصد خاستگاه آسیای شمال شرقی باستانی
۴۶.۶ درصد خاستگاه استپ غربی
علاوه بر این، او دارای خط نیای پدری اوراسیای غربی و خط نیای مادری استپهای شرقی بوده است.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16105" target="_blank">📅 02:40 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx5EDMt5T9PvKD7rhLyptarcqIy3sUHkFkfxSBgg5Xucjndj9_C-dj3V7XkoLu9WSQMXtJTTkIocYjLJBCs_MRQl_ebbENwCES4UlpqCh146GRn4bm8e-gqwhRfnRCAtGZdBXCt0-H1kJI-_9eJAQHG4IYXGq0PUsqg53LjEg1IYMIAKC5WE5fY_hZvHuS4yBHHkeq-C5ShJ6XGSmpmPfJp_G-QjSIDtz-OT3f2E0HjE2I2Qw3LK83tytLO-Ve2l5St_0nPO70vbpJQ20qrFuDesIBDv1eflSyIdxP2g6ZzUZVU61gg25SigrjmZ7sINPzxrue8rDTeJ9A5BZIKvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین کابوس ترک گرایان در ترکیه: آزمایش های ژنتیکی! - بخش 1    مقدمه  موضوع اجداد ژنتیکی به موضوعی بحث برانگیز در میان ملی گرایان افراطی ترکیه تبدیل شده است، زیرا مطالعات اخیر روایت های ملی گرای دیرینه درباره ترکیب قومی ترکیه مدرن را به چالش کشیده است.…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16104" target="_blank">📅 02:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟢
تشریح ساختار و مواضع فدرال رزرو
✔️
بانک‌های مرکزی در هر کشور، به‌واسطه اختیارات قانونی اعطا شده از سوی نظام حقوقی، نقشی تعیین‌کننده در هدایت اقتصاد و شکل‌دهی به انتظارات فعالان بازار دارند. در این میان، Federal Reserve System به‌عنوان بانک مرکزی ایالات متحده،…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16102" target="_blank">📅 01:42 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

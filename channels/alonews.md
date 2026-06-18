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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-128976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده‌های جدید نشان می‌دهد که ترافیک دریایی از طریق تنگه هرمز پس از تفاهم‌نامه ایران و آمریکا از سر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/alonews/128976" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128975">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_A0IWcGsQeVC4a0rqSG2aZ4oEPECQAGatgLQedTLerviliybBlfOZspu8KBuFzeDUQ5yLZoQkyPbfk0WA9VzKN7ByMweVxK0OGOl4HCiPloNm-9a4PDxBHlcAUskqaGMXx1Uhn0aoVGE2PNFMNfwhD1yn-JS83a5t_CHfjRu_eUvS01h3csbW3OS8e3lsJ_P4d7OVRnhIFD5NuZomOBkuqeavSS-U2T2Vv58i7Bt6GT8ckY049RLElFuhCLDJlWbCG-RMQTS1f4UD255PjOw3_bvu4j22LTf1UcsQxu7Cz1bC1mEmltn9QYINqBjC-B2Puz2rdwl9KRFkAnQXAN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس:  پیام جدید رهبری منتشر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/128975" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128974">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-51rL8JuYNVdAf3hkPFi3e4pDuSsLoDcdDv3TTxpEu1GkJ7yAJqsmZgb0law4b1bBFnik7MRJLYKBe19-V16Ld2UoYqZ0Yu0loGEfT0Gahlfx48OZCbok8SdVVQ35q7hmIKK7cTQZOJyPd6sLXEeZqbSCydUJWJlHtDI_hsdfN9Hd9AiVnb3kFRJW_t3tjCznaGDTAx-iLMfVDGWSl2OrdF-4x4gJPTFdPfs04iZgYs9UkxVlpYVFSW_C3kzRYxls-WIZ23MhdsniuOZIOkPCdtSAPGC9khHVx4eUpjko9Tzw5yammNee8RCJFryNJNsC7YpgtgxXocp1XuXCweYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین به زیر ۶۳,۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/128974" target="_blank">📅 21:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128973">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فایننشال‌تایمز: طبق توافق آمریکا و ایران، ایران به تدریج به ۶ میلیارد دلار از دارایی‌های مسدود شده خود در قطر دسترسی پیدا خواهد کرد
🔴
این پول فقط می‌تواند برای خرید کالاهای بشردوستانه و سایر کالاهای آمریکایی غیرتحریمی استفاده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128973" target="_blank">📅 20:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
خبرنگار : چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی.دی ونس : تمایل زیادی از سوی جهان عرب و همچنین از خارج از جهان عرب وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/128972" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128971">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128971" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128970">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
جی دی ونس: نتانیاهو بهتر است بداند بدون ترامپ و آمریکا قدرتی ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128970" target="_blank">📅 20:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128969">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ونس: تعداد نیرو‌های آمریکا در خاورمیانه را به سطح پیش از درگیری باز می‌گردانیم
🔴
برنامه ما این است که به سوئیس برویم؛ دقیقاً نمی‌دانم چه زمانی
🔴
درباره تأمین مالی صندوق ۳۰۰ میلیارد دلاری، تمایل زیادی در جهان عرب و خارج از آن وجود دارد که درگیر سرمایه‌گذاری در ایران شوند
🔴
در سه ماه گذشته، دو سوم تسلیحاتی که از اسرائیل محافظت کرده‌اند، با پول مردم آمریکا تأمین شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128969" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128968">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا تحریم های جدیدی را علیه حزب الله اعمال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128968" target="_blank">📅 20:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128967">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8DOvv5KboeYqXG9q-Q166BDF26lMQ72vaYC-Om7xOEqvoN4ni4WE35qkigFdVhdi1VMj4UhjiYdPxhQ81Gj7Y7tHpX5-_NB_RSyr-1NUcMNLcMxfwPB4qoyrfVVl7jC4-y_KAuxXVPT6qPABx_K98_iZE-dl-suN1A9T0XsmCS-EvaITanIcyu9fS_cbFze9frrYwrp0k5oIAOKLC9AQfnqruMCR8wGVdkvzQ9g43Mi3oxIvSFebIGX450nwv8UMOOfa94Zbz_vX-E0Ff-taEpou9TfbFxqtV-57Jh9FaQPyjAZzKADnHDVZMvrGMtxle1FlZp6fZrEM_Jdif8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سنتکام : امروز، نیروهای آمریکایی بر اساس دستور رئیس‌جمهور، محاصره دریایی تمام ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128967" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128966">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نرخ دیه سال ۱۴۰۵ اعلام شد!
🔴
رئیس قوه قضائیه با صدور بخشنامه‌ای، مبلغ دیه کامل در ماه‌های غیرحرام را برای سال ۱۴۰۵ تعیین کرد.
🔴
بر اساس این بخشنامه که در اجرای ماده ۵۴۹ قانون مجازات اسلامی مصوب سال ۱۳۹۲ و پس از انجام بررسی‌های لازم صادر شده است، مبلغ دیه کامل از ابتدای سال ۱۴۰۵ در ماه‌های غیرحرام، ۲۱ میلیارد ریال تعیین شده است.
🔴
این بخشنامه از سوی رئیس قوه قضائیه به مراجع قضایی سراسر کشور ابلاغ شده و از ابتدای سال ۱۴۰۵ ملاک محاسبه دیه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128966" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128965">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le5y6NkIsyEHLWJCmPamzajrRTleSud9pGV_Tw1mPryWH9rIvYIituPoNfZLQR7MuG0t2biwAsmQoRv6OkQU3y4rpneK6umO3yamjmNigK8irbqL-Krpvv27-phEmSqGtbVLL4c4kNlWkycmSrHC7BZP0Z-_ZD5MW4tjv7CFjsQIqwE-HWzdVZpcAuGjzsCGWQD2_B_oficPHku_V0cU_gvjB_polmaXCl7Ainn21aEhOOSLT8RF2w9CbPbu65GouBsoDfptNUQabDXhBGfivlOHz_FC4WUMQipKBh-LH6Pqe5NOaEdOLW8qkLlG5A8IeCxftqDcZIpWpM5RmVRsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران وجود ندارد. این اخبار جعلی است! همه چیزی که آمریکا دارد، موفقیت، کاهش قیمت نفت و پیروزی است. به بازار بورس نگاه کنید. تبلیغات دموکراتیک در حال اجرا است!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128965" target="_blank">📅 20:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128964">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ونس : من تنها کسی در کابینه هستم که نمی‌توانم اخراج شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128964" target="_blank">📅 20:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128963">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
من معمولاً نسبت به درگیری‌های نظامی بی‌پایان بسیار بدبین هستم.
🔴
فکر می‌کنم این مورد متفاوت بود چون واقعاً هدف مشخص و پایان روشنی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128963" target="_blank">📅 20:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128962">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: ایرانی‌ها پیشنهاداتی ارائه می‌دهند که حتی شش ماه پیش هم در حد رویا بود. پس بیایید این مذاکره را ادامه دهیم.
🔴
ببینیم آیا اقدامات ایرانی‌ها واقعاً با گفته‌هایشان مطابقت دارد و کمی به ایالات متحده آمریکا اعتبار بدهیم، کشوری که به نظر من مدت‌هاست شریک فوق‌العاده‌ای برای دولت اسرائیل بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128962" target="_blank">📅 20:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ونس: مقدار دقیق دارایی‌های مسدودشدۀ ایران را نمی‌دانم
🔴
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. حتی اعدادی بیش از ۲۰۰ میلیارد دلار.
🔴
بخش عمدۀ این پول در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در کشورهای حاشیه خلیج فارس است، یا در اروپا، یا در جاهای دیگر.
🔴
اما مقدار دقیق این پول را نمی‌دانم؛ فقط می‌دانم که رقم بسیار بزرگی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128961" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از یک‌ مخالف توافق بعد امضا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/128960" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ونس: امکان تعلیق موقت تحریم‌های ایران بدون مصوبه کنگره وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/128959" target="_blank">📅 20:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ونس درباره نتانیاهو: من گزارش Axios را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128958" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اننقاد تند جی. دی. ونس به بن‌گویر و اسموتریچ: شما افرادی را در ساختار سیاسی اسرائیل دیده‌اید، بن‌گویر و اسموتریچ، که به این توافق حمله کرده‌اند.
🔴
و فکر می‌کنم پاسخ من به آن‌ها این خواهد بود: پیشنهاد دقیق شما چیست؟
🔴
شما کشوری با ۹ میلیون نفر جمعیت هستید. نمی‌توانید صرفاً با کشتن، از پسِ حل تک‌تک مشکلات امنیت ملی‌تان برآیید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128957" target="_blank">📅 20:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فارس: پیام بسیار مهم رهبر انقلاب دربارهٔ تفاهم پایان جنگ، خطاب به مردم ایران، تا ساعتی دیگه منتشر میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128956" target="_blank">📅 20:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=IkK7YY7lhTwqOZTNemISRjZPmqV6SeLRykhi54cpjxrxypMN3cy9Hr1DEOJILJzr2WWlMGN6EBhS8BiCs0FMZvmXWYvPsGbBqZ1TzTOcc2A4mKhOZoUsPfdk_n1PrrVtUVejyk8o4SftcrV0XVbDyLNoLNVo2KWKTsAQtpVq_Smw8CoWZ1e0eNBqlQJFjJPMy85HnSzDc-twrOF57Z7iXpeGv_rmow7wIoXI4nOuNShPpy3osGwJWyT-P-soICYyh3bBSqheBCgCA3_OZgUUi_BeUK4S6-UpH3r8-vSA4FT0SinzBdauwqIYG5L1vABZwP5xrGTKorrOtEOIjj03dKO7px7ySbns90dFQgmD6gHYPWaJsPfmFJF2mPNQapirydy_JVP-S9uyQgxXkKquGnorgu53f-MSKqixUYZaQ2wnpe8Xu_izCePNRXA3W6_Bw89FKWFcETT8iK5509J0B5-fzB2h_0O7XRHK3M1tzby6aYuFhKIPXgVonr_KE0AJz1I0M9Dy3-ZwCpDM7DIIsCyfhzxMSfUM4YfQJZcCkW6JoQhA_MUe1hx2PB2GFjvrXhqeEqWsG_w82DiifXP-6qnnX2LEDBeYtQYqqBeHGowgL1GuidDzjBjJvZrN6xPmSWspI0HB0alNOeaulU3FGZwV_7hdQN8aJrsBFvjXt5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=IkK7YY7lhTwqOZTNemISRjZPmqV6SeLRykhi54cpjxrxypMN3cy9Hr1DEOJILJzr2WWlMGN6EBhS8BiCs0FMZvmXWYvPsGbBqZ1TzTOcc2A4mKhOZoUsPfdk_n1PrrVtUVejyk8o4SftcrV0XVbDyLNoLNVo2KWKTsAQtpVq_Smw8CoWZ1e0eNBqlQJFjJPMy85HnSzDc-twrOF57Z7iXpeGv_rmow7wIoXI4nOuNShPpy3osGwJWyT-P-soICYyh3bBSqheBCgCA3_OZgUUi_BeUK4S6-UpH3r8-vSA4FT0SinzBdauwqIYG5L1vABZwP5xrGTKorrOtEOIjj03dKO7px7ySbns90dFQgmD6gHYPWaJsPfmFJF2mPNQapirydy_JVP-S9uyQgxXkKquGnorgu53f-MSKqixUYZaQ2wnpe8Xu_izCePNRXA3W6_Bw89FKWFcETT8iK5509J0B5-fzB2h_0O7XRHK3M1tzby6aYuFhKIPXgVonr_KE0AJz1I0M9Dy3-ZwCpDM7DIIsCyfhzxMSfUM4YfQJZcCkW6JoQhA_MUe1hx2PB2GFjvrXhqeEqWsG_w82DiifXP-6qnnX2LEDBeYtQYqqBeHGowgL1GuidDzjBjJvZrN6xPmSWspI0HB0alNOeaulU3FGZwV_7hdQN8aJrsBFvjXt5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد ونس به اسرائیل
🔴
ونس : در سه ماه گذشته، دو سوم از جنگ‌افزارهای دفاعی که از اسرائیل محافظت کرده، با دستان آمریکایی ساخته شده و با دلارهای مالیات‌دهندگان آمریکایی پرداخت شده است.مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیتی را که آن کشور در آن قرار دارد، حس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/128955" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=t2Dkk6d3HsnMsjeeSRNJcxEAHYUIKIbq-UjHkOdH3zM3XfhEO5diixwF0FS-nM6Y6ZZhSx1kVdZDEGVEp8x4BPVe669-V9CvGKr4vrhfmwQjpPDcrzljFF-AOYbRiBHQQBBz_aCKelMjTUUEBLpNKwdSegeKfbcYYLxFlyCitISpndFBF8_QyXVt4P_GcOJNtRBUApzA978b3Fm3byqqnECCNKfjK4af9wi1tjKyFQkIKKHvveWodHqHhabMmaTgp4kNHIQxVC2f_K2pB-fgSVwOQU4hZ4jvIccl8GDVq3zW6UNUtt3d13wb2J4hinoJFyLZkfADQCF-vuFC-hDEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=t2Dkk6d3HsnMsjeeSRNJcxEAHYUIKIbq-UjHkOdH3zM3XfhEO5diixwF0FS-nM6Y6ZZhSx1kVdZDEGVEp8x4BPVe669-V9CvGKr4vrhfmwQjpPDcrzljFF-AOYbRiBHQQBBz_aCKelMjTUUEBLpNKwdSegeKfbcYYLxFlyCitISpndFBF8_QyXVt4P_GcOJNtRBUApzA978b3Fm3byqqnECCNKfjK4af9wi1tjKyFQkIKKHvveWodHqHhabMmaTgp4kNHIQxVC2f_K2pB-fgSVwOQU4hZ4jvIccl8GDVq3zW6UNUtt3d13wb2J4hinoJFyLZkfADQCF-vuFC-hDEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چه کسی آن صندوق 300 میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی‌دی ونس: تمایل زیادی از سوی جهان عرب و فراتر از جهان عرب وجود دارد که اگر ایران به‌درستی رفتار کند، واقعاً در آن کشور مشارکت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128954" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
جی دی ونس: ما یکشنبه با ایران توافق را امضا کردیم اما نمیدانم به چه علت، ایرانی ها از ما خواستند که تا روز جمعه متن آن منتشر نشود البته شاید به خاطر تهیه یک متن فارسی
🔴
اقتصاد ایران رو به فروپاشی است و تورم آن سر به فلک کشیده است و یک هزار میلیارد از جنگ آسیب دیده بنابراین فروش چند میلیون بشکه نفت نمیتواند تاثیر خاصی داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128953" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=T0szU5E8XsVrxxoH9ruHw9u43qlR2MO1tJNERZxO15FQColB66ckMwIwGFWfZKOEepZaaPK7OVN0sgzivBgvjFwf12ykXl-pYC4H07ZtAefEEI7w7Wre-oA9MCUIbHZFdxel2cgVAsagMYQ0JNJdyE9ebkfJaJV42nCASU2m1KiN6_2OZbLYKWf06zkUI6z8-I2S8QgHcZr8fqvkU-2HwF-QDPaXWg3sdNqPKmsG_a3HOHCwXR-xCkVY0kk1gnynq5G1e9kfb0OvsRsT7cZ5qGGvGUyuQJRn1xcxCNWrwtJbZMkoARX2jWhFWbnVoPm_AV_IbJ6gVVpb3LvSzqatdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=T0szU5E8XsVrxxoH9ruHw9u43qlR2MO1tJNERZxO15FQColB66ckMwIwGFWfZKOEepZaaPK7OVN0sgzivBgvjFwf12ykXl-pYC4H07ZtAefEEI7w7Wre-oA9MCUIbHZFdxel2cgVAsagMYQ0JNJdyE9ebkfJaJV42nCASU2m1KiN6_2OZbLYKWf06zkUI6z8-I2S8QgHcZr8fqvkU-2HwF-QDPaXWg3sdNqPKmsG_a3HOHCwXR-xCkVY0kk1gnynq5G1e9kfb0OvsRsT7cZ5qGGvGUyuQJRn1xcxCNWrwtJbZMkoARX2jWhFWbnVoPm_AV_IbJ6gVVpb3LvSzqatdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ چند روز دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128952" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جی دی ونس در مورد اسرائیل: به نظر می‌رسد که ما درست در آستانهٔ یک پیشرفت بزرگ در توافق بودیم، و بعد ناگهان یک انفجار بزرگ در یک منطقهٔ غیرنظامی در بیروت رخ می‌دهد، و تعداد زیادی از مردم که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128951" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdKwIAUh8rDAe9k1Q-m_p0hM20ZYAVX84eymA3U571Y8r4BN0hnvfytE3bz6U_qeJNDBgH9PGjEah1QdmmWBKK-IkCHgJCseoZXij72F4xOg_wlBUaXsScdMJ-3Uh9SiIFY5xVlPYwijtv2_BiwTsdMvmhRtbmmlY_ib_p3BpZievo8u00rRT8FnmcMdHryQ2jYH0OgCGr-AdL3kKACZDrIIJYF38ZCd-6RzgHrxUzv5brT5FtvaqjNxRik8799OR3WR1QzMLb_olVo6XAfY6x8B6dfQjOiIPsl8_GiXuvjQeCttHyZtlxk4BlogyPP5S6UuiHGLrf8O3klhRJ03D1mlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdKwIAUh8rDAe9k1Q-m_p0hM20ZYAVX84eymA3U571Y8r4BN0hnvfytE3bz6U_qeJNDBgH9PGjEah1QdmmWBKK-IkCHgJCseoZXij72F4xOg_wlBUaXsScdMJ-3Uh9SiIFY5xVlPYwijtv2_BiwTsdMvmhRtbmmlY_ib_p3BpZievo8u00rRT8FnmcMdHryQ2jYH0OgCGr-AdL3kKACZDrIIJYF38ZCd-6RzgHrxUzv5brT5FtvaqjNxRik8799OR3WR1QzMLb_olVo6XAfY6x8B6dfQjOiIPsl8_GiXuvjQeCttHyZtlxk4BlogyPP5S6UuiHGLrf8O3klhRJ03D1mlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
🔴
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
🔴
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
🔴
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128950" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جی‌دی ونس درباره لبنان: ما انتظار داریم حزب‌الله راکت‌ها و پهپادهایی به سمت اسرائیلی‌ها شلیک نکند و همچنین انتظار داریم اسرائیلی‌ها در لبنان به شدت عمل نکنند.
🔴
هر دو طرف باید به تعهدات خود پایبند باشند.
🔴
همان‌طور که می‌دانید، گاهی این آتش‌بس‌ها کمی پیچیده هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128949" target="_blank">📅 19:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=ac_Kv4ePSkNWp7gDfRjOAr4llloEVl6PdyXlULui5qA2sozyzS2kpPuzcuRzOmRb-2lJCfgt0T4MaUPPWXb2noECmYleL9SiiWZQyjh88P8SHCZx4T2F90X4p0WQiYXKu2CjHrG35OdXmCJlGlanzd9e5Ln1kMdYjdi718gDxRcQdghl0PoNoXnnHLUbMMskXqKZYVyW_ramcrSrYw_W6Eq1DPC_XX9Zl-PJtJYlPyFhwh-OgkI93ThyoKDU1jTivXcQJtPxPX6xrA8AmEoZL3m_m1uYki-wxUqI2oRiaDlspOk3w57osomhwfEQcpkdFJiOfsY26CmmG9CaxziGe6_UmOg7kbcLMf1QqlwqwyGmxvXx3TLnz-cg33Jn5dynFfHSzcYsaA7ro2UugMEm3X7VfsHdeF0p6jeq68mhomUAiAXXTMsMmO-SGBxXtdwr2kEoU4wxLXCU4SME8rEAh9TnZgJTi4IgmCotOekE5kGIiiTxrsSxeBoK134HuWOeadSRaAPnGiv1Dur3oZteNarv2fMB3monuoxqyBfKZQ8ZuW8aq-XDllvgJJPTo8aTaPStNlCGk_t-W9iiiO8x0SeEuTzH9ww_2W0d4LzPcV6FOHwJ1u32SLWqZOPh_IPPm0k0fBa_940HjAO3U5yPb1F2_IpDFVoQRq1MwxSOmEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=ac_Kv4ePSkNWp7gDfRjOAr4llloEVl6PdyXlULui5qA2sozyzS2kpPuzcuRzOmRb-2lJCfgt0T4MaUPPWXb2noECmYleL9SiiWZQyjh88P8SHCZx4T2F90X4p0WQiYXKu2CjHrG35OdXmCJlGlanzd9e5Ln1kMdYjdi718gDxRcQdghl0PoNoXnnHLUbMMskXqKZYVyW_ramcrSrYw_W6Eq1DPC_XX9Zl-PJtJYlPyFhwh-OgkI93ThyoKDU1jTivXcQJtPxPX6xrA8AmEoZL3m_m1uYki-wxUqI2oRiaDlspOk3w57osomhwfEQcpkdFJiOfsY26CmmG9CaxziGe6_UmOg7kbcLMf1QqlwqwyGmxvXx3TLnz-cg33Jn5dynFfHSzcYsaA7ro2UugMEm3X7VfsHdeF0p6jeq68mhomUAiAXXTMsMmO-SGBxXtdwr2kEoU4wxLXCU4SME8rEAh9TnZgJTi4IgmCotOekE5kGIiiTxrsSxeBoK134HuWOeadSRaAPnGiv1Dur3oZteNarv2fMB3monuoxqyBfKZQ8ZuW8aq-XDllvgJJPTo8aTaPStNlCGk_t-W9iiiO8x0SeEuTzH9ww_2W0d4LzPcV6FOHwJ1u32SLWqZOPh_IPPm0k0fBa_940HjAO3U5yPb1F2_IpDFVoQRq1MwxSOmEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او بخواهد شما را قربانی کند؟
🔴
جِی‌دی ونس: نه، اصلاً. منظورم این است که فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب اوقات این کار را می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128948" target="_blank">📅 19:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
جی‌دی ونس از "حق دفاع از خود" و حق داشتن موشک‌های بالستیک ایران حمایت می‌کند: «اسرائیل اگر حزب‌الله به سمت اسرائیل موشک یا پهپاد شلیک کند، از حق دفاع از خود دست نمی‌کشد. ایرانی‌ها هم از حق دفاع از خود در کشورشان دست نمی‌کشند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128947" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من می‌گویم دوره ۶۰ روزه رسماً امروز آغاز شده است.
🔴
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128946" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران
:
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی که می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
🔴
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ یک از مزایای این معامله را دریافت نمی‌کنند. اما آیا ارزش امتحان کردن ندارد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128945" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=bDyjoVCopxkqbl9GaelHyZBfd0N_OgMRcvpm1M-TvBYqF1yIiDwia-gaFDOOUhQT_96Vy_O1UOlhC0XnLuKeBQr7DwHRDyo2aWqGyw4QXKp1fdSvptBL0N7HzAbYy73ddhpTrH4UzE5WX1NYOOfJLnDsdqudOcdTLQtvv5lHQJUOxoRqq4bWuvY_GMj_aCxfMFQQW4m0KZmWG-58XX3OaR5c0RbrpoUHrvBMUHs5M7kCT5SWkqsmW5Bwr2OJTCBtXGSS6WBPwG7HwMELG2IthrD2R2WVLE5ik8gxwFpoeDLhirXEkeGtAICNIbIpIM89hgF8efhLOQTxf14MU0s6b40DFCp8xDVFYYFry818Cwt8hGLefHAchSTQ7tQGCe37V34CnJoYalPlW4glUo2Z5aDbNc86TWFrxliPOqRiPEGn4JTgLVMN0_17t99v6J3SLZ_oBnkxVCKAFPXI16Uqa2rE7jguZQJMy3BGBp4YRrED8Ns3O5NkirSP6t82WrYmW8feFOklBcTF__d4CTAj2R26O3lwzWXQnunv2pl0TnVEKDSuDwxp-yFgb2jnyxVgA8KAGICmZFoR8b9NZN6ByDurO2x03mr2Pm6ApeUYTgoIAbvHDpu4192cqlEAa-DHQkwTbnvvW968NmXjOv5yv9HVipaMt4PauSsJu4IPX5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=bDyjoVCopxkqbl9GaelHyZBfd0N_OgMRcvpm1M-TvBYqF1yIiDwia-gaFDOOUhQT_96Vy_O1UOlhC0XnLuKeBQr7DwHRDyo2aWqGyw4QXKp1fdSvptBL0N7HzAbYy73ddhpTrH4UzE5WX1NYOOfJLnDsdqudOcdTLQtvv5lHQJUOxoRqq4bWuvY_GMj_aCxfMFQQW4m0KZmWG-58XX3OaR5c0RbrpoUHrvBMUHs5M7kCT5SWkqsmW5Bwr2OJTCBtXGSS6WBPwG7HwMELG2IthrD2R2WVLE5ik8gxwFpoeDLhirXEkeGtAICNIbIpIM89hgF8efhLOQTxf14MU0s6b40DFCp8xDVFYYFry818Cwt8hGLefHAchSTQ7tQGCe37V34CnJoYalPlW4glUo2Z5aDbNc86TWFrxliPOqRiPEGn4JTgLVMN0_17t99v6J3SLZ_oBnkxVCKAFPXI16Uqa2rE7jguZQJMy3BGBp4YRrED8Ns3O5NkirSP6t82WrYmW8feFOklBcTF__d4CTAj2R26O3lwzWXQnunv2pl0TnVEKDSuDwxp-yFgb2jnyxVgA8KAGICmZFoR8b9NZN6ByDurO2x03mr2Pm6ApeUYTgoIAbvHDpu4192cqlEAa-DHQkwTbnvvW968NmXjOv5yv9HVipaMt4PauSsJu4IPX5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: در ایران تقسیمات واقعی وجود دارد.
🔴
آنچه در چند ماه گذشته دیده‌ایم این است که عمل‌گرایان درون نظام ایران — افرادی که واقعاً می‌خواهند رابطه خود را با خاورمیانه و جهان تغییر دهند — در حال پیروزی در این بحث هستند.
🔴
ایالات متحده می‌خواهد این افراد در این بحث پیروز شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128944" target="_blank">📅 19:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / ونس: ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/128943" target="_blank">📅 19:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: برای بخش نظامی، چند نکته وجود دارد که همچنان درست است و چه ایرانی‌ها با بقیه توافق همکاری کنند یا نکنند، این نکات پابرجا خواهند بود.
🔴
برنامه هسته‌ای آن‌ها کاملاً نابود شده است. ظرفیت غنی‌سازی آن‌ها، تأسیساتی که برای توسعه غنی‌سازی و ساخت احتمالی سلاح هسته‌ای استفاده می‌کردند، همچنان نابود شده است.
🔴
نیروی نظامی متعارف آن‌ها همچنان نابود شده است. ظرفیت آن‌ها برای تهدید همسایگانشان عمدتاً از بین رفته است.
🔴
اکنون می‌بینیم که آیا آن‌ها مایل به رعایت گام بعدی طرح صلح رئیس‌جمهور هستند یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128942" target="_blank">📅 19:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=GsngrdOf8_GXE2VBcbT1py9G-ilpifaWB6UFUbd8HzVv-0f-h0QPgMBZyqkq1dcrp66LMLdE2OnZlzjCCLVnq_OOLpVhdmgZPzE5ayNCAGo3M44Ufv5xFn2q6wG7AcyiEq2RWYQTBq_xuqLXgqCP4KZAn9Be2_Y0IBWsmEV6l82S_es-SHDpA3Gqf3DhHI-CRqYq7p_IAuyU4qPrTFmaHV4Ab7o4Hzd26DqGq6NPp-Xo28wMaCxSOA5PKDIwMkVEJJVumJq4SaRK-fvB71UWYmuPYG54E6iD3JuY_t3bb5AMq6dnKJUCtaNctqbI2EdfUuKyIg22FRKdutaeHt7eRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=GsngrdOf8_GXE2VBcbT1py9G-ilpifaWB6UFUbd8HzVv-0f-h0QPgMBZyqkq1dcrp66LMLdE2OnZlzjCCLVnq_OOLpVhdmgZPzE5ayNCAGo3M44Ufv5xFn2q6wG7AcyiEq2RWYQTBq_xuqLXgqCP4KZAn9Be2_Y0IBWsmEV6l82S_es-SHDpA3Gqf3DhHI-CRqYq7p_IAuyU4qPrTFmaHV4Ab7o4Hzd26DqGq6NPp-Xo28wMaCxSOA5PKDIwMkVEJJVumJq4SaRK-fvB71UWYmuPYG54E6iD3JuY_t3bb5AMq6dnKJUCtaNctqbI2EdfUuKyIg22FRKdutaeHt7eRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا حتی یک سنت هم به ایران نمی‌دهد / جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/128941" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: فکر می‌کنم طرح صلح رئیس‌جمهور در ایران در حال حاضر برای مردم آمریکا ثمرات واقعی به همراه دارد.
🔴
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
🔴
این بالاترین میزان از آغاز درگیری است.
🔴
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا کنون، به تعهد خود پایبند بوده‌اند.
🔴
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128940" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=JPqA-BIrxUMlFUbvAL9a-LDA2plDFUX8_21zDcFMjig1dFel1RBcrobuzJJtmb40H09qAfFg1wy4uvfvaA5JEGeYS6AR217wQaoRO4fA8H6CQVxmIhT0dCOEf8CWUGXKjxl9VUHF85ZoBCd6aUmNLOuxEXf6zc_HB-HZyBl_wJgqXsAb5AazXli2LzsArol8JPpCVdWoz6BNKuXQou_NwGqnQIZl9BT_ZMXTHlThVcAXuOI4J4yV2TvOMd1tmU3OHZBB--7wCaxh7QTN5wnIBfWJsmvfra7UUFCehMwGpSut0NeczwpNQClXua3cnaBkZFQq6qYmVu07tIkRXTq01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=JPqA-BIrxUMlFUbvAL9a-LDA2plDFUX8_21zDcFMjig1dFel1RBcrobuzJJtmb40H09qAfFg1wy4uvfvaA5JEGeYS6AR217wQaoRO4fA8H6CQVxmIhT0dCOEf8CWUGXKjxl9VUHF85ZoBCd6aUmNLOuxEXf6zc_HB-HZyBl_wJgqXsAb5AazXli2LzsArol8JPpCVdWoz6BNKuXQou_NwGqnQIZl9BT_ZMXTHlThVcAXuOI4J4yV2TvOMd1tmU3OHZBB--7wCaxh7QTN5wnIBfWJsmvfra7UUFCehMwGpSut0NeczwpNQClXua3cnaBkZFQq6qYmVu07tIkRXTq01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غرفه نقطه آتش اوکراین در یوروساتوری ۲۰۲۶ در پاریس، حملات پهپادی FP-1 و FP-2 امروز به پالایشگاه مسکو روسیه را به نمایش می‌گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128939" target="_blank">📅 18:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔴
شهباز شریف: صبر، استقامت و رویکرد مبتنی بر عقلانیت و تدبیر مسئولان و ملت ایران ستودنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128938" target="_blank">📅 18:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
علی‌هاشم، خبرنگار الجزیره: مسعود پزشکیان شاید تنها رئیس‌جمهور ایران باشد که چندین حیات سیاسی مختلف را در یک دوره تجربه کرده است
🔴
به قدرت رسیدن پس از جان باختن رئیس‌جمهور قبلی در سقوط هلیکوپتر
🔴
ترور اسماعیل هنیه در مراسم تحلیف
🔴
حمله مستقیم ایران به اسرائیل
🔴
سقوط سوریه، ترور نصرالله و حمله به ایران
🔴
شعله‌ور شدن اعتراضات
🔴
تغییر رهبری در شرایط جنگی
🔴
امضای توافق صلح با آمریکا
🔴
در دوران پزشکیان، ایران هرگز از حرکت و گذار از یک مرحله به مرحله‌ای دیگر باز نایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128937" target="_blank">📅 18:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / معاون نخست‌وزیر و وزیر خارجه پاکستان: از آنجا که یادداشت تفاهم میان آمریکا و ایران به‌صورت مجازی امضا شده است، مراسم رسمی امضای آن که قرار بود روز جمعه در سوئیس برگزار شود، لغو شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128936" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128935">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع: بررسی اصلاحیه قیمت‌های ایران خودرو نشان می‌دهد که نرخ نهایی اکثر محصولات این شرکت بدون تغییر باقی مانده و تنها چند خودرو با «کاهش محدود» قیمت مواجه شده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128935" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=WZr4dgrBYAVBhCXeQdETGtmTSzzW2hv_DmZxSXNKweqrCP9YAbMNDnUCYt6dOU284gFnnk3cDtH6yWnlt_brZrx8_MqnrrSYkIZolt0Cx7dWr0prLGMwffDvxVSthI6SEvb_-RwPPuKP2Q93bS0JZiQ8NrPulpsFv8MDmRbjzez67_p-o3Js_QONtyB5HYBPM4IHWj29h3I6qfqiw_4QV4CD3oJ4fQOWwTO2mVDnEOEZP7cP4KcnVueIco_niIGj8tdMiqbA4AT4NdJcYL0THIVtUSlWvmzT0jdbKSFWsSN313uOwNN5ORa05bEL-1etUesXw-F8YEC-HbBQ3YLDDxfWxzlARAyxp6A6dyg6wYamBjcs0DyiaVaT7TZ9hLJAF1qBfpqz5iQLWS2sGLsKyMSROj5iat8Wb1XMk-cvvxOFoBb8yt1H9vo3-pFAp4DkHaPQe_cxukR8Bh4lGjxLTA70YG_w5fk-cqSM4xlbnDHkF3i3NdubwJj9nY8Yu9uDuA9ffhziaiuhTk5FlSm94kNoW1ibHMdPoT-rvjkUdCvJqiUKB3w04NIM0oB5XfzHvqefTFlP3WQYmAhFc2A5oXlyq-Iq6gaa62KISgH1BVqLZo2vL4iHD4WiMrN3XBel8bqZD5rM5SU_byKcOF5L-riU8t89Egw_pPYFrXj4q1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=WZr4dgrBYAVBhCXeQdETGtmTSzzW2hv_DmZxSXNKweqrCP9YAbMNDnUCYt6dOU284gFnnk3cDtH6yWnlt_brZrx8_MqnrrSYkIZolt0Cx7dWr0prLGMwffDvxVSthI6SEvb_-RwPPuKP2Q93bS0JZiQ8NrPulpsFv8MDmRbjzez67_p-o3Js_QONtyB5HYBPM4IHWj29h3I6qfqiw_4QV4CD3oJ4fQOWwTO2mVDnEOEZP7cP4KcnVueIco_niIGj8tdMiqbA4AT4NdJcYL0THIVtUSlWvmzT0jdbKSFWsSN313uOwNN5ORa05bEL-1etUesXw-F8YEC-HbBQ3YLDDxfWxzlARAyxp6A6dyg6wYamBjcs0DyiaVaT7TZ9hLJAF1qBfpqz5iQLWS2sGLsKyMSROj5iat8Wb1XMk-cvvxOFoBb8yt1H9vo3-pFAp4DkHaPQe_cxukR8Bh4lGjxLTA70YG_w5fk-cqSM4xlbnDHkF3i3NdubwJj9nY8Yu9uDuA9ffhziaiuhTk5FlSm94kNoW1ibHMdPoT-rvjkUdCvJqiUKB3w04NIM0oB5XfzHvqefTFlP3WQYmAhFc2A5oXlyq-Iq6gaa62KISgH1BVqLZo2vL4iHD4WiMrN3XBel8bqZD5rM5SU_byKcOF5L-riU8t89Egw_pPYFrXj4q1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ۹ مارس: این موضوع واقعاً روی ما تأثیر نمی‌گذارد؛ ما نفت و گاز فراوانی داریم، خیلی بیشتر از نیازمان.
🔴
ترامپ در ۱ آوریل: ما اکنون کاملاً از خاورمیانه مستقل هستیم. به نفت آن‌ها نیازی نداریم.
🔴
ترامپ در ۱۷ ژوئن: اگر به بمباران شدید ایران ادامه دهیم، ذخایر ما در حدود ۴ هفته تمام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128934" target="_blank">📅 18:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=Ote_3ThNOZj_YFlHfNE9r9X3maqLp2AvqtyvFbWqP9jzyieDzl1liZX2CPnvEHI-EiIx7SC2lxt7R-iTEmAvAihEnY0lcYiFfkdkfafBOjuz9ZjHHE4xzWc-KuI6mQUY55e0JtXuiye9c_USHmrEP-E7_hv8kkQImPvE_YBwtYBDez1NyMD6klowRYvZcOLGECvADY6vi_nKNOPxZ-XYDtRBsa47hiMCzT3CyLSUaHcA8UCPZ16hQbBNRbE7UFt5Vj6fNP4cbOrh5CedO32XqFjDJWwz6tRdc3XjcR7BgNlI0kiZ8oS2MbfHF3CSpFDIpl_zJ3N0RKbxW-v3FZXvCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=Ote_3ThNOZj_YFlHfNE9r9X3maqLp2AvqtyvFbWqP9jzyieDzl1liZX2CPnvEHI-EiIx7SC2lxt7R-iTEmAvAihEnY0lcYiFfkdkfafBOjuz9ZjHHE4xzWc-KuI6mQUY55e0JtXuiye9c_USHmrEP-E7_hv8kkQImPvE_YBwtYBDez1NyMD6klowRYvZcOLGECvADY6vi_nKNOPxZ-XYDtRBsa47hiMCzT3CyLSUaHcA8UCPZ16hQbBNRbE7UFt5Vj6fNP4cbOrh5CedO32XqFjDJWwz6tRdc3XjcR7BgNlI0kiZ8oS2MbfHF3CSpFDIpl_zJ3N0RKbxW-v3FZXvCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرا با اسرائیل دارای سلاح هسته‌ای برخورد نمی‌کنید؟
🔴
گروسی: چون عضو ان پی تی نیست! خواهش میکنم عضو شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/128933" target="_blank">📅 18:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=GSJpY15H8BpQ7C2LqjrT20qL9kYC5hta_bwoz_hnS_1nXoKTfwN8HW2GFK32dYlY40-dgpEOl5fEZSm5AxoDCwYLwnDKCgHNKqgoHkZkMQFFw23j8Z94kIxqyKHT7HThq_2qBl8L5tS0WbdjNl4KGH-1nF4qs16_EXUoIjAWBUBadC3lGFECT7Tptx8D548CnjT0VrhxtlWqyNDIhzAlDdua2u_uT3NvQGHZ7cL4k7L3NtPGQvK3oVU4ES1Gtqyk-6v7zUvBmeGR1OzPvbIqNbEHuvS3xHPOwMXPhckIBIUbfcX0McPJ5IGpbbKJKamAn7Yf7D_sVmR-1w-iBdm2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=GSJpY15H8BpQ7C2LqjrT20qL9kYC5hta_bwoz_hnS_1nXoKTfwN8HW2GFK32dYlY40-dgpEOl5fEZSm5AxoDCwYLwnDKCgHNKqgoHkZkMQFFw23j8Z94kIxqyKHT7HThq_2qBl8L5tS0WbdjNl4KGH-1nF4qs16_EXUoIjAWBUBadC3lGFECT7Tptx8D548CnjT0VrhxtlWqyNDIhzAlDdua2u_uT3NvQGHZ7cL4k7L3NtPGQvK3oVU4ES1Gtqyk-6v7zUvBmeGR1OzPvbIqNbEHuvS3xHPOwMXPhckIBIUbfcX0McPJ5IGpbbKJKamAn7Yf7D_sVmR-1w-iBdm2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنانی‌ها همچنان به سمت جنوب لبنان هجوم می‌آورند تا به خانه‌های خود بازگردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128932" target="_blank">📅 18:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGsCBKWwVafGC--nw2rXFM0xOIMjT-T6FXJYPtd4PN1Ddph7auN2khKwZB-ppulijfldnhYqHkqDMgC5ehY3eXzkG9RaDwz-5GIR2q-Y6ArmuYsllYQJKdrRHvZSGWKiVpxvITv8ouG8XWj1vX1BkDenFNvCTpZHX1HZXUYVSsUchMXvZo7hT66OveUAWCtfkzktxqaNZBR9ayw4rJ1sU9IMw9vV1QwRnLl7GjCzqeqJvG-f1GnmRP-MMIGkYm_1XQODWZTuUO-echJUjIpUKV1RDQVxq7aiMV5XjsTgUKgzwkLs-bzBs3okCzU30_GqFhaZt0f3BPy2Tlk8c-Dc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش‌فروش‌ بازی Grand Theft Auto VI رسماً از ۲۵ ژوئن آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128931" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128930" target="_blank">📅 18:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در دفتر نخست‌وزیری:
معاون وزارت امور خارجه نماینده پاکستان در نشست سوئیس خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128929" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ به کانال ۱۱ عبری: آماده دیدار با نتانیاهو هستم
🔴
او باید منطقی‌تر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128928" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4IAAJXC_xVWhGkQdMHe6CeeiubMzgzKHjX4EIshFYyRsgVVXbR6zn5ZQFs9kqggH_qlyu5mcCE0fbkO8wIU2HgRotWxGzlkBG70Frz55cuU4qfmXenlN6zay28MiPpBXEcs8_lMkZHvIKLHTqss5yceFPnOEaGh8zU_QKLMvsdaP33tolBqWogpFXXSegdSak8A1FK63m5pkx737iM0jmJSzsbGo_lCfFhvosKX3TkYzKaPz8UC4XYX6gHb1y7vuBO3E36m8omemRl6oqk-Wx3gmFEu0hme2g4znrKwpSwcF7-fCo2J-Y6AHs9qU6KqxNxqf1OeRmvWUZaeWWBnDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ به کان نیوز:
من به احتمال زیاد در انتخابات پیش رو از نتانیاهو حمایت خواهم کرد، اما باید ببینم چه کسانی نامزد شده‌اند.
ما رابطه خوبی داریم، اما او باید منطقی‌تر باشد. من آماده‌ام با او دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128927" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ:
هیچ ملت و فرد عاقلی نمیگه بمبارون رو ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128926" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMtWc7bp1e938hL98mwXAtokT9V6sgFiFuLxNmCVVtsl503kFD9GLSG_PJKNDxVN2RudVlET2cnFyh3PxPKVHTMB-PUIevI_fQZIODDKzadbZEwtB2h1mksh2y2jga309CDYx0F9wfdHdQl2LFbcHt9uQrvRKl0Z2sfxqhGuWytuGtBDvXxZo4ZbTuY6YE-AE6XLP_puntKThivAPVQWjIbc53GEjw2d4j5U8gWf0m3FNPYnJwJFjBZbJh_IlXdHG2H45DY0APdfbMLvn0bWBJ-ut1CWUI59sTtkaEqKRXjyuVALHEb_eE1dZFKwrfabQwDYN82Fqpm8FO8gE1q0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: نفت در حال جریان است ، ایران هرگز نمی تواند سلاح هسته ای داشته باشد (جهان در امان خواهد بود!), بازار سهام در حال رشد است ، شغل در رکورد است ، و قیمت ها در حال کاهش است (قیمت مناسب!).
🔴
کشور ما قوی ، امن و محترم است مثل هیچ وقت پیش. خواهش میکنم!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128925" target="_blank">📅 17:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128924">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128924" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128923">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تلویزیون پاکستان:  سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128923" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128922">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=ba_qMjILiDP7naB7vjwV0FwDohbpG8_6XOXY0Mh_pwX4orDpMa7_jJDPSFY8ZQK2Ej1A5Fa3hsDW0yknCjNsV3VEJ3yhYAdjAzXv-LgOke_f0Z9i9lLXkTwWgPwTzwAd18YMorGJbABY7L5FeU2p2OUogwtHcSIJUJJCz_e9pT-v-0Mu9-WVPHhzJvt9_pyBF56dTICPm3QYmB_q9UkbhO4Y2JNnOMsdLA8Jlt0xJlgSbUuBcYX3XyfL1EK3eNGsuZ0GcTROLuNLEniLByagyNp3mdePS_RkTp68AP-lrALnQmZPMEMIkhWNx3UkHtDtosHOXUhWCThrw0InjVBb0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=ba_qMjILiDP7naB7vjwV0FwDohbpG8_6XOXY0Mh_pwX4orDpMa7_jJDPSFY8ZQK2Ej1A5Fa3hsDW0yknCjNsV3VEJ3yhYAdjAzXv-LgOke_f0Z9i9lLXkTwWgPwTzwAd18YMorGJbABY7L5FeU2p2OUogwtHcSIJUJJCz_e9pT-v-0Mu9-WVPHhzJvt9_pyBF56dTICPm3QYmB_q9UkbhO4Y2JNnOMsdLA8Jlt0xJlgSbUuBcYX3XyfL1EK3eNGsuZ0GcTROLuNLEniLByagyNp3mdePS_RkTp68AP-lrALnQmZPMEMIkhWNx3UkHtDtosHOXUhWCThrw0InjVBb0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128922" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128921">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128921" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128920">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8cD3dUf7F3k1embW72nYgk6ZcjlWGSecu_YaDlhFG8FBk0AuMBp98XZ6QzfupJ1bOBoPMzp1u64D5IulsYqoeFQaKggg_4o0qTAZsvb24dbWuxG1A71r13HQenhBK6cBZtHxpeWMT22K03f7Tnwp9hHViaqKBdDrHV6Jjh1BRzW6vL0ift7SD7cLnnQ0AHuvP6RK1IRqApOQla4OC_JrU0T8IdxweSN8RUmPK9X92fkyPmPxVTycJ1oN_ELCKVZeqHkJix5k_BB-L1EUmjp8Hu9rVCZ3RflJ5Hv_O0e4B-p8AYqzo0pzYr-LqrRI0Ro3-7sBPJ4ilFXZDFZWM21DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این عکس رو هم آمریکایی‌ها خیلی زیر پستهای جمهوری‌خواهان و جنبش MAGA دارن میذارن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128920" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIF8scEGc1q2tRc2mIQQwz324_-xvWmgb2G4SXPV-vWfxapXwAsREO_yqJxOQleI7mqfeI9ZP5svCZ8GyoUaLvaXiPQnMpHUJG1NVuolgMfdOV_CF5Hyorxlt2-ukIekcHNNvJKwOzVcNq1Pd0l-AEsNGtDoSjfBth59TUmi6RKwAJryNcnf9xiUG7K98FY5SfhSXfWzA16BolQk6R5bI6ZSnqqYeTlqVyfuKvI9u_Sd5eWLeOJ6RIhIZEot3Ak6FwPVzR8gu5PG0uB_rlKDRTM_sgkElGI_KFvF2KpmQgfE7Bp900MKflr5OVkrTcZhvqLu-YLsSo89WaTFdsFKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هنوز تصمیم قطعی برای رفتن به ژنو در تهران گرفته نشده است اما در صورت رفتن ریاست هیات ایرانی با قالیباف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128919" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128918">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9FIy0kJ_B4MJqmPRk08kQYkjLvqo7iwCGy--XzP5XTQjUuzwaMsStzshxWnQrI_b04M9PVrljqYdXPzBH3HPqNJgt5sf7bsLdtKzyQX19xiJ0khKBtr2mBCNxyKXSPuWzvy0vfLC7ow9BCY79Z5c88GdWBiKqB5RtbqZt_iEruDHkIY4vV5hLaQreZ-XAcRi8HR9oIz1KuLtwIQoss6AEvRBrvDM5iCvkxzuCMyGUSfKJMp2gIF8ogTryEJPJfS46eSU37Z9bBqCpDnCio7dMOPy1D5Bqiaxpq_Q9VO3BskCUKeS2TM8A4O-xC3XcWFgoIcmb3myeLPS0_PscDuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی ثاقی:
یه مشت وطن فروش به برنامه ما هِیت میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128918" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128917">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هنوزم آتش زرتشت ز سینه پرتو افشان است
هنوزم فره‌ی یزدان به ایرانشهر تابان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128917" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128916">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128916" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128915">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: ما امنیت را به شمال باز خواهیم گرداند و این مستلزم حفظ منطقه امنیتی در لبنان است. ما نباید از آنجا عقب‌نشینی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128915" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF720fGwB-OxHCuEZT3RQbeRDbDoYFEwTKtEv0S0AVLjQiAPcFl-_TiD6L1GrXq2vMfmCjB6RXkgr4gU4NvKYr_gIrXDGfCIneWjghpAhfoTLxfg6-3cEtFeX293J95M7_wp6RNrU0dOMXAa_YlR73hfFX_F2WlknBEhaF_dfQzQPWm9orfTHK1qKT7fqd5pnVl5N_STTJmTntTGoXISXLlmP5Z19llqQunUodsouoSjfowK1DeJBPjNZLRAt9_vE26tZ-bcj6RYjelNdBhI3D-uyHYUUpiNImRxpI0e-LmVBmm__7LRjrcad9esZbWaFdwxt0NuZrCQFd_cgX4bTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxPbNNQftdXliPx37-Sje_SsIzlGcrzXtoy5OjnnAJKU7pL2dhR8CpuiSZ0IGLeUgXVsgLapQP8CNn2HAGQNEhDxBLAIMguz5ok2MJMNqGf_PCQlfmstl7tU9TzdfCh8sWb2nvIbt5MWZiDL_uqambq4veqLGcOK2aJ9j-2DB11gBn2pxNEvCQMzX0PZUNl0X2AjJBjnukjtP5g1hwj3X169ghB6KDc01OC5ndZZFBgSvWcc1NhM2W9-EhIFZSlkuyi-yWfkxPpCxLU_9FXogDJN6lZkurplK3t0c60cb0bqHoN-7jPJoQEzICa0duKjHVWYIxk-9mB777S6JuJEXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128913" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=gIDYi91SKBLUuOtlPZrNIs5JypjU3RZj4KTI6CQikGrWwgKAhWLnfF07XYaVX7FKLibTuS6TNdCCogiL9NTrDJUgeaAEy0ItouzPXkdUJF1yqxOgN3BbBHt_PpfhifROK0076-RFl8tAM6LmJxsybnH_Tb_NEDHAhuROOVSrB1WcZcoJkzaaL81Wiyz80TvvdxlQmFcD0WNiL-o_HWYeWf63XPx-GzHuVP_v9Pn81ldI0BA6lmSjzjB_xzkkFBLjlGuP3ASen1rnKxHwmX6aV6bxVRIeVhRd3NHW_CCePqCatUmXa-l1hjd_iCl7GwVhR-zydj1Hx3GD7wBdubLOiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=gIDYi91SKBLUuOtlPZrNIs5JypjU3RZj4KTI6CQikGrWwgKAhWLnfF07XYaVX7FKLibTuS6TNdCCogiL9NTrDJUgeaAEy0ItouzPXkdUJF1yqxOgN3BbBHt_PpfhifROK0076-RFl8tAM6LmJxsybnH_Tb_NEDHAhuROOVSrB1WcZcoJkzaaL81Wiyz80TvvdxlQmFcD0WNiL-o_HWYeWf63XPx-GzHuVP_v9Pn81ldI0BA6lmSjzjB_xzkkFBLjlGuP3ASen1rnKxHwmX6aV6bxVRIeVhRd3NHW_CCePqCatUmXa-l1hjd_iCl7GwVhR-zydj1Hx3GD7wBdubLOiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه سنگین حاج فتل به میثاقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128912" target="_blank">📅 16:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پولتیکو: ترامپ به وضوح از تماشای عکس‌های سوختن کلیسای جامع دورمیشن کی‌یف که زلنسکی به او نشان داد، تحت تأثیر قرار گرفت
🔴
این فشار نهایی باعث شد که او از یک بیانیه مشترک سخت‌گیرانه‌تر درباره اوکراین حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128911" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFT-xgPYr4jwqUmRaSsLv06BSCAEnQeAP91XbTdT7PKyhAe2XTIoHDpTKuDLde2PAHd5cYnlvW-n6Y3FSXmgl233w1RBt2yspoDVHJwaNJPARGCwIfyq21SRPG0-4xIpZ9h_GVQaKuoL_3fbzIw3fs92YXFBhi9H5bbHFyuCqowTvHV4CJFVj8aXt59_wCQGVzhJnIjAwcJtP8XEuC1PuYM-CRBvaT-F37YC26eKMVvQL2Y0zDCfNMtjLerAaAiSgmRFrUpXIpFFApF6MzQkD4ZRPADLV0WM-vJnUYY2u_Uxt41-hyGHqL_dRA4Ochl2gVGaZTK7EH_lvvnpN4xrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از تأیید پاپ لئو بر توافقش با ایران خوشحال است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128910" target="_blank">📅 16:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=ItFX16sBCas8TEIH5nGxV3PEz2lAdPEc5N3EEb7oDYQfCAY--kAAXOkG8cbnSuu2nuOOzMPnK-Pz6JpvEjGXyXRphSMfFCPSqCViB90wGwAdDLCvucKiJ96tjrOoi5Rmc6UpDBxol6elnm9R0XnzQcW3e8kb3-9rKCQ40FPR7fQb1SP4puYNb2OO9DiNi48T2qJGer2JVWNfdsxT5iK5floQcdfL68VxL3HwsA-RHVuoAxqrhz9LCmz-2H0sb1HPhCPziR2oPm9k-8fdJcunXTrpdZC4FZUMpRVNtOCdjDtkfdLukrjCkP9bghraBL5IYMIcmPRPrGsPADf1bXsnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=ItFX16sBCas8TEIH5nGxV3PEz2lAdPEc5N3EEb7oDYQfCAY--kAAXOkG8cbnSuu2nuOOzMPnK-Pz6JpvEjGXyXRphSMfFCPSqCViB90wGwAdDLCvucKiJ96tjrOoi5Rmc6UpDBxol6elnm9R0XnzQcW3e8kb3-9rKCQ40FPR7fQb1SP4puYNb2OO9DiNi48T2qJGer2JVWNfdsxT5iK5floQcdfL68VxL3HwsA-RHVuoAxqrhz9LCmz-2H0sb1HPhCPziR2oPm9k-8fdJcunXTrpdZC4FZUMpRVNtOCdjDtkfdLukrjCkP9bghraBL5IYMIcmPRPrGsPADf1bXsnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب کشور: رقابت های جام جهانی مصرف آب را در کشور افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128909" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ارتش اسرائیل: بنا به نیازهای عملیاتی، نیروهای ما در منطقه امنیتی ۱۰ کیلومتری عمق خاک لبنان مستقر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128908" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
صداوسیما: ۱۱ فروند کشتی از محاصره آمریکایی‌ها عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128907" target="_blank">📅 16:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه در تماسی با وزیر امور خارجه عربستان سعودی درباره توافق واشنگتن و تهران گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128906" target="_blank">📅 16:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UW2uFvej3JGm6nlzuTkWGTb4lZNctHiHueqyR9FoE9IfcWNFGRwBvEQS7TWyFpgplT9sReUOYhJYwrMpNSkfKRUCOSjckbRHxzCo72jFjQaW4o1-yvpO8kiqh3DB7uh7oweFiRIg3UuJo_3DEKNnFBHpzFkwiqMl1g0W9ZKXuwgOheckXlx_k91uwaI5mC1wyIowmMD-zFbZgnPyurHW-kYpWhJ4tIBtO5_LQgUPZRcdCs0HRK9PNAJSZifqoywJL3w36w2qbz5q1WO9a_3GsI7Eeu4-ZDs8qSkChUrLHkZUQHaHQB_2RN9h60q33v8GKgh7IY80P8PYU0CTcMKHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/me5s6ZoNnY9eNXUWfVASeIyk5a80ttOUdnocDhl1kv7Dvf_knk2Ee7hoBSVNcrp2X9-7SNdmNEAdhGEN82p2MWeEBJ9HNnhbwosuI7PnIe7T5ob01E8qOFDO0BAnU76AkD_qtS_uG3GaLBdbfMHbA4zDBeJFlHJDT3jk_ibBItfjN-KaGafCQjBUzoXvOuPYQtjtsAsHw7Kd2V3q6i2Je2dp60-Z0AIr6e6c0yw8QBczbXPZzWJAgtGE2-Y0Rtf4fzU0SDk4nUTH6c_bBW0GaWhmO8MWGCsODNq8g077q30cJiR2sB7n55k3YEbqdlnPsvNt4YWC5fjkfF2f2DC_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری / رئیس جمهور پزشکیان متن اصلی تفاهم‌نامه بین جمهوری اسلامی و آمریکا رو منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128904" target="_blank">📅 16:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی‌ان‌ان‌: نتانیاهو در تلاش است که بر توافق نهایی ایران و آمریکا، از طریق سناتور‌های حامی اسرائیل تأثیر بگذارد و بر ترامپ فشار وارد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128903" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌ان‌ان گفت:
نتانیاهو معتقد است ایران با محدودیت‌هایی بر برنامه هسته‌ای خود موافقت نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128902" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: کشور‌هایی که از تنگه هرمز بهره‌مند می‌شوند، برای باز نگه داشتن آن اقدام کنند؛ ما به این گذرگاه وابسته نیستیم
🔴
مذاکرات با ایران، حول موضوع عدم دستیابی به سلاح هسته‌ای خواهد بود
🔴
حضور ما در خاورمیانه به میزان پایبندی تهران به یادداشت تفاهم بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128901" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
توقیف کشتی حامل ۶۶۰ هزار لیتر گازوئیل قاچاق در خلیج فارس
🔴
محکومیت متهمان به ۴۲ میلیارد جزای نقدی و حبس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128900" target="_blank">📅 15:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128899">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/طبق گزارش CNN: نتانیاهو به ترامپ اطلاع داده است که اسرائیل خود را متعهد به یادداشت تفاهم آمریکا و ایران نمی‌داند، همچنین جنگ در لبنان را نیز متوقف نخواهد کرد و نیرو های ارتش اسرائیل از جنوب لبنان عقب نشینی نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128899" target="_blank">📅 15:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128898">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128898" target="_blank">📅 15:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128897">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فرهیختگان: گفتن اینکه توافق با مهر تأیید رهبر است و یا تحمیل توافق به رهبر؛ هر دو خطاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128897" target="_blank">📅 15:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128896">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
امارات متحده عربی با تصویب قانونی جدید، حداقل سن مجاز برای فعالیت در شبکه‌های اجتماعی را به ۱۵ سال افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128896" target="_blank">📅 14:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128895">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بقایی: بازگشایی تنگه هرمز صراحتاً بر عهده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128895" target="_blank">📅 14:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128894">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مدنی‌زاده، وزیر اقتصاد مملکت: قرار نیست توافق با آمریکا، اقتصاد ایران رو به شرایط کاملا عادی برگردونه.
🔴
حتی اگر جنگ هم نمی‌شد، با چند صد هزار میلیارد تومان کسری بودجه روبه‌رو بودیم؛ الان شرایط سخت‌تر هم شده.
🔴
دولت چهاردهم بعد از جنگ ۱۰۰ هزار میلیارد تومان از بانک مرکزی گرفته و آثار تورمی اون در ماه‌های آینده نمایان می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128894" target="_blank">📅 14:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128893">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت صمت: ر اعلام قیمت از سوی شرکت ایران‌خودرو، نسبت به آنچه که توسط سازمان حمایت محاسبه شده، اختلافی وجود دارد و ایران‌خودرو رقم بیشتری را اعلام کرده است که آن را هم اصلاح می‌کند و اصلاح‌شده آن را قریب‌الوقوع و امروز به بورس اعلام خواهد کرد.
🔴
دیروز چهارشنبه شرکت ایران‌خودرو بین ۳۰ تا ۵۰ درصد قیمت محصولاتش را گران کرد.  این خودروساز از پارسال تاکنون ۴ بار قیمت محصولاتش را افزایش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128893" target="_blank">📅 14:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128892">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d006ba55fd.mp4?token=Y45z9fADNhS_gd5QObLIGtZuVXd3R7JfZhlcb6cyBf4ZboDpf_o47AZ9R4JlwXN1RYJhR81iKc2DJllrZiSdiGfQVl8PKJX4DS4UiQhF7YRrkqX62ItG3mqp44Dwk55A2oFTz7hXyIZ38dQwY0MHrYOgH5jRUqX24n8dQWfUpRrQJ5oSqQ84ZWAvPSNPY6eKt3chssotlmAtstTAjNyKHt80FaXD-K-aHaUo4nncIhCoOGJzmBfLDvTrPRO60AZyNgY6jlpfYIdvEmVoOe-YsM3CX5hkQiCeo-vDH8NvvlhhmNh-QX53hC-In-uTfLtOYV6mvGhJ2oQKmwzdzpnyTb9XvB2WowdB0OgF7nwsqKWNEXZOtsp6mdL9CIkCG7PsqHBOi9I-bog-bc5giI5uauQqDz0ipxZZ_ikYOJ9XmWsutWIrswZtoPtJJ8jQr8MgAcXB7Ae-Vc9GzNC8qWgmVWLDzH8FkJ7d4zdb4KTtJkfOBHEP6FFywJhwHVL6thWR--a4fNmPC8QoCU_45FqPXduBR0doNFuSzcmO0Xd1Gf1fwLKOmLr3o49OKqqngMsBv7Os6ht7U10H-ixm8d4bfMB2kQbeXl6I-erLzuwnWOmyAczGNvn8YbLhverT_lBmoRFQAvh6Gt5Qd7fDO9RJX7egOm1SgegqQ0_umNk3hQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d006ba55fd.mp4?token=Y45z9fADNhS_gd5QObLIGtZuVXd3R7JfZhlcb6cyBf4ZboDpf_o47AZ9R4JlwXN1RYJhR81iKc2DJllrZiSdiGfQVl8PKJX4DS4UiQhF7YRrkqX62ItG3mqp44Dwk55A2oFTz7hXyIZ38dQwY0MHrYOgH5jRUqX24n8dQWfUpRrQJ5oSqQ84ZWAvPSNPY6eKt3chssotlmAtstTAjNyKHt80FaXD-K-aHaUo4nncIhCoOGJzmBfLDvTrPRO60AZyNgY6jlpfYIdvEmVoOe-YsM3CX5hkQiCeo-vDH8NvvlhhmNh-QX53hC-In-uTfLtOYV6mvGhJ2oQKmwzdzpnyTb9XvB2WowdB0OgF7nwsqKWNEXZOtsp6mdL9CIkCG7PsqHBOi9I-bog-bc5giI5uauQqDz0ipxZZ_ikYOJ9XmWsutWIrswZtoPtJJ8jQr8MgAcXB7Ae-Vc9GzNC8qWgmVWLDzH8FkJ7d4zdb4KTtJkfOBHEP6FFywJhwHVL6thWR--a4fNmPC8QoCU_45FqPXduBR0doNFuSzcmO0Xd1Gf1fwLKOmLr3o49OKqqngMsBv7Os6ht7U10H-ixm8d4bfMB2kQbeXl6I-erLzuwnWOmyAczGNvn8YbLhverT_lBmoRFQAvh6Gt5Qd7fDO9RJX7egOm1SgegqQ0_umNk3hQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین درباره روسیه و اوکراین: ما حتی یک قطعه سلاح کشنده به هیچ یک از طرف‌های درگیر ارائه نکرده‌ایم و کنترل سختگیرانه‌ای بر کالاهای دو منظوره اعمال کرده‌ایم.
🔴
زمان آن رسیده است که ناتو برداشت نادرست خود از چین را اصلاح کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128892" target="_blank">📅 14:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128891">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
میانگین قیمت بنزین در آمریکا برای نخستین بار از ۳۰ مارس (۱۰ فروردین) به زیر ۴ دلار در هر گالن کاهش یافت؛ موضوعی که همزمان با افت قیمت نفت و تحولات اخیر در بازارهای انرژی با امضای تفاهم‌نامه میان ایران و آمریکا رخ داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128891" target="_blank">📅 14:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128890">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBmN6Xcc6yYsp1RCn7axLkbY94JNVsRAaHtlDcwtAO1ckRts7rBKSIlhlQ_KyNGPVDoO2nHRdFIlg-tjJ485Z1cD6_b3-qik7W5LrRlTQWvWvSZmvwNxS1-Y19X7GDNj8vRztdMHBQ6NOe0fjy3mVyYOqthrHexmUi_OIaQn4YkswI8M3RqkM_cIaw33_j5QrDyr8cEceMgkfxM3gqs8xw4JXyFpHk03Z8XaFGBPeysWIaMbsCJnowqXcSjxP7erI9VxAtEfciWYltjaIifY47bunsMPsiZnPVImUxE2CWONHPzVypBqNZi4zgsiMjsuxYLMkszLGKBSM8yYPAZBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به گفته چهار مقام آگاه، وزارت دادگستری ایالات متحده در حال تحقیق در مورد چگونگی ایجاد یک سبد سرمایه‌گذاری جهانی گسترده توسط مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با اتکا به بانک‌های وال استریت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128890" target="_blank">📅 14:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128889">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVg1XCQvtm3EawX7_uc6VxOgm3Iuwa2fBDLtopSwe_XANkuFJceacwipBRF1boBtzQJpAJhX_hXY6Oy9fIRuVD_N-kPSuRvixZm6P4UFq1bZK9diNWs_8Rim_Unx1cOT08V57kB772QmKnKWuHLYvWvw-NrpzMwaUiZ1WtURxNUlPXAuWGjz0yakrGmPG-8mIB-dvo0SsdSkjd5uCZB5_uevDHi0w6htsp3RLhnli7DM8hNCTJMUzv8CDDRGlRkanveF5f4ChzoXm7NxX19_CJAi9p_zNsuSFf1RK4mD8FjEfOkouBd9XvcNsmO5Vj_HFNlTM6cKagike6BWV0mnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128889" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128888">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJDPR5b4VmEXyKw8T1tYxWaEEqs8NOu7iubDXiDsPva7tgupVJ8g5bqg6myM4DrxwiEBEdH8iSJiN0D3t-le5r2DcC9-ZTl0k7_8C5IrxDkOfWvtD6OPRdQs2Xw4u7bhzOWiWPwSkmoc4zRUGgEqgrrJjD372d7Md34Riuf1KR6Yc0gyyxLxkxyFF3ZYcWhLb1y_tajfqGlLvcjBbLBj4QyRxCaTKg4uH8Ecljw7YF3hLOn0-P1BHNApd0N5iFAp2RFHkxK82o7pkkZOnEip2nF0iFnPrJvcSi9wgFw97uSkSbZqw38xTH3O9lsB5MbxeeFRuh5AehazZ0FtDpJRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهرام پارسائی نماینده سابق مجلس:اگر کشور بی در و پیکر نبود این حرام خوارها بی کیفیت ترین خودروهای جهان را ناگهانی ۵۰ درصد گران نمی کردند اگر آنقدر که برای مذاکره دست و پا می زنید و با هم رقابت می کنید کمی به حقوق ملت اهمیت می دادید در این کارخانه های غارتگر مال و جان و عزت مردم را تخته می کردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128888" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128887">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به نقل از المیادین، یک تحلیلگر اسرائیلی در مقاله‌ای در روزنامه «یدیعوت آحارانوت» از آنچه «شکست راهبردی ایالات متحده» در نتیجه توافق با ایران برای پایان دادن به جنگ خواند، سخن گفت و مدعی شد: «این توافق، جایگاه ایران و حزب‌الله را تقویت می‌کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128887" target="_blank">📅 14:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
زلنسکی: اگر اوکراین بسوزد، مسکو هم خواهد سوخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128886" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128885">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فیصل بن فرحان آل سعود، وزیر خارجه عربستان: «حمله ایران به پادشاهی و کشورهای شورای همکاری خلیج فارس، اعتماد متقابل را سلب کرد. پس از تفاهم پکن و آغاز روند عادی‌سازی روابط، ما در آستانه گشایش همکاری‌های اقتصادی بودیم، اما اکنون عقب‌نشینی کرده‌ایم.
🔴
پیش از هر بحثی درباره سرمایه‌گذاری یا همکاری، باید درباره بازسازی اعتماد و رابطه گفتگو کنیم؛ این مسئله برای بسیاری از کشورهای شورای همکاری نیز صادق است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128885" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128884">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVmzKCxbJxUt-NkBT6P9uu9BWMAJJZCLMEXfCoBA-oFHcWwkAhMGPLIdmJaUeLDd9rRbPDtY2WWYucAdMlv0riK71251BVQNRfapjbv_LLSps9I_MzxaO9z2UCfFqqX-ighoOsML889nmdFDkUJIde-cOmcOYKWJvcQy4fNWRsAHQeO35pgBsmlmbfecbtHxfta-VnXFLq9Pgs8aAb1il0oQUUkUVQiTAGZOIoZIRX-_mJaflO292pdREfGFyhDiag0sho4XpA1mCZE8ptuxRqP71u1mOvcQcVuaHe420FbjD3bsu54TtMnFTFynyEiHpmJxo_ilXjkgWgku82EOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان نخستین رئیس‌جمهور، جمهوری اسلامیست که امضایش کنار رئیس‌جمهور آمریکا برای پایان یک جنگ قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128884" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128883">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128883" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128882">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رشیدی کوچی، نماینده پیشین مجلس: متن تفاهم‌نامه ایران و آمریکا بیرون آمد؛ آقایان پر مدعا؛ دقیقا کجای این متن ما را مستعمره آمریکا می‌کند؟
🔴
آقایان فحاش؛ کدام بند مغایر با منافع کشور بود که اتهام جاسوسی به مردان میدان دیپلماسی زدید؟
🔴
شرم بر شما که این‌گونه به خاطر بغض‌ها و کینه‌های سیاسی، امنیت ملی را به بازی گرفتید؛ رو سیاهان تاریخ شدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128882" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128881">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: تنگه هرمز یک آبراه بین المللی و برای بسیاری از کشورهای جهان حیاتی است، اما ما به آن متکی نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128881" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3g9oJPRvwhafhc-atA1zBWMINXHBmzGS-NgVQH7MmqRkRey7lm7NXu3BX4-_sMgvi_iPIjhCWjYMawK_SrF2xjY_AB2LKydcgxYyLQpctJgDD1yEVtGnAdtxeSVQiKfWJZ9sXfTC3ncMk0KKDDIpi9qL4AZV8KZKfU2JUG9KmXQLsT312G-zPy1eWl-IKzYamEGwRC8mdmwUpjuGXecwqAuN1sEPt-vuG9_AvjKcG--yhxHJ433F71n42rqRYyEaR5YjBL9HVbGuY-jx3L2FaOWCZQro3I0tmuZ83Bp2nlB-8oMwfF0hjq0vioHBVtStW702QQAMLPdv_jYp290dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128880" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1nMWaOPBAvFyZlxbvQEpQNADi1YF809uuPXRASMsUae3neRYue8nHDn80QvQnQKcVXR0JxMkZo5oGfseECsy64bQGk5UzK3G-DC4_H6Qh8e3kVd21gEEz31z_-1J57wsjTf5FwK07qrwEKwqjclRIRkANOMXE12_iNgsUZp2s1xJOD5kor0IKkTRD54ficdsPbR2QsKbMfk5QUg43u90l8n1R8OPipqT50VRh9sSIYE18Ah-FPWDFRjmIhK_Md6EqL38_aNCmaThVHtt5nalDDZ6Doo08uS59giw0gwoLum9VMwvu8O9PS57vY7j6jqt8OUmHcujB6YOCRx2NuEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه  اسرائیل اعلام کرد: پس از آنکه کایا کالاس، اسرائیل را با رژیم آپارتاید مقایسه کرد، روابط خود را با او قطع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128879" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128878">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دار و دسته رائفی پور بُت سوزوندن
😐
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128878" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js_omgd2e3s759hJSKNUazAiSFFqNfGOnP7B3dFhJpwqSuM4z_ZPXpCKXT0etmJmGk7nMxr65_Jl7bpGve-ev1g5oCV1C3Z94_6_zqIT9wmVJAraQAAWXoFnI8a_do7RpwTbfHKwc__d0UbOi-GvTJvMWsy1L56lm6UKg_VyVXUAzArICdG56Tu3JaJii7jx5br_fpxKwlEAEDcf7SWQSnQMpeOrNQc__pxSASOTA3F7DKMXmRPLECRVIgkLoAxQYoREMDevgYEpBJuv4R6jbKpqGOad7hm-sQa09YhakV_aIsK2-oHZkqx7GFf7W9EbUS1Iq6VedIusztga6Fp3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: چه عکس جالبی. امانوئل مکرون که کاملاً اروپایی‌ها را در مورد ایران نادیده گرفته و مخالفت آنها با جنگش را سرزنش کرده بود، موفق شد دونالد ترامپ را وادار به امضای تفاهم‌نامه در ورسای کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128877" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه المنار اعلام کرد که حملات اسرائیل به شهرکهای کفرتبنیت و حداثا در جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128876" target="_blank">📅 12:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTCmGC7cMgk5S-62lI2pSn_QP49E-FG0IDjTAA7tWLG6Uz9d_vVvM1YU7tnp88vN_laq32CVRtKzBfFgS95rFszDb4AsziVDd_mW_tUEAPV6AS3aTYcmHGVSaCmFPr1j87QuH5A59V0Mg-6rYvBzh8O5eVQqJhHrBkAuIwUHG-28igpAbUcUAuHXnfXh6Rztxb3lCjUNG237BY5YhTHGRcBh3H1Zz6l9B3UniaVtU1aVutjSeRbQ2CZLOZ09CKLULw4X-9M0UNzDHRdtSlCbbfqNVMu_JJMXEzQIsCB-SFBxzVRTo7-SOTgh5F_3AiZcNoIm18cSlRjjWQPpjW1gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانش آموزها دایرکت سوراخ کردن که اینو بزاریم، ماهم گذاشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128875" target="_blank">📅 12:50 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کاخ سفید: ترامپ روز یکشنبه آینده در فینال جام جهانی فوتبال شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/134789" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کانال ۱۵ عبری: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/134788" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویتِ : ترامپ فردا به نیویورک میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/134787" target="_blank">📅 20:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوریه اعلام کرد محموله‌ای شامل موشک‌های دوربرد، موشک‌های ضدزره و پهپاد رو که برای حزب‌الله لبنان ارسال میشد، در مرز عراق توقیف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/134786" target="_blank">📅 20:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پرواز بیش از ۱۰ هواپیما سوخت رسان امریکا در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/134785" target="_blank">📅 20:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سفارت آمریکا به شهروندانش در عراق هشدار داد که در پی حملات پهپادی ایران به اربیل، در بالاترین سطح آمادگی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/134784" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: تفاهم نامه  برای ما تنفس بیشتری داشت؛ میلیاردها دلار نفت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/134783" target="_blank">📅 20:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تسنیم: دود سیاه اطراف شهر بهبهان خوزستان مربوط به سوزاندن لاستیک است و هیچ مورد نِظامی و امنیتی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134782" target="_blank">📅 20:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قطر: ما گزارش‌های رسانه‌ای اسرائیلی را که ادعا می‌کنند ما با مشارکت در یک عملیات نظامی علیه ایران موافقت کرده‌ایم، رد می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134781" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کرملین: هیچ درخواستی از تهران برای برگزاری مکالمه تلفنی پوتین و پزشکیان دریافت نکرده‌ایم
🔴
به تماس‌های خود با ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134780" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: تصاویر ماهواره‌ای نشان می‌دهد که یک پرتابگر سامانه موشک پاتریوت آمریکایی در حمله پهپاد شاهد-۱۳۶ ایران به فرودگاه اربیل عراق منهدم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134779" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3aA9rrFC9CPQJO3Rn1NT2mVLSJbt-_fC-XB54SpuC5CfcKp9yaxzYzFljfxFoMsola2DE8Bp9GZBNdTmRQUcJdqDB4KMS8DQfVAqpUr1ZRqidd2IbRpa9RChApB_58SgkMMA2ato-okxAKlHGV73hTUyGpk-i41vOJkPV14a7BfVWk4r9RtiMapLoNW4vKzdU2JFyR5JIypDD4ayZIG6QvMdgkLtp-hO1hkqdy_BsYivmMuCNQnbyMC6-DLcwgNIFzoya0s0Uyr3hJRpq9Qus-8OicTjrprqzmoyx6jyoH0Xm6jc9ikU1hQHy-2TG4PJXAyZOBEyF5GpCYb1Y8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در اقدامی جدید برای شکستن محاصره عربستان، شرکت هواپیمایی ماهان ایران از ۱۸ جولای پروازهای مستقیم بین تهران و صنعا را آغاز می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134778" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز به نقل از مقامات پاکستانی:  ناامیدی وجود دارد، اما ما میانجیگری بین تهران و واشنگتن را رها نخواهیم کرد.
🔴
تشدید اخیر تنش‌ها، سفر هیئت ایرانی به اسلام‌آباد را به تعویق انداخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134777" target="_blank">📅 20:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSOfWpFZnShnQKd5mKAPyivd5rSPM5uOeVfu_sFfsW903OkLVGQUf7lys7rTUfeL4hUs4yle9C_RwIejQ4nLkl4vkBuJ2N7lM7rUOW56YUiWzk-_TQqflrXxswOksVL_34JK8XnM1GyD6bnzZCqVrokH75mURoxfzJoWDu6y_W9c_OfxkAm1U7pNOxlwaQXWrbGPTq2AHfJ02i4RcGYiCFIbuydk1np-2xZ3SRkjR-9NQ5X7Byfdh76k5XqhG5kR3vYhXK902YZyNhusXASFsqCVNwmL0DwjuqHZe4jwCjCHmoDIVPjHYhGxfOSmcKTJ9znycSekMZ0_2-KsiRYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر  بعد از حمله سپاه به دبی که آسمان‌خراش‌های دبی را شفاف نشان می‌دهند.
🔴
هیچ آسیبی و برخوردی وارد نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134776" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عضو کابینه اسرائیل الی کوهن: حفظ تفاهم با لبنان به صراحت بیان می‌کند که ما در سال‌های آینده در لبنان باقی خواهیم ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134775" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXwNSMQf8GC2JsAmaQxVDJQo0mpQb5pKEEIKqctNR8_7Hh3danVXugHc2k48xdEK1jrhTgQ8EvtgHpR7W4iKASrbHahPgm8descdZMEeMUnnlb_sEWdX8IFb5qqHp1PNYCavY619ca_n7P2IbIY_1kLtCUNjfyDlakXcHX32UCJvq_35Hi5ynXzJQxycrivyYSoLU7jB5ia_AFH-dw-wvG4EQJQiQnHKzNlZ0w2EJExsDYxqXcDWKczYryvvmOJqbowBJNU7mpO9B6Ge63bAu0bMYK-IocAPyduMprneeCmDgvgyGZaJ68JS5JevlEG1Dj9MuQUTBJmO5-kMi7GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام وزارت دفاع امارات به فایتاکس : هیچ انفجاری تو دبی رخُ نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134774" target="_blank">📅 20:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134773">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رسانه عراقی نایا (نزدیک به حشدالشعبی): صدای انفجار در منطقه فاو، در نزدیکی مرز عراق و کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/134773" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/رویترز: انفجار هایی در دبی و ابوظبی شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134772" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز نوشت: درحالی که ترامپ در تبلیغات انتخاباتی خود متعهد شد به جنگ های ابدی آمریکا پایان می‌دهد، اکنون خود را درگیر جنگ طولانی با ایران می‌بیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134771" target="_blank">📅 19:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saZrvoSR532OeiePrwNMMDv4uIi6WvY7KvNAr7s1Q6yYTMBI0hURsI9GzmBvhN3xZx4eSPIx-doNfQX4_WEAnv0d82eH_qAHfz5RRPnImPuQEusQ2X5uplImj2jsyO6uQa5wIiBAJcO2BD5gdbPyLJP1P_O5DWnmAdv3U0LPvTwqFVFUqq-e-lryCwO9Qme4os-WSh-0IN0K5BCUTgioBkVzMOHBwStX6xzwOYFqidLaJN6oUggZH610Upn13MUmAsRW3pYo2uIPIWQH7VUtmOHOS4beWa8YU1MPhb6xe-1k-XAZXe_UiCAg19SEwXSHTwShcMN3nrUh_Kk9K4S_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال آماده‌سازی یک برنامه انتقال برای ونزوئلا است که بازسازی پس از زلزله‌های ۲۴ ژوئن را با آماده‌سازی برای انتخابات دموکراتیک ترکیب می‌کند، گزارش‌های ABC می‌گویند.
🔴
پیشنهاد تایید نشده شامل حدود ۳۰۰۰ پرسنل آمریکایی و تقریباً ۳ میلیارد دلار در تأمین مالی اولیه است.
🔴
این برنامه بر بازسازی زیرساخت‌ها و هماهنگی کمک‌ها به جای اشغال نظامی تمرکز خواهد کرد. مهندسان آمریکایی و متخصصان غیرنظامی به بازسازی جاده‌ها، بنادر، سیستم‌های انرژی، تأمین آب و خدمات عمومی کمک خواهند کرد.
🔴
واشنگتن در حال بررسی یک اداره نظارتی موقت برای مدیریت بازسازی و جلوگیری از کنترل نهادهای چاویستا بر کل انتقال است. این برنامه شامل الحاق ونزوئلا نخواهد بود، اما به ایالات متحده نقش مرکزی در نظارت بر بازیابی کشور می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134770" target="_blank">📅 19:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134769">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/134769" target="_blank">📅 19:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134768">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134768" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134767">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
حزب الله هرگونه فعالیت در سوریه را قویا تکذیب کرد و اشاره کرد این شایعات برای اهداف پشت پرده آمریکا پخش می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134767" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134766">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اسکات
بسنت
: اگر کار درست را انجام دهید، اگر می‌خواهید سخت کار کنید، اگر می‌خواهید تصمیمات خوبی بگیرید، آنگاه هنوز رویای آمریکایی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134766" target="_blank">📅 19:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134765">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فرمانده نیروی هوافضای سپاه: درگیری با ایالات متحده در مراحل بحرانی خود قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134765" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134764">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134764" target="_blank">📅 19:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134763">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8014c826a.mp4?token=ddM_EYuDFLkcDXAflL13vmAPPQesGG6FKBendORiiuIM4DJXJR9yZi8cwcqIlsv28jVMwHeByLebMdVYo-Isl_Ao0IRhyAL1Gcy0IJ6Stn-cSAb7zXQFP_JzolMzsJHw__ixbjqkm6_R5B33kW5zFo4DCKzXixmq_RQVdSZ58EbBFJiukSs3NY-Z54szw49ZiGTIEtFFinvY3aZYhz0TqBdX5yBrDMifOVQrtOjUpy1M5TDIdNZh1E9yfUAlvLRxXuWWjPprM-HVBMaBUgF4DFw6vJq_2cwtXHMqonB8Y45ffwyQilv837KLm7p8a3GuDM7J5uY4O4Fwyv13mK3qmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8014c826a.mp4?token=ddM_EYuDFLkcDXAflL13vmAPPQesGG6FKBendORiiuIM4DJXJR9yZi8cwcqIlsv28jVMwHeByLebMdVYo-Isl_Ao0IRhyAL1Gcy0IJ6Stn-cSAb7zXQFP_JzolMzsJHw__ixbjqkm6_R5B33kW5zFo4DCKzXixmq_RQVdSZ58EbBFJiukSs3NY-Z54szw49ZiGTIEtFFinvY3aZYhz0TqBdX5yBrDMifOVQrtOjUpy1M5TDIdNZh1E9yfUAlvLRxXuWWjPprM-HVBMaBUgF4DFw6vJq_2cwtXHMqonB8Y45ffwyQilv837KLm7p8a3GuDM7J5uY4O4Fwyv13mK3qmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیزر فینال جام‌جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134763" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134762">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEGoVC8-Ax8j8AoWRgzUAqg-ntj2tWiuademHa0X56VOG7fnvLXU9PrSqWT6Qa5HcZ3od14VRUH-WfxddunYDp4ACCr2puQ-_2hUDIrbXdE-Ra95YeKFQ4EehaaSmQEdIuwAAdSVhTd5s8V6HhIfuITxt6FGBrutW0f_aB01pjR3b4gbmXDb6nOO4ZxA_C9CEkfwQCFXnGdjxVTRbfNj1Asef-uc8JZk_Nq2dynwuEPolYd12xKX_dr7sscPvbMLJHHP04cfpZIV8LzXP-BJccKIUxz2Mut0GABca6SkX2eJz5sWqHpjDbQyf4xIE0bFT_gWjq9ywEU9LlnUuxfsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سوریه احمد الشرع، حسین الصلما، رئیس اطلاعات را با یک متحد مورد اعتماد جایگزین کرد تا درگیری‌های داخلی قدرت را کاهش دهد و هماهنگی بین نهادهای امنیتی سوریه را بهبود بخشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134762" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134761">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJew05Kw1FpehCyL8xp93flbqiWMZl8Gm0tqeQ8GNTXFkpjPVp11Pr0y8r9bc-12lbvLP6gg9DGqWizbfthBRG0PZ7UXgHsz742Jf1cHMrhg3zzoseoj_hHldgGpM2vTNQSW4S5m50MRG1nwXLLJkpn7l8mY0eiUC44PLf7e8ZBt_L0IEaBH7fel2200-JPOi_Yo3YonrM49Bccpy2LlGijOLHj1ka2_zpYBF68iuCkBgZMLBvFP_BxnIWFyh1bYHOqPkHzPaFgXESXjbwabY6A2Exrj9mYs69owx7LlOCtm7bqOUeX4bJ-sxbb-RfNbnJa9tGdXj3tYwDI_9uTBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه: آمریکا با نقض تفاهم‌نامه اسلام‌آباد، آتش جنگ را دوباره شعله‌ور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134761" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134760">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
معاریو: ارتش اسرائیل ساخت پایگاه های نظامی دائمی در منطقی امنیتی لبنان را آغاز کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134760" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134759">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzYaLeRAfBsioetWrxSsTIX4RNDb9SxfPrYjjfEU8lAoaKFBXfbvfoGlauuPW4FeBHR_5TVTKoImnaNH62MFX4unYBM_yatstBnpsyGQd0WnRIfAsIXskVJoBLN8afiJKkOJ1KShEKgkSqPV1aJcXTNzK2K9BzsNbWj-N474rAZ0kIFZYHFASzd3YCSQCECuEI6P2bz6SKjmPnHQ688iVGbTwyke2CyzS6p7bvQ_Vi8u7PjfFI8pD0FsXKex6w6tdErZCoLmdGztUrjW0L0vA4wczeyZmlHh-2aRpcrCSTwO_091AU06aogqBsDCTjrK-qPYXgYWVcllRW9cCNq3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا مبالغ مالی تا سقف ۱۵ میلیون دلار برای ارائه اطلاعاتی که ساختار مالی جنبش انصارالله یمن را هدف قرار دهد، تعیین کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134759" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134758">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134758" target="_blank">📅 18:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134757">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر دفاع سابق اوکراین، فدوروف: وقتی اولین شاهد با استارلینک از بالای کی‌یف پرواز کرد، فهمیدیم که اگر استارلینک را برای روس‌ها قطع نکنیم، شاهد‌های هدایت‌شونده توسط اپراتور که نمی‌توان آن‌ها را مختل کرد، مسیر پروازی خود را تغییر داده و تمام پدافند هوایی ما را نابود خواهند کرد؛ پاتریوت‌ها، اف-۱۶ها و همه چیز.
🔴
شانس موفقیت در این کار ۱ درصد بود. اما ایلان گفت: «بیایید فقط از طریق ویدیو صحبت کنیم.»
🔴
این اولین تماس ویدیویی ما بود. او گفت: «باشه، انجامش می‌دهم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/134757" target="_blank">📅 18:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134756">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134756" target="_blank">📅 18:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134755">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11f469213.mp4?token=X8wBwwP5UwEVzqW0zobeEO1cS62_fq-T7wSi5Hu2abkDMQ4crjuQDTDde-01xLw0IVhW7PAhHBb6zKgNGLZ1Dsj4hOxyBdXymCTjHtI4kFjLcU2Bwww36Ez2SbhVUKAwldh94LZ_XflTiC0YpcB-LIKj2tw9tqx14klDyCbZt3kTDD_HAbvhBfYDXia1RwGuHP8wRlbDcoTthrnZubl65aqKw16JgX8UNn7j9uiutu47n_W_2bG6dzBKRuSlMLKmTVf4DHD9m9KLk01aSsnBbmzYn5xV7I3-0WLHzurO9NNVAEo-Sf6vK36e3fg9-wSgpkptlwdZQdxyCQUFJm1AYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11f469213.mp4?token=X8wBwwP5UwEVzqW0zobeEO1cS62_fq-T7wSi5Hu2abkDMQ4crjuQDTDde-01xLw0IVhW7PAhHBb6zKgNGLZ1Dsj4hOxyBdXymCTjHtI4kFjLcU2Bwww36Ez2SbhVUKAwldh94LZ_XflTiC0YpcB-LIKj2tw9tqx14klDyCbZt3kTDD_HAbvhBfYDXia1RwGuHP8wRlbDcoTthrnZubl65aqKw16JgX8UNn7j9uiutu47n_W_2bG6dzBKRuSlMLKmTVf4DHD9m9KLk01aSsnBbmzYn5xV7I3-0WLHzurO9NNVAEo-Sf6vK36e3fg9-wSgpkptlwdZQdxyCQUFJm1AYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه ترکیه، هاکان فیدان:
اگر نمی‌توان جنگ را به طور کامل متوقف کرد، حداقل در چند منطقه حیاتی — امنیت دریای سیاه و امنیت انرژی — می‌توان آتش‌بس اعلام کرد. نیازی به حمله به اهداف نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134755" target="_blank">📅 18:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134754">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پکن: آمریکا باید فوراً تهدید به توسل به زور علیه کوبا را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134754" target="_blank">📅 18:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134753">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وال استریت ژورنال: نیروهای آمریکایی در پیامی رادیویی برای کشتی‌ها اعلام کردند «مسیر جنوبی تنگه باز است»؛ یک ملوان از طریق بی‌سیم گفت «گمشو»
🔴
افسران نیروی دریایی آمریکا هشدار می‌دهند که پهپادها و موشک‌های ضد کشتی ایران می‌توانند تنگه را به یک «جعبه کشتار» برای نیروهای آمریکایی تبدیل کنند
🔴
تهران به اندازه کافی از زرادخانه موشکی و پهپادی برخوردار است تا عبور کشتی‌های غیر نظامی را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134753" target="_blank">📅 18:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134752">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134752" target="_blank">📅 18:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امید محدث؛ کارشناس مسایل سیاسی : مذاکره بخشی از جنگ و ادامه آن است
🔴
دیپلمات فردی عافیت طلب و محافظه کار نیست؛ بلکه سرباز جنگ است؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134751" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134750" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134748">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات شدید در کیف پایتخت اوکراین
🔴
معترضین خواهان استعفای وزیر جنگ اوکراین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134748" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستار هدایت خواه، نماینده مجلس هستن که توی تجمات شبانه کلاه خودشو در آورده گفته هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134747" target="_blank">📅 17:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQfwH_82SwTTXhjqceWkzH8V2TxUNUF2FDLC00ajO5r77ykJtsx7AbC2Oulukk1oMBlRC8LX-Mg6-kak-vDG7kiWvI4cocWmP3SbbFfcm0r3YkBQzamc5jOM7qW9WmUW9WZ2fZmQfOun_4vv7rFfqa5hlcN8F5xAef6d5f0NmjJ6fuzK9MMcyfBTStoVWLqRcnmQDh8pqyi7UDrRIBUJ6tPOkt6lVb1UaMvCaMYhv-c4kwB9D7hrYJr3wR72YYbNBEIt13MHClgqNdrwR5NVZGMYVOoA_5EeeP-XgeS0JsdXE5OnVGtcaGo9QvsRWdYZmjnZ9SUfynNNE6fN_kzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: من جانباز هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134746" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رهبر انصارالله یمن: عربستان باید مجازات شود
🔴
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134745" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مصاحبه با فاکس نیوز:
اگر ایران به بازدارندگی اتمی برسد ، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/134744" target="_blank">📅 17:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاشه پهپاد MQ۹ ‌آمریکایی در دهلران‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134743" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در میدان مرکزی میوه و تره‌بار کرج و اعتراض کسبه به مدیران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134742" target="_blank">📅 17:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه:
در ایالات متحده، سهم حملات و توطئه‌های تروریستی چپ‌گرا به سطوحی رسیده است که در دهه‌های گذشته مشاهده نشده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134741" target="_blank">📅 17:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مشاهده دود در منطقه ۲۲ تهران مربوط به آتش‌ زدن ضایعات بوده
🔴
سخنگوی سازمان آتش‌نشانی تهران:
منشأ دود مشاهده شده در منطقه ۲۲ مربوط به آتش زدن ضایعات در یکی از کارخانجات تولیدی اطراف تهران بوده است.
🔴
این حادثه هیچ ارتباطی با شرکت مینو نداشته است.
🔴
مشکل خاصی در محل وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134740" target="_blank">📅 17:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPwSSHoCsJkzVc485PXXghHq9oy7uvV48OSUifsCGY8OoHOhbXE2-viTXTNQN_4qIrYqHtvBj8ka5fB3Lw7y_Oe8Q_rakr_yuN45R506tvKczJ6MGKfHzQd0_4x9xw-VLlngbUW8tw9ka3-8cwJZFRJYQbOS7yfWUyMe62-uKI0ZcH5_8-BC-h-qm0QYkvSL8eAKIeJGMj3P2vSRSbofHmOaUU6msvFwzN4MvAf8DppQnVDQ8Z_TBOOSl3pzDEWeeR8SyhXHz-6fEfPoGEg6ghJwdS-E7XLZdLFXs__37Z1qSj-QHkPBsAW5F66Q1sEMFXR7M6CYUw5IuqzRiAUPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دوقم عمان حمله کرده است
🔴
این هتل محل اقامت نیروهای آمریکایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134739" target="_blank">📅 16:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1XmPBs6DNW8cH4jGLZJL0kQlSWCGg-rA-iTi1xFi0aqzcIeehg5wkvbNflvOUcsbNMhSVZmdd0nhuuro7d5FPb-HBcQJm8LY3BO-5iPy-X6LrXGTDmnJlFE3sShOrXAeQZ4IydAzfSwQjlE-nFAgkoGuUKhHZzldSLK1RIQ0rzSFw6mzB-UaTlUqi1qFgp_rlZg6hDjiqnj6atXM3HiuQ0zkhKI256aMetSklu0PdmPoGvDGuD7wW09Y7Xv8Mp_pVzbHNnh3ldhcoYp9w3CEVMKJDsmsMx2RgKgvz6nfN9JuvDhHeB8h2lvr9iqESQrxwBsQ8U4sfSIOSCigxPt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134738" target="_blank">📅 16:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVpzwx7ZLUGFaNJCscAbm_aM9sK0EeTBa4kxqyi_fntHFph8Fb_DGR7xeLMy32V6E_eRfn4J6_GCj-yomQZi0gQCct8cib3rYBVkQ-LjIgkyCaEa2zPrnbFjbKmj9VDvdzJCJSqCgF0LMohw-xyTvI6LF59zqUj7ZKyT91k8T3JCIZWQdmJ-9I_fvhNUTMcW2gJa8d7LHXwhyl5VQUYo0b4fo1fxOnQJBp-SiFYGS8KNm9q_cQN1FJIgaumUvA7IkcL2kTKqvZqVMxfo6NSfyPGNy2L-404wb8FJAOBjtEP0hLFAC6j1IabLRZJ9jxkeOJVJyWvKS6h1SwYizdNL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت حمله دیشب آمریکا به فرودگاه سمنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134737" target="_blank">📅 16:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLj5MV55fCYO8TTIody9DFqzCp-KoQVXg8ixyD6iMHYBuBs5TEhlXe06CLjn-wOzepyrp3y5_IUy_klQWyzJH0Sp4j0Z3DUsaq6B_vvii6w4Z1-zBoobEQbgAsDKxLV8GeZui2JobILp6uZS5LURkox_rTjAKad8nIniK4k1uOdDSbWu7_BRPmVHhEWPl05qqP4g_NZQWpQBC6_-n70NFB93YBxRC2cjo4OiYEw89RQtN70xUsOC_E_bw9u9co3NFjkTX9USsq1ZSkitqvDH8PmLfsfKv5gFk2VSgvRrBlsBSyftn3gn3lEETKY71XYowOPx1noKQsk4wJKxUsm6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز
:
مذاکره‌کننده ارشد ایران گفت راه دیپلماسی همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134736" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlBe20rR1iI6ubqWVmlH71WenoFVaiNOEyndyMZlgKKzesu23kgWoSS5bSv5BUYSE2WaxYtPqER0tzM5kzzd-HSu9Su7ciPgYyqzjnPphVTpxY1cthj0aLDDfbR9Ws864OZAQZhEpsM1Q7zl9kGsrJ7B0-gQV9A70tYGP5o3pGBEfEmuKSCUb34_GPNaLq4bsCZnDz5VmmVKLMf1ZMNid2PFdKiF0xq7N9SWMEdOYTjcsJj8H2Qzux9tYEugn5yFnjiBFsvNBJGNU5aI_J-8pvjIhBe2VBYUcjmV6lR-IyfE9i-P_sxw_Kb8bpw0CsAeldLLOtDQYKemq671-NDgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
با از سرگیری درگیری نظامی ایران و آمریکا، قیمت نفت هم به وضعیت صعودی خود بازگشت. شنیده شدن اخباری مبنی بر احتمال بسته شدن تنگه باب‌المندب از سوی حوثی‌های یمن نیز بر نوسانات این بازار تاثیر می‌گذارد.
🔴
در حال حاضر نفت تکزاس ۸۰.۴۱، نفت برنت (معیار قیمت جهانی) ۸۵.۶۹ و نفت امارات ۷۸.۹۹ دلار در هر بشکه قیمت خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134735" target="_blank">📅 16:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هند خواستار پایان حضور دریانوردان خود در تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134734" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134733" target="_blank">📅 16:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز: شرکت‌های حمل و نقل دیگر به اسکورت‌های نظامی ایالات متحده در تنگه هرمز اعتماد ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134732" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=sdKAd3GFfRuR3ulb-MNgnjWFNZHH29MFAdAkedojY6Go9z03cGgCgOPF3o4_3dyVQq-JSA-IL2vY-mTYe7PmnC1T6kBLHwOnyLbZYIVjbD_bx8PMGxXmR6SUkykzE4mjd0QLAJu_-jcZT0D_ZQTZvt--qFS2m2cCrXbr6vUl_Dpu4iJAojmJme2TOVyX5eE4emSwzgKBJJ1rk82_OoSaaZK_nA8BhH8G_o2CJvvqaq3OYsGZphWJD8kxq-Sgbw5b1T362rPyTDGf7eOfmyoSQGGeMqTWTHZ1-7-ScuM-X_Ck57dBcoHWftNVUDwqVLt3DFnfH17s6x1nmnhBdWByJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=sdKAd3GFfRuR3ulb-MNgnjWFNZHH29MFAdAkedojY6Go9z03cGgCgOPF3o4_3dyVQq-JSA-IL2vY-mTYe7PmnC1T6kBLHwOnyLbZYIVjbD_bx8PMGxXmR6SUkykzE4mjd0QLAJu_-jcZT0D_ZQTZvt--qFS2m2cCrXbr6vUl_Dpu4iJAojmJme2TOVyX5eE4emSwzgKBJJ1rk82_OoSaaZK_nA8BhH8G_o2CJvvqaq3OYsGZphWJD8kxq-Sgbw5b1T362rPyTDGf7eOfmyoSQGGeMqTWTHZ1-7-ScuM-X_Ck57dBcoHWftNVUDwqVLt3DFnfH17s6x1nmnhBdWByJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویس کرمی، مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران: نصف ظرفیت پالایشگاه لاوان در حمله دشمن آمریکایی - اسرائیلی از دست رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134731" target="_blank">📅 16:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5MkzPaTR3pA_dLs6BCvEvPms3Ak-RKDaCUQXlsc1jnwvOCcbP3FV5ipDCmfxQIFAv8hVO5Kozb1pxHFWoGTxYprPAh5569J9BHZznjT4lolBsMh8ijvGN8Iy_ZrlujL221QIVJl409-GnRyat7-DAYxctOIsk5mH1uXPeI1Sf78PRVweoZhG8mF6duId32EgyHo1b4CQhfCPVwJ7AAYpfIwqKIdOKldvFQtxRYEZEsSi8lhIxB3KNWLvZQiKSweKCmFggff4o9tPBLBqVsCR3mIPaIP-tZ8mxGbqRRvqsxJGOdIZ9Huws-koKbA1LhmyHJGlANbd4H-GwgLjS5cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جدید محصولات سایپا اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134730" target="_blank">📅 16:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی ارتش: آسیب به توان موشکی و پهپادی ما در حدی نبوده که عملیات‌های ارتش رو مختل کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134729" target="_blank">📅 16:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / آژیر خطر در داخل سفارت آمریکا در بغداد شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134728" target="_blank">📅 16:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
🔴
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134727" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134726" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm4z7NTt7kQ03tQxqgnw_7wEKMmEhSKqbBkHsyhUybKghmnD_vu9JTVk_KmTPFuColomjZvk0VOkHYZYWGhOb2oANgp0ow_Y6f3h5eOUMrPbrIyuRHazEZsbapV-PHWFkqwFZk8-0b9r_D0OCv5hE2S5hSMBDA58aFObfj2RfQ0M-gGEdLVkMZsYkDv9pwds1yLtNBvYmkt3U0kwDfoKjp4nvdkC-HDn1u_UKaC4T2x_lyoKk68exvqNtx0Wr4L_FpXkKnBEbSGb5AMhNuW7-Qsc0ANPXUhQCrEij8B62MjOfFEDYWXx0A7fDtTauW9sXejNYAPy2pwlRtt33Ml8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریگوری برو: عرضه فراوان نفت در ایام منتهی شروع درگیری اخیر باعث شده قیمت نفت فعلا بالا نرود
🔴
قیمت فعلی نفت با وجود حملات زیر ۸۵ دلار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134725" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
منابع عبری خبر از گفتگوی تلفنی بین وزیر دفاع آمریکا و وزیر امنیت اسرائیل در مورد جنگ با ایران میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134724" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز به نقل از منابع: حوثی‌ها اعلام کرده‌اند که در صورت هدف قرار گرفتن شبکه برق ایران، تنگه باب‌المندب را مسدود خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134723" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کپلر: ۱۳ کشتی روز گذشته از تنگه هرمز عبور کردند و تنها یک مورد از مسیر عمانی استفاده کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134722" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM916EH3FkwU1bHIbUvC31AvRnanVfuiTunRQVzCXAgvCmVVuTOhjUwa_jZreJMtHpfts9kmi-t_RyNzOjNTDF3Yh_SSkX4s-XLGmTz_nlCpxbnqhmtoLzm67wdIYA9mxNzH1Ba1zs22Bxj-DCIwVqfzQ0QZF-D4WW7o7BopQFD647yOVO-WFajpDlZ6WFXoIhVpi2WqKtjIDVFuxMfArBa1J9L_4E737_huF4jIfcvZi-RMaQ_XSbCijAcqrqJH1t413wP6TokdkSNKS-haZRI_TNyVQ6CUTJItkJyxwkNCWNyg94r6tE5slEXab7yluuii9MlkEhbeF8vj0g4JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134721" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: در حالی که اسرائیل در حملات آمریکا به ایران شرکت نمی‌کند و به آتش‌بس در لبنان پایبند است، نوار غزه همچنان مهم‌ترین منطقه برای عملیات‌های ارتش اسرائیل است.
🔴
در غزه، ارتش اسرائیل دامنه عملیات خود را گسترش داده و در ماه‌های اخیر، حملات خود را با شدت بیشتری انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134720" target="_blank">📅 15:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ثابتی و رسایی رو باید بست به سرجنگی موشک و زد به پایگاه ناوگان پنجم تو بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134719" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_igszQqJR-US6nhPNImotEyklOemFV2XRx4WsZNyPUkWyo2ndT_1tJmStH7u_g7v9Y8b5xtE8b1nSAYExoAR5eE0WsvNxy8Lthsj847byuU8krPSmKmXLaVsBOt-3Hdvli2lnyIjpTlPJAt7ATN85TXxw_FyAPb6xsRWXukkW1uw_O1ChonV7ATsZMSzyDtTWfUsnFoj_a1CwXtg9q9zVscArnNdrGuVf_lK_Dfra2hBknwGlmG3BD1WWttg9lxol3sLdogynvR0B18hfbWM_73CsCDKjPV8JYO9nRSU6Ak6h5JDxrThMrf6wN2UpZi7VLyVh7U_2HvUrsHb58Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی منتقدان خودش رو ولگرد خوند و نوشت ۱۸ماه جبهه رفتم و الانم دوست دارم برم جنوب
🔴
بنده ادمین الونیوز جلوی 950هزار نفر اعلام میکنم، آقای رسایی ....... هستی اگه نری جنوب و زیر بمبارون ۱هفته زندگی نکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134717" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F56Yy5vKRSntxztfhe8V9XZYg-dmNh1nQtopADEMEuH4wto2KE4GVcjteHxIWnJg-9ELWq7iJTXfubVySU-JgHxb9jKu7nfknG5pdG9ei4f6nRl25CmXYfGyptZxoQu-bGLub9SjVMqrZIu-vHP6LMQNdUSBQzpQyho3me-kX5-_aqZ1cErxZzMyO85H9yjt7P-Ls9xL4V7-poNZCp0tZQY7K7imbSyKRyMsC5mpkYoLLLlalpMQRj2dhtnl_7-BtD1XxdA9360lP8r851qUTIpqJE6Trn3KpN-56yZoObCbqjnFE3YjWFSuTqTo0ahyVfqY-fFsJj0WJRl_jDrXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
#بوتاکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134716" target="_blank">📅 15:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری اماراتی در آسمان جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134715" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJBUT1JDmOHR0dQ-YXGtHBq9-aqb3ojQmV1nkyM1aK7nvgiOMAFLw9uVQosy51tzOJbALTUVlzZaJMrUMOYe206ZMQRKeyxLkKHgTFFIk7AZVbVU4hJf6VJk8pLTfXDe4nK8p0OiMTxa20XWboBQ7M8nl04fGAcofQ8B84M5528yJi1cr884qyu22BwOKNtHJscFEQssu8zxnaqDMMeUPMUWsj3nM8OXLhdNDpbicvZkJ8iw-PRM8avxC_XXCrfN2oLE8qIWqMEAAhYY6TCRsd_fvoF_P5_4GcRqNdrhSoPNA5gklyJn8UNnssAH5k8L04Uf2utUkoiTkt4wAARvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حملات جدید به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134713" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم  #قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134712" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFxI9UHkBTmpIaUOKKY3LLabv9zBorUwV7pX8nHC8dqNpUygFbBT0Yd3ctqTj6LBAV73LOou5vFIVEQ_iyAXcY78AfA1G39o6vH3MZIR6Ed3xV978j6XBVvzsk_3pdxqnO8ARP_Miy82LS_Ckyzct0rHodnOIMm7-TAwuaIeTffqHlUPrvexwfPz8VOFFmuWENBYS1wxpuZmLy-KbBHZHMN2WwR75a_Cn_UWgjxSZQcnCCg-KjzsfV3mwjC90ra86tIvUocXUW5E2Q_ATpHTbxrB8GlOBcdhCUOZQm_x_2_bRHwae7jt5KL1V49L-CKgc8uqg9H3wFT-2UesXIpbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZDh3d7yrz8NA6SCSYIm8CS4s-OFD1N9NJg25FHE_G_v5jOC_1TwZVDOUJk2ekZiRKHu2tAbAm53p7og1XCPYGiab5LVA27QxI1wkW6DXsyZwcBSkd5bZBhoBt1FaLtJEDByw6pjuO37yjF6w-iDLQOSuL2jBZ_vE3MqHZYdhdpJI0_1pHV1FMuB8l4maQc0PiQlAsrHt9cw-1ud6IRCIGLtLPd5wFfqHS92VBY-iERIumv6SuVEMT8TV2eQX6wvhgpvfbq6UMjq-SNK9zvUWEkBeAeZF_dneSC4wGSjpA4Qujk0cPDATt16wwaks5MsxZU_Geie_sid19g9nE71Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی کارخانه مینو در منطقه ۲۲ تهران!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134710" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ژیلا صادقی،مجری صدا و سیما: همه جای دنیا مشکل اقتصادی و قطعی برق هست،مردم بعضی کشورا تا روزی 6 ساعت برق ندارن، مردم ما ناشکرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134709" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بیت‌کوین امروز در محدوده ۶۴ هزار و ۲۸۵ دلار معامله شد و اتریوم نیز با رشد ۰.۶۸ درصدی به یک هزار و ۸۹۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134708" target="_blank">📅 14:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb22f7q9UP9f4G_shXzXwnoKHq1ewoAmGSfO8waJG-VLuA5A1MBBL9YWYxDuSUlxbd80DLWfS8psp1zH5Oy1VbabX1WKZ_N3t8NI1cUnAYZt0N_ISQhzMaR-7Q6KS-xJ-OR4O13f6uHZHhpenFqmKVLZCNmRVwxrH0TEp-S27G2ojdORQxepdAyvWZLaE_sbrx0UV1oDXlFza5gj96zJ3lp8NnjKLKc0vrzp92aGY6m-fEIKJXAJ5V2Q9CUBc2M-FKPyvFLzvHTWY1NZCrK4o6ragRkJDP9g_cKL-m6ePfMLjfXXmxKCzwPbTCSB-zphDr5HSNzBTf4lHQRJAfmqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم
#قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134707" target="_blank">📅 14:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134706" target="_blank">📅 14:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5n-s5VMnACtujf1LB_ue4PZjmngrWLuUZwZXprtDC69GeXYAiiOalxqI0QQy3pRYzG6pcSUNrT4Z9Gi5LE4mZNqY1XiUyJEyFXMlfyRuM9NvgE8hWYzau27jVnAfmz2emMvHrfMQFccdAbxSf7cqzop1AG_wBcirk4K6IGpwHZsfPNY7AcaHK77cH3YZ-1VQP4gVzIb4rr-uVHwucPMVtbB19scDumHgxuNRDxV7v6Zuz3CR6aAQU-SRFrtxX-B18bNPo5uSQAKvTppTORku27egKdhB5rKEZFJba61993wCJg1OcKJBfOl1dP2bTaGNzXUf-ONsIdqr6OSIFPThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هم اکنون حمله پهپادی به کویت
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134705" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که سفر فرمانده نیروی دریایی این کشور به بندر لاذقیه سوریه در روز دوشنبه گذشته به منظور تقویت همکاری نظامی میان دو کشور و تلاش برای بازسازی ساختار نیروهای مسلح سوریه انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134704" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره: تردیدها درباره نقش پاکستان در میانجی‌گری میان ایران و آمریکا افزایش یافت
🔴
شبکه الجزیره در گزارشی به بررسی تشدید دوباره تنش‌ها میان ایران و آمریکا و آینده تلاش‌های دیپلماتیک برای مهار این بحران پرداخته و نوشته است که نقش پاکستان به‌عنوان میانجی میان دو کشور با چالش‌های جدی مواجه شده است.
🔴
بر اساس این گزارش، پاکستان که تنها چند هفته پیش توانسته بود زمینه تمدید آتش‌بس میان تهران و واشنگتن را فراهم کند، اکنون با فروپاشی تدریجی همان توافق روبه‌رو است. درگیری‌های اخیر نیز برای سومین بار آتش‌بسی را که در ۸ آوریل میان دو طرف برقرار شده بود، در معرض شکست قرار داده است.
🔴
الجزیره با اشاره به دیدگاه برخی کارشناسان می‌نویسد که پاکستان اگرچه توان ایجاد کانال‌های ارتباطی میان طرفین را دارد، اما از ابزارهای لازم برای تضمین اجرای توافق‌های حاصل از این میانجی‌گری برخوردار نیست.
🔴
در ادامه این گزارش تأکید شده است که سرنوشت بحران، بیش از آنکه به تلاش میانجی‌ها وابسته باشد، به تصمیم‌های ایران و آمریکا درباره تنگه هرمز گره خورده است؛ آبراهی راهبردی که همچنان در کانون یکی از حساس‌ترین و خطرناک‌ترین منازعات ژئوپلیتیکی سال ۲۰۲۶ قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134703" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd3dpajRakqov9DHmh8sCmt3kuqfQ3fOcizhiUQrZ5Z8munaPZsVsNbyLsIfpzrs61nnlb1jmyBz2k4SnuGmKfoeC8IGYD9jSLAh2-E-G_g35Ga-v7gPIP6CjD_ltHhOXLTWpwRT9IDLPZWM2OGCHFifLE-m--EcJLvEfxOhE3RQztDHklnq_OY7UFcTnXBmR6s4b-ls1mOtGNyiv_mNl1f8Ai2GN3t0afDqCLHQ947T-8PJEn02x3WFToWwgzuLoWzQXRS7_uzDu7jMqx7Z5acWZELxLbLlVr_h16ydYSSTSZQaKk2SjoCeB9tks0d4yBukJ1yvfDg7DyDrekHaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار مرکز پژوهش‌های مجلس: نیمی از روستاها زیر خطر فقر می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134702" target="_blank">📅 14:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کاخ کرملین (روسیه): با ایران تو تماس هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134701" target="_blank">📅 14:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گزارش ها از اختلال در ایرانسل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134700" target="_blank">📅 13:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaOPg0cFO2-ao-LxkkyJeZuApgsKKspKPZDDqOcaQdQyqevm7-vVG4OOSQYss5fwQAt66tuI3l2shPHN71EZV4bNjMIEDQrZGC6-Q_CuvAnxjHpGfwCMVfuloHffsnRWGkARw8KpctXrJenv_ADDoyYCBuZvR1FbxN5rHWyooM1OfuyhvYC5T3grkqlRp-2IzmMup3GwkE9BGKwsQov2vsPezXWdFzZg0r2y_dRCoUR2k9F3rR7qgZ3goro9vx6Y8YzS35Zo7tIG549YoLZt11vPmL-k3UnTkFRm6gvoWLWXHicYXz7cHqOM8GVxIhL0dOSWAKmB6QxHYb-gwIgefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین دیوارنگاره میدان ولیعصر با اشاره به مرگ سناتور لیندسی گراهام: نفر بعدی کیه
🔴
حروف D و T در متن بزرگ نوشته شدند که اول اسم و فامیل دونالد ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134699" target="_blank">📅 13:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YClWd7Y9MoaL__uqwr94dvjTH0utOEDguFonbjkez-gkLSCKEUdFQOZ1N71NqRcYm-8cmajqx_VFHXc2IMg69JAQbtRcqyEgvtbdG4sq4gJ4Vqny9v95ykV4ICnPWKj4xkXBal-va-sKh7IhJJ2ub6NLstViGcr1bmZaNdq9nEVHenCdOHVjL3qGRbg4dqb699Dpb1Ch0JoTD6B-aNhjrpQowqFI_ChKu1Y-9sPaQ528bAiC1QeL4mQQ5NCL1FVNPDyF1EgUY28FBEDWgF_6t8hJScYK3I6taoGFwhUGu4xIr7VwcrtRRZPkrf7OB_ijSeCZ9wNPUvm6tdAcB8M5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از احوالات روس ها در جنگ با اوکراین، نقشی سوخویی که برای فریب کشیده شده اما روی همان نقش هلیکوپتر میل گذاشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134698" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سفارت ایران در لبنان: تنگه هرمز جز با «شرایط ایران» باز نخواهد شد.
🔴
ایالات متحده باید این واقعیت را درک کند. یا از طریق گفتگو یا با استفاده از قدرت نظامی ایران که آن را مجبور به رعایت «شرایط ایران» کند، راه دیگری وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134697" target="_blank">📅 13:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134696">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کاظمی، وزیر آموزش و پرورش: برنامه آموزش و پرورش برای سال تحصیلی جدید، برگزاری حضوری و بازگشایی کامل مدارس است. به شایعات فضای مجازی دقت نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134696" target="_blank">📅 13:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134695">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqqZt-h861O8dOkiM3PoP1NbZi2EHbQY1XjkO_TslWHFU_3OxxXxZoANImzu-xGCEyl6oCK3nn8ZVsaNlmOklmzT2jjB5GBK7gi9bBo2Hcs7S36hJBN4YeQ-IsPXFniXcIa1yBuej_7xjdjuIb58MYI5Iu5i-tOxs_Z3QkpwgOz2dNrX1GZUZv3osuRGgPbG9OlNsQPKaPbIBJCRaEQMk0uMED2OxT3keZWqVsAgkcBU44YZnhLsnk05GSiDyal5etfNB59v3OmQ5m04LmS8r9QTouu4_NEcGZh_1L2g6Jxh5gPZiwcGP-TFzoipn_R4X21p0R2qsQEbOdyfU9By8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: از لبنان، سوریه و غزه خارج نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134695" target="_blank">📅 13:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134694">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
الجزیره: پهپاد به نفتکش در آب‌های عراق اصابت کرد؛ صادرات نفت بصره موقتاً متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134694" target="_blank">📅 13:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134693">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی و نفتی عراق: یک نفتکش در بندر بصره مورد حمله پهپادی قرار گرفت، اما خسارتی به آن وارد نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134693" target="_blank">📅 13:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی ایران:  گفته می‌شود حدود ۸۰ میلیون بشکه نفت خام در این بازه زمانی(بعد از امضای تفاهم) به بازارهای جهانی تزریق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134692" target="_blank">📅 13:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozzgdrO1CIXRFzRV_FxaI8Ow4CYjJzobWeBigTRhFibpknCwFFGSAIQD593uTFyCT9PVH0xqAkPEz870JsHvpWdpSbESNFZEZmYwWDw0rZlhesx1EbsW4AmmfUB2CW4GrWZFcLQj1tPiMqOkBMpnoFl2vNStU8JMnhc0kto8fExiKl4h4s3YSmAutqFxc3qnMR7J-er_Jl0fJ0uprH0ShvaMiSIql90q7bH07KU-_EKu2sKgXj9r4ayZbxYmBwT_BjdMDtYMnN9gAFh_EvgxThYe1p2Q_rxpBvTZSorRT_E2aCbPP66KDRp14clqufIfiHTP1BJi1VkHKh-cK5xNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افتخار ایرانی‌ها
❤️
انتخابت رو به عنوان داور فینال جام جهانی تبریک میگیم و ایشالا خار بشه بره تو چشم لبنانی‌ها و عراقی‌های مقیم ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134691" target="_blank">📅 13:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عربستان تعطیلی سه روزه فرودگاه بین‌المللی ابها را در پی حملات دوشنبه‌شب نیروهای مسلح یمن تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134690" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134689" target="_blank">📅 13:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=p3qET4yLfHgQ26Xyn-YM-y70LgeInMoDmRIk525pY0udHE88owV6GOPal-UKIZja-gR2g-Vp8svlaYfvfwrLYIwZ49i3D3dir3uU41aJd7kv3Wtgvrp9mSi8Z6_QkBxx2MkWIc9unre5-KArMuLyK9TSP-0iIrW3w96-Z9Gg9nWYELqEewPJsc5aBMSuLL2ni_q0xoNOmjjxJCqGr5NVro8Yja6dRbgnAsi2FmtTzoFajrat9Sop6NO5VN5jPbyry_KoM5Oz5CDa5R-lJM7--vaDKLlP9AcWu9o35lzntOh9Xp4Fm5_k5uhnf1anNTa-Dq89e5S1hMnnkCkpFTURBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=p3qET4yLfHgQ26Xyn-YM-y70LgeInMoDmRIk525pY0udHE88owV6GOPal-UKIZja-gR2g-Vp8svlaYfvfwrLYIwZ49i3D3dir3uU41aJd7kv3Wtgvrp9mSi8Z6_QkBxx2MkWIc9unre5-KArMuLyK9TSP-0iIrW3w96-Z9Gg9nWYELqEewPJsc5aBMSuLL2ni_q0xoNOmjjxJCqGr5NVro8Yja6dRbgnAsi2FmtTzoFajrat9Sop6NO5VN5jPbyry_KoM5Oz5CDa5R-lJM7--vaDKLlP9AcWu9o35lzntOh9Xp4Fm5_k5uhnf1anNTa-Dq89e5S1hMnnkCkpFTURBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا شب گذشته لایحه توقف کمک‌های سالانه ۳.۳ میلیارد دلاری آمریکا به اسرائیل را رد کرد.
🔴
نکته قابل توجه، رای مثبت 103 نماینده دموکرات به توقف کمک‌ها به اسرائیل بود. موضوعی که به هیچ وجه 10 سال قبل قابل تصور نبود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134688" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCdmQ1mKdk5q-OUbLqoDf9BH6cuFUdrQNj9MVQT8GZu1sAzBi1PtjrJQnxs8EeIuhFqK2sNtmUMinhi9FI2KvrbHDBKOFqcucHmSxwaLv9YtCP13zBPk7LNiOdMnGjJwGQnAJl_rLV_CK9wVJNtrAm4eJhs3g198_iakrC0QWbLBi6g1xXWzWEXBU4dIcfFu6ItkzfvEAaFIQ5ulbqQpDZA84Ex29V4YGPWJ-ItpdlFoZFp5jVj-RxrqdQgtb6uqX0pdk1AOAaj0GYEYRAAIvgB-b9AWec_Ves9iaTAVa6SDc2jkgOhwXJd-Qziov98M0Qw4yQm1oPVLQEJp7eXepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده از سنتکام، از حمله دیشب به یک دکل ارتباطی در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134687" target="_blank">📅 12:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJnVekd3nCLV2Z74hQATLIBvxl9XwqNG2P6teXFN0pMEUmRdmvzB9N5_Fcklfx8zTAhikT6xr70D1Hq6umg1JSGO7VbPa8qwmBCltwyVmudl8TN6C2dwjLK-iB8Su2Ey69l6uFS81epPmZPPDHl8LUg6yvANmSy4hloXgCrGSGerdHBHxT3rxG89qpwppjA4EP-hUDQLKdV-DuwUUOxAmEhrvgntL7S3OAv7IHGdnl_itZHo6J2TH51sIpX2fuD6iiMeLBQqTdKjTNxASKgsoWC1AwfQYfs8cfAbhH-yzKX1qzpNqMNJriSjiD2lfSOHXc-OR_qIdRTUQNnDD7Q1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز گزارش می‌دهد که شرکت‌های کشتیرانی پس از حملات اخیر ایران به کشتی‌های تجاری، به طور فزاینده‌ای از مسیر ترانزیتی تحت هدایت ارتش ایالات متحده از طریق تنگه هرمز اجتناب می‌کنند.
🔴
یک منبع کشتیرانی با اشاره به ایمنی خدمه و بدتر شدن فضای امنیتی گفت: «به نظر نمی‌رسد ایالات متحده هیچ کنترلی بر اوضاع داشته باشد.»
🔴
در حالی که واشنگتن مدعی است که تنگه همچنان باز است و بسیاری از کشتی‌ها با هماهنگی ایالات متحده به عبور خود ادامه می‌دهند، شرکت‌های امنیت دریایی هشدار می‌دهند که هیچ تضمین قابل اعتمادی برای عبور ایمن وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134686" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

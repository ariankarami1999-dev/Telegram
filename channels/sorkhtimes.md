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
<img src="https://cdn4.telesco.pe/file/kO5wo2Xiam_6EBm5rbR9NigpEKHHbnTcb8jTCfBQiyqL1i6dDmr2VugHhEiWtEjXBPcjHL6p8RBIepY2gxKyDyxf8d9mOY9IUiVj7vhK5AzSTjNlB4msxSHwzEkIEhe5SBFqn3bp52rekiIfaTKW6R3OOAynLQzKZ8LfDzTqSf_U0t9Ryxk8I1iywrEQooX5XoZ1MRUsseR3PGZN2nIddxy6UPo9j1XkgXFJHAvZ7CGCPkXK4AWxrYIw-X_4fqY6CnKeP_-1j-grzSBdcWRE2FBQgTKIdcxkdAOL660Ulr9rNETBUUMGwyAPJxVG5bUCQRAWVs67D3hL2L1fo7qz4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/134667" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2UbMWxeVFbUFzz42GhdtyGw_0nfgZ99yKhLPJxjpFLm235_N62Mfi1L7IpK1Uwb08xv9Yp5sr1U7uSCjECRRocqwIhmFPsML3ptwEFo7K_eliHNSdZJFMUaAQVPZafnMF6R8958WieUIgAVDYrtgklDGY2dB96kxJ7mtbFRgveUTyJyaEYfpGu1naLBg6EflH1wgZR_ydbOW7zaTWFEClA41wKsfS8o8xedaMhFnfl8Fol4m3DHHgVbVDxJVjsuC8FT8KsOzlXRcT-2-FMzUqS7M2GNraFv4G02uDra5sQifSmA5uPfxKl8eXY9YDqHetoPxdKQBq7dSL85YcN0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از جام جهانی
🏆
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
باضریب
⬅️
3.42
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SorkhTimes/134666" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
اوسمار به باشگاه اعلام کرده به رغم دلخوری ها بابت قرارداد سال بعد، شکایتی از پرسپولیس ندارد.
📊
به گزارش خبرنگار قرمزآنلاین، اوسمار ویرا امروز در باشگاه پرسپولیس حضور یافت و جلسه ای را با مدیریت در ساختمان باشگاه برگزار کرد. علت حضور این مربی برزیلی، ظاهراً…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/134665" target="_blank">📅 19:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
خبرورزشی: امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال ۱ میلیون دلار (معادل ۱۷۰ میلیارد تومن) پاداش گرفت. ۱ میلیون دلارهم بازیکنا و سایر اعضا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/134664" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
شایعات؛ چکی که زنوزی به دانیال داده برگشت خورده و شرایط فسخ کردن داره و خودش بدش نمیاد دوباره با اسکوچیچ کار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/134663" target="_blank">📅 18:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
تیوی بیفوما برای جدایی از پرسپولیس خواهان 350 هزار دلار شده است
🔴
همچنین این بازیکن پیشنهاد بازگشت به استقلال خوزستان را دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/134662" target="_blank">📅 18:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
تایید شد
🔴
تیکدری به پرسپولیس پیوست.//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/134661" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها :
🚨
باشگاه بزودی با انتشار یک پوستر، از مهدی تیکدری به عنوان اولین خرید رونمایی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/134660" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
اوسمار به باشگاه اعلام کرده به رغم دلخوری ها بابت قرارداد سال بعد، شکایتی از پرسپولیس ندارد.
📊
به گزارش خبرنگار قرمزآنلاین، اوسمار ویرا امروز در باشگاه پرسپولیس حضور یافت و جلسه ای را با مدیریت در ساختمان باشگاه برگزار کرد. علت حضور این مربی برزیلی، ظاهراً…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/134659" target="_blank">📅 18:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7wK4DbNjWZjg8s0ByzpaGMwmhzEIkFBh9c-PN9MKFk3wwA-1SNh1ny-gGjdOf7PvQxr8570iBbKCf7iLHcycV1fdezkTIXMOq0i8kP_Idk0E2QhuaSfJ2NcBNp64Wl-paJ-oVG1xBHZ47ShNCyafoCS8VkX8Qv-uIYwxCJtR0xT4WAfH0Dh-PvcCJ7yIAFnzWGTLMgCIbfD9VvzjRLO8x5fNGby5qfu6oL6_fnhzY-HWm4AjqRYgg4H_UGXf9KBYpQWW7QYlz4SU8vzS2TNpxBN-bHPvyv9l1393cO7NR77socLfkBxhY4umQthBscs3YifQo_zeuTu7IoNlwT0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ادعای فرشید حقیری!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/134658" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNk4rrpULbwXYmEsN-eDX4urzfC6eNhPCw2GmJmKKA1C4xEQ-vAw3lwYaUpP_sKyXWzSpeXDpFIwWz8is5JKF7cZcT0SpW8PoyopRPfFunpwtM-HyHPqvshyX4ryPhfvmw4b2tNxjvVq1m1zIqlw6ORFSyVny9XmQ_ch-FWXSQNwcaiN4u6rpk_nKKftIi6IYxYX3_S9DnlHaNU0Zqx4lXYGi5DCZz2tJNCyeAkKrbrc_2CJdKfKACY5VyB54cenxuwvctrI_hrbWTmn2lfqEKdql5gD9eMN-b0oflrWifSqbbX1SqepEmdMjFapCyK5exuAcguFvFnm2NJoi1hFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
تیکدری را پرسپولیسی بدانید. طبق شنیده ها تیکدری تا 48 ساعت آینده وارد باشگاه پرسپولیس خواهد شد و رسما از او رونمایی میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/134657" target="_blank">📅 17:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
طاهرخانی: اوسمار ویرا سرمربی بعدی تراکتور سازی تبریز هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/134656" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134655" target="_blank">📅 16:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
پایان اوسمار در پرسپولیس/ اسکوچیچ به زودی سرمربی جدید سرخپوشان می شود
🚨
🚨
مذاکرات باشگاه پرسپولیس با دراگان اسکوچیچ مرد کروات با نتایج مثبت به پایان رسیده است. اسکوچیج نسخه ای از قرارداد را در اختیار وکیلش قرارداده تا آن را بررسی کند و از سوی دیگر باشگاه…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/134654" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها :
🚨
باشگاه بزودی با انتشار یک پوستر، از مهدی تیکدری به عنوان اولین خرید رونمایی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/134653" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
❗️
تیکدری: پرسپولیس؟ پیشنهاد همیشه وجود دارد و امیدوارم سرمربی این تیم زودتر مشخص شود تا من هم تکلیفم را بدانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134652" target="_blank">📅 15:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
غیررسمی
📊
اسمار ویرا با جدایی از پرسپولیس به عنوان سرمربی جدید تراکتور انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134651" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید:
🔻
روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است.
🔻
روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134650" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚡️
⚡️
⚡️
🚨
فوووووووووووووری
⏺
اوسمار ویه را با امضای تفاهم نامه ای از پرسپولیس جدا شد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134649" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/134648" target="_blank">📅 15:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
شایعات؛ چکی که زنوزی به دانیال داده برگشت خورده و شرایط فسخ کردن داره و خودش بدش نمیاد دوباره با اسکوچیچ کار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134647" target="_blank">📅 15:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134646">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/134646" target="_blank">📅 15:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134645">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3be099de2.mp4?token=NQh4tCOVvjqXlRGC4NZaD7MOCKUdSW5YZR1dEMc36F7GT32d_9zjoq0K-FLAVf6eLVyNxoDqW1lylRuG9FB6FPWTv3Y-mje1x33k9H74RzaD0kO1N9YvViB7tockNV4UlamfRW_5ALZLcJpGHljUjsc6CwGrCA9bzJ4m8F1jFM5qk1UP_gUDApEvzZ1yelKprsbzqhzcbVzTGVzy3qT-o5fFr60vvbKkUW0cTJWokjPI5r4P3ZoOfg3-lsTySRrbHVFtPXJ-7iUARoKQeWZamGJmTWR47ex_HndD3FjDIDvo7c0sDJRPT20b5xtyz0JfNzrDCoJTG7OJ-DfLjz2NNT17sjMINpvk3zw0v_u8ojui_tgFAjtV-moMxJQ6Zyx9q_7Ht3IpHWmh-UBt2NVthLBBowzMg4o3AHpigZeZ-787C7cEbQgP9qD1iVUrD4Q8oYVyibMjjXe2jpYwgbV5JG71bP7zY_L5rfwPobUnFbg1k5MNx2fQmJ2QS54s9h5ZNmI2OPa0g8fXmpKCykmWT21JFZeW0Azf8bsQgTRsnzLhjTqF9SNfq2_wLA1vDd-filfxIo0RcawP0rRVVkbCPnxleqhAdgdS6M47v88rMkLvEyHCT1Fw09s0oigYqU3QK-0BIDfkbCFmV0rf2kCWm8GTK7kM9d5yXANXG6U3XCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3be099de2.mp4?token=NQh4tCOVvjqXlRGC4NZaD7MOCKUdSW5YZR1dEMc36F7GT32d_9zjoq0K-FLAVf6eLVyNxoDqW1lylRuG9FB6FPWTv3Y-mje1x33k9H74RzaD0kO1N9YvViB7tockNV4UlamfRW_5ALZLcJpGHljUjsc6CwGrCA9bzJ4m8F1jFM5qk1UP_gUDApEvzZ1yelKprsbzqhzcbVzTGVzy3qT-o5fFr60vvbKkUW0cTJWokjPI5r4P3ZoOfg3-lsTySRrbHVFtPXJ-7iUARoKQeWZamGJmTWR47ex_HndD3FjDIDvo7c0sDJRPT20b5xtyz0JfNzrDCoJTG7OJ-DfLjz2NNT17sjMINpvk3zw0v_u8ojui_tgFAjtV-moMxJQ6Zyx9q_7Ht3IpHWmh-UBt2NVthLBBowzMg4o3AHpigZeZ-787C7cEbQgP9qD1iVUrD4Q8oYVyibMjjXe2jpYwgbV5JG71bP7zY_L5rfwPobUnFbg1k5MNx2fQmJ2QS54s9h5ZNmI2OPa0g8fXmpKCykmWT21JFZeW0Azf8bsQgTRsnzLhjTqF9SNfq2_wLA1vDd-filfxIo0RcawP0rRVVkbCPnxleqhAdgdS6M47v88rMkLvEyHCT1Fw09s0oigYqU3QK-0BIDfkbCFmV0rf2kCWm8GTK7kM9d5yXANXG6U3XCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
مراکشیا کف آمستردام دارن جشن صعود میگیرن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/134645" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134644">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/134644" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134643">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/134643" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzKB0whBjii-BE_rGcj8JpY9UkFXEMEeN-23NJJraZIKcP3KMJaYhsHiH-JFD0D3srfQuSrynnJfwga6Pd6pH4ndIA-JkDx8Ftwqoqw34mKldGp3r39PsbzbM219nZkQtYslscEENeu68yytJuXQtzMRCvKEieylv0Sb-Eu_wUd9Eo8jvobdEIDJwKzMVDDoZgTF-SJTjv0v_8Yjerbtm2dckT2K91mXN6_PZqHSK8C1qUZpIk5TcGyk64oFzkgaIm0NZ56cqrn2WUZ11GQNkOdkvBjoM5qMj6xlpOVl6kaX1wthXHZw75OacXkrwu9xiiY7ugPFe0Xmx7s46Xz3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
کریستیانو رونالدو دوتا هواپیما پر از تجهیزات و لوازم پزشکی به قربانیان زلزله در ونزوئلا فرستاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134642" target="_blank">📅 13:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134641">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134641" target="_blank">📅 12:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
پیشنهاد تاجرنیا به بیرانوند ۱۰۰ میلیارد بوده ولی بختیاری‌زاده گفته نمیخوامش و از بین حسینی و خلیفه یکی رو بیارید.
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134640" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134639" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
مهدی تیکدری از گل گهر سیرجان جدا شد
🔴
تیکدری برای عقد قرارداد با پرسپولیس متتظر تعیین و تکلیف نیمکت پرسپولیس است!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134638" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134637" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
برگاتون بریزه؛ بعد از اینکه شاگردان قلعه نویی نتونستن تو یکی‌از آسون‌ترین گروه‌ها صعود کنن حالا فدراسیون میخواد به هر بازیکنی 20 میلیارد تومان پاداش بدهد. دقیقا این پاداش برای چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134636" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
🔴
فیروز کریمی: آقای تاج، حتما باید فحش خارمادر بشنوی که بری؟ یا روی برانکارد؟ باز میخواد بگه دوتا میله کاشتیم؟ بهش آب مناسب هم دادیم تبدیل به گل شده!!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134635" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
پایان اوسمار در پرسپولیس/ اسکوچیچ به زودی سرمربی جدید سرخپوشان می شود
🚨
🚨
مذاکرات باشگاه پرسپولیس با دراگان اسکوچیچ مرد کروات با نتایج مثبت به پایان رسیده است. اسکوچیج نسخه ای از قرارداد را در اختیار وکیلش قرارداده تا آن را بررسی کند و از سوی دیگر باشگاه…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134634" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134633" target="_blank">📅 09:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134632" target="_blank">📅 09:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134631" target="_blank">📅 09:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
برخلاف ادعای مدیرعامل گل گهر، انتقال مهدی تیکدری به پرسپولیس نهایی و قطعی شده است.
✅
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134630" target="_blank">📅 08:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134629" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134628">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134628" target="_blank">📅 08:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">من عضو کانالشونم، تحلیل‌هاشون نسبت به بقیه واقعاً منطقی‌تره. پیشنهاد میکنم حداقل یه نگاه بندازین.»</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134626" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksN5jmttbFhhahDcL1LhJ7MJs3wiU49NFfJLUzI2oLrbLHLp7uOh44iM_XVTMHftkNR024iOJ8XdkmH6eiQwzM36enqXXV0gJQe5OpEq6AmBUwuehhlXLa2fzldUcxY0JIf1LMjIdSBQFv56e1jqxzyzPfWjBAnxf8SK4lP_NkwJJ-gKMWJAzq6nD3j4SHIXS0ShKggEwNvSQU_ZmRV07sh_CiDgsq8Eq6b8wWQDGfl04gZXOJau7hPpUDuYbkJ4HYOq_H-HfvYUz1jUTd7w6CqE5WAbNXMl4AKF5bir-puW0kiBJFgXEXdAvMUJ5jJvSX3sC0DgDkF3A-7s0l9PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+LTqi6B-mG8kxMzU0
https://t.me/+LTqi6B-mG8kxMzU0</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/134625" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134623" target="_blank">📅 00:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134622" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
فرهیختگان : باشگاه پرسپولیس بعد از برگزاری نشست‌های طولانی با ایجنت اوسمار ویرا در نهایت با او در مورد مسائل مالی به توافق رسید.
🔴
🔴
توجه به این قضیه باشگاه پرسپولیس فقط قرار شد طلب مربوط به قرارداد این فصل اوسمار را که حدود ۳۰۰ هزار دلار است را به وی بپردازد.…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134621" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
استوری جدید فرشید حقیری : امید عالیشاه از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134620" target="_blank">📅 23:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134619" target="_blank">📅 23:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134618">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
کریم باقری: ما بد بازی کردیم و باختیم/ بازیکنان مقصر شکست هستند؟ در این یکی دوسال پرسپولیس شرایط خوبی نداشت آن هم به دلیل تغییرات زیاد است
❌
آمدن اسکوچیچ به پرسپولیس؟  تیم ما مربی داشت که بحث اسکوچیچ شد/ این موضوعات فقط حاشیه سازی  است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134618" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134617" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbbo1UQmFML_LDzgofY3tzcMilHRhAX8dDf0vTgaojU00J1d8iKdEsPIejMvDHmNNA8yhlLGwu5fkbZ83m0QCcgrdK2Q7fizh71vvzjOdPUmraAtv1NcYDu5NLVY0Glni80WhMVaT3bnB3oIttFkRfIndBbbjr_gRdnLh9WfXOAyVYI7bOFnV7FcCtH-N1vgq7KDtWMhwgmZU9qsaE0tnLwnVZRqh1JHjbEmV3Xl9Sz9TUQO9GES2-HOYgH-5KzLAhTjVw76_cigNR0sIW7cchB7oZcA63Xka0gabLFP6g5Xn4HGkTMvnMrHD2V6OJ_B4u21TBV3rm53oRxuWO3gyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
میکس VIP  از بازیهای جام جهانی
🏆
🇧🇷
برزیل
🆚
ژاپن
❤️
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
باضریب
⬅️
4.08
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134616" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ضربات پنالتی دیدار چادرملو و گل‌گهر (۲۲ ضربه)!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134615" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134614" target="_blank">📅 22:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134613" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134612" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134611" target="_blank">📅 22:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
خدا لعنت کنه بازیکنان بی غیرت مارو که حذف شدن وگرنه امشب قهرمانی سه جانبه ما بود و رفتن به سطح دو آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/134610" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134609">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
پایان 90 دقیقه بازی چادرملو 0 _ 0 گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/134609" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134608">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw-6Yh7twmQn_nT7fJKH08hxJ7ZOJsMGKHOpaxjL4qRXoBFGh9vCbbpBzNGtqj4UjKkAhsGUC9rOoiVu8uSiMjz4AsR9ydHYI8n1qNuOw2GXS25mHn-XABB__7T_yNCU-xZnUMQBZhubIhXbeJ_Kb1jZ8i64VMtotCFjzUAyB-mfccL5x9l0sbLNxecjqMt24gQCg_Z3PtNA9gnECm7RL0-Pks6rPzw1LgDIk4II9FaqJD-pmhbKWNj5eE6CwzBcEdwrost519rIZJU7kBPDTI2N5o0gaqSsL1TUBXCYpL8S7HmqfPrt2orzbMR5QQ870ZsCHfGm6W95juSC5mGNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل قاسمی دومین گلزن و بهترین پاسور امیدهای کشور و ذوب‌آهن به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134608" target="_blank">📅 21:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔖
🔖
تیم‌های چادرملو و گل‌گهر سیرجان امروز ساعت ۱۹ به مصاف یکدیگر می‌روند تا سهمیه سوم فوتبال ایران در لیگ آسیایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134607" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134606" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
آقای قلعه نوعی .یاد بگیر از ژاپن ...بدون اما و اگر صعود کرد و نیمه اولم از برزیل برده بازی و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134605" target="_blank">📅 21:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134604" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134603" target="_blank">📅 20:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
زیبا‌ترین گل‌های جام‌جهانی 2026 تا پایان مرحله گروهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134602" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134601" target="_blank">📅 18:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🤩
🤩
🤩
گفته می‌شود مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کند تا طرفین برای جدایی به توافق برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134600" target="_blank">📅 18:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6_dZhfJ1mBRKBR369itr8XxWBO-hRuxHZX_Pr4_mKck50qRF4dLc3x0if9KxNqZAeHe5-2FLuo-TI1EBRIdiTg6sNZ3xpqB284R5QNpwULdPZjkJSH_HFbzLV2nm7RRJIRCzb_HF8GFNpKmu1Fhq7VYcK0binSkpl9s9xWwzHWpHAARydDjctUi6I288in1AIMySWYF8ncqhVyrZ1AB7HwZGAztueNXeuDZjInxwwThkFZuQ7_Tie3b3cLZW2Xm17oT08zObreNp1TSm2cINWWZR0spNAwQwcsbc9oOUdiEkeUPGW6KfgfBtrq4eI8WSRdt2GBD7-M7w1BPaRH8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته فرهیختگان، باشگاه برنامه ای برای تمدید قرارداد علیرضا رفیعی نداره و این بازیکن بزودی از پرسپولیس جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134598" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134597" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134596" target="_blank">📅 16:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
❗️
میلاد محمدی ظاهراً دوست داره برگرده یونان. از اون طرف، مدیران باشگاه هم خیلی تمایلی به تمدید ندارن و دنبال جذب رزاق‌پور هستن اما اسکوچیچ به سبک بازی محمدی علاقه دارد و شاید با توجه به پافشاری سرمربی مدیران باشگاه راه چاره‌ای جز مصالحه با میلاد نداشته…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134595" target="_blank">📅 15:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/134594" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
غیر رسمی: اسکوچیچ فردا بعنوان سرمربی پرسپولیس رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134593" target="_blank">📅 15:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJrsLpSdNZtMMNF22C-s53uV87BvQwYjeqpbyeZWQ2PsIMS7azVvfe8GOCoqDGiftcYJaI7PJ9NVcDAhi0m3vy2bZYYUx4vmGeQbahfZnGNwn6fnG8lqRMTSTdoOACuhJqsRIgHUMJPaxWhz_YY-Pm3jBlTK-iI5Azx1MhpFiKwJIOkGin8qz0vDDcXQqywq5XZDX2spI5D6FcdAGVUj4Wq4hvr563E5HH0KTLC7EgTcjVArALJP5xTAu9fR1boCNlJl7ft4obaqkL8EGp5Wl1x4xEyEnUyUu2dBJ8_CaohaIsMrNO1udIfe9fUGo4as8EAs8ipK8ylGN7F1GPLaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/134592" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134591" target="_blank">📅 15:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
تراکتور بعد از دانشگر و محمد مهدی محبی اینبار رضا غندی پور هم جذب کرد ..امیدوارم باشگاه برای جذب بازیکن دیر اقدام نکنه ...چون بازیکن خوب روی زمین نمی‌مونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/134589" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
محمد مهدی محبی با قراردادی ۳ ساله رفت ترتر و بعد از ممد دانشگر دومین خرید ترتره .
🔴
مدیران ما هم هنوز تو خواب زمستانی هستن .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/134588" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134587" target="_blank">📅 14:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134586" target="_blank">📅 14:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134585" target="_blank">📅 13:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
با اعلام مسعود پزشکیان، 6 میلیارد دلار از دارایی های ایران در قطر آزاد و به ایران تحویل داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134584" target="_blank">📅 13:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
استقلال رسما با ارسال نامه ای به وکیل بیرانوند پیشنهاد دو ساله به ارزش ۲۰۰ میلیارد داد./ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134583" target="_blank">📅 13:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134582">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🔴
🔴
چرخ گردون، گاهی با توپِ گل می‌چرخه، گاهی هم با پرچمِ آفسایدِ کمک‌داور!
🚨
همون حسی که اون روز به ما دادی، امروز با یه آفسایدِ شیرین برگشت پیش خودت دیدنش واقعاً تماشایی بود
🚨
اسمش کارماس شلیل زاده
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134582" target="_blank">📅 11:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134581">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bllC3LWmBiWAKfcC8n07NpraxlKi5HckvxLLd5ZUEjnTbDIEW8pWGCGqJOoGaSx0oHnkFYFsfE11PyURmbl06dndMLQj3BGKvcAV0kH-Ve_uQKsKbHa4EQ-8_vEtegYYj_WVYGmENiutYpPorAWjddV8gYXA4hOagvfJeaodrnC2eKXSqZEcpbwtTkV4xpemGPdAxom96DzfcqdlaZcQozvmrjjt0FmKckJEg-yye-_tdfT1gMh6b1xOr_ZTsSXJju04xRkH2eVY3isY-8WyPewXEIZqWxcOaTnQQ9j4NEHbRFnQWdvJTkGskMcTkgOenvEaFzkSYLM1vZucSpj3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔴
چرخ گردون، گاهی با توپِ گل می‌چرخه، گاهی هم با پرچمِ آفسایدِ کمک‌داور!
🚨
همون حسی که اون روز به ما دادی، امروز با یه آفسایدِ شیرین برگشت پیش خودت دیدنش واقعاً تماشایی بود
🚨
اسمش کارماس شلیل زاده
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134581" target="_blank">📅 11:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134580" target="_blank">📅 11:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134579">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
🔺
اعلام زمان مسابقه دوم پلی آف آسیا
🔸
مسابقه دو تیم چادرملو اردکان – گل گهرسیرجان  ساعت ۱۹ روز دوشنبه ۸ تیر ساعت ۱۹ در ورزشگاه پاس تهران  و بدون حضور تماشاگر آغاز می شود.
🔸
برنده این مسابقه به عنوان نماینده فوتبال کشورمان در لیگ قهرمانان سطح دو آسیا به کنفدراسیون…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/134579" target="_blank">📅 11:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134578">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/134578" target="_blank">📅 11:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134577">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
عراقچی: موضوع هسته‌ای، رفع تحریم‌ها، بازسازی و پول‌های بلوکه شده در یادداشت تفاهم آمده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134577" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134576">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🔴
قرارداد اوسمار دیشب با پرسپولیس فسخ شد و این سرمربی برزیلی از پرسپولیس جدا شد.
✅
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134576" target="_blank">📅 11:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134575">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/134575" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0b066411.mp4?token=aM9Gh02tossxNSkc-S8IyLDYDgp7It5qNXN_bgr3DZPQk5rRKMiLFQay0YkIm6UIASSr2A9bkIFonvYTS9fDqESg7NFn7nxImH1xxBNgt8LATf5kpzqhLlshMaWgpuO9AAV9LxkZy73IgTih06aT1dT64SlVY7QqbknYxMAg_2NpOYPh8pxv3QCXJjP_6lSJcuRDveE1U9UTOlv77U_4f1HhvDUhHEK9bw_ccUF3xVsdxRq3T6fGP_aQAEkDHgFl-D5X7f2RPGbySlJLTforVlFdomAIIqqv2Ayfyca34_z74OsU7yJmmV-blToMPDvQUB0EmAzoon7gqN4rzeUNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0b066411.mp4?token=aM9Gh02tossxNSkc-S8IyLDYDgp7It5qNXN_bgr3DZPQk5rRKMiLFQay0YkIm6UIASSr2A9bkIFonvYTS9fDqESg7NFn7nxImH1xxBNgt8LATf5kpzqhLlshMaWgpuO9AAV9LxkZy73IgTih06aT1dT64SlVY7QqbknYxMAg_2NpOYPh8pxv3QCXJjP_6lSJcuRDveE1U9UTOlv77U_4f1HhvDUhHEK9bw_ccUF3xVsdxRq3T6fGP_aQAEkDHgFl-D5X7f2RPGbySlJLTforVlFdomAIIqqv2Ayfyca34_z74OsU7yJmmV-blToMPDvQUB0EmAzoon7gqN4rzeUNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خیابانی در مورد اسکوچیچ
✅
رنگ رخساره خبر می‌دهد از سر درون؛ فدراسیون فوتبال ایران یک عذرخواهی به تو بدهکار است.
🔴
وقتی فساد هست وضعیت همین است، نباید اون اتفاقات قبل از جام جهانی 2022 میفتاد‌، به بازیکن چه سرمربی عوض کند، هیچ ایرانی نپذیرفت آن زمان سرمربی ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134574" target="_blank">📅 08:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134573" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134572" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga_ql2GKWKcJIXUP_kRXtHrdXVNy0J2jhZ2uQXKqN83CiGMqV2iE6bcNfpSXJP4mp2F9WqI_pmFa7kdZXd2pkOG93stNPpJ-luPmaB2m7H-5BKzeFF3NpqIUL2D5L0y8WGtDm3fPO2fOStD4XXwySe6iyFSPWngUSi3CK9hImhVaw_Um-m236IEQj8cNbMv9LNXnG8kBW7IxYC_gylcO86gBanK7_9VCAEdc4BXJDCj-XPMdEXeRMhytdH6LxJkUYZ3YOzY-URZhAfFNRKt_4tnKhmAc9-EXluRwx63nrN2L-5--KSXEYFyGubpbF5HwMEVPfz5ueyYqi17-VUd3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/134571" target="_blank">📅 01:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#فوری
⁉️
👎
خبر منتشر شده مبنی بر مذاکره حسین خبیری با بانک شهر کذب است،و نقل قول منتسب به خبیری صحت نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134569" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: مدیران باشگاه قرارداد رو برای اسکوچیچ ارسال کردن…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134568" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/134567" target="_blank">📅 00:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134566" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
پنجره کیسه بسته است بابت بدهی خارجی .ولی اونوقت مجوز حرفه ای گرفتن.عجب داره واقعا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/134565" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134564" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
دانشخر به سوراختور پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/134563" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

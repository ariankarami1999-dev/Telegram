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
<img src="https://cdn4.telesco.pe/file/nh5aeHiWNH1jU7Uic6mVf7nFzueFjz5ZEeBoT1fOnNEefMU-ZkUZ4OxWbdAqy8e_V6crzg5_6fHfSzOeRmeA8nevbivucJ1Y6qAf1I0nKmLw9Kxy7-CeO8QUtLat5bJVSLaGRHVxGwUVLiNRWWJSaIy_q-sxDtvv8ONj4JfwgsROBVw9uN4MsGVWqDV7sMhn8C7kJHOmNrmGRi3NJccFQIYhDUJKOdBGtUlmT74qIZWDP0BdL8NGwLP6iYQhavFHhDJmSFcLhMOPhT--cPR-NYJOr9rXZnkcWpen6oKyXbnMOKN_ccB7lOuUN_5EjFTC7i-fbGpVKjNVeIz_zdvpDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-144914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اسماعیل بقایی: هیچ فعالیت هسته‌ای در کوه کلنگ نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/144914" target="_blank">📅 15:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در نشست خبری: عاصم منیر نه پیام مثبتی داشت، نه پیام منفی
🔴
ایشان در چارچوب نقش‌آفرینی پاکستان برای
کمک به کاهش تنش
، به ایران سفر داشت و دیدگاه‌های خود را مطرح کرد.
🔴
این تلاش‌ها نه‌فقط از سوی پاکستان، بلکه از طرف برخی دیگر از کشورها هم ادامه دارد.
🔴
درباره نحوه ادامه تفاهم‌نامه اسلام‌آباد با توجه به شرایط روز تصمیم می‌گیریم
🔴
در شرایط فعلی باید بر دفاع و مقاومت در برابر زیاده‌خواهی آمریکا متمرکز شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/144913" target="_blank">📅 15:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLL3trZhDJ_JLwmSeg3hr-AMYcMcisZYtmT6vDeV974Vf_7XboTbxC5YZQPGpkobv6j5ks8DHChlc3hFZmLzs3ntWZ8HC90Mo0nfRcgJ7uNQmbH--vou1PAQ1Z2LJcUlRWx1LPHIj5smSwUhoVA0kScVe-UIT7xAQFdfmaE1UX1FhgADT8trBHlzs0aZ-a8KynqkkwdueIzAFPukLNOzFiWX_scADOnuKwPoZEygTrOMpdGJs3gg5EWcSTUA8UYHJKr3savX1e8ERKbT9MOFSHrzhEOtXPCowMKGMdT79Po0_eA5mQ8vOHZtdjqSS38F84ZpCF9a_qpPl3FUfEG0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک توپخانه‌ای ارتش اسرائیل به شهر حولا در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/144912" target="_blank">📅 15:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مجازات فحش دادن در سال ۱۴۰۵ اعلام شد: اگه در حد تحقیر باشه جریمه‌اش بین ۲۰ تا ۸۰ میلیونه.
🔴
اگه فحش ناموسی و جنسی باشه ۸۰ ضربه شلاق و تا ۶ ماه حبس داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/144911" target="_blank">📅 14:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144910">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: رایزنی‌ها با عمان و پاکستان درباره اقدامات برای کاهش تنش در منطقه ادامه دارد.
🔴
حل‌نشدن بحران تنگه هرمز به تشدید تنش منجر خواهد شد و به همه آسیب می‌زند.
🔴
با شرکای خود برای دستیابی به یک راه‌حل مسالمت‌آمیز و بازگشایی تنگه هرمز تلاش می‌کنیم.
🔴
هشدار داده‌ایم که اسرائیل از تشدید تنش در منطقه برای تحمیل یک واقعیت جدید سوءاستفاده نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/144910" target="_blank">📅 14:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144909">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نخست وزیر پاکستان: پیمان دفاعی مکه علیه هیچ کشوری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/144909" target="_blank">📅 14:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144908">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shpch1BBY5q53dLJZqMavBtgOfpG6G__PVpAcIW_kHYES5nZAKe9FzY1QsJcgPFttPu53ljzZT5IYZgL9gb1eJNX3eHRXxcuOP-pE19U7QGt01DpKGCyuJZlFH6rmWYZAA9lsPhIIZNxkehupLNRZd4_fhhFURcW6qZdu0jGgRIZpIZ61hOftNhKbuqxY6NY463HEKQc8la1tDeaqYRzTZhZJVbXJLN4N4uHvmvr63izU2ls2N6dU34DjaRK8mULxX9mGy3RcrdWoMnGmJJOx8i-e4fXfnYw-_VBFyRbezfA0C4onuWyhofJpFybjXpXXpEOIQEl8uAp85QsM2H-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های آمریکایی: شب گذشته، رویدادی به شدت نگران‌کننده و قابل‌توجه در سواحل شرقی آمریکا رخ داد.
🔴
پایگاه دریایی نورفولک، پایگاه اصلی نیروی دریایی آمریکا و بزرگ‌ترین پایگاه دریایی جهان، به دلایلی که هنوز مشخص نیست در وضعیت آماده‌باش کامل قرار گرفت
🔴
به گفته یک سخنگوی رسمی، «دسترسی به این تأسیسات محدود شده و برخی دروازه‌ها بسته شده‌اند یا با لاین‌های عبوری کمتری فعالیت می‌کنند» که علت آن وجود یک تهدید نامشخص اعلام شده است.
🔴
نکته نگران‌کننده اینجاست که یکی از معدود دفعاتی که چنین هشداری صادر شده بود، بلافاصله پس از حوادث ۱۱ سپتامبر رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/144908" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144907">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر اعلام کرده رایزنی‌ها با عمان و پاکستان برای کاهش تنش‌های منطقه‌ای ادامه دارد.
🔴
دوحه هشدار داده حل‌نشدن بحران تنگه هرمز می‌تواند به تشدید تنش منجر شود و همه طرف‌ها را متضرر کند؛ قطر می‌گوید با شرکای خود برای رسیدن به راه‌حلی مسالمت‌آمیز و بازگشایی تنگه تلاش می‌کند.
🔴
قطر همچنین هشدار داده اسرائیل نباید از تشدید تنش‌ها برای تحمیل «واقعیتی
جدید» در منطقه استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/144907" target="_blank">📅 14:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144906">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
۱۱ کشور اتحادیه اروپا خواستار پایان استفاده «مانع‌تراشانه» از حق وتو در سیاست خارجی شدند
🔴
اتریش، دانمارک، بلژیک، فنلاند، فرانسه، آلمان، لوکزامبورگ، هلند، رومانی، اسپانیا و سوئد خواستار بررسی ایده گذار از اصل اجماع به رای‌گیری با اکثریت واجد شرایط در سیاست خارجی اتحادیه اروپا شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144906" target="_blank">📅 14:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144905">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0dSismnDvC7JoF5T04BXDEkEd7VtpqZ-ORVJ2vgMQbetYE47xkvaH_DFE3NKl1luDq6TLfERhPg8HI1xfRhVEUSo0W0BqWuXEbzgLFOVvThewotd34Gn5ojevmVOV-DtPcv42-1Sv_5SwX-l0ZfwvIdCx5rPAeCRo5ryYusPd8WJVCdVSuJfkGrlNm8uakWfwm1iwJP3xw_1EU4Z_MfS10T4CUrR1nnjxapOErC7bWL-vkebExcomvyRODxBg8zo1tHkc-cA-D39-KpKSKStkj-u3Sr8vl9eXrx4zks8K1iLtMyPDVP61DuNpFerlwqb0VhGdOAyDLulXeq7eLMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امارات متحده عربی به تأثیرگذاران هزاران دلار پیشنهاد می‌کند تا علیه حماس تبلیغ کنند پیام‌های مستقیم نشت‌شده، پیشنهاد ۱۵۰۰ دلاری از سوی لوی الشریف، فعال در زمینه توافق‌های ابراهیم، را فاش می‌کند که در آن نکات کلیدی ارائه‌شده درباره برادری مسلمانان را به یک تأثیرگذار آمریکایی پیشنهاد داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/144905" target="_blank">📅 14:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561954f020.mp4?token=HieCwXOxS_-ia95WVmx2eKfhfeYaO3fHOV-VR7-bJ2asvTD3agW4sk1c_nnyrhT3n98PH7_ihrBNWhHpqs3BByzuSdIWkK1VI4bdB9yltMtbSAnJlOHhMx1I5TB_hIJehPRiHKSrzioKvnOBVNHLLWt7PNGaKNUSaRJdhRwQx7pGSBCbAn02Rr9Cxjo81VUV4sZs6kv8qznfnjQdnVC-6SNbk4ovzb7-gn8WL5Lb-e6zB8y3U_cKnTdxtCR3axlrUN-E8OFv2Ohgz2_TTPIlbDLKrcfrvjCo6AyGrVoex9F5B0Pp_ikU_z51gs-RaWLRYEjLBqhF87HV8mQMz2GYNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561954f020.mp4?token=HieCwXOxS_-ia95WVmx2eKfhfeYaO3fHOV-VR7-bJ2asvTD3agW4sk1c_nnyrhT3n98PH7_ihrBNWhHpqs3BByzuSdIWkK1VI4bdB9yltMtbSAnJlOHhMx1I5TB_hIJehPRiHKSrzioKvnOBVNHLLWt7PNGaKNUSaRJdhRwQx7pGSBCbAn02Rr9Cxjo81VUV4sZs6kv8qznfnjQdnVC-6SNbk4ovzb7-gn8WL5Lb-e6zB8y3U_cKnTdxtCR3axlrUN-E8OFv2Ohgz2_TTPIlbDLKrcfrvjCo6AyGrVoex9F5B0Pp_ikU_z51gs-RaWLRYEjLBqhF87HV8mQMz2GYNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار بزرگ در ادلب سوریه
🔴
منابع سوری از انفجار در یک انبار مهمات در شهر «بنش» واقع در شمال استان ادلب خبر دادند که تاکنون دلیل آن مشخص نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144903" target="_blank">📅 14:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: مدارس حضوری آغاز می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/144902" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilRJ-Zpa_pdyP5TT7h51kjLg72CR_x3BMJT6Wm8DVsiL2FR1dXS4Nh8L23mMkA-jVIYgjPPFcyglvnwXGLOom51XIyulpQvWi_6lfVJpiQcCDFon5viL7_4JvjX4Y51-6rKikd8DP3jxlQIWN3tDIm5VFYtVoshqEAZDro6CeLMCClGQAz9-D4a8CdkT37Ky-yiG-8Fw2Ngo9vsr9ugSDsR6Es4QYCdNf-3K0QvdBGo3eHVNPIiRwVIZOKW5y45TRBB_lnv_MRoLFMLLhRODHlOfpeK6ZRkMM0UGmCBmdOgYmfLAO-bKoej5ADtS1qB6tatTXZn9YPYDZ6F5biXyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / پست جدید ترامپ در تروث سوشال : ترامپ قصد داره بعد از اولین درگیری و تبادل آتش با ایران توی چند هفته اخیر، قراره یه ضربه «سخت» به ایران بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/144901" target="_blank">📅 13:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هر یک دلار 214,000 تومان شد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/144900" target="_blank">📅 13:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32155ad92.mp4?token=lqeZkhBrZzDI25SZSw_X0gY9RsLoYkEXdMiULtzph1g46VncTZ9rL_F57XkieZBwhoztGMqPh5_MdAjPgNAjune04DvPpRunkChnGKjaMM5lRniF5M9rCHRJfTrlCRv_Sel9BmRhxi3ySHJUfByrOME527Ziai_uEde4FYZiTU5Hd2ayUBuUiwnD2qFExB30R2J3hmqWJgC9qgb0BnHzsEBARyecwB8JQBeUY8Jp5dVBXBS6aEh0Y2Xumc79_eCuZacfKSXD3LzKRtkdYcmrSarhE-Ga1IPzVj0idG6SO_mAD8qHwisrDYuFqDqkejXWBE-fpxrTRALjYD2nBuT4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32155ad92.mp4?token=lqeZkhBrZzDI25SZSw_X0gY9RsLoYkEXdMiULtzph1g46VncTZ9rL_F57XkieZBwhoztGMqPh5_MdAjPgNAjune04DvPpRunkChnGKjaMM5lRniF5M9rCHRJfTrlCRv_Sel9BmRhxi3ySHJUfByrOME527Ziai_uEde4FYZiTU5Hd2ayUBuUiwnD2qFExB30R2J3hmqWJgC9qgb0BnHzsEBARyecwB8JQBeUY8Jp5dVBXBS6aEh0Y2Xumc79_eCuZacfKSXD3LzKRtkdYcmrSarhE-Ga1IPzVj0idG6SO_mAD8qHwisrDYuFqDqkejXWBE-fpxrTRALjYD2nBuT4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دولتی سوریه پس از انحلال نیروهای دموکراتیک سوریه (SDF)، وارد شهر حسکه شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/144897" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRPQltAcovhfviyzrdv3QKEQ-meb1FxJ45SvAD7dPMS2-WjIZpY0kmhjZkQcxOF0MldP0Fdb6aVqTLTU-NBJMuWUOsCjFxt0SeVqBkX91D-ql0gChOY0Z7-flaLvVbzTIE4UGizc5QCibNPfJSkPdHVKcYAmUfOxjR3UToVApm8x7oyW3lB0sfM49tB27AHypruBjjKAvtgflhCmvm_zy3BR2mzNMS1ZkaRHHBiGDankN7D9g3Kbb8SOPRjihrplwPVa2nE_7ha1XYT3Sz25U9yQxSjg6w8zT7VW3Lpkkvbgks-9x5wl8sv0YHPcxnLxsufyiF6m1diLa93MZhF9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مهاجری: رئیس صداوسیما در دیدار برخی مسئولان در برابر انتقادات تند فقط برّ و برّ نگاه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/144896" target="_blank">📅 13:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144894">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60357d956a.mov?token=k1RI_0wwoijSvmlEm1oyyBnMWVyNDKp9AUSAqw4vxi6FpOCz-S2nkawKc8hTAt5aVFf6CBr9lwfbNIxvEfocy9TiQsKB9OJMm7gtSt6e8LCM_OC9pw5ihg2a1ySfLI7M1jByAXinHYAvE9Rx75HXVMjRZok5P2b-jIOp56Bv0xIQ0lGKKDDEIfsDYPUnDvdvCMzV3QT8vP6ysxWWfltUWHILGW0CsArBJg3Fv4Y1HMpt1KYmRSdfqKbOZngDgiWqZi0dCvbO1fYuAq6TJaA832bZFku0DKu4WKV1PdFJp4f2B75o14arpVpsUNLNz_LL9kAShOJNA-iktPYkUMKAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60357d956a.mov?token=k1RI_0wwoijSvmlEm1oyyBnMWVyNDKp9AUSAqw4vxi6FpOCz-S2nkawKc8hTAt5aVFf6CBr9lwfbNIxvEfocy9TiQsKB9OJMm7gtSt6e8LCM_OC9pw5ihg2a1ySfLI7M1jByAXinHYAvE9Rx75HXVMjRZok5P2b-jIOp56Bv0xIQ0lGKKDDEIfsDYPUnDvdvCMzV3QT8vP6ysxWWfltUWHILGW0CsArBJg3Fv4Y1HMpt1KYmRSdfqKbOZngDgiWqZi0dCvbO1fYuAq6TJaA832bZFku0DKu4WKV1PdFJp4f2B75o14arpVpsUNLNz_LL9kAShOJNA-iktPYkUMKAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های بالستیک اسکندر-ام روسیه، مجهز به سر جنگی خوشه‌ای، کی‌یف را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/144894" target="_blank">📅 13:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144893">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نتانیاهو: «من نزدیک به ۴۰ سال است که با مسئله ایران درگیر بوده‌ام.
🔴
زمان زیادی طول کشید تا بتوانم نهادهای امنیتی خودمان را متقاعد کنم که مستقیماً با خودِ ایران مقابله کنند.
🔴
همچنین زمان زیادی طول کشید تا ایالات متحده را به این درک برسانم.
🔴
توانستم این کار را انجام دهم، چون نزدیک به هزار ساعت در تلویزیون‌های آمریکا حضور پیدا کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144893" target="_blank">📅 13:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144892">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی دولت درباره هشدار اقتصادی رئیس مجلس: قالیباف جنگ را به خوبی می‌فهمد و می‌داند که معنای مقاومت چیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/144892" target="_blank">📅 13:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144891">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ۷۰ درصد نوار غزه ویران شده، بدون تونل یا زیرساخت، و تحت کنترل کامل ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144891" target="_blank">📅 13:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144890">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: پاکستان در موضوع جنگ علیه ایران، قویاً به دنبال صلح است و به ماموریت خود برای میانجی‌گری ادامه می‌دهد
🔴
تنها راهکار دیپلماسی است
🔴
اجرای تفاهم‌نامه اسلام‌آباد به برقراری صلح کمک بزرگی می‌کند
🔴
مسدود شدن مسیر‌های حمل و نقل که ناشی از جنگ است، معیشت جهانی را به لرزه درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144890" target="_blank">📅 13:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144889">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر ارتش اسرائیل، گالانت: یک مقام ارشد از جنبش حماس دستگیر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144889" target="_blank">📅 13:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رئیس سرویس فدرال همکاری نظامی-فنی روسیه: روسیه و ایران برنامه گسترده‌ای برای همکاری نظامی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144888" target="_blank">📅 13:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAtxXMOlXeN6PSVEf5cBp19tRyg3iD4ABn7XRg7n49sUkIBC733PPqo4dV-6j-Ux17LliUutPaSm2uPI7HpoEkqrtDa0AgMhcPPVWUkTosaxyX1-V3kCsEtJtu1OLvpavzm1IwucYY5QgqfsXbL0mPt6ii7Wko1pBDVMlWuIScgMeOblgXCNJd6klHq5rUCwuMeGppuEbGLfzGLlmVslhyJZiORelD4mkwNkBwC9PQtThYCZ0kn_SgrlX7624tQ4mBDy4tZV4326y3YlZByv5b3Ly3PKZeRKcXx1mM7ZjBBBcATp75zHsSmpD76zxEkeNUdi9GhYdfEqy-vLb69p8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در جریان معاملات شاخص کل بورس با افزایش ۳۶ هزار و ۱۱ واحد در سطح ۶ میلیون و ۵۸۳ واحدی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144887" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144886">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
منابع خبری از حمله توپخانه‌ای اسرائیل به اطراف شهرک «حولا» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144886" target="_blank">📅 13:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144885">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت بهداشت: کرونا دوباره شیوع پیدا کرده و تو هفته اخیر افزایش آمار مبتلایان رو داشتیم.
🔴
بهداشت رو رعایت کنید و در فضاهای بسته از تهویه استفاده کنید
🔴
پ.ن : به ایران خوش آمدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144885" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144884">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کره جنوبی و عربستان به شهروندان خود ابزارهای هوش مصنوعی رایگان می‌دهند
🔴
دولت کره جنوبی در برنامه‌ای تازه دسترسی رایگان و نامحدود به هوش مصنوعی را برای تمام جمعیت این کشور فعال می‌کند. این ابزارها با اتصال به سامانه‌های دولتی در مواردی مانند خدمات درمانی، امور مالیاتی و آموزش به کار گرفته می‌شوند و بیش از ۵۱۲ پردازنده پیشرفته برای پردازش مدل‌های بومی در اختیار شرکت‌های مجری قرار می‌گیرد.
🔴
هم‌زمان شرکت ادوبی اعلام کرده که در قراردادی ۴ میلیارد دلاری با عربستان، امکان استفاده ۱۲ ماهه رایگان از امکانات هوش مصنوعی خود را برای بیش از ۲۷ میلیون شهروند این کشور فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144884" target="_blank">📅 12:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5QmOaXRpLXMr9kI2uOjl2JQi0RqKqWmq8_16oxYLf32zWz9LrVtlnkK7bGXd4F1_iSo6h4-loCt4Ah13lbwbLxnopd4tk7wswqSBKNf7VEzAZd-XoGuUmI5C6_vqQipfQK7L4DGAtkF6HnIPJ2hhmtliwq3Ox5j7nl2Dn3s2AK4DaAB-1Fkv0sDgyRqkxpPW8i9QNKWHjwJqEpFqH5yn1Bb6R049HzraeVsBNN4Ny7wFM_BFL7snXdfzyZ9WLA6IRDQAGqj0FhG_CAKiNXkd-7-BpXelvuJYLP54BGpEoG5Zbyq_7k_iTg_Y-2qyrKJluhetqQWLY6b1HPu0KNLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144883" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkjJbCpu595YtOXy0QnWPSXCjtZgf6BhCJ7v-Iv_QHe-P8zfXLjSYf7V-UN3okLdP8-CJaPUwAYKCmw9CICvbbQZ4C5B8sAnKTcTY94GKjcgSzuBHfQ9SVDleb0NcLKSFhfoZedlq6bf-NEMl4ag4yuM_r8jx-jlS24lZbgq4TnsktwjeU5V6FepF6UTWo7V3GN8TOlJ44pT_LTHGGgHSAcDuCL-R-_8asY3bSq51ZhuhLwS5CeA8GbfrcPexQe6k1dC8bdAzjoeNUiROoez9sLE-pfnKnd9b-dQJ2xnz-4N1EhqbQjjBNK0qtef5ogLVpe7pd7u-cVl7IgBWFbOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید در ۲۴ساعت اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144882" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144881">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دلار در تهران از 212 هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144881" target="_blank">📅 12:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvtbiJbEbC5_gdCIBIZAbuDjM_zl6KVuji0Ccm4SsPPqh7_fZbTHebBhs0-pNgOZfzzS76KHxn9vwTTiNaL5kouRvvv_mXyDXGFZlPwFbRF6CTrTvIiJUhq0s3o5HSL0dJaytjb_Z22QWfGbrVAVs2qeNIaVo8JtiwbLmNt26d58YKOgC4B_wUweI_fp7SNT_pI8gi6BqJ8ZjBMU39kb-58NfSrySq1TswUBV3Uau-eZ-scoNvZs52j19Q15FsWO3Mv_Qou5UhMP08N_eh3VaWxYJDkaWLWgjQ7Ney-qbfxnv3lXAEWwOcApoYXJ2jO4St1DnRdWRap9KZCwgFOmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتلو بزودی آزاد میشه
🔴
تتلو از زندان: از وطن فروشا و پهلوی متنفرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144880" target="_blank">📅 12:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11a7dde2d.mp4?token=oZfwvw3dXk054KPGhkVqP9W0q0yHIEXEuwr3kPXG4_S51O3S4Rs4ISLuFIqGh7rj3odZ6ImoOdpWYVr-xoEAV0f2FMIHtgwQCfc9P_m2PVsdkvg8JsOw85i0bVrwpjbfST8H7Uj_hJF03yW7lPfED3__7cfWU2vEhgj3agLE3z4wCpBR6xudBlwyspkaM9vg902S_-nL8xiH9JxvDHqSi4SX3BnZ_ZbmhskOjL-QN7YQUo1Wo5p6lBwrFcyf2hL2WbH-H0mbMQM1pAkEcvcWHaynWKi8LfG5eQw6VS0kF6smM09kT_KkR9KC7zNwMGiY12KUk2eh139q7bxo1wP2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11a7dde2d.mp4?token=oZfwvw3dXk054KPGhkVqP9W0q0yHIEXEuwr3kPXG4_S51O3S4Rs4ISLuFIqGh7rj3odZ6ImoOdpWYVr-xoEAV0f2FMIHtgwQCfc9P_m2PVsdkvg8JsOw85i0bVrwpjbfST8H7Uj_hJF03yW7lPfED3__7cfWU2vEhgj3agLE3z4wCpBR6xudBlwyspkaM9vg902S_-nL8xiH9JxvDHqSi4SX3BnZ_ZbmhskOjL-QN7YQUo1Wo5p6lBwrFcyf2hL2WbH-H0mbMQM1pAkEcvcWHaynWKi8LfG5eQw6VS0kF6smM09kT_KkR9KC7zNwMGiY12KUk2eh139q7bxo1wP2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود دکتر مسعود پزشکیان به اجلاس شانگهای پلاس
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144879" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر نیرو: اگر جنگ اتفاق نمی‌افتاد و بعضی نیروگاه‌ها از دست نمی‌رفتند، امروز در نقطه تراز قرار داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144878" target="_blank">📅 11:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر علوم: آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144877" target="_blank">📅 11:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: دور جدید حملات میان ایران و آمریکا، قیمت نفت خام را به بالای ۹۱ دلار در هر بشکه رسانده و نگرانی‌ها درباره تداوم تورم را احیا کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/144876" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737291ddef.mp4?token=b1tDyrdjCphlTORCLtnbgqS8GzZdvI2wUlXfjOqqj48pDnsIPPxTahMh_KlxS0jLz_mY79derP-ZKWGG05WeE_1um9ybkkX-2JCLXAJXQnbGWU9tp5z5AFgFLzMDm9mNFBaruli6teKpVe8iVI9Y5G8j4katDYgZiNox2nOvMk4xh9FoMjMqpiSvV7DRpgzj6tYrq1mGticWq1kpE-vZq1FU-2KFV4cqepMwNx8vvMcY8cSs-2XhgBythfibCWueVFtCCy4Ae-MN3OQrnAwm4oIYRzWtVGgI2hteoDajX7HbGZliqGyjVRg7qq5AtRasY0TFtxWnM0of9FCW2ToHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737291ddef.mp4?token=b1tDyrdjCphlTORCLtnbgqS8GzZdvI2wUlXfjOqqj48pDnsIPPxTahMh_KlxS0jLz_mY79derP-ZKWGG05WeE_1um9ybkkX-2JCLXAJXQnbGWU9tp5z5AFgFLzMDm9mNFBaruli6teKpVe8iVI9Y5G8j4katDYgZiNox2nOvMk4xh9FoMjMqpiSvV7DRpgzj6tYrq1mGticWq1kpE-vZq1FU-2KFV4cqepMwNx8vvMcY8cSs-2XhgBythfibCWueVFtCCy4Ae-MN3OQrnAwm4oIYRzWtVGgI2hteoDajX7HbGZliqGyjVRg7qq5AtRasY0TFtxWnM0of9FCW2ToHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: برای تأمین سوخت نیروگاه‌ها و افزایش تاب‌آوری شبکه گاز برنامه‌ریزی کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144875" target="_blank">📅 11:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی دولت: افزایش قیمت دلار، نتیجه تحریم‌های ظالمانه آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144874" target="_blank">📅 11:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مهاجرانی: دولت هیچ برنامه‌ای برای واقعی کردن قیمت‌ها ندارد چون درآمدها واقعی نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144873" target="_blank">📅 11:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=DUkjt__SdwSb9aOPyIwxCFJnA7Ist08HbU-6MLacU8H88PhcLZXbjjsIOcP9sDMRIO05jApvx2YM7QgfOjJ54mLanNXy7OQn7L6WCyZHeIcWWDzffY3mhRACYw_3EqgynZf7XVqvinzBunaiHr-ub2dGbp4sDbEP4E5gnFMWq3L5ctBdiPTu5sSKdtn9_726Hz-AU3AIod2_0Vn0guXoOH3jYCcqkrJRK3DPHx3jPw7tVVZT5DRoXDJK4MQGoiMdhUFbNSPrudfU5hP90OXgcs6GKgi0YtqY1EMdoGWRkYuoj0kpsc7ZI8bsGYGjKbLlnX8j4gTeQx8AM9QbNPm8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=DUkjt__SdwSb9aOPyIwxCFJnA7Ist08HbU-6MLacU8H88PhcLZXbjjsIOcP9sDMRIO05jApvx2YM7QgfOjJ54mLanNXy7OQn7L6WCyZHeIcWWDzffY3mhRACYw_3EqgynZf7XVqvinzBunaiHr-ub2dGbp4sDbEP4E5gnFMWq3L5ctBdiPTu5sSKdtn9_726Hz-AU3AIod2_0Vn0guXoOH3jYCcqkrJRK3DPHx3jPw7tVVZT5DRoXDJK4MQGoiMdhUFbNSPrudfU5hP90OXgcs6GKgi0YtqY1EMdoGWRkYuoj0kpsc7ZI8bsGYGjKbLlnX8j4gTeQx8AM9QbNPm8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144872" target="_blank">📅 11:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2d996101.mp4?token=avN-iO4PydDNHWWfT_-MWlrtG6LhIgpJghT-D4z-XbwW1x4zX9yMI7CVnz3iI5Aqqt1ABusbHn94R20yhMsRi0dn6GML7axTDdtVnADA6f9twd1-ZiRuC9U6uHHPn-1qdPPmZPT_PD_UrZ1ZEM574eNwx9JPnUXCRAiu-bkKd_J-IKTDVIe4HqT9KPVV83R3pIluyeIbtTbOz8zgELtVpxR20gQgZSG9OpmGOjzS1W-S094YEqR_jR-UJFHb-Ok0bcv9RNw3PxX0hYnCaBxGqBVO1CspjCOSUqKgT4i7teHP75upKOw-657uspWUC51mke9pPgKsi11sxCgDxaMqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2d996101.mp4?token=avN-iO4PydDNHWWfT_-MWlrtG6LhIgpJghT-D4z-XbwW1x4zX9yMI7CVnz3iI5Aqqt1ABusbHn94R20yhMsRi0dn6GML7axTDdtVnADA6f9twd1-ZiRuC9U6uHHPn-1qdPPmZPT_PD_UrZ1ZEM574eNwx9JPnUXCRAiu-bkKd_J-IKTDVIe4HqT9KPVV83R3pIluyeIbtTbOz8zgELtVpxR20gQgZSG9OpmGOjzS1W-S094YEqR_jR-UJFHb-Ok0bcv9RNw3PxX0hYnCaBxGqBVO1CspjCOSUqKgT4i7teHP75upKOw-657uspWUC51mke9pPgKsi11sxCgDxaMqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: ایران پیشنهاد ایجاد «مرکز راهبردی مطالعات امنیتی» و «مجمع پارلمانی کشور‌های عضو شانگهای» را ارائه داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144871" target="_blank">📅 11:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز: داده‌های ردیابی دریایی نشان می‌دهد تردد کشتی‌های حامل کالا از تنگه هرمز همچنان در سطح پایینی قرار دارد؛ به‌طوری که شمار کشتی‌های عبوری به حدود ۵ فروند رسیده است، در حالی که میانگین آن طی ۱۰ روز گذشته حدود ۱۴ فروند بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144870" target="_blank">📅 11:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
افزایش ۳ دلاری قیمت نفت و رسیدن به ۹۱ دلار در هر بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144869" target="_blank">📅 10:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
همتی، رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/144868" target="_blank">📅 10:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144867">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449457076d.mp4?token=eA1xVw4YYeFIyVH_tjWl2XNzlCGlDFT-e6t8xsM5r82aBn_Lc4XC_gKhQAIspiF1y7Egsox4LMzRB5sJ_7ZuU0db7Fo3jecERlBZS-217A58kTb3vH1svGvD0MSeT6_dNEBbSCPlt0lrIpQ-XCG1JMgnUnABd-_rjbSrtFYjzUAhbLVfAipTvAg2fBHcP7O745UYDol_vegtT-d4AaaxAfqsf_bw8IMHbFZzTFvEoE7P36nrFRy9fPC1OEQuLNAc5YbEyVDO7Pryltw_ZDXwwA3JT74ufle85cY_bzRPN9ZGNDIqE5xfDXQzMgMExQzRBF4zZ-U_1eQxN2BHu6iR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449457076d.mp4?token=eA1xVw4YYeFIyVH_tjWl2XNzlCGlDFT-e6t8xsM5r82aBn_Lc4XC_gKhQAIspiF1y7Egsox4LMzRB5sJ_7ZuU0db7Fo3jecERlBZS-217A58kTb3vH1svGvD0MSeT6_dNEBbSCPlt0lrIpQ-XCG1JMgnUnABd-_rjbSrtFYjzUAhbLVfAipTvAg2fBHcP7O745UYDol_vegtT-d4AaaxAfqsf_bw8IMHbFZzTFvEoE7P36nrFRy9fPC1OEQuLNAc5YbEyVDO7Pryltw_ZDXwwA3JT74ufle85cY_bzRPN9ZGNDIqE5xfDXQzMgMExQzRBF4zZ-U_1eQxN2BHu6iR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امضای اسناد تفاهم توسط روسای سازمان همکاری شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144867" target="_blank">📅 10:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فارس : سید مجتبی خامنه ای دستور عفو ۲۵۰۰ زندانی رو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144866" target="_blank">📅 10:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144865">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaGNktn5ScROJmF4EVvRGf2d7i_lE4pyE94UPu8TkW_UIKjT-QG_ZEInL2IzgZSBPLTxwBCBMpQehW6cPgwEghu53auETTk-SeSm4U3y8i6kg6wV1B0wK1Y5ZqrYDw3puzqoMQurk_rpmN7V6kEjKyUc_TYdd2pS_mwGWV1AFlIJxkuR89B4X7ZfvH62WPhEtQMVJfQGniJXHC-uRkDFebXvs9jhW4FNv2GLbVnzgMxEkfLrB9WdtLZSX_50wvYMQk3VTrtU5LoLg2Euq5vmYkloIs8E4HGTpNMHV4EzdE3Lv5zjqmtdFAYazEoelV7R1KF2qWNVYQfDDOwxooY2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هالیوود یک فاجعه کامل و تمام‌عیار است! برخلاف اسمش، کار بسیار کمی انجام می‌دهد. هیچ انگیزه‌ای برای حضور در آنجا وجود ندارد و به کالیفرنیا آسیب زیادی می‌رساند. جان و بسیاری دیگر در این صنعت، پیشنهاد می‌کنند که ما مشوق‌های مالیاتی فدرال را اجرا کنیم تا تجارت تولید فیلم و تلویزیون خود را دوباره عالی کنیم، شاید بزرگتر از همیشه!
🔴
مقدار پولی که برای مشوق‌های مالیاتی هزینه می‌شود، ده برابر پولی است که به خزانه خزانه‌داری سرازیر می‌شود. جلساتی با رهبران هر دو حزب در حال برگزاری است تا این کار انجام شود. این کار باید دو حزبی باشد، به خصوص از آنجایی که پول زیادی در کالیفرنیا و سایر ایالت‌های عمدتاً آبی از دست می‌رود.
🔴
من پیشنهاد می‌کنم که جمهوری‌خواهان و دموکرات‌ها دور هم جمع شوند و فوراً قانونی را برای نجات تجارت فیلم، تلویزیون و سرگرمی در آمریکا تدوین کنند.
🔴
کنگره باید فوراً یک مشوق تولید فدرال را برای ایجاد مشاغل سرگرمی در آمریکا تصویب کند. این کار می‌تواند به سرعت، دقیق، کارآمد و مهم‌تر از همه، به نفع همه آمریکا باشد.
🔴
آنچه ما روی پرده نقره‌ای سینما تماشا می‌کنیم باید در جایی ساخته شود که زمانی پایتخت سینما و تصاویر متحرک جهان بود. بیایید این کار را انجام دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144865" target="_blank">📅 10:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICXArrR9RNT_F7Q27GyV5hjojfPavLx4m2_rAockvum2tAA6LiTVOrY7hYmUy2oAaAT_GGQnpANZgdMiiW4Uwp_uE72w0fkt_eb8ojEXeNExFL70IqFOMk5FhMi_4-nF5nthcesbcRFAOABmpga1Ao1yVBgLKSjZygKlpx6xBMbsAyEIs0Ls-3KvalkhvrgJNwh84eH8qLPsf5yXZ97GRK_LjNJMc-vAZjz-YRIHrm_4y80zqae4hGU210XfjnFnBd4l84S7CB1e6SXd9JiYYGvLoVahleupF0wgeKIspqWh3SZiFeaAh8Aa1X3Z4gGbH-x_08d5fXnlAXvziaraJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔴
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144864" target="_blank">📅 10:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f8e698f2.mp4?token=rgDUH-Xt_NxFlZ0sNYq1o5tJqxtrKhS5LstVuSIAhPRbQeG0l_KwAL6cpItgxbZ10Cd8jjG9fiCaPwq1VYlIJrcPI4c5m96qkRpkTG64TpWR-vaZOpv7wR0zi0l_0LOeMNnZE4l5Tmbv9DltYnkgX5n1X2VqlMwsTPOJxAFt7d6lQqtP-NXAyLYhy_JQ7u6UhTp1MPWwzGqaykbf4cAbnE_UXJ6OQpVMJ2jeR5Y-O0nEzXDY22GZ0eRqnM0psj0yYgwKglBIFCsm-r0BwLZliJOkS7t7-5zsbTNJkZSJzDVG03IHz73QNd8fzFQ6pCiThEyPoYUk_gPxWiS2e5xOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f8e698f2.mp4?token=rgDUH-Xt_NxFlZ0sNYq1o5tJqxtrKhS5LstVuSIAhPRbQeG0l_KwAL6cpItgxbZ10Cd8jjG9fiCaPwq1VYlIJrcPI4c5m96qkRpkTG64TpWR-vaZOpv7wR0zi0l_0LOeMNnZE4l5Tmbv9DltYnkgX5n1X2VqlMwsTPOJxAFt7d6lQqtP-NXAyLYhy_JQ7u6UhTp1MPWwzGqaykbf4cAbnE_UXJ6OQpVMJ2jeR5Y-O0nEzXDY22GZ0eRqnM0psj0yYgwKglBIFCsm-r0BwLZliJOkS7t7-5zsbTNJkZSJzDVG03IHz73QNd8fzFQ6pCiThEyPoYUk_gPxWiS2e5xOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع خبری اعلام کردند با کشف ۸۴ جسد دیگر، تعداد کشته‌های سیل ناگهانی نپال و چین از ۱۰۰۰ نفر فراتر رفته است و ۴۴۶۲ نفر همچنان مفقودند.
🔴
اجساد تا صدها کیلومتر پایین‌تر از مرکز سیل، حمل می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144863" target="_blank">📅 10:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGHND_ZqPgGm0ndrEEu4VUupKuIMD6ZmEh2dDCpApq4ohdl0J0tc7Ix8VKreAa8dSIW83hJTqkCTt6cOz-kmdmfdjPnucYaXW-RTTcxym2XM2XIShoVycgORO-GRb1Wpr6VY7kfk71hnlUtr2IOUHSFZrhjzysAXGvfL0GuH0DcaEfRAKNIoJwIJPkA6u9F4VXkYS1NARBB_4S8ytOMu5VWfdIOSdYEwDv8KncDLih2Ye9mcggcl5m8R8o2jeJW2AazmgghC98HaBFiEu-UqXZtdxwoHLCv7_vbF9z-DWMzzQ1P_W49I2YGX6rTu-sDLwqmKrpYy_7lDt41nYtaU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد آمریکایی MQ-4C که از پایگاه هوایی موفق السلتی در اردن به پرواز درآمده، هم‌اکنون بر فراز خلیج فارس در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144862" target="_blank">📅 10:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
جبلی خطاب به پزشکیان: دیدن صداوسیما افتخار است، کسی که نمی‌بیند از این افتخار به دور است!
🔴
پزشکیان پیش از این خطاب به جبلی گفته بود دیگر تلویزیون نگاه نمی‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144861" target="_blank">📅 10:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کشتی‌ای که دیشب به‌گزارش سازمان عملیات تجارت دریایی انگلیس در مسیر جنوبی تنگهٔ هرمز هدف ۳ پرتابه قرار گرفت، نفتکش غول‌پیکر عربستانی «سیدر» با ظرفیت حمل ۲ میلیون بشکه نفت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144860" target="_blank">📅 09:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aovfPZAnJQlUqs__zJim6m5uobxL2zI59hOHBL0z2rCgeHDPNOPHm_82bBUAokRWRdDOy2V9vlryRXW86Nd6lyMIaEBqkDi4ceLNc2rM50eNSG1mva3xMXsO-FqELsECnbaoHw_arZSHuLQ0lR_YDJypPRrUOCAsgSEjjj4Pa8y_xnII722bSVj1aHRADr6hy8YffpAxmrMQLdG70Z-DVve2jRUT1ubrlERpCrLldvz6Xl8ep6AoJKLAtqrNV9fA7SPyomNXpPVPql1iT0O1Sm8ZJTeh-reI3QKW1RoopLMq0dBNFrb-Aq4Pzz4Ma73wJMJHUNyy3-Kz5nLOGXWZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیتر هگست، وزیر جنگ آمریکا
:
🇨🇦
(این واقعی است)
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144859" target="_blank">📅 09:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع بلند پایه ایرانی: در پی حملات آمریکا به لارک، ایران ضربات سخت و دردناکی به پایگاه نظامی ایالات متحده در اردن وارد کرد
🔴
خود آمریکایی‌ها بیش از هر طرف دیگری از شدت و حجم ویرانی‌ای که پاسخ قاطع تهران بر جای گذاشته، آگاه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144858" target="_blank">📅 09:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
همتی خطاب به ترامپ: ارز داریم، به قدر کافی هم داریم، بازار ارز هم آرام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144857" target="_blank">📅 09:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXNdLA1yAGf6IfkO5VNKYuCyke2JaPMCLigGk4apNsKezrt4eWQ3zYFooEfbPHCTCwgTWmPEZZlXYQH7C21cIAw3zTx3sIrMcgcb-8K2G0CKXhoVb5TuVR3KmN6vJC2Fe1P_rQWGU7Hm5Bx7DanGkzk9QH4WgqetXn5H0DI0r6yzZf-0U6klAW638ZF0FN0-90aHW3L9mqPdYPUO3N1R65fjuZgItojycwniMqyXhw2SxL4hgaHYkW3f2i8DwPrIJ1epaDzO-Dpv6WzJ19wiZ6RLnrI2kHuZ5z7-l36U5fZHABoJSpxlgGN6ljFbG3_qiXAYGkfE5gw7UKyoxKbHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های ناتو که در مأموریت پلیس هوایی بالتیک حضور دارن، در واکنش به یک تهدید احتمالی در حریم هوایی لودزا، لتونی به پرواز درآمدن؛ این منطقه نزدیک مرز روسیه قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144856" target="_blank">📅 09:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkAoOii9VZUqyCloI47LY-8J5fJdyTlvuyK2tnVEc2yzkBvGZEScQfyZg5Hb96ISHWDSLrTPjEWjQG7s9w4sGyTx9XMEM-UaUFdnIML6I-vb-lLCWbtVpFvGB3bcRTLw0FfSR2lG-WVtEv6cLgvfMdV8FMI-xieSKGmde4QTYHa7yf9JXSIY6lrzbxHPa-LEsC-I359-4jpHo0ccRH-aRL-J58Z7r7AbTXNK9hEmd62MMx_2C7yNFhbyN56xrQhT5lou6Fn0hHyN_Dmj45I5_05kpTz-wvCBRUhCVwyLS5Ytq0GovbBwNOPp6d-iBxeIUG5L79ItJO-B6Rpdpftrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش وال‌استریت ژورنال، شرکت North American Blue Energy Partners به رهبری آلخاندرو بتانکورت قصد داره طی سال‌های آینده بیش از ۵۰ دکل حفاری در میادین نفتی ونزوئلا مستقر کنه تا تولید نفت رو به‌شدت افزایش بده؛ این کار بخشی از توافق نفتی اخیر با آمریکاست.
🔴
این شرکت می‌خواد تا پایان ۲۰۲۶ ۶ دکل فعال داشته باشه، در سال ۲۰۲۷ ۱۲ دکل دیگه اضافه کنه و از سال ۲۰۲۸ به بعد، ماهی دو دکل وارد مدار کنه تا در نهایت تعداد دکل‌ها به ۵۲ دستگاه برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/144855" target="_blank">📅 09:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پزشکیان در اجلاس سران سازمان همکاری‌ شانگهای: تداوم رویکردهای مبتنی بر زور نه‌تنها امنیت کشورها، بلکه ثبات منطقه و جهان را تهدید می‌کند.
🔴
شکست‌های سنگینی به آمریکا و اسرائیل تحمیل و پیروزی‌های درخشانی کسب کردیم
🔴
آمریکا به تعهدات تفاهم‌نامه برگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
🔴
پاسخ به تروریسم، افراط‌گرایی و تهدیدات نوظهور امنیتی، نیازمند تقویت ظرفیت‌های نهادی و کارشناسی سازمان است.
🔴
آمریکا به تفاهم‌نامه برگردد، ایران نیز عمل متقابل خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144854" target="_blank">📅 09:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پزشکیان در اجلاس سران سازمان همکاری‌ شانگهای: تحولات اخیر در منطقه غرب آسیا، ایران، لبنان، غزه، کرانه باختری بار دیگر نشان داد که بی‌توجهی به قواعد حقوق بین‌الملل و تداوم رویکردهای مبتنی بر زور و فشار، نه تنها امنیت کشورها، بلکه ثبات کل منطقه و جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/144853" target="_blank">📅 08:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC-1QU_Ld0bTxw4Y2u1jmMv_B9GcA5btpC5Go3SyQDn8FODCvhFVo9VD-VZNUsOzbOxm61JlQTDQ7hfKxKIvXmV_gE54QgordfmFDEoCpAwYWrcoAhW65JOVRCNe1rNTTOSvVI7W4Na3di2oXOeIN61Jt8Nseq8N4g_9L4Qgz-WB7IhtMh9RS_ibwJToT-um5DPf9l8Z6WRfEd3iLpYFzjdvUJNc4-bx7TnA7zG5sXxrR-I1KxiXq1e9AyvkNzMbuylqnYBHTVgwtyb6HbsP6MoBlJK56TbSUxd5aq_cARPOHOKxyYWZPw7nYX73FhNNucVCqHVM45Z1j1VyKBzp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: از امروز تو اکثر نقاط کشور دما کاهش پیدا میکنه و بعضی جاها تا ۱۰ درجه دمای هوا پایین میاد و کم کم آماده میشیم برای ورود موج سنگین بارندگی به کشور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/144852" target="_blank">📅 08:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جی دی ونس: دو شب پیش حملاتی در تنگه هرمز انجام شد؛ ایرانی‌ها در آستانه مین‌گذاری بودند
🔴
بخش قابل توجهی از اقدامات ما، با هدف تضمین جریان آزاد تجارت در تنگه انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/144851" target="_blank">📅 08:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آغاز سخنرانی دکتر پزشکیان در اجلاس شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/144850" target="_blank">📅 08:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maWRapdmPDKTYfAcxn05WKKl_7BLXOu5irYA809_4sDhBVig19eP97gVrw8FVPeILP-771KJ3sfJS2-Oo-SQsGjNxbUmf8Z0yNtVHYwOW0_4Tb8j9QXmCzZSlLPevppqeF8ibVVSfRfxpsR81MdzCaL0EJOmAN4mEhf2-FfvJcVmgFiYWGBan0N6dg7QhsKaHt-1HMBkmwY9dJ9xq4GBwLD2Noi1j7MioMYpbinVw9OJu9uW9szC46XjBazamephFGmUXwe6NMrMATxfOzzfEv7sCxsdHSq3kWFfHNd8aEE4pcBevSq0nZAXXRcVtt80FNXNe8ffnXf29PaAdHHRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش بعد از ماه‌ها اختلاف با «پیت هگزث» رئیس پنتاگون، بامداد سه‌شنبه از سمت خود کناره‌گیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/144849" target="_blank">📅 08:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl2pnx7wm2BG2MrBibW8oKArBe5QEAvLjKioAAHmfP2-54PsnVjQQ8xsmU6i8tPXpwwj8MHnADbrkb1BVVpsTctPv8tXvAwi1hNf4K34KSHY1PxhdeLusPRM1MfM20utVc8cYaxtQXAM-6lOxcn4ggn2qRpVlEys_f7kyt0oEqg9sEaJ7S6YybSFFB1uEJSWqHr2cCXleVl-CQxSCxT9s3Sr-7a84rfalqsWVoYozOKIHNTyjSbi0JrzYbRp9N2u3DxUpThBrXCY9tFx8RbLK0MNstm0TyaLMBUP21iBCcnESkvXBD92n4zYueRoDnlOaryPdNCMjr2dpOgvGe-A0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی هم توسط ایران مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/144848" target="_blank">📅 02:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQi-54vdTa-S--Rg19mW2A9nk8mCtdaR5zaCvsSpUgIX4AhM0Dgu0E7jeh_kL4k8WcBNi6sZGVjvkVq-YBUUAsrvOkZZomepws2T-ic9kcig9I_G_PqYKpbEZ538pvXYc-4Vl0qzMPUk_zjdDzqn54OsxDNUcQ2MU0cXbdtPeDmmc0C4kLkGp7WYtZEy40eZG6kdFcR23Gu-X-Vp5y9psgT7RD8e7VdRX87IlktY9XwORrZWoIxHa5Cy6WiEk8bHHdQwT2UmeIEiit_-zIHkGHHZc96QbdCxdi_FSsM3AUid8rP5O0lUq3czsS_M3ljht0QRqHCtKHSiElG1XBZ5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشتی ایرانی که از فرمان ایالات متحده سرپیچی کرد توسط  یک هواگرد آمریکایی مورد هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/144847" target="_blank">📅 02:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
چرخش عجیب فردوسی پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران ، میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/144846" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba1e9e2c5.mp4?token=EmnUoPUjP_KXBQRhs-4uwSNIOjUaEcBHN6rxegwNfeGOw979q5bfdGrFQu4IISy5TPW0vTQ0ewhOUlklcgsQdfu33t1LFk47vigaA4moOqAwIfDKRT-SqIE1Ey6eGpG-Zw8_FjzgzdCYHfY4OSiXzAV5Kh981PhR-cBvbH4fAegcIZiQCRmVNXHm7O6J_f6rbD7yBgToUqrtF2hfO7ngcG3xPtRWBfPzGvEXvzAqIPaKxnwaKT9Zo-4X16DB3iOPlnI_J37jYMKcVDiV2dQ3AD--6XLQ2dbToG_fnCOzucyTH9CReeXiwP16cS1xRv8_vr20-2J6XcZ7k2A47UbjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba1e9e2c5.mp4?token=EmnUoPUjP_KXBQRhs-4uwSNIOjUaEcBHN6rxegwNfeGOw979q5bfdGrFQu4IISy5TPW0vTQ0ewhOUlklcgsQdfu33t1LFk47vigaA4moOqAwIfDKRT-SqIE1Ey6eGpG-Zw8_FjzgzdCYHfY4OSiXzAV5Kh981PhR-cBvbH4fAegcIZiQCRmVNXHm7O6J_f6rbD7yBgToUqrtF2hfO7ngcG3xPtRWBfPzGvEXvzAqIPaKxnwaKT9Zo-4X16DB3iOPlnI_J37jYMKcVDiV2dQ3AD--6XLQ2dbToG_fnCOzucyTH9CReeXiwP16cS1xRv8_vr20-2J6XcZ7k2A47UbjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرخش عجیب فردوسی پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران ، میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/144845" target="_blank">📅 01:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=BEtvcRYd3q8UtrIz1lDhQZNkHWcEs7rqAwNqWgw1RzNyqdyxeUdmZRwGlOaQD5AzbWf7O3qz3ztzp97Y6uqIQiI15yyPk1El0qpIOD_iqGr5_RrZxNKk9QKZCc2ndFoaqFc8gJ03xPkJ3ywcdzYIiUuoFGQmOEti1VpRqUe7XGdi6q2JV0r8IPHTsDh9V3iC2Pq_oDjMEzhlqWJWtT3dlHHlqks00zPmSQRppZ5yQk-WXqQJvuvD-_UZhHYQzJWuAnVxqbDjOXvLH7n81lqdJp7HErSbgOuECIWGUlwtLJRDd-_58aw6BkOrVoj5aZUgIeqx6_3D6azTekiYw-HlZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=BEtvcRYd3q8UtrIz1lDhQZNkHWcEs7rqAwNqWgw1RzNyqdyxeUdmZRwGlOaQD5AzbWf7O3qz3ztzp97Y6uqIQiI15yyPk1El0qpIOD_iqGr5_RrZxNKk9QKZCc2ndFoaqFc8gJ03xPkJ3ywcdzYIiUuoFGQmOEti1VpRqUe7XGdi6q2JV0r8IPHTsDh9V3iC2Pq_oDjMEzhlqWJWtT3dlHHlqks00zPmSQRppZ5yQk-WXqQJvuvD-_UZhHYQzJWuAnVxqbDjOXvLH7n81lqdJp7HErSbgOuECIWGUlwtLJRDd-_58aw6BkOrVoj5aZUgIeqx6_3D6azTekiYw-HlZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتش آمریکا استعفا داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/144844" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFvX83o9Afp-5fJ0N_cm7sSOEc5wgM2hBehReDnDM6nh2vXXNu-V3sfyVfkAV72xnDj55qjFlEAlFR2du_j4ZBrlSOAS8cpT5MyaeE3SDr13wxRCSJVTztvCphU1AQ-GPcAMr2GvOMQ_JNY16UJkaOQpF7iHBXv4mQzvCQi1txEb-2cIQq4NFOMWJW8qpUW7PfqkL7D3BQOI6yGGqi55NbfMbvKQj2euLOel91SvWhc-3PDCV9C3ct3ojoUbxXd5TAkaclA5KKkEpmfhcK_KPVdvXAXBW8TyWtQBOlDYJG3SUNRKCl8nbty8kCngT4xbqIcy1BUBABRucvJSWlP4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
صدا و سیما برداشته پیام صادقیان صاحب چندین سایت شرطبندی و یکی از مروجین فحشا تو ترکیه رو به دلیل حمایت از حکومت آورده تو برنامه زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/144842" target="_blank">📅 01:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLeC8hWev4EKeNu9fyneRFyIxirWbFEl_L-gpDj1HEMuKyjZhegxg_urGF23UvPCUSgZn41vJaqNYuqe2onB3_Zvt_C6ss-AIvNV8dBAjiMFx2RTAhr4AIjKIfAcaD98bj7MfmuMft_5SJUpYvNrZf-2LUTFm0n-4i5vkdcpJj-MY9QnPl9S4BOpw1bVJa_MjPkS25APv6b5qTuMwSwZ2IQSA4iWtSAyejfAO3BgrEw59SIG4l7OjKr-hA7LNtJvnJgu59NWwUj3JWB07dv1xW0AAZ-dQQxxVLMyR6e45DQb_yTjBWxEesYtHIq2LI0i3Q7ZSmckkAcW8tP7V8s54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
تو ایران 60 تا 80میلیون نفر حامی نظام هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/144841" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/144840" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111cb2948b.mp4?token=ajBI7MhulQeU1vvPvrOCuoFXaSrduMXSCpjXklxEMV6qSA8DxNbIhs6sS6zkLg2KjW-CkVB6zEWv8aRLkwBPdi4OmH38I2RJNySVDpcwloK3aqO3mXGK4HOYw0WMsEVRI22gcS-PEND2ig7Uf65x5f5YHOLZtrQUmisEPx2LjNL07dBZ9SjSvwsvDi6F1e-HZzFs0kc4Fu7_J44XM-k4mYSdptceaXDHyn-0Zg4ihBU1zH3hMwhu7i-Yo4xwZRPWz7oj-bI9Xh2Jm5bOd_tuL3-IKxRYOA8R3ifxC4AZVGniC0gT738RZKtaMtajD_K5al8GSfGkpIJq6GLiv3Kb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111cb2948b.mp4?token=ajBI7MhulQeU1vvPvrOCuoFXaSrduMXSCpjXklxEMV6qSA8DxNbIhs6sS6zkLg2KjW-CkVB6zEWv8aRLkwBPdi4OmH38I2RJNySVDpcwloK3aqO3mXGK4HOYw0WMsEVRI22gcS-PEND2ig7Uf65x5f5YHOLZtrQUmisEPx2LjNL07dBZ9SjSvwsvDi6F1e-HZzFs0kc4Fu7_J44XM-k4mYSdptceaXDHyn-0Zg4ihBU1zH3hMwhu7i-Yo4xwZRPWz7oj-bI9Xh2Jm5bOd_tuL3-IKxRYOA8R3ifxC4AZVGniC0gT738RZKtaMtajD_K5al8GSfGkpIJq6GLiv3Kb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمام پیش بینی های ۱۸ ماه قبل «نوید کلهرودی» دقیقا به حقیقت پیوست و‌ چون هرچی گفته بود اتفاق افتاد؛ بازدداشتش کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/144839" target="_blank">📅 00:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb3fQjxs022ol-L4dkEEdv2jpilbZcp6cPf4kkeXQQGoCMie5kI1nxNdxB11d2u-9IaEZ4-fur0RdcAJGPGi1KJ-V8gU85KMIi7fidqWqvOwIlqlRDK5-qukg6MJwoQFQJqOPAieDKLF5BjUDbTxbGvZKCijjlknBwInVFvONEz1pJsWfJIQOEnc1LFQ9Ygf8KwUgnptwWkMhZlJeBV9vbpNndr0CNfUMz81-1UCqiyhejf4LTcA3xaq1KPu-mJsReKDUyqRT6bCV-VfXh2d-musozyfz2flCaxf12hiJSxDMsRseROihvBswVIwHKlp17N212y3pZ4Ootnnfvi70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر راه:
رادار نداریم و پروازها رو ذهنی هدایت میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/144838" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کارشناس صدا و سیما: ماهم میتونیم مقامات دشمن رو ترور کنیم اما این یه کار کثیف هست و ما دنبال این چیزا نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/144837" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrA9OcxTFlBaf_5xemxL7LGuL2dKEuAmm6uWpoPPFzRkch28OJIR6DiYDDxAiz0Ojc0qnLcUHm4t4D710a1lLfBbmBt4qR3U5gpMx3UgMVKpz_nsAL9PZt2yWhF68KgkCe-ptvWac2NQ8RyBqGSVvkUBeuiFBjoAbKDDvta3gLfxOm4jkJUMIWir-D1LUbhovQMwFIwkpX3sIigDwhRD1y3jmlguNJHC8iY6_jhmfxWppJs1tQ1DLh3B1IphTCFnvqvq75gHsrQTuVeRztddR2a0hhdqGf_b-CBhMgyR7Q7yztRMUwI-N9il4pstBrFDbwUFtgnj2zSNNaV54gKZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴۵۰گرم چیپس 1,000,000 تومان
💢
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/144836" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqhyeGrmmeuUD3eSZI2icbim625l0O3zhoPck9on8wA9whPdjOJJrjWpwBsFI29KVqb2LTxYq6tyHczDZwVBasmxFkC1bbSoDNRBvMnFwT5cMq5SeUswIvuAv7m7SW_JRhgwcV5BtE8-X8-3h0AwsQnJZ4L42hk5VrvRQyctXuomeuM_bnhgEv9VMB7U-DDwnJsll0Z2X5fF0TYbMmObksyzCqXVmIjNjUNcb2dfnfq--v5jYzgFM87-fG3daTi4IcnHAOT6TT5a9H2MQPBQUe2IkneMXjR_EyAmoAykQi08RGV3YsE16V000xLLn2LESg8kiDFrdtZC7gzu3_IV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: قالیباف و عراقچی با ایالات متحده تماس گرفتند تا سطح تنش‌ها کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/144835" target="_blank">📅 00:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f8e52b27.mp4?token=k5ao_hVggf324D4GVF1dzwbASOqZ0oJbOvIzvvXqSxX2s8QnyrciJqAFMxbSXRx0QV5nE6a-9faRtp7-HOZMvuCiFQ-H1VpGer19He16Z-KKWIGWt9MOrlHttzw19ouZMDd_mKgxRTDQ1uvNAtzio_k92OESimT3s8AMWvxUz7EyyhE1bX7BOvGbv-xddw4Q-jnaHGlsABbehOMDigdgtPBaCwg53yj-U9RFNyBgcotL6MmCR0uO6yniuMEXeCI15_SqtCCMrN_G51xw5fvDi1M1513iR0YFswhtUuANAdHin1ibf_-Q0Z0If0StrJrKQOiTzutAM5LMhFIx7q4Nkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f8e52b27.mp4?token=k5ao_hVggf324D4GVF1dzwbASOqZ0oJbOvIzvvXqSxX2s8QnyrciJqAFMxbSXRx0QV5nE6a-9faRtp7-HOZMvuCiFQ-H1VpGer19He16Z-KKWIGWt9MOrlHttzw19ouZMDd_mKgxRTDQ1uvNAtzio_k92OESimT3s8AMWvxUz7EyyhE1bX7BOvGbv-xddw4Q-jnaHGlsABbehOMDigdgtPBaCwg53yj-U9RFNyBgcotL6MmCR0uO6yniuMEXeCI15_SqtCCMrN_G51xw5fvDi1M1513iR0YFswhtUuANAdHin1ibf_-Q0Z0If0StrJrKQOiTzutAM5LMhFIx7q4Nkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کلمه به کلمه این صحبتها رو باید روی سنگ حکاکی کرد تا عبرت آیندگان باشه.
🔴
حرفهایی که زنده‌یاد رضا فاضلی ۲۰ سال پیش گفت و کمتر کسی توجه کرد.
🔴
انگار همین دیروز گفته شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/144834" target="_blank">📅 00:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/144833" target="_blank">📅 00:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/144832" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
کرملین: تعیین بهترین شکل میانجی‌گری درباره ایران دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/144831" target="_blank">📅 00:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saDGSkCMO8UGHq5CLU2tZ_YcvviFwjL4pmzGa-Y2yp4qiICw9FSc_cw8ApJr-m4c5T7K5qSdNAEvqjhEq5Dxuh-u09zO61c0klZXq1XMU_7m0-yLF11hOLJO5QnHDO2BmHFVaGeDbu63ClNsU77C1DQcqtJ5C898Gl2cOh1lzZWRKjNrCpTHhCp196jtkoFoQONJlbZ11Af5h5uVNB8UMc4D0kceSBPfzmkGlpKs201V3Id5j-P4QO5Br9q5rcnzRcmRgGU_EtCSS5skbi1bTnQ6fN5iKP-nwL-M-BdIaYStWcZgfT7kmlITMEmUfAyS-Sy0_31N-sw8u94EPzJcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا از وقوع حادثه‌ای با حضور یک تانکر و نیروهای نظامی در اقیانوس هند، نزدیک عمان، خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/144830" target="_blank">📅 23:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4ac4eed4.mp4?token=hYilAJuSJLHQXuYF731lSAGwFD_LyIdcgBlhiyxnIrtqxS4GRSW39noOh6dTRa5Xi4Ry2ilkJt03GC569_-nq7yslR7ncyHz0oPaRdvfe1LYOzDXU9riPNiNS7XzkZWimyRbtCo7arjnNy0hHbA-ralHnnozCwrNdRRIX0ZUf6vUGE7qYwiOWljcY07Ce8nZWNbc1Gr9NKsUl6UY0qoByfKndukxms2svgoplCVYnV6jN0aoqNIow8GC16pwSK3h2dvXhe54BxN1UvW8Lroh8HIqNp2o78WvEBhFeEUMAyd-nt-QwfYqQBm0F6fBoQzPQ4PYNMkF4PQKFO3NoqiqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4ac4eed4.mp4?token=hYilAJuSJLHQXuYF731lSAGwFD_LyIdcgBlhiyxnIrtqxS4GRSW39noOh6dTRa5Xi4Ry2ilkJt03GC569_-nq7yslR7ncyHz0oPaRdvfe1LYOzDXU9riPNiNS7XzkZWimyRbtCo7arjnNy0hHbA-ralHnnozCwrNdRRIX0ZUf6vUGE7qYwiOWljcY07Ce8nZWNbc1Gr9NKsUl6UY0qoByfKndukxms2svgoplCVYnV6jN0aoqNIow8GC16pwSK3h2dvXhe54BxN1UvW8Lroh8HIqNp2o78WvEBhFeEUMAyd-nt-QwfYqQBm0F6fBoQzPQ4PYNMkF4PQKFO3NoqiqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «ما به کالاهای آن‌ها نیازی نداریم... بنابراین اگر تجارت با آن کشور را قطع کنیم، عملاً ۴۰ میلیارد دلار به نفع‌مان می‌شود.
🔴
اگر همین کار را با چند کشور دیگر هم انجام دهیم، آمریکا به یک ماشین بزرگ پول‌سازی تبدیل می‌شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/144829" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebac51303f.mp4?token=gCcVFRFf4m8TD0nUQ3j1r-NOVSjF5yB9JUipn-MGoQJ2UAS6F4GLmEbqcux5wzP0l2XVtMmZ93eVyzy7VxIs_0sIUzRL38yB78pxxI7KeDVRKbQDuHa9eWTgTQ_znjkVRzRkFxi3_-HyszXwojtjF6fGyG57YR-0UVJfBj31kaPTV7CUC94yix2gkjbSQKzcYljLvgA3krvtg7Ba7GSp64hvSB12XhH_1y6f19dviNmqbcfCVbKJcIx9dKTHSruRWrGZNaRVNHELt6Zf0ieZ5iCqJGaOyvb0cYE3RkT85a46mOUgC1mD-V6FjswXQWTVtZWO5JNVUGrex9OGF0Hgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebac51303f.mp4?token=gCcVFRFf4m8TD0nUQ3j1r-NOVSjF5yB9JUipn-MGoQJ2UAS6F4GLmEbqcux5wzP0l2XVtMmZ93eVyzy7VxIs_0sIUzRL38yB78pxxI7KeDVRKbQDuHa9eWTgTQ_znjkVRzRkFxi3_-HyszXwojtjF6fGyG57YR-0UVJfBj31kaPTV7CUC94yix2gkjbSQKzcYljLvgA3krvtg7Ba7GSp64hvSB12XhH_1y6f19dviNmqbcfCVbKJcIx9dKTHSruRWrGZNaRVNHELt6Zf0ieZ5iCqJGaOyvb0cYE3RkT85a46mOUgC1mD-V6FjswXQWTVtZWO5JNVUGrex9OGF0Hgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «همه می‌گفتند غیرممکن است فرانسه با دو یا سه برابر شدن قیمت داروهایش موافقت کند، اما آن‌ها پذیرفتند.
🔴
آن‌ها قبول کردند چون من گفتم اگر این کار را نکنید، روی تمام کالاهایی که از فرانسه وارد آمریکا می‌شود تعرفه وضع می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/144828" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما وارد ایران شدیم و داریم حسابی پدرشون رو درمیاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/144827" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ درباره مهمات: «آن‌ها می‌گویند ما [مهمات زیادی] در ایران استفاده کردیم. در مقایسه، ما در ایران خیلی کم استفاده کردیم.
🔴
جو بایدن بیش از ۳۰۰ میلیارد دلار تجهیزات و تسلیحات را به‌صورت رایگان در اختیار اوکراین قرار داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/144826" target="_blank">📅 23:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ درباره جنگ ایران: این برای ما جنگی نسبتا کوچک است؛ این یک جنگ بزرگ نیست
🔴
اما میدونید پول های ما کجا رفت؟ اوکراین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/144825" target="_blank">📅 23:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار: «دلیل دعوت از روس‌ها برای نشست گروه ۲۰ چه بود؟»
🔴
ترامپ: «ما دوست داریم با همه روابط خوبی داشته باشیم.
🔴
یکی از دلایل موفقیت من این است که می‌توانم با همه کنار بیایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144824" target="_blank">📅 23:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5fc9c854.mp4?token=LNRH-Wqz58qmP8XWCN37_DCSlHrg3wOpOXiSX4cvFiBBTe5M4ZWtbTdtZN5zzEYtcGyZVE2MM7GuZ5oXPjpEnQeFC9CzNPA6UGn8PX2QTk6a6K6acEo8LuqfUnxj7I9-T5YTf3Pmbjz5lrVL37PUI11bNQxyrIfF2svakkmVjDs37w1-ht_Em_9VCox5UHWFboUBA6iO4Svup5lj7AXxhew3I0jXdafqZbI6q9IfYDI8WQ1GCBdec6PqIRoNcQHqOuBub3_EzKHFRXcvfNQwViIVoZP28XtWSiqoGquba07cspHGS_TeXu8bm3wCT_gQXgi-otjBAUI7YU960gFPnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5fc9c854.mp4?token=LNRH-Wqz58qmP8XWCN37_DCSlHrg3wOpOXiSX4cvFiBBTe5M4ZWtbTdtZN5zzEYtcGyZVE2MM7GuZ5oXPjpEnQeFC9CzNPA6UGn8PX2QTk6a6K6acEo8LuqfUnxj7I9-T5YTf3Pmbjz5lrVL37PUI11bNQxyrIfF2svakkmVjDs37w1-ht_Em_9VCox5UHWFboUBA6iO4Svup5lj7AXxhew3I0jXdafqZbI6q9IfYDI8WQ1GCBdec6PqIRoNcQHqOuBub3_EzKHFRXcvfNQwViIVoZP28XtWSiqoGquba07cspHGS_TeXu8bm3wCT_gQXgi-otjBAUI7YU960gFPnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی می‌دانید؟»
🔴
ترامپ: «معمولاً هیچ‌وقت چنین چیزی را صریح نمی‌گویم، اما پاسخ بله است؛ دلیلی برای استفاده از آن وجود ندارد. چه سؤال احمقانه‌ای!
🔴
آن‌ها کاملاً شکست خورده‌اند. من شکست‌شان داده‌ام؛ حالا باید علاوه بر آن، از سلاح هسته‌ای هم علیه‌شان استفاده کنم؟ چه سؤال احمقانه‌ای!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/144823" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ درباره ونزوئلا: «روسیه آنجا بود، چین هم آنجا بود؛ اما دیگر نیستند، مگر نه؟
🔴
می‌دانید حالا چه کسی آنجاست؟ آمریکا.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/144822" target="_blank">📅 23:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ درباره جنگ ایران: این برای ما جنگی نسبتا کوچک است؛ این یک جنگ بزرگ نیست.
🔴
اما میدونید پول های ما کجا رفت؟ اوکراین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/144821" target="_blank">📅 23:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/144820" target="_blank">📅 23:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad44d1a82.mp4?token=ozdR2Ew4FGo7ODtQJphzq29NSzqcW2BzUjNGooV9rsAG0MAbhJbBi1PZw0M0ppSGONL0NnKeoqhNJoY2FFvOvido4JfPsAdrekhk26AhN-eyK-nft8p1QOgYTrOrcf7ZHFjz9Hebv2fRDsEe0feSC-_kmBu1jQX_tLqdhiW-niB5uYiDH0Zr-O6XX07krCiM7-Bh77I-d_2Nb0cECQmH76bs6A4DpOSAXoJMIwRT53_ww7Iavh_PS6v53fMfBKmxclj1x_7SDGSY1Qm8iVqxNxWe8tI9c49sBtgX_UzKnGiMJYq4cgluIqz_728bnWW4hx3FNKCRrey7kixLACodXjq_mpKMVZSgK3diqvsNhAboc1LuZHArpch2_Eg4iohifs8KGNUMup70Bo_qb_mxgpIUfrMJ_lxkjq_G2yBeWYP5Duhhlsni-pTEZpndz05gXwDJw-gGtlmu-n8JDQDdHL_n2sKLrO8-FvUYapXAHczir5D_59-Infjy-m9tnFoO3pzDp_5OUBRI4V1XoC2hzOopBTso_Stcd3rdxIRcFvd-zwcwuBJFu52NYlqugb-JmLgXQSUZ63QaNITHA2di-bYrI4-dTi8dFciK39i7r26FNifDXD_1JGW5IT6Q9JDDDQjuuFPXuEOoYYsxYAynv2h0JV3Ey2LVeM4sTwgd3Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad44d1a82.mp4?token=ozdR2Ew4FGo7ODtQJphzq29NSzqcW2BzUjNGooV9rsAG0MAbhJbBi1PZw0M0ppSGONL0NnKeoqhNJoY2FFvOvido4JfPsAdrekhk26AhN-eyK-nft8p1QOgYTrOrcf7ZHFjz9Hebv2fRDsEe0feSC-_kmBu1jQX_tLqdhiW-niB5uYiDH0Zr-O6XX07krCiM7-Bh77I-d_2Nb0cECQmH76bs6A4DpOSAXoJMIwRT53_ww7Iavh_PS6v53fMfBKmxclj1x_7SDGSY1Qm8iVqxNxWe8tI9c49sBtgX_UzKnGiMJYq4cgluIqz_728bnWW4hx3FNKCRrey7kixLACodXjq_mpKMVZSgK3diqvsNhAboc1LuZHArpch2_Eg4iohifs8KGNUMup70Bo_qb_mxgpIUfrMJ_lxkjq_G2yBeWYP5Duhhlsni-pTEZpndz05gXwDJw-gGtlmu-n8JDQDdHL_n2sKLrO8-FvUYapXAHczir5D_59-Infjy-m9tnFoO3pzDp_5OUBRI4V1XoC2hzOopBTso_Stcd3rdxIRcFvd-zwcwuBJFu52NYlqugb-JmLgXQSUZ63QaNITHA2di-bYrI4-dTi8dFciK39i7r26FNifDXD_1JGW5IT6Q9JDDDQjuuFPXuEOoYYsxYAynv2h0JV3Ey2LVeM4sTwgd3Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: گزارش‌هایی رو دیدید که می‌گن هگست قصد داره در انتخابات ۲۰۲۸ شرکت کنه؟ ممکنه ازش حمایت کنید؟
🔴
ترامپ: اون داره کار فوق‌العاده‌ای انجام می‌ده. هنوز خیلی زوده که درباره این چیزها صحبت کنیم. آدم خیلی خوبیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/144819" target="_blank">📅 23:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dcb827cd.mp4?token=Z5i4cff-hdkvuyOW95nLkQFWlr_9KuQvM-KNpPCJOz0Z1p37xBcD3SBEQL9PPQE4iVPELGIuHPLXSL0TpRG7v5Yz2my1m_Vu8xT2jFu2a5lptW1ex2JU_J1jzK_UnRI-HMaAzVGRCwCQz5yjrzJWCgbOuqsbJ4wshMEto_nxKx_w6aWXlIPeL-UOtRZCc6vEn-1HlK2nwpEmEtWaeABqJoJRvm3SBWSAW98t8q5FnRt8bXBFa7s6Fp2015ZsNOlw3poB12roVFavNoxhlN2EDENSjl6hXxaG7qPejvxxHlZWS0qLaHZJMk8WXZq3vlOC_8a3wcu9UwT_IO6Qrwucdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dcb827cd.mp4?token=Z5i4cff-hdkvuyOW95nLkQFWlr_9KuQvM-KNpPCJOz0Z1p37xBcD3SBEQL9PPQE4iVPELGIuHPLXSL0TpRG7v5Yz2my1m_Vu8xT2jFu2a5lptW1ex2JU_J1jzK_UnRI-HMaAzVGRCwCQz5yjrzJWCgbOuqsbJ4wshMEto_nxKx_w6aWXlIPeL-UOtRZCc6vEn-1HlK2nwpEmEtWaeABqJoJRvm3SBWSAW98t8q5FnRt8bXBFa7s6Fp2015ZsNOlw3poB12roVFavNoxhlN2EDENSjl6hXxaG7qPejvxxHlZWS0qLaHZJMk8WXZq3vlOC_8a3wcu9UwT_IO6Qrwucdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما باید پایین‌ترین نرخ بهره در دنیا رو داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/144818" target="_blank">📅 23:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8afb17985.mp4?token=nhUZdz2UW54bN8WrQBXriifsvotJu7WySmYZFpx87Jb_7zE_PopTMvoVTLlXMGUZGKEWnvFclGlMz_tA_HPEMYff2yLzbfl1--_vza0gSOUxIHdyXzFGjk6x8npHam6Y18jRxWQwFXDEYIkMkeYs371AppYcc4E-SnpHTD81CV3X9_feDVosoYoEHaVJReWfF9NV_JErh0-i1RCRZlNBkhBPFPmxVbAUeqHib3rmwljHfrD4rSGwAgdF70xwoiqlWeX-C3zyxAq20P2kdrsLx218vg8u1bDXKVVOSd-7mRabQOFfQ-5osq-_K7Y4h75ih4oUny0CFz-3ugTxBIISpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8afb17985.mp4?token=nhUZdz2UW54bN8WrQBXriifsvotJu7WySmYZFpx87Jb_7zE_PopTMvoVTLlXMGUZGKEWnvFclGlMz_tA_HPEMYff2yLzbfl1--_vza0gSOUxIHdyXzFGjk6x8npHam6Y18jRxWQwFXDEYIkMkeYs371AppYcc4E-SnpHTD81CV3X9_feDVosoYoEHaVJReWfF9NV_JErh0-i1RCRZlNBkhBPFPmxVbAUeqHib3rmwljHfrD4rSGwAgdF70xwoiqlWeX-C3zyxAq20P2kdrsLx218vg8u1bDXKVVOSd-7mRabQOFfQ-5osq-_K7Y4h75ih4oUny0CFz-3ugTxBIISpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا ونزوئلا باید از اوپک خارج شود؟»
🔴
ترامپ: «این تصمیم با خودشان است. ما رابطه خیلی خوبی با ونزوئلا داریم. می‌شود گفت به‌نوعی مثل یک تیم هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/144817" target="_blank">📅 23:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. کل قضیه هم همینه؛ موضوع چیزهای دیگه نیست.
🔴
بحث اینه که ایران، چه برای ما به‌عنوان یک کشور و چه برای کل دنیا، نباید به سلاح هسته‌ای دست پیدا کنه. اگه ایران سلاح هسته‌ای داشت، اسرائیل نابود شده بود.
🔴
الان دیگه اسرائیلی وجود نداشت و احتمالاً خاورمیانه هم وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/144816" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2794d40dd9.mp4?token=ewvUwnaxxVmbvlxycrYrpvyinUoJpYqM5Wlgg7FxYWYU3IEDT-bCCrhFc9e-xN6gdbpfOgskKV3Neli9ydMaXFtPQj6rhUATJRp3m_rNzvVyQo1iatcknjdyo1X9CpB5YBs20GDBdYuOQLHg5UIMH-UrTlCbdByZQb9ozQdk6vL7WO-5ulWj47N6cDlNyEpZmDOGnUO81d1elEvyUVErIVjOed8sh4yO8bIQvCZagSLSbeDrWnsxNfzStwpWcEV1XQJTF1Tt1XebJtMXUaV4zdccCKX4WQ4QOVzcDcbtNS3wyPqTOp_rgT-50xzJxEZus1Ds2fLYiX3uYZ7-mHgbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2794d40dd9.mp4?token=ewvUwnaxxVmbvlxycrYrpvyinUoJpYqM5Wlgg7FxYWYU3IEDT-bCCrhFc9e-xN6gdbpfOgskKV3Neli9ydMaXFtPQj6rhUATJRp3m_rNzvVyQo1iatcknjdyo1X9CpB5YBs20GDBdYuOQLHg5UIMH-UrTlCbdByZQb9ozQdk6vL7WO-5ulWj47N6cDlNyEpZmDOGnUO81d1elEvyUVErIVjOed8sh4yO8bIQvCZagSLSbeDrWnsxNfzStwpWcEV1XQJTF1Tt1XebJtMXUaV4zdccCKX4WQ4QOVzcDcbtNS3wyPqTOp_rgT-50xzJxEZus1Ds2fLYiX3uYZ7-mHgbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:‌‌ اونا واقعاً نمی‌دونن رهبرشون کیه.
🔴
آدم‌های افراطی رو دارن، ولی از نظر نظامی تقریباً نابود شدن، چون توان نظامیشون فقط بخش کوچیکی از چیزی شده که قبلاً بود.
🔴
واقعاً فکر نمی‌کنم خودشون بدونن رهبرشون کیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144815" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceccfae54c.mp4?token=JCh_J85fbqAVZDOpgS8x3G1x3G6k_UCVVA7AIg1R7jokdQgRnzNgTkmu8yO_qkA2c-H1xuOR5F8sQ3PkHiwjSwfb2xuzEQciZuP75wi-SUh3XG-hydY3X0m2D1LRsuUlV2rkDi5AUZllcuibUhPxZx8wK4f87re4EV8YoCl5__VzLP4c-dLXDx6SnYazWMBbJNv147DHVDMMwZWxJT3KlbxYMEOdYQipq9keJiw8FNpP_XXyloFRzfxPfJ4uNyFYP2LeRP4-TO7-wKtRWMNz5qgEx4ClsOMOxk5meEYXg17MCc6DryAof0YQXhrXlbbswWozVo9hCHVwQgYvHICn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceccfae54c.mp4?token=JCh_J85fbqAVZDOpgS8x3G1x3G6k_UCVVA7AIg1R7jokdQgRnzNgTkmu8yO_qkA2c-H1xuOR5F8sQ3PkHiwjSwfb2xuzEQciZuP75wi-SUh3XG-hydY3X0m2D1LRsuUlV2rkDi5AUZllcuibUhPxZx8wK4f87re4EV8YoCl5__VzLP4c-dLXDx6SnYazWMBbJNv147DHVDMMwZWxJT3KlbxYMEOdYQipq9keJiw8FNpP_XXyloFRzfxPfJ4uNyFYP2LeRP4-TO7-wKtRWMNz5qgEx4ClsOMOxk5meEYXg17MCc6DryAof0YQXhrXlbbswWozVo9hCHVwQgYvHICn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «حتی در مورد تنگه هرمز هم، شی در مقایسه با آنچه می‌توانست انجام دهد، نسبتاً منفعل بوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/144814" target="_blank">📅 23:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: تورم تو ایران به ۳۵۰ درصد رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/144813" target="_blank">📅 23:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWjdz_DquhUzJQFRXY5A2BCYBm1mRkfCqsDo7Sl28xv-GfEUpoxj_tJpQA8w38ZpJtasfQtecGWCcFrlcou6TScAZnxr96JqnzwaoMj-IU2r5QpGVLqNgGzQjr5yfaR1TGOcEe-uPkOwW_3t_3kCJYjpvADjrH0sMOLukEv5tEQfcGnnzJlarc1S-NejqgUvpTR_wpEoYUNGr24O5T2Z14fYyUcoTq1fYEQ7gzd2yzPyoIxFP8qui0OInsJ9unll4APEsMkcIXIBADZEnB5PtI5Nqi-_d-hr0oTtpyGlKK_S8HpcQ1h9pb3vaKC_gnXi2j0dDJE653fLaInL1OhqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله اکونومیست که قبل از آغاز هر سال اتفاقات اون سال رو با یک عکس پیش بینی میکنه، اتفاقات سال 2027 رو پیش بینی کرد و اعلام کرد سال 2027 سال خوبی نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/144812" target="_blank">📅 23:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef5c4d9a0.mp4?token=Asi__c7xyUklHCNoNY33cRRQvheErQjg9QsxdTBZAt1L-_K1CJ0MzX7ZLzYNvlTMECz_GxJf06-wd77tzv-mg_BEgSigLrSTSjZ22MZbgK9a6GVo9Lit6v_KPVNR-Qlt2bpxVOH1Obbai4eBcsyqBqJjjRPYRmtJY-t_8m7i081WNTiaSZ5lhtXaTDQHVoP1C310GPjw6wUFZLjSGElnprWuQ4uxCg--ZUkBqZG2HOdeC6cjJBLWFQLbSXzZztu81II-sXOlPPAez3nxZx0G-0kk37Zzn70wGFs5KMw7t29Pc2iBUP92yesYbi8gCnQUaaJJ2LUvtNyvQRJ0cEXNLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef5c4d9a0.mp4?token=Asi__c7xyUklHCNoNY33cRRQvheErQjg9QsxdTBZAt1L-_K1CJ0MzX7ZLzYNvlTMECz_GxJf06-wd77tzv-mg_BEgSigLrSTSjZ22MZbgK9a6GVo9Lit6v_KPVNR-Qlt2bpxVOH1Obbai4eBcsyqBqJjjRPYRmtJY-t_8m7i081WNTiaSZ5lhtXaTDQHVoP1C310GPjw6wUFZLjSGElnprWuQ4uxCg--ZUkBqZG2HOdeC6cjJBLWFQLbSXzZztu81II-sXOlPPAez3nxZx0G-0kk37Zzn70wGFs5KMw7t29Pc2iBUP92yesYbi8gCnQUaaJJ2LUvtNyvQRJ0cEXNLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
«وضعیت تنگه هرمز را بسیار خوب تحت کنترل داریم.
🔴
به‌طور میانگین، هر شب ۳۰ کشتی از آن عبور می‌کنند. این تعداد زیادی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144811" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9246d8d841.mp4?token=HvFqY8flqdBnpe2GPrub-N8t191zWy6dqkGMZEqGYkniOZzXUHjVLKgLSKD7VWoZYZXzWwKhp6MpY4tKlYc27_I4Q7a8S9uOvmsCyfxDAr0-AO98i6TjHIh1nQDnJbyHIfVvV7w4r5V0Or4a79L6XmbIsfKeslglqomucIkxoLvaVij4TS-JigmCy4kjBL6zMY66SqVORpy47dTbBD4qY0hIo8PHF1h4iK28XgOZ5U3I4qRbNLXYmchiT2XQYxoEVh0roWx4cmSXfcWpL8S7FOTuckupjzbo_PeWn01cSJ2D2njpl_90fg6wXt6h8LPvbTWjddt9N5OmE6L75UjPYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9246d8d841.mp4?token=HvFqY8flqdBnpe2GPrub-N8t191zWy6dqkGMZEqGYkniOZzXUHjVLKgLSKD7VWoZYZXzWwKhp6MpY4tKlYc27_I4Q7a8S9uOvmsCyfxDAr0-AO98i6TjHIh1nQDnJbyHIfVvV7w4r5V0Or4a79L6XmbIsfKeslglqomucIkxoLvaVij4TS-JigmCy4kjBL6zMY66SqVORpy47dTbBD4qY0hIo8PHF1h4iK28XgOZ5U3I4qRbNLXYmchiT2XQYxoEVh0roWx4cmSXfcWpL8S7FOTuckupjzbo_PeWn01cSJ2D2njpl_90fg6wXt6h8LPvbTWjddt9N5OmE6L75UjPYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
«ازسرگیری حملات به ایران، یک عملیات محدود است یا یک جنگ تمام‌عیار؟»
🔴
ترامپ
:
«آن‌ها یک کشور شکست‌خورده‌اند... این به آن معنا نیست که به آن‌ها ضربه نخواهیم زد. خواهیم دید چه اتفاقی می‌افتد.».
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/144810" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

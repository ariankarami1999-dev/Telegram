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
<img src="https://cdn4.telesco.pe/file/JxUApXNeeRg8RmR05A0xdd413RzMzWIvjQUqjwUk6RHHxqMQ5vop5KmTCR4bKbJwkKeJfMoqE0k9w5J42OtVV9UiNe5FaHN0J3_Wlmkm3YhMffyyD0p-6mRyjnWBygf9S_Rfhx26QsbSQbhI7q8AjxA2JG_xTJOhvygzd08k5nMbxJ9gm3Vf8wTEXGlo8wtnl68_f07G0Ona7ND5x5DX8j2RWxCcj4ubY-FVRv7SIge40kEPd5I0sza8d1b9k6mb1Ze_wmmV5jm8sJG1KXWckGUsGzyiye91cY7z6mCtWgooZ-HR9DtzkDE5X-85aJQlqFwGDfkNc6-xl5uuMd8I4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : شورای ملی ایرانیان آمریکا، معروف به نایاک (NIAC Action)، که از مهره‌های نفوذی جمهوری اسلامی در آمریکا محسوب می‌شود، از دونالد ترامپ در دادگاه فدرال شکایت کرده است. نایاک خواستار غیرقانونی اعلام شدن عملیات نظامی آمریکا علیه ایران به دلیل نبود مجوز کنگره شده است. در این پرونده نام نیما دیلمقانی، آلن بند(زنش ایرانیه عرزشیه) و پروین اسماعیلی‌زاده نیز به‌عنوان اعضای نایاک مطرح شده و جمال عبدی از چهره‌های اصلی سازمان در پیگیری پرونده است.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/24263" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24262">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo-tSBUMY3uqZ8gwGCruz9FCzvDRNPBvE9YAWVKBZpWjkAqWpilGaMZEv6TWub7R1DvEcrm7lruzDj7xxtiq9Wq2MzI15Y4tTSSL5rrb4zZHgZ7ivOCvfmgYlPrfFppQa4diww3DuxhHqHKoXJlZkWmmsvdID_1KBCr3j7Rs70_b57R4kuEc1iA1JQWasNFtmRZsabJjbh9sXaZVd6gc5ZcpwvZgyo_w5Hmd2U5G94dLsHaHS5XoBBAZLt-lznGDx5CL0QeZi1yQkj7ZGiP02pFQO2AvBLVOuuN13HJPwBlCBPjyEIOVHwr7QosZED-sHVfWDfnq-87R8jeI7kAr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانمی که چند سال پیش به عنوان بزرگترین دزد و جیب‌بر خیابون انقلاب تهران شناخته میشد، آزاد شده و به تازگی در رزمایش جانفدا شرکت کرده
@WarRoom</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/24262" target="_blank">📅 20:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ژنرال جک کین: شی می‌خواهد ایران جنگ را طولانی کند و نفوذ آمریکا را تضعیف سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/24261" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌بی‌اس به نقل از یک منبع: انتظار می‌رود دور جدید مذاکرات آمریکا و ایران هفته آینده برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/24260" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24259">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارشهای بسیار از اختلال گسترده در سیستم بانکی و دستگاه های کارتخوان
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24259" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24258">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتش اسرائیل: امروز صبح، انبار تجهیزات نظامی حزب‌الله را در منطقه سجده، در جنوب لبنان، مورد حمله قرار دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/24258" target="_blank">📅 19:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا برای تشدید تحریم‌ها علیه جمهوری اسلامی با بیش از ۵۰ کشور تماس گرفته است و به آن‌ها پیام داده: «در قبال ایران یا با ما هستید یا علیه ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/24257" target="_blank">📅 18:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏اکسیوس: واشینگتن خواستار امتیاز هسته‌ای از تهران است
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
@WarRoom</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/24256" target="_blank">📅 18:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24255">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=u4b5Pq7heji-Duby4eBePsqAOIZ89N7bYH_8bazy5QB3jApQpBQeGwjuLPrH2I2Mfq-jnv4HZXWMI5j_CbmcUMddWWLzz-R3LCmkAcss55jqtqEyTQHp79iHGgMyvfBlxopYn2wOop9wX4_XKNjMbjcUThqXLyp4xGXPdZUGfpd9LnNyJ40X5TpyRfrje32tQZUEARS-rHizSLn8tw8tCCxLO210pPHY2QMTAw79v0m8Cb-iu4Zp1Ik7-Z4ZhwmK8tSrn1ThIpFm82EFqXzmJVcGALW4Xrga4Ayw1prrwy6fR4hxaU3FtLupm0tVDSf3pifX7UZ9xbDBuAQQPGU3_Vl6Su2-UQN3TjnAhYu7IMCt_2aNTVkDi6qBhwmeF_0MS7BlJvp-pJof878NUexctUx9ro4tdVLhF_CSBg8ulaDCnDngRRLHJeU3wvCLy08O2HKbX6_v-RCVRc1b-GE5w16PAZlmg_WsQ3BrsfI77M59dznPwNQ5lmlVdNQdOXmaIpTBkzDCQ8UaQJhUbdAJ-6Ww7NY9RSpbM3CVQFcDGSid7FuongS_muzxOC4iDjkcAwh7PzCqutGSWly6eTE16Y6S1eDcCOVjQqDfEOD8ivONgWz4QzVs86x475kK2-WrPLc94ww8tY29Sq9h10i5rPN5fE4Z7V7zU0RLDAUeAq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=u4b5Pq7heji-Duby4eBePsqAOIZ89N7bYH_8bazy5QB3jApQpBQeGwjuLPrH2I2Mfq-jnv4HZXWMI5j_CbmcUMddWWLzz-R3LCmkAcss55jqtqEyTQHp79iHGgMyvfBlxopYn2wOop9wX4_XKNjMbjcUThqXLyp4xGXPdZUGfpd9LnNyJ40X5TpyRfrje32tQZUEARS-rHizSLn8tw8tCCxLO210pPHY2QMTAw79v0m8Cb-iu4Zp1Ik7-Z4ZhwmK8tSrn1ThIpFm82EFqXzmJVcGALW4Xrga4Ayw1prrwy6fR4hxaU3FtLupm0tVDSf3pifX7UZ9xbDBuAQQPGU3_Vl6Su2-UQN3TjnAhYu7IMCt_2aNTVkDi6qBhwmeF_0MS7BlJvp-pJof878NUexctUx9ro4tdVLhF_CSBg8ulaDCnDngRRLHJeU3wvCLy08O2HKbX6_v-RCVRc1b-GE5w16PAZlmg_WsQ3BrsfI77M59dznPwNQ5lmlVdNQdOXmaIpTBkzDCQ8UaQJhUbdAJ-6Ww7NY9RSpbM3CVQFcDGSid7FuongS_muzxOC4iDjkcAwh7PzCqutGSWly6eTE16Y6S1eDcCOVjQqDfEOD8ivONgWz4QzVs86x475kK2-WrPLc94ww8tY29Sq9h10i5rPN5fE4Z7V7zU0RLDAUeAq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد شدم و بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادین!
حدس بزنید چه اتفاقی افتاده؟ حالا دیگر هیچ پولی ندارند، چون خودشان خواستند تنگه را ببندند. من هم گفتم: «بسیار خب، ما هم آن را به روی خودتان می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/24255" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=cAor5e5qJd0m9L7aU6NCyBSixHbQNnZsWmsOvmf7PqBCfFwsuWVIWcupa0wCnHt6ZFGL8yT-hVLp5BUvkGh7ULz0ewhc5wAqtyFyfF5oTJjtGFjxxYf8MANxiq1w54KsZs2Xke6FNv1xox6fhgGR8ThTtYS03EGLjrqz4jPWg-EWcxAz_yDATQP__kbfBKukqSUK_qsslLAGy4aPNWV6_puXfQ7_Bfv3M3i6syZUp363gmYM8JB0e_AbLBIS3qYv65CCjmKt-PFUOExhm8wisaoMVVLH8ogAEgIQ0n6ztpAEi_AJs4oA8I_DLpfFGQf6JyssZ5XsraG-hAhJVJt14rmHcur9dvvOFuDqXPPVYClySzbba_N3o7LF61c1k_B0OtEtKHmZ3k5bpUBUFa_9jdNSI9qAZPsEm0rgmNijcO3uoOindB8rlYyzZay-ILpmAC9eWvYUF_nsFYhlZGjzdXCTLA1b6xNc9TRJ2S48aUEzamex-xNZYILROaTPd2IUUbewWIrBWk90FnaFW4plV2tWCFW91gMXmr0dcGJA8hcd_xgwOZTKZrCaI8RRRdmmeH7NZ-pkZSq_kTXYLJ3noFhoNrvX-vNmFhpHxoiMkKjUxkxUinZyTbusa1BH6DfNlp8BL_lX-K1roV-g9C4E42DaP4OK53bLMaNR8iKuKM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=cAor5e5qJd0m9L7aU6NCyBSixHbQNnZsWmsOvmf7PqBCfFwsuWVIWcupa0wCnHt6ZFGL8yT-hVLp5BUvkGh7ULz0ewhc5wAqtyFyfF5oTJjtGFjxxYf8MANxiq1w54KsZs2Xke6FNv1xox6fhgGR8ThTtYS03EGLjrqz4jPWg-EWcxAz_yDATQP__kbfBKukqSUK_qsslLAGy4aPNWV6_puXfQ7_Bfv3M3i6syZUp363gmYM8JB0e_AbLBIS3qYv65CCjmKt-PFUOExhm8wisaoMVVLH8ogAEgIQ0n6ztpAEi_AJs4oA8I_DLpfFGQf6JyssZ5XsraG-hAhJVJt14rmHcur9dvvOFuDqXPPVYClySzbba_N3o7LF61c1k_B0OtEtKHmZ3k5bpUBUFa_9jdNSI9qAZPsEm0rgmNijcO3uoOindB8rlYyzZay-ILpmAC9eWvYUF_nsFYhlZGjzdXCTLA1b6xNc9TRJ2S48aUEzamex-xNZYILROaTPd2IUUbewWIrBWk90FnaFW4plV2tWCFW91gMXmr0dcGJA8hcd_xgwOZTKZrCaI8RRRdmmeH7NZ-pkZSq_kTXYLJ3noFhoNrvX-vNmFhpHxoiMkKjUxkxUinZyTbusa1BH6DfNlp8BL_lX-K1roV-g9C4E42DaP4OK53bLMaNR8iKuKM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: من توافق پیشنهادی آن‌ها را رد می‌کنم. آن‌ها می‌خواهند فوراً تنگه هرمز را باز کنند، چون به‌شدت در حال شکست خوردن هستند. می‌دانید، این را نه در رسانه‌های جعلی می‌خوانید و نه می‌بینید، اما ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز خارج می‌شود و دیشب ۲۹ کشتی از آن عبور کردند. آن‌ها می‌خواهند به توافق برسند و به‌نظر من این خوب است؛ من هم اهل توافق هستم، اما چنین توافقی قابل قبول نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/24254" target="_blank">📅 17:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=XIIG4IhyWLJgxHAkxziJtbcYMDslXJYSBsUmmV7P0DlwPx-LSEoBz8d_zsE2aNJLxOBGBuSBjXgxYr_I9zfVpB8CTzfEENJsNsYBbgK9D0hJg6LXJ127sk0gwzJM6D0AX8GO5RuhMHx1RMZ3aZHwFPf-d96h7TieyPKKtPtNNzpxg8mKOOKR6LmCTA33E3H4dLan3YDiHGTuG-_yaXIf0xLGcy59_m7c177l-fP5otUevrOsIBXYk2tr7RCBztii_PBMHSuy-fG6OdWKPQXoRjGP4tUsgABW3w99cQq1BkTyB0mv0gzLYVAJ_M2m3Li-H80IrubtV53McTR-nSthAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=XIIG4IhyWLJgxHAkxziJtbcYMDslXJYSBsUmmV7P0DlwPx-LSEoBz8d_zsE2aNJLxOBGBuSBjXgxYr_I9zfVpB8CTzfEENJsNsYBbgK9D0hJg6LXJ127sk0gwzJM6D0AX8GO5RuhMHx1RMZ3aZHwFPf-d96h7TieyPKKtPtNNzpxg8mKOOKR6LmCTA33E3H4dLan3YDiHGTuG-_yaXIf0xLGcy59_m7c177l-fP5otUevrOsIBXYk2tr7RCBztii_PBMHSuy-fG6OdWKPQXoRjGP4tUsgABW3w99cQq1BkTyB0mv0gzLYVAJ_M2m3Li-H80IrubtV53McTR-nSthAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/24253" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: ایران خودش را در یک بن‌بست قرار داده است با بستن تنگه هرمز، و ما بزرگترین محاصره‌ای را در تاریخ نظامی بر ضد آن اعمال کرده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/24252" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: ایران متحمل خسارت می‌شود، زیرا به پول دسترسی ندارد و منبع درآمدش از تنگه هرمز تامین می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/24251" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: حجم عظیمی از نفت از طریق تنگه هرمز عبور می‌کند و شب گذشته 29 کشتی از آن عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/24250" target="_blank">📅 17:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: ایران خواهان یک توافق است و من هم به توافق‌ها علاقه‌مندم، اما این پیشنهاد قابل قبول نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/24249" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: ما به یک پیروزی بزرگ دست خواهیم یافت و کنترل کامل را بر تنگه هرمز به دست می‌گیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/24248" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: من توافقی را که ایران از طریق آن خواسته است تجارت را فوراً از سر بگیرد، رد می‌کنم، زیرا این کشور متحمل خسارات زیادی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/24247" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند امیدوار است موضوع به این مرحله نرسد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/24246" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV04QAXATGNU7pQqA4M2J3wNCYuLpxMZbkkL6ENQrGb_Kc7IERBlC8umA8sRUqhSH-LwirMhyMcalN6IsH5jHGtXzgrb964gCpOYFqgD2O_LuYNBhMbYhwnTNjbKO3DVrX5WLLp7wAHBUqJdr9FkSnnamIafQDmWZBUKYuWIo0rozhDq28P9KW2bM0Wr1zJnMMSKCcmzzOx5TtL9SjYDkPlg8XLhjgxue_OzrgLuLzddGYh3zNwVAKi6G6csaOS-BVy3mmtQCJ457tzdMSU3kvN5WBKjEFQsJIZW5vG1ulV3MyxuxQB7LofufWKmuBiFuWO4XKCpIXCU3WH-aiSCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در ۲۲ و ۲۳ سپتامبر، هواپیماهای C-130H3 هرکولس از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/24245" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراق: خروج ائتلاف بین‌المللی (مبارزه با داعش) به رهبری آمریکا از این کشور در آستانه تکمیل است.
رئیس سلول رسانه‌ای امنیتی عراق اعلام کرد ائتلاف تمام پایگاه‌ها و مقرهای خود در مناطق فدرال عراق
(از جمله پایگاه عین‌الاسد)
را تخلیه و به مقامات عراقی تحویل داده و خروج نیروهای باقی‌مانده از
اقلیم کردستان و پایگاه اربیل
نیز در حال انجام است. مهلت نهایی پایان مأموریت ائتلاف در عراق
برابر با ۸ مهر ۱۴۰۵
تعیین شده است. این به معنای قطع همکاری آمریکا و عراق نیست و پس از آن، روابط امنیتی دو کشور در قالب
همکاری دوجانبه
ادامه خواهد داشت.
@WarRolm</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/24244" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تایمز آو اسرائیل:
ائتلاف سعودی اعلام کرد دو پهپاد حوثی‌ها را که به سمت ریاض شلیک شده بودند رهگیری کرده است؛ این حمله در پی افزایش حملات حوثی‌ها و همزمان با مذاکرات امنیتی عربستان، ترکیه و پاکستان رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24243" target="_blank">📅 15:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUbwPBqlmvff5H1udGSyUb_LOXZs7hHPcbov3r0nKulOcAlMxw2qrmwczKmhr4l8yDBtxXLFwn98djwI001QxAiZWeu666KZlE89ifw5l0KQZlF94fXKfKsTAZEnldUDq3xs2ZadVd5jRbB5oGfCfTptkLXvAs2oxuECetUudTtaKW5jE1yg2LGwAHioirW8SxzCSBjStzmaXe9irQk9-SFLo93jiTwNjb0bKCBPPEuRdiR2UkG5q8_d5fNe-GNFrOQzDy5UeXUOgQ8wUHbzLJDOQGu8G0cBtaLL2H6304hPPRPndGloUUhnFWFjlmcMWE530vHFCiLLhOkFyYUJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ در
واکنش
ی
تمسخرآمیز
به رژیم ایران تصویری از نقشه تنگه هرمز در شبکه اجتماعی خود منتشر کرده که روی آن نام
«تنگه ترامپ»
درج شده است؛ این اقدام پس از پیشنهاد ایران برای بازگشایی تنگه ظرف هفت روز انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/24242" target="_blank">📅 15:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیروی هوایی عربستان سعودی در حملاتی در شهرستان حیفان، جنوب استان تعز، پروژه تصفیه آب منطقه الأکبوش و شبکه ارتباطات این منطقه را هدف قرار داد.
این حملات در منطقه
الأکبوش ـ الأحکوم
انجام شده؛ منطقه‌ای که طی روزهای اخیر شاهد درگیری‌های شدید میان نیروهای یمنی و حوثی‌ها بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24241" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پزشکیان در مصاحبه با سی‌بی‌اس: ما چند زندانی آمریکایی را آزاد کردیم، اما آمریکا به تعهد خود عمل نکرد.
پزشکیان گفت: «ما کاری را که آمریکا از ما خواسته بود انجام دادیم و چند نفر از زندانیانی را که درخواست کرده بودند آزاد کردیم. قرار بود پول‌های ما آزاد شود؛ این پول از کره جنوبی آمده بود و قطر قرار بود آن را به ما منتقل کند. ما به تعهد خود عمل کردیم، اما آمریکا به تعهدش عمل نکرد.» پزشکیان افزود: «آمریکا چیزی را که می‌خواهد می‌گیرد و بعد به تعهداتش عمل نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24240" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بلومبرگ: پایگاه نظامی دائمی آمریکا در لهستان، موسوم به «فورت ترامپ»، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
رئیس‌جمهور لهستان، کارول ناوروتسکی، گفته امیدوار است این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل و افتتاح شود. مذاکرات درباره
مسائل مالی و اداری و انتخاب محل و زیرساخت پایگاه
همچنان ادامه دارد. بر اساس گزارش بلومبرگ، این پایگاه می‌تواند محل استقرار حدود
۵ هزار نیروی آمریکایی
باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24239" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24238" target="_blank">📅 14:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرمول کلاهبرداران
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/24237" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یاشار جان درود اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/24236" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMojtaba Bahrami</strong></div>
<div class="tg-text">یاشار جان درود
اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24235" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗔𝗝𝗔𝗗™</strong></div>
<div class="tg-text">حاجی پس ما برقمون قطو وصل میشه بخاطر این لاشیا بود
🤣</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24234" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">IRAN: NO PLACE FOR AMATEURS
ایران جای آماتورها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/24233" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگر بیماری قلبی دارید زیرزبانی دم دستتان باشد.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/24232" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند.
همچنین واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/24231" target="_blank">📅 13:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24230" target="_blank">📅 13:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان: در حال حاضر قطر و پاکستان پیام‌های ما را به واشنگتن منتقل می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24229" target="_blank">📅 13:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/24228" target="_blank">📅 13:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ee584150.mp4?token=l84J5eEZoI3IC-BkZHvPp3nzQ6pYy8H7gsS0u4ECNu7L7n_EgLUDusnekK03LLEynrK0dQRE3YpBYt_FcIS3GY2jheej3vWjtQsmCH4GwakjjwZKd-Tqc8Xz26d6hOWx1f17hwKTqfhnPtmPqfwFqIjkoRJqr3Csa1avBiH5PGHoWOk4BWWP3Tg2v1D477Zy-_3E1pxtV6so7EvBfH8BIZPDqNfBMSkZ81xtp63Y41XbQTDICZwOUZP6iiy1Hijz9vuws-FWg6DoGXwBzeSurZSh3ZHT6PA5EtOBR-M499FyyfehSrNreuhoW2yZwZ3KMqd_eCjArJ0x9ckwjI6j7i2huBVwsYo1yopdUszgWV0q8YfD4BmJP87pqL5-cuFx7m8BtmRsAK9RZTNFdc9jVxg6rteoF_lQ-fpfJR49eer__17YKfldvWparlCa64mEymkgnHREwSk-60q6VuMXDOgO-F9ZcWze8OyTbAiHNXXVhYSjUb8rjvdq5uLguzRqoqkHj-l5uvioaInG3LvQ6yTKgi4xWgwVBAb7cEZw3pEtVWolzDK45Y40iVBMNBAPUeWRZGHhdO7Ai7eJXrsaDjZ4OoZqB3wGePM28ft_kLKou-ITNoxpn3ceQkg3pB2jVU9dEAvzJVLXk1YhLld04SfNZC1CfVw4bLtztBpNMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ee584150.mp4?token=l84J5eEZoI3IC-BkZHvPp3nzQ6pYy8H7gsS0u4ECNu7L7n_EgLUDusnekK03LLEynrK0dQRE3YpBYt_FcIS3GY2jheej3vWjtQsmCH4GwakjjwZKd-Tqc8Xz26d6hOWx1f17hwKTqfhnPtmPqfwFqIjkoRJqr3Csa1avBiH5PGHoWOk4BWWP3Tg2v1D477Zy-_3E1pxtV6so7EvBfH8BIZPDqNfBMSkZ81xtp63Y41XbQTDICZwOUZP6iiy1Hijz9vuws-FWg6DoGXwBzeSurZSh3ZHT6PA5EtOBR-M499FyyfehSrNreuhoW2yZwZ3KMqd_eCjArJ0x9ckwjI6j7i2huBVwsYo1yopdUszgWV0q8YfD4BmJP87pqL5-cuFx7m8BtmRsAK9RZTNFdc9jVxg6rteoF_lQ-fpfJR49eer__17YKfldvWparlCa64mEymkgnHREwSk-60q6VuMXDOgO-F9ZcWze8OyTbAiHNXXVhYSjUb8rjvdq5uLguzRqoqkHj-l5uvioaInG3LvQ6yTKgi4xWgwVBAb7cEZw3pEtVWolzDK45Y40iVBMNBAPUeWRZGHhdO7Ai7eJXrsaDjZ4OoZqB3wGePM28ft_kLKou-ITNoxpn3ceQkg3pB2jVU9dEAvzJVLXk1YhLld04SfNZC1CfVw4bLtztBpNMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از
فایبرگلاس
استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای آلومینیوم هوافضایی ساخته می‌شود و در بخش‌هایی از آن نیز فولاد، تیتانیوم و مواد پلیمری به‌کار می‌رود. این مخازن از نوع Drop Tank هستند و خلبان می‌تواند در شرایط عملیاتی، پس از مصرف سوخت یا برای کاهش وزن و مقاومت آیرودینامیکی، آنها را عمداً از هواپیما رها کند (Jettison)
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24227" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nxv2dLnzpwlIQU1L9bqGg-t9KVgiLHnKb--Z-26eh5_cr5BAHlKAnVQ002eTnhTil4oqvRz4IsJHwhoJGygT1LQIEnJuI2bOVaywCZydMVIprwS6QrFHk2bR5IeAQbUV56Bs1UtOOQS_MApFSxP8PttsbHWtSS67BiekaYuD9J8eFYhQG-cWofjlkPHfiw8fiE_bpdKjepggOFrOiHnVu3LV5IDjudIxgd9WTzx_5Pob7X1PfewEsMzAz4b3-pOkaLlu0uArys2hIjEagRnRT3H60KdX8mtufruMYeBx05JEeKsRv-FY0MTONilp2kqxGuBEMTT0FhY_OLalwR_S9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nxv2dLnzpwlIQU1L9bqGg-t9KVgiLHnKb--Z-26eh5_cr5BAHlKAnVQ002eTnhTil4oqvRz4IsJHwhoJGygT1LQIEnJuI2bOVaywCZydMVIprwS6QrFHk2bR5IeAQbUV56Bs1UtOOQS_MApFSxP8PttsbHWtSS67BiekaYuD9J8eFYhQG-cWofjlkPHfiw8fiE_bpdKjepggOFrOiHnVu3LV5IDjudIxgd9WTzx_5Pob7X1PfewEsMzAz4b3-pOkaLlu0uArys2hIjEagRnRT3H60KdX8mtufruMYeBx05JEeKsRv-FY0MTONilp2kqxGuBEMTT0FhY_OLalwR_S9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش یک معتاد خمار از لانچر
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/24226" target="_blank">📅 12:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozpa_OxNbHF7Jt86aezQ6OqnpuQEgW4qYIdZJQCwX2X2Xp8fY4-EslE8viqMvWMcqprys1Ce-NxiGaTwUMRZlQ_CTngb9PJVqrQ0APq0sq8FA1W0O-sHfV36-GPqx5MlMr-S7kXO9oUUcZdCybJWSxBp0Jmv6ieDDLTdlrI_eVFK8SztlbmxmLI1jgb-__amEfbkif-c48cGQ-G9Eyr_qHO_FP2Ju8he8qjRYgTXnqoeCUZojYvJ2IVXP3AgaW7bZhw_rxhB8pdAy9Hek3YcVdKcctzXrfN-cng81Uy3b-fRxz-A1FziTTZvNGw-97Okg2R1h4rN2AT36f6EL5-Pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان دو ساعت و نیم پیش نیویورک را ترک کرد و هم اکنون حدودأ در مرکز اقیانوس آتلانتیک شمالی است. بسیار جای مناسبی است تا کوسه‌ها او را بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24225" target="_blank">📅 12:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=sgccC8TSBLu1gVJxUrOMvstN3vkM8v5-oauJJknGTxC6ahagDC2tiBmCmMi3KAFWkS37rARqsHjgzDHkqlzsJZ3qrZMP4_ZFtSWMQ8oNAp3uRAp7Oh_DKcaUCZcgsW7ENV4NZ75vrtNKivamDo7maWayoAfsVOB68850xsJOEwpVkDAfH7hD1JZViT-0sUzJIqHP71bJKEra8JzmToZZi_ZB-j-ajGcN3vK1Ugw5WPOIcc8hCnBQ_2WXDTrKIfFK5yUaEjRsjrq-PVcZoaVBDuY_-DpTaITMqMFHAXmN4r9hj1Rm8z8UCFMd63uWputbCK6qMJkmAMzJ7i8VMB_D5j4ewDiNWmZtMp2i7_Bmyr8261KfwLr217ZFtFeuZaJb_B3qkdBodQumGexBnzoO0-Qr9_iTMgKBz2XNln1nDbzmYHJ5hu5S6t4GqO6hqTxeqfJlVukCUlyrmClVgKGKAYgDcVcyL5PwPg_EVYVqjMahdXhfU48gL4tTOhQp_J6sGIyOrvNSCHxvV5wRCHRvxFk7fciE_tQiDwyn__BnqNGO5JwzbP_3JuF-8dllcmVd7eWpr59kG4z4OduspSG_JG7h1vDgCQHTQ28DcU_eCm6pnxQWm5bSeo8NTWxdclJTklyx-dAlvudsnmgqKuFRS6C6duteZSHETGBdPgACntM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=sgccC8TSBLu1gVJxUrOMvstN3vkM8v5-oauJJknGTxC6ahagDC2tiBmCmMi3KAFWkS37rARqsHjgzDHkqlzsJZ3qrZMP4_ZFtSWMQ8oNAp3uRAp7Oh_DKcaUCZcgsW7ENV4NZ75vrtNKivamDo7maWayoAfsVOB68850xsJOEwpVkDAfH7hD1JZViT-0sUzJIqHP71bJKEra8JzmToZZi_ZB-j-ajGcN3vK1Ugw5WPOIcc8hCnBQ_2WXDTrKIfFK5yUaEjRsjrq-PVcZoaVBDuY_-DpTaITMqMFHAXmN4r9hj1Rm8z8UCFMd63uWputbCK6qMJkmAMzJ7i8VMB_D5j4ewDiNWmZtMp2i7_Bmyr8261KfwLr217ZFtFeuZaJb_B3qkdBodQumGexBnzoO0-Qr9_iTMgKBz2XNln1nDbzmYHJ5hu5S6t4GqO6hqTxeqfJlVukCUlyrmClVgKGKAYgDcVcyL5PwPg_EVYVqjMahdXhfU48gL4tTOhQp_J6sGIyOrvNSCHxvV5wRCHRvxFk7fciE_tQiDwyn__BnqNGO5JwzbP_3JuF-8dllcmVd7eWpr59kG4z4OduspSG_JG7h1vDgCQHTQ28DcU_eCm6pnxQWm5bSeo8NTWxdclJTklyx-dAlvudsnmgqKuFRS6C6duteZSHETGBdPgACntM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در مصاحبه با شبکهCBS: هر بار که تفاهم هم کردیم باز حمله کردند و کشتنمان،  آمریکا به تفاهم عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24224" target="_blank">📅 11:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار : به زودی قیمت سوراخ موش در‌ ایران سر به فلک خواهد کشید …
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24223" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند. @WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/24222" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/24221" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کوین‌دسک ,
رشد برخی آلت‌کوین‌ها
: در گزارش بازار روز جمعه، کوانتوم (QNT) حدود
۳۸
درصد، اوندو (ONDO) حدود
۲۸
درصد و چین‌لینک (LINK) حدود
۱۱
درصد رشد روزانه ثبت کرده بودند. این ارقام قیمت لحظه‌ای امروز نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/24220" target="_blank">📅 11:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روزنامه گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
@WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/24219" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏سیدمحمد مرندی، مشاور پیشین تیم مذاکرات هسته‌ای رژیم جمهوری اسلامی، مدعی شد مذاکرات غیرمستقیم با دولت ترامپ بدون پیشرفت بوده و منطقه به سوی تشدید تنش می‌رود. او همچنین کشورهای حاشیه خلیج فارس را به همراهی با آمریکا در جنگ علیه ایران متهم کرد و اقدامات ترامپ و اسکات بسنت را «توطئه علیه مردم ایران» خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/24218" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز ، عربستان، ترکیه و پاکستان هماهنگی امنیتی را افزایش دادند: مقام‌های دفاعی سه کشور در ریاض درباره وضعیت امنیتی منطقه، تبادل اطلاعات، هماهنگی نظامی و یکپارچه‌سازی نیروها گفت‌وگو کردند. این نشست در چارچوب توافق دفاعی مشترک مکه برگزار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/24217" target="_blank">📅 11:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">«یک مقام ارشد اطلاعاتی اسرائیل، در توصیف میزان ویرانی رفح در سال ۲۰۲۶، گفته است: تقریباً هیچ ساختمانی در رفح باقی نمانده، مگر ساختمان‌هایی که تصمیم گرفته شده بود حفظ شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/24216" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=Dqq6sPL2f6xut42UpVFpuD7nSCn7IbhlVgQyEBcv_T_0xTTmKQY95L2lNJwezU3VbbNc3pOTUOnLvZhiXST76gsBvpYJ2oJkhKUGhmvLQJL5zE_KnNJRMhIAXm3YFIh_b880gP9-0Ay3zRJXktvtDa1fOWa8SrdEO0iXnzooZIjeMMYVAew4b2denEugbL5RCSgAWqqi2N7DDmbGaIdnWISUnlA2qKp2rvexjOOyDlJmdG2zQNRSGRF3om3ct4WxXLTcfaftdOTh7zWsxBoZdHeeEZZJf69VhgfR9MsE9zgVqrlTxLg2DNGfDhQNcSEc25xbyitY3OTD33CB9N6dorCq7-NkiOKh-tazaKb5kwPJaB39COAFMAWheK97BU7LGB7j9u_YLunG0GfMVKAKBcw0AhA7QwdebGEwMq4bvseU3tdWCkmzcdvjaoyGmbZ9BxzxBBFqC0Hu-_m5l09Teu4wnzxej9fML1WcNeBfGfMMluD6shRu0ITNqKKFCT4u9XkbrCDRfrX2nrM-KhnsgtQbCaHgYRxp-VNi08b9JQ2KSpBUl5M2bXYc934s13VJjqgG7qcZoKctxTbZGqAdauOsewzDpn2oFMa_kW7eyJmhspP23CuQxpTBn83Z1T8wsHErySnDBPAyXo1X-1TbnmzlT1zX5l0tTdQzDnyPheY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=Dqq6sPL2f6xut42UpVFpuD7nSCn7IbhlVgQyEBcv_T_0xTTmKQY95L2lNJwezU3VbbNc3pOTUOnLvZhiXST76gsBvpYJ2oJkhKUGhmvLQJL5zE_KnNJRMhIAXm3YFIh_b880gP9-0Ay3zRJXktvtDa1fOWa8SrdEO0iXnzooZIjeMMYVAew4b2denEugbL5RCSgAWqqi2N7DDmbGaIdnWISUnlA2qKp2rvexjOOyDlJmdG2zQNRSGRF3om3ct4WxXLTcfaftdOTh7zWsxBoZdHeeEZZJf69VhgfR9MsE9zgVqrlTxLg2DNGfDhQNcSEc25xbyitY3OTD33CB9N6dorCq7-NkiOKh-tazaKb5kwPJaB39COAFMAWheK97BU7LGB7j9u_YLunG0GfMVKAKBcw0AhA7QwdebGEwMq4bvseU3tdWCkmzcdvjaoyGmbZ9BxzxBBFqC0Hu-_m5l09Teu4wnzxej9fML1WcNeBfGfMMluD6shRu0ITNqKKFCT4u9XkbrCDRfrX2nrM-KhnsgtQbCaHgYRxp-VNi08b9JQ2KSpBUl5M2bXYc934s13VJjqgG7qcZoKctxTbZGqAdauOsewzDpn2oFMa_kW7eyJmhspP23CuQxpTBn83Z1T8wsHErySnDBPAyXo1X-1TbnmzlT1zX5l0tTdQzDnyPheY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در شبکه CBS: اسرائیل هر کسی رو که دلش بخواد با تواناییی که داره ترور می‌کنه، با پشتیبانی آمریکا. رهبر ما مگه تروریست بود که کشتنش. خیلی راحت میان ترور می‌کنن و بعد به دنیا می‌گویند ما با تروریست‌ها می‌جنگیم.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/24215" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضجه های حقیرانه پزشکیان در شبکه سی‌بی‌اس: آنها دنبال این هستند جامون رو پیدا کنند و هر وقت دلشون خواست بکشنمون ما گفتگو می‌کردیم که آنها ترورها را آغاز کرده‌اند. هیچ ضمانتی وجود ندارد که دوباره آمریکا و اسرائیل دست از ترورها بردارند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/24214" target="_blank">📅 11:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873be0f119.mp4?token=DWig07a_gR-lnSx4EnexJ1TnFOBY_uCIhGzpF2Lr52lCjUhUqAt9r4I3Z-WMBbaL_e6GwrNCOHsm3nI1s16C3cTCcTPXOHvxKnAThRyxx-fwhiZTPm69QCgoy-HTCrgXyLAxagQ4efqhScp6pnzy3a-qJrxpXOjke5cxszOkob8uG7kjyu4GwsJDAKFnWrvla-ZXlHYQcWUGO-ESSTrwKrSntw1_HkYl3oOwGYGCzvlpBR_i6z4FHKVE-Nc1xgDGr30MOWKhxDzUXi5stFrrZ8N1Dnlt8sJCknEcojyjMv72W6U2Olo83S2lcLdGeBAgcx94BvfVDP3HtT2IL7C-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873be0f119.mp4?token=DWig07a_gR-lnSx4EnexJ1TnFOBY_uCIhGzpF2Lr52lCjUhUqAt9r4I3Z-WMBbaL_e6GwrNCOHsm3nI1s16C3cTCcTPXOHvxKnAThRyxx-fwhiZTPm69QCgoy-HTCrgXyLAxagQ4efqhScp6pnzy3a-qJrxpXOjke5cxszOkob8uG7kjyu4GwsJDAKFnWrvla-ZXlHYQcWUGO-ESSTrwKrSntw1_HkYl3oOwGYGCzvlpBR_i6z4FHKVE-Nc1xgDGr30MOWKhxDzUXi5stFrrZ8N1Dnlt8sJCknEcojyjMv72W6U2Olo83S2lcLdGeBAgcx94BvfVDP3HtT2IL7C-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس: «اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران هم به آن پایبند خواهند بود؟»
مسعود پزشکیان: «طبیعتا هر تعهدی که بپذیریم، پایبند خواهیم بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24213" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24212" target="_blank">📅 10:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید امیدبخش ترامپ در تروث شامل صحنه‌ای از منهدم کردن لانچر رژیم جمهوری اسلامی
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24211" target="_blank">📅 05:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود ۲۰۰ جنگنده در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود ۵۰۰ هدف را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از ۱۰۰۰ هدف را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24208" target="_blank">📅 05:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود
۲۰۰ جنگنده
در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود
۵۰۰ هدف
را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از
۱۰۰۰ هدف
را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا ۲۳ مارس بیش از
۱۰ هزار پرواز رزمی
و بیش از
۱۰ هزار هدف
در عملیات ثبت شده بود. گزارش سپتامبر Air & Space Forces Magazine می‌گوید Epic Fury در مجموع به
بیش از ۱۳ هزار هدف
حمله کرد و حدود
۱۰ هزار سورتی رزمی
در ۳۸ روز اوج عملیات انجام شد. همان منبع آن را
بزرگ‌ترین کارزار هوایی آمریکا در یک نسل
توصیف می‌کند. خود CENTCOM در ابتدای عملیات آن را
بزرگ‌ترین تمرکز منطقه‌ای قدرت آتش آمریکا در یک نسل
نامید.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24207" target="_blank">📅 04:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۱۵ روز قبل از شروع جنگ ۴۰ روزه ۰۲/۱۳/۲۰۲۶</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24206" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24205" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24203" target="_blank">📅 04:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24202" target="_blank">📅 04:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24201">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏هم اکنون مایک والتز ⁦سفیر آمریکا در سازمان ملل : رژیم تروریست جمهوری اسلامی باید از بین برود
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24201" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/24200" target="_blank">📅 04:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">واشنگتن‌پست: پنتاگون ۳۷ نظامی مجروح دیگر را به آمار جنگ ایران اضافه کرد؛ مجموع به ۸۶۱ نفر رسید.
پنتاگون این هفته بدون توضیح عمومی، ۲۹ ملوان نیروی دریایی و ۸ تفنگدار دریایی را به آمار مجروحان اضافه کرده است. زمان و نحوه مجروح‌شدن این افراد اعلام نشده و یک مقام نیروی دریایی گفته ملوانان به خدمت بازگشته‌اند. مقام‌های دفاعی پیش‌تر گفته بودند ثبت آمار تلفات ممکن است با تأخیر انجام شود، از جمله در موارد ضربه مغزی و آسیب‌های مغزی که علائم آن‌ها دیرتر بروز می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24199" target="_blank">📅 04:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24198" target="_blank">📅 04:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/24197" target="_blank">📅 04:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24196" target="_blank">📅 04:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ito294G3WSX7JfRTP0rCvxehdkwqXBt0bZBHOd1wZSTFlZ1IFqq5IHCsPFY3q6rBIRVIiNTiLuJG2ntiCRk5mFRUeLhtjjFL5K8Z97uU_GsqufhMYL3EDlNcaH4WFtoeT-zmBDiLiOsBT0qpWfJlf-zH3kDWKHK0CpyqEAu2eKtAq3bZT7TStQpvuuf-jffZUlrsXSzAvT5I42d1q0wi2oI_CoUbX4-lGYlPBfD5F_asIS625cHLMMmPrIGduwP2DrpQUGudJroKjf3Lk8b2CLBIrwELE1ajeC-gZmZE4yWraWLxQLMhfzH8cnT3U0DGs8KA_1g7hegbLup95qkNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24195" target="_blank">📅 04:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24194" target="_blank">📅 03:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/24193" target="_blank">📅 03:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/24192" target="_blank">📅 03:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/24191" target="_blank">📅 03:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=Es3gXuvRA8p4mbGlE_XWnS_akrC4szfPN7AivRzti5omiipJmFf8deVV6DRtRHd9Wc4499N2iWivlBL5tOHGHN5aCNg_0x8gizP3EdQY2GRnv7Errn_u8I51_-8SjAgLaojLGgJY298Xd6g5Kq4o6Nzi0Zf2XyoYwjkOpnXhXegVWbkrAqTciwJeTZDLL2qqYs2N1BTCV8qmMRPpv_5ef9tW3g5n-srgrZvRE3_vMiq4SAqIvebRUozCoj1Uu2Yr8_qkKyizwYiY6sOAV4EK0U3wEO6Jl52XwFM07JlyMYqG5WVZ1r37Ffr8qtne6OVvQ-cIZgTyj3zH5tEPzzEKqx7Uv5aaZGH8UNbiaBUGNkad_w27gfZlt7T8C0LibnSdftzdAegcdjZcaVKa64_WC6U1kAQv8jtxvLzFxrQj_EieMHk2twd_KTgsy_63IJXIoTzKurUuky2pBSvBu3rK50NliqACp1iTwG0pTp8lQN78IOh-mlsO2xlI-LvvwRQdk5Eh400GarDlA0Bzq8aN_yLvE9g7h9ryxSPnzCZvgHdJtU3XAfLy2zLAlK7YWjAyUHyRFwO-kGfDyCCZHGQc-86yL9bj-9DHgBsJlIPz-WbslkmLkU6tp5zGcTqrWn8P3AVaWBm2VeXxRn7rr6MxVnNrqJVZX5wcwVD6UX8x-s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=Es3gXuvRA8p4mbGlE_XWnS_akrC4szfPN7AivRzti5omiipJmFf8deVV6DRtRHd9Wc4499N2iWivlBL5tOHGHN5aCNg_0x8gizP3EdQY2GRnv7Errn_u8I51_-8SjAgLaojLGgJY298Xd6g5Kq4o6Nzi0Zf2XyoYwjkOpnXhXegVWbkrAqTciwJeTZDLL2qqYs2N1BTCV8qmMRPpv_5ef9tW3g5n-srgrZvRE3_vMiq4SAqIvebRUozCoj1Uu2Yr8_qkKyizwYiY6sOAV4EK0U3wEO6Jl52XwFM07JlyMYqG5WVZ1r37Ffr8qtne6OVvQ-cIZgTyj3zH5tEPzzEKqx7Uv5aaZGH8UNbiaBUGNkad_w27gfZlt7T8C0LibnSdftzdAegcdjZcaVKa64_WC6U1kAQv8jtxvLzFxrQj_EieMHk2twd_KTgsy_63IJXIoTzKurUuky2pBSvBu3rK50NliqACp1iTwG0pTp8lQN78IOh-mlsO2xlI-LvvwRQdk5Eh400GarDlA0Bzq8aN_yLvE9g7h9ryxSPnzCZvgHdJtU3XAfLy2zLAlK7YWjAyUHyRFwO-kGfDyCCZHGQc-86yL9bj-9DHgBsJlIPz-WbslkmLkU6tp5zGcTqrWn8P3AVaWBm2VeXxRn7rr6MxVnNrqJVZX5wcwVD6UX8x-s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از مهمانان ضیافت شام دفتر نمایندگی مفت خورهای جمهوری اسلامی در نیویورک تحت عنوان «دیدار با ایرانیان فرهیخته و مقیم ایالات متحده آمریکا»
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/24190" target="_blank">📅 03:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4E9zJ-mGP-dMe9119UkCViPBFWRjHjV-cSVa__JSh2qCl_eizfhS9HmTByYXLElv_BNrGAzbZPhTLed-1Kv1tNX9lP4A5TMBntUUrlu9hlpka3-oLVWEw0k8u5Xy1leMy6Dk3gGav9W1vcdLbY-iDJ2Pc-3EF1pYIpk7FbznvRQxDQ48WcJlWyoh19DvHQjB0XaxnznC7awxFT52Rgw_YtvusLSuLAEGoFH9nuR_j-85cIRX6yr3_fYlRP5w-2-tgvVgcsXnWNyG3lWahZt-Ymvb0a8kfZMP6jZmLbBsUPOgWc26hovSd9dWk_YM6qOROfB8BadluD9vKkWaG1QZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ریخت و وارد کانال ۹۷$ شد
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/24189" target="_blank">📅 03:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/24188" target="_blank">📅 03:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24187" target="_blank">📅 03:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/24186" target="_blank">📅 03:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش صدای انفجار شدید از‌ تنگه ، پیغام های زیاد از بندر و قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/24185" target="_blank">📅 02:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24184">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش انفجار شدید / شاید شایذ پرتاب از مرکز شهر تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24184" target="_blank">📅 02:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من قدم ۱۹۱ هست
😂
عکس‌ ها رو هم عزیزان دلم درست میکنند
😼</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24183" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24182">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🩵</strong></div>
<div class="tg-text">با قد ۱۶۰سانت واسمون کماندو شدی</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24182" target="_blank">📅 02:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کمیسیون بورس و اوراق بهادار آمریکا (SEC) توضیحات جدیدی درباره قوانین کریپتو منتشر کرد!
طبق این توضیحات، بازخرید توکن توسط یک پروژه لزوماً باعث نمی‌شود آن توکن اوراق بهادار محسوب شود. همچنین توکن‌هایی که کاربران در ازای استیک کردن دارایی‌هایشان دریافت می‌کنند نیز در برخی شرایط اوراق بهادار محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24181" target="_blank">📅 01:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی هم اکنون : سیا توبه توبه سیا نرمه نرمه
البته CIA
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24180" target="_blank">📅 01:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyR84j3OEtGqwgDu1z7V61J_96AnnY8w-Vnhmk-ba-60TyILsp7g4fRABiIVbmziyr1nGah0qh_2v_Gj81cV6g4zh0nX1appINSKlIPBnovrkblUFRo8KNtCYrBLTNfOSfpTlmUSnxM9wZACV6II6Zxuy327SCB1H6qu3cF7JgNERBn-izAe1ht-5xobjnj89fV2EQr4JZCGEhseuQ4FKJvfd4SjjawTJaL3oB_t0x0mVU8F4hYS7vL6v6omQo5_CLWpGOspOTxvTGalwWa-MR8GvanfkaFxVGnh8Q1IAm4Y6hbUAK8fXYzQSMz6R_IjWjayzN9MKZdfMQMPTt5fLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوخترسان جدید الان از قطر بلند شدن در‌ مجموع ۵ سوخترسان همگی ‌از قطر و ۱ پی ۸ از بحرین از که از ۸ ساعت پیش در حال انجام ماموریت بر فراز خلیج فارس و تنگه هرمز هستند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24179" target="_blank">📅 01:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خانعلی‌زاده : دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24178" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromادمین</strong></div>
<div class="tg-text">یاشار. داداش من الان رسیدم پیام هات رو دارم یکی یکی نگاه میکنم من و خانومم خیلی وقته اینتر آشغال رو نگاه نمی‌کنیم کلا پاک کردیم خیلی روحیه مون خوب شده من که فقط کانال تو رو دنبال میکنم ،دهنت سرویس چقدر تو کانالت خندیدم،بزار اعتراف کنم اولین کانالی هستی هم اطلاع رسانی هم تربیت هم فرهنگ سازی هم مبارزه طلبی و هم خنده و روحیه خوب داری به مردم یاد میدی در کل عشقی داداش</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24177" target="_blank">📅 01:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVW6NwqeE2apn7E89JWi_xFbYfEC-DjRFPPgemP5HUQiTiSYriJ6qh6oDLWuz3zX1DMHA-pb5bgXpkGbA1Cd1nvwDElBE1N76UwmkNdDGkrGIAfMrg-esAUwn9grY0Uu3qLcKdjQYSRbwC_SbJFMRtnZTE2aFV01ifh5YxsWYB15X4SFLcZzynluYLMbW0_i5RIfE-m5yF0mjSgqbSP7jNxitosSqSoU6xvTrdPksMSbQ91e7LIgwGo-_7I23XCFOEXyILZPyq5fGJC-k7SqykZadKdM5UTf4OUrIu4IZgLzDnnIuV6JSzOwHZUOxIZBrxYZ8Ml1to2kgFQJXJDP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : ایران آزاد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24176" target="_blank">📅 01:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی: ما از طریق قطر، این پیام را به آمریکا را منتقل کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24175" target="_blank">📅 00:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امشب دیرتر‌ میرم بالا منبر</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24174" target="_blank">📅 00:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صدای ریکشنا نمیادااا اهااااا بیا وسطط</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24173" target="_blank">📅 00:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پرتاب ۴ موشک از سیریک با صدای کشته شده های حکومتی‌که راننده مست زد پرتشون کرد اونور بلوار
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24172" target="_blank">📅 00:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24171" target="_blank">📅 00:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل گفت اسرائیل هم خواهان تغییر حکومت در ایران است و هم به تحقق آن امید دارد. او افزود این موضوع هدف رسمی عملیات نظامی اسرائیل نیست، اما به گفته او، تحقق چنین تغییری به سود مردم ایران و کل منطقه خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24170" target="_blank">📅 00:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراقچی در نشست خبری نیویورک:
اگر شرایط فراهم بشه و فضا از فشار و تهدید دور باشه، تنگه هرمز ظرف ۷ روز باز می‌شه و امنیت کشتیرانی هم تضمین خواهد شد.
این مهلت ۷ روزه از زمانی شروع می‌شه که آمریکا طرح پیشنهادی جمهوری اسلامی رو بپذیره؛ الان توپ در زمین آمریکاست.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24169" target="_blank">📅 00:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سنتکام: رزمایش «شیر آماده ۲۰۲۶» در آمریکا به پایان رسید.
این رزمایش دو هفته‌ای روز ۲۴ سپتامبر در پایگاه فورت کارسون ایالت کلرادو به پایان رسید و بیش از
۲۰۰ نیروی نظامی آمریکایی و اردنی
در آن شرکت داشتند. این نخستین‌بار بود که رزمایش «شیر آماده» در خاک آمریکا برگزار می‌شد و آموزش‌ها بر
عملیات ستاد فرماندهی مشترک، دفاع سایبری، واکنش به بلایای طبیعی و افزایش هماهنگی عملیاتی
میان نیروهای دو کشور متمرکز بود. این رزمایش دوازدهمین دوره «شیر آماده» و بخشی از همکاری دفاعی بیش از
۲۲ ساله آمریکا و اردن
محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24168" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سلامتی همگی
😂</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24167" target="_blank">📅 23:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مستند «پیجینگ حزب‌الله» درباره پشت‌پرده عملیات انفجار پیجرها و بی‌سیم‌های حزب‌الله در سپتامبر ۲۰۲۴ ساخته شده است. در این مستند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیوید بارنیا، رئیس پیشین موساد، دیوید پترائوس، رئیس پیشین سازمان سیا
و چند مقام و چهره اطلاعاتی اسرائیلی و آمریکایی حضور دارند. این مستند به کارگردانی جاستین فولک ساخته شده و قرار است
۳۰ اکتبر ۲۰۲۶، برابر با ۸ آبان ۱۴۰۵
در آمریکا اکران شود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24166" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE70qlXXShjY3saTXU7uitjMlMhqDAmSNonrgd5YIGKgUhvKT7KiAPjs7gqCmX_FdkdWvY4pwzDOMxJDsiDeJ4WDMX698l_HIMQOzqJmxAmjB24HQsn9j8fAfnIhxrtNsRN0D-Jk5nFQQVaD6J8_FQ6wjQT7f1CAvQs4pV5NKJlbGfKVlFr59ca0QYwBmQJkhcMCeNnGgkjCMNBh9opwsQnerWJkVssPSU8eiESXZV5QbJYrbiXs3mhADbmLgSmilKGieb9vOPHjDelcdBL4gH4aVMrKfxiIRLOP0kaKBAVQnxedTW4u9X2ztjg02O60V5JY7eLbIQqsH56sBSu6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت برنان
(مجری و خبرنگار سیاسی شبکه CBS آمریکا)
: رئیس‌جمهور ایران، مسعود پزشکیان، در گفت‌وگویی با ما درباره وضعیت
دیپلماسی با آمریکا برای بازگشایی تنگه هرمز، برنامه هسته‌ای، رهبر جمهوری اسلامی و جنگ
صحبت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24165" target="_blank">📅 22:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShDS_opbBUaqJq-LdsuLAfP7xOXwB2kIDLaRJTpkahv7-ak7MWQJSuJaN1m77DW8ubKr1bKpH5IGVtYD0T-8ipgmwoYqus6yfHFS2lQ2biib_YFeOIV3an9JCA5N4R1frBdmlM6pG6VxMLL_BUhIsC_XDdAdU_FDq5YlOxREXDdcq_9Mm6m5F9CoAAEK2SZEKliKiVhUykTt6cdDdEfYo5psgq92HklIR8q3v7H9NlKD6lfP-J1MHRsVzy448gtkatPhQEw7s727mDxyrpoGEs-Om13vgaWzwOmTHQ4aZ4jrwdbZgsSFkKmVToBDYKalutAedNGXCdZeBkUx-soWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: هنگام آغاز سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل، چند هیئت دیپلماتیک در اعتراض سالن را ترک کردند. بر اساس تصاویر و گزارش‌های منتشرشده، صندلی‌های هیئت‌های عربستان سعودی، ایران، سودان، تونس، ازبکستان، سریلانکا، بنگلادش، الجزایر، مالزی، مونته‌نگرو،…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24164" target="_blank">📅 21:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoeAwppe3aDECG7yWnCucbzHdF2sSdW8NFKBXmSd5AeWxgYXHYTQtcZ7_ZShLm-8wvvjnnSZrWKRzfkHbAIrrbu48t6SjdjUXVfjmbeiX4YeMscbjLoDQL0w9zGVzapqrtt1yDfBC58P-TEhzAAx8u5M0CTCER2a-5T0ubzg-rt-3UrEpSLjoTqKFEiiD6Y8vqSEvaQ1A_D7XfJrtStHqZ-3PcwrENC-Id9-pf1cWP1qU12Lg4yT31wi_3lzmdM3zDmsz2IuZKzYBAINwNrtAnBpSD4uUGNVyd0uk4gncVKh6SHRcQZG4z0xaAdO6S3v3XbpsWvNheJbfDrerLT4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای سوخت‌رسان بریتانیا وارد جنگ علیه یمن شده‌اند؛ به‌طوری‌که برای نخستین بار از زمان آغاز جنگ عربستان و یمن، یکی از این هواپیماها بر فراز خاک عربستان سعودی و در نزدیکی مرز یمن دیده شده است.
این هواپیمای سوخت‌رسان بریتانیا از نوع Voyager KC.2 با شماره ZZ333، صبح امروز از پایگاه آکروتیری در قبرس برخاسته
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24163" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مشاور ارشد محسن رضایی : تاکنون
هیچ پیشرفتی
در مذاکرات میان ایران و آمریکا حاصل نشده است،آمریکا با شرایط ایران برای بازگشایی تنگه هرمز
مخالفت
کرده است،در صورتی که دولت ترامپ محاصره دریایی علیه ایران را لغو نکند و تحریم های نفتی علیه ایران را کاهش ندهد،پنجره نیمه باز دیپلماسی به زودی بسته خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24162" target="_blank">📅 21:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در تروث : رئیس‌جمهور شی و خانم پنگ به‌تازگی واشنگتن را به مقصد چین ترک کردند. این دیدار، نشستی سرشار از دوستی، اقتدار و موفقیت برای هر دو کشور چین و ایالات متحده بود. ما بار دیگر در ماه نوامبر در چین و سپس در ماه دسامبر در اجلاس گروه ۲۰ (G20) در میامیِ فلوریدا با یکدیگر دیدار خواهیم کرد. دستاوردهای بسیاری حاصل شده و خواهد شد. مشتاقانه منتظر دیدار بعدی‌مان هستم!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24161" target="_blank">📅 20:48 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/TFs_PvKVOICHK2FN1Dm7zloTe-sSCAAnirBHEfXmxDofv43Jgwftj6os2WKU3jRltSAq2YO97A965EXvS3XNl9G5CgHAivyZWS2kDSPIj8BCWwe-mqQAksy3Es_XMHFFSlWoNh9dy-Khjvhbmhlv1Rjg4lg0Wof-eRAq61ySKNSY7Cn_kYfS9FFOIKS5eGKidmTWiQswMf5SQVi7qseTdJWwfzp8jdUwvbN2A4XVCMDYbExc4LoDoDMLgxzQ4l-tKeAuOEKrsocYCxNc2gZFGD4hSgtWOnVONXnRj_KTVZChMSjtf3giUqNyoMdTkUIKHrY0ghDvfsvD0ehJexKExA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 11:06:32</div>
<hr>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یاشار : امروز سنای آمریکا قرار است ساعت
۱۰:۳۰ صبح به وقت شرق آمریکا
، برابر با
۱۸:۳۰ به وقت تهران
، درباره لایحه
CLARITY Act
رأی‌گیری کند. این لایحه با هدف ایجاد چارچوب قانونی شفاف برای بازار ارزهای دیجیتال تدوین شده و از مهم‌ترین قوانین تاریخ صنعت کریپتو به شمار می‌رود. در صورت تصویب، بسیاری از تحلیلگران انتظار دارند بیت‌کوین در کوتاه‌مدت بین
۳ تا ۸ درصد
رشد کند و آلت‌کوین‌ها نیز افزایش بیشتری را تجربه کنند. در صورت رد شدن، احتمال اصلاح
۵ تا ۱۰ درصدی
قیمت بیت‌کوین وجود دارد، هرچند شدت واکنش بازار به ادامه مذاکرات بستگی خواهد داشت. با توجه به وضعیت فعلی مذاکرات، احتمال پیشبرد این لایحه حدود
۵۵ تا ۶۵ درصد
و احتمال شکست آن
۳۵ تا ۴۵ درصد
برآورد می‌شود، اما هنوز اختلافات سیاسی بر سر برخی بندهای آن به‌طور کامل برطرف نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZHgsDXZ4gIPvbtgbHAtvwKZuKfuhb52_bZbTGy85dJ7AN-Mwu-hCzaMlUsSPPWo1yLqS21wMN_SSQqeExRSvBKxaU3LTGsuA9GcU5kWq8EpkO-AZMDiX-PT16dYBTJ-CTPqz1Gd2CmBYnH3aEEuFeDIsjbzFJId-Q8QLXuGREneJ6wMqyJ6y-gqVTlLYJRGlXVyUL_omjpB6mI8I03d8a_TXlfZ8v8ms0JPtqWF_1j2b1PcReLXHAwS9u621_GcSWIlrD_r4I5REA9_tRd5SZK0sbtDyrVELvYMURXn6rb0qWNTPEbFt044mA6LsKksNkjlCmlUgf_-FTUS7WC99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9S1anE1ldEHSXAgxxPINMjyGR00uvrWAMaD4boDMdNRwnSVLAPjZLITrWDFliIx2i8_DngI_FUlRf_aDhUVVmoD42joQUxpigL-jH_kDY0_1K_CEhopdtUUeBPrc-xee5Qez6Fm6CpHDYLehPUL82qYQ6tHDmDqHoIJraJaoIvl90MPWz56-HbQ_yG5qi5Kxapo3BTxd0vMyzzUN8_mtBwEOC4VlYx7-9sSv142ImNKF5Q5x5h4qxyRlgv3zqosvEy7OiOt42BsUkE85XLIyq0d9MJmlog4ZB5lZYr67OBWUh1JlDqK-pDwdMDP6l5yOFMCWTLesSiIlvZI9z4L6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت بهای معاملات آتی نفت خام برنت با کاهش، به ۷۹ دلار و 2 سنت در هر بشکه رسید
@WarRoom</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/20557" target="_blank">📅 09:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFMLm-dJloEHsM5Vx0svCoAg16gku4piVSe54-kt2v1WJvKqohdqjqMOQvXL8c-rHIwX3HQW7n0sSDiOP54_MeFUGig4tJcmkMeWXunYfpCmsXRMAPah2_ZcPFNBzdkPmOfgJaVS-jgFpSHz7pImXev6tXaCIEoqTYUj02a2YVQavy6PUbFn4Str8mqvulFMl56pOFUteZL0HmRluBvo2AseFlyIO_e4gbaMsv4KOLbouOufMzYMde0LD7hMaHQcZLYoMSEhir5P8S0xAhSoWcHykU5SW3OkxMnpYAH4BEU6R5BkyIvDqVDpOzN5gLK0yrl8L-fwS6O71NIki2HEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «
افشاگران» این اظهارات خیانت‌آمیز تحت تعقیب هستند. احکام حبس طولانی مدت برایشان
درخواست خواهد شد!
@WarRoom</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/20556" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا : بر اساس این گزارش، فرمانده یک نفتکش در حال عبور از تنگه هرمز اعلام کرده است که در فاصله حدود ۹ مایل دریایی جنوب‌شرقی منطقه کُمزار عمان، صدای دو انفجار را شنیده است. @WarRoom</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/20555" target="_blank">📅 07:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی دی  ونس : من با ترامپ در مورد ایران اختلاف نظر ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/20554" target="_blank">📅 07:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سناتور تام کاتن: «ارتش ما آماده است تا کار را تمام کند».
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/20553" target="_blank">📅 07:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAoPIWhtMq3xGDes_mKdiK_SSCLhJV3sm28Tw6wgUEgewBkB1zPNR7ukRm0h_dK3FaLWpvug3nbjaDxODjcUbXXP35enyxHaIJf__8ND4d8wYkeTelnQoYW9tXS9KBLdD8IBQsBQ8v3d4WjQ3Vy-KbnnVFNzE1gRWf-4sUxaH2Q0sHQjcyv3ZXwJp2jSPnT_Yxi9WQoNK28xR7NA2zbkjBSt-tug9qyawOhhf97pgd-dOoY6Dc5WNyHnurm7NtRe7PgUoLCJ3AsqkJjBepBLeqX0DtRB_M3spkMja2M71xbifgObYQuA8N9dLifZtaQsKTm0Gp9KkVjrczFm0LC1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک @WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/20552" target="_blank">📅 07:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=KUWcKBYKA5WX9Q1cia_7YmoFet6b5ZQWYULHmrUyt1lZEx48vkPSzBnWFJCVyExRah-uAfGP0TaNKs8gar1j50fIRotPfzC9tV44W166a3sfFbxgnHRp80JUnDO7lP_mTfrdAkj0-xbbSfKNI_6Fj68eGJLZywCn54U752rjD75kMfW57ldsH1i4kkJ1DrsHtEKu-yjXa2LxQ2EfRp6BJC4hZByTdXDB-wwrinrX6qjsdAYxacQyjvrWvjrscosIoFVteaUviFRl-5ZbKxqxzRirY8-VjjhSnnUx8fvxHucsxSixkYoTGvtIo_Bqcpk-5gb2b9jY_miSSLp0obr05A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=KUWcKBYKA5WX9Q1cia_7YmoFet6b5ZQWYULHmrUyt1lZEx48vkPSzBnWFJCVyExRah-uAfGP0TaNKs8gar1j50fIRotPfzC9tV44W166a3sfFbxgnHRp80JUnDO7lP_mTfrdAkj0-xbbSfKNI_6Fj68eGJLZywCn54U752rjD75kMfW57ldsH1i4kkJ1DrsHtEKu-yjXa2LxQ2EfRp6BJC4hZByTdXDB-wwrinrX6qjsdAYxacQyjvrWvjrscosIoFVteaUviFRl-5ZbKxqxzRirY8-VjjhSnnUx8fvxHucsxSixkYoTGvtIo_Bqcpk-5gb2b9jY_miSSLp0obr05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران با من تماس گرفت. آنها بزرگترین حمله از زمان جنگ جهانی دوم را نمی‌خواستند.
ما گفتیم: "ترجیح می‌دهم این کار را به این شکل انجام دهم." من به دنبال کشتن مردم و نابودی کامل همه چیز نیستم. و این همان جایی بود که ما به سمت آن می‌رفتیم.
آنها می‌خواستند مذاکره کنند و ما در حال انجام این کار هستیم. و به نظر می‌رسد که این [مذاکره] کاملاً خوب پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/20551" target="_blank">📅 07:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=IVDPK5WJ1dnEIXvgqnjgAYUMO9ProBHvCGjimW4qKRJswmlzQo_KjRmUx6DoFaGLAH73f_kloDoC6oFygz8gZsTYkPnKyySew-c3AVUz404jjTJ9vgctWtC6l7P5YolwaESkqr0j49lC3Ii07a2dA5U6KLf3bNHKZsfStNM3UchnM6UId0B9qHVGIg6pvJHmCkI6WkRxBMOqp71HOrlkJuOl27myI6wVeppE1eMBuz0DQO2_BREQaqCsk5vcVO7xK1yOrnoCJol-dVA-7dLpH4An6nc1OrLewlirDqLmUO45OUMDaA3UJTkex349q0Zbs4i8KqrThx-WlcUYCw_UCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=IVDPK5WJ1dnEIXvgqnjgAYUMO9ProBHvCGjimW4qKRJswmlzQo_KjRmUx6DoFaGLAH73f_kloDoC6oFygz8gZsTYkPnKyySew-c3AVUz404jjTJ9vgctWtC6l7P5YolwaESkqr0j49lC3Ii07a2dA5U6KLf3bNHKZsfStNM3UchnM6UId0B9qHVGIg6pvJHmCkI6WkRxBMOqp71HOrlkJuOl27myI6wVeppE1eMBuz0DQO2_BREQaqCsk5vcVO7xK1yOrnoCJol-dVA-7dLpH4An6nc1OrLewlirDqLmUO45OUMDaA3UJTkex349q0Zbs4i8KqrThx-WlcUYCw_UCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است این بار با مذاکرات متفاوت باشد؛ ممکن است نباشد.
ما آماده حمله بودیم. در زندگی واقعی، آنها می‌دانند چه زمانی آماده حمله هستید و چه زمانی فقط بلوف می‌زنید.
و اگر مجبور باشیم، آماده حمله هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/20550" target="_blank">📅 07:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شبکه i24news درباره تنش‌ها با ایران: "وقتی بازدارندگی آمریکا تضعیف می‌شود، بازدارندگی اسرائیل نیز تضعیف می‌شود."
@WarRoom</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/20549" target="_blank">📅 07:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=WQWddLvOKAYVC3MoP2kqiNj6rDfYohNHGbasmQkoFCBh0rtKQZWRPxQlhDlU9nZDjjnrNh5k5Oiz5hFSO4PMB92_VEHMgtxCvfjCZAF-FfiPHHMD3Ah01cK2RCb37nL3GI_PG3ylwAr1cJLXXWdkeVSGFTR23KWpyz90o_ni5o3-wIlIWVL78bDe3RtiEcWVrCR8rXW8n7crGB0Cha1C0080dj2g1OrJ8jF3fz0J--0swRFlSubhYP1i3AbrB_8wdlmT40NersJGr4ig536hw6qL0wS02AYoee65mGNCNOfMBfT7ComA86pg2Z4xEeP4uhMxh2_IfXpzkHK6q3vM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=WQWddLvOKAYVC3MoP2kqiNj6rDfYohNHGbasmQkoFCBh0rtKQZWRPxQlhDlU9nZDjjnrNh5k5Oiz5hFSO4PMB92_VEHMgtxCvfjCZAF-FfiPHHMD3Ah01cK2RCb37nL3GI_PG3ylwAr1cJLXXWdkeVSGFTR23KWpyz90o_ni5o3-wIlIWVL78bDe3RtiEcWVrCR8rXW8n7crGB0Cha1C0080dj2g1OrJ8jF3fz0J--0swRFlSubhYP1i3AbrB_8wdlmT40NersJGr4ig536hw6qL0wS02AYoee65mGNCNOfMBfT7ComA86pg2Z4xEeP4uhMxh2_IfXpzkHK6q3vM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره عبدال السید :
این آدم از یهودی‌ها متنفره. بعضیا می‌گن این حرف تنده، ولی نه؛ از یهودی‌ها و اسرائیل متنفره
عبدال السید! باورش می‌شه؟ فقط برای من همچین چیزی پیش میاد
عبدال السید ظاهرش محترمه، ولی آدم پر از نفرتیه
@WarRoom</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/20548" target="_blank">📅 07:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/20547" target="_blank">📅 07:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20542" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را 30-40 هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستن
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20541" target="_blank">📅 22:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروهای یمنی اعلام کردند که با استفاده از یک موشک بالستیک، یک تانکر نفتی به نام "دیزی" که متعلق به عربستان سعودی است، را در خلیج عدن مورد هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20540" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو در یک مراسم:
نیازهای سیاسی فوری این لحظه از من می‌خواهند که پیش از پایان این مراسم مهم ترک کنم.
ما در حال حاضر در میانه رویدادهای نظامی و سیاسی مهمی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHpuuumOeRsDXp6srhwZnx9cMFNOnkHVfk1_feXayRGLU584R_Sn3jIQdWjMxG6Dpd9dAKUr9NNVQ0wl9zBM9zS9pucRJzw-9FU76HBB_6-bY-N7ydcyLrdEtLStqKgktAo25RmwSNrZx9msDReL-HmHu27thmLtmmpmD_G6tc9Xf6GQ3CVC-5ZD2Qexv12wam_6-U2_d9ZGveoC1dXbifAhkUOYW8NNO4S0PP4Swd8IK_KTZrr1ZShjOd71epGU3hkjpoR8poPmauopkxDZgDEhjsJ3CmHBqLJwAylhZaAjsdROfQ_S_TYqvYhNECD_fXZ3QOKYkUFq8L52sihmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okenti8icJrjLwkp_ddEXpkWHNbUyWEiQ_N5iR-mHH_l_UtZa2nf7JD4oe4B-t0piiPGKYCrNetCPTz_V_JB0qaMfLziS-q6HzraL6nxTR84txLonkh9b9hOVLOFgFlew6XBXLx8WJP3rdTSpDiZaxdrX9wupGK63A2b4KUWavEIEnaqTSLUpc_vlxe1coZE2WjaRMa7FG7sIrtgrEGFKNK2YfSe-sK4Sdmtj8xPImn2G4engDIQAJY0DZNsMUPkVY-BjDSzMSx_7Udmkd3IQlHXzIBuTHuEwxhRWUp3o_oU0SKkZaNE6Nv6rStmTRY85umtGybJ-lWWtV74hQjqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=K-H1mIfMWe_5zW6DD-Qt4oT8rFSjFmvn4HhvU_CE_TCb3exBMk4GGDQFie1hoBUfFrQdT7j8DeJ2q_CGZicuGUV0zsDPRqPsQIjay90FCwa194Tvwq3fhNymWAfnTHPrpLQ6XFHBS_XIy_p7Azks6cnQMJc4yemm7y4u4tWXxpMaZpJv1c3XPXUrVxqxbgDxqS-NZ-m_ru81KXM4-tgUqPm4DdaGAPf-_hG4IdHn31p2fiJPLlyO529nhsI8SHazOTlzmzn0yq0O2J0LoarNjAxei1VvuurtqeNElc--lNWW5CbpcSSVoPY90oeQPyrY9r3tQGgEN09yOXcb0aInig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=K-H1mIfMWe_5zW6DD-Qt4oT8rFSjFmvn4HhvU_CE_TCb3exBMk4GGDQFie1hoBUfFrQdT7j8DeJ2q_CGZicuGUV0zsDPRqPsQIjay90FCwa194Tvwq3fhNymWAfnTHPrpLQ6XFHBS_XIy_p7Azks6cnQMJc4yemm7y4u4tWXxpMaZpJv1c3XPXUrVxqxbgDxqS-NZ-m_ru81KXM4-tgUqPm4DdaGAPf-_hG4IdHn31p2fiJPLlyO529nhsI8SHazOTlzmzn0yq0O2J0LoarNjAxei1VvuurtqeNElc--lNWW5CbpcSSVoPY90oeQPyrY9r3tQGgEN09yOXcb0aInig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرنگار: اکنون در قبال رژیم جمهوری اسلامی در چه مرحله‌ای قرار داریم؟
‏ ترامپ: «ظرف ۴۸ ساعت آینده خواهیم فهمید.»
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=gQ7nZVHitn8ZAo8uLgLm5qgH06anAV9vxvIzkViar3vqqxBcvYUtDCG7eOfSYEbKHJLFyttcHfYMpCfeNNjjhDhXV2CMH-iQ1ChBUvZMqkF6GJYNJzw1rEPeoiE8vp03dlqzjBjt1CboqjrYFigci4Vw-XzgN3opgQpQZvT9ZDxqvz0xA5ulNhfURWz88Pb4VqcBbwW5dkujRaTKWCUpYG3iCdXXtU0JHx1NMhw2fC6315MUfcaTIES29xkBeyQ3MW3pVkKlWhktBUr8kmi7Vq5xubXdiF84UPjW0gnwJZVO_lNvIjNFKM-vssGHFKsYrr14_HUztrG1hmlZL6X9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=gQ7nZVHitn8ZAo8uLgLm5qgH06anAV9vxvIzkViar3vqqxBcvYUtDCG7eOfSYEbKHJLFyttcHfYMpCfeNNjjhDhXV2CMH-iQ1ChBUvZMqkF6GJYNJzw1rEPeoiE8vp03dlqzjBjt1CboqjrYFigci4Vw-XzgN3opgQpQZvT9ZDxqvz0xA5ulNhfURWz88Pb4VqcBbwW5dkujRaTKWCUpYG3iCdXXtU0JHx1NMhw2fC6315MUfcaTIES29xkBeyQ3MW3pVkKlWhktBUr8kmi7Vq5xubXdiF84UPjW0gnwJZVO_lNvIjNFKM-vssGHFKsYrr14_HUztrG1hmlZL6X9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ما خیلی خیلی محکم میتونیم به ایران ضربه بزنیم ولی خب اینکارو نمیکنیم، صحبتای خوبی باهم کردیم ولی اونا نمیخوان قبول کنن. اونا به ما زنگ زدن و مودبانه گفتن: میتونیم مذاکره کنیم لطفا؟
ما به رسانه‌ها اعلام میکنیم که داریم مذاکره میکنیم ولی ایرانی‌ها میگن که اصلا صحبتی با آمریکا نکردیم. پس داشتیم چکارمیکردیم؟
تنگه هرمز به زودی باز میشه و اگه این اتفاق نیفته اونا ضربه محکمی میخورن چون ضربه‌ی اصلی ما هنوز مونده ولی امیدوارم کار به اونجا نکشه.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=hYdPyuxDhuTQe0Rdygk3ESxo8jPjqJX_Bi8nwvGnhV_nCdzr4-qVPKfuTiuY5rsZJICARbJaig0DtyiyuASmyUjjFNg0ZCg3ag8k9f_4oG3kWI97ekddvckuhUjHGNl0rG7fH4Zeg1UXT9XrTC2JdG9iq_JSxuwmDw-3tZL_DXR3zZMvJAzuoaiMDFI1PQGMx9fUlwQ5Me9wD36sz143RcVgla6loli_r0cSx_rMzMFTYEIY-jCNdFk7Yy_wUc-T8GJd5BpdozNyRxjAO7qc3f1yZhlK-iCAJpOXVdnYBP1URHmN35IYlc9xxtHKGG4H7sphcaexyZtatAceh5THAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=hYdPyuxDhuTQe0Rdygk3ESxo8jPjqJX_Bi8nwvGnhV_nCdzr4-qVPKfuTiuY5rsZJICARbJaig0DtyiyuASmyUjjFNg0ZCg3ag8k9f_4oG3kWI97ekddvckuhUjHGNl0rG7fH4Zeg1UXT9XrTC2JdG9iq_JSxuwmDw-3tZL_DXR3zZMvJAzuoaiMDFI1PQGMx9fUlwQ5Me9wD36sz143RcVgla6loli_r0cSx_rMzMFTYEIY-jCNdFk7Yy_wUc-T8GJd5BpdozNyRxjAO7qc3f1yZhlK-iCAJpOXVdnYBP1URHmN35IYlc9xxtHKGG4H7sphcaexyZtatAceh5THAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou4in2Fh0RynLXUGls6uufw7c-AZ7qlrg6Pu9Rf-Qokxt90dkdOY0MlRjQGkrmEsI0f14fWWSuR65BksziekwSoFwD_BXIb8e5H-IW98BqNl8sXLvhfYz9776TyFV9Z-H3gCBohpBdmlZeHU8O25WOcajoW723uPQTg8mbgJN_r_CnvzDlJEjfQENzMBKVfZu1BkV6ph4hzU8RUgMr1tGmUiWwlM_N2nGqf9M6UFcyfZtxpTYHAUry9z0rcdDojTolBsHELsxkoGMD-HiW4CCv_-UU_l-A4phzSUU0zOmB2Dgq8-8b8F4G-QmrwwCe1TDzT39-M5KEC7HoOFLN3gdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=oq2ab7ARd4OVqrweu1__z2Adxuvuh7Z9nENFkYHhWTAm8OidPUq4BqyAqQXxd26drdTU5OeDGXVdOEHRkWGxYNhPm927TJ4HcuvktLsH9Kbq-lfmU9QbV2YsQDz4IcxDJ7Upw3v-Z978zCs3PnslHdFbB9k3GVf6S1iPHOfQirKu_iFUVjktX6sXowu_AG6eFvZtg9gARNaxF4B0fozgaHZz-IujGLaWUoUnnWAOg2-JK0On1wToIkdOkFoR7BmgPCzh4JEoqD-e2W3Kpl2TRONXUJh5dBhAORmkw4mpZPnNdjRP13FJ5Eyb8_8jYV8PQaV8mQ2ZF845Vxi1gRG6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=oq2ab7ARd4OVqrweu1__z2Adxuvuh7Z9nENFkYHhWTAm8OidPUq4BqyAqQXxd26drdTU5OeDGXVdOEHRkWGxYNhPm927TJ4HcuvktLsH9Kbq-lfmU9QbV2YsQDz4IcxDJ7Upw3v-Z978zCs3PnslHdFbB9k3GVf6S1iPHOfQirKu_iFUVjktX6sXowu_AG6eFvZtg9gARNaxF4B0fozgaHZz-IujGLaWUoUnnWAOg2-JK0On1wToIkdOkFoR7BmgPCzh4JEoqD-e2W3Kpl2TRONXUJh5dBhAORmkw4mpZPnNdjRP13FJ5Eyb8_8jYV8PQaV8mQ2ZF845Vxi1gRG6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWfmUEuImWxolIv8fg1uVuPDmzMtqJHwK8R-hQFxdN_ycakhq79GdY1Rx_Npo5Mb54XhAoaNDJBtBznQIqAogeMOUKPhvNu-uiTW-pbnFSK6f7GfbjTnCSdeuDoR_JHmfHxK3td1udWf11rHcRcc9hSnvH3ZazOlQriPmGD30S00ejVoABmIrPebxhz0ebZCAG07pkMi7Buho-MtF5o8uZKxGd1KTcsEvgbnhyG5_a_cXzHpdeNnHoPChTV_hohB-2uuU3qIsXGLgEPM0hMpzw5-ch8n9BhLJ-_TLfHqyMq9gto3hyFUa0XZMAv9_z6QUH8L1ZT3JrXruXz6nFO__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNQvu3fl_Wvdi56tWk-PIx-upEyOMDhQgrfphmPdhxQSTO_renIvtHDkZv_5hZOC3zer6ZAL7jACG9slyBdWh1iEf_52e2_9wyT8oKzW--AlAk4RJyHshFlL_ta6jP-vm6y7uXFa4qHVmzKkGTC6kDy2skv8STWmUFklPdVmyrlddLq0NSf5Cg6VqeHQQrybGs4L_01yrwKIelg9g6frbsjUfFIpz64O5TsZGhorSeehW85uUiYqQtNwVL_mVauGJuAMMpbUoGKKMMK7nQn_0DU3YLxDFiw0cr2bsB-CuVfMG-xF787y0_XDsYYKI2GDnBpG1KqXtswiPmX7bkOU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae_SLEiFDwrrUryxIq_V1G7bCrkV4UtCBWCwPHIBudPKMkKIa4PBtydME2wEuxfMGF1QLqZOknEnmYppSAuBsPiZkSI8MRCeUL78TPbNhzTIB-fNiw7kJ7RkWGoFwHHDLDAHnUE5wXF0EDtCDY48_Kv44bRqj8b83t0pHe4FnKZlRmisHB-z0LaWXIOjJNGeHz8aSIU8pcsBnEdc4HYIhJjENHrmJZGpkc2OZlYRvFVNLGy1zYQo6gXLe6xkENs0ks7fLJZ_lQnhiAgE_F8N0yCygWgTGhPIoOD053Z4pQNKiuzbAE6R2_ziWLjHEEnIFfQO-6RObDCT909OlZqEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE_LONK0dhm3RUpZc-gnc3Vm--MSPXo7e79aonIxbA1UYTtGK93-O-rlEXY24zuukGhJFqHqIDH0D3zJnnbfowjtR79EQKEw2sX4iyg6f7AC2Q4ou39QgP_9WvY5RTFGF-tqg8pWdSERuRolRTY4vYkz8MZYF3wIUcDKWt-5dEsBfIlWoA3EltyXNVqDQAM1PosjxTOE18doeknLX6Dd9ew1MBL-uWDoGIV-Pwhbabyou0CROLtNjFM1FX_YOs6b3yHSovawu4LsGLs-2HJw_22JAADlNsa37kQUjNisRaeIx3TpSdwl1YbTHoI7J4iFnnDwsnovlVeVETthnwM_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Rr2y1dFTX5I9cbACopN9wKlDYzjQEooCCZbcej5ROlG8iQu9AFthUOk93qy6V1HjHHJKfMQzvxvNhNRpnkxbSEdct0wJh26aUmkFlHiBtjkIHFRoLKZXFjl1tccDicqc2nP-wi4Ch2i5yat2ZvZI7YJGpp7gZikUxAgaOCQsBNbtSTCCACzbOavyK0wVf1o3vGiAfjuUrdIelz2JZp4NJfUxlMb03EuC6ayYuph8bT5oa6lGPrcPzMH-ey4Ca1z9GORjs_gcScC5cOHzaPEzzcdUeG84ZY3uoyv-ix4K8_iE6TjHGsg4X6d8bw0NLI1eeAmLtnW3m5WlrdLrcrPfbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=Rr2y1dFTX5I9cbACopN9wKlDYzjQEooCCZbcej5ROlG8iQu9AFthUOk93qy6V1HjHHJKfMQzvxvNhNRpnkxbSEdct0wJh26aUmkFlHiBtjkIHFRoLKZXFjl1tccDicqc2nP-wi4Ch2i5yat2ZvZI7YJGpp7gZikUxAgaOCQsBNbtSTCCACzbOavyK0wVf1o3vGiAfjuUrdIelz2JZp4NJfUxlMb03EuC6ayYuph8bT5oa6lGPrcPzMH-ey4Ca1z9GORjs_gcScC5cOHzaPEzzcdUeG84ZY3uoyv-ix4K8_iE6TjHGsg4X6d8bw0NLI1eeAmLtnW3m5WlrdLrcrPfbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6jM0iaYYH4qucCabX2WjUT8uJvvIJTlczk2sCk5yMzppScpBL7ab15jYbyI1gfA6bAn_ChPoDqXl6_iu3arbUZgpPNFeOeQZ50ddOYLrYwFRrajeZZEIZ2tuydOch-FPPxJXU6KkuoMQr63mxOQnxwRCHzB7XKPuu-O5kbvfBwo-PGWaluaQprgR1B2wV3tqRyiTwyHFOIdBeGqRtnhuPh-pgHtXXgJ1b7hTvnt0MZEdGsLXhOQdWmqBJZlHZkWWkMq7d8JyqXnkfu2NaphJjVqLCR-ZsY-KkLlTK_2EYG_5EyUXRSV-7UEMubtOv7QLU_rtIiAe0584pdEde27KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=GVHHnQ8M-I_dA8FvFMZDiTqiPoWDOgA2WGXFiMwCLzABrCR5i6g08s-yPF1jFBH9dmf_fPRCyTHc8SJgsOwnyIit7WK365vHSn7SxS2USgkaO6N8oezNViZ3fUevpt2rtwjg6Ub8lMvF1NmOysn54kc5m4lmLyNBWxJB2TiDbUQmGEqfWrqUyfDbuGEXMTtpGVk7O8PfU9np7vzHZ5fVFiNQgJ1LRa-HpusYAj0A9n_13bxRl5tkagcR9na6S7QLere8PPavfAD5Y6io0iP1dlHFpbMq-H_VXPZtOHJPNXShqd8Hqs8cWXU0ZNkxbma1d1PFvey-R8XnUhacE31oSiw4w-PXlPnyc_4fYUTes_8CyqS27-eXbR-2kjp8BwrJigUIPL46DwLjnl_2PhxAKjOZSn0nF_qF_NzwWUR9lDx57qT-DOyDKmmwD1IoQYOHhCaIo_OD1c4KFjVBa0XCKLVy2gLDEOxjdpW-Qg7OcdsD5zKi0kEvM0ixcZvmmB5VrByB8WTBh-_F1piqPCH8AP-Ih7EPjlVp0TWLf9Y_5E_LlR32d0UWEO7DfoiTc9BdfXV0k9gblrltLl2WZqaRV7j3M_0SPD-USEXM-0CiKZFVIzJXfNsaImfxCtvFFG1DHDHdCyFAMsx2k1X2L10n-pKneeGgjWbOIMp7vAtMJLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=GVHHnQ8M-I_dA8FvFMZDiTqiPoWDOgA2WGXFiMwCLzABrCR5i6g08s-yPF1jFBH9dmf_fPRCyTHc8SJgsOwnyIit7WK365vHSn7SxS2USgkaO6N8oezNViZ3fUevpt2rtwjg6Ub8lMvF1NmOysn54kc5m4lmLyNBWxJB2TiDbUQmGEqfWrqUyfDbuGEXMTtpGVk7O8PfU9np7vzHZ5fVFiNQgJ1LRa-HpusYAj0A9n_13bxRl5tkagcR9na6S7QLere8PPavfAD5Y6io0iP1dlHFpbMq-H_VXPZtOHJPNXShqd8Hqs8cWXU0ZNkxbma1d1PFvey-R8XnUhacE31oSiw4w-PXlPnyc_4fYUTes_8CyqS27-eXbR-2kjp8BwrJigUIPL46DwLjnl_2PhxAKjOZSn0nF_qF_NzwWUR9lDx57qT-DOyDKmmwD1IoQYOHhCaIo_OD1c4KFjVBa0XCKLVy2gLDEOxjdpW-Qg7OcdsD5zKi0kEvM0ixcZvmmB5VrByB8WTBh-_F1piqPCH8AP-Ih7EPjlVp0TWLf9Y_5E_LlR32d0UWEO7DfoiTc9BdfXV0k9gblrltLl2WZqaRV7j3M_0SPD-USEXM-0CiKZFVIzJXfNsaImfxCtvFFG1DHDHdCyFAMsx2k1X2L10n-pKneeGgjWbOIMp7vAtMJLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=rJe3gnkmntDY_bknblHcySCBTmXfNiE1f7Vc0_IrbVpTS7mvWOqU2G8fvX8C9a3lQ0LXdap3JPWUlvH9OkbciX5nFcpTZkSARxpsf80pIRGvccyxhstmV0T0oVqIKa5ja0t6TCtqJVPhTy05_2iNO7ZoaZyX-Pbh1hmV4PZQIghby0I4RknZuqZSEcm7Vbejcup-vTcJdgga2fTYx5ooFUHe_mOvFS2SOPRaJbq6inpIXdlhToWDcodBzaAILJ4r1L5NkH_VeEjHEDj3TmCq6lL2sSXl1nu7DTCnBwtnzIy0opq2jDCHnd-r3Jc06wUHU7EhC7WJ4vc0puQNUQxr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=rJe3gnkmntDY_bknblHcySCBTmXfNiE1f7Vc0_IrbVpTS7mvWOqU2G8fvX8C9a3lQ0LXdap3JPWUlvH9OkbciX5nFcpTZkSARxpsf80pIRGvccyxhstmV0T0oVqIKa5ja0t6TCtqJVPhTy05_2iNO7ZoaZyX-Pbh1hmV4PZQIghby0I4RknZuqZSEcm7Vbejcup-vTcJdgga2fTYx5ooFUHe_mOvFS2SOPRaJbq6inpIXdlhToWDcodBzaAILJ4r1L5NkH_VeEjHEDj3TmCq6lL2sSXl1nu7DTCnBwtnzIy0opq2jDCHnd-r3Jc06wUHU7EhC7WJ4vc0puQNUQxr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i55K5_HnMsTDL04BVYvnE5VOVSQ9ZmluSuS3D_4BMZp3Kfo792_Qg4HvRbnCIfqKJgwjMNJmkreKVeEO08oacMeCY_cPOkH8LnSfm-dB9YITG4lnxmYSTcji8AwJu8TONV7Mzl4GhhjvIKrbBvu2IcXabHKBOlh7yaY_TJUuW6Y0V1bdUufHEyUvPphQfmC_sEGacqcP_sJi-wz9x94mLR5TnaGYmHlfLfHEYkLUwZcnvQLrY75JjisJUbrhXr3kTL_uxbLSbdoUFMNX8aI6mKSlRllLpcNIZEsEewau-QGlDxMTs_oVwOrIfBCczFSZTGoT7JfbZT09vDIArr8BqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=TqC8eDj13YPIDgYDEbSXYLw5RU07tS_laF_r0tiJ4TctOxU72yefUdNRYabVObNXxLajMMGun2CigUnvG2YX7SxgWgOEJErc8rmUvvan1fYJJ9I1zWzXkc9JCYRA9Twlr_mUJePZ4rqtGzlROV9NNGSGQVmP9U0m9QaxEwCKXVnqMMrpkpGyFZqV8otSu2UIQI1crOA__QSX9Xx6CGKG1pLUfQ7g-0mTpLAQxlif881qhmIDMnUtPjXv56UWPlFx21xLBTLbbgNUwwF9hnej5wEEMNxyABZ9MHh4MTJlTdAgxNemAXpUgkA3m5684Gi2-2seUWUAOkun3QOpbVl6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=TqC8eDj13YPIDgYDEbSXYLw5RU07tS_laF_r0tiJ4TctOxU72yefUdNRYabVObNXxLajMMGun2CigUnvG2YX7SxgWgOEJErc8rmUvvan1fYJJ9I1zWzXkc9JCYRA9Twlr_mUJePZ4rqtGzlROV9NNGSGQVmP9U0m9QaxEwCKXVnqMMrpkpGyFZqV8otSu2UIQI1crOA__QSX9Xx6CGKG1pLUfQ7g-0mTpLAQxlif881qhmIDMnUtPjXv56UWPlFx21xLBTLbbgNUwwF9hnej5wEEMNxyABZ9MHh4MTJlTdAgxNemAXpUgkA3m5684Gi2-2seUWUAOkun3QOpbVl6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqfnhJn4IYYXa46thN64WndYFlcVR8pJnN-9UqP3w0TWc6ZqCJVhpp1NqQXRw0jIHl0itIedOiDatd6o1bSuuXHzee7qUT0rdoGjcZnEeNrXNvEeyUkTZ4Z_u0wMVKK4bU5JIl7uij2s7jA6qCSqytVoCOsaOUWSbGSROWLSDds2egDiTuaBlcshYQbTlksfYuWn8s68gwlMEGEJTnrKDkoiDfRj_oBRRfmu5GS8brS_orwnVBdKSntcVQMyqGVKJVnBzeu1IHrz2UWLmvDUNxVj6B7pwxHonQ661RbGFGjYAsKRUsJ_vDDOHz6RIxILEi5835YmRrd8qyZBoRJG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=WBNopwhY0MoPgqhgY1d5tPaYA0apy8jAxtKyKJqnuE6wQKxWFTGbVORhYJrMdpoKUoa9GIrEZIS4P2AakJI8WSYuGwXiifyyn3mH-fQG5MBYaghUD0vH4RH8VxdAHM-4L4UvGqtvIaORAPHutB9BeWcsOwnOeREX1pVvCRzAt0HClGiTa7V4cXaEuIUFK_iGsrils_obdYL6hfQclkYNAMWbZ9lWwTQxDTqC6zkEV24RtvjmObYpO32zFz7q04tForIshJR2-Lz1W7_YyWCbhtNnDFpctjbRdPUsvkBcjO4Nn_cyvjwHq9e1THINCMWijscmkRXt5jlmrffVTlV9-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=WBNopwhY0MoPgqhgY1d5tPaYA0apy8jAxtKyKJqnuE6wQKxWFTGbVORhYJrMdpoKUoa9GIrEZIS4P2AakJI8WSYuGwXiifyyn3mH-fQG5MBYaghUD0vH4RH8VxdAHM-4L4UvGqtvIaORAPHutB9BeWcsOwnOeREX1pVvCRzAt0HClGiTa7V4cXaEuIUFK_iGsrils_obdYL6hfQclkYNAMWbZ9lWwTQxDTqC6zkEV24RtvjmObYpO32zFz7q04tForIshJR2-Lz1W7_YyWCbhtNnDFpctjbRdPUsvkBcjO4Nn_cyvjwHq9e1THINCMWijscmkRXt5jlmrffVTlV9-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO9mwWl8JyC8LzoTIO4FCE8aExdE8RK-LVNfDMPGVCTCKJ47no_wbOAIg5X08yVV45y28DwyzW-xDufZlRSbWMqokrfs1-wUAHXrHHwU63QiCLZusszoX92O8HSMXTulunxO3ZdDzlQiWNJ7-QCYIDVhyUA3e5n2OLaAP8pfxTd642clgCz35qKuDEp-peAQ_Lu3cBQ0qc5Ud3y9SWHFQXHyj98czEM8z58ciF9VUgQ6aXELeDbzDb-pvfKeJiwy-L2UiOpRv3xNvrW0bAXmOxl-oa475DqQTtiRqAU3pJ4foJZA14yerDHE8_z8_Jfm7aREvtJTLG7u9_wsiOXt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=AR05-w0NMOu4cQ8pWLpB4TNVyMi7N4gGdJtn3eLvtdTZlKpDA7V14nexd0oeDJ5vIHSwVLYbqJGwdhlX-iGnitEAF5U6bdxQEVdLC6SdwASW_recsxpOppXcP_3lvH4VJa13UKUp8oTPeGoyrmy998Bfy_C3yBb6uotft1h4KTCJ3ExcErQxtgNGwt79bKRMCi8Uu8ZL4iZdcpMdGmN76mKWyEBERzfwfXC9CfrZUMFWG0119lJzbUXUVEgY03Yt16FrBH3DN9wGAzrgcjLLZH98f-NlezL6Gt13BLJ0D433HUMduHCRvuiGQUu-MyOaBfuKxQvsxxu7L01a7cuTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=AR05-w0NMOu4cQ8pWLpB4TNVyMi7N4gGdJtn3eLvtdTZlKpDA7V14nexd0oeDJ5vIHSwVLYbqJGwdhlX-iGnitEAF5U6bdxQEVdLC6SdwASW_recsxpOppXcP_3lvH4VJa13UKUp8oTPeGoyrmy998Bfy_C3yBb6uotft1h4KTCJ3ExcErQxtgNGwt79bKRMCi8Uu8ZL4iZdcpMdGmN76mKWyEBERzfwfXC9CfrZUMFWG0119lJzbUXUVEgY03Yt16FrBH3DN9wGAzrgcjLLZH98f-NlezL6Gt13BLJ0D433HUMduHCRvuiGQUu-MyOaBfuKxQvsxxu7L01a7cuTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPhXwZX-OI1p3Glei-m8W6oB1W7TlnZFYQpAZ1laQDbMnavxxvquJ66MHD2Xg_s-d3Y3cHg8bxvQo4a8BFqHI-n9je96ylb9TBrcKWEwhL-em0VblTtiJqeOSXgg26jodBsXuSo_5VBgUBx4KTmA-K4AVGTIjQ_yKRQfVlRUlx1BAJD3cj_jh5a0_jal6JJfH4GDOio_JnwagYAhb0fQBgk9vZbZxoS8iLlPVpctAy3stT0xDmu0Img95evQ_LU11E3vObUbVIHFq0i-HywfrXVYhoGdGY5aZlbtkdTTgIECT4kww9cYn6ZzIHuCUUJM-X4r_FQrzO9s6UMky53Myw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=XmN8W_RUE_dLO28FqnOG0jgg4AyH4sxDwFSyU242AJrPJe5glGcl8Rs0VtsIZFO8LxasJF1CMiNlW8v8XT2uslG2ZINUC91Ta-Gv5j8FkDdTDQIUDu8GDhGtCy0odCrZyauIexh2zsN322NoU7KLJE6KDTcnLRJxPTdERzf-kILO4MS4mHpYLrgA0h2ckwO2KQFUyDLZznu-YGcW7h3YtNCVnqxu2aEzYWxi7H0kq8Wh1K1vFPV43SmnlZODfpmgzJBAoFluDdlK2SJRmiaBw6u-MkCQzKQ242jREMZA2-4Jn6yXKSk4gmW7qSESQRgJsBzvEUnUuZrcIGC9gpZ6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=XmN8W_RUE_dLO28FqnOG0jgg4AyH4sxDwFSyU242AJrPJe5glGcl8Rs0VtsIZFO8LxasJF1CMiNlW8v8XT2uslG2ZINUC91Ta-Gv5j8FkDdTDQIUDu8GDhGtCy0odCrZyauIexh2zsN322NoU7KLJE6KDTcnLRJxPTdERzf-kILO4MS4mHpYLrgA0h2ckwO2KQFUyDLZznu-YGcW7h3YtNCVnqxu2aEzYWxi7H0kq8Wh1K1vFPV43SmnlZODfpmgzJBAoFluDdlK2SJRmiaBw6u-MkCQzKQ242jREMZA2-4Jn6yXKSk4gmW7qSESQRgJsBzvEUnUuZrcIGC9gpZ6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SheHVqiopnihl1UkkMJGOT0KDCGaw1v54xMYgwu5BUw6Hk0eK5t0SL7vWw9x17Y0bndqSRVHuPnsua_GgUiU-25RLJ3sDEci7zW-GgVFD7zGHNAm-GxIn_T9QZi3m0GG-wrXaSDc8hK2HqKyA6P7IvgURdg1R4cN6Knm6V5jhe215w2vXBaO4hzZEH2Rh_rl28YrE2gHaW6aUcMBAkBrMC4h6uZVFCxCRlOPEjpXAvTvsRcMJYcGHxfhwUu5G5svKVOyYK-h-pD7ZlHckrB9cYqVeI75IslSsTgKXVPsqxljLzfJadpBeEofhKRam7xxufgisye9-Y1lnRUt8eCDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رویترز: یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت پرتابه‌هایی قرار گرفت و یکی از ملوانان مفقود و باقی کشتی تخلیه کردند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20457" target="_blank">📅 12:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دور جدید مذاکرات بین لبنان و اسرائیل در رم آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20456" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
@WarRoom
اتاق جنگ با یاشار : دقیقا در پست ۴ ماه پیش اتاق جنگ «نشانه» 10May به این موضوع اشاره کردم</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20455" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">روزنامه روسی Izvestia : آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20454" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl2ExqtnVDlMWYyZdVGgQQyYQik3oRoBhbO94U1bDpiLagbfwKDJHeciA_Z_mNSmSySHxfylPhqoqZY5ql5H1NVv6ojy85WSTLMPadI2gGfC51tc_hbZmtJEfM2XG9Wg77kjLbWPmmiNwJjRQJhQO4IVIJbHu5mo78t0Yqdm5dd335WFZNVoxVTBlxJusDO6J6Bqo7rj3WDwYOFXCajSQ2gBow16n0e1-rWJcdvbdFjCg7iN0L42IGUl-SRgOs5OFSAAgEYlaJv4FA0cQwnqjVc1E2LeBTdyuiEiWyWhEOymhwpI5Vq4X2ueygkjY9ltzT4-3YAHaqfznY5hYY2s3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غزه قبل و بعد از ۷ اکتبر ۲۰۲۳
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20453" target="_blank">📅 10:48 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

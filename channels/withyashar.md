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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل می‌گوید ایران از ماه مارس حداقل ۵۶ نفر را اعدام کرده است - افزایش چشمگیری نسبت به ۱۵ مورد تخمینی در مدت مشابه سال گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/withyashar/20564" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏واشینگتن پست گزارش داد که دونالد ترامپ، رییس‌جمهوری آمریکا، در دیداری خصوصی با حامیان مالی خود گفته است: در نهایت، باید جی‌دی را انتخاب کنیم. این اظهارنظر نشانه‌ای از احتمال حمایت او از جی‌دی ونس در انتخابات ریاست‌جمهوری ۲۰۲۸ است.
@WarRoom</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/20563" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/20562" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/20561" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/20560" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZHgsDXZ4gIPvbtgbHAtvwKZuKfuhb52_bZbTGy85dJ7AN-Mwu-hCzaMlUsSPPWo1yLqS21wMN_SSQqeExRSvBKxaU3LTGsuA9GcU5kWq8EpkO-AZMDiX-PT16dYBTJ-CTPqz1Gd2CmBYnH3aEEuFeDIsjbzFJId-Q8QLXuGREneJ6wMqyJ6y-gqVTlLYJRGlXVyUL_omjpB6mI8I03d8a_TXlfZ8v8ms0JPtqWF_1j2b1PcReLXHAwS9u621_GcSWIlrD_r4I5REA9_tRd5SZK0sbtDyrVELvYMURXn6rb0qWNTPEbFt044mA6LsKksNkjlCmlUgf_-FTUS7WC99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9S1anE1ldEHSXAgxxPINMjyGR00uvrWAMaD4boDMdNRwnSVLAPjZLITrWDFliIx2i8_DngI_FUlRf_aDhUVVmoD42joQUxpigL-jH_kDY0_1K_CEhopdtUUeBPrc-xee5Qez6Fm6CpHDYLehPUL82qYQ6tHDmDqHoIJraJaoIvl90MPWz56-HbQ_yG5qi5Kxapo3BTxd0vMyzzUN8_mtBwEOC4VlYx7-9sSv142ImNKF5Q5x5h4qxyRlgv3zqosvEy7OiOt42BsUkE85XLIyq0d9MJmlog4ZB5lZYr67OBWUh1JlDqK-pDwdMDP6l5yOFMCWTLesSiIlvZI9z4L6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت بهای معاملات آتی نفت خام برنت با کاهش، به ۷۹ دلار و 2 سنت در هر بشکه رسید
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/20557" target="_blank">📅 09:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFMLm-dJloEHsM5Vx0svCoAg16gku4piVSe54-kt2v1WJvKqohdqjqMOQvXL8c-rHIwX3HQW7n0sSDiOP54_MeFUGig4tJcmkMeWXunYfpCmsXRMAPah2_ZcPFNBzdkPmOfgJaVS-jgFpSHz7pImXev6tXaCIEoqTYUj02a2YVQavy6PUbFn4Str8mqvulFMl56pOFUteZL0HmRluBvo2AseFlyIO_e4gbaMsv4KOLbouOufMzYMde0LD7hMaHQcZLYoMSEhir5P8S0xAhSoWcHykU5SW3OkxMnpYAH4BEU6R5BkyIvDqVDpOzN5gLK0yrl8L-fwS6O71NIki2HEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «
افشاگران» این اظهارات خیانت‌آمیز تحت تعقیب هستند. احکام حبس طولانی مدت برایشان
درخواست خواهد شد!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20556" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا : بر اساس این گزارش، فرمانده یک نفتکش در حال عبور از تنگه هرمز اعلام کرده است که در فاصله حدود ۹ مایل دریایی جنوب‌شرقی منطقه کُمزار عمان، صدای دو انفجار را شنیده است. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20555" target="_blank">📅 07:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی دی  ونس : من با ترامپ در مورد ایران اختلاف نظر ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20554" target="_blank">📅 07:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سناتور تام کاتن: «ارتش ما آماده است تا کار را تمام کند».
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20553" target="_blank">📅 07:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAoPIWhtMq3xGDes_mKdiK_SSCLhJV3sm28Tw6wgUEgewBkB1zPNR7ukRm0h_dK3FaLWpvug3nbjaDxODjcUbXXP35enyxHaIJf__8ND4d8wYkeTelnQoYW9tXS9KBLdD8IBQsBQ8v3d4WjQ3Vy-KbnnVFNzE1gRWf-4sUxaH2Q0sHQjcyv3ZXwJp2jSPnT_Yxi9WQoNK28xR7NA2zbkjBSt-tug9qyawOhhf97pgd-dOoY6Dc5WNyHnurm7NtRe7PgUoLCJ3AsqkJjBepBLeqX0DtRB_M3spkMja2M71xbifgObYQuA8N9dLifZtaQsKTm0Gp9KkVjrczFm0LC1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20552" target="_blank">📅 07:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/20551" target="_blank">📅 07:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20550" target="_blank">📅 07:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شبکه i24news درباره تنش‌ها با ایران: "وقتی بازدارندگی آمریکا تضعیف می‌شود، بازدارندگی اسرائیل نیز تضعیف می‌شود."
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20549" target="_blank">📅 07:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20548" target="_blank">📅 07:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20547" target="_blank">📅 07:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20542" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را 30-40 هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستن
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20541" target="_blank">📅 22:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیروهای یمنی اعلام کردند که با استفاده از یک موشک بالستیک، یک تانکر نفتی به نام "دیزی" که متعلق به عربستان سعودی است، را در خلیج عدن مورد هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20540" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRKFTzWkKEK4Hw0ucZ6G88rNQtytAdTfVxfLXlUSrMhqmGDyv0OWtocjvgI_J0zNVzpnCY8sJfQplfqXi3VjGaauzGmt3TVio8V32a8pL2h3Rt18YMgGy34qNARtDXjT2QI04b7f_2IR4ukC9IR840yqhtt1ElO1wjn2GHaNNake3GjW1qUHKmZC5r9pcTTQO_yGeVarfJnvIVgmrGmrtaDO6GSB8AuLjvflrA7PbP5Ded0iZudPFCSYN1erLPLdpAvgV_iUjZhI0G2d-S2aZWfdkw0OZqPUQ-cD_aqe1br-lSZx9DwkV8PnvFf-IDFAS4C2yTzMsvJ826irMuxofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJZNgIg3Bz4FOus7DcD7WcFrp5uLaXwGFcGx1QHPcYqG2WP3l477nNbUnKL6b7qa4d38yo7CtEWJ6PaQlxMQrdO8DL1a7CZ-XlT7GOKQalg4K_rjBiQdh5KMnsQRl_rmIeHUrbx_rTkO_yUDvI7KD9D9ZhzKCoLVE-hI7lFzTjvIsj_mY8VOL629n_TdCMZ-53fafj4h9_ZT0GH8Vzabgh89kmfIeO7AdgZ3C2qAS_8Nnaov8RJYzGnOld5KMPb3UJTX5eaqkfy52KFI9udEQLy93bJQG2eoMm6kewZVTiGzAmt2Gs6WjOpJCPARxz80hgn72C2YLM2iITYeQ5ITGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou4in2Fh0RynLXUGls6uufw7c-AZ7qlrg6Pu9Rf-Qokxt90dkdOY0MlRjQGkrmEsI0f14fWWSuR65BksziekwSoFwD_BXIb8e5H-IW98BqNl8sXLvhfYz9776TyFV9Z-H3gCBohpBdmlZeHU8O25WOcajoW723uPQTg8mbgJN_r_CnvzDlJEjfQENzMBKVfZu1BkV6ph4hzU8RUgMr1tGmUiWwlM_N2nGqf9M6UFcyfZtxpTYHAUry9z0rcdDojTolBsHELsxkoGMD-HiW4CCv_-UU_l-A4phzSUU0zOmB2Dgq8-8b8F4G-QmrwwCe1TDzT39-M5KEC7HoOFLN3gdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=D2PltT8qEwkzNm7SUNIdMxOgp9A43cFEB6XBa2s3LNYudaaRFxvtsu4LgoRaVPxppKlug4QO5wI5ZfxGsTClr1ld1I3CZpKmENqQZj6QGbYFP-eO4yoLp1zZplhvSu6LunnN5ueJqgcDgFwShkpHx9dWk1iIJnu68a5QZiKRa-W5UnM-sWGp3wbTtNyeodUZcIKTdDPsQX4URaZbTs1GXRo9xmYL0J8Bp4ct2VEqY48oEux4pe8bJleqFX8iau3v1kQfWtpyPmSVGVLUjJG1b9yL14pMkA0AtqRk3TFSq_A8c2tnmx3PitSc7ahq7194UnVimPJeyFr8XwKjis8wBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=D2PltT8qEwkzNm7SUNIdMxOgp9A43cFEB6XBa2s3LNYudaaRFxvtsu4LgoRaVPxppKlug4QO5wI5ZfxGsTClr1ld1I3CZpKmENqQZj6QGbYFP-eO4yoLp1zZplhvSu6LunnN5ueJqgcDgFwShkpHx9dWk1iIJnu68a5QZiKRa-W5UnM-sWGp3wbTtNyeodUZcIKTdDPsQX4URaZbTs1GXRo9xmYL0J8Bp4ct2VEqY48oEux4pe8bJleqFX8iau3v1kQfWtpyPmSVGVLUjJG1b9yL14pMkA0AtqRk3TFSq_A8c2tnmx3PitSc7ahq7194UnVimPJeyFr8XwKjis8wBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZDzdBzi7L3kDBHf_hkjdxb13d-usJ_8rzA0i_1CzcGcFMVe_1wejCds2gKCuquvSRPB2Xr5bPRAjSSlGlqRHp3-ZnnRzjRyKSySNg23xc2MF2N9qUL_CKGRglWvn9JLXq_x0z1_7ZiiKx98wO4d1iiHvcUUFPS7QVS3eJDTs00J8rgB3uy9ZWFuiSDifnKhJmwX6BtTjeCBpFXltWZWjCkvvsoZzUqGJOj98zM0w0TYctdqXfvP71UVwEEZoXNPGTmvbYhAKjNuFyP5olAx2Q4UNsR9LvxtU8vJShiI1Eapx1q1miNPLzt88Ko7pXJ3DMDSwjNDS7U6bysyUIXOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFsjKrrVtwB6p-8YLOSfBAHXgB3-MUWtN9fxmInvV8wW_wmTkm9Kwg_hb5RAxs7ZdtR42cOEuEkX7cegWJkhnO-E7xQ1IgJQpKWuH67jt_oTt5oREeFm-ELzycyCs7I4qlUkhct5JIMmFKU4uXTVcIyJP1KlOQJ6M3OGtC8Xb6IJEyRq44H8VLSIm1qeBYWUNTZvJ_8K_axmHpbpzRxgnLh9xPS7CGUJ7lYj6STxVIlb83aXFy5jQF1xQNVPtJZLsurGqR4cpX-76mg3dfV_GYO_C-O7RomcvFs29Jv3MYG6jW6yWMk5Wrpyp4rLWH_So5EDfD34p-oLkRbdjB_JZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqAghFgUWsx2FC0sYOwuEaV3jAJSIcqIiEZJxPn_WMnkvtO3i-0lGhIVuAmhaK4-EY8SCLOmLotFVPOkzY_kcY4EKGpygjWuxI2yATBIjxWZ02a30vk4HirQVaBwz_uL1N3m1ZhNGMeHHshqWqarT3UYDOMyderauNXqZCajagOGdo52gSckJwo6BXSP1ol_DhOcpv5nOEnMHM8TwDFdotYdjsCW5cVDfV0xbTRVsB4GXAIhhaGQMIUlWZRLXYqbXI9XezijS8lw_F_IRU-FAPKpRMd9c3BZkVAcdVY03vsZqATxWplgZ3ldwokjY1f_CKiDmLtjvF90B8VZ0uwglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5ZnJWS3NkHqwzcaeERA75O6cCrcXEZgxE4WgkkTF4h1rI2uJkng8BUjhh24imT2PjmL_pKKZmAT_GRFQ2SUBZvdH3Sia6zJQKlfkX4W3YaqP03bfKiNLIVQ1rk5DAzqIg54f9r_7g6Z-7PH0V5DmnCKDFOuXsJV1GLJIEEWkuSkOxkRJzKW__kb5G_gGWn6f_xOB2PM2ZEwzSgUXV-rqguUTcwWGwJ6QiuAfp8N1HUAQfmiVJQ9m20T4XA--m5ptNyDh7lxw8eha65Rii0r_-As8vpXJ-Igm45JJUmH3NKE0gUZGf1qzH0QjSUEMlv-mP6VcmuRbp97ed83IEMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=g3CU3LDoz5YIvx-ezro-QiQqXrJxTVL1u6bFFFKQMZHxGzPFpmIdUo9RsIDji0YveUT3NENUJYUAdqSAYCckUwMaiL0xtBDzzVNQATIf3htv6viOQ3vD0gg3yXT_7KKBrTFcbgXaxqPMlFI3aQYlch_UuAB-cYkS0fdQUJL_HwqcmFNaf562tA1s7yxtSnI-M6rxuiN9PmkNkRNyfrs3Rhw0bGJfx8wHEysqTW9FpR7sjFsvjy0oI-bifqP1Vcr6maFdLSrx2wPFuLJTZ_SYFs-dw-GWCquG2xl4ApIXnVo-06LNElwD31YysjKYYJm54ZzMCDF9DyCjJn0cOCilYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=g3CU3LDoz5YIvx-ezro-QiQqXrJxTVL1u6bFFFKQMZHxGzPFpmIdUo9RsIDji0YveUT3NENUJYUAdqSAYCckUwMaiL0xtBDzzVNQATIf3htv6viOQ3vD0gg3yXT_7KKBrTFcbgXaxqPMlFI3aQYlch_UuAB-cYkS0fdQUJL_HwqcmFNaf562tA1s7yxtSnI-M6rxuiN9PmkNkRNyfrs3Rhw0bGJfx8wHEysqTW9FpR7sjFsvjy0oI-bifqP1Vcr6maFdLSrx2wPFuLJTZ_SYFs-dw-GWCquG2xl4ApIXnVo-06LNElwD31YysjKYYJm54ZzMCDF9DyCjJn0cOCilYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdJxITtb0HbmXvsBGtNJKLPZCPuCgdX2R1s1ofR3_1_LFaOAN832v5Xc9gdpQXAu27KIbqPMAPwV1VjFchRaFuu3vf8w8cXYMMwoPQFdzU3e234fQc27iwirjoJP_rE91KSGPScvjJMviepMyHgri5Tv3CAunl0ZpgkzVY2q_CDGTSDnemNMa72WjF1f_PV-RXnEnSfwHBICXIxuIuj9HNLWBEtJ0Yv-iLrYVa-Y3NNpc5Ce-GFNKJEVxfBkGXJU76Ky0mHKcSNi98X35H28U86Zh8yfI4nPils0mloZ9AtLDzme-ZdVKeDGrlXmDI-FTjTwLaFw6e-dPCllbQp3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=vriJnqbU4fLVdk4bLZa2BX_ZoU1G5r7HM7_1r_bXDFm7LYDBaK2DntcXXzHwBULpXONC-npL4sqEA-m8GR_6S4qZowVIQ0E5TBhKtbFEx4hl_fbztxbU_UHKnyUdt6Y56YAxf0smRDs_PTvE_qPuUQ9iD_xC7nbMs0Gvwy2vV836okeyj8L96zI9kT47hmCZWm-N5xaIXeerUCck8IUW7TDj3Zuy_Y9gfkO516KkNPZys3KKWjST-6dC1xP_Qy9IxEDOWYNWyPyqzwC9s540kXohPOey9Nzf4xMWZ6ZYe3qyz58beq7mA3tscq7B06r2VqLsjHwHfpM2Wn6T_OWCLS0yOMn2M5oBLD_7kyLsSCDef_ruye1LRMDImM4O2UlxQN8yghWWWmBXdc-ZjQyeUUXJxTyu_wEnANq1uRUQ5H_oHqS4lFX1L98vAFyb4H470U0_f0aotSAxe0iVoSprNHrxQ7Mn3wzUHfy7F4idOShy_uPXqLPeED0jNljQnW9SB7COI7nqsYAizgmQ896MXGjDRIgvwnpOPkT8bDHHv9tVkNUEu1vQbIypad-Srqv1xvLadVGNQcFQUtnc_lCLyVwI3nSdJHhCtCvhOX0M0xPNpThW85w2c06YuQY2PB31lRIKFim3OxE-Lt4iUDPI43N3r6qhV0Lki0TAct1A4u8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=vriJnqbU4fLVdk4bLZa2BX_ZoU1G5r7HM7_1r_bXDFm7LYDBaK2DntcXXzHwBULpXONC-npL4sqEA-m8GR_6S4qZowVIQ0E5TBhKtbFEx4hl_fbztxbU_UHKnyUdt6Y56YAxf0smRDs_PTvE_qPuUQ9iD_xC7nbMs0Gvwy2vV836okeyj8L96zI9kT47hmCZWm-N5xaIXeerUCck8IUW7TDj3Zuy_Y9gfkO516KkNPZys3KKWjST-6dC1xP_Qy9IxEDOWYNWyPyqzwC9s540kXohPOey9Nzf4xMWZ6ZYe3qyz58beq7mA3tscq7B06r2VqLsjHwHfpM2Wn6T_OWCLS0yOMn2M5oBLD_7kyLsSCDef_ruye1LRMDImM4O2UlxQN8yghWWWmBXdc-ZjQyeUUXJxTyu_wEnANq1uRUQ5H_oHqS4lFX1L98vAFyb4H470U0_f0aotSAxe0iVoSprNHrxQ7Mn3wzUHfy7F4idOShy_uPXqLPeED0jNljQnW9SB7COI7nqsYAizgmQ896MXGjDRIgvwnpOPkT8bDHHv9tVkNUEu1vQbIypad-Srqv1xvLadVGNQcFQUtnc_lCLyVwI3nSdJHhCtCvhOX0M0xPNpThW85w2c06YuQY2PB31lRIKFim3OxE-Lt4iUDPI43N3r6qhV0Lki0TAct1A4u8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=vr9izIl0uBReLtYMJBdIFkdHc0wkTesTnThCx0h-qY2fGqVkbCuamd9ES2rB6N5qx7nTctewrjnaH_wR9GuSj5hrxULLhcli7uMlnYTwEF89IymR4_WfQqPrmcEXG43zgo2U9Q1FqNobQ13oJT47dpBnazvnbtgvKagCkXLZL_21HtqQfmZRCw2DWqG9YftuM02sURyGND0zCHYDLEwXltRDYFM2b5Roc3jK5fSXAQSo2m4Ceg0t8vLexdKngPDK3UWm15-e5hijY34j_SMM6uABPZ47r_jfUjuie_4bM4FYn4ltwIH8z07dJXEj1m117raBiTpKfJ7GYTW8SLqaZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=vr9izIl0uBReLtYMJBdIFkdHc0wkTesTnThCx0h-qY2fGqVkbCuamd9ES2rB6N5qx7nTctewrjnaH_wR9GuSj5hrxULLhcli7uMlnYTwEF89IymR4_WfQqPrmcEXG43zgo2U9Q1FqNobQ13oJT47dpBnazvnbtgvKagCkXLZL_21HtqQfmZRCw2DWqG9YftuM02sURyGND0zCHYDLEwXltRDYFM2b5Roc3jK5fSXAQSo2m4Ceg0t8vLexdKngPDK3UWm15-e5hijY34j_SMM6uABPZ47r_jfUjuie_4bM4FYn4ltwIH8z07dJXEj1m117raBiTpKfJ7GYTW8SLqaZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQlKVTRpc___f5OqYEID5WWoCMiJs87uPpx9p0VZ_-RVxQ3qN6Izg5FJup3oKbYxiQyd8lYp7CEtyD1hNk3rAWDoBip1ZxoGwdEAkkpR0pGvDVZrlAdBZY4LkYTHrE_DKhJrpUV_G04Im45dAs28OXEC-YYtETKVqr0StTm7VwDjn43Eh3_BSVj3uBDtBUMFCHcQLEC_xc7vUH_66w2MOOd5Ny3O5mVResA6IupFKd0mxGX8auuEJfIgUZXCFXGqI9NPrW4P69tMeLEYlmCz0UQ4CaqpT5zq5Kr9iDyaBbyVGvP6Z_10IzRa6Cy4Es9L181Y3tsjBP37qiNz0JgZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=IslB9uldxC0_o8hGu3HNDCnLUqTU7sjtMr_CChD6milyhTenZBfgS_oqWd1dQC4TXwFlTtPyloVaMtm6uTffsnEHPtArAIaa3Qqg19uu3NmoJjL2M7aK9zhtwhSESOEci55e3dqH1Vm8iV1Kp1Ut8h5x0LUL4KCn1adkYuNZKTYPkE5pSlwqH32lOnLl-4QM_4ByOsyZDl3LWXrIrysYYPetDzX34tOnuyDcy_3UL3XWzOk7qyLO_KteI9mqkSVl0grHtqU8mF28kRdn1CVuxledHAEnDsX9Y77OIyg2GSlLUniOOhOmpxyZe1u0DvzR2uZdXdDA_oXWoHQZU6jnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=IslB9uldxC0_o8hGu3HNDCnLUqTU7sjtMr_CChD6milyhTenZBfgS_oqWd1dQC4TXwFlTtPyloVaMtm6uTffsnEHPtArAIaa3Qqg19uu3NmoJjL2M7aK9zhtwhSESOEci55e3dqH1Vm8iV1Kp1Ut8h5x0LUL4KCn1adkYuNZKTYPkE5pSlwqH32lOnLl-4QM_4ByOsyZDl3LWXrIrysYYPetDzX34tOnuyDcy_3UL3XWzOk7qyLO_KteI9mqkSVl0grHtqU8mF28kRdn1CVuxledHAEnDsX9Y77OIyg2GSlLUniOOhOmpxyZe1u0DvzR2uZdXdDA_oXWoHQZU6jnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM-R8pu07mdboqp80vsXT_GjddYDi7HnJbTBjrH4AUVFn9WnqiI1zVBRo1tozfoxcfOpDPv1KW49igaB71tdbZJnyieonhxcFK9Xf7AjV7SRHx4Vi6gqGrpZUmthBfrA84_5MOkbGS1njE9EaEWPROKCp_xDWD7GfHxsY4h8Zp2ku_18-tBiSlVBODqd_p7rizo4moMy8KE-kqebfg2dSRyDSoQVrzIR3An5CONDwuMENnj0u-abn2puhUQsMZeZaVbjIWK5K0MxI5M7LzC6RpCnzi1RmSvziPAsPQfj1P6NK_h_3gts3_IKJQCz5VIRWgKN8lyjks0V3OtU3kuqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=NgAaAl4sUT48FEkNN1kXmKojz6vtL1IQpiEjH0K3XVijcJ1Yv-4JIM3D3uftaBjy7QGY1FK30z5-Zth1ja1mMvSUR0IV0R3aaFLy0tnxPhnuv3XDoxudqBnuFi9U4daeRJ1y1zP-X3kq5DV5OqqGCmDOWEbnhccI_FJgoZPwCDHHhpBBdacpAYftQGczMEjU9r2E47ksLKovonPt6EuCeV-8MYk9GQZJSNzAx2K-9KkJJNwnrbpglh04miccDjFsUe89CTvCwNTLK5BoHjWePfPiEBqXHdeCWp7OwcvINWygUjJhlb1F8g3q_vSBDnQCyw0TwavJrT3H8KFzOpH2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=NgAaAl4sUT48FEkNN1kXmKojz6vtL1IQpiEjH0K3XVijcJ1Yv-4JIM3D3uftaBjy7QGY1FK30z5-Zth1ja1mMvSUR0IV0R3aaFLy0tnxPhnuv3XDoxudqBnuFi9U4daeRJ1y1zP-X3kq5DV5OqqGCmDOWEbnhccI_FJgoZPwCDHHhpBBdacpAYftQGczMEjU9r2E47ksLKovonPt6EuCeV-8MYk9GQZJSNzAx2K-9KkJJNwnrbpglh04miccDjFsUe89CTvCwNTLK5BoHjWePfPiEBqXHdeCWp7OwcvINWygUjJhlb1F8g3q_vSBDnQCyw0TwavJrT3H8KFzOpH2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20467" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvz2St97NARWYqTM4nEiBt0UnwdoebpHEKG5T4jjxg0fUvlTSpY1pQGvg8o1G3xj_UP3eGSpO3s-XtmuQ0pim3gXjP3IzHwLGlM0myneBlAseyIdBaRfIqBSsjmy0U5tsBhf-bEfLgnRNdt9uvaL1rgsFblAW3c6WIGV-zdMxNrKh6dCXzhe8219yf9997AcM1W8BKknICgTG0zElCFj1DuE2IQw59LZoxsWXi2dp74hhLtFqJpLX54eXqUViHlKM6hz-XwRrhwhxX7RammLknCnH6MD1UkI8iyz5doFfMOQdiJa9Bx34wVWZH9dY9l8SsAJ4jxJzjUEyjfHR8JRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی دیگر از دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20466" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=NCJGgUqzYtO8xbh4a_vPBXMwaW7mZH48F345Hl3kWqx1FtY75oR5vhY7jgepivLQ-gXbkestSkvN5t0eh67W9SMmbbOM_Os8iXypvdXG9EQW4TMbAii9vaI_5LLW95eQ2yxy46Ki1Q0WUUCKSL_TEIC0TWPayQwPVIB-txOJz6yuoobVheJmueqlkuoRusK-kM4EDl-vOu8SOAZmSJbVYCG_945FNvUNBGICYU7GkFybbQCOQ5zMTVa_w04Zr6cj_OroCYIi1wk4isV2kpHbpUPx0WsX24iQ9GvRVWnRLfglQnJQsumADSeS0WS6cZBEfobhk9sHLBIRQhMUq5yWqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c3af8280.mp4?token=NCJGgUqzYtO8xbh4a_vPBXMwaW7mZH48F345Hl3kWqx1FtY75oR5vhY7jgepivLQ-gXbkestSkvN5t0eh67W9SMmbbOM_Os8iXypvdXG9EQW4TMbAii9vaI_5LLW95eQ2yxy46Ki1Q0WUUCKSL_TEIC0TWPayQwPVIB-txOJz6yuoobVheJmueqlkuoRusK-kM4EDl-vOu8SOAZmSJbVYCG_945FNvUNBGICYU7GkFybbQCOQ5zMTVa_w04Zr6cj_OroCYIi1wk4isV2kpHbpUPx0WsX24iQ9GvRVWnRLfglQnJQsumADSeS0WS6cZBEfobhk9sHLBIRQhMUq5yWqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش مردمی :
دوباره زدن
، صدای صوت موشک قشنگ شنیده میشد چند ثانیه قبل از انفجار و الان صدای جنگنده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20465" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUrC9jJ8f5Dm8_-yNJiooF1ajbtq-F94v4qSj0Ij-Ky-q0eDi36Vf9Pav5-ffoUMeDCQ1RQlCZf1dgRY5HWSWuGNI2lEo7nJYXfVH11EGZRcPRnWvaH9G4WUjE45IxlteYLLiu3CbRIb0JiMgIyTgSuN_IQ4VKGusa2jBG9vwNW-g4gaYKNLLjR3SN2yoRu6NM-aJFxXplLTQ5GKldP7ey6hdxJ9pMLk-dldEMluF8p4UDZjAiMSqeP0pr1Z4hyd6NEIXqPqZ1qn4oQJMADN4FzMLSPQIJI1QdPho-zZSYX6G6FVz60SrqnJAM2WXAbjt6pnSbHr765B3ioG62AUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید گزارش های مردمی تایید نشده : مورد ۱ :دو کارخانه منفجر شده مورد ۲ : کلانتری فشافویه رو زدن @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20464" target="_blank">📅 13:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20463" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20462" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه) @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20461" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7200405da8.mp4?token=YMrPaPg-G8wPxZlSG8QmQb7vr6HljJn7APtuo1yWVfN2Z0l93dUgJfQ0u7FmpVZYy4fQ2jgvNgx7uUfBvzXBoCysumQGI3z3yvDJ_Zqkkd725q7yEUDoIzJjRm_mnYh6mW2Vtj67OyiyVJYJ3Md7uwWwsScuG603yNmVfF6K0nCIIfe6L_E-9dpfN8ZCgMA-4wi3Fb_hd2HyySe2XDyR6HF3jx84HDner4lz4UctDe4eYTFA9clVE1Cj5LcE4F6IUAvZZypdUbQZ_cHRPqrKQNcAaCoEi2nYGBu-Q_IsnzNF7EpHvhoKPyK20dGrJA9vK2_Sv5sbAk2inXoW6rlXpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7200405da8.mp4?token=YMrPaPg-G8wPxZlSG8QmQb7vr6HljJn7APtuo1yWVfN2Z0l93dUgJfQ0u7FmpVZYy4fQ2jgvNgx7uUfBvzXBoCysumQGI3z3yvDJ_Zqkkd725q7yEUDoIzJjRm_mnYh6mW2Vtj67OyiyVJYJ3Md7uwWwsScuG603yNmVfF6K0nCIIfe6L_E-9dpfN8ZCgMA-4wi3Fb_hd2HyySe2XDyR6HF3jx84HDner4lz4UctDe4eYTFA9clVE1Cj5LcE4F6IUAvZZypdUbQZ_cHRPqrKQNcAaCoEi2nYGBu-Q_IsnzNF7EpHvhoKPyK20dGrJA9vK2_Sv5sbAk2inXoW6rlXpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های بومی : زدن بدم زدن ! خودش نترکیده زدن ! ‌ کارخانه پهپاد سازی هم بوده ، ۲ تا کلانتری و کارخونه هم قبلا زده بودن همینجا (حسن آباد فشافویه)
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20460" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQHEn6jfQTL2grhzqaeWzvJ14D6vD-60HRUDQNyi99jB8gu7x_WjNrMGcSQKUUdp25LIfnRYxqYuGSGshLj0AwishKwvMY1zXbB_WCYlMFh84ifwDZiyWrzOgbsQq2cjXmQiuLZd99dTRzMXAq4-lGNM4Yjophvd2suXY4s7BnqAOfKEY1wpyqDw0e7uDoO4rqFsplQNcpQSzz3H-ZBqk4jALwokYhTrvCRz5MNoSwudjluA1nRM4Ku371lkSgT1btFuN74SsdXMFMQ9aUNABxvmtFzON5GSrkM_voNxsP-vRO-7G9pi2IawjvQmXz3bglW7o2ZBW8TL57D7hkwf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرک صنعتی شمس اباد فشافویه توی خیابون گلشن ترکید
گزارش های مردمی تایید نشده :
مورد ۱ :دو کارخانه منفجر شده
مورد ۲ : کلانتری فشافویه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20459" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20458" target="_blank">📅 13:02 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

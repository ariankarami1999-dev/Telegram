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
<img src="https://cdn4.telesco.pe/file/DglKu2MKBPRGxrPo1lOlfAsttA1y2jDYXKZOTmWm1AyQMc6b-GU9AnS_IFJXz0jPoEJEA_xJp07d9YueqW_Fw-KuIKMeg3AGgd8xjSNAfR8imPqCYmQzVvrK9Ta2WrfcjWF-KdBDBQAllJbre9ibXT8iI7kjHSoCFdH79MNeygau35F3qWtddf3aJUfSVh-o1l4KsnRmtPEAkioBP9VMJEpCFUwG7yVQcKIvO5_w7eTykrVBlBRRZsvAJBstjg7RLOpyl4GBJE8M17Cr6tH4sXfPXo11USI_RVrZ8j9ZCl7FNoPH3VaQmbTaW401V272latSiU-OxC3tagkasKvMHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 09:02:39</div>
<hr>

<div class="tg-post" id="msg-682160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ12_5NoHhU4360VxNLfPQ7x2GqPTDG8ClRtzf8aNU5jIvtLn61ckxFyseOsUKUtuPjhERNu_gHHXNWBgyxKi-XxO_k2w0grmS4aw9dK9_2EVa5X9Bzel2QRZ9FDMyYTcAZNc1glZ8mERRP0CusDB89pCaPnmmhY9NuHZfhTKHUuF_hxjCbKm6ghPukqyEh6xB5fYn6j1YKfefXXS-3urVNJhsUGAPjeGEeikVau-CEZ2gpcyWRNCfzJ9zckXfL_Ulpwb4Tz7Mxq6i5iwdsPTgkPeBua1l7SGfGqdc-2vk717tQ89QijgzhSyRym7S77MwGt0bag5FXnzF6_DohVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روغن‌های آغشته به مواد روانگردان به مقصد نرسید
🔹
پلیس فرودگاه امام خمینی(ره) از کشف ۱۹۸۰ گرم روغن آغشته به ماده روانگردان شیشه که داخل چمدان یک مسافر جاسازی شده بود، خبر داد. متهم به مراجع قضایی تحویل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/akhbarefori/682160" target="_blank">📅 08:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف به عراق سفر می‌کند
🔹
قالیباف، رئیس مجلس با هدف گفت‌وگو درباره تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا صبح فردا (چهارشنبه ۲۸ مرداد) در راس یک هیئت بلندپایه پارلمانی عازم عراق خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/682159" target="_blank">📅 08:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ردیابی دو لکه نفتی بزرگ در آب‌های ایران و عمان با ماهواره
🔹
محققان موسسه آب، محیط زیست و سلامت دانشگاه سازمان ملل متحد تصاویر ماهواره‌ای گرفته شده را تجزیه و تحلیل کردند.
🔹
تصاویر ماهواره‌ای نشان می‌دهد که در آب‌های نزدیک جزایر حلانیات عمان، لکه‌ای نفتی با…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/akhbarefori/682158" target="_blank">📅 08:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
بیش از ۷۵۰ هزار متقاضی آزمون‌های سراسری و دانشجو معلم کارت گرفتند.
🔹
حزب‌الله عراق: شرط ما برای هرگونه تفاهم با دولت عراق، خروج نظامیان آمریکایی و ترکیه‌ای است.
🔹
دبیرکل اتحادیه عرب خواستار موضع واحد در مقابل رژیم صهیونیستی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/682157" target="_blank">📅 08:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=BJfheCkK0HdCkIEROZP3cd5WwQfKipNB6-w1nCUauocPrwXzm6o6HG_T17XD2NCYvqiho5wE9KfyHEhcAG7zfbJ_R1YSZmzVKC_atmm9yWLgBVFeVBE5BFQ3EbUd7JyrrKkDcLv6eVlE_rc4Jj5dfwDHEGklTQfuhGCJn1G04KpdEkpnx4aaJFQ1_yO6_y63vk7k4BSgGidMzVokE3B-EA971CBFR6AOb53p3wL_KPphdJWjroJiSShxxzL5QCS4CFI0_kOLlkCaSs_8ogRumG_Sej2SV_jgdTU3P33KUhc3IQhxcgeUtfa_Q_72pjAhws5TTDRcE4ZdVR8q3tlROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=BJfheCkK0HdCkIEROZP3cd5WwQfKipNB6-w1nCUauocPrwXzm6o6HG_T17XD2NCYvqiho5wE9KfyHEhcAG7zfbJ_R1YSZmzVKC_atmm9yWLgBVFeVBE5BFQ3EbUd7JyrrKkDcLv6eVlE_rc4Jj5dfwDHEGklTQfuhGCJn1G04KpdEkpnx4aaJFQ1_yO6_y63vk7k4BSgGidMzVokE3B-EA971CBFR6AOb53p3wL_KPphdJWjroJiSShxxzL5QCS4CFI0_kOLlkCaSs_8ogRumG_Sej2SV_jgdTU3P33KUhc3IQhxcgeUtfa_Q_72pjAhws5TTDRcE4ZdVR8q3tlROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» اینجاست!
🔹
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/682156" target="_blank">📅 08:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df9764dab.mp4?token=heDMmn9z0jCtRyFlxdKPYBAHJTnShsLgu8q1yCp8XSNrcvSkkkYscLMBzFjwoBl3_1Dd2kr_5-p7VTuMhlZUBWRlAaH-8FQ9yGpt-6YZ6GGTxpU7vw1kpoWGT-kuw8u7fjdz753PeQhRdRiIcXcSMxK3NVXQiUEPJgD6JWtnEsx-OXKSIEwwAkY_va8VimJyOuKM3Y7N0kNLRV69xrmHwc5YFy6oKwN368VFexZ0mqTsOfIugeO-eyGsuLw-hKpF2kn5V1sWm-wQWGiVXhkbAcnO4GiMd4XECmShR8TQIZjBeIpVshhkK6pKCvLrhOVF5OnyyjIZJnpzczF9fFHYajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df9764dab.mp4?token=heDMmn9z0jCtRyFlxdKPYBAHJTnShsLgu8q1yCp8XSNrcvSkkkYscLMBzFjwoBl3_1Dd2kr_5-p7VTuMhlZUBWRlAaH-8FQ9yGpt-6YZ6GGTxpU7vw1kpoWGT-kuw8u7fjdz753PeQhRdRiIcXcSMxK3NVXQiUEPJgD6JWtnEsx-OXKSIEwwAkY_va8VimJyOuKM3Y7N0kNLRV69xrmHwc5YFy6oKwN368VFexZ0mqTsOfIugeO-eyGsuLw-hKpF2kn5V1sWm-wQWGiVXhkbAcnO4GiMd4XECmShR8TQIZjBeIpVshhkK6pKCvLrhOVF5OnyyjIZJnpzczF9fFHYajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم افتتاحیه فصل صید ماهی در دریای جنوبی چین
🔹
چین پس از پایان ممنوعیت تابستانی صید، در ۱۶ آگوست فصل ماهیگیری در دریای جنوبی چین را آغاز کرد و ده‌ها هزار کشتی راهی دریا شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/682155" target="_blank">📅 08:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
هشدار هواشناسی: تداوم ۴۸ ساعته گرمای غیرمعمول در سراسر کشور
🔹
کارشناس هواشناسی، از تداوم حداقل ۴۸ ساعته گرمای غیرمعمول در کشور خبر داد. طبق نقشه‌ها، دمای جنوب به ۵۰ و شمال شرق به ۴۰ درجه می‌رسد؛ همچنین رگبار در شمال و وزش باد و گردوخاک در نیمه شرقی پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/682154" target="_blank">📅 08:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس سازمان پژوهش آموزشی از اصلاح برخی کتب درسی از جمله مطالعات اجتماعی، تاریخ و دینی پس از شهادت رهبر شهید انقلاب خبر داد.
🔹
گاز مجموعه ورزشی شیرودی به دلیل بدهی سنگین قطع شد.
🔹
تیراندازی دانش‌آموز کلاس هفتمی در فیلیپین، ۲ کشته و ۹ زخمی برجای گذاشت.
🔹
تلگراف: روسیه دست‌کم ۱۰ پایگاه پهپادی نزدیک بخش شرقی ناتو ساخته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/682152" target="_blank">📅 08:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8064346f28.mp4?token=Icfxmpz_uJGio4HJmB9cOSbN5rLf1OEwpJ5f9SSbORDWTLXWyBicgYmSEMwz9MpIm1-SCKv2utiijnlcHnK5_8fLHEx-TQi1LnD9vnHvuSUgpDKDmUF7QgJ-hLgYemfDH9Ttduh91EZCtDMsQng3EU08gBqCl3TbriJk4CTjoLl5vEIi6XtM2Xf37-oktNBMw7O12RjUK_WUJxACxi6GfGzT7KyCP-8ldeBhO9l4zPCLAOZP7oOQyBDKuar8xTe99fzFxYT2o0F-N9uPiWmBXV_pkJ3OxI1uD56LSFq5-qn7gqzkg8zbTbrB5Sc3TmJtI1APqXGr1xQfFrjG-kT3sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8064346f28.mp4?token=Icfxmpz_uJGio4HJmB9cOSbN5rLf1OEwpJ5f9SSbORDWTLXWyBicgYmSEMwz9MpIm1-SCKv2utiijnlcHnK5_8fLHEx-TQi1LnD9vnHvuSUgpDKDmUF7QgJ-hLgYemfDH9Ttduh91EZCtDMsQng3EU08gBqCl3TbriJk4CTjoLl5vEIi6XtM2Xf37-oktNBMw7O12RjUK_WUJxACxi6GfGzT7KyCP-8ldeBhO9l4zPCLAOZP7oOQyBDKuar8xTe99fzFxYT2o0F-N9uPiWmBXV_pkJ3OxI1uD56LSFq5-qn7gqzkg8zbTbrB5Sc3TmJtI1APqXGr1xQfFrjG-kT3sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ حرکت ساده برای اصلاح فرم بدن و صاف ایستادن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/682151" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
محبوبیت ترامپ به پایین‌ترین سطح رسید، فقط ۳۳ درصد
🔹
بر اساس نظرسنجی رویترز - ایپسوس، اکثریت قریب به اتفاق آمریکایی‌ها نگران طولانی شدن جنگ (تجاوزکارانه) آمریکا علیه ایران هستند.
🔹
فقط ۳۳ درصد از شرکت کنندگان در این نظرسنجی چهار روزه عملکرد ترامپ در کاخ سفید را تأیید می‌کنند، در حالی که ۶۷ درصد از دونالد ترامپ راضی نیستند./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/682150" target="_blank">📅 07:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی پس از انفجار یک مخزن سوخت در سلیمانیه عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682149" target="_blank">📅 07:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بی‌برقی چهار روزه ناوشکن نیروی دریایی آمریکا در دریای چین
🔹
بر اساس گزارش رسانه‌های آمریکایی، ناوشکن «یواس‌اس بنفولد» ماه گذشته به دلیل نقص فنی به مدت چهار روز در دریای چین جنوبی بدون برق ماند.
🔹
قطع برق باعث شد ملوانان از خدمات آشپزخانه، توالت و تهویه مطبوع محروم شوند و آب آشامیدنی داخل کشتی نیز تحت تأثیر قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682148" target="_blank">📅 07:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مجلس امروز صحن علنی برگزار خواهد کرد؛ عملکرد دولت در اجرای طرح کالابرگ و نحوه حمایت از معیشت خانوارها بررسی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/682147" target="_blank">📅 07:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682146">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e116f039a2.mp4?token=vvdqd-PnKA09OEZ8fgQF7iPFK3EAUx6_Qz3nwJf92pvbGJilrmGcU7SytkqLplyMSbOgtORMQoo2h7S60FXmLvJ3vP0ZAkTEWTvJjey4e8w5Xu5wlDRQg6eIOhOF8uYzVTDmvGYyjKS_Zv65NjHaqx4aJ4ahPbX7knCWJQnYLwQGKnfoXCUgwRyRjdIfNLHvJjBdcXnIR6OYWu5XFj4qahtA3D-6WH0_1wqSIDg3Jgq2-fP4jsDyi9JF4xH_uQTm5rHypnHdrIADndCCZlVGTjjlggTTcI0jyUw_x4_lkuJtAzQX28oFYmFEEQEi5CDe6ofsz-3f4Ejddfws7AEe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e116f039a2.mp4?token=vvdqd-PnKA09OEZ8fgQF7iPFK3EAUx6_Qz3nwJf92pvbGJilrmGcU7SytkqLplyMSbOgtORMQoo2h7S60FXmLvJ3vP0ZAkTEWTvJjey4e8w5Xu5wlDRQg6eIOhOF8uYzVTDmvGYyjKS_Zv65NjHaqx4aJ4ahPbX7knCWJQnYLwQGKnfoXCUgwRyRjdIfNLHvJjBdcXnIR6OYWu5XFj4qahtA3D-6WH0_1wqSIDg3Jgq2-fP4jsDyi9JF4xH_uQTm5rHypnHdrIADndCCZlVGTjjlggTTcI0jyUw_x4_lkuJtAzQX28oFYmFEEQEi5CDe6ofsz-3f4Ejddfws7AEe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی پس از انفجار یک مخزن سوخت در سلیمانیه عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/682146" target="_blank">📅 07:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682145">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0CNNnYUUTfXSHpmF2jCgoQn1A44Lj2vfCOXWfkVc8J1ejqmJU7Pqy7tQSgCdWtFjSMvmDJdDeR2qk6ylhcuZSU6QQLQH4r8MUn-gv0woZ-tGSn6j6GRkL61XqQUT71YhcTqOEcanbS0otdHzaNtyMs9LPy9w2aPTQTVeCRSjwa44uOlufIm19Je1J-ZIkGmMZeXSPov2tt9w8pxAL0Y8U2Go8t3MOzPIcTkK5A8gXmCjpixl9tVMtvw4hFVvRDB9MiAs4_RlZZ_zhXrRqWIJKNGIF2f0XfoZBp4BJy4yj1pmzZp4sXZ2JJLO5iEuv44N6pSjTH-NmPeyBrBTI4-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟  ترامپ:
🔹
فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/682145" target="_blank">📅 07:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شروط ۴گانه «کتائب حزب‌الله» برای همکاری با دولت عراق
🔹
خروج کامل نیروهای دشمن آمریکایی از زمین و آسمان عراق
🔹
اطمینان از عدم بازگشت نیروهای دشمن آمریکایی و رهایی از تصمیمات سیاسی و اقتصادی از هژمونی آمریکا
🔹
حذف نیروهای ترکیه که شمال عراق را اشغال کرده‌اند
🔹
منحل شدن نیروهای پیشمرگه، زیرا آنها مسلح‌ترین شبه نظامیان و خطرناکترین برای وحدت عراق هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/682144" target="_blank">📅 07:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
احتمال زمین‌گیر شدن ناوهای هواپیمابر آمریکایی در تعمیرگاه
🔹
«برایان کلارک» مدیر مرکز طراحی و فناوری دفاعی در اندیشکده «هادسون» هشدار داد که عدم آمادگی و برنامه‌ریزی پنتاگون برای جنگ با ایران، ناوهای هواپیمابر را در تنها دو کارخانه تعمیر و نگهداری آنها زمین‌گیر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/682143" target="_blank">📅 07:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQhzuTg9r-t9lNfcB-WUg47WbBCpT0dR92PsDPEAKWxWWD8oYYCcRjlUz1xPs6Z3JeYXc0u-HclAdZrDomGAyCt5nuRn2O308MXk7Ae8nYuRJLPIg35QS9BPqGgruOn3bdVKDDwYlhIFZER1cOGL6RCZy_DQH0sjMtNirTy-d5rLwEpyvY5L7WfFn8Lowe0JP1D3QYfs4tMrjq867L28qSIlzGUQkgKNXNuWmHFXnU8ewezZG4dsg5PJIE_OFD3xg_2xmNYkpq7-Yq8OEhineTK0pf2G8UkVlbkp70HVySDc6Td71sFxfZ5fvx3CkfiDCqC9YfQK_JZzxIvRsgoXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۷ مرداد ماه
۵ ربیع‌الأول ‌۱۴۴۸
۱۸ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/682142" target="_blank">📅 07:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWD5BRLppk6VGAJ2F4Py8NHax24VySYRSEOLj7iWH9JwxxW1reEl6OD51809RSkYpUHbKJKX8Iw77Qf65uU3VyumoFsE7V4iKfby7_240elyn2PCeNMo79y7F77CL917ZH762M0DEhnltiLezyi7BFMcgqdfiJxH5GYUd2jk8bM9l8LS6KrIZnyRGmqEPPGLmepfYPEzO1yqppB3VmQ5Qos0kcLhPzNhrE7vDAQqBWFh1RZVzwpoBmOhvHqhiSwigTo1lxnYNo8iNBWX45vQdTbigi2GpQYQK_npOSyHdItbJty6kyVeKnRevYRsnu7s2eCdI_wguzOhT6OHz9QonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی بزرگ ارکیده شاپ شروع شد!
🎉
این بار خرید از ارکیده شاپ می‌تونه براتون فقط به معنی خرید نباشه؛
شانس برنده شدن ۳ جایزه جذاب
رو هم دارید!
😍
🎁
🏆
جوایز قرعه‌کشی:
😍
👇
🥇
کرلی شیگلم | ۹,۵۰۰,۰۰۰ تومان
🥈
شیور صورت و بدن شیگلم | ۸,۳۰۰,۰۰۰ تومان
🥉
سشوار روونتا | ۷,۰۰۰,۰۰۰ تومان
🛍️
خرید کنید و شانس خودتون رو امتحان کنید؛ شاید برنده این ماه شما باشید!
💜
📌
ارکیده شاپ | انتخاب مطمئن برای خانه و آشپزخانه
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/682141" target="_blank">📅 07:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حمله جنگنده‌های رژیم صهیونیستی به فرودگاه ادلب سوریه
🔹
منابع خبری از انجام چهار حمله هوایی به فرودگاه نظامی ابوالظهور در حومه شرقی ادلب سوریه خبر دادند.
🔹
برخی گزارش‌ها حاکی از آن است که نیروهای ترکیه در این فرودگاه مستقر هستند و حملات، باند فرودگاه نظامی را هدف قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/682140" target="_blank">📅 07:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682139" target="_blank">📅 06:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682138">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdVO_r8X9P0I6ZUkTEZSTztFT1-xiNef8BStcoXGAK-VQwO2-MYGwGhPH2ETHYE0JlEQ_bDSemWoiDi2WFqwUONqeTqdCk_8qc3wSXpvpnHGwnSLYIhB9aMMtVFShsAwAHKVe6qaDw-dPcDqVcOOF6FI-xE6lUaxsmenZGeqSn9mRuuV8brxXJBh1N32SXd21EFF9Oqf1P8QWN0Wn_ajGt5EXs-l6gLD5IzU-m-m3WIv_9Y7Nm3xXcHkAh5ZRSihIWkGxeQpEpri9CGBFSwZ36tP-xgg1yYtVl006cahnmLi0qJDRK6dDdFI404eDz9YXv4jxYa87k9UgaxiNxzhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/682138" target="_blank">📅 06:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru5EKm0er9KJ3553A2V7fa2dmqDAjzfWDe1Rlr_--By02llkNj9vaF2KJR2ryvzb6le-pqwPsM3W-jpIk1xwYLqhNl1ZK6gxVvTtH6oMloN4qAWlKunC9dCpDZRZCWCbJW7hAksEemyjeV4as4xBCYx2Va3pAFLA_dy5xuuBeGtZr6JavIoft6A1NdJD998-mCajEHsvk7QPBMjpH6rBkUzlfL6SE9HIfYUzLsu4INtKOcikF7p_UR9M1y-DuzRkYh6VeG8tsF_apsHPbgWsh35LhwvarGvfqRqQ-Dp80kPoHlR2xDrXOBw5VJ7egbiL25wW3qiAl1WGXqAVb83NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ با عکس کیم جونگ اون: هی دونالد، ما رفیقیم... مگه نه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/682136" target="_blank">📅 01:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تماس تلفنی اردوغان با ترامپ و رایزنی درباره ایران و توافق ترکیه، عربستان و پاکستان
🔹
اردوغان، اهمیت  ادامه گفتگو با ایران را به ترامپ مورد تاکید قرار داد.
🔹
رئیس جمهور ترکیه همچنین با ترامپ درباره توافق عربستان، ترکیه و پاکستان گفتگو کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/682135" target="_blank">📅 01:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrbAd7TmmnmORmNSXWRpIYNn4qIr9LRi37NSawP6wUSsk2xmbchRvMA-irlRxxz_vdng55nQ1Y3_9N3qeI-wylzyojRwDJpQlBSy_zCTQuH9oiHy5D-cCjDMBrZHJBDSQBaotTnFM-hTVBJvl1z078oUoxz3CTworsfSHkh0z_wWXjpwNKwrk7n26VZvP29LFxV7Qy9SNFbou3-1ZY41FtTPtqJm9pFbvxNPKEyyYwLmoiwAKK0AAhjbXekcpUbidH1rVBMRAQHcpZiqo7qZMC1ZPKW224ECNz0RzMt3xGrTty4WUWeGglc59vbsW7vEpkWTgK5wcmopTchRwSuTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به نفتکش یونانی پس از بارگیری نفت روسیه در دریای سیاه
🔹
بر اساس گزارش های منتشر شده،‌ یک نفتکش یونانی پس از بارگیری محموله نفت روسیه در دریای سیاه مورد حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/682134" target="_blank">📅 01:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682133">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b74ba770f.mp4?token=nGSVxeY1Oli0e5NYTabXLJP0niz2fcjd-N9cNabLPkVfrYpSNf2NTuF2Y7uD1vyt0X3RUGSA3nNT6ERELr2Zo0Q2yMkf-zoWdlIxGnKxlMRd7yDVIFqiYuLsqW6ixOtni0ZgT00cX_Y3YPMGoyVmDYAnP33v0Yg_6HCW_O6ZFLr2PRwUXwgWD5xfFdrnER_GzebwnRojAk8E_nJs8lnGSK1OdFAyduNjn0zgMYUZAit-DxdzspIvbjL8BGGwmIClSJYHrbE08D_2WZVy-Nu4mEZgzcOHhdr5Z5D5tlo2nEGnBLdR7ZqRy0t6pNvRQB44JiwQE12EKcZ0Irje0v5ITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b74ba770f.mp4?token=nGSVxeY1Oli0e5NYTabXLJP0niz2fcjd-N9cNabLPkVfrYpSNf2NTuF2Y7uD1vyt0X3RUGSA3nNT6ERELr2Zo0Q2yMkf-zoWdlIxGnKxlMRd7yDVIFqiYuLsqW6ixOtni0ZgT00cX_Y3YPMGoyVmDYAnP33v0Yg_6HCW_O6ZFLr2PRwUXwgWD5xfFdrnER_GzebwnRojAk8E_nJs8lnGSK1OdFAyduNjn0zgMYUZAit-DxdzspIvbjL8BGGwmIClSJYHrbE08D_2WZVy-Nu4mEZgzcOHhdr5Z5D5tlo2nEGnBLdR7ZqRy0t6pNvRQB44JiwQE12EKcZ0Irje0v5ITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مخزن سوخت در منطقه کردستان عراق
🔹
رسانه‌های عراقی بامداد سه‌شنبه تصاویری از آتش‌سوزی ناشی از انفجار یک مخزن سوخت در «سلیمانیه» منتشر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/682133" target="_blank">📅 01:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682132">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vozNR94ns3lXc-LpI3stJp4PjobtaD0VVUx066BTbKOX36QIcwnB44tCjYk-aqhVx_NxWaXseo-m8yp8WGy4YaajFqHXHSZJbWC73_MQRJXC1EWZ7A-3ZGVaqcwPCM20bvHDnASvob1wtCbsrKnih6WsLx9rHnQ9m8hru54C4J_vgmFYbgDQdIANIS7Ut03SPrY8UZCpMspFuTYbHWPqXa51bvflSjic-2Sqm-JmAc6dKzbvSqN02uA8Iip7in-ZM54CwbwIIono9pR_pIcxt07EXPTB_8odai8_u_iNqIe3UZJjDSEC3gd4KZk_55GNrW90ZKWxM_M0UKlknYNA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشتی حامل سلاح عربستان در باب‌المندب منفجر شد
🔹
یک فروند کشتی باری با پرچم اندونزی در منطقۀ راهبردی باب‌المندب، واقع در جنوب یمن مورد حمله قرار گرفت.
🔹
این حمله در حالی رخ داد که کشتی مذکور در همان اسکله‌ای پهلو گرفته بود که پیشتر نیز هدف حملات مشابه یمنی‌ها قرار گرفته بود.
🔹
یمن اعلام کرد این شناور حامل تجهیزات و محموله‌های نظامی متعلق به عربستان سعودی بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682132" target="_blank">📅 01:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682131">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
مقام مطلع نظامی: شبکه لجستیک تجاری پشتیبان عملیات آمریکا زیر رصد است؛ از شرکت و مالک کشتی تا اپراتور و خدمات بندری
🔹
تأمین سوخت، مهمات و تجهیزات جنگی آمریکا در جنگ با ایران در پوشش قرارداد تجاری با اقدامات مقابله‌ای و بازدارنده متناسب مواجه خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/682131" target="_blank">📅 01:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682130">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
کنفدراسیون فوتبال آسیا: مهلت استقلال برای معرفی ورزشگاه میزبانی در رقابت‌های لیگ نخبگان به پایان رسیده و ای‌اف‌سی تکلیف استادیوم مسابقات باشگاه را مشخص می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682130" target="_blank">📅 00:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682129">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ChHloVO6zTY-b3CS4lymrnAxY_ZvyHpVQoP4TRrFKfBqyCI55lsJnD_8FdavfVn64b6_5Ue74LmLwwQigfWc0UqZDL3VzgBDEQgvTaK6WoVGcrZ-myNeGsfNOX1MJHRhF0KRbqyckI8YGkZLjKtmxJlUAxKSttxExIGP2zM5VEl7nrpYzDTJQxKJoXtWFZ8d1puyM9He9DRcfjkqwu3_I0dNcpbRLA4oZIXmkMBvS9qJr0wujSHDfC36VyJJIPNU7MjLWv7QR2SgSdDf4uVoi-E9G3gDqJcFf3KnZB0X5Ux3NuuDP_jjtWxF44zKIPoXyvp-ZSTu1HsB3nzSsERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
﻿
اینجا اسپانیا یا پرتغال نیست، اینجا لاهیجان عروس گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/682129" target="_blank">📅 00:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682128">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رئیس دفتر سیاسی حماس، رهبران و نمایندگان گروه‌های فلسطینی، اسرائیل را مسئول توقف توافق غزه به دلیل پشت پا زدن به توافقات دانستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/682128" target="_blank">📅 00:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4pliuGLUWS8lEce0gfp5-dt_S4BNWQJNWsxg36ASLdIYqmwVItCgXqernxl7rm4-KE0Qyp72N3MfN4vJfQTJt5mpyQHFYG2LYt4Wf-uwr8vGm5IIdAgUtp_67S6vvQ8TS9xFuxNleUy1Ro_j4H3YnMnwvc3PivvzPDaeUrTlRJYslIhbf2JX70dfADkJ2_Tv_A0Fqm_ibUo-OOAja2NqHKzMhVWgU0E9054CPYT9t22I_Q6k7j6CeV9ZEc4cjLLxfQmwW4ChcBxdaTm3KbvxEZlYIW9z0xIeiMAb2K8MqkRg5AWdRxWNa2SuNWeRXMvHInliVUCAsFirNEyMsrK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌خط رهبر شهید بر صفحۀ اول قرآنی که هدیه داده بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/682127" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682126">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۸ درصد دانش‌آموزان در مدارس دولتی درس می‌خوانند و ۱۲ درصد در مدارس غیردولتی
عبدالوحید فیاضی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
بیش از ۸۸ درصد دانش‌آموزان در مدارس دولتی و ۱۲ درصد دانش‌آموزان در مدارس غیردولتی تحصیل می‌کنند.
🔹
دریافت شهریه در هر پایه‌ای از مدارس دولتی، به‌ویژه برای پایه اول ابتدایی، کاملا غیرقانونی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/682126" target="_blank">📅 00:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682125">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر راه: ۱۰۰ فروند از هواپیما‌های ما در جنگ آسیب دیدند؛ آنهایی که عملیاتی بودند و انهدام کامل شدند، ۸ فروند بودند
🔹
ادارات فارس به علت مدیریت مصرف انرژی چهارشنبه دورکار هستند
🔹
صید ماهی شیر جنوب برای ۲ ماه ممنوع شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/682125" target="_blank">📅 00:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXdrlx_zubFDGnpe1GnKEVdOCqF1nhLP3lr2Zu3JZnBzBphqCGUuxzmfg8wf_uv-SIbqdo_um9SwqUYXvf6lMbvff7DdbEvj_kov9oE1jrXtFxJvuZ1z4490bxc4QIZsgVpCfY3Qkj1n2gI0kFQE10T2Hd4eNqJJ_7sAEVRELv0T26EaC_oCh07d2jCsOzN3V5htg9MVNykRnYl-5hDxw8JDIQeKG9av_3G2KK3ECVkyTmxqGjxbEZoXEywXodsFFhD4DtNJ6Bj0CvcuKrz1va3m2VIs4wpMKC8mgKsJunDkmVesj-hTPw4f0FhvNyzy71Y1IAJ5amywIprCHkcjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرر ۴.۳ میلیارد دلاری شرکت‌های هواپیمایی خاورمیانه از جنگ ایران
میدل‌ایست‌ای:
🔹
چشم‌انداز ماه ژوئن انجمن بین‌المللی حمل‌ونقل هوایی (یاتا) تخمین زده که شرکت‌های هواپیمایی فعال در خاورمیانه از جنگ ایران ۴.۳ میلیارد دلار ضرر خواهند کرد.
🔹
تیم کلارک، مدیرعامل امارات گفت که هواپیماهای او با سه چهارم ظرفیت خود پرواز می‌کنند.
🔹
جدیدترین بولتن آژانس ایمنی هوانوردی اتحادیه اروپا به اپراتورها توصیه می‌کند که «تا ۳۱ آگوست ۲۰۲۶ از حریم هوایی بحرین، کویت، قطر، امارات متحده عربی و بخشی از خلیج عمان اجتناب کنند»./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/682124" target="_blank">📅 00:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUSgmwWUWmKn5dUrNkVor5LrR7hNHLyLdF2FEyEZVbr7J3xALEqvrAq_hYr8uiRPdEm_WrQle3zbH92kx5ksEs5PQo3aIY9mESk-gw_F1HGfYiNnqzT6VBsc24tm5PwPDuMiEZ3Fb4pPKNcXlF5JDW3rOgQvbd0s2Pi52wiAQsyFmrJdHhvKZAN-lApjUI5SFamZS8sg3tDAgasEW4bgaXlWLcTguaY1-slXvWjrAdrQyR8MDDUZulpgdAr4Wd61JzZ1rIP4XPkkOlkqPePix1domI_9FophcIaS_g25fGvs2nwW9eXX8EnB3_I0xwbymsS984jpx8Z-9X4uKfEzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/682122" target="_blank">📅 00:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUgHBB1A3uVSd21j8WLwT0DyD8hizrg9EwpD15nUkySh3EifjudtB6GPv5P_i0u-gSgyNd1Kln_n1uTqK9vAU6OBnyiSRofVRG-fvXxY0yURka4NswApNXznLOPFcYhKOJkDmpfKHccMbIrZVlyLRjBRAP1ZNJ2SV2l9dJ1S1nbsBuAJLMILEhctsiMiOSruKMOJdQqM3hBHl5OcRJY_As3EjQMVPB4FjAYRROcbsHQF0tq0i0fqoitZhGFdopiBkHuRTuLwiDS_9mGn3sfzIBsqJ6JhCOJARnmKJD6dokU35HtgKH4uy0Imeg3nvm1WZEpxizUehtWVmiFc3rFuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به عملیات پرچم دروغین در کردستان عراق؛ دوستان کرد ما، هوشیار باشند
🔹
هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند. دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/682121" target="_blank">📅 23:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBv8NuxD6qR2YNUfV0eP0Be8LhnVwhThTyTi2aoxRifizMD5Fycg0yHQo-NcUwdvB6fvEGdoeZbE5EyqsODrAqVgA9-kkbB-yEDYD0CRKNkAOeRyx4dDYlgUczwV4ZiXn5udvy4o8-gXBwWrEC_WJ1-8Azu4z0OCceFA0_nbzVsYtaquHPpQlsdjEpJGuxG872vxJAfhp7Wm2iGst9i17kPLbzBsPMojQI_qwoy08hCAN_zgvJ7jA7r9oe8J7aVJUXWsywhg4_8Rs4NROP-5fZMWXjngDAQVo9YqEPrskjcq8VtLV1C3nT-bR2iYfKa7KlQaL5wjOiQ6leKhBjFaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft_sAVJVyVT-YQRZ9iR_PVMpPPlv-NhGSwMmfo5ZcVUK3WsoHUSVvZ6TweE8kWL0mrtHcmy8t-M2Grj9QXFkmKqvwgCrCJw3JXbg3xOZydeZUxgv7izlrndNIuLsdN49_XrgNKmPJl-hu9cTCL-v8VxbD0vsCgMalm-T61FxNPfSzDu1_DCTb3_Seq_ERiKWPuI-fNAgYwv_0k5-KptiX6kXM3a6_i_ku0pCbPAULvLg9XYONbd_3jaAjRgKwi27TtIODBv28mXDTRyBkEFU_MiYIgpbi_-noCTeoLFSFFwPJL6lMQwyktMkJWaOUMcE1whE1S8z54H-zrUQWrjETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntMSAFNbcHvvjZDAYcw2_vC6c8vsGvNlM7I0u5NWP5yIciFlBabp82NvhgqjCiQid0W3I0AghehWgxQ4AnVZ14D1E-37EKMe_gjqK2pWnt9XCyjykKOn2bfupz3UkHTHcVTCxKtQBDV7yDKJEJr7ysurnDAX6WqZwR0SOwVF0Pl239yHbPDUtAh6S2D9t0J9cviBb0JqZl3lAO-JFcfNZeqSa78wAl0fEoQjhxOx0ZTl6zvY0h5P3sC5CoaeDIt5fHcOnaStVO26D1-Ml-JwvDUZ6T4Ml9dTJuuIet5N62GgilTzia_oLIAySUncdFLShm5kZt9XdYTM_-P2zEWEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
هر قطره آب ارزشمند است. با کاهش زمان استحمام و رعایت الگوی صحیح مصرف، می‌توانیم در حفظ منابع ملی سهمی مؤثر داشته باشیم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682118" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
پاکستان بار دیگر نسبت به هرگونه ماجراجویی نظامی به هند هشدار داد
🔹
ارتش پاکستان با استناد به آنچه دستاورد غیرقابل انکار خود در نبرد ۴ روزه با هند در اردیبهشت سال گذشته می خواند، به دهلی‌نو هشدار داد ‌که هرگونه ماجراجویی نظامی در آینده با پاسخ قاطع و نامتناسب پاکستان مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/682117" target="_blank">📅 23:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf722c295.mp4?token=rOJewH4tv41ldXGJJx393lZNhyFioLNFAjZwKqcJJvtwDZhiE4a5uhUXWOtrafTkfnGfiHSCOkFbfLoZblexigzm0GK3ZsutScfJVYLIQEwAGjR13jR4pFQFs3sxuEsFXSSClgt9VOEV8XF98uqUWg8l7Nl-iadKN2Pwu6WAZ3zEFP5PEY3E2b4pEAk-K3fn6fYfBW36JDH_IxY1cdlhKR35NImfYRiEShoWgCLJET4nX4vZY-5F3rLH-UHX9r-ehJV1-e-lVSH6vqa64H4lec-vEIQS30rX_oPPKjxPEpqwo-W2fJxa2oLZgT8nUyS-Zg7-tWHyos5JlVFP2uG9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf722c295.mp4?token=rOJewH4tv41ldXGJJx393lZNhyFioLNFAjZwKqcJJvtwDZhiE4a5uhUXWOtrafTkfnGfiHSCOkFbfLoZblexigzm0GK3ZsutScfJVYLIQEwAGjR13jR4pFQFs3sxuEsFXSSClgt9VOEV8XF98uqUWg8l7Nl-iadKN2Pwu6WAZ3zEFP5PEY3E2b4pEAk-K3fn6fYfBW36JDH_IxY1cdlhKR35NImfYRiEShoWgCLJET4nX4vZY-5F3rLH-UHX9r-ehJV1-e-lVSH6vqa64H4lec-vEIQS30rX_oPPKjxPEpqwo-W2fJxa2oLZgT8nUyS-Zg7-tWHyos5JlVFP2uG9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش کاربردی برای تمیز کردن کثیف‌ترین کاشی‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/682116" target="_blank">📅 23:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
بورس در آستانه فتح قله ۶ میلیونی
🔹
در بازار سرمایه امروز، ۹۰ درصد نمادها در محدوده مثبت قرار گرفتند و ۵۷ درصد نمادها با صف خرید بسته شدند.
🔹
هم‌زمان، سهامداران حقیقی حدود ۱.۹ همت از صندوق‌های درآمد ثابت خارج کردند و در مجموع ۵.۲ همت نقدینگی به بازار تزریق شد.
🔹
ارزش معاملات خرد نیز به ۲۷ همت رسید. تداوم این روند می‌تواند شاخص کل را در معاملات فردا به سمت مرز ۶ میلیون واحد هدایت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682115" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeJ_WujvAREa5EVa6n68w-oxtUVNgDlMNJqYXVFrcKpw3AOZNKk1Gf-VwLJjNoiDnlKDMbbrczi8XCF4iTXLCecE3n68cHzzGlCv5P9BaTVMnWyjNmFRkiSGo1JDEvDUSoh_bSZOhayc2SUCTlnShBNpXEAwvuEnBVTNOgqVdkGtUMUMxRYj8XfcYdNFwL6wjFl6sAzhakGh_j7AeocZ8umvuDGfpffWKfU9llTRu1uqaMAk_ltFjt1EuCfDkn_T1Rj5n5BMDlbEtROPEq5j3dfjTZUxaQCS4Whu3n4pXlEkiALzf5wrBniHLgId7D4hLbqrfKqAUyODpYnU6bG-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب قاطع پسر ربیعی:خبر خرید ۳هزار میلیاردی شمش فولاد کاملاً کذب است/ پس از شکایت رأی دادگاه را منتشر میکنیم
🔹
صالح ربیعی، فرزند دستیار اجتماعی رئیس‌جمهور، اتهامات مطرح‌شده درباره خرید شمش فولادی از شرکت چادرملو توسط شرکت «تهران تینو» را ادعایی بی‌اساس خواند و آن را تکذیب کرد.
🔹
این ادعا توسط عبدالرضا داوری در شبکه ایکس مطرح و وی مدعی شده است که فرزندان علی ربیعی با خرید اقساطی شمش فولاد به مبلغ ۳ هزار میلیارد تومان، باعث وارد شدن زیان ۸ هزار میلیارد تومانی به سهامداران چادرملو شده‌اند.
🔹
صالح ربیعی صراحتا اعلام کرد: «این معامله اصلاً وجود نداشته شکایت میکنم، رأی دادگاه هر چه شد منتشر میکنم.»
🔹
او در ادامه با اشاره به منبع این خبر، آن را اقدامی هماهنگ از سوی جریانات خاص دانست و نوشت: «اونهایی که نخ این آدم رو از بالا می‌چرخونن و امثال این براشون خبرکشی میکنند، از چین تا گعده‌های خودسر و باندهای فاسد، هر وقت اسم علی ربیعی وسط بوده منافع شون رو در خطر دیدند، بار اول نیست.»
🔹
بر اساس این واکنش، فرزندان ربیعی قصد دارند از طریق مراجع قضایی این موضوع را پیگیری کرده و رأی دادگاه را برای شفاف‌سازی منتشر کنند.
🔹
روابط عمومی شرکت چادرملو نیز امروز ادعاهای مطرح‌شده را تکذیب و از پیگیری قضایی منتشرکنندگان این ادعای کذب خبر داد.
🔹
پیش‌تر نیز علی ربیعی در موارد مشابه، هرگونه سوءاستفاده اقتصادی توسط فرزندانش را رد کرده بود.</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/682114" target="_blank">📅 23:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c6698ce2.mp4?token=sSbHIJBrVQQHi5QPLyMMQSn_tLWL0ZcKTkETd0PrK5U7A6gmoH2dEkAJ7M9TxwP0cFttiLrm8e9Gx9UYm5b_HpzIIMXDRGRzSdTUa8UydMASsV-Yqi3k1PaPEqMgwNlxDFKYCQfMunkU-5VBAE7L3AggM-9jnEFXhwPqoJjskDWOlGivhamU3vl0NvH8fCas9n2d7VYgn2ZXRHsXJKW0Wrj0m6pdPOeLOsj_TgC3Z87Ta2cmmikj74OFC30qk5sVla7SeE-8fpD9k41JFe9VBeyphRypIQoF-KnTdyZdeH_0m8X2IgbveSjUk3vGaCyzegbOtUYaXMvTiOPNWtV0lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c6698ce2.mp4?token=sSbHIJBrVQQHi5QPLyMMQSn_tLWL0ZcKTkETd0PrK5U7A6gmoH2dEkAJ7M9TxwP0cFttiLrm8e9Gx9UYm5b_HpzIIMXDRGRzSdTUa8UydMASsV-Yqi3k1PaPEqMgwNlxDFKYCQfMunkU-5VBAE7L3AggM-9jnEFXhwPqoJjskDWOlGivhamU3vl0NvH8fCas9n2d7VYgn2ZXRHsXJKW0Wrj0m6pdPOeLOsj_TgC3Z87Ta2cmmikj74OFC30qk5sVla7SeE-8fpD9k41JFe9VBeyphRypIQoF-KnTdyZdeH_0m8X2IgbveSjUk3vGaCyzegbOtUYaXMvTiOPNWtV0lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تا حالا زیادی صبر کرده‌ایم، لازم شود از NPT خارج می‌شویم و خودتان می‌دانید این یعنی چه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/682113" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رئیس اندیشگاه بیانیه گام دوم: رهبر شهید، هدف انقلاب را تمدن نوین اسلامی می‌دانست؛ تمدنی که زمینه‌ساز ظهور خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682112" target="_blank">📅 23:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f77b99b95.mp4?token=UzBpmxsTGBWTxKcPw59P8gde42_jb6RKpvRWKXvGOEBE2kLZvdcbxngjXllE8lEx1SOwS_5NS8hdqMVczkhS54jekTueKCQLJpm1mNA6qCaQJ3hbrHWSToACRt1nopL9vLE8axIaWmDTZA77i9H6E9bDr3AzUVaqLzIyAKiIT1Sre_4e6cwdOoZcui0YwMui-jFF7_EszX3zoo6HJEd6cdvdwvrdmwArWFgRLKECmTZLvF7gYGXTB_HQ4ndeRPsRj0ZB0t5PKBWrPXppTtqL3EU9Sh0yFwS3_ZB9dl2TH77Ki73Se0L264_mftf-uHMp5jjAGiV9b1Xh9VtYOJLN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f77b99b95.mp4?token=UzBpmxsTGBWTxKcPw59P8gde42_jb6RKpvRWKXvGOEBE2kLZvdcbxngjXllE8lEx1SOwS_5NS8hdqMVczkhS54jekTueKCQLJpm1mNA6qCaQJ3hbrHWSToACRt1nopL9vLE8axIaWmDTZA77i9H6E9bDr3AzUVaqLzIyAKiIT1Sre_4e6cwdOoZcui0YwMui-jFF7_EszX3zoo6HJEd6cdvdwvrdmwArWFgRLKECmTZLvF7gYGXTB_HQ4ndeRPsRj0ZB0t5PKBWrPXppTtqL3EU9Sh0yFwS3_ZB9dl2TH77Ki73Se0L264_mftf-uHMp5jjAGiV9b1Xh9VtYOJLN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این قانون مدیریت پول رو یکبار برای همیشه یاد بگیر
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/682111" target="_blank">📅 23:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uEFawcvUUI1wQ6QhvnLXDxUwy1WKPjmrIWtZZujR-YxeDhPJcabkWw1qgw8hZm5CL-QzpnLaOaA047HsUi1XkVO5WgavWFXZQzYAbqC6yOiNCVef6GOY_-sl-60x6ix7AZDi5gS_ux62I7YP-7m5MqFIEE8CNWSsxMIiEIKB1xHyZAlo7IpvplCI82y4juvlwl_584GXG8Pova3dWV5lzEAQQcjCiavRgqWlheXcEXKgFxcHG58PjRQG3fWPWeEhSlC0If8beEQC9U1BT1aRtjEHhbDLNAV4RjYonreLwOhT68OGr2xvp9tlRDZ1i71nZl1rKyTHUSTOpyTdWDfmFzfPHWykEtlZrIrnFPs5Ff_X9ZRm6qV7TXD1Kw-RBuA4EmhSNEZWb3puqgYs8XPXPo2_Tw8_UH9snzVfiKmkLiwRTnMymH-HXCAuX2HiW5k44gHbVJqXnQVYeZ2Ky0O6YXXuh0K5zzWgLqqYtiyQx6PhnYaKuGhmukzVxQp_nFmhKq08gDIs6pq8kFIKEqNqm7OrL0VB_OwApEv1vLgGtdECOMiOQqjtL6eMmc8OValLwZGBzei20W_iSmsiMPHdxgr3AVkEjEZUUZIjj33NSWnpcLNYrK0vFRZnAfTB6Zw1-wog57S4ye2Mk3E1A0do3HOfQvVOWHuqC1309CXDiOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uEFawcvUUI1wQ6QhvnLXDxUwy1WKPjmrIWtZZujR-YxeDhPJcabkWw1qgw8hZm5CL-QzpnLaOaA047HsUi1XkVO5WgavWFXZQzYAbqC6yOiNCVef6GOY_-sl-60x6ix7AZDi5gS_ux62I7YP-7m5MqFIEE8CNWSsxMIiEIKB1xHyZAlo7IpvplCI82y4juvlwl_584GXG8Pova3dWV5lzEAQQcjCiavRgqWlheXcEXKgFxcHG58PjRQG3fWPWeEhSlC0If8beEQC9U1BT1aRtjEHhbDLNAV4RjYonreLwOhT68OGr2xvp9tlRDZ1i71nZl1rKyTHUSTOpyTdWDfmFzfPHWykEtlZrIrnFPs5Ff_X9ZRm6qV7TXD1Kw-RBuA4EmhSNEZWb3puqgYs8XPXPo2_Tw8_UH9snzVfiKmkLiwRTnMymH-HXCAuX2HiW5k44gHbVJqXnQVYeZ2Ky0O6YXXuh0K5zzWgLqqYtiyQx6PhnYaKuGhmukzVxQp_nFmhKq08gDIs6pq8kFIKEqNqm7OrL0VB_OwApEv1vLgGtdECOMiOQqjtL6eMmc8OValLwZGBzei20W_iSmsiMPHdxgr3AVkEjEZUUZIjj33NSWnpcLNYrK0vFRZnAfTB6Zw1-wog57S4ye2Mk3E1A0do3HOfQvVOWHuqC1309CXDiOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات کارشناس پدافند هوافضای سپاه دربارۀ هدف‌گیری جنگندۀ اف-۱۵ و بقایای باقی‌مانده از آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/682110" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پولتیکو: رئیس‌جمهور چین قرار است برای نخستین بار در ۱۱ سال گذشته روز ۲۴ سپتامبر در سفر به واشنگتن با ترامپ دیدار کند
🔹
انتظار می‌رود در دستور کار این دیدار تحولات ایران و تنگه هرمز قرار داشته باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682109" target="_blank">📅 23:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
ترامپ: دنبال تمدید تفاهم‌نامه با ایران نیستیم
👇
khabarfoori.com/fa/tiny/news-3238469
🔹
رامین رضاییان وسط تمرین زنان... ماشاءالله!/ عکس
👇
khabarfoori.com/fa/tiny/news-3238424
🔹
مسمومیت دسته‌جمعی و عجیب شهروندان پاوه
👇
khabarfoori.com/fa/tiny/news-3238237
🔹
معشوقه افشا شده ترامپ، خبر اول شبکه های اجتماعی آمریکا/ چرا ناتالی هارپ برای ما ایرانی‌ها باید بسیار مهم باشد؟
👇
khabarfoori.com/fa/tiny/news-3238475
🔹
از نقطه سبز در گوشی‌ خود ساده نگذرید
👇
khabarfoori.com/fa/tiny/news-3238009
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682108" target="_blank">📅 23:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=qpj8kc2nbPpgcTgDAX6r0E4IGBTAd-anupa9ZD3xvZq_2WqFYqxRuIKh5XTrK0HUfBLruPhpyZPd--8n_5rPPUj3B06DJ_sn87Y2ipnRLO2xvYjN-Mk_3Y4g9LBlGejWsxBgCSQ9_swydcZZvK4PV39Ue0EbAINsdHMmrYUubPd_4SW5KSf9dV7p1_buIrDnCfUKWavatnvKnH6JBYwTL2nHISCUYNtvyLRSK2XE-uaw4CPKbl6yrIYBhLQvUB52yZiHGcFwg4EG1wbl5eU_uoR-V4rBnRgt9mPXXEGZXtY6y4b-880QhAoI6k3fsRHrjt3KQmcbQZKY2MOrBFTNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71102e9aa6.mp4?token=qpj8kc2nbPpgcTgDAX6r0E4IGBTAd-anupa9ZD3xvZq_2WqFYqxRuIKh5XTrK0HUfBLruPhpyZPd--8n_5rPPUj3B06DJ_sn87Y2ipnRLO2xvYjN-Mk_3Y4g9LBlGejWsxBgCSQ9_swydcZZvK4PV39Ue0EbAINsdHMmrYUubPd_4SW5KSf9dV7p1_buIrDnCfUKWavatnvKnH6JBYwTL2nHISCUYNtvyLRSK2XE-uaw4CPKbl6yrIYBhLQvUB52yZiHGcFwg4EG1wbl5eU_uoR-V4rBnRgt9mPXXEGZXtY6y4b-880QhAoI6k3fsRHrjt3KQmcbQZKY2MOrBFTNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات شنیدنی از هدف قرارگرفتن یک پهپاد MQ1 و ۲ پهپاد MQ9 در عملیات نجات خلبان آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/682107" target="_blank">📅 23:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_LV1kR3_EL6Oh2-Pq7Zkr3ZUyVPqn0-zCrCvo7eGp_ZXFKymar4eweyvgi7mzkK2k2d2WBxjHvIk6rNdnWo0CEWRmeRx0xbJE7tPNGiy3sGLq8hljsdDwou9jqLASYMciIcgBHtpDSWMI2eX77-Wgr956lATlEP1tKOZsCzk3PHQHaGZkKQvTXXPCUCb4Dsa3a5n0Un3sEc_d3A0OLM3HRhyolxzuFex11fEL4gBxTlOrjDbxlovGjLLphna1-NDaObKwrbS0UDuQiinbFMRbQtZZ720_YB3nPjvwI0-0nN6izs9zPkZn-X10fyp7i7SQMuc813rQSgrFw7QgneNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعاهای مضحک و تغییر پذیر ترامپ متوهم
🔹
ترامپ در ساعت ۸:۰۰ صبح: عمان را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۳:۰۰ بعدازظهر: ایران را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۷:۰۰ شب: کوبا را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۹:۰۰ شب: من تنها رئیس‌جمهوری هستم که عاشق صلح است و شایسته دریافت جایزه نوبل است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682106" target="_blank">📅 23:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران برنامه مخفی برای ادامه جنگ با آمریکا دارد
ادعای وال‌استریت‌ژورنال:
🔹
ارتباطات رهگیری‌شده و سایر اطلاعاتِ شناسایی‌ شده، حاکی از تغییر راهبردی در میان رهبران ایران برای افزایش هزینه‌ها برای آمریکا و متحدان منطقه‌ای آن است.
آنان به جای اعتماد به مذاکرات، دو ماه گذشته را صرف آماده‌سازی برای یک نبرد بزرگ‌تر کردند.
🔹
ایرانی‌ها نیروهایشان را برای گسترش جنگ و افزایش هزینه‌ها برای آمریکا آماده می‌کنند. این موضوع کشورهای ضعیف‌تر حاشیه خلیج‌فارس مانند کویت را به شدت نگران کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682105" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2m2Zq91z6491vvoCWUSz493mIRqKzVW0ockw7ffcMO0KtgOtz2QQAqZLNkhZu4vh1GEFlaGsQ51GELU67eySN1-KWaWZ06f8j2tpE2ByJq73UtuoYUF8BUevDfgGBvRST1iL4tCFz8mWd-kKz5EbXCSRGoZQcowjuloOXZcpbd2QYVE-JfnkQ3UFwisbYhdTqu-Q9u_VuqbfsEOnVPqf2shHyx1auqqSIrvEYWG5uzco9CCe8S2jVemSGSdB4kKTyUMjn2x77tHPM2TH1po-fIyn7D7fTiinFYq-tybsyZjgHSlNNka1XygawEUoQYAvBuYKHLZeeS3cmBQsKierw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوضاع و احوال میزان افزایش قیمت دارو
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/682104" target="_blank">📅 23:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اکسیوس به نقل از یک مقام در شورای امنیت: تعریف «تهدید قریب‌الوقوع» در غزه به یکی از نقاط اصلی اختلاف با اسرائیل تبدیل شده است
‎
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682102" target="_blank">📅 23:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3YPhgo3zzm_XN7T_TecCStQbuDlVVHn-SiS0zllIglUgNWO96ZyfQIdVdSL06Czc6rYVFtf9apZwKF4vMF3zNhBdDyANK254_MFudqzLjczy6uM9ORNEbkLHd0LkSJ511pPDY_0OwRT0YXD4rkmD-fK_5fUyCxDdSMXvgGsIqxK_Iju5Hk0a6egkXggkENhHo5S2KZRZpJPNYMYnIOH0gdciWyutG3SNhaQDVFnKytck_I6Kf6xLp9u4xIHakFm97LsXit8csDdPQxkS_FCJc4ZhPpYEjeCFgsrpf6cu-TbNe6uL0pioq6qKmN_mCrX5xgqcplbtBqA69VAB2Ohsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معشوقه افشا شده ترامپ، خبر اول شبکه‌های اجتماعی آمریکا/ چرا ناتالی هارپ برای ما ایرانی‌ها باید بسیار مهم باشد؟
🔹
ناتالی هارپ، دستیار اجرایی ۳۴ ساله دونالد ترامپ، این روزها به یکی از داغ‌ترین سوژه‌های شبکه‌های اجتماعی تبدیل شده است.
در خبرفوری بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3238475</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682101" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای داماد ترامپ: حماس سلاح را به دولت تکنوکرات فلسطینی تحویل خواهد داد
🔹
وب سایت خبری آکسیوس به نقل از منبع مسئول آمریکایی نوشت که جرد کوشنر، داماد ترامپ گفته است خلع سلاح غزه با تحویل سلاح‌های حماس به دولت تکنوکرات فلسطینی آغاز خواهد شد.
🔹
رژیم صهیونیستی طی دو هفته اخیر ادعا کرده است که این سلاح‌ها باید در خارج از غزه منهدم شود که بر خلاف توافق ۱۵ بندی اخیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/682100" target="_blank">📅 23:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4373363a9d.mp4?token=Jy3nSXf8fNbM7-tvNV-Jwn9pmYZb0Y9vLpySqGPk023wcT-M0DvVOSZK68LpV6iL8-wbHTOa5iE27v5y0dB_113ANIm2R77WnaCeFM8t3fCbaCw638ZxPKZskFDsTTyVywsAEL4IvZd56RkKDeh7EiFOxZeoXmIlrSKqvL-Lm6zQdbrJchLdl2cCjdIacbiWvaZ44tsSNZL5NEam_-Z4KmoSNSFUOkt3D3eiur4KgEc4Jhv7bK0Yw0PcIFsPoqa4HVfmpLtZRFqiP20-M_RBXaJgYmXMmnO_Q-utq_CYrxfnDBTpcs1CU8iIoe4blm8GUchEt577-fWN1cQ10Tju4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4373363a9d.mp4?token=Jy3nSXf8fNbM7-tvNV-Jwn9pmYZb0Y9vLpySqGPk023wcT-M0DvVOSZK68LpV6iL8-wbHTOa5iE27v5y0dB_113ANIm2R77WnaCeFM8t3fCbaCw638ZxPKZskFDsTTyVywsAEL4IvZd56RkKDeh7EiFOxZeoXmIlrSKqvL-Lm6zQdbrJchLdl2cCjdIacbiWvaZ44tsSNZL5NEam_-Z4KmoSNSFUOkt3D3eiur4KgEc4Jhv7bK0Yw0PcIFsPoqa4HVfmpLtZRFqiP20-M_RBXaJgYmXMmnO_Q-utq_CYrxfnDBTpcs1CU8iIoe4blm8GUchEt577-fWN1cQ10Tju4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند حرکت ساده لباساتو به سرعت تا بزن و مرتب کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/682099" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmH0tD31tuUak7xxoQvu-lPfEsoYVaOeerQeRro8dHqdLSQaP5awK0c382UofsSppFyvo34L-0Ua3whHJ7uIYVfQhLLY_NG3MCeX1Ffd2_1cqAw_lJosZfWFFLKzdU46AI2aM_K4YSCSGqmPK-Qq2axMSeyUKHF5JS5Jayv4vOSLUbyJPDdAV5uRe9nsY1Kl_vRb1yCFaX3eij9RDazu4wf7Oy0laky44EVzH_GvgvpnJihHxQXayesPCz6sRUtGLJ1dxuNsVa41yF3kLqtdZV0VYlVUZCh0jM0G1WqvvDIMvsYTV03sa3Mdq2fg1CV2TFc2MqDZzUjYw5JUFcQnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت آمریکا از جنگ با ایران افشا شد
تایم:
🔹
گزارشی از مرکز مطالعات استراتژیک و بین‌المللی (CSIS) که تخمین می‌زند که این جنگ ۳۴ تا ۴۲ میلیارد دلار هزینه داشته است.
🔹
طبق گزارش CSIS، حدود ۲۶.۱ میلیارد دلار صرف مهمات شده است، از جمله ۱۸.۵ میلیارد دلار برای سیستم‌های دفاع هوایی مانند موشک‌های پاتریوت و رهگیرهای THAAD. ۷.۵ میلیارد دلار دیگر نیز صرف مهمات حمله زمینی شده است با وجود این سرمایه‌گذاری، حملات ایران همچنان به پایگاه‌های آمریکا در سراسر خاورمیانه آسیب رساند و خسارتی حدود ۴ تا ۹.۴ میلیارد دلار به بار آورد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/682098" target="_blank">📅 23:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682097">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
طلاسازها هم راننده اسنپ شده‌اند
نادر بذرافشان، رئیس اتحادیه تولیدکنندگان و فروشندگان طلا، جواهر و نقره تهران در
#گفتگو
با خبرفوری:
🔹
در یک سال گذشته حدود ۵ درصد از واحدهای تولیدی طلا تعطیل شده و همکاران و کارگران ما که هنر تولید مصنوعات را دارند ناچار به فعالیت در اسنپ یا مشاغل دیگر شده‌اند.
🔹
بضاعت صنعت طلا و دانش روز آن طی سال‌های اخیر ارتقا پیدا کرده و این صنعت ظرفیت بالایی برای صادرات، ارزآوری و اشتغال‌زایی دارد، اما حمایت‌های دولتی برای توسعه صادرات و پشتیبانی از تولید هنوز پررنگ نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/682097" target="_blank">📅 23:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اقتصاد هنوز در شوک؛ رشد ۱.۲ درصدی که خبر خوبی نیست
🔹
تازه‌ترین آمار تراکنش‌های شاپرک در تیرماه، تصویری نگران‌کننده از اقتصاد ایران ترسیم می‌کند. ارزش تراکنش‌ها نسبت به ماه قبل تنها ۱.۲ درصد افزایش یافته اما با حذف اثر تورم، رشد واقعی به نزدیک منفی ۲ درصد می‌رسد.
🔹
اگرچه شرایط نسبت به اسفند و فروردین، هم‌زمان با جنگ تمام‌عیار، بهتر شده، اما افت شدید تعداد تراکنش‌ها نشان می‌دهد اقتصاد هنوز از فضای رکودی و جنگی خارج نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/682095" target="_blank">📅 22:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh4EwPENu47tnIaTRzTDKJJSZFffM_4-RXSNthTOKQydYQe0yAbWyUQ8O0-fbIL8dQPF0cvNfSlKjoFzmBddyAKJvkqWEYCOgMk7rdFT-spwKi-RQ3iwQLjaortKtmNusWZX884A7V1-mcexymwqtCfZWtDTVXWoeceQF4looO4DU04oH1p1oGC4td2CXaekbsbs14tm383OcpC15xcYi3MM036EOeD-UJuSF3si7cGwds-3lYBnCn8b8JVEG4WzJulLZx0Jc7gdlR3xKKfDrC-l2WV1cWZJ5c-KAA1t-gOJHoDLNvCV42L3a-HtiFD_gHWc5M9XxosmyOgcsBLvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: صبر و همبستگی کلید ایستادگی ایران در مقابل فشارهای خارجی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/682094" target="_blank">📅 22:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
کوشنر: اگر ایران حاضر باشد توافقی را که تاکنون با ما درباره آن مذاکره کرده‌ایم نهایی کند و توانایی ساخت سلاح‌های هسته‌ای را کنار بگذارد، طبیعتاً [ترامپ] آماده توافق است
🔹
اما در حال حاضر، ایران هیچ نشانه‌ای از تمایل به انجام کاری که از نظر ما منطقی باشد، نشان نمی‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/682093" target="_blank">📅 22:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXsJtQ7xupzp0l2-q1X_TzL_5Iq8H8vqas7mT5TPSEAUBjouuDZReoh-IV-BkA2dFcRZZSMJ2NBUXvHChhkj8bcxWZYPGEtoVuMJv6JxLltR8MJv4JBeis0CT0lCkfo1b_6c_k0dKD3xD9UXvhXl_3NMuz972iPTFq1mVop11V8JPPjwsRuZYzeS7N5i3E_sy86058JguwzoFjjbdW5NfS1oPMXDczEG1QaOgQc3aKSJs0IYmr5mjItLQdgorhoV22dqtgnGs1SlYvwUIZlsSaCJE_ja62OUgqVHSmtYGK_8Or6_jolImFqAyDuEz-issSgCS3WN2udEcuSKeiuMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoF21UY_qNK-H11VAVU2cEl-lfN2jEtjgfe0toDwghYuS2n1bhk5G60pZ8cvIgxUINBwEixUmAvpSNnCWyKhNk3ScGPGAEWNmLrN5GTNqp-mN4cECt9U_74A2vSD5YPv3ctbd7ua99dRLyRKrwsZ9MhYPNk4_33KPXVZuQNp14ffqdizPR07hJ7OaUd1PSIPwWacGG0DsLOkeHE4MbQMUsTSyC4S7DbpO5IpjwnUTuTZ6K5Vhul9OhPXT7DBN_f13AWIDzrpI0nNgukEpugPKTmmIoRpBpAqT3yHNQfuyghn84QB5BHrQILWUgWcSy5ltvcrSy-LEOUNYohYEmqCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOYR74eq73eKDrgjdEpZ6qds5SQ0DspHBWo4m-RFly5IzItWpMoeTKTiqxvT895bj21usGlwvOiBo0XwRuz_RFpHTx_OmbOZEQOI7wb6NSahtkz9B4NJwYmKbiaUx3UEE9Air04ga_v3wIqgsm6T7-ko9QbuckoFPTf7ZM04_1lTXInuKRmd-McrvawmhbRCP5Ee0ykK-GwR-svbCN2TWX9okiuBz_fokIYcZL3JSVXeWdZUx7qi4_8yKd-eMlC1dfkYJU4FrPVHKigu7eFUsQOueq72GqlUXAI8RX73lNyvDTvFEVhxj7pQZZiK-BNcf_9w4x22md_VJwEjZQEy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5fKr2KBBOqGKpznhECj8xH39yTPGB_yTrQNmW1gvJotk95uQwPSj_Zpy7QFrZdfxZOoXUBMXn4qzTjTMJkdwA6KGYoUYpW4nKaruRaWRTDdXB2jl6n0JIxT2g3oE74FX5FBKc8ZjH-TnDqXa6IRxxw1Kii1M4oY1pU5dzP6FYgWeCvwAyp0ygeEzJn2zXzPp9wEuJsV6t3pKldgUiO2OYpPIEkTMZHWWZ0g1F4gVziuuqfw20aNrkgCOBngTiy55fn-eNQn-tE6nIKAE15XnPwbiziiAU1Cp_i3nqdV3EYefkd7PuMUWbOYWTSKXYV0n6TggAfUHM-1JaN3-uN1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiVqU2CBEH_XLzMEaplZB-uSjSFfgxix4GKf82dpPd9JX2RwmNg_tvcNGxR6FK_2qK5nlh8CJF4WA4BnPo_tmh9WuE_5qn8WQTZllQakSdOq2ZpRe7GPHwyXcfogyhm5_VVM7Wzg0kXlQL7oDSNhpzo4TO0GxfL4H7UEdEz0Q_fQDxqR8qSl9BdSJ1wENM9hqCjG1xkIfbqtnkTvGsoAREbpC1O-5I_VEZVFU_Jfp40oUSV0k9cDqKsv31hSjR9R8qeLrL3z9is5Sue75qzS6uYa_nbgOUIyaGrA8Fj-J4Ab0HakLlePYSmO_auHnGw-NwVtJy2FyAGoVZtMcHxyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcM9m2hb0orCi-KgpHJoKz3svKiZEiLbtrpmaHTk3PK6b7vJHlWzOQVhe3zs6jTbNvfI0IhPHqsavHwQ_3eGxEOe8jLBgUv4dRs2ZsBZdLSEGv7sx_7rWYVRjVn4WIAujfEe4PKVW2wkg9F8YJoCORm9zWKHmqH1Jx8en8tPfrhPUI5iZE9u5yvb08dwbfohOPo-lN4zcToGTZSbBc8hTgthQcxxxVKLBc-n77CaMAWfTTFNSy5H7ICPmMqXxWxun7bKpuiEX7jmEljPf-8IDsyAyBd4Y10STHOXhRRS71z4Tv9BitqjVqB_EBMPgJvV6Ql38KMV1hWYtVrW6He92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvb8BdIbYNL5Rhlakyu6YWk9AzrDpdSGk4n3jZFcbDvB0I6dIEgbfydLF7YItK173sUVP4HpANtvjPkllE-qwPQ8cT_GZEt1KrrSdexzXtIvOKTZN_lcJdv201953etJ5iPVEg_Nll54JjO8Pvdr9at1lN8-WbYJSx243ys1PkH1bjozLuLBwUKY258S_Bu7bFU7IfkGlpWWbtUNhNzNfr1FeCZkLHVzAU1iJrYd0GmrHs-eP9Ce9JAbfZSg3bFC510H58PHYaNLJ6gb6WFtrW_2I-csMOJGL-3wUFD4vutQmzYuw-0oJQEB1LM25qpwVOFSP0u1awZFipMN3t7c1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پشت‌پرده جهش عجیب قیمت مسکن
🔹
جنگ قیمت مسکن را بالا برد، بعد کمی عقب نشست؛ اما چرا دوباره صعود کرد؟
پشت این رفت‌وبرگشت، ماجراهای متنوعی وجود دارد که در این اسلایدها می‌بینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682085" target="_blank">📅 22:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682084">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRvM1tUP3AFlJWbv_baKOq5RLppI27qI1ilHDdusqyIn5lTLB1UxICE-Gu45b0_iNfX3ETqSG8Oc0vZ1mTLBou22J5zG_pE4YIwjuH5rUbmy7pLQcUy-DngE7RIIsHjk-BljpyPFpdpxx1myuYU2A16tucDX7xHcN34HPXMWcueZye7ZTYCeq2UYMlpjTDo3BoDkFro2aemNAQQECYtOsNR4B3PibI2QOvnUMsnw46dGXDn9Zc18IcOw8tZBtJa_3BTKZBJNAT5ysSwgUVgGS3sKhGxR2NrQ5kZmWsYmOiZ7kaAXk2At9Dh0sZcGEDGtge2Gocqqn_CR7qhqaAJWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر اسرائیلی: میگن که فرستادگان بلندپایه‌ای از امارات اخیراً چندین بار به تهران سفر کرده‌اند تا به توافقی دست پیدا کنند
🔹
تا جایی که من می‌‌دانم ، امارات از ترامپ التماس کرده بود که ایران را به‌طور کامل از ریشه نابود کند، فارغ از اینکه این کار چه هزینه‌ای داشته باشد
🔹
اما آنها به جایی رسیدند که از ترامپ ناامید شدند، چون فهمیدن که با یک دلقک طرف هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/682084" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682083">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZo4nAphHqDqAQjzfTGspIRkk1TGtagFObJElS1Mg6WOKMsVwdDl8ma829juFVZ6ifgQXki0eiDiiaitK33Mynphemt8spV6eS8WeGqrOstif4UOVNTYM99MnxWIseOWOc8YemJc914YfRl-KKeC4LtcJFXRJWIVQ8q1SbDUq5UxQ4_vsWtKd-gvOJOxC3ueWZLdhFBSCbE-4LMq8zSe3AcpDyPatj2U-vMgHQ8eR9KqM2uQ51VF_hhUzL0y5fy5-nie_uLhCLa59XBxfoXLhsFWAgXkpm_wV2AACbgDoY4kSSoAX0S0qE01c0K4hZi2GBFQmLib-_6mew8_8Z4j1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خرید اعتباری آهن‌آلات با LC تا ۶ ماه
⚡️
مزایای خرید با LC از آهنگر:
* تأمین انواع آهن‌آلات موردنیاز پروژه
* امکان خرید اعتباری از طریق LC
* مناسب پروژه‌های ساختمانی، صنعتی و عمرانی
* تأمین از منابع معتبر بازار
* پشتیبانی از استعلام تا تأمین و تحویل بار
برای دریافت شرایط فروش LC، سقف اعتبار و استعلام قیمت وارد لینک زیر شوید و فرم را پر کنید.
🌐
ثبت درخواست</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/682083" target="_blank">📅 22:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
بازار طلا حتی با جنگ هم سکه است
🔹
پیش از آغاز جنگ ایران، بازار طلا به‌طور متوسط ماهانه ۲.۸ درصد رشد کرده بود. در فاصله ۳۸ ماهه میان جنگ اوکراین و جنگ ایران نیز قیمت طلا تنها در ۱۰ ماه کاهش داشت.
🔹
این موضوع نشان می‌دهد که در این چند سال اقبال شدیدی به بازار طلا به وجود آمده است. این عطش البته ریشه‌ای عمیق‌تر دارد. سهم طلا از پرتفوی بازار جهانی که در سه‌ماهه چهارم ۲۰۰۰ حدود یک درصد بود، در سه‌ماهه نخست ۲۰۲۶ از ۶ درصد عبور کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/682082" target="_blank">📅 22:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اصرار رئیس‌جمهور لبنان به مذاکرات بی‌حاصل با صهیونیست‌ها
🔹
«جوزف عون»، رئیس‌جمهور لبنان در دیدار با هیاتی از سازمان «تاسک فورس برای لبنان» به ریاست «ادوارد گابریل» تأکید کرد که بیروت علیرغم دشواری‌های کنونی به اجرای توافق چارچوب با رژیم صهیونیستی ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/682081" target="_blank">📅 22:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1c0edcd3.mp4?token=Q6gLw6iHY80UGY29uLSWcw8CvigOPRNgh_LI_x2rEckQpYo7qXoY3xrd5XxECch0rjQYrh_sjVmr5o6sgB5JUqfmkWVfr3vaVSeUsa8eD7k8iLlmsE5vwoxGVkCidnjITzSgGN2ecgIOy-U5zCGvd1AOkMenP1eS_mYJlGpSW1-EhBaUiqsGjvb2kLcVRI2TLZIoEz14q7DrNNeneydlCR9Kom-s25zTDy9Su8Q4JdVUY8oSgbF9TzHw6BdRadUbT07mrLhZGxgadWdi7qk6W19Q92v95X9WSgAI5vFl3VYtBV4kwZfH8knM_ZLhL6MscH6DZIyC3bpV10rkYoh81Cct45AU222bNuIQc7sJacyXzL4a9cQWiL-FY44yItJWSpwr7iAjCL9-Rpg2Oj4oQqKsg_UZhFNab1m_LmKKJC8QY7qcQQYHTNFYxmzjBxsUhs47VBzjyFeDYES8Zmjrjxjl9v9AzUKHUR8_vrqEEq4WJ3zXOJhDICHT4ZVmoBiVWib0dFNizSqpAmriGQsispn-rBDyo2yYtVX-XnWz0Zm3XoA3mOTYEjxJK2YfL1rpWPNPR84gVyyUg14M19wYFs8_14upok3PuOEAeHqoTWUIdnQEd4pQYWiSnPIwv6-Y0xyDS63uAd5gA-neOCZyBW7AnTHNOilnZTtLNHSIgK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1c0edcd3.mp4?token=Q6gLw6iHY80UGY29uLSWcw8CvigOPRNgh_LI_x2rEckQpYo7qXoY3xrd5XxECch0rjQYrh_sjVmr5o6sgB5JUqfmkWVfr3vaVSeUsa8eD7k8iLlmsE5vwoxGVkCidnjITzSgGN2ecgIOy-U5zCGvd1AOkMenP1eS_mYJlGpSW1-EhBaUiqsGjvb2kLcVRI2TLZIoEz14q7DrNNeneydlCR9Kom-s25zTDy9Su8Q4JdVUY8oSgbF9TzHw6BdRadUbT07mrLhZGxgadWdi7qk6W19Q92v95X9WSgAI5vFl3VYtBV4kwZfH8knM_ZLhL6MscH6DZIyC3bpV10rkYoh81Cct45AU222bNuIQc7sJacyXzL4a9cQWiL-FY44yItJWSpwr7iAjCL9-Rpg2Oj4oQqKsg_UZhFNab1m_LmKKJC8QY7qcQQYHTNFYxmzjBxsUhs47VBzjyFeDYES8Zmjrjxjl9v9AzUKHUR8_vrqEEq4WJ3zXOJhDICHT4ZVmoBiVWib0dFNizSqpAmriGQsispn-rBDyo2yYtVX-XnWz0Zm3XoA3mOTYEjxJK2YfL1rpWPNPR84gVyyUg14M19wYFs8_14upok3PuOEAeHqoTWUIdnQEd4pQYWiSnPIwv6-Y0xyDS63uAd5gA-neOCZyBW7AnTHNOilnZTtLNHSIgK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سر اسرائیل در کدام آخور بند شده که در این جنگ نیست؟
🔹
اینکه اسرائیل در جنگ فعلی آمریکا با ایران حضور ندارد برای خیلی‌ها تعجب آور شده است. اما ماجرا پیچیده‌تر از این حرف‌هاست
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/682080" target="_blank">📅 22:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n93ulAWEMrIberks_RzFtCTwxpCNDyGiaeiixlE7OrdSZLgxUecEVe608_l1wiOnPfMEJS2yeXWOSNSzUZMI7d-sEd36KvbTIsSQtTbtGbRDBFHR4bTFUuPRFMGmlVNbNiM-xy2-7MthN-cXCkrIGn0ekX38eu8CmDvWD5Eui5A3v739kWxSeR3NnzbcqY083lzvDPrbG-69v09RfY4PnwOD1E2of3IFxSxO7PLAYmSzseBXsmbCdoQnrYpk14sCBx8h3MNVENdbD5947TQUfMEhqytpjAlhZd4gP806DzuzfeBcSiba8wiA8z5x_i2YCErvyaUplL9ujMBix4UGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم در صدر عوامل گرانی مسکن
🔸
در این نظرسنجی بیش از ۳۸ هزار نفر شرکت کردند که سهم روبیکا ۵۵ درصد، بله ۲۷ درصد و تلگرام حدود ۱۸ درصد بوده است.
🔸
حدود ۲۹ درصد شرکت‌کنندگان، تورم و بیش از ۲۲ درصد، دلالی و سوداگری را مهم‌ترین عامل گرانی مسکن در ایران دانسته‌اند.
🔸
بررسی تحلیل‌های کارشناسان مسکن نیز نشان می‌دهد تورم، هزینه ساخت، قیمت زمین و سوداگری از مهم‌ترین عوامل گرانی مسکن در ایران‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/682079" target="_blank">📅 22:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfhW9LpcZywzx0oXnmMhbffYnpjLsVNhRyuR8yCBApTa9Lfkpq2nlWdrFLQKZ79Ons1TszDdQIKiFelYXcu0ChQQ3x6zvt2lpSX9XzjDxiVzO4Vpto9SAYYsYyTcbdSVAaoxxiSpBOfRDmZirOfhjoe1M1bgktAuTQEzNzw5xD1uaOFY2n7TSVX9Yz_jLTGBllm-guwBeU2TmLzOLRQqYPBkg27RE1e2aQbBGTwEGoU2ZK08duilLFevRbKnoJjp6QSQ5ep_-Kv6DR14l74CgKp5QniXVt-UgDp6Ox1MHFHOxrL7ti3ewWlnbIvbhpdGhL6mlO_VBEEJ8dqs4dXX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رهبر شهید انقلاب درحال قرائت قرآن کریم در کتابخانهٔ شخصی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682078" target="_blank">📅 22:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آتلانتیک: ترامپ، کره جنوبی را به خاطر جنگ ایران تنبیه می‌کند
آتلانتیک:
🔹
پس از جنگ ایران، ترامپ دستور کاهش رزمایش‌های مشترک آمریکا و کره جنوبی را صادر کرده است.
🔹
اقدامی که به گفته منتقدان، در واکنش به امتناع سئول از پیوستن به کارزار ایران انجام شده است. تحلیلگران این اقدام را نشانه‌ای از انتقال هزینه شکست‌های استراتژیک واشنگتن به متحدان می‌دانند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682077" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMddgVAJbmycChOGPF26NyAc0TJ7l1XI12ZlX0P9yRGoehgs3zr3a5lkH6IBsmJ57EXWcG-5dkg0d0Qz9zUU9Qcy1A7USHuTjPmSITvxkIPiZlMTbt7PwEZ55Fm2xj57vXClHlXk9GjL-bvZwfgTAQzKBch10bqTsCiQxlMc8i5oqVHdTebRdgHW6ERd4Qk-ecWIaa9v3NEq9td72MSxc484s8ZF4wvF7FeU8h-orPR4x1d7b1KeldqI5oVMv0lnqbAo87KxkRRncIIeJQhk2GCzDHpCajQIhfBwHQ8wcNRIb06oNfDAcOxKu-LwNiDrabx4R4rKOrgI57xApxL9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای نخستین بار؛ تصاویری از رهبر انقلاب، امام سیدمجتبی خامنه‌ای، در عیادت از جانبازان انفجار پیجرهای لبنان
🔹
حضور در کنار کسانی که درد و رنج را با تمام وجود لمس کرده‌اند؛ دیداری سرشار از همدلی، آرامش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682076" target="_blank">📅 22:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY_T-glZaWnycnrPyxyGoTeRCyB4cxyZMi_3DEb1Z-k_1NAIQKr0U8qbu5BeoKG3h3bdm9iW0qWgUWcTF7GMi2RI_VxFm0jFShM5aajHum57ZOuBv2ufhIgckL11WYH7gr7Qv0_51p9bQ3ej_r527C0CLiZBzvcyWFyoowsJzC1WTFlwe29o2Q26e8L_hP9_fS99P47K3e49RpuNl9v7fUd67fPKuL0gQj8bpU6IjEvZMhpVMleLY-_cVZx5ZF6HajVuMwC4verlXr09OTeOoMnEf2Vf58ZgWXrDX7GK1NeU5ul69-aP7FZLJOzGgWWmaHlzSRHg9RXsUag8JNL_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به عملیات پرچم دروغین در کردستان عراق؛ دوستان کرد ما، هوشیار باشند
🔹
هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند. دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار باشند.
🔹
ما در برابر صدام و داعش از دوستان کرد خود حمایت کردیم و از امنیتی که آنها در مرز ما فراهم می‌کنند، سپاسگزاریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682075" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22bf43f174.mp4?token=TZL4C3Nvyc7KPjjNxIukqbW1-fRlnsqY2yGtK5yX6Wfw6aeVW5E63BBiAwZd3hJJ5NjqpEo-GL0m3u4rAS0NvFG91hsbIv31QhQNjhmOxQDNqaFCjpKzZbxlCL4gL8YoCyR8BhvLvA_JyPky9HE13yy-zv1MAKLaaxCQIWnjLx6ocxIBp8taU3nRH4odz5EKHvlGCTT89YCiBIOfXbI4zR-W6UBtyiZlYyXjYedIa5Z4oZOvNP0JOUE5tuSdcmz35G0u15kZ-9YVz_vYV4dOULXnPccxFlPai0-xpFiu3zHtld9pYeSiHxZCEboY0f9IhflWB4wsKJ7w_U4BdX2J0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22bf43f174.mp4?token=TZL4C3Nvyc7KPjjNxIukqbW1-fRlnsqY2yGtK5yX6Wfw6aeVW5E63BBiAwZd3hJJ5NjqpEo-GL0m3u4rAS0NvFG91hsbIv31QhQNjhmOxQDNqaFCjpKzZbxlCL4gL8YoCyR8BhvLvA_JyPky9HE13yy-zv1MAKLaaxCQIWnjLx6ocxIBp8taU3nRH4odz5EKHvlGCTT89YCiBIOfXbI4zR-W6UBtyiZlYyXjYedIa5Z4oZOvNP0JOUE5tuSdcmz35G0u15kZ-9YVz_vYV4dOULXnPccxFlPai0-xpFiu3zHtld9pYeSiHxZCEboY0f9IhflWB4wsKJ7w_U4BdX2J0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار زیر میز ترامپ؛ سکانسی که پایانش همه را غافلگیر کرد
🔹
یک امضا، یک خودکار و یک انفجار مرگبار؛ همه‌چیز تمام شده به نظر می‌رسد. اما چند ثانیه بعد، مشخص می‌شود که ....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/682074" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmwNDM31rdfMjDsiK0-NKMowsoeI73-kaPOrPoH8mKiHOEoCNBNb7532o4AQib0H74cpZOeXDGdNke6m5j21WegvRVDZFSbOb1v-ltyrMc5fxQd3HgYuxRYrEeVjAkDCJJ5-oLrcxh58DGEi3VMudL7OGVb44X_tW4XufwzxIyByIFqFdwHzWmmI7gTWjhGZLRgZhU-uu8dqDCAAPB9nX2_fHpksW-GDPnBP-guS758M3MG0Ssp05LvpTW63AR0gZxN8oBBED3QGUYA2O8UoYehriX_dPDVnsByv0MEfKcjl3Dgy3eY4h6nd_YUa_Z-BsKNwQQ0VSnwUqHrQu5Vi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس واقعی از خدا، آدم را سخت‌گیرتر نمی‌کند؛ مهربان‌تر و بخشنده‌تر می‌کند
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند کسی که از حساب و بازخواست الهی بیم دارد، در برابر لغزش دیگران زودتر راه عفو و گذشت را انتخاب می‌کند. بزرگیِ انسان فقط در قدرتش نیست؛ گاهی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/682073" target="_blank">📅 22:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeVQB0_cDpVZ3NQLLfEgp9puENWnVa9D-SxYquE5UEab_Ih2T0MlxjjYwE8gsR7kDa7qivCSbvPRszYKmwEvIUIPqLEBLxiKgTRZiMuJjR7LCRlvbBGY5VPcNdMI9OQDO6NnMGCvkWyFT3pcuewKCvWMFUuQ9RS5f1zMFr95TyFH1Ik9YkLWsD4NdVnE4nk_su-DI5c4DQBlCV7Gwex93g1-bxpGUV6p3jvoPwEDKIPTGEanXBCBN4ouYm_JMMRG0IL44JJ-nZxTv36dfpzPZE5du1hPZu8jGqMxoQE8YzzcRp3Y1u4UIjL7VJYjYksywh5q2OCeNjKS98JjcVgcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌بس هیچ
🔹
آتش‌بس ۶۰ روزه میان ایران و آمریکا در حالی به پایان خود نزدیک می‌شود که به دلیل بدعهدی‌ها و اقدامات آمریکا، از همان ابتدا نیز چندان شبیه یک آتش‌بس واقعی نبود. در طول این مدت، موارد مختلفی از نقض تعهدات و افزایش فشارها مطرح شد و همین مسئله، آتش‌بس را کاملا بی‌معنی کرد. اکنون برخی رسانه‌ها از احتمال تمدید شدن این آتش‌بس هیچ خبر می‌دهند، آتش‌بسی که در صورت تمدید احتمالا بازهم هیچ خواهد بود.
🔹
هشتصدوسی‌‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/682072" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b0d45dd.mp4?token=Farpun-sCkgU8AF_Q-teqZyfvXPQIIO0rzXpfSEoZ1GNhRIMtY3tgGJcEF9icHF1w9ife8gTdufBNv92YMAGYxGv9hNcY2OoaXwC-yzvL6cnkAxo60b8lq_cK525G1JpqpDaQIXeFO_RpBlLBTyAJeht9wYKU8d9WbqERKeAuAxsdt1I_-cfhKkuzUvmTUK81VEPrTxVpMNKe5sayQt2OAnnuf2N5aX0wp_xkRO17e7KJQz5AlkbV6WIjBEM3m8KDqJqDv3BxwRsxPKYQQyBXcayWoieYWikDogorF-HaRL29FCzSxvZ41nHXp3aGxNFE6TeW395XqGqQbRKjZrekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b0d45dd.mp4?token=Farpun-sCkgU8AF_Q-teqZyfvXPQIIO0rzXpfSEoZ1GNhRIMtY3tgGJcEF9icHF1w9ife8gTdufBNv92YMAGYxGv9hNcY2OoaXwC-yzvL6cnkAxo60b8lq_cK525G1JpqpDaQIXeFO_RpBlLBTyAJeht9wYKU8d9WbqERKeAuAxsdt1I_-cfhKkuzUvmTUK81VEPrTxVpMNKe5sayQt2OAnnuf2N5aX0wp_xkRO17e7KJQz5AlkbV6WIjBEM3m8KDqJqDv3BxwRsxPKYQQyBXcayWoieYWikDogorF-HaRL29FCzSxvZ41nHXp3aGxNFE6TeW395XqGqQbRKjZrekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ قمارباز درباره ایران: ایران در وضعیت بسیار وخیمی قرار دارد. کشورشان در هرج و مرج است
🔹
نیروی نظامی آن‌ها کاملاً شکست خورده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682071" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24fe61119.mp4?token=mGjVZItnmN5EMGrm65p_lo2mbgAWoHEeanTan4Aw4MPULJfyQ2bFOg9lYV53YUtflPnhUarJdSVk3e9eJYEiIxt0HelgcJbYxVp-awcqsPzZ084BBYkrs2uTtElQ9YTRcaqy5wOQ0y9L3IsqjTVbCt0ggTDmvpDVFO7QIRRiQyyJeqpIvkwSSIS9lSgTo1wF4PGcBmp-MpXUK2LgZuoKlkiHrha-9D2SBA3gtetb9o011D0L4cHuQS7UJ61cxJNN0oVmuRyjSnUkxvvAnqsDMKwniHt9x50WW_CD8CyCtUVGShZaoDPKIdBItpQmsh6fu9KBkdAMfQH6cwnxhCxAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24fe61119.mp4?token=mGjVZItnmN5EMGrm65p_lo2mbgAWoHEeanTan4Aw4MPULJfyQ2bFOg9lYV53YUtflPnhUarJdSVk3e9eJYEiIxt0HelgcJbYxVp-awcqsPzZ084BBYkrs2uTtElQ9YTRcaqy5wOQ0y9L3IsqjTVbCt0ggTDmvpDVFO7QIRRiQyyJeqpIvkwSSIS9lSgTo1wF4PGcBmp-MpXUK2LgZuoKlkiHrha-9D2SBA3gtetb9o011D0L4cHuQS7UJ61cxJNN0oVmuRyjSnUkxvvAnqsDMKwniHt9x50WW_CD8CyCtUVGShZaoDPKIdBItpQmsh6fu9KBkdAMfQH6cwnxhCxAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دروغگو مدعی شد که ایالات متحده به دنبال تمدید توافق‌نامه همکاری با ایران نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682070" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4c402d2c.mp4?token=b1I54xO78Zkwj7NnAbaOXh8HdAbYIsDRdSGRmiQfhPX4uonszweVffleQg8saCo_rAs1A7DZVZCvKjceGBMferlokbNd2yBuJWP5QqSKcmX-l7Zq505fuyuMwnKdpL-0YanBf8VaQl7yoOV9OYsMcQLrd6ZWpkNz2Tgk3hmOnbDPuWjZ598Z6TaTrd18wGSJ7sIBrUOg3wY1WrGoV3nXwhAgGs3wZOes4gaqaLdZJewCdII9XkkwIRuE_Nvz-hnUJ1NbiEBlQfIKOCcfJ0u3HwgKcK2a2mfE7hpcoOmHLTh8usfWHq1u3ykOyuIyarn3QjFY04098XtaE9itbiMd3qzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4c402d2c.mp4?token=b1I54xO78Zkwj7NnAbaOXh8HdAbYIsDRdSGRmiQfhPX4uonszweVffleQg8saCo_rAs1A7DZVZCvKjceGBMferlokbNd2yBuJWP5QqSKcmX-l7Zq505fuyuMwnKdpL-0YanBf8VaQl7yoOV9OYsMcQLrd6ZWpkNz2Tgk3hmOnbDPuWjZ598Z6TaTrd18wGSJ7sIBrUOg3wY1WrGoV3nXwhAgGs3wZOes4gaqaLdZJewCdII9XkkwIRuE_Nvz-hnUJ1NbiEBlQfIKOCcfJ0u3HwgKcK2a2mfE7hpcoOmHLTh8usfWHq1u3ykOyuIyarn3QjFY04098XtaE9itbiMd3qzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ دیوانه درباره ایران: من ایده اعلام کردن تنگه هرمز به عنوان یک منطقه متعلق به ایالات متحده را دوست دارم
🔹
ما کنترل کامل بر این تنگه را در اختیار داریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682069" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933209adaa.mp4?token=eyk9NGDuyWIo3mPMYFgDPS1C7k5npDoSBogkz5WUuPpOyj2LPonZL_R7MbwCSI5xjcgH55m-j9JsORwJIXApUv-8YexSisDCKLggiaEmOuj2Ua5z0YrE7zJGekVXqbQ2Zcp21t_GybOe0uqajk-t20ILeLOnFBhzizGIDYAQC8XMBFLGs9zO4HyMTpqVTNiljqbPpzxpf-NOZet3U6gbyrg8Hq5faPEo766B0JpzDfKqbNl8jfgP_pgjERMPj_j5ZPvLDq90sA1kPHdS06K2NJ3tMQaXpePAUFvluuJohLA1Ik7zhuGjRw47bzcvz5qgtAbXomM6rT9MYq8Km4BzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933209adaa.mp4?token=eyk9NGDuyWIo3mPMYFgDPS1C7k5npDoSBogkz5WUuPpOyj2LPonZL_R7MbwCSI5xjcgH55m-j9JsORwJIXApUv-8YexSisDCKLggiaEmOuj2Ua5z0YrE7zJGekVXqbQ2Zcp21t_GybOe0uqajk-t20ILeLOnFBhzizGIDYAQC8XMBFLGs9zO4HyMTpqVTNiljqbPpzxpf-NOZet3U6gbyrg8Hq5faPEo766B0JpzDfKqbNl8jfgP_pgjERMPj_j5ZPvLDq90sA1kPHdS06K2NJ3tMQaXpePAUFvluuJohLA1Ik7zhuGjRw47bzcvz5qgtAbXomM6rT9MYq8Km4BzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: افرادی که با این طرح ساخت سالن رقص مخالفت می‌کنند، به نظر من، بسیار غیروفادار به کشور ما هستند
🔹
بسیار، بسیار غیروفادار به کشور ما.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682068" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=bXcB9GAGhegz2nFMHAi6EwRxrEOMRvJZMC474-6sVdQ2ROhH9rsOWSi0zjQnC7eC69RKvgf3Oo9UZOjx0B0YfNB8rA83_mYwjpz_Lr809XfmH3gJcy0htwSOpV_gbSF9TPUn2IBR5IOIkgJS9WP8se9Qp7xo_3ZIgPhKMBtF7WXBulWfl1JG680E2WAT4ljNJTO3jVIVzDRz0ii5HlpYuZhBHawXluGPDrX0OE8Gx4NDfFSpMKUVZRJVy1i1sZa7dD0X_cHRmNQez-p7SctmPQktMf33ivgq07h-ujiVGpvvZg24yLaJMvwD_o7BiPnbSuv1t9YTjDK5u5DUlv-5WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=bXcB9GAGhegz2nFMHAi6EwRxrEOMRvJZMC474-6sVdQ2ROhH9rsOWSi0zjQnC7eC69RKvgf3Oo9UZOjx0B0YfNB8rA83_mYwjpz_Lr809XfmH3gJcy0htwSOpV_gbSF9TPUn2IBR5IOIkgJS9WP8se9Qp7xo_3ZIgPhKMBtF7WXBulWfl1JG680E2WAT4ljNJTO3jVIVzDRz0ii5HlpYuZhBHawXluGPDrX0OE8Gx4NDfFSpMKUVZRJVy1i1sZa7dD0X_cHRmNQez-p7SctmPQktMf33ivgq07h-ujiVGpvvZg24yLaJMvwD_o7BiPnbSuv1t9YTjDK5u5DUlv-5WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: ساکت، ساکت، ساکت. شما بسیار بی‌احترامی می‌کنید. ساکت باشید. شما با چه کسی هستید؟
🔹
گزارشگر: من از شبکه CNN هستم.
🔹
ترامپ: شما خبرهای دروغین منتشر می‌کنید. ساکت باشید، ساکت باشید، ساکت باشید. شما یک گزارشگر دروغگو هستید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682067" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76bf98717.mp4?token=DxuaJ4o6ancB3yiDFb_Kb3vuMFcz27zhN1FhjKVwH_7Hyqp2P684Hqdd_8Y-xV5_njFllS5RXDZmJbRrw9ddBhASLFeA5PpCH8adjfbNoip-bj3jdRIa3hMPEFgcGRWmlOpSZInZ-a1crnOm05OKXy9mSgYgqGxfAbUhcLenW7MIoFmaEfldjAInJDw1-Zs9xdCZwdSwfABwvDR4oveKc6Kdud0kt7C1Y0-79XBTiv9oxTPRATsMg9_LyHcIUK0ECwafurEExdoSDvGMgX_e4M6yILa1KTIkkkOg6SccLTNjCNOF2myuPzEE4C4QSeaBIlexYkqhgDCuHsyYTsEApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76bf98717.mp4?token=DxuaJ4o6ancB3yiDFb_Kb3vuMFcz27zhN1FhjKVwH_7Hyqp2P684Hqdd_8Y-xV5_njFllS5RXDZmJbRrw9ddBhASLFeA5PpCH8adjfbNoip-bj3jdRIa3hMPEFgcGRWmlOpSZInZ-a1crnOm05OKXy9mSgYgqGxfAbUhcLenW7MIoFmaEfldjAInJDw1-Zs9xdCZwdSwfABwvDR4oveKc6Kdud0kt7C1Y0-79XBTiv9oxTPRATsMg9_LyHcIUK0ECwafurEExdoSDvGMgX_e4M6yILa1KTIkkkOg6SccLTNjCNOF2myuPzEE4C4QSeaBIlexYkqhgDCuHsyYTsEApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ترامپ جنایتکار درباره ایران: ما هر هفته میلیون ها بشکه نفت استخراج می کنیم
🔹
تنگه باز است، قیمت نفت در حال کاهش است و به کاهش خود ادامه خواهد داد مگر اینکه تصمیم بگیریم کاری افراطی تر از آنچه در حال حاضر انجام می دهیم انجام دهیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682066" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای ترامپ کودک‌کش: با رئیس جمهور کره جنوبی تماس گرفتم. من به او گفتم: «در مسئله ایران به ما کمک می‌کنی؟ اگر بخواهی، نیازی به کمک نداریم». او پاسخ داد: نه، متشکرم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682065" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز صاحب آن نخواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682064" target="_blank">📅 21:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e021862a.mp4?token=PwjVbWun9qYT_KUwFQbsQxq_GJrOqxLGo_fM8tQgQYSs_iX-AyAsDMWZ_np7QfcgLuIFg5VIU_ibXUG_k-RQh4pqk1T2OxnuCme40NqYADpuPyzUpGTKTrChhx6flNGLTVrG5ALPT9HMbRr1xT2JgoQCVp2GBmL28mRA9FdYZ4QfvnYFz38OIhEh5g3FDz5_yHNaxwu-OaJb3p2E4rL0o_6ExSLhpZPXvMq3wVIv9AWYw7E83KFq-BE4D2EgLzBeEGh0KeVuguQe-3UgMrn7GG3QuGzrIe-3DJgNZSTdKhv2v3-ynaJbLZrA-N5eN6Q1wueR43UMYHLKHuJLAK2JoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e021862a.mp4?token=PwjVbWun9qYT_KUwFQbsQxq_GJrOqxLGo_fM8tQgQYSs_iX-AyAsDMWZ_np7QfcgLuIFg5VIU_ibXUG_k-RQh4pqk1T2OxnuCme40NqYADpuPyzUpGTKTrChhx6flNGLTVrG5ALPT9HMbRr1xT2JgoQCVp2GBmL28mRA9FdYZ4QfvnYFz38OIhEh5g3FDz5_yHNaxwu-OaJb3p2E4rL0o_6ExSLhpZPXvMq3wVIv9AWYw7E83KFq-BE4D2EgLzBeEGh0KeVuguQe-3UgMrn7GG3QuGzrIe-3DJgNZSTdKhv2v3-ynaJbLZrA-N5eN6Q1wueR43UMYHLKHuJLAK2JoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.  #اخبار_گلستان در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/682063" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEjJQ7iUqGXSjpXMxtczznsasfvr3EgBrGj3br6JrYhc-R1TKfZrCd341hC36srZcvWuRd2P_fJ9Nj6B7dLnFJgffHh1peh8GVsOpV6B31NdH8G74EwSOjTUReBsBtxAlzYSpXxRJFBLanJczwdALo4IxVgGYPQmsPwNvxqXaOuqaZLzb2oO5_Ypr0VcMUdA5NkW3yi9YuzKLdHYZbhsS4KLa_eNXboLRoP1G6m6fDAH3UtL2Busd_8q6fSw30xIGa56M8fGrW_O2Z_J69boW5c35-derjqib89jadXXf1EPvmiUV9YmqyH4na5eu-Be92I-tXkxCOuC8DwONFPM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شرایط فروش کی ام سی اس ایگل(KMC EAGLE )
▫️
قیمت: ۲،۴۸۲،۵۰۰،۰۰۰ تومان
▫️
پیش پرداخت: ۱،۵۰۰،۰۰۰،۰۰۰ تومان
مشاهده شرایط فروش</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/682062" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز صاحب آن نخواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/682061" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
عضو سنا: ترامپ روی توالت طلایی می‌نشست و نمی‌داند سختی چیست
🔹
مارک کلی روز دوشنبه اظهارات ترامپ درباره ناو آبراهام لینکلن را «غیرقابل قبول» دانست.
🔹
او در مصاحبه با ام‌اس‌نَو گفت که رئیس‌جمهور آمریکا بخش قابل‌توجهی از دوران بزرگسالی خود را «روی توالت‌های طلایی» نشسته است و معنای سختی کشیدن را نمی‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/682060" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d187a30294.mp4?token=LPyiMFWUm424VYkDWr79sWFZWP6zHutht8UaA9U9TsWG2Ldm7qn9e-1Ys5-lX0BsUtQfWejLQ38HYGzJYUHKGdgoXDyHEqqnKTaIIdHXPyfRXJ40n2gwrHramZCHUmgzycc63alG_PWkCD4eXXVCChRiHnfl5Mmabb3x5oaVeCai0ftIp1R8aa8L8jmkba1QKQHUOvuu6_s8uFHeLK0Ps_RoggotA8HFSm6zLJrC40s5oteRcZ5evtLEG6PzJ5TPx2SFxEyZo7w0-l8WmoVwwStIqZN51FGpUwhEDc4dS429g6C4_vp72oeFAQeIfRf24h0NBXqbN6NYylVNOmkIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d187a30294.mp4?token=LPyiMFWUm424VYkDWr79sWFZWP6zHutht8UaA9U9TsWG2Ldm7qn9e-1Ys5-lX0BsUtQfWejLQ38HYGzJYUHKGdgoXDyHEqqnKTaIIdHXPyfRXJ40n2gwrHramZCHUmgzycc63alG_PWkCD4eXXVCChRiHnfl5Mmabb3x5oaVeCai0ftIp1R8aa8L8jmkba1QKQHUOvuu6_s8uFHeLK0Ps_RoggotA8HFSm6zLJrC40s5oteRcZ5evtLEG6PzJ5TPx2SFxEyZo7w0-l8WmoVwwStIqZN51FGpUwhEDc4dS429g6C4_vp72oeFAQeIfRf24h0NBXqbN6NYylVNOmkIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از تصادف عجیب در اتوبان بابایی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/682059" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟
ترامپ:
🔹
فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما ما به‌راحتی از پس آنها برمی‌آمدیم؛ درست همان‌طور که با مسائل دیگر برخورد می‌کنیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/682058" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا: با وجود کاهش تردد در تنگه هرمز، به انتقال نفت و گاز از این مسیر ادامه می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/682057" target="_blank">📅 21:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صادرات محموله‌های پسته خام با پوست به مقصد ترکیه تا زمان دریافت شرایط قرنطینه‌ای از این کشور، متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/682054" target="_blank">📅 21:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پروژه تخریب در ایران اینترنشنال؛ چرا باشگاه خیبر هدف قرار گرفته است؟
در ادامه موج رسانه‌ای علیه چهره‌ها و مجموعه‌هایی که مواضع و فعالیت‌هایشان در حمایت از جمهوری اسلامی ایران و منافع کشور تعریف شده، این‌بار نام مسعود عبدی، مالک باشگاه خیبر خرم‌آباد و مدیر مجموعه آرین سازه، در گزارش‌های شبکه ایران اینترنشنال برجسته شده است؛ گزارشی که با بازنشر تصاویری مربوط به اعتراضات سال گذشته درباره پروژه «ستین»، تلاش دارد تصویری منفی از فعالیت‌های اقتصادی عبدی ارائه کند.
اما مرور سوابق فعالیت‌ها و بررسی روند اجرایی پروژه‌های این مجموعه، روایت متفاوتی را نشان می‌دهد؛ پروژه‌هایی که بخشی از آنها به بهره‌برداری رسیده و برخی دیگر همچنان در حال اجرا هستند.
آرین سازه طی سال‌های گذشته پروژه‌های متعددی را در تهران اجرا کرده که از جمله آنها می‌توان به پروژه «آبشار» اشاره کرد؛ مجموعه‌ای متشکل از دو برج مسکونی با ۲۷۴ واحد که هم‌اکنون ساکنان آن در این پروژه زندگی می‌کنند. پروژه تجاری ـ اداری «یاس ۳» نیز از دیگر پروژه‌های این مجموعه است.
در کنار پروژه‌های به بهره‌برداری رسیده، پروژه پدافند ارتش نیز از جمله طرح‌های در دست اجرای آرین سازه است که بر اساس برنامه‌ریزی‌های انجام‌شده، طی دو تا سه سال آینده آماده خواهد شد.
پروژه «ستین»؛ روایت حاشیه‌ها یا واقعیت حقوقی؟
پروژه «ستین» طی سال‌های گذشته با حواشی و اختلافاتی همراه بوده است. بر اساس توضیحات ارائه‌شده از سوی آرین سازه، زمین پروژه از سوی این شرکت خریداری شد و هنگام انعقاد قرارداد، واگذاری زمین همراه با مجوز عنوان شده بود؛ اما پس از گذشت حدود دو سال مشخص شد که امکان دریافت مجوز مطابق آنچه در ابتدا مطرح شده بود، وجود ندارد.
در ادامه، آرین سازه شخصاً فرآیند دریافت مجوزهای لازم را دنبال کرد و در نهایت موفق به اخذ مجوز شد. پس از دریافت مجوز نیز عملیات اجرایی پروژه با اجرای فونداسیون آغاز شد و پروژه وارد مرحله عملیاتی شد.
با این حال، شبکه صهیونیستی اینترنشنال در گزارش خود تصاویری از اعتراضات مربوط به این پروژه را بازنشر کرده که مربوط به سال گذشته است؛ تصاویری که اکنون و در شرایطی متفاوت، بار دیگر در یک گزارش رسانه‌ای مورد استفاده قرار گرفته‌اند.
از سوی دیگر، در جریان اختلافات شکل‌گرفته، شکایت‌هایی نیز علیه شرکت آرین سازه و مسعود عبدی مطرح شد که بنا بر مستندات ارائه‌شده از سوی این مجموعه، پس از ارائه مدارک و مستندات، با صدور آرای قضایی به نفع آرین سازه به پایان رسیده است.
عبدی؛ از فعالیت اقتصادی تا حضور آشکار در فضای ملی
اما آنچه این گزارش را از یک پرونده صرفاً اقتصادی فراتر می‌برد، سابقه حضور و فعالیت مسعود عبدی در حوزه ورزش و مواضع آشکار مجموعه تحت مدیریت او در قبال ایران است.
عبدی به عنوان مالک باشگاه خیبر خرم‌آباد، طی ماه‌های اخیر تلاش کرده فعالیت این باشگاه را صرفاً در چارچوب مسائل فوتبالی تعریف نکند و در مناسبت‌ها و برنامه‌های مختلف، بر هویت ایرانی و تعلق ملی باشگاه تأکید داشته باشد.
اوج این رویکرد را می‌توان در مراسم رونمایی از پیراهن فصل جدید خیبر مشاهده کرد؛ مراسمی متفاوت که طراحی و روایت پیراهن، به شکل مستقیم به ایران، شهدای جنگ و حوادث اخیر کشور پیوند خورده بود.
در این مراسم، باشگاه خیبر از روایتی استفاده کرد که هدف آن تأکید بر هویت ملی، ایستادگی و حمایت از ایران بود؛ اقدامی که در فضای رسانه‌ای داخلی بازتاب پیدا کرد و نشان داد مجموعه تحت مدیریت عبدی تلاش دارد مواضع خود را نسبت به مسائل ملی و کشور به شکل آشکار بیان کند.
همین جنس از اقدامات، در کنار حضور عبدی در حوزه اقتصادی و ورزشی، این پرسش را ایجاد می‌کند که آیا تمرکز رسانه‌ای اخیر بر او صرفاً به مسائل مربوط به یک پروژه ساختمانی بازمی‌گردد؟
وقتی یک پروژه اقتصادی بهانه‌ای برای حمله سیاسی می‌شود
﻿
در شرایطی که پروژه‌های آرین سازه همچنان در حال اجراست، مجوز پروژه «ستین» اخذ شده، عملیات فونداسیون آغاز شده و پرونده‌های قضایی مطرح‌شده نیز بنا بر مستندات ارائه‌شده از سوی شرکت، به نفع آرین سازه خاتمه یافته است، بازنشر تصاویر قدیمی اعتراضات از سوی یک رسانه خارج از کشور، محل تأمل است.
منتقدان این رویکرد معتقدند نمی‌توان ارتباط میان فعالیت‌های اقتصادی، ورزشی و مواضع ملی عبدی را در تحلیل این حملات رسانه‌ای نادیده گرفت؛ به‌خصوص زمانی که مجموعه تحت مدیریت او در یکی از مهم‌ترین برنامه‌های اخیر خود، یعنی رونمایی از پیراهن خیبر، روایتی صریح و ملی‌گرایانه با محوریت ایران ارائه کرده است.
به بیان دیگر، آنچه در این میان اهمیت دارد، تنها یک پروژه ساختمانی نیست؛ بلکه تصویری است که از یک چهره اقتصادی و ورزشی ساخته می‌شود که در سال‌های اخیر، حضورش در ورزش و فعالیت‌های باشگاهی با تأکید بر هویت ایرانی و حمایت از کشور همراه بوده است.
منبع: مشرق نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682053" target="_blank">📅 21:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq0SRWXyd75o4uhCM-RszuI8IGnQ7aF6cg9g1hCU-rV7JqQWi6juGN1gjH67TD8hmQkU2nyR9DiRHZRIAxZur6U3RjeALwgHCPjm7yIft3HyO_JxYT9d1K7s_7FmGOCGpvO2Z99rCDjt_ui0XJMzarhWH45LF4uEv6mqBzCycY9s3dA877caFr6p55Y7a3_z1AjKk3GQR2WPlBEwSZDuOYK1pThWEJ7A45b_J0gk-ZesR3S3SwxYXYJjlVgo9TrwWkMFEeORfI3W3kshySEfXusrTwjdR-YguKX7Nq_5r4ur8ML2aBmAUICqgB4Agy_Didb9x368PX9cG0sU-Lmu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۰ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/682045" target="_blank">📅 21:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682044">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعاهای جدید وزیر انرژی آمریکا: ایالات متحده در حال اتخاذ یک رویکرد بلندمدت در قبال ایران است، استراتژی ما اعمال محاصره اقتصادی فلج‌ کننده علیه ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682044" target="_blank">📅 21:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682043">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان از سرگیری محاصره دریایی ایران، ۶۴ کشتی تجاری را منحرف و ۳ کشتی را از کار انداخته‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/682043" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682042">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
معاون وزارت خارجۀ ایران امروز در پکن با معاون وزیر خارجۀ چین دیدار کرد
🔹
۲ طرف در این دیدار دربارۀ مناسبات دوجانبه، موضوعات امنیت منطقه‌ای، وضعیت تنگه هرمز و همکاری در مجامع بین‌المللی به گفت‌وگو نشستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682042" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682041">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فایننشال تایمز به نقل از یک مقام رژیم صهیونیستی: اختلافاتی میان اسرائیل و آمریکا درباره امکان خلع سلاح حماس وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/682041" target="_blank">📅 20:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682040">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای مقام پاکستانی درباره ادامه مذاکرات پیرامون بازگشایی تنگه هرمز
🔹
یک مقام دولتی پاکستان به «MS NOW» اعلام کرد که مذاکرات برای بازگشایی تنگه هرمز که حدود یک‌ پنجم نفت جهان از آن عبور می‌ کند و دستیابی به پایانی مسالمت‌ آمیز برای این جنگ (تنش آفرینی آمریکا علیه ایران و ناامن کردن منطقه)، همچنان ادامه دارد.
🔹
کاخ سفید در پاسخ به سوالی درباره احتمال تمدید آتش‌بس، «ام‌اس‌ناو» (MS NOW) را به اظهارات روز دوشنبه ترامپ در گفتگو با فاکس‌نیوز ارجاع داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/682040" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682039">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875008b658.mp4?token=C-v0Lb1uX8c3GeStvIJrI3mbrdm58Ma_i0luR_28hmWKj4qFKJhePc9iLJ0RMENlIEwfnKb6B65OBKfWnMIsawlXTt7Tapkqv-3EJNuL97908T7cxCGC8QjJktACNTeGI4vqpxWl0HEqMB1XdnhD1nVypgFSa9ljA7aYsXpvhv1a9ctwneUbOkGWOK4NHtmERYpSg9vn6AH1DdT2m_fRyRuRwpy8-F9MG5G1kLx1ZeFSivo7eUF4ZXzRAUX8wIcFOGJqEyqEutpC0BfyGFeAm4eLD0pONo4YTxZKDUhoomFss-o25vn1uPyHbne68m5NYpN0zefLfTkLgFcs0lTZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875008b658.mp4?token=C-v0Lb1uX8c3GeStvIJrI3mbrdm58Ma_i0luR_28hmWKj4qFKJhePc9iLJ0RMENlIEwfnKb6B65OBKfWnMIsawlXTt7Tapkqv-3EJNuL97908T7cxCGC8QjJktACNTeGI4vqpxWl0HEqMB1XdnhD1nVypgFSa9ljA7aYsXpvhv1a9ctwneUbOkGWOK4NHtmERYpSg9vn6AH1DdT2m_fRyRuRwpy8-F9MG5G1kLx1ZeFSivo7eUF4ZXzRAUX8wIcFOGJqEyqEutpC0BfyGFeAm4eLD0pONo4YTxZKDUhoomFss-o25vn1uPyHbne68m5NYpN0zefLfTkLgFcs0lTZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده‌های کاربردی خمیر دندان در پاکسازی وسایل منزل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/682039" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682038">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFULv5KYg_DX6Uaznvs17RQ9g21Ri-WJIJ26a-lV2A3TnVwcja-UdGyO04PUGoaSXUgUI_1eP1_jisnPwfMueTbuRpaPE7fahVMrjMneY260zn19QtxMWyFvS5ViL6VrTM24Nqy_BqnI9dh7gzPE9AV-zsAHKlAh65xHTtg-V3PoPDNF_r7LTG_3UreerG65nFWJ08bppBn-y5n2PtuVV05ZUvWNkbOKMVU7YMn6Hi-J1DZHkPR4_oyAZ13jyHGf1T2x_ii0WYEaM4zkJuJy_lwOqDAKy5vid5FQFDxdF30WQYWoa52lgF-9BF6r3-2R7NfnhXB64ZHGVsy64qaY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان
🔹
خبرگزاری ملی لبنان از وقوع یک انفجار شدید در جنوب این کشور از سوی اشغالگران صهیونیستی خبر داد.
🔹
وحوش صهیونیستی اقدام به ایجاد یک انفجار بزرگ در شهرک زوطر الشرقی در جنوب لبنان کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/682038" target="_blank">📅 20:27 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/SgUfEcR3shLhuSwninn-34iOUl9mK5wKS_vUSoWP2bc_L2sa8XUuUN2fVWx4Tw1wylhm1s4xRWB1NrwpBSNubVYjyffUklrr9Uh62Gr2HX2Jz0Y4Xff2PT6pR4TJIizSSpV7HD3PsEIEiZkz2qfcIpFf-UZwlmI1xYjz-3RAIVD_paqDFWYxFzz1r9shUowHePLg4mYIHcSbhbnSXZo6AQhRjCVhRTMhs71g3ppbV6q5XHAPrUKRd9DW5J5_ts1t8FX7ycmHnTnk-hbkHJw7IaqIo7m270fgCHz2Syq-GrRout5zbrzgEKw2uNkBaVYIsDRGXuERh36N_s1bI2TYhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 22:31:10</div>
<hr>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6xRxFN01fZqAEiAMAnzas2hSpq5jYp-v9ObVRl0-OzxGGWJHGTbnz7CK-7kTEScJ8Wnzrf1c49beaC74Kjs0fSrYFKHyFcRAIc79LqmFYjC829KFse6V3mPLLYCugGgtLE6xwN1CqwuQVBGZNHl8Pfo5BBUBj8NLx3KEv_kJ0txW3BDR7C2kE3WyZaKYhxf9POVtQfNNoCRmCKs8YL2mlQk1Hc_cM7dcl5ktdron7V7q2MhvVlj0_AX28DAHdVP0fFEuiaOD6r6p7kkaRLOwbQpXN04eEwa0CrREH8oaabfBrUxiDjvUP4WpOzoI7OAImbeSNkEEStKmAb9R0f2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe8rXpSFObkAe_8SFkzFU2JVNtf-0ISEB0Vbk1_N181OMiOoNLYnHENKsiw_XfWvgdMqCt1sgLMOcjNH5Jz2BiL2JlU8IlQ6Wv0CWlW4WVjKEbkeFnQjlLoGVEcXxYshmxMOnncQ3OTplXDtPwz-fpXhgMm932j8bYc9-ifDtKGFr4EMdBSosvE1QIzGHauhvZgMnEjrSyvtO-OepVXDbRXoCPureJqcqowSuWBNOFA_1Xu0X70nVIuhaRpXwTvqFWbAY66tGKyM0kHP_o687jt54QbOGMiun3H_QtrCmuF1ZEHEKZ4Xnl1ZArCxMxRvV4kfxM6n7lrKqPFxYh1puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌دونستی‌امکان پرداخت قسطی می‌تونه تصمیم خرید رو برای مشتری راحت‌تر کنه؟
با درگاه‌امن اسنپ‌پی،
حتی بدون داشتن سایت
هم می‌تونی پرداخت ۴ قسطه رو به فروشگاهت اضافه کنی. این‌جوری علاوه بر اعتمادسازی، خرید رو برای مشتری‌هات ساده‌تر می‌کنی و فروش و درآمدت بالاتر میره. برای اطلاعات بیشتر و شروع همکاری با اسنپ‌پی، روی لینک زیر بزن
👇🏻
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/28692" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=jT6Fj1Z51CNnfc4z8R-sq6gPAm4gUpZM1Dq2AWKWUJZPylFH6vCLKDP3lI1DDdsl0b1rtTc9osZOYFhcRXmtVmHWH5ivD7qCfX05KpbcVCCWASpd76h4E6-MamgMAcuVtoIAQcDdngMSQCqwFzpDjnRLZ0kRoLJ3WIaQUe2afJ76sVnZM2ywKHSYVdlgOIDY8uocFhUL_lhitKM5pS_FH1Mh2awKqzhKS93_45LUllD7qdXgNbxFg9VbT-AoGxIv-SqZHQxrO4Cm8Cb-ZsWa3XdASgd_3HR8N8FelfZL3KXXp-bvBDNFN5g9QX89uNx42u7Lg95fwK0M9qiBNSq8kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=jT6Fj1Z51CNnfc4z8R-sq6gPAm4gUpZM1Dq2AWKWUJZPylFH6vCLKDP3lI1DDdsl0b1rtTc9osZOYFhcRXmtVmHWH5ivD7qCfX05KpbcVCCWASpd76h4E6-MamgMAcuVtoIAQcDdngMSQCqwFzpDjnRLZ0kRoLJ3WIaQUe2afJ76sVnZM2ywKHSYVdlgOIDY8uocFhUL_lhitKM5pS_FH1Mh2awKqzhKS93_45LUllD7qdXgNbxFg9VbT-AoGxIv-SqZHQxrO4Cm8Cb-ZsWa3XdASgd_3HR8N8FelfZL3KXXp-bvBDNFN5g9QX89uNx42u7Lg95fwK0M9qiBNSq8kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9zwb81LZt2mGw5IYggqPewwgYeaWu6MfxXwAQcZRbaZyFc84zkNPSAMcB0nCsP5UmIIjnoGQ-2if-cEOQRosEbIzxwQw1gs6oYJO9qbdH1VTziUDUt5-9hpC5omFNNfRkzeYYH5CS9UvXMtGDUr50M_A0QDFHerzeb3ZwCXu0kUjLLf7_P7ukxBtg2VORJTvXvpjgLnvsxnyLjKV96NXEstwOWAHQod9RBUkWhP66kWfkOydbFIc9rE2HW67HQzHkCP5fpX3AfiBUuzKtc95W9hDZHt-VF8IBfz3e2UldEBFld-kJNcQAPx8DSPh5_zBNmAtl_ykfLKMc_eY5APpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwiTpQZHSGQ9LRqdW9HdvhUKpNUPixIed26KMnmL94ASySifVgsKetHIhMzpk2SGVXVjAZirWfkG3VoXtKtLrRLrqJygKWQwEQUYsDdH1luWseJV0XIhAZBW1caqUtHjbhnGIvH7-t51Lg-Rqamzkzr1W09yHTNVP5Bd1SyfSv69vZmGRPmixqaUFCMu_TJsh6XxWAOVzv_-_mDV-vIM6L67jPJCRPdtY5ueOQt1I-OCpsmm7-LS-ae7mT1Qu7IwJXzGVaNmLRjgU_oNyRIhBBx74Rmr-wlYzX-XuNtakmNwGWEkr4UQKqa2UpMbFEMX8EBKJsA6CiXEfKuvslRODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW2RzCML7Qt5yaS09fFL-r8aJJGXwXSArUMa1q3P4ESMWrNwHs9TI2a2uVEYy7eK4lIJ-25YRD-hLkf4I4PZ7bKEpCJ1ENzs3aC9fNJAAeajUQg9UE4jzpyi9LSfCajqY-NdGD0uboxiDI-gh8GZyd3BwvYUSVl2kao54lcLIXIq53PnGVdzdn70D3ns1v_ckSIEl0j70d4OvwF2RNHhJ3MCvW4OsIGUnb7wPLrZGKCR1_bwCcVcf6lRzonfG1BRDIGpAMMmfJzDvwuMqc19YeNxUEkqdvqD9NeRKgY3geCQ-XEV70eIfXGH5BlI6BOxN-B08IBl9C2RbPZ9skgTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwIFvQz_uMg8nbJbeD9YWqwQ6oRlYg462Aer--v_4CXQK4QzkBGW2mQgsDmG_g6KTMjRodZAfQgUxDzIBu4mTLtbGFtLaNL7SDqi6QAFTjGgYYKVk3fiFM0aPUW4uJyBxDqOWqNJU3gswXAYmjlCQ23H9eADciuqbMEvepz_SNEA9FeqKZEHaoAEpEsOhnckZeQ0d0PsrT7LXSnXz5j1xq2fZHWXW8uaDnAARl9gSk4IKuOQOlb-60YeKNljBDbvDzdDHo01x4cUvI9FSD6ZGu3Kxkv9lbumoFvvFG3BfYzbTNN9Vj1Vbl8A00UAyMVAlTu7V4KTPYX_1Ti3k8MdPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urHvuG8BG7TNyXEs8ryfywTIMsw16NDWxLQfKu2YdDv66GQrbn4Y2mS_jporUznSH_76AbEjA0s6rPDd2mdKEayomDypKhANZymMR0M5NBSm6-ZGUYo50_f_eL9UICh0s3k-g0f-UeUGIYXqpxqQe3ibkzhMzcaIQJzcqOHpXNZbufU0vIjAqphI0oRxMOG798B9zN1_Bf3P5w56WT4SOO2_hDemxRiO2TsKsRyQNMysnPxonVTj4vgYH2NJJLHqXGZC69NMYRYGODvEjIoOVTk7nKGFfr2KOklhNG4qVj7nGzMk5ligVi1K3mUajygK_J9-ZnuntD7ThDb6hQp5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY8vJzw_x7ISsSPFguY-gbPcPFLAKy2BmgDju4UCkUhTi58j1JqldmNAjc9BIeBUCybryO4s0xpMF8z8E4AFhIkDMlrtogTm237ENxyKflLUIm3KTAvkD5aKwXGI6H6CizMBobyUHnE_QhVAwChenFYOfdTH85yYMvlZeGTUhyWb8UBG3bSMdSBzwt6N0KpFoRFemqaJRwN1msAcdJwGgT76Qru5hPFWnxlI9MAGa_TkZEKTyubmMU4fm-diEUPZxvYG9oWTngzWDG5bT4mmGwRl-m6_tBQRELUiEDsLD7ifFnQE5DlR3qWOTs9jgbG5d94cxLDMFF9WgnMCrxO-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=Nsy_1_fYeJjGHZCX4ZEqTgZWgMtcKgXTLlr3AI0I386g6qd1SCtawU5Az1pZNfi5Bud--iDpzTvsT9Q9exrKouOLRmYNkEL2jKyyR1zGOIwKFBTX91c2HmrW_tUXga-4cI6EAy6176PSD9AQE7TvQtlIERJhxmLdlVB2kdpDaNIERrkiI8hgQ7kfmD8Cd9kbzEdbJCYvj0HLXdyhzJQ0kpomp6qMZp1O_JMZ1XpbqAtfm0MCe9YNIYGR2t8yucxMYTKYkLMTuuv-x4abwGfexJUUe2E3ZwcLbDPxQ498YJF5jqKEpxMSmJuE9d2Io_Ks6IX75hmmqLSm6UAFLfXOKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=Nsy_1_fYeJjGHZCX4ZEqTgZWgMtcKgXTLlr3AI0I386g6qd1SCtawU5Az1pZNfi5Bud--iDpzTvsT9Q9exrKouOLRmYNkEL2jKyyR1zGOIwKFBTX91c2HmrW_tUXga-4cI6EAy6176PSD9AQE7TvQtlIERJhxmLdlVB2kdpDaNIERrkiI8hgQ7kfmD8Cd9kbzEdbJCYvj0HLXdyhzJQ0kpomp6qMZp1O_JMZ1XpbqAtfm0MCe9YNIYGR2t8yucxMYTKYkLMTuuv-x4abwGfexJUUe2E3ZwcLbDPxQ498YJF5jqKEpxMSmJuE9d2Io_Ks6IX75hmmqLSm6UAFLfXOKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVxdF22F_sB8xbDBMYFiIKEdeDXknzxHEiLeTYCINA_WXNMqmh5DTRmkejWCgWNk8F6KKbAdmNQcPoXnpoT_eDb4U_ofpAAUbCgxi4aScgfqKxPG_aI-fgDWEy0voBqpcAzsMVvZ1IzZYZ2ISVn0E4Ua3dpCkjrcziZZySOLMDOTSOvkkmfq9htsEAoENp8HQPCg3v7yyNYBuh_SGfmfb5lKYnEVK5jOTeHwpw2Vd_4Qa_ObW-XLPNgcQKQvA93Xck71PRY2A3o7R7Iz2oom_aRJao2Nwdo4wLLAY3lwdJSYgOMPiohsQV-X18BEub0DpTBWboWELq3Ug6Tb-WV3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGY2cQQoym6Mbv5IVD1Z4RVVr36DFOqdllDrPAQvM8L9wkIW_V7ctDTl0FPvdpg1_eM5e71F8T77Mz6CX2XYStAR2Ns_tOom463qKLACTh9ZOtqkpj7tAon2AScuGMTAXcTzmyp4d7ju4zuVvrGTEvAzaB8i_oiharzK-0-ldIFraMdqAw6kGW1HIdSJ_oA3pWNGdQvG5f9NVrBLi1GgZ1fbWSzrbGN_zUpTFKZ7DRfVTEO4UPMbte3no-u6rUnjL5gk4abApR10p1pXbzzY1GbllOobmpGZXKB4_9Kc7pfLNdk6_7wasdqF178FP79dhLhw_u9JIJ44tCCrN0cFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب با ۱۰۰ هزارتومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/28680" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh9EnJFhhR_8MVGqrqkuP5zqI0rdRPrntEvNj7q2S3pak8dymgSxQmb_5OEyMgjxUCtUwy1GTJez6llcHHSkmjaWAGl7bL23IV-fneozBSn-kQ1jdztxp0saAA5vaf_qv2vPf1x1Q--GfI4uYAqKSrsBoPWyaggdFTSMmKPYXqmT2YVmEB3Wy8VdXEAu7J6m1eX6jwElMHurH8oiPE91nBstViUlEWIfwBjVZyC7tqxKx9GAB4M6cycUlnig4bQHX5mApVy0E0k-7lE71bcDL-4PjqAM4n_7qhbdXGYN9scrdHvCR8-aTl22owOB3Q7BedJJGFoByCN7edPpkKxGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uzsJ1SzPR1QcIzvJHRUHeS9s3EetlGwV838oqL0HE9Jyb1nFnRrCgKUu-CuSlGiObbICIZECZK7Ya_wJxvD0ZxS0KSUhKubvk100JGq30aHioRcvo4U1Y7YYhy7kSkIibi3zDPbLHrNWEs9EooCkGVgfmiSx5HzYU1DDfCv-3YlMDkmUZG3esKw0ar4bsDToz4WjNq-NnhBjd3EU6XOx92_5RladdxUqu9sOERXljkMCkTObIaCMu8ePxX6_KgsII5mVsc5UBsKstGf3nV9GR9KaVpuzBCBYCGm1jyLvZx6obP_pwhrfQUB-_Cm6vpO3lk2w-4WjHiq80h5pKAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlDvNK0UDuqtR6g3Q2c77Y7rtBn43LJcpVb7I1CBIaD1kYSfeTERFUKZHwqTezu0YMc2mN1p4y5TvVhjbp0SnUZEEK0opEmP8JzBnrUPax1iB-fMFujUNH0zQcUFUQxV2ywOJoH0GXkvphdlLjL9stRf1Px4AgzQPzRURYjEMwTF_HtYgCbFxqCCSYToo03NfqfX0nJhpKTFrhlD61UkGETZPk6rRJIP-pMKkvQ89v8o8Plc2Q5YoBXLk5oLpoU8LzbFAW-kn9T81eA3ubKBgswghtSEbomryP6zbB3JN1YzmP1LXdPBlqfMx3Cof-_XlethZcOo8EDouPcYLL4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mavqbls4e3vJT1k8j_rplps3T9OjzEIUX-jLsrV8V3ycRXD9VjoU3L7tpTpzHgsmv_gdS-dDREQQ6rU0yeBNpE-O27DZj0AtO5AYRxiSw2VtHRgRUfsJyI6zq-AapP2E4uMyj8B7GM4pu7w4TRjj4FsUF5c3Ia0SkbmRFzYofLka2sE__kudg2DMu-v7m9UskUG3FKj6CQHH1yvnWhjhgQ2_NemFVpGSOyNAxGLR9AJHX5xJvrvDae5FcboY3VD3JquTjzZUv1XxZdc1zibQKyWSqZYdJ7NaYMfJfsGUesgRL9L0x6FK6TFFbZtFfdp_9fNnJnjOgMdrNitkySEWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq-zt1RVJGBiy9M8N_VNfWEUfYTkpVqySqVrKrBs9MRYb1hBeLT-tCF9CXrUZsDv4UXXcuoCJnT1lzVnBNdJ3kGnMX7BEXfdjzHCizL-GjEWKnMVFszlTK5Y7tpRkZ-QGXoUQg4VBlBdlaDYd6IMscCUA92Dui1T2-E_VdAvNr1snvjfRflMejbleYT8Mt9HF92CFHfQFbe28kkdJ9QmTFS5lIy8pBczIKFKmCqkgis0m6CPRE5B3m7Z1kw3SE7YXNJ8IkET8edWReW-Qf1pBLFBAksYB6vXjSHw7QPwgSBB8N9EQAATJSm0P3GSWQs9WIo822rMVSDu5KyUThVRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzjjsHhnnCzsstLwpRTVAMdRe5g2n7CA0g9bwOQ9lHzPBr7s5Y4VR1Tb5Dl__fzWFsqmVmNsKy8sJIHLYNOJqfzWrCiVD-CHE7kRhWSW3K7Pixsgx4P8_WaPFhUel-FF_G8uMUdimHRLI_deK8cE5NkRQkpo8JwmKynjJyblNjpXM1LrUp8f7oGw_sFZJWqXpIgbV_fJaIdnrREPsmg4k3Sl3FhUG_29zcChV2bE4de9UohpNSzZoyDL6JCk8rzf_SAEK-BtMohkS10mZlEjbUCjzeSsXZ8DMXTyb_Qnrdyjygs_2ll66osLWHlJRI_aEmoXTBzD-v8DtEsVRIvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCsQ8MHwbJrTt7XP1wLl59QAXOnRHL0NAm2Swc0Ggx5gO7jJb1uw9G_L24Mp2FnCSLp2iAKfCgxtI36S-hBMb6ujzJuRyT8bAPasrIaBlSh24JTOmHX8gDQKy2KT-WVsWyfTgopTQL91RWMF9TRUVwnXiJ7uvr2KlHmKnlI4kMHFRFlT_LkOkd1I2N9-ANPW7y-FbqusG08YRLoadE8QqodF9aMDZQONPA0nuHSgKfsu7F7dtcdnTd0RDGOE2OYVafwAw8ZY-Gw3ZKVsJxnyBRVNb5zZ1qnctiQMilmCNcHrHfWrom90DQabDf9_WuJefb4dIPJCigpwo4RAtYHnqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evpvrIKjbzyLCHI-IwIMBU5vgthZeBsxENf3qPUD3MobTPCK0x4A2SdrEDJosclhsflpYaGbRM6x6uj9nITOH2GF8wPI2Zrv4lrG5umuCKNd5FpcNy8Q-qtk5aJ6Rok98oQZUwdHEMaX4mTT9F-vIASAh1-2FgNUpy2-O_r2y1x1QgKiBvvCYEu3QxqzWyjVqaPJICulY3X4XCCMR1Wz6ysMtLqszK-00DnVWQvBGLndqcS6pJRJMEvawN03RqwsgLWxXxT8s2NN6Sq4vlVMLa9iOAlyle6yQuB1uCQNKOA6yx48nsYvlMZ8xyschRL--J0aOwp0apVfEOhn1ia3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTyK6QmftGFWt1HlbX2KlAszpzS1z7_VSD83NHI-oMCKGRBzjarBPjV4zlw6-h5pKo9IlfQBrWQytQyRtsTF3b09QWaLZRI9Y5cEHMUSI5RjWdXTw3z9-lTy44ZKWjiCB9pIdRXT2nOsjl3LROJrhGN-oduevkDIrnNu6M8j4pg75_1xDGPsZg_VIQ2FBWpks2-OYz2Wjb3bF2UcIrI2tIP6EW3jIh33IoF-jfWVSY0WpMQ5ptB53sKW_p2FgcbS2s_VhZ5ld7_djmhUBe588s7D8BDGLiVicZ_XTmTn72W_ErUuy35y1NuwmllehEbjfnNzPpGOfcyDnaDQuJczlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzVE0vahYMfuPgJqznV8oNFfPI6212gXTI-cZ-aXl2MWq9D08Yk1sZO2fGOaeiCV-18GnvGGexEGeniPunPd7zBsviFRbAYdivJxWmgvljKiz2T4eF_0ygTwGlCeulaW6u4GuIojneGEP49IhahJ7U4nn487bkay66i4cazknWogn5I8ae59v5P_WNsbuKNucClfSuAXpXzH61D5Q4O0-elaCWDdu47mduvBVgGoyuotDfBZDsi3FJ929KfF82dpMcdDb8CbpUKc-0yoOWnIHMz8P7yzkhQXlE5sqJQ_X9OeDCbCtCcc6yw_KqCVWqMqkuL9xcUS9zJJu36zXxbCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5mdntFpKMTSl8fHes8r-T4lCPmHFhoiiGHIbbEC8FXCWMXhZIP_N46zlcOqFsxoc6J9RB2EQDYunRRTSVtYHVOCOdPZ8x_VgyVtdXDblnLH_oBfnfc0Xymv6RG3RX0jT5q6Awm3RDMc1xwZ1MXagcwQU92qw6gLJJAk46AxRoT6qtwZxFsi8gV0PoHvQxK-BMvBB2g3Gz88WgZvm5d0JcHf7NOlyNSOgmZYZYQ3nc53PQYHtWWYlMfcj5IyPnxjxfWbi6625yZt-zgh5SfqXj32kEAbtDsy89xhhrb4fJKdXZZG-FKeVXvlA3mi17O2i5LUdOaFEuNexnAPNyz-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2IHbGsfYfgY42W2VzLGwldlRh-0BTCAq8cDAfCXJHDYuYAgLaJUZbOirk0MdI4qw9DK4v-rOSRTYyR7f2Wa5XWn-rto43pkl8k-Gwje2Y7g0oFBS9T4Qtwp2UkSz4FPkDamDILywaNPafyEOUkdd-HAyoPHldHZwAfAXq1QApvWPbAbEQeMTnuuFArjvVY5gqYmnBnfDurLh-VB_AfAzmEfQd2o2PR6eSYKFjkAenI33DGO8YZZbcNr8-Ky4w2vpm-s-CN2F_vI984PIj3ifOSDBtIOVPCiQbkiF31EiZcGx_GX35p0aJvKTOFjBrzzWwBhqs7pmEFuAIt7jNih8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj7lAmyRxd35v_T8V9dAn7ugAmw2AIkH6jkImXKrv_tEfMkikgxUQfJ4EpjWiIiM9WG14IsrkxIsF6Muz_b08adtiC_2-ogNEMt0ZvpJQeQx4-RpqVirt32fS7wQwNSXgPVgXyQOAepTjtMHAd4L68_roUuUfap_TpVDv4kUtppw8ogZ4mpMCAGSdKusGJrvLb1Mo_YvzuDKZe2K6THzRIuWUvgy6JtGYJeDzFzgzfFRqn09vK63gPvw1HIbxzGHEs28i4nbpVJksC7imjIkdYigGfWX7H_E4i_adtd7tP8gzfKvm04ZzaG8o4lWEXERyOfX7xrqFQ3n-s2U7LT2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhMfbwt7GHyHooPYANjybepy5mqeyMx66ErgLvnwJCqnEuLi3suVScWREX1Mzc_MYGdz8yNXSleogTudEjTMMj8LwKkXdCOda9puq1nghVszYnifW_CE_0gfDPbq_6OqC4ESNZqMu76nYmZPB-HkShpCMlqmO4rQp9lyoan3iCRHeQxGy6o888V_6jKOnJlQnKlFG6qyAiv2QaRUAeElyck1DCX6YZOhomR4Ho9vKQ37E-Uk5QycraB-sr-dvoeiWJW_87c2v_I5BeLq8FrOI-pRgPrm-R-52RcQej-BQIAtYL6Jpt5I8tha4jPdxP1JI6aneJTe_ctqF4uLEiew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSTTzgSWljDqPyMMbLnbcH2Kwv18fbZJ1TXD1NVYzNkWDBVYyTTWL4Okh8GN6SLr6kGtBV-36v-phx0BjCuqIh1L05H6jYzj-or6ko5HP92bF0h_wYamylx8oCJZ09_ZeXloUauiACLyyAaK-Qc79aHqqiaC3cSPEEXqhxQTNIAS0J2EadWJxBBwkWPM-1fcF6FrF4LOP8IouMVbvEbj0Krt0bFpmveLAnd4MxHdV_OlvGmAU8ATGWlB9LZ1IXXebWoaHcy4lviILtwlZ-MtuYlsbzEaGWbJLf5SnxiHzEHq7wIoG8T808VWJzNx3H3eTdBAAI1YWATcbIeV5rtM8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjDUbadaSD7pqeNBJVJwdrsjOKnjnq5i5LWN1xhHV2W1akAmwQ8HWgYWRSwMZhJ_XKBO7e9Dy_IulaA_KCGALIQCpOv_oplNTHvAUILfaQsHFuEk3nfVRkxRnl2l5AVtFHxZ6uG5JMZsa7K9zLyDYF4DSuU4igTMZdaL2c7ZOeJ0AiG99xHv6QvbQpIz-9OjYydcRezpUMMwJkQy-oE5Q-Swth5m-mf2lYvfIgYDFNbRj5DnZcUKBdFgoZXgFrwYqIXlIqFWEh5GH3mbz1pB9PFg-6t1KhtTee8QtECpJIFFOkyEbsC0CsiMDrk6xB87JbLKUICOBLoC4GvbHidDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=aAjOg63VabBmlOqHS8kkpxL9NJg5pyGBt-GT9XJWkX4RoE7N-6iZZmANqZx5Owg-wycENwla8L__V720d9APXt5XOeo2zQM-V0237dyQXe3c8BDqbgANSLib-ZC8WQjAYL2sLhrUpu5Vr2HexwHiXzRq1GpgFmye6mKYszxlfRtDYGlXo0CRL4wsBI4qA-b96af0-nEumReSNwSE8ibExNWtTGWkm87MxfOK-rgXD5a-yzsbb9t2kXi_D6bQEv71vjSO_DVBfzKkAUArSNMKa2Ry5s3ZAV-OoiQElAvLo2yEcdCMzck6OIsrpAkljxT0NVjIQhpKIG4nLB2tUu8hkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=aAjOg63VabBmlOqHS8kkpxL9NJg5pyGBt-GT9XJWkX4RoE7N-6iZZmANqZx5Owg-wycENwla8L__V720d9APXt5XOeo2zQM-V0237dyQXe3c8BDqbgANSLib-ZC8WQjAYL2sLhrUpu5Vr2HexwHiXzRq1GpgFmye6mKYszxlfRtDYGlXo0CRL4wsBI4qA-b96af0-nEumReSNwSE8ibExNWtTGWkm87MxfOK-rgXD5a-yzsbb9t2kXi_D6bQEv71vjSO_DVBfzKkAUArSNMKa2Ry5s3ZAV-OoiQElAvLo2yEcdCMzck6OIsrpAkljxT0NVjIQhpKIG4nLB2tUu8hkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=qPKy2jwsHif-6UEnmcLc_DBIs5-0SYqzn7xJanSUiR2yqPXxcLw2aIQNUIKzIf7_1-JTRVsdha-cQaWyuyS03u8FIM2sQwVn0p_4tEKDZVZuhxvvEmU_hPg0vgmF8XEITSLr6xfpINAQk3Fz6HB3xaILUvBPfUZeWf5AYcdCPs9VbWNqlr3qGXs-weGyEYO8Vq5Znm3ZjXbrEgkATbfSvzDGz_skAMc4d9sg2p7UnLA8xHAH9B6d_fLr-tctG8ZxSCZXAoXJoXEY-pEl3qpsIlk0zFVve9xA-aP_hzdmos5S7ObSM-LClnIhGR5c7Y5KZVV87eFomdwF11R6i253AJQuej2eq3A-2-YUI7d_8gZyIBmrjFJnXBD_WTgJC5djGB8DQCsU-r5BW15-aC2PENNRfoGVs6uy2UMnW4DaoCGlYIGZ_iHs9mZudcphlln3DIMTjmoQPgJ7wUjVmjnPLcGNQ9sr76Cu08bo5-tgfzLZBn60uOxsaczrHHiKmnpysTD9vgPy1sWWggWwCyaXbUm0oaR57NsUBBJBoXcS8OOnBmY5Aw8IenfKrFocbV-nqShSNaalBmd-0Q4QZw9sRo4gJkNdaI_KMjHNnKwyHoH6XjJvf31vC7gQZL-pfX_OXsmcTqf48uq5YU1bcZD4X5hMvEg67XTvBDJplaSNJjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=qPKy2jwsHif-6UEnmcLc_DBIs5-0SYqzn7xJanSUiR2yqPXxcLw2aIQNUIKzIf7_1-JTRVsdha-cQaWyuyS03u8FIM2sQwVn0p_4tEKDZVZuhxvvEmU_hPg0vgmF8XEITSLr6xfpINAQk3Fz6HB3xaILUvBPfUZeWf5AYcdCPs9VbWNqlr3qGXs-weGyEYO8Vq5Znm3ZjXbrEgkATbfSvzDGz_skAMc4d9sg2p7UnLA8xHAH9B6d_fLr-tctG8ZxSCZXAoXJoXEY-pEl3qpsIlk0zFVve9xA-aP_hzdmos5S7ObSM-LClnIhGR5c7Y5KZVV87eFomdwF11R6i253AJQuej2eq3A-2-YUI7d_8gZyIBmrjFJnXBD_WTgJC5djGB8DQCsU-r5BW15-aC2PENNRfoGVs6uy2UMnW4DaoCGlYIGZ_iHs9mZudcphlln3DIMTjmoQPgJ7wUjVmjnPLcGNQ9sr76Cu08bo5-tgfzLZBn60uOxsaczrHHiKmnpysTD9vgPy1sWWggWwCyaXbUm0oaR57NsUBBJBoXcS8OOnBmY5Aw8IenfKrFocbV-nqShSNaalBmd-0Q4QZw9sRo4gJkNdaI_KMjHNnKwyHoH6XjJvf31vC7gQZL-pfX_OXsmcTqf48uq5YU1bcZD4X5hMvEg67XTvBDJplaSNJjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PN3BwWcwWwMtH0b7QhyH6f9QD_cgrJtO3jR05UyrobHFJKr6_6LM3pH7a9eF_4nNBsQFPBDxNAOA6n3zMZHl6nwp8hfysm-OLTSmooFoqilNG8k0Sb-mXzN0b67Q4rUVz3jdoyESE1uBaHYQIfd4BWyA0981tcyjBRnyNjPEcqqiMoXSESaPbwD3wqG6Pf9Mx0WuTE2BN67cIhOLSJielPU3DCi0-7LS24NuW5koUIWfOTjoQ-r-LWUgAHesJ3EGh8RRzw3S9ED-jtKvG-Q1FvMD8zm7II0-AO19Mbk00cRnqE4m_svbWZ9LvHN_OcQ26vdXwzB9vv-kynnlFecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28654" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeHUcSyCh-cPIphf5_geC8155R2IoVKbx7Pe_fztwo1-x73zrs-wiw3hgIktZn99MWJ2zCIvEM4IpF_SmH5zhL0GbVTzy6xvm5dNQSHpXP4nH3kkDkzi4akxgjeqxBHHYngm7x6AA2Q_wOexyqqI8Fh7E4VEYlSh3dqiVX_9b5SiZ_Z05m-8UAo7-zAlu3Ie2Sy-NClLo4TCHZmWTQV9JLzwOJEjH_tBDuoMzus_wWG6bHTUI_G_CbGU2s49u4E1uUu3yiml6KLhJq9IaD2BgAI66ACHBMPew-tziwi6Ic9yjo-Fmbky01xPD6-rNHsSiwklN1Ps_YlICAF_hhA64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjVvj9UUia33sgxvm6I1N7IBrok7MRlFK0oAZ_wJsNPquhnUwK_rboymaWDP6Xyh6xk6kFCod9KNzrXfNK-aCQ-bRJnCs5sfp819jf4g8Bf7uR2YwW9NAgaFXMjj013vm_Yzs-TlqNp3Ruw_VKjoKhKpMU1FmygORKSX3FMU8i2HafxtY6muZdU3Lbwn644xrv4ZgYI0p1LY749n2RCAkCrSuh9oArBSffu0GyoaOA2aV4iEMk3E56g5aYGmc3zg-9nSozpE0RPJS1HyqbFZqnyFxuE6lULI-e9sHC959SSotFx0FxqFgU1e3PBZGWoz19dYJhtdH-tJR233soWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCYaLXw0_VoZZue91u0y6bvpIJ6cC8qVtjpGhLyILdS0vAZaiLTx2AjouWAR0Ya1ofFM4mfAFi7i1ltVRB_72Ttcvmhq5tXp4TGaw-nrK-CuipuG7wdX5T4JqLly64FGZ_1kmicMaytljes_0nf-yTdh5p6KoRAWJ7Wg2EtuhsDGfUw6sGjDMJYfsKV7zTvrir7qafywSIqy9XQUt4QOg-NqKOG9Ip83k3qXUZACiZeRxiE-6igY7dg235oaOGXEIb0jZDoOwD66CVNmm1BXKruVGEUEGcfZqJ4OySG8_Ywy-srwL6Gi96GQCaemX8ifGvJIcbqaS83BrvEobVosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRpMZGeSY_gyVj82YAT-dHRlWVY1wuUowtvfZyE6s8nt0rUQPYckadndr3jWO15_b1qno2H8AYklpRV7RUTFqp4y2HWdmSXFrvk9dGLXIaWdSQudYVYIqDk2B9t5b8J3yy3v8ivwKWYol88kBByUxkVHdLLSgs9LieVaVWpUD__ZCIJEt7c0U5tqRUvovLgvCZKW_xpcoI4p78jaVCjSutxayCm0EnUYFkuQAX_HdKs-OPscuu3ruKXJwj2qBYswksKMpLKKJYNMAR8CcOgeODDDdI7adL5f6QWrhnccsNTb0ChdWVVsETbhyhORJSXuViGTUVagAoV2S_W7syZtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEPzhq6OKBo3a3hi077DTiyN-1SEQOSloQdc1Y3wZ9gbBLmpJnWJ5reKBEjhuSttpVNIIaYuoum5D5l8UFfIxEjvtxj1Pe0iB5cEsrJrNUZAslPBC91WKE4-hCuk51_HtR7bH8D7-SANICi5FPD4SHsr23ZB04HSTJxytU1WkQyewmDRYeFFoO-lhpNxBl0imPpLFnQeprY6m0_MDWYt3M2Sf9To8OXcRKuCXhK5HDkVck2JVIu7-SpDnA3bywxkHbeuDeaRY8juRokkzE2ECfZUluqnZ62x1hZ_HhGq0s8m3jVjoXoRjZgNQgCkMb-TArLNFS3EKPWTYSvzL3idSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8liOPhALxuMaf2PMeC9ryAcqYVoSUlDAV0FH4UVc1XVRyA-_f85rogLHQBc-AyoSbWaC4Gz1h7h5thTB2qCHjoRxONOETRWsTYSxy360ihHsORRvNRWled47iYnTDqbBUe7FsZLjOOz7Os-pa-9AYP1s49tL8q10SYxVTaLeJCZvkBldKUpIVXldGkU0taKiBN_N8GDRHFrSYmmZWb1k-V-35J2bygn-VHVedFllyADdmDjHx4ljJFAqyt5WM7MxqA5NClama80pWgk-jTfDMyBjj18_BahbUzSw-_QvVbx2dWsI_G5HuZ74oF-dQpUXgPNHLMbMhv0W_BabIcCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nspNbG-okgTvOla7E99KeeJT3wdUAfLvki3H-m7APCJR6S6N5nZYxeO9oFTw6pg99_HkY0ghAhMxZP8fH8MW-Fpw1cXs_1l7i4-Y4jXErlTOK3hHZGO_HQoNg3WjznMOnswSFfOL1JlbkqitfUf4QqYYDl5oZ7kIrp7p6ZC2-X9iDZkI-25HrpPpaeSUH54Fw-XYXDolabgAlqaJs-VJcJ-N9xdlGrxEB6JPIFc953PP5dEQqH5CtM3QdFRAlBV_UYbPjNIPtrG7HXd3zGkUoO6KyfDUtBHhdp4jOxh8U_weQOKZjS4JCKt2cDeW3z-tjl57CpEKomF_IHn1rAgClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpNkTrXo6fgiP23D3QRewaYtwkwuEA9ADf1l1yfZ3bYaHltUzj1FZFvIxc1VZICS9gAIxgve_xZkRZTptECjxAbzUNOJ9-7oyMzRtTAv8x8H6aD-sMAUZjH4-wwR2mOLcCT4BZ4IbnDjCegYebCUZ1VNiYeJoKuiWjopID5eYrMNotKi0uursULuwXqA9d4CorzefNUq9isHKW79pifFz4Oc5iziKfW7xY7lacCZKvEFq29IJdAU4TqgTibLtntcUNpyIpW7QozkHsm_CkjuJplLqbqhPX096Ui2LgTXsQjcpPXftqGvjW85lXYN9Jm2itbF7YW28h1Gw61Rr_NFlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOIvlNmMLZJI5Pft4gO98ZbVNCtBgPc0nFQ-C7kZ_sgHKKDdzyh_gt05IYhnzBOJk_n79OmA9K847_NSCP7-33m80rjPMNHCezPhuF7mtkbtoF-OHzCDxz2cv_bWa2OiZZBH7JHRke7TNyzTlhEQsff4xhmGPQ7X4rcnPriN5ZQksw-CpPbiSP3mVdtxrXI1xvelUGakssA98YsjFYIBbeTxLtgGjyaYlUy65is3pcpdziS23qjHtJjx68OsHEL9AmBnl3OuUPm3oonRisq2rOg5Gk5FOB5_LwhzdFD6rwWH2gRvvvPSUimqm2LK9vnKoeq2DRxB9V5rALBLYdYv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFkstdEM1-ZKRNK7EsduaD0tCbeksPf5obi_i8XElBY-H7f7jf4IL31zTtow14nb7uBYxGkCxdwtMovPVgmKS970BIuS6JrL3QM_Jffm8__mzk58Xm1CuszjP7bAXJzkQwz28OdYhNRCHt5_A3xDwHj-03I0aF7tI4zSwNh4qGnXIaDjPSeu1hM1U6pIqhIkFHz9eqkseDxHUH7lCFFBkE-QPBq3N1Pyvcyv_Co19qatrp-iZ1lHxaqOTPuecrL2D4NS7aTJnhRS8qljbwSc3H8s0Gd7GJ2fm0S7I4Vm1i5pyHWDUBd2_hB7YAA5cKOSL88v04uxLnEOm1M56jOz6wUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFkstdEM1-ZKRNK7EsduaD0tCbeksPf5obi_i8XElBY-H7f7jf4IL31zTtow14nb7uBYxGkCxdwtMovPVgmKS970BIuS6JrL3QM_Jffm8__mzk58Xm1CuszjP7bAXJzkQwz28OdYhNRCHt5_A3xDwHj-03I0aF7tI4zSwNh4qGnXIaDjPSeu1hM1U6pIqhIkFHz9eqkseDxHUH7lCFFBkE-QPBq3N1Pyvcyv_Co19qatrp-iZ1lHxaqOTPuecrL2D4NS7aTJnhRS8qljbwSc3H8s0Gd7GJ2fm0S7I4Vm1i5pyHWDUBd2_hB7YAA5cKOSL88v04uxLnEOm1M56jOz6wUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلزنی رونالدو در بازی امشب النصر با التعاون؛
این 978امین‌گل CR7 در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsTCIwQ6deQ4Ik8Np2a9oKncobS5pOpSTwNXDj7mctJp8UiXAsT9xI5WnEdoz5MhrCyeCHLqWyh4IZIrHo0_u-gQNHI_5JrJEM3lPVJhTLyUMWVD6kyQtoZWoKpA2qdvZaSQ9LbgK1RMvEeBj5Po9_zgwpq3vyXxEsek5Zbj75rAK1imuYm4lZUj0Ha8rSNxfbW8hlSeUhBGWztb-6QRvKwa_7dHE1rV1lcIWV0ijYNFE27h35PJCoxlvIRaXq_Bfi4QSYcHgOWOGStC9qNSu1MK7SBS5LWitW9OwWO00o-vQ2y585AdRqcsStS2GO6HdLzlFNiD6y-tb5SsTPEBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YafQODvvifPuK-6LxEjODkSfClMqpJdI9OYrUqFZya86bqBOfoCy0lrt_gHeszxD8OsD3CvmpQs9_Y5Z7qqHohhBIh0_G9cy4qOYpcpTFXaBonOxQEx9PaqLE8jwJh1zYeVXCyQD2hWuzXJIssOStVzMhRumRwe0Z_1eocOEljsgb57eP7AjxdGLOkQykuZWZPQsKDtHHlo-YmZTMIGD0H4m1sbKYyNsCLHkojZjCA5N5xZVUlaM6l9YTnmWCzw4W9ASDwOfg-qpPS0alOtIy00SxDgdnxOv-WuN3fZVmR3L2EHjXxy-bWC4YPw-ssRxuAAy3Syw-5g3Y8pZTkAR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17182aab77.mp4?token=fgMWG5sJOG6XqWXsNaRCjL3AJrv8U8KOztwucABzDBlQAPMOwR2ZvvuCN2pbfBR5FMkvzCon0uQfvlX-c_tvXpUq_HUGAQuNGM-3fSyMSioRcwj6wx6d3OUwaI7RgLkqlClOB9EfXeX_MNmqiiqDgEb_OxozgwPaOQHR-mgKbcNcJdULuimeIOSvXRM1YgiL411AiGNJOkKQiPi91BhnO2rlnMKE5nf9pt3geuNRN53KlxZ9yA4XqMmpANtrkrVmUUl8o1OBWWGFeqL6DKrF157VE464noB8qodvn4BFBW6PxxmU88WBxSmO01jZZAcB4eIwhPp79R98ARFzmgJv4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17182aab77.mp4?token=fgMWG5sJOG6XqWXsNaRCjL3AJrv8U8KOztwucABzDBlQAPMOwR2ZvvuCN2pbfBR5FMkvzCon0uQfvlX-c_tvXpUq_HUGAQuNGM-3fSyMSioRcwj6wx6d3OUwaI7RgLkqlClOB9EfXeX_MNmqiiqDgEb_OxozgwPaOQHR-mgKbcNcJdULuimeIOSvXRM1YgiL411AiGNJOkKQiPi91BhnO2rlnMKE5nf9pt3geuNRN53KlxZ9yA4XqMmpANtrkrVmUUl8o1OBWWGFeqL6DKrF157VE464noB8qodvn4BFBW6PxxmU88WBxSmO01jZZAcB4eIwhPp79R98ARFzmgJv4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛ شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=FGFzCXrsW9pzpw6p3iUZv6ByHRmRczChVkdS0Z_ItQ-bK1Xo9Uh6ethlfoFCYoKefuKAPyyQNNfX3pZHLXPrG9hlRpP6S0BqYxYnM1PyinoTxLlAqzFeZ7vXvd8EofDHyLLKpFnfPa6jTO1uZwg73yTuuW5eqn8JIella6hNOd34Oa_0qawjeSATuunMixLQVpne402kdtzATzo5qyDxD_mbUTo73LhmxBiaD6m6dOX1dXmBc7UqXbCv1RIXir-3333BAZMLcN_VbLmNDXWfRXnL8x3GqxO7y4MyFxXKoIrGsnRuO6ymYo9-PeKSAMkjdCEZ1ou8DwvxSq83q_7bHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=FGFzCXrsW9pzpw6p3iUZv6ByHRmRczChVkdS0Z_ItQ-bK1Xo9Uh6ethlfoFCYoKefuKAPyyQNNfX3pZHLXPrG9hlRpP6S0BqYxYnM1PyinoTxLlAqzFeZ7vXvd8EofDHyLLKpFnfPa6jTO1uZwg73yTuuW5eqn8JIella6hNOd34Oa_0qawjeSATuunMixLQVpne402kdtzATzo5qyDxD_mbUTo73LhmxBiaD6m6dOX1dXmBc7UqXbCv1RIXir-3333BAZMLcN_VbLmNDXWfRXnL8x3GqxO7y4MyFxXKoIrGsnRuO6ymYo9-PeKSAMkjdCEZ1ou8DwvxSq83q_7bHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
ستاره جدید نیومده گلزنی کرد؛ گل اول تیم سپاهان به گل‌گهر توسط کسری طاهری در دقیقه 6
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTsmVeIdDcsjiU206Y3Y81yX8dLZcUey_XEG3FyCEBbtBsyNdrVyQIMEm-LvQMtgGX84LLyuWiyqSpWN0550P_MnIZUIBvGzJjdM_QHM5EmjFJAP6kcOCNPwsQKSZkyzi7B4VNufGDiyEDkPP-1tN-Kn9hiFxs-RUUeYrnyKqLuVmQCZuxrTei9boTJRusNanptp_3GN6WM14bJ5mUnH1WPE9FOtm4yDp9HWKuh4CbcKNM2c4lXA4toY6GScHtIbkJn3Y32Tb1Q5ixwbmRKmdizSF1RU72YKjHIE7T958ubo8qakshIUyn3qqa3lYvyREP2VplaBSOIe8fk9NcgfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ8-0R-jSt6luBFfcGdt7u1WYiHChqxCNg8w2PsUlXV-DpBNh5ecqFyuUVY9iHNSlPPcYWAAlcpOQePt5lpFHv7vQJvliuhuDLVColjHzXvCFxwKwcop_w0j7rXPvNKPeCQZSmT5MbPCqGpvs0xIFroha490I-umCqBuNjgJt7g63r0wgico7obS4ITOyrx6Poa4271n-XbTMVJSNXAxIJTSh_wnoMuyG5ixWkxTyQTFm6kvitGTLvHB0cLZUj61eCmTFZTNG9erVkgr3bv8Bu5pWq_dwm1iBzGqy5q_QAEpc62-_koTepu92dzHAQGQtxLv-_rps-FkG2nMPGj8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2F0M-bnZv1o9G1qxvhZpz8kwZDmPqyQSSeiUuDo8R8QxJNeRLKqsl4Mf2uEqmfwudTjp5zGBQRkBC6YRJW_tbts5T4hlUtuhBTTZS7GbXc53VVon61F4WWh9je2XP3fzDQR9KPrL1MOcGkn-Ks5TO7DFlAOi1oRcKup-4aXbjVq7iLNaYOJM4NRKgfIOeedYgayau_nB3dLCUTaWPzvo07bnsaJxH5_RMfIZSV2CbAgXXfefMEzJQAqGx2Y9tnFSh52Z90BzNQIydZnRqBam6658IWnRjAG6gHbvqBfiXDtEQmgWJvy3aWuoVJ0WCH3wAO4vNJdWqRjfn2sWBcoxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=s6K67s9X-blyzMP6NLG3ZkJ_VnLWP2A4SWpwfO5PttPCOTAgvyK1dSs3Wv39mP0alGnRzkA-n0kRCOLLwG_9pVaw3mmGetqvUdQCUfz1nsHtw_CFWRZNas50fmprnp6Fv3nzDIP5oU1CYKWt8ZlgILszqNqEIYx5dmCq7hi8QjTx-zvJvUPMkJjOkjm9aWpFzjv6nqmkZ9vUCEsPtHhST8FUZOabrl_4EHsxEY6Sa8EyPin8LKYvuPR1lxZ3CSw_baK89p2X_6jYN7AZo7wTQQnPqoM08gtDlhUERd9DJN6imE9QZ5B943wAykeD8iKMrbpjewXX9fdE0_12aC8wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=s6K67s9X-blyzMP6NLG3ZkJ_VnLWP2A4SWpwfO5PttPCOTAgvyK1dSs3Wv39mP0alGnRzkA-n0kRCOLLwG_9pVaw3mmGetqvUdQCUfz1nsHtw_CFWRZNas50fmprnp6Fv3nzDIP5oU1CYKWt8ZlgILszqNqEIYx5dmCq7hi8QjTx-zvJvUPMkJjOkjm9aWpFzjv6nqmkZ9vUCEsPtHhST8FUZOabrl_4EHsxEY6Sa8EyPin8LKYvuPR1lxZ3CSw_baK89p2X_6jYN7AZo7wTQQnPqoM08gtDlhUERd9DJN6imE9QZ5B943wAykeD8iKMrbpjewXX9fdE0_12aC8wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=T6WEaUJawQaqeb__SoX43NDH3Zc50KILci0g4MZv_vQGiNp9J8mSoFwIwGrT4rjzTQne4L3MJGEiVuP1jP8GyhBHyoyyMCqABEf4jOg5bRP9DcGUct_TLROz_RwJJLF0i1x3Tu7VRdShCkRMvWVvMUKwoVQ6Yv9kkXddSgJU70J8UTXHlj936SNz4b3nljFqLem7YFI0bNedGcEuLsxkVkOZVpq9o9JWWviRLZzftxq3MoPMyeVICdU8ySA5_1xO5-xyI46kguDx7KhoDHfJxU4q52gKjAvr4nn3djY6CFAwejgkWjQf0EkJZWyOoprhMkY1dtbWYTI35QfBRGArhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=T6WEaUJawQaqeb__SoX43NDH3Zc50KILci0g4MZv_vQGiNp9J8mSoFwIwGrT4rjzTQne4L3MJGEiVuP1jP8GyhBHyoyyMCqABEf4jOg5bRP9DcGUct_TLROz_RwJJLF0i1x3Tu7VRdShCkRMvWVvMUKwoVQ6Yv9kkXddSgJU70J8UTXHlj936SNz4b3nljFqLem7YFI0bNedGcEuLsxkVkOZVpq9o9JWWviRLZzftxq3MoPMyeVICdU8ySA5_1xO5-xyI46kguDx7KhoDHfJxU4q52gKjAvr4nn3djY6CFAwejgkWjQf0EkJZWyOoprhMkY1dtbWYTI35QfBRGArhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8S6xGcG_J7betvhKUfz4YT6LgtNvRCJE0RwFqE3WHuAcAoHrGHBLDc4qOeX9oWWfboDjOyp0jKN1a-2Utln3gTTsGDHtqxEQVsRCrgMidlE9DUqijKuHDBPIXfBJS41dybPWXDYfPlri6KOhgj8l54XiEJOW11-voeE4JNj_esfBasTsvX9nfq5LaS8cYUwCjNjdfP6rvj6rapXsEd-GYg8-MiBcjRfx9qlD3LIHrCh8Rovkv6lo86b3InJrqFAn4MccmfrMHXJJNVxquDbzq-zBf9Vh7dmOkcHwlrCarCWy5FlfiVDYV9V3EBWMpXiv42w4nDT06zQLGmmNt9-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ-FthModIYDsSBhLXaRQyolUxRoHkenmTNm995wOrCN9xLr6wfvMeXBaJn93q_TeH5pWy-BGC6RffiQpsMXeJRV-DstDi0c6xdB_F5_4YzY62XZzgQ4L1J3K8Ks-KFJeiq_dooiEsimnqp_anAi4MtjQuxdM3ojkTSWSTbjGUx1KdcBUVR5cHEQmpVTIquzw_VKTQ6XIBVp7xUJj7aWN0imQoF6gDheYFqEL7NB8EGU2ViFZQSOt8R_eeUs-xrGJT3-f28z2li2bsvWpLWogf9uj3a04OTZ4a8HqyF3BsLQ1Bm_GbHujP_BouQQoL0ASFkPlI8uxd9aiV1eQcLHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unkVLk9OtyHpRn0_2m3dzHfT2HFmRplKZ-voztg3lbp1xH1X1prXHZRTR5U3oFg2QG2YRvhi8UUeQzUeHFephd_DgpN4vYVWQOiuEWlqvyIuxlXa7uXxhtVSjZvJQdPCAjNYa0_z1aGE62fqr8uI1ZnqmJ4b2CfyvCcFQNVxPAVkAVkrf1s-y7CmKXI10iEQ-xNHk1N3Josr5YWPRZj3cMSqDYA4xOWhrbuSkDoiGRCd6zlWeC2mhp1YKanuZKNtAQ-ss_AD4BkH8vH5f4uVMDQhz2qZL1ObiTilVjro2fjUrB2QFGxoE9-RcS6Vq2379GFdezyV4lnml_hYrbjPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3NYLAUGZN33CeqFMrQqyi_20IIGcSDcr44uxPTGd-Ddfe2ffblhuw1Cr5ca8jE6K2NIaD0OXJu1fES-q3QTFnkEUtZpZ0Mnkv1OjXp9CMrzlL8EMk1nonWgAoPtCp_K9Zi78y9uC-dGdDUmuCEAWNT1eKAAvk_3bJWkTMNNGB3GivWIy_jC6oJwj_3xKIWik12wMCtX9dHVdsoih3MjaZcNSNH7ZZVvSfNf-sj1IqqtvmYO2bPSqUv3rT8qL4nR5_MHP2hP93fthvQBOvz49k_lrYvD4J0b6EPLWWFsCDXLBttbo0uUjkZ4duQ3fiVR1g9u6oaJp4dPl2dI7nW5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwxtVDDJ2uVBu532gaYRXbx_DqQIwaGZpPXO0-5KnfcNOmQr60NSNVnkrXym1XPK4-ZTCmtG7NCbtHw1sAwrGEGXTzJs1uqOE7-605Icef09rP54riF0LE1cZ5Rr7vaZTb6h5LrztO7cTSH_u5wbh1hjis332qJ5ImHND4uC-z-BzYXoWWzMnKe6z17Oku0bDd6cIWUgv95l3LbHStwOVTLVgMaGEWuA-IS75my-6F-lPdKMy92VjbY1tWzxnT-Jiu-gSveFrGLI4vqCr95gW3wh9-WwrnexIuBH_ag-ndfX0T8wV9IS0tgvmBQy4xkbCKs4M_DoYBr-2IW3XX1pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyNOp9iY9Nu1t1Qsk4GIFktFf7xbzQUTghmKJV0Ge3PZWeHbJlFNpcNdtdQRDBkuxhw_VRyCqYCRnQIwR6nn7hASJ_N1gGaWPfTIEzPws5UjOOo6_UbvVjIRdc0r5HjLAoTvz8h1fqcsUaeVnCwEqtzggFEOYMQaRtUng2BfMX0ugUN3yB7XwYipJioZH589VPr_qUFfW06CLY87dbvpVYBnCM0gypgx9_npIrPj0qzsGqE4HttFIQ9KEZHebtqJLt2AuQRBPknB--Gyctr5RMo-ZhLNR4NUQLQHoLsuUXzIS6NCPlMzyldfhcAAgpQRP1GvUxfbJJe6dVR0H9x6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bs_AfcBx9E48IK2XI4ShsjH-6aOQDzfjwbqUqOWEQplftxzE2qPTxg5WCXswIlNhvmIFTC5392G6qXIY7ymDezqHtOWaDjH4ZRTRGn73G_IQrqyleXtVJpiF_N_K4ZzThGsrVxbrlbdarpGs10wXmcN2j8s495u_Er9-oZ31fSYEFgnGHpP6jc6mCR-c1rJp2ECq5ek-x7oxDNAD1v1stvfKTPkgVpbjNuNt7vEqW3-Fr_1IPKUVW4hRGvsP7fpQ95WvDCqC-VLuDlXyEZUDD7HQa6ZJ30psp8FTKxjbNkTARChN0RKwvrI1LQhin4CKN_NJNWvDaRzteHwEdQlG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTMlTl9wGfP7-fJP0tv8BgJYPqkb4z4oG0z5zsLfoN50QmJGR1Tg-x3Pj9NjT-Q5wnunFuSN7GxxVWtAtDzRChjUmpMR0jnqMkY3Q-auH4iH7QpQeJZirl7V55w9J6XiFQ9q8iOudq1DCFw-KHfWY2TioJDqGRG-vsqgXSMCiunRvjN05f-K8ey_WF8mTcb8Eo3gx_DAIy18z163JBy37fSbrHy6_jYJ4raz7IbCqbZYaDachGYhrFjbdnWI_sxDi2ZhIhrJb96DrNvJNLs5QP8gjsUnll-DhBIUo8_SPoemtQrK3nd2o3iLVboGnqA9gj4jINKq8jQdRIEIac7jWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwmMp2li7zGkUOma_-5mFjt69XPb2Af8DstMKLf_y-s7aLSqXdA9hBFT6uI6lUvhjvBNJlBqMXjbiGqDISRLtyHe4eceVAj7zZJSkMnhtkH-N-jy95_CvOauH2538b46xs6U-ljTM051qWCdnptLvNnAaq2dAlbdh7kZog6_AkIF5fIzHzss6m79q8qeFC6cvgMvN14yenzJlaEH4t9YmWmwPE6Oy_hzfirOIe0LtDRoUSValVcKwQm4ocOgvoUw1P3QSzbgi0T0QiZsHpvEwVf6-fIr3eHrnlgjMVx41iid7e_z38GEM8DD49vkcejeRncaIr08UeG5LOH7l2LS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dojPIYoNJT2CeE6bYqdouNqze2povjY50BouFpXDSc11UOvIxf5YQBATvvNQLqD5BcRpfKMErM8tS9enA7GLNm3mXULzoxCe2VFNCX08yCm2P2kMObFyNEurLvzF9GGrw1lJbUdwpUF7u-Em4BfzpmtIu17guUqS6Mh7bLVpcYenBdQV5ohcNxj-NuHcIvTWBG2IacSsVTtob2jIuT4EEtwNWYkOEJyRi15owaA2p_9TlJr8bEmnQd_uqLbjzLqRSr1A1jJrcb1_l6gWsFW9QcCh1ZuY5nScg441iML3tyzxTPQ8lpyQxN7rzu8Oz2on5XiONyTcgj6a4bzbizPu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIwK5p0uFSIDS2vvqGI-iJenDCht15qJL8fdHwG7hidIFLAnbEiWDs8laPZ3_k3Dk-x7QGu_8ojVr4s-nf13hg9bAMGdnMXuqpPaOn1dcA-56Z9xgOxXZJ2sofEXXiAISfY9qnHsS9_vFPBOMVRE4X0w3BRfCuAiQZHaJeVNJAZeF_k1imR0NrH6tcDdL_Ar41CFvlO9R-aaIj-KWDTryUOJ1oyJUJFjHZwFLm1JU7nkLD_oQSwYFroVYvMtSzBM4WRUozh0Ot3Ro0IxCcUByubmR-Ynp_uWNCd463SyuEEA8GRdlKzLs189bQGQyDzmKiD--CWf0Ya9pMlRh1mlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef91S3117Va4-LAiEnG3ku4TLo3jlRPTG70GfbmQbNz2mGgPcdi5V_ywTFKHCDdw6O_GJttUW5Z0Jd3hGmStjvU0PxP_OPTtCbXl6SLkUyFcqDOOLzJDk-3C7gsMilZHRX7VRW_uAiCjl-_F99F1cwosATP3xsvTkXp2ZQCGDWKeLHbe4K6TlyYCDiw4OGo-Ov8iRXsDvF7Z3AP53iwCaW9p_-XcctUEiO16f7la3JNmmHCdLGtVUzy16bbt5SIgg7F02Y6L42YVRbESWimSQsiYXNig48JnWwlCip8ZBOU8st9LwvA-10LFc2yPKlPGHnZoWkIwmm3q-NmzZQXO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDBnsV_ketvQKdOQ-OvsgDpvATmlZHI0oYVxtbGZnCSLDzaDC9Qe4VKzpLhWRYWjNnnmc-T0BZTvj55QhiHgYRuzzowtRCnmvBLof0J23AxejVgL-mKmCNmeqNSxPoGINWMjeK07aFbncuLVLyemwft04WllGnsz6wOLk1x4Vy108x_S0Rh25kLWUiYwy1W1SeFRs-DieCgwKmFtQ4RAfyaaYa-XQ-sNiWgt0NiAPXDiGjI-JcPpzZS0_4e1VWTEo3kbPHEs3oi3qDZzikxXkDTjY2fQWE7Ovv_hEAXaE_Ao7eUFpBIeVRrruRi5vmIARmRzvd8ljMsZ9dk-_iEGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYS4O11rTUhhLS_TNTedpP9dQEwYaWVCrOToupUC2WBYTJLP7-lstWMUsxPJg6jffgi1NXnPsdExkhjkyBKRpa0qeP16FHEJ--QGPRygef8t59RpA8bvYy3PWpexG2JqSRB0NFaUJjDHVSNUyublLbBL-biG9VCXSvMvzxnQtPPgZ2fvPV-9rUD0i6HSCKSat3tFlCINgoiHbcvFmXtY4pwml3APE-BrmKXOh6Fw4M4daw_2JI9gRYq_dPJ3okM0scAYs52u8l5UI5vEl9YY_XfCqBu8DUPa6kr0F1B9c7-gCzUZRW7YNHCnREEJPZvM1Ua2OxnFXxzCzcRfNZGlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgyfVCa6dMOQ2sRmsVBQGnriQxL3wwhwDwMqtv3vCJdCmYqWsjjw3s8eiPtDWOIqyvlkvOUb_n9J2C7Ki3B_WuT5hk0UBmJucFLqaIyVBNH1uot_14lNJp49SDq3qFeI1RILtjDkPrhUpew9AvGhe8ZiX94xcOWxhGIwKroxr0J0Vs-GCqN0ytx3PppGfr9_pR12FrrHnKORIDGZvqt7xB0L_G5KqoOPes1Xxe1_3pdLvg5BNAXzvmTGOYLjjRkzJTa0ncOK5oY7YRFeOAU1ilBxM5Po94HSUzmrb_LKXm0njHLW9OMG-XRk18SCQAuhSzuf5synvQzjrf-19uvBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnuVzGvF1e4DDouXTCV5w3Z6LKxFW0Uit8CThyk8lNcLBtAX-ENGu-WgnXww0Z-ssa3N6vybLIMhmay4e1giUp6iPFGP4eJ56m8VlhA8g0z9CMlSEQ_SnsTooIbYuzkIwQ007aecrVOTZWLAfTguxv0ivvWtn_srfuiSnUWJ8_DQeMCcQBTmoqCrQQrlQTtbHVFwvQMOb3qvZ6ekOZXL2TTA9xlTAE1TGQhrpsKJWgwUi9FgHZsK_RCQ5wuCdd6FHkC4m8SveCuovoLEtUSpqfsNKFe9F7RNDbmfkgHGdcqP_bB35Ahngcl2wGn7nTe4MosLxldB0JBu22F51DxhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ADo-Zo3ezUt6Et8T0RsTIcyYr_nSLwC291M_awHhLiwMcWYCsToGV7yoTp81kmbQgaRHNajZvvZ0xtLNJZ5QsiIBESfk0n2jt1-2DVeix6dFaO38u0njUa8zCH7ERyJrFFbEkHf8PcxPJ31embrYZx9LtbYewh02-CSl10-LeQjflhWg8so2vNQxCZpq5_eGtsxliTXMuOBRuHp__q2s9srUIbPJdclGT_84DdnA0OQC-lmOb2sZV64GSIghnKiM7JIKRf6SkYSVt2yLhOUE1wC5k5gL43p5MRjqXEf5qyIpxr6GoZIh_7qCXlyV9Siomg0oc8TnmXx1lOCcx5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kunKXURk34l3ROgKawEd72nbQbrm3Rf2HE3axkIO4-EvpDe9B1yKnlF-iZ39A4yLq2KjA4JjxPLKD-R5HFywUnqmReT19nxwTrASZDdjyoDgvJ0EzYu5p58T3MQIYyaSFSUmpuYcmFowkyJY7jzdP9hngwRKtHKv95tOJlk6hpxXaexVA8vCvCMMIQ16q8awlbXLTO8XhEqiE299i-wf--VbZ3B8Kb0aeGqaGmy6ETiEuoq1tUgsL5Lidnt-lzl28qqw_d-D4A6zavmlTsX3jcfPBG4B-pulwfvJpps2BlH3dGa6e-rYRoSTzdtfekZPKw-9fO_56nEajure1Ziqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swOhMUxCNeLBtROJMlXS_GhzK1L-cG0NrLFDGe3tIIH7_AvgSKV71d2wFNIgQKvp05vC5S8BRNbyrkrsrbHjjFzyjm5DXijOM-h3hwSxBp12IS7f8t4FKbFWZ5rz7nEHR3kMmYpHjG8bK7HR5BO4X-DGJFTTDsw4trC2HtjPUyj2RzMD7ajdLLpxM7ml9gPm6VEQLdzvKZ_0PV5cBDyktNz8-nvpoGBtm_nKaKUrdzUGUL9pOZdGkAMI7SKSAMQuHA6D-4LGjgwwPLIhhsGqFy2_hp8fXJkHICgYfRZPh8qoGn4AgW66xqLBaMKxgMP5O0YLyee7YEoyNIhlVvVmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SepKSvMG1XZrfZcu_f8PUHKRDxIuqcuBjJ0c_rO0Y9WLahalMVpZ4bhkdc8uRfO2KS8uUNYkE-PPDUQC_2hVcRCrPz_FwTPyvxUtwxa6eAzWrOehrEZEUOrnJOGQZSkdrnI0K2uD_E4kPtCKERc-yTlsNM7I7ixD1vR3yYlGdOtxp72VE097060KF52__pHRxBMZvh9-SyaVc8F-F4wajVnh_3oXFbhzaqoef2XmQRmjwd9gC5gULVqWZ3-h1qA1WIGQz8uAF6gyXh86TFE1XRW0FpdNNrISzJ7p9s5J7shaJq8pBJVKQPHwGsjFjNeGpHmdYEzH2zumNANU3CeCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28607">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjHKV-5HExPVuMnjwfiV9ZU0d6ELs-uWIA33IRZLYR9WYxYbA-vhkUIgMFa_ZounzivABUUAIa_D0SERbFg46mfeH-Gea1thJz_UjW1zRl0c9dJ2ZFN84UySnQ5H7QF0eufHjcDBFe5MI7OxdbfliU6A0BGIK6ww9Febbha52gm_yaNd7JxmDWq3QzYP-SpNvesRWpMBmubWhcJilHgqN6J3xi1qgkW2Cjva6ufNKrYJLQi_qlCIh9ILsGL39LgLWMlqI0XpA9Hn7LO989KN1kNdc0O-2GyjgPb_L58rKonB9oXzvbdEoamUOSIbL8IdR5uhe8FuHpjdAvEHomekng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28607" target="_blank">📅 09:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28606">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1xmfDb1eywFZ_mw9V-Bhf3y9ydJrTdRuEPKTY3R8Cl4BgK3_a1zmESadmTBNhHPYIiPcCWPcRpeRiLQ3GCQiEFByiZv2NWyGwrRH6w__mpOsQbKpsyDHlrxZ8flVb1YG-FdzVis7DAFFUZ50MQhfY9XEVkOc9DpLpAV8sj-RdSYNMLuTgkLp7TOumX1ZQFBIJgEpseOFc48UCAIgTOCCO-i9XRoI8YnF2zbQhUc1yOFzxVrTMKLOe16oh9Vz-XK-DyzvPqJRRJERNDz4pCsERfnL3xcZXEMFgHuH6ggytxKZKTlI_qMmOgbCyxZ9K-9yJsPwqlG_19b2wIG8iDrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28606" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW50RgIzV5i5agfRXRz-A3jA-lfJlAsVKMwzOC3EaO5AQ71_v_tNY_BZUMENExTVKaApo3YyudcAGopxrs5vv3F1ftUVHyiviHa7E50ollXpvkagkDikPGHC4ta5xGZJf5K4j2YZrxkzd7LSmwkLLnZzvgPcKYZIvRQJBLBcXEMmaO5rvzAdVQ5WHllR_tRPzD3Xg1Oo7fp7yvNcalllzoJJbzw9NnWl_pSHio4ftFuHlsWBWsPCkED4mCfQOEnfwFu-jARMyLdg0u9Q3tsxOyRhVtaURorvZQfUZVbMSBGUjzn3gQ3iz28Srzl1tDvex_bZvMPjsjitU2BlZjK79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل مرحله گروهی لیگ قهرمانان اروپا در یک نگاه؛ چه بازی‌های جذابی قراره ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28604" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b440142175.mp4?token=lxstQSewUtBYNxMyrk2IWMmUF-TpEX7A-5IsQ2jdM4kfDzM8nBy8Mze6Kv41c2yRenO-jx_fqHuDU_BJt5NYhSdlYsChQK23KQVXtFP2bX979AMV1MvR_AZEB69sfGy7PuNOdCO6sfex0ntV6S1V7qrlqOsl4QXHGK_ODR4QI_NY_2Goe5unbZENNQWXE_8gLkF_DP_ffZBXo1PxeELO2J2ICQS9vp1l8hGmuESaNJ_7cX_OAraozROUaMUUK9lSc_3PxEUA2I_Cnx3iyo-EdxhcT2hWaCxIdlxLFkFCF7v1QztOcg0eUFuijbenC8nQAkSfLOic21vtPlnTegHx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b440142175.mp4?token=lxstQSewUtBYNxMyrk2IWMmUF-TpEX7A-5IsQ2jdM4kfDzM8nBy8Mze6Kv41c2yRenO-jx_fqHuDU_BJt5NYhSdlYsChQK23KQVXtFP2bX979AMV1MvR_AZEB69sfGy7PuNOdCO6sfex0ntV6S1V7qrlqOsl4QXHGK_ODR4QI_NY_2Goe5unbZENNQWXE_8gLkF_DP_ffZBXo1PxeELO2J2ICQS9vp1l8hGmuESaNJ_7cX_OAraozROUaMUUK9lSc_3PxEUA2I_Cnx3iyo-EdxhcT2hWaCxIdlxLFkFCF7v1QztOcg0eUFuijbenC8nQAkSfLOic21vtPlnTegHx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی جالب دیدارهای هفته‌چهارم رقابت‌های لیگ برتر؛ سیوش‌کنیدببینیم چندتاش درست در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28603" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🗓
🔴
🔴
#تقویم
؛
15 سال پیش درچنین روزی؛
شاگردان سر الکس فرگوسن در اولترافورد با نتیجه‌ تحقیر آمیز 8 بر 2 تیم آرسنال رو شکست‌ دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28602" target="_blank">📅 08:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTLe__FpW-Kn-lMB35RRtD4H4vL_-Xf6eDfvy9SC2qbU565aA9OLpfCqI35OcqO2YjnJY0h0uyRKZFk0bZQGJb5JZyDDwkpbVEkGbjDjFqbJVQQj519aTCWMfYqtqyJkEbYUHjydRzwGGNa66ELLjR2P-Q96s6qrQeFkyHDaIf1xLzJWngQf5ytpZ6rvcywm49d2cOpneemR32LNgMciSXzdkgnZ1hbuHpyzYZpL5ME5JlMkndO1HX1AAT3EfbIJlzlO7zalvWmlHhyG6SScTYSwYiBygNxTAIsYe6u6wrFOpHYb3eGzjrJmZTJSwFzbUflg9Vl_6ZpD5jfm22Y55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKKyEp32V0iUDjjrVZRl4KAyByjB8ivkcWkeXsQkeCYtOEAslYW6xdvywTM96jh2Nbw97nZ0L2pEtF4a4-foScNq2S4GYOyMb478ybTeUcSbdsFnh_sWV5jQy7cxXQ6S9F1Y2hsgbyw66sw5SKd9AcJSxvrsz1nXtTX8wQoMUxnnb9PqWH8aBiwKQ471JYq5RfwUrvO5bl4jtfFhu2BOa4H3VDpVes5zHcwTGxMx28W-92il1-8-p_P9-Qr0GRiNsecmjUpJxEOs7HLDnqXu5DVj5GFsvOix-1MylBicOX7Rp2yDCtt8RN06FqRaPVNfowwpwnnMVKLF2pDTCJezzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی با گلزنی ولبک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-HKrS-DESVJWfZn67rS1hjRvmUwbZM7ViRK1CV9EvzNPFeuVUtW1IxAp2saHhw6eZol7a9AC8Ar6g2sO7LfMOxUd2hZZoTjzub3IqAcRFqMOkD2FVQUObZc7zVgfR0g9MJiYbYmv4V-5jWEZ0K_iLZ7kwTiOCmMYLkMAjs76g3-ahhQFAYWjRJjEWICeyV2qJUxN58Tm6-EgT3TafCnYjpqCHS3CFBzdtMuv_BcfVUw1DbG1TzqQDXhgAEONnzDa5Bbf71bqA6cVifwH_rIzPLgL2MGzFjgfnBcDPWZGCFrcfk9e46wt8MULBDCfZ_UHlLayc2-G33jsgJyLFw-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djKp0uHLkY9LXjhgQSCYVMsliaMfhmv-CMSsa5bG8dLWpfjCVjhrf418Aqyr4eJPrCyAo9-WKeAGWi6unj8BEpU3eXv18PasUi_B17gwo_xeE805LqDd5Zbstuo_G4e3ItIk_bCo5XE7H-4P3D_VZioLakgelU4WyUmDFjsaLKGqPxwOZIuOJchXW-x3dvrvuH-LZ5ryH4YL4fLN6hKk9v-5RgG8poC_LmxAK4xOokiG0PYDxZozTqxSmtWICVp9azo_vlqUFi6Aa_i77IY27y51Kp9dRSRf2xucTIuMV1KK_Ny9q_EdEZP6n5cIvUNGNoo5Zc7iZjgnH0cHNFsQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده و پاس گل از سال 2020 تا کنون؛
کیلیان‌امباپه‌وکوین‌دیبروینه در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28598" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=PMXnniW-vRIKlg2fUew7aS-WLe1TJTaP7UMkQeHjKh-zPXGzRkqzpoYt-VgQm9KNdRZitzvYY6tvO7n57-SilkSqrGQSrJy83EdqgGoTFNNK_4C-nQhkQsRA4drWrqd4SF6p_bYd25mkAqPuRoen6VOPTApMLdZeRncXqbAaq1QjvMpkyP4ku29au7-6lDTdwLjEa1h9RaDokXDwwOr3xiyA7KMmhtoRx8TVDdVnnswXZZzU5pItVftFrt8HlZrz4FFdfbHaz3cgu4Nmi-7kiweJgK9hJOxJM1XbhkbUrlajQJn2T1RSd3eypV_W-8ZIZzFPtqpQIDDOOxZFhSHmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=PMXnniW-vRIKlg2fUew7aS-WLe1TJTaP7UMkQeHjKh-zPXGzRkqzpoYt-VgQm9KNdRZitzvYY6tvO7n57-SilkSqrGQSrJy83EdqgGoTFNNK_4C-nQhkQsRA4drWrqd4SF6p_bYd25mkAqPuRoen6VOPTApMLdZeRncXqbAaq1QjvMpkyP4ku29au7-6lDTdwLjEa1h9RaDokXDwwOr3xiyA7KMmhtoRx8TVDdVnnswXZZzU5pItVftFrt8HlZrz4FFdfbHaz3cgu4Nmi-7kiweJgK9hJOxJM1XbhkbUrlajQJn2T1RSd3eypV_W-8ZIZzFPtqpQIDDOOxZFhSHmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28597" target="_blank">📅 00:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28596">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUt7SY7UXXvAF2CYRTf4sZcwVuSxGZ867kX9JhW4FXuoO6pnVPTUCzsWTjUHBwOQXF7NmiAz7WoyOpJ79_NP1ohj56jh81Nj4AQXoqYs_VXJxvAXKXByrFLVoyAnjJwR9DgwEUnV6G21UEoalc2N2C36fY3ohA9COKuqxvLz9wkz4xozupwGpw8oqoXFwymDEhBagLG3F4oPNwPBaVw3ptpVYwLI8qlgdJbbyW_GR2QFkiOk9CAbmR5PVhp2URm5SBB-UTocos9Tw3dCvnsK29vswmahMyoNbB1TpUQHaKlHo4uY9gGfLbi6orz4ExnZlw0m_4vrGyE0vB7Nl9MzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28596" target="_blank">📅 23:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28595">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTxX9Xb2dT0uLc7-x5Ta0sPyFISBIBnTGWAE5M6idfRbbeRyYpmSru4n28IiBE5oBDlbKIY99s8LrD7u6p_XDrvbLSxTUAC1q2EiwgssxPgYYiccy42JMiXmW-W6hBGtnSaX0csQPw2vkXhO8pAVDGmaDaHmlw4tZe73skGfOrZtQdN9Z1eqzwoD0-vF_LQ4COYlGqS-Oag_cdKuM8Jf6ZwuPM-OpUlejtHO3W8UAUcW18OLatO3oBiCW3W4ODgs-p6i5rEYefcNRpjoBLbOP_nlu8hsU3EC-D0e-qTV7ziy8fqXm0_KyUpyyd0rDRBBLAHQQgTXlK_12pg0RRjwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28595" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28594">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoGg7kj1NPaCjgWJLsQ3upmHpUHeVk1M5F9spQxuZocn4EFB0GECda7d0aIvYG7R0evIcU9JdhpYZ4aBW1bxQ90EMHmURLeLfy12g5D1f9kWGJ6dNqY8Ihh7mw6k48z1JQ9ckwloIxbFmuX4vJCvUivkvlKLdjRGIVpAj0b8lQecXL6HqaC9-LNA9AS5mCb97MQ7Z9NyJ1MeZ_TjZBUa61IRtEkdgauesX6eieq-FrdxmdYAr-Fa52HDYk9LKO4YJmiHI8rUiRDigcm8VDHeWCh6nbkOluzdvhxW0D9mgeBdVudJRwDTeMdL80FlUQ8ywJk30HIzWZyMeT0FCGQm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
🤩
بیانیه‌جدیدباشگاه اتلتیکومادرید: تحت هیچ‌شرایطی خولیان الوارز رو به بارسا نخواهیم داد. تنها تیمی‌که‌موافق‌هستیم آلوارز رو بفروشیم آرسناله و هیچ گونه مشکلی هم با این انتقال نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28594" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28593">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0U7j82XyNb3Bj_wzS4oNfFwR58zvU16PF7hyR5Q1kW-mZX-Fp13Bfz7nKPUpsOfyI7O1WG5lLH3dpAtCDdQPNB_3lRCaZmRzBjLTbD4gvE0cyLZUKVg9hxJLobDz_wIIeNLnuH6DYpxvgrjdd0zVx6TRhuRVmVlH97RDNnQ6U0gkXZRna4aLDO2FSBH57N8rcSHLdqhW8Bs3nYeA5g4IHbNXOZeFZY1KjM8VCh8EZDacg4ktMLmP7c7cHVm3h4-In_-2Wp5o2lbNH_CokWi_3pArzz3QIQcyXMjXKYoufo7Ynut7AnscWvmeWwsV3q2W88hLNu9j5YwUYPtViygoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28593" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28592">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FduFlWm5K5tMpyaA7CKYK-w6F6ml46W0etxKWEv7a01d-EdzpdixlZrg4VIDi0zAYSadOYNM4xq1AqbjiTB1m44ca57NnENAV5y-E5MJtZTfT4829c4RbMfMDnVICkbKneX-haG4cvc7YIOhyOeDdZGS28ezldSzw01-Tx_96MzXCqOJ4b2CPo8rmYgQgLNvQ281YS243S-sWQ0_q9mBqq480cpXiow8ELm7UBpfrojciwt43EbUiFdatLNQSjIIvMsev1CeTN2CLQBQQP7sd01PjQhvAX2ZbYVDoRI9ihiie1drlfWmrStb38hQeBgGoSy9tqUn4KFlxlCRsELg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار به مدیریت‌تیم پرسپولیس گفته اگه پیشنهادی با رقم بالا برای فروش اورونوف به باشگاه ارسال‌شدمیتونن اورونوف رو بفروشند. حقیقت اینه تارتار اورونوف رو نمیخواد و میخواد فراریش بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28592" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28591">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrvDsUL6VQ73Hp8LSuux-WhjADsDElcibBrxyVMd2W2-PVxYHP3vz-TgP9Mdy1SqvpAJl5H2QLcU_MjhE-TB7raccQu79ClCPHZIz50syna7kKxrw-wsajRigQf-Y-hWwaGjTle1F0JYtFbqusUMloVbVMkt99xs1IGz5RkSYH07U1BnS9huujGRkYbuUkPXFJ7-r0quXVYiGWxuxbQmtImXnrE-RANrut5W_yjGzs6ymBMId3fIbO2qLSdYtwofXBwWzM68aOfpUzwziTze90IjUeyaDDl1Gt5XdwQ-VHBN-2RtJXq6oUvJELmSWMrg951hLk19fp4ncop4BH1myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28591" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28590">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlAxCvts4AXZSnYGm7EyQsRjh8NAnquU_ziJx5BhLKNWwFiJrhouOypFpk08qMFwtAUNfLK4ACnd5gdVmIcDERM48m2tr0GN-QZTXWOL2hFho8sQVfysc4nVd4ux25hmvCccrQ9peEIbMkbVTxMcWg0hWQ2gI2cHF7yMfjjhRzdv3Kg5-aJpS8PA85VebmFCc4LzWUfF_cc3_fDvNMgZKApFGF8NXWCTmr12GD1MaXXnkFIOQEqJx7VzR2648bu-9l5Ucd-2boveZ40T0ZsJKuOyQrsYpwEhDul0UnR8VKhagVY97wnF9X4VhHGPf5TcNojj3diT2fMPYEf-3Ttl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28590" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=pZtObYN_7DUm6PXzr0d_UoR448Dy7dTdCjFEbFsaLaOtkUyDz9czskEoZPBHTO-CTJZtN4iqbQ6Ikhwy_nIjuD4rC6AMFrY9KXsSm8rNzvfMqPAmlIzg6_4QuhiNN9LnmSdWKFoM-dlW7_SLD5yWOsjUOdvH09As5NTezekMTxLy-J_Wl4FqzI6snGWhwo9yqH8Ka5tT7Oaf05mVjA8pQNhFTwEoqYynsKSPFdjCUeGCLIkeYUtTKsfX95Ii6aRvqHQAPKrDt91uen_DmEtWYLOKF7slILyw5c-5kMVMozKj55gzQqyiinCVfVZ8vMyFAUqN3aCVh5XwFJA1eBjrQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=pZtObYN_7DUm6PXzr0d_UoR448Dy7dTdCjFEbFsaLaOtkUyDz9czskEoZPBHTO-CTJZtN4iqbQ6Ikhwy_nIjuD4rC6AMFrY9KXsSm8rNzvfMqPAmlIzg6_4QuhiNN9LnmSdWKFoM-dlW7_SLD5yWOsjUOdvH09As5NTezekMTxLy-J_Wl4FqzI6snGWhwo9yqH8Ka5tT7Oaf05mVjA8pQNhFTwEoqYynsKSPFdjCUeGCLIkeYUtTKsfX95Ii6aRvqHQAPKrDt91uen_DmEtWYLOKF7slILyw5c-5kMVMozKj55gzQqyiinCVfVZ8vMyFAUqN3aCVh5XwFJA1eBjrQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzABXN6oH9tdNHhMixz-PvQI1LW2QGS2d_4LxQ4OURzsAVFfZlLH_mX1pGQIhfm77YD09_yJZVJCHU1moZ398r8_hsUEcJMt4BOkbL09dAYWOEQeyjEWxyeTNB8O0LmziR4qzNrXdveAv1Lt9YJsieSEL0uDGTA1ftwrpl-5oYQeqsFHWlbVmUkoGybwmblSxevjkAPdzwtK_RUWF8HP9fEUFJ2NRPfEn9a4jA3cIfqJmCwQpJ-svOnc5J7hXrTEVC8PBT5ggnFQlPJ6T_eyyJoz_uCwVVs0ua2UEVvL581TqHET_UJJAShfTjpqZ9X8u7SQm41eOLjq8bnwyrdUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErBkkk4_VxU67Dud3aDnwQxNcBUL7qBR2tvXQtAtUcjIHvwyY1RKk5gWkYgZWg7UjM4m6OJIwLxbUQ1_RSDw1uIMqwWpz8NoBpSaqJAlonseumaB78fBTMYIMYqg05atnzfo1rrXpZDTSsKxuVtMV-hsWFTKnhZMGdNkGcmvlK8Of7w7YEmJe3qEavWLovi80o0qbzB__QMl1Zcc7u9fBixDmI6PvjeuG0h0YLAr9OjScIonSEFLIV2H2Nkt8cOc7jNCLgs28HJeSeAyCBWaqmybZBscBopOjkQlggNSSHjngfHHYlqziEA7cmLnZmRrOOqfQGbdnEWyj2MaHQX9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvPNVkKI6taUbebsNPnkIjtxunMmroZLOuFppyMM9MC1r28A7IXukyfp66xZW3F8DoPNm_VcI8lWAcjw91xJjsdaq6TJnnY4U48IkCrqMl-i9tfczo4oD6pPEvZoQCWmlhi0xx5qP9xRGb_8SPW_7DhtffyO15Jy3Panhdm0Ne5S9_nHJsUEdObo9U7C_iWH7oQr1aG7-J4RFu5BkNR1Kle-Xnrtvlrn0M_jpQKL2WVOb9orU5metxO1c7eVgPp77eEVG85xCuVr0DJPnbPivT4oppAaAYmrY7B-XWYKpWNr_op9RgZSV5bumoYoZKts_8e25N3hCPu-RzNCMIxwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8qHLHjvbnF2wG_Pe9DY-k5vhh6P4iwLwObelqGuGueCA3VUncegu0qunXpReEZzi4AfY74lxXLK13abfBXelk0R4TSLLc6miVoyaDgx2V_BhQGeWVXySl2F5zMv067B3TtgwjHW0rgGLMp7DZXBQA0xn-H8y_mC5SzRcMrQ9_Z_J5CSkSiSPSVyS_yy0GYrVEeCjATVWqCdRMYnzzxufUFGShHhDCU9a1ATBZ0mdo4FsCRC_thJPFF5Syoy5bag5dn1uYvB7juANRf8vyD2Syyd_QXJRqYMyGIHR3pT-BF0uS8NVTHh9cOAhXxNx4mXUENIUCwFG-jGYpA3fiDRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

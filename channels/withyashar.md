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
<img src="https://cdn4.telesco.pe/file/fmhiJGaTNUY5IKvUKUKA1aTNBmwO4WtQL7ysil7pXd4bYB-HlQXGmeqtd2QtxqsEwpULODbnvU3W0t6LzvSihan8YGLE0jzYYiCsZeRTLnAr8DDvfWoIGcrAITyVFhTsr8m4VfPj9ojDZ2UuBUY1-ZtDLny5BjnkC4GSVoKRqaFWyuUHPjq2ZiQPqKzawZ5n5xR5jlWayPleiH-SFDIVAIJRrwZu68-YZgkdNrnF1jFyP6yC0JH6MTEGl1N0Cg04v_VSaFaKjQPFP-vreuVGt80lS7UP-WzjA1ps7LZ1_dbuOKNAMpuqJJtIE4PwSQeoXOW_s5vvki0MzIirt6-8mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 462K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال‌استریت ژورنال: نتانیاهو در سفر کوتاه خود به نیویورک به دنبال ترتیب‌دادن دیداری با دونالد ترامپ بود، اما این دیدار محقق نشد.
همزمان، هواپیمای نخست‌وزیر اسرائیل به جای فرود در فرودگاه‌های اصلی نیویورک، در فرودگاه «استوارت» در دره هادسون و حدود ۱۰۰ کیلومتری شمال منهتن به زمین نشست؛ اقدامی که گزارش‌ها آن را در ارتباط با ملاحظات امنیتی و لجستیکی سفر نتانیاهو عنوان کرده‌اند. منابع اسرائیلی همچنین از حضور غیرمعمول نیروهای سرویس مخفی آمریکا در تمهیدات امنیتی سفر او خبر داده‌اند. نتانیاهو پس از سخنرانی در مجمع عمومی سازمان ملل قرار است نیویورک را ترک کند و در این سفر نیز دیداری با ترامپ در برنامه رسمی او قرار نگرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/24013" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، و ملانیا ترامپ در کنار شی جین‌پینگ، رئیس‌جمهور چین، و همسرش پنگ لیویوان، در مراسمی ویژه به تماشای اجرای گارد افتخار نیروی دریایی ایالات متحده نشستند. این یگان ۲۴ نفره که به «گارد افتخار بدون فرمان صوتی» شهرت دارد، مجموعه‌ای از حرکات نظامی و نمایش‌های دقیق با تفنگ را به‌صورت کاملاً هماهنگ و بدون دریافت هیچ‌گونه فرمان کلامی اجرا کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/24012" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین: بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/24010" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=eAVKEx9FXDL2uwiQl4iMnPTB3wbV5OE8hoQMq3YMQSi520GXZK300oFqw8BMPhPPJp70az9rmS7FqYY-P7ZCbfNZwrBD4-AKAzRAyIc-cwtF_L4ecqDHz9wbyKsv52XQSqG3A9vBgRR_R-4E_V08tkNPG-CeNPdo-MVtKIRDWy-rz0SnGKq8e0HMeK5oUHpnDJPFZ8CNPuAde3J2FbtBNpkrTS97EHPcu_GHH-lAArXK-B_HFDRl3VWl0ljNzi7TrV-qxTafoKbpozd0z6G6ChhWl66GwupWIPgjFHktiDAA8AbQpkATkkS4FsMqokbhzFvYKvSgKnocTLPbmpEVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=eAVKEx9FXDL2uwiQl4iMnPTB3wbV5OE8hoQMq3YMQSi520GXZK300oFqw8BMPhPPJp70az9rmS7FqYY-P7ZCbfNZwrBD4-AKAzRAyIc-cwtF_L4ecqDHz9wbyKsv52XQSqG3A9vBgRR_R-4E_V08tkNPG-CeNPdo-MVtKIRDWy-rz0SnGKq8e0HMeK5oUHpnDJPFZ8CNPuAde3J2FbtBNpkrTS97EHPcu_GHH-lAArXK-B_HFDRl3VWl0ljNzi7TrV-qxTafoKbpozd0z6G6ChhWl66GwupWIPgjFHktiDAA8AbQpkATkkS4FsMqokbhzFvYKvSgKnocTLPbmpEVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین:
بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم چین، می‌خواهم با ابراز سلام صمیمانه به مردم آمریکا و تبریک صمیمانه به مناسبت ۲۵۰مین سالگرد استقلال ایالات متحده، آغاز کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/24009" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پرزیدنت ترامپ: رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/24008" target="_blank">📅 18:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=OyKhV6XOmTQ8x7pzrdwzW16r04KF7r_MuJ2M3S5mF9lfcIFVEVQS1d9Kjq9zQdWKRQS2rTvZZovyEgSOsgP8d5_RVI-Yn5GlxarQmuHbuDMi-sCV-hieUYwYcmNKzNw3WtZ7Rm-rcidMPeJIqejglMH16hJb6ZiuCKteynVpobMgfYX4vBFSidQUdeWMGYmVy6uuI0pST7KglSPeds0KwUUezYsVoE5Owr2AEpoxp5ME00by1-fzyFWUM9VvHVCyga8dIN_L8Ez6GQ_3GvhCxD5H2L8W7Gj_g-C7ZHwabiJWbgJMnVlJV-LZn-Qg5043E42f1vQQ9oCWofA5XjaBlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=OyKhV6XOmTQ8x7pzrdwzW16r04KF7r_MuJ2M3S5mF9lfcIFVEVQS1d9Kjq9zQdWKRQS2rTvZZovyEgSOsgP8d5_RVI-Yn5GlxarQmuHbuDMi-sCV-hieUYwYcmNKzNw3WtZ7Rm-rcidMPeJIqejglMH16hJb6ZiuCKteynVpobMgfYX4vBFSidQUdeWMGYmVy6uuI0pST7KglSPeds0KwUUezYsVoE5Owr2AEpoxp5ME00by1-fzyFWUM9VvHVCyga8dIN_L8Ez6GQ_3GvhCxD5H2L8W7Gj_g-C7ZHwabiJWbgJMnVlJV-LZn-Qg5043E42f1vQQ9oCWofA5XjaBlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/24007" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24006">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شاهزاده باید هرچه زودتر یه فراخوان اقتصادی بده ، حتی اگه اعتصابات هم نبود ، باید فراخوان پرداخت نکردن قبض‌ها و هرگونه تراکنش مالی با رژیم رو اعلام کنه که همه همزمان انجام بدن !!!! خانوم فلانی آقای بیساری که اینجایی برسون به ایشون !
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/24006" target="_blank">📅 18:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد @WarRoom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/24005" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/24004" target="_blank">📅 17:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVZcSYs2Iz-NfMKXdASWiW-x2_MaWmEwjRqX5HJl-rbf0cBOh4EV2xR1nOZ3HU25AC9AM0UBpGpT-uiuaT6ZEFJgi8weud3uCNfn7YxCzfjy4J4QBZrim2xIhEyYf2ShEX64bDUp_RNRFNEyKNIhIbYgNJwcMehYQ-aVWvXn3g0OioHZlvY_O_ZtQk5NcQfHa89QnOCWNKllRl10R9Tt284kYgPlP8UmR-bEvv_ICch7Fc7HWcNf7ynJ5S3M_LvIMm9iKScxBBNeErm9-uRD7mKkLHPW_KvLk5OcdO99MCT43htkLbjNz4SxaGEjqHJCtBAXNxIMBL8YImzTMIsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پل سنگین ترابری نظامی آمریکا در این لحظه. همچنین چهار سوخترسان هم اکنون بر روی تنگه هرمز مشغول انجام عملیات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/24003" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24002">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تنگه صدای فرمانده پیشین هوا فضا سپاه میاد
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24002" target="_blank">📅 17:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام نظامی بیشتر علیه ایران مخالفت کردند.
به گزارش CNN، رهبران کشورهای عربی و خلیج فارس تلاش کردند ترامپ را از تشدید بیشتر جنگ با ایران منصرف کنند؛ آنها نگران گسترش جنگ و کشیده‌شدن بیشتر کشورهای منطقه به درگیری هستند
@WarRoom</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/24001" target="_blank">📅 17:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری فرانسه:
یحیی رحیم‌صفوی، مشاور رهبر جمهوری اسلامی، هشدار داد اگر آمریکا حملات خود را از سر بگیرد، ایران ممکن است دامنه جنگ را از خلیج فارس و دریای سرخ به اقیانوس هند و حتی فراتر از آن گسترش دهد. این نخستین‌بار است که یک مقام ارشد ایرانی به‌طور صریح از احتمال کشیده‌شدن درگیری به اقیانوس هند سخن می‌گوید.
@WarRoom</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/24000" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بلومبرگ: ترامپ و شی آتش‌بس تجاری آمریکا و چین را تا ۱۰ ژانویه ۲۰۲۷ تمدید کردند.
این توافق که قرار بود ۱۰ نوامبر منقضی شود، دو ماه دیگر ادامه خواهد داشت و از تشدید دوباره تنش‌های تجاری میان دو اقتصاد بزرگ جهان جلوگیری می‌کند؛ هرچند اختلافات بر سر عناصر کمیاب، محدودیت‌های فناوری و تایوان همچنان پابرجاست.
@WatRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/23999" target="_blank">📅 14:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیروهای دولتی یمن: سرنگون کردن یک پهپاد متعلق به حوثی‌ها در آسمان منطقه "جبل حبشی" در استان تعز.
@WarRoom</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/23998" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک منبع اسرائیلی: ایران فعالیت‌های خود برای انتقال و تقویت تأسیسات هسته‌ای در منطقه کوه کلنگ، در نزدیکی نطنز، را افزایش داده است. این منبع مدعی شده در صورت عبور تهران از «خطوط قرمز» تعیین‌شده، اسرائیل بار دیگر برای حمله به تأسیسات هسته‌ای ایران اقدام خواهد…</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23997" target="_blank">📅 14:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی ائتلاف: ۶ موشک بالستیک که توسط شبه‌نظامیان حوثی تروریست شلیک شده بود، منهدم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/23996" target="_blank">📅 14:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی دولت بریتانیا به شبکه الجزیره: ما با فرانسه و کشورهای دیگر همکاری می‌کنیم تا طرحی را برای پاکسازی مین‌ها از تنگه هرمز تدوین کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/23995" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap8SEE8UC3GN-Zkc6m3Fv2g2aW9rNgdekDHP72csHLZENzI7FNNMlS_Oj9Oc-i0IpqYCljPq3ALWicTuw36URcuR2vVqPcarX2v9NvMC9vMmkt2yh5HFnSy2zBX3PoDz2jPXl4_0K8kaK3s2xKKM2iWeusqhJD1S79tT7-D4w2h4Li2YqSAjDDVU42QfCanwcSfnwIHXWHfDTJIXwjUvvw5vDRDIih1QyoHogcXc7sjXikzTJUe7JVVOs-O_cGpTSn8lBdcCn7QH62ONWRR1lEiOsfCM3wAO46hty8tiofAq1zdqlPPnuvuuFkS2X9KmWw0-B0M-5C2CpHukhoyzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدان استاندارد کرج  خودرو ضد شورش زرهی تو جنگ مونده بود زیر آوار از زیر خاک کشیدن بیرون
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/23994" target="_blank">📅 14:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eba653675.mp4?token=ZsBOdr1Y1SaOp_nIdSmmqpcAm0BNfgNIjPIAl6f1RDdBsBBFfX58ZZ4j1928ODTh7N9ExVwHt4Lqe9OdPW-MCoApKnvi9w-wN4lb9Quu0X90dEn6L_b5zecNEF2b9-mjO-HLDDeveeHuWmFfElBTu282B8eHXbexzLBzXY_4vqgF12VGAeiv0puTdsc8Xf3Zmy7380m4qxizoHD771TsvsJzSr5_N-8l7Fy4hqwf65Quw793g417O_D3-PLvJheAWiwI28dNV_W-Ojd19w7kKnUkJ0UzysuqofzXVNZS8fqhIxt0P8a7VBS5ifxW-WRLUWBjI95vcxgfxSd7j75Nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eba653675.mp4?token=ZsBOdr1Y1SaOp_nIdSmmqpcAm0BNfgNIjPIAl6f1RDdBsBBFfX58ZZ4j1928ODTh7N9ExVwHt4Lqe9OdPW-MCoApKnvi9w-wN4lb9Quu0X90dEn6L_b5zecNEF2b9-mjO-HLDDeveeHuWmFfElBTu282B8eHXbexzLBzXY_4vqgF12VGAeiv0puTdsc8Xf3Zmy7380m4qxizoHD771TsvsJzSr5_N-8l7Fy4hqwf65Quw793g417O_D3-PLvJheAWiwI28dNV_W-Ojd19w7kKnUkJ0UzysuqofzXVNZS8fqhIxt0P8a7VBS5ifxW-WRLUWBjI95vcxgfxSd7j75Nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبان نیایش ، شرق به غرب، قبل از باکری ,ساعت یازده صبح پنجشنبه @WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23993" target="_blank">📅 13:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش انفجار هایی در جده عربستان
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/23992" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0962eac3cf.mp4?token=sf5_7YWNTHUDsf2NHfuHxGt3dJ5_iRvxlOfIJpVlng5tNRVzMCKKrc57-TnQitLTPhvxuxrrbWtzwwmQe0277VIAPivlCjOGdF4VtPPg67vQqvWkkBNWB2dI4aCdrMMDOrZE-7ipqA87enC0iBhun73GloDeC5p7GfXZJSDReF3pI2yJLh6Wwk5vTtbmG0dXL_OY--O8g1KXj8dVzzXkN8XWcsto8fIP-3mcTjEPQjC0vgHVviw012iSvniL3BjKdicG9CrVqKf6HL5G6psq2MKRx-KT2cfczIfrpfhxGDXVdx4c7YT71esGXMtyp_Cig8GG4enO0WNUsAiWJo8owQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0962eac3cf.mp4?token=sf5_7YWNTHUDsf2NHfuHxGt3dJ5_iRvxlOfIJpVlng5tNRVzMCKKrc57-TnQitLTPhvxuxrrbWtzwwmQe0277VIAPivlCjOGdF4VtPPg67vQqvWkkBNWB2dI4aCdrMMDOrZE-7ipqA87enC0iBhun73GloDeC5p7GfXZJSDReF3pI2yJLh6Wwk5vTtbmG0dXL_OY--O8g1KXj8dVzzXkN8XWcsto8fIP-3mcTjEPQjC0vgHVviw012iSvniL3BjKdicG9CrVqKf6HL5G6psq2MKRx-KT2cfczIfrpfhxGDXVdx4c7YT71esGXMtyp_Cig8GG4enO0WNUsAiWJo8owQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبان نیایش ، شرق به غرب، قبل از باکری ,ساعت یازده صبح پنجشنبه
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/23991" target="_blank">📅 13:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fd497cbd.mp4?token=gODWYnXyww-kaeTt_JHtR4crx8_hruNBCMFb0u9GNrgsrU41_PoxeDingnNOFhWxllSh6lTVhJexCy_Sb1ejowbxy6CVIvv78fdEbm7g23ovyuRFfw68tr5Jp_cBTGh7FH4gx58LnI7B1sg_FQ8rq22-utweh21jloNlwUzLwkgT2qeX5BifJ1rSHawpqotoZqF_9KcPRKm2RSy64gDMy_xfHOFlloQ5OFucaVCspH53V_BErDOEAktyCctTUE0BSHHoYBcTtaCIo5rqR1nAYoOQvTL7ziHasLDXeZy0w-cO6oznPtX9Q6BgpnhDVWzfES3-jXnAG3QICxbJTCm2yxfLKsBuMYp88DCpIoFcw7gpJszz2o083fOr3pMgJ9mDNLWsc8cm9v4MHw3mEfnz6Z8u4zkbb7om2VEL2d597UcCMSMsqUqISlslKOqxbdKIcj3LQBFJoFgccSF5bURjoovjfv0p5dRDv7cTcu540bsz4RJ1qKpNu48OOeYZTequQ9dNBXP2pksjLFyWszEsa7Se-HK7YPJkXLOtStp-Ba45H-Roa-_gJZXcJH9eljM6lxp9moLcsdB_4MbmLKag5JDFSoxVG0wTRGhlN2bDQQUAKRKxh5fBGKpJ5guZzUPkD81Jf4SnUURawIPzBk3wo92eDDcw10BQqfhnOvktZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fd497cbd.mp4?token=gODWYnXyww-kaeTt_JHtR4crx8_hruNBCMFb0u9GNrgsrU41_PoxeDingnNOFhWxllSh6lTVhJexCy_Sb1ejowbxy6CVIvv78fdEbm7g23ovyuRFfw68tr5Jp_cBTGh7FH4gx58LnI7B1sg_FQ8rq22-utweh21jloNlwUzLwkgT2qeX5BifJ1rSHawpqotoZqF_9KcPRKm2RSy64gDMy_xfHOFlloQ5OFucaVCspH53V_BErDOEAktyCctTUE0BSHHoYBcTtaCIo5rqR1nAYoOQvTL7ziHasLDXeZy0w-cO6oznPtX9Q6BgpnhDVWzfES3-jXnAG3QICxbJTCm2yxfLKsBuMYp88DCpIoFcw7gpJszz2o083fOr3pMgJ9mDNLWsc8cm9v4MHw3mEfnz6Z8u4zkbb7om2VEL2d597UcCMSMsqUqISlslKOqxbdKIcj3LQBFJoFgccSF5bURjoovjfv0p5dRDv7cTcu540bsz4RJ1qKpNu48OOeYZTequQ9dNBXP2pksjLFyWszEsa7Se-HK7YPJkXLOtStp-Ba45H-Roa-_gJZXcJH9eljM6lxp9moLcsdB_4MbmLKag5JDFSoxVG0wTRGhlN2bDQQUAKRKxh5fBGKpJ5guZzUPkD81Jf4SnUURawIPzBk3wo92eDDcw10BQqfhnOvktZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز هواپیمایی وارش از تهران به شهر دوشنبه پایتخت تاجیکستان از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت
+ همچنین تمامی پرواز های ایران به دبی لغو شد
@warroom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/23990" target="_blank">📅 13:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این وضعت زندگی تو ایرانه من با پراید داغون اسنپ کار میکنم عراقی اینجا درس میخونه و بهترین زندگی میکنه این خیلی زور میاره ب ادم ک ما جوونا هیچ تصویر ذهنی از این ماشینا نداریم
😞
💔
(دانشگاه کاشان)</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/23989" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromreza.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzSvrJxOuKVNAfh7DsWRkJpvYA1kO7laIOt5ae3jjCe9Ii9UFBfoBiKsFyE6muQHd_FeXZCdwjTdwDIp2aPna7hA6IGOCS-3lzXLVGQMwuWDqgU4RL89ZhcH0oNj1voyZVAmG3lY8DfGLsf4KDFDZfC5-TfFbA1LbFOndPrZ9I6cl4W6N4HLGVmpfYNTNbsuZO_MtA50QE1KDsAatKDWs8GNQMH9so4WZA6CmAguqy9dyI06uNHqOkT1Q2CfRLvOhrcycXFzMycSeCnB3xtwYYjsGMbYB4T_BmnOiyGenk6K53jW4LH7LTQAZMG98bqZG_oOFVaxxIgNEDTzzATqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وضعت زندگی تو ایرانه من با پراید داغون اسنپ کار میکنم عراقی اینجا درس میخونه و بهترین زندگی میکنه این خیلی زور میاره ب ادم ک ما جوونا هیچ تصویر ذهنی از این ماشینا نداریم
😞
💔
(دانشگاه کاشان)</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/23988" target="_blank">📅 13:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تلویزیون اسرائیل اعلام کرد که برنامه سفر نخست وزیر به نیویورک، شامل دیدار با ترامپ نیست و او بلافاصله پس از سخنرانی به کشور باز می‌گردد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/23987" target="_blank">📅 13:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش اختلال شدید جی‌پی‌اس در‌تهران
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/23986" target="_blank">📅 13:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روزنامه ال موندو: دستگاه اطلاعاتی آمریکا به چند دولت اروپایی هشدار داده که ممکن است روسیه در حال برنامه‌ریزی برای عملیات پهپادی علیه اسپانیا، فرانسه یا ایتالیا باشد
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/23985" target="_blank">📅 13:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری‌های رژیم: تمامی پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی، از نیمه شب گذشته، لغو و اطلاع رسانی شده و مربوط یه الان نیست
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/23984" target="_blank">📅 13:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یک منبع اسرائیلی: ایران فعالیت‌های خود برای انتقال و تقویت تأسیسات هسته‌ای در منطقه کوه کلنگ، در نزدیکی نطنز، را افزایش داده است.
این منبع مدعی شده در صورت عبور تهران از «خطوط قرمز» تعیین‌شده، اسرائیل بار دیگر برای حمله به تأسیسات هسته‌ای ایران اقدام خواهد کرد. گزارش‌های پیشین نیز از ادامه فعالیت‌های عمرانی و تقویت ورودی‌های مجموعه زیرزمینی کوه کلنگ خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/23983" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسکات بسنت وزیرخزانه‌داری به فاکس‌نیوز:  ما اکسیژن رژیم را قطع کردیم ، انها ۵۰،۰۰۰ نفر را کشته اند ( بیش از ۴ دقیقه با زیرنویس) @WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/23982" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e053007122.mp4?token=HcvK8znslZ2A4zwzhpMUUWCt23iZv5lmxlVCW8A-c-ZX7SUcjmeMOpQ-1wxNLzwp3lEn8P0NIuv68XZnXW8vA4HN6bhuLnyJGzopOY8jZ5oywft5kmzwnVehwqSnNEUH_n1zLHM6avdyG2roiOZRQP-9Av0TJduCmTvLTejl7q6GchDtlAVz5V_Tk6JEeXYDHvAm3SXL0o6wya9Soqe17i6yKIL8E_ziRBCJ1n_H1TnQ-7kNs54TSXXxTwfldPzggWWPyQuh7Oq7qi44ngirriGRgJZNo91VIRoPHmH4TaKMlmVScx_SoOAaWwbiX_MN0v9w6pMw2L7xwysa9vjSkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e053007122.mp4?token=HcvK8znslZ2A4zwzhpMUUWCt23iZv5lmxlVCW8A-c-ZX7SUcjmeMOpQ-1wxNLzwp3lEn8P0NIuv68XZnXW8vA4HN6bhuLnyJGzopOY8jZ5oywft5kmzwnVehwqSnNEUH_n1zLHM6avdyG2roiOZRQP-9Av0TJduCmTvLTejl7q6GchDtlAVz5V_Tk6JEeXYDHvAm3SXL0o6wya9Soqe17i6yKIL8E_ziRBCJ1n_H1TnQ-7kNs54TSXXxTwfldPzggWWPyQuh7Oq7qi44ngirriGRgJZNo91VIRoPHmH4TaKMlmVScx_SoOAaWwbiX_MN0v9w6pMw2L7xwysa9vjSkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف رفت مدرسه بچه ها  ترسیدن
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/23981" target="_blank">📅 12:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">استانداری خوزستان: صدای انفجار شنیده شده در آبادان، ناشی از نقص فنی در پالایشگاه این شهر است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23980" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک پست:
سه مرد بامداد چهارشنبه حدود ساعت ۴:۳۵ از یک دریچه فاضلاب در نزدیکی هتل محل اقامت بنیامین نتانیاهو در نیویورک خارج شدند و با دو خودرو از محل گریختند. پلیس نیویورک می‌گوید فعلاً نشانه‌ای از ارتباط این افراد با نتانیاهو یا تروریسم وجود ندارد، اما به‌دلیل حساسیت محل و برگزاری مجمع عمومی سازمان ملل، همراه با نیروهای فدرال تحقیقات و بررسی‌های امنیتی بیشتری انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23979" target="_blank">📅 11:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زلنسکی : اوکراین دو سرباز کره شمالی را که در روسیه اسیر شده بودند، به کره جنوبی فرستاده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23978" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqzgYQa40fhC8T0UlxdauZjWLuielcBBRxNppNlTxHhbrSLGYNAPT651PrT5ha5wSsWGVm9QiCDA2BJeYN4mHzs8t-wc7PlHwqtbnPLKnAJ3Zt26cwZmXcCZo1At2y9kChl1cnOngzHhmfVusidf1WdYYnGT2GXkixZ-MPOK58Ry1XW6lsRchmkFI7KbXqKPSvOh7pn11uQMSmUgczKwuSI2PC0GsoP3c3oVYA09B19_RvbiL_aXIdWpKwPGkCYk3XIDFdPRvLujiNINnxe3NsyOu4jAAACOgVXJDxcJMyOLy1z1qDAVuIqvyLsr0qsew2JTO7QbN1lTureR0oroEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
محمود عبدالفتاح عواد، فرمانده شاخه نظامی حماس در شهر غزه که به گفته ارتش اسرائیل در نگهداری
۷ گروگان اسرائیلی
از جمله دانیلا گلبوعا، کارینا آریِف، دورون اشتاین‌برخر، نعما لوی و زیو برمن نقش داشت، در حمله هوایی اسرائیل در آخر هفته کشته شد. ارتش اسرائیل همچنین مدعی شده او اخیراً در برنامه‌ریزی حملات علیه نیروهای اسرائیلی و بازسازی توانمندی‌های حماس نقش داشته است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23977" target="_blank">📅 11:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دولت بریتانیا:
محدودیت‌های مالی علیه پنج بانک ایرانی فعال در بریتانیا، شامل
بانک سپه، بانک ملی، بانک صادرات، پرشیا اینترنشنال و بانک تجارت
را تشدید کرد. بر اساس دستور جدید خزانه‌داری بریتانیا، درخواست مجوز این بانک‌ها از این پس به‌طور پیش‌فرض رد می‌شود و تنها در موارد
الزام قانونی یا شرایط استثنایی و فوری
امکان صدور مجوز وجود دارد. همچنین مجوز عمومی فعلی این بانک‌ها پس از پایان اعتبار در
۲۲ اکتبر ۲۰۲۶
تمدید نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/23976" target="_blank">📅 11:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd879fd06.mp4?token=KSd8KgzZkRmZJb7RcYCNHkbRJFpyelhwvUXpSQ9g_2nbTAvSC_7JGucNMkW71hyWIxkkdUjbi2d8uXkrpc_0BPrjObMlce_A5ry5LKyZEL51y4nOXx1IuUvQi0o5Z781RIpEF-qmLNpyupIjwKojsG8c42e9Zp6mW5EPLrJyVbU_WMUVOu7PulVzYCS9Ax7reKTIxSARm_YmlzU4Wb4NIqYgOn670S1rtpR51Edq6hpVBe64Yt38N_eCbQF4qirIfg_lBDvcIjGzZM-H7amla0lYZgradoiouGytTJABQUvrEugyzgqEdOiXzzsLXxLxki3NHJfcQJeG3WUSrqoA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd879fd06.mp4?token=KSd8KgzZkRmZJb7RcYCNHkbRJFpyelhwvUXpSQ9g_2nbTAvSC_7JGucNMkW71hyWIxkkdUjbi2d8uXkrpc_0BPrjObMlce_A5ry5LKyZEL51y4nOXx1IuUvQi0o5Z781RIpEF-qmLNpyupIjwKojsG8c42e9Zp6mW5EPLrJyVbU_WMUVOu7PulVzYCS9Ax7reKTIxSARm_YmlzU4Wb4NIqYgOn670S1rtpR51Edq6hpVBe64Yt38N_eCbQF4qirIfg_lBDvcIjGzZM-H7amla0lYZgradoiouGytTJABQUvrEugyzgqEdOiXzzsLXxLxki3NHJfcQJeG3WUSrqoA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوئی که
گفته می‌شود پیامدهای حمله ایران به یک نفتکش LNG
(
گاز طبیعی مایع
) را نشان می‌دهد؛ این کشتی بامداد چهارشنبه در حال عبور از
تنگه هرمز
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23975" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/23974" target="_blank">📅 10:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ایران در مذاکرات غیرمستقیم با آمریکا در نیویورک، یک هفته به واشنگتن فرصت داد تا با شروط تهران برای بازگشایی تنگه هرمز موافقت کند؛ اما مذاکره‌کنندگان آمریکایی این درخواست را رد کرده و گفتند ایران کنترل تنگه هرمز را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23973" target="_blank">📅 10:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آنتونیو کوستا، رئیس شورای اروپا، پس از گفت‌وگو با پزشکیان از ایران خواست همکاری با آژانس بین‌المللی انرژی اتمی را از سر بگیرد، حملات به کشورهای همسایه را متوقف کند و آزادی کشتیرانی در هرمز را برقرار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23972" target="_blank">📅 10:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسکات بسنت وزیرخزانه‌داری به فاکس‌نیوز:  ما اکسیژن رژیم را قطع کردیم ، انها ۵۰،۰۰۰ نفر را کشته اند ( بیش از ۴ دقیقه با زیرنویس) @WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/23971" target="_blank">📅 10:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیروی دریایی آمریکا: ۸ مورد اقدام به خودکشی در گروه رزمی ناو «آبراهام لینکلن» ثبت شد.
به گفته هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، این موارد در میان خدمه ناو، بال هوایی، ناوشکن‌های اسکورت و دیگر نیروهای گروه رزمی در جریان مأموریت طولانی آنها که شامل عملیات علیه ایران نیز بود، ثبت شده است. این ناو و گروه رزمی آن حدود
۲۸۶ روز
در مأموریت بودند و هیچ مرگ ناشی از خودکشی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23970" target="_blank">📅 10:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسکات بسنت وزیرخزانه‌داری به فاکس‌نیوز:
ما اکسیژن رژیم را قطع کردیم ، انها ۵۰،۰۰۰ نفر را کشته اند ( بیش از ۴ دقیقه با زیرنویس)
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23969" target="_blank">📅 10:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فاکس‌نیوز: اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت احتمالاً بیش از ۸۰ تا ۹۰ درصد پروازهای خارجی ایران لغو شده‌اند.
او افزود: «مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان برگردند.» این اظهارات پس از تحریم‌های گسترده آمریکا علیه صنعت هوانوردی ایران مطرح شده؛ با این حال، برخی پروازهای ایران به چین، ترکیه و امارات همچنان برقرار بوده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/23968" target="_blank">📅 09:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543ea3d1d0.mp4?token=q5B5AD_ZuwSpHRn5mR1gAQIQLBOj4cki0d4x2Eouz8JUqLtfkxtCPwn8VaxO5CK56ij2pPV0tmt0ICFCI5_82VgOCS2tTZGbUlgPP1nQ5_bkr4JHR0GMASO6IBxB4zl36gYWAoDfTZpoOKeOIXgYtcoGRMHYcxaFsgTxQdQRoXWTwpybo7eOKxiyKR3sc1k0Cs7mw-kuKKU3CER1MYpszEv4bXwhMhqizJQw3HdVFn-y6HCdjpj-Yf7rrvZKaBevDrXGVKy13h1iyR5_aSxIl5UCTVb74jLuaNnsZr-1Y_XwmaNkw2bgdVJYxwh3oRrMzNoquZotDnbmnNu238qnsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543ea3d1d0.mp4?token=q5B5AD_ZuwSpHRn5mR1gAQIQLBOj4cki0d4x2Eouz8JUqLtfkxtCPwn8VaxO5CK56ij2pPV0tmt0ICFCI5_82VgOCS2tTZGbUlgPP1nQ5_bkr4JHR0GMASO6IBxB4zl36gYWAoDfTZpoOKeOIXgYtcoGRMHYcxaFsgTxQdQRoXWTwpybo7eOKxiyKR3sc1k0Cs7mw-kuKKU3CER1MYpszEv4bXwhMhqizJQw3HdVFn-y6HCdjpj-Yf7rrvZKaBevDrXGVKy13h1iyR5_aSxIl5UCTVb74jLuaNnsZr-1Y_XwmaNkw2bgdVJYxwh3oRrMzNoquZotDnbmnNu238qnsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای استقبال ترامپ و ملانیا از شی و همسرش. در لحظهی که دو بمب افکن B1b رد میشن، قیافه ترامپ و اداهایی که در میاره دیدنیه
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23963" target="_blank">📅 09:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال‌استریت ژورنال:
در شش ماه نخست ۲۰۲۶ حدود ۱۳۰۰ محموله قطعات دوکاربردی از چین به وزارت دفاع ایران ارسال شده که برخی در ساخت پهپاد و موشک‌های بالستیک کاربرد دارند. چند روز پیش از آغاز جنگ نیز حدود ۳۰۰ تن ترکیبات شیمیایی از چین به ایران ارسال شد و در جریان جنگ، بیش از ۱۰ محموله دیگر از قطعات پهپادی به ارزش بیش از ۶ میلیون دلار وارد ایران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23958" target="_blank">📅 09:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ژاپن:
نخست‌وزیر ژاپن، سانائه تاکائیچی، خواستار آن شده که مذاکرات درباره هرمز فقط میان ایران و آمریکا نباشد و کشورهای وابسته به این مسیر و سازمان بین‌المللی دریانوردی نیز در آن حضور داشته باشند. ژاپن می‌گوید حدود ۹۳ درصد نفت وارداتی‌اش در شرایط عادی از مسیر هرمز عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23957" target="_blank">📅 09:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدای انفجار سیریک(میناب) مربوط بود به یه موشک/پهپاد که پرتاب شده بود و رو هوا رهگیری کردن آمریکایی‌ها و زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/23956" target="_blank">📅 00:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1iUvXijEt7kGaee-FRXJBG8DOV-n1OT0YmBahwxFf4WWgGWhj7D-VfybQfZcn7w4xX_CMU7fSz_7FjRSQTORx2uJcTZqCIU5VwA02_s2ksXCTNKXQYpR-7SHwsc6s-jfaKZcl5lWXxc5Edwv3wc6RKmE_O5UWZZJpft6YwdV7Y9leuAMba-EssglmlvkAwm9u4wEiAwaLldgLzDQKB4iuf7qy_E_TSYLfDbkg-fR-feCASc2tJF0f3wBgZ5_fcCeftkufQZLZIR77W0G5QCXOkZLJz0FNmLuRcTt_19E5OMXszyAwcynKnm_sr_5RrWYIlvjzu_xmLMnMPEsQDSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوخترسان از اسرائیل بلند شدن به سمت منطقه  ، ۴ سوخترسان بر روی تنگه هرمز / خلیج فارس
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/23955" target="_blank">📅 00:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش صدای جنگنده نطنز
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23954" target="_blank">📅 00:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش صدای انفجار‌ خارگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23953" target="_blank">📅 00:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش صدای انفجار‌ و لرزش شدید میناب
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23952" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رگباری گزارش میاد از انفجار در بندر عباس
@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/23951" target="_blank">📅 00:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23950" target="_blank">📅 00:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a2badc4b.mp4?token=AZ9TZVM27pQkvBD9zn7w7GGmySnHVoSJwiQ583HsRv1i01SOy6dGLRMkX1gSRYy9lPxxc79npoHtKz6xIx0SUjB7qjDDF-8GzBBSrZGh90Z1H1JMethIME8Lj4XQl_RQHlrT-gKvWueMHZipApRjVN-VBhIrrWxgOxRHaA0FFFQ9toducB1H4W07BBKnc9aaqDf5LdRNr-D3OWv8RYCXwWULHG6wvwfFtklhSJxYhql691WJtDoUQQozqrOodm7P_vA8xNf5lp1P2whdnWtiYpm_eL-1qg0vw7TtRr7ygkmU33AquEfJ9OU3fEGjyVCQ3Pjn5aNXFqoAzubQDKLq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a2badc4b.mp4?token=AZ9TZVM27pQkvBD9zn7w7GGmySnHVoSJwiQ583HsRv1i01SOy6dGLRMkX1gSRYy9lPxxc79npoHtKz6xIx0SUjB7qjDDF-8GzBBSrZGh90Z1H1JMethIME8Lj4XQl_RQHlrT-gKvWueMHZipApRjVN-VBhIrrWxgOxRHaA0FFFQ9toducB1H4W07BBKnc9aaqDf5LdRNr-D3OWv8RYCXwWULHG6wvwfFtklhSJxYhql691WJtDoUQQozqrOodm7P_vA8xNf5lp1P2whdnWtiYpm_eL-1qg0vw7TtRr7ygkmU33AquEfJ9OU3fEGjyVCQ3Pjn5aNXFqoAzubQDKLq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی از خبرنگار خارجی میپرسه نظرت درباره تیم ملی ایران تو جام جهانی چه بود؟
خبرنگار خارجی‌ میگه : جالب بودید، مخصوصا اون عینک شجاع خلیل زاده
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23949" target="_blank">📅 23:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏حالا من کاری ندارم ولی این یارو «باصر بهرام نژاد» که محافظ موشعلی بی گور  بوده و تو جنگ اخیر سقط شده ، بیشتر بهش میخوره بابای نوه های خامنه ای بوده باشه تا محافظش @withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23948" target="_blank">📅 23:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تنگه صدای  بادیگاردهای خامنه‌ای میاد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23947" target="_blank">📅 23:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری The National
: طبق اطلاعات منابع منطقه‌ای، طرح ایران شامل
آتش‌بس منطقه‌ای تا ۶۰ روز، بازگشایی مرحله‌ای هرمز، پایان محاصره آمریکا و تعیین یک جدول زمانی برای مذاکرات جامع
بوده است. این منابع می‌گویند
ترامپ فعلاً حاضر نیست محاصره را پیش از مشاهده «اقدامات اعتمادساز» از سوی ایران لغو کند
.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23946" target="_blank">📅 23:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارتش اسرائیل در عملیات گسترده ۲۳۰ فرد را بازداشت کرد و یک آزمایشگاه بمب را کشف و منهدم کرد.
تیپ ناحال ارتش اسرائیل طی ماه‌های اخیر در مناطق یهودیه و سامریه (کرانه باختری) بیش از
۱۲۰۰ مکان
را بازرسی کرده، حدود
۱۰۰۰ مظنون
را مورد بازجویی قرار داده و بیش از
۱۰۰ قبضه سلاح
کشف و ضبط کرده است. به گفته ارتش اسرائیل، نیروها همچنین یک آزمایشگاه تولید مواد منفجره را شناسایی و منهدم کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23945" target="_blank">📅 23:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2od5axPQiIDfrdYKqz7geX2I_gz0_wLExWb9ycgCHl6gqPCqM7kP8rv9nMKMiQSe4TtPAs5hxAW6ucwg39-lVErP4G07IuYOR_tCIPITgqX3e2bFjFTbk29AAvGFJAEApfawp2wJd0r8ZQ6BIP3Qrds4ZHWyedAAHGsGLxnMH_SjPA8SHHKKfLoqNHp5QV-yp6HoEWyIfN6ZcuvTQVtf5PAzOXzlpOggSrHUjz6iqtKW2ls5QnsCcN8xnBQWxZbfYJqEHAB3VoISMz9HSCGYrtZ5P3AjXgA2mtLo9-n6EVCSftOYkLPIRX4KGfowT2muhqmCEq816wye89nymp7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز امنیت دریایی عمان اعلام کرد کشتی تجاری
CAPE DAO
در نزدیکی استان مسندم و در فاصله ۲.۵ مایل دریایی از ساحل هدف قرار گرفته و در پی حمله، موتورخانه کشتی آتش گرفته است.
۲۷ خدمه تخلیه شدند و یک خدمه، که یک شهروند هندی بود، جان باخت.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23944" target="_blank">📅 23:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پزشکیان در نیویورک در هتل مستقر نشده است؛
رئیس‌جمهور ایران به‌جای هتل، در
محل اقامت نماینده ایران در سازمان ملل (رزیدانس)
مستقر شده است. فارس دلیل این اقدام را کاهش هزینه‌های سفر عنوان کرده و گفته این اقدام برای نخستین‌بار توسط یکی از روسای‌جمهور ایران انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23943" target="_blank">📅 22:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رویترز : ایران تهدید به فلج کردن فرودگاه‌های کشورهای همسایه کرد:
محسن رضایی، دبیر شورای عالی امنیت ملی ایران، گفت اگر کشورهای همسایه در همکاری با آمریکا پروازهای ایرانی را متوقف کنند، ایران کاری خواهد کرد که فرودگاه‌های آنها دیگر قادر به فعالیت نباشند. این تهدید در پی اعمال فشارها و تحریم‌های جدید آمریکا علیه شرکت‌های هواپیمایی ایران مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23941" target="_blank">📅 22:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چقد زرنگین‌ برای پست نتانیاهو ریکشن خنده رو میبندی</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23940" target="_blank">📅 22:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBI DO?</strong></div>
<div class="tg-text">چقد زرنگین‌
برای پست نتانیاهو ریکشن خنده رو میبندی</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23939" target="_blank">📅 22:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانادا: امروز پنج فرد و پنج نهاد ایرانی را تحریم کرد.
وزیر امور خارجه کانادا اعلام کرد این تحریم‌ها تحت مقررات اقدامات ویژه اقتصادی علیه ایران اعمال شده و دلیل آن، از نگاه دولت کانادا، نقش این افراد و نهادها در
نقض حقوق بشر، سانسور، سرکوب و استفاده از خشونت غیرقانونی
عنوان شده است. در میان افراد تحریم‌شده
اسکندر مومنی، وزیر کشور ایران، داوود معظمی گودرزی، رئیس پلیس فتا تهران بزرگ، رسول جلیلی، محسن فتحی‌زاده و روح‌الله مومن‌نسب
قرار دارند. پنج نهاد نیز شامل
ساترا، کارگروه تعیین مصادیق محتوای مجرمانه، گروه دوران، شرکت یافتار پژوهان پیشتاز رایانش و سازمان فضای مجازی سراج
هستند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23938" target="_blank">📅 22:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPxBakvUK48399bG_TLfuJ5AgEn1IoMKf5Q5-XRyAWBHfQOLSUE6be049UYl73wOIVP5HsrZty5hVHcpE1iUb6IsR6v_zdjk4mWrls7hz7qOaK4z_K1RL6t3We9LaZQoEA2QqVW_eh55LXQGaCybgTHRNJjup-Z89upR7c-o1QzP6QnC8BcSLPjUkz4emuDr-we9C5LcKSwo-qZjdnJlVmKYj-8PvD62YRssiVNF4Wjd1nnqA9fhzymrivJkDj2bChrnEaaOfcMxwaZopYAeoDgsXmWOnvWSppbpkG34C5LuOqngz433xvj80fQtbgXccsArEbrtJRGCxa3b4Y2BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت به 103.52 دلار برای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23937" target="_blank">📅 22:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الجزیره ,جزئیات مذاکرات ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل:
ایران از طریق میانجی قطری شروط خود را به آمریکا منتقل کرد که شامل
پایان جنگ در همه جبهه‌ها، توقف اقدامات نظامی آمریکا، رفع محاصره دریایی، پایان جنگ اقتصادی و آزادسازی دارایی‌های ایران
است. اسماعیل بقایی، سخنگوی وزارت خارجه ایران، این شروط را اعلام کرده است. در همین حال، استیو ویتکاف، فرستاده ویژه آمریکا، گفت دو طرف از طریق میانجی‌ها مذاکرات طولانی و فشرده‌ای داشته‌اند و این گفت‌وگوها را «سازنده و امیدوارکننده» توصیف کرد. تهران بازگشایی تنگه هرمز را نیز به کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران مشروط کرده و گفته است در صورت تحقق این شروط، امکان بازگشایی هرمز ظرف هفت روز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23936" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e07f1b30d.mp4?token=szfVlLYPB-luud3CxIcJtfe0aVvv2rlfS0K5ruPVN7i4w7fgumUQlNvqhwWfEHhH_612IJQsCUu3mif1khTDtyGHU1FVav6E4A_r1nDYXOKd_hPULxij6tDDV6eWT5dCqQCw9FP2YGBbcAHR4mmJyn9Jveg0yLDv4cZnk-sCcgJznq_C6ogwH6kdpFx6nrQ4YCFVUiEv-8JZpVMEXhcnZ-J_MO8fvAkKV7Mz8__XuHtxC4JMYw_WBwrtCpRb69C_Wvlioag6vUqS-TaC7XfiX5Dgw10wt-pN91C3u8iHyllFlQtUK0WDD9Dk8F-jQk0qmNN6lwSQBtxz8Dh3KcHcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e07f1b30d.mp4?token=szfVlLYPB-luud3CxIcJtfe0aVvv2rlfS0K5ruPVN7i4w7fgumUQlNvqhwWfEHhH_612IJQsCUu3mif1khTDtyGHU1FVav6E4A_r1nDYXOKd_hPULxij6tDDV6eWT5dCqQCw9FP2YGBbcAHR4mmJyn9Jveg0yLDv4cZnk-sCcgJznq_C6ogwH6kdpFx6nrQ4YCFVUiEv-8JZpVMEXhcnZ-J_MO8fvAkKV7Mz8__XuHtxC4JMYw_WBwrtCpRb69C_Wvlioag6vUqS-TaC7XfiX5Dgw10wt-pN91C3u8iHyllFlQtUK0WDD9Dk8F-jQk0qmNN6lwSQBtxz8Dh3KcHcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : تا امروز ۲۳ سپتامبر، ۱۱۵ کشتی تجاری برای اجرای محاصره «دیوار فولادی» آمریکا تغییر مسیر داده‌اند.
از آخرین بروز رسانی‌ دیروز ،
پنج کشتی جدید تجاری دیگر جلویشان گرفته شده و بازگردانده شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23935" target="_blank">📅 22:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تایمز اسرائیل : بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امشب عازم نیویورک می‌شود و صبح پنجشنبه ۲۴ سپتامبر وارد آمریکا خواهد شد. او قرار است ساعت ۲ بعدازظهر به وقت نیویورک در مجمع عمومی سازمان ملل سخنرانی کند و همان شب، بدون حتی یک شب اقامت در نیویورک، به اسرائیل بازگردد. این سفر به‌شدت کوتاه شده و گزارش‌ها از ملاحظات امنیتی و نگرانی‌های مربوط به اعتراضات و شرایط منطقه‌ای به‌عنوان عوامل این تصمیم خبر می‌دهند. نتانیاهو نیز گفته است که در سخنرانی فردا «غافلگیری‌هایی» خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23934" target="_blank">📅 21:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695a72d7e.mp4?token=tH4hRjRCOHpcJP0J63OdF2JMXG_OtHmeqotiI6BAeM_1PzVSo40vWyjCj9u9MuZACa2UHmZKVgOwqmStvLbJkN6xLq3juJpMD5PxDnYc9bM5rGyYI1kUP-g9WSBb3kpww4dZwAmHt5_m0UeL9H6Gzlf9aQv9cjETcsGs-qj5J4xyZpMxe831shN0CsE3zEx9irWs1qs9ThdSZ4Y5xv6zuuorUy_BbSievTk7AzC4C0NXLvItXToUrjQ6Xp6_Ty31oqKpyhA4BuiTi4JQZrIuFLl41YVnY8B9RFZrzdddilKR1Bk6_mzPuysYFoQk6s2SiiRjzX5-90W2DZ1kWWBYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695a72d7e.mp4?token=tH4hRjRCOHpcJP0J63OdF2JMXG_OtHmeqotiI6BAeM_1PzVSo40vWyjCj9u9MuZACa2UHmZKVgOwqmStvLbJkN6xLq3juJpMD5PxDnYc9bM5rGyYI1kUP-g9WSBb3kpww4dZwAmHt5_m0UeL9H6Gzlf9aQv9cjETcsGs-qj5J4xyZpMxe831shN0CsE3zEx9irWs1qs9ThdSZ4Y5xv6zuuorUy_BbSievTk7AzC4C0NXLvItXToUrjQ6Xp6_Ty31oqKpyhA4BuiTi4JQZrIuFLl41YVnY8B9RFZrzdddilKR1Bk6_mzPuysYFoQk6s2SiiRjzX5-90W2DZ1kWWBYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:ما برای وقوع معجزه‌ای دعا می‌کنیم که جان پسر سفیر اسرائیل در آمریکا را نجات دهد. او در جریان یک حادثه تصادف در کرانه باختری مجروح شده است. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23932" target="_blank">📅 21:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">در آخرین درگیری امروز قرارگاه قدس نیروی زمینی سپاه و مهاجمان در منطقه سراوان ‌فرمانده قرارگاه عملیاتی سجاد ، حسین ظریفی ‌کشته شد @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23931" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxdDa8oRZcUb_lLQpTrt8XndUsWPk-lp75d5wPknlWgjSYmelwUUXm8l3dp4BvnGM_P-sKwr67sKpw6MWpQJYehC1vsuQqrcADyNX--77MvsJKngj73vYnfyl_cEIWoA2HMuUuyPhxdjokhZNrVX3WyKe5AW5mVW-GmdCp2Upn_gXCxgJbbbES361MT1Bqdhv3FAJBB7ThuSQHuZZ_wSUzcIXPyGa48KspWOR6LJos-NdZ2Ea2kMo0D3xT4LNmeBqBx1SH8RlM49hR86GsyIoecNb63B4d4Zy_nlqion553dA8SYy-v7RIfXzmpform4AmYr57ki4PPJpLuwlOkHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری شدید نیروهای مزدور رژیم با گروهای مسلح در سراوان همین الان ! @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23928" target="_blank">📅 20:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو:ما برای وقوع معجزه‌ای دعا می‌کنیم که جان پسر سفیر اسرائیل در آمریکا را نجات دهد. او در جریان یک حادثه تصادف در کرانه باختری مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23927" target="_blank">📅 20:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK6TuytkJm7oCIurNG0HAX2OYscvb32oeUp8wIm6yqUKudWITWK80itsW-QJConQrjdW9JC5RKWujg48r2imemQv4XaxnrVgv2iQdPLv1EHOip1ku8W2L6m37u1E1Eoo3x5UgSPClwH1FoIWrYi1O2OXnkqZkdLOyWi3yZ_1skFOcu29RoJlUWAe2d1BQkfWMPQDFXr4Wi83V_Tcc2PJ0LWHAxvKXqXXF0LE2KgTd_Tv1wxfruJYotEdS5H-5_znfA_CqQSUpm66eity4FUuJZFAgbV4BMZ1PjRMC99EjW1tcIsxVNC17ohbuETNZ1mgj0LJKHDqjHQwWskxqkYsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر و داماد پزشکیان در سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23926" target="_blank">📅 20:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز:
چین پیش‌تر از ایران خواسته بود برای مهار حوثی‌ها اقدام کند؛ این درخواست پس از افزایش سریع نفوذ نظامی حوثی‌ها و نگرانی عربستان از تهدید باب‌المندب مطرح شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23925" target="_blank">📅 20:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد. این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23924" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ایران:
مذاکره بس است.
عمل کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23923" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506767e20.mp4?token=c_tPX3nTVOdbl37wuF-mEfingCa5IgOR0fH4aLtHZqR1BsKmjeEpVXq9qK80XdUQFqqYeZFOvaG05CxMze6oXls8U-yTdwwQcoqrVtAf_aFdNhblcTyCQXkWrMaOYHZYFP4i6gYuacwkwv6gh_DELbVcaSxAwokNmMDQgvm4nxOhsvV4TSn12RrhjZNAjfO3XzgyD19-AftOrPxZc4rTiW7ST06db5K2ay5-MUO2uvKFK8QWbPg-lTQSPT-l1cEjXDQ8fC3XCsYxvkjk4aGXW9E-GOegcj8tUHdvYB3KY82i2hjY4QZXz2hcZeB__vmGspbKvuFw2NvV_As1t0QOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506767e20.mp4?token=c_tPX3nTVOdbl37wuF-mEfingCa5IgOR0fH4aLtHZqR1BsKmjeEpVXq9qK80XdUQFqqYeZFOvaG05CxMze6oXls8U-yTdwwQcoqrVtAf_aFdNhblcTyCQXkWrMaOYHZYFP4i6gYuacwkwv6gh_DELbVcaSxAwokNmMDQgvm4nxOhsvV4TSn12RrhjZNAjfO3XzgyD19-AftOrPxZc4rTiW7ST06db5K2ay5-MUO2uvKFK8QWbPg-lTQSPT-l1cEjXDQ8fC3XCsYxvkjk4aGXW9E-GOegcj8tUHdvYB3KY82i2hjY4QZXz2hcZeB__vmGspbKvuFw2NvV_As1t0QOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در سخنرانی مجمع سازمان ملل به جای لغت سانتری‌فیوژ گفت سانتیری فوژ
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23922" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26cd367cad.mp4?token=jDrQrPyWUkldviwOsGsGh6XAK-jqtWkLFt4I6JIn56XOmecr8QKD9yJPaPxCaOfKGsc2K8aAUuvvN4NtJUtxyasmLAzmhzvJ0beEnpscumcgoYLvrRaTfgxEiM26cIiAIo-HDRiBgvsN6QIpNuhLBpNbMZnYR3Xas8TCBqmdv_wxU3tX-hcXmzB08sXF96YSc0sjErlSm8-MZaY5EG0obx0kiUrgj61YHc57HYAyt7DsuXq8ncPuixnwPwOonrt-9xqvC7DHFnScWbfH_Y8s9MccoNEaz18rImKvsYz4-UcXjDbRXBj94qrWPIahjWnyqaWf8VmYFiJceIyDO9u8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26cd367cad.mp4?token=jDrQrPyWUkldviwOsGsGh6XAK-jqtWkLFt4I6JIn56XOmecr8QKD9yJPaPxCaOfKGsc2K8aAUuvvN4NtJUtxyasmLAzmhzvJ0beEnpscumcgoYLvrRaTfgxEiM26cIiAIo-HDRiBgvsN6QIpNuhLBpNbMZnYR3Xas8TCBqmdv_wxU3tX-hcXmzB08sXF96YSc0sjErlSm8-MZaY5EG0obx0kiUrgj61YHc57HYAyt7DsuXq8ncPuixnwPwOonrt-9xqvC7DHFnScWbfH_Y8s9MccoNEaz18rImKvsYz4-UcXjDbRXBj94qrWPIahjWnyqaWf8VmYFiJceIyDO9u8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو، درباره مهمات جنگ با ایران : ما مهمات کافی برای دستیابی به اهداف خودمان در صورت ایران داریم، اما تنها در ایران نیستیم.
ما تعهداتی در منطقه هند-اقیانوس آرام داریم. ما تعهدات فزاینده‌ای در فرماندهی جنوبی داریم. ما تعهدات و متعهد بودن‌هایی به ناتو و شرکایمان در آنجا داریم. هر بخشی از جهان که بروید و به آن‌ها بگویید که پنج سرباز آمریکایی کمتر و دو هواپیما کمتر خواهد بود، همه وحشت‌زده می‌شوند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23921" target="_blank">📅 19:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، شروط رژیم را اعلام کرد: در حاشیه نشست مجمع عمومی سازمان ملل، در ادامه گفت‌وگوهای میانجی‌گرانه بین ایران و آمریکا،
از طریق میانجی قطری میان دو طرف پیام‌هایی ردوبدل شد
. این روند حدود دو ساعت ادامه داشت و شروط ایران برای احیای دیپلماسی به‌گونه‌ای مطرح شد که
هیچ شک و شبهه و بهانه‌ای برای طرف آمریکایی باقی نماند
.
بقایی افزود:
شروط ایران روشن و شفاف است
؛
توقف اقدامات تجاوزکارانه آمریکا، از جمله حمله محاصره دریایی و تروریسم اقتصادی، پایان جنگ در همه جبهه‌ها، آزادی اموال مسدودشده یا محدودشده ایران و پذیرش مسیر امن کشتیرانی مطابق توافق میان دو دولت ساحلی
…
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23920" target="_blank">📅 19:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f84599d5.mp4?token=sdWUMfU1036GV6A4nQ1hJ9OAYaTUUqZXCXvZFGUrvFyZAghBx9NMfZn5ZYFr8UWEG1au5NZpnTehBmpbFGOAzPYl7UEqDJd5PTqjU1LKPcqv-4GdNzKlhP6zy8WrdSN4dpIUHv1RA_SwBk-DX0x1HN9lFTuM0xpu8v8SIRO-fxhPxxyCq158BqgCzjp32AMYk6cHCbEpS6EU6qczeunBG2ZvNzL5B5b_fOc3a5iZ4MGW9B-7enXbeZCwnKugCCxS-bep7d7bUbVIn_ceOZNKZhEz06VXInEJMJ2qbSRHR8pcouG7UusK0Ks-HCo3k-BENODQuszwc-elKlrDZOlP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f84599d5.mp4?token=sdWUMfU1036GV6A4nQ1hJ9OAYaTUUqZXCXvZFGUrvFyZAghBx9NMfZn5ZYFr8UWEG1au5NZpnTehBmpbFGOAzPYl7UEqDJd5PTqjU1LKPcqv-4GdNzKlhP6zy8WrdSN4dpIUHv1RA_SwBk-DX0x1HN9lFTuM0xpu8v8SIRO-fxhPxxyCq158BqgCzjp32AMYk6cHCbEpS6EU6qczeunBG2ZvNzL5B5b_fOc3a5iZ4MGW9B-7enXbeZCwnKugCCxS-bep7d7bUbVIn_ceOZNKZhEz06VXInEJMJ2qbSRHR8pcouG7UusK0Ks-HCo3k-BENODQuszwc-elKlrDZOlP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: من نمی‌خواهم مذاکرات دیروز را به‌عنوان یک پیشرفت بزرگ توصیف کنم، اما در عین حال فکر می‌کنم مهم بود که دست‌کم یک گفت‌وگو صورت گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23919" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f1d757e.mp4?token=jSG57wPXftkWzkuvNreZUk42J7IOvLwYiIASNm9pmN6rE4GxTxOES0Bp0Z-YXFuWKJ5z4tS7aKHF556H8DFY4F4NWqizHlmK7OjxLAX1n0Yo2cAXx9KkoW9G59IOsc6hgEx2kIB7zUd0g-_g9HEOKFPQ93GhO8jmokKF1Q8VdfvnPlK6dgtCEPPalaRLmGGea9renwmHqFF7c-Cq0dw5sA9gsUbe2Cqu44GmalGU8uEBIFG0BL1HQO9bx5wDj2H9xoZ8SeoYowN-U1GObIiPBC3xmTpVEEj1Iz_OJHlZV9F-1-QBgS5N1yBVqdDMvmFtYmC5huW0sZKvTcwNKk3_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f1d757e.mp4?token=jSG57wPXftkWzkuvNreZUk42J7IOvLwYiIASNm9pmN6rE4GxTxOES0Bp0Z-YXFuWKJ5z4tS7aKHF556H8DFY4F4NWqizHlmK7OjxLAX1n0Yo2cAXx9KkoW9G59IOsc6hgEx2kIB7zUd0g-_g9HEOKFPQ93GhO8jmokKF1Q8VdfvnPlK6dgtCEPPalaRLmGGea9renwmHqFF7c-Cq0dw5sA9gsUbe2Cqu44GmalGU8uEBIFG0BL1HQO9bx5wDj2H9xoZ8SeoYowN-U1GObIiPBC3xmTpVEEj1Iz_OJHlZV9F-1-QBgS5N1yBVqdDMvmFtYmC5huW0sZKvTcwNKk3_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنگام سخنرانی مسعود پزشکیان در مجمع عمومی سازمان ملل، نمایندگان آمریکا، بریتانیا، آلمان، فرانسه، اسرائیل، سوریه، لبنان، عربستان سعودی، مصر، امارات متحده عربی، الجزایر، لهستان، سوئد، دانمارک، کانادا، ژاپن، جمهوری آذربایجان، مالزی، نیوزیلند، استرالیا، کنگو، اکوادور، قبرس، ایسلند، مکزیک، کویت، بحرین، اردن و آرژانتین سالن را ترک کردند.
در مجموع ۳۰ کشور.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23918" target="_blank">📅 19:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امروز بانک مرکزی امارات متحده عربی درپی تحریم آمریکا بانک ملی ایران را از فعالیت در این کشور منع کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23917" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تایمز اسرائیل :
مارکو روبیو، وزیر خارجه آمریکا
گفت امشب جلسه دیگری با ایرانی‌ها برگزار خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23916" target="_blank">📅 18:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abc111212.mp4?token=hH17Fa2RegHqru9pwqZDtU3y_2i5jU2SbH_gdhdD_hPM0x4wsFknztk4Dc-OKFTap4y_OIICpwTT9cXsuW-u2DoDHbOCgv868yhrPeUd0f7QjiQ8ynhRygqkh-WLTxVa3d9pTX4qH-SZ2FvFD30UJGGTQ6jiJr3UGasPoFxglwYxL85LUG4NVbiddKpbFkMzlmjLW2JGIxoqOT8MChXvw12o9f-WuEMuhAOInpZa_inCh6A9dklmmL4jv2O3XryndRcCfr-qNSlOQEbObIBIioj7kio5Qnvg1AxJSbjKjsYRDsIYFkRM0lJ9dSAWNE8J9vS1OPohv_o0ctNjWzR_mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abc111212.mp4?token=hH17Fa2RegHqru9pwqZDtU3y_2i5jU2SbH_gdhdD_hPM0x4wsFknztk4Dc-OKFTap4y_OIICpwTT9cXsuW-u2DoDHbOCgv868yhrPeUd0f7QjiQ8ynhRygqkh-WLTxVa3d9pTX4qH-SZ2FvFD30UJGGTQ6jiJr3UGasPoFxglwYxL85LUG4NVbiddKpbFkMzlmjLW2JGIxoqOT8MChXvw12o9f-WuEMuhAOInpZa_inCh6A9dklmmL4jv2O3XryndRcCfr-qNSlOQEbObIBIioj7kio5Qnvg1AxJSbjKjsYRDsIYFkRM0lJ9dSAWNE8J9vS1OPohv_o0ctNjWzR_mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه اراجیف پزشکیان در سازمان ملل: پزشکیان با اشاره به جنگ ایران و آمریکا و اسرائیل، حملات به ایران را محکوم کرد و گفت ایران قربانی تروریسم و تجاوز شده است؛ او در اقدامی قابل‌توجه تصویر علی خامنه‌ای را در مجمع عمومی بالا برد و گفت رهبر ایران بدون دلیل ترور…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23915" target="_blank">📅 18:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766b749308.mp4?token=NLKwxgIdEdWS3NsDIeVPBulTISPs-u2-L_AQBLUh54z1NlGdLZlR1TGhByAbSyxnzABkq48ufr5_FeLHBlqpHw7NAesZ4_O8saRR4B8upqj4YJbAEbQDxwG9D8Tf1sZX-E49vPyCiETB9mnqvCO2SFPXNuMphH5wb8xc_bXnVPqTXm87XJ4x0UiVLNh59HiiWWfTK8E6VYI2_CNPYUjM6wJSvUsrMWNam9gYMZET3InM4OjGNqmKLhaBc4haw81VBbbA8TY-lyhK1es8K3rFbVumVq1_KHSzmGR7NQZ8iMvWtYm9yVsKVQEdjRVSycxHhtpIRzecEuJQuvf5ylGIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766b749308.mp4?token=NLKwxgIdEdWS3NsDIeVPBulTISPs-u2-L_AQBLUh54z1NlGdLZlR1TGhByAbSyxnzABkq48ufr5_FeLHBlqpHw7NAesZ4_O8saRR4B8upqj4YJbAEbQDxwG9D8Tf1sZX-E49vPyCiETB9mnqvCO2SFPXNuMphH5wb8xc_bXnVPqTXm87XJ4x0UiVLNh59HiiWWfTK8E6VYI2_CNPYUjM6wJSvUsrMWNam9gYMZET3InM4OjGNqmKLhaBc4haw81VBbbA8TY-lyhK1es8K3rFbVumVq1_KHSzmGR7NQZ8iMvWtYm9yVsKVQEdjRVSycxHhtpIRzecEuJQuvf5ylGIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه اراجیف
پزشکیان
در سازمان ملل:
پزشکیان با اشاره به جنگ ایران و آمریکا و اسرائیل، حملات به ایران را محکوم کرد و گفت
ایران قربانی تروریسم و تجاوز شده است
؛ او در اقدامی قابل‌توجه
تصویر علی خامنه‌ای
را در مجمع عمومی بالا برد و گفت رهبر ایران بدون دلیل ترور شده است. پزشکیان همچنین تصاویر
کودکان و دانش‌آموزان کشته‌شده در حمله به مدرسه میناب
را نشان داد و حمله به غیرنظامیان و کودکان غزه را محکوم کرد  و گفت صلح پایدار در غرب آسیا بدون عدالت برای فلسطین غیرممکن است. او درباره برنامه هسته‌ای گفت
ایران به دنبال ساخت سلاح هسته‌ای نیست
و انرژی هسته‌ای صلح‌آمیز را حق ایران دانست، اما هم‌زمان به وجود زرادخانه هسته‌ای اسرائیل اعتراض کرد. او آمریکا و اسرائیل را عامل حملات و تشدید بحران منطقه معرفی کرد، از عملکرد سازمان ملل و شورای امنیت انتقاد کرد و گفت ایران در برابر تهدید و فشار تسلیم نخواهد شد. او همچنین قدرت نظامی ایران را
دفاعی
توصیف کرد و درباره تنگه هرمز بر مواضع ایران تأکید کرد. در عین حال، گفت
ایران راه مذاکره و دیپلماسی را کاملاً نبسته است
و در صورت احترام به حاکمیت و حقوق ایران، امکان رسیدن به راه‌حل سیاسی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23914" target="_blank">📅 18:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23913" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23912" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23911" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba6328511d.mp4?token=PpzBYp6i5TpaBcqEMC3CYeKc32AOTumm65-7vnoQf97t7xem2ryJPCu6rcTtIKJW_5kemvOQh4qbniylX6R5QeJHgKq3-9mJdpGdyZqNtaIEin7fDtlJagp2g6lUtHCiHOtrh3Tk4wJbiVVbkCpGQrG5Et7D2FD_sbnX145LLVjWgBjIlCmt7LdbKd_rCL97YudxxOnaFcz1_60PxP_pcxIyWzCK2EsSo_508VwqUK84FMPU3YZ1C2MW8LBefeGRteoHw9EmrShVRS7sfM3C6SQ_m2RDqpDfNk5nCi8tuiLSSFiBWyAnVd8BofB_pgBieWeCG0OdQfU_BEE1lOWhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba6328511d.mp4?token=PpzBYp6i5TpaBcqEMC3CYeKc32AOTumm65-7vnoQf97t7xem2ryJPCu6rcTtIKJW_5kemvOQh4qbniylX6R5QeJHgKq3-9mJdpGdyZqNtaIEin7fDtlJagp2g6lUtHCiHOtrh3Tk4wJbiVVbkCpGQrG5Et7D2FD_sbnX145LLVjWgBjIlCmt7LdbKd_rCL97YudxxOnaFcz1_60PxP_pcxIyWzCK2EsSo_508VwqUK84FMPU3YZ1C2MW8LBefeGRteoHw9EmrShVRS7sfM3C6SQ_m2RDqpDfNk5nCi8tuiLSSFiBWyAnVd8BofB_pgBieWeCG0OdQfU_BEE1lOWhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده آمریکا در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخن می‌گفت، مجمع را ترک کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23910" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکت دار قرمز میشه
⚠️
@WarRoom
🔻</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23908" target="_blank">📅 17:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P58QeEk87MHMFf-PXy1ficp8my_40XIloOhHYgCh_grNwQ3ZYkVCS_nlrlnlNbYkU8c5Qu7KA4JnnStusJfg1LiaiPRt7TbI6dERJ0MFIoX3NmaB-kMs175uhzl7QhKtMlogsfYCe-OxFML367_3oN7twZTKlvld3WMP3dxr7_eu5NI78Kz5RFYi1GCuBJiYeCyokWPKx5ZvVbra6PNcAuc-_eUCx2URiWtEvgpXBb9Mbow5kNFGtaKgrodefjVtNHXtS1ovo3O8UtHlJN21KsElpaaLUICx3khVi8Bcfl5fFLs9m-P05HVO9hNdMBti_6LoNybF8LXt0RcTolEH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا: یک کشتی باری در تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت که منجر به زخمی شدن دو نفر در کشتی شد. خدمه تخلیه شده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23907" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پزشکیان چرک هم اکنون وارد سازمان ملل شد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23906" target="_blank">📅 17:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">غوغای دانیال ایوازی از بازماندگان سرکوب اعتراضات ایران دیروز ۳۱ شهریور ۱۴۰۵ در مجمع عمومی سازمان ملل در نیویورک، وی در اعتراضات ایران هنگام تلاش برای کمک به یک معترض، هدف گلوله نیروهای جمهوری اسلامی قرار گرفته و زخمی شده بود. سخنان کوبنده  او علیه جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23905" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274a2e46ed.mp4?token=q9TNIzbxfPk9D0laKuDTDaCbmxt12FnkafPEdPQeLT1ymKver_CH87pu9ZrF-2DU6BvJm9qCkLx0i-1MbDyz-dvUpcOsCMZY4U638v7TyvY4sfNfrwNGa51nTj9L0j-NKPDRTqsUMf9aNstPaylHP9x-GqZp4SBbxOzxswTWw6osuD88mAudaKLQ3M9L_xGTBidUdZVsx5Zt5Fw0D-JVp_zYky-xSsJNqSO9kKIc7C5F1hYNhm4MGVI-WTyV5GMvPuufsFwXJ_XTd43At1YSIcCjuj_FpQAGQBnN2WNABKst48p0x-H146OhbuN_CpQfPOFWRXXvKFGvwSNbf-jPMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274a2e46ed.mp4?token=q9TNIzbxfPk9D0laKuDTDaCbmxt12FnkafPEdPQeLT1ymKver_CH87pu9ZrF-2DU6BvJm9qCkLx0i-1MbDyz-dvUpcOsCMZY4U638v7TyvY4sfNfrwNGa51nTj9L0j-NKPDRTqsUMf9aNstPaylHP9x-GqZp4SBbxOzxswTWw6osuD88mAudaKLQ3M9L_xGTBidUdZVsx5Zt5Fw0D-JVp_zYky-xSsJNqSO9kKIc7C5F1hYNhm4MGVI-WTyV5GMvPuufsFwXJ_XTd43At1YSIcCjuj_FpQAGQBnN2WNABKst48p0x-H146OhbuN_CpQfPOFWRXXvKFGvwSNbf-jPMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری شدید نیروهای مزدور رژیم با گروهای مسلح در سراوان همین الان !
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23904" target="_blank">📅 16:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPkngCWqrQ-fvYC2JgUPJgL0VyaDzeFgDpZzpybpVbH52SpvzuxPnkpmFFDTY-4j0RnrR5vs854Lq0gbaK_a-WMugugoEl22oYHmxmk5svXWjZgv59XNU2pnbkfnLPta91Q5eQ2xZWNeEvGtJ0mhEkH4K8jeVJL15qyUBV5LP5_NhgdbRXhO4LOV-MO7_2jVUV0Jkqu-XrUygIyPIjaSvzOoeaTaN90-vZXSBZmLeZ8o44n9GuaU2NBmbvwp961oz5E2oZg83fDb6x3TMV7ZyOvkv9Bsgs9aq6DYDUNBY9RnxDwYiqqU0UKxmxpp3FV57MeM5wEO7ddgtFygBn0xMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج نفتکش غول‌پیکر (VLCC) حامل نفت خام، بامداد دیروز در حالی مشاهده شدند که مسیر شرقی خود را از تنگه هرمز به پایان می‌رساندند. این نفتکش‌ها در مختصات ۲۵.۹۵۸۰، ۵۶.۵۵۸۱ ثبت شده‌اند. این مسیر راحت و بدون خطر نبوده و کشتی‌ها در شرایطی خطرناک و زیر آتش از تنگه عبور کرده‌اند. همچنین آثار باریک و کشیده‌ای از سوخت در دریا اطراف یکی از کشتی‌هایی که مورد اصابت ایران قرار گرفته، مشاهده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23903" target="_blank">📅 16:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری فارس:عراقچی اجازه دیدار با ویتکاف را نداشت و باید عذرخواهی کند.
گویا چپقچی مجوز شعام رو نداشته ، حالا هی سپاه موشک میزنه نفت بره بالا  این میره مذاکرات قیمت رو میاره پایین
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23902" target="_blank">📅 16:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDOnA0CXvjyFslv7CnWe5CByZBVNi1vQHsmmMDeBz8HNP4AqqGZLaPlmagDiBadyWjYt5cBE_SmB0p_TExc5yH4HnEOQUJ2cej-T1N6QEs7Usf2ZulCbVXkoQOb-psLd6id-c4lefBMbv2w1oQ5sGrbj34Li6ymwwlJ3z5kmQS5t-B_KYrLuBlTgHOA-mo0LOYRzREQvdZA1oOS4iPlsk4fFpOBX08ZBKErb3_LKJiaMVZqF_4Yiy5ln92-DGGB1QAsgrycthfKJy76GTJuXpXj9QCQXYALv45wVVE2CV-2S4e2IR2sVJvldraehVV-n9vtTvoIBhxNMk3YwZsxHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا:
یک کشتی باری در تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت که منجر به زخمی شدن دو نفر در کشتی شد. خدمه تخلیه شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23901" target="_blank">📅 15:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پنتاگون، پایگاه داده مربوط به سربازان کشته شده خود را به‌روزرسانی کرد ، این لیست نشان میدهد که یک سرباز زن آمریکایی در عربستان سعودی بر اثر "یک حادثه پزشکی" جان خود را از دست داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23900" target="_blank">📅 15:16 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

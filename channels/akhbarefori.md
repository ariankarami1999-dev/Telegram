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
<img src="https://cdn4.telesco.pe/file/CYmjr-x9uLu12tVcN89f4EPKRSCW-iJ0vcLSZoz6WpS4YEE4r-P40kipEEVDx5Zjel7R83iyHKQ6g_zhbpQPN9SdHGSYhxAiS-N45iCfY3bK_6AdPYRGVodCQPJmtx04sUTGNTyYfRxx6IlIz7UHd-VHiyULVgbQjApRS5zHM4PgTUg4HQBTlV41MOqWAU5vrOBGL9dh43s6aGTAGDgmXyevds8eEjcDi0GcIFKmLS5zWCETgwvOpNIXMEp_LBNdOl8xs0Xgz39GOYm2d-FG0YyB7wH4Ys1CcM-UJJ67rHjxyJL6rkO1ET5DMr2Wk1-qT3SNXua3lj-IP1cSU5m9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-655764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای کویت: ۶۳ نفر در اثر حمله ایران به کویت مجروح شده‌اند
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/akhbarefori/655764" target="_blank">📅 15:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
صدور روادید بازیکنان، کادر فنی و اجرایی تیم ملی فوتبال ایران
سفیر ایران در ترکیه:
🔹
بر اساس پیگیری‌ و هماهنگی به‌عمل آمده میان سفارت جمهوری اسلامی ایران در آنکارا و سفارت مکزیک، امروز روادید بازیکنان تیم ملی فوتبال جمهوری اسلامی ایران، کادر فنی و اجرایی برای حضور در رقابت‌های جام جهانی ۲۰۲۶ صادر و تحویل شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/akhbarefori/655762" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1018e153e.mp4?token=FZzPV_JI8sjxYUjSbksF1dl9fR9qhQeGZITXNTFij-OwxSWeWttl_0u391aEOLPO-GOz195xQce4YTu_3NysnvZsYXGl-MqRcuO3XlDrP1_adS8N5Gep6OGhUs5ySkRPhXHt_q6jngryh5ajUFBNhwRWUxKwR8_4jwP5mXygUXvHzjsNuGEvkRPT9kVEVuw8JALz8OQim_YbxEn8W7XQj2WeEJkQ74FyGggX2vrsVblHI4tNW35Cd76UrKjZgS_Rjs-UMl7pTVmQaJhiYsYki0N-sz_ulT-1ttrzM_4Q63yrmW5t3nZpasWCQMKBqNGYEbVbTPJFg82HJEmOTP_LUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1018e153e.mp4?token=FZzPV_JI8sjxYUjSbksF1dl9fR9qhQeGZITXNTFij-OwxSWeWttl_0u391aEOLPO-GOz195xQce4YTu_3NysnvZsYXGl-MqRcuO3XlDrP1_adS8N5Gep6OGhUs5ySkRPhXHt_q6jngryh5ajUFBNhwRWUxKwR8_4jwP5mXygUXvHzjsNuGEvkRPT9kVEVuw8JALz8OQim_YbxEn8W7XQj2WeEJkQ74FyGggX2vrsVblHI4tNW35Cd76UrKjZgS_Rjs-UMl7pTVmQaJhiYsYki0N-sz_ulT-1ttrzM_4Q63yrmW5t3nZpasWCQMKBqNGYEbVbTPJFg82HJEmOTP_LUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات دوخواهر از خانه ای در محله حاجی‌آباد
🔹
۲خواهر ۷ و ۱۵ ساله در سنندج پس از تحمل شرایطی دردناک، با دستور قضایی و ورود اورژانس اجتماعی از خانه‌ای در محله حاجی‌آباد نجات یافتند.
🔹
بر اساس گزارش‌ها، این کودکان توسط پدر و نامادری خود در سرویس بهداشتی منزل محبوس شده بودند و هنگام نجات در وضعیت جسمی و روحی نامناسبی قرار داشتند.
🔹
تحقیقات قضایی درباره ابعاد این پرونده ادامه دارد.
#اخبارفوری_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/akhbarefori/655761" target="_blank">📅 15:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f95f4785.mp4?token=vY-LqPRWgZa17VePuH9bDRYgAVgzUmQ66cN5Zs1DCAHnYJWoMWa66hKMbFos7xUUnZhHm08oemM3OUK2q6lx_ZYxTcBi1yEUHSeD59amb5Jb17zs9jNekFVSOrmCLzS0PhzxPqarXQjtVgg-fgJTw5uzONgFerEwRGAmr-mM7S3hK0h6Bl0mpwposi1ul3KwcYHBJG8nqyJIv2y7uUfp3YZd95jt5QGGhCQ7Owz4Wl1ZH7jcBbpHEE3-bNn8F3-ti6g6YlmXr0AKr2j7AYTIAzHig5YcBYYzUnrT7mXxpXS4mAcB_ntbKFsiaP8FsQgfq4iPnViWzK16oun3idhydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f95f4785.mp4?token=vY-LqPRWgZa17VePuH9bDRYgAVgzUmQ66cN5Zs1DCAHnYJWoMWa66hKMbFos7xUUnZhHm08oemM3OUK2q6lx_ZYxTcBi1yEUHSeD59amb5Jb17zs9jNekFVSOrmCLzS0PhzxPqarXQjtVgg-fgJTw5uzONgFerEwRGAmr-mM7S3hK0h6Bl0mpwposi1ul3KwcYHBJG8nqyJIv2y7uUfp3YZd95jt5QGGhCQ7Owz4Wl1ZH7jcBbpHEE3-bNn8F3-ti6g6YlmXr0AKr2j7AYTIAzHig5YcBYYzUnrT7mXxpXS4mAcB_ntbKFsiaP8FsQgfq4iPnViWzK16oun3idhydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران در حرم مطهر رضوی در آستانه عید غدیر
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/655760" target="_blank">📅 15:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ششمین سال خشکسالی در فلات مرکزی؛ کاهش ۳۹ درصدی بارش در تهران
رئیس مرکز مدیریت بحران خشکسالی سازمان هواشناسی:
🔹
استان‌های فلات مرکزی تا محدوده گیلان از جمله اصفهان، قم، مرکزی، تهران، قزوین، سمنان و گیلان در سال آبی جاری با بارش کمتر از حد نرمال مواجه شده‌اند.
🔹
در این میان تهران با ۳۹ درصد کاهش بارندگی بیشترین کم‌بارشی را ثبت کرده و پس از آن استان‌های مرکزی و قزوین با حدود ۳۰ درصد کاهش قرار دارند.
🔹
میزان کاهش بارش در گیلان نیز حدود ۲۵ درصد اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/655759" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b44dad95ff.mp4?token=XU-kN1HG1RtgvGqJldc_kuf4L7ZdQuIdMGrTrvqw09ovVE6Bt0NKQU6SaIH0MBJoO9JiKj-1FvE1VgxnothQu0JksKpXU3lb0o8d0kImSSDsQVJPdJJNOwvwejHEprB235tn-l5Lga5atm4zaR_0bY8PewR92RgH3KGhZ32GqYww-kEEHKSC5u1pPde-mcBz1B-956k-13H4takONqmvKrXQKSCXT4VSh5-o4z993vk7CQwsWIMIb8yYqPaDgWRtJAPqQpzEbJBhxu1IzvdpsBeXttSansrVXwUKA_Tp4Eg7whubrfyh94Zw-gsnr-Dbj3hDa6PjklTYsAv8wGHvby2rESLZsXGrK-MC5AuvUvpvvfR51CwI705ytkG-dehrCIZAUnY1kjGSrZ2MOQrxfPm_ycMZ9pnMulEKG4rqErdnbyTF0DLw1xpNRGq_AF5OkadaUqDRWsV9bEznQCGGPRaAMJ-6oAPAq5ODYSw3vvOAAZyeiXDA6qVeBHtH4ygPR7_aK3k2WHhiCRxmXU4NyzwvLlvJxXcXGtwdums28Km3jQHXvA9URtAIiLhcxuW746Zj4aQOA50r9cW8WLPEavTA1Vxr1qPGRjqjhRFL7kg7BQcT3Mx1k6B3IPB7FAgZIRjvRksfhxMT1SabgYWRIxh_hzYkV4ew4Xmd5H53SPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b44dad95ff.mp4?token=XU-kN1HG1RtgvGqJldc_kuf4L7ZdQuIdMGrTrvqw09ovVE6Bt0NKQU6SaIH0MBJoO9JiKj-1FvE1VgxnothQu0JksKpXU3lb0o8d0kImSSDsQVJPdJJNOwvwejHEprB235tn-l5Lga5atm4zaR_0bY8PewR92RgH3KGhZ32GqYww-kEEHKSC5u1pPde-mcBz1B-956k-13H4takONqmvKrXQKSCXT4VSh5-o4z993vk7CQwsWIMIb8yYqPaDgWRtJAPqQpzEbJBhxu1IzvdpsBeXttSansrVXwUKA_Tp4Eg7whubrfyh94Zw-gsnr-Dbj3hDa6PjklTYsAv8wGHvby2rESLZsXGrK-MC5AuvUvpvvfR51CwI705ytkG-dehrCIZAUnY1kjGSrZ2MOQrxfPm_ycMZ9pnMulEKG4rqErdnbyTF0DLw1xpNRGq_AF5OkadaUqDRWsV9bEznQCGGPRaAMJ-6oAPAq5ODYSw3vvOAAZyeiXDA6qVeBHtH4ygPR7_aK3k2WHhiCRxmXU4NyzwvLlvJxXcXGtwdums28Km3jQHXvA9URtAIiLhcxuW746Zj4aQOA50r9cW8WLPEavTA1Vxr1qPGRjqjhRFL7kg7BQcT3Mx1k6B3IPB7FAgZIRjvRksfhxMT1SabgYWRIxh_hzYkV4ew4Xmd5H53SPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه افق: فردوسی‌پور و قیاسی چطور می‌توانند از تیم ملی فوتبال ایران صحبت کنند وقتی از کودکان ایرانی پرپرشده توسط آمریکا و اسرائیل حرفی نزدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/655758" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76da5eaac.mp4?token=pGmFScU0c6a53_p7gYnBr50k1a6EgDxRqEvy2spJJYPEQdPl7r-__Qe7pAF-PegWwEqAZQFByJUR8hdRT40Er_aaQVSoc8hX6oZErjkzXoOG9Z9rNaKWKfrqY747adoIYhVPJfvMumzzetfkG6T-PdkIvERt6aW4LzvcsvOXBqjJLyps1xr0tZ0ZN9Hti-IGXBRzDzr9pERlOP4v2SDCC5rBshZwcU_Va01ACTbieloHUdixm2XnMqJvgdQf_BLpytSF2zEwq9HvrItSaoOvXVNxWkW_nvyS6c_vPhytWWb-9WWc7qZ5UkV3EG59Bl_AJgjdpSucu5PWWR_fcgJL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76da5eaac.mp4?token=pGmFScU0c6a53_p7gYnBr50k1a6EgDxRqEvy2spJJYPEQdPl7r-__Qe7pAF-PegWwEqAZQFByJUR8hdRT40Er_aaQVSoc8hX6oZErjkzXoOG9Z9rNaKWKfrqY747adoIYhVPJfvMumzzetfkG6T-PdkIvERt6aW4LzvcsvOXBqjJLyps1xr0tZ0ZN9Hti-IGXBRzDzr9pERlOP4v2SDCC5rBshZwcU_Va01ACTbieloHUdixm2XnMqJvgdQf_BLpytSF2zEwq9HvrItSaoOvXVNxWkW_nvyS6c_vPhytWWb-9WWc7qZ5UkV3EG59Bl_AJgjdpSucu5PWWR_fcgJL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت مردی در اربیل به‌دلیل ایجاد صدای شبیه پهپاد «شاهد»
🔹
پلیس اربیل در شمال عراق فردی را بازداشت کرد که با استفاده از یک بوق، صدایی شبیه به پهپادهای شاهد ایجاد می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/655757" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
زمان شروع قطعی برق خانه‌ها مشخص شد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران:
🔹
پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که در این مدت همراهی و همدلی همگانی ضروری است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/655756" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=aGphsp0W_t8gpPh4M27G-aLpbaOWYYkfjidOq93ihIu7FAAIrNdWi-xnfpw6OcG7vt_bmnVnDG4AboMLyHVQrhlSMBiw7cpoGH7c5CCe4CmVeFGlVuMiFSa-NVXTMHjSQ-HZmcHYplSJR-1vKsDY9d8kHzMMKPhf0z36iXMjM8HpSH0lrCTcFKPk8T6UTqeMf5wIxJXccXW4MmIjuxxQZj98KaMbKfwKZIrG68EJb8US2UQBe3cTaIkJsPhRTScYgiyXjRS4C45kNnB1efocij8ec9DHKs3UvdX8dDNzeGSz7HGivIn_nEXHqL_e-R-A_2YJLx13RZdpUIAGqzHg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=aGphsp0W_t8gpPh4M27G-aLpbaOWYYkfjidOq93ihIu7FAAIrNdWi-xnfpw6OcG7vt_bmnVnDG4AboMLyHVQrhlSMBiw7cpoGH7c5CCe4CmVeFGlVuMiFSa-NVXTMHjSQ-HZmcHYplSJR-1vKsDY9d8kHzMMKPhf0z36iXMjM8HpSH0lrCTcFKPk8T6UTqeMf5wIxJXccXW4MmIjuxxQZj98KaMbKfwKZIrG68EJb8US2UQBe3cTaIkJsPhRTScYgiyXjRS4C45kNnB1efocij8ec9DHKs3UvdX8dDNzeGSz7HGivIn_nEXHqL_e-R-A_2YJLx13RZdpUIAGqzHg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب امام خمینی(ره) به تمجید آیت‌الله مشکینی از ایشان
🔹
ما آن قدری که گرفتار به نفس خودمان هستیم کافی است، دیگر مسائلی نفرمایید که انباشته بشود در نفوس ما و ما را به عقب برگرداند. شما دعا کنید که آدم بشویم. دعا کنید به ظواهر اسلام حداقل عمل کنیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/655755" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956d48d0ad.mp4?token=QirUFzvENooH4oIRfYn-6XAdkPKiAf3wORDgozMoNHQ8wp4LP7bkgKJh0__89RAHR0y5hJWwZXSEBmSunMSgPziD64BXEp8oecCd7QHwqQQA_ovctrtqVqxwUuMWEmOm74iMz3v4LO6tvJlpqidPOlseeCM_GdJS9PX2gu-ZqXQNyDo5nBzNmIl8VKF1hxhTWEWvOZEdmSjD0xbj8TpcZIHA2KTm9JATc4QxU3TEdlaEocTO0EL3mHxRlhiQM5XTWlzJ9dwP0p6MAw7baEWkMgtNjpyV4ZkEZzK3j6MEFe5BtyVtp2i0ujxP4NZctdbycZ1ep8aUzP-fhwj6dN0Sxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956d48d0ad.mp4?token=QirUFzvENooH4oIRfYn-6XAdkPKiAf3wORDgozMoNHQ8wp4LP7bkgKJh0__89RAHR0y5hJWwZXSEBmSunMSgPziD64BXEp8oecCd7QHwqQQA_ovctrtqVqxwUuMWEmOm74iMz3v4LO6tvJlpqidPOlseeCM_GdJS9PX2gu-ZqXQNyDo5nBzNmIl8VKF1hxhTWEWvOZEdmSjD0xbj8TpcZIHA2KTm9JATc4QxU3TEdlaEocTO0EL3mHxRlhiQM5XTWlzJ9dwP0p6MAw7baEWkMgtNjpyV4ZkEZzK3j6MEFe5BtyVtp2i0ujxP4NZctdbycZ1ep8aUzP-fhwj6dN0Sxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق زده شدن داوران برنامه محفل از قرآن خوندن بامزه دختر بچه شیرین زبون
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/655754" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
دقایقی پیش بارش فوق شدید و استوایی باران در شهرستان سلماس
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655752" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c63ec2e8.mp4?token=Wu6WEIxgSSvKVOBqqD9Pl3SYZHHVHp0VuqtSVwpAPjW5ywsRouAVon_Gmxu5VPPMX55pCi8kDlTn0mhzei18ze_IEXXgIFGP4MN8K_7Q2wUgYSjrui8Mth16h8FLvhvexfxHXQ03moasyuOgKAJSeNGDg1dSQew5qHcelJZU8CcAihOVXE8sSvwx2hkj1EWjlyV2R3y51gKZYSFKAYmXh7P3B3GjByuk0s6qIExe_jcfuPeTmy5QB2A9tbf6tAvwTrB7TBWt_M9ZD6zRt4WdL5Sj0hNqmnjkZjUKrF8up-TQH2895As_DbI0kHhs7RonZ5Isx6OHZiE5OTk9k59k6TKUQrbfcdTNrRLjwE0Mjg2NA4sl-AV0XK5Oes9AeseffwEqqj5UUfyxbybDZkGDzqDwb-0gaO1VHRDGSI7wIV5K4Gd6glAZxME_DsnXh6dxfEK8yGfAUcrpGdOIV3Gwb16Gz-gpzgLhoOnLZ4cCwr2Lt0niq-UT40Pa23HhHDC2ERBlOaY0-4w5ryMn5bzD-M-wgnl4Q5IQZXPdR-52S-awoS-PYyorWmVX0IZGQibWaAvIfBPQJtl6kd9GNN7C2comfTVUDxZtKICyR2QEEwcMKuJMmbwHYmlwtyEWAroiEHtdXTjXGSqqhKTiLKur9CD7mSBSPI3j79nVbtpl6ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c63ec2e8.mp4?token=Wu6WEIxgSSvKVOBqqD9Pl3SYZHHVHp0VuqtSVwpAPjW5ywsRouAVon_Gmxu5VPPMX55pCi8kDlTn0mhzei18ze_IEXXgIFGP4MN8K_7Q2wUgYSjrui8Mth16h8FLvhvexfxHXQ03moasyuOgKAJSeNGDg1dSQew5qHcelJZU8CcAihOVXE8sSvwx2hkj1EWjlyV2R3y51gKZYSFKAYmXh7P3B3GjByuk0s6qIExe_jcfuPeTmy5QB2A9tbf6tAvwTrB7TBWt_M9ZD6zRt4WdL5Sj0hNqmnjkZjUKrF8up-TQH2895As_DbI0kHhs7RonZ5Isx6OHZiE5OTk9k59k6TKUQrbfcdTNrRLjwE0Mjg2NA4sl-AV0XK5Oes9AeseffwEqqj5UUfyxbybDZkGDzqDwb-0gaO1VHRDGSI7wIV5K4Gd6glAZxME_DsnXh6dxfEK8yGfAUcrpGdOIV3Gwb16Gz-gpzgLhoOnLZ4cCwr2Lt0niq-UT40Pa23HhHDC2ERBlOaY0-4w5ryMn5bzD-M-wgnl4Q5IQZXPdR-52S-awoS-PYyorWmVX0IZGQibWaAvIfBPQJtl6kd9GNN7C2comfTVUDxZtKICyR2QEEwcMKuJMmbwHYmlwtyEWAroiEHtdXTjXGSqqhKTiLKur9CD7mSBSPI3j79nVbtpl6ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت این پرچم هزاران عشق نهفته‌‌است
❤️
#ایران_من
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/655751" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جراحی زیبایی به قیمت جان؛ مرگ دختر جوان در پی عمل بینی
🔹
دختر جوانی که از یکی از شهرستان‌های غرب کشور برای انجام عمل زیبایی بینی به تهران آمده و در یکی از بیمارستان های خصوصی بستری شده بود، شب گذشته جانش را از دست داد.
🔹
اولیای این دختر جوان ۲۷ ساله از کادر درمان شکایت کردند.
🔹
به دستور  بازپرس شعبه پنجم دادسرای جنایی، این پرونده به دادسرای ویژه جرائم پزشکی ارسال شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/655750" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd0d23fac.mp4?token=YdmGZ9JVjCgP6IwX_d2FUGjHGujPSRwsjKfpQfwFIM9ixuzrrmBp3ApaUoumeIpJwzDu1VVfTlcKfdWNA6y04Q60IwJNgCJDSS15d6-O5ENeHzeVGDuC2_YytVXDQPnpfAfhOPAZZoWQtzPNYD737O6O0NMwnU5fi9QBkp5lOyfNEFk3fZV4KgMDxpd4JJuVhEecF2Uy8hb4ml4PSEV4SV_kDVHJiQAqNeAMTw6apuP-BoYrE0dqs-gIyj8qwTszYKgonINYJXlugfbXgSLZazttoWsiSN_Tgq5Q-lGO7xJAkWxTEpbEnJmGJfOejB8b8tyX3p67mnrgFW1p365RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd0d23fac.mp4?token=YdmGZ9JVjCgP6IwX_d2FUGjHGujPSRwsjKfpQfwFIM9ixuzrrmBp3ApaUoumeIpJwzDu1VVfTlcKfdWNA6y04Q60IwJNgCJDSS15d6-O5ENeHzeVGDuC2_YytVXDQPnpfAfhOPAZZoWQtzPNYD737O6O0NMwnU5fi9QBkp5lOyfNEFk3fZV4KgMDxpd4JJuVhEecF2Uy8hb4ml4PSEV4SV_kDVHJiQAqNeAMTw6apuP-BoYrE0dqs-gIyj8qwTszYKgonINYJXlugfbXgSLZazttoWsiSN_Tgq5Q-lGO7xJAkWxTEpbEnJmGJfOejB8b8tyX3p67mnrgFW1p365RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهد وارد باشگاه شکارچیان لانچر شد
🔹
برای نخستین بار، نیروهای روسی یک لانچر پهپاد انتحاری (FP) اوکراینی را که روی یک کامیون نصب شده بود، با استفاده از پهپاد شاهد-۱۳۶ هدف قرار داده و منهدم کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/655749" target="_blank">📅 14:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ویدئویی از کویتی‌هایی که هنگام رانندگی سعی دارند از فعالیت پدافند هوایی فیلمبرداری کنند و با ماشین تصادف می‌کنند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/655748" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b99f8f25c.mp4?token=h5l9q7-MPx7OBdv0W9CO6y3KybjxIJNUlBsxyOB5WtHEx4UhOyQCcMqVCIu_iAGMwX25C6vudCKx3B9Nk-8ivtAyQxFpIpPA64KLqJHHJN9bqRyQmoFDrbr1zzSqjrKOdEuM9TbDQAAB21NT72j_AkwGGf0-rttsiua2wRQ1df80rom3J5e-eDyfW_L_WrppMIyHEg7AOs_YRj5O_ultTq-bjTgiaSHwVq9I0zyM8WzgGvAUVTyzp6erxVaqxWVvnB-3sOs9RM0DF0a5noRmcmfXfIhnBrujdoqxQ6_WPT4puObFcLJyTMMETEE3jkDY5BGGh3u6zsqFFxqFoZ_Ikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b99f8f25c.mp4?token=h5l9q7-MPx7OBdv0W9CO6y3KybjxIJNUlBsxyOB5WtHEx4UhOyQCcMqVCIu_iAGMwX25C6vudCKx3B9Nk-8ivtAyQxFpIpPA64KLqJHHJN9bqRyQmoFDrbr1zzSqjrKOdEuM9TbDQAAB21NT72j_AkwGGf0-rttsiua2wRQ1df80rom3J5e-eDyfW_L_WrppMIyHEg7AOs_YRj5O_ultTq-bjTgiaSHwVq9I0zyM8WzgGvAUVTyzp6erxVaqxWVvnB-3sOs9RM0DF0a5noRmcmfXfIhnBrujdoqxQ6_WPT4puObFcLJyTMMETEE3jkDY5BGGh3u6zsqFFxqFoZ_Ikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: در حال حاضر نیازی به اعزام نیروی زمینی به ایران نداریم #Devil
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/655747" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سپاه: دشمن ناگزیر به پذیرش قواعد جدید ایران است
سپاه پاسداران در پیامی به مناسبت گرامیداشت سالروز رحلت امام خمینی (ره) و قیام ۱۵ خرداد:
🔹
حضور مردم در خیابان‌ها پشتیبان میدان رزم، سنگر دیپلماسی و عامل ضروری رقم خوردن پیروزی کامل و نهایی است.
🔹
ایرانیان هرگز تسلیم واژه‌سازی‌ها و دستاوردسازی‌های دروغین دشمن نخواهند شد.
🔹
دشمن ناگزیر به پذیرش قواعد جدیدی است که ملت ایران و نیروهای مسلح بر میدان تحمیل کرده‌اند؛ به ویژه در عرصه مدیریت و کنترل هوشمند تنگه هرمز.
🔹
مقاومت تا نابودی کامل توطئه‌های استکباری، اخراج بیگانگان از غرب آسیا و آزادی قدس شریف با نابودی رژیم صهیونیستی، مقتدرانه ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/655746" target="_blank">📅 14:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تسنیم: مذاکرات تا زمانی که شروط ایران درباره لبنان تامین شود در حالت تعلیق می‌ماند
منابع آگاه:
🔹
طی روزهای گذشته ایران هیچ پاسخی به آمریکایی‌ها درباره متن تفاهم نداده و به دلیل جنایات رژیم صهیونیستی در لبنان، عملاً تبادل متن از طریق واسطه‌ها را نیز تا زمانی که شروط ایران درباره لبنان تامین شود، تعلیق کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655745" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ: نتانیاهو را «دیوانه لعنتی» خطاب کردم  نیویورک پست:
🔹
دونالد ترامپ تأیید کرد که در تماس تلفنی روز دوشنبه، بنیامین نتانیاهو را «دیوانهٔ لعنتی» خطاب کرده است.
🔹
او گفت از ادامه درگیری‌های نتانیاهو با لبنان ناراضی بوده و از او خواسته آتش‌بس کند. با این…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/655744" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85b392914.mp4?token=L2HiFtFRqDXwo5h2Bp0I4Pc7hyowGYv4L0w3OnTqP0f9pbW0WEGebwfYanUOw1rxAFtIi_isfu44i4qM1uQwr_dcpan-ASIBwjmPryMFcq4fV6D2MShk5pqCAw4qpv8i-_ir1L0642w5ARDvWZHnD-HCoChpPIPocQvlPAopVKNoZvpFkwkb_6OL3nVU2IRGojT5h6yg9NuNyHOUVZ956ZNzp9Vq8oW8kTd-9HnWgn8_bVhx9l1tj9iGAxLIpEHnkGjjz5ivCDJbKpq4HpLZJMi7h4soa-QHGyJhVJqtab4tn1VAzIWYretqjz4WWXSHmlCLTvrEaPmloFNuomqPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85b392914.mp4?token=L2HiFtFRqDXwo5h2Bp0I4Pc7hyowGYv4L0w3OnTqP0f9pbW0WEGebwfYanUOw1rxAFtIi_isfu44i4qM1uQwr_dcpan-ASIBwjmPryMFcq4fV6D2MShk5pqCAw4qpv8i-_ir1L0642w5ARDvWZHnD-HCoChpPIPocQvlPAopVKNoZvpFkwkb_6OL3nVU2IRGojT5h6yg9NuNyHOUVZ956ZNzp9Vq8oW8kTd-9HnWgn8_bVhx9l1tj9iGAxLIpEHnkGjjz5ivCDJbKpq4HpLZJMi7h4soa-QHGyJhVJqtab4tn1VAzIWYretqjz4WWXSHmlCLTvrEaPmloFNuomqPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
هدف، هدف، ای مقصود من نجف
وطن کجاست، عقلا منطقا نجف...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/655743" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تیزر قسمت ششم از فصل چهارم
🔹
در این قسمت روایت اولین تجربه نزدیک به مرگ آقای محمدعلی درودی که به خاطر شرایط سخت زندگی با پدر جانبازش و غم از دست دادن برادرش از زندگی ناامید شده و از خداوند طلب مرگ می کند به همین دلیل تجربه‌ای از جدا شدن روح از جسم توسط موجودی وحشتناک و رفتن به عالم برزخ و درک عمیقی از الطاف الهی را مشاهده و با ما در میان می گذارند
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محمدعلی درودی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655742" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ به نتانیاهو گفت چه غلطی داری می‌کنی؟  خلاصه صحبت‌های ترامپ با نتانیاهو را این مقام آمریکایی چنین بیان کرد:
🔹
«تو دیوانه‌ای. اگر من نبودم، الان زندان بودی. دارم نجاتت می دهم. الان همه از تو متنفرند. به خاطر این قضیه، همه از اسرائیل متنفرند.»…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/655741" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای ترامپ: اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد
🔹
رهبر ایران در حال حاضر مشغول مذاکرات با ماست و ممکن است در مقطعی با او دیدار کنم.
🔹
ممکن است محاصره ایران تا روز کارگر برداشته شود. #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/655740" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNELvPfhAy3UVcPjEZje85YP8F-JreS0B-ZyD2kKPqFHYI_kFknji5lFcmdQ0ekzD5oKZJ_1cNMUdX559qVPVrJamQzo_ZoaMDM4myLhbsTelQkCE0ohPxA-_TVy1khylM4xODimLFUoqjB8GTLZFCqvnf-VsLNMQYybm0NtyvhzWYhBu12vaUHZYVcLJ1QFn8ZTsoYKXhZ6t2-KqRXqjJUSfmwnWl7r_U6Vf-DYYtdQ1nY8JHSpEygaKqLPk2sctx8CFqdncOqVFV3z-J5Sa4TYX5REA7U7gD2FODccxJwkDU9j3Skyse_w8RjA4zDMYd1JaEqcuNnHnCWk8Z1w-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست عجیب ترامپ: Trump 007
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655739" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc7ddeec0.mp4?token=ade_LB_6mDYeEv5W6OwjLfnH4xcRLZNqd91LCaIDN5WBT6g-mtst1hVpERqPxIKkkxKn29ARU1wq-_4oUwreYIdq0wVcIIsuRRqTgpFY2IsUgyyl56V45eQqBoptqdNn-deJAFCVOWLHJ2h0-ck18o8WPIn2sA5CUtk85mzSwV-y8ncXpxjlex_QamFH-xZJLx37FC8VzaCMaJQck_N3wPiZ0SpLyNJkw67P09uyE8CLY708f71tlsGKun865iFM5N2S63-juvPHEbcVO3fYmNE2k0o9aleVt53Sj2A4d52Dcox8FCsnsUwGUH4jVhrYx0XjgnqH7Y2DOHX9ripRwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc7ddeec0.mp4?token=ade_LB_6mDYeEv5W6OwjLfnH4xcRLZNqd91LCaIDN5WBT6g-mtst1hVpERqPxIKkkxKn29ARU1wq-_4oUwreYIdq0wVcIIsuRRqTgpFY2IsUgyyl56V45eQqBoptqdNn-deJAFCVOWLHJ2h0-ck18o8WPIn2sA5CUtk85mzSwV-y8ncXpxjlex_QamFH-xZJLx37FC8VzaCMaJQck_N3wPiZ0SpLyNJkw67P09uyE8CLY708f71tlsGKun865iFM5N2S63-juvPHEbcVO3fYmNE2k0o9aleVt53Sj2A4d52Dcox8FCsnsUwGUH4jVhrYx0XjgnqH7Y2DOHX9ripRwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/655738" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb634c64b.mp4?token=VxAp0n4Y-7QXN7iFNupRm2JYccwWJf7KOigKT8v6dZQdL_ZJcMiLsgKzq--eKndW2gcGF68G6KZK92fgia51KfnfwzTOx1WXdqc1w5XqVjPH88Fpdpj0cz_yg3GkSabLx12n89D7VRkOYnaTgDZKhsmxUk2ivP1sE0BI_BEeo76GC0Y81kDSdnozjwkvjH-F2S9Sk41Wmu1Vf1M-4JCffyWlcYPE9d9I8caP2r8frN26cXmfjl2u8zG6tsZwYcCTIO9ctFsFGppLndBJ7SfbzXOO1f11DAB2ziIZgDQ6y53BCapPXnzjpCz-CJRvjyFpQSeswiwvB5pcd0YLJ97ozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb634c64b.mp4?token=VxAp0n4Y-7QXN7iFNupRm2JYccwWJf7KOigKT8v6dZQdL_ZJcMiLsgKzq--eKndW2gcGF68G6KZK92fgia51KfnfwzTOx1WXdqc1w5XqVjPH88Fpdpj0cz_yg3GkSabLx12n89D7VRkOYnaTgDZKhsmxUk2ivP1sE0BI_BEeo76GC0Y81kDSdnozjwkvjH-F2S9Sk41Wmu1Vf1M-4JCffyWlcYPE9d9I8caP2r8frN26cXmfjl2u8zG6tsZwYcCTIO9ctFsFGppLndBJ7SfbzXOO1f11DAB2ziIZgDQ6y53BCapPXnzjpCz-CJRvjyFpQSeswiwvB5pcd0YLJ97ozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی مهیب در جنگل‌های اسپانیا
🔹
آتش سوزی بزرگ جنگلی در مورسیای اسپانیا، بیش از ۱۰۰ هکتار از جنگل های این منطقه را سوزانده و ساکنان را مجبور به تخلیه خانه های خود کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655737" target="_blank">📅 13:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عصائب اهل الحق عراق کمیته‌ای برای پایبندی به انحصار سلاح تشکیل داد
🔹
گروه عصائب اهل حق عراق از تشکیل یک کمیته مرکزی برای شروع اقدامات قطع ارتباط با حشد‌الشعبی و پایبندی به انحصار سلاح در دست دولت خبر داد.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/655736" target="_blank">📅 13:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای
ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655735" target="_blank">📅 13:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyS-xo259qA_ce6qpwhwt8GlujbMuqorp1UyM4bAPdXBXaPNNpqbhEqdOTLhlWXBLafkwePoCheFgPHNujtbmj6L7FHiqW9jXPqSMZ8Wh-ka4mUAg8R-SIJhkbEYsLFyCnmZSJpOplY4Lb3Qigx-tchZK8yRdG5pwAB2ysrRf9qEwTPkZnjNSq4GmPeF7b-ZGoLmhC9bnJ8x-JhmY5XmFuurpG-J7K21EMzNxImBsJknGC3505rcw7gejeZTxvX0QgsYyJCq006ZDEWDIHKttZ5FFtiZ0MdiJisllYa1Njk5gdF76KGVCH_A1Y9CC3NUvoYqqlFcNlw64YA_BaHHsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با رخت سبز به تعطیلات رفت
🔹
در جریان معاملات امروز شاخص کل بورس با افزایش ۱۴ هزار و ۳۷۴ واحد در سطح ۴ میلیون و ۳۵۸ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655734" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571a0fb2b2.mp4?token=Gw0b5Ix_8-Y2dkpigsQxI1ZSOBRqAnbyY4AzYoJ14oKtZvg3uYOm3hgIqdNYjr_iGSIMAC4qE8QwuO5YpdMg7RKgOzmInTx7lRv-l8wqWEFnmWeSI3Ng9KhXK0lfY8cyQT-Lj4Nfy83MCHhFdHJnJKbgvpajuaEP8w8n5Vu7JxO8q2a-ZxI7bYtetSdct-97xjj9SNgmaRit6H0gSy-SmFH5SZdEjlJznMwOtfdsx7UKjG7dFIHfUetfRH7z82NUUk1UViMSysOkIqJVmFkBZ7mfPLCY84j_oYIlBnJP9HsK_ikJ3cpVlLqHEt3mKeuh57BrAs1Y-NEzhCW1jOx5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571a0fb2b2.mp4?token=Gw0b5Ix_8-Y2dkpigsQxI1ZSOBRqAnbyY4AzYoJ14oKtZvg3uYOm3hgIqdNYjr_iGSIMAC4qE8QwuO5YpdMg7RKgOzmInTx7lRv-l8wqWEFnmWeSI3Ng9KhXK0lfY8cyQT-Lj4Nfy83MCHhFdHJnJKbgvpajuaEP8w8n5Vu7JxO8q2a-ZxI7bYtetSdct-97xjj9SNgmaRit6H0gSy-SmFH5SZdEjlJznMwOtfdsx7UKjG7dFIHfUetfRH7z82NUUk1UViMSysOkIqJVmFkBZ7mfPLCY84j_oYIlBnJP9HsK_ikJ3cpVlLqHEt3mKeuh57BrAs1Y-NEzhCW1jOx5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ شقایق نوروزی؛ فمینیست و فعال سیاسی ضدجنگ به ناامید شدن مجری ایران اینترنشنال از پهلوی و اپوزیسیون و آرزوی او برای حضور فردی شبیه جولانی در ایران: نگاه کن ببین ایران اصلا جولانی‌خیز هست یا نه؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/655733" target="_blank">📅 13:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سقوط بالگرد در جنوب غرب انگلیس
پلیس انگلیس:
🔹
یک بالگرد نیروی دریایی در مزرعه‌ای در جنوب غرب کشور سقوط کرده است.
🔹
جزئیات حادثه در دست بررسی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655732" target="_blank">📅 13:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd4306a5.mp4?token=HE-pdH0KoWWWzmPjFwduX8TOc_kNkOah1qpnQ-DATduRKVEiqOFNAauFOPsX6THSqKCmV3bstz0hbXlDGxILYf6WstbESq_xFxClU08k-6VcMYhAuvHdEJqMF7HyCyuPD-TtKQHV4rbfJgRF5Ak6pNI6hSkubp4DAgFyBnqKl-T2zYEbYg7pMYL3YOb3qRaNkwdMcjHqKf_ldk_d1E7kNPPu4rbrL_IOM7kmph_f3Pz1-seihB9yMopoBw5_EbhNCEnlw3zoa19LMh1w4AhCGQuwXfuAkxx7u7bHbeTLH0CWn86ShaTROQ2mycMzAX6GP5DjJTeYXFlNQ7cAVZGEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd4306a5.mp4?token=HE-pdH0KoWWWzmPjFwduX8TOc_kNkOah1qpnQ-DATduRKVEiqOFNAauFOPsX6THSqKCmV3bstz0hbXlDGxILYf6WstbESq_xFxClU08k-6VcMYhAuvHdEJqMF7HyCyuPD-TtKQHV4rbfJgRF5Ak6pNI6hSkubp4DAgFyBnqKl-T2zYEbYg7pMYL3YOb3qRaNkwdMcjHqKf_ldk_d1E7kNPPu4rbrL_IOM7kmph_f3Pz1-seihB9yMopoBw5_EbhNCEnlw3zoa19LMh1w4AhCGQuwXfuAkxx7u7bHbeTLH0CWn86ShaTROQ2mycMzAX6GP5DjJTeYXFlNQ7cAVZGEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدیده عجیب رعد و برق در کوهستان‌ مه‌آلود |گواتمالا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655731" target="_blank">📅 13:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حنظله: اطلاعات افسران و پایگاه‌های محرمانه آمریکا در اختیار ماست
🔹
فرماندهی سایبری حنظله در بیانیه‌ای با اشاره به عملیات ترکیبی گسترده و هدفمند بامداد امروز که در پی «تجاوز نظامی آمریکا» انجام شد، اعلام کرد که بانک اطلاعاتی به‌روز و تازه‌طبقه‌بندی‌شده‌ای از اهداف مرتبط با پایگاه‌های نظامی آمریکا را در اختیار یگان‌های موشکی و پهپادی سپاه پاسداران انقلاب اسلامی قرار داده و تمامی اهداف تعیین‌شده با موفقیت مورد اصابت قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/655730" target="_blank">📅 13:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtORWiDvw9pIRS6SfM6nCAGZs87ucqqNQ23E_BxOSdDy49j1KaZinOoezJJKaHaDm12odyaeKfR_1aEX7pNUI1ixOLQmxFQBjUghf4cX2Iz6cHf3xhPW-28SCpRo2lO7nPqxYGiRX3WAtELUFj5uUPmaOgClefm3GUiMTlnIPFa2Zu0KcvYB6xe-JcnSgKibt7QsLp2gWq1iB-RLwBB2mjkQ5LuUw9V91Ch2jN_ewXapGn8SDtnLoJBRYyXPdzdDdjyqwYaJhTwlP52Jtr_PXAKxxU151ttdGXY-PZA_a6fj1eGaljdnS0pOqkS2j9fjwfwKgJxEoqj-S6cHzYwZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارکرد قسمت‌های مختلف گوشت گوسفند
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655729" target="_blank">📅 12:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rohBOAC-Y3TLejSmPJcFwHsK-CO5b4vYmcspR8AFQruZdwdMA2VafiP8SkeyLf8z4O4KcQ-5eS5FA5UBAw40Jv84f5vFbHifCe5l4yQmCrbdmve7ESRUH88TZbDnajONo_DNxEf-qhhVCLVeHSsa1LTm0euVy4jT8ziaMdEUkHvFcVqIW-7ppuZRSb5RlCF6aPXRxdKXkEZKyt9zpe3OlvTPkqR6Y_02CK5c-87f9vR_x4E7pNmdCrLIA8mnk8vkVGEKjh8UfCMVRVZThj9k7LCn62VY9MxZ7dNGQUTTneAdfVjkKunRZYaFJLQ0OEXOu9F7NcFZkTcFSvdDIOpbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f711e1264.mp4?token=iM1MvKMIyJOHr3NgaWXE0m7Jz0piCHsD2KRopjRNHPRAP2h8sZFspc-_pwLrJUeOntvnIjEguiyLHIgSDNCUNDvHxuRz0ayUj6XRiAUlwTEsCrD8lQbRoA_9wWY1jYiqomzJ2zJIbpvkF9CAHSQ7tsdAksJ-BbjOQ2Gpq6lWba_xTLUba3jl4s0mRlzpuWaCLUO0JK-FKtTb1ESo4eDEupS3L7o_1GlQxfLFzuF2RlPAkhvZHqu1xR_wZVQzJpxfSolJPHIR5gilez970ybR6L5jvrX1oXdCSvSVfTpRBnyKd6QZchvxoogtTmNYzjBlQmmLxl1JUuFSWq_3zPFtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f711e1264.mp4?token=iM1MvKMIyJOHr3NgaWXE0m7Jz0piCHsD2KRopjRNHPRAP2h8sZFspc-_pwLrJUeOntvnIjEguiyLHIgSDNCUNDvHxuRz0ayUj6XRiAUlwTEsCrD8lQbRoA_9wWY1jYiqomzJ2zJIbpvkF9CAHSQ7tsdAksJ-BbjOQ2Gpq6lWba_xTLUba3jl4s0mRlzpuWaCLUO0JK-FKtTb1ESo4eDEupS3L7o_1GlQxfLFzuF2RlPAkhvZHqu1xR_wZVQzJpxfSolJPHIR5gilez970ybR6L5jvrX1oXdCSvSVfTpRBnyKd6QZchvxoogtTmNYzjBlQmmLxl1JUuFSWq_3zPFtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئیت سفارت ایران در تونس با عنوان «یک جبهه یک مبارزه
🔹
در این توئیت تقابل بین نمادهای خداباوری و امپریالیسم آمریکایی با به تصویر کشیدن مجسمه‌های آزادی و مسیح با استفاده از هوش مصنوعی نمایش داده شده و بیش از شش میلیون بازدید داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655727" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d4dce72.mp4?token=pHxLyDMYnwbPm74xZTLpXs2QBUDHOFswFqQ2kTk2EtwpoQtwKdq3wSWjsCHDBdJbWQvpOmG2Q3Zq9Wpm01zSofSTL43mE6F7GQ4SUsTJ40UXJRntkcCsPvNAIRqtIRi958d1bszhdGXhUz2hGTSuc96pg6onv5RsIO98FPh9EvUY2kRuyynYI_HOCeXyyICQoLwiXb2uuCJ60dcxMzE3SGmuitwc92S4VJ4fxEreoPIeF4cdDgR60rP8im2oOPeZkLFGngS8zXEGmab15TDCft4VSeNYv5SJNMwA7PBDdbtLY1ZjvNTFAZovGawZwWwSe8i-XL9yo24z-Ut20Nf_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d4dce72.mp4?token=pHxLyDMYnwbPm74xZTLpXs2QBUDHOFswFqQ2kTk2EtwpoQtwKdq3wSWjsCHDBdJbWQvpOmG2Q3Zq9Wpm01zSofSTL43mE6F7GQ4SUsTJ40UXJRntkcCsPvNAIRqtIRi958d1bszhdGXhUz2hGTSuc96pg6onv5RsIO98FPh9EvUY2kRuyynYI_HOCeXyyICQoLwiXb2uuCJ60dcxMzE3SGmuitwc92S4VJ4fxEreoPIeF4cdDgR60rP8im2oOPeZkLFGngS8zXEGmab15TDCft4VSeNYv5SJNMwA7PBDdbtLY1ZjvNTFAZovGawZwWwSe8i-XL9yo24z-Ut20Nf_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروژه جنجالی گوگل؛ رهاسازی ۳۲ میلیون پشه در آمریکا برای نابودی ناقلان تب دنگی، زیکا و تب زرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655726" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=bgBp25VvxXGBsoX1AOdQa3oQWjZKwKEf47Z_dC7Nf20EQmSux1uHQIjTdyVyO70rrb7IjJhgoQj5EmdTO_gyPYSU3hNqCzdoaOtwbG6mToduWeJ0ncUULSUYlIPI15p1LGcojEurwR_mY75vUJJLwcMdm-WIqV7X-vxuK4tnh7pV2R4aUhL0pjfx6dn7ktuACV55q27bmain9ZgFs8Wxqxny0hnUrfjDy-oKXC-BYmzhAL3kMXkHT2oAIC4hgNx0PtuX0nEWIBR95XYwQbdmeQa2o3kY651gg42oGCaG3QDyMfc9AnSSXvNZ_3EQhxDHztcmCJiLLyGqgJwHynDS-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3647677f2f.mp4?token=bgBp25VvxXGBsoX1AOdQa3oQWjZKwKEf47Z_dC7Nf20EQmSux1uHQIjTdyVyO70rrb7IjJhgoQj5EmdTO_gyPYSU3hNqCzdoaOtwbG6mToduWeJ0ncUULSUYlIPI15p1LGcojEurwR_mY75vUJJLwcMdm-WIqV7X-vxuK4tnh7pV2R4aUhL0pjfx6dn7ktuACV55q27bmain9ZgFs8Wxqxny0hnUrfjDy-oKXC-BYmzhAL3kMXkHT2oAIC4hgNx0PtuX0nEWIBR95XYwQbdmeQa2o3kY651gg42oGCaG3QDyMfc9AnSSXvNZ_3EQhxDHztcmCJiLLyGqgJwHynDS-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در حین پخش برنامه آشپزی شبکه سه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655725" target="_blank">📅 12:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655724">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
۹۵ درصد بلیت پروازهای لغو شده جنگ تعیین تکلیف شد
رئیس سازمان هواپیمایی کشوری:
🔹
۹۵ درصد بلیت‌های پروازهای لغو شده جنگ تحمیلی سوم تعیین تکلیف شد.
🔹
روند تسویه با معدود مسافران باقی‌مانده همچنان ادامه دارد و تا بازپرداخت کامل وجوه و استیفای حقوق تمامی مسافران متوقف نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655724" target="_blank">📅 12:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orjhzt3PAVzCrvvjvtFd3w21paGWdVHpenI9BNdlgAh075bS_pffu9CdKvkpj9B-hteO54VI44h_uyrZMuy1ej6e9kGt3rubZh2WDEfLuordp1ylk3R0ri369IAgO_iEI7Yio1bG1I04uRQQ04QwkMsDrh7iYWG2u07FJuT8F97O7VBIbNcHm1A78ROyxTsc1pkeeBH1iVzGlqw8lFtCpGOGbMiTadvq5gqBAdVExtzkNgho27FKiYqPXo3HBFG5NgXsXNMMXbP0W2vbaUX44Y9b9jzsEMaxQxdBGrj0w5g6HzA6GfLlnNQyadK99iBKQFZMvBiOMxkgXnOPlBFwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
مهمونی بزرگ در پناه ِ غدیر،
🔹
با حضور ۱۱۰ موکب پذیرایی، بازی کودکان، غرفه‌های فرهنگی و هنری و ...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: پنجشنبه ۱۴ خردادماه از ساعت ۱۹  الی ۲۳
✨
مکان: مشهد، حدفاصل چهارراه نخریسی تا چهارراه چمن
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655723" target="_blank">📅 12:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ستادکل نیروهای مسلح: تا پای جان از ایران و انقلاب اسلامی دفاع می‌کنیم
🔹
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا(ص) در بیانیه‌ای به مناسبت سالگرد رحلت امام خمینی(ره) و قیام ۱۵ خرداد اعلام کردند نیروهای مسلح مقتدر تا پای جان از انقلاب اسلامی و کیان…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/655722" target="_blank">📅 12:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhdTim_cQw9t1KiTGbVfOjltVykveLe6CFfbOjdOT7YJQt7_kJkCcwXQ5tRKicp6GmO_u19UuaqRt_vqV67Cha8ryBHpkwuWaqCCiMS1M9WCfhxNPCXJZJzBJs95uHba9ocRCq-ZGmWGituMa-0xKpZd2eOvqjxCtGY14Jt6LN_n0DW7FBdMTZezNhWEWn2kEcfK-D5dy4p84jC6-69Us8d9SBt-d7Gq_MeHseqqaYCeE2m5DWUmiDWwLLJibhJNqB5YOnRnk-V6M9QuR4q4OpA4wwmh2JxKkcwI567XIAW8pe-lf_wRdTnrPtrhP1JMiKyr0666fxRYIoA1diyxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مالک باشگاه طارمی آماده پرداخت عوارض تنگه هرمز
🔹
ماریناکیس، مالک باشگاه ناتینگهام فارست انگلیس و المپیاکوس یونان اظهاراتی جنجالی علیه ترامپ و به نفع ایران انجام داد و اعلام کرد که «حاضر به پرداخت عوارض به ایران برای عبور کشتی‌هایش از تنگه هرمز» است.
🔹
ماریناکیس با داشتن بیش از ۱۵۰ کشتی و نفتکش جزو ۱۰۰ چهره تاثیرگذار صنعت کشتی‌‍رانی دنیا به شمار می‌آید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655721" target="_blank">📅 12:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b74e202e.mp4?token=ilAM6sgI0tgWhoYs-FTbPozOdC13YQM9aRsUbOqAIvsbPgmhHh_G_HgYc_eOP9mUthU8jlaqeU10oZ--dd8VqOAqCr24J7VAq0yFrlaVL4jekMqJATh99sHhYpHxzKkk_wYHCqXEIybA-iVEj3TeIEW0CNZJcv4nTkXiwiiySMpmQNHunJ3RvlPq3C5lFn8U45md3qfwrC5kdAU8RbZ-SmnNhod6lHlNPB4ZBRBBXk9EaggEbPRHY7EMAls-G5NfRzUcVRhQUvU3FZUeztau6odCDLP0HOgpFKfqcpGRUoGAmuqEYOB60hxOh9bDnrOEKv-fDfFlSE8yGAw1iaaQrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b74e202e.mp4?token=ilAM6sgI0tgWhoYs-FTbPozOdC13YQM9aRsUbOqAIvsbPgmhHh_G_HgYc_eOP9mUthU8jlaqeU10oZ--dd8VqOAqCr24J7VAq0yFrlaVL4jekMqJATh99sHhYpHxzKkk_wYHCqXEIybA-iVEj3TeIEW0CNZJcv4nTkXiwiiySMpmQNHunJ3RvlPq3C5lFn8U45md3qfwrC5kdAU8RbZ-SmnNhod6lHlNPB4ZBRBBXk9EaggEbPRHY7EMAls-G5NfRzUcVRhQUvU3FZUeztau6odCDLP0HOgpFKfqcpGRUoGAmuqEYOB60hxOh9bDnrOEKv-fDfFlSE8yGAw1iaaQrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اولیه از فرودگاه کویت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/655720" target="_blank">📅 12:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRaPqbAXSluh2PTxN16ec3oShBhZCZQxrUiL0qeeU0rBoInGy-2LEhF7ZbY6Q93qMyajtopyl2bNsIYbJG22IMKbRgh_9wKimxDlF2Ob1nNte45oB8cVCGzfMETZtdsp1AwxD37kp3dYQ7CFZjVeO0eiiUBbisjvohYcTYeT0Ow-TIr18glHStQudVBB3c1HruvALkD64d1swXzI44SX9piufMyCqKZHdcPikAOdvZWo_QwUD7nPe2IQV4B1unOsXNLCh_FMxz6QuPkXo04offwnxVGz45nx3MUHpzGD6hrVUAu2DrrPs4yduw6qzf5gwQNSBHi5qPuIcaibk2HFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مغز ما شایعات را باور می‌کند؟
🔹
انتشار شایعات نه یک اتفاق تصادفی، بلکه نتیجه‌ مستقیم واکنش‌های هیجانی و سوگیری‌های شناختی ماست #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655719" target="_blank">📅 12:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poEadhHVceIMJRUBMUUUw8SehQCvy9l1sZRRnoYjV1YKJbWLqf5az7WDEIvdBfMZWkg18gNl7WyU8oT9ST0oGmxSJJOLB-NvlajNlRtrdgg16NgKcxH9tTt748PMGAtl8hdpNTEn_a0QvzCJdHeXWvqSjMRv_MoTlQrkPKxr9_0eOkvZBXfgHucmnMQDiM3Czb6V142mqF5yTXiFL8jySG5k38xm-bYrln19fJ0ltyZZN8KowEeWU__Jw3zAWcRPm4uVcB6GxjuS68_tiZcy9LXTlARmuueN5RjmWDZasqrDN3yjeKvRaBgQ-u86epJnHQ5n6rMczqwzez0CELVHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انجمن فین‌تک اعلام کرد: تحریم چند صرافی به معنای در خطر بودن دارایی کاربران نیست
🔹
تحریم صرافی‌های رمزارزی حق دسترسی شهروندان ایرانی به ابزارهای مالی شفاف، فناورانه و روزآمد را محدود می‌کند.
🔹
به‌علاوه تحریم چند صرافی به معنای در خطر بودن دارایی کاربران نیست. زیرساخت‌های نگهداری دارایی در پلتفرم‌های رمزارزی، از جمله استفاده از کیف‌پول‌های سرد و سازوکارهای امنیتی چندلایه، برای حفاظت از دارایی کاربران طراحی شده‌اند.
🔹
بنابراین، تفسیر این خبر به‌عنوان تهدید مستقیم و خودکار علیه دارایی همه کاربران، نادرست و نگرانی‌آفرین است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655718" target="_blank">📅 12:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932b0a2d61.mp4?token=wBi6BA4w7Ius3QMcCV1dHvQqUYugmmZvfKEfIvV5sbTAQNq6KozEoyNZwhHg2QpsE6RT-0J4gdV-0XuXCpaBCNRrH0CZ8jp1UMFjtUGxpC3xcAqIuNaWVahOVKq27ol_evvMfBe7UisA49zfFt9qtYYsVsCqr3uQJP-YxmQndmm25OsdEtF-XEoeQqOzKBPdjV61TljMCj9Ka2grk8YumH-9J6HCc9OGz-eBML9ho9IDPM_vBb4sthnWS4kpYuhn96pxQRNJKKhLBOnD8OwgS-dTaQR_KakDGS_AHt98qkzbtHdkKurd4KQX61BQnDcZArTK2aMHSZdYtNnq0MhmB5AM5UoG5wQi3oBU3_aAS3iLNYjsPUoBwSFtWPlA595ng0ejJ-j3vzLoehJnnNmIb4FnSgdj0BNX0K-GSeOcWVgk6Zu4xy7mOSG-gUKYj1ldrvSoSdMI7HAXG5E-VFfhFkm7V8pVXY1q5ARfxIGaRE2ayklpWCOBzSDm1WieESSFaInEWwcex3YVnZwLybwZrVQ2_nxuyTZfg0Bn5h8-TM4YXc4mHoKzBQABkGzFEc3-bax-2nBiuobHTNAJ629XxcDF4CNy5XQhzbE4Kyi1npNk984Wo_4zAdaQ1suNhi5DVOhYxFtEclJ9YiHp2aOrujT6vwz4zxCSj_wdjjTFEqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932b0a2d61.mp4?token=wBi6BA4w7Ius3QMcCV1dHvQqUYugmmZvfKEfIvV5sbTAQNq6KozEoyNZwhHg2QpsE6RT-0J4gdV-0XuXCpaBCNRrH0CZ8jp1UMFjtUGxpC3xcAqIuNaWVahOVKq27ol_evvMfBe7UisA49zfFt9qtYYsVsCqr3uQJP-YxmQndmm25OsdEtF-XEoeQqOzKBPdjV61TljMCj9Ka2grk8YumH-9J6HCc9OGz-eBML9ho9IDPM_vBb4sthnWS4kpYuhn96pxQRNJKKhLBOnD8OwgS-dTaQR_KakDGS_AHt98qkzbtHdkKurd4KQX61BQnDcZArTK2aMHSZdYtNnq0MhmB5AM5UoG5wQi3oBU3_aAS3iLNYjsPUoBwSFtWPlA595ng0ejJ-j3vzLoehJnnNmIb4FnSgdj0BNX0K-GSeOcWVgk6Zu4xy7mOSG-gUKYj1ldrvSoSdMI7HAXG5E-VFfhFkm7V8pVXY1q5ARfxIGaRE2ayklpWCOBzSDm1WieESSFaInEWwcex3YVnZwLybwZrVQ2_nxuyTZfg0Bn5h8-TM4YXc4mHoKzBQABkGzFEc3-bax-2nBiuobHTNAJ629XxcDF4CNy5XQhzbE4Kyi1npNk984Wo_4zAdaQ1suNhi5DVOhYxFtEclJ9YiHp2aOrujT6vwz4zxCSj_wdjjTFEqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از لحظات دلهره‌آور خارج کردن یک بمب عمل‌نکرده از پشت درب واحد یک هم‌وطن تهرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655717" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndpmqS6J7OgsgtlxZgsnuIHvpotZ2qDdU56iHsMF0t8nWSPBNX4hoaiObrGIud-PACUJmgkJ6eWC6NK-6qDCHjz4oph6JyeB8yjkPhfXnL6fkojagG4V2Q6qqfDo4mHTUY5wi8xmfTg4C5X5YUua-OJef6HtVKAKwZQk1VI-u8kUi2W98IXI3yptXx3ZOrx6OBkti0I2dLNkvxloTpMMzUGw4M8VO4NsPNVZWMGR2uQhhM4U-d8Mc_OeRr6Q0mpttbL-6sJyMT4kM_BipEILNmsdmbgeQD_hnyz0Q1Ha9K1kG61FmrlYXkIJo6rCFw6fiAncGMIeKBJW4q6Hdyn6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNHvSoysADl1AS_YKrKd3f-RrAeuFttZlG1LX0xlTsZF55vmIiWsWBBgGFe4fys436CsVKeJQgWRMG8StXZRbLIWLomIvk2lx2nC0VBJzRCistKSr-5fV--kV2j-W8xr29gxI0qxlf--d_QsheedUjSVT2qapMKJrzjLKCOI1kZA6eYG_pUmS4ZiW1sbRxOrkaAurIXbkM3f67xxcAUXuhQFO9B6d38e24V8NREUuJcsJ2YQNNgI7Da64tyuHpsWCB-WuEUlDB7wYa6MyRS1y_2XzeWjAaGx4-FAk9Dj240-wWpPwOZsWcstIkOPbwxXDQ5UscvWEWiEMTY2BvI2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgxlmNo2ySGazwceY0sSJiOcoD9d8wVvkkmd9fPmW77Qxw8j2xjspsMIAyBahbZys7tk-0XRyLJDgf7tX_1H_ne3rK8bIRQ-63DUflvKI1b4aRpjMbPa2SU-IpOfgLfLD3S_IYmet6wuSxyy2-kXMHIWPJmWycNDKbZRagYGpZcXgnakdSdGMV6g7HdkIaNwOmCNiu98GDPBLBtN8_QZD5jR0Wz_MG9n4CVuX4DBDlPnor77iexiT7rLrTJMH4LD8GtbSbUsoOoQSA3w3nmlyXqm0fDfavRnt-2qj88lsAQGKzW4HQKuoYva7ltm5D6zH6y4U3Fclytyhg3k_uQVsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادعای کویت: حمله به فرودگاه منجر به مجروح شدن افراد و خسارت شدید شد
🔹
سازمان هواپیمایی کشوری کویت همچنین مدعی شد که هدف قرار گرفتن فرودگاه کویت منجر به مجروح شدن تعدادی از افراد و وارد آمدن خسارت‌های شدید به برخی از تاسیسات آن شد.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655714" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر نیرو: برق و آب مشترکان پرمصرف قطع می‌شود
وزیر نیرو:
🔹
در صورت تجاوز از قواعد تعیین شده مصرف، ابتدا جریمه مالی در نظر گرفته و در صورت ادامه روند پرمصرفی، آب و برق مشترکان قطع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655713" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اعتبار دومین مرحله خرید کارت امید مادران شارژ شد.
🔹
قاتل شهید سرگرد محمدجواد بخشیان از شهدای دی ماه همدان اعدام شد.
🔹
جلسۀ صحن مجلس یکشنبۀ هفتۀ آینده برگزار می‌‌شود.
🔹
ساعت معاملات بورس تهران به روال قبل یعنی ساعت ۹ تا ۱۲:۳٠ بازگشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655712" target="_blank">📅 12:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiPV2eynWifss0ASuWuQHVl53nJOftWLBd6sJDHuv-2gSxBAB75jgybqklqEzmCuU7I7a08mQM5MQs2JW3_9TQrS9G69Ab2xJBmkf_6oswCNk69vUc_EcX30bjKQxw_xAEUfyY83J8XpkTmgHMkQ2XHhjqx6pNXy8ULUKePrI6hJOYBc-LGN1ImqIoSgPs-MVdmgX87d8dPMwh85-Gnc79kZJyC9h3KHDzjmhZVA38CZ80iaR-7z6rBLbCfLgJtoR6ewjiOKBDjxnPMGQHfl3LlSa7bvdRU7OlhlMyr610oilhTfG78kGC3cuzAeEe9jLgncVrt6fTJQwmf7mqSbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است
🔹
نه در مذاکره و نه‌ در روند آتش‌بس اجازه زیاده‌خواهی به آمریکا را نخواهیم‌ داد. پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است. تاریخ به عقب باز نمی‌گردد و متجاوز به سرعت تنبیه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655711" target="_blank">📅 12:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ستادکل نیروهای مسلح: تا پای جان از ایران و انقلاب اسلامی دفاع می‌کنیم
🔹
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا(ص) در بیانیه‌ای به مناسبت سالگرد رحلت امام خمینی(ره) و قیام ۱۵ خرداد اعلام کردند نیروهای مسلح مقتدر تا پای جان از انقلاب اسلامی و کیان ایران دفاع خواهند کرد و اجازه پایمال شدن خون شهدا را نمی‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655710" target="_blank">📅 11:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ترامپ خواستار تعهد کتبی از ایران شد
🔹
مقامات آمریکایی و یک منبع مطلع دیگر به شبکه آمریکایی ای‌بی‌سی نیوز گفته‌اند که دونالد ترامپ، رئیس‌جمهور آمریکا، از تهران می‌خواهد به صورت مکتوب، امتیازات هسته‌ای مشخصی را به‌ عنوان بخشی از یک توافق اولیه با آمریکا ارائه دهد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655709" target="_blank">📅 11:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
محکومیت شدید حملات تجاوزکارانه آمریکا علیه نفتکش ایرانی و دکل مخابراتی در قشم
🔹
وزارت امور خارجه ایران حمله آمریکا به یک نفتکش ایرانی در تنگه هرمز و دکل مخابراتی در قشم را نقض آشکار حقوق بین‌الملل و منشور سازمان ملل دانست.
🔹
کشورهای منطقه‌ایِ مرتبط در این امر مسئولند ایران در چارچوب حق دفاع مشروع، پاسخ متناسب خواهد داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655708" target="_blank">📅 11:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308373b99b.mp4?token=healC8C7HIWfezGCB_FcOtfL3cKZU1h4AaAzy-145tvcdA5vy4xanxaiB4Mn3Dx9-Y1WzIuvRR9mthEPal40cpssn0YxSsONi4780-u0hbOB7JmQIYHBlMdZY-VHTCmIRpmN4m_J_XAmt6d8nmRXCRAnPMhCS3JZnDShi2cvrsEFXPFo5eplquRrEhsQxdTE7LfFR_Uvun4E8Szt4bnwUJp5PkOsiy5KmDd_83bW2AbGc33NM3m87O0HhviHXLZaMkcWo-hym5y159o2gMH8tib_ktSztdu1U2v2doFLx7DEy1leG-Zql9Bv5GGjAFwiP6tFla20IOCjv1ZWpIkovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308373b99b.mp4?token=healC8C7HIWfezGCB_FcOtfL3cKZU1h4AaAzy-145tvcdA5vy4xanxaiB4Mn3Dx9-Y1WzIuvRR9mthEPal40cpssn0YxSsONi4780-u0hbOB7JmQIYHBlMdZY-VHTCmIRpmN4m_J_XAmt6d8nmRXCRAnPMhCS3JZnDShi2cvrsEFXPFo5eplquRrEhsQxdTE7LfFR_Uvun4E8Szt4bnwUJp5PkOsiy5KmDd_83bW2AbGc33NM3m87O0HhviHXLZaMkcWo-hym5y159o2gMH8tib_ktSztdu1U2v2doFLx7DEy1leG-Zql9Bv5GGjAFwiP6tFla20IOCjv1ZWpIkovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربران رسانه‌های اجتماعی لبنان تصاویری از یک انفجار بزرگ را منتشر کردند که ارتش اسرائیل در منطقه «عریض دبین» در جنوب لبنان انجام داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/655706" target="_blank">📅 11:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پلیس اطلاعات فاتب: ۱۲ نفر به اتهام هنجارشکنی سازمان‌یافته در فضای مجازی و اخلال در آرامش روانی جامعه شناسایی و تحت پیگرد قانونی قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655705" target="_blank">📅 11:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a515e9a0.mp4?token=NQ5IyjLeO7IvnkEeJ8G6nATxz5yUDRn3AhersNKyq0DCH2H6lFYxM1QtUuond0llrHL_jvZfMqSvoZg6LbZsVpV7DIosmtFm-O52KvIvfu5U47Z347zdsC-qIcz5R_eVb1ZW0LIygHzaHk4yZTeQahcCkwZeXr9YOUffDyv0Y_KbmX990WGj23qpEHIjtX3Ni9MOGLIUnEXq8cMeKwv-mJpm8vYrdylrAId-P66wfklwB3SPUl3c-J0GCW8OTCADitHrG9ey8FLIHXv8J6iDxtIPZJWXvoHFcCieIx469oJAWotNd_coW87e3L3fYg0AshM7yfBb_7mVMlEGpVMPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a515e9a0.mp4?token=NQ5IyjLeO7IvnkEeJ8G6nATxz5yUDRn3AhersNKyq0DCH2H6lFYxM1QtUuond0llrHL_jvZfMqSvoZg6LbZsVpV7DIosmtFm-O52KvIvfu5U47Z347zdsC-qIcz5R_eVb1ZW0LIygHzaHk4yZTeQahcCkwZeXr9YOUffDyv0Y_KbmX990WGj23qpEHIjtX3Ni9MOGLIUnEXq8cMeKwv-mJpm8vYrdylrAId-P66wfklwB3SPUl3c-J0GCW8OTCADitHrG9ey8FLIHXv8J6iDxtIPZJWXvoHFcCieIx469oJAWotNd_coW87e3L3fYg0AshM7yfBb_7mVMlEGpVMPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداقل ۱۸ کشته در پی آتش سوزی ساختمانی در هند
🔹
براثر آتش سوزی یک ساختمان در یکی از محله های دهلی نو، حداقل ۱۸ نفر کشته و چندین نفر زخمی شدند.
🔹
این ساختمان در بخش جنوبی شهر قرار داشته و برخی از قربانیان اتباع خارجی بودند که برای درمان پزشکی به هند سفر کرده بودند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655704" target="_blank">📅 11:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655702">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=oPd8-RnbKafgjb5IKATY9ji5V5mwr4vfvYC2tDabBW2mO-xchUiejxLSH4im9WscgxybKXVNMwkECFsqJ8SXbJ_a-vbCllWnPGYWOJRYO05D6joGafc3-NSZpcwgztizN00wTHr3N0WqBpJAN5nNoa-AdKlpUXR27ctilJqlbuGD_aP34Kh5JahBWIVw-AET1J5k7715TG_WmOTExFfl4EgXS276DJKmDlt6hDi3gRSwtFdTZGYMJGAKX9cSWhqPw6uwxI2kxLEk-5owpbI_gG2BLFN_flarIXbEhMwKx14ElLNKvN9A7RWFNSnMv2OYDiCqK-8TEhJeBShcCQUESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=oPd8-RnbKafgjb5IKATY9ji5V5mwr4vfvYC2tDabBW2mO-xchUiejxLSH4im9WscgxybKXVNMwkECFsqJ8SXbJ_a-vbCllWnPGYWOJRYO05D6joGafc3-NSZpcwgztizN00wTHr3N0WqBpJAN5nNoa-AdKlpUXR27ctilJqlbuGD_aP34Kh5JahBWIVw-AET1J5k7715TG_WmOTExFfl4EgXS276DJKmDlt6hDi3gRSwtFdTZGYMJGAKX9cSWhqPw6uwxI2kxLEk-5owpbI_gG2BLFN_flarIXbEhMwKx14ElLNKvN9A7RWFNSnMv2OYDiCqK-8TEhJeBShcCQUESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ اوکراین به سن‌پترزبورگ همزمان با حضور نمایندگان ۱۳۰ کشور در این شهر
🔹
درحالی‌که نشست «مجمع اقتصادی بین‌المللی سن‌پترزبورگ» از امروز با حضور پوتین برگزار می‌شود، ترمینال نفتی این شهر هدف حملهٔ پهپادی قرار گرفت.
🔹
منابع اوکراینی گزارش کرده‌اند که این حمله همزمان با آغاز نشست ۴ روزهٔ مجمع اقتصادی بین‌المللی سن‌پترزبورگ بود که نمایندگان تجاری و دولتی ۱۳۰ کشور در آن حضور دارند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655702" target="_blank">📅 11:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اعتراض به وصل شدن اینترنت/ ترقی: دولت باید از ورود این سموم فرهنگی جلوگیری کند!
حمیدرضا ترقی، سیاستمدار و قائم‌مقام دبیرکل حزب مؤتلفه اسلامی در
#گفتگو
با خبرفوری:
🔹
همین چند روزی که اینترنت باز شده است شما شاهد انواع و اقسام دروغ‌پردازی و شبه‌افکنی‌ها توسط دشمنان از طریق اینترنت هستید
🔹
لازم است در چارچوب قانون این تصمیم‌گیری‌ها پخته و مبتنی بر یک عقلانیت دوراندیشی صورت بگیرد؛ نه بر اساس احساسات و احیانا فشارهای سیاسی برخی از جریان‌ها.
🔹
در حال حاضر یک فضایی از قبل از جنگ حاکم بر کشور بوده که موجب قطع کردن اینترنت شده است، این فضا تغییر نکرده و طبیعتا باید منتظر باشیم تا آن فضا تغییر یابد.
🔹
مردم یا باید خود را در برابر شنیدن این خبرها و القاهای دشمن مصون کنند یا اگر احساس ‌می‌کنند تحت تاثیر قرار می‌گیرند دولت وظیفه دارد از ورود این سموم فرهنگی به داخل کشور جلوگیری کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655701" target="_blank">📅 11:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3e8e77f0.mp4?token=kQJH9Rn5-0iLuO7t5SHbOiYzaXyEHDk5Lc16UqdrYyuQvJJcbZQfpCAvqmWduZugd8mRuMEmI9mS-qSoi_D_XphhYFEwItSisjZOfQhCG5WxN_l5aX2xqAw1C00LLot9erDeLNFGq4PIkLrzGU224FPbXtbJytT4wgdUE_yA3r05FxoOF0iLSEdP0apYOWS_DVanFg5DEVjj-kH017YRPtZkQCHTMquVDw1q0tJkB_uKa-f0gv5YKfiMZFp-N9bVrAXB52o94rurq-gcGZ3zdzbtIp2KwmAv1fJumrGqACVNPfNaGx0Tu_9dIQJWpPVmXVWDq5EZr5H33QbdHwFG_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3e8e77f0.mp4?token=kQJH9Rn5-0iLuO7t5SHbOiYzaXyEHDk5Lc16UqdrYyuQvJJcbZQfpCAvqmWduZugd8mRuMEmI9mS-qSoi_D_XphhYFEwItSisjZOfQhCG5WxN_l5aX2xqAw1C00LLot9erDeLNFGq4PIkLrzGU224FPbXtbJytT4wgdUE_yA3r05FxoOF0iLSEdP0apYOWS_DVanFg5DEVjj-kH017YRPtZkQCHTMquVDw1q0tJkB_uKa-f0gv5YKfiMZFp-N9bVrAXB52o94rurq-gcGZ3zdzbtIp2KwmAv1fJumrGqACVNPfNaGx0Tu_9dIQJWpPVmXVWDq5EZr5H33QbdHwFG_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه آسمانی سلسائو قبل از جام جهانی ۲۰۲۶
🔹
تیم ملی برزیل با مراسم مذهبی راهی آمریکا شد.
🔹
مسئولان فرودگاه با برگزاری آیین «غسل‌ تعمید» هواپیما برای این تیم در جام جهانی آرزوی موفقیت کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655700" target="_blank">📅 11:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95fbed9f42.mp4?token=ocbfTDIb5A9JARPvwKardyijXnXJW3o1X9S57zIWECpguMUlvjvLWyUGFHPeNETxa3DnWii2amlIRKIDjAOxHlKRmx-J2C3TrB2ovmyPDEM25utR3Pr7UTwbgOp-ucSWEhDCuOzkU8GOz2AuO1UWEgaUykunAiMV-e60Xd-rfpo4H0jk8i4Jtqrj7rEX6hKfkSoqtPYA5tV8f4GGhSJ33Jm_67c8PFJGTHmp4zGRSaJuckQtZztZUM9FBWMlTfhlWtJplu4ryR6is1mD2Sg10cinOk5DLfp8vSmSRbQ45Ayttg4UGbYOD8Y65BL8FkRGoPd7fHeJe7SeTr9LLpOYQHlf3j4Cxa4RK-PyKSDJCTy7dqQ34XNfxUrTpQav5HXp5nS_7ZJDiPAyNQevjEzlI5fLyIHW1Li5Dd7xFo_UWFfJhmNP5zZjIPEab3v2489evvMZbx42U0tCrxXsNH28jo1bzO_RSUt0wcLISO1Hns9uHOCLRcj85FH6cjXfrEPJXJ7nsVpj4azzkjYFGiUMvG6cpESMxyxSNz-fkrWbIbYycsS9qNPWb-Nxn3fQGuGDZCCRyTSjLXuL5VLSv5Y_B0URp7iE8iBw03c3E4bm6XS7DuZcV8GivrCLS8KZ_T4dSk45XJ_lD0qGInLcRdgP3ZVP7zDCtBnF2AZ7tm6hotM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95fbed9f42.mp4?token=ocbfTDIb5A9JARPvwKardyijXnXJW3o1X9S57zIWECpguMUlvjvLWyUGFHPeNETxa3DnWii2amlIRKIDjAOxHlKRmx-J2C3TrB2ovmyPDEM25utR3Pr7UTwbgOp-ucSWEhDCuOzkU8GOz2AuO1UWEgaUykunAiMV-e60Xd-rfpo4H0jk8i4Jtqrj7rEX6hKfkSoqtPYA5tV8f4GGhSJ33Jm_67c8PFJGTHmp4zGRSaJuckQtZztZUM9FBWMlTfhlWtJplu4ryR6is1mD2Sg10cinOk5DLfp8vSmSRbQ45Ayttg4UGbYOD8Y65BL8FkRGoPd7fHeJe7SeTr9LLpOYQHlf3j4Cxa4RK-PyKSDJCTy7dqQ34XNfxUrTpQav5HXp5nS_7ZJDiPAyNQevjEzlI5fLyIHW1Li5Dd7xFo_UWFfJhmNP5zZjIPEab3v2489evvMZbx42U0tCrxXsNH28jo1bzO_RSUt0wcLISO1Hns9uHOCLRcj85FH6cjXfrEPJXJ7nsVpj4azzkjYFGiUMvG6cpESMxyxSNz-fkrWbIbYycsS9qNPWb-Nxn3fQGuGDZCCRyTSjLXuL5VLSv5Y_B0URp7iE8iBw03c3E4bm6XS7DuZcV8GivrCLS8KZ_T4dSk45XJ_lD0qGInLcRdgP3ZVP7zDCtBnF2AZ7tm6hotM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر رهبر شهید به سید جواد هاشمی: شما هر فیلمی رو بازی نکن!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655699" target="_blank">📅 11:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
دانشگاه آزاد اسلامی: تاریخ امتحانات ۱۸ و ۱۹ تیرماه دانشگاه آزاد اسلامی به روزهای ۲۲ و ۲۳ تیرماه تغییر کرد
🔹
این تصمیم به منظور جلوگیری از تداخل امتحانات پایان ترم دانشجویان مقطع کارشناسی با آزمون کارشناسی ارشد ۱۴٠۵ اتخاذ شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655698" target="_blank">📅 11:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYpCa0ngeCUicXzBe__9-sVUqAj9uHYJLay95ul_JQ_VlwOZO7g_GX3w3B5f9A3H_CpgvddfsWH-mm3OzZaE2ebJzXkvemk8yOyuleI-7VIwDzZZgS-1vcqNI1uj1sm5BA0x_azQYUxS8nmI87gDgP8Ez0jZ4UfEhp79DlOcSy06C7kibVKz3cHGQ9Zj7T-pgEjA_Gohcd94M7FlBZy4m34sG6i9E4qpC7ihF62GAyBdYEZT9irFeZ1749g__V6S4bCuTjNjpvWnPe12LDvlQ98yCZ2BdNnop6Yehwy8a9E0mHlrMQ8xBue117PZ1di0t_V-Hu6H0mFIwnlXYU07Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دریاچه مهارلو از پنجره هواپیما؛ تابلویی صورتی از بهشت فارس در آسمان
#اخبار_فارس
در فضای مجازی
👇
@akhbarfar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655697" target="_blank">📅 10:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
هزینه اخذ پاسپورت حدود دو برابر شد!
🔹
در شرایطی که هزینه اخذ پاسپورت در سال ۱۴۰۳، طی سه مرحله از ۴۰۰ هزار تومان به ۹۰۰ هزار تومان رسیده بود، در سال ۱۴۰۴ این هزینه به حدود یک میلیون و ۱۶۰ هزار تومان جهش پیدا کرد؛ اما حالا هزینه اخذ پاسپورت بین‌الملل به دو میلیون و ۲۰۰ هزار تومان رسیده و همزمان با افزایش تورم، هزینه‌های خدمات پلیس +۱۰ هم افزایش چشمگیری داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655696" target="_blank">📅 10:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkmiMfTpF59P8h0sK1JE41tly1ILcKtmv0KdTOHWJ8xZ0MNge7m7OZGlW96_s298i8vz5qx6bYidwqAvU9dGvG0hGmpoiLylXRQRvGW49ZUO-wYrEAzDTVuJdJTKBr8Vs8agwFnZz1Hp9dYlzFZnPIpW3arvrCifphpXshJMkn80ILmhUbQV9mmWG5vnj3tTuBOqKfKavHAiFSlaK-wQpXPonOMEpFufdH1kFCKNd603aMGp1guqvqNbZwKmko9wF6s-fzIC0UBMLV8015v9rPE3GvM8NBTPLkohrfUca-JnOTSl1oqllBT0z3BMDOyR0uLmXmwsfm6mUxixLbds-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثروتمندان فوق‌ثروتمند جهان کجا بیشتر می‌شوند؟/ آمریکا اول، چین دوم
🔹
پیش‌بینی می‌شود تا سال ۲۰۲۶، آمریکا بیشترین افزایش ثروتمندان فوق‌ثروتمند را داشته باشد و چین در رتبه دوم قرار گیرد.
🔹
هند نیز رشد قابل‌توجهی را تجربه می‌کند، در حالی که لهستان، قطر و ترکیه سریع‌ترین رشد درصدی را خواهند داشت. این روند نشان‌دهنده گسترش خلق ثروت از اقتصادهای سنتی به بازارهای نوظهور است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655694" target="_blank">📅 10:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ-3k04-DFfFLaNM-OXXDFKUbTQc1L0y-VFJHvuZTCQyd9cxCGCKqR-xoSSC35ZLF67q91BoTf3qInWCV8CbIH_mhIxd0gl-B77-sQofEdd0URZdGJmM-31HKw0ZWdBc7P0HI-Alt-rxtfVlLpYQhuusWPIIclG4fPtqc2kuEeheuSQACT4FtU8s5koSVMZhOMB5wPIaIFBQJ988y-mv_wwC8pRv5gfOrZhqDfTvtlx7PYDHv048KStpc-JUwCkpN70IwKZV7q9H-KO8QcwVMxKOTMl1spMBx8grPgVnMcaRN_rfMC4Bb6DahsQjFPtMHt4vEsmu3QyvpLsDK36Cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارش‌های سیل آسا در راه ایران؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655693" target="_blank">📅 10:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893412ed0a.mp4?token=TKu8IZtjNYysEWik7ACWLoQ64h6KW-jzHT6Znwratcc83bK6J9n6p-FFKcXiFmD-a03nesb8HkKxz9SI1uOpLlrpeIZ8nh58VUjN_K26QlQqUxaeDlr7rukoEmCyMThAHfPYqPWS4WR1Q-oFJrqMOfFoQEclBuq2mAhpdpdshi_CufmAQCW7kvLSYcLydGIEPoLOXRWu1yxEdQ2x6a3J4mRKqZkjwOv3gCul3cjM0T3EPW3DaHCC-IXTUvsGwx5qihWNmy2f0QSMbKYaDPY95v8m-6n2D7nUImFY-9YpJnonf4OSRXebf5_LoVqB7ZhyWeuuoWmbhKmnebjtp2mxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893412ed0a.mp4?token=TKu8IZtjNYysEWik7ACWLoQ64h6KW-jzHT6Znwratcc83bK6J9n6p-FFKcXiFmD-a03nesb8HkKxz9SI1uOpLlrpeIZ8nh58VUjN_K26QlQqUxaeDlr7rukoEmCyMThAHfPYqPWS4WR1Q-oFJrqMOfFoQEclBuq2mAhpdpdshi_CufmAQCW7kvLSYcLydGIEPoLOXRWu1yxEdQ2x6a3J4mRKqZkjwOv3gCul3cjM0T3EPW3DaHCC-IXTUvsGwx5qihWNmy2f0QSMbKYaDPY95v8m-6n2D7nUImFY-9YpJnonf4OSRXebf5_LoVqB7ZhyWeuuoWmbhKmnebjtp2mxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احترام از «خودت» شروع می‌شه
✋
این ۳ تا عادت رو کنار بذار تا نگاهِ دنیا بهت عوض بشه.  #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655692" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بحرین نوتام(ممنوعیت پرواز) صادر کرد
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/655691" target="_blank">📅 10:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiV2D1CByginRXIPImjjuI6qEyfOkdduSMo_ZnNP2SS25EzNnUeyk6NJ7UN0FbTE0WPZBC5uH95V81Xzs4_Ek1E3EohcWPbRhGFGAGmaY6V5C9btfQ_iRveO2Kiz7zQQ4crwfIfZI_CvWaYH-v1z1ciHGm2vB0JjH4Kbk8vSkdAn3Nqd5Fac5APik5dwd70v_wyoxPS7TwP0Kujp-IdyE1FbgRxQ3mAuV82tr3ASqSkCFmhES71YAw2YJARa963FCaCutrB_edhVxQvU8oxhfFzvIpSokenKMQJpc2uJEgiQiWuoexX6ZrcpT_ruxSbCiot9AdKFZruWW22-9iY27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
چلک
۱۰۰۰ متر زمین
۶۵۰ متر بنا
تعداد خواب ۵
استخر داخلی
چشم انداز جنگل و دریا
سند تکبرگ و مجوز ساخت
شهرک معتبر و برند
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/655690" target="_blank">📅 10:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf92e7e83.mp4?token=ZBJyEXksW1AW6HRl_3gTCgpOfC_qyyq7XaXlLNU-bxjupDwdwnEGPAVPeWjXMK5PKdKrkq4xQFQ1GPxUdORi24B21L3v4GMlECYiZLeLTSjYDbv5Li3Pc6iKlAcD8z7d22hmG9crtQv3p5sFLDdoYiuRoK0ZwhE_R2HYnxXCy6gvtYM_KbFslpXTCGp6zlGf2rg-pFsQDEXMo77gObUxHpVy3rsERilbt6KJaWbFYtNWuDrQcxYpjJgONN6o6mi2EK_yMnxH6N7L9unIqkQ4VvZtGy2F6I39S-4USi-I7Geq5fTROMUA5Idsgafg6Zj8wNzvs3CFTe256zOcxrpmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf92e7e83.mp4?token=ZBJyEXksW1AW6HRl_3gTCgpOfC_qyyq7XaXlLNU-bxjupDwdwnEGPAVPeWjXMK5PKdKrkq4xQFQ1GPxUdORi24B21L3v4GMlECYiZLeLTSjYDbv5Li3Pc6iKlAcD8z7d22hmG9crtQv3p5sFLDdoYiuRoK0ZwhE_R2HYnxXCy6gvtYM_KbFslpXTCGp6zlGf2rg-pFsQDEXMo77gObUxHpVy3rsERilbt6KJaWbFYtNWuDrQcxYpjJgONN6o6mi2EK_yMnxH6N7L9unIqkQ4VvZtGy2F6I39S-4USi-I7Geq5fTROMUA5Idsgafg6Zj8wNzvs3CFTe256zOcxrpmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله خرس در ژاپن؛ ۴ نفر زخمی شدند
🔹
در حمله یک خرس به دو کارخانه و یک منطقه مسکونی در استان فوکوشیمای ژاپن، چهار نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655689" target="_blank">📅 09:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f56cfb493.mp4?token=I5r1gp1F2LvNz3m0n48Vl5nYajyB9alRF25E3Yi1CmPd5KfW4C4F_yjQiP1IxoKW4X0_ZqHUywIqsRnHG1xYThBv9I63iA-KtjjHwbmRUm9F0hE31WzgBZn47r1YPSgi-FM2hXsbbnheJngY2fWlscLYWjLkIAziZrqs5yFcPkZCLiTYljf3UXDType22rQidytSu_HxHXDncOLZbrKQOAkEakDZJJV4ISPWv1yspNH3PMYIcRAHtL24l40PaZIGcXZnr7xNeJEBchR4N60_mkj81-Z3vqt2q3zSE-rr5BJpvnuvp1MtxXXeiwYAbqVP6JxZ4E0a4zMw2oHd2Ry0i4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f56cfb493.mp4?token=I5r1gp1F2LvNz3m0n48Vl5nYajyB9alRF25E3Yi1CmPd5KfW4C4F_yjQiP1IxoKW4X0_ZqHUywIqsRnHG1xYThBv9I63iA-KtjjHwbmRUm9F0hE31WzgBZn47r1YPSgi-FM2hXsbbnheJngY2fWlscLYWjLkIAziZrqs5yFcPkZCLiTYljf3UXDType22rQidytSu_HxHXDncOLZbrKQOAkEakDZJJV4ISPWv1yspNH3PMYIcRAHtL24l40PaZIGcXZnr7xNeJEBchR4N60_mkj81-Z3vqt2q3zSE-rr5BJpvnuvp1MtxXXeiwYAbqVP6JxZ4E0a4zMw2oHd2Ry0i4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروگان‌گیری و تهدید به بمب‌گذاری در کالیفرنیا
🔹
پلیس بیکرزفیلد اعلام کرد فردی که احتمالاً جلیقه یا کمربند انفجاری همراه دارد، چند نفر را در یک شعبه بانک چیس گروگان گرفته است.
🔹
نیروهای پلیس پس از دریافت تهدید بمب‌گذاری، محل را محاصره و مذاکرات با گروگان‌گیر را آغاز کردند.
🔹
به گفته پلیس، تاکنون یکی از گروگان‌ها آزاد شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/655686" target="_blank">📅 09:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بیانیه کویت درباره حملات هوایی
🔹
وزارت دفاع کویت بامداد چهارشنبه: ما تحت حمله موشک‌ها و پهپادها هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655685" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
طلا روی ترمز افزایش قیمت زد
🔹
قیمت طلا در معاملات روز چهارشنبه بازار جهانی در پی افزایش قیمت نفت که نگرانی‌ها درباره تورم را تشدید کرد، کاهش یافت.
🔹
قیمت هر اونس طلا برای تحویل فوری، ۰.۳ درصد کاهش یافت و به ۴۴۷۱ دلار و ۳۸ سنت رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/655684" target="_blank">📅 09:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAxuM4TnJzLbLm6MIqVrwlmZNk_-qRevSnxysPjgKWlxU569biQGsNtCkgUaXkBuIoUc71-pi_Xnvpg_iqzCAwwxt8qcJRKj9xVSo-ZO6VQ8zg_4pSzDN5xHRcPaqCNdB4kUJGmEJztgh9_DBY0KEDm5a00OVThbtjqAn6PffjtH0tC5n0cbXyQroLI3c6zhdmxtQYzgyDpAIg4I_lMoE6ANJs_g0mDdLFFwer48oaF8OjmVMCKnY_pJPJ6COAXsIBIYdY9wPGhwX3m-nvV4D7HHLlRtYNKNZhXgauhxYylF0wcudkHoevkFrruEFSxw5esIygvDzH2pl6bBwa6g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghZIQjQign8HCxdqI9H_rg7xsL5-GMAEWcIAf1WcQSLEZIeQSMbY8UgWaxu_bSL1eFbfE2gJF2VXotrTg_Dy6KAXDhmfvJBNNxSF8lBaRgJBq7YP8eTVH4D_VYINFKyi_wB9-Wr1JnjU7pJu8R1Bqe6MNyyroOaV6mP551AKotNiaWY6vMGwlwzhEWA_w3go-TNfLJx8Bou1R2XnD6mG5Ui161zpL5ITtHUIB1TcOQSdNl6Nth4MDsQKQuQMKjZZ2n5S3ER6rJ7UUO3zmNE_egfQBRJGN5syeZkHRWyG7s_GJRCPdLI6uTOTnPLGZ30PfKZlrd5RLp5xfL3iXTnPVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5177ee38.mp4?token=IxsrNWPPS9kQTNn7pC8o2aXaw5ztmXxAponb9dw2Hj_l8-k63Tb8kisM1QtYF-fjw8IXGqWqYNk-xtZffxZ2yP772FQaEQFA0fPAwhXrSlC8RgbDCNmW0oEnVIb5AldB4ycgqwjf-TFd_dItc39GrMQKw1WK2phFYEWwsdBmgx5W4ZfIqsvtSuvlf_9diZf6alxMS9WXc4XLkpNzYigJ1nVXvBQsn2YHIiUBvsFgbEeVxk_K1NGQztqRUKYkdIrszJhonR_B80rxvq0iBUIJI9DCt2dWrADonEG4gTTYSxZ9DKFqTAJJYkXp6BDd5wRnF1bHCwrpTCMBz9koDordmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5177ee38.mp4?token=IxsrNWPPS9kQTNn7pC8o2aXaw5ztmXxAponb9dw2Hj_l8-k63Tb8kisM1QtYF-fjw8IXGqWqYNk-xtZffxZ2yP772FQaEQFA0fPAwhXrSlC8RgbDCNmW0oEnVIb5AldB4ycgqwjf-TFd_dItc39GrMQKw1WK2phFYEWwsdBmgx5W4ZfIqsvtSuvlf_9diZf6alxMS9WXc4XLkpNzYigJ1nVXvBQsn2YHIiUBvsFgbEeVxk_K1NGQztqRUKYkdIrszJhonR_B80rxvq0iBUIJI9DCt2dWrADonEG4gTTYSxZ9DKFqTAJJYkXp6BDd5wRnF1bHCwrpTCMBz9koDordmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه خودرویی کاروان تیم ملی ترکیه به جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655680" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=AVX6pj_aF-WejQw45HdkjgSREKPwDfgQxvF3FX1uz4C9YSUfSg1pV0nJA2ffwFJ6H5wAQin27yw9QRxlL4VTQc3z6sCfrJ1QpD9w3Jz7UDVCtX0EshkPkgL5O38sS-FzXFmV6a8I2FqXdfGamujGd5Fy0fA4i3BpaF_Ba3hxvYIylVvjSW4XHsY3TJU23PNyu5KYmDrLngIewPlcCrrp4hJJO3pMPn-ImbffuafcGCpvP8WegI6WxW33qwmd03wc3B3Bl5xckdwgsMuI_QjtYAsJcWlVsEn2jk2Aikw80DHl1SXJyR152Nnvrynty6qhlzuvY8b3lY0KMAjDWrZ2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=AVX6pj_aF-WejQw45HdkjgSREKPwDfgQxvF3FX1uz4C9YSUfSg1pV0nJA2ffwFJ6H5wAQin27yw9QRxlL4VTQc3z6sCfrJ1QpD9w3Jz7UDVCtX0EshkPkgL5O38sS-FzXFmV6a8I2FqXdfGamujGd5Fy0fA4i3BpaF_Ba3hxvYIylVvjSW4XHsY3TJU23PNyu5KYmDrLngIewPlcCrrp4hJJO3pMPn-ImbffuafcGCpvP8WegI6WxW33qwmd03wc3B3Bl5xckdwgsMuI_QjtYAsJcWlVsEn2jk2Aikw80DHl1SXJyR152Nnvrynty6qhlzuvY8b3lY0KMAjDWrZ2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه این‌مدارس در ایران است؟!
ویدئوی بالا به هیچ وجه از دست ندید.
دبیرستان دخترانه هوشمند مدبّران برنده جایزه بهترین سیستم آموزشی خاورمیانه
"مدارسی از جنس رشد و شکوفایی"
🟢
این مدارس توسط
دکتر علی میرصادقی (روانشناس) طراحی وبنیانگذاری شده است.
✅
همین الان جهت ثبت نام در آزمون ورودی و کسب اطلاعات بیشتر به آیدی زیر  در تلگرام پیام بدهید:
@Modaberane_Barsa
یا عدد 4 را به 3000909030 ارسال کنید .
توجه:این دبیرستان ها تنها در تهران دایر است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655679" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae9_CgCmvG908dpHjwMlFbvb3ZpzwfnUHtQL9JA4nLA7Lthu42E41sk6h-nK7X5iqpLjsxuUI_6yyqsbpK-AOi0OjFQbda3iqS2GymslaspP4aVxkHp2pw8optqUZX-ed1RIwqOQmiP_sYBjtQaJoUvrfXBU85fjuMh2_4LeCSWQv2suhDhFkpWFpVR0NJ-lQy6-CSUOAV4QTgNOT9uMXaDWL34zmtV8QdsetKCCmrX0FoM0HD1XRT3NAwctBSPQ6hNKboB1CTF5JlC0SFDuuWe3VIDzuit8p9k1oKRhWJt-ULXl76QGBTgrri1Aldwp6UxKV-P829XqsOZJzElUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حراج پیراهن پله در اولین بازی جام جهانی ۱۹۵۸ به قیمت ۶ میلیون دلار!
🔹
پله در این بازی دو بار دروازه سوئد را باز کرد و جوان‌ترین گلزن تاریخ جام‌های جهانی شد. این رکورد هنوز شکسته نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655678" target="_blank">📅 09:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هواشناسی: کسانی که می‌خواهند به شمال بروند، فردا و پس‌فردا منتظر بارش باشند.
🔹
سپاه اصفهان از احتمال شنیده شدن صدای انفجار کنترل شده در محدوده جنوب اصفهان خبر داد.
🔹
سازمان ملل: وضعیت تنگه هرمز معیشت حدود یک میلیارد نفر را تحت تاثیر قرار خواهد داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/655677" target="_blank">📅 08:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1vNWTs1PK34gWOGqnkFPV4Eo2tYVrR2OcBx44noi3ac1o1cFhdJm_HoMAHlPC3RZuw-UZoPBYVatCFZT6lDmqrPuOnON6arca_Fg9iwzC4VlZiBwUOHMp2K_YHMjLs31ROchD-nDNQYuWIMHFLqixbTfbgEVRrTEZxCL_H_okocOeLiug9effzXjURteXwB4zjzLJntPzeDFvqDoGmov9hsN25qeFXS7PC_jneijwFeMo8QvLYxFl8whqWw3lLzxXG5Wa77iTXnCGuVKkfqfqx4iyq_AjCMRUeFht1nSYLLcmoTO79N4uBZVh04n9BBAVCFBNZ1EQejUAvE3QuBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/655676" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549228439c.mp4?token=ipvfcRDu9JGwC0QRuKNYXgL3vKpILCgNFXp2f-XaV-TGOiFS-hFzUEhnA-I8759UppVcWyIFIxmNbOxre1Ql_2anzkkXvRfxvxWFrBpiKEmX2VlXLbRxR2Tl0uIFxYKy3YOcmAR4BTOHGtvwEwAPKWgBb-AT8jc-Vo_Qfj8bS7NrP0GMBcKuCZPr-f_H6zszEYqg0Rz4wQELC08O40B2jGhb3c5Xrt4A-YbdSLXy9N9Wc_iv8dAdHz5CfK5kalDx6jbvZyhgT4zwbP2mRMrWBZdayRZqPDAsqAwuYYJo58hVlcDj_DnYcElphqJN8mrIoAo9z2hishvttCGtHHf6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549228439c.mp4?token=ipvfcRDu9JGwC0QRuKNYXgL3vKpILCgNFXp2f-XaV-TGOiFS-hFzUEhnA-I8759UppVcWyIFIxmNbOxre1Ql_2anzkkXvRfxvxWFrBpiKEmX2VlXLbRxR2Tl0uIFxYKy3YOcmAR4BTOHGtvwEwAPKWgBb-AT8jc-Vo_Qfj8bS7NrP0GMBcKuCZPr-f_H6zszEYqg0Rz4wQELC08O40B2jGhb3c5Xrt4A-YbdSLXy9N9Wc_iv8dAdHz5CfK5kalDx6jbvZyhgT4zwbP2mRMrWBZdayRZqPDAsqAwuYYJo58hVlcDj_DnYcElphqJN8mrIoAo9z2hishvttCGtHHf6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده در شهرک تبنین در جنوب لبنان بر اثر حملات اشغالگران
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655675" target="_blank">📅 08:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d8d8d73b.mp4?token=pe-72xqAESYQhieW4ghD78cOpZO17ZJs_4uYusOWUqBmgpNd02SHkLmbwN1ZBhaGjsP4-RpAKE2TLAFmV9FaZawGqo5v7g4JQewM1G_5F267uO_EkQJpQuw7NIjyTULNVJHmS39yVz0VurPVfHqdnv_q1OraPrJ6SeMYxPVMjNcFYO4eISTO0Muoel49E9LcM2y8Oi89DGMSWiqYA5vgrfc61rX9CAc3oOISEf5bx5CSl6ZfCG2APnRpUNAUI4OhtP3Udro_lJS82kpfbSFwkTUPGQNmHjXIRmQQ1f20EHR9rNZO7k2M0ohbCfU6aE8zZa0HtHzZH63bs5ODYeNfPkcsH2Q08ckyDr0WZaBtd32P3LxStwPstr4L3R3wDawaPhEagGT7Tj0q5X5bSSog9FjZT3N9kY70un7ffz1N67LZchfImPPFshXLTWbLcZ2GjudKxdCuXOC9ZGZ-409rpXUKbhI3hPGjCMz8pjCqLd3mSh4yHKbKE8j7I8PaK05z2jAZrF4ka8_-hRwD4XyVwAfekVa78WTzyMrDZXLppTRQ15yTx9s6oZDpgHpRcHfQ80DieKpCfCWdxC-4DgJ5KH1MYK7NwCZWN8OT-7x9BbV0oDLkaqeAYXFfg3b2-tzGDyQPkkd2bKUMz06qkF7mA-3HjH0EGBrQ3LI1_UJY_KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d8d8d73b.mp4?token=pe-72xqAESYQhieW4ghD78cOpZO17ZJs_4uYusOWUqBmgpNd02SHkLmbwN1ZBhaGjsP4-RpAKE2TLAFmV9FaZawGqo5v7g4JQewM1G_5F267uO_EkQJpQuw7NIjyTULNVJHmS39yVz0VurPVfHqdnv_q1OraPrJ6SeMYxPVMjNcFYO4eISTO0Muoel49E9LcM2y8Oi89DGMSWiqYA5vgrfc61rX9CAc3oOISEf5bx5CSl6ZfCG2APnRpUNAUI4OhtP3Udro_lJS82kpfbSFwkTUPGQNmHjXIRmQQ1f20EHR9rNZO7k2M0ohbCfU6aE8zZa0HtHzZH63bs5ODYeNfPkcsH2Q08ckyDr0WZaBtd32P3LxStwPstr4L3R3wDawaPhEagGT7Tj0q5X5bSSog9FjZT3N9kY70un7ffz1N67LZchfImPPFshXLTWbLcZ2GjudKxdCuXOC9ZGZ-409rpXUKbhI3hPGjCMz8pjCqLd3mSh4yHKbKE8j7I8PaK05z2jAZrF4ka8_-hRwD4XyVwAfekVa78WTzyMrDZXLppTRQ15yTx9s6oZDpgHpRcHfQ80DieKpCfCWdxC-4DgJ5KH1MYK7NwCZWN8OT-7x9BbV0oDLkaqeAYXFfg3b2-tzGDyQPkkd2bKUMz06qkF7mA-3HjH0EGBrQ3LI1_UJY_KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب کتیبه عید سعید غدیر در حرم مطهر امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/655674" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUc-sGCL5N7BAZeBSQEpvz1ON3oO8ZW-tB6i5ToTblCke06iIOuf5Q8qTKwYIp_9ZKdDuC6WRFaUbBpZddDaapipkQ0GSp6SX_nVA-QEddl0g6Pl55ZxhtAAoHon4n7SmF8kUy_PfXzaYtDToVIY-t1r_q9ouTnP3bxxy8uUike8Ve0ZM2rRFVQekXDHi3MtqbqQ6yFqNEIL2ty_CJ7WSArNKOGKDSChRsjfqjRPEtvcrzc8TEH8r-d6JjiMKeW1_0sGM1TdE9ee6DzKsV5_-6Zcfc_WQ606sbt480OQFVxoPNzB_jSPzdd9vnmbKXQwiRBmn3l_O3fmGCgJJ-e25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سنی تیم‌های شرکت‌کننده در جام جهانی ۲۰۲۶/ ایران دومین تیم پیر جام
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655673" target="_blank">📅 08:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
پروازها در بحرین، کویت و امارات تا اطلاع‌ثانوی لغو شد
🔹
رسانه‌های عربی گزارش دادند که پروازها در فرودگاه بین‌المللی بحرین، فرودگاه بین‌المللی کویت و فرودگاه‌های دبی و ابوظبی تا «اطلاع‌ثانوی» به‌حالت تعلیق درآمده است./فارس
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655672" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcef435e9.mp4?token=cr3P2nZr4xR_sR75SktGdxo4yUh8m76Bpo1OuNY80As6E1v551Vr9NZfkGjhTlb-mobn7t0Q7KzZ7tNGRSYNKKRf4WRaGrl6QMD1Ng80VCyIIbXYncm3ZcIUm-nhNJfJ1TKU_dURQ8q7gxAbLHcPGvnnzWAhtUH7yoZrMYzekDpmEcUClY2xtY9E5BadpLn_o1dlGgKkiOaKKxEEuKEzms2JZdfZTFeh8zPdOXiCZYH_Tv1Bl5gcglM-oqyecIcg3jvJG48VySNH0m1ldAGCYX4jsI3UghSVSfpJfw8sN6tlC0P3Co2ByoZVyMP6d7gn5-LESlv591Xd6EIL2BSwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcef435e9.mp4?token=cr3P2nZr4xR_sR75SktGdxo4yUh8m76Bpo1OuNY80As6E1v551Vr9NZfkGjhTlb-mobn7t0Q7KzZ7tNGRSYNKKRf4WRaGrl6QMD1Ng80VCyIIbXYncm3ZcIUm-nhNJfJ1TKU_dURQ8q7gxAbLHcPGvnnzWAhtUH7yoZrMYzekDpmEcUClY2xtY9E5BadpLn_o1dlGgKkiOaKKxEEuKEzms2JZdfZTFeh8zPdOXiCZYH_Tv1Bl5gcglM-oqyecIcg3jvJG48VySNH0m1ldAGCYX4jsI3UghSVSfpJfw8sN6tlC0P3Co2ByoZVyMP6d7gn5-LESlv591Xd6EIL2BSwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید باور نکردنی شنای تایسون  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/655671" target="_blank">📅 08:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a9afa507.mp4?token=V4p9zBA2T9iK5XaspUJee3kbW80P3L1yX-rBLNIknWJCeRBl9wn1EVoNamA6DssNUU7yZicOg9hAa0G41HIhWubU8ZNw14YIPx3sF93_jDvTDQmv7AWNdukxVgTEABod7rqZURZNJTH8HXI0k79hIv_7f7lWsIoFichKwTKqIYS46jYuY63wBPC51pRLUkocpnsftOcgHJ6zha2z7OmAWUwq76xjVALlFzP-7JhYicZ_qVIZ-uJLJkrnxiP8nVuw4tOis4cHHxYYLjEUR2_dt31p3XMdeezDTa87kv5zNA3QBAWalH1VQrQ-JGxZoIwPKBlyd1puh_yFLIKmLA7efg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a9afa507.mp4?token=V4p9zBA2T9iK5XaspUJee3kbW80P3L1yX-rBLNIknWJCeRBl9wn1EVoNamA6DssNUU7yZicOg9hAa0G41HIhWubU8ZNw14YIPx3sF93_jDvTDQmv7AWNdukxVgTEABod7rqZURZNJTH8HXI0k79hIv_7f7lWsIoFichKwTKqIYS46jYuY63wBPC51pRLUkocpnsftOcgHJ6zha2z7OmAWUwq76xjVALlFzP-7JhYicZ_qVIZ-uJLJkrnxiP8nVuw4tOis4cHHxYYLjEUR2_dt31p3XMdeezDTa87kv5zNA3QBAWalH1VQrQ-JGxZoIwPKBlyd1puh_yFLIKmLA7efg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خودرو در پمپ گاز اتوبان یاسینی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655670" target="_blank">📅 07:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
توقف کامل پروازها در بحرین، کویت و امارات
🔹
رسانه‌های عربی گزارش دادند که فعالیت فرودگاه‌ها و تمام پروازها در بحرین، کویت و امارات عربی متحده به دلیل حملات هوایی متوقف شده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/655669" target="_blank">📅 07:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پوران دخت</div>
  <div class="tg-doc-extra">پادکست کافئین | قسمت بیست هشتم</div>
</div>
<a href="https://t.me/akhbarefori/655668" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
پوران‌دخت ساسانی
🗓
وقتی هدایتِ یک سیستم پر از بدهی و اشتباهاتِ گذشتگان به ما سپرده می‌شود، آیا فرار می‌کنیم یا برای «مرمت در دلِ ویرانی» می‌ایستیم؟ درسِ بزرگِ نخستین پادشاهِ زنِ تاریخ ساسانی برای مدیریتِ بحران‌های امروز.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/655668" target="_blank">📅 07:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285776b7c.mp4?token=OHgtFRv1BcfO6CtSTtsBgoblG6mLkcNBDr1Cu9rWk-IN_AQE6j3BoM8dqdhO5DtWCSNeDRJA4flccjXM5mPusaQLNbk6drGQkcTm7OWhnc4CwBzAHIGznYMG1aEvvICHv3OK9_o03V2enN78XXcX1mKvmS64tAZDdIl4Z5sG4qOIFAAwiek-PC2CLgSrb27906mRoWLZ54Weqelk4uwBrN67Sg9PjhH8piaAjNk3uXAx51u5JVlvCzcsRgxHAmElAf9FYHewPTH1zXIXA_eFgNc5jbAr42SiWxAumTLlehkOTXvLjCtDwdXrIB2EuNtJog4tPhR6xshbiKLcyIwfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285776b7c.mp4?token=OHgtFRv1BcfO6CtSTtsBgoblG6mLkcNBDr1Cu9rWk-IN_AQE6j3BoM8dqdhO5DtWCSNeDRJA4flccjXM5mPusaQLNbk6drGQkcTm7OWhnc4CwBzAHIGznYMG1aEvvICHv3OK9_o03V2enN78XXcX1mKvmS64tAZDdIl4Z5sG4qOIFAAwiek-PC2CLgSrb27906mRoWLZ54Weqelk4uwBrN67Sg9PjhH8piaAjNk3uXAx51u5JVlvCzcsRgxHAmElAf9FYHewPTH1zXIXA_eFgNc5jbAr42SiWxAumTLlehkOTXvLjCtDwdXrIB2EuNtJog4tPhR6xshbiKLcyIwfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوران‌دخت ؛ نخستین پادشاه زن تاریخ ایران
#پادکست_کافئین
| قسمت بیست‌و‌هشتم
☕️
در این اپیزود به سراغ تاریک‌ترین برهه‌ی تاریخ ساسانی رفتیم؛ روزگاری که بوی خون و طاعون پایتخت را گرفته بود و سرداران در حالِ غارتِ کشور بودند. در این اوجِ ناامیدی، زنی تاجِ پادشاهی را بر سر گذاشت که با دستِ خالی، ماشینِ جنگیِ امپراتوری روم را متوقف کرد و به دادِ اقتصادِ ویران رسید.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/vauuzfo
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/655667" target="_blank">📅 07:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMb5HcSMdEBiuiOe43VGpbB8m3-0D_TeWPr2HITb7qWXB24dczIuKSZNB6lxxxYhO2-7hTKZajye3mP4Sp0VgRiyPmtKCdgWx31It9_e1hlsgr7exJDRLxvMNnyxUUmvzDl-HCUmqKOE7TOdGNoxmbN50Fu7Q-2EswBXMgeswAZM-5_7j1niVr7v29vH4zGWSEeIrdDm8gTGrPtPpdL1RKpbuO52GEde1GBM1i04JSEYvc2D7pKH7kwxgs0B3O-Y_vrN95RANYTnJbhVoYbFBo-wGr0D0jrKy8OJxXOfj14aj39OxYPI2tvVO6T0PrLCZzCY8fjjXsykl-ydfAvCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی هر بشکه نفت برنت از ۹۷ دلار فراتر رفت
🔹
درپی پاسخ قاطع نیروهای‌مسلح ایران به اقدام نظامی آمریکا در منطقۀ خلیج فارس، قیمت نفت برنت با رشد ۱.۰۷ درصدی به ۹۷.۱۱ دلار در هر بشکه رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655666" target="_blank">📅 07:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce24ae559.mp4?token=DzJudBRRYKew0-3mX436zpKVTxYbrjG-YdF3TDFXAyb8nEuDDJ3kRlWiFQD1og2J-7wsgN1Lfb3Fy8Go4yTdpR4VtQxPv_ooBltJR46ZT2ej4cbSCBuC8XqUZAUCXDkzOR6KYpVfXhd8gCaI6C81GN0NSPLibg74B5JDRDZsLjQDqZHLn3EdFrYYkuqBNY1DD_TeoPxy3bBpQCVh1VAo8CBYkeNarOPCsA3A2xG69nSACrU0JhlU7xfchmQCQe61SCAY8edcZJqS9V9kV1noWCPc5Dx22bdtFiWw5ABHqyHXuZs_XQmdyD8ZHHbqpwV73bDg6tWZTQQ1v7GJaIolWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce24ae559.mp4?token=DzJudBRRYKew0-3mX436zpKVTxYbrjG-YdF3TDFXAyb8nEuDDJ3kRlWiFQD1og2J-7wsgN1Lfb3Fy8Go4yTdpR4VtQxPv_ooBltJR46ZT2ej4cbSCBuC8XqUZAUCXDkzOR6KYpVfXhd8gCaI6C81GN0NSPLibg74B5JDRDZsLjQDqZHLn3EdFrYYkuqBNY1DD_TeoPxy3bBpQCVh1VAo8CBYkeNarOPCsA3A2xG69nSACrU0JhlU7xfchmQCQe61SCAY8edcZJqS9V9kV1noWCPc5Dx22bdtFiWw5ABHqyHXuZs_XQmdyD8ZHHbqpwV73bDg6tWZTQQ1v7GJaIolWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر منتسب به لحظه اصابت موشک بالستیک ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655665" target="_blank">📅 07:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a2af85ea.mp4?token=amcVjDsEe3dPEZkrgsquRcAjJvN6CX7bzlKZTiknTCPHET3OpR0D_mdoxYgsEuW7c3n6wC2wOp8-cyDVElrNGGZU-xsKgYh3T3Po0wQlaHGVTCvG6mFmRuz0b0ASiToCOrvyO2dkqbPs7YB9InkRnYwY70-Na75cS-zIzbRc8rRhkGmEOGp5BKjioWh3oBoY4iIejdCz86JaTOXXPrVckGy8yMTddPn6M6159RAw0fUDTtyds2vrMBI6PsFQOxGnUcDHfwgAyo-Boyjg-aJnYUBTHzUrJpRYNA9y9IoayZ3rKuf7QgdbiPDCFlYaYKa94pYQBVNfxbfLDT5cUEkKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a2af85ea.mp4?token=amcVjDsEe3dPEZkrgsquRcAjJvN6CX7bzlKZTiknTCPHET3OpR0D_mdoxYgsEuW7c3n6wC2wOp8-cyDVElrNGGZU-xsKgYh3T3Po0wQlaHGVTCvG6mFmRuz0b0ASiToCOrvyO2dkqbPs7YB9InkRnYwY70-Na75cS-zIzbRc8rRhkGmEOGp5BKjioWh3oBoY4iIejdCz86JaTOXXPrVckGy8yMTddPn6M6159RAw0fUDTtyds2vrMBI6PsFQOxGnUcDHfwgAyo-Boyjg-aJnYUBTHzUrJpRYNA9y9IoayZ3rKuf7QgdbiPDCFlYaYKa94pYQBVNfxbfLDT5cUEkKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی/ گزارش‌ها از حمله به پایگاه «علی السالم»
🔹
برخی منابع عربی می‌گویند که انفجارهایی در شهر «السره» در جنوب کویت و همچنین پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/655664" target="_blank">📅 07:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kofguKDhazFzZYmGoWG9nXky42ZYuwSTZDYz8PeMYwU_ta6xXrivQ9OeOCt8v-yxbsTEZ2XYxBNPAxKN_CSEAVcleMVyQoWbIVIc5g81e9dH4bWLg8-j5jcrIJN2jhB2675fEuNbIYnMRPoaTSdC9Tz2X_-wEkh3gKB7oh3Awm2f98Fuh5ZUY9RqXruIM-Eu2IHGcbKtWDbXOicHZGAbIJYPtLudsfv7wh-Iijgju3U82cNPLg8oA366RPC1u_eAqrXUte5IwvOMNTOrpiytgEirY9UQLXiaB6n7Fc_Rjg9zLO8UE4Juqxop_GkflQq525jDhxke-J5njiFDXztImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۳ خرداد ماه
۱۷ ذی‌الحجه ۱۴۴۷
۳ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655663" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoFMy8UkxsXFM_HpKGV4IIJ_Fwhv2gswAnhqv4R-np6wNuYpbgB2jXbsALfGjyByy2k0NmMHHX09UOrPC_rF8vl7j_dmPB5naamw6A2FuUc-2vvQAgOXVYW2_guiG4Edljz5OBbM-PM7Xu69iCgT9sk52A8fA8BGvoER-qtoMLcm0Xwvb3uc0BEch52n9KKMNEzXUYVliLaN7GbR9stZLebqRmMtbH8xJJweAvVIAu72v1BCBpPYkeRuxr9oicOAbzQatgf7ZExGLOB6QsWtkbuD21lllCj96gvK8NLiLTmdoQvgI_ftzMkIhclR1tnGzQs4gudSPwq1uP-FpNXZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانیا، فرشته‌ی ۶ ساله‌ی همدانی، مبتلا به سرطان خون، برای تهیه‌ی دارو، نیاز به کمک مالی دارد
💔
🥺
پدرش، کارگر و ساکن خانهٔ اجاره‌ای، توان تأمین مخارج سنگین درمان را ندارد.
😭
❤️‍🩹
هر کمکِ شما، قدمی بزرگ برای کاهش رنج‌های این خانواده و بازگرداندنِ زندگی به این کودک معصوم است. نذرِ سلامتیِ عزیزانتان، مانیا را دوباره راهیِ زندگی کنید.
🙏
😭
🌹
💳
شماره کارت/شبا خیریه: برای کپی کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
| برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/655662" target="_blank">📅 03:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_oVdnmc9hIQSjJHjAf8B9vBa5dDbixdU4-npRv1EMLNXqjwsUfmr950j0m9Dr9gwyE_IyAPLxsPZV_M44EyU5zQd5iQL2QRIuf75xWOIE8JrXLr0KqNmdiWMAe0J629wknDnkmW-RqteIRCdQiotM91ZR2WKtqDz9p2MqY_-Dj89R1NpKb7SBmF6UcQaQTephBcVNNrRV1R5fbcycen-OyAQ-otVYLJ1LxY_wbvrlA8r7G10nL_roh0lpuwuGHVtqJRjkJvWj2P9v_h_hDjlldKDxrENJ0wsJs45adB6n1O95NFsvfsAoGlUXjTz24ifUjRlCHrUJF4GXmBtZEgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
ایمپلنت کره‌ای با روکش
💰
فقط ۲۴,۶۰۰,۰۰۰ تومان
🎯
ویژه ۱۰۰ نفر اول
✅
ثبت‌نام و استفاده از این شرایط ویژه فقط با:
عضویت در کانال تلگرام
و ارسال *نام و شماره تماس* به آیدی زیر
👇
📩
ادمین:
@robindentalclinic
📌
کانال:
https://t.me/RobinClinic</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655661" target="_blank">📅 03:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا، از جمله الظفره، الصفران و المنهاد و بخش نظامی فرودگاه بین‌المللی دبی در امارات متحده عربی هدف حملات هماهنگ و گسترده قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/655660" target="_blank">📅 03:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
صدای انفجار مهیبی در شهر قامشلی سوریه شنیده شد
🔹
هنوز مبدا و عامل این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/655659" target="_blank">📅 03:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند  روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله القاصم الجبارین فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
در اواخر شب گذشته…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/655657" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/655656" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
منابع عربی از پرواز هواپیماهای جنگی در آسمان استان کرکوک در شمال عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/655655" target="_blank">📅 03:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سنتکام: ایران پایگاه‌های آمریکا را هدف قرار داد
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که نظامیان این کشور در کشورهای حاشیه خلیج فارس، هدف موشک‌ها و پهپادهای ایرانی قرار گرفتند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/655654" target="_blank">📅 03:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سنتکام: ایران پایگاه‌های آمریکا را هدف قرار داد
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که نظامیان این کشور در کشورهای حاشیه خلیج فارس، هدف موشک‌ها و پهپادهای ایرانی قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/655653" target="_blank">📅 03:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
🔹
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
🔹
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
🔹
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
🔹
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/655650" target="_blank">📅 03:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
به‌ ادعای برخی رسانه‌های عراقی، شناورهای نظامی در آب‌های نزدیک سواحل امارات هدف اصابت موشک و پهپاد قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/655649" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
